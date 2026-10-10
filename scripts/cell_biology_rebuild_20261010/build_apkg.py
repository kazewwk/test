from pathlib import Path
import json,hashlib,zipfile,shutil,re
from anki.collection import Collection
from anki.import_export_pb2 import ExportAnkiPackageOptions,ExportLimit,ImportAnkiPackageRequest,ImportAnkiPackageOptions
R=Path('/tmp/biology_rebuild');O=R/'output';cs=json.loads((O/'cards.json').read_text())['cards'];name='SHU_Cell_Biology_Rebuild_Batch01_20261010.apkg';p=R/'anki_build';p.mkdir(exist_ok=True)
col=Collection(str(p/'collection.anki2'))
try:
 model=col.models.by_name('细胞生物学完整问答·20261010')
 if model is None:
  model=col.models.new('细胞生物学完整问答·20261010')
  for f in ('Front','Back'):col.models.add_field(model,col.models.new_field(f))
  t=col.models.new_template('普通问答');t['qfmt']='{{Front}}';t['afmt']='{{FrontSide}}<hr id="answer">{{Back}}';col.models.add_template(model,t);model['css']=(O/'card.css').read_text();col.models.add(model)
 did=col.decks.id('SHU细胞生物学·完整问答重制20261010::第01章_绪论')
 existing={str(n[1]):n[0] for n in col.db.all('select id,tags from notes')}
 for c in cs:
  match=col.db.scalar('select id from notes where tags like ?','%卡片编号::'+c['id']+'%')
  note=col.get_note(match) if match else col.new_note(model);note['Front']=c['front_html'];note['Back']=c['back_html'];note.tags=c['tags']
  if match:col.update_note(note)
  else:col.add_note(note,did)
 for f in (O/'collection.media').iterdir():shutil.copyfile(f,Path(col.media.dir())/f.name)
 check=col.media.check();assert not check.missing and not check.unused,(check.missing,check.unused)
 assert col.db.scalar('select count(*) from notes')==len(cs) and col.db.scalar('select count(*) from cards')==len(cs)
 assert all(m['type']==0 for m in col.models.all() if col.models.use_count(m))
 limit=ExportLimit();limit.whole_collection.SetInParent()
 assert col.export_anki_package(out_path=str(O/name),options=ExportAnkiPackageOptions(with_media=True,with_scheduling=False,with_deck_configs=False,legacy=True),limit=limit)==len(cs)
finally:col.close()
with zipfile.ZipFile(O/name) as z:
 assert z.testzip() is None;assert 'collection.anki2' in z.namelist();media=json.loads(z.read('media'));assert set(media.values())=={f.name for f in (O/'collection.media').iterdir()}
 for number,filename in media.items():assert hashlib.sha256(z.read(number)).digest()==hashlib.sha256((O/'collection.media'/filename).read_bytes()).digest()
p=R/'anki_fresh_import';p.mkdir(exist_ok=True);col=Collection(str(p/'collection.anki2'))
try:
 request=ImportAnkiPackageRequest(package_path=str(O/name),options=ImportAnkiPackageOptions(merge_notetypes=True,with_scheduling=False,with_deck_configs=False));col.import_anki_package(request)
 assert col.db.scalar('select count(*) from notes')==len(cs) and col.db.scalar('select count(*) from cards')==len(cs)
 assert not any('图册' in d['name'] for d in col.decks.all())
 check=col.media.check();assert not check.missing and not check.unused
 identities=col.db.all('select id,guid from notes order by id');sentinel=col.db.scalar('select min(id) from cards');col.db.execute('update cards set type=2,queue=2,due=1234,ivl=10,reps=7,lapses=1 where id=?',sentinel)
 scheduling=col.db.all('select id,type,queue,due,ivl,reps,lapses from cards order by id');col.import_anki_package(request)
 assert col.db.all('select id,guid from notes order by id')==identities;assert col.db.all('select id,type,queue,due,ivl,reps,lapses from cards order by id')==scheduling
 for c in cs:
  raw=col.db.scalar('select flds from notes where tags like ?','%卡片编号::'+c['id']+'%');assert raw==c['front_html']+'\x1f'+c['back_html']
 report={'status':'PASS','package':name,'notes':len(cs),'cards':len(cs),'basic':len(cs),'cloze':0,'cards_with_images':sum(bool(c['images']) for c in cs),'embedded_media':len(media),'image_gallery_decks':0,'fresh_native_import':'PASS','repeat_native_import':'PASS','repeat_keeps_review_sentinel':'PASS','stored_fields_equal_export':'PASS','missing_media':0,'unused_media':0,'archive_media_hashes':'PASS','format':'legacy APKG / collection.anki2 / built with native Anki backend','physical_android_device':'not tested','sha256':hashlib.sha256((O/name).read_bytes()).hexdigest(),'bytes':(O/name).stat().st_size}
finally:col.close()
(O/'apkg_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
