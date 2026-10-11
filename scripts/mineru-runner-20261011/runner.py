"""Prepare source pages, resume one chapter, or assemble and publish both completed books."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / 'work'))
import checkpoint

def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        while data := stream.read(1024 * 1024):
            digest.update(data)
    return digest.hexdigest()

def prepare():
    (ROOT / 'sources').mkdir(exist_ok=True)
    (ROOT / 'output').mkdir(exist_ok=True)
    (ROOT / 'work/inputs').mkdir(exist_ok=True)
    (ROOT / 'work/states').mkdir(exist_ok=True)
    manifest = json.loads((ROOT / 'work/source-manifest.json').read_text())
    for bid, spec in enumerate(manifest['books']):
        target = ROOT / 'sources' / f'book{bid}.pdf'
        if target.exists() and target.stat().st_size == spec['size'] and sha(target) == spec['sha256']:
            continue
        temporary = target.with_suffix('.tmp')
        with temporary.open('wb') as output:
            for part in spec['files']:
                path = '王金发细胞/' + part['path']
                url = f'https://raw.githubusercontent.com/{checkpoint.REPO}/{checkpoint.BRANCH}/' + urllib.parse.quote(path, safe='/')
                digest, size = hashlib.sha256(), 0
                with urllib.request.urlopen(url, timeout=180) as response:
                    while data := response.read(1024 * 1024):
                        size += len(data)
                        digest.update(data)
                        output.write(data)
                assert size == part['size'] and digest.hexdigest() == part['sha256'], part['path']
        assert temporary.stat().st_size == spec['size'] and sha(temporary) == spec['sha256']
        temporary.replace(target)
    import pymupdf
    books = json.loads((ROOT / 'work/chapters.json').read_text())
    for book in books:
        with pymupdf.open(ROOT / book['source']) as original:
            assert len(original) == book['page_count']
            coverage = []
            for chapter in book['chapters']:
                key = f"book{book['id']}-{chapter['number']:02}"
                coverage.extend(range(chapter['start'], chapter['end'] + 1))
                wanted = os.environ.get('WORK_CHAPTER')
                if wanted and key != wanted:
                    continue
                dest = ROOT / 'work/inputs' / (key + '.pdf')
                if not dest.exists():
                    with pymupdf.open() as split:
                        split.insert_pdf(original, from_page=chapter['start'] - 1, to_page=chapter['end'] - 1)
                        split.save(dest, garbage=4, deflate=True)
            assert coverage == list(range(1, book['page_count'] + 1))

def parse_chapter():
    prepare()
    checkpoint.restore()
    for attempt in range(3):
        for lock in (ROOT / 'work/states').glob('*.lock'):
            shutil.rmtree(lock)
        if attempt:
            (ROOT / 'work/engine-slots.json').write_text(json.dumps({'n_parallel': 1}))
        result = subprocess.run([sys.executable, '-u', 'work/parse_books.py', '--worker', '0'])
        if result.returncode == 0:
            marker = ROOT / 'work/states' / (os.environ['WORK_CHAPTER'] + '.done.json')
            assert marker.exists()
            return
    raise RuntimeError('Chapter failed after three attempts; committed batches remain resumable')

def finish():
    prepare()
    checkpoint.restore(all_chapters=True)
    books = json.loads((ROOT / 'work/chapters.json').read_text())
    for book in books:
        for chapter in book['chapters']:
            key = f"book{book['id']}-{chapter['number']:02}"
            dest = ROOT / 'output' / book['title'] / chapter['name']
            for start in range(1, chapter['page_count'] + 1, 4):
                end = min(start + 3, chapter['page_count'])
                batch = dest / '解析批次' / f'pages_{start:04}-{end:04}'
                marker = json.loads((batch / 'complete.json').read_text())
                assert marker['chapter_pages'] == [start, end]
                assert marker['source_pdf_pages'] == [chapter['start'] + start - 1, chapter['start'] + end - 1]
            source = ROOT / 'work/inputs' / (key + '.pdf')
            shutil.copyfile(source, dest / '原始页面.pdf')
            info = dict(chapter, title=book['title'], source_sha256=sha(source),
                        validation='All expected durable four-page batches restored; no manual page review')
            for path in [dest / '章节信息.json', ROOT / 'work/states' / (key + '.done.json')]:
                path.write_text(json.dumps(info, ensure_ascii=False, indent=2))
    subprocess.run([sys.executable, '-u', 'work/preserve_sources.py'], check=True)
    subprocess.run([sys.executable, '-u', 'work/finalize_books.py'], check=True)
    subprocess.run([sys.executable, '-u', 'work/publish_books.py'], check=True)

if __name__ == '__main__':
    {'prepare': prepare, 'parse': parse_chapter, 'finish': finish}[sys.argv[1]]()
