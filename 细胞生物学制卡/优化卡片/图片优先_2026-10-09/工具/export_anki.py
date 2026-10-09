#!/usr/bin/env python3
"""Export the reviewed JSON to UTF-8 Anki text; never synthesize a GUID."""
import argparse, csv, json
from html import escape, unescape
from pathlib import Path
import re

HEADERS = '#separator:Tab\n#html:true\n#notetype:Basic\n#tags column:3\n#columns:Front\tBack\tTags\n'

def export(cards, destination, mode='optimized'):
    with Path(destination).open('w', encoding='utf-8', newline='') as f:
        f.write(HEADERS)
        w=csv.writer(f, delimiter='\t', lineterminator='\n')
        for c in cards:
            old=c.get('original_front')
            if mode=='update' and old is None: continue
            if mode=='new' and old is not None: continue
            front=c['front_html']
            back=c['back_html']
            if mode=='update':
                front=old
                if c['front']!=unescape(re.sub('<[^>]+>', '', old)).strip():
                    back='<b>题面修正提示</b><br>'+escape(c['front'])+'<br><br>'+back
            w.writerow([front,back,c['tags']])

def main():
    p=argparse.ArgumentParser()
    p.add_argument('cards_json',type=Path)
    p.add_argument('--output-dir',type=Path)
    a=p.parse_args(); out=a.output_dir or a.cards_json.parent
    out.mkdir(parents=True,exist_ok=True)
    cards=json.loads(a.cards_json.read_text(encoding='utf-8'))
    if any(c['note_type']!='Basic' for c in cards): raise ValueError('Only the reviewed Basic format is supported')
    for name,mode in [('SHU_Cell_Biology_Optimized_Basic.txt','optimized'),('SHU_Cell_Biology_2440_KeepFront_Update.txt','update'),('SHU_Cell_Biology_New_Image_Basic.txt','new')]:
        export(cards,out/name,mode)
    print(json.dumps({'Basic':len(cards),'Cloze':0,'new':sum(c.get('original_front') is None for c in cards)}))

if __name__=='__main__': main()
