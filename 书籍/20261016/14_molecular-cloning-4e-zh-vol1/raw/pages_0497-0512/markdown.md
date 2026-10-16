![](images/page_496_image_2.jpg)

## 讨论

许多关于小 RNA 深度测序数据的研究提取完美定位至基因组（有时考虑到测序错误，会允许一些错配的存在）的读段，并丢弃未定位的读段。然而，由于 SNP、转座子、重复片段和结构变体在大多数生物中都非常常见，我们很可能见到许多读段无法与参考基因组形成比对，这些现象实际上会成为有趣的生物学结果。例如，缺少 hen1 的果蝇，表现为内源 siRNA 和 piRNA 的广泛被截尾（trimming）和加尾（tailing）现象，这里 hen1 是一种给内源 siRNA 和 Piwi 互作 RNA（piRNA）的 3'端添加 2'-O-甲基基团的甲基化转移酶。这些被截尾和加尾的序列不可能通过标准短读段定位算法定位至参考基因组。为此，已设计了一种基于后缀树的算法来发现这些读段和它们未被修饰的基因位点（Ameres et al. 2010, 2011）。

## 其他快速短读段定位法

用于短读段与一个参考基因组进行比对的最快算法包括 Bowtie、BWA 和 SOAP2。它们都采用了相似的 BW 变换来压缩储存一个基因组的后缀/前缀 trie。这些算法之间的区别在于它们对待错配、空位和双端测序读段的策略不同。关于这些工具的比较可参见 Li 和 Durbin（2009）的文章及 Li 和 Homer（2010）的文章。模拟结果显示 SOAP2 是最快的，BWA 是最准确的。请注意 SOAP2 需要的内存空间大约是 BWA 和 Bowtie 的两倍。通常，速度以准确度为代价，这些对准方法都是非常具有竞争力的。

## 网络资源

BEDTools http://code.google.com/p/bedtools/

Bowtie http://bowtie.cbcb.umd.edu/

Cygwin http://www.cygwin.com/

Gene Expression Omnibus (GEO; an NCBI database for microarray and sequencing data sets) http://www.ncbi.nlm.nih.gov/geo/

SAMtools http://bowtie-bio.sourceforge.net/index.shtml

twoBitToFa http://hgdownload.cse.ucsc.edu/admin/exe/

UCSC bedGraph format http://genome.ucsc.edu/goldenPath/help/bedgraph.html

UCSC Genome Browser http://genome.ucsc.edu

## - 寻峰算法简介

微阵列和下一代测序技术极大地促进了通过多种生化方法富集的基因组 DNA 的发现。染色质免疫共沉淀技术（ChIP）就是一种常用方法，可富集被某一抗体特异识别的染色质片段（此方法的具体信息见第 20 章）。ChIP 通常分为三个步骤。

1. 由活细胞中将染色质纯化出来，其中基因组 DNA 与结合蛋白交联。
2. 通过机械方法（如超声法）或酶解（如使用微球菌核酸酶进行消化）将染色质分解

成片段。

3. 使用能够特异性识别转录因子、组蛋白或甲基化 DNA 的抗体将与蛋白质结合的基因组 DNA 片段拉下来。

得到的 DNA 片段可以通过微列阵（ChIP 芯片；Buck and Lieb2004）或测序（ChIP-seq; Robertson et al. 2007）进行测定（见第 20 章，方案 5 和方案 6）。在全基因组研究中，ChIP-seq 的准确度和通量都超过了 ChIP 芯片，因此，本方案的重点在于 ChIP-seq 数据分析。

由于仅基因组的一小部分与特定转录因子结合或具有表观遗传学标记（组蛋白修饰或DNA甲基化），ChIP-seq数据集中的大部分序列读段为背景。以下例子说明了这个现象。三甲基组氨酸H3赖氨酸4（H3K4me3）是一个基因转录起始位点（transcription start site，TSS）附近富集的标记。如果我们假设人类基因组中有30000个被H3K4me3标记的TSS，且H3K4me3区域的平均大小为1000个碱基对（1kb），预计在无抗体富集的情况下，仅能得到 $1\%$ 的H3K4me3区域的读段，计算过程如下:$30000 \times 1000 / 30000000000 = 1\%$ 。如果抗体存在情况下平均富集程度为10倍的话，该数值可被提高至 $9.2\%$ ，计算过程如下:$30000 \times 1000 \times 10 / [30000 \times 1000 \times 10 + (3000000000 - 30000 \times 1000) \times 1] = 9.2\%$ 。如果因抗体富集倍数为100倍的话，该数值能被提高至 $50\%$ 。由于基因组中转录因子的结合位点比组蛋白修饰位点更少，故对转录因子来说，来自背景的读段所占比例会变得更高，背景读段在基因组上随机分布，但是由于DNA剪接、切割位点和/或测序错误的存在，背景读段的分布并不是绝对均匀的，且随组织类型和ChIP方案的不同而有所变化。因此，理想情况下，背景DNA应在无抗体的ChIP-seq实验中进行测量，来自这样实验得到的数据被称为输入（input）。分析ChIP-seq数据的第一步是识别一个ChIP样本中与对照样本相比被富集的区域，这些区域被称为峰。为此，已经设计了很多软件工具（综述和对比请见Pepke et al. 2009; Wilbanks and Facciotti 2010）。这些算法被称为寻峰算法，它们在检测点状峰（punctate peak, $< 10\mathrm{kb}$ ）时非常有效。在下一节中，我们会从概念上解释这样的算法是如何运行的。

## 寻峰算法

ChIP-seq 实验中的 DNA 片段的平均大小很小，通常为数百碱基对。出于经济考虑，大多数 ChIP-seq 实验使用单端测序（single-end sequencing），读段长度仅够在基因组中的大多数位置产生单一的定位位点。方案 5 描述了定位短读段的算法。Illumina 和 ABI 测序仪默认都产生 36bp 的读段，该长度足够使读段定位至大多数真核基因组非重复区域的单一位点。由某个特定基因座产生的 DNA 片段会产生两堆短读段:一种来自正链，另一种来自负链，与 DNA 片段的两端相对应。寻峰算法是沿 3' 方向移动每个读段开始，止于平均片段长度一半的地方（图 8-27）。

