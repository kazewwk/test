# 格式、媒体和更新身份

用户只参考Obsidian制卡策略时，不生成START/END等插件文本；交付用户真正要求的文件。

规范源可使用JSONL：id、type、deck、front／text、answer（完整字符串数组）、criteria、terms、tags、source、image／back_image及媒体路径。必须另存逐独立知识点的覆盖表、真实source_lines、答案与评分位置、明确要求回忆状态及缺口。渲染器负责HTML转义与换行；默认全部Basic；正确处理比较符号、表格及真实媒体。

`.apkg`包含collection.anki2、媒体映射及实际图片，适用于AnkiDroid。用genanki时模型ID和GUID必须稳定；默认所有字段哈希GUID会因改一个字新增笔记，所以用已知稳定键。全新系列可以建立自己的GUID，不能声称其等于旧TXT的未知GUID。首次新建与更新已有系列应区分。

传统APKG不包含整个用户集合替换，不应命名collection.apkg。按章节建牌组、正常合并导入；不包含人为学习进度。实际测试空集合导入和相同／旧系列更新：字段、标签、牌组、媒体SHA、缺图、实际卡数、身份与必要进度样本。不自动反向或批量挖空。

通用脚本依赖genanki。能运行Python anki库时增加临时集合往返导入核验；不能实际运行时明确只做结构检查，不能伪称客户端测试通过。

备份导入文件为UTF-8、HTML、真实Tab分隔三列Front/Back/Tags，无表头，内部换行用br；回读核验字段数、空值与数量。TXT无法自身携图，安卓用户主交付不能依赖手动媒体目录操作。提供可下载真实APKG及简单AnkiDroid导入步骤。

参考：Anki官方手册文本导入（https://docs.ankiweb.net/importing/text-files.html）、牌组导入（https://docs.ankiweb.net/importing/packaged-decks.html）、genanki（https://github.com/kerrickstaley/genanki）。版本行为有疑问应查官方说明并做实际测试，不凭旧说明宣称进度保留。
