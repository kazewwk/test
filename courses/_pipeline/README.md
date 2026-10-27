# 新概念英语视频多模态解析

范围：Google Drive 中新概念第一册、第二册 L01–L48、第二册 L49–L96，共 555 个视频，约 127.52 小时。每个分 P 独立交付，教材课号与分 P 播放顺序分别保存。当前实际完成数请看[课程目录](../README.md)，不能以代码、清单或样本存在代替整节课完成。

## 高精度模型组合

| 用途 | 模型与运行方式 |
|---|---|
| 原文转写 | Qwen3-ASR-1.7B，GPU FP16 |
| 词级时间对齐 | Qwen3-ForcedAligner-0.6B |
| 独立交叉转写 | Faster-Whisper Large-v3，GPU FP16，不量化 |
| 文字与坐标 | PP-OCRv5 server，原始 1920 像素画面 |
| 课件结构、公式、表格 | PaddleOCR-VL-1.6，含图片内文字识别和遗漏区域复查 |
| 独立文档核查 | MinerU 4.0.12 Advanced / MinerU2.5-Pro-2605-1.2B |
| 图示、操作、圈画和遗漏文字 | Qwen3.5-9B，原生 BF16、完整分辨率，不使用 4-bit 量化 |

大模型按阶段独立运行并释放显存，适配 L4 24GB。模型仓库 revision 固定在 `model_revisions.json`；安装脚本为 ASR、Paddle、通用视觉、MinerU 建立四个 Python 虚拟环境，处理其 PyTorch／Transformers 版本差异。不使用 Docker。

这些是本任务实际部署的模型，不声称小型本地视觉模型在所有场景都比商业大型模型准确。MinerU 是课件结构解析的补充，不能替代语音转写或截图。单帧试运行已经观察到音标遗漏和视觉勾号误识，因此所有候选、原始截图及不确定标记均保留。

## 安装与单节处理

Ubuntu、Python 3.12、FFmpeg、已安装 NVIDIA 驱动的 L4。安装前自行配置标准 Drive OAuth/rclone 凭据与 GitHub 登录；不要把密钥放入仓库。

```bash
sudo apt-get update
sudo apt-get install -y python3.12-venv ffmpeg libgomp1 git
bash scripts/install.sh cuda /work/env
/work/env/bin/python -m course_pipeline.cli process \
  --inventory ../inventory.json --file-id DRIVE_FILE_ID \
  --rclone-config /private/rclone.conf \
  --cache /work/cache --output /work/courses \
  --ocr-python /work/env-ocr/bin/python \
  --visual-python /work/env-vlm/bin/python \
  --mineru-python /work/env-mineru/bin/python \
  --device cuda:0 --threads 10
```

已有视频可用 `--video /path/video.mp4`。`--prepare-only` 只检查媒体并抽取关键帧；`--asr-only` 只保存语音阶段检查点，均不会生成假冒完整结果的 `manifest.json`。

CPU 可以运行语音与部分 OCR，但耗时和内存需求较高。本机旧 Xeon 的实测 60 秒语音耗时约 334 秒（两模型合计）；旧 3B 视觉模型单张约 291 秒，并出现 CPU 指令兼容问题。9B FP32 还需要显著更多内存。因此当前完整高精度流程使用 L4。`install.sh cpu` 主要供语音／OCR 测试，未声称已验证 CPU 上运行完整 MinerU Advanced。

## 信息保留与质量控制

- 全部音频连续分段处理，核心段 30 秒，边界重叠 2 秒；静音检测仅用于质检，不删除静音区原文候选。
- 不翻译、不总结、不删除重复强调。两套原始转写独立保留；分歧段扩大上下文重跑。出现中文被意外转成英文时增加原语言提示复查。
- 复查选择保留来源记录；不会仅因与 Whisper 一致就删除主模型中较长的英语例句。词级对齐无法可靠还原段边界时保留完整窗口并标记。
- FFmpeg/OpenCV 解码所有画面，检测全局、局部、渐进动画和持续变化。固定时间仅作为补充审计触发。关键帧保存源分辨率无损 WebP，并记录真实视频时间戳和 SHA256。
- PP-OCRv5 与 PaddleOCR-VL 分别提取；对后者遗漏的高置信度 OCR 区域重新裁剪识别。MinerU 输出保留原始结构，不能用摘要替代原文。
- 视觉模型记录教学信息和圈画，保留未经修订的模型输出。蓝色勾号与圈选可用像素及 OCR 坐标辅助核查，无法得到支持的标注明确标为待核验。
- 检测空白转写、相邻重复字幕、时间戳异常、OCR 空白／低置信度、OCR 与视觉模型分歧及源音画起始偏移。音画语义对应仍可能需要人工复核。

