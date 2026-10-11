"""Native GitHub checkpoints for one chapter per Actions job; no hosted parsing API."""
import base64
import hashlib
import io
import json
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = os.environ.get('GITHUB_REPOSITORY', 'kazewwk/test')
BRANCH = 'mineru-local-wang-jinfa-20261010'
PREFIX = '.local-mineru-checkpoints-20261011'
STATE = None

def api(path, data=None, method=None, missing=False):
    url = 'https://api.github.com/repos/' + REPO + '/' + path
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'mineru-chapter-checkpoint',
               'Authorization': 'Bearer ' + os.environ['GH_TOKEN']}
    body = None if data is None else json.dumps(data).encode()
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code == 404 and missing:
                return None
            if exc.code not in (429, 500, 502, 503, 504) and not (exc.code == 403 and exc.headers.get('Retry-After')):
                raise
            if attempt == 4:
                raise
            time.sleep(min(int(exc.headers.get('Retry-After', 5 * 2**attempt)), 60))
    raise RuntimeError('GitHub request retries exhausted')

def raw(path):
    url = f'https://raw.githubusercontent.com/{REPO}/{BRANCH}/' + urllib.parse.quote(path, safe='/')
    with urllib.request.urlopen(url, timeout=120) as response:
        return response.read()

def read_json(path, missing=False):
    result = api('contents/' + urllib.parse.quote(path, safe='/') + '?ref=' + BRANCH, missing=missing)
    return None if result is None else json.loads(base64.b64decode(result['content']))

