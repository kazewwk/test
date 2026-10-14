# 分子制卡

以朱玉贤《现代分子生物学》为主干，把 Watson《基因的分子生物学》第七版中译本、Campbell Biology 第 16–21 章、Lehninger *Principles of Biochemistry* 第 9、24–28 章的对应内容插入各章，便于制作卡片。

## 目录结构

- 每个 `NN_第N章_…/` 对应《现代分子生物学》一章：`NN_第N章_….md` 为合并文本，`images/` 为该章引用的全部图片（四本书的都在），链接为相对路径 `images/…`。
- `00_中文教材前置内容/`：《现代分子生物学》与 Watson 中译本的目录、前言。
- `99_附录_无对应章节/`：Watson 附录 1（模式生物）、Watson 索引与版权页、《现代分子生物学》书末索引。
- `对应关系.json`：机器可读的对应表。

## 合并规则

1. 《现代分子生物学》原文完整保留，顺序不变。
2. 三个来源以“片段”为单位插在对应中文二级节（N.M）的**末尾**：Watson 按章或按大节拆分（第 7、13、15、18、19、20 章拆分，其余整章）；Campbell 按 Concept；Lehninger 按 §N.M 小节。
3. 块标记：Watson `<!-- W-BEGIN … -->`，标题 `### 【中文对照 Watson 第N章：…】`，内部标题降为 `#### [W] …`；Campbell `<!-- C-BEGIN … -->`、Lehninger `<!-- L-BEGIN … -->`，标题 `### 【英文对应 …】`，内部标题 `#### [EN] …`。可按标记整体检索或剔除。
4. 同一插入点的顺序：Watson → Campbell → Lehninger；同一来源按原书顺序。
5. Campbell、Lehninger 各章的章首导言放在对应中文章开头；Campbell Review、Lehninger Key Terms/习题/简答、Watson 小结/参考文献/习题（附录 2 答案附后）放在对应中文章末尾。
6. 每章开头有一段“本章插入内容”清单。

对应关系按主题人工判定；觉得某处放得不合适，改 `scripts/build_molbio_cards.py` 里的 `W_SPLITS/W_WHOLE/C_MAP/L_MAP` 后重新运行即可。

## 章节对应表

