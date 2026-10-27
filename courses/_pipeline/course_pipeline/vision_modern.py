from pathlib import Path
import json,time
from .common import load,write_json


def run(job):
    import torch,cv2
    from PIL import Image
    from transformers import AutoProcessor,AutoModelForImageTextToText
    from .models import model_path,reusable,VISUAL_PROMPT
    from .grounding import ground_annotations
    name=job.get('visual_model','Qwen/Qwen3.5-9B')
    revision=job['model_revisions']
    path=model_path(name,revision)
    device=job.get('device','cuda:0')
    dtype=torch.float32 if device=='cpu' else torch.bfloat16
    if device!='cpu' and not torch.cuda.is_bf16_supported():
        raise RuntimeError('Native BF16 vision requires a compatible GPU, such as L4')
    model=AutoModelForImageTextToText.from_pretrained(path,dtype=dtype,device_map=device,attn_implementation='sdpa')
    processor=AutoProcessor.from_pretrained(path)
    processor.tokenizer.padding_side='left'
    output=Path(job['output']);output.mkdir(parents=True,exist_ok=True)
    write_json(output/'model_revisions.json',revision)
    pending=[f for f in job['frames'] if not reusable(output/(Path(f['path']).stem+'.json'),job,'image_sha256',f['sha256'])]
    size=job.get('batch_size',4);cursor=0
    while cursor<len(pending):
        batch=pending[cursor:cursor+size]
        images=[];prompts=[];ocr_records=[]
        for frame in batch:
            image_path=Path(job['lesson_dir'])/frame['path']
            images.append(Image.open(image_path).convert('RGB'))
            ocr_path=Path(job['lesson_dir'])/'evidence/ocr'/(image_path.stem+'.json')
            ocr=load(ocr_path) if ocr_path.exists() else {};ocr_records.append(ocr)
            question=job.get('prompt',VISUAL_PROMPT)+'\nOCR候选仅供定位，不能盲从：'+json.dumps(ocr.get('texts',[]),ensure_ascii=False)
            messages=[{'role':'user','content':[{'type':'image'},{'type':'text','text':question}]}]
            prompts.append(processor.apply_chat_template(messages,tokenize=False,add_generation_prompt=True,enable_thinking=False))
        inputs=processor(text=prompts,images=images,padding=True,return_tensors='pt').to(device)
        started=time.perf_counter()
        try:
            with torch.inference_mode():
                ids=model.generate(**inputs,max_new_tokens=job.get('max_new_tokens',2048),do_sample=False)
        except torch.cuda.OutOfMemoryError:
            del inputs
            torch.cuda.empty_cache()
            if size==1:raise
            size=max(1,size//2)
            continue
        elapsed=time.perf_counter()-started
        decoded=processor.batch_decode(ids[:,inputs.input_ids.shape[1]:],skip_special_tokens=True,clean_up_tokenization_spaces=False)
        if len(decoded)!=len(batch):raise RuntimeError('Vision batch returned a different number of records')
        new_ids=ids[:,inputs.input_ids.shape[1]:]
        for index,(frame,raw,ocr) in enumerate(zip(batch,decoded,ocr_records)):
            stripped=raw.strip().removeprefix('```json').removesuffix('```').strip()
            try:
                parsed=json.loads(stripped)
                if not isinstance(parsed,dict):raise ValueError('JSON object required')
            except ValueError:
                parsed={'description':raw,'uncertain':['unparseable_model_output'],'needs_document_ocr':True,'kind':'other'}
            if not isinstance(parsed.get('uncertain',[]),list):parsed['uncertain']=[str(parsed['uncertain'])]
            generated_tokens=int((new_ids[index]!=processor.tokenizer.pad_token_id).sum().item())
            if generated_tokens>=job.get('max_new_tokens',2048):
                parsed.setdefault('uncertain',[]).append('generation_reached_token_limit')
            annotations=parsed.get('annotations',[])
            if isinstance(annotations,list) and all(isinstance(a,dict) for a in annotations):
                pixels=cv2.imread(str(Path(job['lesson_dir'])/frame['path']))
                doc_marker=Path(job['lesson_dir'])/'evidence/document'/Path(frame['path']).stem/'complete.json'
                doc_blocks=load(doc_marker).get('blocks',[]) if doc_marker.exists() else []
                checked,flags=ground_annotations(pixels,annotations,ocr,doc_blocks)
                parsed['annotations']=checked;parsed.setdefault('uncertain',[]).extend(flags)
            record={'path':frame['path'],'time':frame['time'],'image_sha256':frame['sha256'],
                    'cache_fingerprint':job.get('cache_fingerprint'),'model':name,'model_revisions':revision,
                    'device':device,'dtype':str(dtype),'quantized':False,'raw':raw,'parsed':parsed,
                    'generated_tokens':generated_tokens,
                    'verification':'model_observation_with_color_grounding_not_human_verified',
                    'elapsed_seconds':elapsed/len(batch),'batch_size':len(batch)}
            write_json(output/(Path(frame['path']).stem+'.json'),record)
            print(json.dumps({'stage':'visual','frame':frame['path'],'seconds':record['elapsed_seconds']}),flush=True)
        cursor+=len(batch)
        del inputs,ids
