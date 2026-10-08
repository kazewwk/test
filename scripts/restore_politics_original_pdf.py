#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
def main():
    root=Path(__file__).resolve().parent.parent;parts=root/'original_pdf'
    manifest=json.loads((parts/'parts.json').read_text());target=root/manifest['output']
    digest=hashlib.sha256();size=0
    with target.open('wb') as out:
        for entry in manifest['parts']:
            data=(parts/entry['path']).read_bytes()
            assert len(data)==entry['size'] and hashlib.sha256(data).hexdigest()==entry['sha256']
            out.write(data);digest.update(data);size+=len(data)
    assert size==manifest['size'] and digest.hexdigest()==manifest['sha256']
    print('Restored and verified:',target)
if __name__=='__main__':main()
