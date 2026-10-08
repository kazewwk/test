#!/usr/bin/env python3
"""以中文章/节为主线生成双教材材料；不调用模型，不重新OCR。"""
import argparse, hashlib, json, os, re, shutil
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote
from mapping import RANGES, EXERCISE_HOME, SECONDARY

HEAD = re.compile(r'^#{1,6} (.+)$', re.M)
SEC = re.compile(r'^(?:## )?(第[一二三四五六七八九十]+节[^\n]*)$', re.M)
IMG = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
RESTORE_TITLE = '第四节 细胞信号转导的整合与控制'

def sha(data):
    return hashlib.sha256(data.encode() if isinstance(data,str) else data).hexdigest()

def dump(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def link(path,from_file):
    return os.path.relpath(path,from_file.parent).replace(os.sep,'/').replace(' ','%20')

def rebase(text,source_file,target_file):
    def replace(m):
        image=(source_file.parent/unquote(m.group(1))).resolve()
        assert image.is_file(), ('missing source image', source_file,m.group(1))
        return m.group().replace(m.group(1),link(image,target_file))
    return IMG.sub(replace,text)

def transform_en(text,source_file,target_file):
    # 降低英文标题级别，保留所有标题文字、段落、公式和图表。
    return rebase(HEAD.sub(lambda m:'#### '+m.group(1),text),source_file,target_file)

def rebase_links(text,source_file,target_file):
    text=rebase(text,source_file,target_file)
    def replace(m):
        href=m.group(1)
        if href.startswith(('https:','http:','mailto:','#')):return m.group()
        path,mark,anchor=href.partition('#')
        dest=(source_file.parent/unquote(path)).resolve()
        # 索引文件可能尚未生成；全部文件生成后由独立校验器检查。
        # LaTeX中的[X](t)不是Markdown链接，不更改这类数学表达式。
        if not dest.exists() and not path.lower().endswith(('.md','.json','.pdf','.zip','.bin')):
            return m.group()
        target=link(dest,target_file)+(mark+anchor if mark else '')
        return m.group().replace(href,target)
    return LINK.sub(replace,text)

def source_region(raw,start,end):
    return raw[start:end]

def build(cn,en,out):
    assert not out.exists(), '输出目录已存在，避免覆盖已有工作'
    out.mkdir(parents=True)
    src_cn=out/'来源/中文教材'
    src_en=out/'来源/英文教材'
    src_cn.mkdir(parents=True)
    shutil.copy2(cn/'merged/full.md',src_cn/'full.md')
    shutil.copytree(cn/'merged/images',src_cn/'images')
    # 保留英文全书阅读视图、全部内容视图及配图；图片路径保持原解析结构。
    for d in sorted(en.iterdir()):
        if not d.is_dir() or not re.match(r'^\d\d_',d.name):continue
        target=src_en/d.name
        target.mkdir(parents=True)
        for name in ['chapter.md','all_content.md','page_map.json']:
            if (d/name).exists():shutil.copy2(d/name,target/name)
        for images in d.glob('chunks/*/images'):
            shutil.copytree(images,target/images.relative_to(d))
    for name in ['manifest.json','validation_report.json']:
        shutil.copy2(en/name,src_en/name)
    shutil.copy2(cn/'reports/metadata.json',src_cn/'原解析元数据.json')
    shutil.copy2(cn/'章节整理清单.json',src_cn/'原章节清单.json')
    # 原中文PDF已经超过100MB，按95MB分片，支持精确还原。
    pdf=cn/'source/细胞生物学_第5版.pdf'
    parts_dir=src_cn/'原书PDF分片';parts_dir.mkdir()
    parts=[]
    with pdf.open('rb') as f:
        while data:=f.read(95_000_000):
            name=f'part-{len(parts)+1:04}.bin'
            (parts_dir/name).write_bytes(data)
            parts.append({'file':name,'bytes':len(data),'sha256':sha(data)})
    dump(parts_dir/'分片清单.json',{'original_name':pdf.name,'bytes':pdf.stat().st_size,
         'sha256':sha(pdf.read_bytes()),'parts':parts})
    (parts_dir/'README.md').write_text('# 中文原书PDF\n\n按序拼接两个分片即可恢复384页原书。\n\n```bash\ncat part-0001.bin part-0002.bin > 细胞生物学_第5版.pdf\n```\n')

    chapters={}; sections={}; cn_records=[]
    for f in sorted(cn.glob('chapters/*.md')):
        ch=int(f.name[:3]);raw=f.read_text()
        if ch==0:
            # 原前言文件的图片路径未经过章节重定向，以merged/full.md作路径基准。
            dest=out/'00_前言与目录/中文原文.md';dest.parent.mkdir()
            adapted=rebase(raw,src_cn/'full.md',dest)
            dest.write_text(adapted)
            cn_records.append({'id':'CN00','chapter':0,'source_file':str(f.relative_to(cn)),
                'source_sha256':sha(raw),'file':str(dest.relative_to(out)),
                'rendered_sha256':sha(adapted),'offsets':[0,len(raw)]})
            continue
        title=HEAD.search(raw).group(1)
        directory=out/f'{ch:02}_{title.split(" ",1)[1]}'
        directory.mkdir()
        chapters[ch]={'number':ch,'title':title,'folder':str(directory.relative_to(out)),'sections':[]}
        # 用已复制的full.md所在位置推导../merged/images，避免指回临时来源。
        raw=re.sub(r'\]\(\.\./merged/images/','](images/',raw)
        canonical=directory/'中文原文.md'
        canonical.write_text(rebase(raw,src_cn/'full.md',canonical))
        effective=raw
        if ch==11:
            effective=re.sub(r'^'+RESTORE_TITLE+r'$', '## '+RESTORE_TITLE,effective,flags=re.M)
        matches=list(SEC.finditer(effective))
        offsets=[0]+[m.start() for m in matches]+[len(effective)]
        # 章首段作为00，所有节完整保留到下一节；思考题不会截断正文。
        for n,(a,b) in enumerate(zip(offsets,offsets[1:])):
            sec_title='章首导读' if n==0 else matches[n-1].group(1)
            file=directory/'小节'/f'{n:02}_{sec_title}.md'
            file.parent.mkdir(exist_ok=True)
            block=effective[a:b]
            identifier=f'CN{ch:02}-S{n:02}'
            sections[ch,n]={'id':identifier,'chapter':ch,'section':n,'title':sec_title,
                'file':file,'text':block,'source_sha256':sha(block),'en':[],'secondary':[]}
            chapters[ch]['sections'].append({'section':n,'title':sec_title,
                'file':str(file.relative_to(out))})
        chapters[ch]['effective_sha256']=sha(effective)
        chapters[ch]['original_chapter_sha256']=sha(f.read_bytes())

    en_meta=json.loads((en/'manifest.json').read_text())
    meta={r['number']:r for r in en_meta['sections']}
    en_data={}
    for number in range(1,25):
        file=src_en/meta[number]['folder']/'chapter.md'
        raw=file.read_text();heads=list(HEAD.finditer(raw))
        en_data[number]={'file':file,'raw':raw,'heads':heads,'assignment':{}}
    groups=[]
    for number,first,last,ch,sec,topic in RANGES:
        d=en_data[number];heads=d['heads']
        assert (ch,sec) in sections or (ch,sec)==(0,0),(ch,sec)
        assert 0<=first<=last<len(heads),(number,first,last)
        for h in range(first,last+1):
            assert h not in d['assignment'],('duplicate',number,h)
            d['assignment'][h]=(ch,sec)
        start=0 if first==0 else heads[first].start()
        end=heads[last+1].start() if last+1<len(heads) else len(d['raw'])
        group={'id':f'EN{number:02}-H{first:03}-H{last:03}','en_chapter':number,
            'first_heading':first,'last_heading':last,'cn_chapter':ch,'cn_section':sec,
            'topic':topic,'first_title':heads[first].group(1),'last_title':heads[last].group(1),
            'source_file':str(d['file'].relative_to(out)),'offsets':[start,end],
            'source_sha256':sha(d['raw'][start:end]),'text':d['raw'][start:end]}
        groups.append(group)
        if ch:sections[ch,sec]['en'].append(group)
    exercises=defaultdict(list)
    for number,d in en_data.items():
        missing=[n for n in range(len(d['heads'])) if n not in d['assignment']]
        assert missing,number
        first=missing[0]
        assert missing==list(range(first,len(d['heads']))),('non-tail unmapped',number,missing)
        assert d['heads'][first].group(1)=='PROBLEMS',('unmapped body',number,first)
        start=d['heads'][first].start();text=d['raw'][start:]
        ch=EXERCISE_HOME[number]
        group={'id':f'EN{number:02}-EXERCISES','en_chapter':number,'first_heading':first,
            'last_heading':len(d['heads'])-1,'cn_chapter':ch,'cn_section':-1,
            'topic':'习题与参考文献','first_title':'PROBLEMS',
            'last_title':d['heads'][-1].group(1),'source_file':str(d['file'].relative_to(out)),
            'offsets':[start,len(d['raw'])],'source_sha256':sha(text),'text':text}
        groups.append(group);exercises[ch].append(group)
        for h in missing:d['assignment'][h]=(ch,-1)

    immuno=out/'补充专题/免疫系统.md';immuno.parent.mkdir()
    for g in groups:
        g['target_file']=str((sections[g['cn_chapter'],g['cn_section']]['file'] if
            g['cn_chapter'] and g['cn_section']>=0 else
            out/chapters[g['cn_chapter']]['folder']/'英文习题与参考文献.md' if g['cn_chapter'] else
            immuno).relative_to(out))
    for number,first,last,ch,sec,reason in SECONDARY:
        matched=[g for g in groups if g['en_chapter']==number and g['cn_section']!=-1 and
                 g['first_heading']<=last and g['last_heading']>=first]
        assert matched,(number,first,last)
        for g in matched:
            if (g['cn_chapter'],g['cn_section'])==(ch,sec):continue
            sections[ch,sec]['secondary'].append({'group':g,'reason':reason,
                'exact_first_heading':first,'exact_last_heading':last})

    def english_block(g,file):
        d=en_data[g['en_chapter']]
        body=transform_en(g['text'],d['file'],file)
        return (f'\n<a id="{g["id"]}"></a>\n\n### 英文补充：{g["topic"]}\n\n'
            f'> 对应中文板块：{g["topic"]}。英文来源：Molecular Biology of the Cell，第7版，'
            f'第{g["en_chapter"]}章；[本章完整原文]({link(d["file"],file)})。'
            f'物理PDF页码范围：{meta[g["en_chapter"]]["pdf_first_page"]}–'
            f'{meta[g["en_chapter"]]["pdf_last_page"]}（整章范围）。\n\n'
            f'<!-- BEGIN EN {g["id"]} -->\n{body}\n<!-- END EN {g["id"]} -->\n')

    for (ch,n),s in sections.items():
        file=s['file'];body=rebase(s['text'],src_cn/'full.md',file)
        intro=f'# {chapters[ch]["title"]} · {s["title"]}\n\n'
        intro+=f'[返回本章](../README.md) · [中文本章原文](../中文原文.md)\n\n'
        text=intro+f'<!-- BEGIN CN {s["id"]} -->\n{body}\n<!-- END CN {s["id"]} -->\n'
        if s['en']:
            text+='\n---\n\n## 对应英文内容\n'
            for g in s['en']:text+=english_block(g,file)
        elif n>0:
            text+='\n> 本节中文内容完整保留；英文教材未设置同主题的独立小节。\n'
            if (ch,n)==(9,6):
                text+='> 核基质与核纤层、染色质三维组织及生物分子凝聚体分别保留其概念边界，未作同义合并。\n'
        if s['secondary']:
            text+='\n## 跨章相关英文内容\n\n'
            for r in s['secondary']:
                g=r['group'];text+=f'- {r["reason"]}：[EN第{g["en_chapter"]}章 · {g["topic"]}]({link(out/g["target_file"],file)}#{g["id"]})。\n'
        file.write_text(text)
        cn_records.append({'id':s['id'],'chapter':ch,'section':n,'title':s['title'],
            'file':str(file.relative_to(out)),'source_sha256':s['source_sha256'],
            'rendered_sha256':sha(body),'offsets':None})

    for ch,gs in exercises.items():
        if ch==0:continue
        file=out/chapters[ch]['folder']/'英文习题与参考文献.md'
        file.write_text(f'# {chapters[ch]["title"]} · 英文习题与参考文献\n\n'+
            '\n'.join(english_block(g,file) for g in gs))
    immuno.write_text('# 补充专题：免疫系统\n\n中文教材没有独立免疫学章节。直接对应吞噬、信号、细胞死亡、黏着的内容已插入对应中文节；其余部分完整保留在这里。\n\n'+
        '\n'.join(english_block(g,immuno) for g in groups if g['cn_chapter']==0))

    outline=['# 双教材章节对照\n\n以中文教材16章、45节为主线；主文按主题段连续区间插入。交叉入口不表示两个主题同义。\n']
    summary_rows=[]
    for ch,c in chapters.items():
        directory=out/c['folder'];readme=directory/'README.md'
        lines=[f'# {c["title"]}\n','中文教材：《细胞生物学》第5版。英文补充：Molecular Biology of the Cell 第7版。\n',
            '[整章整合教材](整合教材.md) · [中文原文](中文原文.md)\n',
            '| 中文节 | 对应英文主章节 | 阅读材料 |\n|---|---|---|']
        integrated=f'# {c["title"]} · 双教材整合\n\n按中文节顺序保留正文，在每节末插入对应英文内容。\n'
        index=[f'# {c["title"]} · 制卡素材索引\n\n稳定编号可用于追溯制卡依据。英文补充保留原语言；本目录为制卡教材材料。\n\n',
            '| 素材编号 | 中文板块 | 英文来源与主题 |\n|---|---|---|']
        for n in range(len(c['sections'])):
            s=sections[ch,n];ens=sorted({g['en_chapter'] for g in s['en']})
            en_labels='、'.join('第'+str(x)+'章' for x in ens) or '保留中文原文'
            lines.append(f'| {s["title"]} | {en_labels} | [打开]({link(s["file"],readme)}) |')
            source=s['file'].read_text()
            # 整章版本由真实小节文件合成；只更改相对路径和首行标题层级。
            rebased=rebase_links(source,s['file'],directory/'整合教材.md')
            rebased=re.sub(r'^# ', '## ',rebased,count=1)
            integrated+='\n---\n\n'+rebased
            for g in s['en']:
                index.append(f'| {g["id"]} | {s["title"]} | EN第{g["en_chapter"]}章：[{g["topic"]}]({link(s["file"],directory/"制卡素材索引.md")}#{g["id"]}) |')
        if ch in exercises:
            lines.append('\n[英文习题与参考文献](英文习题与参考文献.md)\n')
        readme.write_text('\n'.join(lines)+'\n')
        (directory/'整合教材.md').write_text(integrated)
        (directory/'制卡素材索引.md').write_text('\n'.join(index)+'\n')
        count=sum(len(sections[ch,n]['en']) for n in range(len(c['sections'])))
        ens=sorted({g['en_chapter'] for g in groups if g['cn_chapter']==ch and g['cn_section']>=0})
        summary_rows.append(f'| [{c["title"]}]({c["folder"]}/README.md) | {len(c["sections"])-1} | '+
                            '、'.join(map(str,ens))+f' | {count} |')
        outline.append(f'\n## {c["title"]}\n\n'+rebase_links('\n'.join(lines[4:]),readme,out/'章节对照.md'))
    (out/'章节对照.md').write_text('\n'.join(outline))
    # 原分章文件把附录附在第16章末尾，额外提供独立入口，保留整章原文。
    tail=(cn/'chapters/016_第16章_细胞的社会联系.md').read_text()
    start=tail.index('<table><tr><td>年份</td><td>获奖人</td>')
    appendix=out/'补充专题/中文附录与索引.md'
    adapted=re.sub(r'\]\(\.\./merged/images/','](images/',tail[start:])
    appendix.write_text('# 中文附录：诺贝尔奖获奖情况与索引\n\n'+rebase(adapted,src_cn/'full.md',appendix))
    (out/'README.md').write_text('# 细胞生物学制卡\n\n'
        '以丁明孝等《细胞生物学》第5版的 **16章、45节** 为骨架，将 Molecular Biology of the Cell 第7版的对应英文原文和图表插入各节。中文原文完整保留，英文补充保持英文，来源明确标注。\n\n'
        '每章打开 `整合教材.md` 可连续阅读；`小节/` 可逐节阅读；`制卡素材索引.md` 提供稳定素材编号。跨章重复适用的内容提供链接入口。\n\n'
        '| 中文章 | 节数 | 对应英文主章节 | 英文主题块数 |\n|---|---:|---|---:|\n'+
        '\n'.join(summary_rows)+'\n\n'
        '[前言与目录](00_前言与目录/中文原文.md) · [章节对照](章节对照.md) · [中文附录与索引](补充专题/中文附录与索引.md) · [免疫补充专题](补充专题/免疫系统.md) · [完整中文原文](来源/中文教材/full.md) · [完整性校验](校验报告.json)\n\n'
        '中文第11章第四节原本被解析为普通文本，已按原教材目录恢复节标题；原解析正文保留。第16章原文末尾的诺贝尔奖附录、索引和封底内容保留在原文和相应整合材料中。\n\n'
        '来源目录保存中文全书解析、463张图、可还原的原PDF分片，以及英文全书28部分的阅读视图、全部内容视图和配图。英文完整原PDF及结构化解析仍可在仓库的 [Molecular Biology of the Cell](../Molecular%20Biology%20of%20the%20Cell/README.md) 目录核对。\n\n'
        'OCR文字沿用仓库既有解析。覆盖校验不代表逐字识别准确；术语、数值、公式和图注制卡时可对照原PDF。\n')
    mapping=[{k:v for k,v in g.items() if k!='text'} for g in groups]
    secondary=[{'cn_chapter':s['chapter'],'cn_section':s['section'],'en_group':r['group']['id'],
        'reason':r['reason'],'exact_first_heading':r['exact_first_heading'],
        'exact_last_heading':r['exact_last_heading']} for s in sections.values() for r in s['secondary']]
    dump(out/'主题映射.json',{'sources_commit':'249b285adb6773db494c4b48e9e409cb8dc1eb3c',
        'mapping_method':'按主题人工指定英文标题连续区间；零基标题索引及文本偏移可追溯',
        'english_groups':mapping,'cross_references':secondary,'chinese_regions':cn_records,
        'chinese_chapters':list(chapters.values()),'structure_fixes':[{'chapter':11,'title':RESTORE_TITLE}]})
    dump(out/'校验报告.json',{'status':'pending_validation'})
    print(json.dumps({'chapters':len(chapters),'sections':sum(len(c['sections'])-1 for c in chapters.values()),
        'english_groups':len(groups),'cross_references':len(secondary)},ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--chinese',type=Path,required=True)
    p.add_argument('--english',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();build(a.chinese.resolve(),a.english.resolve(),a.output.resolve())
