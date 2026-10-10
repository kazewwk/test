from en01_origin_genomes import *
import re,hashlib

# Correct translations while keeping the supplied taxonomy and named organisms.
for c in CARDS[107:]:
 c['front']=c['front'].replace('九头虫','水螅')
 for p in c['answer']+c['rubric']:
  p['text']=p['text'].replace('九头虫','水螅').replace('“核／核仁状核心”','“果核／细胞核”')
  p['text']=p['text'].replace('有孔虫所在的根足类群','有孔虫所在的根足生物类群')
  p['text']=p['text'].replace('参与氧化和有毒分子处理的小囊状细胞器。本段以过氧化氢的参与概括其作用','用过氧化氢使有毒分子失活的小囊状细胞器。本段概括其作用')
 c['tags']=['学科::细胞生物学','章节::第01章_绪论','主题::'+('生命树与代谢' if int(c['id'][-4:])<128 else '基因创新与细胞器' if int(c['id'][-4:])<148 else '真核起源与基因组'),'任务::'+c['kind'],'卡片编号::'+c['id']]
 if c['images']:c['tags'].append('需看图')
for k in KNOWLEDGE:
 k['knowledge']=k['knowledge'].replace('九头虫','水螅')
 if k.get('card_id'):
  k['question']=next(c['front'] for c in CARDS if c['id']==k['card_id'])

# Headers contain no additional factual content; their complete paragraphs are mapped.
for ref in [E(92),E(177),E(184),G(31)]:
 omit(ref,'纯章节或总结标题；标题下正文已逐项读取与映射，不用标题代替阅读。')
# The chapter summary adds no new facts, but preserve explicit pointers to all repeated answers.
HANDLING[G(32)]={'status':'repeated_mapped','cards':[c['id'] for c in CARDS if c['front'].startswith(('真核细胞的“细胞器”','结合图1-21解释核','除细胞核外','线粒体内共生起源','叶绿体起源与'))],'reason':'本总结的核、细胞器、骨架及细菌内共生证据分别与上述完整答案重复；保留多卡来源关系。'}
for cid in HANDLING[G(32)]['cards']:
 c=next(c for c in CARDS if c['id']==cid)
 if G(32) not in c['source_units']:c['source_units'].append(G(32))

# Do not silently turn a potentially misleading wording into an established biological rule.
gap(E(127),'英文“recycle energy”是否意指能量循环','本段使用“capture and recycle energy”；已覆盖动物依赖其他生命的供能供物质关系，但能量流动与物质循环须区别，该措辞待与实际热力学正文核对，不作为“能量循环”定论导出。')
gap(G(29),'protist定义是否在全书一致','该图注把protist限为自由生活、单细胞、能移动的真核对象；当前卡明确限定为本段用法，未把它推广为所有原生生物的完整定义，待与全书其他分类用法核对。')

# Repair the first-batch termination answer using its already visually read diagram;
# this is the same recall task, so identity and the existing note GUID remain unchanged.
old=next(c for c in CARDS if c['id']=='RB-CN01-0107')
old['answer'][0]['text']=old['answer'][0]['text'].replace('伴随GTP水解和因子组分变化','伴随GTP水解成GDP和无机磷酸（Pi），并有带GDP的因子组分离开')
old['rubric'][0]['text']+=' 图示GTP→GDP＋Pi及带GDP组分离开；不凭未标注图像自行命名该组分。'
if 'GTP水解成GDP' not in old['answer'][0]['text']:
 old['answer'][0]['text']+=' 图示GTP水解成GDP和无机磷酸（Pi），带GDP的释放因子组分离开；未标注组分不自行赋名。'

scope=[]
for u in UNITS.values():
 n=int(u['unit_id'][-3:])
 if (u['block_id']=='EN01-H000-H030' and n>=92) or u['block_id'] in ['EN01-H031-H033','EN01-H034-H038'] or (u['block_id']=='EN01-H039-H053' and n<=5) or u['unit_id']=='EN11-H009-H013-P004':
  u['reading_status']='actually_read_2026-10-10';scope.append(u)
cache={}
for u in UNITS.values():
 if u['reading_status']!='actually_read_2026-10-10':continue
 if u['file'] not in cache:cache[u['file']]=Path('/workspace/cell-anki/source',u['file']).read_text()
 text=cache[u['file']];marker=f'<!-- BEGIN {u["language"]} {u["block_id"]} -->';start=text.find(marker)
 start=start+len(marker) if start>=0 else 0;pos=text.find(u['text'],start)
 u['line']=text[:pos].count('\n')+1 if pos>=0 else None
 u['location_mode']='file_line_and_stable_paragraph' if pos>=0 else 'file_and_stable_paragraph_no_exact_line'
for u in scope:assert u['unit_id'] in HANDLING,u['unit_id']
for v in HANDLING.values():v['cards']=list(dict.fromkeys(v['cards']))
for k in KNOWLEDGE:
 if k['status']=='covered':
  c=next(c for c in CARDS if c['id']==k['card_id'])
  assert k['answer_anchor'] in [p['anchor'] for p in c['answer']]
  assert k['rubric_anchor'] in [p['anchor'] for p in c['rubric']]
  assert set(k['source_units'])<=set(c['source_units'])
  assert all(UNITS[s]['reading_status']=='actually_read_2026-10-10' for s in k['source_units'])
(B/'source_units.json').write_text(json.dumps(list(UNITS.values()),ensure_ascii=False,indent=2)+'\n')
(B/'resolved_ch01.json').write_text((BASE/'resolved_ch01.json').read_text())
(B/'new_read_units.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
(B/'changes_to_batch01.json').write_text(json.dumps([{'card_id':old['id'],'change':'同一翻译终止题补全图示GTP→GDP＋Pi及带GDP因子组分离开，未命名未标注组分。','reason':'逐步解释图中化学变化，保留原学习目标与GUID。'}],ensure_ascii=False,indent=2)+'\n')
a.save()
