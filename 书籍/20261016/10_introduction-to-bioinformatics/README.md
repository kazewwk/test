# Introduction to bioinformat_

解析：MinerU 4.0.12 Advanced（最高精度），Colab Tesla T4，本地模型。

原始 PDF 440 页；源 SHA-256：`5ea36c3c18b008eac96f2e10b74ebab3a78d31223a0f475e8f4c478c5f98b649`。

[完整内容](book.md) · [结构化结果](structured_content.json) · [逐页映射](page_map.json) · [原始 PDF](source/) · [校验记录](validation.json)

FULL 内容视图保留模型识别出的页眉、页脚、页码、边栏、脚注、图片、公式和表格；原 PDF 字节完整保留。`source_images/` 另存 PDF 中嵌入的光栅图像；矢量内容仍完整保留在原 PDF 中。

`raw/` 是逐批原始 MinerU 输出及素材。章节 JSON 内的 `image_path` 相对于本书目录；章节 Markdown 与结构化内容的链接已按章节位置生成。

仓库每个文件不超过 95 MB。原 PDF 的恢复方法见 `source/README.md`；若存在 `split_files.json`，运行 `python3 restore_large_files.py` 可逐字节恢复其他大文件并校验。

| 章节 | 原始 PDF 页码 |
| --- | --- |
| [封面、前言与目录 / Front matter](chapters/000_%E5%B0%81%E9%9D%A2%E3%80%81%E5%89%8D%E8%A8%80%E4%B8%8E%E7%9B%AE%E5%BD%95%20_%20Front%20matter/content.md) | 1–24 |
| [1 Introduction](chapters/001_1%20Introduction/content.md) | 25–84 |
| [2 Genome organization and evolution](chapters/002_2%20Genome%20organization%20and%20evolution/content.md) | 85–136 |
| [3 Scientific publications and archives: media, content, and access](chapters/003_3%20Scientific%20publications%20and%20archives_%20media/content.md) | 137–176 |
| [4 Archives and information retrieval](chapters/004_4%20Archives%20and%20information%20retrieval/content.md) | 177–214 |
| [5 Alignments and phylogenetic trees](chapters/005_5%20Alignments%20and%20phylogenetic%20trees/content.md) | 215–265 |
| [6 Structural bioinformatics and drug discovery](chapters/006_6%20Structural%20bioinformatics%20and%20drug%20discover/content.md) | 266–329 |
| [7 Introduction to systems biology](chapters/007_7%20Introduction%20to%20systems%20biology/content.md) | 330–345 |
| [8 Metabolic pathways](chapters/008_8%20Metabolic%20pathways/content.md) | 346–380 |
| [9 Gene expression and regulation](chapters/009_9%20Gene%20expression%20and%20regulation/content.md) | 381–421 |
| [INDEX](chapters/010_INDEX/content.md) | 422–440 |
