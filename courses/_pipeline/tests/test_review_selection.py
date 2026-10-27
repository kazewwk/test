from course_pipeline.fusion import select_checked,language_mismatch

def aligned(text,words):
    return dict(text=text,words=[dict(text=w,start=i,end=i+.5) for i,w in enumerate(words)],
                core_start=0,core_end=30,start=0,end=30)

def test_context_review_recovers_original_language_without_deleting_raw():
    primary=aligned('This means it is none of your business.', ['This','means','it','is','none','of','your','business'])
    secondary={'text':'这句话表示与你无关。'}
    review=aligned('这句话表示与你无关。',list('这句话表示与你无关'))
    text,flags,chosen,selection=select_checked(primary,secondary,review,secondary)
    assert text=='这句话表示与你无关。'
    assert selection['selected']=='review_qwen'
    assert 'primary_language_mismatch' in flags
    assert primary['text']=='This means it is none of your business.'

def test_review_cannot_replace_primary_when_agreement_worsens():
    primary=aligned('Hello, hello!', ['Hello','hello'])
    secondary={'text':'Hello hello'}
    review=aligned('Goodbye.', ['Goodbye'])
    text,flags,chosen,selection=select_checked(primary,secondary,review,secondary)
    assert text=='Hello, hello!' and selection['selected']=='qwen'


def test_review_must_not_win_only_by_omitting_an_english_example():
    p=aligned('请注意。He goes to a private school.继续。',list('请注意')+['He','goes','to','a','private','school']+list('继续'))
    s={'text':'请注意继续'}
    r=aligned('请注意继续。',list('请注意继续'))
    # This is mixed original speech, not an English translation of Chinese.
    s['text']='请注意 He goes 继续'
    text,flags,chosen,selection=select_checked(p,s,r,s)
    assert 'private school' in text