寻峰算法的主要任务是探测在 ChIP 样本中存在的读段数（reads）显著高于输入（未结合抗体；图 8-27）的基因组区域。例如，如果某个区域中有 $N_{\mathrm{ChIP}}$ 个读段和 $N_{\mathrm{input}}$ 个读段（ChIP 数据和输入数据的总测序深度已被标准化至一致，且等于两者中较低的一方），ChIP 相对于输入的富集程度的显著性如何？显著性可以通过 $p$ 值来衡量，$p$ 值被定义为不被抗体（即输入数据中对应的抗体）识别的某一区域被错误地预测为峰的概率。我将 $N_{\mathrm{input}}$ 的分布称为零分布（null distribution），从该分布我们可以计算得到与一个 $N_{\mathrm{ChIP}}$ 对应的 $p$ 值。方案 4 讲述了在检测差异表达基因时如何计算 $p$ 值，计算在 ChIP 实验中被富集区域相对于输入的 $p$ 值过程与此完全相同。$N_{\mathrm{input}}$ 分布可以通过分析得到（分析零假设）或通过电脑模拟得到（经验零假设）。一种广泛应用的寻峰算法——MACS（model-based analysis of ChIP-seq，基于模型的 ChIP-seq 分析）（Zhang et al. 2008），首先使用长为 DNA 片段平均长度两倍的滑动窗口（sliding window）扫描基因组。MACS 假设 $N_{\mathrm{input}}$ 遵循泊松分布（Poisson distribution）

（一种分析零假设），该分布被用于计算 $N_{\mathrm{ChIP}}$ 的 $p$ 值。然后MACS将相互重叠的显著性窗口进行合并。

![](images/page_498_image_3.jpg)

图 8-27 寻峰算法的步骤。（步骤 1）将所有读段在 3' 方向平均片段长度一半的位置进行移位。定位至基因组正链的读段被显示为红色，定位至基因组负链的读段被显示为紫色。（步骤 2）在每个滑动窗口中，计算 ChIP 得到的读段总数（蓝色）和 input 中的读段总数（灰色）。（步骤 3）执行统计学检验来检测每个滑动窗口中的 ChIP 读段是否多于 input 读段，并基于零分布来计算统计学显著性（p 值）（彩图请扫封底二维码）。

与寻找过表达基因（方案4）相似，寻峰算法也面临着多重检验问题。因为大量的基因组区域被评估，其统计具有显著性。我们可以使用方案4中描述的相同方法，根据以下三个步骤来执行错误发现率校正（Benjamin and Hochberg 1995）。

1. 所有区域根据其 p 值从小到大进行排列。
2. 计算各个区域的 $q$ 值, $q$ 值是指一个区域被检测认为具有显著性的最小 FDR。排序在最后的区域 $q$ 值等于其 $p$ 值。根据排序列表, 第 $k$ 位区域的 $q$ 值为 $M \times p_k / k$ 与 $q_{k+1}$ 这两者中的较小值, 其中, $k$ 是排列的位置, $p_k$ 是第 $k$ 位的 $p$ 值, $M$ 是区域总数量。
3. 仅保留其 $q$ 值小于事先确定的 FDR 临界值的区域（如 $\mathrm{FDR} = 0.01$，或者被预测的区域中 $1\%$ 为假阳性）。或者，我们也可以根据一个经验零假设来进行 FDR 校正。

在 MACS 的例子中，峰检测是在以 ChIP 数据集为背景下在输入（input）数据集上进行的（input vs. ChIP）。某个特定 p 值所对应的 q 值是在相同参数条件下，由 input vs. ChIP 获得的峰数除以由 ChIP vs. input 获得的峰数。

## 检测尖锐峰的顶点

在孤立抗体附着且强烈富集情况下，例如，含有一个强序列基序的孤立转录因子结合位点，可能会产生尖锐的峰。这些峰的顶点或许对应转录因子结合位点。因此，寻峰算法通常会输出每个峰的顶点，即峰中具有大多数读段的位置（图8-27）。

## 检测在多个生物样本中被富集的区域

ChIP-seq 可以在多个样本中进行，例如，在最近一项研究中（Cheung et al. 2010），利用 ChIP-seq 方法来检测 9 位不同年纪的正常人前额皮质神经元（prefrontal cortex neuron）中的 H3K4me3。这项研究的目标之一就是在比较样本中 3 个婴儿（小于 1 岁）与 3 个最老个体（大于 65 岁）的基础上，找出各自的 H3K4me3 富集区域。寻峰算法 MACS 以 3 位年长者的联合脑数据集为对照，在被合并的 3 个婴儿数据集中运行；反之亦然。那些具有显著 MACS p 值的区域将被进一步研究。对每个区域还计算了另外两个数值:t 检验的 p 值和倍数变化（婴儿样本中平均读段密度与老人样本中平均读段密度的比值）。为了避免由非常小的读段密度除以更小的读段密度而带来的较大倍数变化，我们可以在计算倍数变化时，在分子和分母中各加上一个伪记数（pseudocount）。与检测差异表达基因（方案 4）相似，我们可以 - $\log_{10}(\text{MACS } p \text{ value})$ 或 - $\log_{10}(t-\text{test } p \text{ value})$ 对 $\log_{2}(\text{倍性变化})$ 作火山图（volcano plot，图 8-28）。火山图中不同区域的基因座展现了强烈富集与样本间微小变化这两者之间的平衡情况。用户可以综合以上三个标准来选择用于进一步生物学检验的区域。

![](images/page_499_chart_4.jpg)

<details>
<summary>scatter</summary>

| Series | -log (read density ratio) (range) | -log (MACS p value) (range) |
| --- | --- | --- |
| MLXIPL | -2.0~0.5 | 0~220 |
| SOX11 | 0.5~2.5 | 0~230 |
</details>

图8-28 由寻峰算法MACS计算得到的 $p$ 值与婴儿和老人之间平均读段密度的倍数变化所作的火山图。每一点都是MACS找到的一个峰。红点表示该峰是在婴儿大脑中富集的H3K4me3区域，而蓝色表示的是在老人大脑中富集的H3K4me3区域。左上方和右上方的点代表了最值得进一步研究的点。读段密度（read density）被定义为一个峰中的读段总数除以峰的长度，此处使用了0.005作为伪记数（pseudocount）来将婴儿和老人大脑中读段密度低于0.005的峰进行排除（彩图请扫封底二维码）。

## ChIP-seq 峰的功能性注释

根据 ChIP-seq 峰与基因转录起始位点（TSS）的接近程度，可以对 ChIP-seq 峰进行分类，因为近距（proximity）意味着调控，尽管这不是直接证据。典型地，2kb 的临界值被用于定义近距。TSS 可以从注释中获得，如 RefSeq（Pruitt et al. 2007）、GenCode（Harrow et al. 2006）或者 UCSC known genes（Hsu et al. 2006），或者理想状态下从相同实验条件下相同细胞类型的 RNA-seq 中获取。如果可以获得定量表达数据（如来自 RNA-seq），我们可以查询那些 TSS 与峰接近的基因与其他基因相比是否有差异表达。这个问题可以通过对这两组基因的表达水平执行一个统计学检验（t 检验或 Wilcoxon 秩和检验）来完成。此外，计算 ChIP-seq 信号（读段的数量）和最近基因表达水平之间的相关性是有可能的。如果 ChIP-seq 邻近的基因属于一些通路，如那些被 Gene Ontology（GO）（Ashburner et al. 2000）分类的基因，我们就可以获取关于这个转录因子生物学功能的额外的信息。还有，与峰对应的 DNA 序列也许富集了转录因子的基序。方案 7 描述了识别序列基序的方法。

