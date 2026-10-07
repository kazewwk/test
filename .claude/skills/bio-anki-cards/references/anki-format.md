# Anki 导入格式速查（官方手册核对版）

本文件是写构建脚本和排查导入问题时查的。日常制卡不用读——`scripts/build_anki.py` 已经按这些规则实现。来源为 Anki 官方手册（docs.ankiweb.net，按 GitHub 源码 ankitects/anki-manual 核对）和 genanki README。

## 1 文本文件导入（.txt/.tsv/.csv）

- UTF-8 纯文本，`#` 开头的行是注释；字段数由第一条数据行决定。
- 头部指令（2.1.54+），每行一条，放文件最顶：
  - `#separator:Tab`（也可 Comma/Semicolon/Pipe/Colon/Space）
  - `#html:true` 字段按 HTML 解释（要用 `<br>`、`<img>`、`<b>` 必须开）
  - `#notetype:名称`、`#deck:父::子` 预设笔记类型/牌组（不存在的牌组会自动创建）
  - `#notetype column:N`、`#deck column:N`、`#tags column:N`、`#guid column:N`（N 从 1 起）——用列按行指定
  - `#tags:tag1 tag2` 给所有笔记加标签；`#columns:…` 列名
- 字段内有换行或分隔符：整个字段用双引号包住，内部 `"` 写成 `""`。更稳的做法是开 HTML、换行写 `<br>`——跨行的 cloze 用引号多行会出错。
- 多种笔记类型放一个文件：用 `#notetype column:`，字段按“第 k 个常规列→第 k 个字段”映射（常规列 = 非 deck/tags/notetype/guid 的列）。本技能为简单起见每种类型一个文件。
- 判重：同一笔记类型 + 第一字段相同视为重复，默认更新其余字段；GUID 列非空时按 GUID 匹配。手册建议把自定义 ID 放第一字段而不是 GUID；本技能用 `#guid column` + 由卡片 id 推导的稳定 GUID，两者都能做到“重复导入即更新”。
- **文本导入不能携带图片**：图片要手动放进 profile 的 `collection.media/`（不能有子目录），字段里只写文件名 `<img src="x.jpg">`。有图的卡用 .apkg。

## 2 笔记类型与模板

- 内置：Basic（1 卡）、Basic (and reversed card)（2 卡）、Basic (optional reversed card)（第 3 字段非空才出反向卡）、Basic (type in the answer)、Cloze（每个 cN 一卡）、Image Occlusion（23.10+）。
- 模板：`{{Field}}` 大小写敏感；`{{FrontSide}}` 只能在背面；`<hr id=answer>` 标答案起点；`{{#F}}…{{/F}}` 非空才显示、`{{^F}}…{{/F}}` 为空才显示；`{{text:F}}` 去 HTML；`{{hint:F}}` 折叠提示；特殊字段 `{{Tags}} {{Deck}} {{Subdeck}} {{Card}}`（别用这些名字当字段名）。
- **正面渲染为空的卡不会生成**——本技能的术语卡反向模板就靠这一点：`Reverse` 字段为空时不出反向卡。
- Cloze：`{{c1::答案}}`、带提示 `{{c1::答案::提示}}`；同号多处同卡隐藏；不同编号各一张卡；`{{c1,2::x}}` 让一处在多张卡上都遮住；2.1.56+ 支持嵌套。Cloze 类型不能加额外模板，要自定义须克隆 Cloze 类型。
- CSS 写在 Styling 区；`.card` 全局；`.night_mode` 前缀适配深色；`img{max-width:…}` 控制图大小。

## 3 .apkg 与 genanki

- 导入 .apkg 是**合并**：同 GUID 的笔记按修改时间更新；23.10+ 导入对话框可选“总是更新 / 从不更新 / 合并笔记类型”；不勾“Import any learning progress”可剥离调度。文件名不要叫 `collection.apkg`（会被当成整个集合替换）。
- genanki：`Model(id, name, fields, templates, css, model_type=Model.CLOZE)`、`Note(model, fields, tags, guid)`、`Deck(id, "父::子")`、`Package([decks]).media_files=[路径]`、`write_to_file()`。
  - model_id/deck_id 要固定（随机生成一次后硬编码，或由名字哈希得出）；每个 Model 唯一。
  - 默认 guid 是所有字段的哈希——改一个字就变新笔记。覆写 `guid` 属性用 `genanki.guid_for(稳定键)` 才能“重复导入即更新”。本技能用卡片 `id`。
  - 字段是 HTML：`< > &` 必须转义，换行用 `<br>`；`media_files` 给路径，字段里只写**文件名**，文件名全局唯一。
  - 标签含空格会抛错（本技能自动换成下划线）。
  - genanki 只在第一个模板的 qfmt 里找 `{{cloze:…}}` 来识别 cloze 卡。
  - 内置 `BASIC_MODEL`、`CLOZE_MODEL` 等叫 “Basic (genanki)”，导入后与 Anki 自带的 Basic 是两种类型；本技能用自己命名的 “Bio 问答 / Bio 术语（可反向）/ Bio 填空”。

## 4 Image Occlusion

23.10+ 内置，是图片版 cloze：在 Add 界面选图、画矩形/椭圆/多边形，每个形状一张卡，模式 Hide All Guess One / Hide One Guess One。字段为 Occlusion、Image、Header、Back Extra、Comments，Occlusion 内容形如 `{{c1::image-occlusion:rect:left=.23:top=.33:width=.20:height=.10}}`。手册没有记载用文本导入或 genanki 生成 IO 笔记的方法；genanki 也没有内置模型。本技能不生成 IO 卡——需要“遮标签认结构”时用图卡的“默画”写法（front 文字描述，图放 back_image），或在 Anki 里手工做少量 IO。

## 5 判重与再导入的实际行为（本技能）

- 同一 `id` 再导入 → 更新字段，保留复习进度。改 `id` → 新笔记，旧的留着（要手动删）。
- 改了牌组名 → 新牌组，旧卡不会搬家；要搬用 Anki 浏览器 Change Deck。
- 删除 JSONL 里的卡不会删 Anki 里的卡。
