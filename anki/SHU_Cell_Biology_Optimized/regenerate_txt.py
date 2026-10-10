"""Render plaintext cards.json to a UTF-8 Anki TSV; escape text exactly once."""
from pathlib import Path
import csv,html,json,re,sys
ROOT=Path(__file__).resolve().parent
NAME='SHU_Cell_Biology_Optimized_20261009.txt'
def esc(s):return html.escape(s,quote=True).replace('\n','<br>')
def images(ms):
 return ''.join('<div style="margin:12px 0">'+('<b>读图提示</b><br>'+esc(m['annotation'])+'<br>' if m.get('annotation') else '')+'<img src="'+m['filename']+'" alt="教材原图 '+m['id']+'" style="max-width:100%;height:auto"><br><small>教材原图 · '+m['id']+'</small></div>' for m in ms)
def render(c):
 front=(c['front'] if c['origin']=='original' else esc(c['front']))+images([m for m in c['images'] if m['side']=='front'])
 back='<b>核心答案</b><br>'+esc(c['answer'])
 if c['boundary']:back+='<br><br><b>解释／边界</b><br>'+esc(c['boundary'])
 back+=images([m for m in c['images'] if m['side']=='back'])
 back+='<br><br><b>来源</b><br>'+'<br>'.join('<a href="'+esc(s['url'])+'">'+esc(s['description'])+'</a>' for s in c['sources'])
 if c['images']:
  back+='<br>图像来源：'+'；'.join('<a href="'+esc(m['url'])+'">'+m['id']+' 原文件</a> <a href="'+esc(m['context_url'])+'">上下文</a>' for m in c['images'])
 back+='<br><small>按仓库段落块与原图文件定位；物理页码以原教材为准。'+('评分要点为改编练习参考，非学校官方真题评分。' if c['level']=='L4' else '')+'</small>'
 return front,back,' '.join(c['tags'])
def build():
 data=json.loads((ROOT/'cards.json').read_text(encoding='utf-8'))['cards']
 name=sys.argv[1] if len(sys.argv)>1 else NAME
 with (ROOT/name).open('w',encoding='utf-8',newline='') as f:
  f.write('#separator:Tab\n#html:true\n#notetype:Basic\n#tags column:3\n#columns:Front\tBack\tTags\n')
  csv.writer(f,delimiter='\t',quoting=csv.QUOTE_ALL,lineterminator='\n').writerows(render(c) for c in data)
 sample=[]
 for ch in range(1,18):sample.extend([c for c in data if c['chapter']==ch and c['origin']=='new' and c['images']][:2])
 sample.extend([c for c in data if c['origin']=='original' and '修订::事实或边界' in c['tags'] and c['images']])
 sample.extend([c for c in data if c['level']=='L4'])
 out=['<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>细胞生物学 Anki 预览</title><style>body{max-width:980px;margin:30px auto;padding:0 16px;font:18px/1.6 system-ui;background:#f5f5f5;color:#171717}article{background:white;border:1px solid #ddd;border-radius:8px;padding:20px;margin-bottom:20px}summary{cursor:pointer;color:#1660a0}img{max-width:100%;height:auto}small{color:#666}h1{font-size:26px}</style><h1>细胞生物学 Anki 导入预览</h1><p>点击显示答案；图片从同目录 collection.media 读取。</p>']
 for c in sample:
  fr,ba,_=render(c);fr=re.sub(r'src="(cell_[^"]+)"',r'src="collection.media/\1"',fr);ba=re.sub(r'src="(cell_[^"]+)"',r'src="collection.media/\1"',ba)
  out.append('<article data-id="'+c['id']+'"><small>'+c['id']+' · 第 '+str(c['chapter'])+' 章</small><p>'+fr+'</p><details><summary>显示答案</summary><div>'+ba+'</div></details></article>')
 out.append('</html>');(ROOT/'preview.html').write_text('\n'.join(out),encoding='utf-8')
 print(name,len(data),'notes;',len(sample),'preview notes')
if __name__=='__main__':build()
