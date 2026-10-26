# 新概念视频多模态解析工具

将 Google Drive 视频逐个转换为可追溯 Markdown、JSONL、字幕、关键帧和质量报告。当前任务范围仅限新概念三个系列，共 555 个分 P；课程编号和分 P 编号分别保留。

## 当前验收状态

代码已实现，基础测试通过；Qwen3-ASR、ForcedAligner、Whisper 和 PP-OCRv5 已完成真实 CPU 片段测试，见[样本与耗时](../_benchmarks/local_cpu_sample/README.md)。整节样课尚未完成，不能把源码和清单当作已完成课程解析。实际完成状态以系列索引、每节 `manifest.json` 和 `qc_report.json` 为准。

本机旧 Xeon 的 DyNet 日语分词依赖触发非法指令，安装脚本将其改为按需导入，不改变中英文处理。PaddlePaddle 3.2.1 在该旧 CPU 上仍存在二进制指令兼容问题；CPU 可显式选用 `--ocr-engine onnx`，运行同版本 PP-OCRv5 server 的 RapidAI 转换权重。该后端已真实验证；复杂文档 PaddleOCR-VL 阶段仍需在兼容硬件上验证。

## 安装

Ubuntu 22.04/24.04，Python 3.10–3.12，FFmpeg。CPU 和 GPU 均使用虚拟环境，不使用 Docker。GPU 主机需已安装 NVIDIA 驱动；PyTorch wheel 安装 CUDA 12.8 用户态库，OCR 使用独立环境的 Paddle CUDA 12.6。

```bash
sudo apt-get update
sudo apt-get install -y python3-venv ffmpeg libgomp1 git
bash scripts/install.sh cpu /path/to/env
# 已授权的 CUDA 主机：bash scripts/install.sh cuda /path/to/env
```

GPU 型号不是硬编码：L4 使用 24 GB 显存，T4 使用 16 GB 显存。模型按阶段在独立进程运行，使用 FP16，避免同时驻留。CPU 使用 FP32 主转写和 INT8 Whisper。是否选择 GPU 应按真实吞吐量、总处理时间和实际计费单价决定。

## 来源清单

`courses/inventory.json` 保留 555 个 Drive ID、原始文件名、目录、课程名、播放顺序、Drive 校验和和时长。Drive 源目录及任何原始文件始终只读。

支持已有 rclone 自定义 OAuth 配置，或在 Python 中向 `Drive` 传入 Google Auth Credentials。凭据只用于标准 OAuth 刷新和 Google Drive API，不写入课程结果或日志。Google Drive 连接器也可用于首次发现和核对目录。

下载使用 HTTP Range 断点续传，源文件变化会使旧 partial 失效。完成后核对字节数、Drive MD5／可用的 SHA256，再计算本地 SHA256。状态数据库以 Drive ID、视频 SHA256 和配置指纹联合标记。

## 单节处理

```bash
python -m course_pipeline.cli process \
  --inventory ../inventory.json \
  --file-id DRIVE_FILE_ID \
  --rclone-config /private/rclone.conf \
  --cache /work/course-cache \
  --output /work/courses \
  --ocr-python /path/to/env-ocr/bin/python \
  --device cpu --threads 8
```

已有本地完整视频时，用 `--video /path/to/video.mp4` 代替 `--rclone-config`。`--prepare-only` 仅做媒体检查和关键帧提取，明确标为未转写，不生成假完成记录。

样课已观察到教师位于画面右下角。该样课可设置 `--ignore-regions '[[0.64,0.25,1.0,1.0]]'`，仅忽略该区域对抽帧触发的影响，保存的截图仍为原始全画面。不得未经检查将此区域套用于其他版式。

## 信息保留与复查

- 音频连续处理，每个核心段 30 秒，前后重叠 2 秒；静音检测只作质检，不丢弃源音频。
- Qwen3-ASR 1.7B 主转写，Qwen3-ForcedAligner 对齐；Faster-Whisper Large-v3 独立转写，不翻译。词边界不确定时保留原始完整窗口并标记，真实重复语音不删除。
- 两模型分歧、非静音空转写和静音内出现文字等疑点，以扩展上下文再跑一次，保留复查候选，不编造“修正答案”。
- FFmpeg 解码所有画面做变化检测，局部网格捕捉渐进标注；稳定帧、持续变化和定期审计共同触发。真实帧时间戳用于变帧率视频。
- PP-OCRv5 提取文字和坐标，视觉模型记录客观图表／操作描述；复杂表格和公式追加 PaddleOCR-VL。机器描述及不确定信息均带核验状态。
- `audio_processing_coverage_ratio` 仅表示已送入处理的音频覆盖率，绝不等于识别准确率；准确率没有人工基准时为 `null`。

