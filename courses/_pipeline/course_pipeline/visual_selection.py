"""Select general-vision reviews for complex content and unresolved OCR, not every frame."""
from pathlib import Path
import hashlib,json
import cv2,numpy as np
from .common import load,write_json


def box_xyxy(box):
    a=np.asarray(box).reshape(-1,2);lo=a.min(axis=0);hi=a.max(axis=0)
    return [float(lo[0]),float(lo[1]),float(hi[0]),float(hi[1])]


def select_frames(root,frames):
    root=Path(root);selected=[];decisions=[];previous_ink=None;previous_context=None
    for frame in frames:
        stem=Path(frame['path']).stem;ocr=load(root/'evidence/ocr'/(stem+'.json'))
        marker=root/'evidence/document'/stem/'complete.json';doc=load(marker) if marker.exists() else {}
        w=frame['width'];h=frame['height'];blocks=doc.get('blocks',[]);reasons=[]
        complex_blocks=[b for b in blocks if b.get('block_label') in ('table','chart','formula','display_formula','formula_number')]
        if complex_blocks:reasons.append('structured_table_chart_or_formula')
        meaningful_images=[];presenters=[]
        for b in blocks:
            if b.get('block_label') not in ('image','chart'):continue
            box=b.get('block_bbox',[])
            if len(box)!=4:continue
            x1,y1,x2,y2=box;area=max(0,x2-x1)*max(0,y2-y1)
            # This is the observed presentation layout, not facial identification.
            presenter=x1>w*.55 and y1>h*.2 and x2-x1>w*.2 and y2-y1>h*.45
            if presenter:presenters.append(box)
            elif area>w*h*.02 and not b.get('block_content','').strip():meaningful_images.append(box)
        if meaningful_images:reasons.append('nontext_instructional_image_or_demonstration')
        uncertain_text=[]
        for text,score,box in zip(ocr.get('texts',[]),ocr.get('scores',[]),ocr.get('boxes',[])):
            if score>=.8 or not str(text).strip():continue
            x1,y1,x2,y2=box_xyxy(box)
            in_presenter=any(x1>=a and y1>=b and x2<=c and y2<=d for a,b,c,d in presenters)
            branding=any(s in str(text).lower() for s in ('bilibili','胶学'))
            if not in_presenter and not branding:uncertain_text.append(str(text))
        if uncertain_text:reasons.append('low_confidence_instructional_ocr')
        if any(r.get('status')=='unresolved' for r in doc.get('region_repairs',[])):reasons.append('unresolved_document_region')
        pixels=cv2.imread(str(root/frame['path']))
        if pixels is None:raise ValueError('Cannot decode source frame')
        hsv=cv2.cvtColor(pixels,cv2.COLOR_BGR2HSV)
        blue=cv2.inRange(hsv,np.array([85,100,70]),np.array([135,255,255]))
        orange=cv2.inRange(hsv,np.array([10,100,220]),np.array([38,255,255]))
        ink=cv2.bitwise_or(blue,orange)
        for x1,y1,x2,y2 in presenters:ink[int(y1):int(y2),int(x1):int(x2)]=0
        context=[];dilated=cv2.dilate(ink,np.ones((31,31),np.uint8))
        for text,box in zip(ocr.get('texts',[]),ocr.get('boxes',[])):
            x1,y1,x2,y2=map(int,box_xyxy(box))
            if np.any(dilated[max(0,y1):min(h,y2),max(0,x1):min(w,x2)]):context.append(text)
        ink_hash=hashlib.sha256(ink.tobytes()).hexdigest();context_hash=hashlib.sha256(json.dumps(context,ensure_ascii=False).encode()).hexdigest()
        if np.count_nonzero(ink)>=24 and (ink_hash!=previous_ink or context_hash!=previous_context):reasons.append('visible_annotation_change_or_changed_target_text')
        previous_ink=ink_hash;previous_context=context_hash
        decision={**frame,'api_selection_reason':reasons,'ocr_uncertainties':uncertain_text,'selected':bool(reasons)}
        decisions.append(decision)
        if reasons:selected.append(decision)
    write_json(root/'visual_selection.json',{'policy':'complex-or-uncertain-v1','selected':len(selected),'total_keyframes':len(frames),'frames':decisions,
        'limitations':['Small or low-contrast annotations may require source-image review','The general visual model is not used to summarize or rewrite speech']})
    return selected,decisions


def not_requested_records(root,decisions):
    root=Path(root)
    for frame in decisions:
        if frame['selected']:continue
        path=root/'evidence/visual'/(Path(frame['path']).stem+'.json')
        write_json(path,{'path':frame['path'],'time':frame['time'],'image_sha256':frame['sha256'],
            'model':None,'status':'not_requested','selection_reason':'No complex visual content or unresolved instructional OCR detected',
            'raw':'','parsed':{'kind':'other','description':'本帧未追加通用视觉模型描述；原始截图、OCR及文档解析已保留。',
                              'annotations':[],'uncertain':[],'ocr_missing_text':[],'ocr_disagreements':[]},
            'verification':'selection_decision_not_a_model_inference'})
