import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
from checkpoint import fetch, REPO, BRANCH, STATUS_REMOTE
status = fetch(f'https://api.github.com/repos/{REPO}/contents/{STATUS_REMOTE}?ref={BRANCH}')
log = (ROOT / 'logs/worker-recovery.log').read_text(errors='replace').replace('\r', '\n')
blocks = re.findall(r'VLM Predict:.*?(\d+)/(\d+) \[', log)
latest = blocks[-1] if blocks else None
phase = json.loads((ROOT / 'work/task-status.json').read_text())
print(json.dumps({'completed_pages': status['completed_pages'], 'remote_phase': status['phase'],
                  'latest_blocks': latest, 'phase': phase['phase'], 'task_status': phase}, ensure_ascii=False))
