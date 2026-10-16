# 合成生物学 (刘建忠)

解析：MinerU 4.0.12 Advanced（最高精度），Colab Tesla T4，本地模型。

原始 PDF 268 页；源 SHA-256：`6dfc7589694af26cff683bdb66f86dfea5787682d9569f6ab88f531ef6ebcd63`。

[完整内容](book.md) · [结构化结果](structured_content.json) · [逐页映射](page_map.json) · [原始 PDF](source/) · [校验记录](validation.json)

FULL 内容视图保留模型识别出的页眉、页脚、页码、边栏、脚注、图片、公式和表格；原 PDF 字节完整保留。`source_images/` 另存 PDF 中嵌入的光栅图像；矢量内容仍完整保留在原 PDF 中。

`raw/` 是逐批原始 MinerU 输出及素材。章节 JSON 内的 `image_path` 相对于本书目录；章节 Markdown 与结构化内容的链接已按章节位置生成。

仓库每个文件不超过 95 MB。原 PDF 的恢复方法见 `source/README.md`；若存在 `split_files.json`，运行 `python3 restore_large_files.py` 可逐字节恢复其他大文件并校验。

| 章节 | 原始 PDF 页码 |
| --- | --- |
| [封面、前言与目录 / Front matter](chapters/000_%E5%B0%81%E9%9D%A2%E3%80%81%E5%89%8D%E8%A8%80%E4%B8%8E%E7%9B%AE%E5%BD%95%20_%20Front%20matter/content.md) | 1–10 |
| [第一章概论](chapters/001_%E7%AC%AC%E4%B8%80%E7%AB%A0%E6%A6%82%E8%AE%BA/content.md) | 11–23 |
| [第二章元件、装置和途径的合成](chapters/002_%E7%AC%AC%E4%BA%8C%E7%AB%A0%E5%85%83%E4%BB%B6%E3%80%81%E8%A3%85%E7%BD%AE%E5%92%8C%E9%80%94%E5%BE%84%E7%9A%84%E5%90%88%E6%88%90/content.md) | 24–66 |
| [第三章合成酶学](chapters/003_%E7%AC%AC%E4%B8%89%E7%AB%A0%E5%90%88%E6%88%90%E9%85%B6%E5%AD%A6/content.md) | 67–95 |
| [第四章合成生物系统](chapters/004_%E7%AC%AC%E5%9B%9B%E7%AB%A0%E5%90%88%E6%88%90%E7%94%9F%E7%89%A9%E7%B3%BB%E7%BB%9F/content.md) | 96–143 |
| [第五章合成基因线路](chapters/005_%E7%AC%AC%E4%BA%94%E7%AB%A0%E5%90%88%E6%88%90%E5%9F%BA%E5%9B%A0%E7%BA%BF%E8%B7%AF/content.md) | 144–177 |
| [第六章放线菌合成生物学](chapters/006_%E7%AC%AC%E5%85%AD%E7%AB%A0%E6%94%BE%E7%BA%BF%E8%8F%8C%E5%90%88%E6%88%90%E7%94%9F%E7%89%A9%E5%AD%A6/content.md) | 178–198 |
| [第七章酵母合成生物学](chapters/007_%E7%AC%AC%E4%B8%83%E7%AB%A0%E9%85%B5%E6%AF%8D%E5%90%88%E6%88%90%E7%94%9F%E7%89%A9%E5%AD%A6/content.md) | 199–232 |
| [第八章医学合成生物学](chapters/008_%E7%AC%AC%E5%85%AB%E7%AB%A0%E5%8C%BB%E5%AD%A6%E5%90%88%E6%88%90%E7%94%9F%E7%89%A9%E5%AD%A6/content.md) | 233–259 |
| [第九章合成微生物群](chapters/009_%E7%AC%AC%E4%B9%9D%E7%AB%A0%E5%90%88%E6%88%90%E5%BE%AE%E7%94%9F%E7%89%A9%E7%BE%A4/content.md) | 260–268 |
