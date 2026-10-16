## 第2章 DNA分析

导言 琼脂糖凝胶电泳 63

DNA 片段分析 67

凝胶中 DNA 的回收 68

Southern 印迹 68

方案 | 1 琼脂糖凝胶电泳 73

2 琼脂糖凝胶中 DNA 的染色检测 76
3 聚丙烯酰胺凝胶电泳 80
4 聚丙烯酰胺凝胶中 DNA 的染色检测 85
5 聚丙烯酰胺凝胶中 DNA 的放射
自显影检测 86
6 碱性琼脂糖凝胶电泳 87
● 附加方案 碱性琼脂糖凝胶的放射
自显影 90
7 成像:放射自显影和感光成像 91
8 用玻璃珠从琼脂糖凝胶中回收
DNA 96

9 低熔点琼脂糖凝胶中 DNA 的回收:
有机溶剂抽提法 98
10 聚丙烯酰胺凝胶中 DNA 片段的回收:压碎与浸泡法 101
11 Southern 印迹 103
12 Southern 印迹:DNA 从一块琼脂糖凝胶同时向两张膜转移 110
13 采用放射性标记探针对固定在膜上的核酸 DNA 进行 Southern 杂交 112
● 附加方案 从膜上洗脱探针 117

信息栏 | 甲酰胺及其在分子克隆中的应用 119

快速杂交缓冲液 120

## 导言

琼脂糖凝胶电泳或聚丙烯酰胺凝胶电泳用于分离、分析、鉴定和纯化 DNA 片段（见下文信息栏中“利用电泳技术进行的早期 DNA 分析”）。该技术操作简单而迅速，并且能分离其他方法如密度梯度离心等不能充分分离的 DNA 片段。此外，凝胶中 DNA 的位置可以用低浓度荧光插入染料（如溴化乙锭或 SYBR Gold 染色）直接观察到，甚至含量低至 20pg 的双链 DNA 条带在紫外线（UV）照射下也能被直接检测到。如有需要，还可以从凝胶中回收这些 DNA 条带。

琼脂糖和聚丙烯酰胺凝胶能灌制成各种形状、大小和孔径不同的分离胶，也能以许多不同的构型和方位进行电泳。上述参数的选择主要取决于欲分离的DNA片段的大小。聚丙烯酰胺凝胶最适合分离小片段DNA（5～500bp），因为这种方法的分辨能力非常强，长度上相差1bp或质量上相差0.1%的DNA都可以彼此分离。虽然聚丙烯酰胺凝胶电泳快速并能容纳较大的DNA上样量，但是与琼脂糖凝胶电泳相比，在制备和操作上还是更繁琐些。聚丙烯酰胺凝胶电泳通常是在恒定电场中沿垂直方向进行泳动。

琼脂糖凝胶比聚丙烯酰胺凝胶的分辨率略低，但它的分离范围更大。50bp 到数兆碱基对的 DNA 都可以在不同浓度和构型的琼脂糖凝胶中得以分离。小片段 DNA（50～20 000bp）最适合在具有恒定强度和方向的电场中沿水平方位的琼脂糖凝胶内进行电泳分离。在这些条件下，DNA 泳动速率通常随 DNA 片段长度的增加而减少，但与电场强度成正比（McDonell et al. 1977；Fangman 1978；Calladine et al. 1991）。然而当 DNA 片段长度超过一个最大极限值时，以上简单相关性会被破坏，最大值主要是由凝胶的构成和电场强度所决定（Hervet and Bean 1987）。当线状双螺旋 DNA 的半径超过凝胶的孔径时就达到凝胶分辨率的极值。此时，DNA 不再被凝胶按其大小筛分，而必须以一端在前的方式在介质中迁移，就像通过曲折而又空间有限的管子。这种迁移模式称为“蠕行”（reptation）（de Gennes 1971）。因此，必须根据所需分离 DNA 片段的大小范围选择合适浓度的琼脂糖和聚丙烯胺凝胶（参见 Stellwagen 2009；Stellwagen and Stellwagen 2009）。

![](images/page_81_image_4.jpg)

## 琼脂糖凝胶电泳

## DNA 在琼脂糖凝胶中的迁移速率

下述因素影响 DNA 在琼脂糖凝胶中的迁移速率

\- 通过凝胶的电流。根据欧姆定律，

$$
V = I R
$$

式中，V 是电压；I 是电流（单位安培）；R 是电阻（单位欧姆）。因为用于电泳的缓冲液通常是微碱性的（pH 7.8～8.0），通过凝胶的 DNA 分子携带负电荷，并以所施加的电流形成的速率向阳极迁移。

\- DNA 分子的大小。双链 DNA 分子在凝胶基质迁移的速率与其碱基对数的常用对数（ $\log_{10}$ ）成反比（Helling et al. 1974）。大分子 DNA 摩擦阻力大，通过凝胶孔径的效率低于小分子 DNA，因此迁移速率慢。

\- 琼脂糖浓度。琼脂糖凝胶是由氢键和疏水作用聚合在一起的多孔胶体。在电流的作用下，DNA 线性分子通过一系列孔径泳动，这些孔径的有效直径取决于凝胶中琼脂糖的浓度（图 2-1）。在 DNA 电泳迁移率( $\mu$ )的对数和凝胶浓度( $\iota$ )之间存在线性

关系，这种相关性可以用方程式来表示

$$
\log \mu = \log \mu_ {0} - K _ {\mathrm{r}}
$$

式中， $\mu_{0}$ 是 DNA 自由电泳迁移率； $K_{r}$ 是阻滞系数，是一个与凝胶性质、迁移分子大小和形状相关的常数。

![](images/page_82_chart_5.jpg)

<details>
<summary>line</summary>

| 迁移距离/cm | 0.5% | 0.7% | 0.9% | 1.2% | 1.4% |
| --- | --- | --- | --- | --- | --- |
| 0.5 | ~4.5 | ~4.4 | ~4.3 | ~4.2 | ~4.1 |
| 1 | ~4.2 | ~4.0 | ~3.8 | ~3.6 | ~3.5 |
| 2 | ~3.8 | ~3.6 | ~3.4 | ~3.2 | ~3.1 |
| 3 | ~3.5 | ~3.3 | ~3.1 | ~2.9 | ~2.8 |
| 4 | ~3.2 | ~3.0 | ~2.8 | ~2.6 | ~2.5 |
| 5 | ~2.9 | ~2.7 | ~2.5 | ~2.3 | ~2.2 |
| 6 | ~2.8 | — | — | — | — |
</details>

图 2-1 DNA 大小及其电泳迁移率的相关性。

- DNA 的构象。超螺旋环状（I 型）、切口环状（II 型）和线性（III 型）DNA 在琼脂糖凝胶中迁移速率不同（Thorne 1996,1967）。上述三种类型 DNA 的相对迁移率主要取决于琼脂糖凝胶的浓度和类型，但是电流强度、缓冲液离子强度和 I 型超螺旋 DNA 的绞紧程度或密度也影响相对迁移率（Johnson and Grossman 1977）。在一些条件下，I 型 DNA 比 III 型 DNA 迁移得更快；在另一些条件下，顺序可能颠倒。绝大多数情况下，区分不同构象 DNA 的最佳方式是在电泳系统中加入未处理的环状 DNA 样品和在单一限制酶切位点经酶切消化后的同一线状 DNA 样品。
- 凝胶和电泳缓冲液中的染料。染料插入双链 DNA 造成其负电荷减少，而刚性和长度增加。因此，线状 DNA-染料复合物在凝胶中的迁移率约降低 $15\%$ (Sharp et al. 1973)。
- 施加电压。低电压时，线状 DNA 片段迁移率与所用的电压成正比。但是，电场强度升高时，高分子质量 DNA 片段的迁移率不成比例增加。所以，当电压增大时，琼脂糖凝胶分离的有效范围反而减小。要获得大于 2kb DNA 片段的良好分辨率，则所用电压不应高于 5～8V/cm。
- 琼脂糖种类。常见的琼脂糖主要有两种:标准琼脂糖和低熔点琼脂糖（Kirkpatrick 1990）。正在研制的第三种是熔点和凝点介于上述二者之间的琼脂糖，它兼有两者的特性。每一大类中都有不同种类的琼脂糖用于不同的分离目的，请见表2-1和表2-2以及相应的信息栏“琼脂糖的级别及其性质”。
- 电泳缓冲液。DNA 的泳动受电泳缓冲液的组成和离子强度的影响。缺乏离子（如用水替代电泳槽及凝胶中的缓冲液）则电导率降至很低，DNA 迁移极慢，或者完全不动。高离子强度时，如错用了 $10 \times$ 电泳缓冲液，电导率升高，即使应用适中的电压也会产生大量的热量。最严重时凝胶会熔化，DNA 会变性。