| 中文章 | 插入内容 | 章首/章末 | 图片 |
| --- | --- | --- | ---: |
| [01_第1章_绪论](01_第1章_绪论/01_第1章_绪论.md) | Watson 第1章「孟德尔学派的世界观」；Watson 第2章「核酸承载遗传信息」；Campbell Concept 16.1 | Watson 第1章；Watson 第2章 | 60 |
| [02_第2章_染色体与DNA](02_第2章_染色体与DNA/02_第2章_染色体与DNA.md) | Watson 第3章「弱化学键和强化学键的重要性」；Watson 第4章「DNA的结构」；Watson 第8章「基因组结构、染色质和核小体」；Watson 第9章「DNA的复制」；Watson 第10章「DNA的突变和修复」；Watson 第11章「分子水平上的同源重组」；Watson 第12章「位点特异性重组和DNA转座」；Campbell Concept 16.2；Campbell Concept 16.3；Campbell Concept 17.5；Campbell Concept 21.4；Lehninger §24.1；Lehninger §24.2；Lehninger §24.3；Lehninger §25.1；Lehninger §25.2；Lehninger §25.3 | Campbell 第16章；Lehninger 第24章；Lehninger 第25章；Watson 第3章；Watson 第4章；Watson 第8章；Watson 第9章；Watson 第10章；Watson 第11章；Watson 第12章 | 614 |
| [03_第3章_生物信息的传递_上_从DNA到RNA](03_第3章_生物信息的传递_上_从DNA到RNA/03_第3章_生物信息的传递_上_从DNA到RNA.md) | Watson 第5章「RNA的结构和功能多样性」；Watson 第13章「转录机制（章首）」；Watson 第13章「真核生物的转录」；Watson 第14章「RNA剪接」；Watson 第15章「信使 RNA」；Watson 第17章「生命起源和早期进化」；Campbell Concept 17.1；Campbell Concept 17.2；Campbell Concept 17.3；Lehninger §26.1；Lehninger §26.2；Lehninger §26.4 | Campbell 第17章；Lehninger 第26章；Watson 第5章；Watson 第13章；Watson 第14章；Watson 第17章 | 291 |
| [04_第4章_生物信息的传递_下_从mRNA到蛋白质](04_第4章_生物信息的传递_下_从mRNA到蛋白质/04_第4章_生物信息的传递_下_从mRNA到蛋白质.md) | Watson 第6章「蛋白质的结构」；Watson 第15章「翻译（章首）」；Watson 第15章「转运RNA」；Watson 第15章「氨基酸连接到 tRNA 上」；Watson 第15章「核糖体」；Watson 第15章「翻译的起始」；Watson 第15章「翻译延伸」；Watson 第15章「翻译终止」；Watson 第16章「遗传密码」；Campbell Concept 17.4；Lehninger §27.1；Lehninger §27.2；Lehninger §27.3 | Lehninger 第27章；Watson 第6章；Watson 第15章；Watson 第16章 | 242 |
| [05_第5章_分子生物学研究法_上_DNA_RNA及蛋白质操作技术](05_第5章_分子生物学研究法_上_DNA_RNA及蛋白质操作技术/05_第5章_分子生物学研究法_上_DNA_RNA及蛋白质操作技术.md) | Watson 第7章「分子生物学技术（章首）」；Watson 第7章「核酸：基本方法」；Watson 第7章「蛋白质」；Watson 第7章「蛋白质组学」；Campbell Concept 20.1；Lehninger §9.1 | Campbell 第20章；Lehninger 第9章；Watson 第7章 | 142 |
| [06_第6章_分子生物学研究法_下_基因功能研究技术](06_第6章_分子生物学研究法_下_基因功能研究技术/06_第6章_分子生物学研究法_下_基因功能研究技术.md) | Campbell Concept 20.2；Campbell Concept 20.3；Lehninger §9.2 | — | 85 |
| [07_第7章_原核基因表达调控](07_第7章_原核基因表达调控/07_第7章_原核基因表达调控.md) | Watson 第18章「原核生物的转录调控（章首）」；Watson 第18章「转录起始的调控：原核生物的实例」；Watson 第18章「λ噬菌体：调控的层次」；Watson 第18章「逆向调控：RNA 合成和稳定性控制相互影响并决定基因表达」；Watson 第20章「调控RNA（章首）」；Campbell Concept 18.1；Lehninger §28.1；Lehninger §28.2 | Lehninger 第28章；Watson 第18章 | 171 |
| [08_第8章_真核基因表达调控](08_第8章_真核基因表达调控/08_第8章_真核基因表达调控.md) | Watson 第15章「翻译的调控」；Watson 第19章「真核生物的转录调控（章首）」；Watson 第19章「组蛋白与 DNA 修饰导致的基因“沉默”」；Watson 第20章「调节 RNA 在真核生物中广泛存在」；Watson 第22章「系统生物学」；Campbell Concept 18.2；Campbell Concept 18.3；Lehninger §28.3 | Campbell 第18章；Watson 第19章；Watson 第20章；Watson 第22章 | 247 |
| [09_第9章_疾病与人类健康](09_第9章_疾病与人类健康/09_第9章_疾病与人类健康.md) | Campbell Concept 18.5；Campbell Concept 19.1；Campbell Concept 19.2；Campbell Concept 19.3；Campbell Concept 20.4；Lehninger §26.3 | Campbell 第19章 | 100 |
| [10_第10章_基因与发育](10_第10章_基因与发育/10_第10章_基因与发育.md) | Watson 第21章「发育和演化的基因调控」；Campbell Concept 18.4 | Watson 第21章 | 111 |
| [11_第11章_基因组与比较基因组学](11_第11章_基因组与比较基因组学/11_第11章_基因组与比较基因组学.md) | Watson 第7章「基因组学」；Campbell Concept 21.1；Campbell Concept 21.2；Campbell Concept 21.3；Campbell Concept 21.5；Campbell Concept 21.6；Lehninger §9.3 | Campbell 第21章 | 96 |

