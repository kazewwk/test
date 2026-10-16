## 参考文献

- Bollum FJ, Chang LM, Tsiapalis CM, Dorson JW. 1974. Nucleotide polymerizing enzymes from calf thymus gland. Methods Enzymol 29:70–81.
- Chang LM, Bollum FJ. 1986. Molecular biology of terminal transferase. CRC Crit Rev Biochem 21: 27–52.
- Gilfillan S, Benoist C, Mathis D. 1995. Mice lacking terminal deoxynucleotidyl transferase: Adult mice with a fetal antigen receptor repertoire.

Immunol Rev 148: 201–219.

Kato KI, Gonçalves JM, Houts GE, Bollum FJ. 1967. Deoxynucleotide-polymerizing enzymes of calf thymus gland. II. Properties of the terminal deoxynucleotidyltransferase. J Biol Chem 242: 2780–2789.

(林艳丽 陈红星 译，陈苏红 校)

## 第8章 生物信息学

导言 | 致谢 434

方案 | 1 使用 UCSC 基因组浏览器将基因组注释可视化 434 关于将上亿短读段定位至参考基因组上的简介 470
- 序列比对和同源性检索简介 442 5 将上亿短读段定位至参考基因组上 472
2 使用 BLAST 和 ClustalW 进行序列
比对和同源性检索
444
● 寻峰算法简介
6 识别 ChIP-seq 数据集中富集的区域
478
3 使用 Primer3Plus 设计 PCR 引物 450 （寻峰） 483
- 基于微阵列和 RNA-seq 的表达谱
分析简介
456
- 基序（motif）寻找简介
7
发现顺式调控基序
491
495
4 使用微阵列和RNA-seq进行表达序列谱分析 461

信息栏 | 数据格式 503

算法、门户网站和方法 506

## 导言

生物信息学是计算科学与生物学结合产生的领域。计算对生物学研究很重要这一观念是在20世纪70年代出现的，当时，由实验得到的蛋白质和核酸序列正开始积累。为此，为许多人公认的生物信息学先驱 Margaret Dayhoff 启动了蛋白质序列收集项目，并将这些蛋白质序列在名为 Atlas of Protein Sequence and Structure（1965—1978）的系列丛书中发表。随着获得越来越多的蛋白质序列，人们清楚地认识到书籍已经不是储存和发布序列的合适媒介，需要数据库来满足这些需求。1984年，Dayhoff 在美国国家生物医学研究基金会（National Biomedical Research Foundation）之下成立了第一个蛋白质序列数据库，名为 Protein Information Resource。与此同时，在洛斯阿拉莫斯国家实验室（Los Alamos National Laboratory）的 Walter Goad 领衔开发了第一个核酸序列数据库——Los Alamos Sequence Database（洛斯阿拉莫斯序列数据库），该数据库由他在1979年启动。Goad 的数据库在1982年以 GenBank 为名得到了美国国立卫生院（National Institutes of Health）的资助，逐渐成为一个可公开存取的核酸序列及其蛋白质翻译序列数据库。同期建立的数据库还有1980年欧洲分子生物学实验室建立的核酸序列数据库（EMBL）和1984年日本建立的DNA数据库（DNA Data Bank of Japan, DDBJ）。这三个数据库在1984年合并为国际核酸序列数据库（International Nucleotide Sequence Database），三者每天都会进行数据交流。到目前为止，GenBank（http://www.ncbi.nlm.nih.gov/genbank/）仍然是提供所有公开DNA序列的最大数据库。它目前和其他很多被广泛运用的数据库一样，隶属于美国国家生物技术信息中心（National Center for Biotechnology Information），并由其进行维护与发布。

序列数据库的应用之一就是研究分子进化，Dayhoff 以蛋白家族形式来组织其序列图集，并率先开发了用于蛋白质序列比对的可编程计算机方法，并基于序列比对来识别进化历史（系统发育和进化树）。随着 NCBI 数据库中序列的快速积累，人们迫切需要开发出一种能够将一个查询序列（query sequence）与数据库中所有序列进行比对的算法，从而识别出与查询序列足够相似的数据库中的序列，进而推断出共同的进化历史（同源性，homology）。自 1989 年起担任 NCBI 主任的 David Lipman 领导了一支团队开发了用于序列两两比对和数据库检索的 BLAST 算法（Altschul et al. 1990），该算法目前仍为应用最广泛的生物信息学工具之一。本章中所描述的许多应用所依赖的其他重要算法是在过去的几十年中发展起来的。关于这些内容的历史记录可以在 Mount（2001）一书中找到。关于一些特定算法的相关信息见本章末尾信息栏中“算法、门户网站和方法”。

生物信息学在20世纪90年代后期因“人类基因组计划”（Human Genome Project）成为被关注的焦点。将1kb长度的读段（reads）拼接成整个人类基因组（3Gb），这本身就是一个巨大的生物信息学挑战。对新测序得到的人类基因组进行注释是另外一个大的挑战，例如，识别包含剪接模式在内的所有基因和所有调控区等。随着测序完成的基因组数据的快速积累，人们很快意识到，关于大部分新发现基因和基因组中许多功能性区域，并没有其他已知的生物学信息可供参考。一种推测生物学功能的方法是通过同源性进行推断:因为同源基因具有一个共同的进化历史，所以它们很有可能具有相同的生物学功能。由于基因组测序的速度不断加快，上述挑战使得生物信息学家们在过去的十年中非常忙碌。

与发表一个测序完成的人类基因组相比，更为重要的是人类基因组计划已经改变了人们对生物学的思维模式，目前更受青睐的做法是同时研究基因组中的所有基因，而不是一次只研究其中一个基因。由人类基因组计划带来的两个革新即微阵列（见第10章）与新的测序技术（见第 11 章），使上述基因组水平的思维模式成为现实。微阵列是寡核苷酸所组成的阵列，这些寡核苷酸是根据一个参考基因组设计的，这样它们就能够与由任何生物化学方法富集的基因组 DNA 或转录物进行特异性杂交。微阵列的一种常见应用是检测基因组中所有基因的转录水平。近年来，测序方法的创新极大地提高了测序通量并降低了 DNA 测序的成本，使得这些测序技术能够为大多数生物学家们所用。例如，RNA 测序技术（RNA-seq）能对基因组的所有转录物进行直接测序，而 ChIP-seq（见第 20 章）则能对所有能够被染色质免疫沉淀所富集的基因组 DNA 进行直接测序。这些实验创新带来了新的生物信息学挑战。例如，新的测序技术促进了对大量短读段序列数据进行定位、组装及解释的新生物信息学方法的发展。

现在，生物信息学已经成为一个宽广的领域，该领域包括了各种各样运用计算方法来研究生物学问题的课题。在计算方面，生物信息学的内容既包括开发新数学公式、统计和计算方法，也包括运用目前已有的理论和算法来解决新的生物学问题。在生物学方面，生物信息学的内容包括了为聚合酶链反应（PCR）设计引物、在一段DNA序列中识别某个基因的结构、通过序列预测蛋白质结构和/或功能、识别某段序列中的调控蛋白结合位点、基于某个蛋白家族的序列来建系统发育树、基于蛋白质间相互作用和蛋白质与DNA的相互作用数据来构建调控互作网络、在多个个体中识别多态性、从头组建某个基因组等各种应用。