表 2-1 不同类型琼脂糖的性质

<table><tr><td>琼脂糖类型</td><td>凝结温度/°C</td><td>熔化温度/°C</td><td>商品名</td></tr><tr><td>标准琼脂糖</td><td></td><td></td><td></td></tr><tr><td>低电内渗</td><td>35~38</td><td>90~95</td><td>SeaKem LE (Lonza Walkersville)</td></tr><tr><td rowspan="3">从 Gelidium spp.分离</td><td></td><td></td><td>Agarose-LE (Affymetrix)</td></tr><tr><td></td><td></td><td>Low EEO Agarose (Agilent)</td></tr><tr><td></td><td></td><td>Molecular Biology Certified Grade (Bio-Rad)</td></tr><tr><td>标准琼脂糖</td><td></td><td></td><td></td></tr><tr><td>低电内渗</td><td>40~42</td><td>85~90</td><td>SeaKem HGT (Lonza Walkersville)</td></tr><tr><td>从 Gracilaria spp.分离</td><td></td><td></td><td>Agarose-HGT (Affymetrix)</td></tr><tr><td rowspan="3">高强度琼脂糖</td><td>34~43</td><td>85~95</td><td>FastLane (Lonza Walkersville)</td></tr><tr><td></td><td></td><td>SeaKem Gold (Lonza Walkersville)</td></tr><tr><td></td><td></td><td>Chromosomal Grade Agarose (Bio-Rad)</td></tr><tr><td>改良的低熔点/凝点琼脂糖</td><td></td><td></td><td></td></tr><tr><td rowspan="2">低熔点</td><td>25~35</td><td>63~65</td><td>SeaPlaque (Lonza Walkersville)</td></tr><tr><td>35</td><td>65</td><td>NuSieve GTG (Lonza Walkersville)</td></tr><tr><td>超低熔点</td><td>8~15</td><td>40~45</td><td>SeaPrep (Lonza Walkersville)</td></tr><tr><td rowspan="4">低黏性低熔点/凝点琼脂糖</td><td></td><td></td><td></td></tr><tr><td>25~30</td><td>70</td><td>InCert (Lonza Walkersville)</td></tr><tr><td>38</td><td>85</td><td>NuSieve 3:1 (Lonza Walkersville)</td></tr><tr><td>30</td><td>75</td><td>Agarose HS (Lonza Walkersville)</td></tr></table>

表 2-2 用不同类型琼脂糖分离 DNA 片段的范围

<table><tr><td rowspan="2">琼脂糖/%</td><td colspan="4">各种类型琼脂糖分辨DNA大小的范围</td></tr><tr><td>标准琼脂糖</td><td>高强度琼脂糖</td><td>低熔点/凝点琼脂糖</td><td>低黏性低熔点/凝点琼脂糖</td></tr><tr><td>0.3</td><td></td><td></td><td></td><td></td></tr><tr><td>0.5</td><td>700bp~25kb</td><td></td><td></td><td></td></tr><tr><td>0.8</td><td>500bp~15kb</td><td>800bp~10kb</td><td>800bp~10kb</td><td></td></tr><tr><td>1.0</td><td>250bp~12kb</td><td>400bp~8kb</td><td>400bp~8kb</td><td></td></tr><tr><td>1.2</td><td>150bp~6kb</td><td>300bp~7kb</td><td>300bp~7kb</td><td></td></tr><tr><td>1.5</td><td>80bp~4kb</td><td>200bp~4kb</td><td>200bp~4kb</td><td></td></tr><tr><td>2.0</td><td></td><td></td><td>100bp~3kb</td><td>100bp~3kb</td></tr><tr><td>3.0</td><td></td><td></td><td>500bp~1kb</td><td>500bp~1kb</td></tr><tr><td>4.0</td><td></td><td></td><td></td><td>100bp~500bp</td></tr><tr><td>6.0</td><td></td><td></td><td></td><td>10bp~100bp</td></tr></table>

## 琼脂糖的级别及其性质

## 标准（高熔点）琼脂糖

制造标准（高熔点）琼脂糖的原料是两种海藻 Gelidium 和 Gracilaria。这两种琼脂糖的凝点和熔点有所不同，但是在实际应用中每种来源的琼脂糖都可以用于分析或分离 1kb～25kb 范围的 DNA 片段。几种市售级别的琼脂糖测试表明:①溴化乙锭染色后的背景荧光很低；②没有 DNA 酶和 RNA 酶；③很低的限制酶和连接酶抑制作用；④产生适量的电内渗（EEO，请见后文）。

新型标准琼脂糖具有高凝胶强度和低电内渗（EEO），可以灌制浓度低至0.3%的凝胶。这种凝胶用于常规电泳能方便地分离高分子质量DNA（高达60kb）。DNA在任何浓度的这种新型凝胶中的迁移速率都比在以往采用的标准琼脂糖凝胶中加快10%～20%，加快程度与缓冲液类型和浓度相关。

## 低熔点/凝点琼脂糖

通过羟乙基化修饰的琼脂糖在较低的温度下熔化，羟乙基化替代的程度决定准确的熔化和凝结温度。低熔点/凝点琼脂糖主要用于 DNA 的快速回收，因为大多数该类型琼脂糖在  $65^{\circ}$ C 熔化，这个温度远低于双链 DNA 的解链温度。这种特性使它还可以用于 DNA 的简单纯化和酶处理（限制酶消化/连接），并可在熔化的凝胶中直接进行核酸的细菌转化。如同标准琼脂糖的情况一样，制造商供应的各类低熔点琼脂糖已经经过检测，用溴化乙锭染色后显示很低的背景荧光；没有 DNA 酶和 RNA 酶活性；只对限制酶和连接酶产生极低的抑制作用。低熔点琼脂糖不仅在低温下熔化，而且只在低温下凝结。该特性使它在  $30 \sim 35^{\circ}$ C 范围仍呈液态，所以能无损伤地包埋细胞。

## 化学修饰的琼脂糖

商业化的经化学修饰的琼脂糖比等浓度的标准琼脂糖具有更高的筛分能力（表 2-1 和表 2-2）。该发现使琼脂糖的分辨能力接近丙烯酰胺凝胶，因此可用于 PCR 产物、小片段 DNA 和小 RNA（<1kb）的分离。现在它能分辨差异低至 4bp 的 DNA 和分离 200～800bp 范围内长度相差仅 2% 的 DNA 片段（见表 2-2）。

由于不同厂家提供的产品有所不同，建议仔细阅读产品说明以获取关于不同琼脂糖产品的更准确信息。

## 电内渗

在琼脂糖凝胶中，核酸向阳极迁移的速率受到电内渗的影响。这个作用是由于离子化的酸性基团（通常是硫酸盐）附着到琼脂糖凝胶的多糖基质引起的。酸性基团导致缓冲液中产生正电荷反向离子，它们向阴极迁移，从而造成与 DNA 反方向迁移的液流。

琼脂糖中负电荷密度越高，EEO流越大，核酸片段的分离效果越差。小片段DNA（＜10kb）的延迟效应不明显，但是大分子DNA却十分显著，尤其在PFGE时。为避免此类问题，最好从声誉良好的厂家购买，并且使用低水平电内渗的琼脂糖。市售的无电内渗琼脂糖并不理想，有两个理由:它们通过加入正电荷基团进行化学修饰，以中和凝胶中的硫酸化多糖，但是这样将可能抑制后续的酶反应；它们也常被掺入刺槐豆胶（locust bean gum），这样会延迟水从凝胶中的排除（Kirkpatrick 1990）。

## 电泳缓冲液

