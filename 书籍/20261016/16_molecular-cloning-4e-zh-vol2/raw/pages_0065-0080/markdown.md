## mRNA 丰度

前面描述的实验可以提供关于两种细胞群中每一个 mRNA 表达的相对丰度的信息。绝对表达水平如何呢？可以通过两种途径进行测定。第一，使用 Affymetrix 平台进行的单色实验能够合理地测定 mRNA 的丰度，因为微阵列中特定点的强度和与它互补的 mRNA 在原始的标记种群中的绝对强度有关。第二，对于双色实验，直接估算转录丰度的方法是比较标记的 mRNA 与标记的基因组 DNA，该基因组 DNA 应当以单拷贝基因存在（除非要解决的基因问题来自于一个多拷贝基因家族）。因此，基因组 DNA 用 Cy3 标记，mRNA 用 Cy5 标记，Cy5/Cy3 值提供了 mRNA 丰度的相对值。如果已知任何 RNA 的绝对丰度，这些比率可以转换为绝对 mRNA 丰度。标准化可用于设置 RNA 的绝对水平，所有其他 RNA 的丰度可以从其 Cy5/Cy3 值相对于已知标准的 Cy5/Cy3 值来推断。

## 比较基因组杂交

比较基因组杂交(CGH)用来检测整个基因组DNA拷贝数的变化(Pollack et al. 1999)。在CGH实验中，使用Klenow DNA聚合酶对两个种群的基因组DNA进行荧光标记。使用与mRNA表达分析相同的实验设计对标记的DNA进行比较。Cy5/Cy3值反映了拷贝数的变化。该方法最常用于肿瘤研究，在肿瘤发生过程中基因缺失及基因扩增的作用已有大量的报道。通过分析基因拷贝数的变化，可鉴定区域性扩增甚至整条染色体拷贝数的变化。以此方法为基础的改良方法亦已用于分析复制时相，由于S期DNA呈现拷贝数的变化，根据基因组DNA片段是否复制，可确定复制的时相。

## 转录结构的确定

用一个探针（点）检测一个基因的微阵列可以很容易地分析 mRNA 水平的变化，但需要不同的方法检测转录物的结构变异。转录物结构的变异包括剪切模式、转录的起始和终止位点的改变。这些转录物结构的改变及其他变化可用 Tiling 微阵列进行检测及作图。例如，转录起始位点可通过与上述绝对丰度杂交类似的方法，精确定位到 10～20 个核苷酸的范围。简单地说，用 Cy5 标记的 mRNA 和 Cy3 标记的基因组 DNA 进行杂交。表达的 RNA 应呈现 Cy5/Cy3 值高的一条长的“方波”:RNA 互补的点两侧对应的基因组序列 Cy5/Cy3 值应较低。高 Cy5/Cy3 值应开始于包含对应序列的 RNA 的 5'端，持续至 RNA 的末端（图 10-2）。这一技术在酵母中已被用来确定转录起始位点，分辨率可达约 20 核苷酸（Yuan et al. 2005），亦用于检测并定位人类细胞中新的转录物( Shoemaker et al. 2001)。

剪切模式的变化亦可通过微阵列进行检测和定位。在采用 Tiling 微阵列分析时，表达的外显子应呈现 Cy5/Cy3 的峰。确定外显子的另外一种方法是外显子微阵列技术，外显子微阵列中的每个点对应于一个外显子。当样品与外显子微阵列杂交时，特定组织中所有表达的外显子均呈高 Cy5/Cy3 值(Shoemaker et al. 2001)。

Tiling微阵列也被用于发现非编码RNA和新基因。因为表达微阵列只涵盖已知基因，而一个Tiling微阵列则包含了整个基因组。例如，21号和22号染色体的Tiling微阵列揭示了几乎全部人类基因组的低转录水平的基因（Kapranov et al. 2002）。

![](images/page_65_chart_2.jpg)

<details>
<summary>line</summary>

| 3号染色体坐标 | \(log_{2}\) mRNA/gDNA |
| --- | --- |
| 24585 | ~-0.7 |
| 24705 | ~-0.6 |
| 24825 | ~0.8 |
| 24945 | ~1.0 |
| 25065 | ~1.3 |
| 25185 | ~1.2 |
| 25305 | ~1.4 |
| 25425 | ~1.5 |
| 25545 | ~1.0 |
| 25665 | ~0.7 |
| 25785 | ~1.0 |
| 25905 | ~1.3 |
| 26025 | ~1.4 |
| 26145 | ~1.7 |
| 26265 | ~1.5 |
| 26385 | ~1.5 |
| 26505 | ~1.4 |
| 26625 | ~0.9 |
| 26745 | ~1.3 |
| 26865 | ~1.5 |
| 26985 | ~1.4 |
| 27105 | ~-0.6 |
</details>

图10-2 Tiling微阵列对mRNA结构的分析。图中显示的是标记的mRNA与标记的基因组DNA进行Tiling微阵列杂交获得的数据， $y$ 轴代表 $\log 2\mathrm{mRNA / gDNA}$ 值， $x$ 轴代表微阵列探针对应的基因组坐标。

## 鉴定RNA-蛋白质相互作用

采用免疫共沉淀方法分离目标蛋白，鉴定出能与特异性的 RNA 结合蛋白相互结合的 RNA 分子。这些 RNA 分子（或者 RNA 的一部分）可与不加抗体的对照免疫沉淀分离的非特异性 RNA 进行比较分析(Hieronymus and Silver 2003；Gerber et al. 2004)。

## RNA群的亚细胞定位

RNA 的功能特征（如翻译）可以用更精密的分离技术进行微阵列分析。在早期的研究中，微阵列已应用于多聚 RNA 的分析(Arava et al. 2003)。如果有合适的纯化技术，也可以研究 RNA 的亚细胞定位，如从神经元中分离树突用于鉴定相关的 RNA 群体(Eberwine et al. 2002)。

## 蛋白质定位研究

目前，Tiling微阵列最普遍的应用是“芯片上的染色质免疫共沉淀”（或ChIP-on-chip；见第20章）。通过染色质免疫共沉淀可以分析特定的蛋白质在染色质上的定位，如转录因子。简单地说，用甲醛将蛋白质共价交联于基因组，染色质通过超声处理成小片段（约500bp）。用特定蛋白的抗体（针对表位标签的抗体，或蛋白特异性的抗体，甚至特定修饰状态的抗体）通过免疫沉淀分离与此蛋白相关联的DNA。洗涤后，打断共价交联，分离基因组DNA。通常此DNA经过扩增，扩增后的样品被标记，与标记的不加抗体的对照扩增反应或沉淀前的样品进行竞争性杂交。ChIP-on-chip微阵列的结果分析能提供转录因子在基因组上定位的“快照”，且已被证明是研究转录因子和染色质对转录调节的强有力工具(Ren et al. 2000; Iyer et al. 2001)。