生物信息学方法本身亦是多种多样的。因为序列是生物数据的主要来源，许多生物信息学工具都被设计用于基因或蛋白质序列、基因序列与基因组之间或基因组之间的快速准确比较。另一类生物信息学工具则通过数据挖掘、模式识别及其他机器学习方法来识别生物学数据中反复出现的模式（如响应某种刺激的基因共同表达模式）。因为将生物学信号从随机噪声中区分出来是很重要的，统计检验成为了生物信息分析中的重要成分。所有生物信息结论都需要得到统计学显著性的证明，即多重检验校正（multiple testing correction）后得到的 $p$ 值或 $q$ 值。

生物信息学工具有多种类型。大型集中化的生物信息资源，如 NCBI 和欧洲生物信息学中心（EBI），提供了许多数据库和网页版的分析工具。这些工具在服务器上运行，并不需要用户提供计算资源。它们具有网页用户界面，因此并不要求用户具有广泛的计算培训经历。其他生物信息学工具，尤其是那些需要大量计算能力和储存空间的工具，通常在类似 UNIX 的环境下运行，且需要被安装在用户的电脑上才能被使用。这些工具常常可以通过安装在本地或通过云计算的计算机集群得到加速。受过电脑培训的用户可以将这些程序进行安装和使用，并根据实际的生物学问题对它们进行修改。

本章重点介绍了分子生物学家经常使用的对序列数据进行分析的生物信息学方法，尤其是那些拥有图形化用户界面且不要求用户具有较强计算背景的方法。本章提供了7种生物信息学分析方案的具体步骤。方案1叙述了如何使用UCSC基因组浏览器在特定基因组区域上进行序列和注释的检索及可视化。方案2介绍了用于序列比对和同源性搜索的两种广泛使用的工具——BLAST和ClustalW。在对数据库与序列比对概念进行介绍的基础上，方案3介绍了用于引物设计的工具Primer3Plus。其余4种方案则适用于高通量数据分析。首先，方案4详细阐述了如何分析由微阵列和RNA-seq得到的表达谱数据。接下来的方案则着重于下一代测序（next-generation sequencing）数据:如何将序列定位至参考基因组上（方案5），检测被最多读段定位的基因组区域（方案6），以及在这些区域中发现序列模式（方案7）。本章仅涵盖了很小一部分生物信息学工具，我们鼓励读者探索生物信息学广阔领域中的其他工具。

与本章末尾的信息栏部分类似，本章各方案前的信息部分提供了更多详细的关于特定算法和方法的信息。

![](images/page_452_image_2.jpg)

## 致谢

我们在此感谢 University of Massachusetts 医学院的 Brian Pierce 教授和 University of Washington 的 William Noble 教授，感谢他们对本章内容进行了评阅和编辑。

## 网络资源

GenBank http://www.ncbi.nlm.nih.gov/genbank/

## 方案 1 使用 UCSC 基因组浏览器将基因组注释可视化

目前，基因组数据和注释在诸如UCSC Genome Browser（http://genome.ucsc.edu/;Rhead et al. 2010）、NCBI（http://www.ncbi.nlm.nih.gov; Sayers et al. 2009）和Ensembl（http://ensembl.org; Hubbard et al. 2009）等数据库中迅速累积。鉴于这些基因组数据库的巨大规模，如何方便地获取某个特定基因位点的已知数据和注释非常重要。例如，对于一个新鉴定的、与某个转录因子结合的顺式调控元件，可以立即想到的问题有:该元件是否位于某个转录起始位点附近，如果是，则需要知道相应基因的名字；该基因座的组蛋白或DNA是否被修饰。UCSC基因组浏览器是以很多真核基因组的参考序列或草图为基础，以通道（tracks）形式来组织数据和注释，并将这些信息呈现在一个强大的网页版图形界面上。本方案描述了如何运用UCSC基因组浏览器将某个特定的基因区域中被选中的通道进行可视化处理、下载相关数据和注释用于进一步的分析，并且检索得到多序列比对及它们的保守评分。

![](images/page_452_image_9.jpg)

## 材料

## 仪器

具有 Internet 连接和网页浏览器的电脑

UNIX 环境

本方案使用了 UNIX 指令。如果你使用的是 Windows 电脑，请安装 Cygwin（http://www.cygwin.com/）以运行 UNIX 指令。Cygwin 是一个免费的软件，它可以在 Windows 上提供一个类似 UNIX 的环境。Mac OS X 用户可以通过以下路径来获得 UNIX 环境:应用（Application）→实用工具（Utilities）→终端（Terminal）。

