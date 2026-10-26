from pathlib import Path
from course_pipeline.common import write_json,digest,load
from course_pipeline.fusion import assemble,validate_lesson


def test_fusion_delivers_traceable_files_and_detects_tampering(tmp_path):
    root=tmp_path/'lesson';(root/'frames').mkdir(parents=True)
    frame=root/'frames'/'f.webp';frame.write_bytes(b'synthetic test image only')
    frames=[dict(path='frames/f.webp',time=0,end=2,sha256=digest(frame))]
    write_json(root/'frames.json',{'frames':frames})
    win=dict(id=0,start=0,end=2,core_start=0,core_end=2)
    words=[dict(text='Hello',start=.1,end=.5),dict(text='中',start=.6,end=.8),dict(text='文',start=.8,end=1.)]
    write_json(root/'evidence/qwen/chunk_00000.json',{**win,'text':'Hello 中文。','words':words,'language':'Chinese,English'})
    write_json(root/'evidence/whisper/chunk_00000.json',{**win,'text':'Hello 中文。'})
    write_json(root/'evidence/ocr/f.json',dict(texts=['Hello 中文'],scores=[.98],boxes=[]))
    write_json(root/'evidence/visual/f.json',dict(parsed=dict(description='Synthetic fixture text slide',visible_text='Hello 中文',uncertain=[])))
    source=dict(title='Synthetic test fixture',drive_file_id='test-only',video_sha256='0'*64)
    media=dict(duration_seconds=2,video={'start_time':'0'},audio={'start_time':'0'})
    audio=dict(duration_seconds=2,source_start_seconds=0,silence_intervals=[])
    qc=assemble(root,source,media,audio,[win])
    assert qc['audio_processed_intervals']==[[0,2]]
    assert qc['accuracy'] is None and qc['human_reviewed'] is False
    assert validate_lesson(root)==[]
    assert '![教学画面](frames/f.webp)' in (root/'lecture_full.md').read_text()
    frame.write_bytes(b'corrupted')
    assert 'hash:frames/f.webp' in validate_lesson(root)
