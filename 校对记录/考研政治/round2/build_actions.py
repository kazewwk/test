import copy,json,sys
from pathlib import Path
R=Path('/workspace/test-repo'); O=Path('/workspace/politics-books/round2')
sys.path.insert(0,str(R/'scripts'))
from review_politics_ocr import read,write,text,block_digest
P=read(R/'scripts/politics_books_plan.json'); D=read(O/'decisions.json'); A=read(O/'items.json')
blocks={}
for b in P['books']:
 for s in b['sections']:
  for p in read(R/b['folder']/s['folder']/'middle_json.json')['pages']:
   for z in p.get('blocks',[]):blocks[b['id'],p['page_idx']+s['pdf_first_page'],z['index']]=z
out=[]
def add(b,p,i,action,reason,**kw):
 z=blocks[b,p,i]; ids=[a['id'] for a in A if a['book']==b and a['page']==p and (a['block']==i or a['block'] is None and (b,p,i) in [(1,4,14),(1,156,2)]) and D[str(a['id'])]['decision'] in ['source_confirmed_correction_needed','source_graphic_replacement_needed','source_scan_unclear']]
 c={'book_id':b,'pdf_page':p,'block_index':i,'action':action,'reason':reason,'expected_block_sha256':block_digest(z),'original_bbox':z['bbox'],'before':copy.deepcopy(z),'source_sha256':P['books'][b-1]['sha256'],'verification':'visual comparison with original PDF region','review_round':2,'candidate_ids':ids,**kw}
 out.append(c)
def sub(b,p,i,old,new,reason):
 assert text(blocks[b,p,i]).count(old)==1,(b,p,i,old,text(blocks[b,p,i]))
 add(b,p,i,'replace_substring',reason,old=old,new=new)
add(1,4,14,'replace_text','版权页两行网址中的第二行漏识别，按原页补入。',text='网 址 http://www.hep.edu.cn  \nhttp://www.hep.com.cn',expanded_bbox=[.443,.54,.74,.578])
for p,i in [(18,1),(20,1),(23,0)]:add(1,p,i,'replace_text','原页页眉为导言，删除虚构的数学表达式/数字。',text='导言')
for p,i in [(83,0),(113,0),(119,0)]:add(1,p,i,'remove','原页扫描边缘无此文字，删除模型生成的英文说明或测试句。')
sub(1,156,2,'举部','率部','原图图注为马占山率部鏖战江桥。')
sub(1,286,5,'中共党史学习教育','中共党史的学习教育','原页此处有的字，当前漏字。')
for p in [299,305]:sub(1,p,0,'24世纪','21世纪','原页页眉为把中国特色社会主义推向21世纪。')
sub(1,401,0,'第三章','第三节','原页此处是第三节的页眉，章字误识别。')
sub(2,18,5,'推进国家治理体系','推进国家治理体','原物理页18末字为体，系是下一页首字且已保留，删除跨页重复字。')
sub(2,134,2,'做大做强做优做强','做大做优做强','原页为做大做优做强，删除重复插入的做强。')
sub(2,193,5,'飞夹峰','飞来峰','原页引文标题为飞来峰。')
sub(2,240,12,'离开展谈改善民生','离开发展谈改善民生','原页为离开发展谈改善民生，补入漏识别的发字。')
sub(3,47,4,'中央军委主席向他','中央军委主席习近平亲自向他','原页图片下方长行漏识别习近平亲自五字。')
out[-1]['expanded_bbox']=list(out[-1]['original_bbox']);out[-1]['expanded_bbox'][2]=.97
sub(4,214,5,'离开展发','离开发展','原页为离开发展，两字顺序被错误交换。')
sub(5,125,0,'第二节','第三节','原PDF可见页眉及原生文字均为第三节。')
sub(5,170,6,'重要性','重要力','该页正文末尾为重要力，量在下一物理页开头；按原页恢复分界。')
add(3,155,5,'mark_source_unclear','原扫描要求的之后字迹褪色，当前之字不能可靠核实；保留缺字标记和原始裁剪，不按语境猜字。',old='要求的之一。',new='要求的〔原扫描此字褪色，无法可靠辨认〕一。',image_note='此段首行“要求的”之后一个字在原扫描中褪色，保留原图；缺字未作推测补写。')
for b,p,i,note in [(1,61,2,'必读文献栏目图标，按原图保留。'),(1,66,2,'碑刻文字，按原图保留书写方向和字形。'),(1,81,2,'延伸阅读栏目图标，按原图保留。'),(1,87,2,'原页二维码图形，按原图保留。'),(1,153,2,'原页二维码图形，按原图保留。'),(1,207,0,'延伸阅读栏目图标，按原图保留。'),(1,425,2,'延伸阅读栏目图标，按原图保留。'),(2,85,0,'本章小结装饰印章，按原图保留。'),(2,211,3,'本章小结装饰印章，按原图保留。'),(2,235,3,'本章小结装饰印章，按原图保留。'),(3,147,7,'德字的字形演变图，按原图保留。'),(5,1,7,'封面出版社标志，按原图保留。'),(5,67,2,'原页知识拓展栏目书本图标，按原图保留。'),(5,205,2,'原页知识拓展栏目书本图标，按原图保留。')]:
 add(b,p,i,'source_image','模型将原页图形误判成文字或空页眉，恢复原图。',image_note=note)
for b,p,i in [(1,61,3),(1,81,3),(1,207,3),(1,253,3),(1,425,3),(2,67,2),(2,85,4),(2,211,4),(2,235,4)]:
 add(b,p,i,'change_type','原页此区域是正文栏目标题；改正页眉分类，使章节阅读版保留该标题。',new_type='paragraph_title',level=2)
add(1,87,3,'change_type','此段为正文续段；改正页眉分类，使章节阅读版保留正文。',new_type='text')
assert len({(c['book_id'],c['pdf_page'],c['block_index']) for c in out})==len(out)
covered={i for c in out for i in c['candidate_ids']}
required={int(i) for i,d in D.items() if d['decision'] in ['source_confirmed_correction_needed','source_graphic_replacement_needed','source_scan_unclear']}
assert required<=covered,required-covered
write(O/'actions.json',out);print('actions',len(out),'covered',len(covered))
