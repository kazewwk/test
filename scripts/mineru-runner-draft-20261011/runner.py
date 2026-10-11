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
    subprocess.run([sys.executable, '-u', 'work/finalize_books.py'], check=True)
    publish(books)

def split_large_files(root):
    oversized = [p for p in sorted(root.rglob('*')) if p.is_file() and p.stat().st_size >= 100_000_000]
    if not oversized:
        return
    records = []
    for path in oversized:
        relative = path.relative_to(root).as_posix()
        info = {'path': relative, 'size': path.stat().st_size, 'sha256': sha(path), 'parts': []}
        folder = path.with_name(path.name + '.parts')
        folder.mkdir()
        with path.open('rb') as stream:
            while data := stream.read(95_000_000):
                part = folder / f"part{len(info['parts'])+1:03}"
                part.write_bytes(data)
                info['parts'].append({'path': part.relative_to(root).as_posix(), 'size': len(data), 'sha256': sha(part)})
        path.unlink()
        records.append(info)
    (root / '大文件分卷.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
    helper = """import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
for item in json.loads((root/'大文件分卷.json').read_text()):
    dest=root/item['path']
    assert dest.resolve().is_relative_to(root.resolve())
    temporary=dest.with_name(dest.name+'.restoring')
    digest=hashlib.sha256()
    size=0
    with temporary.open('wb') as output:
        for spec in item['parts']:
            part=root/spec['path']
            assert part.resolve().is_relative_to(root.resolve())
            data=part.read_bytes()
            assert len(data)==spec['size'] and hashlib.sha256(data).hexdigest()==spec['sha256']
            output.write(data)
            digest.update(data)
            size+=len(data)
    assert size==item['size'] and digest.hexdigest()==item['sha256']
    if dest.exists():
        assert hashlib.sha256(dest.read_bytes()).hexdigest()==item['sha256']
        temporary.unlink()
    else:
        temporary.replace(dest)
    print('Restored',item['path'])
"""
    (root / '恢复大文件.py').write_text(helper)
    with (root / 'README.md').open('a') as stream:
        stream.write('\n仓库中超过 100 MB 的文件已分为小于 100 MB 的分卷。执行 `python 恢复大文件.py` 可按校验和还原；Release ZIP 包含完整原文件。\n')
    hashes = [sha(p)+'  '+p.relative_to(root).as_posix() for p in sorted(root.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.txt']
    (root / 'SHA256SUMS.txt').write_text('\n'.join(hashes)+'\n')


def publish(books):
    # Only after complete page coverage, original scan preservation, ZIP CRC, image refs and hashes pass.
    names = ['Cell-Biology-Wang-Jinfa-MinerU-Local-Hybrid.zip', 'Cell-Biology-Laboratory-2e-MinerU-Local-Hybrid.zip']
    notes = ['两本教材以 MinerU 4.0.11 standard 档、ONNX + llama.cpp 混合模式解析。',
             '前 59 页来自先前本地解析断点，其余章节在 GitHub Actions 运行器本地推理；未调用远程解析 API。',
             '按章节保留图片、公式识别、Markdown、完整分页 Markdown、结构化 JSON、原始模型输出和原始 PDF 页面。',
             '已自动检查 793 页连续覆盖、所有图片引用、原始扫描图像流、文件与 ZIP 校验和；按要求不逐页人工核对。OCR 和公式仍可能有识别误差。', '']
    attachments = []
    for book, name in zip(books, names):
        src = ROOT / 'output' / book['title']
        report = json.loads((src / 'manifest.json').read_text())
        assert report['parsed_pages'] == report['source_pages'] == book['page_count']
        assert report['page_coverage_passed'] and report['missing_image_references'] == 0
        for line in (src / 'SHA256SUMS.txt').read_text().splitlines():
            expected, relative = line.split('  ', 1)
            path = src / relative
            assert path.resolve().is_relative_to(src.resolve())
            assert sha(path) == expected
        split_large_files(src)
        dest = ROOT / book['title']
        if dest.exists():
            old = {p.relative_to(dest).as_posix(): sha(p) for p in dest.rglob('*') if p.is_file()}
            new = {p.relative_to(src).as_posix(): sha(p) for p in src.rglob('*') if p.is_file()}
            assert old == new, 'Existing book folder differs; stop without overwriting'
        else:
            shutil.copytree(src, dest)
        archive = ROOT / 'output' / name
        assert archive.stat().st_size < 2_000_000_000
        attachments.extend([str(archive), str(archive) + '.sha256'])
        notes.append(f"- {book['title']}：{book['page_count']} 页；ZIP SHA-256 `{sha(archive)}`")
    for book in books:
        assert all(p.stat().st_size < 100_000_000 for p in (ROOT / book['title']).rglob('*') if p.is_file())
    subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
    subprocess.run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', 'add', '--sparse', '--', *[b['title'] for b in books]], check=True)
    changed = subprocess.run(['git', 'diff', '--cached', '--quiet']).returncode
    if changed:
        subprocess.run(['git', 'commit', '-m', 'Add complete chapter-organized MinerU cell biology books'], check=True)
        subprocess.run(['git', 'pull', '--rebase', 'origin', 'main'], check=True)
        subprocess.run(['git', 'push', 'origin', 'HEAD:main'], check=True)
    notes_file = ROOT / 'output/release-notes.md'
    notes_file.write_text('\n'.join(notes) + '\n')
    tag = 'cell-biology-local-hybrid-2026-10-10-0933c203'
    found = subprocess.run(['gh', 'release', 'view', tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if not found:
        subprocess.run(['gh', 'release', 'create', tag, '--target', 'main', '--title', '细胞生物学两书 · MinerU 混合解析 · 按章完整归档', '--notes-file', str(notes_file)], check=True)
    subprocess.run(['gh', 'release', 'upload', tag, '--clobber', *attachments], check=True)
    release = json.loads(subprocess.check_output(['gh', 'api', f'repos/{checkpoint.REPO}/releases/tags/{tag}']))
    for name in names:
        asset = next(a for a in release['assets'] if a['name'] == name)
        archive = ROOT / 'output' / name
        assert asset['size'] == archive.stat().st_size and asset['state'] == 'uploaded'
        assert asset.get('digest') == 'sha256:' + sha(archive)
    print('COMPLETE: BOOK FOLDERS PUSHED AND RELEASE ASSETS VERIFIED', release['html_url'], flush=True)

if __name__ == '__main__':
    {'prepare': prepare, 'parse': parse_chapter, 'finish': finish}[sys.argv[1]]()
