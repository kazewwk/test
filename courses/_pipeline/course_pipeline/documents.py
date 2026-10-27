from pathlib import Path
import json,time,tempfile
from .common import load,write_json,artifact_hashes


def mineru_worker(job):
    from PIL import Image
    from mineru.parser import parse
    from mineru.config import VlmConfig
    from mineru.parser.writer import FileBasedDataWriter
    from .models import reusable,model_path,fresh_artifact_directory
    from mineru.config import config
    from mineru.model.registry import MINERU_2_5_PRO_2605_1_2B
    from mineru.model.download import MODEL_COMPLETE_MARKER
    model_name="opendatalab/MinerU2.5-Pro-2605-1.2B"
    revision=job["model_revisions"][model_name]
    snapshot=Path(model_path(model_name,job["model_revisions"]))
    config.model.base_dir=str(Path.home()/".cache/course-pipeline/mineru"/revision)
    pinned=MINERU_2_5_PRO_2605_1_2B.local_dir();pinned.mkdir(parents=True,exist_ok=True)
    for item in snapshot.iterdir():
        dest=pinned/item.name
        if not dest.exists():dest.symlink_to(item,target_is_directory=item.is_dir())
    (pinned/MODEL_COMPLETE_MARKER).touch()
    for frame in job['frames']:
        out=Path(job['output'])/Path(frame['path']).stem
        marker=out/'complete.json'
        if reusable(marker,job,'image_sha256',frame['sha256']):continue
        fresh_artifact_directory(out,job)
        started=time.perf_counter()
        with tempfile.TemporaryDirectory(prefix='nce-mineru-') as directory:
            image=Path(directory)/(Path(frame['path']).stem+'.png')
            Image.open(Path(job['lesson_dir'])/frame['path']).convert('RGB').save(image,compress_level=1)
            result=parse(image,tier='advanced',ocr_mode='ocr',image_analysis=True,
                         vlm_config=VlmConfig(engine='vllm',max_concurrency=4))
            result.save(FileBasedDataWriter(str(out)))
        write_json(marker,{'artifacts':{k:v for k,v in artifact_hashes(out).items() if k!='complete.json'},'image_sha256':frame['sha256'],'source_frame':frame['path'],'source_time':frame['time'],
                           'cache_fingerprint':job.get('cache_fingerprint'),'tier':'advanced',
                           'model':'MinerU2.5-Pro-2605-1.2B','model_revision':revision,'elapsed_seconds':time.perf_counter()-started})
        print(json.dumps({'stage':'mineru','frame':frame['path']}),flush=True)