我们很难判断 TSS 相距较远的峰是否调控基因，如果答案为是，那就需要找出它们调控了哪些基因。虽然峰与基因相距较远，这些峰仍然对最近的基因进行调控这个假设依旧非常诱人。我们有两种实验方法可以对以上假设进行检验。

1. 例如，使用 RNAi 敲低（或沉默）相关因子，也许会导致基因的差异表达。

2. 使用 5C（Dostie et al. 2006）或 Chia-PET（Li et al. 2010）等技术来检验峰对应的基因组 DNA 和启动子 DNA 之间的物理联系。

随着越来越多的基因组数据集可被利用，一种方法就是去研究由一个 ChIP-seq 数据集获得的峰是否与另一组基因组数据集检测到的区域发生重叠。这种重叠可以通过一个统计学检验 [如超几何分布检验（hypergeometric test）] 来实现，或者通过两组数据在一个预先设定的基因组区域内（如基因组中所有被注释的启动子区域或所有 5kb 长的不重叠的窗口）的读段数量之间的相关性来完成。另一种比较多个基因组数据集的有力方法是使用接下来所描述的聚合图（aggregation plot）策略。

## 使用聚合图来展现基因组特定位置附近的平均信号谱

通常，转录因子的 ChIP-seq 的峰小于 1kb。在 TSS 附近富集的组蛋白修饰（如 H3K4me3 和 H3K27ac）往往标记几千个碱基（即一部分相近的核小体可以具有这个组蛋白标志）。其他组蛋白修饰（如 H3K4me27me3 和 H3K36me3）可以标记数十万个碱基。尽管不同基因位点之间的信号谱变化很大，在一组基因组位置（锚点，anchor）将平均信号谱（signal profile）排列起来仍能说明问题。通常使用的锚点为 TSS、转录终止位点（TTS）、剪接位点和转录因子结合位点。这些图被称为聚合图（aggregation plot），因为它们聚合（平均）了通过锚点对齐的信号谱。

图 8-29 显示的聚合图，涉及转录因子 GATA1 和 Egr1、一种绝缘子（insulator）结合蛋白 CTCF，以及人类基因组中所有被注释的 TSS 附近的组蛋白修饰 H3K4me3、H3K27ac、H3K36me3 和 H3K27me3。这些蛋白质根据其表达水平进行分组。作为比较，图中还包括了在相同细胞系中使用相同实验方法产生的输入(input)。这些数据由 ENCODE 协会(Raney et al. 2011; ENCODE Project Consortium 2011)产生。基于此图可以得到以下结论。

1. 转录因子（GATA1、Egr1 和 CTCF）比 H3K4me3 和 H3K4me27ac 具有较小的信号谱，而 H3K4me3 和 H3K4me27ac 又比 H3K36me3 具有较小的信号谱。
2. H3K4me3 和 H3K4me27ac 的波形中存在凹陷，对应于与 TSS 紧接着的、上游无核小体的区域。

3. H3K36me3 的波形在 TSS 下游上升，说明该标记位于基因之内。

![](images/page_501_image_3.jpg)

图 8-29 某个 TSS 附近所锚定的不同 TF 或组蛋白修饰与输入（input，背景）的聚合图例子。（A）GATA1；（B）Egr1；（C）CTCF；（D）H3K4me3；（E）H3K27ac；（F）H3K27me3；（G）H3K36me3；（H）Input。所有标记都根据它们与最近的 TSS 之间的距离（碱基数）进行聚合。我们可以从视觉上区分 TSS 附近标记的特定分布。例如，我们可以分辨出 H3K4me3 在 TSS 附近高度富集，尤其是在 +1 核小体附近，而在 -1 核小体附近衰减（彩图请扫封底二维码）。

## 方案 6 识别 ChIP-seq 数据集中富集的区域（寻峰）

本方案演示了如何使用 MACS 软件在一个 ChIP-seq 数据集中寻找峰（peak）。MACS 是使用最广泛的寻峰程序之一。本方案描述了如何在 UNIX 环境下，以及在 Galaxy 上运行 MACS 软件，如何提取由 MACS 获得的具有最显著 p 值的 500 个峰附近 50bp 距离的序列。

![](images/page_501_image_7.jpg)

## 材料

## 仪器

具有 Internet 连接和网页浏览器的电脑

MACS 软件

在 Unix 系统的电脑上下载并安装 MACS 软件包（安装指南见 http://liulab.dfci.harvard.edu/MACS/INSTALL.html）。或者，MACS 还可以在网页平台 Galaxy（http://main.g2.bx.psu.edu/）上运行，Galaxy 提供了一系列用于管理和分析生物数据的有用工具（Goecks et al. 2010）。

MS Excel 软件

UNIX 环境

本方案使用了 UNIX 指令。我们强烈推荐您在 Ubuntu、Centos/Red Hat 或 Mac OS X 等基于 UNIX 的操作系统中进行工作。如果你使用的是 Windows 操作系统，请先安装 Cygwin，然后在 Cygwin 下安装 Python 和 MACS。Cygwin 是一个免费的软件，它可以在 Windows 上提供一个类似 UNIX 的环境。我们可以在 http://www.cygwin.com/上找到 Cygwin 的安装包。在 Cygwin 上安装 Python 指南见 http://docs.python.org/install/index.html。

![](images/page_502_image_2.jpg)

## 方法

## 在 UNIX 环境中运行 MACS

1. 首先，如方案 5 所描述，将所有序列读段与参考基因组进行比对，MACS 接受多种格式（http://liulab.dfci.harvard.edu/MACS/00README.html）。在本方案中，我们使用方案 5 产生的 BED 文件 STAT1.sorted.bam.bed 和 INPUT.sorted.bam.bed。MACS 所要求的 BED 格式文件必须包括 6 个域（fields）（如方案 5 步骤 7.ii 所示）。

2. 根据实验设计设置以下三个参数。

i. 带宽（bandwidth）。为构建模型，设置用来扫描基因组的窗口大小。将带宽设置为被测序的 DNA 片段的平均大小。

ii. 标签尺寸（tag size）。序列读段的长度。

iii. 移位尺寸（shift size）。沿 3' 方向移动读段的核苷酸数量，如图 8-30 中步骤 1 所示。设置移位尺寸为 DNA 片段平均大小的一半。MACS 可以自动估计这个参数的大小。

