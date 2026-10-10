import copy
import hashlib
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.mineru/lib/python3.12/site-packages'))
from mineru.parser import ParseResult
from mineru.render.contracts import RenderMode
import fitz

def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from walk(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk(value)

books = json.loads((ROOT / 'work/chapters.json').read_text())
all_ready = True
for book in books:
    bookroot = ROOT / 'output' / book['title']
    original_document = fitz.open(ROOT / book['source'])
    rows = []
    for chapter in book['chapters']:
        key = f"book{book['id']}-{chapter['number']:02}"
        if not (ROOT / 'work/states' / f'{key}.done.json').exists():
            all_ready = False
            continue
        dest = bookroot / chapter['name']
        if (dest / '自动核验.json').exists():
            rows.append(json.loads((dest / '自动核验.json').read_text()))
            continue
        merged = None
        parsed = []
        missing_images = []
        for batch in sorted((dest / '解析批次').iterdir()):
            assert (batch / 'complete.json').exists(), batch
            data = json.loads((batch / 'middle_json.json').read_text())
            if merged is None:
                merged = copy.deepcopy(data)
                merged['pages'] = []
                if 'docvortex_layout' in merged.get('extensions', {}):
                    merged['extensions']['docvortex_layout']['pages'] = []
            merged['pages'].extend(data['pages'])
            if 'docvortex_layout' in data.get('extensions', {}):
                merged['extensions']['docvortex_layout']['pages'].extend(data['extensions']['docvortex_layout']['pages'])
            parsed.extend(p['page_idx'] for p in data['pages'])
            if (batch / 'images').exists():
                (dest / 'images').mkdir(exist_ok=True)
                for image in (batch / 'images').iterdir():
                    target = dest / 'images' / image.name
                    if target.exists():
                        assert hashlib.sha256(target.read_bytes()).digest() == hashlib.sha256(image.read_bytes()).digest()
                    else:
                        shutil.copyfile(image, target)
        assert parsed == list(range(chapter['page_count'])), (key, parsed)
        merged['is_full_document'] = True
        result = ParseResult.from_dict(merged)
        (dest / '正文.md').write_text(result.markdown(), encoding='utf-8')
        (dest / '完整分页.md').write_text(result.markdown(mode=RenderMode.FULL), encoding='utf-8')
        (dest / 'middle_json.json').write_text(result.to_json(), encoding='utf-8')
        dump(dest / 'structured_content.json', result.structured_content())
        for node in walk(merged):
            image = node.get('image_path')
            if image and not (dest / image).is_file():
                missing_images.append(image)
        assert not missing_images, (key, missing_images)
        with fitz.open(dest / '原始页面.pdf') as original_chapter:
            assert len(original_chapter) == chapter['page_count']
            preserved_pages = []
            for local_page, original_page in enumerate(range(chapter['start'] - 1, chapter['end'])):
                def image_digests(document, page):
                    return sorted(hashlib.sha256(document.xref_stream_raw(item[0])).hexdigest()
                                  for item in document[page].get_images(full=True))
                assert image_digests(original_document, original_page) == image_digests(original_chapter, local_page), (key, original_page)
                preserved_pages.append(original_page + 1)
        sparse_pages = []
        for page in merged['pages']:
            texts = [n.get('content', '') for n in walk(page) if n.get('type') in {'text', 'equation', 'inline_equation'} and isinstance(n.get('content'), str)]
            char_count = len(''.join(texts).strip())
            if char_count < 20:
                sparse_pages.append({'chapter_page': page['page_idx'] + 1,
                                     'source_pdf_page': chapter['start'] + page['page_idx'],
                                     'text_char_count': char_count})
        row = dict(chapter, parsed_page_count=len(parsed),
                   image_file_count=len(list((dest / 'images').glob('*'))),
                   formula_node_count=sum('formula' in str(n.get('type', '')) or 'equation' in str(n.get('type', '')) for n in walk(merged)),
                   missing_images=missing_images, sparse_pages=sparse_pages,
                   original_pdf_preserved=True, original_scan_streams_verified_pages=preserved_pages)
        dump(dest / '自动核验.json', row)
        rows.append(row)
        print('ASSEMBLED', book['title'], chapter['name'], len(parsed), flush=True)
    if len(rows) != len(book['chapters']):
        original_document.close()
        continue
    original_document.close()
    coverage = [p for row in rows for p in range(row['start'], row['end'] + 1)]
    assert coverage == list(range(1, book['page_count'] + 1))
    source = ROOT / book['source']
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    report = {'book': book['title'], 'mineru_version': '4.0.11',
              'backend': 'local hybrid: ONNX + llama.cpp', 'tier': 'standard',
              'ocr_mode': 'ocr', 'image_analysis': True,
              'source_sha256': source_hash,
              'source_pages': book['page_count'], 'parsed_pages': len(coverage),
              'page_coverage_passed': True,
              'chapter_count': 15 if book['id'] == 0 else 12,
              'folder_count_including_front_back_matter': len(rows),
              'missing_image_references': 0,
              'images': sum(r['image_file_count'] for r in rows),
              'formula_nodes': sum(r['formula_node_count'] for r in rows),
              'sparse_pages': [p for r in rows for p in r['sparse_pages']],
              'validation': 'automated only; no page-by-page manual review',
              'limitation': 'Page coverage and image references are checked. OCR/formula semantic accuracy is not guaranteed. Original chapter PDF pages are retained.',
              'chapters': rows}
    dump(bookroot / 'manifest.json', report)
    dump(bookroot / '自动核验报告.json', report)
    lines = [f'# {book["title"]}', '',
             f'MinerU 4.0.11 本地混合模式（ONNX + llama.cpp），standard 档，扫描 OCR，保留图片和公式识别。', '',
             f'源书 {book["page_count"]} 页，解析页数 {len(coverage)} 页。已自动检查章节连续覆盖、解析页数和图片引用。未逐页人工核对，OCR 与公式仍可能存在识别误差。', '',
             '每章包含：`正文.md`、`完整分页.md`、`images/`、`middle_json.json`、`structured_content.json`、`原始页面.pdf`、`章节信息.json`、`自动核验.json`。`解析批次/` 保留分批原始解析输出，包括模型输出。', '',
             '`完整分页.md` 保留逐页标记；所有原始页面均另存为各章 PDF，用于查漏和核对。封面、版权、前言、目录、参考文献、索引和附录也已保留。', '',
             '| 文件夹 | 原 PDF 页码 | 页数 |', '| --- | ---: | ---: |']
    lines.extend(f'| [{r["name"]}]({r["name"]}/正文.md) | {r["start"]}–{r["end"]} | {r["page_count"]} |' for r in rows)
    (bookroot / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    hashes = []
    for path in sorted(bookroot.rglob('*')):
        if path.is_file() and path.name != 'SHA256SUMS.txt':
            assert path.stat().st_size < 100_000_000, (path, path.stat().st_size)
            hashes.append(hashlib.sha256(path.read_bytes()).hexdigest() + '  ' + path.relative_to(bookroot).as_posix())
    (bookroot / 'SHA256SUMS.txt').write_text('\n'.join(hashes) + '\n', encoding='utf-8')
    filename = ['Cell-Biology-Wang-Jinfa-MinerU-Local-Hybrid.zip', 'Cell-Biology-Laboratory-2e-MinerU-Local-Hybrid.zip'][book['id']]
    target = ROOT / 'output' / filename
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(bookroot.rglob('*')):
            if path.is_file():
                archive.write(path, arcname=path.relative_to(bookroot.parent).as_posix())
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
    ziphash = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT / 'output' / (filename + '.sha256')).write_text(ziphash + '  ' + filename + '\n')
    print('BOOK PACKED', target.name, target.stat().st_size, ziphash, flush=True)
print('ALL_READY', all_ready, flush=True)
