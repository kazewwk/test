43. 往上述样品中加入以下试剂:

| ATP(100mmol/L) | 1.1μL |
| --- | --- |
| Plasmid-Safe ATP-Dependent DNase(10U/μL) | 5.0μL |
| 外切核酸酶(20U/μL) | 3.0μL |

轻轻翻转，颠倒混匀。

44.  $37^{\circ}$ C 温育 30min 进行反应。

45. 在 PCR 仪内 $70^{\circ} \mathrm{C}$ 孵育 $30 \mathrm{~min}$ 热灭活。

46.（可选）DNA 样品  $4^{\circ}$ C 保存过夜。

## LoxP 环化 DNA 的片段化

47. 将  $110 \mu L$  DNA 样品转入 miniTUBE-Blue AFA 管，离心去除气泡。

48. 将样品放入 Covaris 水浴槽。

运行 Covaris 程序 8kb\_illumina:

Duty Cycle: 20%

Intensity: 5

Cycles/burst: 500

Time: 30 sec

49. 水浴锅中取出样品管并将溶液转移至 1.7mL 离心管中。

50. 合并被剪切的 DNA。如果只做了一份环化反应，则无需合并。

51. 往被剪切的 DNA 中加入 3 倍体积的 ERC 缓冲液，振荡。

52. 用 QIAquick PCR 纯化柱纯化。

i. 将反应液/缓冲液的混合液加入纯化柱。

ii. 14 000g 离心柱子 1min，或使用抽真空装置使 ERC 混合液全部过柱。

iii. 离心结束后，弃去废液。

iv. 加入  $750 \mu L$  PE 缓冲液。

v. 14 000g 离心柱子 1min，或使用抽真空装置使 PE 缓冲液全部过柱。

vi. 离心结束后，弃去废液。

v ii. 将离心管旋转  $180^{\circ}$ ，14 000g 离心 1min。

viii. 将纯化柱放入新的 1.7mL 离心管，弃去废液管。

ix. 加入  $20 \mu L$  EB 缓冲液，室温孵育 1 min，14 000 g 离心纯化柱 1 min。

x. 再加入  $20 \mu L$  EB 缓冲液，室温孵育 1min，14 000g 离心纯化柱 1min。

xi. 弃去纯化柱，保留含洗脱 DNA 的 1.7mL 离心管。

## 片段末端修复补平

53. 在 $1.7 \mathrm{~mL}$ 离心管内加入下述试剂:

| DNA | 38μL |
| --- | --- |
| 5×末端修复补平缓冲液 | 10μL |
| 末端修复补平酶混合液 | 2μL |
| 总体积 | 50μL |

振荡混匀，室温下孵育 30min 进行末端修复补平反应。

54. 加入 3 倍体积 ERC 缓冲液，振荡。

55. 按照步骤 52.i～52.viii 用 QIAquick PCR 纯化柱纯化末端，修复补平片段。

56. 用  $33 \mu L$  EB 缓冲液洗脱 DNA。室温孵育 1 min。

57. 取 $1\mu \mathrm{L}$ DNA 用 Quant-It dsDNA BR Assay Kit 测量纯化 DNA 的浓度，用分光光度计读取结果（可参见方案 11 或方案 12）。

## 末端配对加 A 尾

58. 用步骤 56 的纯化产物设置加 A 反应:

| 纯化的末端修复补平 DNA | 32μL |
| --- | --- |
| 10×Klenow 缓冲液 | 5μL |
| dNTP(1.0mmol/L) | 10μL |
| Klenow Exo (5U/μL) | 3μL |
| 总体积 | 50μL |

在 PCR 仪内  $37^{\circ}$ C 温育 30min。

59. 加入 3 倍体积 ERC 缓冲液，振荡。

60. 按照步骤 52.i～52.viii 用 QIAquick PCR 纯化柱纯化 DNA。

61. 用 $16 \mu \mathrm{L}$ EB 缓冲液洗脱 DNA。室温孵育 $1 \mathrm{~min}$ 。

## 末端配对接头连接

62. 计算需要多少皮摩尔的 DNA 接头（双链）。

i. 首先根据其大小计算需要多少皮摩尔的插入片段 DNA。

插入片段 DNA 的皮摩尔数=DNA 的微克数×(1pmol/660pg)× $10^{6}$ pg/μg×1/N N 是插入片段 DNA 的平均大小；

所需 DNA 接头=（插入片段 DNA 的皮摩尔数）×50

例如，对于 30ng 平均大小为 850bp 的 DNA:

插入片段 DNA 的皮摩尔数

$$
= 0. 0 3 \mu \mathrm{g} \times (1 \mathrm{pmol}) / (6 6 0 \mathrm{pg}) \times 1 0 ^ {6} \mathrm{pg} / \mu \mathrm{g} \times 1 / 8 5 0 = 0. 0 5 3 \mathrm{pmol}
$$

所需 DNA 接头

$$
= (0. 0 5 3 \mathrm{pmol}) \times 5 0 = 2. 7 \mathrm{pmol}
$$

63. 将 PE Illumina 接头寡聚核苷酸混合液从  $4 \mu mol/L$  稀释至  $1 \mu mol/L$ 。使用  $2.7 \mu L$   $1 \mu mol/L$  DNA 接头储存液。

或者用网站 http://www.Promega.com/biomath/default.htm.上的计算器。选择 dsDNA:“micrograms to picomoles”，输入数字得到样品的皮摩尔数。

例如:以步骤 62 的例子为例，选择 “micrograms to picomoles” 回答以下问题。

- How long is your DNA(in base pairs)? 输入 850
- How many micrograms of DNA do you have? 输入 0.03