`audio_processing_coverage_ratio` 表示送入模型处理的时间覆盖率，**不是识别准确率**。没有人工基准时 `accuracy` 为 `null`。即使模型一致，也不能保证没有共同误识。

## 文件结构

```text
课程系列/教材课号_分P_标题/
  transcript_raw.md       主模型完整重叠窗口原文
  transcript_checked.md   交叉校验稿及未解决分歧
  lecture_full.md         时间轴上的语音、OCR、图示、文档解析与截图
  subtitles.srt
  segments.jsonl          含 id/text/metadata，可直接导入常见 RAG
  manifest.json           来源 ID、视频 SHA256、模型配置、产物校验和
  qc_report.json          时长、覆盖范围、片段／关键帧数、疑点时间区间
  frames.json
  frames/                源分辨率关键帧
  evidence/              两模型原始输出、复查候选、OCR、MinerU、视觉输出
```

Markdown 图片使用相对路径。JSONL 同时保留便于检索的 `text` 与完整结构证据，便于 GPT、Claude、Gemini 或其他系统回查截图和来源。

## 断点续跑与逐课发布

Drive 源文件始终保留。下载支持 Range 续传、失败重试、字节数及 Drive MD5／SHA256 校验；状态按 Drive ID、视频 SHA256 和配置指纹记录。每个音频窗口／画面结果原子落盘。不能复用输入、模型或配置不一致的检查点。

先完整处理一节中英混讲、含 PPT 变化的样课，检查实际结果并保存审查记录：

```json
{"decision":"pass","reviewer":"实际审查者和审查方式","checked_intervals":[[120,180]],"lesson_directory":"/work/courses/series/lesson","manifest_sha256":"实际摘要"}
```

机器审查不能写成人工听写确认；允许明确记录尚未解决的识别疑点。样课未完成时不得伪造通过记录。

```bash
/work/env/bin/python scripts/batch.py \
  --inventory ../inventory.json --pilot-review /work/pilot-review.json \
  --cache /work/cache --output /work/courses --checkout /work/test-sparse \
  --rclone-config /private/rclone.conf \
  --ocr-python /work/env-ocr/bin/python \
  --visual-python /work/env-vlm/bin/python \
  --mineru-python /work/env-mineru/bin/python \
  --device cuda:0 --public-authorized
```

每节先校验全部产物，再向 `kazewwk/test` 的 `main` 单独提交并推送，核对远端 Git blob 与本地字节哈希。保留仓库原内容，不上传原始视频、音频和凭据。公开完整文本／截图已获得本次用户明确授权。远程发布可通过 `NCE_GITHUB_TOKEN_FILE` 指定权限 0600 的临时凭据文件，仅在 GitHub 发布进程中读取。

批处理记录每节错误，继续其他视频；再次运行时跳过已验证发布且源校验和一致的视频。上传验证后可清理任务自己的临时媒体和已交付产物，保留来源、质量报告和提交回执；用 `--retain-completed` 保留本地完整副本。单节超过 512 MiB 或单文件接近 GitHub 大小限制会明确报错，不能默默删截图。

```bash
/work/env/bin/python -m course_pipeline.cli validate /work/courses/series/lesson
/work/env/bin/python -m pytest -q tests
```

## Colab 与费用记录

本任务使用已有 Colab 计算单元，未授权新增购买或充值。已观察费率：CPU 0.08 CU/h、T4 1.07 CU/h、L4 1.54 CU/h；实际余额与持续运行用量保存在任务私有账本。计算单元不能在缺少购买记录时直接宣称为某一笔实际现金支出。

Colab 运行时会回收。本次已发生过回收并从本机检查点恢复。运行结果需要持续备份，不能仅留在 `/content`。结束后释放本任务运行时，并查询会话列表与余额确认。

## 官方参考

- [Qwen3-ASR / ForcedAligner](https://github.com/QwenLM/Qwen3-ASR)
- [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)
- [PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)
- [MinerU SDK](https://opendatalab.github.io/MinerU/usage/sdk_api/)
- [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Colab 资源限制](https://research.google.com/colaboratory/faq.html)
