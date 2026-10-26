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
