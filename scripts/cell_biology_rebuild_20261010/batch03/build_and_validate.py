from pathlib import Path
import csv,hashlib,html,json,re,shutil,tempfile,zipfile,subprocess,sys
from urllib.parse import quote
from anki.collection import Collection
from anki.import_export_pb2 import ExportAnkiPackageOptions,ExportLimit,ImportAnkiPackageRequest,ImportAnkiPackageOptions
B2=Path('anki/SHU_Cell_Biology_Rebuild_20261010/Batch02')
B3=Path('anki/SHU_Cell_Biology_Rebuild_20261010/Batch03')
S=json.loads((B3/'input/authoring_state.json').read_text())
previous=json.loads((B2/'cards.json').read_text())['cards']
new=S['cards']
assert len(previous)==218 and len(new)==71
def write_json(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def esc(text):
    return html.escape(str(text),quote=True).replace('\r','').replace('\n','<br>')
media_by_id={m['figure_id']:m for m in S['media']}
positions=json.loads((B2/'read_positions.json').read_text())
old_positions={u['unit_id']:u for u in positions}
source_root=Path('细胞生物学制卡')
source_text=(source_root/'01_绪论/整合教材.md').read_text(encoding='utf-8')
for u in S['units']:
    assert u['text'] in source_text
    lines=source_text.splitlines()
    segment='\n'.join(lines[u['line']-1:u['line']-1+len(u['text'].splitlines())])
    assert segment==u['text'],u['id']
    u['sha256']=hashlib.sha256(u['text'].encode()).hexdigest()
    u['kind']='image' if u['text'].startswith('![') else ('heading' if u['text'].startswith('####') else 'text_or_table')
    old_positions[u['id']]=u
positions.extend([{k:u[k] for k in ['unit_id','block_id','language','file','line','location_mode','sha256','reading_status','kind']} for u in S['units']])
assert len(positions)==1083 and len({u['unit_id'] for u in positions})==1083
def source_link(uid):
    u=old_positions[uid]
    target='细胞生物学制卡/'+u['file']
    link='https://github.com/kazewwk/test/blob/'+S['source_commit']+'/'+quote(target,safe='/')+'#L'+str(u['line'])
    label=u['file']+' 行'+str(u['line'])+'；'+uid
    return '<a href="'+esc(link)+'">'+esc(label)+'</a>'
def figure_html(record):
    m=media_by_id[record['figure_id']]
    caption=record.get('annotation') or m['figure_id']
    return '<figure class="figure"><img src="'+esc(m['filename'])+'" alt="'+esc(caption)+'"><figcaption>'+esc(caption)+'</figcaption></figure>'
for c in new:
    c['front_html']='<p class="prompt">'+esc(c['front'])+'</p>'+''.join(figure_html(i) for i in c['images'] if i['side']=='front')
    answer='<h3>完整答案</h3>'+''.join('<div class="answer-part" id="'+c['id']+'-'+p['anchor']+'"><b>'+p['anchor']+'</b> '+esc(p['text'])+'</div>' for p in c['answer'])
    scoring='<h3>必答点</h3>'+''.join('<p id="'+c['id']+'-'+p['anchor']+'"><b>'+p['anchor']+'</b> '+esc(p['text'])+'</p>' for p in c['rubric'])
    detail=('<h3>理解与联系</h3><p>'+esc(c['detail'])+'</p>') if c.get('detail') else ''
    figures=''.join(figure_html(i) for i in c['images'] if i['side']=='back')
    support='<h3>依据与来源</h3><div class="source">'+esc(c['basis'])+'；Molecular Biology of the Cell，第7版，第2章及图解2–1至2–6；定位采用文件真实行号与稳定段落ID，不是PDF或教材印刷页码。<br>'+'<br>'.join(source_link(u) for u in c['source_units'])+'<br>卡片ID：'+c['id']+'<br>知识点ID：'+' '.join(c['knowledge_ids'])+'</div>'
    c['back_html']=answer+scoring+detail+figures+support
cards=previous+new
knowledge=json.loads((B2/'knowledge.json').read_text())+S['knowledge']
gaps=json.loads((B2/'gaps.json').read_text())+S['gaps']
handling=json.loads((B2/'source_unit_handling.json').read_text())
handling.update(S['handling'])
assert len(cards)==289
assert len({c['id'] for c in cards})==289
assert len({k['knowledge_id'] for k in knowledge})==len(knowledge)
knowledge_by_id={k['knowledge_id']:k for k in knowledge}
for c in cards:
    assert c['type']=='Basic' and c['front_html'] and c['back_html']
    assert len(c['tags'])>=3 and all(not re.search(r'\s',t) for t in c['tags'])
    assert not any(ch in c['front_html']+c['back_html'] for ch in '\x00\t\n\r\x1f')
    assert all(u in old_positions for u in c['source_units'])
    for kid in c['knowledge_ids']:
        k=knowledge_by_id[kid]
        assert k['status']=='covered' and k['explicit_recall'] is True and k['card_id']==c['id']
        assert k['answer_anchor'] in {p['anchor'] for p in c['answer']}
        assert k['rubric_anchor'] in {p['anchor'] for p in c['rubric']}
    if '需看图' in c['front']:
        assert any(i['side']=='front' for i in c['images'])
for k in knowledge:
    assert all(u in old_positions for u in k['source_units'])
    if k['status']=='covered':
        assert k['card_id'] and k['answer_anchor'] and k['rubric_anchor'] and k['explicit_recall']
for u in S['units']:
    assert u['id'] in handling
cm=B3/'collection.media'
cm.mkdir(exist_ok=True)
for p in (B2/'collection.media').iterdir():
    if p.is_file():shutil.copyfile(p,cm/p.name)
for m in S['media']:
    src=source_root/m['path']
    raw=src.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==m['git_blob_sha'],m['path']
    assert m['reviewed'] is True and m['original'] is True
    m['sha256']=hashlib.sha256(raw).hexdigest()
    m['bytes']=len(raw)
    shutil.copyfile(src,cm/m['filename'])
all_media={p.name:p for p in cm.iterdir() if p.is_file()}
references=set()
for c in cards:
    references.update(re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']',c['front_html']+c['back_html']))
