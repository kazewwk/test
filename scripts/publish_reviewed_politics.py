#!/usr/bin/env python3
"""Package the reviewed repository snapshot for its existing GitHub release."""
import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def sha(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def archive(directory, target, prefix, evidence=False):
    # Fixed metadata makes repeated packaging independent of checkout timestamps.
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED, compresslevel=5, allowZip64=True) as out:
        for path in sorted(directory.rglob('*')):
            if not path.is_file() or evidence and path.name == 'evidence-package.json':
                continue
            relative = path.relative_to(directory).as_posix()
            item = zipfile.ZipInfo(prefix + '/' + relative, (2026, 10, 9, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            content = path.read_bytes()
            if evidence and relative == 'README.md':
                content = content.decode().replace('(../../', '(https://github.com/kazewwk/test/blob/main/').encode()
            out.writestr(item, content, compresslevel=5)
    with zipfile.ZipFile(target) as out:
        assert out.testzip() is None, target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    repo, output = args.repository.resolve(), args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    central = repo / '校对记录/考研政治'
    plan = read(central / 'politics_books_plan.json')
    packages = read(central / 'book-packages.json')
    total_pages = total_corrections = checked_files = 0
    for book in plan['books']:
        directory = repo / book['folder']
        records = read(directory / 'SHA256_manifest.json')
        for record in records:
            path = directory / record['path']
            assert path.is_file() and path.stat().st_size == record['size'], path
            assert record['size'] < 100_000_000 and sha(path) == record['sha256'], path
            checked_files += 1
        info = read(directory / 'ocr_review/summary.json')
        assert info['original_pdf_and_raw_mineru_unchanged']
        assert not info['all_characters_manually_verified']
        pages = read(directory / 'ocr_review/page_audit.json')
        assert [p['pdf_page'] for p in pages] == list(range(1, book['pages'] + 1))
        assert all(p['source_sha256'] == book['sha256'] for p in pages)
        total_pages += len(pages)
        total_corrections += len(read(directory / 'ocr_review/corrections.json'))
        target = output / book['archive']
        archive(directory, target, book['folder'])
        fingerprint = sha(target)
        (output / (target.stem + '-SHA256SUMS.txt')).write_text(fingerprint + '  ' + target.name + '\n')
        for label, source in [('manifest', directory / 'manifest.json'),
                              ('validation', directory / 'validation_report.json'),
                              ('OCR-review', directory / 'ocr_review/summary.json')]:
            shutil.copyfile(source, output / (target.stem + '-' + label + '.json'))
        package = next(p for p in packages if p['book_id'] == book['id'])
        package.update(**info)
        package.update(zip_sha256=fingerprint, zip_bytes=target.stat().st_size, files=len(records)+1)
        print(book['title'], 'pages', len(pages), 'corrections', info['source_confirmed_corrections'], flush=True)
    assert total_pages == sum(b['pages'] for b in plan['books'])
    assert total_corrections == len(read(central / 'ocr-corrections.json'))
    completion = read(central / 'round2/completion.json')
    assert completion['all_remaining_candidates_adjudicated']
    assert completion['total_revision_records'] == total_corrections
    write(central / 'book-packages.json', packages)
    target = output / 'politics-OCR-review-evidence.zip'
    archive(central, target, '考研政治', evidence=True)
    fingerprint = sha(target)
    (output / 'politics-OCR-review-evidence-SHA256SUMS.txt').write_text(fingerprint + '  ' + target.name + '\n')
    write(central / 'evidence-package.json', {'asset_name': target.name, 'bytes': target.stat().st_size,
        'sha256': fingerprint, 'release': 'https://github.com/kazewwk/test/releases/tag/' + plan['release_tag']})
    assets = [{'name': p.name, 'size': p.stat().st_size, 'sha256': sha(p)}
              for p in sorted(output.iterdir()) if p.is_file()]
    assert len(assets) == 27 and all(not a['name'].endswith('.pdf') for a in assets)
    write(output.parent / 'publication-results.json', {'pages': total_pages, 'corrections': total_corrections,
        'checked_files': checked_files, 'assets': assets, 'books': packages})


if __name__ == '__main__':
    main()
