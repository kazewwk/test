# 生物化学(下册) (昌增益, 施一公, 王新泉)

解析：MinerU 4.0.12 Advanced（最高精度），Colab Tesla T4，本地模型。

原始 PDF 587 页；源 SHA-256：`0d937c719970e74b25f98040b0d2c4a24cd300835b04b4554d15960c77bb16f9`。

[完整内容](book.md) · [结构化结果](structured_content.json) · [逐页映射](page_map.json) · [原始 PDF](source/) · [校验记录](validation.json)

FULL 内容视图保留模型识别出的页眉、页脚、页码、边栏、脚注、图片、公式和表格；原 PDF 字节完整保留。`source_images/` 另存 PDF 中嵌入的光栅图像；矢量内容仍完整保留在原 PDF 中。

`raw/` 是逐批原始 MinerU 输出及素材。章节 JSON 内的 `image_path` 相对于本书目录；章节 Markdown 与结构化内容的链接已按章节位置生成。

仓库每个文件不超过 95 MB。原 PDF 的恢复方法见 `source/README.md`；若存在 `split_files.json`，运行 `python3 restore_large_files.py` 可逐字节恢复其他大文件并校验。

| 章节 | 原始 PDF 页码 |
| --- | --- |
| [封面、前言与目录](chapters/000_%E5%B0%81%E9%9D%A2%E3%80%81%E5%89%8D%E8%A8%80%E4%B8%8E%E7%9B%AE%E5%BD%95/content.md) | 1–17 |
| [第III篇 糖类和脂质的结构与功能·分篇页](chapters/001_%E7%AC%ACIII%E7%AF%87%20%E7%B3%96%E7%B1%BB%E5%92%8C%E8%84%82%E8%B4%A8%E7%9A%84%E7%BB%93%E6%9E%84%E4%B8%8E%E5%8A%9F%E8%83%BD%C2%B7%E5%88%86%E7%AF%87%E9%A1%B5/content.md) | 18–19 |
| [14 糖类](chapters/002_14%20%E7%B3%96%E7%B1%BB/content.md) | 20–60 |
| [15 脂质](chapters/003_15%20%E8%84%82%E8%B4%A8/content.md) | 61–95 |
| [第IV篇 生物体内的物质与能量代谢·分篇页](chapters/004_%E7%AC%ACIV%E7%AF%87%20%E7%94%9F%E7%89%A9%E4%BD%93%E5%86%85%E7%9A%84%E7%89%A9%E8%B4%A8%E4%B8%8E%E8%83%BD%E9%87%8F%E4%BB%A3%E8%B0%A2%C2%B7%E5%88%86%E7%AF%87%E9%A1%B5/content.md) | 96–97 |
| [16 代谢总论](chapters/005_16%20%E4%BB%A3%E8%B0%A2%E6%80%BB%E8%AE%BA/content.md) | 98–143 |
| [17 糖类分解代谢](chapters/006_17%20%E7%B3%96%E7%B1%BB%E5%88%86%E8%A7%A3%E4%BB%A3%E8%B0%A2/content.md) | 144–180 |
| [18 柠檬酸循环](chapters/007_18%20%E6%9F%A0%E6%AA%AC%E9%85%B8%E5%BE%AA%E7%8E%AF/content.md) | 181–213 |
| [19 氧化磷酸化](chapters/008_19%20%E6%B0%A7%E5%8C%96%E7%A3%B7%E9%85%B8%E5%8C%96/content.md) | 214–256 |
| [20 光合磷酸化](chapters/009_20%20%E5%85%89%E5%90%88%E7%A3%B7%E9%85%B8%E5%8C%96/content.md) | 257–283 |
| [21 糖类合成代谢](chapters/010_21%20%E7%B3%96%E7%B1%BB%E5%90%88%E6%88%90%E4%BB%A3%E8%B0%A2/content.md) | 284–319 |
| [22 脂肪酸分解代谢](chapters/011_22%20%E8%84%82%E8%82%AA%E9%85%B8%E5%88%86%E8%A7%A3%E4%BB%A3%E8%B0%A2/content.md) | 320–346 |
| [23 脂质合成](chapters/012_23%20%E8%84%82%E8%B4%A8%E5%90%88%E6%88%90/content.md) | 347–396 |
| [24 氨基酸分解代谢](chapters/013_24%20%E6%B0%A8%E5%9F%BA%E9%85%B8%E5%88%86%E8%A7%A3%E4%BB%A3%E8%B0%A2/content.md) | 397–442 |
| [25 生物固氮及氨基酸生成](chapters/014_25%20%E7%94%9F%E7%89%A9%E5%9B%BA%E6%B0%AE%E5%8F%8A%E6%B0%A8%E5%9F%BA%E9%85%B8%E7%94%9F%E6%88%90/content.md) | 443–492 |
| [26 核苷酸的合成与分解代谢](chapters/015_26%20%E6%A0%B8%E8%8B%B7%E9%85%B8%E7%9A%84%E5%90%88%E6%88%90%E4%B8%8E%E5%88%86%E8%A7%A3%E4%BB%A3%E8%B0%A2/content.md) | 493–535 |
| [27 哺乳动物代谢整合与激素调控](chapters/016_27%20%E5%93%BA%E4%B9%B3%E5%8A%A8%E7%89%A9%E4%BB%A3%E8%B0%A2%E6%95%B4%E5%90%88%E4%B8%8E%E6%BF%80%E7%B4%A0%E8%B0%83%E6%8E%A7/content.md) | 536–578 |
| [后记](chapters/017_%E5%90%8E%E8%AE%B0/content.md) | 579–581 |
| [索引与封底](chapters/018_%E7%B4%A2%E5%BC%95%E4%B8%8E%E5%B0%81%E5%BA%95/content.md) | 582–587 |
