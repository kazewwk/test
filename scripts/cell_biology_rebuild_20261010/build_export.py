from pathlib import Path
import json,html,csv,hashlib,re,shutil,zipfile
from urllib.parse import quote
R=Path('/tmp/biology_rebuild');O=R/'output';M=O/'collection.media';M.mkdir(exist_ok=True)
S=Path('/workspace/cell-anki/source');SNAP='b036244ba7c8f82d6c35602a5e570d6729b0bee4'
cs=json.loads((R/'cards_ch01.json').read_text())['cards'];ks=json.loads((R/'knowledge_ch01.json').read_text());us={x['unit_id']:x for x in json.loads((R/'source_units.json').read_text())};fs={x['id']:x for x in json.loads(Path('/workspace/cell-anki/work/figures.json').read_text())}
def url(path,line=None):return 'https://github.com/kazewwk/test/blob/'+SNAP+'/'+quote('细胞生物学制卡/'+path,safe='/')+(f'#L{line}' if line else '')
def esc(s):return html.escape(s,quote=True).replace('\n','<br>').replace('\t',' ')
media={}
for c in cs:
 for m in c['images']:
  f=fs[m['figure_id']];p=S/f['path'];b=p.read_bytes();sha=hashlib.sha256(b).hexdigest();assert sha==f['sha256'];name=f'cell_rebuild_{f["id"]}_{sha[:10]}.jpg';m['filename']=name;m['sha256']=sha
  if name not in media:shutil.copyfile(p,M/name);media[name]={'filename':name,'figure_id':f['id'],'original_file':f['path'],'sha256':sha,'bytes':len(b),'size':f['size'],'url':url(f['path']),'review':'actual_original_view_2026-10-10','cards':[]}
  media[name]['cards'].append(c['id'])
 for sid in c['source_units']:assert us[sid]['reading_status']=='actually_read_2026-10-10',sid
CSS='''.card{font-family:Arial,"Noto Sans CJK SC",sans-serif;font-size:19px;line-height:1.65;text-align:left;color:#222;background:#fff;margin:14px;overflow-wrap:anywhere}img{max-width:100%;height:auto}h3{font-size:1.04em;margin:1em 0 .3em;color:#1f5571}p{margin:.35em 0}small,.source{font-size:12px;line-height:1.5;color:#666}.figure{margin:12px 0;padding:6px;border:1px solid #ddd}.figure figcaption{font-size:12px}.nightMode .card{color:#eee;background:#202124}.nightMode h3{color:#91c9e8}.nightMode .source{color:#bbb}a{color:#2675a0} .answer-part{margin-bottom:.65em}'''
def imgs(c,side):
 return ''.join('<figure class="figure"><img src="'+m['filename']+'" alt="'+m['figure_id']+'"><figcaption>'+esc(m['annotation'])+'</figcaption></figure>' for m in c['images'] if m['side']==side)
rows=[]
for c in cs:
 front=esc(c['front'])+imgs(c,'front')
 back='<h3>完整答案</h3>'+''.join('<p class="answer-part" id="'+p['anchor']+'"><b>'+p['anchor']+'</b> '+esc(p['text'])+'</p>' for p in c['answer'])
 back+='<h3>必答点</h3>'+''.join('<p id="'+p['anchor']+'"><b>'+p['anchor']+'</b> '+esc(p['text'])+'</p>' for p in c['rubric'])
 if c['detail']:back+='<h3>理解与联系</h3><p>'+esc(c['detail'])+'</p>'
 back+=imgs(c,'back')
 back+='<h3>依据与来源</h3><p>'+esc(c['basis'])+'。</p><div class="source">'
 for sid in c['source_units']:
  u=us[sid];book='丁明孝等《细胞生物学》第5版' if u['language']=='CN' else 'Molecular Biology of the Cell，第7版'
  loc=u['file']+(f'，文件第{u["line"]}行' if u['line'] else '')+'，段落 '+sid
  back+='<p><a href="'+url(u['file'],u['line'])+'">'+esc(book+'；'+loc)+'</a></p>'
 back+='</div><p class="source">卡片ID：'+c['id']+'<br>知识点ID：'+esc(' '.join(c['knowledge_ids']))+'</p>'
 tags=' '.join(c['tags']);assert '\t' not in front+back+tags and '\n' not in front+back+tags
 c['front_html']=front;c['back_html']=back;rows.append((front,back,tags))
name='SHU_Cell_Biology_Rebuild_Batch01_20261010'
with (O/(name+'.tsv')).open('w',encoding='utf-8',newline='') as f:
 for row in rows:f.write('\t'.join(row)+'\n')
(O/'cards.json').write_text(json.dumps({'cards':cs},ensure_ascii=False,indent=2)+'\n')
(O/'knowledge.json').write_text(json.dumps(ks,ensure_ascii=False,indent=2)+'\n')
(O/'media_manifest.json').write_text(json.dumps(list(media.values()),ensure_ascii=False,indent=2)+'\n')
with (O/'coverage.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['教材位置','具体知识点','知识点ID','卡片ID','答案对应位置','是否明确要求回忆','必答点位置','处理状态'])
 for k in ks:
  loc='；'.join(us[s]['file']+(f':{us[s]["line"]}' if us[s]['line'] else '')+' / '+s for s in k['source_units'])
  w.writerow([loc,k['knowledge'],k['knowledge_id'],k.get('card_id',''),k.get('answer_anchor',''),'是' if k.get('explicit_recall') else '否',k.get('rubric_anchor',''),k['status']])
read=[{k:u.get(k) for k in ['unit_id','block_id','language','file','line','location_mode','kind','sha256','reading_status']} for u in us.values() if u['reading_status']=='actually_read_2026-10-10']
(O/'read_positions.json').write_text(json.dumps(read,ensure_ascii=False,indent=2)+'\n')
shutil.copyfile(R/'gaps_ch01.json',O/'gaps.json');shutil.copyfile(R/'resolved_ch01.json',O/'resolved_issues.json');shutil.copyfile(R/'handling_ch01.json',O/'source_unit_handling.json')
(O/'card.css').write_text(CSS)
preview='<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+CSS+'</style><body class="card">'
for c in cs:preview+='<article data-card="'+c['id']+'"><h2>'+c['id']+'</h2><div class="front">'+c['front_html']+'</div><hr>'+c['back_html']+'</article><hr>'
preview+='</body></html>';preview=preview.replace('src="cell_rebuild_','src="collection.media/cell_rebuild_');(O/'preview.html').write_text(preview)
with zipfile.ZipFile(O/'make-biology-anki_complete_coverage_skill.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted((R/'skill').rglob('*')):
  if p.is_file():z.write(p,'make-biology-anki/'+str(p.relative_to(R/'skill')))
print(json.dumps({'notes':len(cs),'knowledge_covered':sum(k['status']=='covered' for k in ks),'embedded_original_media':len(media),'read_units':len(read)},ensure_ascii=False))
