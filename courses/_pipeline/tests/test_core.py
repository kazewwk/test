import hashlib
from pathlib import Path
import numpy as np
import pytest
from course_pipeline.common import digest, write_json, load, checkpoint_valid
from course_pipeline.media import audio_windows, choose_events
from course_pipeline.inventory import lesson_directory
from course_pipeline.fusion import core_text, interval_union, disagreement, srt_time
from course_pipeline.fusion import needs_asr_review


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
    rng=np.random.default_rng(31)
    image=rng.integers(0,256,(32,64,3),dtype=np.uint8)
    dest=tmp_path/'frame.webp'
    assert cv2.imwrite(str(dest),image,[cv2.IMWRITE_WEBP_QUALITY,101])
    assert np.array_equal(image,cv2.imread(str(dest)))
