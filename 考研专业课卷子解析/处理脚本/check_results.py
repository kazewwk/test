"""Check output pages/assets/hashes; flag recognition coverage for human review."""
from pathlib import Path
import json,re,hashlib,unicodedata,collections
R=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normalize(s):
    s=unicodedata.normalize('NFKC',s).lower()
    return ''.join(re.findall(r'[a-z0-9\u4e00-\u9fff]',s))
def shingles(s,n=6):return {s[i:i+n] for i in range(max(0,len(s)-n+1))}
def main():
    inv=json.loads((R/'inventory.json').read_text());prep={r['id']:r for r in json.loads((R/'prepared_inputs.json').read_text())['papers']}
    splits={r['id']:r for r in json.loads((R/'split_pages.json').read_text())['papers']}
    done=[];pending=[];errors=[];review=[]
    for paper in inv['papers']:
        pid=paper['id'];out=R/'results'/paper['subject_group']/pid;record=out/'run.json'
        if not record.exists():pending.append(pid);continue
        run=json.loads(record.read_text());ps=splits.get(pid);expected=ps['output_pages'] if ps else prep[pid]['pages']
        try:
            assert run['status']=='success' and run['tier']=='advanced' and run['effort']=='xhigh'
            assert run['versions']['mineru']=='4.1.5'
            for rel,digest in run['output_sha256'].items():assert sha(out/rel)==digest,('hash mismatch',rel)
            middle=json.loads((out/'middle_json.json').read_text());structured=json.loads((out/'structured_content.json').read_text())
            assert middle['metadata']['producer']=={'name':'mineru','version':'4.1.5'}
            assert middle['extensions']['mineru']['tier']=='advanced'
            assert len(middle['pages'])==len(structured['pages'])==run['processed_pages']==expected
            assert [p['page_idx'] for p in structured['pages']]==list(range(expected))
            blank_ok={p['output_page']-1 for p in (ps or {}).get('page_mapping',[]) if p.get('blank_half_preserved')}
            empty=[i for i,p in enumerate(structured['pages']) if not p.get('blocks') and i not in blank_ok]
            if empty:review.append(dict(id=pid,reason='unexpected_empty_page',pages_1based=[i+1 for i in empty]))
            md=(out/'markdown.md').read_text()
            assert len(md.strip())>50
            for ref in md.split('](')[1:]:
                ref=ref.split(')',1)[0].strip('<>').split('#')[0]
                if ref and not ref.startswith(('https:','http:','data:')):assert (out/ref).is_file(),('missing asset',ref)
            output=normalize(md);output_shingles=shingles(output)
            refs=paper.get('existing_text_files',[]);ref=next((Path(x) for x in refs if 'reviewed' in x),None)
            if ref is None and paper.get('subject_boundary'):ref=Path(paper['subject_boundary']['canonical_subject_text_path'])
            metrics={}
            if ref is not None:
                raw=ref.read_text();lines=[]
                for line in raw.splitlines():
                    if not line.strip() or any(x in line for x in ['来源：','来源:','方法：','方法:','http','文本方法','逐字校对']):continue
                    if line.lstrip().startswith('#') and not re.match(r'^#+\s*[一二三四五六七八九十、0-9]',line):continue
                    lines.append(line)
                reftext=normalize('\n'.join(lines));rs=shingles(reftext)
                coverage=len(output_shingles&rs)/len(rs) if rs else 1
                end=normalize(''.join(lines[-5:]));es=shingles(end);endcoverage=len(es&output_shingles)/len(es) if es else 1
                metrics=dict(reference=str(ref.relative_to(Path(inv['repository_root']))),reference_6char_coverage=round(coverage,4),last_lines_6char_coverage=round(endcoverage,4),reference_characters=len(reftext),output_characters=len(output))
                if coverage<0.70 or endcoverage<0.55:review.append(dict(id=pid,reason='reference_text_coverage_needs_review',**metrics))
            done.append(dict(id=pid,subject=paper['subject_group'],pages=expected,**metrics))
        except Exception as exc:errors.append(dict(id=pid,error=repr(exc)))
    report=dict(completed=len(done),pending=len(pending),by_subject=dict(collections.Counter(x['subject'] for x in done)),errors=errors,review_flags=review,checks=done,pending_ids=pending)
    (R/'quality_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k not in ['checks','pending_ids']},ensure_ascii=False,indent=2))
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
