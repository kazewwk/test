import json,pathlib,pymupdf,unicodedata,re
from PIL import Image,ImageDraw,ImageFont
root=pathlib.Path('/workspace/politics-books');plan=json.load(open(root/'politics_books_plan.json'));rows=json.load(open(root/'independent-differences.json'));out=root/'ocr-review/independent';out.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',21);docs={b['id']:pymupdf.open(root/'source'/b['asset_name']) for b in plan['books']};items=[]
common={('入','人'),('己','已'),('一',''),('','一'),('','一一'),('祉','社'),('仝','全'),('逄','逢'),('目','自')}
for rid,r in enumerate(rows):
 if r['book'] not in [1,2,4] or r['type'] not in ['text','paragraph_title','doc_title','page_footnote','index','footer'] or r['similarity']<.9:continue
 ranges=[];offset=0
 for line in r['lines']:
  n=''.join(c for c in unicodedata.normalize('NFKC',line['text']) if c.isalnum());ranges.append((offset,offset+len(n),line,n));offset+=len(n)
 for di,d in enumerate(r['diffs']):
  old=d['mineru'];new=d['independent']
  if (old,new) in common or max(len(old),len(new))>8:continue
  if old=='' and all(c.isascii() for c in new):continue
  if new=='' and all(c.isascii() for c in old):continue
  k=d['ref_start'];found=next(((i,j,line,n) for i,j,line,n in ranges if i<=k<j),None)
  if not found:continue
  i,j,line,n=found;poly=line['polygon'];x0=min(q[0] for q in poly);x1=max(q[0] for q in poly);y0=min(q[1] for q in poly);y1=max(q[1] for q in poly)
  frac=(k-i)/max(1,len(n));lo=max(0,frac-6/max(1,len(n)));hi=min(1,frac+(max(1,len(new))+6)/max(1,len(n)));p=docs[r['book']][r['page']-1]
  rect=pymupdf.Rect((x0+(x1-x0)*lo)*p.rect.width,max(0,y0-.003)*p.rect.height,(x0+(x1-x0)*hi)*p.rect.width,min(1,y1+.003)*p.rect.height)
  if rect.is_empty:continue
  pix=p.get_pixmap(matrix=pymupdf.Matrix(3,3),clip=rect,alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((660,75));items.append((rid,di,r,old,new,im))
for start in range(0,len(items),32):
 sheet=Image.new('RGB',(1400,16*135),'white');draw=ImageDraw.Draw(sheet)
 for q,(rid,di,r,old,new,im) in enumerate(items[start:start+32]):
  x=(q%2)*700;y=(q//2)*135;draw.text((x+4,y),f'#{rid}.{di} B{r["book"]} P{r["page"]} b{r["block"]}: {old or "∅"} → {new or "∅"}',font=font,fill='black');sheet.paste(im,(x+4,y+38))
 sheet.save(out/f'independent-{start//32+1:02d}.jpg',quality=93)
print('segments',len(items),'sheets',(len(items)+31)//32)
(root/'independent-review-items.json').write_text(json.dumps([{'row':i,'diff':j} for i,j,r,a,b,im in items]))
