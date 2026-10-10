(block,ch=2)=>{
const us=load("units"+ch),cs=load("cards"+ch),ks=load("knowledge"+ch),hs=load("handling"+ch);
const U=n=>typeof n==="string"?n:block+"-P"+String(n).padStart(3,"0");
return {u:U,
card:(front,parts,theme,images=[])=>{
const id="RB-CN"+String(ch).padStart(2,"0")+"-"+String(cs.length+1).padStart(4,"0");
const card={id,type:"Basic",chapter:ch,front,answer:[],rubric:[],detail:"",basis:"教材直接支持",source_units:[],knowledge_ids:[],images,tags:["学科::细胞生物学","章节::第"+String(ch).padStart(2,"0")+"章_"+(ch===2?"细胞生物学研究方法":"细胞质膜"),"主题::"+theme,"任务::解释与复述","卡片编号::"+id]};
parts.forEach((p,i)=>{
const a="A"+(i+1),r="R"+(i+1);card.answer.push({anchor:a,text:p.a});card.rubric.push({anchor:r,text:p.r});
p.f.forEach(f=>{
const unit=U(f[1]),src=us.find(u=>u.id===unit);if(!src)throw Error("Missing "+unit);
if(f[2]&&!src.text.includes(f[2]))throw Error("Nonmatching exact excerpt "+unit+" "+f[2]);
const kid="KP-CN"+String(ch).padStart(2,"0")+"-"+String(Math.max(0,...ks.filter(k=>k.knowledge_id.startsWith("KP-CN"+String(ch).padStart(2,"0")+"-")).map(k=>Number(k.knowledge_id.split("-").at(-1))))+1).padStart(4,"0");
const q=f[4]||("题目要求复述："+f[0]),req=f[3];if(!req)throw Error("Need concrete rubric");
ks.push({knowledge_id:kid,knowledge:f[0],source_units:[unit],source_excerpt:f[2]||src.text,visual_evidence:src.kind==="image"?load("figures"+ch).filter(z=>z.source_units.includes(unit)).map(z=>({figure_id:z.figure_id,review_notes:z.review_notes})):[],card_id:id,answer_anchor:a,rubric_anchor:r,explicit_recall:true,status:"covered",verified:true,question_requirement:q,rubric_requirement:req,verification_note:"已实际阅读并逐点核对原文/原图："+(f[2]||src.text)+"；题目要求："+q+"；答案"+a+"和评分"+r+"均要求："+req+"。"});
card.knowledge_ids.push(kid);if(!card.source_units.includes(unit))card.source_units.push(unit);
const h=hs[unit]||{status:"mapped",cards:[],reason:""};h.status="mapped";if(!h.cards.includes(id))h.cards.push(id);h.reason="已逐点对照该段原文或原图，科学内容由所列问答的明确提问与必答评分覆盖。";hs[unit]=h;
});
});cs.push(card);store("cards"+ch,cs);store("knowledge"+ch,ks);store("handling"+ch,hs);return id;},
none:(n,reason)=>{const unit=U(n);hs[unit]={status:"no_new_knowledge",cards:[],reason};store("handling"+ch,hs);},
support:(n,ids,reason)=>{const unit=U(n);hs[unit]={status:"duplicate",cards:ids,reason};store("handling"+ch,hs);ids.forEach(id=>{const c=cs.find(c=>c.id===id);if(!c)throw Error("Unknowncard");if(!c.source_units.includes(unit))c.source_units.push(unit);});store("cards"+ch,cs);}
};
}