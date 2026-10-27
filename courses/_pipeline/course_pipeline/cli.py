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
from .fusion import assemble, validate_lesson, needs_asr_review, needs_document_ocr, overlap, core_text,language_mismatch
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


def inference_fingerprint(stage,job):
    kind=stage.removeprefix('review_')
    from .models import VISUAL_PROMPT,ASR_CONTEXT
    names={'qwen':['Qwen/Qwen3-ASR-1.7B','Qwen/Qwen3-ForcedAligner-0.6B'],
           'whisper':['Systran/faster-whisper-large-v3'],
           'visual':[job.get('visual_model','Qwen/Qwen3.5-9B')],
           'document':['PaddlePaddle/PaddleOCR-VL-1.6'],
           'mineru':['opendatalab/MinerU2.5-Pro-2605-1.2B']}.get(kind,[])
    data={'adapter_version':2,'stage':stage,'source_sha256':job['source_sha256'],
          'model_revisions':{k:job['model_revisions'][k] for k in names}}
    if kind in ('qwen','whisper'):
        data.update(windows=job['windows'],audio_format='16kHz-mono-pcm16-v1',
                    beam_size=job.get('beam_size',5) if kind=='whisper' else None)
        if kind=='qwen':data.update(context=job.get('context',ASR_CONTEXT),language=job.get('language'))
        if kind=='whisper':data['compute_type']='int8' if job.get('device')=='cpu' else 'float16'
    else:
        data['frames']=[(f['sha256'],f['time']) for f in job['frames']]
        if kind=='ocr':data['ocr_engine']=job.get('ocr_engine','paddle')
        if kind=='visual':
            data.update(prompt=job.get('prompt',VISUAL_PROMPT),max_tokens=job.get('max_new_tokens',2048))
            data['ocr_inputs']=[digest(Path(job['lesson_dir'])/'evidence/ocr'/(Path(f['path']).stem+'.json')) for f in job['frames']]
    # Hardware choice is recorded in each result; completed hypotheses can be
    # reused when moving the remaining stages between CPU and GPU.
    return hashlib.sha256(json.dumps(data,sort_keys=True).encode()).hexdigest()


def worker(stage, job, job_dir, ocr_python,visual_python=None,mineru_python=None):
    job={**job,'cache_fingerprint':inference_fingerprint(stage,job)}
    kind=stage.removeprefix('review_')
    output=Path(job['output'])
    if kind in ('qwen','whisper'):
        targets=[(output/f"chunk_{w['id']:05d}.json",'source_sha256',job['source_sha256']) for w in job['windows']]
    else:
        targets=[(output/(Path(f['path']).stem+'.json') if kind in ('ocr','visual') else output/Path(f['path']).stem/'complete.json',
                  'image_sha256',f['sha256']) for f in job['frames']]
    from .models import reusable
    if targets and all(reusable(p,job,key,value) for p,key,value in targets):
        print(json.dumps({'stage':stage,'state':'reused_complete','records':len(targets)}),flush=True)
        return
    path = job_dir / (stage + '.json')
    write_json(path, job)
    python = (ocr_python if stage in ('ocr','document') else
              visual_python if stage=='visual' and visual_python else
              mineru_python if stage=='mineru' and mineru_python else sys.executable)
    log = job_dir / (stage + '.log')
    env=os.environ.copy()
    env['PATH']=str(Path(python).parent)+os.pathsep+env.get('PATH','')
    library_dirs=sorted(Path(python).parent.parent.glob('lib/python*/site-packages/nvidia/*/lib'))
    if library_dirs:env['LD_LIBRARY_PATH']=':'.join(map(str,library_dirs))+':'+env.get('LD_LIBRARY_PATH','')
    # Model processes run sequentially; their GPU/CPU memory is released on exit.
    retry(lambda: run([python,'-m','course_pipeline.models', stage.removeprefix('review_'),path],
                      timeout=86400,log=log,env=env), tries=2)


