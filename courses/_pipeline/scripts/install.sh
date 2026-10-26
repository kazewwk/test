#!/usr/bin/env bash
set -euo pipefail
PIPELINE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PIPELINE_DEVICE="${1:-cpu}"
PIPELINE_ENV="${2:-$PIPELINE_ROOT/.venv}"
python3 -m venv "$PIPELINE_ENV"
"$PIPELINE_ENV/bin/python" -m pip install --upgrade pip
if [ "$PIPELINE_DEVICE" = cuda ]; then
  nvidia-smi
  "$PIPELINE_ENV/bin/pip" install torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu128
elif [ "$PIPELINE_DEVICE" = cpu ]; then
  "$PIPELINE_ENV/bin/pip" install torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cpu
else
  echo 'Usage: install.sh cpu|cuda [venv-path]' >&2
  exit 2
fi
"$PIPELINE_ENV/bin/pip" install -r "$PIPELINE_ROOT/requirements-asr.txt" -e "$PIPELINE_ROOT"
"$PIPELINE_ENV/bin/python" "$PIPELINE_ROOT/scripts/patch_optional_japanese_import.py" > "$PIPELINE_ROOT/compatibility-patch.json"
python3 -m venv "$PIPELINE_ENV-ocr"
if [ "$PIPELINE_DEVICE" = cuda ]; then
  "$PIPELINE_ENV-ocr/bin/pip" install paddlepaddle-gpu==3.2.1 -i https://www.paddlepaddle.org.cn/packages/stable/cu126/
else
  "$PIPELINE_ENV-ocr/bin/pip" install paddlepaddle==3.2.1
fi
"$PIPELINE_ENV-ocr/bin/pip" install -r "$PIPELINE_ROOT/requirements-ocr.txt" -e "$PIPELINE_ROOT"
"$PIPELINE_ENV/bin/pip" freeze > "$PIPELINE_ROOT/installed-asr.lock.txt"
"$PIPELINE_ENV-ocr/bin/pip" freeze > "$PIPELINE_ROOT/installed-ocr.lock.txt"
command -v ffmpeg >/dev/null
command -v ffprobe >/dev/null
"$PIPELINE_ENV/bin/pip" check
"$PIPELINE_ENV-ocr/bin/pip" check
