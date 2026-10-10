from pathlib import Path
import hashlib,json,subprocess,time
from urllib.parse import quote
import requests
base=Path('anki/SHU_Cell_Biology_Rebuild_20261010/Batch03')
report=json.loads((base/'apkg_validation.json').read_text())
assert report['status']=='PASS'
commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
url='https://raw.githubusercontent.com/kazewwk/test/'+commit+'/'+quote(str(base/report['package']),safe='/')
last_error=None
for attempt in range(6):
    try:
        response=requests.get(url,timeout=(15,90))
        response.raise_for_status()
        raw=response.content
        assert len(raw)==report['bytes'],(len(raw),report['bytes'])
        actual=hashlib.sha256(raw).hexdigest()
        assert actual==report['sha256'],(actual,report['sha256'])
        result={'status':'PASS','asset_commit':commit,'url':url,'bytes':len(raw),'sha256':actual,
            'validation':'Downloaded the actual public pinned APKG and compared bytes and SHA-256 against the native-import-validated build.'}
        (base/'remote_download_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result))
        break
    except Exception as error:
        last_error=error
        if attempt<5:time.sleep(5)
else:
    raise last_error
