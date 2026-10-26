from __future__ import annotations
import json
import os
import shutil
import subprocess
import threading
import time
from pathlib import Path
import psutil
from .common import utcnow


class Monitor:
    def __init__(self, path):
        self.path = Path(path)
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.loop, daemon=True)

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.thread.start()
        return self

    def __exit__(self, *args):
        self.stop_event.set()
        self.thread.join(timeout=5)

    def loop(self):
        while not self.stop_event.is_set():
            p = psutil.Process()
            processes = [p] + p.children(recursive=True)
            memory = 0
            for process in processes:
                try:
                    memory += process.memory_info().rss
                except psutil.NoSuchProcess:
                    pass
            data = {'time': utcnow(), 'process_tree_rss_bytes': memory,
                    'system_cpu_percent': psutil.cpu_percent(),
                    'system_available_memory_bytes': psutil.virtual_memory().available,
                    'disk_free_bytes': shutil.disk_usage(self.path.parent).free}
            if shutil.which('nvidia-smi'):
                r = subprocess.run(['nvidia-smi','--query-gpu=name,utilization.gpu,memory.used,memory.total,power.draw',
                                    '--format=csv,noheader,nounits'], capture_output=True, text=True, timeout=5)
                data['gpu'] = r.stdout.strip()
            with self.path.open('a') as stream:
                stream.write(json.dumps(data) + '\n')
            self.stop_event.wait(15)