然后点击 Calculate ，会给出答案:0.053pmol DNA

将样品皮摩尔数乘以 50（50 倍）

对于带索引文库，用 “ILL Index Adaptor Duplex” 代替 “ILL\_indexAdaptor\_Duplex\_IDT”

64. 在 $1.7 \mathrm{~mL}$ 离心管混合下述组分:

| 加A尾的DNA | 15μL |
| --- | --- |
| 2×快速连接酶缓冲液 | 25μL |
| ILL PE forked adaptor duplex或者ILL index adaptor duplex | xμL |
| 水 | yμL |
| 总体积 | 45μL |

65. 轻弹或者翻转颠倒混匀，加入  $5 \mu L$   $2000 U/\mu L$  的连接酶，室温孵育 15 min。

66. 用 AMPure XP 磁珠纯化 DNA。

i. 往 DNA 样品中加入  $75 \mu L$  校准的 AMPure 磁珠。
ii. 于离心管旋转器上室温孵育 5min。
iii. MPC 上静置 2min 以分离上清液和磁珠。
iv. 吸去上清液。
v. 用  $500 \mu L$  70%乙醇清洗磁珠两遍。
vi. 真空干燥器中抽干 2min。
vii. 加入  $50 \mu L$  EB 缓冲液，振荡，室温孵育 1 min。
viii. MPC 上静置 1min。
ix. 将上清转移到新的 1.7mL 离心管。

## 末端配对文库的固定

67. 吸取  $25 \mu L$  链亲和素磁珠到一个新离心管中，使用 MPC 聚集磁珠并吸去缓冲液。
68. 使用 MPC，加入  $50 \mu L$   $2 \times$  文库结合缓冲液清洗磁珠两遍。
每次清洗时涡旋混匀。
69. 用 $50\mu \mathrm{L}2\times$ 文库结合缓冲液重悬磁珠，加入 $50\mu \mathrm{L}$ 清洗过的链亲和素磁珠到步骤65的 $50\mu \mathrm{L}$ DNA中，涡旋混匀，置于离心管旋转器上室温孵育 $15\mathrm{min}$。
70. 用 MPC 聚集磁珠并吸去上清液。
71. 用 $500 \mu \mathrm{L}$ TE 缓冲液清洗固定化的文库三次。每次清洗要涡旋混匀。
72. 吸去全部 TE 缓冲液，用  $30 \mu L$  TE 缓冲液重悬磁珠。

## 末端配对 PCR 的优化

执行步骤 73 或者步骤 74。

## 对于 Nonindex 文库

73. 在 $0.2 \mathrm{~mL}$ 离心管中加入下述组分为一个反应体系:

| DNA/磁珠 | 2μL |
| --- | --- |
| Phusion 混合液(2×) | 25μL |
| PE PCR 引物 1.0 (8μmol/L) | 0.5μL |
| PE PCR 引物 2.0 (8μmol/L) | 0.5μL |
| 分子级水 | 22μL |
| 总体积 | 50μL |

## 对于 Index 文库

74. 从 Index 1～48 中挑选一个 Index PCR 引物。在同一个流动槽中运行不同的文库，为每个文库挑选不同的 Index PCR 引物。

| DNA/磁珠 | 2μL |
| --- | --- |
| Phusion 混合液(2×) | 25μL |
| Multiplexing 引物 1.0 (8μmol/L) | 1uL |
| Multiplexing 引物 2.0 (0.5μmol/L) | 1μL |
| Index PCR 引物 (8μmol/L) | 1μL |
| 分子级水 | 20μL |
| 总体积 | 50μL |

## 75. 设置两个 PCR 程序。

程序1

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 1 | 98°C, 30s |  |  |
| 14个循环 | 98°C, 10s | 65°C, 30s | 72°C, 30s |

程序结束后维持在  $4^{\circ}$ C。

程序2

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 2个循环 | 98°C, 10s | 65°C, 30s | 72°C, 30s |

程序结束后维持在  $4^{\circ}$ C。

76. 取 6 个 0.2mL 离心管，分别标记为:PCR-14, PCR-16, PCR-18, PCR-20, PCR-22, PCR-24。

77. 运行 PCR 程序 1，从标记为 PCR-14 的 0.2mL 离心管中吸出 5μL 反应液。

78. 运行 PCR 程序 2 继续进行 PCR 优化，从标记为 PCR-16 的 $0.2 \mathrm{~mL}$ 离心管中取出 $5 \mu \mathrm{L}$ 反应液。

79. 重复步骤 78 完成剩余的 4 个循环数优化试验（PCR-18，PCR-20，PCR-22，PCR-24）。

80. 取  $5 \mu L$  反应产物加入  $1 \mu L$  上样染料，快速涡旋并离心。

81. 制备 2.2% FlashGel, 13 孔内各加 4μL 水, 第 1 和第 8 泳道各加 2μL Flash 50\~1500bp 分子质量标记物。

82. 第 2～7 泳道中各加  $6 \mu L$  PCR 产物，275V 电泳 5～7min。

83. 凝胶照相。确定过度扩增的循环数。进行大规模 PCR 时采用未显现过度扩增的最大循环数。例如，如果 PCR-22 和 PCR-24 显现过度扩增而其他循环数未显现，则使用 PCR-20 的条件。一个样本的 PCR 结果见图 11-10（例如，Turtle 24×泳道显现过度扩增）。

![](images/page_179_image_17.jpg)

<details>
<summary>text_image</summary>

Turtle
16x 18x 20x 22x 24x 50-500-bp ladder
Macaque
16x 18x 20x 22x 24x
</details>

