测序验证所构建质粒的序列。对于这些项目，就应该采用双脱氧/毛细管测序。然而，应该注意的是，对于大量患者样品中单一基因的测序，下一代测序技术可能会更合适。毛细管测序所得到的人类基因组参考序列的错误率是万分之一，而实际的错误率大概几十万分之一。下一代测序技术及其所提供的高覆盖率，会使所得结果的错误率低于百万分之一，因此下一代测序技术的准确度会远超过与之比对的原始参考序列。

也许最复杂的测序是一个基因组的 de novo 测序（以前从未测序的基因组，无参考序列）。经验表明，毛细管测序数据拼接的基因组更加完整。然而，这种测序技术的成本大大超过下一代测序技术。目前，对基因组的 de novo 测序要么联合使用长 reads 下一代测序仪（454）和短 reads 下一代测序仪（Illumina 或 SOLiD），要么单独采用 454。Pacific Biosciences 测序仪的长 reads 也可能会在这里发挥很好的作用。有时毛细管测序获得的长 reads 也可用来完成拼接。一般来说，研究人员可视项目的经费情况将不同的测序方法进行组合。

![](images/page_128_image_4.jpg)

## 方案介绍

我们在此提供了一系列方案，分为两个部分。第一部分涉及毛细管测序及代表性平台（Illumina 和 454）的各种样品制备方法。第二部分是对测序结果进行评估和分析处理。

毛细管测序在分子生物学领域仍然处于重要地位。对于验证一个克隆构建是否正确，或下一代测序技术发现的一个有趣的变种是否可靠，毛细管测序是一个非常灵活的工具。毛细管测序的模板一般是克隆的质粒 DNA（参见方案 1）或 PCR 产物（参见第 7 章，方案 2）。若为后者，则需设计特异性引物来扩增原始样品中的目的 DNA 序列，扩增的产物则采用定制的引物测序。用于扩增目的序列的特异性引物是用专门的软件设计的。第 8 章方案 3 中介绍的 Primer 3 是通常用于设计引物的软件，方案 3 介绍了质粒 DNA 和 PCR 产物的毛细管测序。

截至目前，Illumina 因其低成本、高通量的优势已经成为使用最广泛的下一代测序平台。下文将介绍各种 Illumina/Solexa 测序样品的制备方法，包括全基因组文库的构建方案（方案 4～8）、RNA 文库构建方案（方案 9）、外显子组和靶向捕获文库构建方案（方案 10），文库定量的各种方法在方案 12～14 中介绍。

与 Illumina 和 SOLiD 测序平台不同，454 测序平台近年来在测序成本上没有大幅下降，但是 454 测序平台在基因组学的两个主要领域仍然在使用。首先，对于一些首次测序的基因组，454 测序平台 reads 的长度在 de novo 拼接中具有优势。总体来看，454 的长读长 reads 有助于基因组的初步拼接，而方案（方案 7 和方案 8）中所介绍的 3kb 和 8kb 的 mate-pair 数据更有助于基因组序列大范围的拼接及其完成。其次，在测序过程中该平台碱基替代的错误发生率较低，能够提供准确可靠的数据，具有独特的优势。对于采用生物信息学方法筛选突变体，基于合成测序原理的 454 测序技术在提供准确有效数据方面是一个有利的工具。在 454 测序平台中，大量的 PCR 产物和杂交捕获产物可以混合在一起进行平行测序，并且碱基替代错误发生的概率比较低，所以能够快速、准确地筛选出可靠的突变体，避免假阳性结果出现。方案 15～17 分别介绍了文库的构建、emPCR 及 Roche/454 测序仪的使用。

第二部分中的方案主要介绍了测序的后处理和数据分析——测序数据的确认（方案18）、质量控制（方案19），以及生物信息学分析（方案20）。

![](images/page_128_image_11.jpg)

## 致谢

在本实验室下述人员的帮助下我们完成了本章的编写工作:Mardis 实验室，Lisa Cook 和 Henry Bauer；操作方案和评阅:McCombie 实验室的 Eric Antoniou, Elena Ghiban, Melissa

Kramer, Shane McCarthy, Stephanie Muller, Jennifer Parla, Rebecca Solomon, Maureen Bell 和 Carolann Gundersen。本章的出版获得了 Cold Spring Harbor Laboratory 出版社下述人员的大力支持:主编 Kaaren Janssen 和 Alex Gann；项目经理 Maryliz Dickerson；出版编辑 Kathleen Bubbeo。

最后，我们要感谢 Jim Watson 领导的人类基因组计划，感谢他在 CSHL 实验室近 20 年无私奉献于基因组分析、DNA 测序，以及对基因组学的毕生贡献。

## 参考文献

