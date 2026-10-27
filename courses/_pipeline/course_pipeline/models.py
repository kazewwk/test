"""Real model adapters. Every raw model hypothesis is retained independently."""
from __future__ import annotations

import argparse
import dataclasses
import json
import os
import time
from pathlib import Path
from .common import load, write_json, utcnow

ASR_CONTEXT='This is a Chinese-English teaching recording. Transcribe the exact words in their original spoken languages. Never translate. Preserve repetitions, questions and examples.'


def reusable(path, job, source_key, source_value):
    if not path.exists():
        return False
    r = load(path)
    return r.get(source_key) == source_value and r.get('cache_fingerprint') == job.get('cache_fingerprint')


def jsonable(value):
    if dataclasses.is_dataclass(value):
        return jsonable(dataclasses.asdict(value))
    if isinstance(value, dict):
        return {k: jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if hasattr(value, "tolist"):
        return value.tolist()
    if hasattr(value, "item"):
        return value.item()
    return value


def model_path(name, revisions):
    from huggingface_hub import model_info, snapshot_download
    revision = revisions.get(name)
    if not revision:
        revision = model_info(name).sha
        revisions[name] = revision
    return snapshot_download(name, revision=revision)


def qwen_worker(job):
    import numpy as np
    import soundfile as sf
    import torch
    from qwen_asr import Qwen3ASRModel
    device = job.get("device", "cuda:0")
    torch.set_num_threads(job.get("threads", 8))
    dtype = torch.float32 if device == "cpu" else torch.float16
    revisions = job.setdefault("model_revisions", {})
    model = Qwen3ASRModel.from_pretrained(
        model_path("Qwen/Qwen3-ASR-1.7B", revisions), dtype=dtype, device_map=device,
        max_inference_batch_size=1, max_new_tokens=2048,
        forced_aligner=model_path("Qwen/Qwen3-ForcedAligner-0.6B", revisions),
        forced_aligner_kwargs={"dtype": dtype, "device_map": device})
    write_json(Path(job["output"]) / "model_revisions.json", revisions)
    audio, sr = sf.read(job["audio"], dtype="float32")
    if sr != 16000 or audio.ndim != 1:
        raise ValueError("Expected mono 16 kHz audio")
    for win in job["windows"]:
        out = Path(job["output"]) / f"chunk_{win['id']:05d}.json"
        if reusable(out, job, "source_sha256", job["source_sha256"]):
            continue
        started = time.perf_counter()
        clip = audio[round(win["start"] * sr):round(win["end"] * sr)]
        language_hint=win.get('language_hint',job.get('language'))
        context=job.get('context',ASR_CONTEXT)
        result = model.transcribe(audio=(clip, sr), language=language_hint, context=context, return_time_stamps=True)[0]
        words = [{"text": w.text, "start": float(w.start_time) + win["start"],
                  "end": float(w.end_time) + win["start"]} for w in result.time_stamps or []]
        record = {**win, "source_sha256": job["source_sha256"], "cache_fingerprint": job.get('cache_fingerprint'), "model": "Qwen/Qwen3-ASR-1.7B",
                  "aligner": "Qwen/Qwen3-ForcedAligner-0.6B", "model_revisions": revisions,
                  "language": result.language, "text": result.text, "words": words,
                  "language_hint":language_hint,"context":context,
                  "elapsed_seconds": time.perf_counter() - started, "device": device,
                  "dtype": str(dtype), "completed_at": utcnow()}
        write_json(out, record)
        print(json.dumps({"stage": "qwen", "chunk": win["id"], "seconds": record["elapsed_seconds"]}), flush=True)


def whisper_worker(job):
    import soundfile as sf
    from faster_whisper import WhisperModel
    device = "cpu" if job.get("device") == "cpu" else "cuda"
    revisions = job.setdefault("model_revisions", {})
    path = model_path("Systran/faster-whisper-large-v3", revisions)
    model = WhisperModel(path, device=device, compute_type="int8" if device == "cpu" else "float16",
                         cpu_threads=job.get("threads", 8), num_workers=1)
    write_json(Path(job["output"]) / "model_revisions.json", revisions)
    audio, sr = sf.read(job["audio"], dtype="float32")
    for win in job["windows"]:
        out = Path(job["output"]) / f"chunk_{win['id']:05d}.json"
        if reusable(out, job, "source_sha256", job["source_sha256"]):
            continue
        started = time.perf_counter()
        parts, info = model.transcribe(audio[round(win["start"] * sr):round(win["end"] * sr)],
                task="transcribe", language=None, beam_size=job.get("beam_size", 5),
                vad_filter=False, word_timestamps=True, condition_on_previous_text=False,
                temperature=0, multilingual=True)
        segments = []
        for s in parts:
            data = dataclasses.asdict(s)
            data["start"] += win["start"]
            data["end"] += win["start"]
            for word in data.get("words") or []:
                word["start"] += win["start"]
                word["end"] += win["start"]
            segments.append(data)
        record = {**win, "source_sha256": job["source_sha256"], "cache_fingerprint": job.get('cache_fingerprint'), "model": "faster-whisper-large-v3",
                  "model_revisions": revisions, "language": info.language,
                  "language_probability": info.language_probability,
                  "segments": segments, "text": "".join(s["text"] for s in segments),
                  "elapsed_seconds": time.perf_counter() - started, "device": device,
                  "completed_at": utcnow()}
        write_json(out, record)
        print(json.dumps({"stage": "whisper", "chunk": win["id"], "seconds": record["elapsed_seconds"]}), flush=True)


def ocr_worker(job):
    if job.get('ocr_engine') == 'onnx':
        return onnx_ocr_worker(job)
    from paddleocr import PaddleOCR
    import cv2
    device = "cpu" if job.get("device") == "cpu" else "gpu:0"
    model = PaddleOCR(ocr_version="PP-OCRv5", lang="ch", device=device,
                     enable_mkldnn=False,
                     text_det_limit_side_len=1920,text_det_limit_type='max',
                     use_doc_orientation_classify=False, use_doc_unwarping=False,
                     use_textline_orientation=False)
    for frame in job["frames"]:
        out = Path(job["output"]) / (Path(frame["path"]).stem + ".json")
        if reusable(out, job, "image_sha256", frame["sha256"]):
            continue
        started = time.perf_counter()
        pixels=cv2.imread(str(Path(job['lesson_dir'])/frame['path']))
        if pixels is None:raise RuntimeError('Key frame cannot be decoded: '+frame['path'])
        result = list(model.predict(pixels))
        if not result:raise RuntimeError('OCR engine returned no result object: '+frame['path'])
        raw = [jsonable(r.json) for r in result]
        texts, scores, boxes = [], [], []
        for r in raw:
            if isinstance(r, str):
                r = json.loads(r)
            d = r.get("res", r)
            texts.extend(d.get("rec_texts", []))
            scores.extend(d.get("rec_scores", []))
            boxes.extend(d.get("rec_polys", d.get("rec_boxes", [])))
        write_json(out, {"path": frame["path"], "time": frame["time"], "image_sha256": frame["sha256"], "cache_fingerprint": job.get('cache_fingerprint'),
                         "model": "PP-OCRv5", "texts": texts, "scores": scores, "boxes": boxes,
                         'device':device,'detection_limit_side':1920,
                         "raw": raw, "elapsed_seconds": time.perf_counter() - started})
        print(json.dumps({"stage": "ocr", "frame": frame["path"]}), flush=True)


def onnx_ocr_worker(job):
    import rapidocr
    from rapidocr import RapidOCR, EngineType, ModelType, OCRVersion, LangDet, LangRec
    from .common import digest
    engine = RapidOCR(params={
        'Det.engine_type': EngineType.ONNXRUNTIME, 'Det.lang_type': LangDet.CH,
        'Det.model_type': ModelType.SERVER, 'Det.ocr_version': OCRVersion.PPOCRV5,
        'Rec.engine_type': EngineType.ONNXRUNTIME, 'Rec.lang_type': LangRec.CH,
        'Rec.model_type': ModelType.SERVER, 'Rec.ocr_version': OCRVersion.PPOCRV5,
        'Global.use_cls': False,
    })
    artifacts={p.name:digest(p) for p in (Path(rapidocr.__file__).parent/'models').glob('*.onnx')}
    for frame in job['frames']:
        out=Path(job['output'])/(Path(frame['path']).stem+'.json')
        if reusable(out,job,'image_sha256',frame['sha256']):
            continue
        started=time.perf_counter()
        result=engine(str(Path(job['lesson_dir'])/frame['path']))
        write_json(out,{'path':frame['path'],'time':frame['time'],'image_sha256':frame['sha256'],
                       'cache_fingerprint':job.get('cache_fingerprint'),'model':'PP-OCRv5_server',
                       'runtime':'ONNX Runtime / RapidOCR 3.9.2',
                       'conversion_source':'https://github.com/RapidAI/RapidOCR',
                       'model_artifact_sha256':artifacts,
                       'texts':jsonable(result.txts) if result.txts is not None else [],
                       'scores':jsonable(result.scores) if result.scores is not None else [],
                       'boxes':jsonable(result.boxes) if result.boxes is not None else [],
                       'elapsed_seconds':time.perf_counter()-started})
        print(json.dumps({'stage':'ocr','frame':frame['path']}),flush=True)


VISUAL_PROMPT = """提取当前教学画面中OCR文字以外的教学信息，并核查OCR遗漏。
只描述课件、教学插图、演示和手写标注，不描述教师外貌、衣着、座椅或背景。
逐项记录圈画、下划线、勾号、箭头：颜色、指向的原文、关系和可见变化。
不要猜测音标、文字或动作；无法看清写[无法确认]。保留英文和中文，不翻译。
OCR候选另行完整保存，下面候选仅帮助定位，不是可靠答案；检查截图可见而候选遗漏或误识的文字。
若有两张图，第一张是前一状态，最后一张是当前状态；只根据看见的变化陈述，不推测中间过程。
输出紧凑JSON，不重复整张课件文字：
{"kind":"slide|diagram|table|formula|demonstration|screen|other","description":"教学关系或演示的客观描述",
"annotations":[{"type":"圈/线/勾/箭头","color":"","target":"标注对象原文或位置","meaning":"仅可见关系"}],
"ocr_missing_text":[],"ocr_disagreements":[],"table_present":false,"formula_present":false,
"formulas":[],"tables":[],"uncertain":[]}。
有表格或公式必须设置相应标志，后续由文档OCR完整提取；简单文字列表不能虚构为表格。"""


def visual_worker(job):
    if job.get('visual_model','Qwen/Qwen3.5-9B')=='Qwen/Qwen3.5-9B':
        from .vision_modern import run
        return run(job)
    import torch
    from PIL import Image
    from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration, Qwen3VLForConditionalGeneration
    device = job.get("device", "cuda:0")
    torch.set_num_threads(job.get("threads", 8))
    if device == 'cpu':
        torch.backends.mkldnn.enabled = False
    revisions = job.setdefault("model_revisions", {})
    model_name=job.get('visual_model','Qwen/Qwen3.5-9B')
    path = model_path(model_name, revisions)
    cls=Qwen3VLForConditionalGeneration if 'Qwen3-VL' in model_name else Qwen2_5_VLForConditionalGeneration
    model = cls.from_pretrained(path,
        torch_dtype=torch.float32 if device == "cpu" else torch.float16, device_map=device)
    processor = AutoProcessor.from_pretrained(path, use_fast=False, min_pixels=256 * 32 * 32, max_pixels=job.get('max_pixels',1024*32*32))
    write_json(Path(job["output"]) / "model_revisions.json", revisions)
    previous = None
    for frame in job["frames"]:
        image_path = Path(job["lesson_dir"]) / frame["path"]
        out = Path(job["output"]) / (image_path.stem + ".json")
        if reusable(out, job, "image_sha256", frame["sha256"]):
            previous = image_path
            continue
        images = [Image.open(image_path).convert("RGB")]
        if previous is not None:
            images.insert(0, Image.open(previous).convert("RGB"))
        question=job.get('prompt',VISUAL_PROMPT)
        ocr_path=Path(job['lesson_dir'])/'evidence/ocr'/(image_path.stem+'.json')
        if ocr_path.exists():
            question+='\nOCR候选（可能有误）：\n'+json.dumps(load(ocr_path).get('texts',[]),ensure_ascii=False)
        messages = [{"role": "user", "content": [{"type": "image"} for _ in images]
                     + [{"type": "text", "text": question}]}]
        prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(text=[prompt], images=images, padding=True, return_tensors="pt").to(device)
        started = time.perf_counter()
        with torch.inference_mode():
            ids = model.generate(**inputs, max_new_tokens=job.get('max_new_tokens',1536), do_sample=False)
        raw = processor.batch_decode(ids[:, inputs.input_ids.shape[1]:], skip_special_tokens=True,
                                     clean_up_tokenization_spaces=False)[0]
        try:
            parsed = json.loads(raw.strip().removeprefix("```json").removesuffix("```").strip())
        except (ValueError, TypeError):
            parsed = {"description": raw, "uncertain": ["Model output is not valid JSON"],
                      "needs_document_ocr": True, "kind": "other"}
        if not isinstance(parsed,dict):
            parsed={'description':raw,'uncertain':['Model output is not a JSON object'],'needs_document_ocr':True,'kind':'other'}
        generated_tokens=int(ids.shape[1]-inputs.input_ids.shape[1])
        if generated_tokens>=job.get('max_new_tokens',1536):
            parsed.setdefault('uncertain',[]).append('generation_reached_token_limit')
        write_json(out, {"path": frame["path"], "time": frame["time"], "image_sha256": frame["sha256"], "cache_fingerprint": job.get('cache_fingerprint'),
                         "model": model_name, "model_revisions": revisions,"generated_tokens":generated_tokens,
                         "device":device,"dtype":"float32" if device=='cpu' else 'float16',
                         "raw": raw, "parsed": parsed, "verification": "model_observation_unverified",
                         "elapsed_seconds": time.perf_counter() - started})
        previous = image_path
        print(json.dumps({"stage": "visual", "frame": frame["path"]}), flush=True)


def document_worker(job):
    from paddleocr import PaddleOCRVL
    import cv2
    from .fusion import normalized
    device = "cpu" if job.get("device") == "cpu" else "gpu:0"
    vl_dir=model_path('PaddlePaddle/PaddleOCR-VL-1.6',job['model_revisions'])
    model = PaddleOCRVL(pipeline_version='v1.6',vl_rec_model_dir=vl_dir,device=device, use_doc_orientation_classify=False, use_doc_unwarping=False,
                       use_ocr_for_image_block=True,use_chart_recognition=True,markdown_ignore_labels=[])
    for frame in job["frames"]:
        folder = Path(job["output"]) / Path(frame["path"]).stem
        marker = folder / "complete.json"
        if reusable(marker, job, "image_sha256", frame["sha256"]):
            continue
        folder.mkdir(parents=True, exist_ok=True)
        started = time.perf_counter()
        pixels=cv2.imread(str(Path(job['lesson_dir'])/frame['path']))
        if pixels is None:raise RuntimeError('Key frame cannot be decoded: '+frame['path'])
        results=list(model.predict(pixels))
        if not results:raise RuntimeError('Document OCR returned no result object: '+frame['path'])
        blocks=[]
        for r in results:
            r.save_to_json(save_path=str(folder))
            r.save_to_markdown(save_path=str(folder))
            raw=jsonable(r.json)
            if isinstance(raw,str):raw=json.loads(raw)
            blocks.extend(raw.get('res',raw).get('parsing_res_list',[]))
        extracted=''.join(normalized(b.get('block_content','')) for b in blocks)
        ocr_path=Path(job['lesson_dir'])/'evidence/ocr'/(Path(frame['path']).stem+'.json')
        repairs=[]
        if ocr_path.exists():
            ocr=load(ocr_path)
            for idx,(text,box,score) in enumerate(zip(ocr.get('texts',[]),ocr.get('boxes',[]),ocr.get('scores',[]))):
                if not normalized(text) or normalized(text) in extracted or score<.6:continue
                import numpy as np
                pts=np.asarray(box).reshape(-1,2);lo=pts.min(axis=0);hi=pts.max(axis=0)
                x1=max(0,int(lo[0])-8);y1=max(0,int(lo[1])-8)
                x2=min(pixels.shape[1],int(hi[0])+8);y2=min(pixels.shape[0],int(hi[1])+8)
                if x2<=x1 or y2<=y1:continue
                crop=pixels[y1:y2,x1:x2]
                repair_dir=folder/'repairs'/f'region_{idx:03d}';repair_dir.mkdir(parents=True,exist_ok=True)
                cv2.imwrite(str(repair_dir/'source.png'),crop)
                candidates=list(model.predict(crop,use_layout_detection=False))
                if not candidates:raise RuntimeError('Document ROI repair returned no result object')
                texts=[]
                for result in candidates:
                    result.save_to_json(save_path=str(repair_dir));result.save_to_markdown(save_path=str(repair_dir))
                    raw=jsonable(result.json)
                    if isinstance(raw,str):raw=json.loads(raw)
                    for block in raw.get('res',raw).get('parsing_res_list',[]):
                        content=block.get('block_content','')
                        if content:texts.append(content)
                repair_text='\n'.join(texts)
                repair={'source_bbox':[x1,y1,x2,y2],'ppocr_candidate':text,'recovered_text':repair_text,
                        'source_crop':str((repair_dir/'source.png').relative_to(folder)),
                        'status':'recovered_candidate' if repair_text else 'unresolved'}
                repairs.append(repair)
                if repair_text:blocks.append({'block_label':'roi_repair','block_content':repair_text,'block_bbox':[x1,y1,x2,y2]})
        if repairs:
            from .common import atomic_text
            md='# 布局遗漏区域的独立复查\n\n'
            for item in repairs:
                md+=f"原图位置：{item['source_bbox']}；PP-OCRv5 候选：{item['ppocr_candidate']}\n\n"
                md+=f"![复查区域]({item['source_crop']})\n\n{item['recovered_text'] or '[无法确认]'}\n\n"
            atomic_text(folder/'region_repairs.md',md)
        write_json(marker, {"image_sha256": frame["sha256"], "cache_fingerprint": job.get('cache_fingerprint'), "elapsed_seconds": time.perf_counter() - started,
                            "model": "PaddleOCR-VL-1.6",'blocks':blocks,'region_repairs':repairs,
                            "verification": "machine_extracted_unverified"})
        print(json.dumps({"stage": "document_ocr", "frame": frame["path"]}), flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=["qwen", "whisper", "ocr", "visual", "document", "mineru"])
    p.add_argument("job")
    a = p.parse_args()
    job = load(a.job)
    Path(job["output"]).mkdir(parents=True, exist_ok=True)
    if a.stage=='mineru':
        from .documents import mineru_worker
        mineru_worker(job)
    else:
        {"qwen": qwen_worker, "whisper": whisper_worker, "ocr": ocr_worker,
         "visual": visual_worker, "document": document_worker}[a.stage](job)


if __name__ == "__main__":
    main()