assert references==set(all_media),(references-set(all_media),set(all_media)-references)
assert len(all_media)==219
write_json(B3/'cards.json',{'cards':cards})
write_json(B3/'knowledge.json',knowledge)
write_json(B3/'gaps.json',gaps)
write_json(B3/'source_unit_handling.json',handling)
write_json(B3/'read_positions.json',positions)
write_json(B3/'new_read_units.json',S['units'])
write_json(B3/'new_figure_review.json',S['media'])
write_json(B3/'resolved_issues.json',json.loads((B2/'resolved_issues.json').read_text())+S['resolved_issues'])
glob=json.loads((B2/'global_reading_status.json').read_text())
for b in glob:
    if b['block_id'] in {u['block_id'] for u in S['units']}:
        count=sum(u['block_id']==b['block_id'] for u in S['units'])
        assert count==b['total_units']
        b['actually_read_units']=count
        b['status']='read_all_provided_units'
        b['content_certification']='原图逐张审阅；内容覆盖与未核实信息见本批coverage.csv、gaps.json，读完不等于无缺口。'
write_json(B3/'global_reading_status.json',glob)
def tsv_export(path,notes):
    lines=[]
    for c in notes:
        line='\t'.join([c['front_html'],c['back_html'],' '.join(c['tags'])])
        assert len(line.split('\t'))==3 and '\n' not in line
        lines.append(line)
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    check=path.read_text(encoding='utf-8').splitlines()
    assert len(check)==len(notes) and all(len(x.split('\t'))==3 and all(x.split('\t')) for x in check)