## 结构探针的核酸酶可及性

Tiling 微阵列也可与标记前经核酸酶诊断性处理的基因组 DNA 杂交，此方法利用基因组的染色质结构能强烈影响核酸酶可及性的特点。目前，已两种核酸酶用于全基因组研究。第一种是 DNA 聚合酶 I，已知其超敏位点位于基因组的调控元件，如启动子、增强子及绝缘子。染色质经 DNA 聚合酶 I 轻微消化，分离被切割的位点后，使用 Tiling 微阵列可分析鉴定切割位点周围的 DNA (Sabo et al. 2006)。第二种是微球菌核酸酶（MNase），其是一种非加工的核酸酶，常切割核小体之间的 DNA 连接子。已证实分析不被 MNase 切割的 DNA(包括与全基因组 DNA 的比较)是全基因组核小体定位研究的重要工具(Yuan et al. 2005)。

## 拼接微阵列

虽然外显子微阵列（见上文）能监测微阵列上呈现的每一个外显子的表达，但不能区别转录产物的结构，特别是外显子微阵列不能检测外显子的连接方式。例如，外显子1、2、3和5的表达可能为含有所有4个外显子的单一转录物，或可能为两种或多种转录物（1-2-5及1-3-5等）。为了确定外显子的连接方式，需要采用由互补于特定拼接序列的寡核苷酸构成的拼接微阵列。

## 再测序和 SNP 检测

DNA 杂交的序列特异性也可用于再测序和多态性检测等基因组分析。在这些应用中，每一个基因组定位在微阵列上由含一个核苷酸差异的几个寡核苷酸表示。如果研究的基因组区域含有 AATGCCA 序列，含有 AATTCCA、AATCCCA 和 AATACCA 的寡核苷酸也将被印制在芯片上。将基因组 DNA 与这些寡核苷酸杂交，可用于确定这些寡核苷酸所探查位点突变或序列多态性。

利用微阵列进行再测序的一种方法即所谓的序列捕获方案（Hodges et al. 2007）。把待研究的基因组区域相对应的寡核苷酸印制于微阵列。然后用 DNA 或 RNA 与此微阵列杂交，经过清洗步骤，所有互补序列都保留于微阵列上。通过杂交保留待测基因组区域后，洗脱杂交材料，用深度测序法测序（参见第 11 章）。

![](images/page_66_image_9.jpg)

## 进行微阵列实验

实验目的不同，特异性结合的寡核苷酸、标记的探针以及微阵列杂交分析的细节也有所不同，但大多数微阵列实验都包括6个步骤。

(1) 设计微阵列;
(2) 印制或者购买微阵列;
（3）分离并扩增 DNA 或 RNA 探针；
（4）用荧光基团标记 DNA 或 RNA;
（5）标记的探针与微阵列杂交；
(6) 分析微阵列杂交结果。

在本章中，我们将按顺序依次讨论每一个步骤。方案1提供了自制微阵列的印制方法；方案2～方案4提供了DNA和RNA的分离及扩增的方法；方案5～方案8提供了几种将荧光基团加至核酸分子的技术；方案9阐述了如何对结合在自制微阵列上的带正电荷的多聚赖氨酸进行封闭。最后提供了一个详细的标记探针与微阵列进行杂交、扫描、格式化以及杂交数据保存的通用方法（方案10）。微阵列分析的简要指南参见第8章。

## 设计微阵列

很多种类的微阵列现已商品化，对于大多数研究者来说，现成的产品足以满足需要。否则，可从厂家定制微阵列或自行设计并印制。微阵列的合理设计取决于其应用目的。对于大多数应用来说，基本的设计原则是相同的。本节介绍两种基本的微阵列，基因表达微阵列和 Tiling 微阵列。特殊形式的微阵列，如拼接微阵列和再测序微阵列，是针对不同的生物体设计的，我们推荐感兴趣的读者阅读相关文献(Hacia 1999; Mockler et al. 2005; Blencowe 2006; Hughes et al. 2006; Calarco et al. 2007; Cowell and Hawthorn 2007; Gresham et al. 2008)。

## 基因表达微阵列

设计用于微阵列的寡核苷酸需要生物信息学方面的专业知识。但是一些基本的设计要素是很容易理解的。第一，选择适当的寡核苷酸长度。目前，大多数寡核苷酸的微阵列印制长度为 $50\sim 70$ 个核苷酸。设计理想长度的寡核苷酸需要考虑几个因素，包括信号强度、特异性、费用及合成效率。越短的寡核苷酸越容易与特定基因组中许多不同的区域交互杂交，通常熔解温度（$T_{\mathrm{m}}$）非常低，易造成杂交技术上的问题。有关寡核苷酸长度与敏感性和特异性之间的关系的详细分析可见Hughes等的报道(2001)。对于大多数应用来说，可采用合理的经验法则，60个核苷酸的寡核苷酸能在这些互相制约的因素之间提供最佳平衡。

寡核苷酸设计要考虑的第二点是微阵列上的寡核苷酸与待研究的生物体的 RNA 种类的特异性或互补性的程度，一般说来，设计的寡核苷酸应当仅与一种 RNA 互补。通常 BLAST 检索（参见第 8 章）可用于筛选设计的寡核苷酸与相应的基因组序列的互补性，以鉴定其与待研究的基因组中多个序列互补的可能性。理想的情况下,使用者应选择在基因组中匹配性仅次于最低的寡核苷酸，而不是关注正常范围的 BLAST 值。

设计寡核苷酸要考虑的第三点是杂交特性的优化。有若干特性是可以优化的，但最重要的是寡核苷酸熔解温度（$T_{\mathrm{m}}$）。明确地说，微阵列上所有寡核苷酸的 $T_{\mathrm{m}}$ 值应在一个尽可能狭窄的区间。其他的一些要素，如熵（序列的复杂性）、GC含量以及自身互补性也应当同时被优化。可借助一些软件工具进行寡核苷酸的设计，包括可公开获得的工具，如ArrayOligoSelector（见下文），或由微阵列公司提供的有偿服务（有关寡核苷酸设计的更多细节见第7章、第8章）。

