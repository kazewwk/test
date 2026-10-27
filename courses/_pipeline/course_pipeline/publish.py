"""Publish a completed lesson in bounded pushes; main changes only after all files are present."""
from __future__ import annotations
from urllib.parse import quote
import hashlib,os,json,shutil,subprocess,tempfile,uuid
from pathlib import Path
from .common import run as common_run,load,utcnow,retry
from .fusion import validate_lesson


def git_blob_sha(path):
    path=Path(path);h=hashlib.sha1(f'blob {path.stat().st_size}\0'.encode())
    with path.open('rb') as f:
        for block in iter(lambda:f.read(8*1024**2),b''):h.update(block)
    return h.hexdigest()


def publish_lesson(lesson,checkout,repository='kazewwk/test',branch='main',*,public_authorized=False,
                   max_push_bytes=512*1024**2,series_files=(),catalog_files=()):
    env=os.environ.copy();token_file=env.pop('NCE_GITHUB_TOKEN_FILE',None)
    if token_file:env['GH_TOKEN']=Path(token_file).read_text().strip()
    def run(argv,**kwargs):return common_run(argv,env=env,**kwargs)
    lesson=Path(lesson).resolve();errors=validate_lesson(lesson)
    if errors:raise ValueError('Unvalidated lesson: '+', '.join(errors))
    meta=json.loads(run(['gh','api',f'repos/{repository}']))
    if meta.get('private') is False and not public_authorized:raise PermissionError('Recorded public-content authorization required')
    files=[p for p in lesson.rglob('*') if p.is_file()]
    if any(p.stat().st_size>=90*1024**2 for p in files):raise ValueError('Individual large artifact needs LFS/storage configuration')
    forbidden={'.mp4','.mkv','.mov','.avi','.webm','.wav','.mp3','.m4a','.flac','.ogg','.opus','.conf','.sqlite'}
    if any(p.suffix.lower() in forbidden for p in files):raise ValueError('Original media or credentials in delivery directory')
    source=load(lesson/'manifest.json')['source'];rel=Path('courses')/source['series']/source['directory']
    delivery={str(rel/p.relative_to(lesson)):p for p in files}
    for p in series_files:
        p=Path(p).resolve()
        if p.parent!=lesson.parent or p.name not in ('README.md','index.md','quality_summary.json'):raise ValueError('Unexpected series index')
        delivery[str(Path('courses')/source['series']/p.name)]=p
    for p in catalog_files:
        p=Path(p).resolve()
        if p.parent!=lesson.parent.parent or p.name not in ('README.md','processing_status.json'):raise ValueError('Unexpected catalog')
        delivery[str(Path('courses')/p.name)]=p
    checkout=Path(checkout).resolve()
    if not (checkout/'.git').exists():
        run(['git','clone','--filter=blob:none','--no-checkout','--depth','1','--branch',branch,f'https://github.com/{repository}.git',checkout])
        run(['git','-C',checkout,'sparse-checkout','set','--no-cone','/courses/_pipeline/','/courses/inventory.json',
             '/courses/processing_status.json','/courses/*.md','/courses/*/*.md','/courses/*/quality_summary.json',
             '/courses/*/*/manifest.json','/courses/*/*/qc_report.json'])
        run(['git','-C',checkout,'checkout',branch])
        (checkout/'.git/course_pipeline_owned').write_text('Temporary publishing checkout created by this pipeline\n')
    if run(['git','-C',checkout,'status','--porcelain']).strip():raise RuntimeError('Preserve and inspect dirty publishing checkout')
    run(['git','-C',checkout,'pull','--ff-only','origin',branch])
    run(['git','-C',checkout,'sparse-checkout','add','--no-cone','/'+''.join('\\'+c if c in '*?[]!' else c for c in str(rel))+'/'])
    run(['git','-C',checkout,'config','user.name','kazewwk'])
    run(['git','-C',checkout,'config','user.email','127607618+kazewwk@users.noreply.github.com'])
    if token_file:run(['gh','auth','setup-git','--hostname','github.com'])
    expected={name:git_blob_sha(p) for name,p in delivery.items()}
    unique_bytes={expected[name]:p.stat().st_size for name,p in delivery.items()}
    final_names={'manifest.json','qc_report.json','transcript_raw.md','transcript_checked.md','lecture_full.md','segments.jsonl','subtitles.srt','frames.json'}
    def final(name):return Path(name).parent!=rel or Path(name).name in final_names
    # Only lesson-root manifests and indexes must be delayed. Evidence is uploaded first.
    def last(name):return not name.startswith(str(rel)+'/') or (Path(name).parent==rel and Path(name).name in final_names)
    names=sorted(delivery,key=lambda name:(last(name),name));chunks=[];chunk=[];size=0;seen=set()
    for name in names:
        added=0 if expected[name] in seen else delivery[name].stat().st_size
        if chunk and size+added>max_push_bytes:chunks.append(chunk);chunk=[];size=0
        chunk.append(name);size+=added;seen.add(expected[name])
    if chunk:chunks.append(chunk)
    staging='course-upload-'+source['drive_file_id']+'-'+uuid.uuid4().hex[:8] if len(chunks)>1 else None
    if staging:run(['git','-C',checkout,'checkout','-b',staging])
    for index,chunk in enumerate(chunks):
        for name in chunk:
            dest=checkout/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(delivery[name],dest)
        with tempfile.NamedTemporaryFile(prefix='course-git-paths-',mode='wb') as spec:
            spec.write(b'\0'.join(name.encode() for name in chunk)+b'\0');spec.flush()
            run(['git','--literal-pathspecs','-C',checkout,'add','--sparse','--pathspec-from-file='+spec.name,'--pathspec-file-nul'])
        if run(['git','-C',checkout,'diff','--cached','--name-only']).strip():
            run(['git','-C',checkout,'commit','-m',f"courses: {source['series']} / {source['title']} ({index+1}/{len(chunks)})"])
        if staging:retry(lambda:run(['git','-C',checkout,'push','origin',staging]),tries=3)
    try:run(['git','-C',checkout,'push','origin','HEAD:'+branch])
    except subprocess.CalledProcessError:
        run(['git','-C',checkout,'pull','--rebase','origin',branch]);run(['git','-C',checkout,'push','origin','HEAD:'+branch])
    commit=run(['git','-C',checkout,'rev-parse','HEAD']).strip()
    remote=run(['git','ls-remote',f'https://github.com/{repository}.git',f'refs/heads/{branch}']).split()[0]
    if remote!=commit:
        run(['git','-C',checkout,'fetch','origin',branch]);run(['git','-C',checkout,'merge-base','--is-ancestor',commit,f'origin/{branch}'])
    run(['git','-C',checkout,'fetch','origin',commit])
    blobs={}
    for row in run(['git','-C',checkout,'ls-tree','-rz','--full-tree',commit,'--','courses']).split('\0'):
        if row:
            info,path=row.split('\t',1);blobs[path]=info.split()[2]
    for name,sha in expected.items():
        if blobs.get(name)!=sha:raise RuntimeError('Remote blob mismatch: '+name)
    if staging:run(['git','-C',checkout,'push','origin','--delete',staging])
    return {'commit':commit,'url':f'https://github.com/{repository}/tree/{commit}/{quote(str(rel))}',
            'source_drive_file_id':source['drive_file_id'],'source_video_sha256':source['video_sha256'],'source_drive_md5':source.get('drive_md5'),
            'verified_files':len(delivery),'verified_bytes':sum(p.stat().st_size for p in delivery.values()),
            'unique_content_bytes':sum(unique_bytes.values()),'push_batches':len(chunks),
            'verification':'Every remote Git blob SHA checked against local bytes','time':utcnow()}