有几种缓冲液适用于天然双链 DNA 的电泳，它们包括 Tris-乙酸盐和 EDTA 缓冲液（pH8.0，TAE，也称为 E 缓冲液）、Tris-硼酸盐和 EDTA 电泳缓冲液（TBE）或 Tris-磷酸盐和 EDTA 电泳缓冲液（TPE），工作浓度约 50mmol/L，pH7.5～7.8。各种电泳缓冲液通常配制成浓溶液于温室存放（见每种实验方案后的配方）。这些缓冲液都非常有效，选择哪一种使用主要看个人工作习惯。三者之中 TAE 的缓冲容量最低，如长时间电泳会被消耗。此时凝胶的阳极一侧将发生酸性化，凝胶中向阳极迁移的溴酚蓝的颜色呈现从蓝紫色到黄色的变化。该颜色变化从 pH4.6 开始，到 pH3.0 终止。定期更换缓冲液或调换两个电极池的缓冲液可以防止 TAE 的消耗。TBE 和 TPE 比 TAE 花费稍贵些，但是它们有高得多的缓冲容量。双链线状 DNA 片段在 TAE 中比在 TBE 或 TPE 中迁移速率快 10% 左右。对于高分子质量 DNA，TAE 的分辨率高于 TBE 或 TPE；对于低分子质量 DNA，TAE 要差些。此差别也许能解释下述现象:高度复杂混合物中的 DNA 片段，如哺乳类动物 DNA，用 TAE 电泳可有较高分辨率。因此，用于分析复杂基因组的 Southern 印迹（Southern blot）均用 TAE 作为电泳缓冲液制备凝胶和电泳。超螺旋 DNA 在 TAE 中的电泳分辨率要好于 TBE。

## 凝胶上样缓冲液

加样到凝胶孔之前，混合上样缓冲液和样品。上样缓冲液有三个作用:可增加样品密度以保证 DNA 均匀沉入加样孔内；使样品带有颜色便于简化上样过程；其中的染料可以预定速率向阳极迁移。溴酚蓝在琼脂糖凝胶中的迁移速率是二甲苯蓝 FF 的 2.2 倍，这一特性与琼脂糖浓度无关。在  $0.5 \times TBE$  琼脂糖凝胶电泳中溴酚蓝迁移速率约与长 300bp 的双链线状 DNA 相同，而二甲苯蓝 FF 约与长 4000bp 的 DNA 相同。上述关系在浓度范围 0.5%～1.4% 琼脂糖凝胶中基本不受凝胶浓度变化的影响。用哪种上样缓冲液可依据个人习惯，各种上样缓冲液配方列于实验方案后面。

![](images/page_85_image_4.jpg)

## DNA 片段分析

经电泳分离后，可以通过方案2（琼脂糖凝胶）和方案4（丙烯酰胺凝胶）所描述的染色法分析DNA片段。为了进一步观察，DNA片段可以从凝胶中回收，或者转移到固相支持物上进行杂交。使用方案 $11\sim 13$ 所描述的方法之一从凝胶中回收DNA片段。在Southern印迹中，通过琼脂糖凝胶电泳分离的DNA片段发生了原位变性，并且从凝胶中转移到膜上或过滤器上，这些在方案11和方案12有所介绍。通过方案13描述的放射性标记探针杂交可以研究转移到膜上的特定DNA序列。

## 利用电泳技术进行的早期 DNA 分析

利用电泳通过支持介质分析 DNA 的方法最初由 Vin Thorne 提出，他是 20 世纪 60 年代中期在格拉斯哥病毒研究所工作的生化学家和病毒学家。他从纯化的多瘤病毒（polyomavirus）颗粒中提取到多种形式 DNA，并对建立分析检测这些 DNA 的新方法很感兴趣。他推断:摩擦阻力和电场力结合将会分离不同形状、大小的 DNA 分子。利用琼脂糖凝胶电泳，他成功分离了同位素标记的超螺旋、切口和线状形式的多瘤病毒 DNA（Thorne 1966，1967）。那时，Thorne 的工作没有引起足够的注意。直到 70 年代早期，限制性内切核酸酶的应用提供了分析大分子 DNA 的可能性，而且发现了凝胶中少量非放射性标记 DNA 的检测方法后，他的研究才得到重视。

在凝胶中用溴化乙锭染料标记 DNA 这一发现似乎是由两个研究组分别提出的。Aaij 和 Borst（1972）的方法是将凝胶浸入浓的染料溶液，并且采用较长的脱色过程降低背景荧光。而冷泉港实验室的一组研究者发现副流感嗜血菌（Haemophilus parainfluenzae）有两种限制酶活性，并尝试用离子交换色谱分离该酶。为了找出快速检测层析柱组分的方法，他们决定采用低浓度溴化乙锭染色含有 SV40 DNA 片段的琼脂糖凝胶。他们很快就认识到:染料能掺入凝胶和电泳缓冲液，对线状 DNA 片段在凝胶中的迁移没有明显影响。在他们（Sharp et al. 1973）的论文中介绍的技术方法已沿用至今，且基本没有变动。

1972～1975年间，研究者们用迅速增多的限制性内切核酸酶绘制感兴趣的DNA酶切图谱时，琼脂糖凝胶的使用明显增加。那时，凝胶在玻璃吸管内灌制，然后用自制的电源在电泳槽中进行垂直电泳。DNA样品在切开的凝胶小圆柱上分析。第一个现代电泳装置是Walter Schaffner发明的，他当时在Zurich读研究生。由于认识到琼脂糖凝胶的电阻基本上与周围的缓冲液相同，他构建了水平电泳槽放置浸没的凝胶，这样的凝胶可以供12个以上的样品电泳。Schaffner分送该装置的设计图给任何需要它的人，直至大家不再怀疑装置的性能。小玻璃管灌制的圆柱凝胶很快被弃用，新的浸没式凝胶沿用至今。

![](images/page_86_image_2.jpg)

## 凝胶中 DNA 的回收

从凝胶中纯化DNA是DNA片段亚克隆过程中的关键步骤。多年以来已经发表了许多从琼脂糖和聚丙烯酰胺凝胶中回收DNA的方法。其中许多方法可能在一定程度上有效，但是它们没有广泛被采纳，这说明这些方法缺乏有效性、重复性、耐用性。传统方法中我们熟悉的问题包括:

- 从琼脂糖凝胶中回收的DNA通常难于连接、消化和放射性标记
- 不能有效地回收大片段 DNA
- 不能有效地回收小量 DNA

鉴于这些问题，如能设计一个方案不涉及凝胶中 DNA 的分离将是最好的选择。PCR 由于兼具快速、经济的特点，往往是个较好的备选方案。但是如果 PCR 在实际操作中不可行，最好利用目前已经广泛应用的商业产品从琼脂糖凝胶中回收 DNA。大多数试剂盒的制造商提供的数据涉及:从不同浓度的琼脂糖凝胶中回收不同大小 DNA 片段的效率，通过回收 DNA 是否能够作为模板或底物进而判断其纯度。这些试剂盒在重复性、可靠性、有效性和快速性等方面的优点因其高成本而大打折扣。但总的来说，试剂盒还是取代了老旧的传统方法。

许多商品化试剂盒操作的核心步骤是将 DNA 结合到硅胶表面。含有 DNA 条带的琼脂糖凝胶块溶解在离散缓冲液（chaotropic buffer）中，这破坏了琼脂糖聚合物之间的氢键。解离的 DNA 滞留在硅胶珠或膜上，经水溶液或含有低浓度盐或乙醇的缓冲液回收。这种类型的试剂盒包括:QIAEX II Gel Extraction 试剂盒（QIAGEN）、Wizard SV 试剂盒（Promega）、Ultra Silica Bead 试剂盒（ThermoFisher）、NucleoSpin Extract IIa（Clontech）和 GenElute（Sigma-Aldrich）。

与此相反，Millipore Montage 试剂盒的工作原理不同:琼脂糖凝胶切片通过内置的雾化器设备高速离心，使凝胶呈碎片状并被压缩，从挤出的缓冲液中收集该 DNA。

因为有些试剂盒需要特别制备凝胶电泳缓冲液，所以使用试剂盒前，应仔细阅读制造商的说明。

## 琼脂糖凝胶中回收 DNA 的非试剂盒技术