例如，某研究者希望为一种近期完成基因组测序的非模式生物设计基因表达微阵列。设计基因表达微阵列的第一步，当然是鉴定基因。由于基因鉴定通常可通过基因组测序完成，因此假定这些基因已用标准工具进行了预测(Zhang 2002; Ashurst and Collins 2003; Brent 2005; Solovyev et al. 2006)。

## ArrayOligoSelector

一旦编码区得到鉴定，就需要针对每一个基因设计寡核苷酸。已有许多程序可用于寡核苷酸筛选，包括应用广泛的 ArrayOligoSelector (Bozdech et al. 2003a,b)，在 http://arrayoligosel.sourceforge.net/免费提供使用（更多细节见第7章、第8章）。

ArrayOligoSelector 被设计用于全基因组分析及制备用户设定长度的寡核苷酸。对于每一条寡核苷酸，ArrayOligoSelector 可计算其唯一性、序列复杂度、自复性、GC 含量的得分。唯一性衡量的是一个特定的寡核苷酸与其最佳匹配或同源性次之的基因组序列的结合能的理论差值。序列复杂度的分析可使用户滤除含有同源聚合物的寡核苷酸，否则将导致杂交问题。自复性分数衡量的是寡核苷酸自复性产生的二级结构。自复性也是出现杂交问题的另外一个潜在原因。最后，将寡核苷酸间 GC 含量比例（%）的差异性降到最低也很重要，同时还有降低 $T_{\mathrm{m}}$ 值的差异、降低点之间的荧光强度的差异。

运行 ArrayOligoSelector 时，可确定以下几个特征:寡核苷酸长度、GC%、每个基因对应的寡核苷酸数量、掩蔽序列及唯一性的正常范围。通常寡核苷酸的长度为 60 聚体或 70 聚体，GC 含量取决于待研究的基因组的 GC 含量，通常选取的是基因组编码区的平均值。每一个基因的寡核苷酸数量取决于使用的微阵列是购买的还是自制的。如果购买的寡核苷酸用于自己印制微阵列，考虑到成本和可印制的点密度，一般很难采用每个基因多于 1 个或 2 个寡核苷酸。另外一种情况，如果使用商品化的微阵列，则可用的点数量决定每一个基因的寡核苷酸数量。掩蔽序列通常不是特定的，但是如果基因组中含有容易出问题的短重复元件，有时就需要将其掩蔽于微阵列的寡核苷酸之外。唯一性的正常范围通常是空白的，这将导致初始化数值的使用（更多信息见《ArrayOligoSelector 手册》）。

实验者可以对 ArrayOligoSelector 输出的结果进行过滤。例如，因为基于反转录酶的标记在基因 3'端区域效率更高，所以通常希望使用位于基因 3'端的寡核苷酸。

## Tiling 微阵列

Tiling 微阵列设计的寡核苷酸设计比基因表达微阵列的设计更简单, 因为 Tiling 微阵列假定微阵列含有待研究区域内的所有寡核苷酸。最简单的 Tiling 微阵列设计包括: 选择某一区域内的核苷酸 1～50 平铺作为点 1, 核苷酸 21～70 作为点 2, 依此类推。一旦完成所有寡核苷酸的设计, 即可用 BLAST 来寻找与目的基因有多个位点匹配的寡核苷酸, 这些寡核苷酸将被去除。更为细致的平铺设计采用了寡核苷酸定位的微小 “摆动”, 即点 2 为核苷酸 16～65, 点 3 为 45～94, 依此类推。这样做对于匹配杂交特性的处理, 如 $T_m$ 值和 GC 含量, 更优于简单的 Tiling 微阵列。

## 印制或购买微阵列

一旦完成寡核苷酸的设计，就可通过商品化渠道印制微阵列。寡核苷酸亦可经商品化渠道合成或通过自己的研究平台合成，然后用点样仪自行印制（参见方案1）。

## 用于微阵列杂交的核酸样品的分离及扩增

大多数用于微阵列的样品制备程序按照标准的方案，许多方案均可在本书的其他章节找到。例如，第1章描述了用目的样本中分离的基因组DNA进行比较基因组杂交分析（CGH）。第6章中描述了基因表达或拼接研究用的RNA或mRNA的纯化方案。第20章描述的染色质免疫共沉淀（ChIP）分离的样品是蛋白定位分析的材料。通常情况下，这些方案的后期检测是基于印迹技术或定量PCR分析，仅需要纳克级的样品。而微阵列标记通常需要几微克核酸，因此，在标记前必须对样品进行扩增。

## 扩增的一般注意事项

核酸扩增是杂交前的步骤，用以产生标记的微阵列探针，核酸扩增不能偏向基因组的任何特殊序列。因此，无偏离（或最小偏离）全基因组扩增方法是许多微阵列应用中的关键部分。

此章节包括 3 种扩增方案:两种适用于 DNA（方案 2 和方案 3），一种适用于 RNA（方案 4）。在进行扩增实验时，要注意以下几点:第一，初次尝试一个扩增方法时，采用量大且易于获得的材料（如肝脏 RNA）扩增小量的起始材料。对扩增材料和起始的“大宗池”的微阵列对比，能提供有价值的扩增偏离数据。完美的扩增结果是一个“黄色”的阵列，所有的原始材料和扩增材料均无任何差异的点。第二，避免任何可能含有 DNA 或 RNA 的物质污染样品。即使是极微量的外源核酸，也将被扩增、污染样品并破坏微阵列实验。

在进行分离和扩增实验时，需戴手套并使用带滤膜的吸头。第三，实验中需设置用水（无DNA或RNA）进行的对照扩增实验，以确定试剂没有被可扩增材料污染。

## 用于表达谱研究的 RNA 扩增

相对于DNA扩增，RNA扩增不是很普遍，但在一些使用微量的细胞种群的实验中仍然有可能用到，如用激光捕获的细胞群进行的神经生物学研究。RNA扩增试剂盒可以从若干供应商获得（如Ambion公司），或者按照方案4的方法进行扩增。

## 荧光标记核酸探针

除了 Affymetrix 微阵列外，用于微阵列的核酸标记与大多数微阵列实验平台中的核酸标记类似。对于大多数平台（自制或购买），荧光分子通过 DNA 聚合酶 I 的 Klenow 片段结合于 DNA。对于 RNA 标记，反转录酶用于制备标记的 cDNA。标记方法包括标记反应中所用的荧光标记的 dNTP（方案 5 和方案 7）。这一方法快速但昂贵，另外有一种便宜但是较为烦琐的替代方案，首先将氨基烯丙基核苷酸结合于核酸分子，然后再将氨基烯丙基基团偶联于荧光基团（方案 6 和方案 8）。在所有的标记实验方案中，标记前的源核酸可未经扩增抑或是扩增后的样品。

