from __future__ import annotations

import difflib
import json
import re
from pathlib import Path
from .common import load, write_json, write_jsonl, atomic_text, seconds_label, artifact_hashes, utcnow


def normalized(s):
    return "".join(c.lower() for c in s if c.isalnum())


def disagreement(a, b):
    a, b = normalized(a), normalized(b)
    return 1 - difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() if a or b else 0.0


def needs_asr_review(a, b):
    aa, bb = normalized(a), normalized(b)
    matcher = difflib.SequenceMatcher(None, aa, bb, autojunk=False)
    omitted = max((max(i2-i1,j2-j1) for tag,i1,i2,j1,j2 in matcher.get_opcodes() if tag!='equal'),default=0)
    return disagreement(a,b)>0.12 or omitted>=12


def core_text(record):
    """Trim only duplicated context outside the ownership interval, never repeated speech.

    Preserve original punctuation by mapping aligned tokens back to source text.
    If mapping fails, preserve the entire raw hypothesis and explicitly flag it.
    """
    words = record.get("words", [])
    if not words:
        return record["text"], ["alignment_missing"] if record["text"].strip() else []
    keep = [i for i, w in enumerate(words)
            if record["core_start"] <= (w["start"] + w["end"]) / 2 < record["core_end"]]
    raw = record["text"]
    if normalized(raw) != "".join(normalized(w["text"]) for w in words):
        return raw, ["overlap_boundary_unresolved_raw_preserved"]
    if not keep:
        return "", []
    positions = [i for i, c in enumerate(raw) if c.isalnum()]
    prefix = [0]
    for word in words:
        prefix.append(prefix[-1] + len(normalized(word["text"])))
    lo = prefix[keep[0]]
    hi = prefix[keep[-1] + 1]
    start = positions[lo] if lo < len(positions) else len(raw)
    end = positions[hi] if hi < len(positions) else len(raw)
    return raw[start:end].strip(), []


def overlap(a, b):
    return max(0.0, min(a[1], b[1]) - max(a[0], b[0]))


def interval_union(intervals):
    result = []
    for a, b in sorted(intervals):
        if b < a:
            raise ValueError("Reversed interval")
        if result and a <= result[-1][1] + 1e-6:
            result[-1][1] = max(b, result[-1][1])
        else:
            result.append([a, b])
    return result


def srt_time(value):
    ms = max(0, round(value * 1000))
    return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"


