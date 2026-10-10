from pathlib import Path
import json,csv,hashlib,zipfile,collections
R=Path('/tmp/biology_rebuild/batch02');O=R/'output'
cards=json.loads((O/'cards.json').read_text())['cards'];ks=json.loads((O/'knowledge.json').read_text());us=json.loads((R/'source_units.json').read_text());new=json.loads((R/'new_read_units.json').read_text());gaps=json.loads((O/'gaps.json').read_text());handling=json.loads((R/'handling_ch01.json').read_text());media=json.loads((O/'media_manifest.json').read_text())
handling['EN06-H040-H046-P013']={'status':'no_new_knowledge','cards':[],'reason':'已读交叉核对小节纯标题；P014—P016正文和原图均已映射到翻译终止完整题。'}
(R/'handling_ch01.json').write_text(json.dumps(handling,ensure_ascii=False,indent=2)+'\n')
(O/'source_unit_handling.json').write_text(json.dumps(handling,ensure_ascii=False,indent=2)+'\n')
shutil=None
for name in ['changes_to_batch01.json','new_read_units.json']:(O/name).write_bytes((R/name).read_bytes())
blocks=[]
for bid in dict.fromkeys(u['block_id'] for u in us):
 a=[u for u in us if u['block_id']==bid];n=sum(u['reading_status']=='actually_read_2026-10-10' for u in a)
 blocks.append({'block_id':bid,'language':a[0]['language'],'mapped_chinese_chapter':a[0]['chapter'],'source_file':a[0]['file'],'total_units':len(a),'actually_read_units':n,'status':'read_all_provided_units' if n==len(a) else 'partially_read' if n else 'not_yet_read','content_certification':'具体知识覆盖及缺口见coverage.csv；读完单元不等于无缺口。'})
