import json
import os
import platform
import shutil
from pathlib import Path

cpu = Path('/proc/cpuinfo').read_text()
print(json.dumps({
    'hostname': platform.node(), 'python': platform.python_version(),
    'cpu_count': os.cpu_count(),
    'cpu_model': next((x.split(':', 1)[1].strip() for x in cpu.splitlines() if x.startswith('model name')), None),
    'meminfo': '\n'.join(Path('/proc/meminfo').read_text().splitlines()[:3]),
    'disk_free_gib': shutil.disk_usage('/content' if Path('/content').exists() else '.').free / 2**30,
    'nvidia_smi_available': bool(shutil.which('nvidia-smi')),
    'os': platform.platform(),
}, indent=2))
