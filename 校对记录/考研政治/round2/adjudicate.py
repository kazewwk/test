import json,pathlib,argparse,datetime
P=pathlib.Path('/workspace/politics-books/round2');p=argparse.ArgumentParser();p.add_argument('sheets',nargs='*');p.add_argument('--keep',default='');p.add_argument('--correct',default='');p.add_argument('--image',default='');p.add_argument('--layout',default='');p.add_argument('--defer',default='');p.add_argument('--note',default='');x=p.parse_args();a=json.loads((P/'items.json').read_text());d=json.loads((P/'decisions.json').read_text());maps=json.loads((P/'revisit-sheets.json').read_text());parse=lambda s:{int(i) for i in s.split(',') if i};keep,correct,img,layout,defer=map(parse,(x.keep,x.correct,x.image,x.layout,x.defer)); selected=set().union(*(set(maps[s]) for s in x.sheets)) if x.sheets else set();selected|=keep|correct|img|layout|defer
for i in selected:
 z=a[i];old=d[str(i)];status=old['decision']
 if i in correct:status='source_confirmed_correction_needed'
 elif i in img:status='source_graphic_replacement_needed'
 elif i in layout:status='reference_layout_mismatch'
 elif i in defer:status='needs_source_revisit'
 elif i in keep or status=='needs_source_revisit' and z['type']!='unmatched_line':status='reference_omission' if not z['reference'] else 'reference_ocr_error'
 evidence=next(('evidence/revisit/'+s for s in x.sheets if i in maps[s]),old['evidence']);d[str(i)]={**old,'decision':status,'evidence':evidence,'notes':x.note or '放大原页对应完整文字块核对；按实际字形裁定。','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(P/'decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');from collections import Counter; print(dict(Counter(v['decision'] for v in d.values())))
