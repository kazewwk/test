#!/usr/bin/env python3
"""Supervise an authorized Colab L4 batch, checkpoint results, recover lost runtimes, release on completion.

Does not buy or recharge compute units. Requires an already reviewed/published pilot.
"""
from pathlib import Path
import argparse,subprocess,os,time,json,tarfile,shlex,signal,uuid,re


def command(args,timeout=90,input=None):
 p=subprocess.Popen(list(map(str,args)),stdin=subprocess.PIPE if input is not None else subprocess.DEVNULL,
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=not isinstance(input,bytes),start_new_session=True)
 try:out,err=p.communicate(input,timeout=timeout)
 except subprocess.TimeoutExpired:
  os.killpg(p.pid,signal.SIGTERM);p.communicate(timeout=10);raise
 if p.returncode:raise RuntimeError(f'{Path(str(args[0])).name} exited {p.returncode}: '+re.sub(r'https?://\S+','[URL redacted]',str(err))[-500:])
 return out


def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ['colab-state','ssh-key','rclone-config','github-token-file','inventory','pilot-review','workspace']:
  p.add_argument('--'+name,required=True)
 p.add_argument('--session',required=True)
 p.add_argument('--use-existing-balance',action='store_true',required=True)
 a=p.parse_args();work=Path(a.workspace).resolve();work.mkdir(parents=True,exist_ok=True,mode=0o700)
 pipeline=Path(__file__).resolve().parents[1];session=a.session
 cli=['colab','--config',str(Path(a.colab_state).resolve())]
 def api(*args):return command(cli+list(args),60)
 def save(state,**data):
  (work/'controller_status.json').write_text(json.dumps({'time':time.time(),'session':session,'state':state,**data},ensure_ascii=False,indent=2))
 def ssh(code,timeout=60,input=None):
  sessions=json.loads(Path(a.colab_state).read_text())
  if session not in sessions or sessions[session].get('accelerator')!='L4':raise RuntimeError('Expected existing L4 runtime')
  control=work/('ssh-'+session)
  # Socket must fit the UNIX socket path limit even for a deeply nested workspace.
  short=Path('/tmp')/('nce-ssh-'+str(os.getuid())+'-'+uuid.uuid5(uuid.NAMESPACE_URL,str(control)).hex[:20])
  proxy=shlex.join(cli+['ssh','--proxy-mode','-s',session,'-i',str(Path(a.ssh_key).resolve())])
  args=['ssh','-T','-o','BatchMode=yes','-o','ConnectTimeout=30','-o','StrictHostKeyChecking=accept-new',
        '-o','UserKnownHostsFile='+str(work/'known_hosts'),'-o','ControlMaster=auto','-o','ControlPersist=600',
        '-o','ControlPath='+str(short),'-o','ProxyCommand='+proxy,'-i',str(Path(a.ssh_key).resolve()),'root@'+session,code]
  return command(args,timeout,input)
 def upload(local,dest):return ssh('umask 077; cat > '+shlex.quote(dest),60,Path(local).read_bytes())
 def deploy():
  ssh('mkdir -p /content/nce')
  archive=work/'pipeline.tar.gz'
  with tarfile.open(archive,'w:gz') as t:
   for f in pipeline.rglob('*'):
    if f.is_file() and not any(x in f.parts for x in ('__pycache__','.pytest_cache','.git')) and '.egg-info' not in str(f):
     t.add(f,arcname='pipeline/'+str(f.relative_to(pipeline)))
  for src,dest in [(archive,'pipeline.tar.gz'),(a.inventory,'inventory.json'),(a.pilot_review,'pilot_review_input.json'),
                   (a.rclone_config,'drive-runtime.conf'),(a.github_token_file,'github-publisher-token')]:
   upload(src,'/content/nce/'+dest)
  ssh('cd /content/nce && tar -xzf pipeline.tar.gz && chmod 600 drive-runtime.conf github-publisher-token')
  remote='''from pathlib import Path
import subprocess,os,json,time,shutil
b=Path('/content/nce')
def run(args,**kw):return subprocess.run(list(map(str,args)),check=True,**kw)
if not (b/'environments.ready').exists():
 run(['bash',b/'pipeline/scripts/install.sh','cuda',b/'venv'])
 (b/'environments.ready').touch()
env=os.environ.copy();env['GH_TOKEN']=(b/'github-publisher-token').read_text().strip()
run(['gh','auth','setup-git','--hostname','github.com'],env=env)
checkout=b/'github-checkout'
if not (checkout/'.git').exists():
 run(['git','clone','--filter=blob:none','--depth','1','--no-checkout','--branch','main','https://github.com/kazewwk/test.git',checkout],env=env)
 run(['git','-C',checkout,'sparse-checkout','set','--no-cone','/courses/_pipeline/','/courses/inventory.json','/courses/*.md','/courses/*/*.md','/courses/*/quality_summary.json','/courses/*/*/manifest.json','/courses/*/*/qc_report.json'])
 run(['git','-C',checkout,'checkout','main'])
else:run(['git','-C',checkout,'pull','-q','--ff-only'])
review=json.loads((b/'pilot_review_input.json').read_text())
relative=Path(review['lesson_relative_path'])
run(['git','-C',checkout,'sparse-checkout','add','--no-cone','/courses/'+str(relative)+'/'])
pilot=b/'courses'/relative;pilot.parent.mkdir(parents=True,exist_ok=True)
shutil.copytree(checkout/'courses'/relative,pilot,dirs_exist_ok=True)
review['lesson_directory']=str(pilot);(b/'pilot_review.json').write_text(json.dumps(review))
run([b/'venv/bin/python',b/'pipeline/scripts/restore_progress.py','--inventory',b/'inventory.json','--checkout',checkout,'--output',b/'courses','--cache',b/'cache'])
checkpoint=b/'checkpoint_repo'
if not (checkpoint/'.git').exists():
 run(['git','clone','--filter=blob:none','--depth','1','--single-branch','--branch','nce-processing-checkpoints','--sparse','https://github.com/kazewwk/test.git',checkpoint],env=env)
 run(['git','-C',checkpoint,'sparse-checkout','set','_checkpoint'])
else:run(['git','-C',checkpoint,'pull','-q','--ff-only'],env=env)
run([b/'venv/bin/python',b/'pipeline/scripts/restore_progress.py','--inventory',b/'inventory.json','--checkout',checkout,'--output',b/'courses','--cache',b/'cache','--checkpoint-checkout',checkpoint])
with (b/'checkpoint_batch.log').open('a') as log:
 backup=subprocess.Popen(['python3',str(b/'pipeline/scripts/checkpoint.py'),'--source',str(b/'courses'),'--checkout',str(b/'checkpoint_publish'),'--token-file',str(b/'github-publisher-token')],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
env.pop('GH_TOKEN',None);env['NCE_GITHUB_TOKEN_FILE']=str(b/'github-publisher-token')
args=[b/'venv/bin/python',b/'pipeline/scripts/batch.py','--inventory',b/'inventory.json','--pilot-review',b/'pilot_review.json','--cache',b/'cache','--output',b/'courses','--checkout',checkout,'--rclone-config',b/'drive-runtime.conf','--ocr-python',b/'venv-ocr/bin/python','--visual-python',b/'venv-mineru/bin/python','--mineru-python',b/'venv-mineru/bin/python','--visual-backend','vllm','--device','cuda:0','--public-authorized']
result=subprocess.run(list(map(str,args)),env=env)
(b/'batch_exit.json').write_text(json.dumps({'exit_code':result.returncode,'time':time.time()}))
'''
  upload_text='from pathlib import Path\nimport subprocess\nb=Path("/content/nce")\n'
  upload_text+='(b/"batch_driver.py").write_text('+repr(remote)+')\n'
  upload_text+='with (b/"batch_driver.log").open("a") as log:\n p=subprocess.Popen(["python3",str(b/"batch_driver.py")],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)\n(b/"batch_driver.pid").write_text(str(p.pid))\nprint(p.pid)\n'
  ssh('python3 -',60,upload_text)
 consecutive_errors=0
 while True:
  try:
   usage=api('usage');m=re.search(r'Current balance:\s*([0-9.]+)',usage);balance=float(m[1]) if m else None
   if balance is not None and balance<=0.1:
    api('stop','-s',session);save('stopped_balance_requires_recharge_authorization',balance=balance);return
   api('sessions');sessions=json.loads(Path(a.colab_state).read_text())
   if session not in sessions:
    save('recovering_lost_runtime',balance=balance)
    session='nce-l4-resume-'+time.strftime('%Y%m%d%H%M%S',time.gmtime())
    api('new','-s',session,'--gpu','L4');deploy();save('recovered',balance=balance)
   status=json.loads(ssh("python3 -c \"from pathlib import Path; import json; b=Path('/content/nce'); p=b/'cache/batch_status.json'; e=b/'batch_exit.json'; print(json.dumps({'batch':json.loads(p.read_text()) if p.exists() else None,'exit':json.loads(e.read_text()) if e.exists() else None,'driver_exists':(b/'batch_driver.pid').exists(),'driver_alive':(b/'batch_driver.pid').exists() and Path('/proc/'+(b/'batch_driver.pid').read_text().strip()).exists()}))\"",45))
   if status['batch'] and status['batch'].get('state')=='complete':
    save('complete',balance=balance,result=status['batch']);api('stop','-s',session);return
   if status['driver_exists'] and not status['driver_alive'] and not status['exit']:
    save('bootstrap_error_requires_repair',balance=balance,result=status);api('stop','-s',session);return
   if status['exit']:
    save('batch_error_requires_repair',balance=balance,result=status);api('stop','-s',session);return
   if not status['driver_exists']:deploy()
   save('running',balance=balance,result=status);consecutive_errors=0
  except Exception as e:
   consecutive_errors+=1;save('retrying_control',error_type=type(e).__name__,detail=str(e)[:500])
   if consecutive_errors>=3:
    try:api('stop','-s',session)
    except Exception:pass
    save('control_error_requires_repair',detail=str(e)[:500]);return
  time.sleep(45)

if __name__=='__main__':main()
