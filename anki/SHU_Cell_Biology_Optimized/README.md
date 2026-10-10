# 细胞生物学 Anki 含图版（2026-10-10）

[安卓完整包：下载后用 AnkiDroid 打开](https://media.githubusercontent.com/media/kazewwk/test/main/anki/SHU_Cell_Biology_Optimized/SHU_Cell_Biology_Android_All_Images_20261010.apkg)

2637 张 Basic 问答学习卡，596 个教材原图文件已嵌在对应卡片中；另有默认暂停的491页教材图册，收录仓库全部3115个原图文件。52张综合卡附参考评分要点，免疫补充专题6张标为选修。

## 手机导入

下载上面的 `.apkg`（约224MB），在手机“下载”里点开，选择 AnkiDroid 并确认导入。无需解压或寻找媒体目录。也可在 AnkiDroid 牌组列表的菜单中选择“导入”，打开该文件。

学习牌组叫“SHU 细胞生物学（含图）”；图册叫“教材图册（查阅，已暂停）”。图册不进入日常复习，可在“浏览卡片”中搜索 `教材图册` 阅读。3115是原文件数，包含大图裁片、表格及前言图片，不等于3115道独立试题。

[较小的学习包（约29MB）](SHU_Cell_Biology_Android_20261010.apkg)含同一套2637张学习卡和596个学习配图。完整包已包含其全部内容。详细步骤见 [ANDROID_IMPORT.md](ANDROID_IMPORT.md)。桌面 Anki 也可直接导入这两个 APKG。

## 更新和验证

原生 Anki 26.9.3 后端已测试：首次导入、重复导入无重复、上一版APKG更新保留2637张卡片身份和已有复习状态；完整包491页图册导入后保持暂停。学习图片596/596、完整原图3115/3115与教材仓库字节哈希一致，缺失引用为0。测试没有访问用户资料，没有在实体安卓设备运行。

中文正文447个原图文件已逐组对照卡片核验；596个学习配图均经过主题和图题对应复核。其他英文图片目前属于初筛及图册查阅，尚未逐标签深度核验。英文153个主题组均有卡片来源入口，来源偏移哈希已检查；主题覆盖不等同英文全文逐句审校。

发现的原教材错误或旧模型（如减数分裂混用倍性和DNA量、固定30nm纤维层级、p16靶标、旧核孔中央栓模型）在图前附读图提示。全部使用教材原图，没有生成插图。

## 内容记录

- [review_report.md](review_report.md)：逐章数量、事实修订和实际审阅范围。
- `additional_image_bindings.tsv`：中文447个正文原图文件的逐项配题或图册处置；`additional_image_bindings.py`：手动判定及读图提示。
- `figure_audit.tsv`：3115个原图文件的出处、哈希、审阅层级和学习卡引用。
- `gallery_manifest.json`：491页图册及所有原图的对应关系；`english_coverage.tsv`：153个英文主题组与卡片来源对应。
- `card_changes.tsv`、`source_inventory.tsv`：逐卡变更和3361个来源文件校验。
- `cards.json`、`new_card_specs.py`：明文制卡记录；`regenerate_txt.py`可重新导出备用TXT。
- `CHECK_REPORT.json`、`apkg_import_test.json`、`full_apkg_import_test.json`、`apkg_update_test.json`：包结构、原图哈希、导入和复习状态测试。

备用TXT与ZIP留作编辑和桌面兼容用途；手机直接使用APKG。TXT采用UTF-8、Tab、HTML、Basic，原2440题第一字段保持一致，支持同笔记类型下按第一字段更新；已自行改题干或换类型的笔记需自行匹配。单独TXT不含图片字节。

原卡CELL03-105、CELL06-039的旧题干含不准确预设，答案已明确纠正并标注“题干::先辨析预设”。综合练习为改编复习题，参考评分不是上海大学官方评分。
