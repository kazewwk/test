from __future__ import annotations

import difflib
import json
import re
from pathlib import Path
from urllib.parse import unquote
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
    english=lambda s:[x.lower() for x in re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)*",s)]
    return disagreement(a,b)>0.12 or omitted>=12 or english(a)!=english(b)


def needs_document_ocr(visual):
    p=visual.get('parsed',visual)
    return bool(p.get('needs_document_ocr') or p.get('table_present') or p.get('formula_present') or p.get('tables') or p.get('formulas')
                or p.get('kind') in ('table','formula'))


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


def whisper_core(record):
    words=[word for segment in record.get('segments',[]) for word in segment.get('words') or []]
    if words:
        return ''.join(w['word'] for w in words if record['core_start'] <= (w['start']+w['end'])/2 < record['core_end']).strip()
    return record.get('text','')


def cjk_fraction(text):
    chars=[c for c in text if c.isalnum()]
    return sum('\u4e00'<=c<='\u9fff' for c in chars)/max(1,len(chars))


def language_mismatch(primary,secondary):
    return cjk_fraction(primary.get('text',''))<.08 and cjk_fraction(secondary.get('text',''))>.35


def select_checked(primary,secondary,review=None,review_secondary=None,language_review=None):
    text,flags=core_text(primary)
    reference=whisper_core(review_secondary or secondary)
    score=disagreement(text,reference)
    selected='qwen';chosen=primary
    rejected=[]
    for name,candidate in [('review_qwen',review),('language_review_qwen',language_review)]:
        if not candidate:continue
        proposed,proposed_flags=core_text(candidate)
        proposed_score=disagreement(proposed,reference)
        # A cross-check model may omit an English example. Agreement alone must
        # not reward deleting a substantial part of the primary hypothesis.
        if not language_mismatch(primary,secondary) and len(normalized(proposed))<len(normalized(text))*.85:
            rejected.append(name+':possible_content_omission');continue
        if proposed.strip() and not proposed_flags and proposed_score+.04<score:
            chosen=candidate;text=proposed;flags=proposed_flags;score=proposed_score;selected=name
    if selected!='qwen':flags.append('checked_uses_context_review')
    if language_mismatch(primary,secondary):flags.append('primary_language_mismatch')
    if rejected:flags.append('review_shorter_content_preserved_for_audit')
    return text,flags,chosen,{'selected':selected,'agreement_with_cross_check':1-score,
                            'primary_agreement':1-disagreement(core_text(primary)[0],reference),'rejected_candidates':rejected}


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



def aligned_subtitles(record,offset=0):
    text,flags=core_text(record)
    if not text.strip():return []
    fallback=[{'start':record['core_start']+offset,'end':record['core_end']+offset,'text':text,'alignment':'window_fallback'}]
    words=record.get('words',[])
    if flags or not words:return fallback
    selected=[i for i,w in enumerate(words) if record['core_start']<=(w['start']+w['end'])/2<record['core_end']]
    if any(words[i]['end']<=words[i]['start'] for i in selected):return fallback
    raw=record['text'];positions=[i for i,c in enumerate(raw) if c.isalnum()];prefix=[0]
    for word in words:prefix.append(prefix[-1]+len(normalized(word['text'])))
    groups=[];current=[]
    for i in selected:
        if current and (words[i]['end']-words[current[0]]['start']>6 or sum(len(words[j]['text']) for j in current)>70):
            groups.append(current);current=[]
        current.append(i)
    if current:groups.append(current)
    cues=[]
    for group in groups:
        lo=prefix[group[0]];hi=prefix[group[-1]+1]
        start=positions[lo] if lo<len(positions) else len(raw)
        end=positions[hi] if hi<len(positions) else len(raw)
        a=max(record['core_start'],words[group[0]]['start'])+offset
        b=min(record['core_end'],words[group[-1]]['end'])+offset
        if a>=b or (cues and a<cues[-1]['end']-.01):return fallback
        cues.append({'start':a,'end':b,'text':raw[start:end].strip(),'alignment':'Qwen3-ForcedAligner'})
    if normalized(''.join(c['text'] for c in cues))!=normalized(text):return fallback
    return cues