非试剂盒技术回收DNA的旧方法存在一个常见问题，即很难权衡从凝胶中回收DNA的效率和纯度。如果从凝胶中分离的DNA用于酶促反应，选择的技术最好能保证适当的产率且能避免严重污染。详细解释见方案8和方案9。

![](images/page_86_image_15.jpg)

## Southern 印迹

Southern 转移和杂交（Southern 1975）通过对特异性探针结合的基因组 DNA 片段内或其周围序列进行限制性内切核酸酶酶切位点作图来研究基因在基因组内部是如何组织排列的。基因组 DNA 首先用一种或几种限制性内切核酸酶消化，消化后的片段通过标准琼脂糖电泳按照大小进行分离。然后 DNA 经过原位变性，从胶上转移到固相支持物上（通常是尼龙膜或硝酸纤维素膜）。附着于膜上的 DNA 与标记的 DNA、RNA 或者寡核苷酸探针杂交，通过特定的检测方法，如放射自显影，可以确定与探针配对的条带位置。通过对经过不同限制性内切核酸酶（单一的或联合使用的）消化过的基因组 DNA 产生条带的大小以及数量的估计，可以判断靶基因上下游限制性内切核酸酶的位置。

Southern 印迹方法在刚建立后的 2～3 年里, 其灵敏度还不能够检测到哺乳类动物 DNA中的单拷贝序列，当时的放射自显影背景有许多杂点或杂带（如 Botchan et al.1976），在今天那样的结果是不能发表的。但是，几年来各个领域取得的显著进步提高了杂交的灵敏度及重复性，现在我们通常都可以获得完美的杂交结果。最为重要的改进是使用了比硝酸纤维素膜更耐用、结合能力更强的尼龙膜作为固相支持物。另外，DNA 现在经过转移后共价结合于膜上，避免了由于高温处理硝酸纤维素膜时 DNA 被洗脱而引起的问题（Haas et al.1972）。其他的进步还包括:

- 多种更有效的从胶上转移 DNA 到膜上的方法，如向下毛细管转移（Lichtenstein et al.1990；Chomczynski 1992）、真空印迹（Medveczky et al.1987；Olszewska and Jones 1988；Trnovsky 1992）双向印迹（请见方案 9）、碱性缓冲液中转移（Reed and Mann 1985）。
- 简洁的体外标记，可获得更高特异性的探针（Feinberg and Vogelstein 1983, 1984）。
- 更高效的可防止放射性标记探针与膜非特异性结合的封闭剂（Church and Gilbert 1984）。
- 使用高敏感度的感光影像仪高效显像。

这些改进方法在 “如何将 DNA 从胶上转移到膜上” 的方案 11 和方案 12 可见。放射性标记探针与固定化 DNA 杂交的方案见方案 13。以上技术方案适用于经限制性内切核酸酶消化后的哺乳类动物基因组 DNA 的 Southern 分析，但是也很容易用于经脉冲凝胶电泳分离的大分子 DNA，以及经限制性内切核酸酶消化的质粒、黏性质粒、 $\lambda$ 噬菌体、细菌人工染色体（BAC）、酵母人工染色体（YAC）。

## 将 DNA 从凝胶转移到固相支持物的方法

将经电泳分离的DNA从凝胶转移到二维固相支持物是Southern杂交的关键步骤。下面讲述了5种将DNA片段从凝胶转移到固相支持物（尼龙膜或硝酸纤维素膜）的方法。

## 向上毛细管转移法

在向上毛细管转移法中，DNA 片段由向上的液流携带从凝胶转移并聚集于固相支持物表面（Southern 1975）。液体通过毛细管作用抽吸过凝胶，借助于一叠干燥的吸水纸巾产生并维持毛细管作用（图 2-2）。转移的速率取决于 DNA 片段的大小和凝胶中琼脂糖的浓度。小片段 DNA（<1kb）大约需要 1h 能够从 0.7% 的琼脂糖凝胶中成功转移；而大片段 DNA 的转移速率和效率会明显下降。例如，大于 15kb DNA 的毛细管转移至少要进行 18h，而且即使 18h 后转移仍不完全。大片段 DNA 的转移效率取决于其在脱水前脱离凝胶分子所占的比例。在洗脱过程中，液体从液池及凝胶本身的孔隙中抽吸出来，这就使凝胶成了阻滞 DNA 分子通过的橡胶性物质。这一因长时间转移所引发的脱水问题有望通过在毛细管转移前对 DNA 进行不完全酸碱水解而得以缓解（Wahl et al. 1979; Meinkoth and Wahl 1984）。凝胶中的 DNA 先用弱酸（引起部分脱嘌呤作用）后用强碱（水解脱嘌呤部位的磷酸二酯主链）处理。产生的 DNA 片段（约 1kb）可以快速高效地从凝胶上转移。然而，重要的是要防止过强的脱嘌呤作用，否则 DNA 断裂成过小的片段，不能有效地结合到固相支持物上。脱嘌呤及水解作用亦可导致在最后的放射自显影片上出现条带模糊的现象，这可能是在转移过程中由于 DNA 扩散程度加重引起的。因此建议只有预知靶 DNA 片段长度大于 15kb 时，才进行脱嘌呤及水解处理。

![](images/page_88_image_2.jpg)

<details>
<summary>text_image</summary>

纸巾
重物
玻璃板
硝酸纤维素膜或尼龙膜
Whatman 3MM滤纸
转移缓冲液
Whatman 3MM滤纸
凝胶
支持物
</details>

图2-2向上毛细管转移法转移琼脂糖凝胶中的DNA。从储液池中吸出的缓冲液流经凝胶至一叠纸巾中。DNA随液流从凝胶上洗脱下来，并沉积在硝酸纤维素膜或尼龙膜上。纸巾上面的重物保证了转移系统中各层之间的紧密连接。

## 向下毛细管转移法

在向下毛细管转移法中，DNA 片段由向下的碱性缓冲液流携带转移并聚集于带电荷的尼龙膜表面。为实现向下的转移，有各种不同的储液池、纱布层排列，以及各种不同的转移缓冲液配方（参阅 Lichtenstein et al. 1990；Chomczynski 1992）。我们目前的最优方案是采用 0.4mol/L NaOH 溶液以及一套可以使转移缓冲液从储液池，经过纱布层流向凝胶上部，并进而借助凝胶下层纸巾的作用而使转移缓冲液通过凝胶的装置。这种方法与传统的向上转移相比更快捷，并且信号强度提高约 30%。这种改进可能是由于凝胶上没有了顶部重物的压力从而使 DNA 片段更容易通过凝胶中的小空隙。

## 同时向两张膜转移

在同时向两张膜转移的方法中，当靶 DNA 浓度较高时（如克隆 DNA 限制性内切核酸酶消化产物），利用毛细管法可将 DNA 同时并快捷地从一块凝胶转移到两张尼龙膜或硝酸纤维素膜上。转移缓冲液唯一的来源是凝胶自身含有的液体，因此转移效率相对较差。如果实验需要较高的灵敏度（如检测哺乳类动物 DNA 中的单拷贝序列），不推荐使用这种方法；但是如果是对质粒、噬菌体、黏性质粒或简单的有机体（如酿酒酵母和果蝇）的基因组进行 Southern 杂交分析，则足够了。实际上，只有少数采用这种方法转移的哺乳类动物基因组 DNA 能够用常规的信号检测方法实现检测。

## 电转移

电转移不适用于使用硝酸纤维素滤膜作为固相支持物，因为核酸结合到这种滤膜上所要求缓冲液的离子强度要高。这些缓冲液传导电流的效率极高，必须采用大体积来保证该电泳缓冲液系统的缓冲容量不会因电解而耗尽。另外，需要充分的外冷却来克服欧姆热。

最近由于带电荷的尼龙膜的出现，电转移法又焕发了生机。这种方法被应用于经聚丙烯酰胺凝胶电泳分离的小分子DNA片段的Southern杂交（Stellwag and Dahlberg 1980; Church and Gilbert 1984）。在离子强度极低的缓冲液中，小至50bp的核酸也可以结合到这些带电荷的尼龙膜上（Reed and Mann 1985）。

