#!/usr/bin/env python3
"""Resume an authorized Colab CPU/L4 batch and release its paid runtime on completion.

Uses only an existing balance. Never purchases or recharges compute units.
"""
from pathlib import Path
import argparse,subprocess,os,time,json,tarfile,shlex,signal,re,fcntl,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from course_pipeline.health import progress_signature,recovery_reason


def command(args,timeout=90,input=None):
 p=subprocess.Popen(list(map(str,args)),stdin=subprocess.PIPE if input is not None else subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=not isinstance(input,bytes),start_new_session=True)
 try:out,err=p.communicate(input,timeout=timeout)
 except subprocess.TimeoutExpired:
  os.killpg(p.pid,signal.SIGTERM);p.communicate(timeout=10);raise
 if p.returncode:raise RuntimeError(f'{Path(str(args[0])).name} exited {p.returncode}: '+re.sub(r'https?://\S+','[URL redacted]',str(err))[-400:])
 return out


def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ['colab-state','ssh-key','rclone-config','github-token-file','inventory','pilot-review','workspace','api-config','session']:
  p.add_argument('--'+name,required=True)
 p.add_argument('--accelerator',choices=['NONE','L4'],default='L4')
 p.add_argument('--use-existing-balance',action='store_true',required=True)
 p.add_argument('--stall-seconds',type=int,default=1800)
 p.add_argument('--max-recoveries-per-hour',type=int,default=3)
 p.add_argument('--probe-only',action='store_true')
 a=p.parse_args();work=Path(a.workspace).resolve();work.mkdir(parents=True,exist_ok=True,mode=0o700)
 pipeline=Path(__file__).resolve().parents[1];state_file=Path(a.colab_state).resolve();session=a.session
 cli=['colab','--config',str(state_file)];key=Path(a.ssh_key).resolve()
 if not a.probe_only:(state_file.parent/'controller.pid').write_text(str(os.getpid()))
 def api(*args):return command(cli+list(args),60)
 def save(state,**data):
  dest=work/'controller_status.json';tmp=dest.with_suffix('.tmp')
  tmp.write_text(json.dumps({'time':time.time(),'session':session,'state':state,**data},ensure_ascii=False,indent=2));tmp.replace(dest)
 def ssh(code,timeout=45,input=None):
  sessions=json.loads(state_file.read_text())
  if session not in sessions or sessions[session].get('accelerator')!=a.accelerator:raise RuntimeError('Expected explicitly allocated runtime with matching accelerator')
  control=Path.home()/'.cache/nce-colab'/session;control.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
  proxy=shlex.join(cli+['ssh','--proxy-mode','-s',session,'-i',str(key)])
  args=['ssh','-T','-o','BatchMode=yes','-o','ConnectTimeout=30','-o','StrictHostKeyChecking=accept-new','-o','UserKnownHostsFile='+str(key.parent/'colab_known_hosts'),'-o','ControlMaster=auto','-o','ControlPersist=600','-o','ControlPath='+str(control),'-o','ProxyCommand='+proxy,'-i',str(key),'root@'+session,code]
  # Shared with interactive control: Colab permits only one SSH bridge per VM.
  with control.with_suffix('.lock').open('w') as lock:
   fcntl.flock(lock,fcntl.LOCK_EX)
   return command(args,timeout,input)
 def upload(src,dest):return ssh('umask 077; cat > '+shlex.quote(dest),60,Path(src).read_bytes())
 def deploy():
  ssh('mkdir -p /content/nce')
  archive=work/'pipeline.tar.gz'
  with tarfile.open(archive,'w:gz') as t:
   for f in pipeline.rglob('*'):
    if f.is_file() and not any(x in f.parts for x in ('__pycache__','.pytest_cache','.git')) and '.egg-info' not in str(f):t.add(f,arcname='pipeline/'+str(f.relative_to(pipeline)))
  for src,dest in [(archive,'pipeline.tar.gz'),(a.inventory,'inventory.json'),(a.pilot_review,'pilot_review.json'),(a.rclone_config,'drive-runtime.conf'),(a.github_token_file,'github-publisher-token'),(a.api_config,'vision_api_credentials.json')]:upload(src,'/content/nce/'+dest)
  ssh('cd /content/nce && tar -xzf pipeline.tar.gz && chmod 600 drive-runtime.conf github-publisher-token vision_api_credentials.json')
  script="from pathlib import Path\nimport subprocess\nb=Path('/content/nce')\n"
  script+="with (b/'batch_driver.log').open('a') as log:\n p=subprocess.Popen(['python3',str(b/'pipeline/scripts/runtime_driver.py'),'--device',"+repr('cpu' if a.accelerator=='NONE' else 'cuda:0')+"],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)\n(b/'batch_driver.pid').write_text(str(p.pid))\n"
  ssh('python3 -',45,script)
 def release(reason,balance):
  api('stop','-s',session)
  (state_file.parent/('released_'+session+'.json')).write_text(json.dumps({'time':time.time(),'reason':reason,'balance':balance}))
  save(reason,resource_released=True,balance=balance)
 def probe():
  script="import sys,json\nsys.path.insert(0,'/content/nce/pipeline')\nfrom course_pipeline.health import inspect_runtime\nprint(json.dumps(inspect_runtime('/content/nce')))\n"
  return json.loads(ssh('python3 -',45,script))
 if a.probe_only:
  print(json.dumps(probe(),ensure_ascii=False,indent=2));return
 previous_path=work/'controller_status.json'
 if previous_path.exists():
  previous=json.loads(previous_path.read_text())
  if previous.get('state')=='complete' and previous.get('resource_released'):return
 watch_file=work/'progress_watch.json'
 try:watch=json.loads(watch_file.read_text())
 except (OSError,ValueError):watch={}
 if watch.get('initial_session')==a.session and watch.get('session'):
  saved_session=watch['session'];known=json.loads(state_file.read_text())
  if saved_session in known and known[saved_session].get('accelerator')==a.accelerator:session=saved_session
 watch['initial_session']=a.session
 def record_watch():
  temporary=watch_file.with_suffix('.tmp');temporary.write_text(json.dumps(watch));temporary.replace(watch_file)
 errors=0
 while True:
  try:
   usage=api('usage');m=re.search(r'Current balance:\s*([0-9.]+)',usage);balance=float(m[1]) if m else None
   rate=re.search(r'Usage rate:\s*([0-9.]+)',usage)
   with (work/'usage.jsonl').open('a') as f:f.write(json.dumps({'time':time.time(),'session':session,'balance':balance,'rate':float(rate[1]) if rate else None})+'\n')
   if balance is not None and balance<=1:
    release('stopped_at_balance_reserve_requires_recharge_authorization',balance);return
   api('sessions');sessions=json.loads(state_file.read_text())
   if session not in sessions:
    save('recovering_lost_runtime',balance=balance)
    session='nce-'+('cpu' if a.accelerator=='NONE' else 'l4')+'-resume-'+time.strftime('%Y%m%d%H%M%S',time.gmtime())
    api('new','-s',session,*(['--high-mem'] if a.accelerator=='NONE' else ['--gpu','L4']))
    watch['session']=session;record_watch()
    deploy()
   status=probe()
   if status['batch'] and status['batch'].get('state')=='complete':
    (work/'completed_batch.json').write_text(json.dumps(status,ensure_ascii=False,indent=2))
    release('complete',balance);return
   now=time.time();signature=progress_signature(status)
   if watch.get('session')!=session or watch.get('signature')!=signature:
    watch.update(session=session,signature=signature,last_progress_at=now)
   reason=recovery_reason(status,watch.get('last_progress_at',now),now,a.stall_seconds)
   if reason:
    (work/'failed_batch.json').write_text(json.dumps({'reason':reason,'health':status},ensure_ascii=False,indent=2))
    recent=[t for t in watch.get('recoveries',[]) if now-t<3600]
    if len(recent)>=a.max_recoveries_per_hour:
     save('recovery_limit_needs_repair',balance=balance,reason=reason,result=status)
     release('needs_repair_checkpoint_preserved',balance);return
    recent.append(now);watch.update(recoveries=recent,last_progress_at=now);record_watch()
    repair=ssh('python3 /content/nce/pipeline/scripts/runtime_driver.py --device '+('cpu' if a.accelerator=='NONE' else 'cuda:0')+' --recover',60)
    with (work/'recoveries.jsonl').open('a') as f:f.write(json.dumps({'time':now,'session':session,'reason':reason,'repair':json.loads(repair)})+'\n')
    save('resuming_from_checkpoint',balance=balance,reason=reason,result=status)
    errors=0;time.sleep(10);continue
   if not status['driver_exists']:deploy()
   record_watch()
   save('running',balance=balance,result=status);errors=0
  except Exception as exc:
   errors+=1;save('retrying_control',error_type=type(exc).__name__,detail=str(exc)[:500],consecutive_errors=errors)
   if errors==3:
    try:api('status','-s',session)
    except Exception:pass
   if errors>=5:
    # A broken SSH bridge is not evidence that productive model work stopped.
    # Reconnect without terminating the runtime; the balance check still runs.
    control=Path.home()/'.cache/nce-colab'/session
    with control.with_suffix('.lock').open('w') as lock:
     fcntl.flock(lock,fcntl.LOCK_EX)
     subprocess.run(['ssh','-O','exit','-o','ControlPath='+str(control),'root@'+session],capture_output=True,timeout=15)
    save('reconnecting_control_without_stopping_runtime',consecutive_errors=errors)
  time.sleep(45)

if __name__=='__main__':main()
