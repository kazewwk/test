import json,pathlib,re,unicodedata,collections,hashlib,bisect,math
import pymupdf
from rapidfuzz.distance import Levenshtein
from PIL import Image,ImageDraw,ImageFont
ROOT=pathlib.Path('/workspace/politics-books');REPO=pathlib.Path('/workspace/test-repo');OUT=ROOT/'round2';OUT.mkdir(exist_ok=True)
PLAN=json.loads((REPO/'scripts/politics_books_plan.json').read_text());font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',19);tiny=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',17);bigfont=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',23)
def norm(s):
 s=re.sub(r'<[^>]*>','',s);s=re.sub(r'\\[a-zA-Z]+','',s)
 return ''.join(c for c in unicodedata.normalize('NFKC',s) if c.isalnum())
def wrap(s,limit):return [s[i:i+limit] for i in range(0,len(s),limit)] or ['∅']
def bbox_rect(bb,p):return pymupdf.Rect(bb[0]*p.rect.width,bb[1]*p.rect.height,bb[2]*p.rect.width,bb[3]*p.rect.height)&p.rect
items=[];thumbs={};large=[];small=[];docs={}
for book in PLAN['books']:
 doc=pymupdf.open(ROOT/'source'/book['asset_name']);docs[book['id']]=doc
 audits=json.loads((REPO/book['folder']/'ocr_review/page_audit.json').read_text())
 for pg in audits:
  page=doc[pg['pdf_page']-1]
  for z in pg['blocks']:
   if not z['differences']:continue
   a=norm(z['current_text']);b=norm(z['independent_text']);assert len(z['differences'])==sum(op!='equal' for op,*_ in Levenshtein.opcodes(a,b))
   line_ranges=[];offset=0
   for line in z['independent_lines']:
    n=norm(line['text']);line_ranges.append((offset,offset+len(n),line,n));offset+=len(n)
   di=0
   for op,i,j,k,l in Levenshtein.opcodes(a,b):
    if op=='equal':continue
    row={'id':len(items),'book':book['id'],'page':pg['pdf_page'],'block':z['index'],'type':z['type'],'diff_index':di,'operation':op,'current_start':i,'current_end':j,'reference_start':k,'reference_end':l,'current':a[i:j],'reference':b[k:l],'current_context':a[max(0,i-12):min(len(a),j+12)],'reference_context':b[max(0,k-12):min(len(b),l+12)],'bbox':z['bbox'],'current_text':z['current_text'],'reference_text':z['independent_text'],'source_sha256':book['sha256'],'similarity':z['normalized_similarity']};di+=1
    islarge=max(j-i,l-k)>8 or z['normalized_similarity']<.85 or not b
    target=next((r for r in line_ranges if r[0]<=min(k,len(b)-1)<r[1]),None)
    if not target:islarge=True
    if islarge:rect=bbox_rect(z['bbox'],page)
    else:
     start,end,line,n=target;poly=line['polygon'];x0=min(q[0] for q in poly);x1=max(q[0] for q in poly);y0=min(q[1] for q in poly);y1=max(q[1] for q in poly)
     frac=(k-start)/max(1,len(n));lo=max(0,frac-7/max(1,len(n)));hi=min(1,frac+(max(1,l-k)+7)/max(1,len(n)))
     rect=bbox_rect([x0+(x1-x0)*lo,max(0,y0-.004),x0+(x1-x0)*hi,min(1,y1+.004)],page)
    if rect.is_empty:rect=bbox_rect(z['bbox'],page);islarge=True
    pix=page.get_pixmap(matrix=pymupdf.Matrix(3,3),clip=rect,alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    row['evidence_crop_bbox']=[rect.x0/page.rect.width,rect.y0/page.rect.height,rect.x1/page.rect.width,rect.y1/page.rect.height];row['crop_kind']='whole_block' if islarge else 'difference_context'
    items.append(row)
    if islarge:
     # Multiple differences within a difficult block share a single whole-block card.
     key=(row['book'],row['page'],row['block'])
     prior=next((v for v in large if v['key']==key),None)
     if prior:prior['ids'].append(row['id'])
     else:large.append({'key':key,'row':row,'ids':[row['id']],'image':im})
    else:im.thumbnail((385,73));small.append((row,im))
  for ci,line in enumerate(pg['unmatched_independent_text_candidates']):
   poly=line['polygon'];bb=[min(v[0] for v in poly),min(v[1] for v in poly),max(v[0] for v in poly),max(v[1] for v in poly)];rect=bbox_rect(bb,page)
   pix=page.get_pixmap(matrix=pymupdf.Matrix(3,3),clip=rect,alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((385,73))
   row={'id':len(items),'book':book['id'],'page':pg['pdf_page'],'block':None,'type':'unmatched_line','candidate_index':ci,'current':'∅','reference':line['text'],'current_context':'区块外文字候选','reference_context':line['text'],'bbox':bb,'current_text':'','reference_text':line['text'],'evidence_crop_bbox':bb,'crop_kind':'difference_context','source_sha256':book['sha256']};items.append(row);small.append((row,im))
small_dir=OUT/'evidence/small';large_dir=OUT/'evidence/large';small_dir.mkdir(parents=True,exist_ok=True);large_dir.mkdir(parents=True,exist_ok=True)
for start in range(0,len(small),64):
 sheet=Image.new('RGB',(1600,16*130),'white');draw=ImageDraw.Draw(sheet)
 name=f'small-{start//64+1:03d}.jpg'
 for q,(r,im) in enumerate(small[start:start+64]):
  x=(q%4)*400;y=(q//4)*130;draw.text((x+3,y),f'R{r["id"]} B{r["book"]} P{r["page"]} b{r["block"]}',font=font,fill='black');draw.text((x+3,y+23),f'当前: {r["current"] or "∅"}  对照: {r["reference"] or "∅"}',font=tiny,fill='black');sheet.paste(im,(x+3,y+51));r['evidence_sheet']='evidence/small/'+name;r['sheet_position']=q
 sheet.save(small_dir/name,quality=95)
large_records=[]
for c in large:
 r=c['row'];im=c['image'];im.thumbnail((985,850));contexts=[]
 for rid in c['ids']:
  rr=items[rid];contexts+=wrap(f'R{rid}: 当前 {rr["current"] or "∅"} | 对照 {rr["reference"] or "∅"}',24)
 current=wrap(r['current_text'],25);reference=wrap(r['reference_text'],25)
 height=max(im.height+65,(len(contexts)+len(current)+len(reference)+5)*29+55)
 sheet=Image.new('RGB',(1600,height),'white');draw=ImageDraw.Draw(sheet);draw.text((5,5),f'B{r["book"]} P{r["page"]} b{r["block"]} [{r["type"]}] R'+','.join(map(str,c['ids'])),font=bigfont,fill='black');sheet.paste(im,(5,55));y=55
 for title,rows,color in [('本卡差异',contexts,'#833000'),('当前完整区块',current,'#111111'),('独立OCR区块',reference,'#555555')]:
  draw.text((1010,y),title,font=font,fill=color);y+=29
  for s in rows:draw.text((1010,y),s,font=font,fill=color);y+=29
 name=f'large-{len(large_records)+1:03d}.jpg';sheet.save(large_dir/name,quality=95)
 for rid in c['ids']:items[rid]['evidence_sheet']='evidence/large/'+name
 large_records.append({'file':name,'ids':c['ids'],'book':r['book'],'page':r['page'],'block':r['block'],'height':height})
(OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n');(OUT/'large-cards.json').write_text(json.dumps(large_records,ensure_ascii=False,indent=2)+'\n')
print('Remaining differences and unmatched lines',len(items),'small crops',len(small),'small sheets',math.ceil(len(small)/64),'whole-block cards',len(large));print('ID ranges',[(b['id'],min(r['id'] for r in items if r['book']==b['id']),max(r['id'] for r in items if r['book']==b['id'])) for b in PLAN['books']])
