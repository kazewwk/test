"""Publish one completed lesson from an isolated sparse checkout; verify every blob."""
from __future__ import annotations
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from .common import run, load, write_json, utcnow
from .fusion import validate_lesson


def git_blob_sha(path):
    data=Path(path).read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()


def publish_lesson(lesson, checkout, repository='kazewwk/test', branch='main', *, public_authorized=False,
                   max_lesson_bytes=512*1024**2):
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
    checkout=Path(checkout).resolve()
    if not (checkout/'.git').exists():
        run(['git','clone','--filter=blob:none','--no-checkout','--depth','1','--branch',branch,
             f'https://github.com/{repository}.git',checkout])
        run(['git','-C',checkout,'sparse-checkout','set','courses'])
        run(['git','-C',checkout,'checkout',branch])
    if run(['git','-C',checkout,'status','--porcelain']).strip():
        raise RuntimeError('Publishing checkout has uncommitted changes; preserve and inspect it')
    run(['git','-C',checkout,'pull','--ff-only','origin',branch])
    source=load(lesson/'manifest.json')['source']
    rel=Path('courses')/source['series']/source['directory']
    target=checkout/rel
    target.mkdir(parents=True,exist_ok=True)
    for p in files:
        dest=target/p.relative_to(lesson)
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,dest)
    run(['git','-C',checkout,'add','--',rel])
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
    listing=run(['git','-C',checkout,'ls-tree','-rz','--full-tree',commit,'--',rel])
    blobs={}
    for row in listing.split('\0'):
        if row:
            info,path=row.split('\t',1)
            blobs[path]=info.split()[2]
    for p in files:
        path=str(rel/p.relative_to(lesson))
        if blobs.get(path)!=git_blob_sha(p):
            raise RuntimeError('Remote blob mismatch: '+path)
    return dict(commit=commit,url=f'https://github.com/{repository}/tree/{commit}/{rel}',
                verified_files=len(files),verified_bytes=sum(p.stat().st_size for p in files),
                verification='Every remote Git blob SHA checked against local bytes',time=utcnow())