def process(source, args):
    source = dict(source)
    if not args.prepare_only and not getattr(args,'asr_only',False):
        env_root=Path(sys.prefix)
        for key,suffix in [('visual_python','-vlm'),('mineru_python','-mineru')]:
            if not getattr(args,key,None):
                candidate=Path(str(env_root)+suffix)/'bin/python'
                if not candidate.exists():raise ValueError(f'Missing {key}: supply its interpreter path')
                setattr(args,key,str(candidate))
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
    code_hash=hashlib.sha256()
    for module in sorted(Path(__file__).resolve().parent.glob('*.py')):
        code_hash.update(module.name.encode());code_hash.update(module.read_bytes())
    settings = dict(device=args.device,threads=args.threads,core_seconds=30,overlap_seconds=2,
                    pipeline_code_sha256=code_hash.hexdigest(),frame_encoding='lossless WebP',
                    ignore_regions=args.ignore_regions,model_revisions=model_revisions,ocr_engine=args.ocr_engine)
    fingerprint=hashlib.sha256(json.dumps(settings,sort_keys=True).encode()).hexdigest()
    state=State(cache/'state.sqlite')
    if (out/'manifest.json').exists():
        old=load(out/'manifest.json')
        if old['source']['video_sha256']==source['video_sha256'] and old.get('config_sha256')==fingerprint and not validate_lesson(out):
            return out
    work=cache/'jobs'/source['drive_file_id']/source['video_sha256'][:16]/'media-v1'
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
            frame_key=hashlib.sha256(json.dumps({'ignore_regions':args.ignore_regions,'image_encoding':'lossless WebP','detector_version':1},sort_keys=True).encode()).hexdigest()
            valid_frames=False
            if frame_record.exists() and (out/'frames.json').exists():
                old=load(frame_record)
                valid_frames=old.get('source_sha256')==source['video_sha256'] and old.get('frame_key')==frame_key
                if valid_frames:
                    valid_frames=all((out/f['path']).exists() and digest(out/f['path'])==f['sha256']
                                     for f in load(out/'frames.json')['frames'])
            if not valid_frames:
                extract_frames(video,out,m,args.ignore_regions)
                write_json(frame_record,dict(source_sha256=source['video_sha256'],frame_key=frame_key))
            frames=load(out/'frames.json')['frames']
            if args.prepare_only:
                write_json(out/'preparation_status.json',dict(state='prepared_only',source=source,media=m,
                           audio=ainfo,keyframes=len(frames),not_run=['ASR','cross_check','OCR','VLM','fusion']))
                state.set(source,fingerprint,'prepared_only')
                return out
            base=dict(audio=str(audio),source_sha256=source['video_sha256'],device=args.device,
                      ocr_engine=args.ocr_engine,
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
                if needs_asr_review(q['text'],w['text']) or (not q['text'].strip() and length-silence>1) or (q['text'].strip() and silence>length*.95):
                    review_windows.append({**win,'start':max(0,win['start']-3),'end':min(duration,win['end']+3)})
            if review_windows:
                state.set(source,fingerprint,'review')
                for stage in ('review_qwen','review_whisper'):
                    worker(stage,{**base,'windows':review_windows,'beam_size':7,'output':str(out/'evidence'/stage)},work,args.ocr_python)
            language_windows=[]
            for win in review_windows:
                q=load(out/'evidence/qwen'/f"chunk_{win['id']:05d}.json")
                w=load(out/'evidence/whisper'/f"chunk_{win['id']:05d}.json")
                if language_mismatch(q,w):language_windows.append({**win,'language_hint':'Chinese'})
            if language_windows:
                worker('review_qwen',{**base,'windows':language_windows,'output':str(out/'evidence/language_review_qwen')},work,args.ocr_python)
            if getattr(args,'asr_only',False):
                raw='# '+source['title']+'：语音阶段草稿\n\n本文件仅完成语音阶段，画面融合和完整质量验收尚未完成。\n\n'
                checked=raw
                for win in windows:
                    q=load(out/'evidence/qwen'/f"chunk_{win['id']:05d}.json")
                    w=load(out/'evidence/whisper'/f"chunk_{win['id']:05d}.json")
                    raw+=f"## {win['start']+origin:.3f}–{win['end']+origin:.3f} 秒\n\n{q['text']}\n\n"
                    text,flags=core_text(q)
                    if needs_asr_review(q['text'],w['text']):flags.append('asr_disagreement')
                    checked+=f"## {win['core_start']+origin:.3f}–{win['core_end']+origin:.3f} 秒\n\n{text}\n\n"
                    if flags:checked+='待复核：'+', '.join(flags)+'。\n\nWhisper 候选：'+w['text']+'\n\n'
                atomic_text(out/'audio_stage_raw.md',raw)
                atomic_text(out/'audio_stage_checked.md',checked)
                write_json(out/'partial_manifest.json',dict(state='asr_complete_visual_pending',source=source,
                           audio=ainfo,windows=len(windows),review_windows=review_windows,keyframes=len(frames),
                           not_completed=['OCR','visual_description','document_OCR','fusion','full_pilot_review']))
                state.set(source,fingerprint,'asr_complete_visual_pending')
                return out
            for stage in ('ocr','document','mineru','visual'):
                state.set(source,fingerprint,stage)
                worker(stage,{**base,'output':str(out/'evidence'/stage)},work,args.ocr_python,
                       getattr(args,'visual_python',None),getattr(args,'mineru_python',None))
            (out/'preparation_status.json').unlink(missing_ok=True)
            for name in ['partial_manifest.json','audio_stage_raw.md','audio_stage_checked.md']:
                (out/name).unlink(missing_ok=True)
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
    s.add_argument('--visual-python')
    s.add_argument('--mineru-python')
    s.add_argument('--ocr-engine',choices=['paddle','onnx'],default='paddle')
    s.add_argument('--ignore-regions',type=json.loads,default=[])
    s.add_argument('--prepare-only',action='store_true')
    s.add_argument('--asr-only',action='store_true',help='Checkpoint complete speech passes and reviews; do not claim full lesson completion')
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
    print(json.dumps({'output':str(out),'prepare_only':args.prepare_only,'asr_only':args.asr_only},ensure_ascii=False))


if __name__=='__main__':
    main()
