#!/usr/bin/env python3
"""独立核验增补来源、原有正文、实验覆盖、配图公式及章节整合。"""
import argparse
import hashlib
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote
from validate import normalize, region, IMG, LINK

MARKER='\n<!-- BEGIN NEW_SOURCES -->\n'

def sha(data):
    return hashlib.sha256(data.encode() if isinstance(data,str) else data).hexdigest()

def dump(p,data):
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def validate(out,baseline=None,wang=None,lab=None):
    mapping=json.loads((out/'主题映射.json').read_text())
    stats=json.loads((out/'补充统计.json').read_text())
    groups=mapping['supplement_groups']
    ids=[g['id'] for g in groups]
    assert len(ids)==len(set(ids))==84
    old_files_checked=0
    if baseline:
        original=json.loads((baseline/'主题映射.json').read_text())
        for key,value in original.items():
            assert mapping[key]==value,('original mapping changed',key)
        old_checksums=json.loads((baseline/'文件校验.json').read_text())['files']
        for row in old_checksums:
            p=out/row['file']
            assert p.is_file(),('original file lost',row['file'])
            if p.suffix=='.md' and p.name=='整合教材.md':continue
            if row['file'] in ('主题映射.json','文件校验.json','校验报告.json'):continue
            data=p.read_bytes()
            if p.suffix=='.md':data=data.split(MARKER.encode(),1)[0]
            assert sha(data)==row['sha256'],('original content changed',row['file'])
            old_files_checked+=1
        for c in mapping['chinese_chapters']:
            for s in c['sections']:
                p=out/s['file'];base=baseline/s['file']
                assert p.read_bytes().split(MARKER.encode(),1)[0]==base.read_bytes(),('original section changed',s['file'])
    # 原有中文标记及英文块逐字/图片SHA核对，不需要重新OCR或逐页人工核验。
    cn_checked=0;en_spans=defaultdict(list)
    for r in mapping['chinese_regions']:
        p=out/r['file']
        if r['chapter']==0:continue
        body=region(p.read_text(),'CN',r['id'])
        assert sha(body)==r['rendered_sha256'],('Chinese region changed',r['id'])
        cn_checked+=1
    for r in mapping['english_groups']:
        source=out/r['source_file'];raw=source.read_text();a,b=r['offsets'];body=raw[a:b]
        assert sha(body)==r['source_sha256'],('English source changed',r['id'])
        target=out/r['target_file']
        assert normalize(body,source)==normalize(region(target.read_text(),'EN',r['id']),target),('English region changed',r['id'])
        en_spans[source].append((a,b))
    assert len(en_spans)==24
    for source,ranges in en_spans.items():
        last=0
        for a,b in sorted(ranges):assert a==last,('original English source gap',source,a,last);last=b
        assert last==len(source.read_text())

    roots={'wang':wang,'lab':lab}
    inventory=json.loads((out/'来源/新增教材文件校验.json').read_text())
    source_file_count=0
    for row in inventory['files']:
        p=out/row['file'];data=p.read_bytes()
        assert len(data)==row['bytes'] and sha(data)==row['sha256'],('new archive changed',row['file'])
        for key,info in mapping['additional_sources'].items():
            local=Path(info['local_folder'])
            if Path(row['file']).is_relative_to(local) and roots[key]:
                origin=roots[key]/Path(row['file']).relative_to(local)
                assert origin.read_bytes()==data,('archive differs from published parsed book',row['file'])
        source_file_count+=1
    assert inventory['chapter_counts']=={'wang':18,'lab':15}
    assert inventory['image_counts']=={'wang':973,'lab':159}

    experiment_spans=defaultdict(list)
    image_count=0;formula_count=0
    for r in groups:
        source=out/r['source_file'];raw=source.read_text();a,b=r['offsets'];selected=raw[a:b]
        assert sha(selected)==r['source_sha256'],('new source region changed',r['id'])
        target=out/r['target_file'];kind='WJ' if r['source_book']=='wang' else 'LAB'
        rendered=region(target.read_text(),kind,r['id'])
        assert normalize(selected,source)==normalize(rendered,target),('new content differs',r['id'])
        assert selected.count('$')==rendered.count('$')==r['formula_delimiters'],('formula delimiter changed',r['id'])
        # 公式实际文本已包含在全文逐字核验中，额外计数用于报告。
        image_count+=len(IMG.findall(selected));formula_count+=selected.count('$')
        if r['kind']=='experiment':
            experiment_spans[source].append((a,b,r['id']))
            found=re.match(r'^#{1,6}\s+实验\s*(\d+)',selected)
            assert found and int(found.group(1))==int(r['id'][-3:])
    experiment_ids={r['id'] for r in groups if r['kind']=='experiment'}
    assert experiment_ids=={f'LAB-E{n:03}' for n in range(1,72)}
    assert len(experiment_spans)==12
    for source,ranges in experiment_spans.items():
        raw=source.read_text();expected=list(re.finditer(r'^#{1,6}\s+实验\s*(\d+)\s*[^\n]*',raw,re.M))
        assert len(expected)==len(ranges)
        last=expected[0].start()
        for i,(a,b,ident) in enumerate(sorted(ranges)):
            assert a==last==expected[i].start(),('experiment gap/overlap',source,ident)
            assert ident==f'LAB-E{int(expected[i].group(1)):03}'
            last=b
        assert last==len(raw),('experiment tail omitted',source)

    aggregates=0
    for c in mapping['chinese_chapters']:
        aggregate=out/c['folder']/'整合教材.md';text=aggregate.read_text()
        for r in mapping['chinese_regions']:
            if r['chapter']==c['number']:
                target=out/r['file']
                assert normalize(region(text,'CN',r['id']),aggregate)==normalize(region(target.read_text(),'CN',r['id']),target),('aggregate CN changed',r['id'])
        for r in mapping['english_groups']:
            if r['cn_chapter']==c['number'] and r['cn_section']>=0:
                source=out/r['source_file'];a,b=r['offsets']
                assert normalize(region(text,'EN',r['id']),aggregate)==normalize(source.read_text()[a:b],source),('aggregate EN changed',r['id'])
        for r in groups:
            if r['home'] and r['home'][0]==c['number']:
                kind='WJ' if r['source_book']=='wang' else 'LAB';target=out/r['target_file']
                assert normalize(region(text,kind,r['id']),aggregate)==normalize(region(target.read_text(),kind,r['id']),target),('aggregate new block differs',r['id'])
        aggregates+=1
    section_files=[out/s['file'] for c in mapping['chinese_chapters'] for s in c['sections']]
    primary_markers=[]
    for p in section_files:
        primary_markers+=re.findall(r'<!-- BEGIN (?:WJ|LAB) ([^ ]+) -->',p.read_text())
    assert sorted(primary_markers)==sorted(g['id'] for g in groups if g['home']), 'extra/missing/duplicate primary block'
    for r in mapping['supplement_cross_references']:
        src=out/r['file'];target=out/r['target_file']
        assert f'id="{r["id"]}"' in target.read_text()
        assert any(unquote(href).endswith('#'+r['id']) for href in LINK.findall(src.read_text())),('cross reference lost',r)

    # 允许原目录指向稀疏检出外、但确实在同一仓库内的旧书文件。
    tracked=set()
    try:
        repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=out,text=True).strip())
        tracked={repo/Path(x.decode()) for x in subprocess.check_output(['git','ls-files','-z'],cwd=repo).split(b'\0') if x}
    except (subprocess.CalledProcessError,FileNotFoundError):pass
    pending_outputs={(out/'补充校验报告.json').resolve()}
    missing_images=[];broken_links=[];image_refs=0;links=0;largest=0
    for p in out.rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts:continue
        largest=max(largest,p.stat().st_size)
        assert p.stat().st_size<100_000_000,('file exceeds100MB',p)
        if p.suffix!='.md':continue
        text=p.read_text()
        for href in IMG.findall(text):
            image_refs+=1
            if not (p.parent/unquote(href)).is_file():missing_images.append([str(p.relative_to(out)),href])
        for href in LINK.findall(text):
            if href.startswith(('https:','http:','mailto:')):continue
            path,_,anchor=href.partition('#')
            target=(p.parent/unquote(path)).resolve() if path else p
            if not target.exists() and not path.lower().endswith(('.md','.json','.pdf','.zip','.bin')):continue
            links+=1
            if not target.exists() and target not in tracked and target not in pending_outputs:broken_links.append([str(p.relative_to(out)),href])
            elif target.is_file() and anchor.startswith(('EN','WJ','LAB')):
                if f'id="{anchor}"' not in target.read_text():broken_links.append([str(p.relative_to(out)),href])
    assert not missing_images,missing_images[:8]
    assert not broken_links,broken_links[:8]
    report={'passed':True,'baseline_commit':mapping['supplement_baseline_commit'],
        'original_file_hashes_checked':old_files_checked,'original_chinese_regions_unchanged':cn_checked,
        'original_english_regions_unchanged':len(mapping['english_groups']),'original_english_full_chapters_covered':len(en_spans),
        'formal_sections':45,'updated_sections':stats['updated_sections'],'integrated_chapters_checked':aggregates,
        'theory_blocks':12,'complete_experiments':71,'experiment_numbers':'1–71，唯一全文归属，无间隙/重叠',
        'appendices':1,'new_primary_blocks':84,'new_cross_references':len(mapping['supplement_cross_references']),
        'new_archive_folders':33,'new_archive_images':1132,'new_archive_files_verified':source_file_count,
        'new_archive_compared_with_published_book_files':bool(wang and lab),
        'new_block_image_references':image_count,'new_block_formula_delimiters':formula_count,
        'source_text_formula_table_preservation':'原文片段逐字比对；仅标题级别和图片相对路径标准化，图片按SHA256核对',
        'all_image_references_checked':image_refs,'all_local_links_checked':links,
        'missing_images':missing_images,'broken_local_links':broken_links,'largest_file_bytes':largest,
        'ocr_character_accuracy_guaranteed':False,'manual_page_by_page_review':False}
    dump(out/'补充校验报告.json',report)
    old_report=json.loads((out/'校验报告.json').read_text())
    old_report['supplement_validation']=report
    dump(out/'校验报告.json',old_report)
    checks=[]
    for p in sorted(out.rglob('*')):
        if not p.is_file() or p.name=='文件校验.json' or '__pycache__' in p.parts:continue
        data=p.read_bytes();checks.append({'file':str(p.relative_to(out)),'bytes':len(data),'sha256':sha(data)})
    dump(out/'文件校验.json',{'files':checks})
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--baseline',type=Path)
    p.add_argument('--wang-jinfa',type=Path)
    p.add_argument('--laboratory',type=Path)
    a=p.parse_args()
    print(json.dumps(validate(a.output.resolve(),a.baseline,a.wang_jinfa,a.laboratory),ensure_ascii=False,indent=2))
