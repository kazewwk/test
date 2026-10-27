#!/usr/bin/env python3
"""Restore authorized course work and run resumable local models plus the user's image API."""
from pathlib import Path
import argparse,json,os,shutil,subprocess,time

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--root',default='/content/nce')
 p.add_argument('--device',choices=['cpu','cuda:0'],required=True)
 a=p.parse_args();b=Path(a.root);env=os.environ.copy()
 env.update(OMP_NUM_THREADS='8',MKL_NUM_THREADS='8',OPENBLAS_NUM_THREADS='8')
 def run(args):return subprocess.run(list(map(str,args)),check=True,env=env)
 def status(state,**extra):
  data={'state':state,'time':time.time(),'device':a.device,**extra}
  temporary=b/'driver_status.json.tmp';temporary.write_text(json.dumps(data));temporary.replace(b/'driver_status.json')
 status('environment')
 install_pid=b/'gpu_install.pid'
 if install_pid.exists():
  while (Path('/proc')/install_pid.read_text().strip()/'cmdline').exists():
   try:alive=bool((Path('/proc')/install_pid.read_text().strip()/'cmdline').read_bytes())
   except OSError:alive=False
   if not alive:break
   time.sleep(5)
 if not (b/'environments.ready').exists():
  if not all((b/name/'installed.lock.txt').exists() for name in ('venv','venv-ocr','venv-mineru')):
   run(['bash',b/'pipeline/scripts/install.sh','cpu' if a.device=='cpu' else 'cuda',b/'venv','api'])
  for name in ('venv','venv-ocr','venv-mineru'):run([b/name/'bin/pip','check'])
  (b/'environments.ready').touch()
 status('restoring')
 env['GH_TOKEN']=(b/'github-publisher-token').read_text().strip()
 run(['gh','auth','setup-git','--hostname','github.com'])
 checkout=b/'github-checkout';review=json.loads((b/'pilot_review.json').read_text());relative=Path(review['lesson_relative_path'])
 if not (checkout/'.git').exists():
  run(['git','clone','--filter=blob:none','--depth','1','--no-checkout','--branch','main','https://github.com/kazewwk/test.git',checkout])
  run(['git','-C',checkout,'sparse-checkout','set','--no-cone','/courses/_pipeline/','/courses/inventory.json','/courses/*.md','/courses/*/*.md','/courses/*/quality_summary.json','/courses/*/*/manifest.json','/courses/*/*/qc_report.json','/courses/'+str(relative)+'/'])
  run(['git','-C',checkout,'checkout','main'])
 else:run(['git','-C',checkout,'pull','-q','--ff-only'])
 pilot=b/'validated_pilot_snapshot'
 if not pilot.exists():shutil.copytree(checkout/'courses'/relative,pilot)
 review['lesson_directory']=str(pilot);(b/'pilot_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2))
 checkpoint=b/'checkpoint_restore'
 if not (checkpoint/'.git').exists():
  run(['git','clone','--filter=blob:none','--depth','1','--single-branch','--branch','nce-processing-checkpoints','--sparse','https://github.com/kazewwk/test.git',checkpoint])
  run(['git','-C',checkpoint,'sparse-checkout','set','_checkpoint'])
 else:run(['git','-C',checkpoint,'pull','-q','--ff-only'])
 run([b/'venv/bin/python',b/'pipeline/scripts/restore_progress.py','--inventory',b/'inventory.json','--checkout',checkout,'--output',b/'courses','--cache',b/'cache','--checkpoint-checkout',checkpoint])
 with (b/'checkpoint_batch.log').open('a') as log:
  backup=subprocess.Popen(['python3',str(b/'pipeline/scripts/checkpoint.py'),'--source',str(b/'courses'),'--checkout',str(b/'checkpoint_publish'),'--token-file',str(b/'github-publisher-token')],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
 (b/'checkpoint_batch.pid').write_text(str(backup.pid))
 env.pop('GH_TOKEN',None);env['NCE_GITHUB_TOKEN_FILE']=str(b/'github-publisher-token')
 script='batch_concurrent.py' if a.device=='cuda:0' else 'batch.py'
 args=[b/'venv/bin/python',b/'pipeline/scripts'/script,'--inventory',b/'inventory.json','--pilot-review',b/'pilot_review.json','--cache',b/'cache','--output',b/'courses','--checkout',checkout,'--rclone-config',b/'drive-runtime.conf','--ocr-python',b/'venv-ocr/bin/python','--mineru-python',b/'venv-mineru/bin/python','--api-config',b/'vision_api_credentials.json','--api-model','gpt-6.1-terra','--api-concurrency','2','--device',a.device,'--threads','8','--public-authorized']
 if a.device=='cpu':args+=['--visual-python',b/'venv/bin/python','--visual-backend','api']
 status('running_batch')
 for attempt in range(3):
  result=subprocess.run(list(map(str,args)),env=env)
  if result.returncode==0:break
  status('retrying_batch',attempt=attempt+1,exit_code=result.returncode)
  time.sleep(30*(attempt+1))
 (b/'batch_exit.json').write_text(json.dumps({'exit_code':result.returncode,'time':time.time()}))
 status('complete' if result.returncode==0 else 'needs_repair',exit_code=result.returncode)

if __name__=='__main__':main()