- Albert TJ, Molla MN, Muzny DM, Nazareth L, Wheeler D, Song X, Richmond TA, Middle CM, Rodesch MJ, Packard CJ, et al. 2007. Direct selection of human genomic loci by microarray hybridization. Nat Methods 4: 903–905.
- Bainbridge MN, Wang M, Burgess DL, Kovar C, Rodesch MJ, D'Ascenzo M, Kitzman J, Wu YQ, Newsham I, Richmond TA, et al. 2010. Whole exome capture in solution with 3 Gbp of data. Genome Biol 11: R62.
- Carothers AM, Urlaub G, Mucha J, Grunberger D, Chasin LA. 1989. Point mutation analysis in a mammalian gene: Rapid preparation of total RNA, PCR amplification of cDNA, and Taq sequencing by a novel method. BioTechniques 7: 494-6-498-9.
- Clark MJ, Chen R, Lam HY, Karczewski KJ, Chen R, Euskirchen G, Butte AJ, Snyder M. 2011. Performance comparison of exome DNA sequencing technologies. Nat Biotechnol 29: 908–914.
- Craxton M. 1993. Cosmid sequencing. Methods Mol Biol 23: 149–167.
- Davies K. 2001. Cracking the genome: Inside the race to unlock human DNA. The Free Press, New York.
- Edwards A, Voss H, Rice P, Civitello A, Stegemann J, Schwager C, Zimmermann J, Erfle H, Caskey CT, Ansorge W. 1990. Automated DNA sequencing of the human HPRT locus. Genomics 6: 593–608.
- Ewing B, Green P. 1998. Base-calling of automated sequencer traces using phred. II. Error probabilities. Genome Res 8: 186–194.
- Ewing B, Hillier L, Wendl MC, Green P. 1998. Base-calling of automated sequencer traces using phred. I. Accuracy assessment. Genome Res 8:175–185.
- Flusberg BA, Webster DR, Lee JH, Travers KJ, Olivares EC, Clark TA, Korschach J, Turner SW. 2010. Direct detection of DNA methylation during single-molecule, real-time sequencing. Nat Methods 7: 461–465.
- Gilbert W. 1981. DNA sequencing and gene structure (Nobel Lecture, December 8, 1980). Biosci Rep 1: 353–375.
- Gilbert W, Maxam A. 1973. The nucleotide sequence of the lac operator. Proc Natl Acad Sci 70: 3581–3584.
- Gnirke A, Melnikov A, Maguire J, Rogov P, LeProust EM, Brockman W, Fennell T, Giannoukos G, Fisher S, Russ C, et al. 2009. Solution hybrid selection with ultra-long oligonucleotides for massively parallel targeted sequencing. Nat Biotechnol 27: 182–189.
- Gocayne J, Robinson DA, FitzGerald MG, Chung FZ, Kerlavage AR, Lentes KU, Lai J, Wang CD, Fraser CM, Venter JC. 1987. Primary structure of rat cardiac β-adrenergic and muscarinic cholinergic receptors obtained by automated DNA sequence analysis: Further evidence for a multigene family. Proc Natl Acad Sci 84: 8296–8300.
- Gordon D, Abajian C, Green P. 1998. Consed: A graphical tool for sequence finishing. Genome Res 8: 195–202.
- Henikoff S. 1990. Ordered deletions for DNA sequencing and in vitro mutagenesis by polymerase extension and exonuclease III gapping of circular templates. Nucleic Acids Res 18: 2961–2966.
- Hodges E, Xuan Z, Balija V, Kramer M, Molla MN, Smith SW, Middle CM, Rodesch MJ, Albert TJ, Hannon GJ, et al. 2007. Genome-wide in situ exon capture for selective resequencing. Nat Genet 39: 1522–1527.
- Korbel JO, Urban AE, Affourtit JP, Godwin B, Grubert F, Simons JF, Kim PM, Palejev D, Carriero NJ, Du L, et al. 2007. Paired-end mapping reveals extensive structural variation in the human genome. Science 318: 420–426.
- Lander ES, Linton LM, Birren B, Nusbaum C, Zody MC, Baldwin J, Devon K, Dewar K, Doyle M, FitzHugh W, et al. 2001. Initial sequencing and analysis of the human genome. Nature 409: 860–921.
- Ley TJ, Mardis ER, Ding L, Fulton B, McLellan MD, Chen K, Dooling D, Dunford-Shore BH, McGrath S, Hickenbotham M, et al. 2008. DNA sequencing of a cytogenetically normal acute myeloid leukaemia genome. Nature 456: 66–72.
- Mardis ER. 2008. Next-generation DNA sequencing methods. Annu Rev Genomics Hum Genet 9: 387–402.
- Margulies M, Egholm M, Altman WE, Attiya S, Bader JS, Bemben LA, Berka J, Braverman MS, Chen YJ, Chen Z, et al. 2005. Genome sequencing in microfabricated high-density picolitre reactors. Nature 437: 376–380.
- Maxam AM, Gilbert W. 1977. A new method for sequencing DNA. Proc Natl Acad Sci 74: 560–564.
- McCombie WR, Heiner C, Kelley JM, Fitzgerald MG, Gocayne JD. 1992. Rapid and reliable fluorescent cycle sequencing of double-stranded templates. DNA Seq 2: 289–296.
- McElheney V. 2010. Drawing the map of life: Inside the Human Genome Project. Basic Books, New York.
- Mullis KB, Faloona FA. 1987. Specific synthesis of DNA in vitro via a polymerase-catalyzed chain reaction. Methods Enzymol 155: 335–350.
- Murray V. 1989. Improved double-stranded DNA sequencing using the linear polymerase chain reaction. Nucleic Acids Res 17: 8889.
- Myers EW. 1995. Toward simplifying and accurately formulating fragment assembly. J Comput Biol 2: 275–290.
- Okou DT, Steinberg KM, Middle C, Cutler DJ, Albert TJ, Zwick ME. 2007. Microarray-based genomic selection for high-throughput resequencing. Nat Methods 4: 907–909.
- Parla JS, lossifov I, Grabill I, Spector MS, Kramer M, McCombie WR. 2011. A comparative analysis of exome capture. Genome Biol 12: R97. doi: 10.1186/gb-2011-12-9-r97.
- Porreca GJ, Zhang K, Li JB, Xie B, Austin D, Vassallo SL, LeProust EM, Peck BJ, Emig CJ, Dahl F, et al. 2007. Multiplex amplification of large sets of human exons. Nat Methods 4: 931–936.
- Saiki RK, Scharf S, Faloona F, Mullis KB, Horn GT, Erlich HA, Arnheim N. 1985. Enzymatic amplification of  $\beta$ -globin genomic sequences and restriction site analysis for diagnosis of sickle cell anemia. Science 230:1350–1354.
- Sanger F, Coulson AR. 1978. The use of thin acrylamide gels for DNA sequencing. FEBS Lett 87: 107–110.
- Sanger F, Nicklen S, Coulson AR. 1977a. DNA sequencing with chain-terminating inhibitors. Proc Natl Acad Sci 74: 5463–5467.
- Sanger F, Air GM, Barrell BG, Brown NL, Coulson AR, Fiddes CA, Hutchison CA, Slocombe PM, Smith M. 1977b. Nucleotide sequence of bacteriophage φX174 DNA. Nature 265: 687–695.
- Sanger F, Coulson AR, Hong GF, Hill DF, Petersen GB. 1982. Nucleotide sequence of bacteriophage λ DNA. J Mol Biol 162: 729–773.
- Shreeve J. 2004. The genome war: How Craig Venter tried to capture the code of life and save the world. Alfred A. Knopf, New York.
- Smith LM, Sanders JZ, Kaiser RJ, Hughes P, Dodd C, Connell CR, Heiner C, Kent SB, Hood LE. 1986. Fluorescence detection in automated DNA sequence analysis. Nature 321: 674–679.
- Smith DP, Johnstone EM, Little SP, Hsiung HM. 1990. Direct DNA sequencing of cDNA inserts from plaques using the linear polymerase chain reaction. BioTechniques 9: 48, 50, 52; passim.
- Staden R. 1979. A strategy of DNA sequencing employing computer programs. Nucleic Acids Res 6: 2601–2610.
- Staden R. 1996. The Staden Sequence Analysis Package. Mol Biotechnol 5:233–241.
- Sutcliffe JG. 1978. Nucleotide sequence of the ampicillin resistance gene of Escherichia coli plasmid pBR322. Proc Natl Acad Sci 75: 3737–3741.
- Sutcliffe JG. 1979. Complete nucleotide sequence of the Escherichia coli plasmid pBR322. Cold Spring Harb Symp Quant Biol 43: 77–90.
- Tuzun E, Sharp AJ, Bailey JA, Kaul R, Morrison VA, Pertz LM, Haugen E, Hayden H, Albertson D, Pinkel D, et al. 2005. Fine-scale structural variation of the human genome. Nat Genet 37: 727–732.
- Venter JC, Adams MD, Myers EW, Li PW, Mural RJ, Sutton GG, Smith HO, Yandell M, Evans CA, Holt RA, et al. 2001. The sequence of the human genome. Science 291: 1304–1351.
- Waterston RH, Lander ES. 2002. Initial sequencing and comparative analysis of the mouse genome. Nature 420: 520–562.
- Wu R. 1970. Nucleotide sequence analysis of DNA. I. Partial sequence of the cohesive ends of bacteriophage and 186 DNA. J Mol Biol 51: 501.
- Wu R, Donelson J, Padmanabhan R. 1970. Nucleotide sequence analysis of DNA. In 8th International Congress on Biochemistry, p. 166. Staples Printers, Kent, UK.
- Wu R, Taylor E. 1971. Nucleotide sequence analysis of DNA. II. Complete nucleotide sequence of the cohesive ends of bacteriophage DNA. J Mol Biol 57: 491.

