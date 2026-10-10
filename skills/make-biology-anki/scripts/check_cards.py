#!/usr/bin/env python3
"""Check export structure and exact coverage anchors; does not certify academic completeness."""
import argparse,json,re,csv
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('cards');p.add_argument('--knowledge');p.add_argument('--tsv');p.add_argument('--media');a=p.parse_args()
cs=json.loads(Path(a.cards).read_text(encoding='utf-8'));cs=cs.get('cards',cs) if isinstance(cs,dict) else cs
by={c['id']:c for c in cs};assert len(by)==len(cs),'duplicate card ID'
for c in cs:
 assert c['type']=='Basic','default export must be Basic'
 assert c['front'].strip() and c['answer'] and c['rubric'] and c['source_units'] and c['knowledge_ids']
 assert len(c['tags'])>=4 and all(not re.search(r'\s',t) for t in c['tags'])
 assert all(x['text'].strip() for x in c['answer']+c['rubric'])
 assert len({x['anchor'] for x in c['answer']})==len(c['answer'])
 if '需看图' in c['front']:assert any(m['side']=='front' for m in c['images']),'missing question media'
 if a.media:
  for m in c['images']:assert (Path(a.media)/m['filename']).is_file(),m
if a.knowledge:
 ks=json.loads(Path(a.knowledge).read_text(encoding='utf-8'));assert len({k['knowledge_id'] for k in ks})==len(ks),'duplicate knowledge ID'
 for k in ks:
  if k['status']=='covered':
   c=by[k['card_id']];assert k['knowledge_id'] in c['knowledge_ids'];assert k['explicit_recall'] is True
   assert k['answer_anchor'] in {x['anchor'] for x in c['answer']}
   assert k['rubric_anchor'] in {x['anchor'] for x in c['rubric']}
   assert set(k['source_units'])<=set(c['source_units']),(k,c['id'])
if a.tsv:
 with Path(a.tsv).open(encoding='utf-8',newline='') as f:
  rows=list(csv.reader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
 assert len(rows)==len(cs) and all(len(row)==3 and all(v.strip() for v in row) for row in rows)
 assert all('\n' not in v and '\r' not in v for row in rows for v in row)
 if a.media:
  refs={x for row in rows for v in row[:2] for x in re.findall(r'<img[^>]+src="([^"]+)"',v)}
  assert refs=={p.name for p in Path(a.media).iterdir() if p.is_file()},'missing or unused media'
print(json.dumps({'status':'PASS','notes':len(cs),'basic_cards':len(cs),'checks':'IDs, fields, anchors, source sets, recall flags, TSV columns, media references','semantic_coverage_certified':False},ensure_ascii=False))
