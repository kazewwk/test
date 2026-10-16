## 设置标准品、对照和样品

6. 按照下表往标准品/对照板相应孔中加入 $2\mu \mathrm{L}$ 标准品或对照，留下2个只含PicoGreen的空白孔。

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 50ng/μL标准品 | 50ng/μL标准品 | 70ng/μL对照 | 70ng/μL对照 |  |  |  |  |  |  |  |  |
| B | 25ng/μL标准品 | 25ng/μL标准品 | 30ng/μL对照 | 30ng/μL对照 |  |  |  |  |  |  |  |  |
| C | 12.5ng/μL标准品 | 12.5ng/μL标准品 | 空白 | 空白 |  |  |  |  |  |  |  |  |
| D | 6.25ng/μL标准品 | 6.25ng/μL标准品 |  |  |  |  |  |  |  |  |  |  |
| E | 3.125ng/μL标准品 | 3.125ng/μL标准品 |  |  |  |  |  |  |  |  |  |  |
| F | 1.5625ng/μL标准品 | 1.5625ng/μL标准品 |  |  |  |  |  |  |  |  |  |  |
| G | 0.78ng/μL标准品 | 0.78ng/μL标准品 |  |  |  |  |  |  |  |  |  |  |
| H | 0ng/μL空白 | 0ng/μL空白 |  |  |  |  |  |  |  |  |  |  |

7. 混匀后低速离心收集样品到管底。

8. 往样品板每孔加入  $2 \mu L$  各种 DNA 样品。

该反应在避光条件下能保持稳定 3h。

## 用 Varioskan 荧光光度计检测荧光

## 启动软件

9. 点击电脑桌面上的 SkanIt RE for Varioskan Flash 2.4.3 图标打开软件。使用用户名 admin(不需要密码)。

10. 用锡箔纸盖好平板。

11. 点击 Open Session 选择 Shake。

i. 点击 Open。

ii. 插入平板。

iii. 选择页面左下角的 Connect。

iv. 振荡平板 20s。

12. 孵育平板 15min。

13. 打开 96 well Varioskan。

14. 另存为 Sample Name。

15. 进入 Executing Session。

## 方案设置（只针对新项目）

16. 在左上角的 Session Structure 框选择 Protocol。

17. 在 Steps 框点击右键然后选择 Fluorometric。设置下述参数:

| Emission wavelength | 530 nm |
| --- | --- |
| Measurement time | 900 |
| Excitation | 485 |
| Excitation BW | 12 |
| Dynamic Range | Auto Range |

## 平板布局设置（只针对新项目）

18. 在左上角的 Session 框选择 Plate Layout。

19. 在 Plate Layout 页面的顶部将该页命名为 Standards Controls。

20. 使用右上角的 Fill Wizard，填写第一个平板的标准曲线、对照和空白。

21. 点击 96 孔板图上 A1 的位置，会出现一个红点。

22. 在 Samples/Type 下拉菜单中选择 Calibrator（标准曲线样品就是 Calibrator）。使 Fill Order 箭头向下。

23. 在 Replicates 下拉菜单中选择 2. 使 Fill Order 箭头向右。

24. 在 Conoentrations 选项中输入 50（单位=ng/ $\mu$ L）。

25. 点击 Generate Series。

26. 在 Series/Operators 下拉菜单中选择 Divide, Step by 2。点击 OK。

27. 在 Samples/Type 下拉菜单中选择 Controls, Number of controls 2, and Number of replicates 2。点击 Add/Close。

28. 在 Samples/Type 下拉菜单中选择 Blank, Number of replicates 2。点击 Add/Close。

29. 在 Plate Layout 页面顶端选择 New。将该页命名为 Samples 或者取一个项目名字。

30. 选择 Fill Wizard。

31. 在 Samples/Type 下拉菜单中选择 choose Unknown, Number of unknowns 96（样品就是 Unknown）。使 Fill Order 箭头向下。

32. 在 Dilution/Unit 下面输入 ng/ $\mu$ L。点击 Add/Close。

33. 布局设置完毕后，点击 Session 和 Save As。以日期或样品板为名保存项目。

## 结果设置（只针对新项目）

只要保存了项目，可以在运行结束后设置或改变结果。

34. 在左上角 Session 框选择 Results。

35. 左下角 Results 框里的 Fluorometric 上点击右键选择 Blank Subtraction。点击右键 Blank Subtraction 选择 Quantative Curve Fit。

36. 在 Extrapolation 里核实 Enable Extrapolation 并将最大浓度改为 500。

37. 在左下角 Results 框选择 Report。

38. 在右上角选择 Parameters 表格。

39. 按住[Ctrl]键，选择 Blank Subtraction1、Curve Fit1 和 Fluorometric1。点击 Add。

40. 从 Added 列表中选择 Curve Fitl。

i. 选择 Format。

ii. 选择 List、Plate、Well 和 Calculated。

iii. 点击 OK。

41. 在窗口下面底部，务必核实 Save to File 和 Unique Name。

42. 文件应该保存在 Z:\varioskan\appropriate year\nmonth 文件夹中，文件保存格式为.xls。

## 执行项目

项目设置并保存后，进行下述步骤。

43. 点击 Varioskan 软件左下角的 Plate Out 按钮，将第一个平板（标准曲线）放入仪器的平板台。

44. 点击 Start。

45. 平板扫描完毕后，点击 Plate Out 按钮取出平板。