## 与微阵列杂交

使用自制微阵列和商品化的微阵列时，标记探针与微阵列杂交的方法明显不同。对于自制的微阵列，首先要封闭玻片，因为残留在玻片上的多聚赖氨酸可与标记材料结合，若不用琥珀酸酐处理以中和，将导致背景显著升高。方案9和方案10分别提供了自制微阵列的封闭和杂交方案。如果使用商品化的微阵列，通常由厂商提供杂交方案。杂交后，使用台式扫描仪进行扫描。数据经收集、格式化，并以数字形式保存用于后续的分析。

## 分析微阵列数据

对微阵列进行数据分析时采用的工具取决于要解决的实验问题:基因定位研究和基因表达研究需要的工具不同。第8章中提供了一些可用的资源。以下我们概括了数据分析的基本步骤。

微阵列数据分析的第一步是去掉错误数据（一些被“标示”的点的数据，因为这些点受荧光沉淀的影响而变得模糊等），然后将其余数据标准化。GenePix 软件输出的标准数据格式是“.gpr”文件，对这些文件进行操作时，通常去掉所有被标示（flagged）的探针，然后处理  $\log_{2}$  比值数据。更高级的用户可以考虑使用特定的功能，如前景和背景强度。

大多数双色微阵列研究采用的标准化方法是  $\log_{2}$  比值平均为 0。此标准化过程隐含的假设是所有被评估的点均未发生整体的变化。因此，面对这些标准化数据时，重要的是记住评估的是相对数值而不是绝对数值。实际上，标准化可通过将未标记的对数比值数据进行平均，然后将表中每一项均减去此数值来实现。这一过程可用电子表格手工计算或用通用命令的语言，如 MATLAB、Perl 或 R。

完成标准化后，根据 log 比值的数据对表格进行归类，以鉴别出明显表达上调或者下调的基因（如果是基因表达微阵列）或鉴别出待研究的蛋白质中的高丰度位点。数据分析途径依据要解决的问题不同而不同。很多微阵列研究都设计多重微阵列，通常将数据进行聚类分析以鉴别行为相似的基因或位点。

聚类分析和聚类的可视化，网上有很多程序可用。本书使用的是经典的 Cluster 和 TreeView 程序(Eisen et al. 1998)，可通过 SourceForge（http://sourceforge.net/）或通过 Eisen实验室网站（http://www.eisenlab.org/）在线获得。用于指导聚类文件格式化的范例文件也可找到，此处不再描述格式化的过程。简言之，将数据上传于Cluster，设置各种阈值（对于特定基因缺失的数据、超出某些阈值的基因数量等），选用几个聚类算法之一进行分析。聚类的数据输出通过TreeView可视化，用户即可建立一个经典的微阵列数据“热图”。

![](images/page_70_image_3.jpg)

## 致谢

此章节中的实验方案修改自 Ash Alizadeh、Chih Long Liu、Audrey Gasch、Jason Lieb、Bing Ren 和 L. Ryan Baugh 撰写的实验方案，感谢他们慷慨提供。

## 参考文献

- Arava Y, Wang Y, Storey JD, Liu CL, Brown PO, Herschlag D. 2003. Genome-wide analysis of mRNA translation profiles in Saccharomyces cerevisiae. Proc Natl Acad Sci 100: 3889–3894.
- Ashurst JL, Collins JE. 2003. Gene annotation: Prediction and testing. Annu Rev Genomics Hum Genet 4: 69–88.
- Blencowe BJ. 2006. Alternative splicing: New insights from global analyses. Cell 126: 37–47.
- Bozdech Z, Llinas M, Pulliam BL, Wong ED, Zhu J, DeRisi JL. 2003a. The transcriptome of the intraerythrocytic developmental cycle of Plasmodium falciparum. PLoS Biol 1: e5. doi: 10.1371/journal.pbio.0000005.
- Bozdech Z, Zhu J, Joachimiak MP, Cohen FE, Pulliam B, DeRisi JL. 2003b. Expression profiling of the schizont and trophozoite stages of Plasmodium falciparum with a long-oligonucleotide microarray. Genome Biol 4: R9. doi: 10.1186/gb-2003-4-2-r9.
- Brent MR. 2005. Genome annotation past, present, and future: How to define an ORF at each locus. Genome Res 15: 1777–1786.
- Calarco JA, Saltzman AL, Ip JY, Blencowe BJ. 2007. Technologies for the global discovery and analysis of alternative splicing. Adv Exp Med Biol 623: 64–84.
- Cowell JK, Hawthorn L. 2007. The application of microarray technology to the analysis of the cancer genome. Curr Mol Med 7: 103–120.
- DeRisi JL, Iyer VR, Brown PO. 1997. Exploring the metabolic and genetic control of gene expression on a genomic scale. Science 278: 680–686.
- Eberwine J, Belt B, Kacharmina JE, Miyashiro K. 2002. Analysis of subcellularly localized mRNAs using in situ hybridization, mRNA amplification, and expression profiling. Neurochem Res 27: 1065–1077.
- Eisen MB, Spellman PT, Brown PO, Botstein D. 1998. Cluster analysis and display of genome-wide expression patterns. Proc Natl Acad Sci 95:14863–14868.
- Gerber AP, Herschlag D, Brown PO. 2004. Extensive association of functionally and cytotopically related mRNAs with Puf family RNA-binding proteins in yeast. PLoS Biol 2: e79. doi: 10.1371/journal.pbio.0020079.
- Gresham D, Dunham MJ, Botstein D. 2008. Comparing whole genomes using DNA microarrays. Nat Rev Genet 9: 291–302.
- Hacia JG. 1999. Resequencing and mutational analysis using oligonucleotide microarrays. Nat Genet 21: 42–47.
- Hieronymus H, Silver PA. 2003. Genome-wide analysis of RNA–protein interactions illustrates specificity of the mRNA export machinery. Nat Genet 33: 155–161.
- Hodges E, Xuan Z, Balija V, Kramer M, Molla MN, Smith SW, Middle CM, Rodesch MJ, Albert TJ, Hannon GJ, McCombie WR. 2007. Genome-wide in situ exon capture for selective resequencing. Nat Genet 39:1522–1527.
- Hughes TR, Mao M, Jones AR, Burchard J, Marton MJ, Shannon KW, Lefkowitz SM, Ziman M, Schelter JM, Meyer MR, et al. 2001. Expression profiling using microarrays fabricated by an ink-jet oligonucleotide synthesizer. Nat Biotechnol 19: 342–347.
- Hughes TR, Hiley SL, Saltzman AL, Babak T, Blencowe BJ. 2006. Microarray analysis of RNA processing and modification. Methods Enzymol 410: 300–316.
- Iyer VR, Horak CE, Scafe CS, Botstein D, Snyder M, Brown PO. 2001. Genomic binding sites of the yeast cell-cycle transcription factors SBF and MBF. Nature 409: 533–538.
- Kapranov P, Cawley SE, Drenkow J, Bekiranov S, Strausberg RL, Fodor SP, Gingeras TR. 2002. Large-scale transcriptional activity in chromosomes 21 and 22. Science 296: 916–919.
- Mockler TC, Chan S, Sundaresan A, Chen H, Jacobsen SE, Ecker JR. 2005. Applications of DNA tiling arrays for whole-genome analysis. Genomics 85: 1–15.
- Pollack JR, Perou CM, Alizadeh AA, Eisen MB, Pergamenschikov A, Williams CF, Jeffrey SS, Botstein D, Brown PO. 1999. Genome-wide analysis of DNA copy-number changes using cDNA microarrays. Nat Genet 23: 41–46.
- Ren B, Robert F, Wyrick JJ, Aparicio O, Jennings EG, Simon I, Zeidlinger J, Schreiber J, Hannett N, Kanin E, et al. 2000. Genome-wide location and function of DNA binding proteins. Science 290: 2306–2309.
- Sabo PJ, Kuehn MS, Thurman R, Johnson BE, Johnson EM, Cao H, Yu M, Rosenzweig E, Goldy J, Haydock A, et al. 2006. Genome-scale mapping of DNase I sensitivity in vivo using tiling DNA microarrays. Nat Methods 3: 511–518.
- Shoemaker DD, Schadt EE, Armour CD, He YD, Garrett-Engele P, McDonagh PD, Loerch PM, Leonardson A, Lum PY, Cavet G, et al. 2001. Experimental annotation of the human genome using microarray technology. Nature 409: 922–927.
- Solovyev V, Kosarev P, Seledsov I, Vorobyev D. 2006. Automatic annotation of eukaryotic genes, pseudogenes and promoters. Genome Biol 7: S10.1–S10.12.
- Yuan GC, Liu YJ, Dion MF, Slack MD, Wu LF, Altschuler SJ, Rando OJ. 2005. Genome-scale identification of nucleosome positions in S. cerevisiae. Science 309: 626–630.
- Zhang MQ. 2002. Computational prediction of eukaryotic protein-coding genes. Nat Rev Genet 3: 698–709.

