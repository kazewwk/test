"""Real model adapters. Every raw model hypothesis is retained independently."""
from __future__ import annotations

import argparse
import dataclasses
import json
import os
import time
from pathlib import Path
from .common import load, write_json, utcnow


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
        result = model.transcribe(audio=(clip, sr), language=None, return_time_stamps=True)[0]
        words = [{"text": w.text, "start": float(w.start_time) + win["start"],
                  "end": float(w.end_time) + win["start"]} for w in result.time_stamps or []]
        record = {**win, "source_sha256": job["source_sha256"], "cache_fingerprint": job.get('cache_fingerprint'), "model": "Qwen/Qwen3-ASR-1.7B",
                  "aligner": "Qwen/Qwen3-ForcedAligner-0.6B", "model_revisions": revisions,
                  "language": result.language, "text": result.text, "words": words,
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
    device = "cpu" if job.get("device") == "cpu" else "gpu:0"
    model = PaddleOCR(ocr_version="PP-OCRv5", lang="ch", device=device,
                     enable_mkldnn=False,
                     use_doc_orientation_classify=False, use_doc_unwarping=False,
                     use_textline_orientation=False)
    for frame in job["frames"]:
        out = Path(job["output"]) / (Path(frame["path"]).stem + ".json")
        if reusable(out, job, "image_sha256", frame["sha256"]):
            continue
        started = time.perf_counter()
        result = list(model.predict(str(Path(job["lesson_dir"]) / frame["path"])))
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


VISUAL_PROMPT = """客观记录当前教学截图中的信息，不概括教师语音，不补充截图外知识。
保持画面中英文和中文原文。逐项描述可见图表、箭头、步骤、公式和演示操作；不确定写[无法确认]。
若有前一帧，仅说明两帧间可见变化，不能把推测的运动过程写成事实。
只返回 JSON: {"kind":"slide|diagram|table|formula|demonstration|screen|other",
"description":"客观描述", "visible_text":"可见文字原文", "formulas":[],
"tables":[], "uncertain":[], "needs_document_ocr":false}。
任何不清晰的文字不得猜写。表格和公式应将 needs_document_ocr 设为 true。"""


def visual_worker(job):
    import torch
    from PIL import Image
    from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration
    device = job.get("device", "cuda:0")
    torch.set_num_threads(job.get("threads", 8))
    if device == 'cpu':
        torch.backends.mkldnn.enabled = False
    revisions = job.setdefault("model_revisions", {})
    path = model_path("Qwen/Qwen2.5-VL-3B-Instruct", revisions)
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(path,
        torch_dtype=torch.float32 if device == "cpu" else torch.float16, device_map=device)
    processor = AutoProcessor.from_pretrained(path, use_fast=False, min_pixels=256 * 28 * 28, max_pixels=1280 * 28 * 28)
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
        messages = [{"role": "user", "content": [{"type": "image"} for _ in images]
                     + [{"type": "text", "text": VISUAL_PROMPT}]}]
        prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(text=[prompt], images=images, padding=True, return_tensors="pt").to(device)
        started = time.perf_counter()
        with torch.inference_mode():
            ids = model.generate(**inputs, max_new_tokens=1536, do_sample=False)
        raw = processor.batch_decode(ids[:, inputs.input_ids.shape[1]:], skip_special_tokens=True,
                                     clean_up_tokenization_spaces=False)[0]
        try:
            parsed = json.loads(raw.strip().removeprefix("```json").removesuffix("```").strip())
        except (ValueError, TypeError):
            parsed = {"description": raw, "uncertain": ["Model output is not valid JSON"],
                      "needs_document_ocr": True, "kind": "other"}
        write_json(out, {"path": frame["path"], "time": frame["time"], "image_sha256": frame["sha256"], "cache_fingerprint": job.get('cache_fingerprint'),
                         "model": "Qwen/Qwen2.5-VL-3B-Instruct", "model_revisions": revisions,
                         "raw": raw, "parsed": parsed, "verification": "model_observation_unverified",
                         "elapsed_seconds": time.perf_counter() - started})
        previous = image_path
        print(json.dumps({"stage": "visual", "frame": frame["path"]}), flush=True)


def document_worker(job):
    from paddleocr import PaddleOCRVL
    device = "cpu" if job.get("device") == "cpu" else "gpu:0"
    model = PaddleOCRVL(device=device, use_doc_orientation_classify=False, use_doc_unwarping=False)
    for frame in job["frames"]:
        folder = Path(job["output"]) / Path(frame["path"]).stem
        marker = folder / "complete.json"
        if reusable(marker, job, "image_sha256", frame["sha256"]):
            continue
        folder.mkdir(parents=True, exist_ok=True)
        started = time.perf_counter()
        for r in model.predict(str(Path(job["lesson_dir"]) / frame["path"])):
            r.save_to_json(save_path=str(folder))
            r.save_to_markdown(save_path=str(folder))
        write_json(marker, {"image_sha256": frame["sha256"], "cache_fingerprint": job.get('cache_fingerprint'), "elapsed_seconds": time.perf_counter() - started,
                            "model": "PaddleOCR-VL", "verification": "machine_extracted_unverified"})
        print(json.dumps({"stage": "document_ocr", "frame": frame["path"]}), flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("stage", choices=["qwen", "whisper", "ocr", "visual", "document"])
    p.add_argument("job")
    a = p.parse_args()
    job = load(a.job)
    Path(job["output"]).mkdir(parents=True, exist_ok=True)
    {"qwen": qwen_worker, "whisper": whisper_worker, "ocr": ocr_worker,
     "visual": visual_worker, "document": document_worker}[a.stage](job)


if __name__ == "__main__":
    main()