46. 取出标准曲线平板，插入样品板。
47. 运行完毕后取出样品板。
48. 点击 Varioskan 软件左下角的 Run Plate 按钮使平板台归位。
49. 查看电脑 My Computer/My Documents 文件夹的.xls 格式结果文件。

![](images/page_210_image_7.jpg)

## 配方

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

## 对照 DNA: Human buffy coat

用无核酸酶的水稀释储备溶液配制  $70ng/\mu L$  和  $30ng/\mu L$  的 Human Buffy Coat。

| 样品 | 初始浓度/(ng/μL) | 样品/μL | 水/μL | 终浓度/(ng/μL) |
| --- | --- | --- | --- | --- |
| Human buffy coat 储备溶液 | 200 | 7 | 13 | 70 |
| Human buffy coat 储备溶液 | 70 | 8.6 | 11.4 | 30 |

# 方案 14 文库定量: 用 Qubit 系统对双链或单链 DNA 进行荧光定量

Qubit 是一种基于荧光的高灵敏度精确定量系统。有几种试剂盒专门针对 Qubit 荧光光度计进行了优化，不过用其他荧光光度计也能有效地发挥功能。高灵敏度双链 DNA Qubit 试剂盒的检测范围是 0.2～100ng。单链 DNA Qubit 试剂盒的检测范围是 1～200ng。

