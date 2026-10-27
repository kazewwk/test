from urllib.parse import quote
#!/usr/bin/env python3
"""Restore verified publication metadata and unfinished text checkpoints after runtime loss."""
from pathlib import Path
import argparse,json,shutil,subprocess,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from course_pipeline.common import load,write_json,utcnow


def main():
 p=argparse.ArgumentParser(description=__doc__)
 for n in ['inventory','checkout','output','cache']:p.add_argument('--'+n,required=True)
 p.add_argument('--checkpoint-checkout')
 a=p.parse_args();rows=load(a.inventory);by_id={r['drive_file_id']:r for r in rows}
 checkout=Path(a.checkout);output=Path(a.output);cache=Path(a.cache)
 commit=subprocess.run(['git','-C',str(checkout),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
 restored=0
 for manifest in (checkout/'courses').glob('*/*/manifest.json'):
  m=load(manifest);source=m.get('source',{});row=by_id.get(source.get('drive_file_id'))
  if not row or row.get('drive_md5')!=source.get('drive_md5') or not source.get('video_sha256'):continue
  if row.get('drive_sha256') and row['drive_sha256']!=source['video_sha256']:continue
  rel=Path('courses')/row['series']/row['directory']
  listing=subprocess.run(['git','-C',str(checkout),'ls-tree','-rz','--name-only',commit,'--',str(rel)],capture_output=True,check=True).stdout
  paths={s.decode() for s in listing.split(b'\0') if s}
  if any(str(rel/name) not in paths for name in m.get('artifacts',{})):continue
  qc=manifest.parent/'qc_report.json'
  if not qc.exists() or not m.get('artifacts'):continue
  dest=output/row['series']/row['directory'];dest.mkdir(parents=True,exist_ok=True)
  shutil.copy2(manifest,dest/'manifest.json');shutil.copy2(qc,dest/'qc_report.json')
  write_json(cache/'publication'/(row['drive_file_id']+'.json'),{
      'commit':commit,'source_drive_file_id':row['drive_file_id'],'source_video_sha256':source['video_sha256'],
      'source_drive_md5':row['drive_md5'],'verified_files':len(m['artifacts'])+1,
      'verification':'Restored published manifest and checked every listed path against the authenticated Git commit tree',
      'url':f'https://github.com/kazewwk/test/tree/{commit}/{quote(str(rel))}','time':utcnow()})
  restored+=1
 if a.checkpoint_checkout:
  checkpoint=Path(a.checkpoint_checkout)/'_checkpoint/results'
  candidates=list(checkpoint.glob('*/*/manifest.json'))+list(checkpoint.glob('*/*/partial_manifest.json'))
  candidates+=list(checkpoint.glob('*/*/source.json'))
  candidates+=list(checkpoint.glob('manifest.json'))+list(checkpoint.glob('partial_manifest.json'))
  seen=set()
  for marker in candidates:
   m=load(marker);source=m.get('source',m);row=by_id.get(source.get('drive_file_id'))
   if not row or row['drive_file_id'] in seen:continue
   seen.add(row['drive_file_id'])
   if (cache/'publication'/(row['drive_file_id']+'.json')).exists():continue
   if source.get('drive_md5')!=row.get('drive_md5'):continue
   dest=output/row['series']/row['directory'];dest.mkdir(parents=True,exist_ok=True)
   for f in marker.parent.rglob('*'):
    if f.is_file() and f.suffix in ('.json','.jsonl','.md','.srt','.txt'):
     target=dest/f.relative_to(marker.parent);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,target)
   # A metadata backup cannot claim that omitted crop images exist.
   (dest/'manifest.json').unlink(missing_ok=True)
 print(json.dumps({'restored_published_lessons':restored}),flush=True)

if __name__=='__main__':main()
