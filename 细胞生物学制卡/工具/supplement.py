#!/usr/bin/env python3
"""把两本已解析教材的增量素材补到现有16章结构；不重新OCR。"""
import argparse
import hashlib
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote
from build import HEAD, IMG, rebase, rebase_links, link

MARKER = '\n<!-- BEGIN NEW_SOURCES -->\n'
END = '<!-- END NEW_SOURCES -->\n'

def digest(data):
    return hashlib.sha256(data.encode() if isinstance(data,str) else data).hexdigest()

def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def own(path, addition):
    """只替换本工具拥有的尾部；原有正文的字节和编号保持不变。"""
    original=path.read_text().partition(MARKER)[0]
    path.write_text(original + MARKER + addition + '\n' + END)

def transform(raw, source, target):
    return rebase(HEAD.sub(lambda m: '#### '+m.group(1),raw),source,target)

def supplement(out, wang, lab, config_path):
    cfg=json.loads(config_path.read_text())
    mapping_path=out/'主题映射.json'
    mapping=json.loads(mapping_path.read_text())
    sections={(c['number'],s['section']):s for c in mapping['chinese_chapters'] for s in c['sections']}
    directories={c['number']:out/c['folder'] for c in mapping['chinese_chapters']}
    roots={'wang':wang,'lab':lab}
    src_roots={}
    source_files=[]
    chapter_counts={}
    image_counts={}
    for key,root in roots.items():
        info=cfg['source_books'][key]
        dest=out/info['local_folder'];dest.mkdir(parents=True,exist_ok=True)
        src_roots[key]=dest
        rows=[];chapters=0;images=0
        for d in sorted(root.iterdir()):
            if not d.is_dir() or not re.match(r'^\d\d_',d.name):continue
            chapters+=1
            target=dest/d.name;target.mkdir(parents=True,exist_ok=True)
            for name in ('正文.md','完整分页.md','章节信息.json'):
                shutil.copy2(d/name,target/name)
            if (d/'images').is_dir():
                shutil.copytree(d/'images',target/'images',dirs_exist_ok=True)
                images+=sum(p.is_file() for p in (target/'images').rglob('*'))
            original='https://github.com/kazewwk/test/tree/'+cfg['baseline_commit']+'/'+quote(info['repository_folder']+'/'+d.name)
            meta=json.loads((target/'章节信息.json').read_text())
            rows.append(f"| {d.name} | {meta['start']}–{meta['end']} | [正文]({quote(d.name+'/正文.md')}) · [完整分页]({quote(d.name+'/完整分页.md')}) · [原页PDF/结构化数据]({original}) |")
        shutil.copy2(root/'manifest.json',dest/'manifest.json')
        (dest/'README.md').write_text('# '+info['name']+' · 制卡补充来源\n\n'
            +'正文、完整分页、章节信息和全部配图按原解析文件逐字节复制。前言、参考文献和书后页面也保留在此。原页PDF及完整结构化输出可通过表中固定提交链接核对。\n\n'
            +'| 来源章节 | 原PDF页码 | 阅读及原页入口 |\n|---|---|---|\n'+'\n'.join(rows)+'\n')
        for p in sorted(dest.rglob('*')):
            if p.is_file() and p.name!='README.md':
                source_files.append({'file':str(p.relative_to(out)),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())})
        chapter_counts[key]=chapters;image_counts[key]=images
    source_inventory={'baseline_commit':cfg['baseline_commit'],'chapter_counts':chapter_counts,'image_counts':image_counts,'files':source_files}
    dump(out/'来源/新增教材文件校验.json',source_inventory)

    groups=[];by_home=defaultdict(list);cross=defaultdict(list)
    appendix=out/'补充专题/实验常用配方与换算.md'
    for item in cfg['items']:
        source=src_roots[item['source_book']]/item['source_path']
        raw=source.read_text();a,b=item['offsets'];selected=raw[a:b]
        assert digest(selected)==item['source_sha256'],('source changed',item['id'])
        home=tuple(item['home']) if item['home'] else None
        target=out/sections[home]['file'] if home else appendix
        record=dict(item,source_file=str(source.relative_to(out)),target_file=str(target.relative_to(out)),
            image_references=len(IMG.findall(selected)),formula_delimiters=selected.count('$'))
        groups.append(record)
        src_info=cfg['source_books'][item['source_book']]
        chapter=source.parent
        pdf='https://github.com/kazewwk/test/blob/'+cfg['baseline_commit']+'/'+quote(src_info['repository_folder']+'/'+chapter.name+'/原始页面.pdf')
        lines=[f'<a id="{item["id"]}"></a>',f'### {item["title"]}',
            f'> 补充目的：{item["reason"]}',
            f'> 来源：{src_info["name"]} / {chapter.name}；[原解析正文]({link(source,target)}) · [完整分页]({link(chapter/"完整分页.md",target)}) · [原页PDF]({pdf})；编号 `{item["id"]}`。']
        if item['note']:lines.append('> 制卡边界：'+item['note'])
        family='WJ' if item['source_book']=='wang' else 'LAB'
        lines+=['',f'<!-- BEGIN {family} {item["id"]} -->',transform(selected,source,target),f'<!-- END {family} {item["id"]} -->','']
        block='\n'.join(lines)
        if home:by_home[home].append((record,block))
        else:
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text('# 实验常用配方与换算\n\n按实验教程附录集中保留换算、试剂配制、保养和培养基。\n\n'+block)
        for sec in item['secondary']:
            cross[tuple(sec)].append(record)
    cross_records=[]
    for key,section in sections.items():
        if not by_home[key] and not cross[key]:continue
        target=out/section['file'];parts=['---','## 新增教材补充','']
        for kind,heading in [('theory','王金发教材：新增案例与图解'),('experiment','实验教程：操作材料')]:
            blocks=[b for r,b in by_home[key] if r['kind']==kind]
            if blocks:parts+=['## '+heading,'']+blocks
        if cross[key]:
            parts+=['## 对应的跨章补充入口','']
            for record in cross[key]:
                dest=out/record['target_file'];href=link(dest,target)+'#'+record['id']
                parts.append(f'- [{record["title"]}]({href})（`{record["id"]}`；全文归属见链接）')
                cross_records.append({'id':record['id'],'file':section['file'],'target_file':record['target_file'],'home':record['home']})
        own(target,'\n'.join(parts))

    chapter_stats=[]
    for c in mapping['chinese_chapters']:
        directory=directories[c['number']];integrated=directory/'整合教材.md'
        text=f'# {c["title"]} · 四教材整合\n\n沿用第5版节顺序，保留中文正文与原有英文补充，在对应小节补入王金发教材的新案例、图解和实验教程的操作材料。\n'
        rows=[];primary=[];secondary=[]
        for section in c['sections']:
            key=(c['number'],section['section']);f=out/section['file']
            content=f.read_text()
            content=re.sub(r'^# (.+)$',r'## \1',content,count=1,flags=re.M)
            text+='\n---\n\n'+rebase_links(content,f,integrated)
            for record,_ in by_home[key]:
                primary.append(record)
                rows.append(f'| `{record["id"]}` | 本节全文 | {section["title"]} | [{record["title"]}]({link(f,directory/"制卡素材索引.md")}#{record["id"]}) |')
            for record in cross[key]:
                secondary.append(record)
                rows.append(f'| `{record["id"]}` | 跨章入口 | {section["title"]} | [{record["title"]}]({link(out/record["target_file"],directory/"制卡素材索引.md")}#{record["id"]}) |')
        integrated.write_text(text)
        wn=sum(r['kind']=='theory' for r in primary);ln=sum(r['kind']=='experiment' for r in primary)
        stats=dict(chapter=c['number'],title=c['title'],folder=c['folder'],theory_blocks=wn,experiments=ln,cross_references=len(secondary))
        chapter_stats.append(stats)
        extra='## 新增教材素材\n\n'
        extra+=f'王金发教材全文补充 {wn} 块；实验全文 {ln} 个；对应跨章入口 {len(secondary)} 个。\n\n'
        extra+='| 稳定编号 | 入口类型 | 本章小节 | 内容 |\n|---|---|---|---|\n'+'\n'.join(rows)
        if not rows:extra+='\n本章已有内容完整保留，未发现需要全文追加的缺口。'
        own(directory/'制卡素材索引.md',extra)
        own(directory/'README.md','## 两本新增来源的补充\n\n'+f'本章补入王金发教材 {wn} 块、实验教程 {ln} 个实验，另有 {len(secondary)} 个跨章入口。参见 [新增素材索引](制卡素材索引.md) 与 [全书补充说明](../补充说明.md)。')

    mapping['supplement_baseline_commit']=cfg['baseline_commit']
    mapping['additional_sources']=cfg['source_books']
    mapping['supplement_mapping_method']=cfg['mapping_method']
    mapping['supplement_groups']=groups
    mapping['supplement_cross_references']=cross_records
    mapping['supplement_review_decisions']={'already_covered':cfg['already_covered'],'excluded_source_text':cfg['excluded_source_text']}
    dump(mapping_path,mapping)
    theory=sum(r['kind']=='theory' for r in groups);experiments=sum(r['kind']=='experiment' for r in groups)
    changed=sum(bool(by_home[key] or cross[key]) for key in sections)
    report=['# 两本新增教材的补充说明','',
        '沿用第5版教材的16章、45节主线及原有153个英文素材块。先对照现有小节正文，区分已经覆盖的机制与缺少的实验细节、案例、表图；每块新增内容只有一个全文归属，其他适用小节提供链接。',
        '',f'本次补入 **{theory} 个王金发教材案例/图解块、{experiments} 个完整实验、1 份通用实验附录**，共更新 {changed} 个正式小节。原来的中文、英文正文及稳定编号保持不变，16章整合教材与素材索引同步更新。',
        '', '两本新增来源的全部33个章节/前后页面文件夹均保存正文、完整分页和全部1132张配图。新增制卡块仅改动标题级别和相对图片路径，公式、表格、原图和原文内容保留。原页PDF和完整结构化输出通过固定版本链接追溯。未重新OCR，也未进行逐页人工核验。',
        '', '[王金发来源](来源/王金发教材/README.md) · [实验教程来源](来源/实验教程/README.md) · [通用配方与换算](补充专题/实验常用配方与换算.md) · [机器校验](补充校验报告.json) · [映射与源码区间](主题映射.json)',
        '', '## 各章补充量','', '| 第5版章节 | 王金发全文块 | 实验全文 | 跨章入口 |','|---|---:|---:|---:|']
    for s in chapter_stats:
        report.append(f'| [{s["title"]}]({quote(s["folder"]+"/制卡素材索引.md")}) | {s["theory_blocks"]} | {s["experiments"]} | {s["cross_references"]} |')
    report+=['','## 王金发教材中的新增内容','','| 编号 | 补入位置 | 缺口/用途 |','|---|---|---|']
    for r in groups:
        if r['kind']=='theory':report.append(f'| `{r["id"]}` | [{r["title"]}]({quote(r["target_file"])}#{r["id"]}) | {r["reason"]} |')
    report+=['','## 实验全文的归属','','目的、原理、仪器材料、试剂配方、操作、结果判读、注意事项与思考题按原文保存；原实验未设置的栏目不虚构。多个章节适用时只放一份全文。','','| 实验编号 | 实验 | 主归属小节 |','|---|---|---|']
    for r in groups:
        if r['kind']=='experiment':report.append(f'| `{r["id"]}` | {r["title"]} | [{r["home"][0]}.{r["home"][1]}]({quote(r["target_file"])}#{r["id"]}) |')
    report+=['','## 已覆盖内容的处理','','| 主题 | 现有位置 | 处理 |','|---|---|---|']
    for row in cfg['already_covered']:report.append('| '+' | '.join(row)+' |')
    report+=['','## 原文边界和识别问题','','原文档案完整保留；学习材料明确标注以下疑点，避免把来源冲突或识别错字直接做成知识卡。']
    for r in groups:
        if r['note']:report+=['',f'- `{r["id"]}`：{r["note"]}']
    report+=['','以下来源区间不计入制卡正文，但仍保存在来源全章：','','| 对应编号 | 区间说明 | 原因 |','|---|---|---|']
    for row in cfg['excluded_source_text']:report.append('| '+' | '.join(row)+' |')
    (out/'补充说明.md').write_text('\n'.join(report)+'\n')
    own(out/'README.md','## 王金发教材与实验教程补充\n\n'+f'已按现有16章45节补入 {theory} 个新案例/图解、全部 {experiments} 个实验及实验通用附录。各章 `整合教材.md`、小节和素材索引已同步。\n\n'
        +'[补充内容与逐项归属](补充说明.md) · [实验配方与换算](补充专题/实验常用配方与换算.md) · [新增校验](补充校验报告.json)\n\n'
        +'来源增加 [王金发教材](来源/王金发教材/README.md) 与 [实验教程](来源/实验教程/README.md)，保存完整阅读视图和全部图片；新素材沿用原始公式、表格与图注，并保留固定版本原页入口。')
    own(out/'章节对照.md','## 两本新增教材的对应补充\n\n以小节缺口为单位归属；71个实验各有唯一全文位置。完整逐项对照见 [补充说明](补充说明.md)，机器可读记录见 `主题映射.json` 的 `supplement_groups` 与 `supplement_cross_references`。')
    own(out/'工具/README.md','## 在原有双教材基础上追加两本已解析书\n\n先使用原 `build.py` 生成双教材基础目录，再运行：\n\n```bash\n'
        +'python supplement.py --output ../ --wang-jinfa /path/to/细胞生物学（王金发） --laboratory /path/to/细胞生物学实验教程_第2版\n'
        +'python validate_supplements.py --output ../ --baseline /path/to/原双教材目录\n```\n\n'
        +'`supplement_mapping.json` 固定每块原文的字符区间、SHA-256、唯一主归属和其他适用节。`supplement.py` 仅替换自有补充标记内的内容，支持重复运行；原中文/英文正文不改写。校验器检查原正文保留、新块一致性、71个实验完整覆盖、配图、公式、整合视图、链接、原始来源哈希和100MB单文件限制。')
    summary={'theory_blocks':theory,'experiments':experiments,'appendices':1,'updated_sections':changed,
        'chapters':chapter_stats,'cross_references':len(cross_records),'source_chapter_folders':chapter_counts,'source_images':image_counts}
    dump(out/'补充统计.json',summary)
    return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--wang-jinfa',type=Path,required=True)
    parser.add_argument('--laboratory',type=Path,required=True)
    parser.add_argument('--mapping',type=Path,default=Path(__file__).with_name('supplement_mapping.json'))
    args=parser.parse_args()
    print(json.dumps(supplement(args.output.resolve(),args.wang_jinfa.resolve(),args.laboratory.resolve(),args.mapping),ensure_ascii=False,indent=2))