tsv_export(B3/'SHU_Cell_Biology_Rebuild_Batch03_Cumulative_20261010.tsv',cards)
tsv_export(B3/'new_cards.tsv',new)
columns=['教材位置','具体知识点','知识点ID','卡片ID','答案对应位置','是否明确要求回忆','必答点位置','处理状态','备注']
with (B3/'coverage.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(columns)
    for k in knowledge:
        loc='；'.join(old_positions[u]['file']+' 行'+str(old_positions[u]['line'])+' '+u for u in k['source_units'])
        w.writerow([loc,k['knowledge'],k['knowledge_id'],k.get('card_id',''),k.get('answer_anchor',''),'是' if k['explicit_recall'] else '否',k.get('rubric_anchor',''),k['status'],k.get('reason','')])
with (B3/'pending_items.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['教材位置','知识点','处理状态','原因'])
    for g in gaps:
        us=g.get('source_units') or [g['source_unit']]
        loc='；'.join(old_positions[u]['file']+' 行'+str(old_positions[u]['line'])+' '+u for u in us)
        w.writerow([loc,g['knowledge'],g['status'],g['reason']])
css=(B2/'card.css').read_text()
css+='\n.card.nightMode{color:#eee;background:#202124}.card.nightMode h3{color:#91c9e8}.card.nightMode .source{color:#bbb}\n'
(B3/'card.css').write_text(css)
name='SHU_Cell_Biology_Rebuild_Batch03_Cumulative_20261010.apkg'
oldpkg=B2/'SHU_Cell_Biology_Rebuild_Batch02_Cumulative_20261010.apkg'
assert hashlib.sha256(oldpkg.read_bytes()).hexdigest()=='ec254091428344ee6175ebdf7296f3d2752e1ded0db39b11b977656f6a8fa289'
def package_request(path):
    return ImportAnkiPackageRequest(package_path=str(path.resolve()),options=ImportAnkiPackageOptions(merge_notetypes=True,with_scheduling=False,with_deck_configs=False))
def identities(col):
    result={}
    for nid,guid,tags in col.db.all('select id,guid,tags from notes'):
        found=re.search(r'卡片编号::(RB-CN01-\d{4})',tags)
        assert found
        result[found.group(1)]=(nid,guid)
    return result
def check_collection(col,count):
    assert col.db.scalar('select count(*) from notes')==count
    assert col.db.scalar('select count(*) from cards')==count
    assert all(m['type']==0 for m in col.models.all() if col.models.use_count(m))
    assert not any('图册' in d['name'] for d in col.decks.all())
    check=col.media.check()
    assert not check.missing and not check.unused,(check.missing,check.unused)
with tempfile.TemporaryDirectory(prefix='cell_anki_batch03_') as tmp:
    root=Path(tmp)
    build=root/'build';build.mkdir()
    col=Collection(str(build/'collection.anki2'))
    try:
        col.import_anki_package(package_request(oldpkg))
        initial=identities(col)
        assert len(initial)==218
        model=col.models.by_name('细胞生物学完整问答·20261010')
        assert model and model['type']==0
        model['css']=css
        col.models.save(model)
        did=col.decks.id('SHU细胞生物学·完整问答重制20261010::第01章_绪论')
        for c in previous:
            nid=initial[c['id']][0]
            assert col.db.scalar('select flds from notes where id=?',nid)==c['front_html']+'\x1f'+c['back_html']
        for c in new:
            note=col.new_note(model)
            note['Front']=c['front_html'];note['Back']=c['back_html'];note.tags=c['tags']
            col.add_note(note,did)
        for p in all_media.values():shutil.copyfile(p,Path(col.media.dir())/p.name)
        check_collection(col,289)
        assert all(identities(col)[key]==value for key,value in initial.items())
        limit=ExportLimit();limit.whole_collection.SetInParent()
        exported=col.export_anki_package(out_path=str((B3/name).resolve()),options=ExportAnkiPackageOptions(with_media=True,with_scheduling=False,with_deck_configs=False,legacy=True),limit=limit)
        assert exported==289
    finally:col.close()
    with zipfile.ZipFile(B3/name) as z:
        assert z.testzip() is None and 'collection.anki2' in z.namelist()
        archive_media=json.loads(z.read('media'))
        assert set(archive_media.values())==set(all_media)
        for number,filename in archive_media.items():
            assert hashlib.sha256(z.read(number)).digest()==hashlib.sha256(all_media[filename].read_bytes()).digest()
    fresh=root/'fresh';fresh.mkdir();col=Collection(str(fresh/'collection.anki2'))
    try:
        request=package_request(B3/name)
        col.import_anki_package(request)
        check_collection(col,289)
        before=identities(col)
        sentinel=col.db.scalar('select min(id) from cards')
        col.db.execute('update cards set type=2,queue=2,due=1234,ivl=10,reps=7,lapses=1 where id=?',sentinel)
        schedules=col.db.all('select id,type,queue,due,ivl,reps,lapses from cards order by id')
        col.import_anki_package(request)
        check_collection(col,289)
        assert identities(col)==before
        assert col.db.all('select id,type,queue,due,ivl,reps,lapses from cards order by id')==schedules
        for c in cards:
            nid=before[c['id']][0]
            assert col.db.scalar('select flds from notes where id=?',nid)==c['front_html']+'\x1f'+c['back_html']
    finally:col.close()
    incremental=root/'incremental';incremental.mkdir();col=Collection(str(incremental/'collection.anki2'))
    try:
        col.import_anki_package(package_request(oldpkg))
        old_ident=identities(col)
        old_cards=col.db.list('select id from cards order by id')
        for index,cid in enumerate([old_cards[0],old_cards[-1]]):
            col.db.execute('update cards set type=2,queue=2,due=?,ivl=?,reps=?,lapses=? where id=?',2345+index,14+index,20+index,2+index,cid)
        schedules={row[0]:row for row in col.db.all('select id,type,queue,due,ivl,reps,lapses from cards order by id')}
        col.import_anki_package(package_request(B3/name))
        check_collection(col,289)
        now=identities(col)
        assert all(now[k]==v for k,v in old_ident.items())
        for cid,values in schedules.items():
            assert col.db.first('select id,type,queue,due,ivl,reps,lapses from cards where id=?',cid)==values
    finally:col.close()
report={'status':'PASS','package':name,'notes':289,'cards':289,'basic':289,'cloze':0,'new_notes':71,'embedded_media':219,
    'fresh_native_import':'PASS','repeat_native_import':'PASS','incremental_218_to_289':'PASS','existing_note_ids_and_guids_preserved':218,
    'existing_review_states_preserved':218,'review_sentinels':2,'stored_fields_equal_export':'PASS','missing_media':0,'unused_media':0,
    'zip_media_original_hashes':'PASS','format':'legacy APKG / collection.anki2 / native Anki 26.9.3','physical_android_device':'not tested',
    'sha256':hashlib.sha256((B3/name).read_bytes()).hexdigest(),'bytes':(B3/name).stat().st_size}
write_json(B3/'apkg_validation.json',report)
statuses={x:sum(k['status']==x for k in knowledge) for x in sorted({k['status'] for k in knowledge})}
quality={'status':'PASS','new_cards':71,'cumulative_cards':289,'read_units':1083,'new_read_units':426,
    'new_original_image_files_actually_viewed':133,'total_embedded_media':219,'knowledge_records':len(knowledge),'knowledge_statuses':statuses,
    'unresolved_items':len(gaps),'source_line_checks':'PASS','unique_card_and_knowledge_ids':'PASS','basic_only':'PASS',
    'three_column_utf8_real_tab_tsv':'PASS','knowledge_answer_rubric_foreign_keys':'PASS','media_references':'PASS',
    'semantic_coverage_certified':False,'full_book_complete':False,'all_original_pdf_pages_reviewed':False}
write_json(B3/'quality_checks.json',quality)
html_start='<!doctype html><html lang="zh"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+css+'</style><body class="card">'
def preview_images(fragment):
    return re.sub(r'(<img\b[^>]*\bsrc=["\'])', r'\1collection.media/', fragment)
preview=html_start+''.join('<article class="note" data-card="'+c['id']+'"><h2>'+c['id']+'</h2>'+c['front_html']+'<hr>'+c['back_html']+'<hr></article>' for c in cards)+'</body></html>'
preview=preview_images(preview)
(B3/'preview.html').write_text(preview,encoding='utf-8')
subprocess.run([sys.executable,'-m','playwright','install','--with-deps','chromium'],check=True)
from playwright.sync_api import sync_playwright
browser_results=[]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':390,'height':1400})
    page.goto((B3/'preview.html').resolve().as_uri())
    page.wait_for_function('Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)')
    for width in [390,1100]:
        page.set_viewport_size({'width':width,'height':1400})
        assert page.evaluate('document.documentElement.scrollWidth')<=width
        broken=page.evaluate('Array.from(document.images).filter(i=>!i.complete || !i.naturalWidth).length')
        assert broken==0
        browser_results.append({'width':width,'overflow':False,'broken_images':broken})
    page.set_viewport_size({'width':390,'height':1400})
    selected=next(c for c in cards if c['id']=='RB-CN01-0286')
    (B3/'mobile_single_preview.html').write_text(preview_images(html_start+selected['front_html']+'<hr>'+selected['back_html']+'</body></html>'),encoding='utf-8')
    page.goto((B3/'mobile_single_preview.html').resolve().as_uri())
    page.wait_for_function('Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)')
    page.screenshot(path=str(B3/'mobile_preview.png'),full_page=True)
    browser.close()
write_json(B3/'browser_validation.json',{'status':'PASS','viewports':browser_results,'screenshot':'mobile_preview.png','actual_image_view_by_author':'pending','physical_android_device':'not tested'})
skillroot=Path('skills/make-biology-anki')
with zipfile.ZipFile(B3/'make-biology-anki_complete_coverage_skill.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(skillroot.rglob('*')):
        if p.is_file():z.write(p,'make-biology-anki/'+str(p.relative_to(skillroot)))
resume={'batch':'Batch03','last_card_id':cards[-1]['id'],'last_knowledge_sequence':S['sequence'],'last_read_unit':'EN02-H042-H090-P334',
    'next_start':S['next_start'],'new_cards':71,'cumulative_cards':289,'embedded_media':219,'unresolved_items':len(gaps),
    'full_book_complete':False,'original_pdf_complete_visual_review':False,'source_commit':S['source_commit'],'baseline_commit':S['baseline_commit']}
write_json(B3/'RESUME.json',resume)
readme=f"""# 细胞生物学完整问答重制 · Batch03累计包
安卓下载本目录的{name}，用AnkiDroid打开即可导入；219张媒体已嵌入对应卡片，不需要媒体目录操作。
本批新增71张Basic，累计289张；无反向卡、无Cloze、无独立图册。旧218张卡的身份及测试复习状态保留。

实际完成范围：Molecular Biology of the Cell第7版，第2章The Chemical Components of a Cell及总结，配套图解2–1至2–6。
对应已提供整合文件01_绪论/整合教材.md真实行953–1837，92＋334个单元逐段读完；133个引用原图文件逐张实际查看并嵌入相关卡片。
英文第2章其余催化、能量、食物利用正文及图解2–7至2–9尚未读完，下一起点见RESUME.json。
中文第1章可读文本和英文第1章已在前两批处理；这不等于原版PDF逐页核查完成，中文其余章、蛋白质和病原体等材料仍待持续制作。

每张新卡有完整答案、必答点、可用的理解说明、真实来源定位、卡片ID和知识点ID。
coverage.csv含{len(knowledge)}条知识记录；其中{statuses.get('covered',0)}条有卡片、答案段和评分段对应。
{len(gaps)}项仍待核实或补图，见pending_items.csv与gaps.json；其中包括元素表颜色、同位素口径、裁切比例尺和原版标签配对。
已读不等于无缺口；没有据未读材料计算全书知识覆盖率，也没有声称全书无遗漏或绝对无学术错误。

原生Anki26.9.3已验证空集合、重复与218→289增量导入，旧身份和复习状态保留，媒体引用及字节校验通过。
手机390px和桌面1100px网页显示检查通过；尚未在实体安卓设备测试。程序检查不代替语义和学术复核。
source_pdf_review为原版PDF外网恢复尝试；只有确实取得且另行查看的原图才会纳入完成记录。
修订skill位于仓库skills/make-biology-anki，ZIP为该目录实际打包；云账户只读技能没有声称被写回。
"""
(B3/'README.md').write_text(readme,encoding='utf-8')
with zipfile.ZipFile(B3/'Batch03_cumulative_cards_and_audit.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(B3.rglob('*')):
        if p.is_file() and p.suffix!='.zip' and 'source_pdf_review' not in p.parts:
            z.write(p,str(p.relative_to(B3)))
manifest=[]
for p in sorted(B3.rglob('*')):
    if p.is_file() and p.name not in ['file_manifest.json','remote_download_validation.json']:
        manifest.append({'file':str(p.relative_to(B3)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
write_json(B3/'file_manifest.json',manifest)
print(json.dumps({'apkg':report,'quality':quality},ensure_ascii=False))
