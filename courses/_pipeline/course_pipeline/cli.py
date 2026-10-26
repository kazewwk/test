from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path
import soundfile as sf
from .common import load, write_json, digest, run, retry, utcnow, atomic_text
from .drive import Drive
from .media import probe, verify_decode, extract_audio, audio_windows, silence_intervals, extract_frames
from .fusion import assemble, validate_lesson, disagreement, overlap
from .monitor import Monitor


class State:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.execute('CREATE TABLE IF NOT EXISTS jobs (drive_id TEXT, sha256 TEXT, config_sha TEXT, '
                        'state TEXT, updated TEXT, detail TEXT, PRIMARY KEY(drive_id,sha256,config_sha))')

    def set(self, source, fingerprint, state, detail=''):
        self.db.execute('INSERT OR REPLACE INTO jobs VALUES (?,?,?,?,?,?)',
                        (source['drive_file_id'], source['video_sha256'], fingerprint, state, utcnow(), detail))
        self.db.commit()


def worker(stage, job, job_dir, ocr_python):
    path = job_dir / (stage + '.json')
    write_json(path, job)
    python = ocr_python if stage in ('ocr','document') else sys.executable
    log = job_dir / (stage + '.log')
    # Model processes run sequentially; their GPU/CPU memory is released on exit.
    retry(lambda: run([python,'-m','course_pipeline.models', stage.removeprefix('review_'),path],
                      timeout=86400,log=log), tries=2)