def assemble(lesson_dir, source, media, audio_info, windows):
    root = Path(lesson_dir)
    frames = load(root / "frames.json")["frames"]
    offset = audio_info.get("source_start_seconds", 0)
    segments, issues = [], []
    for win in windows:
        q = load(root / "evidence/qwen" / f"chunk_{win['id']:05d}.json")
        w = load(root / "evidence/whisper" / f"chunk_{win['id']:05d}.json")
        text, flags = core_text(q)
        score = disagreement(q["text"], w["text"])
        if needs_asr_review(q['text'],w['text']):
            flags.append("asr_disagreement")
        silence = sum(overlap([win["core_start"], win["core_end"]], s)
                      for s in audio_info["silence_intervals"])
        length = win["core_end"] - win["core_start"]
        if not text.strip() and length - silence > 1:
            flags.append("empty_transcription_in_non_silence")
        if text.strip() and silence > length * 0.95:
            flags.append("speech_inside_detected_silence")
        previous_end = win["start"]
        for word in q.get("words", []):
            if word["end"] < word["start"] or word["start"] < previous_end - 0.3 or word["end"] > win["end"] + 0.5:
                flags.append("invalid_or_overlapping_word_timestamp")
                break
            previous_end = word["end"]
        if segments and normalized(text) and normalized(text) == normalized(segments[-1]["speech"]["text"]):
            flags.append("repeated_adjacent_transcript_preserved")
        start, end = win["core_start"] + offset, win["core_end"] + offset
        associated = [f for f in frames if f["time"] < end and f["end"] > start]
        review = root / "evidence/review_qwen" / f"chunk_{win['id']:05d}.json"
        visual_records = []
        for frame in associated:
            name = Path(frame["path"]).stem + ".json"
            ocr = load(root / "evidence/ocr" / name)
            visual = load(root / "evidence/visual" / name)
            document_dir = root / "evidence/document" / Path(frame["path"]).stem
            docs = [str(p.relative_to(root)) for p in document_dir.glob("*.md")]
            visual_records.append({**frame, "ocr": ocr, "visual": visual,
                                   "document_ocr_markdown": docs})
        segment = {"schema_version": "1.0", "segment_id": f"{source['drive_file_id']}:{win['id']:05d}",
                   "source_drive_file_id": source["drive_file_id"], "source_sha256": source["video_sha256"],
                   "start": start, "end": end,
                   "speech": {"text": text, "raw_primary": q["text"], "cross_check": w["text"],
                              "primary_words": q.get("words", []), "word_timebase": "extracted_audio",
                              "audio_source_offset": offset, "language": q.get("language"),
                              "disagreement": score, "verification": "automatic_cross_check_only",
                              "review_hypothesis": load(review) if review.exists() else None},
                   "frames": visual_records, "flags": sorted(set(flags))}
        segments.append(segment)
        for flag in segment["flags"]:
            issues.append({"type": flag, "start": start, "end": end, "segment_id": segment["segment_id"]})
    for frame in frames:
        name = Path(frame["path"]).stem + ".json"
        ocr = load(root / "evidence/ocr" / name)
        visual = load(root / "evidence/visual" / name)
        if not ocr["texts"]:
            issues.append({"type": "empty_ocr_needs_image_review", "start": frame["time"], "end": frame["end"], "frame": frame["path"]})
        if any(s < 0.8 for s in ocr["scores"]):
            issues.append({"type": "low_confidence_ocr", "start": frame["time"], "end": frame["end"], "frame": frame["path"]})
        if any(re.search(r'/[^/\n]{2,50}/', text) for text in ocr['texts']):
            issues.append({'type':'phonetic_symbols_need_review','start':frame['time'],'end':frame['end'],'frame':frame['path']})
        if visual["parsed"].get("uncertain"):
            issues.append({"type": "uncertain_visual_description", "start": frame["time"], "end": frame["end"], "frame": frame["path"]})
        other_text = visual["parsed"].get("visible_text", "")
        if other_text and disagreement(" ".join(ocr["texts"]), other_text) > 0.6:
            issues.append({"type": "ocr_visual_text_disagreement", "start": frame["time"], "end": frame["end"], "frame": frame["path"]})
    coverage = interval_union([[s["start"], s["end"]] for s in segments])
    total_covered = sum(b - a for a, b in coverage)
    total_audio = audio_info["duration_seconds"]
    if len(coverage) != 1 or abs(total_covered - total_audio) > 0.1:
        issues.append({"type": "audio_coverage_gap", "intervals": coverage})
    av_offset = abs(float(media["audio"].get("start_time", 0)) - float(media["video"].get("start_time", 0)))
    if av_offset > 0.3:
        issues.append({"type": "source_audio_video_start_offset", "seconds": av_offset})
    quality = {"schema_version": "1.0", "state": "complete_with_review_flags" if issues else "machine_processed",
               "video_duration_seconds": media["duration_seconds"], "audio_duration_seconds": total_audio,
               "audio_source_start_seconds": offset, "audio_processed_intervals": coverage,
               "audio_processed_seconds": total_covered, "audio_processing_coverage_ratio": total_covered / total_audio,
               "transcription_segments": len(segments), "keyframe_count": len(frames), "issues": issues,
               "accuracy": None, "human_reviewed": False,
               "checks": {"empty_asr": True, "repeated_adjacent_text": True, "timestamp_continuity": True,
                          "ocr_empty_and_confidence": True, "ocr_vlm_disagreement": True,
                          "source_av_offset": True, "semantic_audio_video_alignment": "requires human review"},
               "limitations": ["Processing coverage is not transcription accuracy",
                               "ASR models can agree on the same error",
                               "OCR and visual descriptions may contain unrecognized errors",
                               "Forced alignment does not validate spoken words",
                               "Visual sampling can miss changes below its configured threshold"]}
    write_jsonl(root / "segments.jsonl", segments)
    write_json(root / "qc_report.json", quality)
    header = f"# {source['title']}\n\n来源：Drive `{source['drive_file_id']}`；SHA256 `{source['video_sha256']}`。\n\n"
    raw_md = header + "以下按重叠音频窗口保留主模型完整输出，窗口交界可能重复。未做概括或自动纠错。\n\n"
    checked = header + "机器交叉校验稿；不等于人工确认稿。疑点保留两种原始结果，所有重复强调保留。\n\n"
    full = header + "语音原文、画面文字、视觉模型观察按源视频时间排列。视觉描述属于待核验的模型输出。\n\n"
    subtitles = []
    for i, s in enumerate(segments):
        span = f"{seconds_label(s['start'])}–{seconds_label(s['end'])}"
        q = load(root / "evidence/qwen" / f"chunk_{i:05d}.json")
        raw_md += f"## {seconds_label(q['start'] + offset)}–{seconds_label(q['end'] + offset)}\n\n{q['text']}\n\n"
        body = f"## {span}\n\n{s['speech']['text'] or '[本段无转写；参见质量报告]'}\n\n"
        if s["flags"]:
            body += "待复核：" + ", ".join(s["flags"]) + "。\n\n"
            body += "Whisper 原始候选：\n\n" + s["speech"]["cross_check"] + "\n\n"
        checked += body
        full += body
        for f in s["frames"]:
            full += f"### 画面 {seconds_label(f['time'])}\n\n![教学画面]({f['path']})\n\n"
            full += "OCR 原文：\n\n```text\n" + "\n".join(f["ocr"]["texts"]) + "\n```\n\n"
            full += "视觉观察（机器输出，未人工核验）：\n\n" + f["visual"]["parsed"].get("description", "[无法确认]") + "\n\n"
            for path in f["document_ocr_markdown"]:
                full += f"[表格／公式结构化提取]({path})\n\n"
        if s["speech"]["text"].strip():
            subtitles.append(f"{len(subtitles)+1}\n{srt_time(s['start'])} --> {srt_time(s['end'])}\n{s['speech']['text']}\n")
    atomic_text(root / "transcript_raw.md", raw_md)
    atomic_text(root / "transcript_checked.md", checked)
    atomic_text(root / "lecture_full.md", full)
    atomic_text(root / "subtitles.srt", "\n".join(subtitles))
    manifest = {"schema_version": "1.0", "source": source, "quality_state": quality["state"],
                "completed_at": utcnow(), "original_video_uploaded": False, "artifacts": artifact_hashes(root)}
    write_json(root / "manifest.json", manifest)
    return quality


