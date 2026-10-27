"""Check visible-color evidence for model-reported handwritten checkmarks.

This does not infer teaching meaning or erase model hypotheses. Unsupported
claims remain in raw output and are explicitly routed to the review queue.
"""
import difflib
import re
import cv2
import numpy as np


def norm(s):return ''.join(c.lower() for c in s if c.isalnum())


def ground_annotations(image, annotations, ocr, document_blocks=()):
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    blue=cv2.inRange(hsv,np.array([85,50,35]),np.array([135,255,255]))
    height,width=image.shape[:2]
    contours,hierarchy=cv2.findContours(blue,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    rings=[]
    if hierarchy is not None:
        for idx,contour in enumerate(contours):
            child=int(hierarchy[0][idx][2])
            if int(hierarchy[0][idx][3])!=-1 or child<0:continue
            area=cv2.contourArea(contour)
            if area<500 or cv2.contourArea(contours[child])<area*.35:continue
            rings.append(contour)
    checked=[];uncertain=[]
    for annotation in annotations:
        item=dict(annotation)
        typ=str(item.get('type','')).lower();color=str(item.get('color','')).lower()
        target=str(item.get('target',''))
        if ('circle' in typ or '圈' in typ) and ('blue' in color or '蓝' in color):
            grounded=[]
            for ring in rings:
                texts=[]
                for block in document_blocks:
                    content=block.get('block_content','').strip();bbox=block.get('block_bbox',[])
                    if not content or len(bbox)!=4:continue
                    x1,y1,x2,y2=bbox
                    center=((x1+x2)/2,(y1+y2)/2)
                    rx,ry,rw,rh=cv2.boundingRect(ring)
                    intersection=max(0,min(x2,rx+rw)-max(x1,rx))*max(0,min(y2,ry+rh)-max(y1,ry))
                    coverage=intersection/max(1,(x2-x1)*(y2-y1))
                    inside=cv2.pointPolygonTest(ring,(float(center[0]),float(center[1])),False)>=0
                    if inside and coverage>=.65:texts.append(content)
                if texts:grounded.append((' '.join(texts),cv2.boundingRect(ring)))
            if grounded:
                selected=max(grounded,key=lambda g:difflib.SequenceMatcher(None,norm(g[0]),norm(target),autojunk=False).ratio())
                similarity=difflib.SequenceMatcher(None,norm(selected[0]),norm(target),autojunk=False).ratio()
                if similarity>=.35 or len(grounded)==1:
                    item.update(target_original_model=target,target=selected[0],grounding='closed_blue_region_and_document_ocr',
                                enclosure_bbox=list(selected[1]))
                    checked.append(item);continue
            item['grounding']='circle_target_requires_review';item['requires_review']=True
            uncertain.append('圈选的精确对象尚需核对：'+target)
            checked.append(item);continue
        if ('underline' in typ or '下划线' in typ) and ('blue' in color or '蓝' in color):
            candidates=[(1.0 if len(norm(target))>=3 and norm(target) in norm(text) else difflib.SequenceMatcher(None,norm(text),norm(target),autojunk=False).ratio(),box,text)
                        for text,box in zip(ocr.get('texts',[]),ocr.get('boxes',[]))]
            if not candidates or max(c[0] for c in candidates)<.65:
                item.update(grounding='underline_location_unresolved',requires_review=True)
                uncertain.append('下划线的对应文字位置未确认：'+target)
            else:
                _,box,text=max(candidates,key=lambda c:c[0]);points=np.asarray(box).reshape(-1,2)
                x1,y1=points.min(axis=0);x2,y2=points.max(axis=0)
                full,part=norm(text),norm(target)
                if part and part in full and len(part)<len(full):
                    begin=full.index(part);span=x2-x1
                    x1,x2=x1+span*begin/len(full),x1+span*(begin+len(part))/len(full)
                xa=max(0,int(x1)-5);xb=min(width,int(x2)+5)
                ya=max(0,int(y1+(y2-y1)*.6));yb=min(height,int(y2+max(10,(y2-y1)*.6)))
                line_mask=blue.copy()
                if rings:cv2.drawContours(line_mask,rings,-1,0,cv2.FILLED)
                count=int(np.count_nonzero(line_mask[ya:yb,xa:xb]))
                item.update(grounding='underline_color_evidence_present' if count>=8 else 'underline_color_evidence_not_found',
                            tested_region=[xa,ya,xb,yb],matching_color_pixels=count)
                if count<8:
                    item['requires_review']=True
                    uncertain.append('未在对应文字下方检出足够蓝色下划线像素：'+target)
            checked.append(item);continue
        if not (('check' in typ or '勾' in typ or '钩' in typ) and ('blue' in color or '蓝' in color)):
            item['grounding']='not_automatically_verified';checked.append(item);continue
        candidates=[]
        for text,box in zip(ocr.get('texts',[]),ocr.get('boxes',[])):
            score=difflib.SequenceMatcher(None,norm(text),norm(target),autojunk=False).ratio()
            candidates.append((score,box,text))
        if not candidates or max(x[0] for x in candidates)<.65:
            item['grounding']='target_ocr_location_unresolved';checked.append(item)
            uncertain.append('标注对象定位未确认：'+target);continue
        score,box,text=max(candidates,key=lambda x:x[0])
        points=np.asarray(box).reshape(-1,2)
        x1,y1=points.min(axis=0);x2,y2=points.max(axis=0)
        # The common right-hand margin placement is a testable geometric cue.
        # A failure is uncertainty, not proof that a faint/occluded mark is absent.
        pad=max(8,int((y2-y1)*.45))
        xa=max(0,int(x2-12));xb=min(width,int(x2+width*.12))
        ya=max(0,int(y1-pad));yb=min(height,int(y2+pad))
        count=int(np.count_nonzero(blue[ya:yb,xa:xb]))
        item.update(grounding='color_evidence_present' if count>=8 else 'color_evidence_not_found',
                    tested_region=[xa,ya,xb,yb],matching_color_pixels=count)
        if count<8:
            item['requires_review']=True
            uncertain.append('未在对应文字旁检出足够蓝色勾号像素，请核对原图：'+target)
        checked.append(item)
    for item in checked:
        if item.get('meaning'):
            item['meaning_original_model']=item['meaning']
        if item.get('requires_review'):
            item['meaning']='[无法确认：标注位置、范围或形状需要核对原图]'
        else:
            item['meaning']='画面中的可见标注，位置与对象见对应字段；不据此推断学习状态或教学意图。'
    return checked,uncertain