# 方案 1 毛细管测序质粒亚克隆的制备

该方案参考少量制备的方法（参见第1章，方案1），介绍如何从细菌培养物或保存的培养物中制备质粒。所制备的质粒DNA在数量和特性方面适合用做毛细管DNA测序（方案3）的模板。另一种制备模板的方法就是方案2中介绍的目的DNA的扩增。该方案需要使用Biomek自动化液体处理系统。

![](images/page_130_image_4.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

本方案中提供的试剂供测序使用。溶液 P1、P2、P3 可根据配方在实验室自行配备或自 QIAGEN 公司购买。

## 试剂

琼脂糖凝胶（0.8%琼脂糖），以  $1 \times TAE$  配制&lt;A&gt;，含有  $0.1 \mu g/mL$  溴化乙锭；其他琼脂糖凝胶电泳所需的试剂和设备，见第 2 章方案 1 的描述

含有待分析质粒的大肠杆菌培养物

乙醇（70%）

甘油（40%）&lt;R&gt;

异丙醇（100%）

NaOH (10mol/L) &lt;R&gt;

P1 缓冲液&lt;R&gt;

P2 缓冲液&lt;R&gt;

P3 缓冲液&lt;R&gt;

RNase H (10mg/mL) (无 DNase) &lt;R&gt;

SDS (10%)&lt;R&gt;

乙酸钠(10mmol/L)&lt;R&gt;

Tris-Cl (10mmol/L, pH 8.0) &lt;R&gt;

## 仪器

Biomek FX 工作站（Beckman Coulter 公司）

圆孔盒（96 孔，每孔 1mL）（Beckman Coulter 公司）

Costar 检测板（96 孔）

铝箔纸带

深孔培养管（2mL）（Whatman 公司）

Jouan 离心机

裂解液澄清板（Whatman 公司）

封口膜（塑料）

涡旋仪

定量仪器（分光光度计、荧光光度计等）

密封垫（硅胶）

摇床 - 培养箱

Skan Wash 2000 洗板机

计时器

![](images/page_131_image_6.jpg)

## 方法

## 用于保存和质粒分离的克隆制备

1. 在 2mL Whatman 培养管中培养携带目的质粒的大肠杆菌 16\~24h。

确保细菌培养物在合适的温度下培养，16～24h为宜。液体培养物和空气的比例为1:1（1mL培养物在2mL的管中），用透气膜封口。摇床的转速对于细菌的最佳生长也是至关重要的。细菌典型的培养温度和转速应该是37℃、275r/min。

2. 将 2mL Whatman 培养管从摇床中移出。

3. 用 Biomek FX 工作站取 $50 \mu \mathrm{L}$ 过夜培养物加入 $50 \mu \mathrm{L} 40 \%$ 无菌甘油，然后加入到 96 孔培养板中。

4. 用铝箔纸带密封 96 孔培养板，混匀 5min。短暂离心后置于 -80℃ 保存。

5. 将 Whatman 培养管中剩余的培养物（步骤 2）置于 Jouan 离心机中，2700r/min 离心 5min。

6. 从离心机中取出试管，轻轻地弃掉上清（不要碰到沉淀）。将试管倒置于吸水纸上，将残留的培养基晾干（1min）。

检查沉淀的大小以确定是否继续后续实验:

可接受的沉淀块大小

OOO

不可接受的沉淀块大小

○ 或者更小

如果 30% 以上的沉淀属于不可接受大小的范围，就不能进行后续实验。细菌沉淀和试管必须排除任何的残留液体以使裂解充分。

▲直接进行步骤7，用铝箔纸带密封试管，置于-20℃条件下保存。

## 细菌裂解

7. 用 Biomek FX 工作站每孔加入  $200 \mu L$  的 P1 溶液，再用封口膜封住培养板。

8. 用最高转速涡旋混匀 10min。

为保证细菌沉淀充分的重悬，可较长时间混匀。充分的重悬是裂解细菌的关键因素。

9. 裂解阶段。

i. 将封口膜取下，设置计时器为 5min。

ii. 使用 Biomek FX 工作站，每孔加入  $200 \mu L$  的 P2 溶液，并迅速地用封口膜封上孔板。

iii. 开始计时，并标记第一个孔为 “1”。

iv. 呈  $45^{\circ}$  角倾斜孔板 6 次。

v. 重复步骤 9.ii\~9.iv，并编号。

细菌加入 P2 缓冲液后不能超过 5min。P2 缓冲液必须每 2 天配制一次。使用之前检查瓶子上的日期。

10. 中和反应。

i. 5min 后，向标注为 1 的孔板的每个孔中加入  $200 \mu L$  预冷的 P3 缓冲液。

ii. 用封口膜将孔板密封，轻柔地倾斜孔板6次，置于冰上。

iii. 其余的孔板重复 10.i～10.iii 步骤。

iv. 当最后一个孔板置于冰上后，开始计时 10min.

P3 缓冲液  $4^{\circ}$ C 保存。

## 过滤操作

11. 向 96 孔、1mL 圆孔盒的每个孔中加入 240μL 100% 异丙醇。所有裂解液都需加入到圆孔盒中。

12. 在 96 孔圆孔盒的顶层放置一个裂解液澄清板，组成过滤器组件。

13. 将 96 孔圆孔盒浸入冰浴 10min，用 Biomek FX 工作站取 400μL 细菌裂解液加入到过滤器组件中。将所有 96 孔圆孔盒中的细菌裂解液转移完毕。

在转移前确保能看见每个孔里有白色沉淀物。

14. 过滤器组件在 Jouan 离心机中以转速 1000r/min 离心 3min。

15. 丢弃顶层的过滤板，用硅胶密封垫密封底部的圆孔。将96孔圆孔盒快速颠倒6次充分混匀，避免平板上各孔之间的污染。

将过滤板丢弃前确保其上无任何液体。

16. 将 96 孔圆孔盒以转速 3800r/min 离心 15min.

17. 立即将上清液倒入乙醇废弃瓶中，简单地在吸水纸上吸干液体。

18. 使用 Skan Wash 2000 洗板机向每个孔中加入 $300\mu \mathrm{L}70\%$ 的乙醇，用硅胶密封垫重新密封，反复颠倒几次以便彻底清洗各孔。

可以使用步骤 15 里的硅胶垫；为了减少孔的污染，也可以用一个新的。

19. 以转速 3800r/min 离心 5min。

20. 弃上清液至乙醇废弃瓶中。

21. 将 96 孔圆孔盒板倒置于纸巾上约 5min，除去残留液体。

22. 重复步骤 18\~21。

▲可室温过夜储存孔板，以使 DNA 沉淀干燥（第二天进行 DNA 的重悬）。也可以  $37^{\circ}$ C 旋转孵育 1h 使 DNA 沉淀干燥。

无论哪种方法，在进行后续步骤前确保孔内完全干燥。见“疑难解答”。

## DNA 的重悬和随机定量

23. 使用 Biomek FX 工作站向每孔加入约  $70 \mu L$  的 10 mmol/L Tris-Cl (pH8.0)（洗脱体积根据下游实验而定）。

24. 用密封垫密封 96 孔圆孔盒板，以最高转速涡旋 10min。

25. 轻敲 96 孔圆孔盒板，收集孔底液体。用 Biomek FX 工作站将每个孔内的液体完全转移到 96 孔 Costar 检测板中。

26. 用铝箔纸密封，储存在-20℃。

27. 从 96 孔 Costar 检测板上随机挑选三个样品进行电泳，以确定所得的质粒的质量和浓度是否符合要求。3μL 样品加 7μL 的 1× 上样染料，进行 0.8% 琼脂糖凝胶电泳，使用 1kb DNA 分子质量标准。

见“疑难解答”。

28. 如果需要将模板定量，可用分光光度计或荧光光度计及其他类似仪器。

见 “疑难解答”。

![](images/page_132_image_29.jpg)

## 疑难解答

问题（步骤 27）:琼脂糖凝胶电泳中除质粒 DNA 的条带之外，出现一条额外的带。

解决方案:如果 P1 缓冲液没有加入 RNase H，那么 RNA 可能会在琼脂糖电泳中跑出

额外的一条带。通常在完成整个质粒提取过程后向 DNA 中加入 RNase 来解决这个问题。

问题（步骤 22 和步骤 28）: $A_{260}/A_{280}$ 的比值（分光光度计）比预期值高（>1.8～2.0）。

解决方案:可能是样品中存在乙醇。重悬和洗脱 DNA 模板之前将所有残留在 96 孔圆孔盒板中的 70% 乙醇（步骤 22）晾干至关重要。这个过程可能需要 1.5h（37℃孵育）或过夜（室温）。

![](images/page_133_image_5.jpg)

## 讨论

根据克隆效率（无论克隆来自低拷贝数质粒还是高拷贝数质粒），一般用此方法制备的质粒浓度为  $100 \sim 500 ng/\mu L$ 。如上所述，洗脱体积随下游实验而定。

![](images/page_133_image_8.jpg)

## 配方

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

## 甘油(40%) (1 L)

1. 在一个洁净的 1L 烧杯中加入:

| 无菌蒸馏水 | 600mL |
| --- | --- |
| 甘油(100%) | 400mL |

2. 搅拌溶液 $5 \mathrm{~min}$ 后, 倒入一个 $1 \mathrm{~L}$ 的瓶内高压灭菌。

## NaOH(10mol/L)

▲制备该溶液时一定要小心，否则可能导致严重烧伤。

1. 在一个干净的 $500 \mathrm{~mL}$ 烧杯中, 加入:

| NaOH 固体(戴手套) | 100g |
| --- | --- |
| 无菌蒸馏水 | 100mL 至总体积 250mL |

2. 用无菌搅拌棒搅拌，直至颗粒完全溶解。

▲注意:这是一个强放热反应。
3. 小心加入无菌蒸馏水，定容至 250mL。
4. 室温储存在玻璃瓶中。此溶液在室温下可稳定储存1年。

## P1 缓冲液（1L）

1. 在一个干净的 2L 烧瓶中，加入:

| 无菌蒸馏水 | 920mL |
| --- | --- |
| Tris-Cl (1mol/L, pH 8.0) | 50mL |
| EDTA (0.5mol/L, pH 8.0) | 20mL |
| RNase H (无 DNase)(10mg/mL) | 10mL |

2. 用无菌搅拌棒搅拌 5min。
3. 过滤后  $4^{\circ}$ C 保存，标注日期（现配现用）。

## P2 缓冲液（1L）

此缓冲液每两天制备一次。

1. 在一个洁净的 1L 烧杯中，加入:

| 无菌蒸馏水 | 880mL |
| --- | --- |
| NaOH (10mol/L) | 20mL |
| SDS (10%) | 100mL |

2. 用无菌搅拌棒搅拌 5min。为避免 SDS 沉淀，在加入 SDS 溶液前先向水中加入 NaOH 溶液并搅拌几分钟。标注日期。
3. 为避免 SDS 沉淀，P2 缓冲液应该室温保存。如果出现沉淀，在 $37^{\circ} \mathrm{C}$ 温浴并搅拌几分钟。

## P3 缓冲液

1. 在一个洁净的 1L 烧杯中加入:

| 乙酸钾 | 294.5g |
| --- | --- |
| 无菌蒸馏水 | 500mL |

2. 搅拌至晶体完全溶解，然后加入 110mL 无水乙酸。
3. 不断搅拌并测定 $\mathrm{pH}$ 。加入无菌蒸馏水至 $900\mathrm{mL}$，$\mathrm{pH}$ 应为 $4.8 \sim 5.5$；如果 $\mathrm{pH}$ 不在此范围内，用无水乙酸滴定。最终体积定容至 $1\mathrm{L}$。
4. 过滤后  $4^{\circ}$ C 保存。

## RNase H (10 mg/mL)(无 DNase)

1. 在一个洁净的 $15 \mathrm{~mL}$ 离心管中, 加入:

| 牛胰 RNase H | 100mg |
| --- | --- |
| 乙酸钠(10mmol/L, pH4.8) | 9mL |

2. 涡旋至 RNase 晶体完全溶解。
3. 将离心管置于沸水浴中 15min。取出离心管，冷却至室温（5min）。
4. 加入 1mL 的 1mol/L Tris-Cl，涡旋 30s。
5. 可将此溶液等分为每份 5mL，于-20℃保存。

RNase H 在  $-20^{\circ}C$  可稳定保存 6 个月。

## SDS (10%)

▲制备此溶液时要特别小心。SDS 是一种潜在的神经毒素。制备时应戴口罩，在通风橱里完成。

1. 在一个洁净的 500mL 烧杯中，加入:

| SDS | $50g^{a}$ |
| --- | --- |
| 无菌蒸馏水$^{b}$ | 500mL |

a. 戴手套。
b. 小心加入。

2. 用无菌搅拌棒搅拌直至 SDS 完全溶解。
3. 过滤并室温保存，该溶液在室温下可稳定保存 6 个月。

## 乙酸钠（10mmol/L）

1. 在一个洁净的 $50 \mathrm{~mL}$ 离心管中, 加入:

| 乙酸钠(3mol/L,pH4.8) | 167μL |
| --- | --- |
| 无菌蒸馏水 | 40mL |

2. 涡旋 30s，加入无菌蒸馏水至 50mL。
3. 室温保存，在室温下可稳定保存 6 个月。

Tris-Cl (10mmol/L, pH 8.0)

1. 在一个洁净的 1L 的烧杯中，加入:

| 无菌蒸馏水 | 900mL |
| --- | --- |
| Tris -Cl (1mol/L, pH8.0) | 10mL |

2. 搅拌 5min，倒入 1L 的瓶子中，高压灭菌。

## 方案 2 毛细管测序之 PCR 产物的制备

该方案介绍了 Sanger 毛细管 DNA 测序（方案 3）中扩增产物的制备，如验证克隆或重组质粒。该方法基于方案 LongAmp（第 7 章，方案 5）中的 DNA 扩增方法和 BigDye 测序（方案 3）用的试剂。

向扩增后的产物中加入外切核酸酶和虾碱性磷酸酶的混合物，从而除去 PCR 产物中未结合的引物和多余的 dNTP，然后可直接进行测序。该方案需要用到 Biomek FX 工作站或者多通道移液器。

![](images/page_135_image_12.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

## 试剂

琼脂糖凝胶（1.0%琼脂糖），以  $1 \times TAE$  配制&lt;A&gt;，含有  $0.1 \mu g/mL$  溴化乙锭；其他琼脂糖凝胶电泳所需的试剂和设备见第 2 章、方案 1 的描述

DNA 样品（如克隆或待验证的重组质粒）

dNTP 溶液，包含 4 种 dNTP，每一种的浓度为 10mmol/L(NEB 公司)

乙醇（100%）

外切核酸酶 I（USB 公司）

LongAmp Taq DNA 聚合酶（NEB 公司）

LongAmp Taq 反应缓冲液 (5×, 有  $Mg^{2+}$ )(NEB 公司)

NaOAc (3mol/L, pH4.8)(Sigma-Aldrich 公司)

引物（稀释到浓度为  $10 \mu mol/L$ ，最好用 Tris-HCl 稀释）

上游和下游（正向和反向）引物对于需要扩增的靶 DNA 是特异性的。

虾碱性磷酸酶（USB 公司）

水，PCR 级

## 仪器

Biomek FX 工作站或多通道移液枪（电动或手动的）

离心机

锥形瓶（50mL）

冰盒或带盖子的托盘

PCR 反应板（96 孔）（带裙边或无裙边）

实验板和/或涡流混合器

密封垫（使用硅胶垫或热封胶带）

PCR 仪

![](images/page_136_image_8.jpg)

## 方法

## 模板的扩增

1. 准备一个 96 孔 PCR 反应板。

2. 加  $4 \mu L$  DNA 样本至相应的孔里（25ng/ $\mu L$ ）。

在每个反应中用到的样本总浓度为 100ng。假如材料有限，那么应进行相应的调整使得反应的总体积为 50μL。

3. 准备如下所示的“下层混液”。下面给出的体积是一个单独的反应所需的。制备过量的下层混液，以满足实验中所有的样品和对照的用量。

| LongAmp Taq 酶反应缓冲液(5×,有 $Mg^{2+}$) | 5μL |
| --- | --- |
| 4 种 dNTP 的 dNTP 溶液,每种浓度在 10mmol/L | 1.5μL |
| PCR 级水 | 10.5μL(总体积为 17μL) |

4. 使用多道移液器加  $17 \mu L$  的 “下层混液” 至含有 DNA 样本的相应孔里。

5. 加入引物:每个相应的孔里分别加入  $2 \mu L$ 、 $10 \mu mol/L$  的上游引物和  $2 \mu L$ 、 $10 \mu mol/L$  的下游引物，注意更换吸头来避免不同孔之间的污染。

6. 密封 96 孔板，短暂离心以使所有液体聚集到孔底。在进行下一个步骤之前预热 PCR 仪（请参阅步骤 9 中的参数）。

整个循环程序大概是 1.5h。

7. 准备如下所示的 “上层混液”。下面给出的体积是一个单独的反应所需的。制备过量的上层混液，以满足实验中所有的样品和对照的用量。

| LongAmp Taq 酶反应缓冲液(5×,有 ${\mathrm{{Mg}}}^{2 + }$) | ${5\mu }\mathrm{L}$ |
| --- | --- |
| LongAmp Taq DNA 聚合酶 | ${2\mu }\mathrm{L}$ |
| PCR 级水 | 18μL (总体积为 25μL) |

8. 使用多道移液器加 $25 \mu \mathrm{L}$ 的“上层混液”至相应的孔里（非常重要的是，要将“上层混液”置于“下层混液/模板/引物”层的上面）。用一个的硅胶垫或热封胶带将板密封；接下来打开PCR仪。

9. 将反应管放置在 PCR 仪上，按下表中设置程序（这里列出了典型的循环条件）并进行扩增。

| 循环数 | 变性 | 复性及延伸 |
| --- | --- | --- |
| 1 | 94°C, 1min |  |
| 35个循环 | 94°C, 15s | 62°C, 80s |
| 末循环 |  | 62°C, 5min |

许多 PCR 仪的结束程序是扩增样品保持在  $4^{\circ}$ C 直至被取出。

复性温度应在最低平均解链温度  $5^{\circ}$ C 以下（引物信息应该由厂商提供）。注意，当使用的复性温度超过  $60^{\circ}$ C，两步法是可行的，如上所示。

聚合酶的延伸时间通常是 50s/kb。

10. 用 $1\%$ 琼脂糖凝胶电泳对选定的样品进行质量控制（QC）检查。

见“疑难解答”。

## 用外切核酸酶/虾碱性磷酸酶处理

在进行毛细管测序前，要用外切核酸酶/虾碱性磷酸酶对 PCR 扩增产物进行处理，以消除多余的引物和 dNTP。

11. 混合下列试剂来准备 “EXO-SAP 预混液”。下面给出的体积是一个单独的反应所需的。制备过量的预混液，以满足实验中所有待处理的样品。

| 外切核酸酶I | 0.3μL |
| --- | --- |
| 虾碱性磷酸酶 | 0.15μL |
| PCR级水 | 1.55μL(总体积2μL) |

12. 加  $2 \mu L$  EXO-SAP 预混液至 96 孔 PCR 反应板的每个孔的底部。

13. 每个 PCR 产物取 $8 \mu \mathrm{L}$ 加入到相应的孔中, 使总反应体积为 $10 \mu \mathrm{L}$ 。

PCR 产物的体积可以按比例增加或下降，这取决于测序反应所需的产物的量，而这个量又是由扩增子的质量和数量决定的。

14. 用一个硅胶垫或热封胶带将板密封，然后短暂离心并将其放置在 PCR 仪上。执行下列程序:

$37^{\circ}$ C, 1h

然后  $72^{\circ}$ C，30min

此板可以储存在-20℃下或可以直接用于测序反应。

![](images/page_137_image_15.jpg)

## 疑难解答

问题（步骤 10）:QC 评估表明扩增失败。

解决方案:在扩增“样本”DNA之前，用对照组DNA进行PCR测试来判断引物的质量。扩增产物通过琼脂糖凝胶纯化并查看结果。如果凝胶图像是可以接受的（即看到适当大小的单一条带），继续用“样品”的DNA来进行下一步实验。如果凝胶图像是不可接受的（多条带或引物二聚体），那么就改变（提高或降低）复性温度（进一步详情，请参阅第7章的介绍）。

## 方案 3 循环测序反应

循环测序往往被用于直接测定克隆以检测基因突变及基因结构。模板通常是由小量提取质粒得到（如方案1所述）。在测序反应中，按方案2所描述的方法制备的扩增产物可以分别用LongAmp扩增反应中的两个引物来进行测序。两条用于扩增模板的引物都是基于“目的片段”特异设计的。这种使用ABI3730xl毛细管测序的方法也可以用来验证基因型数据和检验更先进的DNA测序技术得到的结果（例如，Illumina公司或Pacific Biosciences公司；详见在这些平台的讨论简介）。

![](images/page_138_image_2.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

## 试剂

ABI BigDye V1.1 (Life Technologies 公司)

ABI 测序缓冲液（5×）（Life Technologies 公司）

琼脂糖凝胶（1.0%琼脂糖），以  $1 \times TAE$  配制&lt;A&gt;，含有  $0.1 \mu g/mL$  溴化乙锭；其他琼脂糖凝胶电泳所需的试剂和设备，见第 2 章、方案 1 的描述

dNTP 溶液，含有所有 4 种 dNTP，每种浓度为 10mmol/L（NEB 公司）

乙醇（100%和70%）

引物（稀释到浓度为  $10 \mu mol/L$ ，最好用 Tris-HCl 稀释）

上游和下游引物（正向和反向）是测序靶 DNA 中的特异序列。

模板 DNA

这里的模板可以是方案 1 中准备的质粒或方案 2 中扩增的 PCR 产物（用 Exo-SAP 处理过的）（见 “讨论” 部分）。

## 设备

ABI3730xl 毛细管测序仪

Biomek FX 液体工作站或者多道移液器

离心机

锥形管（50 mL）

冰盒或带盖子的托盘

PCR 反应板（96 孔）（带裙边或无裙边）

实验板和/或涡流混合器

密封垫（使用硅胶垫或热封胶带）

PCR 仪

![](images/page_138_image_25.jpg)

## 方法

## 循环测序法

1. 准备循环测序反应混合液。下面给出的体积是一个单独的反应所需的。准备过量的混合液，以满足所有的测序样品。

| ABI BigDye version 1.1 | ${1\mu }\mathrm{L}$ |
| --- | --- |
| ABI 测序缓冲液(5×) | ${1.5\mu }\mathrm{L}$ |
| PCR 级水 | ${1.5\mu }\mathrm{L}\left( {{4\mu }\mathrm{L}\text{ 总体积 }}\right)$ |

2. 加  $4 \mu L$  的循环测序反应混合液至 96 孔 PCR 反应板的各个孔中。

3. 每个孔中加入  $1 \mu L$   $10 \mu mol/L$  引物。

从方案 2 中得到的 PCR 产物，其测序引物与扩增它们的引物是相同的。

4. 加入适当体积的模板 DNA。由于该反应的总体积为 $10\mu \mathrm{L}$，模板 DNA 产物的体积不应超过 $5\mu \mathrm{L}$。如果小于 $5\mu \mathrm{L}$，加适量的 PCR 级水来弥补体积的差异。

在进行下一个步骤之前预热 PCR 仪（参见步骤 7 中的设置）。

5. 用一个硅胶垫或热封胶带来密封 96 孔 PCR 反应板。

6. 离心 96 孔 PCR 反应板。

7. 将 96 孔 PCR 反应板放入 PCR 仪中，按下表中设置程序，并进行测序:

| 循环数 | 变性 | 复性 | 延伸 |
| --- | --- | --- | --- |
| 1 | 96°C, 2min |  |  |
| 35 | 96°C, 10s | 50°C, 5s | 60°C, 4min |

$4^{\circ}\mathrm{C}$ 保存

## BigDye 循环测序反应的沉淀

8. 循环完成后，立即离心 96 孔 PCR 反应板。

9. 准备一份“沉淀预混液”，在 $50\mathrm{mL}$ 锥形管混合 $1\mathrm{mL}3\mathrm{mol / L}$ 乙酸钠和 $23\mathrm{mL}100\%$ 的乙醇。

10. 取  $25 \mu L$  沉淀预混液加入到循环测序板（即上述 96 孔 PCR 反应板）各孔里。

11. 快速涡旋 96 孔 PCR 反应板使液体混合, 然后离心。

12. 将 96 孔 PCR 反应板置于冰盒或带盖子的托盘中（ABI 的 BigDye 试剂是光敏感的）冰浴 30min。

要确保所有的孔都在冰面下。

13. 将 96 孔 PCR 反应板以 4000r/min 离心 30min。

14. 从96孔PCR反应板中倒出液体，并轻轻拍打，把所有剩余的液体都吸附到纸巾上，注意不要搅动沉淀。

15. 加 $200\mu \mathrm{L}$ 的 $70\%$ 乙醇到相应的孔中，用硅胶垫密封96孔PCR反应板，颠倒三次来清洗孔壁。

16. 将 96 孔 PCR 反应板以 4000 r/min 离心 15min。

17. 从 96 孔 PCR 反应板中倒出液体，并在纸巾上轻轻拍打 96 孔 PCR 反应板。

18. 重复步骤 15～17，总共用 70%乙醇洗涤两次。

19. 第二次洗涤后，再次离心 96 孔 PCR 反应板，这次将 96 孔 PCR 反应板翻扣于折叠纸巾上，以 $200 \mathrm{r} / \mathrm{min}$ 的转速除去过量的乙醇。

20. 将 96 孔 PCR 反应板放置在一个 PCR 仪上，37°C、10 min 或室温下 1 h，晾干。

▲在沉淀结块重悬之前必须确保将96孔PCR反应板的乙醇清除干净。

21. 在确定所有的孔晾干之后，加 $30\mu \mathrm{L}$ 的PCR级水至96孔PCR反应板各孔中并用胶垫密封好。

22. 用涡旋振荡器高转速（2500 r/min）涡旋96孔PCR反应板10min。

23. 为了使样品达到能在 ABI3730x1 毛细管测序仪进行分析的标准，还需用甲酰胺在 384 孔板中稀释样品，稀释方法如下:

i. 选择合适数量的孔，每孔加入  $4 \mu L$  甲酰胺。

ii. 每孔加入  $3 \mu L$  重悬的沉淀测序产品，总体积共  $7 \mu L$ ，用来上样。

用 384 孔板稀释是为了避免上样量过大，因为上样量过大会使信号强度过高，从而导致碱基判读出错。

![](images/page_140_image_2.jpg)

## 讨论

这些反应所需的扩增产物（经外切核酸酶/虾碱性磷酸酶处理纯化）的体积应通过肉眼观察扩增产物的亮度来估算和均一化。大体上来说，如果条带看上去“弱”，那么可以用5μL经EXO-SAP处理过的产物进行循环测序反应。对于一个看上去“强”的条带，用1～2μL经EXO-SAP处理过的产物就可以了。此外，如果要验证ABI3730xl毛细管测序仪上得到的结果，可以使用1/8体积的BigDye V.1.1反应体系重复上述测序反应。

## 方案 4 全基因组:手工文库制备

此方案介绍手工方法制备适用于 Illumina 测序的基因组文库。将超声破碎获得的基因组 DNA 片段连接到接头并进行 PCR 扩增；随后通过凝胶电泳分离和筛选合适片段的扩增 DNA，即可作为全基因组测序的模板。自动化的文库制备方法见方案 5 和方案 6。

![](images/page_140_image_7.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

```txt
聚丙烯酰胺凝胶，预制（Life Technologies 公司）
dATP (1mmol/L)
DNA 分子质量标记(100bp) (NEB 公司)
DNA 分子质量标记 (50bp) (TrackIt; Life Technologies 公司)
DNA 1000 reagents (Agilent 公司)
DNA Terminator End Repair Kit (Lucigen 公司)
乙醇(70% 和 100%)
FlashGel DNA 电泳槽(2.2%, 12+1 孔) (Lonza 公司)
FlashGel DNA 分子质量标记(50bp～1.5kb) (Lonza 公司)
FlashGel 上样染料 (Lonza 公司)
含溴酚蓝的凝胶上样缓冲液(10×)<A>
基因组 DNA
GlycoBlue (15mg/mL) (Ambion 公司)
Klenow 片段外切核酸酶(New England Biolabs 公司)
MinElute PCR Purification Kit (QIAGEN 公司)
NaCl (400mmol/L)
PE forked adaptor duplex (4μmol/L) (Illumina, Sigma-Aldrich 公司)
```

PE PCR 引物 1.0 (8μmol/L) (HPLC purification, 100-nm scale; IDT):

A\*ATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT

PE PCR 引物 2.0 (8μmol/L) (HPLC purification, 100-nm scale; IDT):

C\*AAGCAGAAGACGGCATACGAGATCGGTCTCGGCATTCCTGCTGAACCGCTCTTCCGATCT

Phusion High-Fidelity PCR Master Mix with HF Buffer (2×) (Finnzymes 公司)

Quick Ligation Kit (NEB 公司)

SYBR Green I nucleic acid gel stain (Life Technologies 公司)

TBE 缓冲液&lt;A&gt;

TBE 凝胶(Novex 4%\~12%, 1.0mm×12 well) (Life Technologies 公司)

## 设备

DNA 1000 芯片和分析仪(Agilent 公司)

荧光光度计（例如，Qubit 公司，Life Technologies 公司）

HV DuraPore filter columns (0.4μm) (Millipore 公司)

微量离心管 (0.2mL 和 1.7mL)

microTube (6mm×16 mm), with AFA fiber and Snap-Cap (Covaris 公司)

Quant-iT dsDNA High Sensitivity Assay Kit (Life Technologies 公司)

超声破碎仪(Covaris 公司)

THQmicro microTube holder (Covaris 公司)

XCell SureLock Mini-Cell (Life Technologies 公司)

![](images/page_141_image_21.jpg)

## 方法

## 文库的超声处理和片段的末端修复

1. 准备 100ng、500ng、1μg 或 3μg 基因组 DNA 样品。

2. 按下述配方在 $1.7 \mathrm{ml}$ 离心管中稀释 DNA:

| 末端修复缓冲液(5×) | 10μL |
| --- | --- |
| DNA 样品 | xμL |
| 纯水 | (40-x)μL |
| 总体积 | 50μL |

振荡混匀 1\~2s 后，离心 5s。

3. 将稀释后的 DNA 转入超声仪样品管，离心以确保溶液中无气泡。

4. 参照超声仪说明书对样品进行超声处理。

提供你要处理的目的片段的大小以决定选择合适的超声处理条件。

5. 将 DNA 进行破碎后，从（冰）水浴中取出样品管，离心收集样品于管底。

6. 往样品管加入  $2 \mu L$  末端修复酶混合液，轻轻振荡混匀，短暂离心，室温下反应 30min。

7. 在 $1.7 \mathrm{~mL}$ 离心管中混合 $50 \mu \mathrm{L}$ 反应液和 $250 \mu \mathrm{L} \mathrm{PB}$ 或 PBI 缓冲液, 振荡混匀。

8. 按下述方法用 MinElute 柱纯化 DNA:

i. 将步骤 7 的混合液加入 MinElute 柱，14 000g 离心 1min，或者放入抽真空装置中抽出液体。

ii. 若离心，弃去废液。

iii. 加  $750 \mu L$  的 PE 缓冲液，14 000g 离心 1min，或者放入抽真空装置中抽出液体。

iv. 若离心，弃去废液。

v. 加 750uL 的 PE 缓冲液，14 000g 离心 1min，或者放入抽真空装置中抽出液体。

vi. 若离心，弃去废液；若使用抽真空装置，将柱子放入废液收集管，14 000g 离心 1min。

vii. 将管子旋转  $180^{\circ}$ ，14 000g 离心 1min。

viii. 弃去废液管。

ix. 将柱子放入 1.7mL 的离心管。

x. 往柱子里加 16μL EB 缓冲液，室温孵育 1min，14000g 离心 1min。

xi. 如果需要的话，可再在柱子里加  $16 \mu L$  的 EB 缓冲液，室温孵育 1 min，14 000 g 离心 1 min。

只有超声破碎的 DNA 量过多时（如  $3\mu g$ ）才需进行两次洗脱。

xii. 弃掉柱子，样品转至0.2mL的PCR管。

## 3' 端腺苷酰化 (加 A 尾)

9. 用步骤 8.xii 纯化的 DNA 进行加 A 尾

| 纯化的末端修复 DNA | 32μL |
| --- | --- |
| Klenow 缓冲液(10×) | 5μL |
| dATP (1.0mmol/L) | 10μL |
| Klenow 外切核酸酶(5U/μL) | 3μL |
| 总体积 | 50μL |

移液器上下摇匀，短暂离心，37℃孵育30min。

10. 在 1.7mL 离心管中，将 50μL 反应液与 250μL PB 缓冲液振荡混匀。

11. 按照步骤 8.i～8.xii 用 MinElute 柱对 DNA 进行纯化，其中 EB 洗脱液用量如下表中所示:

<table><tr><td colspan="4">起始 DNA 样品量</td></tr><tr><td>100ng</td><td>500ng</td><td>1μg</td><td>3μg</td></tr><tr><td>10μL 两次</td><td>10μL 两次</td><td>18μL 两次</td><td>18μL 两次</td></tr></table>

## 接头连接

12. 使用加 A 尾反应的纯化产物（得自步骤 11），按下表准备接头连接反应:

<table><tr><td rowspan="2"></td><td colspan="4">起始 DNA 样品量</td></tr><tr><td>100 ng</td><td>500 ng</td><td>1μg</td><td>3μg</td></tr><tr><td>纯化的带 A 尾 DNA</td><td>20μL</td><td>20μL</td><td>20μL</td><td>20μL</td></tr><tr><td>PE forked adaptor duplex</td><td>1.0μL</td><td>2.5μL</td><td>5.0μL</td><td>7.0μL</td></tr><tr><td>NEB 快连缓冲液 (2×)</td><td>25μL</td><td>25μL</td><td>25μL</td><td>25μL</td></tr><tr><td>水</td><td>1.5μL</td><td>—</td><td>—</td><td>—</td></tr><tr><td>NEB 快速连接酶 (2000U/mL)</td><td>2.5μL</td><td>2.5μL</td><td>2.5μL</td><td>2.5μL</td></tr><tr><td>总体积</td><td>50μL</td><td>50μL</td><td>52.5μL</td><td>54.5μL</td></tr></table>

i. 在离心管中混合 DNA 与接头，短暂离心。

ii. 加2×缓冲液和水，吹打混匀，短暂离心。

iii. 加连接酶，吹打混匀，短暂离心。

iv. 室温孵育 15min。

13. 按步骤 8.i～8.xii，用 MinElute 柱对 DNA 进行纯化，其中步骤 8.x 和步骤 8.xi EB 洗脱液用 10μL。
14. 使用 Quant-iT dsDNA HS Assay Kit (用于 100ng 起始 DNA 样品量) 或 BR Assay Kit (其他量), 用 $1 \mu \mathrm{L}$ DNA 测 DNA 浓度, 荧光光度计读取结果 (应用方案 11 或方案 12)。

纯化的、连接好的 DNA 产量应该不少于起始 DNA 样品量的 20%。例如，100ng 的初始 DNA 文库应该产生不少于 20ng 的连接好的 DNA。

若纯化的 DNA 浓度>10ng/ $\mu$ L，按下表用 EB 缓冲液稀释样品:

| 起始 DNA 样品量 | 稀释至 |
| --- | --- |
| 100ng | 1ng/μL |
| 500ng | 10ng/μL |
| 1μg | 10ng/μL |
| 3μg | 10ng/μL |

## 样品用量按下述方法计算

定量后样品的洗脱体积为  $10.5 \mu L$ 。DNA 浓度为  $21.6 ng/\mu L$ 。如果起始 DNA 样品量是 500ng 的话，要将纯化好的 DNA 稀释至  $10 ng/\mu L$ 。用下面的公式计算需要添加多少 EB 缓冲液到样品中，从而获得浓度为  $10 ng/\mu L$  的样品。

最终体积= $(10.5\mu L \times 21.6ng/\mu L)/(10ng/\mu L)=22.68\mu L$

22.68μL-10.5μL=12.18μL≈12.2μL←添加 12.2μL 的 EB 缓冲液到样品中以稀释至 10ng/μL。

## PCR 循环数优化

15. 在 $0.2 \mathrm{~mL}$ PCR 管里, 为每个文库构建反应设置扩增反应。不管有多少样品, 都要设一个阴性对照 (用 EB 缓冲液替代 DNA)。可以先配置不含 DNA 的扩增反应混合液, 分装至 $0.2 \mathrm{~mL}$ PCR 管中。然后加入 $1 \mu \mathrm{L}$ 样品或 EB 缓冲液 (阴性对照), 混匀并短暂离心。

| 从连接反应(步骤13)纯化获得的DNA样品 | 1μL |
| --- | --- |
| Phusion PCR master mix (2×) | 25μL |
| PCR PE 引物 1.0 (8μmol/L) | 1μL |
| PCR PE 引物 2.0 (8μmol/L) | 1μL |
| 水 | 22μL |
| 总体积 | 50μL |

## 16. 设置 2 个 PCR 程序

## 程序 1

| 循环数 | 变性 | 复性 | 聚合 |
| --- | --- | --- | --- |
| 1 | 98°C, 30s |  |  |
| 4或${6}^{\text{a}}$个循环 | 98°C, 10s | 65°C, 30s | 72°C, 30s |

a. 10ng PCR 进行 4 个循环，1ng PCR 进行 6 个循环。

程序结束后维持在  $4^{\circ}$ C。