import concurrent.futures,hashlib,io,json,pathlib,urllib.parse,urllib.request,zipfile
root=pathlib.Path('/workspace')
base='https://raw.githubusercontent.com/kazewwk/test/mineru-local-wang-jinfa-20261010/'
def get(path):
 with urllib.request.urlopen(base+urllib.parse.quote(path,safe='/'),timeout=300) as r:return r.read()
def restore(pair):
 key,spec=pair
 data=b''.join(get(p['path']) for p in spec['parts'])
 assert len(data)==spec['size'] and hashlib.sha256(data).hexdigest()==spec['sha256']
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  assert z.testzip() is None
  for member in z.infolist():
   dest=root/'output'/member.filename
   assert dest.resolve().is_relative_to((root/'output').resolve())
   if not member.is_dir():dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(member))
 print('RESTORED',key,flush=True)
spec=json.loads((root/'work/source-manifest.json').read_text())
for bid,book in enumerate(spec['books']):
 dest=root/'sources'/f'book{bid}.pdf'
 if not dest.exists():
  with dest.with_suffix('.tmp').open('wb') as f:
   for part in book['files']:
    data=get('王金发细胞/'+part['path'])
    assert len(data)==part['size'] and hashlib.sha256(data).hexdigest()==part['sha256'];f.write(data)
  dest.with_suffix('.tmp').rename(dest)
 assert dest.stat().st_size==book['size'] and hashlib.file_digest(dest.open('rb'),'sha256').hexdigest()==book['sha256']
 print('SOURCE VERIFIED',bid,flush=True)
status=json.loads(get('.local-mineru-checkpoints-20261011/status.json'))
(root/'work/restored-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2))
(root/'work/durable-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(restore,status['checkpoints'].items()))
import pymupdf
(root/'work/inputs').mkdir(exist_ok=True);(root/'work/states').mkdir(exist_ok=True)
books=json.loads((root/'work/chapters.json').read_text())
for book in books:
 with pymupdf.open(root/book['source']) as src:
  assert len(src)==book['page_count']
  pages=[]
  for chapter in book['chapters']:
   pages.extend(range(chapter['start'],chapter['end']+1))
   dest=root/'work/inputs'/f"book{book['id']}-{chapter['number']:02}.pdf"
   with pymupdf.open() as pdf:
    pdf.insert_pdf(src,from_page=chapter['start']-1,to_page=chapter['end']-1)
    pdf.save(dest,garbage=3,deflate=True)
  assert pages==list(range(1,len(src)+1))
 print('CHAPTERS PREPARED',book['id'],flush=True)