## 方案 1 印制微阵列

大多数实验室选择从供应商处订购微阵列，如 NimbleGen、Agilent、Affymetrix 或 Illumina 公司。这些供应商销售的产品涵盖了生命体基因组的 3 个领域。大多数公司也可根据订单定制微阵列。印制微阵列非常简单，对微阵列需求广泛的小实验室也会发现其成本效益，值得制作自己的微阵列。印制微阵列需要一个点样机器人。能够买到的点样机器人有若干种，如 OmniGrid series (Digilab Genomic Solutions)。这些设备很昂贵，通常放置于研究院所或大实验室的仪器中心。多年前斯坦福大学的 Brown 实验室已完成了点样机器人的设计，可作为一种选择。制造点样机器人的方法不在本章节讨论的范围内，感兴趣的读者可以在 http://cmgm.stanford.edu/pbrown/mguide/找到制作方案。

对于典型的微阵列，寡核苷酸配制于  $3 \times SSC$ ，浓度为  $20 \sim 40 \mu mol/L$ ，然后分别加入 384 孔板。寡核苷酸被印制在多聚赖氨酸包被过的微阵列玻片上。印制过程中湿度最好高于 50%。当湿度为  $20\% \sim 30\%$  时，有可能出现点样针干燥的问题。为了提高或维持适当的湿度，可以考虑在机器人周围建造一湿度可控的外包。对于缺少外包的机器人，在印制过程中打开 1 或 2 台加湿器就足够了。

印制方案的细节根据使用的机器人不同而变化，因此请按照生产厂家的说明进行操作。本方案提供了一个使用配备接触式钢羽针的机器人的典型工作流程。

