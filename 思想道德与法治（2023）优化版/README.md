# 思想道德与法治（2023）优化版

原始PDF共264页，使用MinerU 4.0.10 **Hybrid混合模式**解析：standard / high、ONNX与llama.cpp CPU，启用图片解析。

[全文](full.md) · [页码覆盖](page_coverage.json) · [完整性检查](validation_report.json) · [来源和解析参数](manifest.json)

正文章节、导论、前置页、结语及后记全部按原始PDF物理页码连续保存。各章节提供Markdown、完整内容视图、结构化JSON、配图引用、原页PDF和原生文本。`raw_chunks/`保留MinerU未经章节重组的全部输出。

原始PDF全部字节在`original_pdf/`按不超过95MB分片保存。运行 `python tools/restore_original_pdf.py` 可精确恢复并核对SHA256。`split_files.json`记录其他超过100MB的文件分片。

页面覆盖不代表逐字识别准确；原PDF与原生文本用于核对OCR、图表、公式及脚注。原文件读取警告保存在`source_pdf_warnings.json`。

| 内容 | 原始PDF页码 | 页数 |
|---|---|---:|
| [前置内容](00_前置内容/chapter.md) | 1–8 | 8 |
| [绪论 担当复兴大任 成就时代新人](01_绪论_担当复兴大任_成就时代新人/chapter.md) | 9–20 | 12 |
| [第一章 领悟人生真谛 把握人生方向](02_第一章_领悟人生真谛_把握人生方向/chapter.md) | 21–50 | 30 |
| [第二章 追求远大理想 坚定崇高信念](03_第二章_追求远大理想_坚定崇高信念/chapter.md) | 51–77 | 27 |
| [第三章 继承优良传统 弘扬中国精神](04_第三章_继承优良传统_弘扬中国精神/chapter.md) | 78–114 | 37 |
| [第四章 明确价值要求 践行价值准则](05_第四章_明确价值要求_践行价值准则/chapter.md) | 115–145 | 31 |
| [第五章 遵守道德规范 锤炼道德品格](06_第五章_遵守道德规范_锤炼道德品格/chapter.md) | 146–196 | 51 |
| [第六章 学习法治思想 提升法治素养](07_第六章_学习法治思想_提升法治素养/chapter.md) | 197–259 | 63 |
| [后记与封底](08_后记与封底/chapter.md) | 260–264 | 5 |

[OCR原页核对与修订记录](ocr_review/README.md)
