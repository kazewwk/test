(async function restoreCheckpoint(workingHead, workingTree) {
if(!workingHead||!workingTree) throw Error("Pass final branch HEAD and tree from handoff delivery; do not reset branch to data snapshot");
const repo="kazewwk/test", dir="anki/SHU_Cell_Biology_Full_20261010/input/ch02_ch03/", snapshot="a11ddbacd466a43d9901757e39534b988daf19b4";
const blobs={"cards.json":"f684dcc82cbf894172697d9ed214ec53f2de35d1","knowledge.json":"e145c219dc05fb9e536b271e5a37a31088dc42be","read_units.json":"a8c36e95794fe54046c4051cd61efdca15f39830","handling.json":"ceb77488174f336fb0c86003a674b8767fede26b","figures.json":"6af79ba43ea34c8b826ac443dfe04b2bd58b8a9d","gaps.json":"0c65d484624e9f3547d3f14234264789f1d726da","progress.json":"ea2baa0b71b0ed801d193f23fcc718a38f03b7fe","source_manifest.json":"5aa167509f4dffa72cd7fd9aa93538b18e2dfb6d","author_helpers.js":"794549fcc516024930ac865fe11de565d4efb775","english_author_helper.js":"e6adb65242705c6bd37de1aaa6ea70c6ff8758f6","checkpoint_helper.js":"f3b1d748adaf6a6bcd961c093d1ad7fc5c271c66"};
const readBlob=async name=>{const r=await tools.mcp__codex_apps__github_fetch_blob({repository_full_name:repo,blob_sha:blobs[name]});if(r.isError||!r.structuredContent?.content)throw Error("Unreadable "+name);return r.structuredContent.content;};
const names=["cards.json","knowledge.json","read_units.json","handling.json","figures.json","gaps.json","source_manifest.json","progress.json","author_helpers.js","english_author_helper.js","checkpoint_helper.js"];
const rs=await Promise.allSettled(names.map(async n=>[n,await readBlob(n)])); const data={};
for(const r of rs){if(r.status!=="fulfilled")throw r.reason; const [n,v]=r.value;data[n]=n.endsWith(".json")?JSON.parse(v):v;}
const units=data["read_units.json"], byChapter=u=>u.file.startsWith("03_")?3:2;
for(const ch of [2,3]) {
store("units"+ch,units.filter(u=>byChapter(u)===ch));
store("cards"+ch,data["cards.json"].cards.filter(c=>c.chapter===ch));
store("knowledge"+ch,data["knowledge.json"].filter(k=>k.knowledge_id.startsWith("KP-CN"+String(ch).padStart(2,"0")+"-")));
store("handling"+ch,Object.fromEntries(Object.entries(data["handling.json"]).filter(([id])=>units.some(u=>u.id===id&&byChapter(u)===ch))));
store("figures"+ch,data["figures.json"].filter(f=>f.figure_id.startsWith("FIG-CN"+String(ch).padStart(2,"0")+"-")));
store("gaps"+ch,data["gaps.json"].filter(g=>g.gap_id.includes("CN"+String(ch).padStart(2,"0"))));
}
store("author_helper",data["author_helpers.js"]);store("english_author_helper",data["english_author_helper.js"]);store("checkpoint_helper",data["checkpoint_helper.js"]);
const vh=await tools.mcp__codex_apps__github_fetch_file({repository_full_name:repo,path:dir+"view_helper.js",ref:workingHead,encoding:"utf-8"});if(vh.isError||!vh.structuredContent?.content)throw Error("Missing persistent view helper");store("view_helper",vh.structuredContent.content);
store("head",workingHead);store("tree",workingTree);
store("source2",{sha:"e32625b2044eab7e811965d69a4044d8ecfe145c"});store("source3",{sha:"f6fe1ff37c7bfff71f4e22acf85ed9f3d729bd0e"});
store("suppsource2",{sha:"78fdc3c4b687dc739d9d39c40c0d49cb65105cba",file:"02_细胞生物学研究方法/英文习题与参考文献.md"});store("suppsource3",{sha:"dcd0aa162f77aee4c7f90618ce48c174986a687f",file:"03_细胞质膜/英文习题与参考文献.md"});
store("extra_sources",data["source_manifest.json"].extra_sources);store("pdf_reviews",data["source_manifest.json"].original_pdf_reviews);store("progress",data["progress.json"]);
store("lastEntries",Object.entries(blobs).map(([f,sha])=>({path:dir+f,mode:"100644",type:"blob",sha})));
return {restored_from:snapshot,cards:data["cards.json"].cards.length,units:units.length,actually_read:units.filter(u=>u.reading_status==="actually_read").length,note:"Image caches may be refetched with persistent view_helper; do not infer review of new images from filename/hash."};
})