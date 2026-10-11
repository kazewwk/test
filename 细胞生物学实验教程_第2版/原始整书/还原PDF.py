import hashlib,json
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
