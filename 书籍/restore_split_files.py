#!/usr/bin/env python3
"""Restore byte-exact original PDFs from the repository's ordered parts."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import os

ROOT = Path(__file__).resolve().parents[1]


def safe_relative(value):
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or '\\' in value:
        raise RuntimeError('Unsafe manifest path.')
    return Path(*path.parts)


def sha256(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()


def restore(book_root, record, output_root):
    output = output_root / book_root.name / safe_relative(record['original_path'])
    if output.exists():
        if output.stat().st_size == record['original_size'] and sha256(output) == record['original_sha256']:
            print('Already verified:', output)
            return
        raise RuntimeError('An existing output has different bytes: ' + str(output))
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + '.restoring')
    combined, total, created = hashlib.sha256(), 0, False
    try:
        with temporary.open('xb') as stream:
            created = True
            for part in record['parts']:
                incoming = book_root / safe_relative(part['path'])
                individual, size = hashlib.sha256(), 0
                with incoming.open('rb') as source:
                    for chunk in iter(lambda: source.read(1024 * 1024), b''):
                        individual.update(chunk)
                        combined.update(chunk)
                        stream.write(chunk)
                        size += len(chunk)
                if size != part['size'] or individual.hexdigest() != part['sha256']:
                    raise RuntimeError('Part checksum mismatch: ' + str(incoming))
                total += size
            stream.flush()
            os.fsync(stream.fileno())
        if total != record['original_size'] or combined.hexdigest() != record['original_sha256']:
            raise RuntimeError('Restored original checksum mismatch.')
        temporary.replace(output)
        print('Restored and SHA-256 verified:', output)
    except BaseException:
        if created:
            temporary.unlink(missing_ok=True)
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--books-dir', type=Path, default=ROOT / '书籍')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'restored-pdfs')
    args = parser.parse_args()
    count = 0
    for manifest in sorted(args.books_dir.glob('*/大文件分片清单.json')):
        for record in json.loads(manifest.read_text()):
            restore(manifest.parent, record, args.output_dir)
            count += 1
    print('Verified original PDFs:', count)