def inline_document(root,relative):
    path=Path(root)/relative
    text=path.read_text(encoding='utf-8')
    prefix=Path(relative).parent
    def target(value):
        if '://' in value or value.startswith(('data:','#')):return value
        return str(prefix/value)
    text=re.sub(r'(!?\[[^\]]*\]\()([^)]+)(\))',lambda m:m[1]+target(m[2])+m[3],text)
    text=re.sub(r'(<img\b[^>]*\bsrc=["\'])([^"\']+)(["\'])',lambda m:m[1]+target(m[2])+m[3],text)
    text=re.sub(r'(?m)^(#{1,4}) ',lambda m:'####'+m[1]+' ',text)
    return text


def assemble(lesson_dir, source, media, audio_info, windows):
    root = Path(lesson_dir)
    frames = load(root / "frames.json")["frames"]
    offset = audio_info.get("source_start_seconds", 0)
    segments, issues = [], []
    gap_file=root/"evidence/audio_gap_review.json"
    gap_reviews=load(gap_file).get("reviews",[]) if gap_file.exists() else []
    for win in windows:
        q = load(root / "evidence/qwen" / f"chunk_{win['id']:05d}.json")
        w = load(root / "evidence/whisper" / f"chunk_{win['id']:05d}.json")
        review_path=root/'evidence/review_qwen'/f"chunk_{win['id']:05d}.json"
        review_w_path=root/'evidence/review_whisper'/f"chunk_{win['id']:05d}.json"
        language_path=root/'evidence/language_review_qwen'/f"chunk_{win['id']:05d}.json"
        qr=load(review_path) if review_path.exists() else None
        wr=load(review_w_path) if review_w_path.exists() else None
        lr=load(language_path) if language_path.exists() else None
        text, flags, chosen,selection = select_checked(q,w,qr,wr,lr)
        extra_audio=[g for g in gap_reviews if overlap([win["core_start"],win["core_end"]],[g["start"],g["end"]])>0]
        if extra_audio:flags.append("voiced_alignment_gap_reviewed")
        score = disagreement(q["text"], w["text"])
        if needs_asr_review(q['text'],w['text']):
            flags.append("raw_asr_disagreement")
        if needs_asr_review(text,whisper_core(wr or w)):
            flags.append("asr_disagreement_unresolved")
        if re.search(r'音标|发音|读音|重音|音节|口型|连读|弱读|元音|辅音|舌头|嘴唇|pronunci|phoneme|syllable',text,re.I):
            flags.append('pronunciation_demonstration_requires_original_audio_review')
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
            api_path=root/"evidence/visual_api"/name
            visual_path=api_path if api_path.exists() else root/"evidence/visual"/name
            visual = load(visual_path)
            if visual.get("image_sha256") not in (None,frame["sha256"]):raise ValueError("Visual evidence image hash mismatch: "+name)
            # Keep the complete hypotheses in their evidence files. Avoid
            # embedding a second copy of the same raw JSON in every segment.
            ocr = {k:v for k,v in ocr.items() if k != 'raw'}
            ocr['raw_evidence'] = 'evidence/ocr/' + name
            visual = {k:v for k,v in visual.items() if k not in ('raw','model_revisions')}
            visual['raw_evidence'] = str(visual_path.relative_to(root))
            document_dir = root / "evidence/document" / Path(frame["path"]).stem
            docs = [str(p.relative_to(root)) for p in document_dir.glob("*.md")]
            mineru_dir=root/'evidence/mineru'/Path(frame['path']).stem
            mineru_docs=[str(p.relative_to(root)) for p in mineru_dir.glob('*.md')]
            visual_records.append({**frame, "ocr": ocr, "visual": visual,
                                   "document_ocr_markdown": docs,'mineru_markdown':mineru_docs})
        segment = {"schema_version": "1.0", "segment_id": f"{source['drive_file_id']}:{win['id']:05d}",
                   "source_drive_file_id": source["drive_file_id"], "source_sha256": source["video_sha256"],
                   "start": start, "end": end,
                   "speech": {"text": text, "raw_primary": q["text"], "cross_check": w["text"],
                              "primary_words": q.get("words", []), "word_timebase": "extracted_audio",
                              "checked_words":chosen.get('words',[]),'selection':selection,
                              "audio_source_offset": offset, "language": chosen.get("language"),
                              "primary_language":q.get("language"),"subtitle_cues":aligned_subtitles(chosen,offset),
                              "disagreement": score, "verification": "automatic_cross_check_only",
                              "review_hypothesis": qr,'review_cross_check':wr,'language_review':lr,'gap_reviews':extra_audio},
                   "frames": visual_records, "flags": sorted(set(flags))}
        rag_parts=[text]
        unresolved=[f for f in flags if f not in ('checked_uses_context_review','raw_asr_disagreement','primary_language_mismatch')]
        if unresolved:
            rag_parts.append('语音待复核：'+', '.join(unresolved)+'\n独立转写候选：'+whisper_core(wr or w))
        for g in extra_audio:
            rag_parts.append(f"有声/对齐疑点复查 {g['start']:.3f}–{g['end']:.3f} 秒（含前后上下文，未直接补入主稿）：\nQwen：{g['qwen']['text']}\nWhisper：{g['whisper']['text']}")
        for frame in visual_records:
            rag_parts.append(f"画面 {seconds_label(frame['time'])}\n"+'\n'.join(frame['ocr']['texts']))
            for doc in frame['document_ocr_markdown']+frame['mineru_markdown']:
                rag_parts.append(inline_document(root,doc))
            rag_parts.append('视觉观察（模型候选，见核验字段）：'+frame['visual']['parsed'].get('description',''))
            if frame['visual']['parsed'].get('text_lines'):
                rag_parts.append('视觉接口逐字读图候选：\n'+'\n'.join(frame['visual']['parsed']['text_lines']))
            if frame['visual']['parsed'].get('annotations'):
                rag_parts.append(json.dumps([{k:v for k,v in a.items() if not k.endswith('_original_model')} for a in frame['visual']['parsed']['annotations']],ensure_ascii=False))
            if frame['visual']['parsed'].get('uncertain'):
                rag_parts.append('视觉待核验：'+json.dumps(frame['visual']['parsed']['uncertain'],ensure_ascii=False))
        segment['id']=segment['segment_id']
        segment['text']='\n\n'.join(rag_parts)
        segment['metadata']={'series':source.get('series'),'lesson':source['title'],'drive_file_id':source['drive_file_id'],
                             'video_sha256':source['video_sha256'],'start':start,'end':end,
                             'image_paths':[f['path'] for f in associated],'uncertainty_flags':segment['flags']}
        segments.append(segment)
        for flag in segment["flags"]:
            issues.append({"type": flag, "start": start, "end": end, "segment_id": segment["segment_id"]})
    for g in gap_reviews:
        issues.append({"type":"voiced_word_alignment_gap_reviewed","start":g["start"]+offset,"end":g["end"]+offset,"review":"evidence/audio_gap_review.json","status":g["status"]})
    for frame in frames:
        name = Path(frame["path"]).stem + ".json"
        ocr = load(root / "evidence/ocr" / name)
        api_path=root/"evidence/visual_api"/name
        visual = load(api_path if api_path.exists() else root/"evidence/visual"/name)
        if not ocr["texts"]:
            issues.append({"type": "empty_ocr_needs_image_review", "start": frame["time"], "end": frame["end"], "frame": frame["path"]})
        if any(s < 0.8 for s in ocr["scores"]):
            issues.append({"type": "low_confidence_ocr", "start": frame["time"], "end": frame["end"], "frame": frame["path"]})
        if any(re.search(r'/[^/\n]{2,50}/', text) for text in ocr['texts']):
            issues.append({'type':'phonetic_symbols_need_review','start':frame['time'],'end':frame['end'],'frame':frame['path']})
        if visual["parsed"].get("uncertain"):
            issues.append({"type": "uncertain_visual_description", "start": frame["time"], "end": frame["end"], "frame": frame["path"]})
        if visual['parsed'].get('ocr_missing_text') or visual['parsed'].get('ocr_disagreements'):
            issues.append({'type':'ocr_omission_or_disagreement','start':frame['time'],'end':frame['end'],'frame':frame['path']})
        description=visual['parsed'].get('description','')
        if ocr['texts'] and re.search('穿着|裤子|男性|衬衫',description) and not re.search('教学|课件|下划线|圈|表格|单词',description):
            issues.append({'type':'visual_description_misses_instructional_content','start':frame['time'],'end':frame['end'],'frame':frame['path']})
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
                               "ASR may normalize deliberately nonstandard pronunciations; pronunciation demonstrations require source-audio review",
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
        for g in s['speech'].get('gap_reviews',[]):
            body+=f"### 原音疑点复查 {seconds_label(g['start']+offset)}–{seconds_label(g['end']+offset)}\n\n"
            body+="下列候选含前后上下文，可能对应发音示范、对齐间隙或遗漏；没有直接当作新增原文插入主稿。\n\n"
            body+='Qwen 候选：'+g['qwen']['text']+'\n\nWhisper 候选：'+g['whisper']['text']+'\n\n'
        checked += body
        full += body
        for f in s["frames"]:
            full += f"### 画面 {seconds_label(f['time'])}\n\n![教学画面]({f['path']})\n\n"
            full += f"[OCR 原始输出](evidence/ocr/{Path(f['path']).stem}.json) · [视觉原始输出]({f['visual']['raw_evidence']})\n\n"
            full += "OCR 原文：\n\n```text\n" + "\n".join(f["ocr"]["texts"]) + "\n```\n\n"
            if f['visual']['parsed'].get('text_lines'):
                full+='视觉接口逐字读图候选：\n\n```text\n'+'\n'.join(f['visual']['parsed']['text_lines'])+'\n```\n\n'
            full += "视觉观察（机器输出，未人工核验）：\n\n" + f["visual"]["parsed"].get("description", "[无法确认]") + "\n\n"
            observations={k:f['visual']['parsed'][k] for k in ['annotations','ocr_missing_text','ocr_disagreements','formulas','tables','uncertain'] if f['visual']['parsed'].get(k)}
            if observations:
                full+='标注、结构与待核验文字：\n\n```json\n'+json.dumps(observations,ensure_ascii=False,indent=2)+'\n```\n\n'
            for path in f["document_ocr_markdown"]:
                full += f"#### PaddleOCR-VL 原文与结构\n\n[独立结果]({path})\n\n"+inline_document(root,path)+'\n\n'
            for path in f['mineru_markdown']:
                full += f"#### MinerU 独立解析\n\n[独立结果]({path})\n\n"+inline_document(root,path)+'\n\n'
        for cue in s["speech"]["subtitle_cues"]:
            subtitles.append(f"{len(subtitles)+1}\n{srt_time(cue['start'])} --> {srt_time(cue['end'])}\n{cue['text']}\n")
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
    for md in root.rglob("*.md"):
        content=md.read_text()
        targets=re.findall(r"!?\[[^\]]*\]\(([^)]+)\)",content)+re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)',content)
        for target in targets:
            if "://" not in target and not target.startswith(("#",'data:')):
                p = (md.parent / unquote(target.split("#")[0])).resolve()
                if not p.is_relative_to(root.resolve()) or not p.exists():
                    errors.append("markdown_link:" + target)
    return errors
