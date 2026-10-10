from en01_exercises import *

def point(cid,anchor,label,sources):
 c=next(c for c in CARDS if c['id']==cid);kid=a.next_kid();c['knowledge_ids'].append(kid)
 for s in sources:
  if s not in c['source_units']:c['source_units'].append(s)
 KNOWLEDGE.append({'knowledge_id':kid,'knowledge':label,'source_units':sources,'card_id':cid,'answer_anchor':'A'+str(anchor),'rubric_anchor':'R'+str(anchor),'explicit_recall':True,'status':'covered','question':c['front']})

# The summaries include two details not stated in the adjacent introductory paragraphs.
c=next(c for c in CARDS if c['id']=='RB-CN01-0152')
c['answer'][0]['text']+=' 章末总结还指出叶绿体有自己的核糖体（ribosomes），与自己的DNA共同体现细菌内共生来源。'
c['rubric'][0]['text']+=' 叶绿体自己的核糖体及DNA与细菌来源联系。'
point(c['id'],1,'叶绿体自有核糖体的章末总结信息',[G(32)])
c=next(c for c in CARDS if c['id']=='RB-CN01-0182')
c['answer'][1]['text']+=' 章末将这些机制描述为在超过10亿年真核演化中仍高度保守。'
c['rubric'][1]['text']+=' 真核演化超过10亿年仍保守的总结范围。'
point(c['id'],2,'真核机制超过10亿年演化中仍保守',[M(124)])

# Do not infer an unspecified quantitative legend from a drawing.
c=next(c for c in CARDS if c['id']=='RB-CN01-0201')
c['answer'][1]['text']=c['answer'][1]['text'].replace('条长显示图示不同蛋白大小，分组和颜色对应结构定位，不是数量表达水平图','图中条形长短不同，但本段未给长度单位；分组和颜色对应结构定位，不能读成表达水平或精确氨基酸数')
c['rubric'][1]['text']=c['rubric'][1]['text'].replace('条长非表达量','条形未给定量单位，非表达量或精确氨基酸数')
c['answer'][0]['text']+=' 本图S用绿、E用红、M用橙、N用紫，RNA为蓝，颜色仅是图示编码。'
c['rubric'][0]['text']+=' 本图S绿、E红、M橙、N紫、RNA蓝的对应。'
for label in ['图1-49S绿色','图1-49E红色','图1-49M橙色','图1-49N紫色','图1-49RNA蓝色']:
 point(c['id'],1,label,[M(106),M(107)])

c=next(c for c in CARDS if c['id']=='RB-CN01-0203')
c['front']=c['front'].replace('需测哪些参数','解释颜色对应，需测哪些参数')
c['answer'][0]['text']+=' 图中橙色是调控DNA、红色蛋白编码区、蓝色mRNA、绿色调节蛋白，属于这张图的编码。'
c['rubric'][0]['text']+=' 橙调控DNA、红编码区、蓝mRNA、绿调节蛋白。'
for label in ['图1-50橙色调控DNA','图1-50红色蛋白编码区','图1-50蓝色mRNA','图1-50绿色调节蛋白']:
 point(c['id'],1,label,[M(118),M(119)])

# Ensure repeated source passages appear in the per-knowledge coverage table too.
for sid in [G(32),M(124),Q(8)]:
 links=HANDLING[sid]['cards']
 for cid in links:
  c=next(c for c in CARDS if c['id']==cid)
  if sid not in c['source_units']:c['source_units'].append(sid)
  relevant=[k for k in KNOWLEDGE if k.get('card_id')==cid]
  if sid==Q(8):
   relevant=[k for k in relevant if any(z in k['knowledge'] for z in ['phototrophic','lithotrophic','无机化学体系','热液H2','热液CO','热液Fe','热液CH4','热液含磷','能量来源','碳来源','固定需要'])]
  elif sid==G(32):
   relevant=[k for k in relevant if any(z in k['knowledge'] for z in ['细胞骨架','双层核膜','核内','线粒体','叶绿体','双膜','自有DNA','染色体'])]
  else:
   relevant=[k for k in relevant if any(z in k['knowledge'] for z in ['模型','模式','保守','核糖体','细胞周期','减数','蛋白替代','酵母研究','测序'])]
  for k in relevant:
   if sid not in k['source_units']:k['source_units'].append(sid)

# Full abbreviations appear on the answer, where they cannot reveal a front-side target.
expansions={
 'DNA':'deoxyribonucleic acid，脱氧核糖核酸','RNA':'ribonucleic acid，核糖核酸',
 'mRNA':'messenger RNA，信使RNA','rRNA':'ribosomal RNA，核糖体RNA','tRNA':'transfer RNA，转运RNA',
 'ATP':'adenosine triphosphate，三磷酸腺苷','GTP':'guanosine triphosphate，鸟苷三磷酸',
 'GDP':'guanosine diphosphate，鸟苷二磷酸','ER':'endoplasmic reticulum，内质网'}