![](images/page_71_image_5.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

所需序列的寡核苷酸

寡核苷酸通常溶于  $20 \sim 40 \mu mol/L$  的  $3 \times SSC$  中。

剪切后的鲑鱼精 DNA&lt;A&gt;（150ng/ $\mu$ L，重悬于 3×SSC）

$$
\mathrm{SSC} (3 \times) <   \mathrm{A} >
$$

## 仪器设备

干燥器

压缩氮气

平板（384孔）

多聚赖氨酸包被的玻片

可以用多聚赖氨酸包被玻片，但是根据我们的经验，失败的比例很高。商品化的多聚赖氨酸包被的玻片（如 Erie Scientific）成本效益最佳。

塑料玻片盒

点样仪

![](images/page_71_image_22.jpg)

## 方法

## 准备印制

## 第0天

1. 将寡核苷酸按照每孔相同体积加入 384 孔板（通常  $10 \sim 20 \mu L/孔$ ）。如果使用冷冻保存的寡核苷酸溶液，可将其置于  $4^{\circ}C$  过夜融化。如果使用寡核苷酸干粉，则将其用  $3 \times SSC$  重悬，并置于  $4^{\circ}C$  过夜。
2. 通过测试印制确认所有的点样针都能印制，并确定阵列经过正确的校准（图 10-3）。

为了尽可能接近实际印制板的黏度，使用含有  $150ng/\mu L$  剪切过的鲑鱼精 DNA（重悬于  $3\times SSC$ ）进行试印制。测试印制时，所有的点样针均应连续印制数百个点。另外，需在玻片盘的多个位置进行测试印制以确定盘片在上次使用后是否被显著扭曲。

如果试印制显示点样机器人不能按要求工作，参见“疑难解答”。

![](images/page_72_image_4.jpg)

图 10-3 点样仪。图中显示了玻片盘（A），实验巢（B）和印制头及清洁/干燥站（C）的位置（彩图请扫封底二维码）。

## 第一天

3. 再次进行测试印制，以确定点样针依然能正常印制。

4. 轻轻地将玻片放置于微阵列仪的玻片盘中。确定所有的玻片都放平并牢固地附着（根据微阵列仪使用抽真空、夹子或者胶带加固）。

▲小心对玻片进行操作，以免产生微小的玻璃片落在玻片表面。

5. 使用压缩氮气吹拂玻片表面除尘。

6. 如果微阵列仪配备了超声水浴来清洗点样针，将其灌满新鲜的水。

7. 将 4 个含有寡核苷酸的 384 孔印制板从 $4^{\circ} \mathrm{C}$ 取出, 放置至少 $1 \mathrm{~h}$, 使其恢复到室温。

8. 约 $1000\mathrm{r / min}$ 离心 $2\mathrm{min}$，以去除板盖上的冷凝水。小心地移去384孔板的盖子和印制板的胶黏板盖。

▲小心不要摇晃板子，孔之间的交叉污染会对后续各种实验数据分析带来严重影响。

9. 将板子放置于点样机器人的持板器上。

## 印制微阵列

10. 开始印制。始终要注意板子的顺序及方向。微阵列数据分析时，确定板子的顺序对于将基因名称与点的位置对应并生成“.gal”文件是必需的。在印制过程中的任何错误，如印制板顺序颠倒（如将3号板置于2号板之前）等，只要被发现就可随时改正。

11. 当完成一块板的印制时，印制头完全停止。若印制板欲干燥储存,可将板子置于超净台中挥发干燥，或用铝箔覆盖并盖上盖子，储存于-80℃。

12. 将下一块板子放于持板器。

13. 如果不进行背靠背的印制，印制完成后，将玻片干燥过夜。

## 第二天

14. 将所有的玻片从微阵列仪转移至塑料玻片盒中。将其储存于干燥器中。

15. 关闭微阵列仪电源。

![](images/page_73_image_9.jpg)

## 疑难解答

问题（步骤 2）:印制针不能正确印制。

解决方案:如果印制针不能印制，可从下面 4 个方面解决。第一，如果脏东西或者其他材料堵塞了针尖，用超声水浴彻底清洗点样针。第二，如果在显微镜下检查发现是某根针被堵塞，可试用剃须刀片仔细地疏通针尖，以清除污物。第三，针的长度的细微差别会使有的针无法工作，更换印制头内的针可改进印制。第四，如果采用所有步骤后，有些针还是不能工作，则换用一根新针。

问题（步骤2）:测试板在微阵列仪的不同位置印制不一致。

解决方案:如果微阵列仪在某些特定位置不能印制，可调整该位置的印制高度。机器人附带的软件可执行高度的调节。

![](images/page_73_image_15.jpg)

## 讨论

成功的印制需要对印制平板进行小心的操作，以避免交叉污染，点样针要定时检查（如每完成一块或两块384孔板之后）以确定其仍能正常印制，清洗针时，水浴（或超声仪）中的水必须足以覆盖点样针，在印制过程中，我们通常每6h向超声仪中加水5～10mL，但这也取决于环境湿度。

为了确定点样针在印制，可从一定角度用手电筒观察玻片。印制过程中沉积的盐呈白色，当点样针停止工作时，印制过的部分与其他部分有所区别。例如，如果印制了5行×20个点，应能看到一个完美的 $5\times20$ 的矩形，如果某一根点样针没有正常工作，矩形不完整。

当某根针停止印制时，小心将其取下，如针内外有灰尘，可在显微镜下清理。若未见灰尘，有时通过超声彻底地清理可恢复正常。否则，用备用针替换有问题的针或移动印制头周围的针作为最后的补救措施。印制过程暂停后，用一张新玻片替换第一张玻片，再次进行测试印制以确认新的调整是否奏效。重新启动点样机器人时，确认印制命令精确地重启于印制工作暂停的位置。

## 网络资源

建造点样机器人的方法:http://cmgm.stanford.edu/pbrown/mguide/

## 方案 2 Round A/Round B DNA 扩增

此程序的目的是随机扩增样本 DNA 以获得最佳的序列重现性。此程序已成功地应用于扩增少于 10ng 的基因组 DNA 样品。此方案包括 3 个系列的酶促反应。在 Round A 中，使用测序酶来延伸随机复性引物以产生后续 PCR 反应的模板。在 Round B 中，特异性引物用于扩增前面产生的模板。最后，扩增后的材料按方案 7 或方案 8 进行标记；还可用此方案的 Round C 在额外的 PCR 循环中掺入氨基烯丙基-dUTP 或 Cy-染料偶联的核苷酸。此方案不适用于小于 250bp 的材料扩增，小于 250bp 的材料不能被均一性地扩增。在这样的情况下，建议使用方案 3。方案节选自 Bohlander 等(1992)。

![](images/page_74_image_4.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

aa-dNTP/Cy-dNTP 混合物 (100×)&lt;R&gt;

BSA (500μg/mL)

从待研究的样品中分离的 DNA（10～100ng）

例如，对于 CGH 分析，按第 1 章的方法分离基因组 DNA；对于蛋白质定位研究，按照第 20 章所述用染色质免疫共沉淀（ChIP）的方法分离 DNA。

dNTP 混合物 (3mmol/L)

dNTP （100×；每种核苷酸 20mmol/L）

DTT (0.1mol/L)

$MgCl_{2}$  (25mmol/L)

PCR 缓冲液（10×）（500mmol/L KCl，100mmol/L Tris，pH 8.3）

引物 A: GTTTCCCAGTCACGATCNNNNNNNNN (40pmol/μL)

引物 B: GTTTCCCAGTCACGATC (100pmol/ $\mu$ L)

测序酶（13U/μL）(US Biochemical，自录号 70775)

测序酶缓冲液（5×）

测序酶稀释缓冲液

Taq 聚合酶（5U/μL）

## 仪器设备

琼脂糖凝胶（1%）

Microcon 30 spin column (Millipore)

热循环仪

![](images/page_75_image_2.jpg)

## 方法

## Round A: 随机复性引物的延伸

1. 按如下配方准备 Round A 反应:

| DNA | 7μL |
| --- | --- |
| 测序酶缓冲液(5×) | 2μL |
| 引物A(40pmol/μL) | 1μL |

应用此方案可有效扩增低至 10ng 的 DNA。设置一个用水来代替 DNA 的反应作为阴性对照。

2. 94℃加热 2min 然后快速降温至 10℃，使模板 DNA 变性及引物复性。将反应混合物在 10℃放置 5min。

3. 配制反应混合物:

| 测序酶缓冲液(5×) | 1μL |
| --- | --- |
| dNTP (3mmol/L) | 1.5μL |
| DTT (0.1mol/L) | 0.75μL |
| BSA (500μg/μL) | 1.5μL |
| 测序酶(13U/μL) | 0.3μL |

4. 将反应混合物与模板-引物混合，放入热循环仪，按如下程序延伸引物。

i. 8min 内从  $10^{\circ}$ C 梯度升温至  $37^{\circ}$ C。

ii.  $37^{\circ}$ C保温8min。

iii. 快速梯度升温至  $94^{\circ}$ C，保温 2min。

iv. 快速梯度降温至  $10^{\circ}$ C，加入  $1.2 \mu L$  稀释的测序酶（1:4 稀释）， $10^{\circ}$ C 保温 5min。

v. 8min 内从  $10^{\circ}$ C 梯度升温至  $37^{\circ}$ C。

vi.  $37^{\circ}$ C 保温 8min。

5. 用水稀释样品至终体积为  $60 \mu L$ 。

## Round B: PCR 扩增

6. 按以下配方准备 Round B 反应物:

| Round A 模板 | 15μL |
| --- | --- |
| MgCl2 | 8μL |
| PCR 缓冲液 (10×) | 10μL |
| dNTP (100×) | 1μL |
| 引物 B (100pmol/μL) | 1μL |
| Taq 聚合酶 | 1μL |
| 水 | 64μL |

7. 将管子放入热循环仪，按以下程序扩增模板。

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 15~35 循环 | 94°C 30s | 40°C 30s,然后 50°C 30s | 72°C 2min |

注: $4^{\circ}$ C恒温放置。

根据起始材料的量，运行程序 15～35 个循环。

为了优化循环数，应每 2 个循环取出一部分溶液以监测扩增的进展。最好使用最少的循环数产生可见的模糊带形（见步骤 8）。

▲必须确认阴性对照中无 DNA。

8. 取 $5\mu \mathrm{L}$ 反应液，进行 $1\%$ 的琼脂糖凝胶电泳。应当在 500bp 和 100bp 之间出现 DNA 的模糊带形。

9. 使用 Round C 程序、方案 7 或方案 8，标记 DNA。

## Round C: 花青染料标记或氨基烯丙基活化 DNA

10. 准备 Round C 反应液:

| Round B 模板 | 10~15μL |
| --- | --- |
| $MgCl_2$ | 8μL |
| PCR 缓冲液(10×) | 10μL |
| aa-dNTP/Cy-dNTP (100×) | 1μL |
| 引物 B (100pmol/μL) | 1μL |
| Taq 聚合酶 | 1μL |
| 水 | 63~68μL |

11. 将管子置于热循环仪，然后按如下程序标记模板:

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 15~25 循环 | 94°C 30s | 40°C 30s,然后 50°C 30s | 72°C 2min |

注: $4^{\circ}$ C恒温放置。

程序运行 10\~25 个循环。

循环数凭经验确定，即产生  $2 \sim 3 \mu g$  杂交用材料所需的最少循环数。

12. 如果在 Round C 中使用 aa-dNTP，需去除 Tris 缓冲液使样品脱盐，因为 Tris 会干扰染料的偶联。在含有样品的 Microcon 30 中加入 400μL 水，然后 12 000r/min 离心 8min。再加入 500μL 水重复此步骤。

13. Cy-染料的偶联按照方案 8 步骤 11 进行。

![](images/page_76_image_14.jpg)

## 讨论

此扩增方案的产品是双链 DNA，测定吸光度对 DNA 进行定量（见第 2 章），根据 DNA 的投入量计算扩增倍数。初次使用此方案的用户，可以用凝胶电泳来检测扩增 DNA 的大小分布。

![](images/page_76_image_17.jpg)

## 配方

为了正确使用本方案中所用的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

aa-dNTP/Cy-dNTP 混合物 (100×)

| 试剂 | 终浓度 |
| --- | --- |
| dATP | 25mmol/L |
| dCTP | 25mmol/L |
| dGTP | 25mmol/L |
| dTTP | 10mmol/L |
| 氨基烯丙基-dUTP 或 CyX-dUTP | 15mmol/L |

注:aa-dUTP 和 dTTP 的比值可改变或优化。

## 参考文献

Bohlander SK, Espinosa R III, Le Beau MM, Rowley JD, Diaz MO. 1992. A method for the rapid sequence-independent amplification of micro-dissected chromosomal material. Genomics 13: 1322–1324.

## 方案 3 核小体 DNA 和其他小于 500bp 的 DNA 的 T7 线性扩增（TLAD）

方案 2 广泛应用于基因组定位分析，尤其对于经超声剪切为约 500bp 的 DNA 效果最佳。但是，当 DNA 被剪切成小于 500bp 的片段时，PCR 过程中的倾向性将导致一些基因组位点的重现性发生偏离(Liu et al. 2003)。然而，一系列的应用需要扩增小于 500bp 的 DNA 片段，如对单核小体 DNA 的 ChIP 实验，其 DNA 片段长约 150bp(Liu et al. 2005)。在这些情况下，首选 T7 线性扩增 DNA（TLAD），与方案 2 中描述的扩增方法相比，它更精确地保持短 DNA 片段的均一性扩增。

利用 TLAD 对双链 DNA 的扩增起始于通过 TdT 将多聚腺嘧啶加于 DNA 的 3' 端。其次，用大肠杆菌 DNA 聚合酶的 Klenow 片段以及 T7-Poly（A）引物，产生带有 5' 端 T7 引物的互补片段。最后，T 结尾的 DNA 链的扩增产生适合基于 T7 转录的模板，最终产生扩增的 RNA（aRNA）。该技术避免了 PCR 中出现的 “jackpotting” 问题，即一个扩增早期事件导致某一个特定序列比例过高，因为 PCR 遵循指数动力学，而转录是一个线性增长过程。

完成此方案需要一些时间。表 10-1 给出了估算的每一步骤所需的时间。

表 10-1 小 DNA 分子的 T7 线性 DNA 扩增（TLAD）

| 步骤 | 时间 |
| --- | --- |
| TdT 加尾和净化 | 30~40min |
| 第二链合成及净化 | 2~2.5h |
| IVT | 5.5~20.5h |
| IVT 净化 | 15~30min |
| RNA 质量及数量评价 | 40~60min |
| 合计 | 9.5~25h |

注:TdT，末端转移酶；IVT，体外转录。

![](images/page_77_image_11.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

β-巯基乙醇

小牛肠磷酸酶 (CIP) (New England Biolabs, catalog nos. M0290S 或 M0290L)

$\mathrm{CoCl}_{2}$ (5mmol/L)

双脱氧核苷酸加尾溶液(8%) (92mmol/L dTTP, 8mmol/L ddCTP) (Life Technologies)

dNTP 混合物 (5mmol/L) &lt;A&gt;

EDTA (0.5mol/L, pH 8.0) &lt;A&gt;

乙醇 (95%\~100%)

DNA 聚合酶 I 的 Klenow 片段(New England Biolabs)

矿物油

NEB 缓冲液 2 (10×) (New England Biolabs)

NEB 缓冲液 3 (10×) (New England Biolabs)

NTP 混合物 (75mmol/L)

试剂盒提供的反应缓冲液

无 RNase 的水

RNase 抑制剂

T7-A $_{18}$ B 引物

引物序列 5'-GCATTAGCGGCCGCGAAATTAATACGACTCACTATAGGGAG(A) $_{18}$ [B]，B 代表 C、G 或 T。引物应经过 HPLC、PAGE 或其他等效方法纯化。

T7 RNA 聚合酶

模板 DNA (最大 500ng/10μL)

末端转移酶 (TdT) (New England Biolabs, 目录号 M0315S 或 M0315L)

末端转移酶缓冲液 (5×) (Roche, 目录号 11243276103)

## 仪器设备

MinElute kit (QIAGEN, 目录号 28204)

无 RNA 酶/DNA 酶的小管(1.5mL)

无 RNA 酶的 PCR 管(0.2mL)

RNeasy Mini Kit (QIAGEN)

旋转蒸发仪 (如 SpeedVac)

热循环仪

真空管 (可选；参见步骤 17)

$37^{\circ} \mathrm{C}$ 水浴或者加热模块

![](images/page_78_image_33.jpg)

## 方法

## 用 CIP 处理携带 3' 端磷酸基团的样品

当源 DNA 经过剪切或 MNase 处理时，需用 CIP 进行处理。用 CIP 对 DNA 处理将去除其 3' 端磷酸基团，产生含游离羟基的 3' 端，这对于用 TdT 进行有效加尾是必需的。此步骤若失败，将可能导致扩增产物降低 50%。

## 1. 配制如下反应液:

| CIP (2.5 U) | 0.25μL |
| --- | --- |
| NEB 缓冲液 3 (10×) | 1μL |
| 模板 DNA (最大 500ng/10μL) | 8.75μL |

$37^{\circ}\mathrm{C}$ 反应 $1\mathrm{h}$。

每次反应可放大至每管  $100 \mu L$ 。

## 2. 按生产厂家提供的使用说明，用 MinElute 小柱净化 DNA，洗脱 DNA 至  $20 \mu L$ 。

对小于 100ng 的 DNA 进行操作时，按厂家（QIAGEN）提供的说明采用  $10 \mu L$  洗脱液，收率可能低于厂家声称的 80%。必要时，可将洗脱体积增至  $15 \sim 20 \mu L$ ，并在干燥过程中减少 DNA 的体积。

## 用末端转移酶进行加尾反应

## 3. 配制加尾反应液:

| TdT 缓冲液(5×) | 2μL |
| --- | --- |
| 8%ddCTP 与 100μmol/L dTTP 的混合液 | 0.5μL |
| CoCl2 (5 mmol/L) | 1.5μL |
| 模板 DNA(最多 75ng) | 5μL |
| TdT 酶(20U)a | 1μL |

a. 最后加。

不要使用 NEB 末端转移酶提供的 NEB 缓冲液 4，因为缓冲液中的 DTT 会使  $CoCl_{2}$  沉淀从而抑制反应。建议使用二甲砷酸盐缓冲液（1mol/L 的二甲砷酸钾，125mmol/L Tris-HCl，以及 1.25mg/mL BSA，pH 6.6），Roche 的酶提供此缓冲液，也可单独购买。使用此含砷的缓冲液时需注意，按照所在科研院所的适当的废物处理要求操作。

dNTP 混合物反复冻融勿超过 3 次。过多冻融将使 dNTP 降解并降低反应效率。

以获得约 1pmol 的模板分子为目标。实验的范围为每  $10 \mu L$  反应体系中 2.5～75ng DNA。可增加起始的模板量而扩大反应体积。对于 ChIP 样本，使用敏感的紫外可见分光光度计或荧光计对样品精确定量。如果 DNA 量是未知的，可扩大反应体积至  $20 \mu L$ ，以确保足量的 TdT 酶进行有效的加尾反应。注意，如果使用的酶量不足，此方案中后续步骤的效率将受到显著影响，并导致产量的明显降低（可低至正常预期产量的 5%～10%）。

我们强烈建议此方案中使用 NEB 的末端转移酶；其他来源的 TdT 酶尚不能满足需求。若使用 Roche 的重组 TdT，酶量需加倍。

4. 在反应液表面加 $1 \sim 2$ 滴矿物油以免在孵育过程中反应物蒸发。在 $37^{\circ} \mathrm{C}$ 孵育 $20 \mathrm{~min}$ 。

5. 加入  $2 \mu L$  （每  $10 \mu L$  反应体积） EDTA(0.5 mol/L, pH 8.0) 以终止反应。

6. 按照生产厂家提供的使用说明，用 MinElute 小柱净化 DNA。用  $20 \mu L$  洗脱 DNA。

在将反应物加入离心柱之前，如起始体积为  $10 \mu L$ ，则加入  $10 \mu L$  水使体积达到  $20 \mu L$ 。若 DNA 量少于 100ng，按照厂家的方案采用  $10 \mu L$  的洗脱体积，则回收率可低于 QIAGEN 声称的 80%。若需要可增加洗脱体积至  $15 \sim 20 \mu L$ ，然后晾干以减少体积。

## 用 Klenow 片段聚合酶进行第二链合成

## 7. 配制第二链合成反应体系:

| T7-A$_{18}$B 引物(25μmol/L) | 0.3μL |
| --- | --- |
| NEB 缓冲液 2 (10×) | 2.5μL |
| dNTP 混合物(5.0mmol/L) | 1μL |
| 水 | 0.2μL |
| 尾端加 T 的 DNA | 20μL |

如果模板非特异性产物的产生是一个显著问题，降低反应液体积同时维持反应物的浓度（尾端加 T 的 DNA 除外），具体范例见此方案末。

dNTP 混合物勿反复冻融超过 3 次。过多冻融将使 dNTP 降解并降低反应效率。