#!/usr/bin/env python3
"""Independent CPU OCR of original physical PDF pages; no automatic edits."""
from __future__ import annotations
import argparse, hashlib, importlib.metadata, json, time
from pathlib import Path

def run(a):
    import numpy as np
    import pymupdf
    from rapidocr_onnxruntime import RapidOCR
    books=json.loads(Path(a.plan).read_text())['books']
    b=next(x for x in books if x['id']==a.book)
    source=Path(a.source)/b['asset_name']
    with source.open('rb') as f:
        assert hashlib.file_digest(f,'sha256').hexdigest()==b['sha256']
    doc=pymupdf.open(source);assert len(doc)==b['pages']
    engine=RapidOCR(intra_op_num_threads=2,inter_op_num_threads=1,
                    det_limit_side_len=1600,det_limit_type='max')
    out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    for number in range(a.first,a.last+1):
        target=out/f'book-{a.book}-page-{number:04d}.json'
        if target.exists():continue
        start=time.monotonic();page=doc[number-1]
        pix=page.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False)
        array=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,3)[:,:,::-1].copy()
        lines,_=engine(array,use_cls=False)
        result={'book_id':a.book,'pdf_page':number,'source_sha256':b['sha256'],
            'engine':'RapidOCR ONNX PP-OCRv4','engine_version':importlib.metadata.version('rapidocr-onnxruntime'),
            'render_dpi':144,'det_limit_side_len':1600,'det_limit_type':'max',
            'render_pixels':[pix.width,pix.height],
            'native_text':page.get_text(sort=True),'lines':[]}
        for box,text,score in lines or []:
            result['lines'].append({'text':text,'confidence':round(float(score),6),
                'polygon':[[round(float(x)/pix.width,6),round(float(y)/pix.height,6)] for x,y in box]})
        result['elapsed_seconds']=round(time.monotonic()-start,3)
        temporary=target.with_suffix('.pending');temporary.write_text(json.dumps(result,ensure_ascii=False)+'\n');temporary.replace(target)
        print(f'book={a.book} page={number} lines={len(result["lines"])} seconds={result["elapsed_seconds"]}',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--plan',default=str(Path(__file__).with_name('politics_books_plan.json')))
    p.add_argument('--source',required=True);p.add_argument('--output',required=True)
    p.add_argument('--book',type=int,required=True);p.add_argument('--first',type=int,required=True);p.add_argument('--last',type=int,required=True)
    run(p.parse_args())