![](images/page_210_image_15.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

## 试剂

试剂盒（Life Technologies 公司的 Qubit dsDNA 或 Qubit ssDNA Assay Kit）

每个试剂盒中包含了浓缩的染料、稀释缓冲液和 DNA 标准品。

## 设备

Qubit 测试管（Life Technologies 公司）

Qubit 荧光光度计（Life Technologies 公司）

运行 Windows XP 的个人电脑

Qubit Data Logger 软件

![](images/page_211_image_2.jpg)

## 方法

## 试剂和样品配制

1. 为每个样品，以及标准品 1 和 2、对照 1 和 2 要用的测试管做好标记。

2. 配制对照 1 和 2。对照 1 是 $1 \mu \mathrm{L}$ 标准品 2（高灵敏度双链 DNA 试剂盒:$10 \mathrm{ng} / \mu \mathrm{L}$；单链 DNA 试剂盒:$20 \mathrm{ng} / \mu \mathrm{L}$）。对照 2 是 $1 \mu \mathrm{L}$ 标准品 2 的 $1: 10$ 稀释液。

3. 为每个样品混合 $1 \mu \mathrm{L}$ 浓缩的染料和 $199 \mu \mathrm{L}$ 稀释缓冲液。为每个样品、两个标准品、两个对照和两份补充测试配制足够的工作液。

4. 振荡 5s。

5. 往每个标记好的样品测试管中加入  $199 \mu L$  工作液。

6. 往每个标记好的标准品测试管中加入  $190 \mu L$  工作液。

7. 往  $190 \mu L$  工作液中加入  $10 \mu L$  标准品 1。往  $190 \mu L$  工作液中加入  $10 \mu L$  标准品 2。

8. 往 $199\mu \mathrm{L}$ 工作液中加入 $1\mu \mathrm{L}$ 对照 1（即标准品 2）。往 $199\mu \mathrm{L}$ 工作液中加入 $1\mu \mathrm{L}$ 对照 2（稀释的标准品 2）。

9. 往  $199 \mu L$  工作液中加入  $1 \mu L$  样品。

10. 每个标准品和样品振荡 5s。

握住测试管顶部而不是底部操作样品。该方法对温度敏感。

11. 室温孵育 2min。

## DNA 定量

12. 打开电脑上的 Qubit 软件（确定 Caps Lock 没有打开）。

13. 点击 Qubit Data Logger 上的 Start 打开 Qubit 仪接口。

14. 按照屏幕上的指示打开荧光光度计。

15. 选择你要进行的测试应用程序，按下 Go。

16. 选择 Run new calibration, 按下 Go。

17. 轻轻摇动标准品 1 测试管，放入 Qubit 仪并关上盖子。按下 Go，然后等待读取完毕。

18. 轻轻摇动标准品2测试管，放入Qubit仪并关上盖子。按下Go，然后等待读取完毕。

19. 在 Qubit 仪记录器里点击合适的孔，扫描样品管上的条形码。

20. 轻轻摇动样品测试管，放入 Qubit 仪并关上盖子。按下 Go，然后等待读取完毕。

握住盖子操作测试管，不要使样品在手中捂热。

21. 选择 Calculate the concentration, 按下 Go。

22. 按照提示输入所用样品的体积，按下 Go。

23. 从 Qubit 仪取出样品。

见“疑难解答”。

24. 为每个样品重复步骤 19\~23，依次保留好样品。

25. 以.csv 格式将 Qubit 记录器文件保存在桌面上。

## 清理

26. 关上 Qubit 仪盖子，关掉 Qubit 仪。按下 Home 按钮。按下箭头至 Power Off 位置，然后按下 Go。

27. 将样品液倒入二甲基亚砜废液瓶。将测试管盖上盖子后放入危险性废物容器中。

![](images/page_212_image_3.jpg)

## 疑难解答

问题（步骤 23）:样品读数超出仪器范围。

解决方案:配制 DNA 样品的 1:5 稀释液，重复步骤 8\~22。

## 方案 15 为 454 测序制备小片段文库

本方案介绍 454 测序系统的 DNA 小片段文库的制备（FLX 或者 XLR）。打断的基因组 DNA 经纯化和加接头之后固定在特定的磁珠上。小片段文库包含了一套单链的 DNA 片段，囊括了全部的目的 DNA。通过质量评价和定量后，单链的文库就可以通过 emPCR 扩增，如方案 16 中叙述。

![](images/page_212_image_9.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

接头

AMPure 磁珠（Beckman Coulter）

用于浓缩和纯化 DNA 样品。

ATP

BSA

EB 缓冲液（室温）

PBI 缓冲液（室温）

PE 缓冲液（室温）

DNA 样品（溶于 TE 缓冲液&lt;A&gt;）

dNTP 混合液

电极清洗液

酶和接头试剂盒（-20℃）

乙醇（70%）

补平聚合酶

补平聚合酶缓冲液（10×）

文库结合液（2×）

文库固定磁珠（4℃）

文库准备缓冲液（所有缓冲液保存在-20℃）（Roche）

文库洗脱液

连接酶

连接酶缓冲液（2×）

Melt Solution

用微生物学级水准备 10mol/L NaOH。见步骤 31。

MinElute PCR 纯化试剂盒

MinElute 柱储存在  $4^{\circ}$ C。柱子在使用前室温放置约 15min。

雾化缓冲液

中和液

用 PB 缓冲液加入 20% 的乙酸配制。见步骤 33。

补平缓冲液（10×）

RNA Pico Chip Kit（室温）（Agilent）

RNA 6000 Pico Chips (Agilent)

RNA 6000 Pico Cond Solution (Agilent)

RNA 6000 Dye Concentrate (Agilent)

RNA 6000 Gel Matrix (Agilent)

RNA 6000 Pico Kit (4°C) (Agilent)

RNA 6000 Pico Ladder (Agilent) (储存在-20℃)

RNA 6000 Pico Marker (Agilent)

离心柱（4℃）

T4 DNA 聚合酶

TE 缓冲液

T4 PNK

Tris-HCl (10mmol/L)

水，分子生物学级

## 设备

Aeromist Nebulizer（雾化器）

FlashGel (1.2%) 和 FlashGel Rig (Lonza)

孵育器

磁力架（MPC）

微量离心机

微量离心管（1.7mL）

微型离心机（Bench-Top）

雾化凝集管

雾化器支架

雾化试剂盒:室温（Roche）

雾化器塞

氮气罐

合适量程的移液器

带滤芯吸头

Safe-Lock Tubes

分光光度计（如 NanoDrop）

螺旋口滤器

注射器工具包

试管旋转器

歧管真空泵

通风雾化罩

涡旋振荡器

![](images/page_214_image_7.jpg)

## 方法

本方案中所说的室温都假设为  $22^{\circ}$ C。

## DNA 片段化

1. 通过 FlashGel 来鉴定 DNA 样品的质量和浓度。

2. 用移液器加 $3 \sim 5 \mu \mathrm{g}$ 的 DNA 样品（溶于 TE）至雾化器的底部。加入 TE 缓冲液使终体积为 $100 \mu \mathrm{L}$ 。然后加 $500 \mu \mathrm{L}$ 的雾化缓冲液，充分混匀。

3. 组装雾化器，将软管接在雾化器的进气口。然后将雾化器转移至通风橱。

4. 将雾化器放到雾化器支架上，将雾化器软管的末端连接到氮气罐上。

5. 用 45psi 的氮气处理 1min 打断 DNA，然后断开氮气。

6. 等压力恢复正常，断开雾化器软管。

7. 将打断的 DNA 样品 1500r/min 离心 30s，然后小心拧松雾化器的顶部，检测雾化样品的体积。

总回收量应大于  $300 \mu l$ 。

8. 加 2.5mL 的 PBI 缓冲液到含有 DNA 样品的雾化杯中，涡旋混合。

9. 用 MinElute PCR 纯化试剂盒中的两个柱子纯化雾化后的 DNA 样品（确保柱子在使用时恢复至室温）。如果样品体积较大，每个柱子可以分两次。每个柱子用一半的 DNA 样品，具体操作方法如下:

i. 把柱子插到歧管真空连接器中。

ii. 加  $750 \mu L$  样品至 MinElute 柱，打开真空泵。再加  $750 \mu L$  样品或是直至所有样品全部抽干。

iii. 在 MinElute 柱中加入  $750 \mu L$  的 PE 缓冲液洗涤 DNA。

iv. 关掉真空管，把 MinElute 柱放回废液收集管。

v. 13 000r/min 离心 MinElute 柱 1min。

vi. 旋转离心柱，13 000r/min 再离心 30s，以去除残留的 PE 缓冲液。

vii. 将 MinElute 柱转移至 1.5mL 的干净离心管中。

viii. 加  $25 \mu L$  的 EB 缓冲液（室温）至 MinElute 柱底膜中心洗脱 DNA。

ix. 将柱子室温静置 1min，13000r/min 离心 1min。

x. 重复步骤 9.i～9.viii，用第二个柱子回收另一半样品。

xi. 将两个柱子的洗脱液收集至同一管中，总体积约为  $50 \mu L$ 。

xii. 用分光光度计（如 NanoDrop）对样品进行定量。

10. 为确保样品雾化成合适片段（300～800bp），在 FlashGel 上分析  $1 \mu L$  的样品。

11. 用移液器定量洗脱体积，用 EB 缓冲液补至终体积  $50 \mu L$ 。

12. 加  $35 \mu L$  的 AMPure 磁珠，涡旋混合，室温孵育 5min。

13. 使用磁力架（MPC）将磁珠完全吸附在离心管壁一侧。

14. 弃掉上清，用  $500 \mu L$  70% 的乙醇洗涤磁珠两次（每次静置 30s）。

15. 弃掉所有乙醇，并将 AMPure 磁珠完全晾干（可以使用  $37^{\circ}$ C 的金属浴）。

16. 从 MPC 上移下管子，加  $24 \mu L$  的 EB 缓冲液（pH8.0），涡旋重悬磁珠。

这一步是将雾化的 DNA 从 AMPure 磁珠洗脱下来。

17. 使用 MPC 再次将磁珠吸附至管壁，然后将含有纯化 DNA 的上清转移至一个新离心管中。

18. 取  $1 \mu L$  混匀的雾化样品，用 FlashGel 鉴定样品质量。

样品 DNA 的平均大小应在 400～800bp 之间。

## 片段末端补平和加接头

19. 在一个 $0.2 \mathrm{~mL}$ 的离心管中，依次加入以下试剂（来自于酶和接头试剂盒）:

| DNA 片段(步骤 15) | 约 $23\mu L$ |
| --- | --- |
| 补平缓冲液($10\times$) | $5\mu L$ |
| BSA | $5\mu L$ |
| ATP | $5\mu L$ |
| dNTP | $2\mu L$ |
| T4 PNK | $5\mu L$ |
| T4 DNA 聚合酶 | $5\mu L$ |
| 总体积 | $50\mu L$ |

充分混合后  $12^{\circ}$ C 孵育 15min；立刻转移至  $25^{\circ}$ C 继续孵育 15min。

20. 用 MinElute PCR 纯化试剂盒的一个纯化柱来纯化已补平的片段（确保柱子在使用前恢复到室温）。

i. 把柱子插到歧管真空连接器中。
ii. 加 5 倍样品体积的 PBI 缓冲液:先加  $100 \mu L$  的 PBI 缓冲液至样品管，吹打混匀，全部转移至 MinElute 柱中，抽真空。
iii. 再加  $150 \mu L$  PBI 缓冲液至样品管，吹打混匀，转移至 MinElute 柱中。
iv. 在 MinElute 柱中加入  $750 \mu L$  的 PE 缓冲液来漂洗样品 DNA。
v. 关掉真空泵，将 MinElute 柱转移回 2mL 的收集管中。
vi. 13 000r/min 离心 MinElute 柱/管 1min。
vii. 旋转 MinElute 柱/管，13 000r/min 再离心 30s，以去除残留的 PE 缓冲液。将 MinElute 转移至一个干净的 1.5mL 的离心管中。
viii. 在 MinElute 柱底膜中心加  $16 \mu L$  的 EB 缓冲液，洗脱样品 DNA。
ix. 将柱子静置 1min，13 000r/min 离心 1min。

x. 使用分光光度计（如 NanoDrop）定量样品（1μL）。

21. 在一个 0.2mL 离心管中，依次加入以下试剂（来自于酶和接头试剂盒）:

▲试剂的添加顺序非常重要！

| Polished DNA | 约15μL |
| --- | --- |
| 连接酶缓冲液(2×) | 20μL |
| 接头 | 1μL |
| 连接酶 | 4μL |
| 总体积 | 40μL |

混合均匀，瞬时离心，25℃连接15min。

22. 利用这段时间来准备固定用的磁珠。

i. 加 50μL 的文库固定化磁珠至 1.5mL 的新离心管中。

ii. 将离心管放在 MPC 上，待磁珠聚集后弃掉缓冲液。

iii. 在 MPC 上使用  $100 \mu L$  的  $2 \times$  文库结合液洗涤磁珠两次。

iv. 加  $25 \mu L$  的  $2 \times$  文库结合液至磁珠中，冰上放置，以备步骤 24（文库固定）使用。

23. 使用 MinElute PCR 纯化试剂盒的柱子来纯化连接产物（确保柱子在使用时恢复至室温）。

i. 把柱子插到歧管真空连接器中。

ii. 加 5 倍样品体积的 PBI 缓冲液:先加  $100 \mu L$  的 PBI 缓冲液至样品管（步骤 21），吹打混匀，全部转移至 MinElute 柱中，抽真空。

iii. 再加  $100 \mu L$  PBI 缓冲液至样品管，吹打混匀，转移至 MinElute 柱中。

iv. 在 MinElute 柱中加入  $750 \mu L$  的 PE 缓冲液来洗涤样品 DNA。

v. 关掉真空泵，将 MinElute 柱转移回 2mL 的收集管中。

vi. 13 000r/min 离心 MinElute 柱 1min。

vii. 旋转 MinElute 柱/管，13 000r/min 再离心 30s，以去除残留的 PE 缓冲液。将 MinElute 转移至一个干净的 1.5mL 的离心管中。

viii. 在 MinElute 膜的中心加  $16 \mu L$  的 EB 缓冲液，洗脱样品 DNA。

ix. 将柱子静置 1min，13000r/min 离心 1min。

x. 使用分光光度计（如 NanoDrop）定量样品（1μL）。

## 文库的固定和补平反应

24. 将洗脱的样品 DNA 加至已洗涤的文库固定磁珠中。

25. 充分混合后放置在试管旋转器上室温旋转 20min。

26. 将含有 DNA 样品和磁珠的离心管放置于 MPC 上，用 $100\mu \mathrm{L}$ 的文库洗脱液漂洗文库两次。

27. 使用一个 $1.5 \mathrm{~mL}$ 的离心管, 依次加入如下试剂 (来自于酶和接头试剂盒), 混合均匀。

▲试剂的添加顺序非常重要！

| 水,分子生物学级 | 40μL |
| --- | --- |
| Fill-in polymerase buffer (10×) | 5μL |
| dNTP | 2μL |
| Fill-in polymerase | 3μL |
| 总体积 | 50μL |

28. 将步骤 26 离心管放置在 MPC 上，从中吸去  $100 \mu L$  文库洗脱液。

29. 在步骤 28 离心管中加入步骤 27 准备的  $50 \mu L$  补平反应混合液，混合均匀，不要产生气泡， $37^{\circ} C$  孵育 20min。

30. 放置于 MPC 上，用  $100 \mu L$  的文库洗脱液洗涤结合的文库两次。

## 单链 DNA 样品（sstDNA）文库的分离

31. 在 $1.5 \mathrm{~mL}$ 的离心管中, 加入 $500 \mu \mathrm{L}$ 的 PBI 缓冲液和 $3.8 \mu \mathrm{L}$ 的 $20 \%$ 的乙酸, 混匀, 制备成中和液。

32. 将步骤 30 离心管放置于 MPC 上，弃掉  $100 \mu L$  文库洗脱液。

33. 在 9.875mL 水中加入 0.125mL 10mol/L NaOH，配制  $1 \times$  Melt Solution。

Melt Solution 只能保持 7 天，使用时先确定它配制了几天，必要时重新配制。

34. 在带有洗涤文库的磁珠中加入  $50 \mu L$  Melt Solution（步骤 30）。

35. 涡旋，放在磁力架上，使磁珠脱离  $50 \mu L$  上清液形成小球状。

36. 小心吸出上清，把它转移到新鲜配制的中和液中。

37. 重复步骤 $34 \sim 36$，共获得 $100 \mu \mathrm{L}$ 冲洗磁珠 Melt Solution（把所有上清液加到同一管中和液中）。

38. 用 MinElute PCR Purification Kit 中的柱子纯化中和过的单链模板 DNA(sstDNA)（确保柱子在使用时已平衡至室温）。

i. 把柱子插到歧管真空连接器中。
ii. 用移液器吸取样品到柱子中，抽真空以使 DNA 结合。
iii. 加入  $750 \mu L$  PE 缓冲液冲洗 DNA。
iv. 关掉真空泵，把柱子放回到 2mL 收集管中。

v. 13 000r/min 离心 1min。

vi. 13 000r/min 再次离心 30s，移掉所有剩余的 PE 缓冲液。

vii. 把柱子转移到一个干净的 1.5mL 管中，在柱子膜中央加入 15μL TE 来洗脱 DNA。

viii. 放置 1min，13 000r/min 离心 1min。

## 单链模板 DNA 文库的质量评估及定量

使用时，把 Agilent kits 平衡至室温 30min，凝胶必须平衡至室温。注意 RNA marker 只能放在冰上。

39. 取  $1 \mu L$  文库在 RNA Pico 6000 LabChip 上运行。

40. 用分光光度计（NanoDrop 或者 Qubit）定量文库（1μL 重复 3 次），并测定文库质量。

平均片段长度应该在 400～800bp，300nt 以下的应小于 10%；总 DNA 量大于 10ng，并且没有可见的二聚体峰。

41. 根据 Pico 6000 LabChip 测定信息，用计算工具（454 Molecular Calculator）按照下面公式计算每微升分子数。

$$
\frac {\mathrm{分子数}}{\mu \mathrm{L}} = \frac {(\mathrm{样品浓度} [ \mathrm{ng/} \mu \mathrm{L} ]) \times (6 . 0 2 2 \times 1 0 ^ {2 3})}{(3 2 8 . 3 \times 1 0 ^ {9}) \times (\mathrm{平均片段长度} [ \mathrm{nt} ])}
$$

吸取  $1 \mu L$  文库，加 TE 稀释到  $1 \times 10^{8}$  个/ $\mu L$ 。

原始库于-25～-15℃保存（如果不立即使用，稀释到 $1\times10^{8}$ 倍后储存）。

42. 必要的话，用浓度为 $1 \times 10^{8}$ 的单链模板 DNA 文库进一步制备稀释液，涡旋混匀所有的稀释液。

i. 取  $1 \mu L \times 10^{8}$  储存液到  $9 \mu L$  TE 缓冲液中制备  $1 \times 10^{7}$  稀释液。
ii. 取  $1 \mu L \times 10^{7}$  储存液到  $9 \mu L$  TE 缓冲液中制备  $1 \times 10^{6}$  稀释液。
iii. 取  $1 \mu L \times 10^{6}$  储存液到  $9 \mu L$  TE 缓冲液中制备  $1 \times 10^{5}$  稀释液。

这些稀释液将会用于 emPCR 中的磁珠与 DNA 的滴度测定（方案 16）。

43. 设置 4 个单管 emPCR，加入下述体积的不同浓度的 DNA 模板库，得到每个磁珠结合的单链模板 DNA 分子数理论值如下:

- Tube 1: $1.5\mu \mathrm{L}2\times 10^{5} / \mu \mathrm{L}$ 单链模板文库（=每个磁珠结合0.5个分子数）
- Tube 2: $6.0 \mu \mathrm{L} 2 \times 10^{5} / \mu \mathrm{L}$ 单链模板文库（=每个磁珠结合 2 个分子数）
- Tube 3: $1.2\mu \mathrm{L}2 \times 10^{6} / \mu \mathrm{L}$ 单链模板文库（=每个磁珠结合4个分子数）
- Tube 4: $4.8\mu \mathrm{L}2\times 10^{6} / \mu \mathrm{L}$ 单链模板文库（=每个磁珠结合16个分子数）

44. 上述 4 管涡旋混匀 5s。

45. 按照方案 16 进行 emPCR。

# 方案 16 单链 DNA 文库的捕获及 emPCR

这个方案描述如何扩增方案 15 中制备的单链模板 DNA 文库中的 DNA 片段。文库片段首先复性，然后捕获磁珠、乳化、PCR 扩增。收集带有扩增的单链模板的磁珠，加入测序引物混匀复性。这样得到的固化 DNA 文库即可用于 454 FLX 或 XLR Titanium 测序。

![](images/page_218_image_4.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

## 试剂

扩增混合物（5×）

复性缓冲液 TW（1×）

磁珠回收试剂盒

漂白剂(10%)

捕获磁珠洗涤液（10×）

去核酸试剂

DNA 捕获磁珠

emPCR Kit (XLR Titanium) (-20°C)

乳化油

强化液 TW (1×)

富集引物

酶混合物

异丙醇（190 proof）

Melt solution (步骤 42)

Mock 扩增混合物

NaOH (10mol/L)

PPIase（肽基脯氨酰基顺反异构酶）

测序引物

已滴定 sstDNA 文库（方案 15 制备的）

水，分子生物级（MBG）（Sigma-Aldrich）

## 设备

微量离心机

移液管吸头（10.0mL）

SABA unit 的圆锥管帽（50mL）

圆锥管（50mL）

库尔特（Coulter）计数器

Custom Blue adaptor

一次性手套

富集磁珠

Eppendorf 重复加样器

锥形瓶架

合适量程的带滤芯吸头

一次性实验服

加热器（预设到  $65^{\circ}$ C）

滚轴混匀仪（Labquake tube roller）

磁性颗粒收集器（MPC）

微型离心机

微型离心管（1.7mL）

合适量程的移液器

带边缘的平板（96孔）

半自动破碎装置（SABA）（用于打破油包水）

酒精棉球

热循环仪

组织研磨仪

组织研磨管管架

8 道移液器

SABA 管

真空管接口

吸液垫（或吸水纸）

涡旋仪

废液缸

![](images/page_219_image_24.jpg)

## 方法

▲整个实验过程中需戴手套及穿一次性实验服。

## 洗涤捕获磁珠

1. 把下列试剂混合，制备捕获磁珠洗涤液:

| 水(MBG) | 9mL |
| --- | --- |
| 捕获珠清洗缓冲液 | 1mL |

2. 按如下步骤在微量离心机上富集磁珠使其呈小球状。

i. 离心磁珠 10s。

ii. 旋转管子  $180^{\circ}$ ，再次离心 10s。

iii. 小心弃掉上清液，不要碰到磁珠。

3. 吸取 $1000 \mu \mathrm{L} 1 \times$ 捕获珠清洗缓冲液到磁珠中, 涡旋 $5 \mathrm{~s}$, 重悬磁珠。

4. 按步骤 2 在微量离心机上富集磁珠成小球状。

5. 重复步骤 3 和步骤 4，第二次洗涤后不要重悬磁珠。

## 结合单链模板 DNA 文库片段

6. 获得足够数量的单链模板 DNA 文库来扩增。

每管包括 3500 万个磁珠(每个试剂盒有 2 管)

按下列公式计算加入文库的量:

每个珠子的拷贝数/文库分子质量=加入磁珠中文库的微计数

7. 在每管捕获珠中加入在方案 15、步骤 43 中所得到的 sstDNA。

8. 涡旋 5s 混匀各组分，使用前一直放置于冰上。

## 第一次振荡乳化油

9. 打开组织研磨仪的防护罩，移去管架装置。

10. 把装有乳化油的样品杯放在组织研磨仪上。

11. 把样品杯用螺丝拧紧在合适的位置(不要拧得过紧从而使杯子破裂)，放下防护罩。

12. 设置组织研磨仪的参数为 28 cycles/s，2min，按下开始按钮开始振荡。

## 制备 Titanium XLR Live 扩增混合物

13. 将冷冻的试剂盒中试剂取出放在冰上使其完全解冻，酶放在 $-20^{\circ} \mathrm{C}$，解冻后，涡旋试剂（除了酶）5s。

14. 制备 Titanium XLR Live 扩增混合物（如下表），最多可做 4 个 LVE（1kit=2LVE），使用前一直放在冰上。注意:如果有多个文库扩增，每个文库必须制备一管 Live 扩增混合物。

| 试剂 | 1LVEs 体积 | 2 LVEs 体积 | 4 LVEs 体积 |
| --- | --- | --- | --- |
| 水(MBG) | 2700 | 5400 | 10800 |
| 扩增混合液(5×) | 780 | 1560 | 3120 |
| 扩增引物 | 230 | 460 | 920 |
| 酶 | 200 | 400 | 800 |
| PPIase | 5 | 10 | 20 |

## 准备乳化杯

15. 在 $15 \mathrm{~mL}$ 圆锥管中, 加入 $1 \mathrm{~mL} 5 \times \text {Mock}$ 扩增混合物到 $4 \mathrm{~mL}$ 水中, 把 $5 \times \text {Mock}$ 扩增混合物稀释成 $1 \times$ (用到的每一个试剂盒)。

16. 把装有乳化油的样品杯从组织研磨仪上取下。

17. 加入 5mL Mock 扩增混合物到样品杯中。

18. 把样品杯放在组织研磨仪上，用螺丝拧紧在合适的位置，放下防护罩，设置组织研磨仪参数为 28 cycles/s，5min，按下开始按钮开始振荡。

## 加 Live 扩增混合物到磁珠及乳化油中

19. 加 1mL Live 扩增混合物到 Library/DNA capture bead 管中，用移液器上下吹打混匀，吸头在下一步骤中继续使用。

20. 把 Library/DNA capture bead/Live 扩增混合物加到一个新的 15mL 圆锥管中，吸头在下一步骤中继续使用。

21. 加 1mL Live 扩增混合物到原始 Library/Capture bead 管中，快速涡旋，短暂离心，把剩余磁珠混匀，加到步骤 20 的 Library/Capture bead/Live 扩增混合物中。

22. 在步骤 20 中得到的 15mL 圆锥管中加入另外 1.75mL（共 3.75mL）Live 扩增混合物。

23. 把含有乳化油和 Mock 扩增混合物的振荡过的样品杯从组织研磨仪上取下。

24. 快速涡旋文库/捕获磁珠/Live 扩增混合物，将其倒入含有乳化油和 Mock/Live 扩增混合物的样品杯。

25. 将样品杯放回到组织研磨仪上用螺丝拧紧在合适的位置，放下防护罩，设置组织研磨仪参数为 12 cycles/s，5min，按下开始按钮开始振荡。

## 制备用于扩增的乳化剂（控制室）

26. 将吸液垫放置在 emulsion hood 上。
27. 乳化后，把样品杯从组织研磨仪上取下，打开乳液杯。
28. 用 Eppendorf 重复加样器取出并分装  $200 \mu L$  到 96 孔 PCR 板（约 90 孔）。
29. 用板盖（盖垫或封板条）盖好平板，除去 hood。

30. 扔掉在 emulsion hood 及工作台中用过的吸液纸（将用过的吸液纸丢弃于垃圾篓），然后用以下物品清洗 emulsion hood 和工作台:

- $10\%$ 漂白液
- DNA Away
- 棉签（酒精擦拭巾）

将用过的纸巾丢入垃圾篓。

31. 打开 emulsion hood 内部的紫外灯，照射 30min。照射完毕后确保 emulsion hood 上的开关都已关闭。

## 扩增反应和珠子回收（扩增子室）

32. 将乳化扩增反应液放在热循环仪上。

33. 检查以确保热盖温度与加热板温度相差不超过  $5^{\circ}$ C。

34. 设置并开始 Titanium EMBPC 热循环程序。

35. 热循环完成后，把所有扩增反应的平板从热循环仪上取出。

戴上手套，穿上一次性实验服做此步骤。

36. 用以下物品清洗工作台和 breaking hood:

- $10\%$ 漂白液
- DNA Away
- 棉签（酒精擦拭巾）

将用过的纸巾丢入垃圾篓。

37. 在 breaking hood 和工作台上放置一排吸水纸。
38. 打开 breaking hood 中的紫外灯开关。照射 30min。
39. 记录 breaking hood 的使用量，并确保照射结束后罩子上的所有设置已关闭。
40. 在 $4 \times$ 强化缓冲液 TW 中加入 $187.5 \mathrm{~mL}$ 水，制备 $1 \times$ 强化缓冲液 TW。
41. 在  $10 \times$  复性缓冲液 TW 中加入 72mL 水制备  $1 \times$  复性缓冲液 TW。
42. 在 $40 \mathrm{~mL}$ 水中加入 $500 \mu \mathrm{L} 10 \mathrm{~mol} / \mathrm{L} \mathrm{NaOH}$ 制备 $1 \times$ Melt solution, 一周后重新制备。
43. 根据以下说明书设置半自动破碎装置（SABA）（图 11-17）。

![](images/page_221_image_35.jpg)

<details>
<summary>text_image</summary>

8道移液器调节器
圆锥管(50mL)
橡胶塞
真空管
8道移液器
锥形瓶捕获
</details>

图 11-17 SABA 装置。

i. 打开真空泵。

ii. 把 8 道移液器慢慢放入乳化液中，逐排吸取每个孔中的乳化液，当所有孔都被吸过后，倒置 8 道移液器，以促进圆锥管吸入乳液。

iii. 用  $150 \mu L$  的异丙醇再次填充各孔。上下吹打以确保乳化液和异丙醇充分混匀。

iv. 用 8 道移液器再次吸取异丙醇/乳化液，倒置 8 道移液器便于充分吸取。

v. 用 $150 \mu \mathrm{L}$ 的异丙醇再次填充各孔。上下吹打以确保乳化液和异丙醇充分混匀。

vi. 用 8 道移液器再次吸取异丙醇/乳化液，倒置 8 道移液器便于充分吸取。

vii. 一旦所有的乳化液都被吸完，慢慢吸取多通道容器中的 5mL 异丙醇到 8 道移液器中。

viii. 关闭真空泵。

44. 拿掉 50mL 圆锥瓶上的盖子，换成 50mL 圆锥瓶的原始盖子。

45. 颠倒管子数次使磁珠充分悬浮。

46. 反复倾倒两个管子直到乳化油混合液均匀分配在两管中。

47. 在管中加入异丙醇，使终体积为  $40 \, mL$ 。

48. 离心前，涡旋振荡磁珠使其悬浮。

## 离心法破乳及清洗磁珠

49. 离心含有乳化液/异丙醇混合液的 $50\mathrm{mL}$ 锥形管，$2000\mathrm{r / min}$ 离心 $5\mathrm{min}$（Allegra 6型离心机 $930\mathrm{g}$）。

50. 不要碰到沉淀，倒掉上清液，加入 35mL 异丙醇，涡旋振荡，直到沉淀完全重新悬浮。

51. 离心含有乳化液/异丙醇混合液的 50mL 圆锥管，2000r/min 离心 5min（Allegra 6型离心机的 930g）。

52. 重复步骤 50 和步骤 51。

53. 不要碰到沉淀，倒掉上清。

54. 加入 35mL 1×强化缓冲液 TW。涡旋振荡直至沉淀完全重悬。

55. 离心含有乳化液/异丙醇混合液的 50mL 圆锥管，2000r/min 离心 5min（Allegra 6型离心机的 930g）。

56. 倒掉上清液，不要碰到沉淀，留下磁珠上方 2mL 液体或者用 50mL 移液器吸弃 33mL 上清液。

57. 用 P1000 移液器转移磁珠至 1.7mL 离心管（需要两个 1.7mL 管）。

58. 用 $600 \mu \mathrm{L}$ 强化缓冲液冲洗 $50 \mathrm{~mL}$ 锥形管，并且与其余磁珠合并于一个管中。如果仍留有一些磁珠，需要重复这个步骤。此时 $1.7 \mathrm{~mL}$ 管中的磁珠需离心沉淀以减少体积。

59. 所有的磁珠被转移后，离心磁珠 10s。旋转管 180°，并再次离心 10s。

60. 弃掉上清液。加入 1mL 1×强化缓冲液 TW，涡旋。

61. 离心磁珠 10s。旋转管  $180^{\circ}$ ，并再次离心 10s。

62. 弃掉上清液。加入  $1 \, mL \times$  强化缓冲液 TW，涡旋。

63. 离心磁珠 10s。旋转管 180°，并再次离心 10s。

64. 弃掉上清液。加入 1mL 1×强化缓冲液 TW，涡旋。

## 间接富集

65. 离心磁珠 10s。旋转管 180°，并再次离心 10s。

66. 在每一个 $1.7 \mathrm{~mL}$ 管中加入 $1 \mathrm{~mL} 1 \times$ 溶解液, 涡旋。

▲不要让磁珠在溶解液中的时间超过10min。

67. 离心沉淀这些磁珠 10s。旋转管  $180^{\circ}$ ，并再次离心 10s。

68. 弃掉上清液。再加入  $1 \, mL \times$  溶解液，涡旋。

69. 弃掉上清液。加入  $1 \, mL \times$  复性缓冲液 TW，涡旋。

70. 离心磁珠 10s。旋转管 $180^{\circ}$，并再次离心 10s。

71. 重复步骤 69 和步骤 70，用  $1 \times$  复性缓冲液 TW 共洗涤 3 次。

72. 弃掉最后一次洗涤液后，加入 $45\mu \mathrm{L}1\times$ 复性缓冲液TW和 $25\mu \mathrm{L}$ 富集引物于每个试管中。涡旋至完全混合。

73. 把试管放在 $65^{\circ} \mathrm{C}$ 加热 $5 \mathrm{~min}$, 然后冰浴 $2 \mathrm{~min}$ 。

74. 加入  $800 \mu L$   $1 \times$  富集缓冲液 TW，涡旋。

75. 离心磁珠 10s。旋转管  $180^{\circ}$ ，并再次离心 10s。

76. 弃掉上清液，用  $1.0 \, mL \times$  强化缓冲液 TW 洗涤两次。

77. 弃掉最后一次洗涤上清液后，加入  $800 \mu L$   $1 \times$  强化缓冲液 TW。

## 富集

78. 准备富集磁珠。

i. 涡旋振荡富集磁珠 1min，使其完全重悬。

ii. 使用磁力架（MPC）使富集磁珠形成小球状。

iii. 弃掉上清液，小心不要弃掉任何富集磁珠。

iv. 从 MPC 中取出试管，在每个试管中加入 1mL 1× 强化缓冲液 TW。

v. 涡旋 3s 重悬磁珠。

vi. 使用 MPC，使富集磁珠形成小球状。

vii. 弃掉上清液，小心不要弃掉任何富集磁珠。

viii. 重复步骤 78.iv\~78.vii。

ix. 加入  $160 \mu L$   $1 \times$  强化缓冲液 TW。

79. 富集带有 DNA 的磁珠。

i. 加  $80 \mu L$  洗涤过的磁珠至各个含扩增 DNA 磁珠的 1.7 mL 管中，涡旋（按照 XLR 方案涡旋）。

ii. 在室温（15～25℃）条件下，用滚轴混匀仪旋转 5min。

iii. 把管放在 MPC 上，静置 2min，使富集磁珠形成小球状。

此时上清液呈白色。

iv. 小心移弃上清液，不要弃掉任何富集磁珠。

v. 从 MPC 上移下管子，轻轻地加入  $1 \, mL \times$  强化缓冲液，涡旋。

vi. 把管子放在 MPC 上，静置 2min，使磁珠形成小球状。

此时上清液呈白色。

vii. 弃掉上清液。

viii. 重复步骤 79.v～79.vii 直到在上清液中观察不到磁珠。这一步可能需要 6 次或 6 次以上洗涤。为了确定上清中是否仍存在磁珠，你可以将上清液收集至一个新的 1.7mL 的离心管中，短暂离心。

80. 收集富集的 DNA 磁珠。

i. 从 MPC 上取下离心管，用  $700 \mu L$  溶解液重悬磁珠。磁珠在溶解液中的时间应不超过 10min。

ii. 涡旋 5s，将离心管放回 MPC 上使磁珠成小球状。