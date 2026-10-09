import json,pathlib,re,unicodedata,collections
from rapidfuzz.distance import Levenshtein
root=pathlib.Path('/workspace/politics-books');plan=json.load(open(root/'politics_books_plan.json'))
def text(v):
 if isinstance(v,str):return v
 if isinstance(v,list):return ''.join(text(x) for x in v)
 if isinstance(v,dict):return text(v.get('content',''))
 return ''
def norm(s):
 s=re.sub(r'<[^>]*>','',s);s=re.sub(r'\\[a-zA-Z]+','',s);s=unicodedata.normalize('NFKC',s)
 return ''.join(c for c in s if c.isalnum())
result=[]
for b in plan['books']:
 rows=[]
 for f in (root/'reviewed'/b['folder']).glob('raw_chunks/*/middle_json.json'):
  for p in json.loads(f.read_text())['pages']:
   n=p['page_idx']+1;ref=json.load(open(root/'independent-ocr'/f'book-{b["id"]}-page-{n:04d}.json'));assert ref['source_sha256']==b['sha256']
   for z in p.get('blocks',[]):
    bb=z.get('bbox');t=text(z)
    if not bb or not t or z['type'] in ['image','chart']:continue
    lines=[]
    for l in ref['lines']:
     x=sum(q[0] for q in l['polygon'])/4;y=sum(q[1] for q in l['polygon'])/4
     if bb[0]-.003<=x<=bb[2]+.003 and bb[1]-.003<=y<=bb[3]+.003:lines.append(l)
    native=''.join(l['text'] for l in lines);a=norm(t);c=norm(native)
    if a==c:continue
    sim=Levenshtein.normalized_similarity(a,c);diff=[]
    for op,i,j,k,l in Levenshtein.opcodes(a,c):
     if op!='equal':diff.append({'operation':op,'mineru':a[i:j],'independent':c[k:l],'mineru_context':a[max(0,i-12):min(len(a),j+12)],'independent_context':c[max(0,k-12):min(len(c),l+12)],'start':i,'end':j,'ref_start':k,'ref_end':l})
    rows.append({'book':b['id'],'page':n,'block':z['index'],'type':z['type'],'bbox':bb,'mineru':t,'independent':native,'similarity':round(sim,6),'diffs':diff,'lines':lines})
 print(b['id'],'different blocks',len(rows),'character diff segments',sum(len(r['diffs']) for r in rows),'high similarity',sum(r['similarity']>.95 for r in rows),flush=True);result.extend(rows)
(root/'independent-differences.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