虽然单链 DNA 和 RNA 可以直接转移，但双链 DNA 片段必须先经过如方案 11 所述的原位变性，随后中和凝胶并将其浸于电泳缓冲液（如  $1 \times TBE$ ）中，最后将其夹放于大电泳槽内平行电极之间的多孔板之间。完成转移这一步骤的时间主要取决于 DNA 片段的大小、凝胶的孔径和所采用的电场强度。然而，因为高分子质量的核酸也能够从凝胶中快速迁移，所以不必进行脱嘌呤及脱水处理，通常  $2 \sim 3h$  内可以转移完毕。因为电转移需要相对较大的电流，故往往难以使电泳缓冲液维持在利于 DNA 有效转移的特定温度。许多商业化的电转移装置附有冷却设备，但也有一些只能在冷室中进行。

## 真空转移

在真空转移中，DNA 或 RNA 可以从凝胶快速并定量地转移。目前商品化的真空转移装置有数种。在这些装置内，硝酸纤维素滤膜或尼龙膜置于真空室上方的多孔屏之上，而凝胶则放在与膜相接触的位置。上槽缓冲液将核酸从凝胶中洗脱，并使其聚集在膜上。

真空转移较毛细管转移更为有效，而且更为快捷。经部分脱嘌呤处理和碱变性处理的DNA在30min内即可从正常厚度（4～5mm）和正常琼脂糖浓度（＜1%）的凝胶中定量地转移。如果操作细心，采用真空转移方法进行Southern杂交可以使杂交信号增强2～3倍(Olszewska and Jones 1988)。

只要操作仔细以保证真空均匀地作用在凝胶的整个表面，所有商品化的该类装置均能正常工作。但应特别注意水平放置的琼脂糖凝胶上的加样孔，因为它们在准备转移过程中极易破裂。如果加样孔破裂，就应在转移前将其修去（只要孔不破裂就不必如此）。还有一点也很重要，即在转移过程中所采用的真空度不宜过高。如果真空超过 60cm 水柱，凝胶将被压缩变紧，转移效率会下降。

## 用于 Southern 及 Northern 杂交的膜

在将近 20 年的时间里，唯一可用于固定 DNA 的固相支持物是硝酸纤维素膜，其最初的使用形式是粉末状（Hall and Spiegelman 1961），稍后出现了片状（Nygaard and Hall 1960; Gillespie and Spiegelman 1965; Southern 1975）。Northern 杂交最初全部是将 RNA 固定于活化的纤维素纸上进行的（Alwine et al. 1977; Seed 1982）。但是不久，人们发现经乙二醛、甲醛及羟化甲基汞变性后的 RNA 可以紧密地结合于硝酸纤维素膜上。几年内，硝酸纤维素膜成为 Southern 及 Northern 杂交共用的固相支持物。尽管取得了显著的成功，硝酸纤维素膜仍不是固相杂交的理想支持物，原因如下:

- 结合核酸的能力较低（约 $50 \sim 100 \mu \mathrm{g} / \mathrm{cm}^{2}$），且随 RNA 和 DNA 的大小不同而变化。尤其是 $< 400 \mathrm{bp}$ 的核酸不能有效地保留于硝酸纤维素膜上。
- DNA 和 RNA 通过疏水作用而不是共价作用力结合于硝酸纤维膜上，在高温洗膜或者杂交操作过程中会缓慢脱落（Haas et al.1972）。
- 硝酸纤维素膜在真空 $80^{\circ} \mathrm{C}$ 烘烤时变脆，而这一步对于固定核酸是必需的。这种易碎的膜不能用于超过 $1 \sim 2$ 次杂交或者高温洗膜。使用具有较高拉伸强度的混合酯类膜可以减轻这一问题，但不能完全消除。
- 如果要成功用于核酸杂交或 Western 印迹实验，在保存硝酸纤维素膜时要多加小心。如果湿度过高，膜将从空气中吸潮膨胀导致卷曲皱缩；如果湿度过低，硝酸纤维素膜将变干并且带静电荷。这种状态下，膜容易折裂、破损且极难浸湿。世界上的大部分地区都需要改变硝酸纤维素膜的储藏条件以适应不同的天气条件。例如，在北京湿热的夏季，硝酸纤维素膜需要密闭保存并放置干燥剂；冬天则要用加湿纸取代干燥剂。这样做的目的是为了保证膜无折痕，易均匀、快速浸湿（30s 或以下），且用水饱和时呈淡蓝色。

硝酸纤维素膜的这些问题因为几种不同的尼龙膜的引入而得到解决。尼龙膜较硝酸纤维素膜耐用，可以不可逆地结合核酸（Reed and Mann 1985）。固定化的核酸可以连续地与几种不同探针的杂交反应而保持尼龙膜不破损。另外，由于核酸可以在低离子强度缓冲液中固定到尼龙膜上，所以可以用电转移将核酸从凝胶上转移到尼龙膜上。这种方法在毛细管或真空转移效率很低时尤其有用，如需要从聚丙烯酰胺凝胶上转移 DNA 这一情况。

商业化可获得的尼龙膜有两种:未加修饰的（或者说中性的）尼龙膜以及带电荷修饰的尼龙膜，即带有氨基基团，被称为正电荷或（+）尼龙膜。两种尼龙膜都可以结合单链及双链核酸，并且在多种溶液中其 DNA 保留率定量可测，如水、0.25mol/L HCl 及 0.4 mol/L

NaOH 等。带电荷修饰的尼龙膜结合核酸的能力较强（表 2-3），但是由于 DNA 或 RNA 中带负电荷的磷酸基团容易结合聚合物表面带正电荷的基团，从而导致或者至少部分导致了背景水平的升高。这一问题可以通过增加预杂交及杂交过程中封闭剂的数量得到解决。

表 2-3 Southern 印迹及杂交中所使用的膜的性质

<table><tr><td rowspan="2">性质</td><td colspan="3">膜的种类</td></tr><tr><td>硝酸纤维素膜</td><td>中性尼龙膜</td><td>带电荷的尼龙膜</td></tr><tr><td>结合容量/(μg 核酸/cm2)</td><td>80~120</td><td>约 100</td><td>400~500</td></tr><tr><td>实现最大结合能力所需的核酸大小</td><td>&gt;400 bp</td><td>&gt;50 bp</td><td>&gt;50 bp</td></tr><tr><td>转移缓冲液</td><td>中性 pH 下的高离子强度</td><td>低离子强度,pH 范围较广</td><td></td></tr><tr><td>固定</td><td>真空条件下 80°C烘烤 2 h</td><td>70°C烘烤 1 h;无需真空条件或者温和的碱性条件,或者 254 nm 紫外照射;潮湿的膜曝露于 1.6 kJ/m2;干燥的膜曝露于 160 kJ/m2</td><td></td></tr><tr><td rowspan="4">商业产品</td><td></td><td>Hybond-N</td><td>Hybond-N+</td></tr><tr><td></td><td>GeneScreen</td><td>Zeta-Probe</td></tr><tr><td></td><td></td><td>Nytran+</td></tr><tr><td></td><td></td><td>GeneScreen Plus</td></tr></table>

注:二氟聚偏二乙烯（PVDF）膜通常不用于 Northern 或 Southern 转移。但是，由于 PVDF 膜具有较高的机械强度以及较高的结合蛋白的能力，所以比硝酸纤维素膜更适合于 Western 印迹实验。尼龙膜非特异吸收免疫学探针的水平高得让人难以接受，所以不应该用于 Western 印迹。

有许多种不同类型的尼龙膜可供选择，它们所带电荷的类型及程度、适用方法和尼龙网眼密度都各不相同。每一个制造商都为将核酸转移到其产品提供了特殊的使用说明。由于这些规则已经证实可以获得最佳结果，使用时应当严格遵守这些规则。

## 参考文献

