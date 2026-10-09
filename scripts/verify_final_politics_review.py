#!/usr/bin/env python3
"""Verify source coverage, immutable evidence, rendered assets and applied review decisions."""
import argparse,collections,json,re,subprocess
from pathlib import Path
import pymupdf
from mineru.parser import ParseResult
from review_politics_ocr import read,write,digest,block_digest,text

def run(repo):
    central=repo/'校对记录/考研政治';plan=read(central/'politics_books_plan.json');ledger=read(central/'ocr-corrections.json')
    decisions=read(central/'round2/decisions.json');completion=read(central/'round2/completion.json');new=[c for c in ledger if c.get('review_round')==2]
    assert len(new)==52 and len(ledger)==359
    status={'source_confirmed_correction_needed':'source_confirmed_correction_applied','source_graphic_replacement_needed':'source_graphic_restored','source_scan_unclear':'source_scan_unclear_annotated'}
    for key,d in decisions.items():
        if d['decision'] in status:
            matches=[c for c in new if int(key) in c.get('candidate_ids',[])]
            assert matches,key
            d['adjudication']=d['decision'];d['decision']=status[d['decision']]
            d['final_resolution']={'status':d['decision'],'revision_blocks':[{'book_id':c['book_id'],'pdf_page':c['pdf_page'],'block_index':c['block_index'],'action':c['action'],'after_block_sha256':c['after_block_sha256']} for c in matches]}
    page_count=section_count=image_count=0;checks=[]
    for b in plan['books']:
        directory=repo/b['folder'];audits=read(directory/'ocr_review/page_audit.json');records=read(directory/'SHA256_manifest.json')
        for r in records:assert (directory/r['path']).stat().st_size==r['size'] and digest(directory/r['path'])==r['sha256'],r['path']
        old=json.loads(subprocess.check_output(['git','show','HEAD:'+b['folder']+'/SHA256_manifest.json'],cwd=repo))
        original=[r for r in old if r['path'].startswith(('raw_chunks/','original_pdf/')) or r['path'].endswith(('/source.pdf','/source_page_text.json','/source_text.txt'))]
        for r in original:assert digest(directory/r['path'])==r['sha256'],r['path']
        before_by_page={};after_by_page={};images=0
        for s in b['sections']:
            folder=directory/s['folder'];raw=read(folder/'middle_json.json');ParseResult.from_dict(raw)
            oldraw=json.loads(subprocess.check_output(['git','show','HEAD:'+b['folder']+'/'+s['folder']+'/middle_json.json'],cwd=repo))
            for p in oldraw['pages']:before_by_page[p['page_idx']+s['pdf_first_page']]=p
            assert len(pymupdf.open(folder/'source.pdf'))==len(raw['pages'])==s['page_count'];section_count+=1
            for p in raw['pages']:
                n=p['page_idx']+s['pdf_first_page'];after_by_page[n]=p;page_count+=1
                assert len({z['index'] for z in p.get('blocks',[])})==len(p.get('blocks',[]))
                pagechanges=[c for c in new if c['book_id']==b['id'] and c['pdf_page']==n];changed_ids={c['block_index'] for c in pagechanges}
                before={z['index']:z for z in before_by_page[n].get('blocks',[])};after={z['index']:z for z in p.get('blocks',[])}
                assert set(before)-set(after)=={c['block_index'] for c in pagechanges if c['action']=='remove'}
                for i in set(before)&set(after):
                    if i not in changed_ids:assert block_digest(before[i])==block_digest(after[i]),(b['id'],n,i)
                for c in pagechanges:
                    assert block_digest(before[c['block_index']])==c['expected_block_sha256'],(b['id'],n,c['block_index'])
                    assert c['source_sha256']==b['sha256']
                    if c['action']!='remove':assert block_digest(after[c['block_index']])==c['after_block_sha256']
                assert audits[n-1]['pdf_page']==n and not audits[n-1]['unresolved_difference_blocks']
                assert [z['index'] for z in p.get('blocks',[])]==[z['index'] for z in audits[n-1]['blocks']]
                for z in p.get('blocks',[]):
                    assert not any(f in text(z) for f in ['The quick brown fox jumps over the lazy dog','The image provided is a QR code','The source image contains no discernible text']), (b['id'],n,z['index'])
            def image_paths(v):
                nonlocal images
                if isinstance(v,dict):
                    for k,x in v.items():
                        if k=='image_path' and x:assert (folder/x).is_file(),(folder,x);images+=1
                        else:image_paths(x)
                elif isinstance(v,list):
                    for x in v:image_paths(x)
            image_paths(raw)
            for name in ['chapter.md','all_content.md']:
                for path in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',(folder/name).read_text()):assert (folder/path).is_file(),(folder,name,path)
        assert sorted(after_by_page)==list(range(1,b['pages']+1))
        for path in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',(directory/'full.md').read_text()):assert (directory/path).is_file(),('full.md',path)
        # The image refinement is allowed to follow an earlier correction on the same block.
        review=directory/'ocr_review';rs=read(review/'round2/candidate_reviews.json')
        for r in rs:
            r.update(decisions[str(r['id'])]);assert (review/'round2'/r['evidence']).is_file(),r['evidence']
        write(review/'round2/candidate_reviews.json',rs)
        info=read(review/'summary.json');info['candidate_decision_counts']=dict(collections.Counter(r['decision'] for r in rs));write(review/'summary.json',info)
        for name in ['manifest.json','validation_report.json']:
            d=read(directory/name);d['ocr_review']=info
            if name=='validation_report.json':d.update(image_paths_checked=images,unchanged_original_files_checked=len(original),unmodified_blocks_verified=True,final_source_review_candidates_verified=len(rs))
            write(directory/name,d)
        index=(review/'index.html').read_text();scripts=re.findall(r'<script(?: [^>]*)?>(.*?)</script>',index,re.S)
        payload=json.loads(scripts[0]);assert payload['pages']==audits
        temp=Path('/tmp')/f'politics-review-{b["id"]}.js';temp.write_text(scripts[1]);subprocess.run(['node','--check',str(temp)],check=True,capture_output=True)
        records=[{'path':f.relative_to(directory).as_posix(),'size':f.stat().st_size,'sha256':digest(f)} for f in sorted(directory.rglob('*')) if f.is_file() and f.name!='SHA256_manifest.json'];assert max(r['size'] for r in records)<100_000_000;write(directory/'SHA256_manifest.json',records)
        image_count+=images;checks.append({'book_id':b['id'],'original_pages':b['pages'],'sections':len(b['sections']),'original_files_unchanged':len(original),'image_paths_checked':images,'candidate_resolutions_verified':len(rs)});print(b['id'],'validated',flush=True)
    write(central/'round2/decisions.json',decisions);completion['candidate_decision_counts']=dict(collections.Counter(d['decision'] for d in decisions.values()));write(central/'round2/completion.json',completion)
    assert page_count==1724 and section_count==65;assert not any('needed' in d['decision'] or d['decision']=='needs_source_revisit' for d in decisions.values())
    report={'source_pages_verified':page_count,'sections_verified':section_count,'image_paths_verified':image_count,'difference_candidates_adjudicated':len(decisions),'revision_records':len(ledger),'all_characters_manually_verified':False,'books':checks}
    write(central/'round2/final-validation.json',report);print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repository',type=Path,required=True);a=p.parse_args();run(a.repository)
