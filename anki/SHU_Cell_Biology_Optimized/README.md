# 细胞生物学 Anki 优化版（2026-10-09）

2637 张 Basic 问答卡，223 幅教材原图；52 张综合卡附评分要点（36 张原卡完善、16 张新增），另有 6 张免疫选修卡。完整 ZIP 包含离线图片；单独 TXT 不包含图片字节。

[下载完整导入包（TXT + 图片）](SHU_Cell_Biology_Optimized_20261009_with_media.zip)

## 桌面 Anki 导入

1. 解压完整 ZIP。把 `collection.media` 内的 **223 个 JPG 文件**复制到当前 Anki 用户资料的 `collection.media` 中。复制图片文件，避免再嵌套一层文件夹。
2. 导入 `SHU_Cell_Biology_Optimized_20261009.txt`：UTF-8、Tab 分隔、允许 HTML、Basic（基础）笔记类型；第 1 列 Front，第 2 列 Back，第 3 列 Tags。
3. 已导入原 2440 张时，选择**原来同一个笔记类型**，重复处理选“更新”，匹配范围选“笔记类型”。原卡正面保持一致。已自行改写正面或更换笔记类型的笔记，不能仅凭本 TXT 自动匹配。
4. 导入后运行 Anki 的“工具 → 检查媒体”，再同步到手机。浏览器打开 `preview.html` 可离线检查示例卡和图片。

首次导入应得到 2637 条笔记、2637 张卡；从原版更新应保留 2440 条并新增 197 条。请使用单向 Basic，反向类型会生成更多卡。

媒体目录常见位置：Windows 为 `%APPDATA%\Anki2\你的资料名\collection.media`；macOS 为 `~/Library/Application Support/Anki2/你的资料名/collection.media`；Linux 为 `~/.local/share/Anki2/你的资料名/collection.media`。

实际使用 Anki 26.9.3 后端测试通过：原 2440 条笔记 ID、GUID、复习状态均保留；重复导入未产生重复卡；223 幅图片没有缺失或闲置引用。测试在临时资料中完成，未访问用户的 Anki 数据。

## 内容与索引

- `review_report.md`：逐章数量、21 项事实/条件修订、6 项解释补充、36 项评分补充及实际审阅范围。
- `english_coverage.tsv`：153 个英文主题组与卡片的对应关系。
- `figure_audit.tsv`：3115 幅图片的原路径、哈希、复核层级、采用情况与来源。
- `card_changes.tsv`：逐卡变更；`source_inventory.tsv`：3361 个来源文件的清单与校验。
- `cards.json`：明文制卡记录；运行 `python regenerate_txt.py` 可重新导出。
- `CHECK_REPORT.json`、`anki_import_test.json`：格式/图片检查与真实 Anki 后端导入测试。

全部图片来自教材原文件，没有重绘或使用图像生成模型。全量缩略图初筛与入卡图放大复核采用不同审阅层级；主题覆盖不代表全书 OCR 已逐字校勘。

原卡 `CELL03-105`、`CELL06-039` 的旧题干含不准确预设，背面已明确纠正，标签为 `题干::先辨析预设`。保留第一字段是为了支持原卡更新；应记忆背面的正确结论。

免疫选修卡可搜索 `范围::选修` 后暂停；综合练习可搜索 `深度::L4`。习题经过改编，评分要点为复习参考，不是上海大学官方真题或官方评分。
