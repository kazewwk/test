import hashlib,json,pathlib,shutil
root=pathlib.Path(__file__).resolve().parents[1];books=json.loads((root/'work/chapters.json').read_text());manifest=json.loads((root/'work/source-manifest.json').read_text())
for book,spec in zip(books,manifest['books']):
 folder=root/'output'/book['title']/'原始整书';folder.mkdir(parents=True,exist_ok=True)
 source=root/book['source'];parts=[]
 with source.open('rb') as stream:
  while data:=stream.read(95_000_000):
   dest=folder/f"original.pdf.part{len(parts)+1:03}";dest.write_bytes(data);parts.append({'path':dest.name,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 assert hashlib.file_digest(source.open('rb'),'sha256').hexdigest()==spec['sha256']
 (folder/'parts.json').write_text(json.dumps({'output':spec['original_name'],'size':spec['size'],'sha256':spec['sha256'],'parts':parts},ensure_ascii=False,indent=2))
 (folder/'还原PDF.py').write_text('''import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
spec=json.loads((root/'parts.json').read_text())
target=root/spec['output'];temp=target.with_name(target.name+'.tmp');digest=hashlib.sha256();size=0
with temp.open('wb') as out:
 for part in spec['parts']:
  data=(root/part['path']).read_bytes()
  assert len(data)==part['size'] and hashlib.sha256(data).hexdigest()==part['sha256']
  out.write(data);digest.update(data);size+=len(data)
assert size==spec['size'] and digest.hexdigest()==spec['sha256']
temp.replace(target);print(target)
''')
 print('SOURCE PRESERVED',book['title'],spec['sha256'],flush=True)
