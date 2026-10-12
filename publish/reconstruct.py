#!/usr/bin/env python3
"""Reconstruct a verified ZIP_STORED APKG; release writes require --publish-verified."""
import argparse, base64, concurrent.futures, gzip, hashlib, json, os, subprocess, time
import urllib.parse, urllib.request, zipfile
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for data in iter(lambda: f.read(1024 * 1024), b''):
            h.update(data)
    return h.hexdigest()


def require_hash(data, digest, label):
    if sha(data) != digest:
        raise ValueError('SHA256 mismatch: ' + label)
    return data


def join_payload(spec, root, cache):
    target = cache / spec['filename']
    with target.open('wb') as f:
        for part in spec['parts']:
            data = (root / part['path']).read_bytes()
            if len(data) != part['bytes']:
                raise ValueError('part length mismatch: ' + part['path'])
            f.write(require_hash(data, part['sha256'], part['path']))
    if target.stat().st_size != spec['bytes'] or file_sha(target) != spec['sha256']:
        raise ValueError('payload length/hash mismatch: ' + target.name)
    return target


def zip_info(values):
    i = zipfile.ZipInfo(values['filename'], tuple(values['date_time']))
    for name, value in values.items():
        if isinstance(value, dict) and set(value) == {'base64'}:
            value = base64.b64decode(value['base64'])
        elif name == 'date_time':
            value = tuple(value)
        if name in zipfile.ZipInfo.__slots__:
            setattr(i, name, value)
    return i


def load_manifest(path):
    path = Path(path)
    data = json.loads(path.read_text())
    if data.get('schema') == 'anki-github-manifest-index-v1':
        spec = data['payload']
        chunks = []
        for part in spec['parts']:
            block = (path.parent / part['path']).read_bytes()
            if len(block) != part['bytes']:
                raise ValueError('manifest part length mismatch')
            chunks.append(require_hash(block, part['sha256'], part['path']))
        packed = require_hash(b''.join(chunks), spec['sha256'], 'compressed manifest')
        if len(packed) != spec['bytes']:
            raise ValueError('compressed manifest length mismatch')
        raw = require_hash(gzip.decompress(packed), data['raw_sha256'], 'manifest JSON')
        if len(raw) != data['raw_bytes']:
            raise ValueError('manifest JSON length mismatch')
        data = json.loads(raw)
    if data.get('schema') != 'anki-github-repack-v1':
        raise ValueError('unsupported manifest schema')
    return data


def source_files(manifest, output, local_apkg=None, jobs=16):
    needed = {r['sha256']: r['storage']['path'] for r in manifest['apkg']['entries']
              if r['storage']['kind'] == 'source'}
    cache = output / 'source-entry-cache'
    cache.mkdir(parents=True, exist_ok=True)
    missing = {h for h in needed if not (cache / h).is_file() or file_sha(cache / h) != h}
    if local_apkg:
        # Local equality test uses original entry bytes, with no 3715-image downloads.
        with zipfile.ZipFile(local_apkg) as z:
            for i in z.infolist():
                if not missing:
                    break
                data = z.read(i)
                h = sha(data)
                if h in missing:
                    (cache / h).write_bytes(data)
                    missing.remove(h)
        if missing:
            raise ValueError(f'local entry-byte reference lacks {len(missing)} required hashes')
        return cache
    repo = manifest['source']['repository']
    snapshot = manifest['source']['snapshot']
    token = os.environ.get('GITHUB_TOKEN', '')

    def download(h):
        url = ('https://raw.githubusercontent.com/' + repo + '/' + snapshot + '/' +
               urllib.parse.quote(needed[h], safe='/'))
        headers = {'User-Agent': 'anki-verified-repack'}
        if token:
            headers['Authorization'] = 'Bearer ' + token
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=45) as r:
                    data = r.read()
                require_hash(data, h, needed[h])
                (cache / h).write_bytes(data)
                return h
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(attempt + 1)
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
        for count, _ in enumerate(pool.map(download, sorted(missing)), 1):
            if count % 250 == 0:
                print(f'Verified source media {count}/{len(missing)}', flush=True)
    return cache