(O/'global_reading_status.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2)+'\n')
nextu=next(u for u in us if u['block_id']=='EN02-H000-H008')
text=Path('/workspace/cell-anki/source',nextu['file']).read_text();pos=text.find(nextu['text'],text.find('<!-- BEGIN EN EN02-H000-H008 -->'))
nextline=text[:pos].count('\n')+1 if pos>=0 else None
resume={'task':'细胞生物学全材料完整问答重制','status':'in_progress_not_complete_book','batch':'02 cumulative','notes':len(cards),'new_notes_since_batch01':len(cards)-107,'covered_point_records':sum(k['status']=='covered' for k in ks),'unresolved_point_records':len(gaps),'read_units_cumulative':sum(u['reading_status']=='actually_read_2026-10-10' for u in us),'read_units_this_batch':len(new),'source_characters_this_batch':sum(len(u['text']) for u in new),'last_card_id':cards[-1]['id'],'next_card_id':'RB-CN01-0219','last_knowledge_id':max(k['knowledge_id'] for k in ks),'next_knowledge_sequence':max(int(k['knowledge_id'].rsplit('-',1)[1]) for k in ks)+1,'completed_reading_blocks':['CN01-S00','CN01-S01','CN01-S02','EN01-H000-H030','EN01-H031-H033','EN01-H034-H038','EN01-H039-H053','EN01-EXERCISES'],'completed_meaning':'以上提供的文本单元均实际逐段读取；图像逐幅查看。仍有原图、标尺及疑点缺口，不能理解为这些范围已无遗漏。','corroboration_only':['EN06-H040-H046-P013—P016','EN11-H009-H013-P004'],'next_material':{'unit_id':nextu['unit_id'],'file':nextu['file'],'line':nextline,'text':nextu['text']},'remaining':'第1章文件夹尚有英文第2章化学正文与面板、第3章蛋白质扩展、第23章病原体及习题未读；中文第2—16章和免疫补充专题及其他英文映射、各章习题也未完成。','source_snapshot':'b036244ba7c8f82d6c35602a5e570d6729b0bee4','source_pdf_review':'中文原扫描PDF有384页，已打开并核实部分页与图；原PDF逐页完整视觉校对尚未完成，不能以文本提取代替此项声明。英文原PDF未提供，仅有实际可读文本、映射及原图裁片。','target_institution':'沿用既有SHU材料命名；没有新增官方大纲或真题频率证据','exam_year_and_subject':'未提供，不以导出日期代替考试年份','installed_cloud_skill_modified':False,'skill_updated_location':'GitHub skills/make-biology-anki 及可安装技能zip；本次采用修订规则'}
(O/'RESUME.json').write_text(json.dumps(resume,ensure_ascii=False,indent=2)+'\n')
with (O/'pending_items.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['来源单元','知识或问题','状态','原因'])
 for g in gaps:w.writerow([g['source_unit'],g['knowledge'],g['status'],g['reason']])
with (O/'new_cards.tsv').open('w',encoding='utf-8',newline='') as f:
 for c in cards[107:]:f.write('\t'.join([c['front_html'],c['back_html'],' '.join(c['tags'])])+'\n')
check={'status':'PASS','actual_checks':['218条TSV各3个真实Tab分隔字段，全部非空，UTF-8回读','Basic一笔记一张卡，无Cloze、反向模板、独立图册牌组','卡片ID和知识点ID唯一，知识记录定位到实际答案A及必答点R','已覆盖记录均有明确回忆目标、真实源段定位；未核实记录无伪造答案位置','657个实际已读源单元均有处理记录，纯标题与书目注明理由','86张媒体全部与原始文件SHA256一致，媒体引用完整且无未引用文件','原生Anki空库、重复导入及107→218升级检查通过','升级保留首批全部107条笔记ID/GUID和两个复习进度测试哨兵','390px与1100px无横向溢出，所有图片解码成功，手机预览已实际查看'],'semantic_coverage_certified':False,'book_complete':False,'physical_android_device':'not tested','important_limit':'结构检查不能证明学术内容或全书无遗漏，需逐条阅读覆盖表与pending_items.csv；原扫描PDF逐页视觉核对未完成。'}
(O/'quality_checks.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
md='''# 细胞生物学完整问答重制 · 第2批累计包

直接下载并用 **AnkiDroid 打开 SHU_Cell_Biology_Rebuild_Batch02_Cumulative_20261010.apkg**。一次导入含全部已使用图片，无需复制媒体目录，无需 Obsidian。已导入第1批107张时，本累计包会增加111张并更新同一任务的已有卡。

累计218条笔记/218张Basic卡，86张教材原图嵌入79张相关学习卡；没有独立图册、Cloze或自动反向卡。本批新增111张。40张首批卡补全缩写或翻译终止图示步骤，卡片ID与笔记GUID保留。

卡背直接显示完整答案、必答点、必要联系、教材依据、真实文件行号及稳定段落定位、唯一卡片ID与知识点ID。机制保留条件和因果，表格逐项保留，历史数据注明版本估算。习题的推导明确写前提、推理与限制；来源不确定的地方不会填成事实。为了让题目可独立回忆，少数有标签的原图放在卡背复核；真正依赖给定图的数据和结构解释题正面有图。

## 已实际读取范围

中文第1章提供的整合文本与16幅原始图片已读取；中文资料的疑点仍见缺口表。英文教材第1章正文按原顺序从通用生命特征到生命树、真核起源、基因组、模式生物完整读取；其15道习题、2幅习题原图和书目也已读取。英文第1章的70个原始图像文件均逐幅查看并进入相关学习卡。译码终止与ABC缩写另有具体小节交叉核对。累计657个实际读取的源单元，本批361个。

这不是全书完成版。第1章文件夹还映射了未完成的英文细胞化学、化学面板、蛋白质、病原体扩展及病原体习题；中文第2—16章、免疫专题及其他英文映射仍待逐批完成。中文原扫描PDF的逐页完整视觉校对尚未完成；英文原PDF没有提供。阅读文本和提取原图不等于已经排除原PDF提取遗漏。

1627条已覆盖知识记录可在coverage.csv中逐项定位到答案与必答点；41条待核实记录在pending_items.csv中逐条说明。另外所有未读范围在global_reading_status.json及RESUME.json登记，不能把41当成全书仅余41个知识点。

## 验证

UTF-8真实Tab三列数据已回读。原生Anki后端空库导入218张、重复导入不重复；从107张升级为218张保留全部原笔记身份和测试复习进度，全部字段与导出一致。86张媒体与原图逐文件哈希相同，无缺失或闲置媒体；手机宽度390px和桌面1100px无溢出，全部图片解码，手机预览已查看。没有真实安卓设备实机测试。结构通过不等于全书学术无遗漏。

## 文件

APKG是安卓正式导入文件。累计三列TSV为备用；new_cards.tsv仅新增111条。coverage.csv、pending_items.csv、source_unit_handling.json、read_positions.json为覆盖和阅读证据；cards.json/knowledge.json用于继续核查。preview.html是阅读预览，不能代替Anki导入。技能zip和仓库skills/make-biology-anki已按“完整覆盖→准确→完整解释→评分→复习负担”修订；云端账户内的已安装技能没有写入接口，因此没有声称该安装副本被修改。

源文件固定在GitHub快照b036244ba7c8f82d6c35602a5e570d6729b0bee4。版本为丁明孝等《细胞生物学》第5版及Molecular Biology of the Cell第7版。不编造印刷页码、考试年份、专业或高频统计。下一起点EN02-H000-H008，详细位置、卡片编号和未完成范围见RESUME.json。
'''
(O/'README.md').write_text(md)
for u in us:
 if u['reading_status']=='actually_read_2026-10-10':assert u['unit_id'] in handling,u['unit_id']
assert len(cards)==218 and len(new)==361 and len(media)==86
for p in [O/'SHU_Cell_Biology_Rebuild_Batch02_Cumulative_20261010.tsv',O/'new_cards.tsv']:
 with p.open(encoding='utf8',newline='') as f:rows=list(csv.reader(f,delimiter='\t'))
 assert len(rows)==(218 if p.name.startswith('SHU_') else 111) and all(len(row)==3 and all(row) for row in rows)
name='Batch02_cumulative_cards_and_audit.zip'
with zipfile.ZipFile(O/name,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(O.rglob('*')):
  if p.is_file() and p.name not in [name,'file_manifest.json']:z.write(p,str(p.relative_to(O)))
manifest=[]
for p in sorted(O.rglob('*')):
 if p.is_file() and p.name!='file_manifest.json':manifest.append({'file':str(p.relative_to(O)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(O/'file_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'notes':len(cards),'covered_points':1627,'pending':len(gaps),'read_units':657,'new_read_units':len(new),'last_knowledge_id':resume['last_knowledge_id'],'next':resume['next_material'],'files':len(manifest)+1},ensure_ascii=False))
