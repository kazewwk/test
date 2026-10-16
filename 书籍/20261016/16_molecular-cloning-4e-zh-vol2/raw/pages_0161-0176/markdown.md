36. 若使用选项3，则继续下一步——附加PCR引物（PCR Index Addition）；否则跳到步骤40。

## 附加 PCR 引物(若不使用一次性板)

37. 准备竖排含 IDT 或者 Illumina Indexes 的索引板。例如，IDT 第一竖排为 A1～H1，含 Indexes 1～8；第二竖排为 A2～H2，含 Indexes 9～16，依此类推。Illumina 第一竖排为 A1～H1，含 Index 1；第二竖排为 A2～H2，含 Index 2；依此类推。

38. 根据样品集大小选择 PCR Index 程序。

39. 运行程序，epMotion 将添加所有引物（每个引物各 $1\mu \mathrm{L}$，即添加 IDT 或 Illumina 索引引物 $8\mu \mathrm{mol} / \mathrm{L}$）到每个样品中。往每个样品加 $1\mu \mathrm{L}$ Index（IDT 或 Illumina Index Primer, $8\mu \mathrm{mol} / \mathrm{L}$）。

依次添加索引序列是为了在多重测序实验中区分样品。

40. 程序结束后，将全部 4 个 PCR 板盖上盖子，振荡并迅速离心。最终，终体积约为 $50\mu \mathrm{L}$。

41. 使用下述 PCR 程序扩增 DNA:

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 1 | 98°C, 30s |  |  |
| 18个循环 | 98°C, 10s | 65°C, 30s | 72°C, 30s |
| 末循环 |  |  | 72°C, 5min |

结束后维持在  $10^{\circ}$ C。

42. 当扩增程序结束，迅速离心 4 个 PCR 板，置于冰上。

## 合并PCR产物

96 个样品进行 PCR 产物合并的运行时间约为 30min。

43. 在 epMotion 上选择应用程序 PCR Pooling。

44. 复核 “Deck Layout and Plate Orientation”。

45. 运行程序，epMotion 会在 Costar 的 96 孔板上合并成对的相似 PCR 产物（合并后的体积为 $100\mu \mathrm{L}$）。

46. 程序结束时，快速离心合并的 96 孔板。

## 用双重SPRI磁珠进行大小筛选

从合并的文库中选择 300～500 bp 的片段。96 个样品用双重 SPRI 磁珠进行大小筛选的运行时间约为 1h 又 50min。

47. 用 $1 \mathrm{~mL}$ 移液器吹打几次重悬磁珠液。

48. 在 epMotion 上选择应用程序 Dual SPRI EB。

49. 复核 “Deck Layout and Plate Orientation”。

50. 运行程序，epMotion 将执行如下步骤。

i. 首先加  $60 \mu L$  磁珠（ $0.6 \times$ ）选择较大的片段，则  $\geqslant 500 bp$  的片段可结合到磁珠上。

ii. 将含<500bp 片段的  $60 \mu L$  上清液添加到含  $20 \mu L$ （ $0.8 \times$ ）浓缩磁珠的 Costar 板内，则  $\leqslant 300bp$  的片段可结合到珠子上。

iii. 洗脱仅含 300\~500bp 片段的样品。

51. 当程序结束后，快速离心洗脱样品（eluted sample）板，置于冰上，每个样品的最终体积约为 $50\mu \mathrm{L}$。

## 检测样品浓度、大小分布和质量

52. 用 Varioskan Flash Multimode Reader、Agilent 或 CaliperGX 仪器测终浓度，参照相应的仪器操作手册进行浓度测量。
53. 为每一个样品制备每个样品的 $5\mathrm{nmol / L}$ 稀释液，要在管上清楚地标明文库已稀释到 $5\mathrm{nmol / L}$ 。

关于样品稀释的技术帮助, 可查询 http://www.promega.com/biomath/Calculators&AdditionalConversions/Dilution。

54. 稀释后的样品现在可以用于 qPCR 和 Illumina Sequencer 测序。

# 方案 7 用于 Illumina 测序的 3kb 末端配对文库的制备

本方案介绍如何制备 3kb 末端配对文库。本方法扩增得到的 DNA 适用于在 Illumina 测序仪上进行测序（参照导言中关于配对文库的讨论）。

