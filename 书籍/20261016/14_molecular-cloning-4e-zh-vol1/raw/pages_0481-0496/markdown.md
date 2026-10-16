## 2. 登录 Babelomics 网站（http://babelomics.bioinfo.cipf.es/）

i. 点击 “Upload data”，如图 8-17 所示。

![](images/page_480_image_4.jpg)

<details>
<summary>text_image</summary>

BABELOMICS
gene expression and functional profiling analysis suite
Upload data
Processing data
Expression
Genomic
Functional analysis
Utilities
Upload data
Select format
View by Data type: Microarray - Expression - One-channel - Affymetrix
Microarray
Expression
One-channel
Affymetrix
Agilent
GenePix
Two-channels
Agilent
GenePix
Data matrix
Expression
SNP
ID list
Gene
Transcript
Protein
SNP
Functional terms
Ranked
Annotation
Gene vs annotation
Extended annotation
Other
Newick
Blast
Interaction
Genotype (PED and MAP zip-filed)
Plink association
Accept
List
a list
</details>

图 8-17 Babelomics 数据上传窗口。点击 “Browse” 上传名为 cMyc.zip 的数据文件。将格式选择 “Affymetrix”，在弹出的 “Select format” 面板中点击 “Accept”，然后将数据名设置为 “cMyc\_raw\_data”。点击 “Upload” 上传文件（彩图请扫封底二维码）。

ii. 上传 cMyc.zip 文件后，点击 “Select format”，选择 “Microarray” → “Expression” → “One-channel” → “Affymetrix”，然后在弹出面板中点击 “Accept”。
iii. 将数据名设置为 “cMyc\_raw\_data”。
iv. 点击 “Upload” 来提交文件，等待确认过程完成。所有提交的数据都被列在 “Data list” 面板中。

3. 在数据上传完成后，“Data list”面板中数据状态将变为“valid”。

i. 为了在标准化之前对原始数据的表达强度进行检查，点击 “Utilities” 页面中的 “Microarrayraw-data plot” 链接。
ii. 在链接的页面中，点击 “browse server”，选择 “Uploaded data” → “cMyc\_raw\_Data”，然后点击 “Accept”。
iii. 将作业名设置为 “CMyc\_original\_boxplot”，然后点击 “Run”。
iv. 当作业完成后，在 “Job list” 面板中点击它，然后点击 “Box-plots” 链接来查看如图 8-18 所示的箱型图（box plots）。

每个箱型图都显示了一个样本的概要统计（summary statistics），图中箱型包含了中间 50% 的数据，箱型的上边缘（下边缘）表示了数据的第 75（25）百分位的数据，垂直的线条表示了最大值和最小值。我们可以看到在本例中的 8 个数据集具有不同的强度分布。

