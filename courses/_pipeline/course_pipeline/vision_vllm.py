"""Native BF16 visual inference with continuous batching; no quantization."""
from pathlib import Path
import time,json
from .common import load,write_json


def run(job):
    import cv2,torch
    from PIL import Image
    from transformers import AutoProcessor
    from vllm import LLM,SamplingParams
    from .models import model_path,reusable,VISUAL_PROMPT
    from .grounding import ground_annotations
    name=job.get('visual_model','Qwen/Qwen3.5-9B')
    path=model_path(name,job['model_revisions'])
    if not torch.cuda.is_bf16_supported():raise RuntimeError('Native BF16 GPU required')
    processor=AutoProcessor.from_pretrained(path)
    engine=LLM(model=path,dtype='bfloat16',max_model_len=8192,
               max_num_seqs=job.get('max_num_seqs',8),max_num_batched_tokens=8192,
               gpu_memory_utilization=.90,enforce_eager=True,enable_prefix_caching=False,
               limit_mm_per_prompt={'image':1,'video':0},mm_processor_kwargs={'max_pixels':2200000})
    output=Path(job['output']);output.mkdir(parents=True,exist_ok=True)
    pending=[f for f in job['frames'] if not reusable(output/(Path(f['path']).stem+'.json'),job,'image_sha256',f['sha256'])]
    size=job.get('batch_size',32)
    for start in range(0,len(pending),size):
        batch=pending[start:start+size];requests=[];ocr_rows=[]
        for frame in batch:
            image_path=Path(job['lesson_dir'])/frame['path']
            ocr=load(Path(job['lesson_dir'])/'evidence/ocr'/(image_path.stem+'.json'));ocr_rows.append(ocr)
            content=job.get('prompt',VISUAL_PROMPT)+'\nOCR候选仅供定位，不能盲从：'+json.dumps(ocr.get('texts',[]),ensure_ascii=False)
            prompt=processor.apply_chat_template([{'role':'user','content':[{'type':'image'},{'type':'text','text':content}]}],
                        tokenize=False,add_generation_prompt=True,enable_thinking=False)
            requests.append({'prompt':prompt,'multi_modal_data':{'image':Image.open(image_path).convert('RGB')}})
        began=time.perf_counter()
        results=engine.generate(requests,SamplingParams(temperature=0,max_tokens=job.get('max_new_tokens',2048)),use_tqdm=False)
        elapsed=time.perf_counter()-began
        if len(results)!=len(batch):raise RuntimeError('Different number of visual results')
        for frame,result,ocr in zip(batch,results,ocr_rows):
            generated=result.outputs[0];raw=generated.text
            try:
                parsed=json.loads(raw.strip().removeprefix('```json').removesuffix('```').strip())
                if not isinstance(parsed,dict):raise ValueError('JSON object required')
            except ValueError:parsed={'description':raw,'uncertain':['unparseable_model_output']}
            if not isinstance(parsed.get('uncertain',[]),list):parsed['uncertain']=[str(parsed['uncertain'])]
            if generated.finish_reason=='length':parsed.setdefault('uncertain',[]).append('generation_reached_token_limit')
            annotations=parsed.get('annotations',[])
            if isinstance(annotations,list) and all(isinstance(a,dict) for a in annotations):
                marker=Path(job['lesson_dir'])/'evidence/document'/Path(frame['path']).stem/'complete.json'
                blocks=load(marker).get('blocks',[]) if marker.exists() else []
                checked,flags=ground_annotations(cv2.imread(str(Path(job['lesson_dir'])/frame['path'])),annotations,ocr,blocks)
                parsed['annotations']=checked;parsed.setdefault('uncertain',[]).extend(flags)
            write_json(output/(Path(frame['path']).stem+'.json'),{'path':frame['path'],'time':frame['time'],
                'image_sha256':frame['sha256'],'input_fingerprint':job.get('frame_input_fingerprints',{}).get(frame['sha256']),'cache_fingerprint':job.get('cache_fingerprint'),'model':name,
                'model_revisions':job['model_revisions'],'dtype':'bfloat16','quantized':False,'backend':'vllm',
                'raw':raw,'parsed':parsed,'generated_tokens':len(generated.token_ids),'finish_reason':generated.finish_reason,
                'elapsed_seconds':elapsed/len(batch),'batch_size':len(batch),'verification':'model_observation_with_color_grounding_not_human_verified'})
        print(json.dumps({'stage':'visual','backend':'vllm','frames':len(batch),'seconds':elapsed}),flush=True)
