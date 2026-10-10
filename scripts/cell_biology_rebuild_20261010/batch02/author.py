from pathlib import Path
import json
ROOT=Path('/tmp/biology_rebuild')
UNITS={u['unit_id']:u for u in json.loads((ROOT/'source_units.json').read_text())}
CARDS=[];KNOWLEDGE=[];GAPS=[];HANDLING={};READ=[]
_knowledge_sequence=0
def next_kid():
    global _knowledge_sequence
    _knowledge_sequence+=1
    return f'KP-CN01-{_knowledge_sequence:04d}'
def uid(value):
    if value.startswith('CN') or value.startswith('EN'): return value
    section,num=value.split('.')
    return f'CN01-S{int(section):02d}-P{int(num):03d}'
def N(q,parts,detail='',images=(),kind='概念解释',basis='教材直接支持'):
    ident=f'RB-CN01-{len(CARDS)+1:04d}';answer=[];rubric=[];kids=[];sources=[]
    for i,(text,score,refs,facts) in enumerate(parts,1):
        answer.append({'anchor':f'A{i}','text':text});rubric.append({'anchor':f'R{i}','text':score})
        refs=[uid(x) for x in refs.split()]
        for ref in refs:
            assert ref in UNITS,ref
            if ref not in sources:sources.append(ref)
            HANDLING.setdefault(ref,{'status':'mapped','cards':[],'reason':''})['cards'].append(ident)
        # Facts are independently named by the author; the answer and rubric anchors locate each one.
        for fact in facts.split(';'):
            if not fact.strip():continue
            kid=next_kid();kids.append(kid)
            KNOWLEDGE.append({'knowledge_id':kid,'knowledge':fact,'source_units':refs,'card_id':ident,'answer_anchor':f'A{i}','rubric_anchor':f'R{i}','explicit_recall':True,'status':'covered','question':q})
    CARDS.append({'id':ident,'front':q,'answer':answer,'rubric':rubric,'detail':detail,'source_units':sources,'knowledge_ids':kids,'images':[{'figure_id':f,'side':s,'annotation':a} for f,s,a in images],'kind':kind,'basis':basis,'type':'Basic','chapter':1,'tags':['细胞生物学','第01章_绪论',kind]})
    return ident
def P(text,score,refs,facts):return (text,score,refs,facts)
def gap(ref,label,reason):
    ref=uid(ref);GAPS.append({'source_unit':ref,'knowledge':label,'status':'unresolved','reason':reason});HANDLING.setdefault(ref,{'status':'partial_pending','cards':[],'reason':''});HANDLING[ref]['status']='partial_pending';HANDLING[ref]['reason']+=' '+reason
    KNOWLEDGE.append({'knowledge_id':next_kid(),'knowledge':label,'source_units':[ref],'card_id':'','answer_anchor':'','rubric_anchor':'','explicit_recall':False,'status':'unresolved'})
def omit(ref,reason,card=''):
    ref=uid(ref);HANDLING[ref]={'status':'no_new_knowledge','cards':[card] if card else[],'reason':reason}
def save():
    (ROOT/'cards_ch01.json').write_text(json.dumps({'cards':CARDS},ensure_ascii=False,indent=2)+'\n')
    (ROOT/'knowledge_ch01.json').write_text(json.dumps(KNOWLEDGE,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'gaps_ch01.json').write_text(json.dumps(GAPS,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'handling_ch01.json').write_text(json.dumps(HANDLING,ensure_ascii=False,indent=2)+'\n')
    print({'notes':len(CARDS),'knowledge_points':len(KNOWLEDGE),'unresolved':len(GAPS)})