- Aaij C, Borst P. 1972. The gel electrophoresis of DNA. Biochim Biophys Acta 269: 192–200.
- Alwine JC, Kemp DJ, Stark GR. 1977. Method for detection of specific RNAs in agarose gels by transfer to diazobenzyloxymethyl-paper and hybridization with DNA probes. Proc Natl Acad Sci 74: 5350–5354.
- Botchan M, Topp W, Sambrook J. 1976. The arrangement of simian virus 40 sequences in the DNA of transformed cells. Cell 9: 269–287.
- Calladine CR, Collis CM, Drew HR, Mott MR. 1991. A study of electrophoretic mobility of DNA in agarose and polyacrylamide gels. J Mol Biol 221: 981–1005.
- Chomczynski P. 1992. One-hour downward alkaline capillary transfer for blotting of DNA and RNA. Anal Biochem 201: 134–139.
- Church GM, Gilbert W. 1984. Genomic sequencing. Proc Natl Acad Sci 81:1991–1995.
- de Gennes PG. 1971. Reptation of a polymer chain in the presence of fixed obstacles. J Chem Phys 55: 572–579.
- Fangman WL. 1978. Separation of very large DNA molecules by gel electrophoresis. Nucleic Acids Res 5: 653–665.
- Feinberg AP, Vogelstein B. 1983. A technique for radiolabeling DNA restriction endonuclease fragments to high specific activity. Anal Biochem 132: 6–13.
- Feinberg AP, Vogelstein B. 1984. A technique for radiolabeling DNA restriction endonuclease fragments to high specific activity. [Addendum] Anal Biochem 137: 266–267.
- Gillespie D, Spiegelman S. 1965. A quantitative assay for DNA–RNA hybrids with DNA immobilized on a membrane. J Mol Biol 12: 829–842.
- Haas M, Vogt M, Dulbecco R. 1972. Loss of simian virus 40 DNA–RNA hybrids from nitrocellulose membranes; implications for the study of virus–host DNA interactions. Proc Natl Acad Sci 69: 2160–2164.
- Hall BD, Spiegelman S. 1961. Sequence complementarity of T2-DNA and T2-specific RNA. Proc Natl Acad Sci 47: 137–163.
- Helling RB, Goodman HM, Boyer HW. 1974. Analysis of endonuclease R-EcoRI fragments of DNA from lambdoid bacteriophages and other viruses by agarose-gel electrophoresis. J Virol 14: 1235–1244.
- Hervet H, Bean CP. 1987. Electrophoretic mobility of  $\lambda$  phage HIND III and HAE III DNA fragments in agarose gels: A detailed study. Biopolymers 26: 727–742.
- Johnson PH, Grossman LI. 1977. Electrophoresis of DNA in agarose gels. Optimizing separations of conformational isomers of double- and single-stranded DNAs. Biochemistry 16: 4217–4225.
- Kirkpatrick FH. 1990. Overview of agarose gel properties. Curr Commun
- Cell Mol Biol 1: 9–22.
- Lichtenstein AV, Moiseev VL, Zaboikin MM. 1990. A procedure for DNA and RNA transfer to membrane filters avoiding weight-induced gel flattening. Anal Biochem 191: 187–191.
- McDonell MW, Simon MN, Studier FW. 1977. Analysis of restriction fragments of T7 DNA and determination of molecular weights by electrophoresis in neutral and alkaline gels. J Mol Biol 110: 119–146.
- Meinkoth J, Wahl G. 1984. Hybridization of nucleic acids immobilized on solid supports. Anal Biochem 138: 267–284.
- Nygaard AP, Hall BD. 1960. A method for the detection of DNA-RNA complexes. Biochim Biophys Acta 40: 85–92.
- Olszewska E, Jones K. 1988. Vacuum blotting enhances nucleic acid transfer. Trends Genet 4: 92–94.
- Reed KC, Mann DA. 1985. Rapid transfer of DNA from agarose gels to nylon membranes. Nucleic Acids Res 13: 7207–7221.
- Seed B. 1982. Diazotizable arylamine cellulose papers for the coupling and hybridization of nucleic acids. Nucleic Acids Res 10: 1799–1810.
- Sharp PA, Sugden B, Sambrook J. 1973. Detection of two restriction endonuclease activities in Haemophilus parainfluenzae using analytical agarose–ethidium bromide electrophoresis. Biochemistry 12: 3055–3063.
- Southern EM. 1975. Detection of specific sequences among DNA fragments separated by gel electrophoresis. J Mol Biol 98: 503–517.
- Stellwag EJ, Dahlberg AE. 1980. Electrophoretic transfer of DNA, RNA and protein onto diazobenzyloxymethyl (DBM)-paper. Nucleic Acids Res 8: 299–317.
- Stellwagen NC. 2009. Electrophoresis of DNA in agarose gels, polyacrylamide gels and in free solution. Electrophoresis 30: S188–S195.
- Stellwagen NC, Stellwagen E. 2009. Effect of the matrix on DNA electrophoretic mobility. J Chromatogr A 1216: 1917–1929.
- Thorne HV. 1966. Electrophoretic separation of polyoma virus DNA from host cell DNA. Virology 29: 234–239.
- Thorne HV. 1967. Electrophoretic characterization and fractionation of polyoma virus DNA. J Mol Biol 24: 203–211.
- Trnovsky J. 1992. Semi-dry electroblotting of DNA and RNA from agarose and polyacrylamide gels. BioTechniques 13: 800–804.
- Wahl GM, Stern M, Stark GR. 1979. Efficient transfer of large DNA fragments from agarose gels to diazobenzyloxymethyl-paper and rapid hybridization by using dextran sulfate. Proc Natl Acad Sci 76: 3683–3687.

## 方案 1 琼脂糖凝胶电泳

琼脂糖是 D-和 L-半乳糖残基通过  $\alpha(1\rightarrow3)$  和  $\beta(1\rightarrow4)$  糖苷键交替构成的线状聚合物。琼脂糖链形成螺旋纤维，后者再聚合成半径 20～30nm 的超螺旋结构。琼脂糖凝胶可以构成一个直径从 50nm 到略大于 200nm 的三维筛孔的通道(Norton et al. 1986; 综述请见 Kirkpatrick 1990)。

商品化的琼脂糖聚合物每个链约含 800 个半乳糖残基。然而，琼脂糖并不是均一的，不同的制造商或不同生产批次的多糖链的平均长度都是不同的（更详细介绍请参照本章导言）。此外，较低等级的琼脂糖也许存在其他多糖、盐和蛋白质的污染。这种变异性（非均一性）影响琼脂糖凝结和熔化的温度、DNA 的筛分和从凝胶中回收的 DNA 作为酶切底物的能力。应用特制等级的琼脂糖可以减少以上潜在的问题，因为它们经检查不含抑制剂和核酸酶，并且在溴化乙锭染色后产生很少的背景荧光。

此方案介绍了琼脂糖凝胶的制备和电泳步骤。通过染色法检测 DNA 见方案 2。微型胶电泳见于此方案后信息栏。