图 11-10 扩增循环数优化试验的凝胶电泳。

## 大规模 PCR

84. 每个反应的用量乘以反应数，制备 PCR 反应混合液。我们推荐进行 15 个反应。

PCR 组分（用于 nonindex 文库）

| DNA/磁珠 | 2μL |
| --- | --- |
| Phusion 混合液(2×) | 25μL |
| PE PCR 引物 1.0(8μmol/L) | 0.5μL |
| PE PCR 引物 2.0(8μmol/L) | 0.5μL |
| 分子级水 | 22μL |
| 总体积 | 50μL |

PCR 组分（用于 index 文库）

| DNA/磁珠 | 2μL |
| --- | --- |
| Phusion 混合液(2×) | 25μL |
| Multiplexing 引物 1.0(8μmol/L) | 1μL |
| Multiplexing 引物 2.0(0.5μmol/L) | 1μL |
| Index PCR 引物(8μmol/L) | 1μL |
| 分子级水 | 20μL |
| 总体积 | 50μL |

引物寡聚核苷酸序列见表 11-2。

85. 根据前一部分优化结果设定 PCR 程序:

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 1 | 98°C, 30s |  |  |
| $N$个循环a | 98°C, 10s | 65°C, 30s | 72°C, 30s |
| 最后一轮 |  |  | 72°C 5min |

程序结束后维持在  $4^{\circ}$ C。

a. 能得到扩增产物的最少循环数（N）。

86. DNA 扩增。
87. 循环结束后，将所有样品合并到一个 $15\mathrm{mL}$ 锥形管中，用EB缓冲液调节至终体积为 $750\mu \mathrm{L}$ 。
88. 加入 3 倍体积 ERC 缓冲液，涡旋。
89. 用 QIAquick PCR 纯化柱按照步骤 52.i～52.viii 纯化 DNA。
90. 用  $50 \mu L$  EB 缓冲液洗脱 DNA。室温孵育 1min。
91. 重复步骤 90。弃掉柱子，保留含 $100 \mu \mathrm{L}$ 洗脱 DNA 的 $1.7 \mathrm{~mL}$ 离心管。

## 双重 AMPure 磁珠纯化进行片段大小选择

92. 涡旋振荡 AMPure 磁珠。

使用校准的 AMPure 磁珠非常关键。校准方法见附加方案 AMPure 磁珠校准。

93. 根据下面公式加入 $x \mu \mathrm{L}$ AMPure 磁珠。往公式中输入 AMPure 磁珠的双末端截止值（PE 截止值）（PE 截止值的测定见附加方案“AMPure 磁珠校准”）。

$$
x \mu \mathrm{L} = (\mathrm{PE} \text {截止值}) \times 1 0 0
$$

$$
x \mu \mathrm{L} = 0. 6 5 \times 1 0 0 = \text {在样品中加入} 6 5 \mu \mathrm{L} \text {AMPure} \text {磁珠}
$$

94. 涡旋混匀，室温静置 5min。
95. 使用 MPC 使磁珠聚集在离心管壁上。
96. 将上清液吸出至新的离心管中，确保上清体积等于  $100 \mu L + x \mu L$  （来自步骤 93）；

如果不足，则加 Tris-HCl 至该体积（例如， $100\mu L + 65\mu L = 165\mu L$ ）。在上清液中加入  $75\mu L$   $10mmol/L$  Tris-HCl（pH 7.5～8.5），然后加入  $y\mu L$  AMPure 磁珠:

$$
y \mu \mathrm{L} = x (\text {来自步骤} 9 3) \mu \mathrm{L} + 2 0 \mu \mathrm{L}
$$

例如，

$$
y = 65 \mu \mathrm{L} + 20 \mu \mathrm{L} = 85 \mu \mathrm{L}
$$

97. 涡旋混匀，室温静置 5min。
98. 使用 MPC 使磁珠聚集在离心管壁上。在清洗时把离心管一直放在 MPC 上。
99. 弃掉上清液，用  $500 \mu L$  70% 乙醇清洗磁珠两遍，每次清洗孵育 30s。

100. 快速离心并弃去所有上清液。

101. 37℃放置 2min 风干 AMPure 磁珠，当看到磁珠开始出现裂缝时即可，不能过度干燥。
102. 加入  $30 \mu L$  10mmol/L Tris-HCl（pH 7.5～8.5），涡旋重悬磁珠，将双末端文库从 AMPure 磁珠上洗脱下来。

103. 使用 MPC 聚集磁珠到离心管壁上，将上清液转至新离心管，弃掉磁珠。

## 最终文库定量

104. 取  $1 \mu L$  步骤 103 的最终样品加到 Agilent 2100 Bioanalyzer DNA 1000 芯片上验证其大小范围。
105. 取 $1 \mu \mathrm{L}$ 最终样品用 Quant-It dsDNA HS Assay Kit 测量纯化 DNA 的浓度，用荧光计读取结果（可参见方案 11 或方案 12）。
106. 将上述值输入 Illumina 文库稀释计算器（Illumina Library Dilution Calculator）中，将双末端文库稀释至 5nmol/L。

## 附加方案 AMPure 磁珠校准

在本方案的文库制备过程中，AMPure 磁珠用于去除文库中过小或者过大的 DNA 片段。由于不同批次 AMPure 磁珠的分子排阻特性具有高度可变性，因此每次购买到的 AMPure 磁珠都要进行校准以测定其分子排阻特性。校准结果将决定在文库制备过程中要用到的 AMPure 磁珠与 DNA 样品比例  $(V:V)$ ，以构建适用于 GS FLX Titanium 化学原理测序的最佳大小文库。

