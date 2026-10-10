async(block,nums,ch=2)=>{
const us=load("units"+ch),records=await Promise.allSettled(nums.map(async n=>{
const id=block+"-P"+String(n).padStart(3,"0"),u=us.find(u=>u.id===id);let z=load("img:"+id);
if(!z){const m=u.text.match(/!\[[^\]]*\]\(([^)]+)\)/);if(!m)throw Error("Noimage "+id);
const parts=("细胞生物学制卡/"+u.file.split("/").slice(0,-1).join("/")+"/"+m[1]).split("/"),stack=[];for(const p of parts){if(p==="..")stack.pop();else if(p&&p!==".")stack.push(p);}const path=stack.join("/");
const r=await tools.mcp__codex_apps__github_fetch_file({repository_full_name:"kazewwk/test",path,ref:"1cca4eb09d83ec631136f60e9dc7dd0e05df843c",encoding:"base64"});if(r.isError||!r.structuredContent?.content)throw Error(JSON.stringify({id,r}));z={...r.structuredContent,path,unit:id};store("img:"+id,z);}
return {id,z};}));
for(const r of records){if(r.status!=="fulfilled")throw Error(JSON.stringify(r));text({id:r.value.id,path:r.value.z.path});image("data:image/jpeg;base64,"+r.value.z.content.replace(/\s+/g,""),"original");}
}