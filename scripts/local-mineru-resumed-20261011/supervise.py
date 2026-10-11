import json,os,pathlib,shutil,subprocess,sys,time
ROOT=pathlib.Path('/workspace');os.chdir(ROOT);PYTHON=str(ROOT/'mineru-venv/bin/python');books=json.loads((ROOT/'work/chapters.json').read_text());initial_pid=int(sys.argv[1])
def complete():return all((ROOT/'work/states'/f"book{b['id']}-{c['number']:02}.done.json").exists() for b in books for c in b['chapters'])
def alive(pid):
 try:
  fields=pathlib.Path(f'/proc/{pid}/stat').read_text().split();return fields[2]!='Z'
 except FileNotFoundError:return False
def progress():
 counts=[0,0]
 for b in books:
  for c in b['chapters']:
   folder=ROOT/'output'/b['title']/c['name']/'解析批次'
   for p in folder.glob('*/complete.json'):
    status=json.loads(p.read_text());a,z=status['chapter_pages'];counts[b['id']]+=z-a+1
 return counts
last=None
for attempt in range(5):
 if complete():break
 worker=None
 if attempt==0 and alive(initial_pid):pid=initial_pid
 else:
  for lock in (ROOT/'work/states').glob('*.lock'):shutil.rmtree(lock)
  stream=(ROOT/'logs/parse.log').open('a');worker=subprocess.Popen([PYTHON,'-u',str(ROOT/'work/parse_books.py'),'--worker','0'],stdout=stream,stderr=subprocess.STDOUT,env=os.environ|{'PYTHONFAULTHANDLER':'1'});pid=worker.pid
 while alive(pid):
  count=progress()
  if count!=last:print('PROGRESS',count,'/',[b['page_count'] for b in books],flush=True);last=count
  time.sleep(30)
 if worker:worker.wait();stream.close()
 if complete():break
 print('PARSER EXITED; RESUMING FROM CHECKPOINTS',attempt,flush=True)
 if attempt==4:raise RuntimeError('Local parsing failed after retries; durable checkpoints retained')
assert complete()
print('ALL CHAPTERS PARSED; ASSEMBLING',flush=True)
subprocess.run([PYTHON,str(ROOT/'work/preserve_sources.py')],check=True)
subprocess.run([PYTHON,'-u',str(ROOT/'work/finalize_books.py')],check=True)
print('PACKED; PUBLISHING REPOSITORY AND RELEASE',flush=True)
subprocess.run([PYTHON,'-u',str(ROOT/'work/publish_books.py')],check=True)
print('ALL COMPLETE',flush=True)
