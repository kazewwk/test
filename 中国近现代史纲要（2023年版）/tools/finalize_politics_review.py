#!/usr/bin/env python3
"""Apply an incremental, hash-guarded source review to an existing parsed snapshot."""
from __future__ import annotations
import argparse,copy,collections,json,shutil
from pathlib import Path
import pymupdf
from mineru.parser import ParseResult
from mineru.render.contracts import RenderMode
from review_politics_ocr import read,write,digest,block_digest,text,apply,audit_page,HTML

def finalize(repo:Path,working:Path):
    central=repo/'校对记录/考研政治';plan=read(central/'politics_books_plan.json')
    actions=read(working/'actions.json');items=read(working/'items.json');decisions=read(working/'decisions.json')
    assert len(items)==len(decisions)==3883
    assert all(d['decision']!='needs_source_revisit' for d in decisions.values())
    previous=read(central/'ocr-corrections.json');assert len(previous)==307
    native=read(central/'native-differences.json');visual=read(central/'visual-review-decisions.json')
    summaries=[]; completed=[]
    for book in plan['books']:
        directory=repo/book['folder'];manifest=read(directory/'SHA256_manifest.json')
        for r in manifest:assert digest(directory/r['path'])==r['sha256'],r['path']
        immutable={r['path']:r['sha256'] for r in manifest if r['path'].startswith(('raw_chunks/','original_pdf/')) or r['path'].endswith(('/source.pdf','/source_page_text.json','/source_text.txt'))}
        src=working.parent/'source'/book['asset_name'];assert digest(src)==book['sha256'];doc=pymupdf.open(src)
        new=[copy.deepcopy(c) for c in actions if c['book_id']==book['id']]
        old=[c for c in previous if c['book_id']==book['id']];reviews=[]
        candidate_by_block=collections.defaultdict(list);candidate_by_page=collections.defaultdict(list)
        for item in items:
            if item['book']!=book['id']:continue
            review={**item,**decisions[str(item['id'])]}
            candidate_by_block[item['page'],item['block']].append(review)
            candidate_by_page[item['page']].append(review)
            reviews.append(review)
        review_dir=directory/'ocr_review'
        for evidence in sorted({r['evidence'] for r in reviews}):
            target=review_dir/'round2'/evidence;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(working/evidence,target)
        audit=[];full=[f'# {book["title"]}\n'];coverage=read(directory/'page_coverage.json')
        vis={(v['page'],v['block']):v['decision'] for v in visual if v['book']==book['id']}
        for section in book['sections']:
            folder=directory/section['folder'];raw=read(folder/'middle_json.json')
            for page in raw['pages']:
                n=page['page_idx']+section['pdf_first_page'];changes=[c for c in new if c['pdf_page']==n]
                for c in changes:
                    z=next(z for z in page.get('blocks',[]) if z['index']==c['block_index'])
                    assert block_digest(z)==c['expected_block_sha256'],(book['id'],n,c['block_index'])
                    if c['action']=='change_type':
                        z['type']=c['new_type']
                        if 'level' in c:z['level']=c['level']
                        else:z.pop('level',None)
                    elif c['action']=='mark_source_unclear':
                        replacement={**c,'action':'replace_substring'};apply(page,[replacement],doc,folder,n)
                        p=doc[n-1];bb=c['original_bbox'];rect=pymupdf.Rect(bb[0]*p.rect.width,bb[1]*p.rect.height,bb[2]*p.rect.width,bb[3]*p.rect.height)
                        rel=f'images/ocr_review/page_{n:04d}_block_{z["index"]}_unclear.png';target=folder/rel;target.parent.mkdir(parents=True,exist_ok=True)
                        p.get_pixmap(matrix=pymupdf.Matrix(4,4),clip=rect).save(target)
                        c['source_crop']=section['folder']+'/'+rel
                    else:
                        apply(page,[c],doc,folder,n)
                        if c['action']=='source_image':z.pop('level',None)
                    if 'expanded_bbox' in c:z['bbox']=c['expanded_bbox']
                    c['after']=None if c['action']=='remove' else copy.deepcopy(z)
                    c['after_block_sha256']=None if c['after'] is None else block_digest(z)
                    completed.append(c);vis[n,c['block_index']]=c['reason']
                all_changes=[c for c in old+new if c['pdf_page']==n]
                ref=read(working.parent/'independent-ocr'/f'book-{book["id"]}-page-{n:04d}.json')
                pg=audit_page(page,ref,section,n,all_changes,[x for x in native if x['book']==book['id']],vis)
                # Preserve computed disagreements; add explicit source adjudication instead of calling them unresolved.
                unknown=[]
                for block in pg['blocks']:
                    rs=candidate_by_block[n,block['index']]
                    changed=any(c['block_index']==block['index'] for c in changes)
                    if block['differences'] and not rs and not changed:unknown.append(block['index'])
                    block['source_review_candidates']=[r['id'] for r in rs]
                    block['source_review_decisions']=[r['decision'] for r in rs]
                    block['automatic_disagreements_adjudicated']=bool(rs or changed) if block['differences'] else True
                    block['final_block_sha256']=block_digest(next(z for z in page.get('blocks',[]) if z['index']==block['index']))
                assert not unknown,(book['id'],n,unknown)
                pg['automatic_unmatched_candidates']=pg.pop('unmatched_independent_text_candidates')
                pg['unmatched_independent_text_candidates']=[]
                pg['source_review_candidate_ids']=[r['id'] for r in candidate_by_page[n]]
                pg['unresolved_difference_blocks']=[]
                pg['source_scan_unclear_blocks']=[c['block_index'] for c in changes if c['action']=='mark_source_unclear']
                pg['requires_text_transcription']=bool(pg['source_scan_unclear_blocks'] or pg['unresolved_image_transcription_blocks'])
                pg['status']='差异候选已裁定；原图中有未可靠誊写文字' if pg['requires_text_transcription'] else '差异候选已裁定；原页保留'
                pg['all_characters_manually_verified']=False
                audit.append(pg);coverage[n-1]['mineru_blocks']=len(page.get('blocks',[]));coverage[n-1]['ocr_corrections']=len(all_changes)
            write(folder/'middle_json.json',raw);result=ParseResult.from_dict(raw)
            chapter=result.markdown();all_content=result.markdown(mode=RenderMode.FULL)
            for c in new:
                if c['action']=='mark_source_unclear' and section['pdf_first_page']<=c['pdf_page']<=section['pdf_last_page']:
                    crop=c['source_crop'].split('/',1)[1];note=f'\n\n【原页核对注：物理页{c["pdf_page"]}】{c["image_note"]}\n\n![褪色文字的原扫描]({crop})\n'
                    chapter+=note;all_content+=note
            (folder/'chapter.md').write_text(chapter);(folder/'all_content.md').write_text(all_content)
            write(folder/'structured_content.json',result.structured_content())
            text_full=result.markdown(asset_base_url=section['folder']+'/')
            for c in new:
                if c['action']=='mark_source_unclear' and section['pdf_first_page']<=c['pdf_page']<=section['pdf_last_page']:text_full+=f'\n\n【原页核对注】{c["image_note"]}\n\n![褪色文字的原扫描]({c["source_crop"]})\n'
            full.append(f'\n<!-- Original PDF pages {section["pdf_first_page"]}-{section["pdf_last_page"]} -->\n'+text_full)
            table=['# 原页OCR核对','\n差异候选已逐项裁定；褪色文字、手写材料或印章不能可靠誊写的地方保留原图并标注。','\n| 原PDF页 | 原页PDF | 状态 | 修订区块 |','|---:|---|---|---|']
            for p in audit[-section['page_count']:]:table.append(f'| {p["pdf_page"]} | [原页](source.pdf#page={p["chapter_page"]}) | {p["status"]} | {", ".join(map(str,p["corrected_block_indices"]))} |')
            (folder/'ocr_review.md').write_text('\n'.join(table)+'\n')
        assert [p['pdf_page'] for p in audit]==list(range(1,book['pages']+1))
        combined=old+new;info=read(review_dir/'summary.json')
        info.update(source_confirmed_corrections=len(combined),incremental_revisions=len(new),
            source_adjudicated_difference_candidates=len(reviews),candidate_decision_counts=dict(collections.Counter(r['decision'] for r in reviews)),
            pages_with_unresolved_differences=[],pages_with_unmatched_independent_text=[],
            pages_with_unresolved_image_transcriptions=[p['pdf_page'] for p in audit if p['unresolved_image_transcription_blocks']],
            pages_with_source_scan_unclear_text=[p['pdf_page'] for p in audit if p['source_scan_unclear_blocks']],
            pages_requiring_review=[p['pdf_page'] for p in audit if p['requires_text_transcription']],
            all_automatic_difference_candidates_adjudicated=True,all_characters_manually_verified=False,character_accuracy_guaranteed=False,
            source_page_review_scope='All remaining automatic difference candidates, their displayed source regions, and selected complete blocks. Does not certify unshown characters.',
            original_pdf_and_raw_mineru_unchanged=True)
        write(review_dir/'summary.json',info);write(review_dir/'page_audit.json',audit);write(review_dir/'corrections.json',combined)
        write(review_dir/'round2/candidate_reviews.json',reviews)
        payload=json.dumps({'title':book['title'],'pages':audit},ensure_ascii=False).replace('<','\\u003c')
        template=HTML.replace('待复核页面','原图待誊写页面').replace("data.pages[n-1].status==='存在待复核差异'","data.pages[n-1].requires_text_transcription")
        template=template.replace('有交叉OCR差异','有已裁定交叉OCR差异').replace('右侧对应物理页OCR；差异是复核候选，不能直接当作错误。','右侧对应物理页OCR；本轮差异候选已裁定，原扫描模糊及未可靠誊写的图像另有标记。')
        (review_dir/'index.html').write_text(template.replace('DATA',payload))
        (review_dir/'README.md').write_text(f'# {book["title"]}：OCR原页核对\n\n全部 **{book["pages"]} 物理页**已做独立OCR交叉核对；本轮剩余 **{len(reviews)} 项差异候选**已逐项查看原页差异区域并裁定，新增 **{len(new)} 项修订**，累计 **{len(combined)} 项修订记录**。\n\n'
            f'已关闭本轮自动差异候选。仍有 **{len(info["pages_requiring_review"])} 页**包含源扫描褪色、手写材料或印章的未可靠誊写文字，均保留原图和明确标记。不能由候选核对推导出所有字符均经人工校验，此版本不承诺文字100%准确。\n\n'
            '[逐页证据](page_audit.json) · [修正前后记录](corrections.json) · [本轮候选和原页截图](round2/candidate_reviews.json) · [核对统计](summary.json) · [离线双栏原页核对器](index.html)\n\n'
            '下载完整ZIP后打开 `index.html`，可并排查看章节原PDF和每一物理页OCR。原始PDF、原生文字与 `raw_chunks/` 未经修改；正文分类错误已经修复。标注缺字没有按语境补写。\n')
        (directory/'full.md').write_text('\n'.join(full));write(directory/'page_coverage.json',coverage)
        for name in ['manifest.json','validation_report.json']:
            value=read(directory/name);value['ocr_review']=info;write(directory/name,value)
        for rel,expected in immutable.items():assert digest(directory/rel)==expected,rel
        count=0
        for s in book['sections']:
            f=directory/s['folder']/'middle_json.json';raw=read(f)
            assert len(raw['pages'])==s['page_count'];assert len(pymupdf.open(f.parent/'source.pdf'))==s['page_count']
            def check(v):
                nonlocal count
                if isinstance(v,dict):
                    for k,x in v.items():
                        if k=='image_path' and x:assert (f.parent/x).is_file(),(f,x);count+=1
                        else:check(x)
                elif isinstance(v,list):
                    for x in v:check(x)
            check(raw)
            for pg in raw['pages']:
                ids=[z['index'] for z in pg.get('blocks',[])];assert len(set(ids))==len(ids)
            for c in new:
                if c['action']=='change_type' and c['new_type']=='text' and s['pdf_first_page']<=c['pdf_page']<=s['pdf_last_page']:assert text(c['after']) in (f.parent/'chapter.md').read_text()
        report=read(directory/'validation_report.json');report.update(image_paths_checked=count,original_immutable_files_checked=len(immutable),source_review_candidates_checked=len(reviews));write(directory/'validation_report.json',report)
        shutil.copyfile(Path(__file__),directory/'tools'/Path(__file__).name)
        records=[{'path':f.relative_to(directory).as_posix(),'size':f.stat().st_size,'sha256':digest(f)} for f in sorted(directory.rglob('*')) if f.is_file() and f.name!='SHA256_manifest.json']
        assert max(x['size'] for x in records)<100_000_000;write(directory/'SHA256_manifest.json',records)
        summaries.append({**info,'zip':book['archive'],'files':len(records)+1});print(book['id'],'pages',len(audit),'new revisions',len(new),'source images needing transcription',info['pages_requiring_review'],flush=True)
    assert len(completed)==len(actions)
    write(central/'ocr-corrections.json',previous+completed)
    target=central/'round2';target.mkdir(exist_ok=True)
    for f in working.iterdir():
        if f.is_file() and f.suffix in ['.json','.py']:shutil.copyfile(f,target/f.name)
    shutil.copytree(working/'evidence',target/'evidence',dirs_exist_ok=True)
    for f in working.glob('*.png'):shutil.copyfile(f,target/f.name)
    write(target/'actions.json',completed);write(central/'book-packages.json',summaries)
    overall={'original_pages':sum(b['pages'] for b in plan['books']),'chapter_and_other_sections':sum(len(b['sections']) for b in plan['books']),
        'remaining_difference_candidates':len(items),'all_remaining_candidates_adjudicated':True,'candidate_decision_counts':dict(collections.Counter(d['decision'] for d in decisions.values())),
        'incremental_revisions':len(completed),'total_revision_records':len(previous)+len(completed),
        'source_unclear_and_untranscribed_pages':{str(x['book_id']):x['pages_requiring_review'] for x in summaries},
        'all_characters_manually_verified':False,'character_accuracy_guaranteed':False}
    write(target/'completion.json',overall)
    docs=f'''# 五本考研政治教材：原页OCR核对

全部 **{overall['original_pages']} 物理页**、**{overall['chapter_and_other_sections']} 个章节及前后附属目录**均保留。第二轮剩余 **{len(items)} 项自动差异候选**已逐项对照保存的原页差异区域裁定，新增 **{len(completed)} 项修订**，累计 **{len(previous)+len(completed)} 项记录**。

自动OCR差异含独立OCR误识别、遗漏和版面错配，均不等同于教材错误。原扫描褪色、手写材料和印章中未可靠誊写的字保留原图并标记；全部候选裁定不能等同于全书逐字人工校对，也不能承诺100%文字准确。

[本轮统计](round2/completion.json) · [每项候选](round2/items.json) · [原页裁定](round2/decisions.json) · [本轮修订前后](round2/actions.json) · [累计修订](ocr-corrections.json) · [截图证据](round2/evidence) · [书籍打包信息](book-packages.json)

原教材PDF、原生文字和原始MinerU解析保留不变。每本书的 `ocr_review/index.html` 支持章节原页PDF和OCR并排查看；ZIP包含本书候选及所引用的原页截图。所有仓库文件均小于100MB，大PDF沿用分卷保存。

'''
    for b in plan['books']:docs+=f'- [{b["title"]}](../../{b["folder"]}/README.md)\n'
    (central/'README.md').write_text(docs)
    (central/'release-notes.md').write_text(docs.replace('(../../','(https://github.com/kazewwk/test/blob/main/'))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repository',type=Path,required=True);p.add_argument('--working',type=Path,required=True);a=p.parse_args();finalize(a.repository.resolve(),a.working.resolve())