3. 参照方案 5 中的相同例子。

i. 点击方案 5 图 8-25 中 “Samples” 部分的链接。在链接页面中，“Extraction protocol” 部分显示 “After adapter ligation DNA was PCR amplified with Illumina primers for 15 cycles and library fragments of \~ 250 bp (insert plus adaptorand PCR primer sequences) were band isolated from an agarose gel[在接头连接 DNA 经过 Illumina 引物 15 个循环的 PCR 扩增以后，由琼脂糖胶中分离得到长度约为 250bp 的文库片段(包含接头的插入和 PCR 的引物序列)的条带]”。此外，“Data processing” 部分中则显示“all the uniquely mapped tags reads (mapped against NCBI36) to the averaged sequenced DNA fragment size \~200 bps” [所有被单一定位的标签读段（被定位至 NCBI36）其长度至多为测序 DNA 片段平均长度大约 200bp]”。

ii. 带宽设置为 250 bp，标签尺寸设置为 36，移位尺寸设置为 100。

4. 输入以下指令使 MACS 以你所设置的参数运行:

```batch
macs -t STAT1.sorted.bam.bed -c Input.sorted.bam.bed --format=BED --bw=250
--tsize=36 --shiftsize=100 --name=STAT1 --pvalue=1e-5 --wig
```

“--pvalue=1e-5”选项告诉 MACS 仅报道具有比 1e-5 更显著 p 值的峰。“--wig”选项告诉 MACS 为每个染色体都产生一个 wiggle 文件，该种文件可以通过 UCSC 基因组浏览器进行可视化（Fujita et al. 2010）。wiggle 格式与方案 5 中描述的 bedGraph 格式相似；这两种格式都可以用于显示被定位至染色体位点的读段数量（http://genome.ucsc.edu/goldenPath/help/wiggle.html）。

要求 MACS 输出 wiggle 文件需要耗时间和空间，因此，如果不要求可视化，“--wig”可以忽略。

5. 被 MACS 识别的峰会被储存在一个名为 “STAT1\_peaks.xls” 的文件中，该文件可以被 Excel 软件用于进一步分析。MACS 还可以将峰及其顶点以 BED 格式输出等 (http://liulab.dfci.harvard.edu/MACS/00README.html)。

6. wiggle 结果文件可以作为一个定制通道上传至 UCSC 基因组浏览器中。上传定制通道过程见方案 1。图 8-30 比较了在相同基因座上被移位的读段与未移位的读段（方案 5，图 8-31）。

![](images/page_503_chart_2.jpg)

<details>
<summary>histogram</summary>

| Category | Peak Value |
| --- | --- |
| STAT1_negative | 59 |
| STAT1_positive | 73 |
| STAT1_shifted_chr1 | 150 |
</details>

图 8-30 在 UCSC 基因组浏览器上比较读段移位前后的分布情况（彩图请扫封底二维码）。

## 在 Galaxy 上运行 MACS

## 7. 为了在 Galaxy 上运行 MACS,

i. 通过点击 “Get Data”，然后点击左侧栏中的 “Upload File”（如图 8-31 红色框中所示），将方案 5 中产生的 BED 文件 STAT1.sorted.bam.bed 和 INPUT.sorted.bam.bed 上传至 Galaxy（http://main.g2.bx.psu.edu/）。

![](images/page_503_image_7.jpg)

<details>
<summary>text_image</summary>

Galaxy
Tools
Options
Get Data
• Upload File from your computer
• UCSC Main table browser
• UCSC Archaea table browser
• BX main browser
• BioMart Central server
• CrameneMart Central server
• Flymine server
• modENCODE fly server
• modENCODE modMine server
• Ratmine server
• YeastMine server
• modENCODE worm server
• Wormbase server
• EuPathDB server
• EncodeDB at NHGRI
• EpiGRAPH server
Send Data
ENCODE Tools
Lift-Over
Text Manipulation
Convert Formats
Upload File
File Format:
bed
Which format/See help below
File:
Choose File no file selected
TIP: Due to browser limitations, uploading files larger than 2GB is guaranteed to fail. To upload large files, use the URL method (below) or FTP of enabled by the site administrator)
URL/Text:
Here you may specify a list of URLs (one per line) or paste the contents of a file
Files uploaded via FTP:
File
Size
Date
✓ STAT1.sorted.bam.bed
820.0 Mb
04/06/2011 04.05 10 PM
✓ INPUT.sorted.bam.bed
719.3 Mb
04/06/2011 04.05 00 PM
This Galaxy server allows you to upload files via FTP. To upload some files, log in to the FTP server at main.g2.bx.psu.edu using your Galaxy credentials (email address and password)
Convert spaces to tabs:
□ Yes
Use this option if you are entering intervals by hand.
Genome:
Human Feb. 2009 (CRCh37/hg19) (hg):
Execute
History
Options
Unnamed history
2: INPUT.sorted.bam.bed
View data
Edit attributes
Delete
</details>

图 8-31 将数据上传至 Galaxy。Galaxy 的网页界面由三个栏组成。左侧 “Tools” 栏包括一系列的工具。点击每个工具标题会在中间栏中产生一个工作（job）提交页面，该页面将会显示该工具的选项和参数，并允许你运用该工具。右侧 “History” 栏记录了所有提交的任务及其结果。在本图中，使用了 “Upload File” 工具提交了两个 BED 文件。这两个文件上传任务被记录在 “History” 栏中。当这些工作结束后，点击这些任务后面的图标可以对它们进行查看、编辑和删除（彩图请扫封底二维码）。

ii. 在 “Upload File” 页面（图 8-31 中间栏的最上方）中，设置文件格式为 “bed” （图中顶部蓝色矩形所示）。

上传小文件时，通过点击 “Choose file” 按钮选择要上传的文件，提供 URL 或者将内容粘贴在 “URL/Text” 文本框（虚线框中所示）中。对于这样的文件（例如，此处的两个 ChIP-seq BED 文件），我们最好通过 Galaxy FTP（ftp://main.g2.bx.psu.edu）将其上传。获取 Galaxy FTP 需要在 Galaxy 进行注册。

iii. 文件上传至 Galaxy FTP 服务器之后，它们会被显示在图 8-31 橙色矩形中。

iv. 通过在文件名之前的方框中打钩可以选中这两个文件，在 “Genome” 下拉框中选择 “Human Feb. 2009(GRCh38/hg19) (hg19)”，并点击 “Execute”（绿色矩形中所示）来提交任务。

v. 这两个文件会显示在右侧的 “History” 栏中。点击 “History” 栏中的铅笔图标来编辑每个文件的各项属性（如文件名、文件类型等）。

## 8. 运行 MACS,

