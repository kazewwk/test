#!/usr/bin/env python3
"""Import the thirteen original book ZIPs and verify GitHub's SHA-256 digests."""
import concurrent.futures
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=json.loads((ROOT/'books/manifest.json').read_text())
REPOSITORY=os.environ.get('GITHUB_REPOSITORY',MANIFEST['repository'])
if REPOSITORY!='kazewwk/test' or MANIFEST['repository']!=REPOSITORY:
    raise SystemExit('This import is restricted to kazewwk/test.')
TOKEN=os.environ['GH_TOKEN']
TAG=MANIFEST['tag_name']
SOURCE=os.environ.get('BOOK_SOURCE_BASE_URL') or json.loads((ROOT/'books/import-source.json').read_text())['base_url']
parsed=urllib.parse.urlsplit(SOURCE)
if parsed.scheme!='https' or parsed.username or parsed.password or parsed.query or parsed.fragment:
    raise SystemExit('The transfer source must be a plain HTTPS base URL.')
SOURCE=SOURCE.rstrip('/')+'/'
DOWNLOADS=ROOT/'book-downloads'
DOWNLOADS.mkdir(exist_ok=True)
HEADERS={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json',
    'X-GitHub-Api-Version':'2026-03-10','User-Agent':'mineru-book-import'}

def api(method,path,body=None,missing_ok=False):
    data=json.dumps(body,ensure_ascii=False).encode() if body is not None else None
    request=urllib.request.Request('https://api.github.com'+path,data=data,method=method,
        headers={**HEADERS,**({'Content-Type':'application/json'} if data is not None else {})})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request,timeout=90) as response:
                raw=response.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as error:
            if error.code==404 and missing_ok:return None
            if error.code in (429,500,502,503,504) and attempt<3:
                time.sleep(min(30,3*2**attempt))
                continue
            raw=error.read()
            try:message=json.loads(raw).get('message','Request rejected')
            except ValueError:message='Request rejected'
            raise RuntimeError(f'GitHub {method} failed ({error.code}): {message}') from None

def progress(event,**fields):
    data=json.dumps({'event':event,**fields}).encode()
    request=urllib.request.Request(SOURCE+'progress',data=data,method='POST',headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(request,timeout=20):pass
    except (OSError,urllib.error.URLError):pass

def digest(path):
    value=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):value.update(block)
    return value.hexdigest()

prefix='/repos/'+REPOSITORY
release=api('GET',prefix+'/releases/tags/'+urllib.parse.quote(TAG),missing_ok=True)
if release is None:
    release=api('POST',prefix+'/releases',{
        'tag_name':TAG,'target_commitish':os.environ.get('GITHUB_SHA','main'),
        'name':'MinerU 书籍解析包：13 份（2026-10-07）',
        'body':(ROOT/'README.md').read_text(),'draft':True,'prerelease':False,'make_latest':'false'})
elif not release['name'].startswith('MinerU 书籍解析包：13 份'):
    raise SystemExit('The tag belongs to an unrelated release; refusing to modify it.')
RELEASE_ID=release['id']
UPLOAD=release['upload_url'].split('{',1)[0]
upload_url=urllib.parse.urlsplit(UPLOAD)
if upload_url.scheme!='https' or upload_url.hostname!='uploads.github.com':
    raise SystemExit('Unexpected GitHub release upload host.')
print('Release prepared:',release['html_url'],flush=True)
progress('release_created',release_url=release['html_url'])

def assets():return api('GET',prefix+f'/releases/{RELEASE_ID}/assets?per_page=100')

def matching_asset(name,size,sha):
    for asset in assets():
        if asset['name']!=name:continue
        if asset['state']=='uploaded' and asset['size']==size and asset.get('digest')=='sha256:'+sha:
            return asset
        if asset['state']=='starter':
            api('DELETE',prefix+'/releases/assets/'+str(asset['id']))
            return None
        raise RuntimeError('A different asset already has the name '+name)
    return None

