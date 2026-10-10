import en01_universal
from author import *
N('图6-76的真核翻译如何在终止密码子处结束？说明释放因子、GTP、水和核糖体再利用的作用。（需看图：A/P/E位点、UAG及肽链释放）',[
P('图中mRNA沿5′→3′排出AUG、AAC、UGG、UAG，已合成Met—Asn—Trp即甲硫氨酸—天冬酰胺—色氨酸；UAG进入A位点后没有正常携氨基酸tRNA接续。两亚基释放因子结合A位点终止信号，其形状与电荷分布类似tRNA，图示结合后伴随GTP（guanosine triphosphate，鸟苷三磷酸）水解和因子组分变化。','mRNA和肽方向、UAG及A位点；两亚基释放因子，不是终止tRNA；GTP相关步骤按本图范围。','EN06-H040-H046-P014 EN06-H040-H046-P015 EN06-H040-H046-P016','图示5′3′mRNA与MetAsnTrp肽;UAG终止在A位点;释放因子形状电荷与tRNA类似;两亚基释放因子与GTP图示'),
P('释放因子使核糖体肽基转移酶催化水而非氨基酸加入，水解肽链与P位点tRNA的连接，释放肽链羧基端。随后mRNA、tRNA、因子和大小亚基解离，亚基可重新组装用于下一轮翻译。图中的水参与断开酯连接，不能把释放写成再增加一个氨基酸。','水代替氨基酸、肽—tRNA水解与羧基端释放；解离及亚基再利用完整因果。','EN06-H040-H046-P014 EN06-H040-H046-P015','水参与肽tRNA连接水解;释放肽链羧基端;核糖体组分解离与亚基再利用')],images=[('ENFIG0802','front','Figure 6-76，指定英文教材的真核终止示意；不外推所有原核释放因子均为相同两亚基装置。')],kind='翻译终止读图')
RESOLVED=[]
for g in list(GAPS):
 if g['source_unit']==uid('2.21') and g['knowledge'].startswith('支原体英文'):
  RESOLVED.append(dict(g,status='resolved_by_specified_textbook',evidence=[E for E in ['EN01-H000-H030-P080','EN01-H000-H030-P088']],resolution='英文第7版明确Mycoplasma genitalium拼写和哺乳动物寄生营养条件；中文400与英文具体525的对象条件比较进入RB-CN01-0101（实际卡片以题干检索为准）。'))
  GAPS.remove(g)
  for k in KNOWLEDGE:
   if k['status']=='unresolved' and k['source_units']==[g['source_unit']] and k['knowledge']==g['knowledge']:
    k['status']='resolved_duplicate';k['resolution']='以最小基因组教材比较题及RB-CN01-0031覆盖，不另导出重复卡。'
for c in CARDS:
 q=c['front']
 if c['id']=='RB-CN01-0031':c['basis']='教材直接支持数值；条件限定为基于指定双教材比较推导'
 if c['id']=='RB-CN01-0038':
  c['images']=[x for x in c['images'] if x['figure_id']!='CNFIG0022']
  c['front']='细菌的基本结构怎样组织？拟核与真核细胞核怎样区别？'
  c['answer'][0]['text']='本章细菌典型结构为细胞壁、细胞质膜、核区和核糖体，某些种还有荚膜与鞭毛。细菌通常没有核膜围绕的典型核；明显但不规则的拟核（nucleoid）为DNA主要所在区域，其周围为较致密胞质。图1-4的猪丹毒杆菌（Erysipelothrix rhusiopathiae）电镜与模式图已核对，但其中旧“中膜体”标注尚待核实，此题采用完整文字作答。'
  c['rubric'][0]['text']='细胞壁、膜、核区、核糖体；部分种类荚膜与鞭毛；拟核无核膜、不规则、DNA与胞质关系；原图菌名与电镜／模式性质。'
  c['front']+=' 本章图1-4采用哪种细菌电镜，原图模式的旧标注为何应暂缓学习？'
  c['detail']='图1-4未放到此卡以免训练未核实中膜体；原图仍保留在来源目录，并记入媒体待核实表，未称完成这一结构的图像回忆。'
 # Add explicit, consistent topic and task tags.
 if int(c['id'][-4:])<=21:topic='细胞学与学科史'
 elif any(x in q for x in ['古菌','古细菌','三域','原核','细菌','蓝细']):topic='细胞类群与演化'
 elif any(x in q for x in ['病毒','辛德毕斯','衣壳']):topic='病毒与宿主'
 elif any(x in q for x in ['DNA','RNA','基因','蛋白','密码','翻译','核小体']):topic='遗传与表达'
 elif any(x in q for x in ['膜','液泡','质体','骨架']):topic='结构与功能'
 elif any(x in q for x in ['热运动','棘轮','自由能']):topic='能量与物理'
 else:topic='生命基本单位'
 c['tags']=['学科::细胞生物学','章节::第01章_绪论','主题::'+topic,'任务::'+c['kind'],'卡片编号::'+c['id']]
 for m in c['images']:
  if '需看图' not in c['tags']:c['tags'].append('需看图')
# Mark which units were actually read; this includes corroboration only, not uncompleted surrounding chapters.
for u in UNITS.values():
 if (u['language']=='CN' and u['chapter']==1) or (u['block_id']=='EN01-H000-H030' and int(u['unit_id'][-3:])<=91) or (u['block_id']=='EN06-H040-H046' and 13<=int(u['unit_id'][-3:])<=16):u['reading_status']='actually_read_2026-10-10'
(ROOT/'resolved_ch01.json').write_text(json.dumps(RESOLVED,ensure_ascii=False,indent=2)+'\n')
# Exact line numbers are located in the archived integration file, and not guessed from print pagination.
cache={}
for u in UNITS.values():
 if u['reading_status']=='actually_read_2026-10-10':
  if u['file'] not in cache:cache[u['file']]=Path('/workspace/cell-anki/source',u['file']).read_text()
  text=cache[u['file']];marker=f'<!-- BEGIN {u["language"]} {u["block_id"]} -->';start=text.find(marker)
  if start>=0:start+=len(marker)
  else:start=0
  pos=text.find(u['text'],start)
  u['line']=text[:pos].count('\n')+1 if pos>=0 else None
  u['location_mode']='file_line_and_stable_paragraph' if pos>=0 else 'file_and_stable_paragraph_no_exact_line'
(ROOT/'source_units.json').write_text(json.dumps(list(UNITS.values()),ensure_ascii=False,indent=2)+'\n')
# Deduplicate only the accounting IDs in handling, not semantic knowledge.
for v in HANDLING.values():v['cards']=list(dict.fromkeys(v['cards']))
save()
