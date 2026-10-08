#!/usr/bin/env python3
"""Restore byte-exact original PDF and any oversized split artifacts."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / 'original_pdf_parts/parts.json').read_text())
destination = root / 'restored' / manifest['output']
destination.parent.mkdir(parents=True, exist_ok=True)
digest = hashlib.sha256()
with destination.open('wb') as output:
    for part in manifest['parts']:
        data = (root / 'original_pdf_parts' / part['path']).read_bytes()
        assert len(data) == part['size']
        assert hashlib.sha256(data).hexdigest() == part['sha256']
        digest.update(data)
        output.write(data)
assert destination.stat().st_size == manifest['size']
assert digest.hexdigest() == manifest['sha256']
print(f'Verified original PDF: {destination}')

split_manifest = root / 'split_files.json'
if split_manifest.exists():
    for item in json.loads(split_manifest.read_text()):
        output_path = root / item['path']
        checksum = hashlib.sha256()
        with output_path.open('wb') as output:
            for part in item['parts']:
                data = (root / part['path']).read_bytes()
                assert hashlib.sha256(data).hexdigest() == part['sha256']
                checksum.update(data)
                output.write(data)
        assert checksum.hexdigest() == item['sha256']
        assert output_path.stat().st_size == item['size']
        print(f'Verified split file: {output_path}')
