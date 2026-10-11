import base64,hashlib,io,json,os,pathlib,subprocess,time,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO='kazewwk/test';BRANCH='mineru-local-wang-jinfa-20261010';PREFIX='.local-mineru-checkpoints-20261011';STATUS_REMOTE=PREFIX+'/status.json'
_state_file=ROOT/'work/durable-status.json'
STATE=json.loads((_state_file if _state_file.exists() else ROOT/'work/restored-status.json').read_text())
def api(path,data=None,method=None):
 args=['gh','api','repos/'+REPO+'/'+path]
 if method:args+=['--method',method]
 if data is not None:args+=['--input','-']
 for attempt in range(5):
  r=subprocess.run(args,input=None if data is None else json.dumps(data).encode(),capture_output=True)
  if r.returncode==0:return json.loads(r.stdout)
  if attempt==4:raise RuntimeError(r.stderr.decode())
  time.sleep(min(5*2**attempt,60))
def entry(path,data):
 obj=api('git/blobs',{'content':base64.b64encode(data).decode(),'encoding':'base64'})
 expected=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();assert obj['sha']==expected
 return {'path':path,'mode':'100644','type':'blob','sha':obj['sha']}
def commit(entries,message,branch=BRANCH):
 for attempt in range(5):
  parent=api('git/ref/heads/'+branch)['object']['sha'];tree=api('git/commits/'+parent)['tree']['sha']
  newtree=api('git/trees',{'base_tree':tree,'tree':entries})['sha']
  made=api('git/commits',{'message':message,'tree':newtree,'parents':[parent]})['sha']
  try:api('git/refs/heads/'+branch,{'sha':made,'force':False},'PATCH');return made
  except RuntimeError:
   if attempt==4:raise
   time.sleep(2)
def status_bytes():
 STATE['phase']='parsing_local';STATE['execution_note']='MinerU 4.0.12 CPU local ONNX + llama.cpp resumed; no remote parsing service.'
 STATE['updated_at']=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
 STATE['completed_pages']=[sum(x['pages'] for x in STATE['checkpoints'].values() if x['book_id']==bid) for bid in [0,1]]
 value=json.dumps(STATE,ensure_ascii=False,indent=2).encode();(ROOT/'work/durable-status.json').write_bytes(value);return value
def sync_batch(batch):
 key=batch.relative_to(ROOT/'output').as_posix()
 if key in STATE['checkpoints']:return
 marker=json.loads((batch/'complete.json').read_text());books=json.loads((ROOT/'work/chapters.json').read_text());bid=next(b['id'] for b in books if b['title']==marker['book'])
 packed=io.BytesIO()
 with zipfile.ZipFile(packed,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(batch.rglob('*')):
   if p.is_file():z.write(p,p.relative_to(ROOT/'output').as_posix())
 data=packed.getvalue();parts=[];entries=[]
 for offset in range(0,len(data),8_000_001):
  chunk=data[offset:offset+8_000_001];path=PREFIX+f'/book{bid}/'+marker['chapter'].split('_')[0]+'/'+batch.name+f'.zip.part{len(parts):03}'
  item=entry(path,chunk);entries.append(item);parts.append({'path':path,'sha':item['sha'],'size':len(chunk)})
 STATE['checkpoints'][key]={'book_id':bid,'pages':marker['chapter_pages'][1]-marker['chapter_pages'][0]+1,'source_pdf_pages':marker['source_pdf_pages'],'size':len(data),'sha256':hashlib.sha256(data).hexdigest(),'parts':parts}
 entries.append(entry(STATUS_REMOTE,status_bytes()));sha=commit(entries,'Save local MinerU checkpoint: '+key)
 print('DURABLE CHECKPOINT',key,sha,flush=True)
def update_status(phase='parsing',**extra):
 STATE.update(extra);return commit([entry(STATUS_REMOTE,status_bytes())],'Update local MinerU progress')