## Watson 中译本各章去向

| Watson 章 | 去向 |
| --- | --- |
| 第1章 孟德尔学派的世界观 | 整章→1.1；小结/习题→第1章末 |
| 第2章 核酸承载遗传信息 | 整章→1.2；小结/习题→第1章末 |
| 第3章 弱化学键和强化学键的重要性 | 整章→2.2；小结/习题→第2章末 |
| 第4章 DNA的结构 | 整章→2.2；小结/习题→第2章末 |
| 第5章 RNA的结构和功能多样性 | 整章→3.1；小结/习题→第3章末 |
| 第6章 蛋白质的结构 | 整章→4.4；小结/习题→第4章末 |
| 第7章 分子生物学技术 | 章首→5.1；核酸：基本方法→5.2；基因组学→11.2；蛋白质→5.5；蛋白质组学→5.5；小结/习题→第5章末 |
| 第8章 基因组结构、染色质和核小体 | 整章→2.1；小结/习题→第2章末 |
| 第9章 DNA的复制 | 整章→2.4；小结/习题→第2章末 |
| 第10章 DNA的突变和修复 | 整章→2.5；小结/习题→第2章末 |
| 第11章 分子水平上的同源重组 | 整章→2.5；小结/习题→第2章末 |
| 第12章 位点特异性重组和DNA转座 | 整章→2.6；小结/习题→第2章末 |
| 第13章 转录机制 | 章首→3.5；真核生物的转录→3.6；小结/习题→第3章末 |
| 第14章 RNA剪接 | 整章→3.8；小结/习题→第3章末 |
| 第15章 翻译 | 章首→4.4；信使 RNA→3.4；转运RNA→4.2；氨基酸连接到 tRNA 上→4.2；核糖体→4.3；翻译的起始→4.4；翻译延伸→4.4；翻译终止→4.4；翻译的调控→8.5；小结/习题→第4章末 |
| 第16章 遗传密码 | 整章→4.1；小结/习题→第4章末 |
| 第17章 生命起源和早期进化 | 整章→3.12；小结/习题→第3章末 |
| 第18章 原核生物的转录调控 | 章首→7.1；转录起始的调控：原核生物的实例→7.4；λ噬菌体：调控的层次→7.6；逆向调控：RNA 合成和稳定性控制相互影响并决定基因表达→7.7；小结/习题→第7章末 |
| 第19章 真核生物的转录调控 | 章首→8.2；组蛋白与 DNA 修饰导致的基因“沉默”→8.3；小结/习题→第8章末 |
| 第20章 调控RNA | 章首→7.7；调节 RNA 在真核生物中广泛存在→8.4；小结/习题→第8章末 |
| 第21章 发育和演化的基因调控 | 整章→10.1；小结/习题→第10章末 |
| 第22章 系统生物学 | 整章→8.5；小结/习题→第8章末 |

## 已知问题

- 文本来自 MinerU 自动解析，原有识别错误未改。《现代分子生物学》第 2 章正文中混有一行页眉“2.1 染色体 / 仅供个人科学教研”，按原样保留。
- Watson 中译本的目录只到第 19 章，第 18–22 章的切分点按正文标题人工指定。
- Lehninger §26.3（RNA 指导的 RNA/DNA 合成：逆转录酶、端粒酶、RNA 复制酶）在《现代分子生物学》中没有专门一节，放在第 9 章 9.2（HIV）末尾；§25.3（重组）放在 2.6（转座）末尾；Watson 第 3 章（化学键）放在 2.2（DNA 结构）末尾，第 6 章（蛋白质结构）放在 4.4 末尾，第 17 章（生命起源）放在 3.12 末尾，第 22 章（系统生物学）放在 8.5 末尾。

重新生成：`python3 scripts/build_molbio_cards.py`
