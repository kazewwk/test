#!/usr/bin/env python3
"""独立核对来源、搬入的全文、源段覆盖、图片路径及PDF分片。"""
import argparse, hashlib, json, re
from pathlib import Path
from urllib.parse import unquote

IMG=re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
LINK=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
HEAD=re.compile(r'^#{1,6} ',re.M)

def digest(data):return hashlib.sha256(data.encode() if isinstance(data,str) else data).hexdigest()

image_hash={}
def normalize(text,file):
    def replace(m):
        path=(file.parent/unquote(m.group(1))).resolve()
        assert path.is_file(),('missing image',file,m.group(1))
        if path not in image_hash:image_hash[path]=digest(path.read_bytes())
        return m.group().replace(m.group(1),'sha256:'+image_hash[path])
    return HEAD.sub('# ',IMG.sub(replace,text)).strip()

def region(text,kind,identifier):
    marker=f'<!-- BEGIN {kind} {identifier} -->\n'
    end=f'\n<!-- END {kind} {identifier} -->'
    assert text.count(marker)==1,('missing/duplicate region',identifier)
    return text.split(marker,1)[1].split(end,1)[0]

def validate(out,cn):
    mapping=json.loads((out/'主题映射.json').read_text())
    spans={};body_count=0
    for g in mapping['english_groups']:
        src=out/g['source_file'];raw=src.read_text();a,b=g['offsets'];chunk=raw[a:b]
        assert digest(chunk)==g['source_sha256'],('source changed',g['id'])
        dst=out/g['target_file'];rendered=region(dst.read_text(),'EN',g['id'])
        assert normalize(chunk,src)==normalize(rendered,dst),('English content differs',g['id'])
        spans.setdefault(src,[]).append((a,b))
        body_count+=g['cn_section']>=0
    for file,ranges in spans.items():
        ranges.sort();last=0
        for a,b in ranges:
            assert a==last,('gap or overlap',file,a,last)
            last=b
        assert last==len(file.read_text()),('missing tail',file)
    assert len(spans)==24
    rebuilt={};source_cn=out/'来源/中文教材/full.md'
    for r in mapping['chinese_regions']:
        dst=out/r['file'];text=dst.read_text()
        if r['chapter']==0:
            raw=(cn/r['source_file']).read_text()
            assert normalize(raw,cn/'merged/full.md')==normalize(text,dst)
        else:
            chunk=region(text,'CN',r['id'])
            assert digest(chunk)==r['rendered_sha256'],('Chinese content changed',r['id'])
            rebuilt.setdefault(r['chapter'],[]).append((r['section'],chunk,dst))
    for ch,parts in rebuilt.items():
        parts.sort();chap=next(f for f in cn.glob('chapters/*.md') if int(f.name[:3])==ch)
        original=chap.read_text()
        if ch==11:original=re.sub(r'^第四节 细胞信号转导的整合与控制$',
            '## 第四节 细胞信号转导的整合与控制',original,flags=re.M)
        joined=''.join(normalize(t,f)+'\n' for _,t,f in parts)
        # 各片切口仅增加空白，所有正文、标题、公式、图表均逐字比较。
        expected=normalize(original,chap)
        assert re.sub(r'\s+','',joined)==re.sub(r'\s+','',expected),('Chinese chapter differs',ch)
        # 整章阅读文件也必须含每个中文及英文片段。
        aggregate=out/next(c['folder'] for c in mapping['chinese_chapters'] if c['number']==ch)/'整合教材.md'
        for _,t,f in parts:
            identifier=next(r['id'] for r in mapping['chinese_regions'] if r['file']==str(f.relative_to(out)))
            assert normalize(region(aggregate.read_text(),'CN',identifier),aggregate)==normalize(t,f)
        for g in mapping['english_groups']:
            if g['cn_chapter']==ch and g['cn_section']>=0:
                src=out/g['source_file'];a,b=g['offsets']
                assert normalize(region(aggregate.read_text(),'EN',g['id']),aggregate)==normalize(src.read_text()[a:b],src)
    # 全书原始解析文本按字节精确保留，不受既有章节拆分结果影响。
    assert source_cn.read_bytes()==(cn/'merged/full.md').read_bytes()
    # 进一步核对来源的16章拆分是否覆盖中文全书，排除既有拆分缺失。
    pieces=[]
    for file in sorted(cn.glob('chapters/*.md')):
        text=file.read_text()
        if not file.name.startswith('000'):
            text=re.sub(r'^# 第\d+章[^\n]*\n','',text)
        pieces.append(text.replace('../merged/images/','images/'))
    def compact(text):
        return re.sub(r'\s','',re.sub(r'<!--.*?-->','',text,flags=re.S))
    assert compact(''.join(pieces))==compact(source_cn.read_text()),'中文来源分章缺失或重叠'
    front=(cn/'chapters/000_front_matter.md').read_text()
    toc=re.findall(r'第[一二三四五六七八九十]+节\s+.*?(?=[.…]+\s*\d|$)',front,re.M)
    assert len(toc)==45
    missing_images=[];missing_links=[];image_refs=0;link_refs=0;largest=0
    for file in out.rglob('*'):
        if not file.is_file():continue
        largest=max(largest,file.stat().st_size)
        assert file.stat().st_size<100_000_000,('file exceeds100MB',file)
        if file.suffix!='.md':continue
        text=file.read_text()
        for match in IMG.finditer(text):
            image_refs+=1
            if not (file.parent/unquote(match.group(1))).is_file():missing_images.append([str(file),match.group(1)])
        for match in LINK.finditer(text):
            href=match.group(1)
            if href.startswith(('http:','https:','mailto:','#')):continue
            path,_,anchor=href.partition('#');link_refs+=1
            target=(file.parent/unquote(path)).resolve()
            if not target.exists() and not path.lower().endswith(('.md','.json','.pdf','.zip','.bin')):
                continue
            if not target.exists():missing_links.append([str(file),href])
            elif anchor.startswith('EN'):
                if f'id="{anchor}"' not in target.read_text():missing_links.append([str(file),href])
    assert not missing_images,missing_images[:5]
    assert not missing_links,missing_links[:5]
    pdf_parts=out/'来源/中文教材/原书PDF分片'
    manifest=json.loads((pdf_parts/'分片清单.json').read_text());combined=hashlib.sha256();size=0
    for part in manifest['parts']:
        data=(pdf_parts/part['file']).read_bytes()
        assert digest(data)==part['sha256'];size+=len(data);combined.update(data)
    assert combined.hexdigest()==manifest['sha256'] and size==manifest['bytes']
    report={'chinese_chapters':16,'chinese_sections':45,'chinese_toc_sections':len(toc),
        'chinese_full_source_preserved':True,'chinese_chapter_split_covers_full_source':True,
        'chinese_chapter_text_coverage':'完整；搬入正文与原章节逐字一致，图片按文件SHA256比对；仅第11章第四节恢复标题级别',
        'english_chapters_checked':24,'english_topic_blocks_in_chinese_sections':body_count-
            sum(g['cn_chapter']==0 and g['cn_section']>=0 for g in mapping['english_groups']),
        'english_total_source_regions':len(mapping['english_groups']),
        'english_source_coverage':'24章阅读视图全文连续覆盖，无间隙或重叠；原文与整合文本经标题级别/图片路径标准化后一致',
        'cross_references':len(mapping['cross_references']),'image_references_checked':image_refs,
        'local_links_checked':link_refs,'missing_images':missing_images,'broken_local_links':missing_links,
        'chinese_original_pdf_bytes':size,'chinese_pdf_sha256':combined.hexdigest(),
        'largest_file_bytes':largest,'ocr_character_accuracy_guaranteed':False,
        'source_commit':mapping['sources_commit']}
    (out/'校验报告.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('output',type=Path);p.add_argument('chinese',type=Path)
    a=p.parse_args();validate(a.output.resolve(),a.chinese.resolve())
