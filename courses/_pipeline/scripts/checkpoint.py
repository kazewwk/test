#!/usr/bin/env python3
"""Persist intermediate text/coordinates to a separate, explicitly unfinished branch."""
from pathlib import Path
import argparse,subprocess,os,time,json,shutil


def main():
 p=argparse.ArgumentParser(description=__doc__)
 for key in ['source','checkout','token-file']:p.add_argument('--'+key,required=True)
 p.add_argument('--repository',default='kazewwk/test')
 p.add_argument('--branch',default='nce-processing-checkpoints')
 p.add_argument('--interval',type=int,default=180)
 a=p.parse_args();source=Path(a.source);checkout=Path(a.checkout)
 env=os.environ.copy();env['GH_TOKEN']=Path(a.token_file).read_text().strip()
 def run(args):return subprocess.run(list(map(str,args)),env=env,capture_output=True,text=True,check=True,timeout=180).stdout
 run(['gh','auth','setup-git','--hostname','github.com'])
 if not (checkout/'.git').exists():
  run(['git','clone','--filter=blob:none','--depth','1','--no-checkout',f'https://github.com/{a.repository}.git',checkout])
  run(['git','-C',checkout,'sparse-checkout','set','--no-cone','/_checkpoint/'])
  remote=run(['git','-C',checkout,'ls-remote','--heads','origin',a.branch])
  if remote:
   run(['git','-C',checkout,'fetch','--depth','1','origin',a.branch])
   run(['git','-C',checkout,'checkout','-b',a.branch,'FETCH_HEAD'])
  else:run(['git','-C',checkout,'checkout','-b',a.branch,'origin/main'])
 run(['git','-C',checkout,'config','user.name','kazewwk'])
 run(['git','-C',checkout,'config','user.email','127607618+kazewwk@users.noreply.github.com'])
 target=checkout/'_checkpoint';target.mkdir(exist_ok=True)
 (target/'README.md').write_text('# 未完成的解析检查点\n\n此分支只备份正在运行任务的原始模型候选、文本和坐标；完整验收资料以 main 分支 courses/ 为准。\n截图／文档裁剪图片不在此备份中，原始 Drive 视频保留，可重新抽帧与复原。没有完成标记的材料不得视为完整课程。\n')
 while True:
  try:
   count=0
   for f in source.rglob('*'):
    if not f.is_file() or f.suffix not in ('.json','.jsonl','.md','.srt','.txt'):continue
    if 'frames' in f.relative_to(source).parts:continue
    data=f.read_bytes()
    if f.suffix=='.json':
     try:json.loads(data)
     except (ValueError,UnicodeError):continue
    dest=target/'results'/f.relative_to(source);dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists() or dest.read_bytes()!=data:dest.write_bytes(data);count+=1
   run(['git','-C',checkout,'add','--','_checkpoint'])
   if run(['git','-C',checkout,'diff','--cached','--name-only']).strip():
    run(['git','-C',checkout,'commit','-m',f'checkpoint: preserve {count} updated course evidence files'])
   # Retry an unpushed commit even when the next snapshot has no content changes.
   run(['git','-C',checkout,'push','origin',a.branch])
   sha=run(['git','-C',checkout,'rev-parse','HEAD']).strip()
   (source.parent/'checkpoint_receipt.json').write_text(json.dumps({'branch':a.branch,'commit':sha,'time':time.time(),'updated_files':count}))
   print(json.dumps({'checkpoint_commit':sha,'updated_files':count}),flush=True)
  except Exception as e:print(json.dumps({'checkpoint_retry':type(e).__name__}),flush=True)
  time.sleep(a.interval)

if __name__=='__main__':main()
