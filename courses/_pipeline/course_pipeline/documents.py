from pathlib import Path
import json,time,tempfile
from .common import load,write_json


def mineru_worker(job):
    from PIL import Image
    from mineru.parser import parse
    from mineru.config import VlmConfig
    from mineru.parser.writer import FileBasedDataWriter
    from .models import reusable
    for frame in job['frames']:
        out=Path(job['output'])/Path(frame['path']).stem
        marker=out/'complete.json'
        if reusable(marker,job,'image_sha256',frame['sha256']):continue
        out.mkdir(parents=True,exist_ok=True)
        started=time.perf_counter()
        with tempfile.TemporaryDirectory(prefix='nce-mineru-') as directory:
            image=Path(directory)/(Path(frame['path']).stem+'.png')
            Image.open(Path(job['lesson_dir'])/frame['path']).convert('RGB').save(image,compress_level=1)
            result=parse(image,tier='advanced',ocr_mode='ocr',image_analysis=True,
                         vlm_config=VlmConfig(engine='vllm',max_concurrency=4))
            result.save(FileBasedDataWriter(str(out)))
        write_json(marker,{'image_sha256':frame['sha256'],'source_frame':frame['path'],'source_time':frame['time'],
                           'cache_fingerprint':job.get('cache_fingerprint'),'tier':'advanced',
                           'model':'MinerU2.5-Pro-2605-1.2B','elapsed_seconds':time.perf_counter()-started})
        print(json.dumps({'stage':'mineru','frame':frame['path']}),flush=True)
