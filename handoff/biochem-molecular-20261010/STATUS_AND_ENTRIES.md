# 状态与文件入口

核验时间：2026-10-10 12:51 UTC。固定资料提交：8e6b33c6d2828b90972196c4d21fc35b05af9207。
本表为已保存快照的入口，不是原执行会话已暂停的证明。

## 深度重制状态

来源：[本轮说明](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/README.md)、[组装检查点](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/audit/assembly-checkpoint.json)。

- 生化就绪：B01、B02、B03、B04、B05、B06、B10、B14、B15、B16、B17、B18、B19、B20、B21、B22、B28、B31。
- 生化待完成：B07、B08、B09、B11、B12、B13、B23、B24、B25、B26、B27、B29、B30、B32、B33、B34、B35、B36。
- 分子就绪：M03、M07、M08、M10。
- 分子待完成：M01、M02、M04、M05、M06、M09、M11。
- M09 为访问受限，必须保持未完成并遵守 [限制记录](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/restrictions.json)。

“就绪”是已有记录的分类，不是本次交接独立验证出的全部内容正确或无遗漏结论。各章源疑点和 gaps 仍须保留；不能机械清空 complete: false 或把 unresolved 当已完成。未决来源单元 192 不等于剩余全书知识点总数。

## 接手阅读顺序

1. [深度重制说明](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/README.md)。
2. [章节源文件目录](https://github.com/kazewwk/test/tree/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/chapters)：22 个章节 JSON，保留原结构、来源定位、知识点/卡片 ID、gaps 和审查记录。不要将此目录没有的待完成章推定为已制作。
3. [组装检查点](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/audit/assembly-checkpoint.json)：当前记录数和剩余章节。
4. [源阅读清单](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/audit/source-reading-inventory.json)：其源提交为 d443ed18fd7b95569ebcbfc3b0d54666a6607687；统计 47 文档、94520 行、41087 个机械来源块。这些统计和 read_batches 不能替代英文逐句/原图视觉/表格逐格的实际阅读证据。
5. [部分导出测试](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/audit/partial-packaging-test.json)：1027 笔记及卡、7 牌组、433 媒体；原生导入通过、重导重复 0；实体安卓未测试。需重新定位测试包，不把旧 APKG 认作本轮 4450 条成果。
6. [旧版诊断](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/audit/previous-diagnosis.json)：解释为何需要深度重制，长度只作诊断，不是质量评分。
7. [B22 数学校核](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/audit/B22-math-check.json)：保留章节专门审计。
8. [组装实现入口](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/deep/assemble.py)：先读懂输入/路径/身份规则再运行；默认最终导出门槛不可伪造通过。检查点模式不能把未完范围改称完整。

## 原始资料与图片

- [教材目录](https://github.com/kazewwk/test/tree/8e6b33c6d2828b90972196c4d21fc35b05af9207/书籍)：重点核对 10_生物化学_上册_朱圣庚_徐长法、11_生物化学_下册_朱圣庚_徐长法、09_现代分子生物学；实际版次、章名、范围以文件与来源清单为准。
- [英文及辅助生化资料入口](https://github.com/kazewwk/test/tree/8e6b33c6d2828b90972196c4d21fc35b05af9207/书籍/02_生物化学原理)。
- [英文及辅助分子资料入口](https://github.com/kazewwk/test/tree/8e6b33c6d2828b90972196c4d21fc35b05af9207/书籍/03_基因的分子生物学_第七版)。
- [已登记源文件](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/source-files.json) 与 [逐行源文件清单](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/source-files.jsonl)。
- [教材导入清单目录](https://github.com/kazewwk/test/tree/8e6b33c6d2828b90972196c4d21fc35b05af9207/books)：含 manifest、extracted-manifest、SHA256SUMS 等。存在与哈希校验不等于读过。
- [现有媒体目录](https://github.com/kazewwk/test/tree/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/media)、[补充源图](https://github.com/kazewwk/test/tree/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/source-images)、[媒体清单](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/media-manifest.jsonl)。
- [历史逐图核验](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/image-review.jsonl)、[源限制](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/source-limitations.jsonl)、[源勘误](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/source-errata.jsonl)。

以上目录入口已核验存在；本次未逐个重读教材、图像和全部章节 JSON，未重新裁定各旧审计结论。使用受限章时，限制记录优先；不得因为目录可见就重新读取受限内容。

## 旧交付与身份迁移

- [历史版本说明](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/README.md)。
- [旧 APKG](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/SHU_Biology_AnkiDroid.apkg)：3920 卡旧版本，不能当作本轮深度重制完成包。
- [旧生化 TXT](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/SHU_2027_Biochemistry_2514_Basic.txt)、[旧分子 TXT](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/SHU_Molecular_Anki.txt)：仅用于核对旧身份/题面与迁移，文件名含 2027 不证明考试年份。
- [旧原生导入报告](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/anki-import-check.json)、[旧 APKG 检查](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/ankidroid-apkg-check.json)、[旧显示抽查](https://github.com/kazewwk/test/blob/8e6b33c6d2828b90972196c4d21fc35b05af9207/anki/audit/card-rendering-check.json)。

旧版导入证据只适用于其测试对象，不能继承为新重制包的验收证明。原 TXT 没有可靠 GUID 自动更新保证；新旧任务含义变化时需要稳定的新版本身份及逐项迁移映射。先备份和测试，不删除、重置或“忘记”旧卡。

## 首批包的验收闸门

1. 确认原制作会话暂停及最终保存提交；比较本快照之后新增文件，避免遗漏未提交的 B24 等正在核验成果。对“B12自由基重排”的会话表述不要自行当作 B12 章节已经完成，必须看保存文件。
2. 逐章检查内容证据、跨章依赖与192个未决单元，确定可独立交付的明确范围。
3. 检查题干确实要求各知识点、完整答案包含其机制/条件/例外、必答点可逐项判定；仅标签或来源提及不计回忆覆盖。
4. 核验所有引用媒体存在并内嵌、所需真实图片足够清晰，手机排版可读；书→章分组，无独立图集。
5. 导出 Basic APKG、三列 UTF-8 TSV、覆盖表、缺口表与报告；核对 ZIP、SQLite、笔记/卡/模板、媒体、稳定身份。
6. 原生 Anki 空库导入与重导；检查重复和媒体，专门验证旧版本迁移及模拟进度保护。没有 AnkiDroid 实机测试就明确说明。
7. 能验收则先交首批可背包并标清剩余范围；不能则报告阻塞，不用样本、旧包或结构脚本替代。

本交接不授权恢复原会话继续生产；接手 AI 应先给核验结果与计划，按用户后续明确要求继续。任何范围删减需要先询问用户。
