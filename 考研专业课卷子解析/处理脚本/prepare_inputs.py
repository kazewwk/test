"""Prepare lossless, per-exam PDF inputs. Does not run OCR or modify originals."""
from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    import pymupdf
    inventory=json.loads((ROOT/'inventory.json').read_text())
    out=ROOT/'inputs';out.mkdir(exist_ok=True)
    rows=[];pending=[]
    for r in inventory['papers']:
        kind=r['recommended_input']['kind'];fs=r['recommended_input']['files']
        for f in fs:
            p=Path(f['path']);assert p.is_file(),p
            assert sha(p)==f['sha256'],('source hash mismatch',r['id'],p)
        dest=out/(r['id']+'.pdf')
        if kind=='doc_compilation_subject_extract_pdf':
            # Owned by prepare_ihb_inputs.py; it must truly remove adjacent-subject content.
            if not dest.exists():pending.append(r['id']);continue
            method='existing_converted_pdf_subject_boundary_redaction'
        elif kind=='original_images':
            if not dest.exists():
                result=pymupdf.open()
                for f in fs:
                    pix=pymupdf.Pixmap(f['path'])
                    # Pixel-matched page at 72 dpi; embeds original PNG without resampling.
                    page=result.new_page(width=pix.width,height=pix.height)
                    page.insert_image(page.rect,filename=f['path'])
                result.save(dest,garbage=4,deflate=True);result.close()
            method='original_images_lossless_pdf_wrapper'
        else:
            assert len(fs)==1 and Path(fs[0]['path']).suffix.lower()=='.pdf'
            if not dest.exists():shutil.copy2(fs[0]['path'],dest)
            assert sha(dest)==fs[0]['sha256'],('copied PDF changed',r['id'])
            method='original_pdf_byte_copy' if kind=='original_pdf' else 'existing_doc_conversion_byte_copy'
        with pymupdf.open(dest) as pdf:
            pages=len(pdf);assert pages>0
            expected=r['recommended_input'].get('pdf_physical_pages') or len(fs)
            assert pages==expected,(r['id'],pages,expected)
        rows.append(dict(id=r['id'],title=r['title'],subject_group=r['subject_group'],input_file=str(dest.relative_to(ROOT)),input_sha256=sha(dest),pages=pages,input_method=method,upload_relative_dir=r['upload_relative_dir'],original_files=r['original_files'],warnings=r['warnings']))
    (ROOT/'prepared_inputs.json').write_text(json.dumps(dict(papers=rows,pending_compilation_crops=pending,prepared=len(rows),total_pages=sum(r['pages'] for r in rows)),ensure_ascii=False,indent=2))
    print(json.dumps(dict(prepared=len(rows),pending=pending,total_pages=sum(r['pages'] for r in rows)),ensure_ascii=False))
if __name__=='__main__':main()
