#!/usr/bin/env python3
"""Build Basic APKG and true three-column UTF-8 TSV from complete authored JSONL.

Requires genanki; --native-check additionally requires anki. This validates
file identities, fields and media, not scholarly accuracy or semantic coverage.
Image entries have path, optional sha256 and optional caption. Existing series
must explicitly pass its identity namespace and model ID to retain identity.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
from pathlib import Path
import re
import tempfile
import zipfile


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def base91(number: int) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~'
    result = ''
    while number:
        number, rest = divmod(number, len(alphabet))
        result = alphabet[rest] + result
    return result


def identity(namespace: str, key: str) -> str:
    return base91(int.from_bytes(hashlib.sha256((namespace + key).encode()).digest()[:8], 'big'))


def escape(value: str) -> str:
    return html.escape(str(value), quote=True).replace('\r\n','\n').replace('\r','\n').replace('\n','<br>').replace('\t',' ')


def items(values: list[str]) -> str:
    return '<ol>' + ''.join('<li>'+escape(v)+'</li>' for v in values) + '</ol>'


def load_cards(path: Path) -> list[dict]:
    if path.suffix == '.jsonl':
        cards = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
    else:
        data = json.loads(path.read_text(encoding='utf-8'))
        cards = data if isinstance(data,list) else data['cards']
    assert cards and len({c['id'] for c in cards}) == len(cards), 'Empty input or duplicate card IDs'
    for c in cards:
        assert c.get('type','basic').lower() == 'basic', (c['id'],'Only Basic is enabled by default')
        assert c.get('front') and c.get('deck'), (c['id'],'Missing independent question or deck')
        assert c.get('answer') and all(isinstance(v,str) and v.strip() for v in c['answer']), (c['id'],'Empty full answer')
        assert c.get('criteria') and c.get('source') and c.get('support'), (c['id'],'Missing criteria or actual source/support')
        assert c.get('knowledge_ids'), (c['id'],'Missing mapped knowledge IDs')
        if c['support'] == '基于教材推导':
            assert c.get('premises'), (c['id'],'Derivation lacks premises')
    return cards


def render(c: dict, base: Path, media: dict) -> tuple[str,str,str]:
    def pictures(entries):
        fragments=[]
        for entry in entries:
            entry={'path':entry} if isinstance(entry,str) else entry
            path=Path(entry['path'])
            path=path if path.is_absolute() else base/path
            assert path.is_file(), (c['id'],'Missing real media',str(path))
            filehash=digest(path.read_bytes())
            assert not entry.get('sha256') or entry['sha256']==filehash, (c['id'],'Media hash mismatch')
            # Root resolves uniquely named source copies; conflicting basenames are errors.
            name=path.name
            assert name not in media or media[name]['sha256']==filehash, ('Conflicting media filename',name)
            media[name]={'path':str(path.resolve()),'file':name,'sha256':filehash,'bytes':path.stat().st_size}
            fragments.append('<div class="figure"><img src="'+escape(name)+'">'+
                             ('<div class="caption">'+escape(entry['caption'])+'</div>' if entry.get('caption') else '')+'</div>')
        return ''.join(fragments)
    front=escape(c['front'])+pictures(c.get('front_images',[]))
    back='<div class="full-answer"><b>完整答案</b>'+items(c['answer'])+'</div>'
    back+='<div class="criteria"><b>必答点</b>'+items(c['criteria'])+'</div>'
    if c.get('premises'):
        back+='<div><b>推导前提</b>'+items(c['premises'])+'</div>'
    connections=c.get('connections',[])
    connections=[connections] if isinstance(connections,str) else list(connections)
    if c.get('pitfall'): connections.append(c['pitfall'])
    if connections: back+='<div><b>理解与联系</b>'+items(connections)+'</div>'
    if c.get('terms'):
        values=[]
        for term in c['terms']:
            assert term.get('zh') and term.get('en'), (c['id'],'Incomplete bilingual term')
            values.append((term['abbr']+'：' if term.get('abbr') else '')+term['zh']+'（'+term['en']+'）')
        back+='<div class="terms"><b>术语</b>'+items(values)+'</div>'
    back+=pictures(c.get('back_images',[]))
    if c.get('figure_note'): back+='<div class="caption">'+escape(c['figure_note'])+'</div>'
    sources=c.get('sources') or [c['source']]
    sources=[s if isinstance(s,str) else json.dumps(s,ensure_ascii=False) for s in sources]
    back+='<details class="source"><summary>依据与来源</summary>'+escape(c['support'])+items(sources)+'</details>'
    back+='<div class="ids">卡片ID：'+escape(c['id'])+'<br>知识点ID：'+escape('、'.join(c['knowledge_ids']))+'</div>'
    tags=c.get('tags',[])
    tags=tags.split() if isinstance(tags,str) else list(tags)
    assert len(tags)>=3 and all(t and not re.search(r'\s',t) for t in tags), (c['id'],'Need at least 3 whitespace-free tags')
    tags=list(dict.fromkeys(tags+['卡ID::'+c['id']]))
    return front,back,' '.join(tags)


def native_check(package: Path, expected: dict, media: dict, model_id: int) -> dict:
    from anki.collection import Collection
    from anki.import_export_pb2 import ImportAnkiPackageRequest, ImportAnkiPackageOptions
    with tempfile.TemporaryDirectory(prefix='biology-native-check-') as tmp:
        col=Collection(str(Path(tmp)/'collection.anki2'))
        try:
            request=ImportAnkiPackageRequest(package_path=str(package.resolve()),options=ImportAnkiPackageOptions(
                merge_notetypes=True,with_scheduling=False,with_deck_configs=False))
            col.import_anki_package(request)
            assert col.note_count()==col.card_count()==len(expected)
            before={}
            for nid in col.find_notes(''):
                note=col.get_note(nid)
                front,back,tags,deck=expected[note.guid]
                assert note.fields==[front,back] and note.mid==model_id
                assert set(tags.split()).issubset(note.tags)
                cards=note.cards()
                assert len(cards)==1 and col.decks.name(cards[0].did)==deck
                before[note.guid]=(nid,cards[0].id)
            result=col.media.check()
            assert not result.missing and not result.unused
            for filename,entry in media.items():
                assert digest((Path(col.media.dir())/filename).read_bytes())==entry['sha256']
            col.import_anki_package(request)
            assert col.note_count()==col.card_count()==len(expected)
            for guid,(nid,cid) in before.items():
                note=col.get_note(nid)
                assert note.guid==guid and note.cards()[0].id==cid
        finally:
            col.close()
    return {'native_backend_import':'passed','repeat_import_duplicates':0,'missing_media':0,'unused_media':0,
            'scope':'Native Anki backend; no physical Android device test.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--identity-prefix',default='make-biology-anki/notes/')
    parser.add_argument('--deck-prefix',default='make-biology-anki/decks/')
    parser.add_argument('--model-id',type=int,default=1937429001)
    parser.add_argument('--model-name',default='生物考研（完整问答）')
    parser.add_argument('--native-check',action='store_true')
    args=parser.parse_args()
    import genanki
    cards=load_cards(args.input)
    media={}; rows=[]; expected={}
    for c in cards:
        row=render(c,args.input.resolve().parent,media)
        guid=identity(args.identity_prefix,c['id'])
        assert guid not in expected, 'GUID collision'
        expected[guid]=(*row,c['deck'])
        rows.append(row)
    model=genanki.Model(args.model_id,args.model_name,fields=[{'name':'Front'},{'name':'Back'}],
        templates=[{'name':'问答','qfmt':'{{Front}}','afmt':'{{FrontSide}}<hr id="answer">{{Back}}'}],
        css='.card {font-family:Arial,sans-serif;font-size:20px;text-align:left;line-height:1.6;overflow-wrap:anywhere;} img {max-width:100%;height:auto;} li {margin:.4em 0;} .criteria {margin:1em 0;} .caption,.ids,.source {font-size:.8em;} .figure {margin:1em 0;}')
    decks={}
    for name in sorted({c['deck'] for c in cards}):
        number=1000000000+int.from_bytes(hashlib.sha256((args.deck_prefix+name).encode()).digest()[:4],'big')%1000000000
        assert number not in [d.deck_id for d in decks.values()], 'Deck ID collision'
        decks[name]=genanki.Deck(number,name)
    for guid,(front,back,tags,deck) in expected.items():
        decks[deck].add_note(genanki.Note(model=model,fields=[front,back],tags=tags.split(),guid=guid))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    package=genanki.Package(list(decks.values()))
    package.media_files=[e['path'] for e in media.values()]
    with tempfile.TemporaryDirectory(prefix='biology-apkg-build-') as tmp:
        intermediate=Path(tmp)/'build.apkg'
        package.write_to_file(str(intermediate))
        with zipfile.ZipFile(intermediate) as zin,zipfile.ZipFile(args.output,'w',compression=zipfile.ZIP_DEFLATED) as zout:
            for filename in zin.namelist(): zout.writestr(filename,zin.read(filename))
    with zipfile.ZipFile(args.output) as archive:
        assert 'collection.anki2' in archive.namelist()
        mapping=json.loads(archive.read('media'))
        assert set(mapping.values())==set(media)
        for key,name in mapping.items(): assert digest(archive.read(key))==media[name]['sha256']
    tsv=args.output.with_suffix('.tsv')
    with tsv.open('w',encoding='utf-8',newline='') as file:
        writer=csv.writer(file,delimiter='\t',lineterminator='\n',quoting=csv.QUOTE_NONE,quotechar=None,escapechar=None)
        writer.writerows(rows)
    with tsv.open(encoding='utf-8',newline='') as file:
        parsed=list(csv.reader(file,delimiter='\t',quoting=csv.QUOTE_NONE,quotechar=None))
    assert parsed==[list(r) for r in rows] and all(len(r)==3 and all(r) for r in parsed)
    report={'notes':len(cards),'cards':len(cards),'decks':len(decks),'media':len(media),
            'all_media_hashes_verified':True,'tsv_rows_read_back':len(parsed),'tsv_fields':3,
            'bytes':args.output.stat().st_size,'sha256':digest(args.output.read_bytes()),
            'identity_prefix':args.identity_prefix,'model_id':args.model_id,
            'semantic_coverage':'Not checked by this builder; requires authored coverage ledger and content review.'}
    if args.native_check: report.update(native_check(args.output,expected,media,args.model_id))
    args.output.with_suffix('.check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))


if __name__=='__main__': main()
