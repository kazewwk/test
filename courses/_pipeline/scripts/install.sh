#!/usr/bin/env bash
set -euo pipefail
PIPELINE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PIPELINE_DEVICE="${1:-cuda}"
PIPELINE_ENV="${2:-$PIPELINE_ROOT/.venv}"
PIPELINE_PYTHON="${PIPELINE_PYTHON:-python3.12}"
command -v ffmpeg >/dev/null
command -v ffprobe >/dev/null
"$PIPELINE_PYTHON" -m venv "$PIPELINE_ENV"
"$PIPELINE_ENV/bin/python" -m pip install --upgrade pip
if [ "$PIPELINE_DEVICE" = cuda ]; then
  nvidia-smi
  "$PIPELINE_ENV/bin/pip" install torch==2.8.0 torchaudio==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
elif [ "$PIPELINE_DEVICE" = cpu ]; then
  "$PIPELINE_ENV/bin/pip" install torch==2.8.0 torchaudio==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cpu
else
  echo 'Usage: install.sh cpu|cuda [venv-path]' >&2
  exit 2
fi
"$PIPELINE_ENV/bin/pip" install -r "$PIPELINE_ROOT/requirements-asr.txt" -e "$PIPELINE_ROOT"
"$PIPELINE_ENV/bin/python" "$PIPELINE_ROOT/scripts/patch_optional_japanese_import.py" > "$PIPELINE_ENV/compatibility-patch.json"
"$PIPELINE_PYTHON" -m venv "$PIPELINE_ENV-ocr"
if [ "$PIPELINE_DEVICE" = cuda ]; then
  "$PIPELINE_ENV-ocr/bin/pip" install paddlepaddle-gpu==3.3.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu126/
else
  "$PIPELINE_ENV-ocr/bin/pip" install paddlepaddle==3.3.0
fi
"$PIPELINE_ENV-ocr/bin/pip" install 'paddleocr[doc-parser]==3.7.0' -e "$PIPELINE_ROOT"
"$PIPELINE_PYTHON" -m venv "$PIPELINE_ENV-vlm"
"$PIPELINE_ENV-vlm/bin/pip" install torch==2.11.0 torchvision==0.26.0 transformers==5.20.2 accelerate pillow qwen-vl-utils -e "$PIPELINE_ROOT"
if [ "$PIPELINE_DEVICE" = cuda ]; then
  "$PIPELINE_PYTHON" -m venv "$PIPELINE_ENV-mineru"
  "$PIPELINE_ENV-mineru/bin/pip" install 'mineru[full]==4.0.12' -e "$PIPELINE_ROOT"
fi
for PIPELINE_SUFFIX in '' '-ocr' '-vlm' '-mineru'; do
  if [ -x "$PIPELINE_ENV$PIPELINE_SUFFIX/bin/python" ]; then
    "$PIPELINE_ENV$PIPELINE_SUFFIX/bin/pip" freeze > "$PIPELINE_ENV$PIPELINE_SUFFIX/installed.lock.txt"
    "$PIPELINE_ENV$PIPELINE_SUFFIX/bin/pip" check
  fi
done
