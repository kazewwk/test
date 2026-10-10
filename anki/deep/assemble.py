#!/usr/bin/env python3
"""Assemble reviewed chapter sources; never promote an unfinished draft to final.

Knowledge/source checks here are structural. Authors must actually read and
review the materials; this script cannot infer semantic coverage from counts.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, default=Path('/workspace/scratch/deep-rewrite'))
    parser.add_argument('--repo', type=Path, default=Path('/workspace/test'))
    parser.add_argument('--materials', type=Path, default=Path('/workspace/materials'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--checkpoint', action='store_true', help='Output only explicitly ready chapters; label as incomplete')
    args=parser.parse_args()
    expected=load(args.work/'fulltext-index.json')
    chapters={p.stem:load(p) for p in (args.work/'chapters').glob('*.json')}
    assert set(chapters).issubset(expected), 'Unexpected chapter'
    ready={ch:d for ch,d in chapters.items() if all(d.get(f) is True for f in ('reading_complete','authoring_complete','export_ready'))}
    pending=sorted(set(expected)-set(ready))
    assert args.checkpoint or not pending, ('Final export blocked: chapter reading/authoring still unfinished', pending)
    assert ready, 'No chapters explicitly ready'

    # Cross-chapter canonical targets may exist in a currently unfinished chapter.
    all_cards={}
    for ch,d in chapters.items():
        for c in d['cards']:
            assert c['id'] not in all_cards, ('Duplicate card ID',c['id'])
            all_cards[c['id']]=c
    units=[]; unit_ids=set(); inverse=collections.defaultdict(list); blockers=[]
    source_cache={}
    for ch,d in ready.items():
        inventory=load(args.work/'fulltext'/f'{ch}-index.json')
        expected_batches={b['id'] for b in inventory['read_batches']}
        actual={b if isinstance(b,str) else b['id'] for b in d['read_batches']}
        assert expected_batches==actual, (ch,'Incomplete sequential reading records')
        old={c['id'] for c in load(args.work/'input'/f'{ch}.json')['cards']}
        assert old.issubset({c['id'] for c in d['cards']}), (ch,'Missing stable legacy IDs')
        assert d.get('self_check'), (ch,'No actual content-review record')
        for k in d['knowledge_units']:
            assert k['id'] not in unit_ids, ('Duplicate knowledge ID',k['id'])
            unit_ids.add(k['id']); units.append(k)
            document=args.materials/k['source_document']
            assert document.is_file(), (k['id'],'Source not actually readable')
            if document not in source_cache:
                source_cache[document]=document.read_text(encoding='utf-8').splitlines()
            lines=source_cache[document]
            coords=k['source_lines']
            assert coords and all(isinstance(n,int) and 1<=n<=len(lines) for n in coords), (k['id'],'Invented line location')
            if k.get('status')!='covered':
                assert k.get('rationale'), (k['id'],'Unresolved disposition needs a reason')
                continue
            assert k.get('recall_required') is True and k.get('card_ids'), (k['id'],'No explicit recall target')
            for cid in k['card_ids']:
                c=all_cards.get(cid)
                assert c and c.get('answer') and c.get('criteria'), (k['id'],cid,'Missing authored canonical target')
                for field,target in [('answer_parts','answer'),('criteria_parts','criteria')]:
                    positions=k.get(field,{}).get(cid,[])
                    assert positions and all(isinstance(i,int) and 1<=i<=len(c[target]) for i in positions), (k['id'],cid,field,'Invalid 1-based position')
                inverse[cid].append(k)
                if not any(cid in {x['id'] for x in z['cards']} for z in ready.values()):
                    blockers.append({'knowledge_id':k['id'],'canonical_card_id':cid,'reason':'Target authored but chapter not yet export-ready'})
    assert args.checkpoint or not blockers, ('Final export has unready canonical dependencies',blockers)

    images={x['id']:x for x in (json.loads(l) for l in (args.repo/'anki/audit/image-index.jsonl').read_text().splitlines())}
    images.update({x['id']:x for x in load(args.repo/'anki/audit/external-images.json')})
    media=args.output/'media'; media.mkdir(parents=True,exist_ok=True)
    media_hashes={}; image_usage=collections.defaultdict(list)
    def picture(fid,cid):
        im=images[fid]
        path=(args.repo if im.get('external_original') else args.materials)/im['path']
        assert path.is_file(), (cid,fid,'Missing real original image')
        data=path.read_bytes(); digest=hashlib.sha256(data).hexdigest()
        assert digest==im['sha256'], (cid,fid,'Original image hash changed')
        # Hash naming avoids collisions among hundreds of images/part directories.
        name='biology_'+digest+path.suffix.lower()
        dest=media/name
        if not dest.exists(): dest.write_bytes(data)
        else: assert hashlib.sha256(dest.read_bytes()).hexdigest()==digest
        media_hashes[name]={'file':name,'sha256':digest,'bytes':len(data),'image_ids':sorted(set(media_hashes.get(name,{}).get('image_ids',[])+[fid]))}
        image_usage[fid].append(cid)
        caption=im.get('source','') if im.get('external_original') else ''
        return {'path':'media/'+name,'sha256':digest,**({'caption':caption} if caption else {})}

    canonical=[]
    for ch,d in sorted(ready.items()):
        frozen=load(args.work/'input'/f'{ch}.json')['cards']
        old={c['id']:c for c in frozen}
        deck=collections.Counter(c['deck'] for c in frozen).most_common(1)[0][0]
        for raw in d['cards']:
            c=dict(raw);cid=c['id'];ks=inverse[cid]
            assert ks, (cid,'No recalled knowledge unit')
            c['knowledge_ids']=sorted(k['id'] for k in ks)
            c['deck']=old[cid]['deck'] if cid in old else c.get('deck',deck)
            c['type']='basic'
            tags=c.get('tags') or old.get(cid,{}).get('tags',[])
            tags=tags.split() if isinstance(tags,str) else list(tags)
            tags+=['生物化学' if ch.startswith('B') else '分子生物学','章节::'+ch,'任务::'+c['ability']]
            topic=str(c.get('theme') or c['concepts'][0])
            topic=re.split(r'[；。！？，、]',topic,1)[0][:32]
            tags.append('主题::'+topic)
            tags=[re.sub(r'\s+','_',str(t)) for t in tags]
            c['tags']=list(dict.fromkeys(tags))
            fs=list(dict.fromkeys(c.get('front_image_ids',[])))
            bs=[x for x in dict.fromkeys(c.get('image_ids',[])) if x not in fs]
            c['front_images']=[picture(fid,cid) for fid in fs]
            c['back_images']=[picture(fid,cid) for fid in bs]
            # Always keep the primary source even when a card also has cross sources.
            sources=[c['source']]
            for k in ks:
                loc=k['source_document']+'，原文件行号'+','.join(map(str,k['source_lines']))+'（非印刷页码）'
                sources.append(loc)
            for fid in fs+bs:
                im=images[fid]
                sources.append(('原图：'+im['path'])+('；'+im.get('url','') if im.get('external_original') else ''))
            c['sources']=list(dict.fromkeys(sources))
            canonical.append(c)
    args.output.mkdir(parents=True,exist_ok=True)
    with (args.output/'canonical.jsonl').open('w',encoding='utf-8') as out:
        for c in canonical:out.write(json.dumps(c,ensure_ascii=False)+'\n')
    with (args.output/'coverage.jsonl').open('w',encoding='utf-8') as out:
        for k in units:out.write(json.dumps(k,ensure_ascii=False)+'\n')
    with (args.output/'coverage.tsv').open('w',encoding='utf-8',newline='') as out:
        writer=csv.writer(out,delimiter='\t',lineterminator='\n')
        writer.writerow(['教材位置','具体知识点','知识点ID','卡片ID','答案对应位置','必答点对应位置','是否明确要求回忆','处理状态'])
        for k in units:
            for cid in k.get('card_ids') or ['']:
                writer.writerow([k['source_document']+' 行 '+','.join(map(str,k['source_lines'])),k['point'],k['id'],cid,','.join(map(str,k.get('answer_parts',{}).get(cid,[]))),','.join(map(str,k.get('criteria_parts',{}).get(cid,[]))),str(k.get('recall_required',False)),k['status']])
    dump(args.output/'gaps.json',{ch:d['gaps'] for ch,d in sorted(ready.items())})
    dump(args.output/'media-manifest.json',{'media':list(media_hashes.values()),'image_usage':image_usage})
    report={'final_scope_complete':not pending,'ready_chapters':sorted(ready),'pending_chapters':pending,'chapters_total':len(expected),'notes':len(canonical),'knowledge_units':len(units),'unready_canonical_dependencies':blockers,'media_files':len(media_hashes),'unresolved_source_units':sum(k.get('status')!='covered' for k in units),'original_media_hashes_verified':True,'semantic_claim':'Chapter author records govern content review; structural script does not certify zero omissions.'}
    dump(args.output/'assembly-check.json',report)
    print(json.dumps(report,ensure_ascii=False))


if __name__=='__main__':main()