![](images/page_91_image_6.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查找相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

琼脂糖溶液（见本章导言表2-1和表2-2）

在需用的缓冲液中熔化琼脂糖直到获得清亮透明的溶液，然后浇灌入模具内，让其凝结硬化。凝结后琼脂糖形成基质的密度取决于琼脂糖的浓度。为了快速分析 DNA 样品，推荐使用微量胶（minigel）（请见此方案后的信息栏“微型胶电泳”）。

DNA 样品

DNA 分子质量标准品

通常使用的 DNA 分子质量标准品源于经限制性内切核酸酶消化已知序列的质粒或噬菌体 DNA。另一方法是连接已知分子质量的单体 DNA 片段，在电泳中形成不同大小的多聚体梯形条带。琼脂糖和聚丙烯酰胺凝胶电泳用的 DNA 分子质量标准品可以从市场购得或者实验室自制。一般最好有两套不同分子质量范围的标准品:一个是 1kb～>20kb 的高分子质量标准品，一个是 100～1000bp 的低分子质量标准品。分子质量标准品储备溶液用凝胶上样缓冲液稀释后用于每次电泳实验。

电泳缓冲液（常用  $1 \times TAE < A >$  或  $0.5 \times TBE < A >$ ）

6×凝胶载样缓冲液 I-IV 型 &lt;A&gt;

## 设备

琼脂糖凝胶电泳仪

附带梳子和电泳槽的清洁干燥水平电泳仪，或有适用梳子的清洁干燥玻璃平板。

封胶带

常见的实验室用胶带，如 Time 胶带或 VWR 胶带都适用于浇灌琼脂糖凝胶时封边。

有盖玻璃瓶或三角烧瓶

成像系统（如 CCD 相机以及紫外照明灯）

KimWipes 擦拭纸

微波炉或沸水浴

可以提供 500V 和 200mA 的电源装置

预设  $55^{\circ}$ C 水浴锅

![](images/page_92_image_5.jpg)

## 方法

1. 用封边胶带封住塑料托盘开放的两边或清洁干燥的玻璃板的边缘形成一个模具（图2-3），并置于水平实验台上。

![](images/page_92_image_8.jpg)

<details>
<summary>text_image</summary>

Illustration showing five sequential steps of a hand using a tool to handle a material, with labeled components and equipment.
</details>

图 2-3 灌制水平琼脂糖凝胶。

2. 配制足量的电泳缓冲液（1×TAE 或 0.5×TBE）用以灌满电泳槽和配制凝胶。

配胶和灌满电泳槽使用同一批缓冲液很重要。因为即使很小的离子强度或 pH 差别也会导致凝胶性能异常，严重影响 DNA 片段的泳动。当检测未知 DNA 片段的大小时，一定要保证所有样品在同一缓冲液配置的同样凝胶中分析。一些限制性内切核酸酶缓冲液（如 BamHI 和 EcoRI）含盐浓度高，不仅能够减缓 DNA 的迁移速率，同时也会使邻近孔 DNA 样品出现失真的电泳行为。

3. 根据欲分离 DNA 片段大小，用电泳缓冲液配制适宜浓度琼脂糖溶液:应准确称量琼脂糖干粉加到盛有定好量的电泳缓冲液的三角烧瓶或玻璃瓶中（表 2-4）。

缓冲液体积应小于烧瓶或玻璃瓶容积的 50%。

分离不同大小的 DNA 所需的琼脂糖凝胶浓度列于表 2-3。一些高分辨率琼脂糖（如 MetaPhor 琼脂糖；Lonza Walkersville）凝胶能分离只有几个碱基对差别的 DNA。此外，经修饰的多糖（市场有出售）加到琼脂糖中可以增加分辨率。修饰多糖与琼脂糖混合制成的浓度为 0.5%～2.0%（m/V）的凝胶不仅分辨率增加，而且更清亮，强度更好。

表 2-4 不同含量标准低电内渗琼脂糖凝胶的分离范围

| 琼脂糖凝胶浓度/[(% (m/V)] | 线状 DNA 分子分离范围/kb |
| --- | --- |
| 0.3 | 5~60 |
| 0.6 | 1~20 |
| 0.7 | 0.8~10 |
| 0.9 | 0.5~7 |
| 1.2 | 0.4~6 |
| 1.5 | 0.2~3 |
| 2.0 | 0.1~2 |

4. 用KimWipes擦拭纸松松地塞住三角烧瓶颈部，如用玻璃瓶一定松松地盖住。在沸水浴或微波炉内加热至琼脂糖熔化。

警惕:微波炉加热时间过长，琼脂糖溶液会变得过热或剧烈沸腾。

仅加热所有琼脂糖颗粒完全溶解需要的最短时间。通常未熔解的琼脂糖呈小透明体或半透明碎片悬浮在溶液中。戴上手套，不时地小心旋转三角烧瓶或玻璃瓶，以保证黏在壁上的未熔化的琼脂糖颗粒进入溶液。熔解较高浓度的琼脂糖需要较长的加热时间。要查看煮沸后是否由于蒸发而溶液体积减少，如有必要用水恢复原体积。

5. 用隔离手套或夹子转移三角烧瓶或玻璃瓶到 $55^{\circ} \mathrm{C}$ 水浴。待熔化的凝胶稍冷却后加入溴化乙锭，终浓度为 $0.5 \mu \mathrm{g} / \mathrm{mL}$ 。轻轻地旋转以充分混匀凝胶溶液。

警惕:SYBR Gold 不应加到熔化的凝胶溶液中。

当用塑料托盘制备凝胶时，灌制凝胶前冷却熔化的琼脂糖溶液至  $60^{\circ}$ C 以下很重要。高温溶液会使托盘变形或出现裂纹。含有高浓度琼脂糖（2%或更高）的溶液应在  $70^{\circ}$ C 存放以免过早凝结。但是因为用于纯化和制备标准琼脂糖方法的改进，这种处理现已没有必要。

6. 琼脂糖溶液正在冷却时，选择一个合适的梳子用来制造加样孔。梳齿底部的位置应在托盘底面上 $0.5 \sim 1.0 \mathrm{~mm}$，这样琼脂糖浇灌到托盘时将形成符合要求的加样孔。

多数凝胶托盘都有适宜放梳子的侧壁或外侧支架。如果没有或不合适，梳齿可能会太接近托盘底面，在拔出梳子时易穿透加样孔的底部，样品液将从凝胶和加样孔之间泄露。应用低浓度琼脂糖（<0.6%）或低凝点琼脂糖时这种问题尤其容易发生。

7. 浇灌温热的琼脂糖溶液进入模具。

凝胶适宜厚度为 3～5mm。需检查在梳齿下或梳齿间应无气泡。熔化的凝胶液中的气泡用 KimWipes 擦拭纸的角轻触即可容易除去。

制备低浓度琼脂糖凝胶（＜0.5%）时，先倒一个1%浓度琼脂糖的支持胶，它没有加样孔。让支持胶在托盘或玻璃板上室温下硬化，然后再直接在支持胶上倒低浓度凝胶。此方式制备的凝胶明显减少了在后续如照相或Southern杂交等操作过程中可能造成的低浓度胶断裂。需要保证两个浓度的凝胶用同一批缓冲液配制，且含有相同浓度的溴化乙锭。低熔点和低于0.5%浓度的琼脂糖凝胶也可以冷却到4℃，并在冷室中电泳以减少断裂的机会。

8. 让凝胶溶液完全凝结，室温下需 $30\sim 45\mathrm{min}$ 。加少量电泳缓冲液于凝胶顶部，小心拔出梳子。倒出电泳缓冲液。轻轻撕去封边胶带，将凝胶安放到电泳槽内。

9. 向电泳槽加入电泳缓冲液，刚好没过凝胶约 1mm。

没有必要在加样前对琼脂糖凝胶进行预电泳。

10. 将 DNA 样品和 0.2 倍体积的 $6 \times$ 上样缓冲液混合。

加样孔能加入 DNA 的最大量取决于样品中 DNA 片段的大小和数目。若一个 5mm 宽条带含有 500ng 以上的 DNA 时，说明加样孔过载，会导致拖尾、条带两侧卷翘的“微笑效应”和模糊不清等现象。如果 DNA 长度增加，上述现象变得更为严重。分析单一 DNA 样品（如  $\lambda$  噬菌体或质粒 DNA）时，每个 5mm 宽加样孔可加 100～500ng DNA。如果样品由不同大小的许多 DNA 片段组成（如哺乳类动物 DNA 的酶切样品），则每个加样孔加入 20～30 $\mu$ g 的 DNA 也不会造成分辨率明显下降。

加样DNA的最大体积是由加样孔容积决定的。通用的加样孔（ $0.5\mathrm{cm}\times 0.5\mathrm{cm}\times 0.15\mathrm{cm}$ ）可容纳约 $40\mu \mathrm{L}$ 样品。切忌将加样孔加得太满，甚至溢出。为避免溢出造成邻孔样品污染，最好配置稍厚些的凝胶能够增加加样孔容积或通过乙醇沉淀浓缩DNA减少加样体积。

11. 用一次性吸头、自动移液器、拉长的巴斯德吸管或玻璃毛细管将样品混合液缓慢加至浸没凝胶的加样孔内。DNA 分子质量标准品应分别加至样品孔的左侧和右侧的两个孔内。

许多情况下，不必每个样品用一个新的移液器吸头，只需在两次加样之间用阳极池内缓冲液充分洗涤后即可再用。但是凝胶要用于 Southern 印迹分析或实验目的为回收 DNA 条带时，每个样品应使用一个新的吸头。

12. 关上电泳槽盖，接好电极插头。DNA 应向阳极（红色插头）侧泳动。给予 1～5V/cm 的电压，其中距离以阳极至阴极之间的测量为准。如电极插头连接正确，阳极和阴极由于电解作用将产生气泡，并且几分钟内溴酚蓝从加样孔迁移进入胶体内。待溴酚蓝和二甲苯蓝 FF 迁移到适当距离后停止电泳。

溴化乙锭的存在使凝胶在电泳的任何阶段都能够置于紫外灯下观察。此时，可以除去托盘，直接放凝胶于透光板上。也可以用一个手提式紫外光源检查凝胶。不管哪种方式，应在检查时短时间关闭电源。

电泳期间，溴化乙锭向阴极迁移（与 DNA 迁移方向相反）。长时间电泳将导致凝胶中溴化乙锭含量显著减少，使小片段 DNA 检测发生困难。此时，可将凝胶浸入  $0.5 \mu g/mL$  溴化乙锭溶液染色 30～45min。

13. 当 DNA 样品或染料在凝胶中迁移了足够距离时，关上电源、拔出电极插头并打开电泳槽盖。若凝胶和电泳缓冲液中含有溴化乙锭，用紫外灯观察凝胶和用装有紫外线透射滤光片的 CCD 相机照相（Oatey 2007）。除此之外，也可采用方案 2 对凝胶进行染色。

从凝胶中回收 DNA 见方案 8～10。Southern 印迹及杂交见方案 11～13。

## 微型胶电泳

用微型琼脂糖凝胶可以对 DNA 样品进行快速的常规电泳分析。微型胶电泳在需要迅速判断是否进行下一步克隆步骤时特别有用。

该法使用的加样孔更小、凝胶更薄、可以观察少于常量的 DNA。此外，由于凝胶能预先制备并迅速电泳，所需试剂量也更少，所以它在时间和经济上都相当节省。许多研究者在一周开始时制备一块微型胶，在实验过程中可以多次重复使用。其步骤是:一批样品上样、电泳和观察后，继续电泳。待样品从凝胶进入缓冲液就可以重新使用该凝胶。注意，微型胶最适合分析 DNA 小片段（<3kb）。由于通常使用的电压较高，凝胶长度又较短，所以大片段的分辨率较差。

一些厂家已经生产了几类用于微型胶电泳的微型电泳槽，它们是常规电泳槽的缩小版本。它的每个加样孔能加样 3～12μL，当然这取决于凝胶的厚度和梳齿的宽度。一般选择加 10～100ng DNA 到加样孔，在较高电压（5～20V/cm）下电泳 30～60min。当溴酚蓝和二甲苯蓝 FF 迁移到适当距离时停止电泳并采用 CCD 相机拍摄紫外线照射下的凝胶图像。

## 参考文献

Kirkpatrick FH. 1990. Overview of agarose gel properties. Curr Commun Cell Mol Biol 1: 9–22.

Norton IT, Goodall DM, Anstren KRJ, Morris ER, Rees DA. 1986. Dynamics of molecular organization in agarose sulfate. Biopolymers 25: 1009–1030.

Oatey P. 2007. Imaging fluorescently stained DNA with CCD technology: How to increase sensitivity and reduce integration times. BioTechniques 43: 376–377.

## 方案 2 琼脂糖凝胶中 DNA 的染色检测

经琼脂糖凝胶电泳分离的 DNA 可以通过染色法检测。染色的染料通常具有少量的内在荧光特性、较强的 DNA 亲和力，以及与核酸结合后的高荧光量子产率。量子产率越高，其信号噪声比就越高。经这些染料染色的 DNA 条带可以在某一波长的紫外光照射下观察，同时在另一个波长紫外光照射下做记录。这里介绍了用三种染料（溴化乙锭、SYBR Gold 和 SYBR Green I）浸染后观察凝胶中 DNA 的方法。有关这些及其他染料的更详细信息见第 1 章 “DNA 定量” 章节中的介绍。

注意, 同 SYBR 染料具有相似特点的染料可以从其他公司, 如 GelStar(White et al.1999) 和 GelRed (Huang et al. 2010) 购买。尽管这些染料的敏感性不如非对称花青染料高, 但是溴化乙锭仍然适用于凝胶中 DNA 的大多数常规染色。

在紫外光照射下,用装有合适的转换荧光屏和滤光片的 CCD 相机可以拍摄染色的凝胶图像。在 Oatey（2007）中陈述了如何建立一个 CCD 系统来拍摄具有最高敏感度的荧光染色图像。

![](images/page_95_image_3.jpg)

## 凝胶 SYBR Gold 染色法

SYBR Gold 是一种新型的、极敏感的染料的商品名称，其与 DNA 结合的亲和力高，并且结合后能够极大地增强荧光信号。该染料与核酸结合的模式和机制与以往其他常规菲啶嵌入型染料（如溴化乙锭、碘化丙锭）不同。

SYBR Gold 可以用于中性聚丙烯酰胺凝胶和琼脂糖凝胶中的核酸染色，同时也可以用于含有变性剂（如尿素、乙二醛、甲醛）的凝胶染色。SYBR Gold-DNA 复合物产生光子的量比 EB-DNA 复合物要大得多，同时其结合 DNA 后产生的荧光信号增强度比 EB 高 1000 多倍。因此，用 SYBR Glod 染色可以检测出琼脂糖凝胶中小于 20pg 的双链 DNA（是 EB 染色最低检测量的 1/25）。此外，利用 SYBR Gold 染料进行琼脂糖或聚丙烯酰胺凝胶染色可以检测出一个条带中含有少至 100pg 的单链 DNA 或 300pg 的 RNA。SYBR Gold 染料的最大激发波长为 495nm，同时在 300nm 有第二个激发峰。其荧光发射波长为 537nm。

SYBR Gold 以  $10\ 000\times$  的浓度储存在无水的 DMSO 中，并应戴无粉手套操作。其昂贵的价格使其无法应用于常规凝胶染色。但是该染料在某些技术中替代放射标记 DNA 是物有所值的，如单链构象多态性（SSCP）和变性梯度凝胶电泳（DGGE）技术。

不能将 SYBR Gold 加入熔化的凝胶中或在电泳前加入凝胶，这是因为在 SYBR Gold 存在的情况下，凝胶中核酸的电泳行为会产生严重失真。由于 SYBR Gold 染料对荧光敏感，所以其工作液（储备溶液 1:10 000 稀释）应该当天用电泳缓冲液新鲜配制，室温存放。

DNA 片段经过凝胶电泳分离后，用 SYBR Gold 工作液（1:10 000 稀释储备溶液）浸染凝胶。浸染的过程需要约 30min（如果凝胶较厚需更长时间）。由于该染料背景荧光水平很低，所以不需脱色。

在紫外灯照射下,用装有蓝光转换荧光屏和SG透射滤光片的CCD相机可以拍摄SYBR Gold染料浸染的凝胶图像（Oatey 2007）。

![](images/page_95_image_11.jpg)

## 凝胶 SYBR Green I 染色法

SYBR Green I 是一种能激发荧光的非对称花青染料，其荧光量子产率为 0.8，能结合双链 DNA, 结合后使荧光信号增强 800～1000 倍（Schneeberger et al. 1995）。SYBR Green I 染料最大激发波长为 497nm，同时在 284～312nm 间可见其他激发峰，这使得该染料适合与氩离子激光器共同使用。其荧光发射波长为 520nm。

SYBR Green I 与 DNA 以高亲和力结合，而且可以用于多种实验目的，包括检测浸染琼脂糖和聚丙烯酰胺凝胶中的 DNA 和寡核苷酸、在聚合酶链反应中扩增的产物，并应用于条带迁移和核酸酶保护分析系统的检测。

SYBR Green I 与双链 DNA 的结合亲和力很强，但与单链 DNA 和 RNA 的结合亲和力较弱。该染料在波长为 300nm 的紫外灯下能检测琼脂糖凝胶中少至 60pg 的双链 DNA 条带和 5% 聚丙烯酰胺凝胶中 50pmol 的寡核苷酸。因为 SYBR Green I 染料具有最强的敏感性，因此可以用于电泳后染色。

SYBR Green I 不会干扰 Taq DNA 聚合酶、反转录酶、限制性核酸内切核酸酶、噬菌体 T4 DNA 连接酶活性，并且在 Ames 实验中显示出弱于溴化乙锭的致诱变性。

因为SYBR GreenI能够被玻璃表面强烈吸收，所以染色溶液应该在塑料容器中配制。