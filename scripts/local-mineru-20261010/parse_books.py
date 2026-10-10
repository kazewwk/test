import argparse
import hashlib
import json
import os
import shutil
import time
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
os.environ['MINERU_MODEL_SMALL_BACKEND'] = 'onnx'
os.environ['MINERU_MODEL_VLM_ENGINE'] = 'llama-cpp'
os.environ['OMP_NUM_THREADS'] = '4'
os.environ['OPENBLAS_NUM_THREADS'] = '4'

def main():
    args = argparse.ArgumentParser()
    args.add_argument('--worker', type=int, required=True)
    args = args.parse_args()
    cores = sorted(os.sched_getaffinity(0))
    chosen = cores[args.worker * 4:args.worker * 4 + 4]
    if chosen:
        os.sched_setaffinity(0, chosen)

    import mineru_llama_cpp
    OriginalEngine = mineru_llama_cpp.Engine
    class LimitedEngine(OriginalEngine):
        def __init__(self, *a, **kw):
            kw.setdefault('n_threads', 4)
            kw.setdefault('n_parallel', 2)
            super().__init__(*a, **kw)
    mineru_llama_cpp.Engine = LimitedEngine

    from mineru.parser import parse
    from mineru.parser.writer import FileBasedDataWriter

    books = json.loads((ROOT / 'work/chapters.json').read_text())
    jobs = []
    for chapter_no in range(max(len(b['chapters']) for b in books)):
        for book in reversed(books):
            if chapter_no < len(book['chapters']):
                jobs.append((book, book['chapters'][chapter_no]))

    states = ROOT / 'work/states'
    states.mkdir(exist_ok=True)
    for book, chapter in jobs:
        key = f"book{book['id']}-{chapter['number']:02}"
        if (states / f'{key}.done.json').exists():
            continue
        lock = states / f'{key}.lock'
        try:
            lock.mkdir()
        except FileExistsError:
            continue
        (lock / 'owner.json').write_text(json.dumps({'pid': int(Path('/proc/self/status').read_text().split('NSpid:')[1].splitlines()[0].split()[0]), 'worker': args.worker}))
        started = time.time()
        try:
            src = ROOT / 'work/inputs' / f'{key}.pdf'
            dest = ROOT / 'output' / book['title'] / chapter['name']
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest / '原始页面.pdf')
            for start in range(1, chapter['page_count'] + 1, 8):
                end = min(start + 7, chapter['page_count'])
                batch = dest / '解析批次' / f'pages_{start:04}-{end:04}'
                if (batch / 'complete.json').exists():
                    continue
                attempts = []
                for attempt in range(3):
                    try:
                        print(f'START worker={args.worker} {key} {start}-{end}', flush=True)
                        result = parse(src, tier='standard', ocr_mode='ocr', image_analysis=True,
                                       page_range=f'{start}-{end}')
                        indexes = [p.page_idx for p in result.pages]
                        assert indexes == list(range(start - 1, end)), indexes
                        result.save(FileBasedDataWriter(str(batch)))
                        status = {'book': book['title'], 'chapter': chapter['name'],
                                  'chapter_pages': [start, end],
                                  'source_pdf_pages': [chapter['start'] + start - 1, chapter['start'] + end - 1],
                                  'tier': 'standard', 'mode': 'local-hybrid-onnx-llama-cpp',
                                  'elapsed_chapter_seconds': round(time.time() - started, 2)}
                        (batch / 'complete.json').write_text(json.dumps(status, ensure_ascii=False, indent=2))
                        (states / f'worker{args.worker}.json').write_text(json.dumps(status, ensure_ascii=False))
                        print(f'DONE worker={args.worker} {key} {start}-{end}', flush=True)
                        break
                    except Exception as exc:
                        attempts.append(str(exc))
                        traceback.print_exc()
                        if attempt == 2:
                            raise
            info = dict(chapter, title=book['title'], worker=args.worker,
                        elapsed_seconds=round(time.time() - started, 2),
                        source_sha256=hashlib.sha256(src.read_bytes()).hexdigest())
            (dest / '章节信息.json').write_text(json.dumps(info, ensure_ascii=False, indent=2))
            (states / f'{key}.done.json').write_text(json.dumps(info, ensure_ascii=False, indent=2))
            print(f'CHAPTER DONE {key} {info["elapsed_seconds"]}s', flush=True)
        except Exception:
            (states / f'{key}.failed.txt').write_text(traceback.format_exc())
            raise
        finally:
            shutil.rmtree(lock)
    print('WORKER FINISHED', args.worker, flush=True)

if __name__ == '__main__':
    main()
