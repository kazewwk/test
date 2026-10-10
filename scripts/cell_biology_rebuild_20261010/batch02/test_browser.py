from pathlib import Path
import json
from playwright.sync_api import sync_playwright
O=Path('/tmp/biology_rebuild/batch02/output');r={};errors=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':390,'height':844},device_scale_factor=1);page.on('pageerror',lambda e:errors.append(str(e)));page.goto((O/'preview.html').as_uri(),wait_until='load');page.evaluate('async()=>{await Promise.all(Array.from(document.images).map(x=>x.decode()))}')
 r['notes']=page.locator('article').count();r['all_image_occurrences_decoded']=page.evaluate('Array.from(document.images).every(x=>x.complete&&x.naturalWidth>0)');r['mobile_390px_overflow']=page.evaluate('document.documentElement.scrollWidth>innerWidth');r['broken_images']=page.evaluate('Array.from(document.images).filter(x=>!x.complete||!x.naturalWidth).length')
 page.locator('article[data-card="RB-CN01-0209"] .front').scroll_into_view_if_needed();page.screenshot(path=str(O/'mobile_preview.png'),full_page=False)
 page.set_viewport_size({'width':1100,'height':950});r['desktop_1100px_overflow']=page.evaluate('document.documentElement.scrollWidth>innerWidth');r['script_errors']=errors;assert r['notes']==218 and r['all_image_occurrences_decoded'] and not r['mobile_390px_overflow'] and not r['desktop_1100px_overflow'] and not errors;b.close()
(O/'browser_validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
