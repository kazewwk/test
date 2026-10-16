# biostat

解析：MinerU 4.0.12 Advanced（最高精度），Colab Tesla T4，本地模型。

原始 PDF 472 页；源 SHA-256：`63ef75170a122ba8ecfee64304b464368fc01d3d78aaaeb0a06be87788910d4b`。

[完整内容](book.md) · [结构化结果](structured_content.json) · [逐页映射](page_map.json) · [原始 PDF](source/) · [校验记录](validation.json)

FULL 内容视图保留模型识别出的页眉、页脚、页码、边栏、脚注、图片、公式和表格；原 PDF 字节完整保留。`source_images/` 另存 PDF 中嵌入的光栅图像；矢量内容仍完整保留在原 PDF 中。

`raw/` 是逐批原始 MinerU 输出及素材。章节 JSON 内的 `image_path` 相对于本书目录；章节 Markdown 与结构化内容的链接已按章节位置生成。

仓库每个文件不超过 95 MB。原 PDF 的恢复方法见 `source/README.md`；若存在 `split_files.json`，运行 `python3 restore_large_files.py` 可逐字节恢复其他大文件并校验。

| 章节 | 原始 PDF 页码 |
| --- | --- |
| [封面、前言与目录 / Front matter](chapters/000_%E5%B0%81%E9%9D%A2%E3%80%81%E5%89%8D%E8%A8%80%E4%B8%8E%E7%9B%AE%E5%BD%95%20_%20Front%20matter/content.md) | 1–9 |
| [1 Introduction to data](chapters/001_1%20Introduction%20to%20data/content.md) | 10–87 |
| [2 Probability](chapters/002_2%20Probability/content.md) | 88–137 |
| [3 Distributions of random variables](chapters/003_3%20Distributions%20of%20random%20variables/content.md) | 138–197 |
| [4 Foundations for inference](chapters/004_4%20Foundations%20for%20inference/content.md) | 198–235 |
| [5 Inference for numerical data](chapters/005_5%20Inference%20for%20numerical%20data/content.md) | 236–289 |
| [6 Simple linear regression](chapters/006_6%20Simple%20linear%20regression/content.md) | 290–329 |
| [7 Multiple linear regression](chapters/007_7%20Multiple%20linear%20regression/content.md) | 330–385 |
| [8 Inference for categorical data](chapters/008_8%20Inference%20for%20categorical%20data/content.md) | 386–467 |
| [Index](chapters/009_Index/content.md) | 468–472 |