![](images/page_161_image_10.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

AMPure XP 磁珠 (Beckman Coulter 公司)

琼脂糖凝胶 (0.8% LE)

EB 缓冲液 (QIAGEN 公司，目录号 19086)

ERC 缓冲液 (QIAGEN 公司，目录号 1018144)

PE 缓冲液 (QIAGEN 公司，目录号 19065)

QG 缓冲液(QIAGEN 公司，目录号 19063)

DNA 分子质量标记(1kb)

DNA 聚合酶(NEB 公司，目录号 M0209)和缓冲液 2 (10×)

DNA 末端修复试剂盒(Lucigen 公司，目录号 40035-2)

dNTP (10mmol/L)

乙醇 (70%)

溴化乙锭

FlashGel (2.2%) (Lonza 公司)

胶上样缓冲液 IV &lt;A&gt;

基因组 DNA

Internal adaptors (2μmol/L) (AB 公司)

```txt
Internal adaptor duplexes (2μmol/L= 2 pmol/μL):
    internal_adaptor-A: 5'-Phos / CGTACA(Bio-dT)CCGCCTTGGCCGT-3'
    internal_adaptor-B: 5'-Phos / GGCCAAGGCGGATGTACGGT-3'
Klenow 大片段
文库结合缓冲液 (2×) (Applied Biosystems 公司)
LMP CAP adaptors (50μmol/L) (Applied Biosystems 公司)
CAP adaptor duplexes (50μmol/L =50pmol/μL)
    LMP Cap_adaptor-A 5'-Phos / CTGCTGTAC-3'
    LMP Cap_adaptor-B 5'-ACAGCAG-3'
NaCl (3mol/L)
Paired End Sample Prep Kit (Illumina 公司, 目录号 1001809)
PCR 引物 1.0 和 2.0 (Illumina 公司)
PE forked adaptor duplex (Illumina 公司)
Phusion 混合液 (2×) (Thermo Scientific 公司)
Plasmid-Safe ATP-Dependent DNase (Epicenter 公司, 目录号 E3110K)
QIAquick PCR 纯化柱(QIAGEN 公司, 目录号 28183)
快速连接试剂盒(New England Biolabs 公司, 目录号 M2200L)
S1 核酸酶(Life Technologies 公司, 目录号 18001-016)
偶联了链亲和素的磁珠 (Dynabeads 公司, 目录号 M-270; Life Technologies 公司, 目
653-05)
分子级水
```

## 设备

DNA 剪切仪(例如, Covaris 公司生产的 S2 系统)

荧光光度计(例如，Life Technologies 公司生产的 Qubit，目录号 Q32857)

冰水浴

磁珠收集器 (MPC)

miniTUBE - Blue AFA plastic tube (Covaris 公司，目录号 520065)

Quant-iT dsDNA BR Assay Kit (Life Technologies 公司，目录号 Q32850)

Quant-iT dsDNA HS Assay Kit (Life Technologies 公司)

PCR 仪

紫外透射仪

试管旋转仪 (例如 Thermo Scientific 公司生产的 Labquake)

带盖子的锥底管 (0.2 mL、1.7 mL 和 15 mL)

真空干燥器 (如 SpeedVac)

![](images/page_162_image_16.jpg)

## 方法

## DNA 片段化

1. 取  $10 \mu g$  DNA 并测其体积，然后加入 EB 缓冲液直至终体积为  $200 \mu L$ 。将该  $200 \mu L$  溶液全部转移到一个 miniTUBE（蓝底）。

2. 使用 Covaris S2 DNA 剪切仪剪切 DNA:

i. 打开 Covaris 软件。
ii. 点击 Open 按钮选择操作条件。
iii. 选择文件 3Kb\_shearing，点击 Open。
iv. 在软件主界面，复核如下参数是否如下:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Duty Cycle: $20\%$  
Intensity: 0.1  
Cycles per Burst: 1000  
Total Treatment Time: 600 sec
</div>

v. 把将第一步配制好的 DNA 样品（来自步骤 1）放入 miniTUBE 试管架，将试管架放入水浴。

vi. 点击 Start 按钮开始剪切程序。

vii. 剪切完成后从试管架取出 miniTUBE。

viii. 将该 DNA 样品转移到 1.7mL 微离心管。

3. 用 $1.2\%$ 凝胶（FlashGel）电泳以确保所有样品均已切割为 $3 \mathrm{~kb}$ 左右的片段。

## 末端修复

4. 在含 DNA 样品（200μL）的 1.7mL 离心管内依次加入下述试剂:

| 末端修复缓冲液(5×)(Lucigen公司) | 60μL |
| --- | --- |
| 分子级水 | 38μL |
| 末端修复酶混合液(Lucigen公司) | 2μL |
| 总体积 | 300μL |

振荡混匀，室温下孵育 30min 进行末端修复反应。

5. 用 QIAquick PCR 纯化柱纯化末端修复片段，一个纯化柱可回收 $10 \mu \mathrm{g}$ DNA。

i. 将末端修复反应液加入到  $900 \mu L$  的 ERC 缓冲液中并混匀。
ii. 将反应液/缓冲液混合物加入到 QIAquick 纯化柱，14 000g 离心 1min，或者将其放置于抽真空装置直至 ERC 混合物全部过柱。
iii. 若离心，弃去废液。
iv. 加 $750\mu \mathrm{L}$ PE缓冲液，$14000g$ 离心 $1\mathrm{min}$，或者将其放置于抽真空装置直至PE全部过柱。
v. 若离心，弃去废液。
vi. 将离心管旋转  $180^{\circ}$ ，14 000g 离心 1min。
vii. 将纯化柱放入新的 1.7mL 离心管，弃去废液管。
viii. 加入  $30 \mu L$  EB 缓冲液，室温孵育 1min，14 000g 离心纯化柱 1min。
ix. 再加入  $30 \mu L$  EB 缓冲液，室温孵育 1min，14 000g 离心纯化柱 1min。
x. 弃去纯化柱，保留含洗脱 DNA 的 1.7mL 收集管。

6. 取  $1 \mu L$  DNA 用 Quant-It dsDNA BR Assay Kit 测量纯化 DNA 的浓度，用分光光度计读取结果（可参见方案 11 或方案 12）。

## Cap 接头连接

7. 计算需要多少皮摩尔的 LMP CAP 接头（双链）。首先根据大小计算插入片段 DNA 的皮摩尔数，公式如下:

（所用 DNA 的微克数；来自步骤 6）×0.51pmol DNA=样品中 DNA 的皮摩尔数，

（样品中 DNA 的皮摩尔数）×100 = 所需 LMP CAP 接头的皮摩尔数（片段的 100 倍），

$$
\frac {\text {所需LMP CAP接头的皮摩尔数}}{5 0 \mathrm{pmol} / \mu \mathrm{L LMP CAP接头}} = \text {所需LMP CAP接头的微升数。}
$$

例如，如果是  $12.6 \mu g$  的约 3000bp 插入片段 DNA:

$$
\frac {12.6\mu \mathrm{g} \mathrm{DNA} \left(\frac {1\mu \mathrm{g} \mathrm{DNA} \times (10^{6}\mathrm{pg/}\mu\mathrm{g}) \times 1 \mathrm{pmol/660pg}}{3000\mathrm{bp}}\right) \times 100}{50\mathrm{pmol/}\mu\mathrm{L LMP CAP接头}}
$$

$$
= 1 2. 7 3 \mu \mathrm{L} \text {LMP CAP 接头需要用于这个样品。}
$$

8. 在 $1.7 \mathrm{~mL}$ 离心管混合下述组分:

| 来自步骤6的DNA | 60μL |
| --- | --- |
| 步骤7计算出的CAP接头 | xμL |
| 快速连接酶缓冲液(2×) | 150μL |
| 分子级水 | yμL |
| 连接酶 | 7.5 μL |
| 总体积 | 300μL |

快速振荡混匀，室温孵育 15min 进行连接反应。

9. 将连接反应液加入到  $900 \mu L$  REC 缓冲液并混匀。按照步骤 5.ii～5.viii，用 QIAquick PCR 纯化柱纯化已连接片段，用 1.7mL 离心管收集洗脱下的 DNA。

## 大小筛选

10. 准备 0.8% LE 琼脂糖凝胶。进行电泳前加 20μL 溴化乙锭到凝胶缓冲液中。

11. 将 1kb DNA 分子质量标记（15μL 分子质量标记+1.5μL 凝胶上样缓冲液）上样至合适孔。

12. 往步骤 9 纯化获得的 DNA 样品中加 $3 \mu \mathrm{L} 10 \times$ 胶上样缓冲液。将全部样品上样至凝胶中, $120 \mathrm{~V}$ 电泳 $60 \mathrm{~min}$ 。

13. 从胶上切下 2\~4kb 大小的 DNA。

电泳结束后一定要彻底清洗凝胶以去除残留的溴化乙锭。

14. 称量切下的胶块并转入 15mL 锥底管。每 2g 凝胶加入 6mL QG 缓冲液。

15. 用台式摇床剧烈振荡管子直至凝胶彻底溶解。

16. 用 1 个或者多个 QIAquick 凝胶提取柱纯化 DNA。单个柱子能处理的凝胶量上限约为 $400 \mathrm{mg}$，因此要根据切下的凝胶重量来计算柱子数量（例如，上述溶解于 $6 \mathrm{~mL} \mathrm{QG}$ 缓冲液的 $2 \mathrm{~g}$ 凝胶需要分成 5 份使用 5 个柱子）。

i. 在每个 QIAquick 柱子中加入溶解了最多 400mg 凝胶的 QG 缓冲液。

ii. 14 000g 离心柱子 1min 或使用抽真空装置使 QG 混合液全部过柱。

iii. 若离心，弃去废液。

往柱子里加入更多的 QG 凝胶混合液并重复离心，直至 QG 凝胶混合液全部过柱。

iv. 按照步骤 5.iv～5.viii 纯化已连接片段。

v. 弃去柱子，保留含有洗脱 DNA 的 1.7mL 离心管，合并纯化的 DNA。

17. 取 $1\mu \mathrm{L}$ DNA 用 Quant-It dsDNA BR Assay Kit 测量纯化 DNA 的浓度，用分光光度计读取结果（可参见方案 11 或方案 12）。

如果发现 DNA 的量 $<1\mu g$ ，推荐重新开始本方案。

## DNA 环化

18. 在 $1.7 \mathrm{~mL}$ 离心管合并和混匀下列组分。可能要设置多组重复反应。

## 环化反应

| 来自步骤17的DNA | 1μg(2~4kb) |
| --- | --- |
| 快速连接酶缓冲液(2×) | 280μL |
| Internal adaptors(2μmol/L) | 0.65μL |
| 连接酶 | 14μL |
| 无核酸酶的水 | xμL |
| 总体积 | 560μL |

计算无核酸酶的水的量（x），使反应液达到各自终体积。体积和 DNA 浓度对于有效环化很关键。

19. 振荡混匀，室温孵育 10min 进行环化反应。

20. 在 $15 \mathrm{~mL}$ 锥底管中混合各个环化反应液和 $1680 \mu \mathrm{L}$ （即3倍体积）ERC缓冲液，振荡混匀。

21. 用 QIAquick PCR 纯化柱按照步骤 5.ii～5.x 纯化环化片段。

## 质粒安全的 DNA 酶处理

22. 在 $1.7 \mathrm{~mL}$ 离心管混合下列组分:

| 来自步骤21的DNA | 60μL |
| --- | --- |
| ATP(25mmol/L) | 5μL |
| Plasmid Safe缓冲液(10×) | 10μL |
| 分子级水 | 24μL |
| Plasmid Safe DNase(10U/μL) | 1μL |
| 总体积 | 100μL |

振荡混匀，37℃孵育40min进行反应。

23. 如果前面进行了多组重复环化反应，合并所有的反应液，加入 3 倍体积 ERC 缓冲液并混匀。

24. 按照步骤 5.ii～5.x，用 QIAquick PCR 纯化柱纯化 DNA。

25. 取  $1 \mu L$  DNA 用 Quant-It dsDNA BR Assay Kit 测量纯化 DNA 的浓度，用分光光度计读取结果（可参见方案 11 或方案 12）。

## 切口平移

26. 往每 200ng 步骤 24 回收的环化 DNA 中添加如下组分，并于冰上混匀冷却。

| 来自步骤24的DNA(200ng) | xμL |
| --- | --- |
| NEB缓冲液 2 (10×) | 10μL |
| dNTP (10mmol/L) | 10μL |
| 无核酸酶的水 | yμL |
| 总体积 | 98μL |

27. 往每个反应管中加  $2 \mu L$   $10 U/\mu L$  DNA 聚合酶 I，振荡混匀，立即冰水浴（ $0^{\circ} C$ ）20min 进行反应。

28. 加入  $300 \mu L$ （即 3 倍体积）ERC 缓冲液终止反应。

29. 用 QIAquick PCR 纯化柱子按照步骤 5.ii～5.x 纯化 DNA。

需要注意的是，由于只要 300～500bp 的片段，如果切口平移步骤产生的片段大小不在 300～500bp 的范围，那么这一步得到的文库样本可能不足以进行测序。

## S1 核酸酶消化

如果进行了多组重复切口平移反应，每个反应应该分别进行消化。

30. 用 S1 核酸酶稀释缓冲液将 S1 核酸酶稀释至  $200 \, U/\mu L$ 。

31. 在 1.7mL 离心管中加入下列组分并混匀:

| DNA(来自步骤29) | 60μL |
| --- | --- |
| S1缓冲液(10×) | 10μL |
| NaCl(3mol/L) | 10μL |
| 分子级水 | 18μL |
| S1核酸酶(200U/μL) | 2μL |
| 总体积 | 100μL |

振荡混匀，37℃温育15min进行反应。

32. 合并反应液，加入 3 倍体积的 ERC 缓冲液并振荡。

33. 按照步骤 5.ii～5.viii 用 QIAquick PCR 纯化柱纯化 DNA，用 1.7mL 离心管收集洗脱的 DNA。

## 末端修复

34. 在 $1.7 \mathrm{~mL}$ 离心管中加入下列组分并混匀:

| DNA(来自步骤33) | 30μL |
| --- | --- |
| 末端修复缓冲液(5×) | 10μL |
| 分子级水 | 8μL |
| 末端修复酶混合液 | 2μL |
| 总体积 | 50μL |

振荡混匀，室温孵育 15min 进行末端修复反应。

35. 加入 3 倍体积的 ERC 缓冲液并振荡。

36. 用 QIAquick PCR 纯化柱纯化 DNA，步骤如下:

i. 按照步骤 5.ii～5.vii 操作。

ii. 加入  $25 \mu L$  EB 缓冲液，室温孵育 1min，14000g 离心柱子 1min。

iii. 再次加入  $25 \mu L$  EB 缓冲液，室温孵育 1min，14000g 离心柱子 1min。

iv. 弃掉柱子，用 1.7mL 离心管收集洗脱的 DNA。

## 结合链亲和素磁珠

37. 取 $25\mu \mathrm{L}$ 链亲和素磁珠放入一个新离心管，使用磁珠收集器（MPC）使磁珠沉淀并弃去上清液。

38. 使用 MPC 用  $50 \mu L$   $2 \times$  文库结合缓冲液清洗磁珠两遍，每次清洗要充分振荡。

39. 用  $50 \mu L$   $2 \times$  文库结合缓冲液重悬磁珠。

40. 将 $50\mu \mathrm{L}$ 清洗过的链亲和素磁珠加入到得自步骤36的 $50\mu \mathrm{L}$ DNA中，振荡混匀，放置于离心管旋转器上室温孵育 $15\mathrm{min}$。

41. 将离心管放入 MPC 仪使磁珠沉淀，弃掉上清。

42. 使用 MPC 用  $500 \mu L$  EB 缓冲液清洗结合的文库 3 遍，每次清洗要充分振荡。

43. 吸去残留的 EB 缓冲液，用  $32 \mu L$  EB 缓冲液重悬沉淀。

## 加 A 尾

44. 在 $1.7 \mathrm{~mL}$ 离心管中加入下列组分并混匀:

| 来自步骤43的DNA/磁珠 | 32μL |
| --- | --- |
| NEB缓冲液2(10×) | 5μL |
| dATP(1mmol/L) | 10μL |
| Klenow片段(5U/μL) | 3μL |
| 总体积 | 50μL |

振荡混匀，37℃温育30min进行反应。

45. 使用 MPC 用 $500\mu \mathrm{L}$ EB 缓冲液清洗结合的文库 3 遍，每次清洗要充分振荡。

46. 吸去残留的 EB 缓冲液，用  $15 \mu L$  EB 缓冲液重悬沉淀。

## Illumina 末端配对接头连接

47. 在 $1.7 \mathrm{~mL}$ 离心管中加入下列组分并混匀:

| 来自步骤46的DNA/磁珠 | 15μL |
| --- | --- |
| 快速连接酶缓冲液(2×) | 25μL |
| PE forked adaptor duplex | 5μL |
| 连接酶 | 5μL |
| 总体积 | 50μL |

振荡混匀，室温孵育 15min 进行反应。

48. 使用 MPC 用 $500\mu \mathrm{L}$ EB 缓冲液清洗结合的文库 3 遍，每次清洗要充分振荡。

49. 吸去残留的 EB 缓冲液，用  $15 \mu L$  EB 缓冲液重悬沉淀。

## PCR 参数优化

50. 在 $0.2 \mathrm{~mL}$ 离心管内为每个反应混合下述组分。为每个配对文库构建准备一个反应。

进行循环数优化是为了测定最佳 PCR 循环数。然后用预先测定的循环数进行后续的文库扩增。

| DNA/磁珠 | 2μL |
| --- | --- |
| Phusion 混合液(2×) | 25μL |
| PE PCR 引物 1.0 | 0.5μL |
| PE PCR 引物 2.0 | 0.5μL |
| 分子级水 | 22μL |
| 总体积 | 50μL |

51. 创建两个 PCR 程序。

程序1

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 1 | 98°C, 30s |  |  |
| 10个循环 | 98°C, 10s | 65°C, 30s | 72°C, 30s |

结束后保持在  $4^{\circ}$ C。

程序2

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 2个循环 | 98°C, 10s | 65°C, 30s | 72°C, 30s |

结束后保持在  $4^{\circ}$ C。

52. 取 6 个 $0.2 \mathrm{~mL}$ 离心管，分别标记为:PCR-10, PCR-12, PCR-14, PCR-16, PCR-18, PCR-20。

53. 用步骤50准备的 $50\mu \mathrm{L}$ 反应液，运行PCR程序1，取出 $5\mu \mathrm{L}$ 反应液放入标记为PCR-10的 $0.2\mathrm{mL}$ 离心管。

54. 运行 PCR 程序 2 继续 PCR 优化，取出 $5\mu \mathrm{L}$ 反应液放入标记为 PCR-12 的 $0.2\mathrm{mL}$ 离心管。

55. 重复步骤 54 完成剩余的 4 个循环数优化试验（PCR-14，PCR-16，PCR-18，PCR-20）。

56. 每  $5 \mu L$  反应产物加入  $1 \mu L$  上样染料，快速振荡并离心。

57. 准备 2.2% FlashGel，13 孔内各加  $4 \mu L$  水，第 1 和第 8 泳道加  $2 \mu L$  的 Flash 50～1500bp 分子质量标记物。

58. 第 2～7 个泳道中各加入  $6 \mu L$  PCR 产物，275V 电泳 5～7min。

59. 凝胶照相。确定哪些循环数会过度扩增。进行大规模 PCR 时采用未显现过度扩增的最大循环数。例如，如果 PCR-18 和 PCR-20 显现过度扩增而其他循环数未显现，则用 16 个循环扩增文库。

## 大规模 PCR

60. 根据下述每份反应的用量和总共的 PCR 反应数，准备 PCR 反应混合液。我们推荐进行 12 份反应。

| Phusion mix (2×) | 25μL |
| --- | --- |
| PE PCR 引物 1.0 | 0.5μL |
| PE PCR 引物 2.0 | 0.5μL |
| 分子级水 | 22μL |
| 每份反应的终体积 | 48μL |

61. 根据前一部分优化的循环数设定 PCR 程序。

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 1 | 98°C, 30s |  |  |
| N个循环a | 98°C, 10s | 65°C, 30s | 72°C, 30s |

程序结束后维持在  $4^{\circ}$ C。

a. 能得到扩增产物的最少循环数（N）。

62. 在每个反应管中加入 $48\mu \mathrm{L}$ PCR混合液和 $2\mu \mathrm{L}$ 来自步骤49的DNA/磁珠，放入PCR仪进行DNA扩增。

63. 循环结束后，将所有样品合并到一个 $1.5\mathrm{mL}$ 锥底管中，用EB缓冲液调节样品至终体积为 $600\mu \mathrm{L}$。

64. 加入 3 倍体积的 ERC 缓冲液，振荡。

65. 用 QIAquick PCR 纯化柱进行纯化 DNA，操作如下:

i. 按照步骤 5.ii～5.vii 进行操作。

ii. 加入  $50 \mu L$  EB 缓冲液，室温孵育 1min，14 000g 离心 1min。

iii. 加入  $50 \mu L$  EB 缓冲液，室温孵育 1min，14 000g 离心 1min。

iv. 弃掉柱子，保留含  $100 \mu L$  洗脱 DNA 的 1.7 mL 离心管。

## 双重 AMPure 磁珠纯化

66. 振荡 AMPure XP 磁珠。

67. 往步骤 65 得到的 $100\mu \mathrm{L}$ 样品中加入 $60\mu \mathrm{L}$ AMPure XP 磁珠，置于离心管旋转器上 $5\mathrm{min}$ 。将此离心管标记为 1 号管。

68. 取 $60\mu \mathrm{L}$ AMPure XP 磁珠放入一个新的 $1.5\mathrm{mL}$ 离心管中，将此离心管标记为2号管。

69. 将 2 号管放置于 MPC 上 3min，直到磁珠与上清液完全分离。

70. 弃掉上清，往“干的”磁珠中加入  $20 \mu L$  AMPure XP，振荡重悬磁珠。

71. 从选择器中取出 1 号管放入 MPC，放置 $2 \mathrm{~min}$ 直到磁珠与上清液完全分离。

72. 将 1 号管的上清液转移到 2 号管中，振荡 2 号管以重悬磁珠，将 2 号管放置于选择器上 5min。弃掉 1 号管。

73. 将 2 号管放置于 MPC 上 2min，直到磁珠与上清液完全分离。

74. 弃掉上清液。

75. 用 $500\mu \mathrm{L}70\%$ 乙醇清洗磁珠，清洗时上下颠倒离心管数次，在MPC上放置1min，弃掉上清液。

▲在整个清洗过程中将离心管放置于 MPC 上。

76. 重复步骤 75。

77. 尽可能地去掉离心管内和盖子上残留的乙醇。

78. 瞬时离心将磁珠收集至离心管底部。

79. 将盛有磁珠的离心管放置于真空干燥器上抽干 1min，检查在离心管底或者磁珠上是否有液体残留（磁珠看起来应该是“破碎的”而不是发亮的）。

80. 如有必要，重复抽干 1min。

81. 用  $20 \mu L$  EB 缓冲液从磁珠上洗脱 DNA。

尽量将所有磁珠都弄到溶液中。例如，可以轻弹离心管，用吸头将管壁的磁珠推入溶液，等等。

82. 将离心管放置于 MPC 上，小心地将上清转移到一个新离心管中。

▲保留好上清，这是最终样品。

## 最终文库定量

83. 取  $1 \mu L$  来自步骤 82 的最终样品，用 2.2% 的凝胶电泳验证 DNA 大小。

84. 取 $1\mu \mathrm{L}$ 最终样品用 Quant-It dsDNA BR Assay Kit 测量纯化 DNA 的浓度，用分光光度计读取结果（可参见方案 11 或方案 12）。

85. 将浓度值输入 Illumina 文库稀释计算器（Illumina Library Dilution Calculator）中，将末端配对文库最终样品稀释至 5nmol/L。

## 方案 8 用于 Illumina 测序的 8kb 末端配对文库的制备

本方案介绍如何制备适用于 Illumina 测序仪的 8kb 末端配对文库。这些是大片段插入文库，初始的剪切将使用多种参数和不同的仪器以获取所需大小的片段（可参考信息栏 “DNA 片段化”）。如果要了解更多的细节，可参考本章导言部分关于末端配对文库的讨论。

![](images/page_170_image_2.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

扩增引物（100μmol/L）

AMPure XP 磁珠（Agencourt，目录号 A63880）

ATP，锂盐（100mmol/L）(Roche，目录号14470220)

Bst DNA 聚合酶，大片段（8000U/mL）（NEB，目录号 M0275L）

EB 缓冲液（10mmol/L Tris pH 7.5～8.5）

ERC 缓冲液（QIAGEN，目录号 1018144）

PBI 缓冲液（QIAGEN，目录号 19066）

PE 缓冲液（QIAGEN，目录号 19065）

QG 缓冲液（QIAGEN，目录号 19063）

DNA 载体

Circularization 接头（20μmol/L）

Cre 重组酶（NEB，目录号 M0298L）

dATP(1mmol/L)

DNA 分子质量标准（1kb）（Life Technologies，目录号 15615-024）（稀释至 100ng/ $\mu$ L）

DNA 终止末端修复试剂盒（Lucigen，目录号 40035-2）

dNTP（10mmol/L）（Roche，目录号11581295001）

DTT(1mol/L)

乙醇（70%）

外切核酸酶 I（20 000U/mL）（NEB，目录号 M0293L）

含有溴酚蓝的胶上样缓冲液（10×）＜A＞

基因组 DNA

GS FLX Titanium Paired End Adapter Kit（Roche，目录号 05 463 343 001）

PCR 引物（8μmol/L）(IDT)

PE forked adaptor duplex (4μmol/L) (Illumina, Sigma-Aldrich)

Klenow 缓冲液（10×）（NEB 缓冲液 2）（New England Biolabs）

Klenow 外切核酸酶（5U/ $\mu$ L）（NEB，目录号 M0212L）

文库接头（20μmol/L）

文库结合缓冲液（2×）&lt;R&gt;

引物

引物/寡聚核苷酸序列参见表11-2。

多重 PCR 引物 1.0（8μmol/L）(IDT)

多重 PCR 引物 2.0（0.5μmol/L）(IDT)

PCR 引物 PE 1.0(8μmol/L) (IDT)

PCR 引物 PE 2.0(8μmol/L) (IDT)

PE forked adaptor duplex (4μmol/L) (Illumina, Sigma-Aldrich)

Phusion HF PCR 混合物（2×）（NEB，目录号 F-531L）

Plasmid-Safe ATP 依赖型 DNase（Epicenter，目录号 E3110K）

快速连接酶试剂盒（NEB，目录号 M2200L）

SDS(20%)

SeaKem LE 琼脂糖（Lonza，目录号 50004）

乙酸钠（3mol/L, pH5.5）

链亲和素磁珠（Dynabeads，目录号 M-270；Life Technologies，目录号 653-05）

SYBR Green I 核酸凝胶染料（Life Technologies，目录号 B9004S）

TBE 缓冲液&lt;A&gt;

ThermoPol 反应缓冲液（10×）（NEB，目录号 B9004S）

Tris-HCl（10mmol/L，pH8.0）或者 EB 缓冲液（QIAGEN，目录号 19086）

## 设备

生物分析仪（Agilent2100，目录号5067-1504）

DNA 1000 试剂盒（Agilent2100，目录号 5067-1504）

DNA 剪切装置（Hydroshear; Gene Machines, 目录号 JHSH000000-1）

DNA 剪切装置（Hydroshear Large Assembly；Gene Machines，目录号 JHSH204007）

DNA 剪切仪（Covaris S2 系统）

电泳装置（Chef Mapper）

磁珠收集器（MPC）

带有盖子的离心管（0.2mL 和 1.7mL）

MinElute 柱（QIAGEN，目录号 28006）

MiniTMBE-Blue AFA 塑料管（Covaris，目录号 520065）

QIAquick 柱（QIAGEN, 目录号 28183）

Quant-iT Assay Kit

Qubit 测量管

Qubit 分光光度计和测试试剂盒

PCR 仪

试管旋转器（如 Labquake）

真空干燥器（如 SpeedVac）

表 11-2 接头和引物的序列

| 接头和引物 | 序列 |
| --- | --- |
| I11-PE 交叉接头 duplex(4μmol/L)(Sigma-Aldrich) | 5'-P-GATCGGAAGAGCGGTTCAGCAGGAATGCCGAG5'-ACACTCTTTCCCTACACGACGCTCTTCCGATCT |
| PE PCR 引物 1.0 | 5'AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGA CGCTCTTCCGATCT |
| PE PCR 引物 2.0 | 5'-CAAGCAGAAGACGGCATACGAGATCGGTCTCGGCATTCCTGCT GAACCGCTCTTCCGATCT |
| ILL IndexAdapter Duplex IDT | 5'-P-GATCGGAAGAGCACACGTCT(5'-磷酸化)5'-ACACTCTTTCCCTACACGACGCTCTTCCGATCT(去磷酸化) |
| 多重 PCR 引物 1.0 | 5'-AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACG ACGCTCTTCCGATCT |
| 多重 PCR 引物 2.0 | 5'-GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT |
| PCR 引物,Index1 | CAAGCAGAAGACGGCATACGAGATCGTGATGTGACTGGAGTTC |
| PCR 引物,Index2 | CAAGCAGAAGACGGCATACGAGATACATCGGTGACTGGAGTTC |
| RCR 引物,Index3 | CAAGCAGAAGACGGCATACGAGATGCCTAAGTGACTGGAGTTC |
| PCR 引物,Index4 | CAAGCAGAAGACGGCATACGAGATTGGTCAGTGACTGGAGTTC |
| PCR 引物,Index5 | CAAGCAGAAGACGGCATACGAGATCACTGTGTGACTGGAGTTC |
| PCR 引物,Index6 | CAAGCAGAAGACGGCATACGAGATATTGGCGTGACTGGAGTTC |
| PCR 引物,Index7 | CAAGCAGAAGACGGCATACGAGATGATCTGGTGACTGGAGTTC |
| PCR 引物,Index8 | CAAGCAGAAGACGGCATACGAGATTCAAGTGTGACTGGAGTTC |
| PCR 引物,Index9 | CAAGCAGAAGACGGCATACGAGATCTGATCGTGACTGGAGTTC |
| PCR 引物,Index10 | CAAGCAGAAGACGGCATACGAGATAAGCTAGTGACTGGAGTTC |
| PCR 引物,Index11 | CAAGCAGAAGACGGCATACGAGATGTAGCCGTGACTGGAGTTC |
| PCR 引物,Index12 | CAAGCAGAAGACGGCATACGAGATTACAAGGTGACTGGAGTTC |
| PCR 引物,Index13 | CAAGCAGAAGACGGCATACGAGATAAACCTGTGACTGGAGTTC |
| PCR 引物,Index14 | CAAGCAGAAGACGGCATACGAGATTTGACTGTGACTGGAGTTC |
| PCR 引物,Index15 | CAAGCAGAAGACGGCATACGAGATGGAACTGTGACTGGAGTTC |
| PCR 引物,Index16 | CAAGCAGAAGACGGCATACGAGATTGACATGTGACTGGAGTTC |
| PCR 引物,Index17 | CAAGCAGAAGACGGCATACGAGATCTATCTGTGACTGGAGTTC |
| PCR 引物,Index18 | CAAGCAGAAGACGGCATACGAGATGATGCTGTGACTGGAGTTC |
| PCR 引物,Index19 | CAAGCAGAAGACGGCATACGAGATAGCGCTGTGACTGGAGTTC |
| PCR 引物,Index20 | CAAGCAGAAGACGGCATACGAGATAGATGTGTGACTGGAGTTC |
| PCR 引物,Index21 | CAAGCAGAAGACGGCATACGAGATCTGGGTGTGACTGGAGTTC |
| PCR 引物,Index22 | CAAGCAGAAGACGGCATACGAGATGGACGGGTGACTGGAGTTC |
| PCR 引物,Index23 | CAAGCAGAAGACGGCATACGAGATTTCTCGGTGACTGGAGTTC |
| PCR 引物,Index24 | CAAGCAGAAGACGGCATACGAGATATTCCGGTGACTGGAGTTC |
| PCR 引物,Index25 | CAAGCAGAAGACGGCATACGAGATAGCTAGGTGACTGGAGTTC |
| PCR 引物,Index26 | CAAGCAGAAGACGGCATACGAGATGTATAGGTGACTGGAGTTC |
| PCR 引物,Index27 | CAAGCAGAAGACGGCATACGAGATTCTGAGGTGACTGGAGTTC |
| PCR 引物,Index28 | CAAGCAGAAGACGGCATACGAGATCAGCAGGTGACTGGAGTTC |
| PCR 引物,Index29 | CAAGCAGAAGACGGCATACGAGATCTAAGGGTGACTGGAGTTC |
| PCR 引物,Index30 | CAAGCAGAAGACGGCATACGAGATCCGGTGGTGACTGGAGTTC |
| PCR 引物,Index31 | CAAGCAGAAGACGGCATACGAGATCGATTAGTGACTGGAGTTC |
| PCR 引物,Index32 | CAAGCAGAAGACGGCATACGAGATTCCGTCGTGACTGGAGTTC |
| PCR 引物,Index33 | CAAGCAGAAGACGGCATACGAGATTATATCGTGACTGGAGTTC |
| PCR 引物,Index34 | CAAGCAGAAGACGGCATACGAGATAGCATCGTGACTGGAGTTC |
| PCR 引物,Index35 | CAAGCAGAAGACGGCATACGAGATCTCTACGTGACTGGAGTTC |
| PCR 引物,Index36 | CAAGCAGAAGACGGCATACGAGATCGCGGCGTGACTGGAGTTC |
| PCR 引物,Index37 | CAAGCAGAAGACGGCATACGAGATTGGAGCGTGACTGGAGTTC |
| PCR 引物,Index38 | CAAGCAGAAGACGGCATACGAGATTGTGCCGTGACTGGAGTTC |
| PCR 引物,Index39 | CAAGCAGAAGACGGCATACGAGATCAGGCCGTGACTGGAGTTC |
| PCR 引物,Index40 | CAAGCAGAAGACGGCATACGAGATGCGGACGTGACTGGAGTTC |
| PCR 引物,Index41 | CAAGCAGAAGACGGCATACGAGATGCTGTAGTGACTGGAGTTC |
| PCR 引物,Index42 | CAAGCAGAAGACGGCATACGAGATATTATAGTGACTGGAGTTC |
| PCR 引物,Index43 | CAAGCAGAAGACGGCATACGAGATGAATGAGTGACTGGAGTTC |
| PCR 引物,Index44 | CAAGCAGAAGACGGCATACGAGATTGCCGAGTGACTGGAGTTC |
| PCR 引物,Index45 | CAAGCAGAAGACGGCATACGAGATGGTAGAGTGACTGGAGTTC |
| PCR 引物,Index46 | CAAGCAGAAGACGGCATACGAGATCATTCAGTGACTGGAGTTC |
| PCR 引物,Index47 | CAAGCAGAAGACGGCATACGAGATGGAGAAGTGACTGGAGTTC |
| PCR 引物,Index48 | CAAGCAGAAGACGGCATACGAGATATGGCAGTGACTGGAGTTC |

![](images/page_173_image_2.jpg)

## 方法

## DNA 片段化

该方法使用大型剪切装备 Hydroshear，将速度设置为 9、循环数设置为 14 时，可以产生平均大小为 8kb 的 DNA 片段。不过每种装备产生的 DNA 片段大小范围不同，应该根据生产商推荐的参数先进行测试。

1. 往 $1.7\mathrm{mL}$ 离心管中加入至少 $15\mu \mathrm{g}$ 基因组DNA样品，然后加入EB缓冲液至终体积 $150\mu \mathrm{L}$。
2. 加入  $40 \mu L$  的  $50 \times$  Lucigen End Repair Buffer，上下翻转颠倒离心管使之混匀。
3. 打开桌面的 Hydroshear 软件。
4. 将 Hydroshear 拨到 Output。点击 OK。
5. 在 “Shearing Parameters” 界面设置参数如下:

Volume: ${200\mu }\mathrm{L}$

Number of cycles: 14

Speed Code: 9

6. 点击 Edit Wash Scheme，确认用 det1、det2 和水各清洗 4 次。点击 OK。
7. 按照电脑弹出框提示完成清洗和最后的排气。
8. 上样。
9. 除了刚完成上样的时候，都按照弹出框操作。不要按弹出框的提示拨向 Output，反而要拨向垂直位置。点击 OK。
10. 在注射器中的气泡已经排出并且机械臂停下后拨向 Output。
11. 开始剪切。
12. 完成样品剪切和回收后，执行步骤 6 和步骤 7 清洗仪器。
13. 清洗完毕后，点击 Manual Operation。

设置参数如下:

Volume: 500μL

Speed Code: 10

Valve: 0

14. 点击 Reinitialize 排空注射器两次。
15. 抽入  $500 \mu L$  水保存。

## 末端补平

16. 检查剪切样品的体积，加水至终体积为  $198 \mu L$ ，加入  $2 \mu L$  Lucigen 末端修复补平酶混合物。上下翻转颠倒或者轻弹离心管使之混匀，瞬时离心后室温孵育 30min 进行末端修复补平反应。
17. 用 QIAquick PCR 纯化柱纯化末端修复补平片段。用一个纯化柱。

i. 将末端修复补平反应液加入到  $600 \mu L$  的 ERC 缓冲液中并混匀。
ii. 将反应液/缓冲液混合物加入到 QIAquick 纯化柱，14 000g 离心 1min 或者将其放置于抽真空装置直至 ERC 混合物全部过柱。
iii. 离心结束后，弃去废液。
iv. 加  $750 \mu L$  PE 缓冲液，14 000g 离心 1min 或者将其放置于抽真空装置直至 PE 全部过柱。

v. 离心结束后，弃去废液。

vi. 将离心管旋转  $180^{\circ}$ ，14 000g 离心 1min。

vii. 将纯化柱放入新的 1.7mL 离心管，弃去废液管。

viii. 加入 30μL EB 缓冲液，室温孵育 1min，14 000g 离心纯化柱 1min。

ix. 再加入 30μL EB 缓冲液，室温孵育 1min，14 000g 离心纯化柱 1min。

x. 弃去纯化柱，保留含洗脱 DNA 的 1.7mL 离心管。

18. 取 $1\mu \mathrm{L}$ DNA 用 Quant-It dsDNA BR Assay Kit 测量纯化 DNA 的浓度，用分光光度计读取结果（可参见方案 11 或方案 12）。

## 环化接头连接

19. 在 $1.7 \mathrm{~mL}$ 离心管中混合以下组分:

| DNA | 59μL |
| --- | --- |
| 分子级水 | 21μL |
| 环化接头(20μmol/L): | 10μL |
| 快速连接缓冲液(2×) | 100μL |
| 总体积 | 190μL |

轻弹或者翻转离心管使其混匀。

20. 加入 $10\mu \mathrm{L} 2000\mathrm{U} / \mu \mathrm{L}$ 的连接酶至反应液中，轻弹或颠倒离心管混匀，瞬时离心后室温孵育 $15\mathrm{min}$ 进行连接反应。

21. 加入  $20 \mu L$   $10 \times$  凝胶上样缓冲液和  $2 \mu L$   $20 \%$  SDS 终止反应。

22. 65℃加热反应液 10min 后冰浴冷却，准备凝胶电泳。

## 用 FIGE 进行大小筛选

23. 混合 $200 \mathrm{~mL} 0.5 \times \mathrm{TBE}$ 和 $2 \mathrm{~g} \text { LE 琼脂糖 }$, 配制 $200 \mathrm{~mL} 1 \%$ 的 LE 琼脂糖凝胶。

24. 往电场反转凝胶电泳（FIGE）槽内倒入  $2.5 \, L \, 0.5 \times TBE$ ，打开 FIGE 冷却器，设置温度为  $14^{\circ}C$ 。

25. 向  $30 \mu L$   $100 ng/\mu L$  的 1 kb DNA 分子质量标准中加入  $3 \mu L$   $10 \times$  凝胶上样缓冲液。

26. 各取  $16.5 \mu L$  DNA 分子质量标准加到 1 号和 5 号上样孔。

27. 将全部样品加入到 3cm 宽的 3 号上样孔。

将样品和分子质量标准隔开一个泳道，尽量避免 DNA 分子质量标准污染。

28. 用 Auto Algorithm 选项运行 FIGE 胶，输入下限 3K、上限 15K，点击 Enter 键设置程序的剩余选项。开始电泳，大约需要 17.5h 完成。

29. 用 SYBR Green 染胶 45min。

30. 用水脱色 15min。

31. 用蓝光源（300nm）看凝胶中的 DNA 并切取 6.5～9.5kb 大小的区段。

32. 称量切下的胶块并转入 $15 \mathrm{~mL}$ 锥底管, 加入 3 倍体积的 QG 缓冲液 (例如, $3 \mathrm{~g}$ 的胶块加入 $9 \mathrm{~mL}$ 的 QG 缓冲液)。

33. 轻轻摇动离心管直至胶块完全溶解，需要 5\~10min。

▲不能振荡！

34. 用 1 个或者多个 QIAquick 凝胶提取柱纯化 DNA。单个柱子能处理的凝胶量上限约为 $400\mathrm{mg}$，因此要根据切下的凝胶重量来计算柱子数量。

i. 在每个 QIAquick 柱子中加入溶解了 400mg 凝胶的 OG 缓冲液。

ii. 14 000g 离心柱子 1min，或使用抽真空装置使 QG 混合液全部过柱。

iii. 离心，弃去废液。往柱子里加入更多的 QG 凝胶混合液并重复离心，直至 QG 凝胶混合液全部过柱。

iv. 按照步骤 17.iv～17.vii 纯化已连接片段。

v. 往第一个柱子加入  $20 \mu L$  、其他的柱子加入  $10 \mu L$  EB 缓冲液。

vi. 打开盖子室温孵育柱子 1min。然后盖上盖子，14000g 离心第一个柱子 1min。

vii. 弃掉第一个柱子，将第一个柱子的  $20 \mu L$  洗脱液加入第二个柱子。14 000g 离心第二个柱子 1min。

viii. 弃掉第二个柱子，将第二个柱子的  $20 \mu L$  洗脱液加入第三个柱子。14 000g 离心第三个柱子 1min。

ix. 弃掉第三个柱子，保留含有约  $40 \mu L$  洗脱 DNA 的 1.7 mL 离心管。

## 补齐反应

35. 在 $1.7 \mathrm{~mL}$ 离心管合并和混匀下列组分:

| LoxP-adaptor 连接 DNA | 38μL |
| --- | --- |
| 10×ThermoPol 缓冲液 | 5μL |
| PCR 核苷酸混合液(10mmol/L) | 4μL |
| Bst DNA 聚合酶,大片段(8U/μL) | 3μL |
| 总体积 | 50μL |

轻轻翻转混匀， $50^{\circ}$ C 温育 15min 进行补齐反应。

36. 按照说明书用 Quant-It dsDNA BR Assay Kit 测量 DNA 的量（也可参见方案 11）。

▲强烈推荐用荧光定量而不是用基于紫外吸收的定量方法。

在这一步中，DNA 的平均产量应该＞400ng，后续步骤需要至少 300ng DNA。如果获得的 DNA 量＞300ng，则将剩余的 DNA 用于环化反应；如果 DNA 产量＜300ng，则应重新合成。

37.（可选）DNA 样品可以  $4^{\circ}$ C 保存过夜。

## DNA 环化

38. 取 300ng 补齐的 DNA，加分子生物学级水至终体积为  $80 \mu L$ 。

39. 在 $0.2 \mathrm{~mL}$ 离心管内依次加入下列组分:

| Filled-in LoxP DNA(300ng)(自步骤35) | 80μL |
| --- | --- |
| 10×Cre缓冲液 | 10μL |
| Cre重组酶(1U/μL) | 10μL |
| 总体积 | 100μL |

轻轻翻转混匀。

40. 使用下述程序在 PCR 仪上进行反应:

```txt
37℃，45min  
70℃，10min  
4℃，永久
```

41. 用 $1 \mathrm{~mol} / \mathrm{L}$ DTT 储存液配制新鲜的 $100 \mathrm{mmol} / \mathrm{L}$ DTT, 振荡混匀, 放置于冰上。

DTT 100mmol/L 稀释液在当天用完就扔掉。

| 分子生物学级水 | 18μL |
| --- | --- |
| DTT(1mmol/L) | 2μL |
| 总体积 | 20μL |

42. 孵育完成后，向 Cre 酶处理的 DNA 反应液中加入 $1.1\mu \mathrm{L} 100\mathrm{mmol / L}$ DTT，上下翻转颠倒混匀，瞬时离心。