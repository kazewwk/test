#!/usr/bin/env python3
"""在临时Anki集合中验证TXT导入、原卡匹配、进度保留和图片完整性。"""
from __future__ import annotations
import csv
import hashlib
import importlib.metadata
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile
from anki.collection import Collection
from anki.import_export_pb2 import CsvMetadata, ImportCsvRequest

REPO = Path(__file__).resolve().parents[1]
ANKI = REPO / 'anki'
BASELINE = 'fce68232f65f9ac6ae21bf526792c9e034eedb3e'
FILES = ['SHU_2027_Biochemistry_2514_Basic.txt', 'SHU_Molecular_Anki.txt']

def rows(raw):
    return list(csv.reader(io.StringIO('\n'.join(l for l in raw.splitlines() if not l.startswith('#'))), delimiter='\t'))

def run():
    status = json.loads((ANKI/'audit'/'status.json').read_text())
    assert status['reviewed_chapters'] == status['total_chapters'] == 47
    assert status['reviewed_auxiliary_folders'] == status['total_auxiliary_folders'] == 4
    assert status['reviewed_images'] == status['total_images']
    original, current = [], []
    for name in FILES:
        original += rows(subprocess.check_output(['git','show',f'{BASELINE}:anki/{name}'],cwd=REPO).decode())
        current += rows((ANKI/name).read_text())
    assert len(original)==3832
    assert len(current)==status['total_cards']
    assert len({r[0] for r in current})==len(current), '同一Basic类型跨文件重复题面'
    assert all(len(r)==4 and '<b>核心答案</b>' in r[1] and '<b>通过标准</b>' in r[1] for r in current)
    manifest = [json.loads(l) for l in (ANKI/'audit'/'media-manifest.jsonl').read_text().splitlines()]
    with zipfile.ZipFile(ANKI/'biology_anki_media.zip') as z:
        assert set(z.namelist())=={m['file'] for m in manifest}
        for m in manifest:
            assert hashlib.sha256(z.read(m['file'])).hexdigest()==m['sha256']
    with tempfile.TemporaryDirectory(prefix='bioanki-import-') as tmp:
        tmp=Path(tmp)
        col=Collection(str(tmp/'collection.anki2'))
        def do_import(path):
            meta=col.get_csv_metadata(str(path),None)
            assert meta.is_html and meta.tags_column==3 and meta.deck_column==4
            assert list(meta.global_notetype.field_columns)==[1,2]
            meta.dupe_resolution=CsvMetadata.UPDATE
            meta.match_scope=CsvMetadata.NOTETYPE
            col.import_csv(ImportCsvRequest(path=str(path),metadata=meta))
        for name in FILES:
            path=tmp/name
            path.write_bytes(subprocess.check_output(['git','show',f'{BASELINE}:anki/{name}'],cwd=REPO))
            do_import(path)
        assert col.note_count()==3832
        notes={col.get_note(nid).fields[0]:nid for nid in col.find_notes('')}
        original_card_ids={front: [c.id for c in col.get_note(nid).cards()] for front,nid in notes.items()}
        saved=[]
        # 模拟不同章节已有学习进度；更新导入不得重建卡或改变这些状态。
        for pos in [0,1000,2513,2600,3831]:
            card=col.get_note(notes[original[pos][0]]).cards()[0]
            card.type=2;card.queue=2;card.reps=7;card.lapses=1;card.ivl=18;card.due=30
            col.update_card(card)
            saved.append((card.id,card.nid,card.did,card.type,card.queue,card.reps,card.lapses,card.ivl,card.due))
        for m in manifest:shutil.copyfile(ANKI/'media'/m['file'],Path(col.media.dir())/m['file'])
        for name in FILES:do_import(ANKI/name)
        assert col.note_count()==status['total_cards'], '更新导入产生意外重复或遗漏'
        after={col.get_note(nid).fields[0]:nid for nid in col.find_notes('')}
        assert all(after[front]==nid for front,nid in notes.items()), '原笔记ID发生变化'
        assert all([c.id for c in col.get_note(after[front]).cards()]==ids for front,ids in original_card_ids.items()), '原卡片ID发生变化'
        for state in saved:
            card=col.get_card(state[0])
            assert state==(card.id,card.nid,card.did,card.type,card.queue,card.reps,card.lapses,card.ivl,card.due), '已有学习进度/牌组改变'
        for front,back,tags,deck in current:
            note=col.get_note(after[front])
            assert note.fields==[front,back], 'Anki导入后的HTML字段不一致'
            assert set(tags.split()).issubset(note.tags), '标签导入不完整'
            assert col.decks.name(note.cards()[0].did)==deck, '章节牌组不匹配'
        media_check=col.media.check()
        assert not media_check.missing, ('Anki检查发现缺图',list(media_check.missing))
        assert not media_check.unused, ('媒体包有未引用图片',list(media_check.unused))
        col.close()
    report={'anki_version':importlib.metadata.version('anki'),'original_notes':3832,'imported_notes':len(current),'stable_original_note_ids':3832,'stable_original_card_ids':3832,'progress_samples_preserved':len(saved),'four_column_mapping':'Front / Back / Tags / Deck','chapter_decks':47,'missing_media':0,'unused_media':0,'media_sha256_verified':len(manifest),'result':'passed'}
    (ANKI/'audit'/'anki-import-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
