import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
import checkpoint as remote

BOOKS = [
    {'directory': '细胞生物学（王金发）', 'pages': 528, 'chapter_count': 15,
     'zip': 'Cell-Biology-Wang-Jinfa-MinerU-Local-Hybrid.zip'},
    {'directory': '细胞生物学实验教程_第2版', 'pages': 265, 'chapter_count': 12,
     'zip': 'Cell-Biology-Laboratory-2e-MinerU-Local-Hybrid.zip'},
]
STATUS = ROOT / 'work/task-status.json'

def update(**values):
    obj = json.loads(STATUS.read_text()) if STATUS.exists() else {}
    obj.update(values, updated_at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    remote.atomic(STATUS, obj)

def active():
    ids = []
    for path in Path('/proc').glob('[0-9]*'):
        try:
            args = (path / 'cmdline').read_bytes().split(b'\0')
            if b'work/parse_books.py' in args and b'--worker' in args:
                ids.append(path)
        except OSError:
            pass
    return ids

def wait_parse():
    restarted = 0
    while True:
        completed = len(list((ROOT / 'work/states').glob('*.done.json')))
        update(phase='parsing', completed_folders=completed, total_folders=33)
        if completed == 33:
            return
        running = active()
        for process in running:
            try:
                (process / 'oom_score_adj').write_text('1000')
            except OSError:
                pass
        if not running:
            if restarted >= 8:
                raise RuntimeError('Parsing stopped repeatedly; completed batches are saved on GitHub')
            for directory in (ROOT / 'work/states').glob('*.lock'):
                shutil.rmtree(directory)
            remote.atomic(ROOT / 'work/engine-slots.json', {'n_parallel': 1})
            env = dict(os.environ, MINERU_MODEL_BASE_DIR=str(ROOT / 'work/models'), PYTHONFAULTHANDLER='1')
            output = (ROOT / 'logs/worker-recovery.log').open('ab')
            subprocess.Popen([str(ROOT / '.mineru/bin/python'), '-u', 'work/parse_books.py', '--worker', '0'],
                             env=env, stdout=output, stderr=subprocess.STDOUT)
            restarted += 1
            update(restarts=restarted)
        time.sleep(15)

def upload_archives():
    remote.STATE = None
    plan = {'tag': 'cell-biology-local-hybrid-2026-10-10-0933c203',
            'title': '王金发细胞生物学与实验教程：本地 MinerU 混合模式分章解析',
            'books': BOOKS, 'archives': []}
    entries = []
    for book in BOOKS:
        path = ROOT / 'output' / book['zip']
        parts = []
        digest = hashlib.sha256()
        size = 0
        with path.open('rb') as stream:
            while data := stream.read(8_000_001):
                digest.update(data)
                size += len(data)
                dest = remote.PREFIX + '/archives/' + book['zip'] + f'.part{len(parts):03}'
                item = remote.entry(dest, data)
                entries.append(item)
                parts.append({'sha': item['sha'], 'size': len(data)})
                update(phase='uploading', current_book=book['directory'], uploaded_bytes=size,
                       total_bytes=path.stat().st_size)
        plan['archives'].append({'directory': book['directory'], 'zip': book['zip'],
                                 'size': size, 'sha256': digest.hexdigest(), 'parts': parts})
    path = ROOT / 'work/publication.json'
    remote.atomic(path, plan)
    entries.append(remote.entry('scripts/local-mineru-20261011/publication.json', path.read_bytes()))
    saved = remote.commit(entries, 'Save both complete local MinerU ZIP archives')
    remote.update_status('parsed_archives_ready', archives_commit=saved)
    return plan

def publish(plan):
    entries = []
    for source, target in [
        ('publish_action.py', 'scripts/local-mineru-20261011/publish_action.py'),
        ('publication.json', 'scripts/local-mineru-20261011/publication.json'),
        ('publish_local_books.yml', '.github/workflows/publish-local-cell-books.yml'),
    ]:
        entries.append(remote.entry(target, (ROOT / 'work' / source).read_bytes()))
    commit = remote.commit(entries, 'Publish complete locally parsed Wang Jinfa cell biology books', branch='main')
    update(phase='github_packaging', commit=commit)
    return commit

def verify(commit, plan):
    run = None
    for _ in range(540):
        try:
            result = remote.fetch(f'https://api.github.com/repos/{remote.REPO}/actions/workflows/publish-local-cell-books.yml/runs?branch=main&per_page=20')
            run = next((r for r in result.get('workflow_runs', []) if r['head_sha'] == commit), None)
        except Exception:
            run = None
        if run:
            update(workflow_url=run['html_url'], workflow_status=run['status'], workflow_conclusion=run.get('conclusion'))
            if run['status'] == 'completed':
                assert run['conclusion'] == 'success', f'Publishing failed: {run["html_url"]}'
                break
        time.sleep(20)
    else:
        raise RuntimeError('Publishing did not finish within the monitoring window')
    release = remote.fetch(f'https://api.github.com/repos/{remote.REPO}/releases/tags/{plan["tag"]}')
    for spec in plan['archives']:
        asset = next(a for a in release['assets'] if a['name'] == spec['zip'])
        assert asset['state'] == 'uploaded' and asset['size'] == spec['size']
        assert asset['digest'] == 'sha256:' + spec['sha256']
    remote.atomic(ROOT / 'work/release-verification.json', release)
    update(phase='github_published', release_url=release['html_url'])
    return release

def save_downloads():
    update(phase='saving_downloads')
    announcement = ROOT / 'work/saving-announced.json'
    for _ in range(120):
        if announcement.exists():
            break
        time.sleep(1)
    request = {'uploads': [{'local_path': str(ROOT / 'output' / b['zip']),
                            'purpose': 'create_library_file', 'library_artifact_type': 'other'}
                           for b in BOOKS]}
    output = subprocess.check_output(['python3', str(ROOT / 'work/library-helper-20261011/library_upload.py')],
                                     input=json.dumps(request).encode(), stderr=subprocess.STDOUT)
    (ROOT / 'work/saved-downloads.json').write_bytes(output)
    results = json.loads(output).get('results', [])
    assert len(results) == 2 and all(r.get('status') == 'succeeded' for r in results)
    update(downloads_saved=True)

if __name__ == '__main__':
    try:
        wait_parse()
        update(phase='validating')
        subprocess.run([str(ROOT / '.mineru/bin/python'), 'work/finalize_books.py'], check=True)
        assert all((ROOT / 'output' / b['zip']).is_file() for b in BOOKS)
        plan = upload_archives()
        commit = publish(plan)
        release = verify(commit, plan)
        save_downloads()
        remote.update_status('complete', release_url=release['html_url'])
        update(phase='complete', release_url=release['html_url'])
        print('COMPLETE', release['html_url'], flush=True)
    except Exception as exc:
        import traceback
        traceback.print_exc()
        update(phase='failed', error=str(exc))
        raise
