#!/usr/bin/env python3
"""Resumable New Concept batch; every completed video is committed and verified."""
import argparse,json,sys,shutil,traceback,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from course_pipeline.cli import process
from course_pipeline.common import load,write_json,digest,utcnow
from course_pipeline.fusion import validate_lesson
from course_pipeline.publish import publish_lesson
from course_pipeline.indexes import update_series_index,update_catalog


def publication_matches(receipt,row):
    return (receipt.get('source_drive_file_id')==row['drive_file_id']
            and bool(receipt.get('source_video_sha256'))
            and bool(receipt.get('commit')) and receipt.get('verified_files',0)>0
            and bool(row.get('drive_md5'))
            and receipt.get('source_drive_md5')==row['drive_md5']
            and (not row.get('drive_sha256') or receipt['source_video_sha256']==row['drive_sha256']))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['inventory','pilot-review','cache','output','checkout','rclone-config','ocr-python','visual-python','mineru-python']:
        p.add_argument('--'+name,required=True)
    p.add_argument('--remote',default='bili_drive')
    p.add_argument('--device',choices=['cpu','cuda:0'],default='cuda:0')
    p.add_argument('--threads',type=int,default=10)
    p.add_argument('--ocr-engine',choices=['paddle','onnx'],default='paddle')
    p.add_argument('--public-authorized',action='store_true')
    p.add_argument('--limit',type=int)
    p.add_argument('--retain-completed',action='store_true')
    a=p.parse_args();cache=Path(a.cache);cache.mkdir(parents=True,exist_ok=True)
    review=load(a.pilot_review)
    if review.get('decision')!='pass' or not review.get('reviewer') or not review.get('checked_intervals'):
        raise SystemExit('Pilot review requires a reviewer, checked intervals, and pass decision')
    pilot=Path(review['lesson_directory'])
    if validate_lesson(pilot) or digest(pilot/'manifest.json')!=review['manifest_sha256']:
        raise SystemExit('Pilot artifact verification failed or changed after review')
    a.video=None;a.prepare_only=False;a.ignore_regions=[];a.asr_only=False
    rows=load(a.inventory);completed=0;failed=[]
    if any(not row['series'].startswith('新概念英语') for row in rows):
        raise SystemExit('Authorized batch scope is New Concept English only')
    for row in rows:
        record=cache/'publication'/(row['drive_file_id']+'.json')
        if record.exists() and publication_matches(load(record),row):continue
        status={'updated_at':utcnow(),'state':'processing','source':row,'completed_this_run':completed,'failures':failed}
        write_json(cache/'batch_status.json',status)
        try:
            out=process(row,a)
            indexes=update_series_index(rows,a.output,row['series'])
            catalog=update_catalog(rows,a.output)
            receipt=publish_lesson(out,a.checkout,public_authorized=a.public_authorized,series_files=indexes,catalog_files=catalog)
            write_json(record,receipt)
            completed+=1
            print(json.dumps({'completed_this_run':completed,'drive_file_id':row['drive_file_id'],**receipt},ensure_ascii=False),flush=True)
            video=cache/'downloads'/(row['drive_file_id']+'.mp4')
            if video.exists() and digest(video)==receipt['source_video_sha256']:video.unlink()
            if not a.retain_completed and out.resolve()!=pilot.resolve():
                # GitHub has every byte and the receipt above. Retain local provenance
                # and QC for series indexes; free only this task's uploaded artifacts.
                for child in out.iterdir():
                    if child.name in ('manifest.json','qc_report.json'):continue
                    if child.is_dir():shutil.rmtree(child)
                    else:child.unlink()
            if a.limit and completed>=a.limit:break
        except Exception as exc:
            failed.append({'drive_file_id':row['drive_file_id'],'title':row['title'],'error':str(exc)[:1000]})
            write_json(cache/'failures'/f"{row['drive_file_id']}.json",{'time':utcnow(),'error':str(exc),'traceback':traceback.format_exc()})
            print(json.dumps({'state':'failed_pending_retry',**failed[-1]},ensure_ascii=False),flush=True)
    pending=[]
    for row in rows:
        receipt=cache/'publication'/(row['drive_file_id']+'.json')
        if not receipt.exists() or not publication_matches(load(receipt),row):pending.append(row['drive_file_id'])
    write_json(cache/'batch_status.json',{'updated_at':utcnow(),'state':'complete' if not pending else 'incomplete',
                                        'total':len(rows),'completed':len(rows)-len(pending),'pending':pending,'failures':failed})
    if pending:raise SystemExit(1)

if __name__=='__main__':main()
