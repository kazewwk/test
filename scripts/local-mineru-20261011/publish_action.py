import base64
import concurrent.futures
import hashlib
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

PLAN = json.loads((Path(__file__).parent / 'publication.json').read_text())
OUT = Path('/tmp/local-mineru-books')
OUT.mkdir(exist_ok=True)

def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        while data := stream.read(1024 * 1024):
            digest.update(data)
    return digest.hexdigest()

def validate():
    for book in PLAN['books']:
        root = Path(book['directory'])
        report = json.loads((root / 'manifest.json').read_text())
        assert report['parsed_pages'] == report['source_pages'] == book['pages']
        assert report['page_coverage_passed'] and report['missing_image_references'] == 0
        assert report['chapter_count'] == book['chapter_count']
        for line in (root / 'SHA256SUMS.txt').read_text().splitlines():
            expected, relative = line.split('  ', 1)
            path = root / relative
            assert path.resolve().is_relative_to(root.resolve())
            assert path.is_file() and sha(path) == expected
            assert path.stat().st_size < 100_000_000
        print('Validated', book['directory'], book['pages'], flush=True)

def prepare():
    repo = os.environ['GITHUB_REPOSITORY']
    def download(part):
        response = json.loads(subprocess.check_output(['gh', 'api', f'repos/{repo}/git/blobs/{part["sha"]}']))
        data = base64.b64decode(response['content'])
        assert len(data) == part['size']
        assert hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == part['sha']
        return data
    for spec in PLAN['archives']:
        archive = OUT / spec['zip']
        with archive.open('wb') as target, concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            for data in pool.map(download, spec['parts']):
                target.write(data)
        assert archive.stat().st_size == spec['size'] and sha(archive) == spec['sha256']
        with zipfile.ZipFile(archive) as bundle:
            assert bundle.testzip() is None
            for member in bundle.infolist():
                if member.is_dir():
                    continue
                assert member.filename.startswith(spec['directory'] + '/')
                path = Path(member.filename)
                assert path.resolve().is_relative_to(Path(spec['directory']).resolve())
                assert member.file_size < 100_000_000
                data = bundle.read(member)
                if path.exists():
                    assert sha(path) == hashlib.sha256(data).hexdigest(), path
                else:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(data)
    validate()

def publish():
    validate()
    attachments = []
    lines = ['两本书使用 MinerU 4.0.11 在当前本地 CPU 环境以 ONNX + llama.cpp 混合模式解析，standard 档。GitHub Actions 只校验、展开和发布本地结果。', '',
             '按章保留 Markdown、完整分页 Markdown、图片、公式识别、结构化 JSON、分批原始模型输出，以及每章原始 PDF 页面。', '',
             '自动检查 793 页连续覆盖、图片引用、原始扫描图像流和文件校验和。按要求不逐页人工核对；OCR 和公式语义可能有识别误差。', '',
             '| 书 | 页数 | 正文章数 | ZIP 大小 |', '| --- | ---: | ---: | ---: |']
    for book in PLAN['books']:
        spec = next(a for a in PLAN['archives'] if a['zip'] == book['zip'])
        archive = OUT / spec['zip']
        assert archive.stat().st_size == spec['size'] < 2_000_000_000
        assert sha(archive) == spec['sha256']
        checksum = OUT / (spec['zip'] + '.sha256')
        checksum.write_text(spec['sha256'] + '  ' + spec['zip'] + '\n')
        attachments.extend([str(archive), str(checksum)])
        lines.append(f'| {book["directory"]} | {book["pages"]} | {book["chapter_count"]} | {spec["size"] / 1024**2:.2f} MiB |')
    notes = OUT / 'release-notes.md'
    notes.write_text('\n'.join(lines) + '\n')
    tag = PLAN['tag']
    exists = subprocess.run(['gh', 'release', 'view', tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if not exists:
        subprocess.run(['gh', 'release', 'create', tag, '--target', 'main', '--title', PLAN['title'], '--notes-file', str(notes)], check=True)
    subprocess.run(['gh', 'release', 'upload', tag, '--clobber', *attachments], check=True)
    release = json.loads(subprocess.check_output(['gh', 'api', f'repos/{os.environ["GITHUB_REPOSITORY"]}/releases/tags/{tag}']))
    for spec in PLAN['archives']:
        asset = next(a for a in release['assets'] if a['name'] == spec['zip'])
        assert asset['state'] == 'uploaded' and asset['size'] == spec['size']
        assert asset.get('digest') == 'sha256:' + spec['sha256']
    (OUT / 'verification.md').write_text(notes.read_text() + '\nRelease: ' + release['html_url'] + '\n')
    print('Published and SHA-256 verified', release['html_url'], flush=True)

if __name__ == '__main__':
    {'prepare': prepare, 'publish': publish}[sys.argv[1]]()