i. 点击工具栏中的 “NGS: Peak Calling”，然后点击左侧栏中的 “MACS” 以进入提交页面（图 8-32）。

ii. 将 “Experiment Name” 设置为 “STAT1”（图 8-32 中间栏中红色矩形）。

iii. 在图 8-32 蓝色框中所示的下拉框中，选择你刚刚上传的两个 BED 文件:STAT1.sorted.bam.bed 作为 “ChIP-Seq Tag File”；INPUT.sorted.bam.bed 作为 “ChIP-Seq Control File”。

iv. 如步骤 4 中所描述的，将 “Tag size” 设置为 “36”，将 “Band width” 设置为 “250”，如图 8-32 绿色框中所示。将其他参数设置为默认值，然后点击 “Execute”。

v. 按照预期右侧 “History” 栏（红色虚线框所示）中会出现两个任务。其中一项任务会产生所有峰区域的 BED 文件，而另一项任务会输出一个关于这些峰的 HTML 格式总结报告。

![](images/page_504_image_12.jpg)

<details>
<summary>text_image</summary>

Galaxy
Tools Options
Get Data
Send Data
ENCODE Tools
Lift-Over
Text Manipulation
Convert Formats
FASTA manipulation
Filter and Sort
Join, Subtract and Group
Extract Features
Fetch Sequences
Fetch Alignments
Get Genomic Scores
Operate on Genomic Intervals
Statistics
Graph/Display Data
Regional Variation
Multiple regression
Multivariate Analysis
Evolution
Motif Tools
Multiple Alignments
Metagenomic analyses
Human Genome Variation
EMBOSS
NGS TOOLBOX BETA
NGS: QC and manipulation
NGS: Mapping
NGS: SAM Tools
NGS: Indel Analysis
NGS: Peak Calling
• MACS Model-based Analysis of ChIP-Seq
• GeneTrack Indexer on a BED file
• Peak predictor on GeneTrack index
NGS: RNA Analysis
ROGENETICS
SNP/WGA: Data Filters
SNP/WGA: QC: LD; Plots
SNP/WGA: Statistical Models
MACS
Experiment Name:
STAT1
Paired End Sequencing:
Single End
ChIP-Seq Tag File:
1: STAT1 sorted bam bed
ChIP-Seq Control File:
2: INPUT sorted bam bed
Effective genome size:
270000000k
default: 2.7e+9
Tag size:
36
Band width:
250
Pvalue cutoff for peak detection:
1e-05
default: 1e-5
Select the regions with MFOLD high-confidence enrichment ratio against background to build model:
32
Parse xds files into into distinct interval files:
Save shifted raw tag count at every bp into a wiggle file:
Do not create wig file listers:
Use fixed background lambda as local lambda for every peak region:
up to 9X more time consuming
3 levels of regions around the peak region to calculate the maximum lambda as local lambda:
1000.5000.10000
Build Model:
Build the shifting model:
Diagnosis report:
Do not product report lister:
up to 9X more time consuming
Perform the new peak detection method (futurefdr):
The default method only consider the peak location, 1k, 5k, and 10k regions in the control data, whereas the new future method also consider the 5k, 10k regions in treatment data to calculate local bias.
Execute
</details>

图 8-32 在 Galaxy 上运行 MACS（彩图请扫封底二维码）。

## 9. 当 MACS 运行完毕后，

i. 点击 “History” 栏中 MACS 输出结果 “html report” 右侧的眼睛图标。你将看到

中间栏中出现了 5 个链接。

ii. 右击 “STAT1\_peaks.xls”，将其保存至你的本地磁盘中。

## 以具有最显著性 $p$ 值的500个MACS峰值为中心，提取 $\pm 50\mathrm{bp}$ 的峰宽序列

10. 将 MACS 输出结果 “STAT1\_peaks.xls” 重新上传至 Galaxy 中。

i. 点击左侧工具栏中的 “Get Data”，然后点击左侧栏中的 “Upload File”。
ii. 在中间栏的 “Upload File” 页面中，点击 “Choose File”，选择你本地硬盘驱动器中的文件 “STAT1\_peaks.xls”，然后点击 “Execute” 提交页面。

11. 根据其显著性得分（significance score）[计算公式为 $-10*\log_{10}(p$ value)] 对文件进行排序，显著性得分是“STAT1\_peaks.xls”文件中的第7列。

i. 点击 “Filter and Sort”，然后点击左侧栏中的 “Sort”，一个 “Sort” 页面将会出现在中间栏中（图 8-33A）。
ii. 在 “Sort Query” 中选择 “STAT1\_peaks.xls”，在 “on column” 中选择 “c7”，在 “with flavor” 中选择 “Numerical sort”，然后在 “everything in” 中选择 “Descending order”。
iii. 点击 “Execute” 来提交任务。
iv. 当任务完成后，点击铅笔图标（图 8-33A 右侧红圈中所示）将文件名改为 “Sorted\_peaks.xls”。

12. 仅保留最前面的 500 个峰。

i. 点击左侧栏中的 “Text Manipulation”，然后点击 “Select first”（见图 8-33C）。
ii. 在中间页面中，在 “Select first” 区输入 “500”，然后在 “from” 下拉选项中选择 “Sorted\_peaks.txt”，点击 “Execute” 来提交页面。
iii. 将文件名改为 “Top500\_peaks.txt”。

13. 得到峰顶点 $\pm 50$ bp 的坐标。每个峰区域的染色体起始和终止位点被列在 MACS 输出结果中。此外，MACS 报道了每个峰的顶点，这些顶点应位于转录因子结合位点附近。MACS 记录了各个峰的起始位点以及峰顶点距离峰起始位点的相对距离。为了得到峰顶点 $\pm 50$ bp 的坐标，我们将对 MACS 的输出结果执行简单的操作（即起始位点+峰顶点的相对距离 $\pm 50$）。

i. 在左侧栏中，点击 “Text Manipulation”，然后点击 “Compute”（图 8-33B）。
ii. 在 “Add expression” 文本框中输入 “c2+c5-50” [c 代表了列 (column), c2 为峰的起始位点坐标, c5 为峰顶点到起始位点的相对距离]。
iii. 在“as a new column to”的下拉选项中选择“Top500\_peaks.txt”，然后将“Round result?”选择框中选择“YES”，点击“Execute”来提交任务。
iv. 将文件名改为 “Top500\_summit.temp.”。
v. 再一次重复相同 “Compute” 操作，但本次操作中将 “Add expression” 文本框中的内容改为 “c2+c5+50”，在 “as a new column to” 的下拉选项中选择 “Top500\_summit.temp”，然后点击 “Execute” 来提交工作。
vi. 将文件名改为 “Top500\_summit.txt”。

