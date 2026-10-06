#!/usr/bin/env python3
"""Publish the prepared books in small, verified, non-force Git pushes."""
import base64
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

from prepare_mineru_books import ROOT, PLAN, fingerprints, prepare_book, write_index, write_json

if os.environ.get('GITHUB_REPOSITORY') != PLAN['repository'] or PLAN['repository'] != 'kazewwk/test':
    raise SystemExit('This import is restricted to kazewwk/test.')
TOKEN = os.environ['GH_TOKEN']
REFERENCE = json.loads((ROOT / 'books/prepared-reference.json').read_text())
EXPECTED = {row['folder']: row for row in REFERENCE['books']}
AUTH = base64.b64encode(('x-access-token:' + TOKEN).encode()).decode()
PUSH_ENV = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='1',
                GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
                GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + AUTH)
PROGRESS = ROOT / 'books/extraction-progress.json'
MAX_BATCH = PLAN['push_batch_max_bytes']
last_push = 0


def git(*args, authenticated=False, capture=False):
    return subprocess.run(['git', *args], cwd=ROOT, env=PUSH_ENV if authenticated else None,
                          check=True, stdout=subprocess.PIPE if capture else None,
                          stderr=subprocess.PIPE if capture else None).stdout


def api(path):
    request = urllib.request.Request('https://api.github.com/repos/' + PLAN['repository'] + path,
                                    headers={'Authorization': 'Bearer ' + TOKEN,
                                             'Accept': 'application/vnd.github+json',
                                             'User-Agent': 'mineru-book-extraction'})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError):
            if attempt == 4:
                raise
            time.sleep(3 * (attempt + 1))


def push():
    global last_push
    time.sleep(max(0, 11 - (time.monotonic() - last_push)))
    for attempt in range(4):
        try:
            git('push', 'origin', 'HEAD:main', authenticated=True)
            last_push = time.monotonic()
            return
        except subprocess.CalledProcessError:
            if attempt == 3:
                raise
            # A non-force rebase preserves intervening work; conflicts stop the import.
            git('fetch', '--quiet', 'origin', 'main', authenticated=True)
            git('rebase', 'origin/main')
            time.sleep(3 * (attempt + 1))


def commit_paths(paths, message):
    with tempfile.NamedTemporaryFile() as pathspec:
        pathspec.write(b'\0'.join((':(literal)' + path).encode() for path in paths) + b'\0')
        pathspec.flush()
        git('add', '-f', '--pathspec-from-file=' + pathspec.name, '--pathspec-file-nul')
    staged = set(git('diff', '--cached', '--name-only', '-z', capture=True).decode().strip('\0').split('\0'))
    staged.discard('')
    if not staged:
        return
    if not staged.issubset(set(paths)):
        raise RuntimeError('Unexpected files in the Git index.')
    git('commit', '--quiet', '-m', message)
    push()


def prepared_folder(book):
    folder = ROOT / '书籍' / book['folder']
    checksum = folder / '仓库文件校验.json'
    if checksum.exists() and fingerprints(checksum) == EXPECTED[book['folder']]['checksum_manifest']:
        report = json.loads(checksum.read_text())
        for row in report['files']:
            if fingerprints(folder / row['path']) != {k: row[k] for k in ['size', 'sha256', 'git_blob_sha1']}:
                raise RuntimeError('Existing book file changed: ' + row['path'])
        return folder
    if folder.exists():
        with tempfile.TemporaryDirectory(prefix='mineru-resume-') as temporary:
            staging = Path(temporary)
            prepare_book(book, staging)
            prepared = staging / book['folder']
            for existing in folder.rglob('*'):
                if existing.is_file():
                    expected = prepared / existing.relative_to(folder)
                    if not expected.is_file() or fingerprints(existing) != fingerprints(expected):
                        raise RuntimeError('Conflicting existing book file: ' + str(existing))
            shutil.copytree(prepared, folder, dirs_exist_ok=True)
    else:
        prepare_book(book, ROOT / '书籍')
    if fingerprints(checksum) != EXPECTED[book['folder']]['checksum_manifest']:
        raise RuntimeError('Prepared book differs from the verified local reference: ' + book['folder'])
    return folder


