import base64
import hashlib
import io
import json
import os
import sys
import time
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'work/library-helper-20261011'))
from library_hosted_apps import HostedAppsClient

REPO = 'kazewwk/test'
BRANCH = 'mineru-local-wang-jinfa-20261010'
PREFIX = '.local-mineru-checkpoints-20261011'
STATUS_REMOTE = PREFIX + '/status.json'
CLIENT = HostedAppsClient()
CONNECTOR = json.loads((ROOT / 'work/hosted-github-tools.json').read_text())[0]['connector_id']
CACHE_PATH = ROOT / 'work/blob-cache.json'
CACHE = json.loads(CACHE_PATH.read_text()) if CACHE_PATH.exists() else {}
STATE = None
LAST_WRITE = 0.0

def atomic(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2))
    temporary.replace(path)

def payload(result):
    if isinstance(result.get('structuredContent'), dict):
        return result['structuredContent']
    for block in result.get('content', []):
        if block.get('type') == 'text':
            try:
                value = json.loads(block['text'])
                if isinstance(value, dict):
                    return value
            except ValueError:
                pass
    raise RuntimeError('GitHub returned no structured result')

def call(name, arguments):
    global LAST_WRITE
    if name != 'fetch':
        delay = LAST_WRITE + 1.0 - time.monotonic()
        if delay > 0:
            time.sleep(delay)
        LAST_WRITE = time.monotonic()
    for attempt in range(4):
        try:
            return payload(CLIENT.call_tool(CONNECTOR, name, arguments))
        except Exception:
            if attempt == 3:
                raise
            time.sleep(min(5 * 2**attempt, 30))

def fetch(url):
    return json.loads(call('fetch', {'url': url})['content'])

def upload(data):
    expected = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if CACHE.get(expected):
        return expected
    result = call('create_blob', {'repository_full_name': REPO, 'encoding': 'base64',
                                 'content': base64.b64encode(data).decode()})
    assert result['sha'] == expected, 'Blob checksum mismatch'
    CACHE[expected] = True
    atomic(CACHE_PATH, CACHE)
    return expected

def entry(path, data):
    return {'path': path, 'mode': '100644', 'type': 'blob', 'sha': upload(data)}

def commit(entries, message, branch=BRANCH):
    for attempt in range(3):
        ref = fetch(f'https://api.github.com/repos/{REPO}/git/ref/heads/{branch}')
        parent = ref['object']['sha']
        old = fetch(f'https://api.github.com/repos/{REPO}/git/commits/{parent}')
        tree = call('create_tree', {'repository_full_name': REPO, 'base_tree_sha': old['tree']['sha'],
                                    'tree_elements': entries})
        made = call('create_commit', {'repository_full_name': REPO, 'message': message,
                                      'tree_sha': tree['sha'], 'parent_sha': parent})
        try:
            call('update_ref', {'repository_full_name': REPO, 'branch_name': branch,
                                'sha': made['sha'], 'expected_sha': parent, 'force': False})
            return made['sha']
        except Exception:
            if attempt == 2:
                raise
    raise RuntimeError('Unable to save GitHub checkpoint')

def state():
    global STATE
    if STATE is not None:
        return STATE
    try:
        found = fetch(f'https://api.github.com/repos/{REPO}/contents/{STATUS_REMOTE}?ref={BRANCH}')
        if 'checkpoints' in found:
            STATE = found
        elif 'content' in found:
            STATE = json.loads(base64.b64decode(found['content']))
        else:
            raise RuntimeError('Unknown checkpoint response')
    except Exception:
        raise
    return STATE

def status_bytes():
    obj = state()
    counts = [0, 0]
    for item in obj['checkpoints'].values():
        counts[item['book_id']] += item['pages']
    obj['completed_pages'] = counts
    obj['updated_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    atomic(ROOT / 'work/durable-status.json', obj)
    return json.dumps(obj, ensure_ascii=False, indent=2).encode()

def sync_batch(batch):
    batch = Path(batch)
    marker = json.loads((batch / 'complete.json').read_text())
    key = batch.relative_to(ROOT / 'output').as_posix()
    obj = state()
    if key in obj['checkpoints']:
        return
    books = json.loads((ROOT / 'work/chapters.json').read_text())
    book_id = next(b['id'] for b in books if b['title'] == marker['book'])
    blob = io.BytesIO()
    with zipfile.ZipFile(blob, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for path in sorted(batch.rglob('*')):
            if path.is_file():
                bundle.write(path, arcname=path.relative_to(ROOT / 'output').as_posix())
    data = blob.getvalue()
    chapter_id = marker['chapter'].split('_', 1)[0]
    remote = f'{PREFIX}/book{book_id}/{chapter_id}/{batch.name}'
    parts = []
    entries = []
    for offset in range(0, len(data), 8_000_001):
        part = data[offset:offset + 8_000_001]
        path = remote + f'.zip.part{len(parts):03}'
        item = entry(path, part)
        entries.append(item)
        parts.append({'path': path, 'sha': item['sha'], 'size': len(part)})
    obj['checkpoints'][key] = {'book_id': book_id,
        'pages': marker['chapter_pages'][1] - marker['chapter_pages'][0] + 1,
        'source_pdf_pages': marker['source_pdf_pages'], 'size': len(data),
        'sha256': hashlib.sha256(data).hexdigest(), 'parts': parts}
    entries.append(entry(STATUS_REMOTE, status_bytes()))
    try:
        saved = commit(entries, f'Save local MinerU checkpoint: book{book_id} {chapter_id} {batch.name}')
    except Exception:
        obj['checkpoints'].pop(key, None)
        raise
    print('DURABLE CHECKPOINT', key, saved, flush=True)

def update_status(phase='parsing', **extra):
    obj = state()
    obj.update(extra, phase=phase)
    return commit([entry(STATUS_REMOTE, status_bytes())], 'Update local MinerU progress')

def restore():
    obj = state()
    for key, item in obj['checkpoints'].items():
        batch = ROOT / 'output' / key
        if (batch / 'complete.json').exists():
            continue
        archive = bytearray()
        for part in item['parts']:
            url = f'https://raw.githubusercontent.com/{REPO}/{BRANCH}/{part["path"]}'
            with urllib.request.urlopen(url, timeout=45) as response:
                data = response.read()
            assert len(data) == part['size']
            assert hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == part['sha']
            archive.extend(data)
        assert len(archive) == item['size'] and hashlib.sha256(archive).hexdigest() == item['sha256']
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            assert bundle.testzip() is None
            for member in bundle.infolist():
                target = ROOT / 'output' / member.filename
                assert target.resolve().is_relative_to((ROOT / 'output').resolve())
                if not member.is_dir():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(bundle.read(member))
    atomic(ROOT / 'work/durable-status.json', obj)
    print('RESTORED DURABLE PAGES', obj['completed_pages'], flush=True)

if __name__ == '__main__':
    if sys.argv[1] == 'restore':
        restore()
    elif sys.argv[1] == 'save-code':
        names = ['parse_books.py', 'finalize_books.py', 'checkpoint.py', 'chapters.json']
        entries = [entry('scripts/local-mineru-20261011/' + name, (ROOT / 'work' / name).read_bytes())
                   for name in names]
        entries.append(entry(STATUS_REMOTE, status_bytes()))
        print('SAVED RECOVERY CODE', commit(entries, 'Prepare durable local MinerU parsing checkpoints'), flush=True)
