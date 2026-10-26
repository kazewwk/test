#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from course_pipeline.cli import process
from course_pipeline.common import load,write_json,digest
from course_pipeline.fusion import validate_lesson
from course_pipeline.publish import publish_lesson
from course_pipeline.indexes import update_series_index

p=argparse.ArgumentParser(description='Sequential resumable processing; requires a verified pilot.')
p.add_argument('--inventory',required=True)
p.add_argument('--pilot-review',required=True)
p.add_argument('--cache',required=True)
p.add_argument('--output',required=True)
p.add_argument('--checkout',required=True)
p.add_argument('--rclone-config',required=True)
p.add_argument('--remote',default='bili_drive')
p.add_argument('--device',choices=['cpu','cuda:0'],default='cpu')
p.add_argument('--threads',type=int,default=8)
p.add_argument('--ocr-python',required=True)
p.add_argument('--ocr-engine',choices=['paddle','onnx'],default='paddle')
p.add_argument('--public-authorized',action='store_true')
p.add_argument('--limit',type=int)
a=p.parse_args()
review=load(a.pilot_review)
if review.get('decision')!='pass' or not review.get('reviewer') or not review.get('checked_intervals'):
    raise SystemExit('Pilot review must include a reviewer, checked intervals, and pass decision')
pilot=Path(review['lesson_directory'])
if validate_lesson(pilot) or digest(pilot/'manifest.json')!=review['manifest_sha256']:
    raise SystemExit('Pilot artifact verification failed or changed after review')
a.video=None;a.prepare_only=False;a.ignore_regions=[]
rows=load(a.inventory)
completed=0
for row in rows:
    if not row['series'].startswith('新概念英语'):
        raise SystemExit('Current authorized batch scope is New Concept English only')
    record=Path(a.cache)/'publication'/(row['drive_file_id']+'.json')
    if record.exists():
        receipt=load(record)
        local=Path(a.output)/row['series']/row['directory']
        if (local/'manifest.json').exists() and not validate_lesson(local):
            manifest=load(local/'manifest.json')
            if manifest['source'].get('drive_md5')==row.get('drive_md5'):
                continue
    out=process(row,a)
    indexes=update_series_index(rows,a.output,row['series'])
    receipt=publish_lesson(out,a.checkout,public_authorized=a.public_authorized,series_files=indexes)
    write_json(record,receipt)
    completed+=1
    print(json.dumps({'completed_this_run':completed,'drive_file_id':row['drive_file_id'],**receipt},ensure_ascii=False),flush=True)
    # Remove only our verified local temporary source after publication. Drive is read-only.
    video=Path(a.cache)/'downloads'/(row['drive_file_id']+'.mp4')
    if video.exists() and digest(video)==load(out/'manifest.json')['source']['video_sha256']:
        video.unlink()
    if a.limit and completed>=a.limit:break
