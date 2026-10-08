#!/usr/bin/env python3
"""Download provenance, resumable MinerU Hybrid parsing and verified packaging.

Run in a venv containing mineru==4.0.10 and pymupdf==1.28.2.
No credentials are saved in the book's outputs.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import time
import zipfile

_location = Path(__file__).resolve().parent.parent
ROOT = Path(os.environ.get('MOLECULAR_CELL_WORKDIR', str(_location.parent if _location.name == 'Molecular Biology of the Cell' else _location)))
SOURCE = ROOT / 'source/molecular-biology-of-the-cell-7e.pdf'
BOOK = ROOT / 'Molecular Biology of the Cell'
MANIFEST = ROOT / 'chapter-plan.json'
MAX_BYTES = 95_000_000
CHUNK_PAGES = 12


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sha256(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def prepare(only=None):
    import pymupdf
    doc = pymupdf.open(SOURCE)
    starts = [(0, 'Front Matter', 1)]
    for idx, page in enumerate(doc):
        if not 39 <= idx < 1443:
            continue
        lines = [line for block in page.get_text('dict', flags=pymupdf.TEXTFLAGS_DICT & ~pymupdf.TEXT_PRESERVE_IMAGES)['blocks']
                 if 'lines' in block for line in block['lines']]
        numbers = [int(span['text'].strip()) for line in lines for span in line['spans']
                   if span['size'] >= 59 and re.fullmatch(r'\d{1,2}', span['text'].strip())]
        titles = [''.join(span['text'] for span in line['spans']).strip() for line in lines
                  if line['spans'] and 25.5 <= max(span['size'] for span in line['spans']) <= 26.5]
        if numbers and titles:
            starts.append((numbers[0], re.sub(r'\s+', ' ', ' '.join(titles)), idx + 1))
    assert [number for number, _, _ in starts[1:]] == list(range(1, 25)), starts
    starts.extend([(25, 'Glossary', 1444), (26, 'Index', 1482), (27, 'Back Matter and Genetic Code', 1552)])
    sections = []
    for pos, (number, title, first) in enumerate(starts):
        last = starts[pos + 1][2] - 1 if pos + 1 < len(starts) else len(doc)
        name = f'{number:02d}_' + re.sub(r'[^\w -]+', '', title).replace(' ', '_')
        section = {'number': number, 'title': title, 'folder': name, 'pdf_first_page': first,
                   'pdf_last_page': last, 'page_count': last - first + 1,
                   'chunk_pages': 1 if number == 0 else CHUNK_PAGES}
        sections.append(section)
        if only is not None and number not in only:
            continue
        directory = BOOK / name
        directory.mkdir(parents=True, exist_ok=True)
        pdf_path = directory / 'source.pdf'
        if not pdf_path.exists():
            split = pymupdf.open()
            split.insert_pdf(doc, from_page=first - 1, to_page=last - 1, links=True, annots=True)
            split.set_metadata({'title': title, 'subject': f'Original PDF pages {first}-{last}'})
            split.save(pdf_path, garbage=3, deflate=True)
            split.close()
        source_pages = [{'pdf_page': i + 1, 'chapter_page': i - first + 2,
                         'text': doc[i].get_text(sort=True)} for i in range(first - 1, last)]
        write_json(directory / 'source_page_text.json', source_pages)
        (directory / 'source_text.txt').write_text('\n\n'.join(f'=== Original PDF page {p["pdf_page"]} ===\n{p["text"]}'
                                                             for p in source_pages), encoding='utf-8')
        write_json(directory / 'page_map.json', section)
    page_numbers = [p for section in sections for p in range(section['pdf_first_page'], section['pdf_last_page'] + 1)]
    assert page_numbers == list(range(1, len(doc) + 1))
    manifest = {'title': 'Molecular Biology of the Cell', 'edition': 7,
                'repository': 'kazewwk/test', 'release_tag': 'molecular-biology-of-the-cell-7e-2026-10-09',
                'source_url': 'https://github.com/kazewwk/test/releases/download/molecular-biology-of-the-cell-7e-2026-10-09/molecular-biology-of-the-cell-7e.pdf',
                'source_size': SOURCE.stat().st_size, 'source_sha256': sha256(SOURCE),
                'source_page_count': len(doc), 'mineru_version': '4.0.10',
                'mode': 'Hybrid', 'tier': 'standard', 'effort': 'high',
                'small_model_backend': 'onnx', 'vlm_engine': 'llama-cpp',
                'ocr_mode': 'auto', 'image_analysis': True, 'chunk_pages': CHUNK_PAGES,
                'sections': sections}
    write_json(MANIFEST, manifest)
    write_json(BOOK / 'manifest.json', manifest)
    if only is not None:
        print(f'PREPARED selected sections {sorted(only)} of {len(sections)}', flush=True)
        return
    # Retain the exact original bytes, including any metadata and attachments,
    # as files strictly below GitHub's 100 MB single-file limit.
    parts_dir = BOOK / 'original_pdf_parts'
    parts_dir.mkdir(exist_ok=True)
    parts = []
    with SOURCE.open('rb') as stream:
        index = 1
        while data := stream.read(MAX_BYTES):
            part = parts_dir / f'molecular-biology-of-the-cell-7e.pdf.part{index:03d}'
            if not part.exists():
                part.write_bytes(data)
            assert part.read_bytes() == data
            parts.append({'path': part.name, 'size': len(data), 'sha256': sha256(part)})
            index += 1
    write_json(parts_dir / 'parts.json', {'output': SOURCE.name, 'sha256': manifest['source_sha256'],
                                         'size': manifest['source_size'], 'parts': parts})
    print(f'PREPARED {len(doc)} pages in {len(sections)} sections', flush=True)


def parse_all(only=None, selected_pages=None):
    from mineru.parser import MinerUParser
    from mineru.parser.writer import FileBasedDataWriter
    from mineru.config import config
    import mineru_llama_cpp
    # Explicitly use CPU runtimes and bounded inference concurrency.
    config.model.small_backend = 'onnx'
    config.model.vlm.engine = 'llama-cpp'
    config.model.vlm.max_concurrency = 1
    # Set the engine's public runtime constructor options without changing
    # inference, page selection or the parser's singleton cache keys.
    cpu_threads = len(os.sched_getaffinity(0)) if hasattr(os, 'sched_getaffinity') else (os.cpu_count() or 2)
    quota_file = Path('/sys/fs/cgroup/cpu.max')
    if quota_file.exists():
        quota, period = quota_file.read_text().split()
        if quota != 'max':
            cpu_threads = min(cpu_threads, max(1, int(quota) // int(period)))
    os.environ.setdefault('MINERU_INTRA_OP_NUM_THREADS', str(cpu_threads))
    os.environ.setdefault('MINERU_INTER_OP_NUM_THREADS', '1')
    original_engine = mineru_llama_cpp.Engine
    class CpuEngine(original_engine):
        def __init__(self, *args, **kwargs):
            kwargs.setdefault('n_threads', cpu_threads)
            kwargs.setdefault('n_gpu_layers', 0)
            kwargs.setdefault('n_parallel', 1)
            super().__init__(*args, **kwargs)
    mineru_llama_cpp.Engine = CpuEngine
    parser = MinerUParser(tier='standard', parse_mode='auto', image_analysis=True)
    manifest = json.loads(MANIFEST.read_text())
    for section in manifest['sections']:
        if only is not None and section['number'] not in only:
            continue
        directory = BOOK / section['folder']
        chunk_pages = section.get('chunk_pages', CHUNK_PAGES)
        for first in range(1, section['page_count'] + 1, chunk_pages):
            last = min(first + chunk_pages - 1, section['page_count'])
            if selected_pages is not None and first not in selected_pages:
                continue
            chunk_name = f'pages_{first:04d}-{last:04d}'
            target = directory / 'chunks' / chunk_name
            checkpoint = target / 'parse_complete.json'
            if checkpoint.exists():
                continue
            start = time.monotonic()
            print(f'START {section["number"]:02d} {chunk_name} ORIGINAL {section["pdf_first_page"] + first - 1}-{section["pdf_first_page"] + last - 1}', flush=True)
            result = parser.parse(directory / 'source.pdf', page_range=f'{first}-{last}')
            actual = [page.page_idx for page in result.pages]
            assert actual == list(range(first - 1, last)), (section, first, last, actual)
            temporary = target.with_name(chunk_name + '.pending')
            if temporary.exists():
                shutil.rmtree(temporary)
            result.save(FileBasedDataWriter(str(temporary)))
            # The FULL renderer also retains page headers, footers and all
            # auxiliary blocks excluded from the default reading view.
            from mineru.parser import ParseResult
            from mineru.render.contracts import RenderMode
            materialized = ParseResult.from_json((temporary / 'middle_json.json').read_text())
            (temporary / 'all_content.md').write_text(materialized.markdown(mode=RenderMode.FULL), encoding='utf-8')
            details = {'first_chapter_page': first, 'last_chapter_page': last,
                       'first_original_pdf_page': section['pdf_first_page'] + first - 1,
                       'last_original_pdf_page': section['pdf_first_page'] + last - 1,
                       'page_indices': actual, 'elapsed_seconds': round(time.monotonic() - start, 3),
                       'tier': 'standard', 'mode': 'Hybrid', 'effort': 'high'}
            write_json(temporary / 'parse_complete.json', details)
            if target.exists():
                shutil.rmtree(target)
            temporary.rename(target)
            print(f'DONE {section["number"]:02d} {chunk_name} {details["elapsed_seconds"]}s', flush=True)
    parser.close()


def rewrite_image_paths(value, prefix):
    if isinstance(value, dict):
        return {key: prefix + item if key == 'image_path' and isinstance(item, str) and item
                else rewrite_image_paths(item, prefix) for key, item in value.items()}
    if isinstance(value, list):
        return [rewrite_image_paths(item, prefix) for item in value]
    return value


def finalize():
    import pymupdf
    from mineru.parser import ParseResult
    from mineru.render.contracts import RenderMode
    manifest = json.loads(MANIFEST.read_text())
    coverage = []
    sections_readme = []
    full_markdown = ['# Molecular Biology of the Cell — Seventh Edition\n']
    for section in manifest['sections']:
        directory = BOOK / section['folder']
        combined = None
        parsed_pages = []
        chunk_pages = section.get('chunk_pages', CHUNK_PAGES)
        for first in range(1, section['page_count'] + 1, chunk_pages):
            last = min(first + chunk_pages - 1, section['page_count'])
            chunk_name = f'pages_{first:04d}-{last:04d}'
            target = directory / 'chunks' / chunk_name
            assert (target / 'parse_complete.json').is_file(), f'Incomplete: {target}'
            raw = json.loads((target / 'middle_json.json').read_text())
            assert [page['page_idx'] for page in raw['pages']] == list(range(first - 1, last))
            prefixed = rewrite_image_paths(raw, f'chunks/{chunk_name}/')
            if combined is None:
                combined = copy.deepcopy(prefixed)
                combined['pages'] = []
                if 'docvortex_layout' in combined.get('extensions', {}):
                    combined['extensions']['docvortex_layout']['pages'] = []
            combined['pages'].extend(prefixed['pages'])
            if 'docvortex_layout' in prefixed.get('extensions', {}):
                combined['extensions']['docvortex_layout']['pages'].extend(prefixed['extensions']['docvortex_layout']['pages'])
            parsed_pages.extend(range(section['pdf_first_page'] + first - 1, section['pdf_first_page'] + last))
        assert parsed_pages == list(range(section['pdf_first_page'], section['pdf_last_page'] + 1))
        combined['is_full_document'] = True
        write_json(directory / 'middle_json.json', combined)
        result = ParseResult.from_dict(combined)
        (directory / 'chapter.md').write_text(result.markdown(), encoding='utf-8')
        (directory / 'all_content.md').write_text(result.markdown(mode=RenderMode.FULL), encoding='utf-8')
        write_json(directory / 'structured_content.json', result.structured_content())
        native_pages = json.loads((directory / 'source_page_text.json').read_text())
        for source_page, parsed_page in zip(native_pages, result.pages, strict=True):
            page_md = ParseResult.from_dict({**combined, 'pages': [parsed_page.to_dict()]}).markdown(mode=RenderMode.FULL)
            coverage.append({'pdf_page': source_page['pdf_page'], 'section': section['folder'],
                             'chapter_page': source_page['chapter_page'],
                             'source_native_text_characters': len(source_page['text'].strip()),
                             'mineru_markdown_characters': len(page_md.strip()),
                             'mineru_blocks': len(parsed_page.blocks),
                             'has_parsed_page': True,
                             'native_text_retained': True, 'source_pdf_retained': True})
        with pymupdf.open(directory / 'source.pdf') as source_doc:
            assert len(source_doc) == section['page_count']
        chapter_link = f'{section["folder"]}/chapter.md'
        sections_readme.append(f'| {section["number"]:02d} | [{section["title"]}]({chapter_link}) | {section["pdf_first_page"]}–{section["pdf_last_page"]} | {section["page_count"]} |')
        directory.joinpath('README.md').write_text(f'# {section["title"]}\n\n原始 PDF 第 {section["pdf_first_page"]}–{section["pdf_last_page"]} 页，共 {section["page_count"]} 页。\n\n'
               '[章节阅读](chapter.md) · [含页眉页脚的全部内容](all_content.md) · [原页 PDF](source.pdf) · [原生文本](source_text.txt) · [页码映射](page_map.json)\n\n'
               '`chunks/` 保留每批 MinerU 原始 Markdown、图片、middle JSON、structured content、model output 和完成记录。\n', encoding='utf-8')
        # Prefix relative assets when combining chapters into the reading file.
        md = result.markdown(asset_base_url=section['folder'] + '/')
        full_markdown.append(f'\n\n<!-- Original PDF pages {section["pdf_first_page"]}-{section["pdf_last_page"]} -->\n\n{md}')
    assert [row['pdf_page'] for row in coverage] == list(range(1, manifest['source_page_count'] + 1))
    write_json(BOOK / 'page_coverage.json', coverage)
    BOOK.joinpath('full.md').write_text('\n'.join(full_markdown), encoding='utf-8')
    weak = [row for row in coverage if row['source_native_text_characters'] > 100 and row['mineru_markdown_characters'] < 100]
    report = {'source_page_count': manifest['source_page_count'], 'parsed_page_count': len(coverage),
              'missing_pages': [], 'duplicate_pages': [], 'chapter_count': 24,
              'section_count': len(manifest['sections']), 'source_sha256': manifest['source_sha256'],
              'pages_needing_review': weak,
              'character_accuracy_guaranteed': False,
              'original_content_preserved': 'Exact original PDF byte parts, complete section PDFs, source native text and all MinerU outputs retained.'}
    write_json(BOOK / 'validation_report.json', report)
    BOOK.joinpath('README.md').write_text('# Molecular Biology of the Cell\n\n第 7 版，原始 PDF 共 1,555 页。使用 MinerU 4.0.10 **Hybrid 混合模式**解析：`standard` / `high`、ONNX 小模型与 llama.cpp VLM，自动 OCR，启用图片解析。\n\n'
        '[全文](full.md) · [逐页覆盖记录](page_coverage.json) · [完整性检查](validation_report.json) · [来源和参数](manifest.json)\n\n'
        '24 个正文章节，以及前置内容、词汇表、索引和封底附录，连续覆盖全部 1,555 页。各目录含章节 Markdown、完整结构 JSON、图片、原页 PDF、原生文本及页码映射；原始分批解析文件位于 `chunks/`。`all_content.md` 还保留页眉页脚等辅助块。\n\n'
        '原始 PDF 的全部字节无损保存在 `original_pdf_parts/`。运行 `python tools/restore_original_pdf.py` 可还原并检查 SHA-256。原页 PDF 和原生文本用于复核模型可能发生的文字、图表或公式识别错误；页面覆盖不代表字符识别完全正确。\n\n'
        '| 编号 | 内容 | 原始 PDF 页码 | 页数 |\n| --- | --- | --- | ---: |\n' + '\n'.join(sections_readme) + '\n', encoding='utf-8')
    tool_dir = BOOK / 'tools'
    tool_dir.mkdir(exist_ok=True)
    shutil.copy2(Path(__file__), tool_dir / Path(__file__).name)
    shutil.copy2(ROOT / 'tools/restore_original_pdf.py', tool_dir / 'restore_original_pdf.py')
    # Check that every materialized image referenced in every JSON is present.
    for path in BOOK.rglob('middle_json.json'):
        def inspect(value):
            if isinstance(value, dict):
                for key, item in value.items():
                    if key == 'image_path' and item:
                        assert (path.parent / item).is_file(), (path, item)
                    else:
                        inspect(item)
            elif isinstance(value, list):
                for item in value:
                    inspect(item)
        inspect(json.loads(path.read_text()))
    # Split any output exceeding the repository file limit losslessly.
    splits = []
    for path in list(BOOK.rglob('*')):
        if path.is_file() and path.stat().st_size >= 100_000_000:
            parts = []
            size, checksum = path.stat().st_size, sha256(path)
            with path.open('rb') as stream:
                index = 1
                while data := stream.read(MAX_BYTES):
                    part = path.with_name(path.name + f'.part{index:03d}')
                    part.write_bytes(data)
                    parts.append({'path': str(part.relative_to(BOOK)), 'size': len(data), 'sha256': sha256(part)})
                    index += 1
            splits.append({'path': str(path.relative_to(BOOK)), 'size': size, 'sha256': checksum, 'parts': parts})
            path.unlink()
    write_json(BOOK / 'split_files.json', splits)
    file_records = [{'path': str(path.relative_to(BOOK)), 'size': path.stat().st_size, 'sha256': sha256(path)}
                    for path in sorted(BOOK.rglob('*')) if path.is_file() and path.name != 'SHA256_manifest.json']
    assert all(record['size'] < 100_000_000 for record in file_records)
    write_json(BOOK / 'SHA256_manifest.json', file_records)
    archive = ROOT / 'Molecular-Biology-of-the-Cell-7e-MinerU-Hybrid.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=5, allowZip64=True) as z:
        for path in sorted(BOOK.rglob('*')):
            if path.is_file():
                z.write(path, path.relative_to(BOOK.parent))
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
    write_json(ROOT / 'archive.json', {'file': archive.name, 'size': archive.stat().st_size,
                                       'sha256': sha256(archive), 'files': len(file_records) + 1})
    print(f'FINALIZED {len(coverage)} pages, {len(file_records)+1} files, ZIP {archive.stat().st_size} bytes', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['prepare', 'parse', 'finalize'])
    parser.add_argument('--only', help='Comma-separated section numbers for parsing')
    parser.add_argument('--pages', default='all', help='Selected chapter page starts, comma-separated, or all')
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare({int(value) for value in args.only.split(',')} if args.only else None)
    elif args.action == 'parse':
        parse_all({int(value) for value in args.only.split(',')} if args.only else None,
                  {int(value) for value in args.pages.split(',')} if args.pages != 'all' else None)
    else:
        finalize()
