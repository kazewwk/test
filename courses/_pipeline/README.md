# 新概念英语视频多模态解析

范围：Google Drive 中新概念第一册、第二册 L01–L48、第二册 L49–L96，共 555 个视频，约 127.52 小时。每个分 P 独立交付，教材课号与分 P 播放顺序分别保存。当前实际完成数请看[课程目录](../README.md)，不能以代码、清单或样本存在代替整节课完成。

## 高精度模型组合

| 用途 | 模型与运行方式 |
|---|---|
| 原文转写 | Qwen3-ASR-1.7B，GPU FP16；CPU FP32 |
| 词级时间对齐 | Qwen3-ForcedAligner-0.6B |
| 独立交叉转写 | Faster-Whisper Large-v3，GPU FP16／CPU FP32，不作整数权重量化 |
| 文字与坐标 | PP-OCRv5 server，原始 1920 像素画面 |
| 课件结构、公式、表格 | PaddleOCR-VL-1.6，含图片内文字识别和遗漏区域复查 |
| 独立文档核查 | MinerU 4.0.12 Advanced / MinerU2.5-Pro-2605-1.2B，用于复杂结构和未解决的文字遗漏 |
| 图示、操作、圈画和遗漏文字 | 用户订阅接口的 gpt-6.1-terra；不确定或主模型不可用时用 gpt-6-luna 复查 |

本地模型按阶段独立运行并释放显存，适配 L4 24GB。模型仓库 revision 固定在 `model_revisions.json`；安装脚本为 ASR、Paddle、MinerU 建立三个 Python 虚拟环境，不使用 Docker。默认视觉接口模式无需部署通用 9B 视觉模型；旧样课使用的原生 BF16 Qwen3.5-9B 输出继续保留，可通过安装脚本第三参数 `local` 安装该后端。

MinerU 补充课件结构解析，不能替代语音转写或截图。真实图片测试发现过音标遗漏和勾号误识，所有候选、原始截图及不确定标记均保留。API 的请求模型、返回模型、可见回答和用量都有记录，凭据及隐藏推理内容不写入交付文件。选择依据与局限见[真实 API 样本](../_benchmarks/vision_api/README.md)。

## 安装与单节处理

Ubuntu、Python 3.12、FFmpeg、已安装 NVIDIA 驱动的 L4。安装前自行配置标准 Drive OAuth/rclone 凭据与 GitHub 登录；不要把密钥放入仓库。

```bash
sudo apt-get update
sudo apt-get install -y python3.12-venv ffmpeg libgomp1 git
bash scripts/install.sh cuda /work/env api
/work/env/bin/python -m course_pipeline.cli process \
  --inventory ../inventory.json --file-id DRIVE_FILE_ID \
  --rclone-config /private/rclone.conf \
  --cache /work/cache --output /work/courses \
  --ocr-python /work/env-ocr/bin/python \
  --visual-backend api --api-config /private/vision-api.json \
  --mineru-python /work/env-mineru/bin/python \
  --device cuda:0 --threads 10
```

已有视频可用 `--video /path/video.mp4`。`--prepare-only` 只检查媒体并抽取关键帧；`--asr-only` 只保存语音阶段检查点，均不会生成假冒完整结果的 `manifest.json`。

接口配置放在仓库外并设置权限 0600：`{"base_url":"https://your-provider.example/v1","api_key":"YOUR_SECRET","review_model":"gpt-6-luna"}`。使用完整原图，默认两路请求，遵守服务端 Retry-After；图像模型不用于改写或补写语音。

Colab 8 核、约 51 GiB CPU 已实测原精度语音和 PP-OCRv5：60 秒语音两模型墙钟合计约 302 秒，单张 OCR 约 74 秒（含下载和加载）。按纯推理外推，全部 127.5 小时仅两轮语音约 155 CU，尚不含复查和画面，超过当时约 83 CU 余额。PaddleOCR-VL 单图测试运行约 304 秒时因费用判断停止，MinerU CPU 全流程尚未验证。详见 [CPU 实测与原始候选](../_benchmarks/cpu_colab/README.md)。CPU 低小时费率不能保证低总费用，当前生产使用 L4 加用户订阅图像 API。

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
  --visual-python /work/env/bin/python \
  --visual-backend api --api-config /private/vision-api.json \
  --mineru-python /work/env-mineru/bin/python \
  --device cuda:0 --public-authorized
```

每节先校验全部产物，再向 `kazewwk/test` 的 `main` 单独提交并推送，核对远端 Git blob 与本地字节哈希。保留仓库原内容，不上传原始视频、音频和凭据。公开完整文本／截图已获得本次用户明确授权。远程发布可通过 `NCE_GITHUB_TOKEN_FILE` 指定权限 0600 的临时凭据文件，仅在 GitHub 发布进程中读取。

批处理记录每节错误，继续其他视频；再次运行时跳过已验证发布且源校验和一致的视频。上传验证后可清理任务自己的临时媒体和已交付产物，保留来源、质量报告和提交回执；用 `--retain-completed` 保留本地完整副本。每次推送控制在 512 MiB，超过时分批上传临时分支，全部文件就绪后才更新 main；单文件达到 90 MiB 时要求配置大文件存储，不能默默删截图。

`batch_concurrent.py` 让本地模型与远程图像复查／发布同时推进；队列最多暂存三节。每个音频窗口、OCR 结果按来源与模型指纹复用。FP16 GPU 与 FP32 CPU 的已完成 Whisper 候选可跨设备复用，并保留原精度记录；旧 INT8 结果不作为该缓存使用。抽帧复用会核对解码后的像素，较快的无损 WebP 编码不改变原始像素。

`runtime_driver.py` 负责环境、GitHub 断点恢复和批处理；`colab_controller.py` 使用同一 SSH ControlPath 监控、在运行时回收后重建、完成后释放资源，余额到 1 CU 预留线时停止，绝不充值。需要显式提供现有余额授权、私有凭据文件及已验收样课记录。用 `--help` 查看参数。运行时控制错误会记录为待修复，不能记为课程完成。

```bash
/work/env/bin/python -m course_pipeline.cli validate /work/courses/series/lesson
/work/env/bin/python -m pytest -q tests
```

## Colab 与费用记录

本任务使用已有 Colab 计算单元，未授权新增购买或充值。已观察费率：普通 CPU 0.08 CU/h、高内存 CPU 0.26 CU/h、T4 1.07 CU/h、L4 1.54 CU/h。高内存 CPU 实测实例已释放；实际余额与持续运行用量保存在任务私有账本。计算单元不能在缺少购买记录时直接宣称为某一笔实际现金支出。用户已确认图像 API 使用既有订阅额度，无额外按 Token 计费。

Colab 运行时会回收。本次已发生过回收并从本机检查点恢复。运行结果需要持续备份，不能仅留在 `/content`。结束后释放本任务运行时，并查询会话列表与余额确认。

## 官方参考

- [Qwen3-ASR / ForcedAligner](https://github.com/QwenLM/Qwen3-ASR)
- [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)
- [PaddleOCR-VL-1.6](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)
- [MinerU SDK](https://opendatalab.github.io/MinerU/usage/sdk_api/)
- [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Colab 资源限制](https://research.google.com/colaboratory/faq.html)
