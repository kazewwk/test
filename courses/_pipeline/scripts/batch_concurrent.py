#!/usr/bin/env python3
"""Keep the GPU producing ASR/OCR while a separate process reviews images and publishes lessons."""
from pathlib import Path
import argparse,json,sys,time,subprocess,shutil,uuid,traceback,os,signal
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from course_pipeline.cli import process
from course_pipeline.common import load,write_json,digest,utcnow
from course_pipeline.fusion import validate_lesson
from course_pipeline.publish import publish_lesson
from course_pipeline.indexes import update_series_index,update_catalog
from batch import publication_matches


def arguments():
 p=argparse.ArgumentParser(description=__doc__)
 for n in ['inventory','pilot-review','cache','output','checkout','rclone-config','ocr-python','mineru-python','api-config']:
  p.add_argument('--'+n,required=True)
 p.add_argument('--role',choices=['supervisor','gpu','finish'],default='supervisor')
 p.add_argument('--device',default='cuda:0');p.add_argument('--threads',type=int,default=10)
 p.add_argument('--api-model',default='gpt-6.1-terra');p.add_argument('--api-concurrency',type=int,default=2)
 p.add_argument('--max-pending',type=int,default=3);p.add_argument('--public-authorized',action='store_true')
 return p.parse_args()


def main():
 a=arguments();cache=Path(a.cache);cache.mkdir(parents=True,exist_ok=True);out=Path(a.output)
 a.visual_backend='api';a.visual_python=sys.executable;a.ocr_engine='paddle';a.remote='bili_drive'
 a.video=None;a.prepare_only=False;a.asr_only=False;a.ignore_regions=[]
 rows=load(a.inventory)
 if any(not r['series'].startswith('新概念英语') for r in rows):raise ValueError('Only New Concept series are authorized')
 def published(row):
  p=cache/'publication'/(row['drive_file_id']+'.json')
  return p.exists() and publication_matches(load(p),row)
 def ready(row):
  p=out/row['series']/row['directory']/'partial_manifest.json'
  if not p.exists():return False
  value=load(p)
  return value.get('state')=='gpu_complete_visual_api_pending' and value.get('source',{}).get('drive_md5')==row['drive_md5']
 if a.role=='supervisor':
  review=load(a.pilot_review);pilot=Path(review['lesson_directory'])
  if review.get('decision')!='pass' or validate_lesson(pilot) or digest(pilot/'manifest.json')!=review['manifest_sha256']:
   raise RuntimeError('Pilot review/artifact validation failed')
  (cache/'gpu_done.json').unlink(missing_ok=True)
  (cache/'batch_exit.json').unlink(missing_ok=True)
  children=[]
  for role in ['gpu','finish']:
   args=[sys.executable,str(Path(__file__).resolve()),*sys.argv[1:],'--role',role]
   log=(cache/(role+'_worker.log')).open('a')
   children.append(subprocess.Popen(args,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True));log.close()
  write_json(cache/'batch_processes.json',{'supervisor':os.getpid(),'gpu':children[0].pid,'finish':children[1].pid})
  while any(p.poll() is None for p in children):
   if any(p.poll() not in (None,0) for p in children):
    for p in children:
     if p.poll() is None:os.killpg(p.pid,signal.SIGTERM)
    break
   time.sleep(3)
  codes=[p.wait() for p in children]
  write_json(cache/'batch_exit.json',{'time':utcnow(),'exit_codes':codes})
  raise SystemExit(any(codes))
 if a.role=='gpu':
  a.gpu_only=True;failed=[]
  for row in rows:
   if published(row) or ready(row):continue
   while sum(ready(r) and not published(r) for r in rows)>=a.max_pending:time.sleep(10)
   write_json(cache/'gpu_status.json',{'state':'processing','source':row,'updated_at':utcnow()})
   try:
    process(row,a)
    print(json.dumps({'state':'gpu_complete_api_pending','file_id':row['drive_file_id']},ensure_ascii=False),flush=True)
   except Exception as exc:
    failed.append({'file_id':row['drive_file_id'],'error':str(exc)[:1000]})
    write_json(cache/'gpu_failures'/f"{row['drive_file_id']}.json",{'error':str(exc),'traceback':traceback.format_exc()})
    print(json.dumps(failed[-1],ensure_ascii=False),flush=True)
  write_json(cache/'gpu_done.json',{'time':utcnow(),'failures':failed});return
 a.gpu_only=False;attempts={};failures=[]
 while True:
  remaining=[r for r in rows if not published(r)]
  if not remaining:
   write_json(cache/'batch_status.json',{'state':'complete','completed':len(rows),'total':len(rows),'updated_at':utcnow()});return
  candidates=[r for r in remaining if ready(r) and attempts.get(r['drive_file_id'],0)<3]
  if not candidates:
   write_json(cache/'batch_status.json',{'state':'awaiting_gpu_or_retry','completed':len(rows)-len(remaining),'total':len(rows),'failures':failures,'updated_at':utcnow()})
   if (cache/'gpu_done.json').exists():
    write_json(cache/'batch_status.json',{'state':'incomplete','completed':len(rows)-len(remaining),'total':len(rows),'failures':failures,'gpu':load(cache/'gpu_done.json'),'updated_at':utcnow()})
    raise SystemExit(1)
   time.sleep(10);continue
  row=candidates[0];attempts[row['drive_file_id']]=attempts.get(row['drive_file_id'],0)+1
  write_json(cache/'batch_status.json',{'state':'api_review_and_publication','source':row,'completed':len(rows)-len(remaining),'total':len(rows),'updated_at':utcnow()})
  try:
   lesson=process(row,a)
   indexes=update_series_index(rows,out,row['series']);catalog=update_catalog(rows,out)
   checkout=Path(a.checkout).parent/(Path(a.checkout).name+'-uploads')/(row['drive_file_id']+'-'+uuid.uuid4().hex[:8])
   receipt=publish_lesson(lesson,checkout,public_authorized=a.public_authorized,series_files=indexes,catalog_files=catalog)
   write_json(cache/'publication'/(row['drive_file_id']+'.json'),receipt);write_json(out/'_publication'/(row['drive_file_id']+'.json'),receipt)
   if (checkout/'.git/course_pipeline_owned').exists():shutil.rmtree(checkout)
   video=cache/'downloads'/(row['drive_file_id']+'.mp4')
   if video.exists() and digest(video)==receipt['source_video_sha256']:video.unlink()
   work=cache/'jobs'/row['drive_file_id']
   if work.exists():shutil.rmtree(work)
   pilot_id=load(a.pilot_review).get('source_drive_file_id')
   if row['drive_file_id']!=pilot_id:
    for child in lesson.iterdir():
     if child.name in ('manifest.json','qc_report.json','source.json'):continue
     if child.is_dir():shutil.rmtree(child)
     else:child.unlink()
   print(json.dumps({'published':row['drive_file_id'],**receipt},ensure_ascii=False),flush=True)
  except Exception as exc:
   failure={'file_id':row['drive_file_id'],'attempt':attempts[row['drive_file_id']],'error':str(exc)[:1000]};failures.append(failure)
   write_json(cache/'publication_failures'/f"{row['drive_file_id']}.json",{**failure,'traceback':traceback.format_exc()})
   print(json.dumps(failure,ensure_ascii=False),flush=True)
   if attempts[row['drive_file_id']]>=3:raise SystemExit(1)
   time.sleep(15)

if __name__=='__main__':main()
