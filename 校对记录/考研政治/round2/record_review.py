import json,pathlib,argparse,datetime
r=pathlib.Path('/workspace/politics-books/round2');a=json.loads((r/'items.json').read_text());p=argparse.ArgumentParser();p.add_argument('sheets',nargs='+');p.add_argument('--defer',default='');p.add_argument('--correction',default='');p.add_argument('--layout',default='');p.add_argument('--notes',default='')
x=p.parse_args()
def ids(s):return {int(v) for v in s.split(',') if v}
defer=ids(x.defer);correction=ids(x.correction);layout=ids(x.layout);f=r/'decisions.json';d=json.loads(f.read_text()) if f.exists() else {};groups=json.loads((r/'compact-sheets.json').read_text()) if (r/'compact-sheets.json').exists() else {}
selected=set()
for sheet in x.sheets:
 if sheet in groups:selected.update(groups[sheet])
 else:selected.update(z['id'] for z in a if z['evidence_sheet'].split('/')[-1]==sheet)
assert selected and defer|correction|layout<=selected
for i in selected:
 z=a[i];status='needs_source_revisit' if i in defer or z['type']=='unmatched_line' and i not in correction else 'source_confirmed_correction_needed' if i in correction else 'reference_layout_mismatch' if i in layout else ('reference_omission' if not z['reference'] else 'reference_ocr_error')
 d[str(i)]={'id':i,'book':z['book'],'pdf_page':z['page'],'block_index':z['block'],'decision':status,'evidence':z['evidence_sheet'],'source_sha256':z['source_sha256'],'scope':'displayed difference region; does not certify unshown characters','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'notes':x.notes or '已对照所保存的原页差异截图逐项查看。'}
f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print('Recorded',len(selected),'total',len(d),'pending revisits',sum(v['decision']=='needs_source_revisit' for v in d.values()),'confirmed correction candidates',sum(v['decision']=='source_confirmed_correction_needed' for v in d.values()))
