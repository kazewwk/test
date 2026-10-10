from pathlib import Path
import hashlib,json,requests,fitz,time
R=Path('anki/SHU_Cell_Biology_Rebuild_20261010/Batch03/source_pdf_review')
R.mkdir(parents=True,exist_ok=True)
url='https://www.cancertelsys.org/teaching/BPC_lectures/pdf_files_BPC_topics/Alberts7th_C2-CellChem-Energy.pdf'
report=R/'download_report.json'
if report.exists() and json.loads(report.read_text()).get('status')=='downloaded_and_rendered':
    print('Previously rendered original PDF pages retained')
else:
    try:
        last_error=None
        urls=[url,url.replace('www.cancertelsys.org','cancertelsys.org'),url.replace('https://','http://')]
        for candidate in urls:
            try:
                response=requests.get(candidate,timeout=(15,45))
                response.raise_for_status()
                assert response.content.startswith(b'%PDF')
                url=candidate
                break
            except Exception as error:
                last_error=error
        else:
            raise last_error
        raw=response.content
        assert raw.startswith(b'%PDF'), 'Unexpected content type'
        doc=fitz.open(stream=raw,filetype='pdf')
        assert len(doc)>=57, f'Not a complete chapter PDF: {len(doc)} pages'
        assert 'chemistry' in ' '.join(doc[0].get_text().lower().split()), 'Chapter identity could not be verified'
        pages=[0,7]+list(range(45,57))
        assets=[]
        for index in pages:
            p=R/f'original_pdf_page_{index:02d}.jpg'
            doc[index].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(p)
            assets.append({'file':p.name,'pdf_page_index_zero_based':index,'pdf_page_sequence_one_based':index+1,
                'expected_print_page_for_review':49+index,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                'visual_review':'pending_actual_view'})
        report.write_text(json.dumps({'status':'downloaded_and_rendered','url':url,'pdf_sha256':hashlib.sha256(raw).hexdigest(),
            'bytes':len(raw),'pages':len(doc),'assets':assets,'note':'PDF file downloaded to memory only; original pages rendered for subsequent actual review, not a claim of semantic coverage.'},ensure_ascii=False,indent=2)+'\n')
        print('Rendered',len(assets),'original pages')
    except Exception as e:
        report.write_text(json.dumps({'status':'unavailable','url':url,'error':type(e).__name__+': '+str(e),'figures_from_supplied_repository_still_available':True},ensure_ascii=False,indent=2)+'\n')
        print('Original PDF unavailable:',type(e).__name__,str(e))