def reconstruct(manifest, parts_dir, output, local_apkg=None, jobs=16):
    output.mkdir(parents=True, exist_ok=True)
    payload_cache = output / 'payload-cache'
    payload_cache.mkdir(exist_ok=True)
    custom_path = join_payload(manifest['payloads']['custom'], parts_dir, payload_cache)
    core_path = join_payload(manifest['payloads']['core'], parts_dir, payload_cache)
    source_cache = source_files(manifest, output, local_apkg, jobs)
    apkg = output / manifest['apkg']['filename']
    with zipfile.ZipFile(custom_path) as custom, zipfile.ZipFile(core_path) as core:
        with zipfile.ZipFile(apkg, 'w', compression=zipfile.ZIP_STORED) as z:
            for row in manifest['apkg']['entries']:
                storage = row['storage']
                if storage['kind'] == 'source':
                    data = (source_cache / row['sha256']).read_bytes()
                elif storage['kind'] == 'custom':
                    data = custom.read(storage['key'])
                elif storage['kind'] == 'core':
                    data = core.read(storage['key'])
                else:
                    raise ValueError('unknown storage kind')
                if len(data) != row['bytes']:
                    raise ValueError('entry length mismatch: ' + row['zip_info']['filename'])
                require_hash(data, row['sha256'], row['zip_info']['filename'])
                z.writestr(zip_info(row['zip_info']), data, compress_type=zipfile.ZIP_STORED)
            z.comment = base64.b64decode(manifest['apkg']['archive_comment_base64'])
        if apkg.stat().st_size != manifest['apkg']['bytes'] or file_sha(apkg) != manifest['apkg']['sha256']:
            raise ValueError('rebuilt APKG differs from original bytes; release is blocked')
        reports = []
        for row in manifest['reports']:
            data = require_hash(core.read(row['key']), row['sha256'], row['filename'])
            if len(data) != row['bytes']:
                raise ValueError('report length mismatch: ' + row['filename'])
            target = output / row['filename']
            target.write_bytes(data)
            reports.append(row['filename'])
    result = {'verified': True, 'apkg': apkg.name, 'sha256': file_sha(apkg),
              'bytes': apkg.stat().st_size, 'reports': reports,
              'source_mode': 'local-entry-bytes' if local_apkg else 'fixed-snapshot-download',
              'zip_entries': len(manifest['apkg']['entries'])}
    (output / 'verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def publish_verified(manifest, output):
    # Invoked by the dedicated branch workflow only after exact reconstruction.
    check = json.loads((output / 'verification.json').read_text())
    if not check.get('verified') or check['sha256'] != manifest['apkg']['sha256']:
        raise ValueError('verified reconstruction record is required')
    rows = [manifest['apkg']] + manifest['reports']
    assets = []
    for row in rows:
        target = output / row['filename']
        if target.stat().st_size != row['bytes'] or file_sha(target) != row['sha256']:
            raise ValueError('release asset is no longer verified: ' + target.name)
        assets.append(str(target))
    tag = manifest['release']['tag']
    existing = subprocess.run(['gh', 'release', 'view', tag], capture_output=True, text=True)
    if existing.returncode == 0:
        raise ValueError('release tag already exists; no old release will be overwritten')
    # The user may also attach release-notes.md as a verified asset.
    notes = output / '.github-release-body.md'
    supplied_notes = manifest['release'].get('notes')
    notes.write_text((supplied_notes if supplied_notes else
                     'APKG由冻结源媒体与交付payload重建，全部条目和最终包SHA256匹配本地导出。')
                     + '\n\n资产校验：\n'
                     + '\n'.join(f"- {r['filename']}: SHA256 `{r['sha256']}`" for r in rows) + '\n')
    cmd = ['gh', 'release', 'create', tag, *assets, '--target', os.environ['GITHUB_SHA'],
           '--title', manifest['release']['title'], '--notes-file', str(notes)]
    subprocess.run(cmd, check=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest', required=True)
    p.add_argument('--parts-dir')
    p.add_argument('--output', required=True)
    p.add_argument('--entry-bytes-from')
    p.add_argument('--jobs', type=int, default=16)
    p.add_argument('--publish-verified', action='store_true')
    a = p.parse_args()
    manifest = load_manifest(a.manifest)
    output = Path(a.output)
    if a.publish_verified:
        publish_verified(manifest, output)
    else:
        if not a.parts_dir:
            p.error('--parts-dir is required for reconstruction')
        print(json.dumps(reconstruct(manifest, Path(a.parts_dir), output, a.entry_bytes_from, a.jobs), ensure_ascii=False))

if __name__ == '__main__':
    main()