UCSC Genome Browser (http://genome.ucsc.edu/)

![](images/page_452_image_16.jpg)

## 方法

## 准备基因组坐标或序列

一个基因组区域可以被其所在染色体及其在基因组草图（genome assembly）中的起始和终止坐标所确定，还可以被某个基因名所确定。如果你有一个基因组区域的坐标或者基因名，请选择“使用UCSC基因组浏览器可视化基因组区域”（步骤5和6）。如果你有多个区域的基因组坐标，请选择“使用UCSC表格浏览器（Table Browser）可视化多段基因组区域”（步骤7\~9）。如果你有的是原始序列，请执行步骤1\~4。

1. 将基因组序列保存为 FASTA 格式（见信息栏“数据格式”），并使用 UCSC 基因组浏览器中的 BLAT 序列相似性搜索工具（Kent 2002）将相关序列定位至某个参考基因组。“BLAT”标签位于基因组浏览器所有页面的顶部。

BLAT 工具非常有用。例如，当你有两个人的转录物 5' 端序列，并想要确认 C-磷酸-G（CpG）岛是否位于这些序列上游 1kb 以内时，你就可以用 BLAT 来解决问题。详见“疑难解答”。

2. 进入UCSC基因组浏览器（Genome Browser）（http://genome.ucsc.edu/）。

i. 点击页面顶部的 “BLAT” 键，并将由 BLAT 提供的两段序列粘贴至查询窗口。
ii. 将 “Genome” 一栏选择为 human, “Assembly” 一栏选择为 Mar. 2006, “Query type” 一栏选择为 DNA, “Sort output” 一栏选择为 score, “Output type” 一栏选择为 hyperlink, 然后点击 “Submit”。以上过程将产生与查询序列匹配的基因组区域列表, 并根据比对分数进行排列 (图 8-1)。

其他分类选项如 “query, score” 和 “chrom, score” 将使以上结果列表以查询形式或染色体形式被分类。

![](images/page_453_image_10.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["browser"] --> B["details transcript_2"]
  B --> C["200 1"]
  C --> D["200 200 100.0%"]
  D --> E["7 + 98844537"]
  E --> F["98844736"]
  F --> G["200"]
  H["browser"] --> I["details transcript_1"]
  I --> J["200 1 200 100.0%"]
  J --> K["7 - 99517108"]
  K --> L["99517307"]
  L --> M["200"]
  N["browser"] --> O["details transcript_1"]
  O --> P["24 166 190 200 100.0%"]
  P --> Q["11 - 111288861"]
  Q --> R["111288886"]
  R --> S["26"]
  T["browser"] --> U["details transcript_1"]
  U --> V["21 165 185 200 100.0%"]
  V --> W["18 + 19124309"]
  W --> X["19124329"]
  X --> Y["21"]
  
  style A fill:#f9f,stroke:#333,stroke-width:2px
  style H fill:#f9f,stroke:#333,stroke-width:2px
  style T fill:#f9f,stroke:#333,stroke-width:2px
  Direct link to visualize this region in UCSC Genome browser
```
</details>

图 8-1 BLAT 输出。点击超链接（红框）来可视化每一个区域（彩图请扫封底二维码）。

3. 仅使用高度可信的命中结果（由 BLAT 所识别得到的与查询序列具有高相似性的基因组区域）用于进一步分析。某个命中结果的可信度可以通过联合考虑得分、长度和序列相同性来衡量。得分正比于比对长度（图 8-1 中 “SPAN” 一栏）。只有那些与查询序列相同性接近 100% 且长度几乎相同的命中结果能够被保留。图 8-1 显示了 4 个命中结果，但是仅有上面的两个命中结果与基因组区域完全匹配，且与查询序列长度相同（长度 = 200，相同性 = 100%）。
4. 提取 BLAT 输出结果中最上面两个命中结果的以下信息:CHRO（染色体）、START（区域起始坐标）和 END（区域终止坐标），然后在 BED 格式文件中指定相关信息（见信息栏“数据格式”）。

i. 如果目标基因组位点可能位于指定区域的上游或下游，BED 文件中的起始或终止坐标可以在考虑染色体链的情况下进行相应调整。例如，在我们所举的例子中，要找到位于这两段区域的上游 1kb 以内的 CpG 岛时，你可以将位于+链上的区域起始坐标减去 1kb，并将位于一链上区域终止坐标加上 1 kb。修改后的 BED 文件如图 8-2 所示。

ii. 继续选择 “使用 UCSC 表浏览器可视化多段基因组区域”。详见 “疑难解答”。

```txt
chr7 99517108 99518307 transcript_1(-strand)
chr7 98843537 98844736 transcript_2(+strand)
```

图 8-2 修改后的包括了扩展区域的 BED 文件。被修改的部分由黑体字显示(彩图请扫封底二维码)。

## 使用 UCSC 基因组浏览器可视化一段基因组区域

5. 点击 “Genome” 标签直接进入基因组浏览器；图 8-3A 阐述了这个过程。

A

![](images/page_454_image_5.jpg)

B

图 8-3 运用 UCSC 基因组浏览器进行查询。（A）通过坐标、基因名或关键词搜索基因组区域；（B）通过关键词搜索返还的候选区域列表（彩图请扫封底二维码）。

i. 首先，选择一个参考基因组和草图（assembly）。请注意基因组是以一定的分割单位（clades）来组织的，并需要指定一个正确的基因组草图，因为在不同草图中坐标可能会发生改变。当选中一个基因组草图的时候，需要记住数据通道是与某个特定的基因组草图联系在一起的。因此，某些通道可能在一个旧的草图中存在，而在最新的草图中反而不存在，反之亦然。
ii.在“position or search term”框中指定基因组区域（如前一个例子中的“chr7:99517108-99518307”）；或者在“gene”框中指定基因名，如“MAPK1”。你也可以用一个关键词进行搜索，如“转座子”，然后一系列可能的基因组区域将被返回，你可以从中挑选一个进行可视化操作（图8-3B）。

6. 选择一个通道列表。通道被分成不同的组以反映这些数据和注释所包含的生物学信息。在上一个例子中，通过将 “display mode” 切换为 “full” 并点击 “refresh”，来打开 “Regulation” 组中的 “CpG islands” 通道。

## 定制通道

我们可以通过点击图 8-3A 所示的 “add custom tracks” 按钮来添加 UCSC 中不存在的包含数据和注释的定制通道。

定制通道可以被存为包括 BED 格式在内的多种格式（图 8-4A），并通过以下三种途径之一提交至 UCSC:将数据直接粘贴到窗口中、将数据上传至网络可访问的位置并将相应链接粘贴至窗口，或者上传一个本地文件（图 8-4A）。通过重复以上过程我们可以上传多个定制通道。定制通道管理器允许你显示、隐藏或者删除定制通道（图 8-4B）。定制通道的显示形式与 UCSC 的公共通道相同（图 8-4C）。

A Add Custom Tracks

![](images/page_455_image_3.jpg)

<details>
<summary>text_image</summary>

clade Mammal genome Human assembly Mar. 2006 (NCBI36/hg18)
Display your own data as custom annotation tracks in the browser. Data must be formatted in BED, bigBed, bedGraph,
GFF, GTF, WIG, bigWig, MAF, BAM or PSL formats. To configure the display, set track and browser line attributes as
described in the User's Guide. URLs for data in the bigBed and bigWig formats must be embedded in a track line in the
box below. Publicly available custom tracks are listed here. Examples are here.
</details>

![](images/page_455_image_4.jpg)

<details>
<summary>text_image</summary>

Paste URLs or data:
Or upload:
Browse...
Submit
track type=wiggle_0 name="Deep sequencing"
description="Example"
visibility=full color=24,116,205
chr1 8044125 8044126 24
chr1 8044126 8044127 23
... Number of reads piled on each region
Upload large data in BED format
including the track line
Header of the data (track line),
should be composed in one line
Clear
</details>

B Manage Custom Tracks

![](images/page_455_image_6.jpg)

<details>
<summary>text_image</summary>

genome Human assembly Mar. 2006 (NCBI36/hg18) [hg18]
Name Description Type Doc delete
Deep sequencing Example wiggle_0
add custom tracks
go to genome browser
go to table browser
</details>

![](images/page_455_chart_7.jpg)

<details>
<summary>histogram</summary>

| Nucleotide | Base Position (approx.) |
| --- | --- |
| C | 564890 |
| T | 564910 |
| G | 564920 |
| C | 564930 |
</details>

图 8-4 添加一个定制通道。（A）将用户信息存储为 BED 格式，设置通道类型为 “bedGraph” 并设置文件名、描述和颜色（RGB 形式，例如，红、绿、蓝，各数值范围均为 0～255），然后点击 “Submit”。（B）定制通道管理器显示了新上传的通道。点击 “go to genome browser” 按钮以返回至浏览器。（C）显示定制通道（彩图请扫封底二维码）。

## 使用 UCSC 表格浏览器可视化多个基因组区域

7. 让我们来继续之前那个在两段基因区域上游定位 CpG 岛的例子（步骤 4），

i. 在 UCSC 基因组浏览器的任意网页上，点击顶部面板上的 “Tables” 键，进入 UCSC 表格浏览器（Table Browser）（Karolchik et al. 2004）。
ii. 选定参考基因组和它的草图，在本例中应将 clade 选为 “Mammal”，将 genome 选为 “Human”，将 assembly 选为 “Mar. 2006”，并在 “Regulation” 组中选择 “CpG islands” 通道。图 8-5A 显示了最终的输出结果。

8. 点击 “define regions” 按钮以打开一个新的网页框（图 8-5B）。

i. 将两个之前被确定的区域以 BED 格式（如图 8-2 所示）粘贴至该网页框中，点击 “submit” 从而返回至表格浏览器。
ii. 为了在 UCSC 基因组浏览器上可视化与上述两个区域重叠的 CpG 岛，我们可以将“output format”设置为“hyperlinks to Genome Browser”，然后点击“get output”，将出现一个新的网页，该网页将显示与基因组区域重叠的 2 个 CpG 岛的超链接。

A

![](images/page_456_image_3.jpg)

<details>
<summary>text_image</summary>

Home Genomes Genome Browser Blat Tables Gene Sorter PCR Session FAQ Help
Table Browser
Use this program to retrieve the data associated with a track in text format, to calculate intersections between tracks, and to retrieve DNA sequence covered by a track. For help in using this application see Using the Table Browser for a description of the controls in this form, the User's Guide for general information and sample queries, and the OpenHelix Table Browser tutorial for a narrated presentation of the software features and usage. For more complex queries, you may want to use Galaxy or our public MySQL server. To examine the biological function of your set through annotation enrichments, send the data to GREAT. Refer to the Credits page for the list of contributors and usage restrictions associated with these data.
clade: Mammal genome: Human assembly: Mar 2008 (NCBI36/hg18)
group: Regulation track: CpG Islands manage custom tracks
table: copgIslandExt describe table schema
region: genome ENCODE Pilot regions position lookup define regions
identifiers (names/accessions): paste list upload list
filter: create
intersection: create
correlation: create
output format: hyperlinks to Genome Browser Send output to Galaxy GREAT
output file: (leave blank to keep output in browser)
file type returned: plain text gzip compressed
get output summary/statistics
</details>

B

![](images/page_456_image_5.jpg)

<details>
<summary>text_image</summary>

Enter region definition
Paste regions: Or upload file: Browse
chr7 99517108 99518307 transcript_1(-strand)
chr7 98843537 98844736 transcript_2(+strand)
submit clear cancel
</details>

![](images/page_456_image_6.jpg)

<details>
<summary>text_image</summary>

Hyperlinks to Genome Browser
CpG: 75 at chr7:99516705-99517638
CpG: 85 at chr7:98843721-98844795
</details>

图8-5 使用UCSC表格浏览器。（A）点击“Table”键进入表格浏览器；在下拉选项中设置clade、genome、group、track、output format等选项。点击“define regions”以指定多个基因组区域的信息。（B）将如图8-2所示的形式的两段区域的信息粘贴至网页对话框中，点击“Submit”。（C）与（B）中区域重叠的CpG岛在UCSC Genome Browser中以超链接的形式显示（彩图请扫封底二维码）。

9. 选择另外一种 “output format” 来保存两个 CpG 岛，用于进一步分析。例如，你可以选择 “BED-browser extensible data” 格式，并指定一个文件名称，将 CpG 岛以文本文件的形式下载下来，随后你可以将这些文本文件作为定制通道重新上传至 Genome Browser 中。

## 检索多序列比对与保守评分

10. 与“使用UCSC基因组浏览器可视化一段基因组区域”一节中查看通道的方法类似，我们可以通过设置“Comparative Genome”组中的“Conservation”通道查看某段区域的保守区域。

i. 点击 “Comparative Genomics” 组中的 “Conservation” 链接（图 8-6A）。在结果页面上（图 8-6B），将 “Maximum display mode” 设置为 “full”，并调整 “Multiz Alignments” 和 “Element Conservation（phastCons）” 为 “full”。
ii. 点击图 8-6B 中青色圈标记的加号来选中全部的三个进化枝（clade）。
iii. 选择红色框所标记的 “No codon translation” 来查看基因组 DNA 序列；否则，由序列翻译得到的氨基酸序列也将被显示。
iv. 如图 8-6C 所示，在页面的底部，点击红色圈标记的加号标志选中所有物种，然后点击 “Submit”。

B

![](images/page_457_image_3.jpg)

<details>
<summary>flowchart</summary>

This image displays a hierarchical tree structure for vertebrate conservation, showing the relationships between species selection, placental mammal groups, and vertebrates.
</details>

![](images/page_457_image_4.jpg)

<details>
<summary>text_image</summary>

UCSC Genome Browser on Human Mar. 2006 (NCBI36/hg18) Assembly
move << << < >> >> zoom in 1.5x 3x 10x base zoom out 1.5x 3x 10x
position/search chrX:151,073,054-151,383,976 gene jump clear size 310,923 bp. configure
Move start
< 2.0 >
Track search default tracks default order hide all add custom tracks configure reverse refresh
collapse all Use drop-down controls below and press refresh to alter tracks displayed. Tracks with lots of items will automatically be displayed in more compact modes.
Mapping and Sequencing Tracks refresh
Phenotype and Disease Associations refresh
Genes and Gene Prediction Tracks refresh
mRNA and FST Tracks refresh
Expression refresh
Regulation refresh
Comparative Genomes refresh
Conservation 28-Way Cons 28-Way Base Cons 28-Way Most Cons 17-Way Cons 17-Way Most Cons
hide hide hide hide hide hide hide
Cons Indels MmCF Tetraoden Ecores Chimp Chain/Net Orangutan Chain/Net Rheaus Chain/Net Mannosech Chain/Net hide
hide hide hide hide hide hide hide hide
Guinea pig Chain/Net Rat Chain/Net Mouse Chain/Net Dog Chain/Net Cat Chain/Net Horse Chain/Net hide hide hide hide hide hide hide hide hide hide hide hide hide hide
hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide hide Hide
</details>

![](images/page_457_image_5.jpg)

<details>
<summary>text_image</summary>

Select subtracks by clade:
Clade	Primate	Mammal	Vertebrate
List subtracks: ○ only selected/visible ● all (4 of 10 selected)
✓ Primate Cons	Primate Basewise Conservation by PhyloP	schema
✓ Mammal Cons	Placental Mammal Basewise Conservation by PhyloP	schema
✓ Vertebrate Cons	Vertebrate Basewise Conservation by PhyloP	schema
✓ Primate Cons	Primate Conservation by PhastCons	schema
✓ Mammal Cons	Placental Mammal Conservation by PhastCons	schema
✓ Vertebrate Cons	Vertebrate Conservation by PhastCons	schema
✓ Primate El	Primate Conserved Elements	schema
✓ Mammal El	Placental Mammal Conserved Elements	schema
✓ Vertebrate El	Vertebrate Conserved Elements	schema
✓ Multiz Align	Multiz Alignments of 44 Vertebrates	schema
4 of 10 selected
Submit
</details>

C

图 8-6 设置 “Conversation” 通道的步骤。（A）点击 “Comparative Genomics” 组中的 “Conservation” 链接。（B）将 “Maximum display mode” 设置为 “full”（如红色圈所示），并将 “Multiz Alignments” 和 “Element Conservation（phastCons）” 均设置为 “full”，将 “Basewise Conservation（phyloP）” 和 “Conserved Elements” 均设置为 “hide”。点击青色圈标记的加号标志，这样就可以把三个进化枝中的所有 44 种脊椎动物物种均包括到多序列比对中。将某物种之前的勾取消会使该物种的序列不参与多序列比对。（右）系统发育树显示了这些物种之间的进化关系。在红色框所标记的 “Codon Translation” 部分选择 “No codon translation”，这样可以让 Browser 显示基因组 DNA 序列。由于蛋白质序列比编码区的 DNA 序列更为保守，所以选择除此之外的其他三个选项以显示翻译得到的氨基酸序列也非常有用。（C）在 “Select subtracks by clade” 部分，点击 “+” 使所有 PhastCons 和 MultiZ 的子通道均显示，然后点击 “Submit” 以显示图 8-7A 所示的保守通道（彩图请扫封底二维码）。

11. 图 8-7A 显示了保守区域和序列比对通道。前三个通道 “Primate Cons”、“Mammal Cons” 和 “Vertebrate Cons” 代表了这些进化枝之间的序列保守性。图中的峰越高，说明保守性越强。请注意外显子是高度保守的，并在内含子和基因间区内存在一些额外的保守区域。

i. 红色框标记的区域显示各物种和人类之间的序列比对情况。点击该区域将显示该基因组区域的多序列比对情况。多序列比对结果被分为不同的模块（“blocks”），每个模块（block）代表了一段高度保守的区域。图 8-7B 显示了其中一个例子。
ii. 点击每个物种开头的 “B” 来浏览该物种被比对的区域，点击 “D” 来检索相应的 DNA。

![](images/page_458_chart_6.jpg)

<details>
<summary>manhattan</summary>

| Gene | Primate Cons. (Range) | Mammal Cons. (Range) | Vertebrate Cons. (Range) |
| --- | --- | --- | --- |
| MMP1 | 0~1 | 0~1 | 0~1 |
| MMP2 | 0~1 | 0~1 | 0~1 |
| MMP3 | 0~1 | 0~1 | 0~1 |
| MMP4 | 0~1 | 0~1 | 0~1 |
| AAG12 | 0~1 | 0~1 | 0~1 |
| Chimer | N/A | N/A | N/A |
| Genit | N/A | N/A | N/A |
| Oregutans | N/A | N/A | N/A |
| Rhesus | N/A | N/A | N/A |
| Mamosei | N/A | N/A | N/A |
| Taripae | N/A | N/A | N/A |
| Mouse_embu | N/A | N/A | N/A |
| Bulkedo | N/A | N/A | N/A |
| Tric_thermii | N/A | N/A | N/A |
| Mouse | N/A | N/A | N/A |
| Ral | N/A | N/A | N/A |
| Kangaroo_ra | N/A | N/A | N/A |
| Gurrera_ea | N/A | N/A | N/A |
| Spathe | N/A | N/A | N/A |
| Rasps | N/A | N/A | N/A |
| Pks | N/A | N/A | N/A |
| Aspaca | N/A | N/A | N/A |
| Dditga | N/A | N/A | N/A |
| Cox | N/A | N/A | N/A |
| Hopoei | N/A | N/A | N/A |
| Cat | N/A | N/A | N/A |
| Doj | N/A | N/A | N/A |
| Microtia | N/A | N/A | N/A |
| Megabot | N/A | N/A | N/A |
| Hippodermes | N/A | N/A | N/A |
| Shirea | N/A | N/A | N/A |
| Ephaeae | N/A | N/A | N/A |
| Rock_pyratae_Tefreci | N/A | N/A | N/A |
</details>

![](images/page_458_image_7.jpg)

<details>
<summary>text_image</summary>

B Alignment block 37 of 175 in window, 153666676 - 153666649, 74 bps
B D Human CTGCAGCTC--GGG--GCTTCG--CTAGGAGCTGACTGAGCCATACTTGCCACTCG--Cct
B D Chimp CTGCAGCTC--GGG--GCTTCG--CTAGGAGCTGACTGAGCCATACTTGCCACTCG--Cct
B D Gorilla CTGCAGCTC--GGG--GCTTCG--CTAGGAGCTGACTGAGCCATACTTGCCACTCG--Cct
B D Orangutan CTGCAGCTC--GGG--GCTTCG--CTAGGAGCTGACTGAGCCACACTTGCCACTCG--Cct
B D Rhesus CTGCAGCTC--GGG--GCTTCG--CTAGGAGCTGACTGAGCCACACTTGCCACTCG--Cct
B D Marmoset CTGCAGCTC--GGG--GCTTCG--CTAGGAGCTGACTGAGCCACACTTGCCACTCG--Cct
B D Tarsier CTGCAGCTC--GGG--GCTTCG--CTGGCAGCCGACTGAGCCACACTTGCCACTCG--Cct
B D Mouse lemur CTACACCTT--GGC--CGCTCC--CTCGCAGCTGACTGAGCCACACTTGCCACAC--Cct
B D Bushhacy CTGCAGCTT--GGC--GCCATG--GT--GGAGCTGACTGAGCCACACTCGCACCA--Cc
B D Tree shrew CTGCAGCTC--GGG--GCTTCA--CTCGGAGCAGACTGAGCCACACTTGCCACTCG--Cct
B D Mouse CTGCAACTT--GGT--GCTTCA--CTTGGAGCAGAGTGAGCCACGCTTGCCACTCT--Cct
B D Kangaroo rat ===================_
B D Guinea pig CTGCAGCTT--GGA--GCTTCA---CTCGCAGCAGACTGAGCCACGCTTGCCACTCG--Cct
B D Squirrel CTGCAGCTT--GGC--GCTTCA---CTTGGAGCAGATTGAGCCACACTTGCCACTCG--Cct
B D Pakbit CTGCAGCTT--GGC--GCTTCA---CTTGGCGCAGACTGTGGCGACACTTGCCACTCG--Cct
B D Fika CAGCGCATC--CGC--GCTTCA---CTTGGAAATTCATTGAGCC CACTTTCCACTCC--Cc
B D Alpaca CTGCAGCTC--GGA--GCTTCG---CTAGGGGTGGACCGAGCCACACTTGCCACCCCG--Cct
B D Dolphin CTGCAGCTC--GGS--GCCCA---CTCGGAGCAGACTGAGCCCCGCTCGCCACCGC--
B D Cov CTGCAGCTA--GGC--GCCCA---CTTGGAGCAGAAATGGCCCCACACTCGCCACTCG--Cct
B D Horse CTGCAGCTT--GGC--GCTTCG---CTTGGACGTACTGAGCCACACTTGCCACTCG--Cct
B D Cat ===================_
B D Dog CTGCAGCTC--GGC--GCCCG---CTCGCGCGCGACTCGCGCGCGCTCGCCACCGC--Cct
B D Microbat CTGCAGCTC--GGC--GCTTCA---CTTGGACCA GAC T GAC CCAC ACT CGCCACCGT--Cct
B D Megabat CTGCAGCTC--GGC--GCTTCG---CTTGGACCA GAC T GAC CCAC ACT TGCCACTCG--Cct
B D Shrew CTGCAGCTT--GGC--GCTTCA---CTTGGACCA GAC T GAC CCAC ACT TGCCACTCG--Cct
B D Elephant CTGCAACTT--GGC--GCTTCA---CTTGGACCA GAC T GAC CCAC ACT TGCCACTCG--Cct
B D Rock hyrax CTGCAACTC--GGC--GACTCG---CTTGGACCA GAC T GAC CCAC ACT TGCCACACG--Cct
B D Tonrec CTGCAGCTC--GGA--GCTTCA---CTTGGACCCA GAC T GAC CCAC ACT TGCCACTCG--Cct
B D Arnadillo CTACAGCTT--GGC--GCTTCA---T TGGACCA GAC T GAC CCAC ACT TGCCACTCG--Cct
B D Opossum CTGCAGCTC--GGC--GAATCCGCCGAATGTGGTACTGGGCCACACTCGCCACTCG--Cct
B D Platypus CTGCAGCTC--GGA--GCTTCG---CTGGGA GAC T GAC GCCCATGT GCCCACCGT-
B D Chicken CTGCAGCTC--TGG--GCTTCG---CTCTGA GTGGTTGTTC CCTTTGCCACAC G-
B D Lizard CTGCAGCTC--TGG--GCTTCG---GTGGGTGTCC CCTGTGGTTGT CCTTTGCCAACAC G-
B D X. tropicalis CTACAAC TGTGTGA-TTC TGA-TTT GTT- ACT GGA-GTTGCCAC AC G-
B D Tetraodon CTGCAGGAC-TGG- CTGCC TC-TCTG-GCCTTGTT TACT GGT CCTGT CCT-
B D Pugu CTACA-AC-TGCC CTC TTT- CTC-TTT GTTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT TTT<nl>B D Stiokleback CTGCAGCAC-TGA-CGCCGC TC-TCT-G-TT CCTGT TT TG CCCCACC CTC-
B D Medaka CTACAAGAC-GGG-TTC CCC CTT-TGT-G-TT CCTGT TT TG CCTGT CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTC CTA<nl>B D Zebrafish CTGCAGCAC-TATCC AGTTC- CGTG-TT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GTT CCTT GGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CCTGT CTA<nl>
</details>

图 8-7 保守和比对通道。（A）显示图 6 中所设置的保守通道。（B）某段保守区域序列比对示图（即模块），由点击 A 中的红色框得到。破折号表示空位（插入或缺失）。点击窗口左侧的 “B” 来浏览该物种的相应区域，点击 “D” 来检索其 DNA 序列。请注意某些物种的基因组数据并未储存在 UCSC 基因组浏览器中（彩图请扫封底二维码）。

12. 要得到多个物种的大区域的保守得分和的多序列比对结果，请前往 UCSC 表格浏览器，根据 “使用 UCSC 表格浏览器可视化多个基因组区域” 中的指示进行操作。

i. 此时将 group 设置为 “Comparative Genome”，将 track 设置为 “Conservation”，然后将 table 设置为 “Multiz Align（multiz 44 way）”。

ii. 在本例中，使用图 8-5B 中所示的相同区域。

iii. 将输出格式选择为 “MAF multiple alignment format”，并提供文件名（如 “download.txt”）用于输出结果。

iv. 点击 “get output” 将输出结果保存在本地文件中。该结果文件中包括了所有含有或部分含有所指定区域的保守区信息。

v. 使用如下 UNIX 指令，基于 MAF 文件来格式化序列比对和保守分值:

```txt
awk -F"+"" {if($1=="a") {a++; print"\nBlock"a"\t"$2; } if($1=="s")
{split($2, token, ".");print token[1]\t"token[2]\t"$3"\t"$4"\t"$5"\t"$7;} }'
download.txt > conservation.xls
```

如果您是 Windows 用户，请安装 Cygwin 来运行以上指令。该指令将产生一个名为 “conservation.xls” 的文件。

vi. 使用 Excel 打开 conservation.xls 文件，如图 8-8 所示。

![](images/page_459_image_11.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  Block_2["Block 2"] --> score569425000000["score=569425.000000"]
  hq18["hq18"] --> chr7["chr7"]
  echTell1["echTell1"] --> scaffold_312536["scaffold_312536"]
  calJac1["calJac1"] --> Contig60["Contig60"]
  rheMac2["rheMac2"] --> chr3["chr3"]
  ponAbe2["ponAbe2"] --> chr7["chr7"]
  qorGor1["qorGor1"] --> Supercontiq_0006866["Supercontiq_0006866"]
  panTro2["panTro2"] --> chr7["chr7"]
  micMur1["micMur1"] --> scaffold_2556["scaffold_2556"]
  otoGar1["otoGar1"] --> scaffold_82111["scaffold_82111"]
  tupBell1["tupBell1"] --> scaffold_142981["scaffold_142981"]
  rn4["rn4"] --> chr12["chr12"]
  mm9["mm9"] --> chr5["chr5"]
  dipOrd1["dipOrd1"] --> scaffold_9623["scaffold_9623"]
  cavPor3["cavPor3"] --> scaffold_30["scaffold_30"]
  speTri1["speTri1"] --> scaffold_151296["scaffold_151296"]
  vicPac1["vicPac1"] --> scaffold_10517["scaffold_10517"]
  bosTau4["bosTau4"] --> chr25["chr25"]
  turTru1["turTru1"] --> scaffold_89700["scaffold_89700"]
  equCab2["equCab2"] --> chr13["chr13"]
  felCat3["felCat3"] --> scaffold_8533["scaffold_8533"]
  canPam2["canPam2"] --> chr6["chr6"]
  pteVam1["pteVam1"] --> scaffold_2197["scaffold_2197"]
  proCap1["proCap1"] --> scaffold_42972["scaffold_42972"]
  loxAfr2["loxAfr2"] --> scaffold_11078["scaffold_11078"]
  choHof1["choHof1"] --> scaffold_69270["scaffold_69270"]
  dasNov2["dasNov2"] --> scaffold_103333["scaffold_103333"]
  monDom4["monDom4"] --> chr2["chr2"]
  G---C---AGTGGCACAGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGATACGGACAT---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CTGTCTCACC----G---CAGTGGCACAGACACCA---CCCC---TTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---AGCGGCACAGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACAGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACAGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACAGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACGACACCA---CCCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACGACTACCA---CCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACGACTACCA---CCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACGACTACCA---CCC---CTTCCCCGGC---GA-CCACAGCCT---CCGTCTCACC----G---CGTGGCACGACTACCA---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC :--CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---CTTCCCCGGC ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA ---CCC ---ACTCCGCACGCAGTCGTGCCTCA ---CTCACAGGA ---GC-CTGGAGCCTGGAGCAGTGTC----G---CGTGGCACGACTACCA ---CCC ---ACTCCGCACGCAGTCGTGCCTCA ---CTCACAGGA ---GC-CTGGAGCCTGGAGCAGTGTC----G---CGTGGCACGACTACCA ---CCC ---ACTCCGCACGCAGTCGTGCCTCA ---CTCACAGGA ---GC-CTGGAGCCTGGAGCAGTGTC----G---CGTGGCACGACTACCA :--ACTCCGCACGCAGTCGTGCCTCA ---CTCACAGGA ---GC-CTGGAGCCTGGAGCAGTGTC----G---CGTGGCACGACTACCA :--ACTCCGCACGCAGTCGTGCCTCA ---CTCACAGGA ---GC-CTGGAGCCTGGAGCAGTGTC----G---CGTGGCACGACTACCA :--ACTCCGCACGCAGTCGTGCCTCA ---CTCATCACAA ---GC-CTGGAGCCTGGAGCAGTGTC----G---CGTGGCACGACTACCA :--ACTCCGCACGCAGTCGTGCCTCA ---CTCATCACAA ---GC-CTGGAGCCTGGAGCAGTGTC----G---CGTGGCACGACTACCA :--ACTCCGCACGCAGTCGTGCCTCA ---CTCATCACAA ---GC-CTGGAGCCTGGAGCAGTGTR----G---CGTGGCACGACTACCA :--ACTCCGCACGCAGTCGTGCCTCA ---CTCATCACAA ---GC-CTGGAGCCTGGAGCAGTGTR----G---CGTGGCACGACTACCA :--ACTCCGCACGCAGTCGTGCCTCA ---CTCATCACAA ---GC-CTGGAGCCTGGAGCAGTGTR----G---CGTGGCACGACTACCA :--ATAA :--CGTGGCACGACTACCA ---CCC ---ACTTCGCCCG ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA :--ATAA :--CGTGGCACGACTACCA ---CCC ---ACTTCGCCCG ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACGACTACCA :--ATAA :--CGTGGCACGACTACCA ---CCC ---ACTTCGCCCG ---GA-CCACAGCCT ---CCGTCTCACC----G---CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGGCACU :--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT:--CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::+ CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CGTGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::—CS TGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGTGAT::+ CGYGTAIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIii
  C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -- C -.-> CGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAG TAG
```
</details>

图 8-8 由 download.txt 中提取保守模块信息，由 Microsoft Excel 进行查看。在每个模块中，各列的含义依次如下:基因组草图（genomic assembly）、染色体、起始坐标、长度、基因组链及序列比对。注意，如果基因链为 “-”，则用于比对的位置和比对结果都是由参考基因组的反向互补序列计算得到的。换言之，以上位置是由基因组模板链的 3' 端开始计算位置得到的（彩图请扫封底二维码）。

![](images/page_459_image_13.jpg)

## 疑难解答

问题（步骤 1）:使用 BLAT 后没有任何命中结果。

解决方案:BLAT 虽然运作迅速，但其敏感性是有限的（详见信息栏“算法、门户网站和方法”）。为了找到具有较高敏感性的命中结果，你可以使用 BLAST（见方案 2），然后将 BLAST 的结果存为 FASTA 格式，以便与本方案中其他步骤保持一致。

问题（步骤 4）:坐标信息来自不同版本的基因组。

解决方案:保持坐标值与基因组草图一致非常重要。如果你想要在两个草图之间切换坐标，请使用 UCSC 基因组浏览器提供的 LiftOver 工具（http://genome.ucsc.edu/cgi-bin/hgLiftOver)。你只需要将 BED 格式的坐标信息粘贴或上传，然后选中原始的基因组草图和新的基因组草图，点击 “submit”，将新的坐标保存用于其他用途。

![](images/page_460_image_3.jpg)

## 讨论

本方案仅介绍了UCSC基因组浏览器可提供的诸多功能中的非常小的一部分。UCSC基因组浏览器在各网页上提供了详细的帮助信息，同时还提供许多非常优秀的教程。这个网站同时还提供一些分析工具。然而，在表格浏览器得到的数据，统计分析最为完善。基于网页的工作平台Galaxy（Giardine et al. 2005）则提供了很多工具，可用于分析由UCSC表格浏览器（Goecks et al. 2010）中获得的基因组数据。此外，用户在电脑上安装了MySQL客户端库后，可以直接存取UCSC基因组浏览器之下的MySQL关系型数据库(http://www.mysql.com/)。与任何通道相关的数据可以通过MySQL下载，或者通过http://hgdownload.cse.ucsc.edu/downloads.html直接下载。

## 网络资源

Cygwin http://www.cygwin.com/

Ensembl http://ensembl.org

MySQL http://www.mysql.com/

NCBI relational database http://www.ncbi.nlm.nih.gov

UCSC Genome Browser http://genome.ucsc.edu/

## 序列比对和同源性检索简介

序列比对算法的目的是试图把一系列蛋白质或 DNA 序列进行整理，使得由共同祖先进化而来的核苷酸或氨基酸得到对齐。这些算法属于最早被开发，也是在生物信息学应用中被经常使用的算法。将一组序列对准，使得检测和度量序列相似性（similarity）变得更为容易，而相似性则是衡量由同一祖先进化而来所产生的同源性（homology）的良好标准，同时，相似性也是相似生物学功能的良好指标。在数据库中搜索同源物（homologs）是对一种新发现的基因或蛋白质进行注释的第一步。同源物（homologs）是指与进化祖先相关的基因，包括直系同源物（orthologs）和旁系同源物（paralogs）。所谓直系同源物，是指在物种形成过程中由一个共同始祖基因进化但位于不同物种中的一组基因；而旁系同源物是指位于相同基因组中由于复制产生的一组基因。

基于对分子进化过程的一些简化假设，一些算法可以用于寻找两个给定序列之间的最优对准。这些算法就是所谓的动态规划算法（dynamic programming algorithm）的实例，其运行时间正比于两个序列的长度之积。然而在实际运行中，对一个大型序列数据库运行动态规划算法可能会慢得令人无法忍受。

动态规划算法是一种用于解决可以被分割为一系列较小子问题的问题且该问题可被递归方式解决的算法。一个动态规划算法的例子就是通过将之前的数字（如 n-1，n-2）进行加和来计算斐波那契数列（Fibonacci sequence）的第 n 个数字。

因此，为了对日益增长的序列数据库进行有效搜索，一种叫做 BLAST（Basic Local Alignment Search Tool）的算法被开发（Altschul et al. 1990）。作为启发式算法（heuristic algorithm), BLAST 是以损失由严格动态规划方法获得最优对准为代价, 来保证很好的运行时间优势 (即运行更快、时间更短)。BLAST 首先在查询序列和目标序列之间寻找一对短小且相似的子序列 (种子, seed), 然后在不允许空位 (gap) 的情况下进行延伸。当相似子序列延伸达到足够长时, BLAST 将进行一次全长的存在空位的比对 (gapped alignment)。BLAST 忽略了数据库中没有与查询序列相似子序列的序列, 从而极大地提高了它的运行速度。此外, 基于序列相似性, BLAST 运用精心设计的统计方法, 来量化数据库中的序列与查询序列之间的同源性。

设计用于寻找最优解的算法通常需要大量的计算资源和时间，启发式算法（heuristic algorithm）则以牺牲一定程度的准确度为代价，通过一个连续渐进的过程，采用时间上经济的方法来搜索一种合理可行的解决方法。在一个精心设计的连续过程中，启发式算法可以找到非常好的解决方法，甚至可以找到最佳结果，但是这种算法通常无法确定或证明所找到的方法是最佳解决方法。

作为一种局部比对算法（local alignment algorithm），BLAST 识别两段序列之间相似性区域时，并不对不配对的延伸区段（overhangs）进行罚分。相反，全局比对算法（global alignment algorithm）则试图对全长的输入序列进行比对。

由于蛋白是模块化的，可能包含多个作为功能单位的结构域，在这种情况下，局部比对及其统计方法通常是搜索同源性的最适宜的方法。不同类型的 BLAST 被用于不同的用途（表 8-1）。例如，BLASTn 用于比对两个核酸序列，BLASTp 用于比对两个蛋白质序列，而 tBLASTn 则使用一段蛋白质序列对翻译后的核酸序列数据库进行查询。由于密码子的冗余性（61 个密码子对应 20 个氨基酸），所以对检测同源物来说，蛋白质比对的敏感度要比核酸比对更高。

表 8-1 几种 BLAST 方法的总结

| 算法 | 查询序列 | 目标序列 | 特征 | 备注 |
| --- | --- | --- | --- | --- |
| blastn | 核酸 | 核酸 |  |  |
| megablast | 核酸 | 核酸 | 所有查询序列被连接为一个序列,所有的命中结果最后统一进行解析和分析 | 当对大量查询序列进行搜索时速度快于 blastn |
| blastp | 蛋白质 | 蛋白质 |  |  |
| PSI-BLAST | 蛋白质 | 蛋白质 | PSI-BLAST 的首次迭代只是简单的 blastp,对每个查询序列,得到的比对后的序列被用于建立一个位点特异性得分矩阵。该矩阵被用于在第二次迭代中搜索目标,如果得到的命中结果多于第一次迭代,则矩阵将被更新。迭代将一直进行直至没有更多新的命中结果 | 在寻找远源同源蛋白时敏感性远远强于 blastp |
| tblastn | 蛋白质 | 核酸 | 目标序列首先通过 6 种可读框被翻译为蛋白质序列,然后查询序列与翻译后的目标序列进行比对 | 寻找蛋白质水平上的同源物;敏感性强于 blastn |
| blastx | 核酸 | 蛋白质 | 查询序列首先通过 6 种可读框被翻译为蛋白质序列,然后与目标序列进行比对 | 同上 |
| tblastx | 核酸 | 核酸 | 查询序列和目标序列均通过 6 种可读框被翻译为蛋白质序列,然后将翻译后的查询序列与翻译后的目标序列进行比对 | 同上;所有算法中运行速度最慢 |

当我们拥有来自多个物种的同源序列时, 我们通常希望能够将这些序列全部进行比对, 因为这样就能对保守性进行更为准确的评估。对多个序列进行比对同时也是建立系统发育树的关键步骤之一。不幸的是, 多重序列比对 (multiple sequence alignment, MSA) 的算法为了保证得到最佳结果, 其运行时间随序列总数呈指数型增长 (见信息栏中 “算法、门户网站和方法” 一节)。为了节省计算时间, 以 ClustalW (Higgins and Sharp 1988; Thompson et al. 2002) 为例的启发式算法, 根据系统发育树, 以逐步优化方式合并最佳对准, 来渐进实现多序列比对。

目前人们仍在努力根据蛋白质的功能域将蛋白质分为不同的家族，这些功能域是指具有特异性催化位点或结合界面的保守模块。被分类的蛋白家族被储存在数据库中，对这些数据库进行搜索可以发现某种新蛋白属于哪个蛋白家族。该策略要比使用 BLAST 对未分类的数据库进行搜索更为敏感。此外，蛋白家族数据库可以提供已经被分类的蛋白家族的多序列比对结果。

## 蛋白家族数据库

许多蛋白质的结构区域和功能区域（如功能域）可以在其他蛋白质或者其他物种的蛋白质中被发现。具有相似结构或功能域的蛋白质很可能具有相同的功能，因此可以被分类至同一蛋白家族。这些蛋白家族中的蛋白质由于具有相同的结构域而具有特异的序列谱（specific sequence profiles）。这些序列谱（profiles）可以通过系统的BLAST结果进行收集，也可以通过分类后的数据进行人工收集。根据每个序列谱可以设计概率模型（probabilistic models）来优化蛋白家族的分类。目前，有许多网络数据库在运用、储存并提供这些信息，如Pfam（http://pfam.sanger.ac.uk/）（Sonnhammer et al. 1998）、Prosite（http://expasy.org/prosite/）（Sigrist et al. 2002）、SCOP（http://scop.mrc-lmb.cam.ac.uk/scop/）（Lo Conte et al. 2000）、CATH（http://www.cathdb.info/）、InterPro（http://www.ebi.ac.uk/interpro/）（Apweiler et al. 2001）和CDD（http://www.ncbi.nlm.nih.gov/cdd）（Marchler-Bauer et al. 2011）。

## 网络资源

```txt
CATH http://www.cathdb.info/
CDD http://www.ncbi.nlm.nih.gov/cdd
InterPro http://www.ebi.ac.uk/interpro/
Pfam http://pfam.sanger.ac.uk/
Prosite http://expasy.org/prosite/
SCOP http://scop.mrc-lmb.cam.ac.uk/scop/
```

## 方案 2 使用 BLAST 和 ClustalW 进行序列比对和同源性检索

本方案叙述了使用 BLAST 对序列数据库进行搜索的步骤，BLAST 主要对查询序列和数据库中的各目标序列进行序列两两比对。在此之后，本方案还叙述了使用 ClustalW 进行多序列比对的步骤。Argonaute 2（Ago2）蛋白是果蝇中小干扰 RNA（siRNA）介导的 RNA 干涉（RNA interference）中的基本组成部分。本方案以 Ago2 蛋白为例来演示如何使用 BLAST 在果蝇蛋白组中搜索所有 Ago2 蛋白的旁系同源物，并用 ClustalW 对搜索得到的序列进行多序列比对。

![](images/page_463_image_2.jpg)

## 材料

## 仪器

BLAST (http://blast.ncbi.nlm.nih.gov/)

ClustalW (http://www.ebi.ac.uk/Tools/msa/clustalw2)

具有 Internet 连接和网页浏览器的电脑

Java virtual machine (JVM)

本方案中介绍了被称为 Jalview 的序列比对编辑器，其运行需要电脑上安装了 JVM。请从 java 官方网站（http://www.java.com/en/download/index.jsp）上下载最新版本的 JVM。

![](images/page_463_image_10.jpg)

## 方法

## 使用 BLAST 在果蝇蛋白组中搜索一个蛋白序列

1. 获取示例蛋白 Ago2 的氨基酸序列，存为 FASTA 格式（见方案 1 和信息栏 “数据格式”）。

i. Ago2 是目前已进行深入研究的蛋白质，其序列可以通过在 NCBI 数据库（Sayers et al. 2009）中搜索它的蛋白质名称得到。登录 NCBI 主页（http://www.ncbi.nlm.nih.gov/），选择 “Protein” 进行搜索，在搜索框中输入 “fly Ago2”，然后点击 “Search”。

ii. 我们本次搜索的结果页面显示了 16 个命中结果，其中一个为 Ago2 的亚型 C，它具有 1217 个氨基酸。点击该命中结果的 “FASTA” 链接以得到它的 FASTA 格式的蛋白质序列。

2. 登录 http://blast.ncbi.nlm.nih.gov/Blast.cgi，选择 “protein blast”（如图 8-9A 中蓝色圈所标记），将出现一个新的页面（如图 8-9B 所示）。

i. 将步骤 1 中得到的 Ago2 亚型 C 的序列粘贴至第一个框中。

ii. 选择 “Reference proteins (refseq\_protein)” 数据库，在 Organism 一栏中输入 “Drosophila melanogaster”, algorithm 一栏选择 “blastp (protein-protein BLAST)”, 然后点击 “BLAST”。

iii. PSI-BLAST 通过迭代运行 BLAST 来找到远源同源物（Altschul et al. 1997）。PSI-BLAST 的初次迭代仅是简单的 BLASTp，并基于某个显著性阈值来选择与检索序列显著性高的目标序列，这些序列被用于建立一个位点特异性记分矩阵 [position-specific scoring matrix，亦称序列谱（sequence profile）；见方案 7]。该序列谱将被用于对数据库进行第二次迭代搜索，如果得到比第一次迭代多的结果，则该序列谱将被更新。迭代将一直进行，直至没有更多新的命中结果出现。使用 PSI-BLAST 时，请将算法选择为“PSI-BLAST(Position-Specific Iterated BLAST)”，然后点击 “BLAST”。