def validate_lesson(directory):
    root = Path(directory)
    errors = []
    required = ["transcript_raw.md", "transcript_checked.md", "lecture_full.md", "subtitles.srt",
                "segments.jsonl", "manifest.json", "qc_report.json", "frames.json"]
    for name in required:
        if not (root / name).is_file():
            errors.append("missing:" + name)
    if errors:
        return errors
    manifest = load(root / "manifest.json")
    for name, expected in manifest["artifacts"].items():
        from .common import digest
        p = (root / name).resolve()
        if not p.is_relative_to(root.resolve()) or not p.is_file() or digest(p) != expected:
            errors.append("hash:" + name)
    for line in (root / "segments.jsonl").read_text().splitlines():
        s = json.loads(line)
        if not 0 <= s["start"] < s["end"]:
            errors.append("segment_timestamp:" + s["segment_id"])
        for f in s["frames"]:
            p = (root / f["path"]).resolve()
            if not p.is_relative_to(root.resolve()) or not p.is_file():
                errors.append("image:" + f["path"])
    for md in root.glob("*.md"):
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", md.read_text()):
            if "://" not in target and not target.startswith("#"):
                p = (md.parent / target.split("#")[0]).resolve()
                if not p.is_relative_to(root.resolve()) or not p.exists():
                    errors.append("markdown_link:" + target)
    return errors
