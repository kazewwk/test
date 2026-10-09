import json,pathlib,pymupdf,unicodedata,re
from PIL import Image,ImageDraw,ImageFont
from rapidfuzz.distance import Levenshtein
root=pathlib.Path('/workspace/politics-books');plan=json.load(open(root/'politics_books_plan.json'));rows=json.load(open(root/'native-differences.json'));out=root/'ocr-review/native';out.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',22);docs={b['id']:pymupdf.open(root/'source'/b['asset_name']) for b in plan['books'] if b['id'] in (3,5)};items=[]
for rid,r in enumerate(rows):
 p=docs[r['book']][r['page']-1];bb=r['bbox'];clip=pymupdf.Rect(bb[0]*p.rect.width,bb[1]*p.rect.height,bb[2]*p.rect.width,bb[3]*p.rect.height)+(-1,-1,1,1)
 chars=[]
 for block in p.get_text('rawdict',clip=clip)['blocks']:
  for line in block.get('lines',[]):
   for span in line['spans']:
    for c in span['chars']:
     for v in unicodedata.normalize('NFKC',c['c']):
      if v.isalnum():chars.append((v,pymupdf.Rect(c['bbox'])))
 raw=''.join(c[0] for c in chars);native=''.join(c for c in unicodedata.normalize('NFKC',r['native']) if c.isalnum())
 # Layout may differ from get_textbox; map native to raw source characters.
 mapping={}
 for op,i,j,k,l in Levenshtein.opcodes(native,raw):
  if op=='equal':
   for x,y in zip(range(i,j),range(k,l)):mapping[x]=y
 a=''.join(c for c in unicodedata.normalize('NFKC',re.sub(r'\\[a-zA-Z]+','',re.sub(r'<[^>]*>','',r['mineru']))) if c.isalnum())
 for op,i,j,k,l in Levenshtein.opcodes(a,native):
  if op=='equal':continue
  inds=[mapping[x] for x in range(max(0,k-4),min(len(native),max(l,k+1)+4)) if x in mapping]
  if not inds:continue
  # Select the changed line; do not include adjacent lines in a single strip.
  mid=mapping.get(k,inds[len(inds)//2]);rect=chars[mid][1]
  for idx in inds:
   cr=chars[idx][1]
   if abs(cr.y0-rect.y0)<max(4,rect.height*.6):rect=rect|cr
  rect=rect+(-15,-3,15,3);rect=rect&p.rect
  pix=p.get_pixmap(matrix=pymupdf.Matrix(3,3),clip=rect,alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((660,78))
  items.append((rid,r,op,a[i:j],native[k:l],im))
for start in range(0,len(items),24):
 sheet=Image.new('RGB',(1400,24//2*140),'white');draw=ImageDraw.Draw(sheet)
 for q,(rid,r,op,old,new,im) in enumerate(items[start:start+24]):
  x=(q%2)*700;y=(q//2)*140;draw.text((x+5,y),f'#{rid} B{r["book"]} P{r["page"]} b{r["block"]}: {old[:14] or "∅"} → {new[:14] or "∅"}',font=font,fill='black');sheet.paste(im,(x+5,y+40))
 sheet.save(out/f'native-{start//24+1:02d}.jpg',quality=93)
print('differences',len(items),'sheets',(len(items)+23)//24)
