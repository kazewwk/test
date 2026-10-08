#!/usr/bin/env python3
"""MinerU Hybrid CPU parsing, page-complete chapter assembly and publication files."""
from __future__ import annotations
import argparse,copy,hashlib,json,os,re,shutil,time,zipfile
from pathlib import Path

ROOT=Path(os.environ.get('POLITICS_WORKDIR','/tmp/politics-books'))
OUT=Path(os.environ.get('POLITICS_OUTDIR',str(ROOT/'parsed')))
PLAN=Path(os.environ.get('POLITICS_PLAN',str(Path(__file__).with_name('politics_books_plan.json'))))
LIMIT=95_000_000

def read_plan():return json.loads(PLAN.read_text())
def book_info(number):return next(b for b in read_plan()['books'] if b['id']==number)
def write_json(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def checksum(path):
    with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def verify_source(book):
    import pymupdf
    path=ROOT/'source'/book['asset_name']
    assert path.stat().st_size==book['size']
    assert checksum(path)==book['sha256']
    with pymupdf.open(path) as doc:assert len(doc)==book['pages']
    return path
def configure_cpu():
    from mineru.config import config
    import mineru_llama_cpp
    config.model.small_backend='onnx';config.model.vlm.engine='llama-cpp'
    config.model.vlm.max_concurrency=1
    threads=len(os.sched_getaffinity(0)) if hasattr(os,'sched_getaffinity') else (os.cpu_count() or 2)
    quota=Path('/sys/fs/cgroup/cpu.max')
    if quota.exists():
        q,p=quota.read_text().split()
        if q!='max':threads=min(threads,max(1,int(q)//int(p)))
    os.environ.setdefault('MINERU_INTRA_OP_NUM_THREADS',str(threads))
    os.environ.setdefault('MINERU_INTER_OP_NUM_THREADS','1')
    engine=mineru_llama_cpp.Engine
    class CpuEngine(engine):
        def __init__(self,*args,**kwargs):
            kwargs.setdefault('n_threads',threads);kwargs.setdefault('n_gpu_layers',0)
            kwargs.setdefault('n_parallel',1);super().__init__(*args,**kwargs)
    mineru_llama_cpp.Engine=CpuEngine

def parse(number,first,last):
    from mineru.parser import MinerUParser,ParseResult
    from mineru.parser.writer import FileBasedDataWriter
    from mineru.render.contracts import RenderMode
    configure_cpu();book=book_info(number);source=verify_source(book)
    assert 1<=first<=last<=book['pages']
    parser=MinerUParser(tier='standard',parse_mode=book['parse_mode'],image_analysis=True)
    target=OUT/book['folder']/'raw_chunks'/f'pages_{first:04d}-{last:04d}'
    if (target/'parse_complete.json').exists():return
    start=time.monotonic();print(f'START book={number} PDF={first}-{last} Hybrid standard/high mode={book["parse_mode"]}',flush=True)
    temporary=target.with_name(target.name+'.pending')
    if temporary.exists():shutil.rmtree(temporary)
    blank=[n for n in book.get('blank_pages',[]) if first<=n<=last]
    normal=[n for n in range(first,last+1) if n not in blank]
    if not blank:
        result=parser.parse(source,page_range=f'{first}-{last}')
        result.save(FileBasedDataWriter(str(temporary)))
    else:
        combined=None;run_records=[]
        runs=[]
        if normal:runs.append(('normal',','.join(map(str,normal)),parser))
        blank_parser=MinerUParser(tier='standard',parse_mode='txt',image_analysis=True)
        runs.extend((f'blank_{n:04d}',str(n),blank_parser) for n in blank)
        for name,selected,engine in runs:
            result=engine.parse(source,page_range=selected)
            run_dir=temporary/'runs'/name;result.save(FileBasedDataWriter(str(run_dir)))
            raw=json.loads((run_dir/'middle_json.json').read_text())
            raw=rewrite_images(raw,f'runs/{name}/')
            if combined is None:
                combined=copy.deepcopy(raw);combined['pages']=[]
                if 'docvortex_layout' in combined.get('extensions',{}):combined['extensions']['docvortex_layout']['pages']=[]
            combined['pages'].extend(raw['pages'])
            if 'docvortex_layout' in raw.get('extensions',{}):
                combined['extensions']['docvortex_layout']['pages'].extend(raw['extensions']['docvortex_layout']['pages'])
            run_records.append({'name':name,'selected_pages':selected,'parse_mode':engine.parse_mode,
                'reason':'Visually verified blank scan; original pixels/PDF retained; txt avoids reading paper shadows or reverse-page show-through.' if name.startswith('blank') else 'regular Hybrid parsing'})
        combined['pages'].sort(key=lambda p:p['page_idx'])
        write_json(temporary/'middle_json.json',combined)
        result=ParseResult.from_dict(combined)
        (temporary/'markdown.md').write_text(result.markdown())
        write_json(temporary/'structured_content.json',result.structured_content())
        write_json(temporary/'model_output.json',{'original_model_outputs':[f'runs/{r["name"]}/model_output.json' for r in run_records]})
        write_json(temporary/'parse_mode_overrides.json',run_records)
        blank_parser.close()
    saved=ParseResult.from_json((temporary/'middle_json.json').read_text())
    indices=[p.page_idx for p in saved.pages]
    assert indices==list(range(first-1,last)),(number,first,last,indices)
    (temporary/'all_content.md').write_text(saved.markdown(mode=RenderMode.FULL))
    write_json(temporary/'parse_complete.json',{'book_id':number,'first_pdf_page':first,'last_pdf_page':last,
       'page_indices':indices,'elapsed_seconds':round(time.monotonic()-start,3),
       'mode':'Hybrid','tier':'standard','effort':'high','parse_mode':book['parse_mode'],
       'mineru_version':'4.0.10','small_backend':'onnx','vlm_engine':'llama-cpp'})
    if target.exists():shutil.rmtree(target)
    temporary.rename(target);parser.close()
    print(f'DONE book={number} PDF={first}-{last} elapsed={time.monotonic()-start:.1f}s',flush=True)

def rewrite_images(value,prefix):
    if isinstance(value,dict):
        return {k:prefix+v if k=='image_path' and isinstance(v,str) and v else rewrite_images(v,prefix)
                for k,v in value.items()}
    if isinstance(value,list):return [rewrite_images(v,prefix) for v in value]
    return value

def split_large_files(directory):
    split=[]
    for file in list(directory.rglob('*')):
        if not file.is_file() or file.stat().st_size<100_000_000:continue
        info={'path':str(file.relative_to(directory)),'size':file.stat().st_size,'sha256':checksum(file),'parts':[]}
        with file.open('rb') as f:
            while data:=f.read(LIMIT):
                part=file.with_name(file.name+f'.part{len(info["parts"])+1:03d}');part.write_bytes(data)
                info['parts'].append({'path':str(part.relative_to(directory)),'size':len(data),'sha256':checksum(part)})
        file.unlink();split.append(info)
    write_json(directory/'split_files.json',split)

def finalize(number):
    import pymupdf
    from mineru.parser import ParseResult
    from mineru.render.contracts import RenderMode
    book=book_info(number);source=verify_source(book);directory=OUT/book['folder']
    doc=pymupdf.open(source);pages={};chunk_metadata=[]
    for first in range(1,book['pages']+1,read_plan()['chunk_pages']):
        last=min(first+read_plan()['chunk_pages']-1,book['pages'])
        chunk=directory/'raw_chunks'/f'pages_{first:04d}-{last:04d}'
        checkpoint=json.loads((chunk/'parse_complete.json').read_text())
        assert checkpoint['page_indices']==list(range(first-1,last))
        raw=json.loads((chunk/'middle_json.json').read_text())
        assert [p['page_idx'] for p in raw['pages']]==list(range(first-1,last))
        assert raw['metadata']['producer']['name']=='mineru'
        assert raw['extensions']['mineru']['tier']=='standard'
        for page in raw['pages']:
            assert page['page_idx']+1 not in pages
            pages[page['page_idx']+1]=(page,chunk,raw)
        chunk_metadata.append(checkpoint)
    assert sorted(pages)==list(range(1,book['pages']+1))
    original=directory/'original_pdf';original.mkdir(exist_ok=True)
    parts=[]
    with source.open('rb') as f:
        while data:=f.read(LIMIT):
            part=original/(source.name+f'.part{len(parts)+1:03d}');part.write_bytes(data)
            parts.append({'path':part.name,'size':len(data),'sha256':checksum(part)})
    write_json(original/'parts.json',{'output':source.name,'sha256':book['sha256'],'size':book['size'],'parts':parts})
    assert sum(p['size'] for p in parts)==book['size']
    coverage=[];toc=[];full=[f'# {book["title"]}\n'];warnings=[]
    for section in book['sections']:
        folder=directory/section['folder'];folder.mkdir(exist_ok=True)
        combined=None;native=[]
        for physical in range(section['pdf_first_page'],section['pdf_last_page']+1):
            raw_page,chunk,raw=pages[physical]
            if combined is None:
                combined=copy.deepcopy(raw);combined['pages']=[]
                if 'docvortex_layout' in combined.get('extensions',{}):combined['extensions']['docvortex_layout']['pages']=[]
            page=rewrite_images(copy.deepcopy(raw_page),f'../raw_chunks/{chunk.name}/')
            page['page_idx']=physical-section['pdf_first_page'];combined['pages'].append(page)
            layouts=raw.get('extensions',{}).get('docvortex_layout',{}).get('pages',[])
            for layout in layouts:
                if layout.get('page_idx')==physical-1:
                    layout=copy.deepcopy(layout);layout['page_idx']=physical-section['pdf_first_page']
                    combined['extensions']['docvortex_layout']['pages'].append(layout)
            pymupdf.TOOLS.mupdf_warnings(reset=True)
            text=doc[physical-1].get_text(sort=True)
            warning=pymupdf.TOOLS.mupdf_warnings(reset=True)
            if warning:warnings.append({'pdf_page':physical,'warning':warning})
            native.append({'pdf_page':physical,'chapter_page':page['page_idx']+1,'text':text})
            # FULL view includes auxiliary blocks, page headers, footers, footnotes and tables.
            view=ParseResult.from_dict({**combined,'pages':[page]}).markdown(mode=RenderMode.FULL)
            coverage.append({'pdf_page':physical,'section':section['folder'],'chapter_page':page['page_idx']+1,
                'mineru_blocks':len(page.get('blocks',[])),'mineru_markdown_characters':len(view.strip()),
                'source_native_text_characters':len(text.strip()),'source_pdf_retained':True,'has_parsed_page':True})
        combined['is_full_document']=True
        write_json(folder/'middle_json.json',combined)
        result=ParseResult.from_dict(combined)
        (folder/'chapter.md').write_text(result.markdown())
        (folder/'all_content.md').write_text(result.markdown(mode=RenderMode.FULL))
        write_json(folder/'structured_content.json',result.structured_content())
        write_json(folder/'source_page_text.json',native);write_json(folder/'page_map.json',section)
        (folder/'source_text.txt').write_text('\n\n'.join(f'=== Original PDF page {p["pdf_page"]} ===\n{p["text"]}' for p in native))
        split=pymupdf.open();split.insert_pdf(doc,from_page=section['pdf_first_page']-1,to_page=section['pdf_last_page']-1,links=True,annots=True)
        split.save(folder/'source.pdf',garbage=3,deflate=True);split.close()
        with pymupdf.open(folder/'source.pdf') as chapter:
            assert len(chapter)==section['page_count']
            for i,p in enumerate(chapter):assert p.get_text()==doc[section['pdf_first_page']-1+i].get_text()
        full.append(f'\n<!-- Original PDF pages {section["pdf_first_page"]}-{section["pdf_last_page"]} -->\n'+result.markdown(asset_base_url=section['folder']+'/'))
        (folder/'README.md').write_text(f'# {section["title"]}\n\n原始PDF第{section["pdf_first_page"]}–{section["pdf_last_page"]}页。\n\n'
            '[章节阅读](chapter.md) · [包含页眉页脚等的全部内容](all_content.md) · [原页PDF](source.pdf) · [原生文字](source_text.txt) · [页码映射](page_map.json)\n\n'
            '原始分批解析JSON、图片、Markdown和模型输出保存在全书的 `raw_chunks/`。\n')
        toc.append(f'| [{section["title"]}]({section["folder"]}/chapter.md) | {section["pdf_first_page"]}–{section["pdf_last_page"]} | {section["page_count"]} |')
    assert [p['pdf_page'] for p in coverage]==list(range(1,book['pages']+1))
    weak=[p for p in coverage if p['source_native_text_characters']>100 and p['mineru_markdown_characters']<100]
    write_json(directory/'page_coverage.json',coverage)
    write_json(directory/'manifest.json',{**book,'mineru_version':'4.0.10','mode':'Hybrid','tier':'standard','effort':'high',
        'image_analysis':True,'small_model_backend':'onnx','vlm_engine':'llama-cpp','chunks':chunk_metadata})
    report={'title':book['title'],'source_page_count':book['pages'],'parsed_page_count':len(coverage),
      'chapter_count':sum(s['kind']=='chapter' for s in book['sections']),'section_count':len(book['sections']),
      'missing_pages':[],'duplicate_pages':[],'pages_needing_review':weak,'source_sha256':book['sha256'],
      'character_accuracy_guaranteed':False,'original_content_preserved':'Exact original PDF bytes, section PDFs, native text and all MinerU Hybrid outputs.'}
    write_json(directory/'validation_report.json',report);write_json(directory/'source_pdf_warnings.json',warnings)
    (directory/'full.md').write_text('\n'.join(full))
    (directory/'README.md').write_text(f'# {book["title"]}\n\n原始PDF共{book["pages"]}页，使用MinerU 4.0.10 **Hybrid混合模式**解析：standard / high、ONNX与llama.cpp CPU，启用图片解析。\n\n'
        '[全文](full.md) · [页码覆盖](page_coverage.json) · [完整性检查](validation_report.json) · [来源和解析参数](manifest.json)\n\n'
        '正文章节、导论、前置页、结语及后记全部按原始PDF物理页码连续保存。各章节提供Markdown、完整内容视图、结构化JSON、配图引用、原页PDF和原生文本。`raw_chunks/`保留MinerU未经章节重组的全部输出。\n\n'
        '原始PDF全部字节在`original_pdf/`按不超过95MB分片保存。运行 `python tools/restore_original_pdf.py` 可精确恢复并核对SHA256。`split_files.json`记录其他超过100MB的文件分片。\n\n'
        '页面覆盖不代表逐字识别准确；原PDF与原生文本用于核对OCR、图表、公式及脚注。原文件读取警告保存在`source_pdf_warnings.json`。\n\n'
        '| 内容 | 原始PDF页码 | 页数 |\n|---|---|---:|\n'+'\n'.join(toc)+'\n')
    tools=directory/'tools';tools.mkdir(exist_ok=True)
    shutil.copy2(Path(__file__),tools/Path(__file__).name);shutil.copy2(PLAN,tools/PLAN.name)
    shutil.copy2(Path(__file__).with_name('restore_politics_original_pdf.py'),tools/'restore_original_pdf.py')
    # Verify all image paths in raw and chapter JSON before splitting or packaging.
    image_count=0
    for file in directory.rglob('middle_json.json'):
        def check(value):
            nonlocal image_count
            if isinstance(value,dict):
                for key,item in value.items():
                    if key=='image_path' and item:
                        assert (file.parent/item).is_file(),(file,item);image_count+=1
                    else:check(item)
            elif isinstance(value,list):
                for item in value:check(item)
        check(json.loads(file.read_text()))
    report['image_paths_checked']=image_count;report['missing_images']=[]
    write_json(directory/'validation_report.json',report)
    # Review weak pages before considering publication complete.
    assert not weak,('Pages need manual review',book['id'],weak)
    split_large_files(directory)
    records=[{'path':str(f.relative_to(directory)),'size':f.stat().st_size,'sha256':checksum(f)}
             for f in sorted(directory.rglob('*')) if f.is_file() and f.name!='SHA256_manifest.json']
    assert all(r['size']<100_000_000 for r in records)
    write_json(directory/'SHA256_manifest.json',records)
    archive=ROOT/book['archive']
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=5,allowZip64=True) as z:
        for file in sorted(directory.rglob('*')):
            if file.is_file():z.write(file,file.relative_to(directory.parent))
    with zipfile.ZipFile(archive) as z:assert z.testzip() is None
    info={'id':book['id'],'folder':book['folder'],'file':archive.name,'size':archive.stat().st_size,'sha256':checksum(archive),'files':len(records)+1}
    write_json(ROOT/f'archive-{number}.json',info)
    (ROOT/(archive.stem+'-SHA256SUMS.txt')).write_text(info['sha256']+'  '+archive.name+'\n')
    shutil.copy2(directory/'validation_report.json',ROOT/(archive.stem+'-validation.json'))
    shutil.copy2(directory/'manifest.json',ROOT/(archive.stem+'-manifest.json'))
    print('FINALIZED '+json.dumps(info,ensure_ascii=False),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['parse','finalize']);p.add_argument('--book',type=int,required=True)
    p.add_argument('--first',type=int);p.add_argument('--last',type=int);a=p.parse_args()
    if a.action=='parse':parse(a.book,a.first,a.last)
    else:finalize(a.book)