14. 将步骤 13vi 中的文件 “Top500\_summit.txt” 转换为 BED 格式。

i. 点击左侧栏中的 “Text Manipulation”，然后点击 “Cut”（图 8-34A）。
ii. 在 “Cut columns” 文本框中输入 “c1,c10,c11”。
iii. 在 “Form” 下拉选项中选的 “Top500\_summit.txt”，然后点击 “Execute” 来提交任务。
iv. 将文件名改为 “Top500\_summit.bed”。

A

![](images/page_506_image_3.jpg)

<details>
<summary>text_image</summary>

Galaxy
Tools
Get Data
Send Data
ENCODE Tools
Lift-Over
Text Manipulation
Convert Formats
FASTA manipulation
Filter and Sort
• Filter data on any column using
simple expressions
• Sort data in ascending or
descending order
• Select lines that match an
expression
• Filter on ambiguities in
polymorphism datasets
Sort
Sort Query:
2: Sort on data 1
on column:
c7
with flavor:
Numerical sort
everything in:
Descending order
Column selections
Add new Column selection
Execute
History
Options
Unnamed history
2: Sort on data 1
1: STAT1 peaks.xls
</details>

B

![](images/page_506_image_5.jpg)

<details>
<summary>text_image</summary>

Galaxy
Tools
Options
Get Data
Send Data
ENCODE Tools
Lift-Over
Text Manipulation
Add column to an existing
dataset
Compute an expression on every
row
Concatenate datasets tail-to-
head
Condense consecutive characters
Convert delimiters to TAB
Merge Columns together
Create single interval as a new
dataset
Cut columns from a table
Change Case of selected columns
Paste two files side by side
Remove beginning of a file
Select random lines from a file
Select first lines from a dataset
Select last lines from a dataset
Trim leading or trailing
characters
Select first
Select first:
10
lines
from:
2: Sorted_peaks.txt
Execute
What it does
This tool outputs specified number of lines from the beginning of a dataset
Example
Selecting 2 lines from this:
chr7 56632 56652 D17003_CTCF_R6 310 +
chr7 56736 56756 D17003_CTCF_R7 354 +
chr7 56761 56781 D17003_CTCF_R4 220 +
chr7 56772 56792 D17003_CTCF_R7 372 +
chr7 56775 56795 D17003_CTCF_R4 207 +
will produce:
chr7 56632 56652 D17003_CTCF_R6 310 +
chr7 56736 56756 D17003_CTCF_R7 354 +
History
Options
Unnamed history
3: Select first on data 2
2: Sorted peaks.txt
1: STAT1_peaks.xls
</details>

C

![](images/page_506_image_7.jpg)

<details>
<summary>text_image</summary>

Galaxy
Tools
Get Data
Send Data
ENCODE Tools
Lift-Over
Text Manipulation
Add column to an existing
dataset
Compute an expression on every
row
Concatenate datasets tail-to-
head
Compute
Add expression:
c2+c5+50
as a new column to:
4: Top500_summit.temp
Dataset missing? See TIP below
Round result?
YES
Execute
History
Options
Unnamed history
5: Top500_summit.txt
4: Top500_summit.temp
3: Top500_peaks.txt
2: Sorted_peaks.txt
1: STAT1_peaks.xls
</details>

图 8-33 Galaxy 中的命令设置。（A）以每个峰的分值降序方式对 MACS 输出进行排序。（B）选择 500 个最可靠的峰。（C）计算每个峰中心 ±50bp 的坐标。必须注意到该操作需要采用不同的表达和文件执行两次（彩图请扫封底二维码）。

15. 为了使 Galaxy 了解 “Top500\_summit.bed” 是一个 BED 文件，且它被定为至 hg19 基因组上，

i. 点击铅笔图标，将 “Database/Build” 改为 “Human Feb. 2009 (GRCh37/hg19)”，然后点击如图 8-34B 中红色矩形中所示的 “Save”。

ii. 编辑属性，再次点击铅笔图标，本次在 “NewType” 下拉选项中选择 “bed”。点击图 8-34B 中蓝色矩形中所示的 “Save”。

16. 获取与峰顶点对应的基因组序列。

i. 点击 “Fetch Sequences”，然后点击 “Extract Genomic DNA”（图 8-34C 左侧栏

中所示）。

ii. 将 “Fetch sequences for intervals in” 设置为 “Top500\_summit.bed”，然后在 “Interpret features when possible” 下拉选项中选择 “No”。

![](images/page_507_image_4.jpg)

图 8-34 Galaxy 配置工具。（A）提取峰顶点坐标，并把它们存储为 BED 格式。（B）设置文件 “Top500\_summit.bed” 的属性和数据类型。请注意你需要编辑两次:一次是在红色矩形标记处，另一次是在蓝色矩形标记处。（C）提取峰顶点 ±50-bp 的 DNA 序列（彩图请扫封底二维码）。

iii. 在 “Source for Genomic Data” 中选择 “Locally cached”，在 “Output data type” 中选择 “FASTA”。
iv. 点击 “Execute” 来提交任务。
v. 将文件名改为 “Top500\_summit.fa”。通过点击软磁盘图标下载此文件，如图8-34C右侧红色圈中所示。
vi. 我们可以对这些序列进行基序分析（见方案 7）来发现 STAT1 上新的或已知的结合基序。

## 如何在没有输入（input）的情况下运行 MACS?

MACS 使用一个参数  $\lambda$  将  $N_{input}$  的分布模拟为泊松分布。 $\lambda$  代表了分布均值和方差。在 MACS 中，在每个以可能峰所在位置为中心的滑动窗口中，根据以下公式对  $\lambda$  进行动态测量。

$$
\lambda = \max (\lambda_ {\mathrm{BG}}, [ \lambda_ {1 \mathrm{k}}, ] \lambda_ {5 \mathrm{k}}, \lambda_ {1 0 \mathrm{k}})
$$

式中，$\lambda_{\mathrm{BG}}$ 是预期的标签数量（被定位至基因组的标签的数量 $\times$ 窗口大小/基因组大小）；$\lambda_{1\mathrm{k}}$、$\lambda_{5\mathrm{k}}$、$\lambda_{10\mathrm{k}}$ 分别指在输入中，以峰位点为中心的 $1\mathrm{kb}$、$5\mathrm{kb}$ 或者 $10\mathrm{kb}$ 大小的窗口中的标签数量。如果没有输入（input）数据，以上所有参数都是基于信号数据来估计的，且不使用 $\lambda_{1\mathrm{k}}$。请注意，MACS 在没有输入（input）数据的情况下运行也许会漏掉宽于 $5\mathrm{kb}$ 的峰。

为了使 MACS 在没有输入(input)数据的情况下运行, 只需忽略-c 参数(-c argument)即可。在我们之前的例子中, 方法部分步骤 4 将成为下列形式。

