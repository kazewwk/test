#!/usr/bin/env python3
"""生成包含全部原图的传统 APKG，并实际导入验证安卓单文件交付。"""
from __future__ import annotations

import csv
import hashlib
import importlib.metadata
import io
import json
from pathlib import Path
import tempfile
import zipfile

import genanki
from anki.collection import Collection
from anki.import_export_pb2 import (
    ImportAnkiPackageOptions,
    ImportAnkiPackageRequest,
)
from anki.utils import base91

from optimize_biology_anki import original_cards

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'anki'
FILES = ['SHU_2027_Biochemistry_2514_Basic.txt', 'SHU_Molecular_Anki.txt']
PACKAGE = 'SHU_Biology_AnkiDroid.apkg'
MODEL_ID = 1833920001
MODEL_NAME = '生化与分子（原图问答）'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def card_state(card):
    return (card.id, card.nid, card.did, card.type, card.queue,
            card.reps, card.lapses, card.ivl, card.due)


def run():
    status = json.loads((ROOT / 'audit/status.json').read_text())
    old_check = json.loads((ROOT / 'audit/anki-import-check.json').read_text())
    assert status['reviewed_chapters'] == 47
    assert status['reviewed_images'] == status['total_images'] == 6615
    assert old_check['result'] == 'passed'
    assert old_check['imported_notes'] == status['total_cards']
    manifest = [json.loads(line) for line in
                (ROOT / 'audit/media-manifest.jsonl').read_text().splitlines()]
    fronts = {c['front']: c['id'] for c in original_cards(REPO)}
    rows = []
    for filename in FILES:
        raw = (ROOT / filename).read_text()
        rows.extend(csv.reader(io.StringIO('\n'.join(
            line for line in raw.splitlines() if not line.startswith('#'))),
            delimiter='\t'))
    assert len(rows) == status['total_cards']
    assert all(len(row) == 4 for row in rows)
    assert len({row[0] for row in rows}) == len(rows)
    expected = {}
    for front, back, tags, deck in rows:
        tagged = [tag.split('::', 1)[1] for tag in tags.split()
                  if tag.startswith('卡ID::')]
        card_id = tagged[0] if tagged else fronts[front]
        # 与既有随机 GUID 的 TXT 笔记不同；本 APKG 系列今后可稳定识别自身笔记。
        digest = hashlib.sha256(('kazewwk/test/biology-anki/' + card_id).encode()).digest()
        guid = base91(int.from_bytes(digest[:8], 'big'))
        assert guid not in expected, ('重复 GUID', card_id)
        expected[guid] = (front, back, tags, deck)

    target = ROOT / PACKAGE
    model = genanki.Model(
        MODEL_ID, MODEL_NAME,
        fields=[{'name': 'Front'}, {'name': 'Back'}],
        templates=[{'name': '问答', 'qfmt': '{{Front}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Back}}'}],
        css=('.card {font-family:Arial,sans-serif;font-size:20px;'
             'text-align:left;line-height:1.55;overflow-wrap:anywhere;}'
             'img {max-width:100%;height:auto;}'
             'summary {cursor:pointer;} hr {margin:1.2em 0;}'))
    decks = {}
    for name in sorted({row[3] for row in rows}):
        digest = hashlib.sha256(('kazewwk/test/biology-deck/' + name).encode()).digest()
        deck_id = 1000000000 + int.from_bytes(digest[:4], 'big') % 1000000000
        decks[name] = genanki.Deck(deck_id, name)
    assert len({deck.deck_id for deck in decks.values()}) == len(decks)
    for guid, (front, back, tags, deck) in expected.items():
        decks[deck].add_note(genanki.Note(
            model=model, fields=[front, back], tags=tags.split(), guid=guid))
    media_paths = []
    for entry in manifest:
        source = ROOT / 'media' / entry['file']
        assert sha(source.read_bytes()) == entry['sha256']
        media_paths.append(str(source))
    package = genanki.Package(list(decks.values()))
    package.media_files = media_paths
    with tempfile.TemporaryDirectory(prefix='biology-apkg-build-') as temp:
        intermediate = Path(temp) / PACKAGE
        package.write_to_file(str(intermediate))
        # 只压缩容器，所有卡片和原图字节保持原样。
        with zipfile.ZipFile(intermediate) as source_archive, zipfile.ZipFile(target, 'w') as output_archive:
            for name in source_archive.namelist():
                info = zipfile.ZipInfo(name, date_time=(2026, 10, 9, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                output_archive.writestr(info, source_archive.read(name))

    with zipfile.ZipFile(target) as archive:
        assert 'collection.anki2' in archive.namelist(), '必须为兼容的传统 APKG'
        media_map = json.loads(archive.read('media'))
        assert set(media_map.values()) == {m['file'] for m in manifest}
        hashes = {m['file']: m['sha256'] for m in manifest}
        for key, filename in media_map.items():
            assert sha(archive.read(key)) == hashes[filename]

    # 原生 Anki 导入整个 APKG，而非只检查其 ZIP 结构。
    with tempfile.TemporaryDirectory(prefix='biology-apkg-import-') as temp:
        col = Collection(str(Path(temp) / 'collection.anki2'))
        try:
            request = ImportAnkiPackageRequest(
                package_path=str(target),
                options=ImportAnkiPackageOptions(
                    merge_notetypes=True, with_scheduling=False,
                    with_deck_configs=False))
            col.import_anki_package(request)
            assert col.note_count() == len(rows) == col.card_count()
            assert len({row[3] for row in rows}) == 47
            imported = {}
            for nid in col.find_notes(''):
                note = col.get_note(nid)
                assert note.guid in expected
                front, back, tags, deck = expected[note.guid]
                assert note.fields == [front, back]
                assert set(tags.split()).issubset(note.tags)
                assert note.note_type()['name'] == MODEL_NAME
                card = note.cards()[0]
                assert col.decks.name(card.did) == deck
                assert card.type == card.queue == card.reps == card.lapses == 0
                imported[note.guid] = (nid, card.id)
            media_check = col.media.check()
            assert not media_check.missing and not media_check.unused
            for entry in manifest:
                assert sha((Path(col.media.dir()) / entry['file']).read_bytes()) == entry['sha256']

            samples = []
            for guid in list(imported)[::800][:5]:
                card = col.get_card(imported[guid][1])
                card.type = card.queue = 2
                card.reps = 7
                card.lapses = 1
                card.ivl = 18
                card.due = 30
                col.update_card(card)
                samples.append(card_state(card))
            col.import_anki_package(request)
            assert col.note_count() == len(rows) == col.card_count()
            for guid, (nid, cid) in imported.items():
                note = col.get_note(nid)
                assert note.guid == guid and note.cards()[0].id == cid
            for state in samples:
                assert card_state(col.get_card(state[0])) == state
        finally:
            col.close()

    assert target.stat().st_size < 100 * 1024 * 1024
    report = {
        'result': 'passed', 'anki_version': importlib.metadata.version('anki'),
        'genanki_version': importlib.metadata.version('genanki'),
        'file': PACKAGE, 'format': 'legacy APKG (collection.anki2 + embedded media)',
        'notes': len(rows), 'cards': len(rows), 'chapter_decks': 47,
        'biochemistry_cards': sum(n for ch, n in status['chapter_cards'].items() if ch.startswith('B')),
        'molecular_cards': sum(n for ch, n in status['chapter_cards'].items() if ch.startswith('M')),
        'embedded_media': len(manifest), 'missing_media': 0, 'unused_media': 0,
        'all_fields_tags_decks_verified': True,
        'second_import_duplicates': 0, 'same_apkg_progress_samples_preserved': len(samples),
        'identity': 'Stable model ID and note GUIDs for this APKG series; cannot match earlier TXT imports by front text.',
        'test_scope': 'Native Anki backend round-trip; no physical Android device test.',
        'bytes': target.stat().st_size, 'sha256': sha(target.read_bytes()),
        'source_txt_sha256': {filename: sha((ROOT / filename).read_bytes()) for filename in FILES},
    }
    (ROOT / 'audit/ankidroid-apkg-check.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    artifact_path = ROOT / 'audit/artifact-manifest.json'
    artifacts = json.loads(artifact_path.read_text())
    artifacts = [a for a in artifacts if a['file'] != PACKAGE]
    artifacts.append({key: report[key] for key in ['file', 'bytes', 'sha256']})
    artifact_path.write_text(json.dumps(artifacts, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run()
