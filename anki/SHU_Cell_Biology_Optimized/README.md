# 细胞生物学 Anki 修正版：图片嵌入对应学习卡

[下载安卓修正版 APKG](https://raw.githubusercontent.com/kazewwk/test/main/anki/SHU_Cell_Biology_Optimized/SHU_Cell_Biology_Android_Cards_With_Images_20261010.apkg)（约 36.5 MB）

下载后点开，选择 AnkiDroid，确认导入。图片已内嵌，无须解压或寻找媒体目录。详细步骤和已导入旧图册时的处理见 [ANDROID_IMPORT.md](ANDROID_IMPORT.md)。

2637 张 Basic 问答学习卡，574 张卡直接含配图，678 个教材原图文件；读图题的图在题面，结构、机制和实验说明图在答案。只保留“SHU 细胞生物学（含图）”及 17 个章节子牌组，独立图片卡和图册牌组为 0。52 张综合卡附参考评分要点，免疫补充专题 6 张标为选修。

## 修订与验证

删除上一版单独图片图册的交付入口；在原 596 个学习配图之外，核对并补入 82 个英文原图文件，均有具体学习卡的对应关系。全部 678 个入卡图像与教材仓库原文件 SHA256 一致，没有生成或重绘图片。对原书的旧模型及容易误读处在图前加读图提示。

原生 Anki 26.9.3 后端验证：首次导入为 2637 条笔记及 2637 张卡；重复导入无重复；三个旧版本的学习卡更新均保留 2637 张卡的身份和已有复习状态。旧图册版本的测试先显式删除那一图册，再更新学习卡，符合手机处理说明。APKG 的 678 个媒体文件全部被对应卡片引用，缺失为 0；手机宽度浏览器检查通过。没有在实体安卓设备上运行。

中文正文 447 个原图文件已经逐组对照学习任务核查；本次额外看图核查 124 个英文原图文件并核对其配题。英文 153 个主题组均有来源入口，来源偏移哈希已检查；全量图片初筛和主题覆盖不等同英文全文逐句审校。实际审阅层级列于审计表。

## 逐项记录

- [review_report.md](review_report.md)：逐章数量、事实修订和实际审阅范围。
- `additional_image_bindings.tsv`：中文 447 个正文图文件的对应学习卡或未采用理由。
- `revision_image_bindings.tsv`：本次英文原图直接配入哪一张学习卡；对应 `.py` 文件记录手动判定和读图提示。
- `figure_audit.tsv`：3115 个来源原图文件的出处、哈希、审阅层级和实际学习卡引用。
- `english_coverage.tsv`、`card_changes.tsv`、`source_inventory.tsv`：英文来源、逐卡变更和 3361 个来源文件校验。
- `cards.json`、`new_card_specs.py`、`regenerate_txt.py`：明文卡片与备用 TXT 生成记录。
- `CHECK_REPORT.json`、`apkg_import_test.json`、`apkg_update_test.json`：文件、原图、导入和复习状态验证。

备用 TXT 与 ZIP 用于编辑和桌面兼容；安卓直接用上面的 APKG。原 2440 张题的第一字段保持一致。CELL03-105、CELL06-039 的旧题干含不准确预设，背面已明确纠正并标注“题干::先辨析预设”。综合练习为改编复习题，参考评分不是上海大学官方评分。
