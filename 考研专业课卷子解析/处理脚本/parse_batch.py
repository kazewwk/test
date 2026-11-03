"""Resumable per-exam MinerU 4.1.5 Advanced run. Never downgrades on failure."""
from pathlib import Path
import argparse,hashlib,json,os,platform,time,traceback,importlib.metadata
ROOT=Path(__file__).resolve().parent

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ids',nargs='*');ap.add_argument('--backend',choices=['cpu','gpu'],default='cpu');args=ap.parse_args()
    gpu=args.backend=='gpu'
    os.environ.setdefault('MINERU_MODEL_SMALL_BACKEND','torch' if gpu else 'onnx')
    os.environ.setdefault('MINERU_MODEL_VLM_ENGINE','vllm' if gpu else 'llama-cpp')
    os.environ.setdefault('MINERU_MODEL_VLM_MAX_CONCURRENCY','16' if gpu else '2')
    os.environ.setdefault('MINERU_PROCESSING_WINDOW_SIZE','8')
    os.environ.setdefault('OMP_NUM_THREADS','4' if gpu else '6')
    os.environ.setdefault('MINERU_INTRA_OP_NUM_THREADS','4' if gpu else '6')
    os.environ.setdefault('MINERU_INTER_OP_NUM_THREADS','1')
    if not gpu:
        os.environ.setdefault('MINERU_MODEL_ONNX_DEVICE','cpu')
        os.environ.setdefault('MINERU_LLAMA_CPP_BACKEND','cpu')
    from mineru.parser import MinerUParser
    from mineru.parser.writer import FileBasedDataWriter
    rows=json.loads((ROOT/'prepared_inputs.json').read_text())['papers']
    if args.ids:
        assert set(args.ids)<=set(r['id'] for r in rows),'unknown exam id'
        rows=[r for r in rows if r['id'] in args.ids]
    splits={}
    if (ROOT/'split_pages.json').exists():
        d=json.loads((ROOT/'split_pages.json').read_text());splits={r['id']:r for r in d['papers']}
    versions={}
    for name in ['mineru','docvortex','mineru-llama-cpp','torch','vllm','PyMuPDF']:
        try:versions[name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:pass
    assert versions['mineru']=='4.1.5',versions
    parser=MinerUParser(tier='advanced',parse_mode='ocr',image_analysis=True)
    assert parser.effort=='xhigh'
    errors=[];done=[]
    for row in rows:
        paper=row['id'];src=ROOT/row['input_file'];expected=row['pages'];mapping=None
        if paper in splits:
            s=splits[paper];src=ROOT/'parsing_inputs'/(paper+'.pdf');expected=s['output_pages'];mapping=s['page_mapping']
        out=ROOT/'results'/row['subject_group']/paper
        out.mkdir(parents=True,exist_ok=True)
        input_sha=sha(src);existing=out/'run.json'
        if existing.exists():
            prev=json.loads(existing.read_text())
            if prev.get('status')=='success' and prev.get('input_sha256')==input_sha and prev.get('versions')==versions and prev.get('backend')==args.backend:
                for rel,digest in prev['output_sha256'].items():assert sha(out/rel)==digest,(paper,rel)
                print('RESUME_VALID',paper,flush=True);done.append(paper);continue
            # Do not silently overwrite an earlier result or failed attempt.
            assert not any(out.glob('middle_json.json')),('existing output needs explicit review',paper)
        start=time.time();print('START',paper,expected,flush=True)
        try:
            result=parser.parse(src)
            assert len(result.pages)==expected,(paper,'missing pages',len(result.pages),expected)
            result.save(FileBasedDataWriter(str(out)))
            md=(out/'markdown.md').read_text()
            assert len(md.strip())>50,(paper,'empty parse')
            for ref in md.split('](')[1:]:
                ref=ref.split(')',1)[0].strip('<>')
                if ref and not ref.startswith(('http:','https:','data:','#')):
                    assert (out/ref.split('#')[0]).is_file(),(paper,'missing markdown asset',ref)
            run=dict(status='success',id=paper,title=row['title'],subject_group=row['subject_group'],tier='advanced',effort='xhigh',ocr_mode='ocr',image_analysis=True,backend=args.backend,small_backend=os.environ['MINERU_MODEL_SMALL_BACKEND'],vlm_engine=os.environ['MINERU_MODEL_VLM_ENGINE'],quantization='original weights' if gpu else 'Q8_0',versions=versions,python=platform.python_version(),input_sha256=input_sha,original_physical_pages=row['pages'],processed_pages=expected,seconds=round(time.time()-start,3),input_method=row['input_method'],page_mapping=mapping,warnings=row['warnings'],output_sha256={str(p.relative_to(out)):sha(p) for p in out.rglob('*') if p.is_file() and p.name not in ['run.json','failure.json']})
            dump(existing,run);print('SUCCESS',paper,run['seconds'],flush=True);done.append(paper)
        except Exception as exc:
            failure=dict(status='failed',id=paper,tier='advanced',effort='xhigh',input_sha256=input_sha,versions=versions,error=str(exc),traceback=traceback.format_exc())
            dump(out/'failure.json',failure);errors.append(failure);print('FAILED',paper,str(exc),flush=True)
            # Runtime/model initialization errors affect every paper: stop instead of repeating 136 failures.
            if not done:break
    dump(ROOT/('batch_status_'+args.backend+'.json'),dict(done=done,errors=errors,requested=len(rows),backend=args.backend))
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
