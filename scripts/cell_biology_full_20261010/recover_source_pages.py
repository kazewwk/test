from pathlib import Path
import hashlib, json, re, subprocess, sys
import fitz
ROOT = Path('anki/SHU_Cell_Biology_Full_20261010')
REQ = json.loads((ROOT/'source_review_requests.json').read_text(encoding='utf-8'))
OUT = ROOT/'source_review'
OUT.mkdir(parents=True, exist_ok=True)
SNAPSHOT = REQ['source_commit']
def git_bytes(path):
    return subprocess.check_output(['git','show',SNAPSHOT+':'+path])
def verify_and_restore_cn():
    folder = '细胞生物学制卡/来源/中文教材/原书PDF分片/'
    manifest = json.loads(git_bytes(folder+'分片清单.json'))
    pieces = []
    for item in manifest['parts']:
        raw = git_bytes(folder+item['file'])
        assert len(raw)==item['bytes']
        assert hashlib.sha256(raw).hexdigest()==item['sha256']
        pieces.append(raw)
    raw = b''.join(pieces)
    assert len(raw)==manifest['bytes']
    assert hashlib.sha256(raw).hexdigest()==manifest['sha256']
    return raw, manifest['sha256']
report = {'source_commit':SNAPSHOT,'method':'Original PDF page rasterization with PyMuPDF; no generative replacement; text extraction is only an aid, pages still require actual human/model viewing.','books':[]}
for req in REQ['books']:
    key = req['key']
    if key=='CN':
        raw, digest = verify_and_restore_cn()
        original = '细胞生物学制卡/来源/中文教材/原书PDF分片/分片清单.json'
    else:
        original = req['pdf_path']
        raw = git_bytes(original)
        digest = hashlib.sha256(raw).hexdigest()
    doc = fitz.open(stream=raw,filetype='pdf')
    texts = [p.get_text(sort=True) for p in doc]
    (OUT/(key+'_page_text.json')).write_text(json.dumps([{'pdf_sequence':i+1,'text':t} for i,t in enumerate(texts)],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    matched = []
    for term in req.get('search_terms',[]):
        hits = [i+1 for i,t in enumerate(texts) if term.lower() in t.lower()]
        matched.append({'term':term,'pdf_sequences':hits})
    pages = set(req.get('pages',[]))
    for match in matched:
        for n in match['pdf_sequences']:
            pages.update(range(max(1,n-req.get('context',0)),min(len(doc),n+req.get('context',0))+1))
    entries = []
    for n in sorted(pages):
        assert 1<=n<=len(doc),(key,n,len(doc))
        page = doc[n-1]
        scale = (2600 if key=='CN' else 2000)/max(page.rect.width,page.rect.height)
        pix = page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
        filename = f'{key}_PDFseq_{n:04d}.jpg'
        data = pix.tobytes('jpeg',jpg_quality=87)
        (OUT/filename).write_bytes(data)
        entries.append({'pdf_sequence':n,'file':filename,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'page_label':page.get_label(),'actual_viewed':False,'embedded_raster_dimensions':[[im[2],im[3]] for im in page.get_images(full=True)]})
    report['books'].append({'key':key,'original_path':original,'original_pdf_sha256':digest,'page_count':len(doc),'page_labels':doc.get_page_labels(),'search_matches':matched,'rendered_pages':entries})
    print(key,'pages',len(doc),'text_chars',sum(map(len,texts)),'renders',len(entries))
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
