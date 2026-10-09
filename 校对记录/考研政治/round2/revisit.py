import json,pathlib,collections,math
import pymupdf
from PIL import Image,ImageDraw,ImageFont
R=pathlib.Path('/workspace/politics-books'); O=R/'round2'; P=json.loads((R/'politics_books_plan.json').read_text()); A=json.loads((O/'items.json').read_text()); D=json.loads((O/'decisions.json').read_text()); fonts=[ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',n) for n in (18,22)]
docs={b['id']:pymupdf.open(R/'source'/b['asset_name']) for b in P['books']}; groups=collections.defaultdict(list)
for a in A:
 if D[str(a['id'])]['decision'] in ('needs_source_revisit','source_confirmed_correction_needed'):groups[(a['book'],a['page'],a['block'])].append(a)
cards=[]
for key,rows in groups.items():
 b,p,bi=key;page=docs[b][p-1];bb=rows[0]['bbox']; bb=[max(0,bb[0]-.012),max(0,bb[1]-.012),min(1,bb[2]+.012),min(1,bb[3]+.012)]
 if bi is None:bb=[0.065,max(0,bb[1]-.025),.935,min(1,bb[3]+.03)]
 if rows[0]['type']=='table':bb=[.065,max(0,bb[1]-.07),.95,min(1,bb[3]+.12)]
 rect=pymupdf.Rect(bb[0]*page.rect.width,bb[1]*page.rect.height,bb[2]*page.rect.width,bb[3]*page.rect.height)
 pix=page.get_pixmap(matrix=pymupdf.Matrix(4,4),clip=rect,alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((1150,1100))
 txt='当前原文：'+rows[0]['current_text']+'\n差异：'+ '；'.join(f'R{a["id"]} [{a["current"] or "∅"} → {a["reference"] or "∅"}] {a.get("current_context","")}' for a in rows)
 lines=[line[i:i+23] for line in txt.splitlines() for i in range(0,max(1,len(line)),23)]
 h=max(im.height+48,len(lines)*25+48); card=Image.new('RGB',(1600,h),'white');dr=ImageDraw.Draw(card);dr.text((5,3),f'B{b} P{p} b{bi} R'+','.join(str(a['id']) for a in rows),font=fonts[1],fill='black');card.paste(im,(5,45))
 for i,l in enumerate(lines):dr.text((1160,45+i*25),l,font=fonts[0],fill='black')
 cards.append((card,[a['id'] for a in rows]))
out=O/'evidence/revisit';out.mkdir(parents=True,exist_ok=True); maps={};batch=[];height=0
def save():
 global batch,height
 if not batch:return
 n=f'revisit-{len(maps)+1:03d}.jpg';im=Image.new('RGB',(1600,height),'white');y=0;ids=[]
 for card,ri in batch:im.paste(card,(0,y));y+=card.height;ids+=ri
 im.save(out/n,quality=97);maps[n]=ids;batch=[];height=0
for card,ids in cards:
 if height+card.height>2600:save()
 batch.append((card,ids));height+=card.height
save();(O/'revisit-sheets.json').write_text(json.dumps(maps,indent=2));print('cards',len(cards),'sheets',len(maps))
