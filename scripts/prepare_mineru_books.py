#!/usr/bin/env python3
"""Extract original archives and split oversized PDFs without changing any bytes."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import tempfile
import time
import urllib.parse
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PLAN = json.loads((ROOT / 'books/extraction-plan.json').read_text())
LIMIT = PLAN['max_file_bytes_exclusive']
PART_LIMIT = PLAN['split_part_bytes']


def fingerprints(path):
    size = path.stat().st_size
    sha256 = hashlib.sha256()
    git_sha = hashlib.sha1(b'blob ' + str(size).encode() + b'\0')
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            sha256.update(chunk)
            git_sha.update(chunk)
    return {'size': size, 'sha256': sha256.hexdigest(), 'git_blob_sha1': git_sha.hexdigest()}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def local_link(path):
    return urllib.parse.quote(str(path), safe='/')


def archive_for(book, source_dir, downloads):
    if source_dir:
        path = source_dir / book['asset_name']
    else:
        downloads.mkdir(exist_ok=True)
        path = downloads / book['asset_name']
        url = ('https://github.com/' + PLAN['repository'] + '/releases/download/'
               + PLAN['release_tag'] + '/' + book['asset_name'])
        for attempt in range(6):
            # A new curl process recalculates the resume offset after each failure.
            result = subprocess.run(['curl', '--fail', '--silent', '--show-error',
                                     '--location', '--continue-at', '-', '--retry', '0',
                                     '--connect-timeout', '30', '--max-time', '1800',
                                     '--output', str(path), url])
            if result.returncode == 0:
                break
            if attempt == 5:
                raise RuntimeError('Release download failed: ' + book['asset_name'])
            time.sleep(3 * (attempt + 1))
    actual = fingerprints(path)
    if actual['size'] != book['size'] or actual['sha256'] != book['sha256']:
        raise RuntimeError('Original archive fingerprint mismatch: ' + book['asset_name'])
    return path


def extract_archive(archive, destination, book):
    names = set()
    with zipfile.ZipFile(archive) as source:
        entries = [entry for entry in source.infolist() if not entry.is_dir()]
        if len(entries) != book['source_file_count']:
            raise RuntimeError('Archive file count changed.')
        if sum(entry.file_size for entry in entries) != book['source_uncompressed_bytes']:
            raise RuntimeError('Archive uncompressed size changed.')
        for entry in entries:
            path = PurePosixPath(entry.filename)
            if path.is_absolute() or '..' in path.parts or '.git' in path.parts or '\\' in entry.filename:
                raise RuntimeError('Unsafe archive path: ' + entry.filename)
            if stat.S_ISLNK(entry.external_attr >> 16):
                raise RuntimeError('Archive symlinks are not supported.')
            parts = path.parts
            if book['strip_prefix']:
                if len(parts) < 2 or parts[0] != book['strip_prefix']:
                    raise RuntimeError('Unexpected archive root.')
                parts = parts[1:]
            relative = PurePosixPath(*parts)
            if str(relative) in names:
                raise RuntimeError('Duplicate archive path: ' + str(relative))
            names.add(str(relative))
            target = destination.joinpath(*relative.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with source.open(entry) as incoming, target.open('xb') as outgoing:
                shutil.copyfileobj(incoming, outgoing, 1024 * 1024)
            # Reading each entry to EOF also checks its ZIP CRC.
            if target.stat().st_size != entry.file_size:
                raise RuntimeError('Extracted file size mismatch.')


def split_pdf(path, book_root):
    original = fingerprints(path)
    relative = path.relative_to(book_root).as_posix()
    target_dir = path.with_name(path.name + '.parts')
    target_dir.mkdir()
    parts, combined = [], hashlib.sha256()
    with path.open('rb') as source:
        number = 1
        while True:
            block = source.read(PART_LIMIT)
            if not block:
                break
            output = target_dir / f'part-{number:04d}.bin'
            output.write_bytes(block)
            combined.update(block)
            parts.append({'path': output.relative_to(book_root).as_posix(), **fingerprints(output)})
            number += 1
    if sum(p['size'] for p in parts) != original['size'] or combined.hexdigest() != original['sha256']:
        raise RuntimeError('Lossless split verification failed: ' + relative)
    result = {'original_path': relative, 'original_size': original['size'],
              'original_sha256': original['sha256'], 'method': 'byte-concatenation', 'parts': parts}
    write_json(target_dir / '分片清单.json', result)
    text = [f'# {path.name}：无损分片', '',
            f'原 PDF 共 {original["size"]:,} 字节，分为 {len(parts)} 片，每片不超过 95 MB。', '',
            '从仓库根目录运行 `python3 scripts/restore_split_files.py`，即可在 `restored-pdfs/` 中还原 PDF。脚本会核对每片和完整原文件的 SHA-256。', '',
            '| 顺序 | 分片 | 大小 |', '| --- | --- | ---: |']
    for number, row in enumerate(parts, 1):
        name = PurePosixPath(row['path']).name
        text.append(f'| {number} | [{name}]({name}) | {row["size"] / 1e6:.2f} MB |')
    text += ['', f'完整原始 PDF SHA-256：`{original["sha256"]}`', '']
    (target_dir / 'README.md').write_text('\n'.join(text))
    path.with_name(path.name + '.分片说明.md').write_text(
        f'# {path.name}\n\n原 PDF 已无损分片，请打开[分片目录]({local_link(target_dir.name)}/README.md)。\n')
    # Read the saved parts again in order, proving the on-disk reconstruction hash.
    reconstructed = hashlib.sha256()
    for row in parts:
        with (book_root / row['path']).open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                reconstructed.update(block)
    if reconstructed.hexdigest() != original['sha256']:
        raise RuntimeError('Saved PDF parts do not reconstruct the original.')
    path.unlink()
    print('PDF_SPLIT_LOSSLESS', relative, len(parts), 'parts', flush=True)
    return result


def prepare_book(book, destination, source_dir=None, downloads=None):
    folder = destination / book['folder']
    if folder.exists():
        raise RuntimeError('Destination already exists: ' + str(folder))
    folder.mkdir(parents=True)
    archive = archive_for(book, source_dir, downloads or ROOT / 'book-downloads')
    extract_archive(archive, folder, book)
    if source_dir is None:
        archive.unlink()
    large_files = sorted(path for path in folder.rglob('*') if path.is_file() and path.stat().st_size >= LIMIT)
    if len(large_files) != book['oversized_pdf_count']:
        raise RuntimeError('Unexpected oversized file count.')
    splits = []
    for path in large_files:
        if path.suffix.lower() != '.pdf':
            raise RuntimeError('Unexpected oversized non-PDF file: ' + str(path))
        splits.append(split_pdf(path, folder))
    write_json(folder / '大文件分片清单.json', splits)
    reading = next((p for p in ['merged/full.md', '全文.md', '合并结果/full.md', 'full.md'] if (folder / p).is_file()), None)
    chapter_dir = next((p for p in ['chapters', '章节'] if (folder / p).is_dir()), None)
    guide = [f'# {book["folder"]}', '', f'原始 ZIP：`{book["original_name"]}`', '']
    if reading:
        guide.append(f'- [阅读全文 Markdown]({local_link(reading)})')
    if chapter_dir:
        guide.append(f'- [按章节阅读]({local_link(chapter_dir)}/)')
    guide += ['- [大文件分片清单](大文件分片清单.json)', '',
              'Markdown、图片、解析 JSON 和原包其他文件位于本目录。原包的单一外层目录已去掉，内部相对路径保持原来的层级。', '',
              f'超过 100 MB 的 {len(splits)} 个 PDF 已无损分片；分片目录的 README 说明还原方法与校验值。', '']
    (folder / '阅读指南.md').write_text('\n'.join(guide))
    if not (folder / 'README.md').exists():
        (folder / 'README.md').write_text('\n'.join(guide))
    files = []
    for path in sorted(p for p in folder.rglob('*') if p.is_file()):
        record = {'path': path.relative_to(folder).as_posix(), **fingerprints(path)}
        if record['size'] >= LIMIT:
            raise RuntimeError('File exceeds the final repository limit: ' + record['path'])
        files.append(record)
    report = {'folder': book['folder'], 'original_zip_sha256': book['sha256'],
              'source_file_count': book['source_file_count'], 'source_uncompressed_bytes': book['source_uncompressed_bytes'],
              'split_pdf_count': len(splits), 'split_part_count': sum(len(s['parts']) for s in splits),
              'reading_path': reading, 'chapter_directory': chapter_dir, 'files': files}
    write_json(folder / '仓库文件校验.json', report)
    manifest_size = (folder / '仓库文件校验.json').stat().st_size
    if manifest_size >= LIMIT:
        raise RuntimeError('Checksum manifest exceeds the repository limit.')
    print('BOOK_PREPARED', book['folder'], len(files) + 1, 'files', flush=True)
    return {k: v for k, v in report.items() if k != 'files'} | {
        'file_count': len(files) + 1, 'total_bytes': sum(f['size'] for f in files) + manifest_size,
        'max_file_bytes': max([f['size'] for f in files] + [manifest_size]),
        'checksum_manifest': fingerprints(folder / '仓库文件校验.json')}


def write_index(destination, summaries):
    write_json(ROOT / 'books/extracted-manifest.json', {'repository': PLAN['repository'],
               'file_limit_bytes_exclusive': LIMIT, 'books': summaries})
    text = ['# MinerU 书籍库', '', '13 份书籍解析包已解压到 `书籍/`，一本书一个文件夹。', '',
            '可以直接在代码仓库阅读 Markdown、章节、图片和解析 JSON，`git clone` 也会取得这些文件。', '',
            '| 书籍 | 全文 | 章节 | 文件数 |', '| --- | --- | --- | ---: |']
    for book in summaries:
        base = '书籍/' + book['folder'] + '/'
        full = f'[全文]({local_link(base + book["reading_path"])})' if book['reading_path'] else '—'
        chapters = f'[章节]({local_link(base + book["chapter_directory"])}/)' if book['chapter_directory'] else '—'
        text.append(f'| [{book["folder"]}]({local_link(base)}) | {full} | {chapters} | {book["file_count"]:,} |')
    text += ['', f'所有仓库文件严格小于 100,000,000 字节（100 MB）。超过限值的 {sum(b["split_pdf_count"] for b in summaries)} 个 PDF 已无损分片，每片不超过 95 MB。运行 `python3 scripts/restore_split_files.py`，在 `restored-pdfs/` 中还原完整 PDF，并核对 SHA-256。', '',
             '每本书的 `仓库文件校验.json` 记录文件大小、SHA-256 和 Git blob SHA-1。', '',
             '[13 份原始 ZIP 下载页](https://github.com/' + PLAN['repository'] + '/releases/tag/' + PLAN['release_tag'] + ')仍提供完整原包，原始压缩包的[目录与校验值](books/manifest.json)也保留在仓库中。', '']
    (ROOT / 'README.md').write_text('\n'.join(text))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path)
    parser.add_argument('--destination', type=Path, default=ROOT / '书籍')
    arguments = parser.parse_args()
    summaries = [prepare_book(book, arguments.destination, arguments.source_dir) for book in PLAN['books']]
    write_index(arguments.destination, summaries)
