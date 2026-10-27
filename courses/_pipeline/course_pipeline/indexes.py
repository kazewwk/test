from pathlib import Path
from urllib.parse import quote
from .common import load,write_json,atomic_text,seconds_label,utcnow


def update_series_index(rows, output_root, series):
    root=Path(output_root)/series
    root.mkdir(parents=True,exist_ok=True)
    selected=[r for r in rows if r['series']==series]
    table=f'# {series} 播放与处理索引\n\n'
    table+='机器处理完成不等于人工确认。各节疑点见质量报告；原始截图和两套转写保留。\n\n'
    table+='| 分 P | 课程标题 | 时长 | 状态 | 复核项 |\n|---:|---|---:|---|---:|\n'
    issues=[];completed=0
    for r in selected:
        lesson=root/r['directory'];qpath=lesson/'qc_report.json';manifest=lesson/'manifest.json'
        status='待处理';count=0;title=r['title'].replace('|','｜')
        if manifest.exists() and qpath.exists():
            m=load(manifest);q=load(qpath)
            if m['source']['drive_file_id']==r['drive_file_id']:
                completed+=1;count=len(q['issues']);status='机器处理完成，待复核' if count else '机器处理完成'
                title=f"[{title}]({quote(r['directory'])}/lecture_full.md)"
                issues.extend({'drive_file_id':r['drive_file_id'],'lesson_directory':r['directory'],**i} for i in q['issues'])
        table+=f"| {r['part']:03d} | {title} | {seconds_label(r.get('duration_seconds') or 0)} | {status} | {count} |\n"
    atomic_text(root/'index.md',table)
    atomic_text(root/'README.md',f'# {series}\n\n[课程索引](index.md) · [质量报告](quality_summary.json)\n\n'
                f'共 {len(selected)} 个视频，已处理 {completed} 个，待处理 {len(selected)-completed} 个。'
                '未提供人工基准时不声明准确率。\n')
    write_json(root/'quality_summary.json',dict(series=series,source_videos=len(selected),completed=completed,
               unprocessed=len(selected)-completed,source_duration_seconds=sum(r.get('duration_seconds') or 0 for r in selected),
               issues=issues,accuracy=None,human_reviewed=False,updated_at=utcnow()))
    return [root/n for n in ['index.md','README.md','quality_summary.json']]


def update_catalog(rows,output_root):
    root=Path(output_root);summaries=[]
    body='# 新概念英语课程解析\n\n每个分 P 单独保存语音原文、双模型复查、课件原文、视觉观察、原始关键帧和质量报告。\n\n'
    body+='| 系列 | 已完成 / 总数 | 视频总时长 |\n|---|---:|---:|\n'
    for series in dict.fromkeys(r['series'] for r in rows):
        selected=[r for r in rows if r['series']==series]
        completed=sum((root/series/r['directory']/'manifest.json').exists() and (root/series/r['directory']/'qc_report.json').exists() for r in selected)
        duration=sum(r.get('duration_seconds') or 0 for r in selected)
        summaries.append({'series':series,'completed':completed,'total':len(selected),'duration_seconds':duration})
        body+=f'| [{series}]({quote(series)}/index.md) | {completed} / {len(selected)} | {seconds_label(duration)} |\n'
    body+='\n“完成”表示机器解析产物已生成；不代表逐字人工确认或百分之百准确。疑点保留候选与来源，见各系列质量报告。\n\n[处理代码与复现说明](_pipeline/README.md) · [完整视频清单](inventory.json)\n'
    atomic_text(root/'README.md',body)
    write_json(root/'processing_status.json',{'updated_at':utcnow(),'series':summaries,'completed':sum(s['completed'] for s in summaries),
                                            'total':len(rows),'accuracy':None})
    return [root/'README.md',root/'processing_status.json']
