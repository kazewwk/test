import json,subprocess,hashlib
from pathlib import Path
REPO='kazewwk/test';TAG='biochem-molecular-v5-20261012'

def api(endpoint,method=None,fields=()):
 cmd=['gh','api',endpoint]
 if method:cmd+=['--method',method]
 for key,value in fields:cmd+=['-f',key+'='+value]
 return json.loads(subprocess.check_output(cmd,text=True))

r=api('repos/'+REPO+'/releases/tags/'+TAG)
renames={
 'd5d4c02810aee275a97bd15b988d730040fa53e38c390b8cd1c21badff0e2acf':'Biochem36_Molecular11_v5_20261012_7202.apkg',
 '2462999e5839b10c0bc2af8a389981279dcc46ec4b49f39ef32f44f0427a33d6':'v5-card-data-and-audit.zip',
 '83ee4a27da4b05d7c9eca2090526d3b0ba2752dd86169e588876d071e8bf66cf':'v5-revision-report.md',
 'e88d5b10bbc848ed4f2983409f628487495fcb0ae711c74c9542bf7d6a17c40f':'SHA256SUMS-local-names.txt',
}
for digest,newname in renames.items():
 matches=[a for a in r['assets'] if a.get('digest')=='sha256:'+digest];assert len(matches)==1
 a=matches[0]
 if a['name']!=newname:api('repos/'+REPO+'/releases/assets/'+str(a['id']),'PATCH',[('name',newname)])
r=api('repos/'+REPO+'/releases/tags/'+TAG)
lines=[]
for a in r['assets']:
 if a['name']=='SHA256SUMS.txt':continue
 digest=a.get('digest','');assert digest.startswith('sha256:')
 lines.append(digest.removeprefix('sha256:')+'  '+a['name'])
p=Path('SHA256SUMS.txt');p.write_text('\n'.join(sorted(lines))+'\n')
subprocess.run(['gh','release','upload',TAG,str(p),'--repo',REPO,'--clobber'],check=True)
print(json.dumps({'release':r['html_url'],'renamed':list(renames.values()),'checksums':'SHA256SUMS.txt'}))
