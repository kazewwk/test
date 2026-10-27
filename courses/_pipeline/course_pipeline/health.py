"""Read actual worker identities and completed artifacts, independently of status heartbeats."""
from pathlib import Path
import json,time


def read_json(path):
    try:return json.loads(Path(path).read_text())
    except (OSError,ValueError):return None


def process_identity(pid):
    try:
        stat=(Path('/proc')/str(int(pid))/'stat').read_text().rsplit(')',1)[1].split()
        command=(Path('/proc')/str(int(pid))/'cmdline').read_bytes()
        return {'pid':int(pid),'alive':bool(command) and stat[0]!='Z','start_ticks':int(stat[19])}
    except (OSError,ValueError,IndexError,TypeError):return {'pid':pid,'alive':False}


def inspect_runtime(root):
    b=Path(root);driver_pid=b/'batch_driver.pid'
    pid=driver_pid.read_text().strip() if driver_pid.exists() else None
    driver=process_identity(pid)
    workers=read_json(b/'cache/batch_processes.json') or {}
    result={'batch':read_json(b/'cache/batch_status.json'),'driver':read_json(b/'driver_status.json'),
            'exit':read_json(b/'batch_exit.json'),'driver_exists':driver_pid.exists(),
            'driver_alive':driver['alive'],'driver_identity':driver,
            'workers':{role:process_identity(value) for role,value in workers.items()},
            'gpu_done':read_json(b/'cache/gpu_done.json'),
            'checkpoint':read_json(b/'checkpoint_receipt.json'),'progress':[],'observed_at':time.time()}
    seen=set()
    for state_file in ['cache/gpu_status.json','cache/batch_status.json']:
        state=read_json(b/state_file) or {};source=state.get('source') or {}
        identity=source.get('drive_file_id')
        if not identity or identity in seen:continue
        seen.add(identity)
        lesson=b/'courses'/source['series']/source['directory']
        counts={};latest=0.0
        for stage in ['qwen','whisper','review_qwen','review_whisper','ocr','document','mineru','visual']:
            pattern='*/complete.json' if stage in ('document','mineru') else 'chunk_*.json' if 'qwen' in stage or 'whisper' in stage else '*.json'
            files=list((lesson/'evidence'/stage).glob(pattern));counts[stage]=len(files)
            if stage=='visual':
                records=[read_json(path) or {} for path in files]
                counts['visual']=sum(bool(record.get('model')) and record.get('status')!='not_requested' for record in records)
                counts['visual_not_requested']=sum(record.get('status')=='not_requested' for record in records)
            for path in files:
                try:latest=max(latest,path.stat().st_mtime)
                except OSError:pass
        selection=read_json(lesson/'mineru_selection.json') or {}
        visual_selection=read_json(lesson/'visual_selection.json') or {}
        frames=read_json(lesson/'frames.json') or {}
        result['progress'].append({'drive_file_id':identity,'series':source['series'],'title':source['title'],
                                   'counts':counts,'mineru_selected':selection.get('selected'),
                                   'keyframes':len(frames.get('frames',[])),
                                   'visual_selected':visual_selection.get('selected'),
                                   'latest_artifact_mtime':latest})
    if result.get('checkpoint'):
        result['checkpoint_age_seconds']=max(0,time.time()-result['checkpoint'].get('time',0))
    return result


def progress_signature(status):
    """Ignore polling timestamps; only persisted results and source changes count."""
    return json.dumps({'completed':(status.get('batch') or {}).get('completed'),
                       'progress':status.get('progress',[])},sort_keys=True)


def recovery_reason(status,last_progress_at,now,stall_seconds=1800):
    if status.get('exit'):return 'driver_exit'
    if status.get('driver_exists') and not status.get('driver_alive'):return 'driver_disappeared'
    running=(status.get('driver') or {}).get('state')=='running_batch'
    if running:
        workers={} if (status.get('driver') or {}).get('device')=='cpu' else status.get('workers') or {}
        dead=[role for role,p in workers.items() if not p.get('alive') and not (role=='gpu' and status.get('gpu_done'))]
        if dead and now-(status.get('driver') or {}).get('time',0)>=120:return 'worker_disappeared'
        if status.get('progress') and now-last_progress_at>=stall_seconds:return 'no_artifact_progress'
    return None
