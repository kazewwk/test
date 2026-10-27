"""Use MinerU for structural content and concrete OCR disagreements."""
from pathlib import Path
from .common import load,write_json
from .fusion import normalized


def select_mineru_frames(root,frames):
    root=Path(root);selected=[];decisions=[]
    for frame in frames:
        stem=Path(frame['path']).stem
        doc=load(root/'evidence/document'/stem/'complete.json');ocr=load(root/'evidence/ocr'/(stem+'.json'))
        reasons=[];blocks=doc.get('blocks',[])
        if any(b.get('block_label') in ('table','chart','formula','display_formula') for b in blocks):reasons.append('complex_structure')
        if any(r.get('status')=='unresolved' for r in doc.get('region_repairs',[])):reasons.append('unresolved_document_region')
        text=normalized(' '.join(b.get('block_content','') for b in blocks))
        missing=[t for t,s in zip(ocr.get('texts',[]),ocr.get('scores',[]))
                 if s>=.9 and len(normalized(t))>=4 and normalized(t) not in text and not any(x in t.lower() for x in ['bilibili','胶学'])]
        if missing:reasons.append('high_confidence_ocr_not_recovered_by_document_model')
        if reasons:selected.append(frame)
        decisions.append({'path':frame['path'],'time':frame['time'],'selected':bool(reasons),'reasons':reasons,'disputed_text':missing})
    write_json(root/'mineru_selection.json',{'policy':'complex-structure-or-unresolved-text-v1','selected':len(selected),'keyframes':len(frames),'frames':decisions})
    return selected