## 输出与续跑

每个视频是独立目录，例如 `新概念英语第二册_L01-L48/Lesson_001_P003_L001 单词讲解造句/`，内含：

```text
transcript_raw.md       主模型重叠窗口原文
transcript_checked.md   机器交叉校验稿，含疑点
lecture_full.md         语音、OCR、视觉观察和图片
subtitles.srt
segments.jsonl          含来源、时间、证据和核验标记
manifest.json          SHA256、配置、产物校验表
qc_report.json         覆盖范围、异常区间及遗漏风险
frames.json
frames/                 原始分辨率无损 WebP
evidence/              两模型及复查候选、OCR 原始结构
```

阶段日志、SQLite 状态和资源监控保存在 `--cache`，不上传原视频和凭据。单个音频窗口或图像处理成功后立即落盘；重试按源指纹复用结果。

## 批处理与发布

先完整跑一节中英混讲且有课件变化的样课，检查实际声音、文字和截图。记录 `pilot-review.json`：

```json
{"decision":"pass","reviewer":"实际复核人","checked_intervals":[[120,180]],"lesson_directory":"/work/courses/series/lesson","manifest_sha256":"实际文件摘要"}
```

不能为未跑完的样课创建通过记录。

```bash
python scripts/batch.py --inventory ../inventory.json \
  --pilot-review /work/pilot-review.json --cache /work/course-cache \
  --output /work/courses --checkout /work/test-sparse \
  --rclone-config /private/rclone.conf --ocr-python /path/to/env-ocr/bin/python \
  --device cpu --public-authorized
```

发布器只向 `courses/` 写入本任务结果，使用独立稀疏检出保留仓库其他内容。每节单独提交、推送，再核对远端 commit tree 的每个 blob 与本地字节内容。推送后才允许清理本工具下载的临时视频。原始 Drive 文件没有删除接口。

单节默认最大 512 MiB，单文件超过 90 MiB 会停止发布，需先检查截图重复或配置 LFS；不会悄悄删图或增加付费存储。只有用户明确授权公开内容时才能使用 `--public-authorized`。本任务已于 2026-10-26 获得该授权。

```bash
python -m course_pipeline.cli validate /work/courses/series/lesson
python -m pytest -q tests
```

## 费用和生命周期

本任务 Colab 初始余额为 108.21 计算单元。标准 CPU 实测费率为 0.08 单元／小时，并不免费。首次 CPU 连接测试遇到 WebSocket 断开，未执行模型，实例已释放；停止后显示 0 个活动实例、余额仍为 108.21，显示精度以下用量不可据此断言为零。

目前没有启动 GPU，没有完成 T4/L4 吞吐量测试；不能仅凭小时单价宣布某卡更便宜。比较公式为 `总单元 = 计算小时 × 实际单元/小时`，并计入模型初始化、复查和 OCR/VLM 时间。新增消费、购买或充值遵循用户预算授权。

Colab 会中断或回收运行时，不能视为有固定 CPU/RAM 保证的永久服务器。结束后使用 `colab stop -s SESSION` 并再次查询 `colab sessions`、`colab usage`。

`scripts/colab_budget_run.py` 提供需明确预算授权的启动、计费轮询、超额提前停止和异常释放包装；尚未完成云端端到端验收，不能把源码存在当作已验证云任务完成。它不购买、充值或擅自选择其他 GPU。

## 模型和官方参考

模型 revision 固定在 `model_revisions.json`，安装环境分别生成 lock 文件。

- [Qwen3-ASR 与 ForcedAligner](https://github.com/QwenLM/Qwen3-ASR)
- [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)
- [PaddleOCR 使用文档](https://www.paddleocr.ai/main/en/quick_start.html)
- [PaddleOCR-VL](https://www.paddleocr.ai/main/en/version3.x/pipeline_usage/PaddleOCR-VL.html)
- [Qwen2.5-VL-3B](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)
- [Colab 资源限制说明](https://research.google.com/colaboratory/faq.html)
