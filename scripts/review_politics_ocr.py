#!/usr/bin/env python3
"""Apply source-confirmed corrections, retain evidence, and package reviewed books."""
from __future__ import annotations
import argparse,copy,hashlib,html,json,re,shutil,unicodedata,zipfile
from pathlib import Path
from rapidfuzz.distance import Levenshtein

def read(p):return json.loads(Path(p).read_text())
def write(p,value):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def digest(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def block_digest(z):return hashlib.sha256(json.dumps(z,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def text(v):
    if isinstance(v,str):return v
    if isinstance(v,list):return ''.join(text(x) for x in v)
    if isinstance(v,dict):return text(v.get('content',''))
    return ''
def norm(s):
    s=re.sub(r'<[^>]*>','',s);s=re.sub(r'\\[a-zA-Z]+','',s)
    return ''.join(c for c in unicodedata.normalize('NFKC',s) if c.isalnum())
def apply(page,changes,doc,folder,number):
    for c in changes:
        z=next(z for z in page['blocks'] if z['index']==c['block_index'])
        # page_idx was renumbered for a chapter, but the block itself is unchanged.
        assert block_digest(z)==c['expected_block_sha256'],(number,c['block_index'])
        if c['action']=='remove':page['blocks'].remove(z)
        elif c['action']=='replace_text':z['content']=[{'type':'text','content':c['text']}]
        elif c['action']=='replace_substring':
            count=0
            def replace(v):
                nonlocal count
                if isinstance(v,dict):
                    for k,item in v.items():
                        if k=='content' and isinstance(item,str):
                            count+=item.count(c['old']);v[k]=item.replace(c['old'],c['new'])
                        else:replace(item)
                elif isinstance(v,list):
                    for item in v:replace(item)
            replace(z);assert count==c.get('occurrences',1),(number,c['old'],count)
        elif c['action']=='source_image':
            p=doc[number-1];bb=c['original_bbox'];rect=__import__('pymupdf').Rect(bb[0]*p.rect.width,bb[1]*p.rect.height,bb[2]*p.rect.width,bb[3]*p.rect.height)
            rel=f'images/ocr_review/page_{number:04d}_block_{z["index"]}.png';target=folder/rel;target.parent.mkdir(parents=True,exist_ok=True)
            p.get_pixmap(matrix=__import__('pymupdf').Matrix(3,3),clip=rect,alpha=False).save(target)
            z['type']='image';z['content']=[{'type':'image_body','index':z['index'],'bbox':bb,'image_path':rel,'content':''},
                {'type':'image_caption','content':[{'type':'text','content':'【核对注】'+c['image_note']}]}]
        else:raise ValueError(c['action'])

def audit_page(page,ref,section,number,changes,native,visual):
    lines=ref['lines'];blocks=[];used=set()
    for z in page.get('blocks',[]):
        bb=z.get('bbox');t=text(z)
        if not bb:continue
        selected=[]
        for i,l in enumerate(lines):
            x=sum(q[0] for q in l['polygon'])/4;y=sum(q[1] for q in l['polygon'])/4
            if bb[0]-.003<=x<=bb[2]+.003 and bb[1]-.003<=y<=bb[3]+.003:selected.append(l);used.add(i)
        independent=''.join(l['text'] for l in selected);a=norm(t);b=norm(independent)
        similarity=Levenshtein.normalized_similarity(a,b)
        differences=[]
        if z['type'] not in ['image','chart']:
            for op,i,j,k,l in Levenshtein.opcodes(a,b):
                if op!='equal':differences.append({'operation':op,'current':a[i:j],'independent':b[k:l],
                    'current_context':a[max(0,i-12):min(len(a),j+12)],'independent_context':b[max(0,k-12):min(len(b),l+12)]})
        matching_native=next((r for r in native if r['page']==number and r['block']==z['index']),None)
        review=visual.get((number,z['index']))
        blocks.append({'index':z['index'],'type':z['type'],'bbox':bb,'current_text':t,
            'independent_text':independent,'independent_lines':selected,'normalized_similarity':round(similarity,6),
            'differences':differences,'native_comparison':matching_native,'visual_review':review,
            'source_image_retained':z['type'] in ['image','chart']})
    # Looking at one highlighted word does not certify the whole block.
    unresolved=[b['index'] for b in blocks if b['differences']]
    unresolved_images=[c['block_index'] for c in changes if c['action']=='source_image' and '未' in c.get('image_note','')]
    outside=[lines[i] for i in range(len(lines)) if i not in used]
    current_all=norm(''.join(b['current_text'] for b in blocks))
    unmatched=[line for line in outside if line['confidence']>=.85 and len(norm(line['text']))>=4 and norm(line['text']) not in current_all]
    return {'pdf_page':number,'section':section['folder'],'chapter_page':number-section['pdf_first_page']+1,
        'original_pdf':'../'+section['folder']+'/source.pdf#page='+str(number-section['pdf_first_page']+1),
        'independent_ocr_completed':True,'source_sha256':ref['source_sha256'],
        'status':'存在待复核差异' if unresolved or unresolved_images or unmatched else '已完成自动核对；未宣称逐字人工校对',
        'unresolved_difference_blocks':unresolved,'unresolved_image_transcription_blocks':unresolved_images,
        'unmatched_independent_text_candidates':unmatched,
        'corrected_block_indices':[c['block_index'] for c in changes],'blocks':blocks,
        'native_text':ref['native_text'],'independent_ocr_lines':lines,
        'independent_ocr_parameters':{k:v for k,v in ref.items() if k not in ('lines','native_text')},
        'independent_lines_outside_detected_blocks':outside}

HTML='''<!doctype html><meta charset="utf-8"><title>OCR原页核对</title><style>
body{margin:0;font:16px system-ui;background:#f5f5f3;color:#222}header{padding:16px;border-bottom:1px solid #ddd}
main{display:grid;grid-template-columns:1fr 1fr;height:calc(100vh - 120px)}iframe{width:100%;height:100%;border:0}article{overflow:auto;padding:20px;background:white}button,select,input{font:inherit;margin:0 5px}pre{white-space:pre-wrap;line-height:1.8}details{border-top:1px solid #ddd;padding:10px 0}.note{color:#805514}
</style><header><strong id="title"></strong><p>左侧原教材PDF，右侧对应物理页OCR；差异是复核候选，不能直接当作错误。</p><button id="prev">上一页</button><input id="num" type="number" min="1" style="width:80px"><button id="next">下一页</button><select id="filter"><option value="all">全部页面</option><option value="review">待复核页面</option></select><span id="status"></span></header><main><iframe id="pdf"></iframe><article id="text"></article></main><script id="data" type="application/json">DATA</script><script>
const data=JSON.parse(document.getElementById('data').textContent);let n=1;
const e=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function show(){const p=data.pages[n-1];e('title').textContent=data.title;e('num').value=n;e('status').textContent=` / ${data.pages.length}　${p.status}`;e('pdf').src=p.original_pdf;
e('text').innerHTML=(p.unmatched_independent_text_candidates.length?`<details open><summary>区块之外的文字候选，需要对照原页裁定</summary><pre>${esc(p.unmatched_independent_text_candidates.map(x=>x.text).join(String.fromCharCode(10)))}</pre></details>`:'')+p.blocks.map(b=>`<details open><summary>区块 ${b.index} · ${esc(b.type)}${b.differences.length?' · 有交叉OCR差异':''}</summary><pre>${esc(b.current_text)}</pre>${b.differences.length?`<details><summary>独立OCR与差异</summary><pre>${esc(b.independent_text)}\n\n${esc(JSON.stringify(b.differences,null,2))}</pre></details>`:''}${b.visual_review?`<p class="note">${esc(b.visual_review)}</p>`:''}</details>`).join('');}
function move(d){do{n=Math.max(1,Math.min(data.pages.length,n+d));if(e('filter').value==='all'||data.pages[n-1].status==='存在待复核差异')break;}while(n>1&&n<data.pages.length);show();}
e('prev').onclick=()=>move(-1);e('next').onclick=()=>move(1);e('num').onchange=()=>{n=Math.max(1,Math.min(data.pages.length,Number(e('num').value)));show()};show();</script>'''

def run(a):
    import pymupdf
    from mineru.parser import ParseResult
    from mineru.render.contracts import RenderMode
    root=Path(a.root);plan=read(root/'politics_books_plan.json');corrections=read(root/'ocr-corrections.json')
    native=read(root/'native-differences.json');visits=read(root/'visual-review-decisions.json')
    summary=[]
    for book in plan['books']:
        directory=root/'reviewed'/book['folder'];records=read(directory/'SHA256_manifest.json')
        for r in records:assert digest(directory/r['path'])==r['sha256'],r['path']
        immutable={r['path']:r['sha256'] for r in records if r['path'].startswith(('raw_chunks/','original_pdf/')) or r['path'].endswith(('/source.pdf','/source_page_text.json','/source_text.txt'))}
        cs=[c for c in corrections if c['book_id']==book['id']];doc=pymupdf.open(root/'source'/book['asset_name']);assert digest(root/'source'/book['asset_name'])==book['sha256']
        visual={(v['page'],v['block']):v['decision'] for v in visits if v['book']==book['id']}
        # Confirmed corrections are review decisions even when no native comparison exists.
        for c in cs:visual[(c['pdf_page'],c['block_index'])]=c['reason']
        audit=[];full=[f'# {book["title"]}\n'];coverage=read(directory/'page_coverage.json')
        for section in book['sections']:
            folder=directory/section['folder'];raw=read(folder/'middle_json.json')
            for p in raw['pages']:
                number=p['page_idx']+section['pdf_first_page'];changes=[c for c in cs if c['pdf_page']==number]
                apply(p,changes,doc,folder,number)
                ref=read(root/'independent-ocr'/f'book-{book["id"]}-page-{number:04d}.json');assert ref['source_sha256']==book['sha256']
                audit.append(audit_page(p,ref,section,number,changes,[r for r in native if r['book']==book['id']],visual))
                coverage[number-1]['mineru_blocks']=len(p.get('blocks',[]));coverage[number-1]['ocr_corrections']=len(changes)
            write(folder/'middle_json.json',raw);result=ParseResult.from_dict(raw)
            (folder/'chapter.md').write_text(result.markdown());(folder/'all_content.md').write_text(result.markdown(mode=RenderMode.FULL));write(folder/'structured_content.json',result.structured_content())
            full.append(f'\n<!-- Original PDF pages {section["pdf_first_page"]}-{section["pdf_last_page"]} -->\n'+result.markdown(asset_base_url=section['folder']+'/'))
            table=['# 逐页OCR核对','\n差异候选不等于识别错误。原页与独立OCR均保留；不确定文字没有按推测替换。','\n| 原PDF页 | 原页PDF | 状态 | 已修正区块 |','|---:|---|---|---|']
            for p in audit[-section['page_count']:]:table.append(f'| {p["pdf_page"]} | [原页](source.pdf#page={p["chapter_page"]}) | {p["status"]} | {", ".join(map(str,p["corrected_block_indices"]))} |')
            (folder/'ocr_review.md').write_text('\n'.join(table)+'\n');(folder/'README.md').write_text((folder/'README.md').read_text()+'\n[逐页OCR核对记录](ocr_review.md)\n')
        assert [p['pdf_page'] for p in audit]==list(range(1,book['pages']+1))
        review=directory/'ocr_review';review.mkdir(exist_ok=True);write(review/'page_audit.json',audit);write(review/'corrections.json',cs)
        info={'book_id':book['id'],'title':book['title'],'original_pages':book['pages'],'independently_ocr_checked_pages':len(audit),
            'visual_reviewed_blocks':len(visual),'source_confirmed_corrections':len(cs),
            'pages_with_unresolved_differences':[p['pdf_page'] for p in audit if p['unresolved_difference_blocks']],
            'pages_with_unresolved_image_transcriptions':[p['pdf_page'] for p in audit if p['unresolved_image_transcription_blocks']],
            'pages_with_unmatched_independent_text':[p['pdf_page'] for p in audit if p['unmatched_independent_text_candidates']],
            'pages_requiring_review':[p['pdf_page'] for p in audit if p['status']=='存在待复核差异'],
            'all_characters_manually_verified':False,'character_accuracy_guaranteed':False,
            'comparison_engine':'RapidOCR ONNX PP-OCRv4 / rapidocr-onnxruntime 1.4.4; 144 dpi original PDF render',
            'comparison_run':'https://github.com/kazewwk/test/actions/runs/37904595224','source_sha256':book['sha256'],
            'original_pdf_and_raw_mineru_unchanged':True,'normalization':'NFKC and alphanumeric comparison; punctuation, layout and formulas still require source-page review.'}
        write(review/'summary.json',info)
        payload=json.dumps({'title':book['title'],'pages':audit},ensure_ascii=False).replace('<','\\u003c')
        (review/'index.html').write_text(HTML.replace('DATA',payload))
        (review/'README.md').write_text(f'# {book["title"]}：OCR原页核对\n\n全部 **{book["pages"]} 页**已渲染原PDF并进行独立中文OCR交叉比较；已查看 **{len(visual)} 个区块的差异局部及重点版面**，实施 **{len(cs)} 项确定修正**。\n\n'
            f'仍有 **{len(info["pages_requiring_review"])} 页**存在尚未裁定的交叉OCR差异、可能遗漏的文字或未可靠誊写的图像；候选包括独立OCR自身错误、扫描倾斜、模糊小字和分块边界问题，不能直接视为教材错误。此版本没有宣称全书逐字人工校对完成。\n\n'
            '[逐页证据](page_audit.json) · [修正前后记录](corrections.json) · [核对统计](summary.json) · [离线双栏原页核对器](index.html)\n\n'
            '下载完整ZIP后打开 `index.html`，可并排查看章节原PDF和每一物理页OCR。原始PDF、原生文字与 `raw_chunks/` 未经修改。无法可靠辨认的手写图像以原图保存并标注，未用推测填充。\n')
        (directory/'README.md').write_text((directory/'README.md').read_text()+'\n[OCR原页核对与修订记录](ocr_review/README.md)\n')
        (directory/'full.md').write_text('\n'.join(full));write(directory/'page_coverage.json',coverage)
        report=read(directory/'validation_report.json');report['ocr_review']=info;write(directory/'validation_report.json',report)
        manifest=read(directory/'manifest.json');manifest['ocr_review']=info;write(directory/'manifest.json',manifest)
        shutil.copy2(Path(__file__),directory/'tools'/Path(__file__).name);shutil.copy2(Path(__file__).with_name('audit_politics_ocr.py'),directory/'tools/audit_politics_ocr.py')
        for rel,expected in immutable.items():assert digest(directory/rel)==expected,rel
        image_count=0
        for f in directory.rglob('middle_json.json'):
            def check(v):
                nonlocal image_count
                if isinstance(v,dict):
                    for k,item in v.items():
                        if k=='image_path' and item:
                            assert (f.parent/item).is_file(),(f,item);image_count+=1
                        else:check(item)
                elif isinstance(v,list):
                    for item in v:check(item)
            check(read(f))
        report['image_paths_checked']=image_count;write(directory/'validation_report.json',report)
        records=[{'path':f.relative_to(directory).as_posix(),'size':f.stat().st_size,'sha256':digest(f)} for f in sorted(directory.rglob('*')) if f.is_file() and f.name!='SHA256_manifest.json']
        assert max(r['size'] for r in records)<100_000_000;write(directory/'SHA256_manifest.json',records)
        output=root/'reviewed-zips';output.mkdir(exist_ok=True);archive=output/book['archive']
        with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=5,allowZip64=True) as z:
            for f in sorted(directory.rglob('*')):
                if f.is_file():z.write(f,f.relative_to(directory.parent))
        with zipfile.ZipFile(archive) as z:assert z.testzip() is None
        (output/(archive.stem+'-SHA256SUMS.txt')).write_text(digest(archive)+'  '+archive.name+'\n')
        for name,src in [('manifest',directory/'manifest.json'),('validation',directory/'validation_report.json'),('OCR-review',review/'summary.json')]:shutil.copy2(src,output/(archive.stem+'-'+name+'.json'))
        summary.append({**info,'zip':archive.name,'zip_sha256':digest(archive),'zip_bytes':archive.stat().st_size,'files':len(records)+1});print(json.dumps(summary[-1],ensure_ascii=False),flush=True)
    write(root/'ocr-review-publication.json',summary)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',required=True);run(p.parse_args())