for c in CARDS:
 for token,meaning in expansions.items():
  done=False
  for part in c['answer']:
   pat=r'(?<![A-Za-z])'+re.escape(token)+r'(?![A-Za-z])'
   found=re.search(pat,part['text'])
   if not found:continue
   tail=part['text'][found.end():]
   if tail.startswith('（') and meaning.split('，')[0] in tail.split('）',1)[0]:done=True;break
   part['text']=part['text'][:found.end()]+'（'+meaning+'）'+part['text'][found.end():]
   done=True;break
 # Correct the noun translation without changing source numerical estimates.
 for part in c['answer']+c['rubric']:
  part['text']=part['text'].replace('人—猩猩','人—红毛猩猩')
for k in KNOWLEDGE:
 if k.get('card_id'):k['question']=next(c['front'] for c in CARDS if c['id']==k['card_id'])

# These four tasks ask learners to recall text/data already learned. Labelled originals
# belong on the answer for checking, so the question does not show its own answers.
questions={
 'RB-CN01-0110':'回忆全球生命树的主要细菌类群：写出PVC、放线菌、绿弯菌、厚壁菌、蓝细菌的中英名称及教材代表，解释环境测序分支的意义。（配图复核：图1-9细菌扇区）',
 'RB-CN01-0111':'回忆全球生命树：螺旋体、立克次体、奈瑟菌、变形菌各怎样与英文名及图示代表对应？真核扇区列哪些对象，Asgard属于哪个域？（配图复核：图1-9）',
 'RB-CN01-0113':'为什么细菌外观简单而基因组高度多样？教材球形、杆形、极小型、螺旋形四组各有什么代表，尺寸有何典型与例外，四组是否按统一形状标准分类？（配图复核：图1-10）',
 'RB-CN01-0192':'回忆教材豹蛙发育记录：从受精卵到蝌蚪有哪些依次阶段及小时数，96h重复图与1mm标尺如何理解，为什么时刻不能推广为所有蛙常数？（配图复核：图1-45）'}
for cid,q in questions.items():next(c for c in CARDS if c['id']==cid)['front']=q
c=next(c for c in CARDS if c['id']=='RB-CN01-0113')
c['answer'][1]['text']+=' 图题是“形状与大小”，极小型按尺寸、另三组按外形，故四列不是统一形状标准的正式分类。'
c['rubric'][1]['text']+=' 形状与尺寸是不同分组维度。'
point(c['id'],2,'图1-10按形状与尺寸两维展示而非统一形态分类',[E(106),E(111)])
for k in KNOWLEDGE:
 if k.get('card_id'):k['question']=next(c['front'] for c in CARDS if c['id']==k['card_id'])

ids={c['id'] for c in CARDS};kidset={k['knowledge_id'] for k in KNOWLEDGE}
assert len(ids)==len(CARDS) and len(kidset)==len(KNOWLEDGE)
for c in CARDS:
 assert c['type']=='Basic' and c['front'] and c['answer'] and c['rubric']
 assert len(c['answer'])==len(c['rubric'])
 assert all(UNITS[s]['reading_status']=='actually_read_2026-10-10' for s in c['source_units'])
for k in KNOWLEDGE:
 if k['status']!='covered':continue
 c=next(c for c in CARDS if c['id']==k['card_id'])
 assert k['explicit_recall'] and k['answer_anchor'] in {p['anchor'] for p in c['answer']} and k['rubric_anchor'] in {p['anchor'] for p in c['rubric']}
 assert set(k['source_units'])<=set(c['source_units'])
for sid,v in HANDLING.items():assert set(v['cards'])<=ids

(B/'source_units.json').write_text(json.dumps(list(UNITS.values()),ensure_ascii=False,indent=2)+'\n')
oldcs=json.loads((B/'batch01_original_cards.json').read_text())['cards']
changes=[{'card_id':c['id'],'reason':'同一学习目标补全缩写或图示GTP步骤，保留卡片ID与原笔记GUID。'} for c,old in zip(CARDS[:107],oldcs) if c!=old]
(B/'changes_to_batch01.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
a.save()
print({'cumulative_notes':len(CARDS),'new_notes':len(CARDS)-107,'covered_points':sum(k['status']=='covered' for k in KNOWLEDGE),'pending_records':len(a.GAPS),'read_units':sum(u['reading_status']=='actually_read_2026-10-10' for u in UNITS.values()),'updated_batch01_notes':len(changes)})