```shell
macs -t STAT1.sorted.bam.bed --format=BED --bw=250 --tsize=36 --shiftsize=100
    --name=STAT1 - pvalue=1e-5 --wig
```

![](images/page_508_image_8.jpg)

## 讨论

MACS 通过比较 ChIP-seq 和 input 数据来识别在 ChIP 中被富集的基因组区域。这些区域可能是转录因子结合位点，也可能具有表观遗传标记。比较多个生物样本的 ChIP-seq 数据是有益的。在多个样本中的重叠区域可以产生更为可靠的结果。MACS 使用了 6 个字节（byte）在内存中储存标签（tag），所以确保你的电脑有足够的内存空间来运行 MACS 非常重要。例如，如果你的数据集中有 5 亿个读段，如 MACS 文件（MACS documentation）中所指出的那样，MACS 将需要至少 3Gb 的 RAM，通常需要大约 4Gb 的空间来储存额外的信息。根据数据集大小和所使用的参数，MACS 可能会需要数个小时来完成工作（http://liulab.dfci.harvard.edu/MACS/00README.html）。

Galaxy 是一个可执行多项任务的柔性平台。本方案中所展示的 Galaxy 功能只是给读者展现了数据逐步分析的风格。Galaxy 还提供了一个将这些所有步骤都串联成一个 “工作流（workflow）” 的功能，这个功能可以被简单地重复使用，并应用于其他数据集。更多信息请见 Galaxy wiki 的网页:https://bitbucket.org/galaxy/galaxy-central/wiki/Home。

## 网络资源

Cygwin http://www.cygwin.com/

Galaxy http://main.g2.bx.psu.edu/

Galaxy wiki https://bitbucket.org/galaxy/galaxy-central/wiki/Home

MACS install instructions http://liulab.dfci.harvard.edu/MACS/INSTALL.html

Python http://docs.python.org/install/index.html

wiggle format http://genome.ucsc.edu/goldenPath/help/wiggle.html

# - 基序（motif）寻找简介

转录因子（transcription factor, TF）是一大类与基因组 DNA 结合并调控转录的蛋白质。人类基因组中存在数千种 TF。转录调控是对基因表达时空分布进行控制的一种常见机制，TF 的序列特异性则是这个复杂调控机制的核心。在原核生物中，单个 TF 与某个位点进行结合可能就足以进行转录调控。在真核生物中，实验数据证实了结合到相邻或重叠位点的多个 TF 之间存在相互作用，这些位点被统称为一个顺式调控模块（cis-regulatory module, CRM）。提出 CRM 这个概念的主要原因是基于这样的事实，即在任何基因组中，在不同细胞类型和受到多种刺激时被观察到的转录模式的数量，远远超过了转录因子的总数。

每个 TF（或者每组紧密相关的 TF）都具有特征性的结合特性，包括其 DNA 结合位点的宽度和各个位点上核苷酸的偏好，这些被统称为序列基序（sequence motif）。某些位点具有严格的核苷酸偏好（这可能是由 TF 和 DNA 上这些位点之间广泛的原子接触所导致的），而其他位点具有较弱的核苷酸偏好。可以通过将与某个 TF 结合的一组已知 DNA 序列比对来确定位置偏好（position preferences）。如果我们假设基序中的所有位点在结合过程中独立发挥作用（本方案始终承认此假设，并认为该假设是一个好的近似方法），比对结果可被总结为一个计数矩阵（count matrix，图 8-35B），运用信息论中熵（entropy）的概念可以对以上矩阵进行量化。熵（entropy）是对不确定性的测量。对于一个可能出现 4 种碱基的位点，各碱基出现的概率为 $p_i$ ($i = A, C, G, T$)，其熵被定义为 $-\sum_{i=1}^{4} p_i \times \log_2(p_i)$。如果 4 种碱基出现的概率相同，那么该位点的最大不确定性或最大熵为 2 bit。如果该位点通常出现某种特定的碱基（例如，$p_A = 1$ 且 $p_C = p_G = p_T = 0$），则该位点的不确定性或熵为 0。因此，一个基序上某个特定位点所包含的信息量为 $2 - (-\sum p_i \times \log_2(p_i))$ ($i = A, C, G, T$)。基序上各个位点的信息含量可以用一张修正后的条形图来表示，图中条形被 A、C、G、T 这些字母的堆叠所取代，字母堆叠的高度与相应位点的信息含量成比例，且 4 种字母的相对高度与该位点出现的碱基的相应频率成比例。这样的图通常被称为序列标识或基序标识（sequence or motif logo）（Schneider and Stephens 1990）（图 8-35A）。

运用相对熵（relative entropy）的概念，一个基序的计数矩阵可被用于预测一段长DNA序列中的结合位点。假设一个基序中的某个位点上出现概率为 $p_i$ （$i = A, C, G, T$）的4种碱基，而非基序DNA（背景）某个位点上出现概率为 $q_i$ （$i = A, C, G, T$）的4种碱基，则基序位点的相对熵就被定义为 $-\sum p_i \times \log_2(p_i / q_i)$。相对熵的值越高，该基序位点与背景的差异就越大。为了便于沿一段DNA序列进行基序快速扫描以找到结合位点，所有4种碱基和所有基序位点的 $p_i \times \log_2(p_i / q_i)$ 可以储存在矩阵中，这种矩阵通常被称为位点特异性记分矩阵（position-specific scoring matrix，PSSM）、位点权重矩阵（positionweight matrix，PWM）或者序列谱（profile）。任何与PSSM长度相等的序列都可以根据序列中各个位点的碱基所对应的分值进行求和，计算得到该序列对应的分值。图8-35A～C依次显示了TATA基序的序列标识、计数矩阵和PSSM。

现在有多个 TF 结合基序及其 PSSM 的集合，使用最为广泛的是 JASPAR（Sandelin and Wasserman 2004）和 TRANSFAC（Matys et al. 2003）。其中，JASPAR 为一个开源的资源（http://jaspar.genereg.net/）。

![](images/page_510_chart_2.jpg)

<details>
<summary>bar</summary>

| Category | Bits |
| --- | --- |
| 1 | ~0.2 |
| 2 | ~1.2 |
| 3 | ~1.4 |
| 4 | ~1.9 |
| 5 | ~1.7 |
| 6 | ~1.3 |
| 7 | ~1.8 |
| 8 | ~0.5 |
| 9 | ~0.6 |
| 10 | ~0.1 |
| 11 | ~0.1 |
| 12 | ~0.1 |
| 13 | ~0.1 |
| 14 | ~0.1 |
| 15 | ~0.1 |
</details>

