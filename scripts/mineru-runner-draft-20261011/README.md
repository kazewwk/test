# MinerU 两本细胞生物学教材续跑草稿

**状态：未启用、未执行。** 当前环境已两次重置，解析停止。此前用户选择当前本地 CPU；将计算改到 GitHub Actions 运行器需先得到用户同意。

截至 2026-10-11 03:16:15 UTC，远程已保留 59 页完整解析批次：王金发教材 30/528 页、实验教程 29/265 页。原始 PDF、章节划分和本地解析代码均已保留。

## 具体执行方案

- 将本目录的代码复制到 main 的 `scripts/mineru-runner-20261011/`，将 `mineru-cell-books.yml.draft` 复制为 `.github/workflows/mineru-cell-books.yml`，触发一次执行。本草稿位于普通目录，不会触发工作流。
- MinerU 4.0.11、mineru-llama-cpp 0.1.2、ONNXRuntime 1.31.0，完整依赖锁定于 `requirements-local.txt`。保持 standard 档、ONNX + llama.cpp 混合模式、扫描 OCR、图片和公式识别；模型在运行器本地推理，不调用远程解析 API，不设置截断上下文或输出长度。
- 原书按 SHA-256 校验后分成 33 个文件夹（15/12 正文章及封面、前言、目录、参考文献、索引、附录）。4 个章节任务同时运行，单任务最多 350 分钟；依照模型实际识别速度运行，无完成时间保证。
- 重用已经完成的 59 页。每完成 4 页，完整批次 ZIP、图片、Markdown、JSON、原始模型输出及校验和立即提交到 `mineru-local-wang-jinfa-20261010` 分支。每章使用独立状态文件，分支更新拒绝非快进并重试，避免并发丢失进度。
- 若中断或失败，可重跑任务；已经提交的批次直接恢复，不重新识别。某章节未完成时，不生成伪完整 ZIP、不发布完成 Release。
- 全部章节完成后自动检查 793 页连续覆盖、解析页码、图片引用、原始扫描图像流、所有文件与 ZIP 校验和。按照用户要求不逐页人工校验。自动检查不能保证 OCR 与公式的语义准确率；每章另保留原始 PDF 页面作为完整原内容备份。
- 两本书的文件夹提交到 main；若单文件达到 100,000,000 字节，则仓库中拆成 95,000,000 字节分卷并附校验和及恢复脚本，Release ZIP 保留完整文件。只修改本任务文件，已有仓库内容保持。
- 发布 tag：`cell-biology-local-hybrid-2026-10-10-0933c203`。上传 `Cell-Biology-Wang-Jinfa-MinerU-Local-Hybrid.zip`、`Cell-Biology-Laboratory-2e-MinerU-Local-Hybrid.zip` 及 SHA-256；确认 GitHub 返回的资产大小和 digest 一致。

## 已完成验证

Python 语法、YAML、33 章连续覆盖、缓存路径一致性、并发分支冲突时保留其他文件、拒绝 ZIP 路径越界、100 MB 文件分卷及精确重构均通过。推理及发布尚未在 GitHub 运行器执行。

官方运行约束：
- https://docs.github.com/en/actions/reference/limits
- https://docs.github.com/en/actions/reference/runners/github-hosted-runners

恢复状态：`.local-mineru-checkpoints-20261011/status.json`，新方案章节状态：`.local-mineru-checkpoints-20261011/runner-status/bookN-XX.json`。
