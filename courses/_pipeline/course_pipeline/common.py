from __future__ import annotations

import hashlib
import json
import os
import subprocess
import time
from pathlib import Path
from typing import Any


def utcnow():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def digest(path, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, obj):
    atomic_text(path, json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def atomic_text(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    with temp.open("w", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    temp.replace(path)


def write_jsonl(path, rows):
    atomic_text(path, "".join(json.dumps(x, ensure_ascii=False, allow_nan=False) + "\n" for x in rows))


def read_jsonl(path):
    return [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]


def run(argv, *, timeout=3600, log=None, env=None):
    if log:
        Path(log).parent.mkdir(parents=True, exist_ok=True)
        with Path(log).open("ab") as stream:
            p = subprocess.run([str(x) for x in argv], stdout=stream, stderr=stream, timeout=timeout,env=env)
        if p.returncode:
            raise RuntimeError(f"{Path(str(argv[0])).name} exited {p.returncode}; see {log}")
        return ""
    return subprocess.run([str(x) for x in argv], check=True, capture_output=True,
                          text=True, timeout=timeout,env=env).stdout


def retry(operation, tries=3):
    for attempt in range(tries):
        try:
            return operation()
        except (OSError, RuntimeError, subprocess.SubprocessError):
            if attempt == tries - 1:
                raise
            time.sleep(min(2 ** attempt, 15))


def checkpoint_valid(record, inputs):
    if record.get("inputs") != inputs or record.get("state") != "complete":
        return False
    return all(Path(p).is_file() and digest(p) == h for p, h in record.get("outputs", {}).items())


def artifact_hashes(directory):
    root = Path(directory)
    return {str(p.relative_to(root)): digest(p) for p in sorted(root.rglob("*"))
            if p.is_file() and p.name != "manifest.json"}


def seconds_label(t):
    t = max(0, int(t))
    return f"{t // 3600:02d}:{t // 60 % 60:02d}:{t % 60:02d}"