def process(source, args):
    source = dict(source)
    cache = Path(args.cache).resolve()
    cache.mkdir(parents=True,exist_ok=True)
    out = Path(args.output).resolve() / source['series'] / source['directory']
    out.mkdir(parents=True,exist_ok=True)
    video = Path(args.video).resolve() if args.video else cache / 'downloads' / (source['drive_file_id']+'.mp4')
    if not args.video:
        if not args.rclone_config:
            raise ValueError('Use --video or --rclone-config')
        receipt=Drive(args.rclone_config,args.remote).download(source['drive_file_id'],video)
        write_json(cache / 'downloads' / (source['drive_file_id']+'.receipt.json'),receipt)
    if video.stat().st_size != source['size_bytes']:
        raise ValueError('Downloaded video size differs from source inventory')
    if source.get('drive_md5') and digest(video,'md5') != source['drive_md5']:
        raise ValueError('Downloaded video MD5 differs from Drive')
    source['video_sha256'] = digest(video)
    if source.get('drive_sha256') and source['drive_sha256'] != source['video_sha256']:
        raise ValueError('Downloaded video SHA256 differs from Drive')
    model_revisions = load(Path(__file__).resolve().parents[1] / 'model_revisions.json')
    settings = dict(device=args.device,threads=args.threads,core_seconds=30,overlap_seconds=2,
                    ignore_regions=args.ignore_regions,model_revisions=model_revisions)
    fingerprint=hashlib.sha256(json.dumps(settings,sort_keys=True).encode()).hexdigest()
    state=State(cache/'state.sqlite')
    if (out/'manifest.json').exists():
        old=load(out/'manifest.json')
        if old['source']['video_sha256']==source['video_sha256'] and old.get('config_sha256')==fingerprint and not validate_lesson(out):
            return out
    work=cache/'jobs'/source['drive_file_id']/source['video_sha256'][:16]/fingerprint[:16]
    work.mkdir(parents=True,exist_ok=True)
    write_json(work/'source.json',source)
    write_json(work/'settings.json',settings)
    state.set(source,fingerprint,'preparing')
    try:
        with Monitor(work/'resources.jsonl'):
            m=probe(video)
            if not (work/'decode.ok').exists():
                verify_decode(video,work/'decode.log')
                atomic_text(work/'decode.ok',source['video_sha256'])
            audio=work/'audio.wav'
            if not audio.exists():
                extract_audio(video,audio,work/'audio.log')
            info=sf.info(audio)
            duration=info.frames/info.samplerate
            origin=float(m['audio'].get('start_time',0))-float(m['format'].get('start_time',0))
            ainfo=dict(duration_seconds=duration,source_start_seconds=origin,
                       silence_intervals=silence_intervals(audio,duration))
            write_json(work/'audio_info.json',ainfo)
            windows=audio_windows(duration)
            # Key frames are verified by content hashes before reusing extraction.
            frame_record=work/'frames.complete.json'
            valid_frames=False
            if frame_record.exists() and (out/'frames.json').exists():
                old=load(frame_record)
                valid_frames=old.get('source_sha256')==source['video_sha256'] and old.get('config_sha256')==fingerprint
                if valid_frames:
                    valid_frames=all((out/f['path']).exists() and digest(out/f['path'])==f['sha256']
                                     for f in load(out/'frames.json')['frames'])
            if not valid_frames:
                extract_frames(video,out,m,args.ignore_regions)
                write_json(frame_record,dict(source_sha256=source['video_sha256'],config_sha256=fingerprint))
            frames=load(out/'frames.json')['frames']
            if args.prepare_only:
                write_json(out/'preparation_status.json',dict(state='prepared_only',source=source,media=m,
                           audio=ainfo,keyframes=len(frames),not_run=['ASR','cross_check','OCR','VLM','fusion']))
                state.set(source,fingerprint,'prepared_only')
                return out
            base=dict(audio=str(audio),source_sha256=source['video_sha256'],device=args.device,
                      threads=args.threads,windows=windows,model_revisions=model_revisions,
                      cache_fingerprint=fingerprint,lesson_dir=str(out),frames=frames)
            for stage in ('qwen','whisper'):
                state.set(source,fingerprint,stage)
                worker(stage,{**base,'output':str(out/'evidence'/stage)},work,args.ocr_python)
            review_windows=[]
            for win in windows:
                q=load(out/'evidence/qwen'/f"chunk_{win['id']:05d}.json")
                w=load(out/'evidence/whisper'/f"chunk_{win['id']:05d}.json")
                silence=sum(overlap([win['core_start'],win['core_end']],s) for s in ainfo['silence_intervals'])
                length=win['core_end']-win['core_start']
                if disagreement(q['text'],w['text'])>.22 or (not q['text'].strip() and length-silence>1) or (q['text'].strip() and silence>length*.95):
                    review_windows.append({**win,'start':max(0,win['start']-3),'end':min(duration,win['end']+3)})
            if review_windows:
                state.set(source,fingerprint,'review')
                for stage in ('review_qwen','review_whisper'):
                    worker(stage,{**base,'windows':review_windows,'beam_size':7,'output':str(out/'evidence'/stage)},work,args.ocr_python)
            for stage in ('ocr','visual'):
                state.set(source,fingerprint,stage)
                worker(stage,{**base,'output':str(out/'evidence'/stage)},work,args.ocr_python)
            document_frames=[f for f in frames if load(out/'evidence/visual'/(Path(f['path']).stem+'.json'))['parsed'].get('needs_document_ocr')]
            if document_frames:
                state.set(source,fingerprint,'document_ocr')
                worker('document',{**base,'frames':document_frames,'output':str(out/'evidence/document')},work,args.ocr_python)
            quality=assemble(out,source,m,ainfo,windows)
            manifest=load(out/'manifest.json')
            manifest.update(config_sha256=fingerprint,settings=settings,
                            publication_authorization='User explicitly authorized full public transcripts and screenshots, 2026-10-26')
            write_json(out/'manifest.json',manifest)
            errors=validate_lesson(out)
            if errors:
                raise RuntimeError('Artifact validation failed: '+', '.join(errors))
            state.set(source,fingerprint,'complete_with_review_flags' if quality['issues'] else 'complete')
    except BaseException as e:
        state.set(source,fingerprint,'failed',type(e).__name__+': '+str(e)[:500])
        raise
    return out


def main():
    p=argparse.ArgumentParser(description='Loss-preserving course extraction; no raw videos are published.')
    sub=p.add_subparsers(dest='command',required=True)
    s=sub.add_parser('process')
    s.add_argument('--inventory',required=True)
    s.add_argument('--file-id',required=True)
    s.add_argument('--video')
    s.add_argument('--rclone-config')
    s.add_argument('--remote',default='bili_drive')
    s.add_argument('--cache',required=True)
    s.add_argument('--output',required=True)
    s.add_argument('--device',choices=['cpu','cuda:0'],default='cpu')
    s.add_argument('--threads',type=int,default=8)
    s.add_argument('--ocr-python',required=True)
    s.add_argument('--ignore-regions',type=json.loads,default=[])
    s.add_argument('--prepare-only',action='store_true')
    v=sub.add_parser('validate')
    v.add_argument('directory')
    args=p.parse_args()
    if args.command=='validate':
        errors=validate_lesson(args.directory)
        print(json.dumps({'valid':not errors,'errors':errors},ensure_ascii=False))
        raise SystemExit(bool(errors))
    rows=load(args.inventory)
    source=next(x for x in rows if x['drive_file_id']==args.file_id)
    out=process(source,args)
    print(json.dumps({'output':str(out),'prepare_only':args.prepare_only},ensure_ascii=False))


if __name__=='__main__':
    main()