def git_hash(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def entry(path, data):
    result = api('git/blobs', {'content': base64.b64encode(data).decode(), 'encoding': 'base64'})
    assert result['sha'] == git_hash(data)
    return {'path': path, 'mode': '100644', 'type': 'blob', 'sha': result['sha']}

def commit(entries, message):
    # Each worker modifies only its own chapter metadata; branch CAS never replaces another worker's status.
    for attempt in range(12):
        parent = api('git/ref/heads/' + BRANCH)['object']['sha']
        old_tree = api('git/commits/' + parent)['tree']['sha']
        tree = api('git/trees', {'base_tree': old_tree, 'tree': entries})['sha']
        made = api('git/commits', {'message': message, 'tree': tree, 'parents': [parent]})['sha']
        try:
            api('git/refs/heads/' + BRANCH, {'sha': made, 'force': False}, method='PATCH')
            return made
        except urllib.error.HTTPError as exc:
            if exc.code not in (409, 422) or attempt == 11:
                raise
            time.sleep(random.uniform(1, 5))
    raise RuntimeError('Unable to fast-forward checkpoint branch')

def own_path(key=None):
    key = key or os.environ['WORK_CHAPTER']
    return f'{PREFIX}/runner-status/{key}.json'

def state():
    global STATE
    if STATE is None:
        legacy = read_json(PREFIX + '/status.json')
        STATE = {'checkpoints': dict(legacy['checkpoints'])}
        own = read_json(own_path(), missing=True)
        if own:
            STATE.update(own)
            STATE['checkpoints'] = dict(legacy['checkpoints']) | own['checkpoints']
    return STATE

def save(entries, phase='parsing'):
    obj = state()
    wanted = os.environ['WORK_CHAPTER']
    bid, number = wanted[4:].split('-')
    chapters = json.loads((ROOT / 'work/chapters.json').read_text())
    book = next(b for b in chapters if b['id'] == int(bid))
    chapter = next(c for c in book['chapters'] if c['number'] == int(number))
    prefix = book['title'] + '/' + chapter['name'] + '/'
    own = {'chapter_key': wanted, 'phase': phase,
           'updated_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           'checkpoints': {k: v for k, v in obj['checkpoints'].items() if k.startswith(prefix)}}
    own['completed_pages'] = sum(x['pages'] for x in own['checkpoints'].values())
    marker = ROOT / 'work/states' / (wanted + '.done.json')
    if marker.exists():
        own['chapter_info'] = json.loads(marker.read_text())
    entries.append(entry(own_path(), json.dumps(own, ensure_ascii=False, indent=2).encode()))
    return commit(entries, 'Save MinerU runner chapter checkpoint: ' + wanted)

def sync_batch(batch):
    batch = Path(batch)
    key = batch.relative_to(ROOT / 'output').as_posix()
    obj = state()
    if key in obj['checkpoints']:
        return
    marker = json.loads((batch / 'complete.json').read_text())
    books = json.loads((ROOT / 'work/chapters.json').read_text())
    bid = next(b['id'] for b in books if b['title'] == marker['book'])
    packed = io.BytesIO()
    with zipfile.ZipFile(packed, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for path in sorted(batch.rglob('*')):
            if path.is_file():
                bundle.write(path, path.relative_to(ROOT / 'output').as_posix())
    data = packed.getvalue()
    chapter_id = marker['chapter'].split('_', 1)[0]
    base = f'{PREFIX}/book{bid}/{chapter_id}/{batch.name}.zip'
    parts, entries = [], []
    for offset in range(0, len(data), 8_000_001):
        part = data[offset:offset + 8_000_001]
        path = base + f'.part{len(parts):03}'
        item = entry(path, part)
        entries.append(item)
        parts.append({'path': path, 'sha': item['sha'], 'size': len(part)})
    obj['checkpoints'][key] = {'book_id': bid, 'pages': marker['chapter_pages'][1] - marker['chapter_pages'][0] + 1,
        'source_pdf_pages': marker['source_pdf_pages'], 'size': len(data),
        'sha256': hashlib.sha256(data).hexdigest(), 'parts': parts}
    try:
        saved = save(entries)
    except Exception:
        obj['checkpoints'].pop(key, None)
        raise
    print('DURABLE RUNNER CHECKPOINT', key, saved, flush=True)

def update_status(phase='parsing', **extra):
    return save([], 'chapter_complete' if (ROOT / 'work/states' / (os.environ['WORK_CHAPTER'] + '.done.json')).exists() else phase)

def restore_item(key, item):
    batch = ROOT / 'output' / key
    if (batch / 'complete.json').exists():
        return
    packed = bytearray()
    for part in item['parts']:
        data = raw(part['path'])
        assert len(data) == part['size'] and git_hash(data) == part['sha']
        packed.extend(data)
    assert len(packed) == item['size'] and hashlib.sha256(packed).hexdigest() == item['sha256']
    with zipfile.ZipFile(io.BytesIO(packed)) as bundle:
        assert bundle.testzip() is None
        for member in bundle.infolist():
            target = ROOT / 'output' / member.filename
            assert target.resolve().is_relative_to((ROOT / 'output').resolve())
            if not member.is_dir():
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(bundle.read(member))

def restore(all_chapters=False):
    legacy = read_json(PREFIX + '/status.json')
    items = dict(legacy['checkpoints'])
    books = json.loads((ROOT / 'work/chapters.json').read_text())
    for book in books:
        for chapter in book['chapters']:
            key = f"book{book['id']}-{chapter['number']:02}"
            if not all_chapters and key != os.environ['WORK_CHAPTER']:
                continue
            own = read_json(own_path(key), missing=True)
            if own:
                items.update(own['checkpoints'])
    if not all_chapters:
        bid, number = os.environ['WORK_CHAPTER'][4:].split('-')
        book = next(b for b in books if b['id'] == int(bid))
        chapter = next(c for c in book['chapters'] if c['number'] == int(number))
        prefix = book['title'] + '/' + chapter['name'] + '/'
        items = {k: v for k, v in items.items() if k.startswith(prefix)}
    for key, item in items.items():
        restore_item(key, item)
    (ROOT / 'work/restored-checkpoints.json').write_text(json.dumps(items, ensure_ascii=False, indent=2))
    print('RESTORED PAGES', sum(x['pages'] for x in items.values()), flush=True)
