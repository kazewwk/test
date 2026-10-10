本目录保存按完整教材覆盖要求重新制作的卡片源、逐知识点台账和审查记录。仓库原有 `SHU_Biology_AnkiDroid.apkg` 是此前版本，不代表本轮已完成重制。

最终交付为一个内嵌真实图片的 AnkiDroid `.apkg`；UTF-8 三列 Tab 文件仅作备用。新卡全部是 Basic，背面显示完整答案和必答点，并标明依据、卡片 ID 和知识点 ID。

`chapters/` 只保存已经完成实际阅读、可靠知识改写和双向核查的章节。源材料错误、不可读结构与缺失条件在各章 `gaps` 中保留；`complete: false` 表示仍有这些真实源疑点，不等于把未读正文宣称为完成。

`audit/assembly-checkpoint.json` 明列其余未完章节与跨章依赖。`audit/partial-packaging-test.json` 是已完成章节的格式与媒体测试，不能证明其余章节覆盖或无学术错误。

`assemble.py` 汇总已审稿卡片、核对真实行号和 1-based 答案／评分位置、保留跨章来源，并复制原图及核验哈希。默认阻止在章节未完成时进行最终导出；`--checkpoint` 只用于明确标为未完成的检查点。实际制卡由逐章审读完成，程序无法由卡数自动证明语义覆盖。

`make-biology-anki.skill` 是更新后的仓库 skill 包；本会话没有修改云端已安装 skill 的写入接口。
