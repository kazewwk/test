(()=>{
function add(ch,front,sources,parts,theme,task,imgs=[]){
 sources=[...new Set(sources.concat(parts.flatMap(p=>p.s||[])))]; const cs=load("cards"+ch),ks=load("knowledge"+ch),hs=load("handling"+ch);
 const id="RB-CN"+String(ch).padStart(2,"0")+"-"+String(cs.length+1).padStart(4,"0");
 const answer=[],rubric=[],kids=[];
 for(let i=0;i<parts.length;i++){
  const p=parts[i];if(!p.v)throw Error("Explicit semantic verification required");
  const kid="KP-CN"+String(ch).padStart(2,"0")+"-"+String(Math.max(0,...ks.map(k=>Number(k.knowledge_id.split("-").at(-1))))+1).padStart(4,"0");
  answer.push({anchor:"A"+(i+1),text:p.a});rubric.push({anchor:"R"+(i+1),text:p.r});kids.push(kid);
  ks.push({knowledge_id:kid,knowledge:p.k,source_units:p.s||sources,card_id:id,answer_anchor:"A"+(i+1),rubric_anchor:"R"+(i+1),explicit_recall:true,status:"covered",verified:true,verification_note:p.v});
 }
 cs.push({id,type:"Basic",chapter:ch,front,answer,rubric,detail:"",basis:"教材直接支持",source_units:sources,knowledge_ids:kids,images:imgs,tags:["学科::细胞生物学","章节::第"+String(ch).padStart(2,"0")+"章_"+(ch===2?"细胞生物学研究方法":"细胞质膜"),"主题::"+theme,"任务::"+task,"卡片编号::"+id]});
 for(const u of sources){const h=hs[u]||{status:"mapped",cards:[],reason:""};h.status="mapped";if(!h.cards.includes(id))h.cards.push(id);h.reason="该段科学知识已纳入所列完整问答及逐点必答内容；对应知识点见 knowledge.json。";hs[u]=h;}
 store("cards"+ch,cs);store("knowledge"+ch,ks);store("handling"+ch,hs);return id;
}
function ids(block,...nums){return nums.map(n=>block+"-P"+String(n).padStart(3,"0"));}
function figure(ch,unit,note){
 const im=load("img:"+unit);if(!im?.sha)throw Error("Original image must be fetched and viewed");
 const fs=load("figures"+ch);let f=fs.find(x=>x.git_blob_sha===im.sha);
 if(f){if(!f.source_units.includes(unit))f.source_units.push(unit);return f.figure_id;}
 const id="FIG-CN"+String(ch).padStart(2,"0")+"-"+String(fs.length+1).padStart(5,"0");
 fs.push({figure_id:id,original_repo_path:im.path,git_blob_sha:im.sha,filename:"cell_full_CN"+String(ch).padStart(2,"0")+"_"+String(fs.length+1).padStart(5,"0")+"_"+im.sha.slice(0,10)+".jpg",source_units:[unit],reviewed:true,review_notes:note,original:true});
 store("figures"+ch,fs);return id;
}
function mark(ch,unitIds){
 const us=load("units"+ch),hs=load("handling"+ch);
 for(const id of unitIds){const u=us.find(x=>x.id===id);u.reading_status="actually_read";
  if(u.kind==="heading"&&!hs[id])hs[id]={status:"no_new_knowledge",cards:[],reason:"本段仅含章节/分类标题，具体科学内容在随后正文问答中覆盖。"};
 }
 store("units"+ch,us);store("handling"+ch,hs);
}
;return {add,ids,figure,mark};})()