在 AMPure 磁珠校准试验中，将 100～1500bp DNA 分子质量标记物和不同磁珠-DNA 比的 AMPure 磁珠孵育，比值范围为 0.5:1 至 1:1（V:V），每个磁珠-DNA 比将提供不同的片段大小截止值参数。通过用 Agilent Bioanalyzer DNA 7500 LabChip 分析磁珠上滞留的 DNA 来评估这些截止值，记录处于 200～500bp 范围的峰值（DNA 浓度）区间。比较校准试验结果和通过经验得到的最优数据，决定所测批次磁珠用于 DNA 文库构建的最佳比值。

![](images/page_181_image_23.jpg)

## 方法

1. 标记 11 个 $1.7 \mathrm{~mL}$ 离心管用于本试验一系列磁珠-DNA 比；其范围如表 11-3 所示，从 $0.50:1$ 到 $1.00:1$ ，增量为 0.05。
2. 在一个新离心管中加入 $48\mu \mathrm{L} 100 \sim 1500\mathrm{bp}$ DNA 分子质量标记物，用 $1152\mu \mathrm{L}$ 分子生物学级水稀释。

3. 往每个标记的离心管中精确地加入  $100 \mu L$  稀释的 DNA 分子质量标记物。

4. 剧烈振荡装有 AMPure 磁珠的管子，取出 $900 \mu \mathrm{L}$ 到新离心管用于下面的试验。

5. 用吸取 $100\mu \mathrm{L}$ 稀释的DNA分子质量标记物的同一个移液器，往每个样品中加入适量的磁珠。一定要按下述方式操作。

- 每次吸取前振荡磁珠。
- 每次吸取磁珠更换吸头。
- 慢慢吸出磁珠，确保没有吸入空气以及在吸头外面没有磁珠。
- 慢慢将磁珠推出，确保所有的磁珠都加入到样品中。

表 11-3 每种磁珠-DNA 比所用的稀释的 DNA 分子质量标记物和 AMPure 磁珠体积

| 磁珠/DNA(体积比) | 稀释的 DNA 分子质量标记物/μL | AMPure 磁珠/μL |
| --- | --- | --- |
| 0.50:1 | 100 | 50 |
| 0.55:1 | 100 | 55 |
| 0.60:1 | 100 | 60 |
| 0.65:1 | 100 | 65 |
| 0.70:1 | 100 | 70 |
| 0.75:1 | 100 | 75 |
| 0.80:1 | 100 | 80 |
| 0.85:1 | 100 | 85 |
| 0.90:1 | 100 | 90 |
| 0.95:1 | 100 | 95 |
| 1:1 | 100 | 100 |

6. 振荡所有离心管，室温孵育 5min。

7. 用 MPC 仪沉淀磁珠，由于悬液比较黏稠，可能需要几分钟。

8. 弃掉上清，用  $500 \mu L$  70% 的乙醇清洗磁珠两遍，每次清洗时孵育 30s。

随着磁珠-DNA 比的提高截止值逐步降低，更长的 DNA 片段将结合 AMPure 磁珠，在每个孵育条件中小于截止值的 DNA 分子将在下一步被洗掉。

9. 吸去每个离心管中的上清，将 AMPure 磁珠彻底风干。为了减少干燥时间，可以将 AMPure 磁珠放入  $37^{\circ}$ C 烘箱，当能看到沉淀开始破裂时即可。

10. 从 MPC 中取出离心管，每管加入  $10 \mu L$  Tris-HCl，振荡重悬磁珠。

11. 用 MPC 仪沉淀磁珠，将上清液转移至一套标记好的新离心管中。

12. 加入 $6 \mu \mathrm{L}$ 水稀释 $4 \mu \mathrm{L}$ 未处理的 DNA 分子质量标记物作为对照。

13. 从磁珠筛选的和对照 DNA 分子质量标记物中各取 $1\mu \mathrm{L}$ 用一个 Bioanalyzer DNA 7500 LabChip 进行分析。

## 磁珠校准分析

结果表明，随着磁珠-DNA 比降低，DNA 分子质量标记物样品中的小片段将逐渐被去除（即只有大片段能结合于低比值的磁珠）。用 12 通道 LabChip 监测所有样品（包括未处理的对照分子质量标记物）在 200～500bp 范围的浓度峰值来评估校准试验。900bp 处的峰应该存在于所有待测磁珠-DNA 比样品中，并用于所有通道的标准化。

- 对每个通道，用 200bp、300bp、400bp 和 500bp 处的 DNA 浓度值（ng/μL）除以该通道 900bp 处的 DNA 浓度值。
- 将 11 个样品的这 4 个值与表 11-4 中第 2 和第 3 列的数值比较。
- 将能产生与表 11-4 中第 2 列数值最相似数值的磁珠-DNA 比用作步骤 93 的截止值。
- 要确保对照通道的峰值比与表 11-4 中第 3 列数值相符。

表 11-4 低分子质量峰与 900bp 峰 DNA 浓度的最优比值

| 峰比(DNA 浓度) | 最优 PE 截止值 | 对照 DNA 的比值 |
| --- | --- | --- |
| 200/900 | N/A | 0.7 |
| 300/900 | 0.25 | 1.1 |
| 400/900 | 0.4 | 1.4 |
| 500/900 | 1.5 | 3.4 |

![](images/page_183_image_4.jpg)

## 配方

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

文库结合缓冲液（2×）（2mol/L NaCl/2×Tris-EDTA 缓冲液）100mL

| Sigma 水 | 58mL |
| --- | --- |
| NaCl (5mol/L) | 40mL |
| TE 缓冲液 (100×, 1:0.1 mol/L) | 2mL |

