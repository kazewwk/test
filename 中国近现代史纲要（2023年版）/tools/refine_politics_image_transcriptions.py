#!/usr/bin/env python3
"""Add source-readable image text and link every adjudication to the final snapshot."""
import argparse,copy,collections,json,shutil
from pathlib import Path
import pymupdf
from mineru.parser import ParseResult
from mineru.render.contracts import RenderMode
from review_politics_ocr import read,write,digest,block_digest,text,HTML

def run(repo,working):
    central=repo/'校对记录/考研政治';plan=read(central/'politics_books_plan.json');ledger=read(central/'ocr-corrections.json');assert len(ledger)==352
    manuscript='我的修养要则\n一、加紧学习，抓住中心，宁精勿杂，宁专勿多。\n二、努力工作，要有计划，有重点，有条理。\n三、习作合一，要注意时间空间和条件，使之配合适当，要注意检讨和整理，要有发现和创造。\n四、要与自己的他人的一切不正确的思想意识作原则上坚决的斗争。\n五、适当地发扬自己的长处，具体地纠正自己的短处。\n六、永远不与群众隔离，向群众学习，并帮助他们。过集体生活，注意调研，遵守纪律。\n七、健全自己身体，保持合理的规律生活，这是自我修养的物质基础。'
    requests=[(2,369,0,'image_text','Ⅲ 中国美凯','侧栏标记旋转后逐字读取；按原图保留。'),
        (5,363,1,'image_text','扫一扫 辨真伪\n获取增值服务','封底扫码说明逐字核对；二维码原图保留。'),
        (3,137,6,'replace_text','申请人：尹典  \n2020年1月31日','原手写署名放大核对为尹典，吴兵为误识别。'),
        (3,137,5,'image_text','敬爱的党组织：\n此时我正在火神山医院建设现场，〔后续小字不能可靠辨认，完整内容见原图〕','手写入党申请书原图。开头可辨认文字已誊写，其余模糊小字未可靠誊写；不按语境补写。'),
        (3,170,5,'full_manuscript',manuscript,'原图为周恩来《我的修养要则》手稿。七条正文按简体字誊写；笔迹、标点和异体字保留原图。末尾题记部分模糊，未作可靠誊写。'),
        (3,170,6,'remove',None,'原手稿已作为完整原图和七条正文保存在区块5，删除重复的分块展示，原始图片文件仍保留。'),
        (3,170,7,'remove',None,'原手稿已作为完整原图和七条正文保存在区块5，删除重复的分块展示，原始图片文件仍保留。')]
    added=[];decisions=read(central/'round2/decisions.json')
    decisions['2475'].update(decision='source_confirmed_correction_needed',notes='最终署名放大图核对为尹典；先前小图误看为吴兵。已按原页修正。',evidence='p137-signature.png')
    write(central/'round2/decisions.json',decisions)
    for b in plan['books']:
        directory=repo/b['folder'];audits=read(directory/'ocr_review/page_audit.json');new=[r for r in requests if r[0]==b['id']]
        for s in b['sections']:
            folder=directory/s['folder'];raw=read(folder/'middle_json.json');changed=False
            for pg in raw['pages']:
                n=pg['page_idx']+s['pdf_first_page']
                for bid,p,i,action,value,note in new:
                    if p!=n:continue
                    z=next(z for z in pg.get('blocks',[]) if z['index']==i)
                    c={'book_id':bid,'pdf_page':p,'block_index':i,'action':action,'reason':note,'image_note':note,'verification':'visual comparison with original PDF; enlarged source image','review_round':2,'expected_block_sha256':block_digest(z),'before':copy.deepcopy(z),'original_bbox':z['bbox'],'source_sha256':b['sha256'],'candidate_ids':[2475] if (bid,p,i)==(3,137,6) else []}
                    if action=='remove':pg['blocks'].remove(z)
                    elif action=='replace_text':z['content']=[{'type':'text','content':value}];c['text']=value
                    else:
                        if action=='full_manuscript':
                            bb=[.565,.155,.875,.441];doc=pymupdf.open(working.parent/'source'/b['asset_name']);page=doc[p-1];r=page.rect
                            rel=f'images/ocr_review/page_{p:04d}_complete_manuscript.png';(folder/rel).parent.mkdir(parents=True,exist_ok=True)
                            page.get_pixmap(matrix=pymupdf.Matrix(5,5),clip=pymupdf.Rect(bb[0]*r.width,bb[1]*r.height,bb[2]*r.width,bb[3]*r.height)).save(folder/rel)
                            z['bbox']=bb;z['content'][0].update(bbox=bb,image_path=rel)
                        z['content']=[z['content'][0],{'type':'image_caption','content':[{'type':'text','content':value+'\n\n【核对注】'+note}]}]
                        c['text']=value
                    c['after']=None if action=='remove' else copy.deepcopy(z);c['after_block_sha256']=None if c['after'] is None else block_digest(z);added.append(c);changed=True
                if any(r[1]==n for r in new):
                    oldpage=audits[n-1];oldpage['blocks']=[x for x in oldpage['blocks'] if any(z['index']==x['index'] for z in pg.get('blocks',[]))]
                    for block in oldpage['blocks']:
                        z=next(z for z in pg['blocks'] if z['index']==block['index']);block['current_text']=text(z);block['bbox']=z['bbox'];block['final_block_sha256']=block_digest(z)
                        cs=[c for c in added if c['book_id']==b['id'] and c['pdf_page']==n and c['block_index']==block['index']]
                        if cs:block['visual_review']=cs[-1]['reason']
                    if (b['id'],n) in [(2,369),(5,363)]:oldpage['unresolved_image_transcription_blocks']=[]
                    if (b['id'],n)==(3,170):oldpage['unresolved_image_transcription_blocks']=[5]
                    oldpage['requires_text_transcription']=bool(oldpage['source_scan_unclear_blocks'] or oldpage['unresolved_image_transcription_blocks'])
                    oldpage['status']='差异候选已裁定；原图中有未可靠誊写文字' if oldpage['requires_text_transcription'] else '差异候选已裁定；原页保留'
                    oldpage['corrected_block_indices']=sorted(set(oldpage['corrected_block_indices']+[r[2] for r in new if r[1]==n]))
            if changed:
                result=ParseResult.from_dict(raw);write(folder/'middle_json.json',raw)
                (folder/'chapter.md').write_text(result.markdown());(folder/'all_content.md').write_text(result.markdown(mode=RenderMode.FULL));write(folder/'structured_content.json',result.structured_content())
            # Refresh page statuses, including chapters whose actual content was unchanged.
            table=['# 原页OCR核对','\n差异候选已逐项裁定。原扫描中不能可靠辨认的字保留原图并明确标注。','\n| 原PDF页 | 原页PDF | 状态 | 修订区块 |','|---:|---|---|---|']
            for pg in audits[s['pdf_first_page']-1:s['pdf_last_page']]:table.append(f'| {pg["pdf_page"]} | [原页](source.pdf#page={pg["chapter_page"]}) | {pg["status"]} | {", ".join(map(str,pg["corrected_block_indices"]))} |')
            (folder/'ocr_review.md').write_text('\n'.join(table)+'\n')
        cs=[c for c in ledger+added if c['book_id']==b['id']];write(directory/'ocr_review/corrections.json',cs)
        for p in audits:
            p['source_scan_unclear_blocks']=p.get('source_scan_unclear_blocks',[])
        reviews=read(directory/'ocr_review/round2/candidate_reviews.json')
        for r in reviews:
            d=decisions[str(r['id'])];r.update(d)
            matches=[c for c in cs if c.get('review_round')==2 and r['id'] in c.get('candidate_ids',[])]
            r['final_resolution']={'status':'source_unclear_annotated' if d['decision']=='source_scan_unclear' else 'revision_applied' if matches else 'current_content_retained',
                'revision_blocks':[{'pdf_page':c['pdf_page'],'block_index':c['block_index'],'action':c['action'],'after_block_sha256':c['after_block_sha256']} for c in matches]}
            if r['id']==2475:
                target=directory/'ocr_review/round2/p137-signature.png';shutil.copyfile(working/'p137-signature.png',target)
            if matches:decisions[str(r['id'])]['final_resolution']=r['final_resolution']
        write(directory/'ocr_review/round2/candidate_reviews.json',reviews);write(directory/'ocr_review/page_audit.json',audits)
        info=read(directory/'ocr_review/summary.json');info.update(source_confirmed_corrections=len(cs),incremental_revisions=sum(c.get('review_round')==2 for c in cs),
            pages_with_unresolved_image_transcriptions=[p['pdf_page'] for p in audits if p['unresolved_image_transcription_blocks']],pages_requiring_review=[p['pdf_page'] for p in audits if p['requires_text_transcription']],
            candidate_decision_counts=dict(collections.Counter(r['decision'] for r in reviews)))
        write(directory/'ocr_review/summary.json',info)
        full=[f'# {b["title"]}\n']
        for s in b['sections']:
            chapter=(directory/s['folder']/'chapter.md').read_text()
            # Reuse the chapter (which includes explicit source-unclear image notes) with chapter-relative image links.
            import re
            chapter=re.sub(r'(!\[[^\]]*\]\()(images/[^)]+)(\))',lambda m:m[1]+s['folder']+'/'+m[2]+m[3],chapter)
            full.append(f'\n<!-- Original PDF pages {s["pdf_first_page"]}-{s["pdf_last_page"]} -->\n'+chapter)
        (directory/'full.md').write_text('\n'.join(full))
        original=(directory/'ocr_review/README.md').read_text();original=__import__('re').sub(r'新增 \*\*\d+ 项修订\*\*，累计 \*\*\d+ 项修订记录\*\*',f'新增 **{info["incremental_revisions"]} 项修订**，累计 **{len(cs)} 项修订记录**',original)
        original=__import__('re').sub(r'仍有 \*\*\d+ 页\*\*',f'仍有 **{len(info["pages_requiring_review"])} 页**',original);(directory/'ocr_review/README.md').write_text(original)
        payload=json.dumps({'title':b['title'],'pages':audits},ensure_ascii=False).replace('<','\\u003c');template=HTML.replace('待复核页面','原图待誊写页面').replace("data.pages[n-1].status==='存在待复核差异'","data.pages[n-1].requires_text_transcription").replace('有交叉OCR差异','有已裁定交叉OCR差异')
        (directory/'ocr_review/index.html').write_text(template.replace('DATA',payload))
        cov=read(directory/'page_coverage.json')
        for p in audits:cov[p['pdf_page']-1]['mineru_blocks']=len(p['blocks']);cov[p['pdf_page']-1]['ocr_corrections']=sum(c['pdf_page']==p['pdf_page'] for c in cs)
        write(directory/'page_coverage.json',cov)
        for name in ['manifest.json','validation_report.json']:
            d=read(directory/name);d['ocr_review']=info;write(directory/name,d)
        shutil.copyfile(Path(__file__),directory/'tools'/Path(__file__).name)
        records=[{'path':f.relative_to(directory).as_posix(),'size':f.stat().st_size,'sha256':digest(f)} for f in sorted(directory.rglob('*')) if f.is_file() and f.name!='SHA256_manifest.json'];assert max(r['size'] for r in records)<100_000_000;write(directory/'SHA256_manifest.json',records)
    assert len(added)==7;write(central/'ocr-corrections.json',ledger+added)
    second=read(central/'round2/actions.json');write(central/'round2/actions.json',second+added);write(central/'round2/decisions.json',decisions)
    completed=read(central/'round2/completion.json');completed.update(incremental_revisions=len(second)+len(added),total_revision_records=len(ledger)+len(added),candidate_decision_counts=dict(collections.Counter(d['decision'] for d in decisions.values())),
        source_unclear_and_untranscribed_pages={str(b['id']):read(repo/b['folder']/'ocr_review/summary.json')['pages_requiring_review'] for b in plan['books']});write(central/'round2/completion.json',completed)
    for name in ['README.md','release-notes.md']:
        path=central/name;s=path.read_text().replace('新增 **45 项修订**','新增 **52 项修订**').replace('累计 **352 项记录**','累计 **359 项记录**');path.write_text(s)
    for f in working.glob('final-*.png'):shutil.copyfile(f,central/'round2'/f.name)
    shutil.copyfile(working/'p137-signature.png',central/'round2/p137-signature.png')
    print(json.dumps(completed,ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repository',type=Path,required=True);p.add_argument('--working',type=Path,required=True);a=p.parse_args();run(a.repository,a.working)
