import hashlib,json,pathlib,shutil,subprocess,sys,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1];REPO='kazewwk/test';CHECKOUT=ROOT/'publish-repo';TAG='cell-biology-local-hybrid-2026-10-11'
books=json.loads((ROOT/'work/chapters.json').read_text())
CHECKOUT.mkdir(exist_ok=True)
subprocess.run(['gh','auth','setup-git'],check=True)
subprocess.run(['git','init','-b','main'],cwd=CHECKOUT,check=True)
subprocess.run(['git','remote','add','origin','https://github.com/'+REPO+'.git'],cwd=CHECKOUT,check=True)
subprocess.run(['git','config','user.name','github-actions[bot]'],cwd=CHECKOUT,check=True)
subprocess.run(['git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com'],cwd=CHECKOUT,check=True)
def run(args,cwd=None):
 return subprocess.run(args,cwd=cwd,check=True,capture_output=True,text=True).stdout.strip()
def sha(path):
 with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def split_large(root):
 records=[]
 for path in sorted(root.rglob('*')):
  if not path.is_file() or path.stat().st_size<100_000_000:continue
  spec={'path':path.relative_to(root).as_posix(),'sha256':sha(path),'size':path.stat().st_size,'parts':[]};dest=path.with_name(path.name+'.parts');dest.mkdir()
  with path.open('rb') as f:
   while data:=f.read(95_000_000):
    part=dest/f"part{len(spec['parts'])+1:03}";part.write_bytes(data);spec['parts'].append({'path':part.relative_to(root).as_posix(),'size':len(data),'sha256':hashlib.sha256(data).hexdigest()})
  path.unlink();records.append(spec)
 if records:
  (root/'大文件分卷.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
  (root/'恢复大文件.py').write_text('''import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
for spec in json.loads((root/'大文件分卷.json').read_text()):
 target=root/spec['path'];temp=target.with_name(target.name+'.tmp');digest=hashlib.sha256();size=0
 with temp.open('wb') as out:
  for part in spec['parts']:
   data=(root/part['path']).read_bytes()
   assert len(data)==part['size'] and hashlib.sha256(data).hexdigest()==part['sha256']
   out.write(data);digest.update(data);size+=len(data)
 assert size==spec['size'] and digest.hexdigest()==spec['sha256']
 temp.replace(target);print(target)
''')
 (root/'SHA256SUMS.txt').write_text('\n'.join(sha(p)+'  '+p.relative_to(root).as_posix() for p in sorted(root.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.txt')+'\n')
archives=['Cell-Biology-Wang-Jinfa-MinerU-Local-Hybrid.zip','Cell-Biology-Laboratory-2e-MinerU-Local-Hybrid.zip'];notes=['两本书使用 MinerU 本地混合模式解析（standard 档）；具体引擎、版本、运行环境及对应页数记录在各书 manifest.json。','保留并复用已完成的本地断点，后续在 GitHub Actions 或 Google Colab 上本地推理，未调用远程解析 API。','按章节保留正文、完整分页 Markdown、图片、公式、结构化 JSON、模型输出和原始 PDF。原始整书按 95 MB 无损分片保留。','自动检查页码连续覆盖、图片引用、文件 SHA-256 和 ZIP CRC；按要求没有逐页校验。OCR/公式识别仍可能有误差，原始整书字节完整保留。',''];attachments=[]
for book,name in zip(books,archives):
 root=ROOT/'output'/book['title'];report=json.loads((root/'manifest.json').read_text())
 assert report['parsed_pages']==report['source_pages']==book['page_count'] and report['page_coverage_passed'] and report['missing_image_references']==0
 for line in (root/'SHA256SUMS.txt').read_text().splitlines():
  expected,relative=line.split('  ',1);p=root/relative;assert p.resolve().is_relative_to(root.resolve());assert sha(p)==expected
 archive=ROOT/'output'/name
 with zipfile.ZipFile(archive) as z:assert z.testzip() is None
 assert archive.stat().st_size<2_000_000_000
 target=CHECKOUT/book['title']
 if target.exists():shutil.rmtree(target)
 shutil.copytree(root,target);split_large(target)
 assert all(p.stat().st_size<100_000_000 for p in target.rglob('*') if p.is_file())
 attachments.extend([str(archive),str(archive)+'.sha256']);notes.append(f"- {book['title']}：{book['page_count']} 页；{report['images']} 个图片文件；{report['formula_nodes']} 个公式节点；运行环境及页数 `{report['execution_page_counts']}`；ZIP SHA-256 `{sha(archive)}`")
# Read-tree carries the unchanged repository tree without downloading all its blobs.
for attempt in range(5):
 run(['git','fetch','--filter=blob:none','--depth=1','origin','main'],CHECKOUT)
 base=run(['git','rev-parse','origin/main'],CHECKOUT)
 existing={b['title']:run(['git','ls-tree','origin/main','--',b['title']],CHECKOUT) for b in books}
 run(['git','update-ref','refs/heads/main',base],CHECKOUT);run(['git','symbolic-ref','HEAD','refs/heads/main'],CHECKOUT);run(['git','read-tree','origin/main'],CHECKOUT)
 run(['git','add','--',*[b['title'] for b in books]],CHECKOUT)
 staged_tree=run(['git','write-tree'],CHECKOUT)
 for book in books:
  if existing[book['title']] and existing[book['title']]!=run(['git','ls-tree',staged_tree,'--',book['title']],CHECKOUT):raise RuntimeError('Target book folder differs on main; avoid overwriting: '+book['title'])
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=CHECKOUT).returncode==0:break
 run(['git','commit','-m','Add complete MinerU hybrid parsing of Wang Jinfa cell biology textbooks'],CHECKOUT)
 pushed=subprocess.run(['git','push','origin','HEAD:main'],cwd=CHECKOUT,capture_output=True,text=True)
 if pushed.returncode==0:break
 if attempt==4:raise RuntimeError(pushed.stderr)
commit=run(['git','rev-parse','HEAD'],CHECKOUT)
remote_commit=json.loads(run(['gh','api',f'repos/{REPO}/git/commits/{commit}']))
assert remote_commit['tree']['sha']==run(['git','rev-parse','HEAD^{tree}'],CHECKOUT)
print('REPOSITORY PUBLISHED',commit,flush=True)
notesfile=ROOT/'output/release-notes.md';notesfile.write_text('\n'.join(notes)+'\n')
found=subprocess.run(['gh','release','view',TAG,'--repo',REPO],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
if not found:run(['gh','release','create',TAG,'--repo',REPO,'--target',commit,'--title','王金发细胞生物学两本教材 · MinerU 本地混合模式','--notes-file',str(notesfile),*attachments])
else:
 old=json.loads(run(['gh','release','view',TAG,'--repo',REPO,'--json','assets']))
 published={a['name']:a for a in old['assets']};pending=[]
 for path in attachments:
  p=pathlib.Path(path)
  if p.name not in published:pending.append(path)
  elif published[p.name]['size']!=p.stat().st_size:raise RuntimeError('Existing Release asset size differs: '+p.name)
 if pending:run(['gh','release','upload',TAG,'--repo',REPO,*pending])
release=json.loads(run(['gh','release','view',TAG,'--repo',REPO,'--json','url,assets']))
assets={a['name']:a for a in release['assets']}
for name in archives:assert name in assets and assets[name]['size']==(ROOT/'output'/name).stat().st_size
server_release=json.loads(run(['gh','api',f'repos/{REPO}/releases/tags/{TAG}']))
for asset in server_release['assets']:
 if asset['name'] in archives and asset.get('digest'):
  assert asset['digest']=='sha256:'+sha(ROOT/'output'/asset['name']), asset['name']
result={'phase':'complete','commit':commit,'release_url':release['url'],'books':[{**b,'archive':name,'archive_size':(ROOT/'output'/name).stat().st_size,'archive_sha256':sha(ROOT/'output'/name)} for b,name in zip(books,archives)]}
(ROOT/'work/final-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('COMPLETE',release['url'],flush=True)
