import hashlib
from pathlib import Path
import numpy as np
import pytest
from course_pipeline.common import digest, write_json, load, checkpoint_valid
from course_pipeline.media import audio_windows, choose_events
from course_pipeline.inventory import lesson_directory
from course_pipeline.fusion import core_text, interval_union, disagreement, srt_time
from course_pipeline.fusion import needs_asr_review
from course_pipeline.fusion import needs_document_ocr


def test_audio_windows_cover_tail_and_overlap_without_loss():
    w = audio_windows(61.25, core_seconds=30, overlap_seconds=2)
    assert [(x['core_start'], x['core_end']) for x in w] == [(0,30),(30,60),(60,61.25)]
    assert w[0]['end'] == 32 and w[1]['start'] == 28 and w[2]['start'] == 58
    assert interval_union([[x['core_start'],x['core_end']] for x in w]) == [[0,61.25]]


def test_progressive_small_region_change_detected_without_scene_cut():
    frames = [np.zeros((60,80),np.uint8) for _ in range(30)]
    for f in frames[10:]:
        f[10:20,10:20] = 255
    for f in frames[20:]:
        f[20:30,10:20] = 255
    events=choose_events(iter(frames),10)
    assert any(1 <= e['time'] < 2 for e in events)
    assert any(2 <= e['time'] < 2.9 for e in events)


def test_ignored_presenter_does_not_trigger_duplicate_slides():
    frames=[np.zeros((60,80),np.uint8) for _ in range(30)]
    for i,f in enumerate(frames):
        f[:,60:] = 255 if i%2 else 0
    events=choose_events(iter(frames),10,ignore_regions=[[.75,0,1,1]])
    assert [e['reason'] for e in events] == ['first','last']


def test_vfr_timestamps_drive_capture_timing():
    frames=[np.zeros((60,80),np.uint8),np.ones((60,80),np.uint8)*255]
    events=choose_events(iter(frames),30,timestamps=[0,12])
    assert events[-1]['time'] == 12


def test_actual_repetition_is_preserved_and_only_overlap_trimmed():
    q=dict(text='yes, yes! 是的。',words=[dict(text='yes',start=0,end=1),
           dict(text='yes',start=2,end=3),dict(text='是',start=4,end=5),dict(text='的',start=5,end=6)],
           core_start=0,core_end=4)
    text,flags=core_text(q)
    assert text=='yes, yes!' and not flags


def test_alignment_mismatch_preserves_raw_not_guessed_text():
    q=dict(text='I heard thirteen.',words=[dict(text='thirty',start=0,end=1)],core_start=0,core_end=2)
    text,flags=core_text(q)
    assert text==q['text'] and flags==['overlap_boundary_unresolved_raw_preserved']


def test_lesson_numbers_are_not_part_numbers():
    assert lesson_directory('L001 单词讲解造句',3).startswith('Lesson_001_P003_')
    assert lesson_directory('1-48总结',1).startswith('Intro_P001_')


def test_changed_source_invalidates_cached_results(tmp_path):
    p=tmp_path/'x';p.write_text('original')
    record=dict(state='complete',inputs={'source':'a'},outputs={str(p):digest(p)})
    assert checkpoint_valid(record,{'source':'a'})
    assert not checkpoint_valid(record,{'source':'b'})
    p.write_text('corrupt')
    assert not checkpoint_valid(record,{'source':'a'})


def test_disagreement_and_srt_rounding():
    assert disagreement('Private, 私人的','private 私人的')==0
    assert disagreement('a','b')==1
    assert srt_time(59.9999)=='00:01:00,000'


def test_missing_english_clause_is_flagged_even_in_long_chinese_context():
    context='这里保留完整的中文讲解。'*30
    assert needs_asr_review(context+'He goes to a private school.',context)


def test_saved_webp_preserves_decoded_pixels(tmp_path):
    import cv2
    from PIL import Image
    rng=np.random.default_rng(31)
    image=rng.integers(0,256,(32,64,3),dtype=np.uint8)
    dest=tmp_path/'frame.webp'
    Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGB)).save(dest,lossless=True,method=0)
    assert np.array_equal(image,cv2.imread(str(dest)))


def test_whisper_hardware_migration_reuses_only_matching_unquantized_results(tmp_path):
    from course_pipeline.models import reusable
    from course_pipeline.cli import inference_fingerprint
    import json
    job=dict(source_sha256='video',model_revisions={'Systran/faster-whisper-large-v3':'rev'},windows=audio_windows(60),device='cpu')
    cpu=inference_fingerprint('whisper',job)
    gpu=inference_fingerprint('whisper',{**job,'device':'cuda:0'})
    job.update(cache_fingerprint=cpu,accepted_cache_fingerprints=[gpu])
    record=tmp_path/'chunk.json'
    record.write_text(json.dumps(dict(source_sha256='video',cache_fingerprint=gpu)))
    assert reusable(record,job,'source_sha256','video')
    assert not reusable(record,job,'source_sha256','different-video')
    record.write_text(json.dumps(dict(source_sha256='video',cache_fingerprint='old-int8')))
    assert not reusable(record,job,'source_sha256','video')


def test_vectorized_change_detector_preserves_original_tile_thresholds():
    import cv2
    from course_pipeline.media import difference
    rng=np.random.default_rng(71)
    for shape in [(216,384),(60,80),(61,81)]:
        left=rng.integers(0,256,shape,dtype=np.uint8);right=rng.integers(0,256,shape,dtype=np.uint8)
        diff=cv2.absdiff(left,right);mask=diff>18
        largest=max(float(x.mean()) for row in np.array_split(mask,12,axis=0) for x in np.array_split(row,16,axis=1))
        assert difference(left,right)==(float(mask.mean()),largest,float(diff.mean()))


def test_table_cannot_silently_skip_document_ocr_due_to_model_boolean():
    assert needs_document_ocr({'parsed':{'kind':'slide','needs_document_ocr':False,'tables':[{'rows':[['a']]}]}})


def test_completed_speech_survives_hardware_and_ocr_changes():
    from course_pipeline.cli import inference_fingerprint
    job=dict(source_sha256='source',model_revisions={'Qwen/Qwen3-ASR-1.7B':'a','Qwen/Qwen3-ForcedAligner-0.6B':'b'},windows=audio_windows(60),device='cpu',ocr_engine='onnx')
    original=inference_fingerprint('qwen',job)
    assert original==inference_fingerprint('qwen',{**job,'device':'cuda:0','ocr_engine':'paddle'})
    assert original!=inference_fingerprint('qwen',{**job,'source_sha256':'changed'})


def test_thin_handwritten_stroke_is_captured_before_later_slide_text():
    frames=[np.full((216,384),255,np.uint8) for _ in range(50)]
    for frame in frames[10:]:frame[50,50:62]=40
    events=choose_events(iter(frames),10)
    assert any(1<=event['time']<2 for event in events)


def test_adding_keyframes_does_not_invalidate_processed_independent_images():
    from course_pipeline.cli import inference_fingerprint
    job=dict(source_sha256='same-video',model_revisions={},frames=[{'sha256':'first','time':0}],ocr_engine='paddle')
    before=inference_fingerprint('ocr',job)
    job['frames'].append({'sha256':'new-added-frame','time':1})
    assert before==inference_fingerprint('ocr',job)