def upload(path,name,sha,label):
    size=path.stat().st_size
    for attempt in range(4):
        existing=matching_asset(name,size,sha)
        if existing:return existing
        connection=http.client.HTTPSConnection('uploads.github.com',timeout=300)
        query=urllib.parse.urlencode({'name':name,'label':label})
        try:
            connection.putrequest('POST',upload_url.path+'?'+query)
            for key,value in HEADERS.items():connection.putheader(key,value)
            connection.putheader('Content-Type','application/zip' if name.endswith('.zip') else 'application/octet-stream')
            connection.putheader('Content-Length',str(size))
            connection.endheaders()
            with path.open('rb') as stream:
                for block in iter(lambda:stream.read(1024*1024),b''):connection.send(block)
            response=connection.getresponse()
            data=json.loads(response.read())
            if response.status!=201:
                raise RuntimeError(f'GitHub upload rejected ({response.status}): '+str(data.get('message','Unknown error')))
            if data['size']!=size or data['state']!='uploaded' or data.get('digest')!='sha256:'+sha:
                raise RuntimeError('GitHub asset size or SHA-256 mismatch: '+name)
            return data
        except (OSError,http.client.HTTPException,RuntimeError) as error:
            if attempt==3:raise
            print('Retrying asset upload:',name,type(error).__name__,flush=True)
            time.sleep(3*2**attempt)
        finally:connection.close()

def import_book(book):
    name=book['asset_name']
    if not re.fullmatch(r'[a-z0-9-]+\.zip',name):raise RuntimeError('Invalid asset name.')
    existing=matching_asset(name,book['size'],book['sha256'])
    if existing:
        print('Already verified:',name,flush=True)
        progress('uploaded',asset=name,size=book['size'],sha256=book['sha256'])
        return existing
    local=DOWNLOADS/name
    print('Downloading:',name,book['size'],'bytes',flush=True)
    progress('download_started',asset=name,size=book['size'])
    if not (local.exists() and local.stat().st_size==book['size'] and digest(local)==book['sha256']):
        subprocess.run(['curl','--fail','--silent','--show-error','--location',
            '--retry','6','--retry-delay','3','--retry-all-errors','--continue-at','-',
            '--connect-timeout','30','--max-time','10800','--output',str(local),SOURCE+name],check=True)
    if local.stat().st_size!=book['size'] or digest(local)!=book['sha256']:
        raise RuntimeError('Download size or SHA-256 mismatch: '+name)
    print('Source checksum verified:',name,flush=True)
    progress('download_verified',asset=name,size=book['size'],sha256=book['sha256'])
    answer=upload(local,name,book['sha256'],book['original_name'])
    print('Uploaded and GitHub checksum verified:',name,flush=True)
    progress('uploaded',asset=name,size=book['size'],sha256=book['sha256'])
    local.unlink()
    return answer

first=min(MANIFEST['books'],key=lambda book:book['size'])
answers=[import_book(first)]
remaining=[book for book in MANIFEST['books'] if book is not first]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    answers+=list(executor.map(import_book,remaining))
for name,path in [('manifest.json',ROOT/'books/manifest.json'),
                  ('SHA256SUMS.txt',ROOT/'books/SHA256SUMS.txt'),('README.md',ROOT/'README.md')]:
    upload(path,name,digest(path),name)
remote={row['name']:row for row in assets()}
for book in MANIFEST['books']:
    asset=remote.get(book['asset_name'])
    if not asset or asset['size']!=book['size'] or asset.get('digest')!='sha256:'+book['sha256']:
        raise RuntimeError('Final remote verification failed: '+book['asset_name'])
release=api('PATCH',prefix+f'/releases/{RELEASE_ID}',{'draft':False,'make_latest':'false'})
result={'repository':REPOSITORY,'tag_name':TAG,'release_url':release['html_url'],
    'verified_zip_count':len(answers),'total_bytes':sum(book['size'] for book in MANIFEST['books']),
    'books':[{'name':a['name'],'size':a['size'],'digest':a['digest'],'url':a['browser_download_url']} for a in answers]}
print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
progress('complete',release_url=release['html_url'],completed=len(answers))
summary=os.environ.get('GITHUB_STEP_SUMMARY')
if summary:
    with open(summary,'a') as stream:
        stream.write(f"13 book ZIPs uploaded and SHA-256 verified: {release['html_url']}\n")