![](images/page_481_chart_2.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 |
| --- | --- | --- | --- |
| G1 | ~6.5 | ~7.5 | ~8.0 |
| G2 | ~6.5 | ~7.5 | ~8.0 |
| G3 | ~6.5 | ~7.5 | ~8.0 |
| G4 | ~6.5 | ~7.5 | ~8.0 |
| G5 | ~6.5 | ~7.5 | ~8.0 |
| G6 | ~6.5 | ~7.5 | ~8.0 |
| G7 | ~6.5 | ~7.5 | ~8.0 |
| G8 | ~6.5 | ~7.5 | ~8.0 |
| G9 | ~6.5 | ~7.5 | ~8.0 |
</details>

图 8-18 点击 “Job list” 面板中的 “CMyc\_original\_boxplot”，然后点击 “Box-plots” 来查看 8 个样本的探针强度的箱型图，如绿色矩形中所示。每个箱型都代表了第一个分位数（第 25 百分位的数据或 Q1；箱型的底部线条）、第二个分位数（第 50 百分位的数据，即中位数，箱型种间的水平线）和第三个分位数（第 75 百分位的数据或 Q2，箱型的顶部线条）。两端线条代表了排除异常值后数据中的最大值和最小值。线条末端之外的圆圈是被归为异常值的数据，没有被用于分位数标准化过程（彩图请扫封底二维码）。

## 分位数标准化

## 4. 执行分位数标准化:

i. 在 “Processing data” 页面中点击 “Affymetrix”（图 8-19）。

![](images/page_481_image_7.jpg)

图 8-19 提交标准化作业。（A）选择 “Affymetrix” 以前往 “Affymetrix normalization” 作业数据提交。（B）使用 “RMA” 分位数标准化方法，对名为 “cMyc\_raw\_data” 的数据集进行标准化（彩图请扫封底二维码）。

ii. 点击图 8-19B 中红色椭圆所示的 “browse server”。

iii. 点击 “RMA”，然后将该作业标记为 “cMyc normalization”。

iv. 点击 “Run”。

5. 当标准化作业完成后，

i. 点击图 8-20 右侧 “Job list” 面板中红色圈所示的 “cMyc normalization”。

ii. 点击图 8-20 中间红色椭圆所示的 “Box-plots”，查看标准化后的箱型图。

在分位数标准化后，很明显，8个样本的强度分布几乎一样。

![](images/page_482_chart_9.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 |
| --- | --- | --- | --- |
| G... | ~4.5 | ~6.0 | ~8.0 |
| G... | ~4.5 | ~6.0 | ~8.0 |
| G... | ~4.5 | ~6.0 | ~8.0 |
| G... | ~4.5 | ~6.0 | ~8.0 |
| G... | ~4.5 | ~6.0 | ~8.0 |
| G... | ~4.5 | ~6.0 | ~8.0 |
</details>

图8-20 查看分位数标准化的结果。蓝色矩形中显示的为RMA处理后的箱型图（彩图请扫封底二维码）。

## 差异表达基因检测

6. 为了检测到差异表达基因:

i. 首先，对各个样本的表型进行赋值。如上所述，4个样本来自于具有 c-Myc 转基因的小鼠，其余 4 个样本来自于没有该转基因的小鼠。将进行 t 检验来比较这两组样本（见步骤 7）。
ii. 选择 “Processing data” 页面中的 “Edit”（图 8-21A），然后在接下来的查询页面中，通过点击 “browse server” 选择被标准化的数据，选择 “Job generated” → “cMyc normalization” → “rma.summary”，然后点击 “Accept”。
iii. 点击如图 8-21B 所示的绿色椭圆中的 “Create new variable”。填写 “Phenotype”，

选择 “CATEGORICAL” 然后在弹出面板中点击 “OK”。

iv. 点击如黄色圆圈所示的魔术棒（magic wand）按钮，输入 “c-Myc\_transgenic” 作为一种表型（phenotype），然后点击 “OK”。再次点击魔术棒按钮以输入另一种表型 “Control”。

v. 点击图 8-21B 中紫色圆圈所示的信息按钮，然后在图中所示的紫色框中设定每个样本的表型值（phenotype values）。

vi. 点击 “submit” 以完成表型设置。

![](images/page_483_image_6.jpg)

图 8-21 为各样本设置表型。（A）点击 “Processing data”，然后点击 “Edit”，如图中红色椭圆内所示。（B）选择由标准化作业产生的 “rma.summary” 文件，如图中蓝色大方框所示。为新变量（绿色框内）设定 “Phenotype” 和 “CATEGORICAL”。设置为两类:“c-Myc\_transgenic” 和 “Control”（黄色矩形内）。最后为各样本输入表型类型（紫色框内）（彩图请扫封底二维码）。

## 7. 执行 $t$ 检验，

i. 在工具条中选择 “Expression”（图 8-21A），然后点击 “Class comparison” 以前往 “Differential expression: class comparison” 作业提交页面。在此页面中，点击 “Browse server” → “Job generated” → “cMyc\_normalization” → “rma.summary”，然后点击 “Accept”。

ii. 将分组名选择为 “Phenotype”，然后选择 “C-Myc\_transgenic” 和 “Control”。

iii. 选中 “T-test”，选择 “Benjamini and Hochberg (BH), FDR” 作为多重检验校正的方法。

iv. 输入 0.05 作为 FDR 临界值（cutoff），然后设定 “cMyc\_T\_test” 作为作业名称。

v. 点击 “Run”。

## 8. 当 t 检验作业完成后，

i. 点击 “Job list” 栏中的 “cMyc\_T\_test”，该项显示存在 789 个显著性（FDR<0.05）

差异表达的基因（图 8-22）。

ii. 点击 “t\_significative\_dataset.txt”，保存上述差异表达基因列表，用于后续的聚类分析（clustering analysis）。

![](images/page_484_image_4.jpg)

<details>
<summary>text_image</summary>

BABELOMICS4
gene expression and functional profiling analysis suite
Home | help | tutorial | contact
Upload data	Processing data	Expression	Genomic	Functional analysis	Utilities
anonymous working on project default: 192.06 Mb of 1.00 Gb (18.76%)
login registers
Results
UNDEFINEDlass comparison
The job named cMyc_T_test was launched on 2010-10-15 22:00:56.0 under the project named undefined, and has been visited 0 times
Input parameters
T-test output files
Significative results
Continue processing
Input parameters
T-test output files
Significative results
Number of significative results (adj. p-value = 0.05) : 789 (500 most significative values will be displayed)
Significative values dataset (adj. p-value = 0.05) : t_significative_dataset.txt
Send to Clustering tool...
Significative values table (adj. p-value = 0.05) : t_significative_table.txt
name	statistic	p-value	adj. p-value
1424942_a_at	35.45	0.009004742	0.02515
1434278_at	26.45	0.009002141	0.01932
1454904_at	22.75	0.009001484	0.01874
1434280_at	19.93	0.009001167	0.01874
1452211_at	19.74	0.009001225	0.01874
1451296_x_at	17.33	0.00904904	0.0295
1454730_at	16.4	0.009005577	0.02515
1417300_at	16.13	0.009003699	0.02383
1454631_at	15.81	0.00901846	0.0295
1426378_at	15.61	0.009008154	0.0295
prev_next_page 1 of 50
T heatmap with significative values (adj. p-value = 0.05)
Control: GSMQ77560 CEL
Control: GSMQ77581 CEL
Control: GSMQ77582 CEL
Control: GSMQ77583 CEL
cMyc_Junctione: GSMQ77576 ...
cMyc_Junctione: GSMQ77577 ...
cMyc_Junctione: GSMQ77578 ...
cMyc_Junctione: GSMQ77579 ...
statistic	adj p-value
35.6519	0.0252
26.4474	0.0193
22.7472	0.0187
19.9326	0.0187
19.7409	0.0187
17.3305	0.0295
16.4044	0.0252
16.1267	0.0238
16.8149	0.0295
16.5673	0.0295
</details>

图 8-22 查看 t 检验作业的结果。在“Significant results”部分中，下载“t\_significative\_dataset.txt”文件用于下游分析。在蓝色框中，所有 FDR 低于（0.05）的探针都可以通过点击 “prev” 和 “next” 按钮来浏览。在下方绿色框中，显示的是 8 个样本中所有显著性探针的热图（heat map）（彩图请扫封底二维码）。

## 差异表达基因聚类

对差异表达基因进行聚类通常能够获得很多信息，因为具有相似表达模式的一个基因集合能揭示被改变的调控过程。

9. 下载 Cluster（Eisen et al. 1998; de Hoon et al. 2004; http://bonsai.hgc.jp/\~mdehoon/software/cluster/）和 Treeview（Saldanha 2004; http://sourceforge.net/projects/jtreeview/files/）。

i. 去除由步骤 8 所生成文件 “t\_significative\_dataset.txt” 中的标题（header），因为 Cluster 不允许文件中含有标题。

ii. 运行 Cluster，然后选中 “File” → “Open” → “t\_significative\_dataset.txt”。

iii. 点击 “Adjust Data” 页面，将 “Center genes” 设置为 “Median”，并将 “Center arrays” 设置为 “Median”，然后点击 “Apply”（图 8-23A）。

iv. 点击 “Hierarchical” 页面（图 8-23B），选中 “Cluster”，然后在 “Genes” 和 “Arrays” 面板中均选择 “Correlation (centered)”。

v. 点击 “Centroid linkage” 作为聚类方法，然后等待状态栏中出现 “Done Clustering” 的信息（图 8-23B）。将产生一个名为 “t\_significative\_dataset.cdt” 的文件，这个文件将作为下一步骤中 Treeview 程序的输入内容。

![](images/page_485_image_10.jpg)

图 8-23 Cluster 3.0。(A) 在 “Adjust Data” 页面（红色椭圆中），将 “Center genes” 和 “Center arrays” 均选为 “Median”。(B) 在 “Hierarchical” 页面（红色椭圆中），选中 “Cluster”，然后在 “Genes” 和 “Arrays” 中均选择 “Correlation (centered)”。点击 “Centroid linkage”，然后等待窗口底部出现 “Done Clustering”（彩图请扫封底二维码）。

10. 为了可视化聚类结果，运行 Java 程序 Treeview，然后打开步骤 9.v 中产生的文件 “t\_significative\_dataset.cdt”。最终聚类的可视化结果如图 8-24 所示。具有相似表达模式的基因簇可以被仔细检查，并用于进一步分析，如检测该基因簇在功能分类中的富集情况。

![](images/page_486_image_2.jpg)

<details>
<summary>text_image</summary>

Java TreeView : C:\Documents and Settings\jhhhung\Desktop\t_significative_dataset.cdt
File Settings Analysis Export Window Help
Dendrogram
View Status
No status info for
GSM2775677_CEL
GSM2775676_CEL
GSM2775679_CEL
GSM2775678_CEL
GSM2775681_CEL
GSM2775680_CEL
GSM2775682_CEL
GSM2775683_CEL
Usage Hints
Click and drag to scroll
1434280_at
1416162_at
1424942_a_at
1423013_at
1450015_x_at
1431037_a_at
1451775_s_at
1450845_a_at
1420918_at
1427468_at
1418513_at
1422528_a_at
1423041_a_at
1415807_s_at
1450105_at
1434181_at
1452037_at
1456043_at
1425491_at
1418023_at
1433496_at
1419513_a_at
1420503_at
1425516_at
1427225_at
1428908_at
1425576_at
1416132_at
1420858_at
1418470_at
1421448_at
1423598_at
1423297_at
1427471_at
1416157_at
1448603_at
1426574_a_at
1451109_a_at
1452364_at
1421415_s_at
1415893_at
1420696_at
1429502_at
1422556_at
1422772_at
1449862_a_at
1452228_at
</details>

图 8-24 聚类结果可视化。（最左栏）基于层次聚类构建的完整系统树图。图中有两个大的基因簇和两个样本簇。上侧的基因簇（红色系统树）由 c-Myc 转基因样本中的上调基因组成。在另一个基因簇中的基因（未显示）为被下调的基因。（中间栏）最左栏中青色框内部分的放大图。（最右栏）相应的探针名称（彩图请扫封底二维码）。

![](images/page_486_image_4.jpg)

## 讨论

基于基因的微列阵仍旧比 RNA-seq 便宜, 因此使得实验可以在更多的生物样本上进行; 然而, 通常微阵列的噪声更高, 且不能对基因组中的重复区域进行测量。此外, RNA-seq 可以用来发现新转录物和新的选择性剪接。随着测序技术的快速发展, RNA-seq 可能会成为表达谱分析的主要技术。RNA-seq 数据分析需要大量计算资源。大多数用于分析深度测序数据的计算工具是命令行驱动的 (command-line driven), 缺乏一个图形化的用户界面。在方案 6 中, 我们描述了 Galaxy (http://main.g2.bx.psu.edu/), 该软件可以整合用于分析大尺度基因组、比较基因组和功能基因组数据的软件工具。Galaxy 的一大优势就是通过一个网页浏览器, 使那些不知道如何编写软件的用户进行复杂的大规模数据分析。用户可以执行独立的程序或者通过拖拽单个程序建立一个类似于管道的工作流程, 将各程序的输入和输出进行配对并设置必要的参数, 目前, 用于分析 RNA-seq 数据的 TopHat (Trapnell et al.2009) 和 Cufflinks (Trapnell et al. 2010) 等工具可以在 Galaxy 中使用。

通常，当发现一组差异表达基因或一簇相关基因的时候，我们对这些基因的共同生物学功能感兴趣。例如，当我们发现大部分差异表达基因与细胞分裂相关时，我们可以进一步将一种生物学机制与表型联系在一起。换言之，我们想要知道这些差异表达的基因是否可以被富集至某个功能注释（如细胞分裂）。这种分析被称为基因集富集分析（gene-set enrichment analysis）（Subramanian et al. 2005; Ackermann and Strimmer 2009）。注释主要来自人工管理的数据库，如 Gene Ontology（Ashburner et al. 2000）和 KEGG（Kanehisa et al. 2010）。因为许多复杂疾病是由相关通路（pathway）中的多个基因引起的，所以基因集富集分析越来越受到关注。对这些引起疾病的基因进行识别可以极大地促进我们对疾病发生机制和可能治疗结果的理解。

## 材料阅读 $t$ 检验和标准化

## 检验 $t$ 检验的正态性假设是否成立

可以对表达水平的分布情况进行作图，并与 Gaussian 钟形分布（Gaussian bell-shaped distribution）进行比较。另外，可以进行 Kolmogorov-Smirnov（K-S）检验，该方法可以评价某一分布（表达水平分布）是否与某一参照分布（Gaussian 分布）显著性偏离。实际上，如果观察到同一表型的样本之间存在预期外或高或低的变化很可能说明数据偏离正态分布。当这种情况发生时，存在以下几种选择。

1. 通过将样本标签随机打乱产生零模型（null model），然后使用经验零假设来计算 p 值。
2. 使用 Wilcoxon 秩和检验，该检验方法是一种无参数检验，并不需要正态性假设（以敏感性降低为代价）。
3. 使用其他可以稳定方差的检验方法，如 SAM (significance analysis of microarrays, 微阵列显著性分析)。关于 SAM 的详细信息见信息栏 “算法、门户网站和方法”。

注意 Student's $t$ 检验也假设待比较的两个分布方差相同。如果情况并非如此，请使用 Welch $t$ 检验。

什么情况下应该执行标准化？

标准化过程对多个微列阵数据比较非常重要。标准化的方法有很多，其中分位数标准化方法被广泛使用，并被认为它在去除噪声和偏差上很有效。请注意在大多数情况中，将标准化后的强度转化成对数形式非常重要；然而，对数转换可能使找到差异表达基因的力度降低。

## 层次聚类

聚类是一种将数据（如基因）分成不同集合（如基因簇）的方法。同一基因簇内的基因表现出相似的特性（如表达谱），它们比不同基因簇间的基因更为相似。两个基因的表达谱之间的相似性可以用相关系数（correlation coefficient）或欧几里得距离函数（function of Euclidean distance）来度量。在层次聚类中，基因簇是通过类树结构来构建的，这种方法要比仅列出一个基因簇更富含信息。层次聚类通常采用凝集策略（agglomerative strategy）。开始时，视每个基因为一个基因簇；然后在各步骤中，找出两个最相似的基因或者基因簇，并合并成一个新的基因簇，于是基因簇数目减少一个，直到最后，所有基因在一个簇中。两个基因簇之间的相似性可以通过它们的质心（centroid）之间的相似性来衡量。质心是一个伪数据，它的特性（如表达谱）是基因簇内所有数据的特性的平均值。在聚合基因簇的过程中，被聚合的基因簇之间的关系和基因簇之间的相似性会被记录，然后被用来构建一个如图8-24所示的系统树图（dendrogram）。通过从根部截平树枝，我们可以轻松控制基因簇的数量。与K均值聚类（K-means clustering）和自组织映射（self-organizing maps）等需要提前设定基因簇数量的聚类方法相比，层次聚类方法更为方便。

## 网络资源

```txt
Babelomics http://babelomics.bioinfo.cipf.es/
Cluster3.0 program http://bonsai.hgc.jp/~mdehoon/software/cluster/
Galaxy http://main.g2.bx.psu.edu/
Gene Expression Omnibus（GEO; NCBI 下微列阵和测序数据组的数据库）http://www.ncbi.nlm.nih.gov/geo/
Java Virtual Machine (JVM) http://www.java.com/en/download/index.jsp
TreeView http://sourceforge.net/projects/jtreeview/files/
```

## - 关于将上亿短读段定位至参考基因组上的简介

能够准确、快速且廉价地测定上亿 DNA 碱基的测序仪器的迅速发展和商业化正在使分子生物学和医学发生革命性的变化（见第 11 章）。许多技术在利用高通量测序仪的基础上被开发，从而对人个体基因组（Altshuler et al. 2010）、整个微生物群体（microbiome，微生物组）（Blow 2008）、癌症基因组（Mardis and Wilson 2009）、具有表观遗传学标记或与转录因子结合的特殊区域（ChIP-seq；Robertson et al. 2007）、mRNA（RNA-seq；Marioni et al. 2008）和小沉默 RNA（Trapnell and Salzberg 2009）进行测序。

与 Sanger 测序仪相比 [该测序仪每次运行产生上千条长度约为 1000 个核苷酸（又称读段，reads）的长序列]，由 Illumina（HiSeq 2000）和 Applied Biosystems（ABI SOLiD 4）生产的新测序仪，每次运行可以产生上亿条短读段（双端测序读段长度最长可达  $2 \times 100$  个核苷酸）。目前正在生产的 Roche/454 测序仪则可以产生片段长度大于 400 个核苷酸的读段。尽管 Pacific Biosciences 测序仪目前处于中等通量阶段，在早期测试阶段可以产生片段长度大于 1000 个核苷酸的读段。这些平台的详细讨论和比较见第 11 章。

因为通常情况下都能得到一个参考基因组，由新一代测序仪带来的第一个生物信息学挑战就是基因组定位问题，即将每个读段定位至一个参考基因组来揭示其在基因组上的位置。因为传统的 BLAST（见方案 2）和 BLAT（见方案 1）等序列比对算法运行速度都太慢而无法执行这样的任务，在过去 3 年中，已开发许多新的算法来将短读段序列定位至一个参考基因组（综述详见 Trapnell and Salzberg 2009）。目前，最为广泛使用的算法都基于对参考基因组的 Burrows-Wheeler (BW)变换 [Burrows-Wheeler (BW) transform]。这些算法包括 Bowtie(http://bowtie.cbcb.umd.edu/; Langmead et al. 2009)、BWA(http://maq.sourceforge.net/bwa-man.shtml; Liand Durbin 2009) 和 SOAP2 （http://soap.genomics.org.cn/; Li et al. 2009b）。尽管在处理错配和空位上的策略不同，这些算法均具有类似的良好表现。

BW 变换是一种最初被用于开发压缩大型文件的技术，目前已被修改用于压缩基因组序列。BW 变换能够与一种被设计用于完全字符串匹配算法（exact string-matching algorithms）的后缀/前缀（suffixes/prefixes trie）数据结构完美结合。Trie（该词来自于 retrieval）是一种储存一个字符串所有前缀/后缀的数据结构，有助于快速搜索，在我们的例子中，它储存的是参考基因组序列。搜索一个查询序列（一段测序读段）可以通过检索前缀与查询序列完全匹配的后缀来完成。因为所有后缀都已被排序，搜索过程可以被迅速完成。准确地说，搜索某个查询序列是否能够与 trie 中某个序列完全匹配的时间复杂度和查询序列的长度呈线性比例，且与参考基因组的长度无关。然而，台式电脑的内存无法储存一个基因组的所有后缀。BW 变换则可以将 trie 压缩至只占用小内存而不明显增加处理时间。

人类基因组是一个具有 30 亿个 A、G、C、T 的文本文件，其 BW 变换后文件仅需要大约 2.2 Gb 的内存空间（RAM），大多数台式机或笔记本电脑都能提供这样大小的空间。基于 BW 变换的算法以每次一个碱基的策略来对查询序列与 BW 变换后的参考基因组进行比较。每增加一个碱基，就筛选基因组中的一系列可能配对。基于字符串完全匹配算法，Bowtie 和 BWA 等算法的主要创新之一，就是对那些无法完全或完美定位至基因组（由测序错误或多态性导致）的查询序列的处理。这些算法对查询序列中很可能产生测序错误的位点上检索错配，以便在基因组中定位相应的配对。

尽管运行速度非常快，这些算法通常仍需要数个小时来处理一个数据集（将上百万个读段定位至一个哺乳动物基因组），且需要在用户的电脑上运行，而不是在可以通过网站访问的程序上。当数据集很大时，我们可以使用一个计算机集群（computer cluster），这样数据集就可以被分割成多个任务，从而提交给多个计算节点（compute node）来处理。然而，参考基因组不可被分割（如每个任务一个染色体）；否则，将需要一个高强度计算的合并过程。因为在基因组分割后，一个定位至基因组上多个位置的读段可能会定位至单一位置。定位至基因组上单一位置读段的百分比通常是一种比对算法的主要结果。在最佳情况下，85%～95%的读段定位至单一位置。然而，这个百分比数值受到以下几个与算法无关的因素的影响。

1. 多态性程度。如果样本基因组与参考基因组之间的进化距离较远，那么即便两者来自相同的物种，多态性数量依旧可能很高，尤其是在基因组中那些进化选择压力较小的区域（如基因间区和异染色质区域）。考虑到多态性，我们可以允许一小部分错配的存在（如每36个碱基一个错配）。更精确的做法是，如果该基因组的各基因型已被记录（例如，对人类基因组来说，HapMap国际人类基因组单体型图计划和千人基因组计划），我们就可以明确地将参考基因组中的多态性包括在内。例如，当我们仅考虑某个多态性位点的两个主要等位基因时，我们可以联合两个人类基因组副本，每个副本在相应位置上有一个等位基因，作为BW变换和搜索的输入参数。
2. 序列数据的质量。数据质量较低通常导致配对情况较差，这种情况通常由低质量的文库或测序问题导致（见第11章，方案19）。例如，一个人的DNA样本可能被严重污染，以致其中很多读段来自于其他生物的基因组。通过对读段各位点的测序质量分值做箱型图可以揭示较差的测序质量——高质量的数据集在所有位点的分值均较高，且3'端不存在大量衰退迹象。
3. 被测序的 DNA 分子长度与参考基因组长度的比较。对一些实验来说，被测序的 DNA 分子长度可能比测序仪的读段长度要小。例如，你想通过降解被蛋白质结合的 DNA 片段两侧碱基，从而高分辨率地研究 DNA 结合蛋白的结合位点。对一个由 N 个随机排列（即无重复序列等高阶排列模式）的碱基所组成的基因组来说，长度小于  $\log_{4}(N)$  个碱基的读段预期至少可随机定位至基因组上一次。同样道理，所有长度小于 16 个碱基的读段预期都可以定位至人类基因组上。因此，如果结合位点短于 16 个核苷酸，确定其基因组位置将很困难。在这个例子中，我们也许应该考虑对更长的 DNA 分子进行测序，然后通过计算识别内嵌的结合位点来提高分辨率。
4. 读段所定位的基因组区域中序列重复程度。从定义可以看出，定位至基因组上重复区域的读段可定位至多个位点。一些比对算法也许不会报道定位至基因组上过多位点读段的所有位置。例如，因为人类基因组中有大约 $10^{6}$ 个 Alu 元件，定位至 Alu 的读段通常会被舍弃。

这个问题仅可以通过以下两种方法来减轻:增加读段长度或使用双端测序以期其中一个片段对能够定位至单一位点。

目前已有的测序技术在不断努力获取更长的读段，并且在不断发展新的技术来产生更长的读段。允许少数错配已经不再是对长片段进行定位的最佳策略了，因为存在部分错配和得失位（indels，插入或缺失位点）的长片段仍旧可以定位至参考基因组上的单一位点。BWA-SW（http://maq.sourceforge.net/bwa-man.shtml；Li and Durbin 2010）等算法比短片段比对（如 Bowtie、BWA 和 SOAP2）的速度要慢，但仍比 BLAST 和 BLAT 之类的传统比对算法要快很多。在可预见的将来，将有一系列的算法可根据不同测序技术进行选择。

定位算法的输出结果是下一步分析的输入数据。下游分析的例子见方案4和方案6。定位结果可以通过UCSC基因组浏览器（Fujita et al. 2010）（方案1）等工具进行可视化。大多数比对算法可以产生SAM格式（或它的二进制等价物，BAM格式；Li et al. 2009a）的输出结果，该格式的文件可以被直接上传至UCSC基因组浏览器。借助SAMtools（Li et al. 2009a）和BEDTools（Quinlan and Hall 2010）等工具，用户可以调用变异读段[如单核苷酸多态性（single-nucleotide polymorphism，SNP)]和堆叠读段将SAM/BAM文件转换成BED格式，为其他软件或网站提供输入参数（基于以上两种工具的管道见如下“方法”部分；有关数据格式见信息栏）。

由于测序技术和定位算法的快速发展，通过期刊和书籍出版物来传递信息的传统途径相形之下就显得很慢。SeqAnswers（http://www.seqanswers.com）是一个由具有不同水平的下一代测序经验的用户所组成的在线论坛。在论坛上，有很多关于定位短读段及其随后数据分析与可视化的现有软件的有用线索。新手用户可以在其上找到运行这些程序时遇到的大多数错误的解决方案，经验丰富的用户则可以在其上得到一些关于参数调整的建议，以便为他们所需要解决的生物学问题提供最佳参数，而算法开发者则可以在其上提供他们的代码用于发布前的测试并寻求反馈。

## 网络资源

Bowtie http://bowtie.cbcb.umd.edu/

BWA-SW http://maq.sourceforge.net/bwa-man.shtml

SeqAnswers http://www.seqanswers.com

SOAP2 http://soap.genomics.org.cn/

## 方案 5 将上亿短读段定位至参考基因组上

本方案描述了通过使用几种程序将短序列读段定位至参考基因组上。本方案中的例子从一组 FASTQ 格式的 ChIP-seq 数据开始，使用 Bowtie 将读段与人基因组进行比对，然后使用 SAMtools 和 BEDTools 中的一些实用工具。SAMtools 和 BEDTools 是两套用于操作短读段比对结果的可执行程序的集合。通过这些工具的联合使用，我们可以对由 Bowtie 产生的序列比对结果进行总结和可视化，并进行基本分析，如确定定位至某个特定基因的读段数目。这些工具也可以被整合至更复杂分析的管道中（pipelines）。最终比对结果则可被用于方案 6 中峰的寻找。

![](images/page_491_image_2.jpg)

## 材料

## 仪器

具有 Internet 连接和网页浏览器的电脑

UNIX 环境

本方案使用了 UNIX 环境。我们强烈推荐您在基于 UNIX 的操作系统，如 Ubuntu、Centos/Red Hat 或 Mac OS X 中进行工作。如果你使用的是 Windows 操作系统，请先安装 Cygwin，然后在 Cygwin 下安装 Bowtie（http://bowtie-bio.sourceforge.net/index.shtml）、SAMtools（http://bowtie-bio.sourceforge.net/index.shtml）和 BEDTools（http://code.google.com/p/bedtools/）。Cygwin 是一个免费软件，它可以在 Windows 上提供一个类似 UNIX 的环境。我们可以在 http://www.cygwin.com/上找到 Cygwin 的安装包。

![](images/page_491_image_8.jpg)

## 方法

一次测序运行的输出结果通常是 FASTA 格式或 FASTQ 格式的。FASTQ 格式与 FASTA（解释见方案 1）类似，每个读段的标题行之后是核酸序列行，此外每个碱基还有对应的测序质量得分 [被称为 Phred 质量（Phred quality）]（见信息栏 “数据格式”）。大多数定位算法使用以上两种格式。

## 生成一个格式正确的数据集

1. 获得被干扰素 $\gamma$（interferon- $\gamma$，IFN- $\gamma$）刺激的 HeLa S3 细胞（GSE12782；Rozowsky et al. 2009）中由 STAT1 抗体钓出而被 STAT1 结合的 ChIP-seq 数据集。

i. 通过 “SPR000/SPR000703” 数据集的 “ftp” 链接（图 8-25 中红色椭圆中所示），从 GEO 网站（Barrett et al. 2007; http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE12782）下载所有的 FASTQ 文件。

ii. 连接页面上包含了两个文件夹，分别为 SRX003799 和 SRX003800，每个文件夹包含了 6 个压缩文件。在文件夹 SRX003799 中，SRR014987.fastq.bz2 到 SRR014992.fastq.bz2 的 6 个文件是 FASTQ 格式，均是基于 STAT1 的 ChIP-seq 数据。在文件夹 SRX003800 中，SRR014993.fastq.bz2 到 SRR014998.fastq.bz2 的文件均是用于输入（去除抗体后的阴性对照；更多信息请见方案 6）的 FASTQ 文件。

2. 将所有下载得到的文件都放在一个名为 “GSE12782” 的文件夹中，然后用任何合适的软件将它们解压，或者在 GSE12782 文件夹中执行以下 UNIX 指令:

$$
\text {bunzip2} *. \text {bz2}
$$

3. 将所有 STAT1 ChIP-seq 的 FASTQ 文件都合并到一起。

i. 使用以下两个 UNIX 指令:

```txt
cat SRR014987.fastq SRR014988.fastq SRR014989.fastq SRR014990.fastq
        SRR014991.fastqSRR014992.fastq > STAT1.fastq
cat SRR014993.fastq SRR014994.fastq SRR014995.fastq SRR014996.fastq
        SRR014997.fastqSRR014998.fastq > INPUT.fastq
```

ii. 将产生两个合并文件:STAT1.fastq 和 INPUT.fastq。

![](images/page_492_image_2.jpg)

<details>
<summary>text_image</summary>

NCBI
GEO
Gene Expression Omnibus
HOME SEARCH SITE MAP GEO Publications FAQ MIAME Email GEO
NCBI > GEO > Accession Display Not logged in | Login ?
Scope: Self Format: HTML Amount: Quick GEO accession: GSE12782
Query DataSets for GSE12782
Status Public on Sep 16, 2008
Title STAT1 transcription factor in Human HeLa S3
Project ENCODE
Organism Homo sapiens
Experiment type Genome binding/occupancy profiling by high throughput sequencing
Summary We report the results of chromatin immunoprecipitation following by high-thoughput tag sequencing (ChIP-Seq) using the GA II platform from Illumina for the human transcription factor STAT1 in HeLa S3 cells. The STAT1 ChIP was performed using HeLa S3 cells that are stimulated using gamma-interferon. We have also generated a sequenced input DNA dataset for gamma-interferon stimulated HeLa S3 cells.
Raw data for this study is available for download from the Short Read Archive database at:
http://www.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?study=SRP000703.
For data usage terms and conditions, please refer to http://www.genome.gov/27528022 and
http://www.genome.gov/Pages/Research/ENCODE/ENCODEDataReleasePolicyFinal2008.pdf
Platforms (1) GPL9115 Illumina Genome Analyzer II (Homo sapiens)
Samples (2) GSM320736 IFN_gamma_STAT1_ChIP-Seq in HeLa S3
GSM320737 IFN_gamma_Input_DNA in HeLa S3
This SubSeries is part of SuperSeries:
GSE12783 Genome-wide maps of transcription factor binding using ChIP-Seq for Human ENCODE
Download family Format
SOFT formatted family file(s) SOFT ?
MINIML formatted family file(s) MINIML ?
Series Matrix File(s) TXT ?
Supplementary file Size Download File type/resource
GSE12782_ELAND_PEAK_BED_README.txt 2.1 Kb (ftp)(http) TXT
GSE12782_RAW.tar 2.5 Gb (ftp)(http) TAR (of TXT)
SRP000/SRP000703 (ftp) SRA Study
Raw data provided as supplementary file
Processed data provided as supplementary file
NLM NIH GEO Help Disclaimer Section 508
</details>

图 8-25 数据集 GSE12782 的 GEO 页面。通过红色椭圆中所示的链接下载 FASTQ 文件（彩图请扫封底二维码）。

4. 通过下载并解压 Bowtie 网站（ftp://ftp.cbcb.umd.edu/pub/data/bowtie\_indexes/）上的预先建立好的文件，获得 Bowtie 所要求格式的人类基因组序列。建立这样的文件的具体步骤如下。

i. 登录 UCSC 基因组浏览器的下载页面（http://hgdownload.cse.ucsc.edu/downloads.html）。点击“Human”，然后点击“Feb. 2009 (hg19, GRCh37)”部分中的“Full data set”。

在连接页面的底部，下载“hg19.2bit”文件，然后将它保存在新建立的本地文件夹“GSE12782”中。这是二进制压缩的人类基因组文件。

ii. 当下载完成后，我们需要使用一个叫做 “twoBitToFa” 的文件来将 “hg19.2bit” 文件转换成 Bowtie 所要求的 FASTA 格式。通过 http://hgdownload.cse.ucsc.edu/admin/exe/链接并选择合适的电脑平台（如 “linux.x86\_84”），然后点击 “twoBitToFa” 将该程序保存在本地文件夹 “GSE12782” 中。

iii. 输入以下指令:

twoBitToFa hg19.2bit hg19.fa

iv. 将产生一个名为 “hg19.fa” 的文件，该文件是人类基因组被分为不同染色体的

FASTA 文件。

v. 为了快速查询和短序列比对，我们需要为人基因组建立索引。输入以下指令:

bowtie-build -f hg19.fa hg19

vi. 将产生 6 个索引文件:hg19.1.ebwt、hg19.2.ebwt、hg19.3.ebwt、hg19.4.ebwt、

hg19.rev.1.ebwt 和 hg19.rev.2.ebwt.

## 使用 Bowtie 将读段与人类基因组进行比对

5. 使用 Bowtie 将 STAT1.fastq 和 INPUT.fastq 中的读段与人类基因组进行比对，

i. 输入以下两个指令:

bowtie hg19 --best --strata -v 2-m 1 -S -q -p 8 STAT1.fastq STAT1.sam

bowtie hg19 --best --strata -v 2-m 1 -S -q -p 8 INPUT.fastq INPUT.sam

ii. 为了在比对时允许 Bowtie 利用存储在 FASTQ 文件中的测序质量信息，将 “-v” 改为 “-n”，然后提供质量得分的计算定义:“-phred33-quals”、“-phred64-quals” 或 “-solexa-quals”。

6. 两个输出的比对文件 STAT1.sam 和 INPUT.sam 都是 SAM 格式。SAM 使用了一种丰富但是紧凑的数据结构，需要利用计算机软件来解析出 SAM 文件中的感兴趣字段，并将选中的字段转化成一个便于阅读的表格。SAMtools 和 BEDTools 就是两套可以用于这种用途的计算机程序。

i. 使用以下指令将 STAT1.sam 和 INPUT.sam 文件转化成二进制 BAM 文件，与 SAM 格式文件相比，BAM 格式文件在储存和可视化方面具有更高的计算效率:

samtools view -bSh -o STAT1.bam STAT1.sam

samtools view -bSh -o INPUT.bam INPUT.sam

## Bowtie 中的参数

Bowtie 具有许多参数，我们有必要了解每个参数的用途，然后选择正确的组合。参数的详细解释请见 Bowtie 手册(http://bowtiebio.sourceforge.net/manual.shtml#the-n-alignment-mode)。步骤 5 中的例子包含了最基本的参数:

“--best --strata”:对每个读段，仅报道错配数量最少的比对

“-v 2”: 仅报道含有或少于两个错配的的比对

“-m1”:仅报道定位于基因组上一个位置的比对（这些读段被称为单一映射）

“-q”: 使用 FASTQ 格式的文件作为输入

“-S”: 将比对以 SAM 格式输出

“-p 8”: 通过在不同处理器或不同核上同时调用 8 个搜索线程来加速 Bowtie 运行。线程的最优数量取决于可用的处理器。

参数 b 使 SAMtools 输出 BAM 文件；参数 S 表示输入内容为 SAM 格式的；参数 h 告诉 SAMtools 在输出结果中保留标题。作为定制通道，STAT1.bam 和 INPUT.bam 可被上传至 UCSC 基因组浏览器。

ii. 图 8-26A 显示了 STAT1.bam 中的一个特定位点（chr1:175 161 500～175 163 500）。那些定位至基因组正链和负链上的比对分别用蓝色和红色表示。将比对区域放大至碱基水平来查看错配，从而找到可能的 SNP 或者测序错误。

![](images/page_494_chart_2.jpg)

<details>
<summary>funnel</summary>

| Metric | Value |
| --- | --- |
| STAT1_negativeness (Positive) | 73 |
| STAT1_negativeness (Negative) | 59 |
| STAT1_positiveness (Positive) | ~73 |
| STAT1_positiveness (Negative) | ~59 |
</details>

图 8-26 在 UCSC 基因组浏览器中可视化 Bowtie 比对。（A）被上传的 STAT1.bam 文件。通过设置比对区域至碱基水平，可见每个读段中的错配。（B）两条定制通道被上传至 UCSC 基因组浏览器。最左侧的标签显示了这些通道的名字（彩图请扫封底二维码）。

7. 这些比对可以作为定位至基因组各个位置的读段数量的直方图表达出来。BEDTools 中的 genomeCoverageBed 程序可以生成这样的直方图，并将它们储存为 UCSC bedGraph 格式（http://genome.ucsc.edu/golden-Path/help/bedgraph.html）。为了提高计算效率，genomeCoverageBed 要求这些比对根据染色体进行分类。以上过程可以通过以下两步完成。

i. 根据基因组坐标，使用以下指令将 STAT1.bam 和 INPUT.bam 分类，并储存结果文件为 STAT1.sorted 和 INPUT.sorted:

samtools sort STAT1.bam STAT1.sorted

samtools sort INPUT.bam INPUT.sorted

ii. 使用下列 BEDTools 指令将 BAM 文件转换成 BED 文件:

bamToBed -i STAT1.sorted.bam > STAT1.sorted.bam.bed

bamToBed -i INPUT.sorted.bam > INPUT.sorted.bam.bed

以下几行来自 BED 文件:

chr1 10446 10474 SRR014988.1614474 255 -

chr1 10459 10487 SRR014991.3802529 255 -

chr1 10496 10524 SRR014987.254257 255 -

chr1 13051 13079 SRR014992.3833233 255 - iii. 程序 genomeCoverageBed 也需要一个列有各染色体名字和大小（碱基对数量）的输入文件，tab 分隔的文件如下（以人类基因组为例）:

```txt
chr1 249250621
chr2 243199373
...
chrY 59373566
```

iv. 因为 BAM 文件也包含了这样的信息，使用下列 UNIX 命令来生成一个名为 human.genome 的文件:

```perl
sed-n'2,94p'SSTAT1.sam|cut -f 2, 3|awk '{split($1, a, “:”); split($2, b, “:”);
print a[2]\t\"b[2]}' > human.genome
```

v. 最后，使用以下命令来生成包含定位至正链和负链上读段数量信息的 4 个文件:

```batch
genomeCoverageBed -bga -ibam STAT1.sorted.bam
-g human.genome -strand + > STAT1_positive.bed
genomeCoverageBed -bga -ibam STAT1.sorted.bam
-g human.genome -strand - > STAT1_negative.bed
genomeCoverageBed -bga -ibam INPUT.sorted.bam
-g human.genome -strand + > INPUT_positive.bed
genomeCoverageBed -bga -ibam INPUT.sorted.bam
-g human.genome -strand - > INPUT_negative.bed
```

vi. 通过设定参数 “-strand” 将定位至基因组不同链上的读段分开。如果在某个应用中，更期望将定位至不同链上的读段混合在一起，就省略这个参数。下面为这样文件中的几行数据信息:

```txt
chr1 566745 566746 9
chr1 566746 566747 12
chr1 566747 566748 15
chr1 566748 566749 22
chr1 566749 566750 26
chr1 566750 566751 29
chr1 566751 566752 32
chr1 566752 566753 34
chr1 566753 566754 38
```

8. 将这 4 个 bedGraph 文件作为定制通道直接上传至 UCSC 基因组浏览器。为了减少文件大小, 使用以下 UNIX 指令提取一个特定的基因位点 (chr1:175 161 500～175 163 500):

```txt
awk ' {if ($1 == "chr1" && $2 >= 175161500 && $3 <= 175163500) print $0}'
```

```batch
STAT1_positive.bed > region_positive.bed
```

图 8-26B 显示了该位点位于正链和负链的直方图。

## Bowtie 可以允许大量错配存在吗？

不幸的是，Bowtie的设计使之不可能找到错配数量大于三个的比对。Bowtie同时还不能保证找到所有具有错配的比对。这个缺点（低敏感性）在大多数快速短片段比对程序中非常常见，因为它们都是由字符串完全匹配算法发展而来的，以牺牲敏感性而提高速度。允许更多的错配存在会显著降低速度。如果敏感性在一个应用中非常关键，我们也许会想要使用BLAST来对未定位的区域进行重新比对，以找到额外的比对。