| 16 | 39 | 37 | 8 |
| --- | --- | --- | --- |
| 4 | 12 | 5 | 79 |
| 90 | 0 | 1 | 9 |
| 1 | 2 | 1 | 96 |
| 91 | 0 | 1 | 8 |
| 69 | 0 | 0 | 31 |
| 92 | 1 | 5 | 2 |
| 57 | 1 | 11 | 31 |
| 40 | 11 | 40 | 9 |
| 14 | 35 | 39 | 12 |
| 21 | 38 | 33 | 8 |
| 21 | 33 | 33 | 13 |
| 21 | 30 | 33 | 16 |
| 17 | 28 | 36 | 19 |
| 20 | 26 | 36 | 18 |

<table><tr><td rowspan="16">C</td><td rowspan="16">T</td><td rowspan="16">G</td><td rowspan="16">C</td><td rowspan="16">A</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr></table>

图 8-35 三种常见的 TATA 基序的表现形式。（A）序列标识。x 轴对应基序的位点，y 轴为对应位点的相对熵的  $\log_{2}$  值。A/T/C/G 字母比例越高，说明基序中该位点出现这个核苷酸的频率越高。（B）计数矩阵。矩阵中每个元素上的数字可以通过基序该位置上的碱基总数进行标准化，产生该位置上各个碱基出现的频率或概率，得到的矩阵亦被称为位点特异性概率矩阵（position-specific probability matrix，PSPM）。（C）位点特异性记分矩阵（PSSM）。计算一个 PSSM 需要背景频率（即前文所提到的  $q_{i}$ ），在这个例子中采用均匀分布背景（ $q_{i}=0.25; i=A, C, G, T$ ）（彩图请扫封底二维码）。

## 基序搜索问题

通过与一组背景序列进行比较，寻找在一组调控序列中富集的基序，通常称为基序搜索问题。调控序列通常有三个来源:①基因组同源序列（如多个物种中直系同源基因的启动子）；②一个物种中被共同调控的基因启动子（由大规模表达研究或文献所确认，在相同调控通路所确定的、具有相似表达模式的基因）；③通过大规模 TF-DNA 结合实验识别的区域，例如，与微列阵偶联的 ChIP 技术(ChIP-chip)，或者与大规模测序(massive sequencing)偶联的 ChIP 实验(ChIP-seq；见方案 6)，或者蛋白结合微列阵(protein-binding microarrays, PBM)(Mukherjee et al. 2004)(见第 10 章和第 20 章)的体外实验技术。

背景序列的选择需要谨慎对待，因为基因组序列是高度结构化的。理想状态下，背景序列应该与调控序列为相同类型，但不与待研究的 TF 进行结合。例如，如果调控序列为肌肉细胞中特异表达的基因启动子序列，一个用于背景序列选择的好策略就是选择在所有类型细胞中普遍表达且表达水平相同的基因启动子。

有两种寻找基序的通用方法。第一种是对任何种类的基序进行从头搜索。第二种是检查一个包含已知基序的文库，并找出与背景序列相比在调控序列中统计学上过量表达的基序。从头搜索方法具有更大的通用性，利用该种方法可以找到全新的基序；但与基于文库的搜索方法相比，增加的搜索空间（整个基序范围 vs. 预先设定的列表）使得从头搜索方法敏感性较低。此外，从头搜索方法仅能预测出基序但不能预测对应的 TF，而预先编译好的文库通常包括了 TF 的注释。

在本方案中,我们将使用三种方法:①对所有 $k$-mer($k$ 为基序宽度)进行穷举搜索(exhaustive search); ②MEME, 一种从头搜索的方法 (Bailey and Elkan 1994); ③Clover, 一种基于文库的方法 (Frith et al. 2004)。感兴趣的读者可以参考用于比较从头搜索 (Tompa et al. 2005) 和基于文库 (McLeay and Bailey 2010) 方法的相关资源, MDscan 是另一种从头搜索方法, 而 AME 则是另一种基于文库的方法, 这些方法在信息栏 “算法、门户网站和方法” 中介绍。

## 所有 k-mer 的穷举搜索

当基序较短（如<8bp）且两组序列（调控序列和背景序列）中存在足够多的序列时，最直观的方法就是对这两组序列中 $k$-mer 的出现频率进行比较。$k$-mer 的平均出现频率可以通过宽度为 $k$ 的滑动窗口来计算，首先计算出一个序列中 $k$-mer 的百分比，然后在整组序列中计算该 $k$-mer 平均值。我们可以作一张散点图（scatter plot）来查看 $k$-mer 的分布情况，图上各点分别代表一个 $k$-mer，两条坐标轴分别代表 $k$-mer 在两组序列中的平均出现频率。图 8-36 通过对一组来自由 UCSC 表格浏览器（UCSC table browser，Karolchik et al. 2004）上获取的 TATA 结合蛋白（TATA-binding protein，TBP）的推定结合位点，阐述了这种方法的使用。关于获取 CREB 结合位点的例子见以下方法部分。为了获得背景序列，我们对 TATA 结合序列进行了随机洗牌(random shuffling)。TATA 组和背景组中共存在 113 个 6-mer。很明显，在 TATA 组中被富集的 6-mer 与 TBP 的结合基序相似（图 8-36）（Bucher 1990）。

![](images/page_511_chart_6.jpg)

<details>
<summary>violin</summary>

| TATA sequence logo | Backlog average frequency (range) | TATA 结合序列中平均出现频率 (range) |
| --- | --- | --- |
| TATAAA | ~0.01 | 0.6~0.6 |
| ATAAAA | ~0.01 | 0.2~0.2 |
| ATATAA | ~0.01 | 0.15~0.18 |
| TAAAAA | ~0.01 | 0.1~0.12 |
| ATAAAG | ~0.01 | 0.1~0.12 |
| TAAAAG | ~0.01 | 0.05~0.08 |
</details>

图8-36 TATA结合序列中6-mer的平均出现频率（y轴）对随机抽取序列中平均出现频率（背景； $x$ 轴）作图。（红色）如小图所示，很明显，位置最高的6个6-mer（与背景相比，在调控序列中富集的序列）为已知的TATA基序的子链（substring）（彩图请扫封底二维码）。

## MEME

MEME 软件假设调控序列是由一个双组分有限混合模型（two-component finite mixture model）产生的。一种组分描述了基序的出现频率，而另一种组分描述了序列中的所有其他位点（正如在背景序列中）。MEME 使用了期望最大化（expectation maximization，EM）方法来估计模型中的两个参数:之前已提及的基序位点特异性概率矩阵（PSPM）和调控序列中核苷酸出现频率的百分比，即基序中每个位置每个核苷酸的出现频率。MEME 在两个步骤之间进行迭代。在给定调控序列和两个参数当前估计值情况下，MEME 的 E（expectation,