1. 在 250mL 烧杯内按上述次序加入并混合试剂。
2. 搅拌 30min，测量并记录电导率、pH 和密度。
3. 每管 $10 \mathrm{~mL}$ 分装于 $15 \mathrm{~mL}$ 锥底管。贴上标签（用绿标签以区分用途）并加入 IMP 数据库。该溶液保质期 3 个月，要在标签上写好过期日期。$-20^{\circ} \mathrm{C}$ 保存。

## 方案 9 RNA-Seq:RNA 反转录为 cDNA 及其扩增

Ovation RNA-Seq 试剂盒可快速、简便地用总 RNA 扩增得到 cDNA。该方法从转录物的 3'端起始扩增，跨越整个转录序列范围；因其读长分布于整个转录序列，故非常适合下一代测序。本方案扩增的 cDNA 将用于构建为 Illumina Genome Analyzer II 平台而优化的文库。

附加方案介绍样品反转录为 cDNA 之前如何去除已降解的小 RNA。

![](images/page_183_image_16.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

DNA 7500 试剂（Agilent，目录号 5067-1506）

乙醇（100%和70%）

Minelute PCR 纯化试剂盒（QIAGEN, 目录号 28004）

Ovation RNA-Seq 试剂盒（NuGEN, 目录号 7100-08）

Quant-iT dsDNA BR Assay 试剂盒（Life Technologies，目录号 Q32853）

Quant-iT RNA Assay 试剂盒（Life Technologies，目录号 P11496）

RNA Nano Assay (Agilent)

RNA 6000 Pico 试剂盒（Agilent，目录号 5067-1513）

要扩增的 RNA 样品

TE 缓冲液（1×）&lt;A&gt;

## 设备

2100 生物芯片分析仪（Agilent，目录号 G2939AA）

荧光光度计（如 Qubit; Life Technologies）

Qubit 检测管或类似品牌（Life Technologies，目录号 Q32856）

SPRIPlate 96R ring magent plate (Beckman Coulter, 目录号 000219)

以前是96孔板。

带 0.2mL 离心管加热板、加热盖和 100μL 反应容量的 PCR 仪

离心管（1.7mL 和 0.7mL）

PCR 用薄壁离心管（0.2mL）

![](images/page_184_image_16.jpg)

## 方法

## RNA 评估

1. 对样品中的 RNA 进行定量，必要时可稀释（参见方案 12～14）。如有必要，按照附加方案 “RNAclean XP 磁珠纯化”（RNA-Seq 前）描述的方法去除 RNA 样品中已降解的小 RNA。
2. 稀释一份 RNA 样品至试验所需浓度范围:25～500ng/μL 用于 RNA Nano Assay（Agilent）或者 50～5000pg/μL 用于 RNA 6000 Pico Assay（Agilent）。用 RNA Nano Assay 或者 RNA 6000 Pico Assay 评估 RNA 样品的质量（范例见图 11-11）。

## cDNA 第一条链的合成

3. 轻弹含有 First-Strand Enzyme Mix（蓝色盖子，来自 NuGEN Ovation RNA-Seq 试剂盒的 A3），瞬时离心，放置于冰上。

4. 室温融化含有 First-Strand Primer Mix（蓝色盖子的 A1）、First-Strand Buffer Mix（蓝色盖子的 A2）和水（绿色盖子的 D1）的离心管，振荡，瞬时离心，放置于冰上。

5. 在 0.2mL PCR 管中为每份 cDNA 文库构建混合下述组分:

| First-strand primer mix | 2μL |
| --- | --- |
| RNA(100ng) | xμL |
| 水 | (5-x) μL |

总体积为  $7 \mu L$ ，RNA 不能超过 100ng。

将 PCR 管瞬时离心，放置于冰上。

RNA 的量超过 100ng 时可能会抑制扩增，必要时可以把反应体积增加到  $8 \mu L$ 。

6. 将 PCR 管放入预热至  $65^{\circ}$ C 的 PCR 仪，孵育 5min 后冷却至  $4^{\circ}$ C，取出 PCR 管放置于冰上。
7. 在 0.7mL 离心管内为每个样品混合 2.5μL First-Strand Buffer Mix 和 0.5μL First-Strand Enzyme Mix。吹打混匀，瞬时离心，放置于冰上。

![](images/page_185_chart_2.jpg)

<details>
<summary>line</summary>

| Metric | Value |
| --- | --- |
| 样品 2 综合结果 | LNCap 稀释的 RNA |
| RNA 范围 | 117.4 |
| RNA 浓度 | \(454pg/\mu L\) |
| rRNA 比率 (28s/18s) | 1.5 |
| RNA 完整性计数 (RIN) | 8.6(8.02.07) |
| 结果标记颜色 | — |
| 结果标记标签 | RIN:8.60 |
</details>

图 11-11 RNA 定量结果（彩图请扫封底二维码）。

8. 向来自步骤 5 的每个离心管加入 $3 \mu \mathrm{L}$ 稀释的酶混合液（总体积 $= 10 \mu \mathrm{L}$），吹打 $6 \sim 8$ 次混匀，瞬时离心。

9. 将离心管放入  $4^{\circ}$ C 预冷的 PCR 仪，按下述条件合成 cDNA 第一条链:

i.  $4^{\circ}$ C, 1min
ii.  $25^{\circ}$ C, 10min
iii.  $42^{\circ}$ C, 10min
iv.  $70^{\circ}$ C, 15min
v. 冷却至  $4^{\circ}$ C。

10. 取出离心管放置于冰上，立即继续 cDNA 第二条链的合成。

## cDNA 第二条链的合成

11. 将 AMPure RNA Clean 磁珠放在实验桌上，自然升温至室温。
12. 轻弹含有 Second-Strand Enzyme Mix（黄色盖子的 B2）的离心管，瞬时离心，放置于冰上。
13. 室温融化含有 Second-Strand Buffer Mix (黄色盖子的 B1) 的离心管，振荡，瞬时离心，放置于冰上。
14. 在 0.7mL 离心管内为每个样品混合 9.7μL Second-Strand Buffer Mix 和 0.3μL Second-Strand Enzyme Mix，吹打混匀，瞬时离心，放置于冰上。
15. 往来自步骤 10 的每个第一条链反应管中加入 $10 \mu \mathrm{L}$ 稀释的酶混合液（总反应体积= $20 \mu \mathrm{L}$），吹打 6～8 次混匀，放置于冰上。
16. 将离心管放入  $4^{\circ}$ C 预冷的 PCR 仪，按下述条件合成 cDNA 第二条链:

i.  $4^{\circ}$ C, 1min
ii.  $25^{\circ}$ C, 10min
iii.  $50^{\circ}$ C, 30min
iv.  $80^{\circ}$ C, 20min
v. 冷却至  $4^{\circ}$ C。

17. 取出离心管放置于冰上，立即继续 cDNA 纯化。

## cDNA 纯化

18. 开始前先确保 RNA Clean 磁珠（来自步骤 11）已经完全达到室温。翻转离心管重悬磁珠。

▲不能振荡或者离心沉淀磁珠。

19. 在室温条件下往每个离心管中加入 $32 \mu \mathrm{L}$ 磁珠, 吹打 10 次混匀, 室温孵育 $10 \mathrm{~min}$ 。

20. 将离心管放置于 SPRI 96R 磁板上使磁珠沉淀。

21. 从每个离心管中吸去 $42 \mu \mathrm{L}$ 结合缓冲液。

22. 用 $200 \mu \mathrm{L}$ 新配置的 $70 \%$ 乙醇清洗磁珠 3 遍。尽可能地去除乙醇。

23. 放置于磁板上风干至少 15\~20min。

24. 用结合在干磁珠上的 cDNA 立即进行 SPIA 扩增。

## SPIA

25. 室温融化含 SPIA Primer Mix（红色盖子的 C1）和 SPIA Buffer Mix（红色盖子的 C2）的离心管。振荡混匀，瞬时离心后放置于冰上。

26. 冰上融化 SPIA Enzyme Mix（红色盖子的 C3），轻轻地上下颠倒 5 次使之混匀，瞬时离心后放于冰上保存。

27. 在 0.7mL 离心管按照下表配制 SPIA 反应混合液。

▲确保最后加酶。吹打混匀，瞬时离心后放置于冰上，立即使用。

| 试剂 | 每份反应 |
| --- | --- |
| SPIA Primer Mix | 10μL |
| SPIA Buffer Mix | 20μL |
| SPIA Enzyme Mix | 10μL |

28. 向每个含有干磁珠（来自步骤 23）的离心管中加入  $40 \mu L$  SPIA 反应混合液。用调至  $30 \mu L$  刻度的移液器吹打 8～10 次混匀。

29. 将离心管放入预冷至  $4^{\circ}$ C 的 PCR 仪，用下述程序进行反应:

i.  $4^{\circ}$ C, 1min
ii.  $47^{\circ}$ C, 60min
iii.  $95^{\circ}$ C, 5min
iv. 冷却至  $4^{\circ}$ C。

30. 取出离心管放置于冰上。

31. 将离心管放置于 SPRI 96R 磁板上，沉淀磁珠 5min。

## SPIA 后修饰 I

32. 将含有 $35 \mu \mathrm{L}$ 已扩增 cDNA 的上清液转移到新的 $0.2 \mathrm{~mL}$ 离心管中。弃去磁珠。

33. 室温融化 post-SPIA Primer Mix（紫色盖子的 E1），振荡混匀，瞬时离心后放置于冰上。

34. 往  $35 \mu L$  样品中加入  $5 \mu L$  引物混合物，吹打  $6 \sim 8$  次混匀，瞬时离心后放置于冰上。

35. 将离心管放入预热至  $98^{\circ}$ C 的 PCR 仪孵育 3min。冷却至  $4^{\circ}$ C。

36. 取出离心管放置于冰上，立即进行 SPIA 后修饰 II。

## SPIA 后修饰 II

37. 室温融化 post-SPIA Buffer Mix（紫色盖子:E2），振荡混匀，瞬时离心后放置于冰上。

38. 瞬时离心 post-SPIA Enzyme Mix（蓝紫色盖子:E3），放置于冰上。

39. 在 $0.7\mathrm{mL}$ 离心管按照下表配制SPIA后修饰混合液，吹打混匀，瞬时离心后放置于冰上。

| 试剂 | 每份反应 |
| --- | --- |
| Buffer Mix | 5μL |
| Enzyme Mix | 5μL |

40. 往每 $40\mu \mathrm{L}$ 反应液（来自步骤36）中加入 $10\mu \mathrm{L}$ SPIA后修饰混合液。

41. 用调至 $40 \mu \mathrm{L}$ 刻度的移液器吹打 $6 \sim 8$ 次混匀, 瞬时离心后放置于冰上。

42. 将离心管放入预冷至 $4^{\circ} \mathrm{C}$ 的PCR仪，按下述条件进行反应:

i. $4^{\circ} \mathrm{C}, 1 \mathrm{~min}$
ii.  $30^{\circ}$ C, 10min
iii.  $42^{\circ}$ C, 15min
iv.  $75^{\circ}$ C, 10min
v. 冷却至  $4^{\circ}$ C。

43. 取出离心管，瞬时离心后放置于冰上。 $-20^{\circ} \mathrm{C}$ 保存扩增的 cDNA。

## 扩增 cDNA 的纯化

44. 按下述过程用 MinElute 柱纯化扩增 cDNA。

i. 加入 5 倍样品体积的 PB 缓冲液（250μL）。
ii. 用新配制的 80%乙醇洗两遍。
iii. 瞬时离心去掉柱子里的水分。
iv. 用  $30\mu L$   $1\times TE$  缓冲液（ $2\times15\mu L$ ）洗脱样品。
v. 孵育 2min。
vi. 离心回收 cDNA。

## 双链 cDNA 得率的定量

45. 每个双链 cDNA 样品配制一份 10 倍稀释液，用稀释样品参照方案 14 进行 Qubit 分析（dsHS）。
46. 每个样品配制一份约 $50\mathrm{ng} / \mu \mathrm{L}$ 的稀释液，用 Agilent DNA7500 仪器分析稀释样品。cDNA 大小范围应该是从 $< 100\mathrm{bp}$ 到 $1.5\mathrm{kb}$，且以 $< 1\mathrm{kb}$ 的为主（范例见图 11-12）。

![](images/page_187_chart_27.jpg)

<details>
<summary>line</summary>

| Peak | Value (bp) |
| --- | --- |
| 50 | 50 |
| 348 | 348 |
| 10380 | 10380 |
</details>

样品 3 的总体结果:ALS 4 枕叶皮质（1015268）

峰的数目: 1

样品 3 中峰的表格 ALS 4 枕叶皮质（1015268）

| 峰 | 大小/bp | 浓度/(ng/μL) | 体积摩尔浓度/(nmol/L) | 观测值 |
| --- | --- | --- | --- | --- |
| 1 | 50 | 8.30 | 251.5 | 低分子质量标记物 |
| 2 | 348 | 48.11 | 209.5 |  |
| 3 | 10.380 | 4.20 | 0.6 | 高分子质量标记物 |

图 11-12 cDNA 定量结果（彩图请扫封底二维码）。

47. 进行 Illumina 文库构建（参见方案 4～8）。PE 文库构建参见下述修正版 Illumina PE 文库构建（仅用于 NuGEN cDNA）。

如果起始 RNA 被降解，cDNA 片段将变小，几乎没有大于 700bp 的片段。如果这样的话，应可以略过 cDNA 剪切直接进行 cDNA 末端修复。

Illumina 文库构建通常需要 500ng cDNA，不过 1μg 也可以。

## 修正版 Illumina PE 文库构建（只用于 NuGENcDNA）

1. 往 Covaris microTube 中加入下述组分

| 样品 | cDNA 量(1μg) | 5×Lucigen DNA Terminator End Repair Buffer | 无核酸酶水 | 终体积 |
| --- | --- | --- | --- | --- |
| 样品 cDNA | $x\mu L$ | 10μL | $y\mu L$ | 50μL |

2. 振荡后瞬时离心。
3. 用 Covaris 程序（prog2-5DC-4I-200CB-90s）进行片段化。
4. 将样品转移到 1.7mL 离心管中。

## 末端修复

5. 往每个 1.7mL 离心管中加入 2μL Lucigen DNA 终止子末端修复酶。
6. 室温孵育 30min，然后  $70^{\circ}$ C 孵育 15min 热灭活。

## AMPure XP 大小筛选

7. 往样品中加入 1.3 倍体积的 AMPure XP Cleanup 磁珠[参见附加方案 “RNAclean XP 磁珠纯化”（RNA-Seq 前）]

i. 往样品中加入 1.3 倍体积（67.6μL）的 AMPure XP 磁珠。
ii. 振荡混匀。
iii. 室温孵育 10min。
iv. 放置于 MPC 上使磁珠沉淀。
v. 弃掉上清。
vi. 用  $500 \mu L$  70% 乙醇清洗磁珠两遍。
vii. 风干。
viii. 用  $33 \mu L$  EB 缓冲液洗脱，振荡重悬，放置于 MPC 上使磁珠沉淀。
ix. 将洗脱的 DNA 转移至 0.2mL PCR 管。

8. 继续 Illumina PE 文库构建的加 A 尾反应及后续步骤。

对方案 4 来说，这是步骤 9（前 7 步代替了方案 4 的步骤 1～8）。

# 附加方案 RNAClean XP 磁珠纯化（RNA-Seq 前）

该方法有时用于从 RNA 样品中去掉大多数已经降解的小 RNA 片段（范例见图 11-13）；其成功率达不到百分之百，不能确保用 NuGEN Ovation RNA-Seq 试剂盒一定能得到长片段 cDNA。

![](images/page_189_image_4.jpg)

## 方法

1. 往新的 1.7mL 离心管中加入  $1 \mu g$  降解的 RNA 样品。

2. 用 1.6 倍体积 RNA Clean XP 磁珠（不是 AMPure XP）进行纯化。

i. 轻轻吹打或者轻弹混匀（RNA 不能振荡）。

ii. 室温孵育 10min。

iii. 放置于 MPC 上使磁珠沉淀（5min）。

iv. 吸去上清液。

v. 用  $500 \mu L$  新配制的 70% 乙醇清洗磁珠两遍，每次清洗孵育 30s 后吸去上清液。

vi. 室温放置 15\~20min 风干磁珠。

vii. 用  $13 \mu L$  无核酸酶的水洗脱样品。

3. 从每个样品取 $1 \mu \mathrm{L}$ 进行 Qubit RNA Assay。

4. 再从每个样品取 $1 \mu \mathrm{L}$ 稀释至约 $5 \mathrm{ng} / \mu \mathrm{L}$ 。

5. 取  $1 \mu L$  稀释的样品进行 Agilent RNA 6000 Pico Assay，每个样品两次重复。

![](images/page_189_image_18.jpg)

图 11-13 RNA 纯化范例。（A）范例 1:RNA 纯化前。（B）范例 1:RNA 纯化后。（C）范例 2:RNA 纯化前。（D）范例 2:RNA 纯化后（彩图请扫封底二维码）。

## 方案 10 液相外显子组捕获

本方案介绍基因组 DNA（gDNA）末端配对文库的构建，以及后续的用 NimbleGen 序列捕获探针和 Illumina TruSeq 寡核苷酸方法捕获基因组特定区段。捕获的 DNA 经过纯化和定量后适于用作 Illumina 测序模板。本方案是最常用的外显子组捕获方法。从前用的是固相方法，但是现在已经被液相方法所取代，部分原因是由于许多公司各自开发特定的试剂。有关液相捕获外显子组方法的优缺点见本章导言“定向测序:概述”部分的讨论（也可参见本章导言部分的图 10-1）

附加方案包括 “AMPure 磁珠纯化和琼脂糖凝胶大小筛选”。

![](images/page_190_image_5.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

琼脂糖（Bio-Rad，低融点）

安捷伦生物分析仪 DNA 1000 和 DNA 12000 试剂

用于 DNA 样品浓缩和纯化的 AMPure XP 磁珠（Beckman Coulter）

条形码（Bioo Scientific NEXTflex）

荧光定量级 COT 人类 DNA（1mg/mL，1mL）

洗脱缓冲液（EB）

EB 是一种通用缓冲液，首先由 QIAGEN 公司推出，其成分为 10mmol/L Tris (pH8.0)。水也可以作为 DNA 缓冲液，但当 DNA 浓度过高或者 DNA 溶液反复冻融时会导致 DNA 的降解。应根据实验方案选择合适的缓冲液。

End Repair Buffer Mix (NEXTflex)

End Repair Enzyme Mix (NEXTflex)

乙醇（100%）

外显子组文库探针（NimbleGen SeqCap EZ Choice 或者 SeqCap EZ 人类外显子组文库 V2.0 探针）

荧光光度计试剂（Qubit 或者 Quant-iT 试剂盒）

基因组 DNA 样品（gDNA）

杂交试剂盒和纯化试剂盒（NimbleGen）

无核酸酶的水

HF 缓冲液（2×）带 Phusion 高保真性酶（New England Biolabs）

QIAquick DNA 纯化试剂盒 (QIAGEN)

重悬缓冲液（Bioo Scientific）

测序试剂盒（Bioo Scientific NEXTflex）

偶联了链亲和素的Dynabeads磁珠（Life Technologies）

TAE缓冲液（1×）&lt;A&gt;

TE(pH8.0)&lt;A&gt;

TruSeq 寡核苷酸（HPLC 纯化；Illumina）

下表是本方案要用到的 TruSeq 寡核苷酸:

| 序列名称 | 数量/μmol | 碱基数 | 序列 |
| --- | --- | --- | --- |
| TS-PCR Oligo 1 | 0.25 | 22 | AATGATACGGCGACCACCGAG*A |
| TS-PCR Oligo 2 | 0.25 | 22 | CAAGCAGAAGACGGCATACGA*G |
| TS-HE Oligo 1 | 0.25 | 58 | AATGATACGGCGACCACCGAGATCTACACTCTTTC CCTA CACGACGCTCTTCCGATC*T |
| TS-HE GENERIC Index | 0.25 | 57 | GATCGGAAGAGCACACGTCTGAACTCCAGTCAC/ideoxy1//ideoxy1//ideoxy1//ideoxy1//ideoxy1//ideoxy1/ATCTCGTATGCCGTCTTCTGCTT*G |

注:TS，TruSeq 酶；HE，杂交增强；\*，3'-磷硫酰修饰；TS-HE Index Oligos，我们用 TS-HE GENERIC Index Oligo 替代不同的特异性 TS-HE Index Oligos。这种通用引物可以在杂交实验过程中替代任意的 TS-HE 引物，从而降低材料成本和实验流程的复杂度；不过通用引物得到的实验结果质量可能不如用特异性 TS-HE 引物的好。

## 设备

Bioanalyzer 2100 (Agilent)

Bioanalyzer 利用微液流技术平台可以进行 DNA、RNA 和蛋白质的大小筛选、定量及质量控制。

平板和离心管用的离心机

超声用的 Covaris 管

烘箱（预先设定 $95^{\circ}\mathrm{C}$ 和 $47^{\circ}\mathrm{C}$ ）

荧光光度计（例如，Qubit、Wallac 1420 multilabel counter）

凝胶电泳槽和支架

Gene catcher 或手术刀

磁力架 (Ambion 或 DynaMag-2)

离心管

0.8mL、96孔MIDI板

96 孔 PCR 板

PCR 平板盖（Bio-Rad 公司）

移液器和吸头

超声破碎仪（Covaris 公司）

分光光度计（如 NanoDrop）

PCR 仪

平板和单个离心管用的振荡仪

水浴锅（预先设定为  $47^{\circ}$ C）

![](images/page_191_image_29.jpg)

## 方法

## 剪切用于文库制备的基因组 DNA

1. 用 DNA 12000 Bioanalyzer 芯片检测基因组 DNA 的质量。
2. 用荧光光度计测定样品浓度。