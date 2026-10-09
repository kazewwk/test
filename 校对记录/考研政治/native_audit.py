import json,pathlib,re,unicodedata,pymupdf
from rapidfuzz.distance import Levenshtein
root=pathlib.Path('/workspace/politics-books');plan=json.load(open(root/'politics_books_plan.json'));out=[]
def contents(v):
 if isinstance(v,str):return v
 if isinstance(v,list):return ''.join(contents(x) for x in v)
 if isinstance(v,dict):return contents(v.get('content',''))
 return ''
def norm(s):
 s=re.sub(r'<[^>]*>','',s);s=re.sub(r'\\[a-zA-Z]+','',s);s=unicodedata.normalize('NFKC',s)
 return ''.join(c for c in s if c.isalnum())
for b in plan['books']:
 if b['id'] not in [3,5]:continue
 doc=pymupdf.open(root/'source'/b['asset_name']);num=0
 for f in (root/'parsed'/b['folder']).glob('raw_chunks/*/middle_json.json'):
  for p in json.loads(f.read_text())['pages']:
   page=doc[p['page_idx']]
   for z in p.get('blocks',[]):
    if z['type'] in ['image','chart','table']:continue
    t=contents(z);bbox=z.get('bbox')
    if not bbox:continue
    box=pymupdf.Rect(bbox[0]*page.rect.width,bbox[1]*page.rect.height,bbox[2]*page.rect.width,bbox[3]*page.rect.height);box=box+(-1,-1,1,1)
    native=page.get_textbox(box);a=norm(t);c=norm(native)
    if a==c or len(a)<2 or len(c)<2:continue
    sim=Levenshtein.normalized_similarity(a,c)
    ops=Levenshtein.opcodes(a,c);diff=[]
    for op,i,j,k,l in ops:
     if op!='equal':diff.append({'operation':op,'mineru':a[i:j],'native':c[k:l],'mineru_context':a[max(0,i-12):min(len(a),j+12)],'native_context':c[max(0,k-12):min(len(c),l+12)]})
    out.append({'book':b['id'],'page':p['page_idx']+1,'block':z['index'],'type':z['type'],'bbox':bbox,'mineru':t,'native':native,'similarity':sim,'diffs':diff});num+=1
 print(b['id'],num)
(root/'native-differences.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('total',len(out))
