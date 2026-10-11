# 审读、勘误与导入核验

源资料固定于提交 `d443ed18fd7b95569ebcbfc3b0d54666a6607687`，旧卡固定于 `fce68232f65f9ac6ae21bf526792c9e034eedb3e`。47章、4个辅助目录、6615个教材图片文件均有逐项审读记录；另1张外部原图单独记录，本版无模型绘图。

| 文件 | 用途 |
|---|---|
| [status.json](status.json) | 最终卡数、图片数、媒体数、每章实际阅读范围与所看图版 |
| [chapters.json](chapters.json) | 章节和辅助目录清单 |
| [source-files.json](source-files.json) | 6699个来源文件的路径、字节数和SHA-256 |
| [source-integrity-check.json](source-integrity-check.json) | 全部来源文件的存在、大小和SHA-256核验 |
| [image-index.jsonl](image-index.jsonl) | 6615个图片的编号、尺寸、哈希与各文档引用位置 |
| [image-review.jsonl](image-review.jsonl) | 每图处理、理由和关联卡；包含装饰、碎片、重复、补充及不可用图 |
| [edits](edits) | 51个分章审读结果，含核心/评分修订、选图、勘误、练习及未决源问题 |
| [source-errata.jsonl](source-errata.jsonl) | 1933条源勘误记录及固定提交的出处行 |
| [source-limitations.jsonl](source-limitations.jsonl) | 条件缺失、损坏题干、旧模型等源材料限制及本版处理；不据此编造唯一答案 |
| [practice.md](practice.md) | 169道较长练习；与每日卡片分开，提供教材图链接 |
| [exercise-audit.md](exercise-audit.md) | 生化第4章31项原教材习题审读与入卡处置，题干见原章节链接 |
| [media-manifest.jsonl](media-manifest.jsonl) | 2146个实际导入媒体的文件名和SHA-256 |
| [external-images.json](external-images.json) | 外部原图出处、署名、许可、视觉复核与学术复核 |
| [aux-doc-review.json](aux-doc-review.json) | 辅助文字、技能/支持文件及旧JSONL/TSV/APKG核验，含明确排除项 |
| [anki-import-check.json](anki-import-check.json) | 临时 Anki 集合中的实际导入和媒体核验 |
| [ankidroid-apkg-check.json](ankidroid-apkg-check.json) | 安卓单文件 APKG 的原生 Anki 导入、全图校验和重复导入核验 |
| [card-rendering-check.json](card-rendering-check.json) | 7张代表性含图卡的浏览器字段渲染与截图人工抽查 |
| [grading-independent-qa.json](grading-independent-qa.json) | 410条补评分独立文字复核；发现的4项证据边界／方向问题均已修复 |
| [artifact-manifest.json](artifact-manifest.json) | 安卓APKG、两份TXT、媒体ZIP和完整导入包的字节数与SHA-256 |

“已审读”指实际看过对应图版并结合图注／必要正文判断，不代表每图都进入卡片。图片总数按物理文件计，同图在不同源目录的副本分别留证；导入媒体按哈希去重。English 阅读范围以每章 review 为准，主要支持图片，无批量独立英文背景卡。

导出脚本：[`optimize_biology_anki.py`](../../scripts/optimize_biology_anki.py)，需要把固定源提交中的来源文件放在 `--source-root` 指定的工作树；包含补回的55个同源教材图路径。脚本按哈希核验后复制原图，保持原题面和牌组，检查四列、唯一题面、图引用及修订冲突。运行：

```bash
python scripts/optimize_biology_anki.py --source-root /path/to/source-worktree
```

原生 Anki 核验脚本：[`check_anki_import.py`](../../scripts/check_anki_import.py)，使用 Python `anki` 库创建临时集合，核验后删除该临时集合：

```bash
python scripts/check_anki_import.py
```

安卓交付为 [`SHU_Biology_AnkiDroid.apkg`](../SHU_Biology_AnkiDroid.apkg)，包括全部3920张卡和2146个原图媒体，采用兼容的传统APKG结构。生成及实际往返导入核验脚本：[`package_biology_ankidroid.py`](../../scripts/package_biology_ankidroid.py)，使用 Python `anki` 与 `genanki` 库：

```bash
python -m pip install anki==26.9.3 genanki==0.13.1
python scripts/package_biology_ankidroid.py
```

笔记GUID与模板ID在本APKG系列内固定，重复导入无需新增卡片；它们不能凭相同题面识别以前从TXT导入的随机GUID笔记。报告区分本APKG的重复导入与旧TXT卡更新核验。APKG已使用Anki原生后端实际导入，未宣称在实体安卓设备上测试。
