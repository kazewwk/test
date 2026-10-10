from pathlib import Path
import json
from anki.collection import Collection
from anki.import_export_pb2 import ImportAnkiPackageRequest,ImportAnkiPackageOptions
R=Path('/tmp/biology_rebuild/batch02');O=R/'output';p=R/'anki_incremental_import';p.mkdir(exist_ok=True)
old=Path('/tmp/biology_rebuild/output/SHU_Cell_Biology_Rebuild_Batch01_20261010.apkg')
new=O/'SHU_Cell_Biology_Rebuild_Batch02_Cumulative_20261010.apkg'
def request(f):return ImportAnkiPackageRequest(package_path=str(f),options=ImportAnkiPackageOptions(merge_notetypes=True,with_scheduling=False,with_deck_configs=False))
col=Collection(str(p/'collection.anki2'))
try:
 assert col.db.scalar('select count(*) from notes')==0
 col.import_anki_package(request(old));assert col.db.scalar('select count(*) from notes')==107
 identities=col.db.all('select id,guid,tags from notes order by id')
 old_guids={guid for _,guid,_ in identities}
 sentinel_ids=[col.db.scalar('select min(id) from cards'),col.db.scalar('select max(id) from cards')]
 for i,cardid in enumerate(sentinel_ids):
  col.db.execute('update cards set type=2,queue=2,due=?,ivl=?,reps=?,lapses=? where id=?',1234+i,10+i,7+i,1+i,cardid)
 schedule={cid:col.db.first('select type,queue,due,ivl,reps,lapses from cards where id=?',cid) for cid in sentinel_ids}
 col.import_anki_package(request(new))
 assert col.db.scalar('select count(*) from notes')==218 and col.db.scalar('select count(*) from cards')==218
 assert old_guids<={row[0] for row in col.db.all('select guid from notes')}
 assert all(col.db.scalar('select guid from notes where id=?',nid)==guid for nid,guid,_ in identities)
 assert schedule=={cid:col.db.first('select type,queue,due,ivl,reps,lapses from cards where id=?',cid) for cid in sentinel_ids}
 cards=json.loads((O/'cards.json').read_text())['cards']
 for c in cards:
  assert col.db.scalar('select flds from notes where tags like ?','%卡片编号::'+c['id']+'%')==c['front_html']+'\x1f'+c['back_html']
 check=col.media.check();assert not check.missing and not check.unused
 report={'status':'PASS','old_notes':107,'cumulative_notes':218,'new_notes':111,'existing_note_ids_and_guids':'all 107 preserved','existing_review_sentinels':'PASS','all_fields_match_current_export':'PASS','missing_media':0,'unused_media':0,'physical_android_device':'not tested'}
finally:col.close()
(O/'incremental_import_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
