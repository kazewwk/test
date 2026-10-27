"""Publish one completed lesson from an isolated sparse checkout; verify every blob."""
from __future__ import annotations
import hashlib
import os
import json
import shutil
import subprocess
from pathlib import Path
from .common import run as common_run, load, write_json, utcnow
from .fusion import validate_lesson


def git_blob_sha(path):
    data=Path(path).read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()


def publish_lesson(lesson, checkout, repository='kazewwk/test', branch='main', *, public_authorized=False,
                   max_lesson_bytes=512*1024**2, series_files=(), catalog_files=()):
    env=os.environ.copy()
    token_file=env.pop('NCE_GITHUB_TOKEN_FILE',None)
    if token_file:
        env['GH_TOKEN']=Path(token_file).read_text().strip()
    def run(argv,**kwargs):return common_run(argv,env=env,**kwargs)
    lesson=Path(lesson).resolve()
    errors=validate_lesson(lesson)
    if errors:
        raise ValueError('Unvalidated lesson: '+', '.join(errors))
    meta=json.loads(run(['gh','api',f'repos/{repository}']))
    if meta.get('private') is False and not public_authorized:
        raise PermissionError('Public full-content publication requires recorded user authorization')
    files=[p for p in lesson.rglob('*') if p.is_file()]
    if sum(p.stat().st_size for p in files)>max_lesson_bytes:
        raise ValueError('Lesson exceeds repository size budget; inspect image sampling before publication')
    if any(p.stat().st_size>=90*1024**2 for p in files):
        raise ValueError('Large artifact requires an explicitly configured LFS/storage delivery path')
    if any(p.suffix.lower() in ('.mp4','.mkv','.wav','.conf','.sqlite') for p in files):
        raise ValueError('Original media or private state in delivery directory')
    source=load(lesson/'manifest.json')['source']
    rel=Path('courses')/source['series']/source['directory']
    checkout=Path(checkout).resolve()
    if not (checkout/'.git').exists():
        run(['git','clone','--filter=blob:none','--no-checkout','--depth','1','--branch',branch,
             f'https://github.com/{repository}.git',checkout])
        patterns=['/courses/_pipeline/','/courses/inventory.json','/courses/*.md',
                  '/courses/*/*.md','/courses/*/quality_summary.json',
                  '/courses/*/*/manifest.json','/courses/*/*/qc_report.json']
        run(['git','-C',checkout,'sparse-checkout','set','--no-cone',*patterns])
        run(['git','-C',checkout,'checkout',branch])
    if run(['git','-C',checkout,'status','--porcelain']).strip():
        raise RuntimeError('Publishing checkout has uncommitted changes; preserve and inspect it')
    run(['git','-C',checkout,'pull','--ff-only','origin',branch])
    source=load(lesson/'manifest.json')['source']
    rel=Path('courses')/source['series']/source['directory']
    delivery={str(rel/p.relative_to(lesson)):p for p in files}
    for p in series_files:
        p=Path(p).resolve()
        if p.parent!=lesson.parent or p.name not in ['README.md','index.md','quality_summary.json']:
            raise ValueError('Unexpected series index path')
        delivery[str(Path('courses')/source['series']/p.name)]=p
    for p in catalog_files:
        p=Path(p).resolve()
        if p.parent!=lesson.parent.parent or p.name not in ('README.md','processing_status.json'):
            raise ValueError('Unexpected catalog path')
        delivery[str(Path('courses')/p.name)]=p
    pattern='/'+''.join('\\'+c if c in '*?[]!' else c for c in str(rel))+'/'
    run(['git','-C',checkout,'sparse-checkout','add','--no-cone',pattern])
    run(['git','-C',checkout,'config','user.name','kazewwk'])
    run(['git','-C',checkout,'config','user.email','127607618+kazewwk@users.noreply.github.com'])
    if token_file:run(['gh','auth','setup-git','--hostname','github.com'])
    target=checkout/rel
    target.mkdir(parents=True,exist_ok=True)
    for name,p in delivery.items():
        dest=checkout/name
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,dest)
    run(['git','-C',checkout,'add','--',*delivery])
    if run(['git','-C',checkout,'diff','--cached','--name-only']).strip():
        run(['git','-C',checkout,'commit','-m',f"courses: extract {source['series']} / {source['title']}"])
        # Never force push; a concurrent update is rebased or reported.
        try:
            run(['git','-C',checkout,'push','origin',branch])
        except subprocess.CalledProcessError:
            run(['git','-C',checkout,'pull','--rebase','origin',branch])
            run(['git','-C',checkout,'push','origin',branch])
    commit=run(['git','-C',checkout,'rev-parse','HEAD']).strip()
    remote=run(['git','ls-remote',f'https://github.com/{repository}.git',f'refs/heads/{branch}']).split()[0]
    if remote!=commit:
        # Another commit can have landed after ours; ensure ours remains an ancestor.
        run(['git','-C',checkout,'fetch','origin',branch])
        run(['git','-C',checkout,'merge-base','--is-ancestor',commit,f'origin/{branch}'])
    # The remote commit's content-addressed tree must match each local delivery byte stream.
    run(['git','-C',checkout,'fetch','origin',commit])
    listing=run(['git','-C',checkout,'ls-tree','-rz','--full-tree',commit,'--',Path('courses')])
    blobs={}
    for row in listing.split('\0'):
        if row:
            info,path=row.split('\t',1)
            blobs[path]=info.split()[2]
    for path,p in delivery.items():
        if blobs.get(path)!=git_blob_sha(p):
            raise RuntimeError('Remote blob mismatch: '+path)
    return dict(commit=commit,url=f'https://github.com/{repository}/tree/{commit}/{rel}',
                source_drive_file_id=source['drive_file_id'],source_video_sha256=source['video_sha256'],source_drive_md5=source.get('drive_md5'),
                verified_files=len(delivery),verified_bytes=sum(p.stat().st_size for p in delivery.values()),
                verification='Every remote Git blob SHA checked against local bytes',time=utcnow())
