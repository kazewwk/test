import finalize_batch01
from author import *
def add_point(c,label,refs,anchor):
 kid=next_kid();c['knowledge_ids'].append(kid)
 KNOWLEDGE.append({'knowledge_id':kid,'knowledge':label,'source_units':refs,'card_id':c['id'],'answer_anchor':'A'+str(anchor),'rubric_anchor':'R'+str(anchor),'explicit_recall':True,'status':'covered','question':c['front']})
for c in CARDS:
 if c['id']=='RB-CN01-0034':
  c['front']='中英文教材如何估算新生儿与成人细胞总量？总个数与细胞类型数如何区别？'
  c['answer'][0]['text']='中文第5版估计新生儿约2×10¹²个细胞，成人约3.7×10¹³个；英文第7版开篇以人体细胞大于10¹³个作数量级概括。人体“200多种”指不同类型，不是总个数。数值是特定版本近似估算，不能视为任何个体的精确常数。'
  c['rubric'][0]['text']='新生儿2×10¹²、中文成人3.7×10¹³、英文大于10¹³；类型数与总数；版本估算限定。'
  c['source_units'].append('EN01-H000-H030-P017')
  add_point(c,'英文人体细胞大于10¹³的数量级概括',['EN01-H000-H030-P017'],1)
 if c['front'].startswith('四种核苷酸怎样编码'):
  c['front']='四种核苷酸怎样编码20种经典氨基酸？列出标准终止信号，解释三联体总数、编码数、简并性及tRNA和核糖体作用。'
  for label in ['标准UAA终止信号','标准UAG终止信号','标准UGA终止信号','由64减3得到61个标准氨基酸编码三联体']:
   add_point(c,label,['EN01-H000-H030-P055','EN06-H040-H046-P014'],1)
 if c['front'].startswith('读图1-2：DNA核苷酸'):
  c['front']='读图1-2：DNA核苷酸怎样形成有极性骨架、互补碱基怎样指导新链？解释共价键、氢键数量、反向链和双螺旋。（需看图：A—E结构与键型）'
  c['answer'][1]['text']+=' 图中A—T间两条连接线对应两个氢键，G—C间三条对应三个氢键，这不同于糖—磷酸的共价骨架。'
  c['rubric'][1]['text']+=' A—T两个、G—C三个氢键，能与共价骨架区别。'
  add_point(c,'图示AT两个氢键',['EN01-H000-H030-P033','EN01-H000-H030-P034'],2)
  add_point(c,'图示GC三个氢键',['EN01-H000-H030-P033','EN01-H000-H030-P034'],2)
 # Include a reference to all later-covered source repetitions without claiming new recall goals.
 if c['id']=='RB-CN01-0031':
  c['answer'][0]['text']=c['answer'][0]['text'].replace('才能维持','可维持')
for k in KNOWLEDGE:
 if k.get('card_id'):
  k['question']=next(c['front'] for c in CARDS if c['id']==k['card_id'])
save()
