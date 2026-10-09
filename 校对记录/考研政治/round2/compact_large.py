import json,pathlib,math
from PIL import Image,ImageDraw,ImageFont
r=pathlib.Path('/workspace/politics-books/round2');cards=json.loads((r/'large-cards.json').read_text());items=json.loads((r/'items.json').read_text());font=ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',21);groups={};short=[];tall=[]
for c in cards:
 i=items[c['ids'][0]]
 if i['type'] in ['header','page_number','paragraph_title','footer','doc_title'] and max(len(i['current_text']),len(i['reference_text']))<=120:short.append(c)
 else:tall.append(c)
out=r/'evidence/compact';out.mkdir(exist_ok=True)
for start in range(0,len(short),32):
 im=Image.new('RGB',(1600,16*150),'white');draw=ImageDraw.Draw(im);ids=[]
 for q,c in enumerate(short[start:start+32]):
  row=items[c['ids'][0]];x=q%2*800;y=q//2*150;draw.text((x+4,y),f'R{",".join(map(str,c["ids"]))} B{c["book"]}P{c["page"]} b{c["block"]}',font=font,fill='black');draw.text((x+4,y+27),'当前:'+row['current_text'][:33],font=font,fill='black');draw.text((x+4,y+54),'对照:'+row['reference_text'][:33],font=font,fill='#744000')
  src=Image.open(r/'evidence/large'/c['file']);crop=src.crop((5,55,990,min(src.height,1000)));# Trim unused white at bottom of source region.
  from PIL import ImageChops
  bb=ImageChops.difference(crop,Image.new('RGB',crop.size,'white')).getbbox()
  if bb:crop=crop.crop((0,0,crop.width,bb[3]))
  crop.thumbnail((780,63));im.paste(crop,(x+4,y+84));ids+=c['ids']
 name=f'headers-{start//32+1:03d}.jpg';im.save(out/name,quality=95);groups[name]=ids
# Stack complete whole-block cards without reducing their source font size.
sheets=[];batch=[];h=0
for c in tall:
 image=Image.open(r/'evidence/large'/c['file'])
 if h+image.height>2600 and batch:sheets.append(batch);batch=[];h=0
 batch.append((c,image.copy()));h+=image.height
if batch:sheets.append(batch)
for idx,batch in enumerate(sheets):
 im=Image.new('RGB',(1600,sum(v.height for c,v in batch)+len(batch)*6),'white');y=0;ids=[]
 for c,v in batch:im.paste(v,(0,y));y+=v.height+6;ids+=c['ids']
 name=f'blocks-{idx+1:03d}.jpg';im.save(out/name,quality=95);groups[name]=ids
(r/'compact-sheets.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2)+'\n');print('Short whole-block cards',len(short),'sheets',math.ceil(len(short)/32),'other block sheets',len(sheets))