git('config', 'user.name', 'github-actions[bot]')
git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
git('config', 'gc.auto', '0')
summaries = []
for number, book in enumerate(PLAN['books'], 1):
    print('BOOK_START', number, book['folder'], flush=True)
    folder = prepared_folder(book)
    files = sorted(p for p in folder.rglob('*') if p.is_file())
    batches, batch, size = [], [], 0
    for path in files:
        length = path.stat().st_size
        if length >= PLAN['max_file_bytes_exclusive']:
            raise RuntimeError('Repository file exceeds 100 MB.')
        if batch and (size + length > MAX_BATCH or len(batch) >= 4000):
            batches.append(batch)
            batch, size = [], 0
        batch.append(path.relative_to(ROOT).as_posix())
        size += length
    if batch:
        batches.append(batch)
    summary = EXPECTED[book['folder']]
    for batch_number, paths in enumerate(batches, 1):
        done = batch_number == len(batches)
        completed = summaries + ([summary] if done else [])
        write_json(PROGRESS, {'verified_book_count': len(completed), 'total_books': len(PLAN['books']),
                             'current_book': book['folder'], 'current_batch': batch_number,
                             'total_batches': len(batches), 'completed_books': [b['folder'] for b in completed]})
        commit_paths(paths + ['books/extraction-progress.json'],
                     f'Add extracted {book["folder"]}: batch {batch_number}/{len(batches)}')
        print('BATCH_PUSHED', book['folder'], batch_number, '/', len(batches), flush=True)
    summaries.append(summary)

write_index(ROOT / '书籍', summaries)
commit_paths(['README.md', 'books/extracted-manifest.json'], 'Index thirteen extracted and size-checked MinerU books')
head = git('rev-parse', 'HEAD', capture=True).decode().strip()
verified = []
for book in PLAN['books']:
    folder = ROOT / '书籍' / book['folder']
    tree_sha = git('rev-parse', 'HEAD:书籍/' + book['folder'], capture=True).decode().strip()
    remote = api('/git/trees/' + tree_sha + '?recursive=1')
    if remote.get('truncated'):
        raise RuntimeError('GitHub tree response was truncated.')
    actual = {row['path']: row for row in remote['tree'] if row['type'] == 'blob'}
    report = json.loads((folder / '仓库文件校验.json').read_text())
    expected = {row['path']: row for row in report['files']}
    expected['仓库文件校验.json'] = fingerprints(folder / '仓库文件校验.json')
    if set(actual) != set(expected):
        raise RuntimeError('GitHub book file set differs: ' + book['folder'])
    for name, row in expected.items():
        if actual[name]['sha'] != row['git_blob_sha1'] or actual[name]['size'] != row['size']:
            raise RuntimeError('GitHub blob verification failed: ' + name)
        if actual[name]['size'] >= PLAN['max_file_bytes_exclusive']:
            raise RuntimeError('GitHub contains an oversized file.')
    verified.append({'folder': book['folder'], 'tree_sha': tree_sha, 'file_count': len(actual),
                     'total_bytes': sum(row['size'] for row in actual.values()),
                     'max_file_bytes': max(row['size'] for row in actual.values())})
result = {'repository': PLAN['repository'], 'verified_commit': head, 'verified_book_count': len(verified),
          'total_file_count': sum(row['file_count'] for row in verified),
          'total_bytes': sum(row['total_bytes'] for row in verified),
          'max_file_bytes': max(row['max_file_bytes'] for row in verified), 'books': verified}
write_json(ROOT / 'books/repository-verification.json', result)
write_json(PROGRESS, {'status': 'complete', **result})
commit_paths(['books/repository-verification.json', 'books/extraction-progress.json'],
             'Record GitHub verification for all thirteen extracted books')
print('ALL_BOOKS_VERIFIED', json.dumps(result, ensure_ascii=False), flush=True)
with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
    summary.write(f'13 book folders verified: {result["total_file_count"]:,} files, all below 100 MB.\n')
