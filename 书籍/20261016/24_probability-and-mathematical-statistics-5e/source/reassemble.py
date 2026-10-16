from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent
manifest=json.loads((base/'manifest.json').read_text())
dest=base/manifest['original_name']
with dest.open('wb') as out:
    for part in manifest['parts']:
        with (base/part['name']).open('rb') as src:
            while data:=src.read(2**20): out.write(data)
with dest.open('rb') as src: actual=hashlib.file_digest(src,'sha256').hexdigest()
assert actual==manifest['original_sha256'], 'SHA-256 mismatch'
print(dest.name, actual)
