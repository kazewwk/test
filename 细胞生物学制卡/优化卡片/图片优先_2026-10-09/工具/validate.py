#!/usr/bin/env python3
"""Independent read-back, identity, HTML/media and coverage checks."""
import argparse, csv, hashlib, json, re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

class FieldParser(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.images=[];self.urls=[];self.text=[];self.stack=[]
    def handle_data(self,d):self.text.append(d)
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='img':self.images.append(d.get('src',''))
        if tag=='a':self.urls.append(d.get('href',''))
        if tag not in {'br','img','hr','input','meta','link'}:self.stack.append(tag)
    def handle_endtag(self,tag):
        if not self.stack or self.stack.pop()!=tag:raise ValueError(f'Unbalanced HTML: {tag}')

def rows(path):
    text=path.read_text(encoding='utf-8')
    assert '\\t' not in text, f'Literal tab escape in {path.name}'
    headers=text.splitlines()[:5]
    assert headers==['#separator:Tab','#html:true','#notetype:Basic','#tags column:3','#columns:Front\tBack\tTags']
    result=list(csv.reader(text.splitlines()[5:],delimiter='\t'))
    assert all(len(r)==3 for r in result),f'Wrong field count in {path.name}'
    return result

def validate(root,source_root=None):
    cards=json.loads((root/'cards.json').read_text(encoding='utf-8'))
    stats=json.loads((root/'统计.json').read_text(encoding='utf-8'))
    images=json.loads((root/'图片核对记录.json').read_text(encoding='utf-8'))
    new=[c for c in cards if c.get('original_front') is None]
    old=[c for c in cards if c.get('original_front') is not None]
    assert len(cards)==stats['final_cards']==2454
    assert len(old)==2440 and len(new)==14
    assert len({c['id'] for c in cards})==len(cards)
    assert all(c['note_type']=='Basic' and c['core'] for c in cards)
    variants=[('SHU_Cell_Biology_Optimized_Basic.txt',cards),('SHU_Cell_Biology_2440_KeepFront_Update.txt',old),('SHU_Cell_Biology_New_Image_Basic.txt',new)]
    used=set();source_checks=0
    for name,expected in variants:
        data=rows(root/name)
        assert len(data)==len(expected)
        assert len({r[0] for r in data})==len(data),f'Duplicate first field in {name}'
        for row,c in zip(data,expected):
            front,back,tags=row
            assert tags==c['tags'] and f'卡片编号::{c["id"]}' in tags
            if 'KeepFront' in name:assert front==c['original_front'],f'Changed identity field: {c["id"]}'
            else:assert front==c['front_html'] and back==c['back_html']
            assert not any(s in back for s in ['未逐图核对','520512d02afe82472','待补图','TODO'])
            for field in [front,back]:
                p=FieldParser();p.feed(field);p.close();assert not p.stack
                for src in p.images:
                    assert re.fullmatch(r'CB5_(CN|EN)\d{4}\.jpg',src)
                    assert (root/'collection.media'/src).is_file(),f'Missing media: {src}'
                    used.add(src)
                assert all(u.startswith('https://github.com/kazewwk/test/blob/'+stats['pin']+'/') for u in p.urls)
    included=[x for x in images if x['review_status']=='reviewed_incorporated']
    assert len(images)==3115 and len(included)==453
    assert Counter(x['review_status'] for x in images if x['language']=='CN')=={'reviewed_incorporated':441,'reviewed_excluded':22}
    assert Counter(x['review_status'] for x in images if x['language']=='EN')=={'reviewed_incorporated':12,'not_reviewed':2640}
    media={p.name for p in (root/'collection.media').iterdir()}
    assert used==media=={x['media_name'] for x in included}
    byid={c['id']:c for c in cards}
    for im in included:
        assert im['review_note'] and len(im['card_ids'])==1
        c=byid[im['card_ids'][0]];assert im['id'] in c['image_ids']
        if source_root:
            assert (source_root/im['document']).is_file()
            a=(source_root/im['path']).read_bytes();b=(root/'collection.media'/im['media_name']).read_bytes()
            assert a==b,f'Media altered: {im["id"]}'
            source_checks+=1
    for c in cards:
        assert set(c['front_image_ids'])<=set(c['image_ids'])
        assert c['sources'] and c['scoring']
        if source_root:
            for s in c['sources']:
                p=source_root/s['path'];lines=p.read_text(encoding='utf-8').splitlines()
                assert lines[s['line']-1].lstrip('# ')==s['heading']
                source_checks+=1
    depth=dict(Counter(re.search(r'深度::(L\d)',c['tags']).group(1) for c in cards))
    assert depth==stats['depth']
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/'collection.media').iterdir()}
    (root/'媒体校验.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    report={'status':'passed','Basic':len(cards),'Cloze':0,'cloze_ratio':0,'update_first_fields_preserved':len(old),'new_cards':len(new),'media_files':len(media),'missing_media':0,'CN_images_reviewed':463,'EN_images_reviewed':12,'EN_images_unreviewed':2640,'source_and_original_media_checks':source_checks,'depth':depth,'anki_application_import_executed':False,'skill_bundled_exporter_executed':False,'exporter':'本包可回读验证的export_anki.py；skill附件脚本不可读取'}
    (root/'校验报告.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('output_dir',type=Path);p.add_argument('--source-root',type=Path);a=p.parse_args()
    validate(a.output_dir,a.source_root)
