# 微生物学(101计划) (邓子新,陈峰,陈向东)

解析：MinerU 4.0.12 Advanced（最高精度），Colab Tesla T4，本地模型。

原始 PDF 710 页；源 SHA-256：`fc62282b614b16800a10b7b51efa2a395417c902544b3ee8454016938b613599`。

[完整内容](book.md) · [结构化结果](structured_content.json) · [逐页映射](page_map.json) · [原始 PDF](source/) · [校验记录](validation.json)

FULL 内容视图保留模型识别出的页眉、页脚、页码、边栏、脚注、图片、公式和表格；原 PDF 字节完整保留。`source_images/` 另存 PDF 中嵌入的光栅图像；矢量内容仍完整保留在原 PDF 中。

`raw/` 是逐批原始 MinerU 输出及素材。章节 JSON 内的 `image_path` 相对于本书目录；章节 Markdown 与结构化内容的链接已按章节位置生成。

仓库每个文件不超过 95 MB。原 PDF 的恢复方法见 `source/README.md`；若存在 `split_files.json`，运行 `python3 restore_large_files.py` 可逐字节恢复其他大文件并校验。

| 章节 | 原始 PDF 页码 |
| --- | --- |
| [封面、序、前言与目录](chapters/000_%E5%B0%81%E9%9D%A2%E3%80%81%E5%BA%8F%E3%80%81%E5%89%8D%E8%A8%80%E4%B8%8E%E7%9B%AE%E5%BD%95/content.md) | 1–17 |
| [1 绪论](chapters/001_1%20%E7%BB%AA%E8%AE%BA/content.md) | 18–40 |
| [2 微生物的显微观察与纯培养](chapters/002_2%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E6%98%BE%E5%BE%AE%E8%A7%82%E5%AF%9F%E4%B8%8E%E7%BA%AF%E5%9F%B9%E5%85%BB/content.md) | 41–63 |
| [3 原核生物的结构与功能](chapters/003_3%20%E5%8E%9F%E6%A0%B8%E7%94%9F%E7%89%A9%E7%9A%84%E7%BB%93%E6%9E%84%E4%B8%8E%E5%8A%9F%E8%83%BD/content.md) | 64–95 |
| [4 真核微生物的结构与功能](chapters/004_4%20%E7%9C%9F%E6%A0%B8%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E7%BB%93%E6%9E%84%E4%B8%8E%E5%8A%9F%E8%83%BD/content.md) | 96–118 |
| [5 病毒](chapters/005_5%20%E7%97%85%E6%AF%92/content.md) | 119–155 |
| [6 微生物的营养与培养基](chapters/006_6%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E8%90%A5%E5%85%BB%E4%B8%8E%E5%9F%B9%E5%85%BB%E5%9F%BA/content.md) | 156–187 |
| [7 微生物的代谢](chapters/007_7%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E4%BB%A3%E8%B0%A2/content.md) | 188–220 |
| [8 微生物的生长繁殖及其控制](chapters/008_8%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E7%94%9F%E9%95%BF%E7%B9%81%E6%AE%96%E5%8F%8A%E5%85%B6%E6%8E%A7%E5%88%B6/content.md) | 221–255 |
| [9 微生物的遗传与育种](chapters/009_9%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E9%81%97%E4%BC%A0%E4%B8%8E%E8%82%B2%E7%A7%8D/content.md) | 256–287 |
| [10 微生物基因表达调控](chapters/010_10%20%E5%BE%AE%E7%94%9F%E7%89%A9%E5%9F%BA%E5%9B%A0%E8%A1%A8%E8%BE%BE%E8%B0%83%E6%8E%A7/content.md) | 288–326 |
| [11 微生物与基因工程](chapters/011_11%20%E5%BE%AE%E7%94%9F%E7%89%A9%E4%B8%8E%E5%9F%BA%E5%9B%A0%E5%B7%A5%E7%A8%8B/content.md) | 327–360 |
| [12 微生物的系统发育与分类鉴定](chapters/012_12%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E7%B3%BB%E7%BB%9F%E5%8F%91%E8%82%B2%E4%B8%8E%E5%88%86%E7%B1%BB%E9%89%B4%E5%AE%9A/content.md) | 361–396 |
| [13 微生物的生态](chapters/013_13%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%9A%84%E7%94%9F%E6%80%81/content.md) | 397–431 |
| [14 微生物物种多样性](chapters/014_14%20%E5%BE%AE%E7%94%9F%E7%89%A9%E7%89%A9%E7%A7%8D%E5%A4%9A%E6%A0%B7%E6%80%A7/content.md) | 432–494 |
| [15 感染与免疫](chapters/015_15%20%E6%84%9F%E6%9F%93%E4%B8%8E%E5%85%8D%E7%96%AB/content.md) | 495–547 |
| [16 合成生物学](chapters/016_16%20%E5%90%88%E6%88%90%E7%94%9F%E7%89%A9%E5%AD%A6/content.md) | 548–582 |
| [17 农业微生物学](chapters/017_17%20%E5%86%9C%E4%B8%9A%E5%BE%AE%E7%94%9F%E7%89%A9%E5%AD%A6/content.md) | 583–616 |
| [18 食品微生物学](chapters/018_18%20%E9%A3%9F%E5%93%81%E5%BE%AE%E7%94%9F%E7%89%A9%E5%AD%A6/content.md) | 617–660 |
| [19 工业微生物学](chapters/019_19%20%E5%B7%A5%E4%B8%9A%E5%BE%AE%E7%94%9F%E7%89%A9%E5%AD%A6/content.md) | 661–681 |
| [名词索引](chapters/020_%E5%90%8D%E8%AF%8D%E7%B4%A2%E5%BC%95/content.md) | 682–697 |
| [微生物中文名索引](chapters/021_%E5%BE%AE%E7%94%9F%E7%89%A9%E4%B8%AD%E6%96%87%E5%90%8D%E7%B4%A2%E5%BC%95/content.md) | 698–702 |
| [微生物学名索引与封底](chapters/022_%E5%BE%AE%E7%94%9F%E7%89%A9%E5%AD%A6%E5%90%8D%E7%B4%A2%E5%BC%95%E4%B8%8E%E5%B0%81%E5%BA%95/content.md) | 703–710 |
