# 替代方案 在大肠杆菌中利用阿拉伯糖 BAD 启动子表达克隆基因

来源于 ara 操纵子的 L-阿拉伯糖诱导系统提供了一种基于 lac 操纵子的替代表达系统。例如，pBAD 系列载体（New England Biolabs）运用 araBAD 启动子和 AraC 抑制基因来调控蛋白质的表达。

使用 araBAD 启动子有一些限制条件，详见于讨论部分。尽管有这些限制条件，araBAD 仍然是一个可有效替代乳糖操纵子的启动子。由于 araBAD 是一个严谨型启动子，因此在大肠杆菌中表达毒性基因时，ara 系统是不错的选择。ara 系统可用于分离和研究必需基因的无义突变，以及这些基因敲除后的表型评估等（Guzman et al. 1995）。

![](images/page_176_image_5.jpg)

## 附加材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

L-阿拉伯糖（20%，m/V）

20g L-阿拉伯糖溶解于 100mL 水中，0.22μm 滤器过滤除菌

![](images/page_176_image_11.jpg)

## 方法

1. 按照方案1,用0.2%阿拉伯糖(1:100稀释)替代步骤7和步骤15中的0.5mmol/L IPTG。

![](images/page_176_image_14.jpg)

## 讨论

一种常见的误解是 araBAD 启动子可调控基因表达量，即培养基中提供的 L-阿拉伯糖浓度能够控制细胞内重组蛋白的表达量。添加到培养基中 L-阿拉伯糖的量和目标蛋白产量之间量效关系，不是由一群中间诱导水平的均一细胞产生的，而是由一群完全诱导和完全不诱导的细胞混合产生的（Siegele and Hu 1997）。相似的现象还发现在衍生的 lac 启动子的 L-乳糖诱导中（Novick and Weiner 1957）。在这两个例子中，全有或全无的表达水平是因为用于糖分子转运透酶量的自调控引起的（Khlebnikov et al. 2000; Khlebnikov and Keasling 2002）。像这样期望通过 L-阿拉伯糖或 L-乳糖诱导剂的浓度调控来克服与蛋白质表达相关的宿主酶的饱和（或）高浓度下蛋白质的聚集是起不了多少作用的。与之相反的是，乳糖类似物 IPTG 既能通过被动扩散的方式进入大肠杆菌中，也能借助 lac 透性酶（lacY）运送（Rickenberg et al. 1956）。因此，IPTG 浓度变化能够提供一个中间水平的基因表达，尤其是利用 lacY 基因灭活的宿主菌时（如 the Tuner, Origami, 或 Merck Biosciences 提供的 Rosetta 菌株）。

第二种误解是，相比于 IPTG，阿拉伯糖较低的成本更适合用于在大肠杆菌中外源基因的大规模化生产。在通常用于蛋白质表达中的浓度，诱导用的阿拉伯糖和 IPTG 在成本方面几乎无区别。尽管自身诱导的方法已经运用在阿拉伯糖和 IPTG 诱导载体中，但是这种方法中使用的确定成分培养基还是相对昂贵的（Studier 2005）。在成本是重要的考虑因素的情况下，温度诱导型启动子是一个更为可行的选择。例如，噬菌体  $\lambda$  pL 启动子和温敏抑制基因 cIts857 相结合，可利用提升温度（>40℃）诱导外源基因表达（Buell et al. 1985）。但是，要注意  $\lambda$  pL 系统有一些缺点，它会诱导某些编码细胞蛋白酶的热激基因同步表达，还有可能发生高温下蛋白质错误折叠的可能性。

## 替代方案 信号肽融合蛋白的亚细胞定位

对于某些蛋白质，分泌到周质空间表达要优于传统的在细胞质中表达的方式（详见讨论部分）。在本方案中，通过将编码序列与编码信号肽的 DNA 序列融合（如利用 pET-22b）来实现蛋白质的外运，而信号肽可在蛋白质运输到大肠杆菌细胞内膜与外膜之间的空间时被信号肽酶切除。通过检测细胞质 6-磷酸葡萄糖脱氢酶可用以区分是周质蛋白的选择性释放还是通常的细胞裂解（Battistuzzi et al. 1977）。更为准确地分析信号肽融合蛋白在不同的细胞空间内的分布，需要运用标志酶来分析每一个亚细胞组分的纯度（周质空间、细胞膜和细胞质）（Guzman-Verduzco and Kupersztoch 1990）。本方法虽然不能定量，但能提供信号肽融合蛋白细胞定位的初步信息。

![](images/page_177_image_5.jpg)

## 附加材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

丙酮（步骤2）

细胞裂解缓冲液（蔗糖 20%，m/V；30mmol/L Tris-Cl, pH 8.0）

来源于方案 1，步骤 1～步骤 5 的 E. coli 培养物（含重组表达载体）

EDTA (500mmol/L, pH 8.0)

溶菌酶（1mg/mL）

见原生质球制备试剂盒。

渗透压休克缓冲液（5mmol/L  $MgSO_{4}$ ），预冷

多黏菌素 B（400μg/mL）

见原生质球制备试剂盒。

SDS 上样缓冲液（5×）

见方案8。

室温储存无二硫苏糖醇的  $5 \times SDS$  上样缓冲液。使用前加入 1mol/L 二硫苏糖醇储存液。

原生质球裂解缓冲液（100mmol/L Tris-Cl，pH 8.0）

三氯乙酸（100%，m/V）（见步骤2）

Tris-Cl (0.1mol/L, pH 8.0)

漂洗缓冲液（10mmol/L Tris，pH 8.0），预冷

## 设备

离心浓缩仪

干冰或者液氮

冰浴器

离心真空浓缩仪

## 原生质球的制备

本方案运用渗透压休克从周质中释放多肽（Neu and Heppel 1965）。其他的原生质球制备的方法包括利用溶菌酶处理（Repaske 1958; Marvin and Witholt 1987）、氯仿处理（Ames et al. 1984）和多肽抗生素多黏菌素B处理（Cerny and Teuber 1971）。

## 溶菌酶处理

使用溶菌酶时，在 30mmol/L Tris-Cl/20%蔗糖中添加 1mg/mL 溶菌酶，省略 5mmol/L MgSO₄ 的渗透压休克步骤。利用 10mmol/L Tris（pH 8.0）清洗细胞的步骤也可以省略。

使用溶菌酶制备原生质球存在两个潜在的缺点。第一，某些商业化的溶菌酶含有水解酶，可能会裂解菌细胞。第二，如果外源目标蛋白的分子质量大小和溶菌酶（约15 000kDa）类似，那么在缓冲液中存在的溶菌酶可能会阻碍目标蛋白经聚丙烯酰胺凝胶（电泳）染色后的观察。相应地，本方案中的渗透压休克方法不应该使用过表达溶菌酶（plysS或plysE）的大肠杆菌宿主，因为它会破坏细胞内膜而释放细胞质内部组分。

## 抗生素处理

使用抗生素释放周质空间内的多肽，用 1mL 的 400 g/mL 多黏菌素 B 重悬步骤 1 中的细胞，冰上放置 2h。按步骤 7 离心处理的细胞。上清中含周质蛋白，细胞沉淀含细胞质蛋白和膜蛋白，按照步骤 9 和步骤 10 所述，可以再次将两者分离。

![](images/page_178_image_15.jpg)

## 方法

1. 按照方案 1 中的步骤 1～步骤 5，通过加入 0.5mmol/L IPTG，在 37℃ 下培养 2～4h，诱导蛋白表达（按需加入 100μg/mL 氨苄青霉素）。设未诱导阴性和阳性平行对照。

2. 培养物于  $4^{\circ}$ C 5000g 离心 15min，以沉淀细胞，去除上清。

检测上清中是否有渗漏的分泌蛋白，可按此操作:

i. 在  $800 \mu L$  LB 上清中加入  $100 \mu L$  的  $100\% (m/V)$  三氯乙酸（TCA）。

ii. 将酸化溶液在冰上放置至少 20min，然后以最大转速离心 20min，去除上清。

iii. 用  $100 \mu L$  丙酮洗沉淀，以最大转速离心回收沉淀。用丙酮重复洗涤一次后，完全晾干沉淀（或用真空离心蒸发浓缩仪短暂离心）。

iv. 用  $50 \mu L$   $1 \times$  PBS 和  $50 \mu L$   $5 \times$  SDS 上样缓冲液重悬沉淀，剧烈振荡混匀。

v.  $85^{\circ}$ C下加热3min，然后上样前始终放置于冰上，取 $20\mu L$ 样品进行SDS-PAGE（步骤11）。

3. 加入 4mL 洗涤缓冲液清洗细胞沉淀。5000g 离心细胞去除洗涤缓冲液。洗涤共重复 3 次。第二步洗涤之后细胞可在 4℃ 下存放过夜。

渗透压休克之前细胞洗涤可以显著地增加周质蛋白产量（Neu and Heppel 1965）。

4. 室温下用 7.5mL 细胞裂解缓冲液重悬细胞，然后加入  $15 \mu L$  的 500mmol/L EDTA 至

其终浓度为 1mmol/L。室温下轻微混匀 10min。

5. 于  $4^{\circ}$ C 10 000g，离心 10min 收集细胞。弃上清。
6. 用 7.5mL 预冷渗透压休克缓冲液充分重悬细胞沉淀。冰浴下轻微混匀 10min。经该步处理，周质蛋白被释放进入缓冲液。
7. 于 $4^{\circ} \mathrm{C} 10000 \mathrm{~g}$, $10 \mathrm{~min}$ 离心来自于步骤6的重悬细胞, 分离原生质球 (沉淀)。回收包含周质蛋白的上清, 置于冰上保存。
8. SDS-PAGE 分析之前浓缩上清。可以参照步骤 2 中上清液的 TCA 沉淀法，或者利用离心浓缩仪浓缩样品至  $100 \mu L$  体积。

建议在离心浓缩周质蛋白前，分别加入终浓度为 150mmol/L 的 NaCl 和 25mmol/L 的 Tris-Cl（pH 8.0）。因为在低离子强度和不适 pH 条件下，很少有蛋白质具有高度可溶性。

9. 用 1mL 的 0.1mol/L Tris-Cl（pH 8.0）重悬原生质球沉淀，通过反复冻融裂解细胞，将细胞置于液氮中的干冰上冷冻，然后在 37℃ 融解，至少重复 2 次该过程。

10. 于 $4^{\circ} \mathrm{C}$, 最大转速下离心上述悬液 $5 \mathrm{~min}$ 。胞质蛋白存在于上清中。用 $100 \mu \mathrm{L} 0.1 \mathrm{~mol} / \mathrm{L}$ Tris-Cl（$\mathrm{pH} 8.0$）重悬含有细胞膜和不可溶的包含体沉淀，并剧烈涡旋振荡。

11. 在每个  $100 \mu L$  的亚细胞部分中加入  $20 \mu L$  的  $5 \times SDS$  上样缓冲液，充分混合，然后在  $85^{\circ}C$  下加热 3min。室温下，最大转速 1min 离心加热样品。

12. 每个组分取  $20 \mu L$  进行 SDS-PAGE 分析（见方案 8）。用考马斯亮蓝染胶，测定外源蛋白在亚细胞中的定位，以及蛋白质分泌进入周至空间的效率如何。

![](images/page_179_image_13.jpg)

## 讨论

对于某些蛋白质，输送至周质具有几个优势。

1. 二硫键常常稳定细胞外蛋白质的折叠。正确的二硫键形成需要氧化环境以及定位于周质中酶的辅助。人生长激素表达是一个被发现在细胞质与周质空间中的外源蛋白的二硫键形成和蛋白折叠不同的早期例子（Gray et al. 1985; Becker and Hsiung 1986）。
2. 有些易被细胞内蛋白酶降解的蛋白质在周质中是稳定的（如 Talmadge and Gilbert 1982）。
3. 因为周质蛋白占细胞总蛋白量<20%，与细胞质蛋白相比，初始纯化时所含的杂蛋白较少（Ghrayeb et al. 1984）。
4. 当毒性蛋白如核酸酶或者蛋白水解酶翻译后直接分泌到周质空间时，有可能对宿主细胞的毒性较小（Bhattacharya et al. 2005）。

在大肠杆菌中，蛋白质通过内膜进入周质空间存在几条途径（综述见 Natale et al. 2008）。大多数可将重组蛋白定位于周质空间的载体利用了翻译后分泌途径（Sec），通过相对短的氨基端信号序列（约 20 个氨基酸）直接输送外源的融合蛋白。紧接着，信号肽酶从易位的多肽上切除信号肽，该酶要求切割位点周围为非大分子氨基酸。普遍用于融合蛋白的定位信号肽序列包括:E. carotovora 果胶酶 B（pelB），噬菌体 f1 基因 III（gIII），E. coli 外膜蛋白 3a（OmpA），E. coli 碱性磷酸酶（PhoA）。在某些情况下，真核生物的信号肽序列也可以直接用于大肠杆菌表达外源蛋白的分泌或者信号肽加工（Talmadge et al. 1980; Gray et al. 1985）。

在外源蛋白输送的过程中遇到的主要问题是信号肽不能切除或者切除的位点不准确（Yuan et al. 1990）、二硫键形成错误，以及产量通常很低。解决这些问题，可以在信号肽序列切割位点和外源蛋白之间插入空间隔离氨基酸，与外源蛋白融合能够催化二硫键形成的酶（DsbA, DsbC, 或硫氧还蛋白），或者利用过表达一种或多种 Sec 途径基因的大肠杆菌宿主。

## 参考文献

- Ames GF, Prody C, Kustu S. 1984. Simple, rapid, and quantitative release of periplasmic proteins by chloroform. J Bacteriol 160: 1181–1183.
- Baneyx F. 1999. Recombinant protein expression in Escherichia coli. Curr Opin Biotechnol 10: 411–421.
- Bardwell JC, McGovern K, Beckwith J. 1991. Identification of a protein required for disulfide bond formation in vivo. Cell 67: 581–589.
- Battistuzzi G, Esan GJ, Fasuan FA, Modiano G, Luzzatto L. 1977. Comparison of GdA and GdB activities in Nigerians. A study of the variation of the G6PD activity. Am J Hum Genet 29: 31–36.
- Becker GW, Hsiung HM. 1986. Expression, secretion and folding of human growth hormone in Escherichia coli. Purification and characterization. FEBS Lett 204: 145–150.
- Berrow NS, Bussow K, Coutard B, Diprose J, Ekberg M, Folkers GE, Levy N, Lieu V, Owens RJ, Peleg Y, et al. 2006. Recombinant protein expression and solubility screening in Escherichia coli: A comparative study. Acta Crystallogr D Biol Crystallogr 62: 1218–1226.
- Bhattacharya P, Pandey G, Srivastava P, Mukherjee KJ. 2005. Combined effect of protein fusion and signal sequence greatly enhances the production of recombinant human GM-CSF in Escherichia coli. Mol Biotechnol 30: 103–116.
- Brinkmann U, Mattes RE, Buckel P. 1989. High-level expression of recombinant genes in Escherichia coli is dependent on the availability of the dnaY gene product. Gene 85: 109–114.
- Buell G, Schulz MF, Selzer G, Chollet A, Movva NR, Semon D, Escanez S, Kawashima E. 1985. Optimizing the expression in E. coli of a synthetic gene encoding somatomedin-C (IGF-I). Nucleic Acids Res 13: 1923–1938.
- Cerny G, Teuber M. 1971. Differential release of periplasmic versus cytoplasmic enzymes from Escherichia coli B by polymixin B. Arch Mikrobiol 78: 166–179.
- Englander SW, Mayne L, Krishna MM. 2007. Protein folding and misfolding: Mechanism and principles. Q Rev Biophys 40: 287–326.
- Esposito D, Chatterjee DK. 2006. Enhancement of soluble protein expression through the use of fusion tags. Curr Opin Biotechnol 17: 353–358.
- Ghrayeb J, Kimura H, Takahara M, Hsiung H, Masui Y, Inouye M. 1984. Secretion cloning vectors in Escherichia coli. EMBO J 3: 2437–2442.
- Gray GL, Baldridge JS, McKeown KS, Heyneker HL, Chang CN. 1985. Periplasmic production of correctly processed human growth hormone in Escherichia coli: Natural and bacterial signal sequences are interchangeable. Gene 39: 247–254.
- Gruber AR, Lorenz R, Bernhart SH, Neubock R, Hofacker IL. 2008. The Vienna RNA websuite. Nucleic Acids Res 36: W70–W74.
- Guzman LM, Belin D, Carson MJ, Beckwith J. 1995. Tight regulation, modulation, and high-level expression by vectors containing the arabinose pBAD promoter. J Bacteriol 177: 4121–4130.
- Guzman-Verduzco LM, Kupersztoch YM. 1990. Export and processing analysis of a fusion between the extracellular heat-stable enterotoxin and the periplasmic B subunit of the heat-labile enterotoxin in Escherichia coli. Mol Microbiol 4: 253–264.
- Hammarstrom M, Woestenenk EA, Hellgren N, Hard T, Berglund H. 2006. Effect of N-terminal solubility enhancing fusion proteins on yield of purified target protein. J Struct Funct Genomics 7: 1–14.
- Herbst B, Kneip S, Bremer E. 1994. pOSEX: Vectors for osmotically controlled and finely tuned gene expression in Escherichia coli. Gene 151:137–142.
- Hirel PH, Schmitter MJ, Dessen P, Fayat G, Blanquet S. 1989. Extent of N-terminal methionine excision from Escherichia coli proteins is governed by the side-chain length of the penultimate amino acid. Proc Natl Acad Sci 86: 8247–8251.
- Khlebnikov A, Keasling JD. 2002. Effect of lacY expression on homogeneity of induction from the  $P_{tac}$  and  $P_{trc}$  promoters by natural and synthetic inducers. Biotechnol Prog 18: 672–674.
- Khlebnikov A, Risa O, Skaug T, Carrier TA, Keasling JD. 2000. Regulatable arabinose-inducible gene expression system with consistent control in all cells of a culture. J Bacteriol 182: 7029–7034.
- Komai T, Ishikawa Y, Yagi R, Suzuki-Sunagawa H, Nishigaki T, Handa H. 1997. Development of HIV-1 protease expression methods using the T7 phage promoter system. Appl Microbiol Biotechnol 47: 241–245.
- Lathrop BK, Burack WR, Biltonen RL, Rule GS. 1992. Expression of a group II phospholipase A2 from the venom of Agkistrodon piscivorus piscivorus in Escherichia coli: Recovery and renaturation from bacterial inclusion bodies. Protein Expr Purif 3: 512–517.
- Marvin HJ, Witholt B. 1987. A highly efficient procedure for the quantitative formation of intact and viable lysozyme spheroplasts from Escherichia coli. Anal Biochem 164: 320–330.
- Mathews DH, Sabina J, Zuker M, Turner DH. 1999. Expanded sequence dependence of thermodynamic parameters improves prediction of
- RNA secondary structure. J Mol Biol 288: 911–940.
- Missiakas D, Georgopoulos C, Raina S. 1994. The Escherichia coli dsbC (xprA) gene encodes a periplasmic protein involved in disulfide bond formation. EMBO J 13: 2013–2020.
- Natale P, Bruser T, Driessen AJ. 2008. Sec- and Tat-mediated protein secretion across the bacterial cytoplasmic membrane—distinct translocases and mechanisms. Biochim Biophys Acta 1778: 1735–1756.
- Neu HC, Heppel LA. 1965. The release of enzymes from Escherichia coli by osmotic shock and during the formation of spheroplasts. J Biol Chem 240: 3685–3692.
- Nichols BP, Yanofsky C. 1983. Plasmids containing the trp promoters of Escherichia coli and Serratia marcescens and their use in expressing cloned genes. Methods Enzymol 101: 155–164.
- Novick A, Weiner M. 1957. Enzyme induction as an all-or-none phenomenon. Proc Natl Acad Sci 43: 553–566.
- Panavas T, Sanders C, Butt TR. 2009. SUMO fusion technology for enhanced protein production in prokaryotic and eukaryotic expression systems. Methods Mol Biol 497: 303–317.
- Panayotatos N, Truong K. 1981. Specific deletion of DNA sequences between preselected bases. Nucleic Acids Res 9: 5679–5688.
- Preibisch G, Ishihara H, Tripier D, Leineweber M. 1988. Unexpected translation initiation within the coding region of eukaryotic genes expressed in Escherichia coli. Gene 72: 179–186.
- Repaske R. 1958. Lysis of Gram-negative organisms and the role of versene. Biochim Biophys Acta 30: 225–232.
- Reznikoff WS. 1992. The lactose operon-controlling elements: A complex paradigm. Mol Microbiol 6: 2419–2422.
- Rickenberg HV, Cohen GN, Buttin G, Monod J. 1956. La galactoside-permease d'Escherichia coli. Ann Inst Pasteur 91: 829–857.
- Rosenberg AH, Lade BN, Chui DS, Lin S-W, Dunn JJ, Studier FW. 1987. Vectors for selective expression of cloned DNAs by T7 RNA polymerase. Gene 56: 125–135.
- Saida F. 2007. Overview on the expression of toxic gene products in Escherichia coli. Curr Protoc Protein Sci 5: 5.19.1–5.19.13.
- Schenk PM, Baumann S, Mattes R, Steinbiss HH. 1995. Improved high-level expression system for eukaryotic genes in Escherichia coli using T7 RNA polymerase and rare Arg tRNAs. BioTechniques 19:196–200.
- Shine J, Dalgarno L. 1974. The 3'-terminal sequence of Escherichia coli 16S ribosomal RNA: Complementarity to nonsense triplets and ribosome binding sites. Proc Natl Acad Sci 71: 1342–1346.
- Siegele DA, Hu JC. 1997. Gene expression from plasmids containing the araBAD promoter at subsaturating inducer concentrations represents mixed populations. Proc Natl Acad Sci 94: 8168–8172.
- Studier FW. 2005. Protein production by auto-induction in high density shaking cultures. Protein Expr Purif 41: 207–234.
- Studier FW, Moffatt BA. 1986. Use of bacteriophage T7 RNA polymerase to direct selective high-level expression of cloned genes. J Mol Biol 189: 113–130.
- Tacon WC, Bonass WA, Jenkins B, Emtage JS. 1983. Expression plasmid vectors containing Escherichia coli tryptophan promoter transcriptional units lacking the attenuator. Gene 23: 255–265.
- Talmadge K, Gilbert W. 1982. Cellular location affects protein stability in Escherichia coli. Proc Natl Acad Sci 79: 1830–1833.
- Talmadge K, Kaufman J, Gilbert W. 1980. Bacteria mature preproinsulin to proinsulin. Proc Natl Acad Sci 77: 3988–3992.
- Tobias JW, Shrader TE, Rocap G, Varshavsky A. 1991. The N-end rule in bacteria. Science 254: 1374–1377.
- Tresaugues L, Collinet B, Minard P, Henckes G, Aufrere R, Blondeau K, Liger D, Zhou CZ, Janin J, Van Tilbeurgh H, et al. 2004. Refolding strategies from inclusion bodies in a structural genomics project. J Struct Funct Genomics 5: 195–204.
- Unnithan S, Green L, Morrissey L, Binkley J, Singer B, Karam J, Gold L. 1990. Binding of the bacteriophage T4 regA protein to mRNA targets: An initiator AUG is required. Nucleic Acids Res 18: 7083–7092.
- Varnado CL, Goodwin DC. 2004. System for the expression of recombinant hemoproteins in Escherichia coli. Protein Expr Purif 35: 76–83.
- Yuan L, Craig SP, McKerrow JH, Wang CC. 1990. The hypoxanthine-guanine phosphoribosyltransferase of Schistosoma mansoni. Further characterization and gene expression in Escherichia coli. J Biol Chem 265:13528–13532.
- Yue BG, Ajuh P, Akusjarvi G, Lamond AI, Kreivi JP. 2000. Functional coexpression of serine protein kinase SRPK1 and its substrate ASF/SF2 in Escherichia coli. Nucleic Acids Res 28: e14. doi: 10.1093/nar/28.5.e14.
- Zuker M. 2003. Mfold web server for nucleic acid folding and hybridization prediction. Nucleic Acids Res 31: 3406–3415.

## 方案 2 用杆状病毒表达系统表达克隆基因

本方案主要包括了几乎所有用于昆虫细胞转染、杆状病毒生产和蛋白质表达的方法。转染前，用标准的分子生物学方法构建一个将目的基因置于病毒启动子控制下的大肠杆菌载体。然后这种构建体通过同源重组转入杆状病毒载体的 DNA 中。虽然主要的下游步骤相同，但是实现转移载体和病毒 DNA 之间的重组有着各种有效的策略。正如本章导言所概述的，这些方法包括从共转染到大肠杆菌宿主内或体外的重组。

在大多数情况下，与转移载体的重组可以拯救一个存在于受体病毒 DNA 上的致命缺失。传统上，几轮的限制性酶切和纯化被用来产生一个在线性化病毒 DNA 上的缺失（Kitts and Possee 1993）。这个方法的一个缺点是，并不是每一个病毒 DNA 分子都被切断，从而可能出现一些非重组杆状病毒。因此，需要一个耗时的病毒噬菌斑分析来分离出重组杆状病毒。随着病毒杆粒 DNA 的出现，该方法得到了改善。它包括在共转染时用于重组的 flashBAC（Oxford Technologies 公司）或 BacMagic（Merck 公司）系统，或在转染前用于大肠杆菌宿主内重组的 Bac-to-Bac（Life Technologies 公司）系统。因为这些病毒杆粒 DNA 缺乏基本的病毒基因，可以在大肠杆菌宿主内繁殖，没有被非重组杆状病毒污染的风险（Zhao et al. 2003）。

因此，不需要用噬菌斑分析来从亲代病毒中分离出重组体。反而，它可以直接进行放大P1病毒种子或进行蛋白质表达（步骤9）。但为了实现目标蛋白表达的优化和可重复性，病毒滴度定量仍然是重要的。相应地附加了一个用于病毒噬菌斑分析的方案（见附加方案“噬菌斑测定法确定杆状病毒原液的滴度”）。

感谢加州理工学院蛋白表达实验室的 Jost Vielmetter 对方案 2 提供的帮助和他的同事 Nangiana Inderjit 对图 19-4 提供的帮助。

## 用于蛋白质表达的昆虫细胞系

正如导言所提到的，只有少数昆虫细胞系通常用于蛋白质表达，尽管存在260余种记录了的昆虫细胞系（Lynn 2007）。传统上，有两种S. frugiperda细胞株常用:衍生自蛹的卵巢的IPLB-Sf-21AE（Sf-21）或其克隆分离株SF-9（Vaughn et al. 1977）。S. frugiperda细胞系已被进一步转基因改造，用于生产具有哺乳动物细胞末端唾液酸化修饰的N糖蛋白（来自Life Technologies和SfSWT-3的SfSWT-1或Mimic）（Hollister et al. 2002；Aumiller et al. 2003）。有两种夜蛾细胞系已被广泛使用:衍生自成虫卵巢的TN-368（Hink 1970）和胚胎的BTI-TN-5B1-4（Tn-5，为Life Technologies销售前五的细胞系）（Granados et al. 1986）。Tn-5细胞株已经被报道可产生异常高水平的重组蛋白，特别是当蛋白质被分泌时（Wickham et al. 1992; Davis et al. 1993; Wickham and Nemerow 1993）。然而，T-ni细胞在缺乏肝素的培养基中悬浮培养时，易产生聚集（Wickham and Nemerow 1993; Dee et al. 1997）。此外，据报道T-ni细胞与S. fruginosa细胞相比，其突变率和转染效率是比较低的。因此，建议将Sf-9或者Sf-21细胞系作为一个起点，使其获得悬浮和单层培养能力，并且提高其重组杆状病毒和蛋白质的产率。

![](images/page_182_image_2.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

适合于选择的转移载体重组的杆状病毒或者杆粒 DNA

例如，BacMagic（Merck Biosciences）、flashBac（Oxford Expression Technologies），或者 ProGreen（AB载体）（用于生产重组杆粒 DNA，见替代方案“用于转染昆虫细胞的杆粒 DNA 的生产”）。

考马斯亮蓝染液（见方案8）

胎牛血清

目的基因、cDNA 片段

适合细胞使用的生长培养基

脂质体转染试剂（使用前存储在  $4^{\circ}$ C；详见步骤 4 的注意事项）

例如，Bacfectin（Clontech），Escort or Escort IV（Sigma-Aldrich），FuGENE（Promega），GeneJuice（Merck），Lipofectin 或者 Cellfectin II（Life Technologies），Tfx-20（Promega）等。

磷酸盐缓冲液（PBS）（1×）

1×PBS 是将 10×的 PBS 稀释于无菌水获得，最终 pH 应为 7.4，尽管 10×PBS 的 pH 可能较低。如果有必要，可以用 1mol/L 的 HCl 调节。

配置 1L 10×PBS 储存液:溶解 80g NaCl、2g KCl、14.4g  $Na_{2}HPO_{4}$  和 2.4g  $KH_{2}PO_{4}$  至 800mL 水中。如果需要，可使用 1mol/L HCl 调 pH 至 7.3。稀释至 1L 体积，过滤除菌或者高压灭菌。最终 10×PBS 储存液含 1.37mol/L NaCl、27mmol/L KCl、100mmol/L  $Na_{2}HPO_{4}$  和 18mmol/L  $KH_{2}PO_{4}$ 。

含 SDS 聚丙烯酰胺凝胶（见方案 8）

阳性对照转移载体

与荧光蛋白如 GFP 融合的融合蛋白表达后可以直接进行监测（图 19-4）。其他商品化的表达系统通常与阳性载体一起提供，这些载体携带相同的启动子，并且表达一种可以通过比色测定法检测到的蛋白质。例如，pBACgus-1（Merck Biosciences）质粒表达β-葡糖苷酸酶，当存在 X-葡糖苷酸时会产生蓝色。

![](images/page_182_image_21.jpg)

图 19-4 杆状病毒感染昆虫细胞的外观变化。使用的是 pVL1393-碱基转移载体和线性化 ProGreen 基因组的杆状病毒载体 DNA 感染 Tn-5 细胞。A. 未感染杆状病毒的细胞；B、C. 杆状病毒感染的细胞。受感染的细胞表达由 ProGreen DNA 编码的绿色荧光蛋白。图 C 与图 B 是相同细胞的相差荧光图像。需注意的是，感染细胞均略大于未感染的细胞。比例尺为  $100 \mu m$  （照片来自加州理工学院蛋白表达实验室的 Drs.Jost Vielmetter 和 Inderjit Nangiana）（彩图请扫封底二维码）。

SDS 凝胶加样缓冲液（6×）&lt;A&gt;（见方案 8）

不含二硫苏糖醇的  $6 \times$  SDS 加样缓冲液储存于室温。在使用缓冲液前，添加 1mol/L 二硫苏糖酵母液至终浓度为 100mmol/L。

## 昆虫细胞无血清培养基

已有一些商业化的无血清培养基可供使用，如Sf-900 III（Life Technologies）、HyQR SFX-Insect（Hyclone）和BD Baculogold Max-XP（BD Biosciences）。这些培养基可直接使用，并且已经包含表面活性剂，因此就不用再加普朗尼克f-68。

已适应合适培养基的 S. fugiperda Sf-9 或者 Sf-21 细胞

见信息栏中“用于蛋白质表达的昆虫细胞系”。

包含插入基因的转移载体

台盼蓝储备溶液（0.4%，m/V）

## 设备

带盖子的摇瓶(1000mL)，无菌(如 Kimble-Chase part no. 25630-1000 和 Corning closure 38mm 聚丙烯部分 no. 430621-0000)

Beckman JA10, Sorvall GS3 或 SLA3000 转子，或与 500mL 离心管配套的转子

Beckman JA20, Sorvall SS34 或 SA600 转子，或与 40～50mL 离心管配套的转子

设定在 $85^{\circ} \mathrm{C}$ 的热块或沸水浴

血细胞计数器

倒置相差显微镜

层流组织培养罩

液氮

无菌微量离心管

这些几乎都是聚丙烯，因此不能用于含脂质体转染混合物的保存。

$28^{\circ} \mathrm{C}$ 摇床

$28^{\circ} \mathrm{C}$ 恒温培养箱

组织培养皿（35mm 的 6 孔板，150mm 的 24 孔培养板），以聚苯乙烯为材料

因为在脂质体介导转染时 DNA 脂质复合物会吸附在玻璃或聚丙烯表面，所以应使用聚苯乙烯培养皿。

有帽的试管（2～7mL），聚苯乙烯材料，无菌（如 Greiner Bio-One 部分 no.189171）

无菌试管（15mL）

设为  $37^{\circ}$  的水浴锅

![](images/page_183_image_26.jpg)

## 方法

## 转染昆虫细胞产生重组杆状病毒

1. 将包含有目的 cDNA 或基因的 DNA 片段插入转移载体中，以使其融合到杆状病毒基因组（第 3 章）。确保克隆策略中载体的蛋白编码序列处在与载体的翻译信号相一致的读码框中。对于没有融合标签或者融合标签在氨基末端的，需要在蛋白质编码序列的 3 端置有同框的终止密码子。

PCR 得到的部分应测序，以确保在扩增反应过程中无伪突变的发生。

对于生产重组杆粒 DNA，请参阅替代方案:“用于转染昆虫细胞的杆粒 DNA 制备”（Bac-Bac 系统，Life Technologies）。

2. 在无血清培养基中扩增用于转染实验的 Sf-9 或 Sf-21 细胞。将低传代数的细胞（2～20）培养到指数生长期（ $1.5 \times 10^{6} \sim 2.5 \times 10^{6}$  个细胞/mL）。检查细胞的存活率为 95% 以上。

昆虫细胞培养的更多信息，请参阅信息栏“昆虫细胞培养物的维持与繁殖”，该信息栏在替代方案“用于转染昆虫细胞的杆粒DNA制备”中。

悬浮或单层培养适应的 SF-9 或 SF-21 细胞可用于生产重组杆粒。该过程不建议使用 TN-5 细胞。

血清可与 DNA-脂质体混合物形成复合物，这可能会降低转染效率。最好是在脂质体介导的转染前，昆虫细胞就应适应于无血清培养基。在这种情况下，之前在含有血清的培养基中生长的细胞，必须依次在 25%、50% 和 100%（V/V）的无血清和含血清的培养基混合物中传代培养 7 天。也可以用以下方法:①洗好的细胞在无血清培养基中用 DNA-脂质体转染，然后在第 5 步时放回含血清的培养基中产生重组杆状病毒；②通过磷酸钙介导转化（详见 Burand et al. 1980）。

3. 将昆虫细胞接种于培养皿中。准备并标记好适量的 35mm 的聚苯乙烯细胞培养皿:每个重组病毒以及阳性和阴性（没有 DNA）对照各一个。准备足够的细胞使表面密度达到 50%～70% 的表面被铺满。对于每个 35mm 培养皿，加 2mL 约含  $1 \times 10^{6}$  细胞的培养基。在水平位置将培养皿室温放置 60min，使细胞附着。

▲ 在转染时不使用抗生素，因其会导致细胞死亡。

4. 在细胞附着期间，准备 DNA 混合物和转染试剂。在微量离心管中将 100～250ng 的病毒 DNA 与 5～10 倍过量转移载体孵育 5min。对应于每个培养皿，在无菌聚苯乙烯管中把 200μL 的无血清培养基与 6μL 的转染试剂混合并旋涡混匀。在相应的离心管中加入实验和阳性对照 DNA 混合物，并轻轻颠倒混匀。准备一个额外的管，用没有 DNA 的转染试剂与培养基混合物作为阴性对照。室温下孵育最终混合物 15～30min 以形成脂质体 DNA 复合物。孵育结束后，再加入 800μL 无血清培养基使每个培养皿中的体积达到 1mL。

这个方案是对于基于合成脂类 N-[1（2，3-二油酰氧基）-丙基]-N，N，N-三甲基氯化铵（DOTAP）与二油酰磷脂乙醇胺混合试剂的初始方案，如 Lipofectin（Life Technologies），Bacfectin（Clontech），GeneJuice（Merck），Escort，或 Escort IV（Sigma-Aldrich）试剂。如果有必要，可以修改以适合所选择的特定转染试剂的厂商说明。

用于转染的 DNA 应该具有高纯度，可以用一些厂家提供的阴离子交换色谱试剂盒纯化的 DNA（如 PureLink HiPure Plasmid DNA Mini-prep Kit, Life Technologies; QIAEX resin, QIAGEN）。大的病毒和杆粒 DNA 对剪切敏感。应避免振荡混合，处理高分子质量 DNA 应该用阔口吸管。这些大分子 DNA 应该在转染的几个星期内被纯化，并且应避免反复冻融。

通过改变 DNA 或转染试剂的量可以优化转染条件。

对于 BaculoDirect 系统，可以直接使用 Gateway 重组反应。对 Bac-Bac 系统，使用 1～2μg 的纯化杆粒 DNA（重组杆粒 DNA 的构建，请参阅替代方案“用于转染昆虫细胞的杆粒 DNA 制备”）。

5. 弃吸附细胞表面的培养基。立即滴加含 DNA-脂质体的 1mL 培养基至每个皿的中心。在 28℃ 培养 5h 或过夜。

为了避免干扰细胞，将皿倾斜  $30^{\circ} \sim 60^{\circ}$  以使液体处于皿的一侧，再用无菌吸管除去。

不要让细胞层变干。

6. 弃实验组和阳性对照组中的培养基，替换为 2mL 适合生长的培养基，在  $28^{\circ}$ C 培养。

如果需要，这一步可以添加抗生素。然而，昆虫细胞培养不建议使用抗生素，因为它们可能会掩盖微生物污染。如果细胞以前一直是在有血清的完全培养基中培养的，那么这一步就使用这种培养基。在培养期间，附近放一些水或用塑料袋密封培养皿可以减少蒸发。

7. 培养基需在 2～3 天后检查与杆状病毒感染相关的变化，以评估转染和重组反应的效率（如下所述的步骤 12）。

8. 感染后 4～5 天，收集并转移培养基至 15mL 无菌试管内，培养基中有重组 1 代的病毒（P1）。4℃ 1000g 离心 10min 去除细胞碎片。将上清转移至新的 15mL 试管。得到 P1 病毒种子。

P1 病毒原料可以在  $4^{\circ}$ C 避光保存几个月。在储存的过程中于培养基中添加 5%～10% 的胎牛血清可以稳定杆状病毒。P1 种子应该存储用于之后的扩增。

商品化的系统，如 flashBAC、BacMagic、ProEasy 和 Bac-to-Bac 系统，可以产生大于 99% 的重组病毒，因此在扩增前不需要用噬菌斑纯化来分离单一重组病毒。对于其他系统可能含有非重组病毒，建议使用噬菌斑纯化（见附加方案中“噬菌斑测定法确定杆状病毒原液的滴度”）。

如果需要，可以在进行扩增前检查杆状病毒滴度（见附加方案中“噬菌斑测定法确定杆状病毒原液的滴度”）。然而，从步骤6和步骤7观察到的现象，包括细胞分裂的停止、细胞脱离和细胞核的增大，可以定性说明已经产生了感染杆状病毒。共表达 GFP 的载体（如使用 pVL-GFP、ProGreen 或 BaculoGold Bright）可以简单地在荧光显微镜下观察病毒的产生（图 19-4）。

## 扩增重组杆状病毒得到更高滴度的种子

9. 按步骤 2 扩增 SF-9 或 SF-21 细胞，以提供给每个杆状病毒实验样本、阳性对照组和阴性对照组  $2 \times 10^{7}$  个细胞。

如果同时扩增阳性对照组，小心避免病毒交叉污染。

通过比较细胞的生长速率和外观，阴性对照组可以帮助监测感染过程。

10. 标记适量 $150\mathrm{mm}$ 培养皿用于昆虫细胞培养。对于每个皿，于 $20\mathrm{mL}$ 培养基中接种 $1\times 10^{6}$ 个细胞/mL。在室温下使细胞吸附 $60\mathrm{min}$，期间确保培养皿处于水平。然后除去旧的培养基，加入 $20\mathrm{mL}$ 新鲜培养基。

11. 在平皿中加入  $500 \mu L$  P1 杆状病毒。轻摇平皿使病毒散开，然后放于  $28^{\circ}C$  培养箱。

为了减少突变累积，感染复数（MOI，病毒的颗粒数目除以细胞的数量）最好为0.1，在病毒扩增时一定小于1.0。没有噬菌斑分析时，通过大多数商品化的系统所得到P1病毒原料由经验估计为 $10^{6}\sim10^{7}pfu/mL$ （pfu是空斑形成单位，即感染病毒颗粒）。将这种估算用于给出的体积:

$$
\mathrm{MOI} = \frac {0 . 5 \times 1 0 ^ {7} \mathrm{pfu/mL} \times 0 . 5 \mathrm{mL}}{2 \times 1 0 ^ {7} \mathrm{个细胞}} = 0. 2 5
$$

12. 感染 2～3 天后，肉眼检查细胞被杆状病毒感染的迹象。预计可见变化包括细胞核体积的增大、细胞尺寸增大、由于小囊泡出芽形成的颗粒状的表面、细胞脱落，以及最终细胞裂解（图 19-4A）。与阴性对照组（没有 DNA）继续生长不同，感染样品将出现细胞分裂率降低现象。一些病毒 DNA 或转移载体可用于目标蛋白与 GFP 的共表达或融合表达（如使用 pVL-GFP、ProGreen 或 BaculoGold Bright）。用荧光显微镜观察 GFP，可以在该过程早期评估病毒制备是否成功（图 19-4B）。

如果第 5 天细胞计数增加到  $4 \times 10^{6}$  个细胞/mL 以上，或细胞形态无明显变化，那么就不会产生有活力的病毒。不必再进行后续步骤。杆状病毒扩增失败可能是由于细胞不健康或没有在对数生长期，或使用高的 MOI 导致培养基中所有细胞在最初就被感染。

13. 经过 4～5 天的感染，收集包含重组病毒的培养基，并转移到无菌的 50mL 离心管。在  $4^{\circ}$ C 以 1000g 离心 5min 除去细胞碎片。将上清转移至一个新的 50mL 离心管。这就是 P2 病毒种子。

14. 为了达到表达蛋白的最佳杆状病毒浓度（大于 $10^{8}\mathrm{pfu/mL}$），通常大规模重复步骤8～步骤13获得P3的种子（例如，通过增加1倍体积）。不建议更多的传代，因为这会积累突变病毒。

P2 病毒的滴度量通常为  $10^{7} \sim 10^{8}$ pfu/mL。

如果需要，P2 或 P3 的病毒的滴定量可由附加方案中“噬菌斑测定法确定杆状病毒原液的滴度”或用商业试剂盒测定。但是注意，测定滴度可能需要消耗与 P3 扩增或者小规模的蛋白质表达实验相同的时间。

## 在昆虫细胞中表达目标蛋白的小规模试验和优化

15. 扩增步骤 2 用于蛋白表达的细胞系[如 SF-9 SF-21, Tn-5(High-Five), 或 Mimic SF-9 细胞]以提供  $0.5 \times 10^{7}$  个对数增长期细胞。

据报道，Tn-5 细胞能表达高水平的目标蛋白，特别是分泌蛋白（Davis et al. 1993）（如需了解更多的使用 TN-5 细胞的详情，请参阅信息栏“用 TN-5（High-Five）提高表达”。Mimic SF-9 细胞已被构建成像哺乳动物细胞一样产生末端唾液酸化的 N-糖链（Jarvis et al. 1998）。

16. 病毒与细胞数量的比值（MOI）和收获时间在初始表达试验时已优化。如果该病毒的滴度是未知的，可以测试不同体积的病毒原液来确定。例如，根据方案，浓度为 $10^{8}pfu/mL$ 病毒原液20μL、10μL、5μL和2.5μL的MOI值分别为10pfu/细胞、5pfu/细胞、

2.5pfu/细胞和 1.25pfu/细胞。将 24 孔板的 6 列标记为不同病毒体积，一列为阳性对照（一种已知的在给定 MOI 值下高表达的病毒），一列为阴性即无病毒对照。4 列分别在不同的时间点收获，如感染后 1 天、2 天、3 天和 4 天（24～96h）。

可以添加小于培养孔总体积 20% 的病毒液。

如果MOI值已经确定，如根据附加方案“噬菌斑测定法确定杆状病毒原液的滴度”，那么MOI值可以为2pfu/细胞、4pfu/细胞、6pfu/细胞和8pfu/细胞进行试验。

高 MOI 值（5～10pfu/细胞）情况下通常最好是同步感染，但非常高的 MOI 值可能会抑制蛋白质的表达。如果 MOI 值 >5 时，需要检查培养基是否适合目标蛋白表达。在高 MOI 值情况下感染 5 天后，大部分细胞应该已经裂解。如果需要的话，目标蛋白可以用分离分泌蛋白的方法从培养基中分离出来（步骤 25）。

17. 将处于对数增长期的细胞稀释到 $10^{6}$ 个细胞/mL 浓度，在板上的每个孔中接种 $200\mu \mathrm{L}$ 细胞稀释液使每个孔接种细胞数量为 $2 \times 10^{5}$ 个。在室温下放置 $60\mathrm{min}$ 让细胞贴壁，并确保每个培养皿水平。

18. 在细胞贴壁时，准备病毒稀释液。在架子上排列 5 个微量离心管，然后将它们分别标记为 30、20、10、5 和阳性对照。第一个管中（标为 30），在 500μL 培养基中稀释病毒至 $8 \times 10^{7} \mathrm{pfu/mL}$ 。在剩下的 4 个管中分别加入 200μL 培养基。首先从第一个管取 200μL 的稀释病毒液转移到第二个，混匀。然后从第二个管取 200μL 转移到第三个，混匀，再重复操作稀释第三个管至第四管。在第六管中稀释阳性对照病毒液获得一个适当 MOI 值（如 $8 \times 10^{7} \mathrm{pfu/mL}$），并且稀释后管内的体积最好为 200μL 或者更多。注意，应小心避免阴性对照组受到病毒的污染，以及阳性对照组和样品交叉污染。

19. 细胞附着后，从第一个管中取  $50 \mu L$  稀释的重组病毒液转移到组织培养板（参见步骤 16 和步骤 17）的标为 “ $30 \mu L$ ” 列的 4 个孔中。重复每个剩余的实验组和阳性对照组。将未感染的第六列作为阴性对照。轻轻旋转培养皿混匀，并将其放置在  $28^{\circ}C$ 。

20. 感染后 $24\mathrm{h}$ 收集第一列、$48\mathrm{h}$ 收集第二列、$72\mathrm{h}$ 收集第三列，$96\mathrm{h}$ 收集最后一列细胞。用培养基冲散细胞。将细胞连同培养基转移到微量离心管中。以 $1000\mathrm{g}$ 离心 $10\mathrm{min}$，沉淀细胞，然后小心取出上清液。在每管细胞沉淀物中加入 $50\mu \mathrm{L}6\times \mathrm{SDS}$ 上样缓冲液重悬细胞，用 $85^{\circ}\mathrm{C}$ 加热块加热样品 $2\mathrm{min}$，然后充分振荡。在微量离心管中以最大转速于室温下离心 $1\mathrm{min}$，所有样品储存在 $-20^{\circ}\mathrm{C}$ 下，直到收集完所有样品，并准备加样到凝胶。

单层的昆虫细胞可以很容易地用吸管吹出的温和培养基流从表面脱附。

21. 在  $85^{\circ}$ C 短暂再加热后，每个悬浮液加样  $40\mu g$  到一个合适浓度的 SDS-聚丙烯酰胺凝胶。在大多数情况下，加载  $5 \sim 10\mu L$  样品比较合适。凝胶用考马斯亮蓝染色和/或用免疫印迹法使诱导蛋白显色（方案 8“蛋白质的 SDS-PAGE”和方案 9“蛋白质的免疫印迹分析”）。

按照经验，5000个昆虫细胞中大约含有 $10\mu \mathrm{g}$ 的总蛋白。

如果蛋白是分泌的，加载  $15 \mu L$  上清液，并通过免疫印迹法分析。

在表达重组基因的细胞提取物中，所预测分子质量的蛋白质在诱导后的一定时间点上应该是可见的。外源蛋白的诱导动力学和稳定性可能与阳性对照组有所不同。在阴性对照，即无病毒对照组中，应该没有可见的相应带。

## 昆虫细胞中目的蛋白的大量表达

22. 对于目标蛋白的大规模表达和纯化，需要扩增用来表达蛋白的细胞系（如SF-21、SF-9、TN-5或Mimic SF-9细胞）以获得处在对数生长期的 $400\mathrm{mL}$ 悬浮培养液（$1.5\times 10^{6} \sim 2.5\times 10^{6}$ 个细胞/mL）（昆虫细胞培养的进一步详情，请参阅替代方案“用于转染昆虫细胞的杆粒DNA制备”末尾的信息栏“昆虫细胞培养物的维持和繁殖”）。如需使用TN-5细胞的进一步详情，请参阅下面的信息栏。

## 用 TN-5（High-Five）提高表达

当 Tn-5（High-Five）昆虫细胞用作宿主时，一些条件的改变可以增强表达能力。

1. 在 TN-5 培养物的增殖和维持的时候，使用含 25mg/mL 硫酸葡聚糖（分子质量 9000～20 000 Da；Sigma-Aldrich 公司，目录号 D6924）适当的培养基（如 ESF921 表达系统）可以避免细胞聚集。
2. 在高细胞密度（如下文所述）的条件下感染应减少硫酸葡聚糖，否则硫酸葡聚糖会抑制感染。
a. 在 400g、4℃下离心分离细胞 10min，然后用适当量的病毒和无硫酸葡聚糖的表达培养基使细胞重悬至密度为  $1.6 \times 10^{7}$ （MOI 值为 1～4）。
b. 130r/min、27℃下摇动细胞1h，然后用不含硫酸葡聚糖的培养基稀释感染的细胞至密度为 $2\times10^{6}$ 。
c. 在步骤 24 的条件下继续表达。

23. 添加一定体积的病毒原液到步骤 22 扩增的细胞，使 MOI 值达到 4.0（或是按上述在昆虫细胞中表达目标蛋白的小规模试验和优化的体积加）。例如:

$$
\frac {4 0 0 \mathrm{mL} \times 2 \times 1 0 ^ {5} \mathrm{个细胞/mL} \times 4 \mathrm{pfu/细胞}}{4 \times 1 0 ^ {8} \mathrm{pfu/mL病毒滴度}} = 8 \mathrm{mL病毒液}
$$

24. 加入病毒原液 4h 后，换上新鲜的培养基。在  $400g\ 4^{\circ}C$  下离心细胞 10min。弃去上清液，然后用 400mL 新鲜培养基轻轻重悬细胞。
25. 在感染后 72h（或上一节中确定的最佳时间），通过 400g 离心 10min 收集细胞。弃上清液，用 5mL 1×PBS 温和重悬细胞沉淀物，将细胞转移到 50mL 的带螺旋帽的离心管。再次在 400g 下离心沉淀细胞 10min。①可以选择弃去 1×PBS 上清液，在液氮中冷冻保存细胞沉淀物，并储存在 -80℃；②立即进行纯化。

如果这种蛋白质是分泌的，那么第一次离心收集培养基上清。将其转移到另一离心管中，30 000g 下离心 1h 以除去杆状病毒颗粒和细胞碎片。或者，将其通过 0.22μm 的过滤器，以澄清上清液。-80℃下冷冻保存上清液，或者直接进行纯化。纯化前，最好是用适当的缓冲液透析，以除去已污染的培养基组分。同样，上清应浓缩 10 倍体积以降低到一个易操作的量。

26. 如果表达的蛋白质中含有多聚组氨酸标签，按照方案 5 纯化。

如果所表达的蛋白质是与谷胱甘肽-S-转移酶融合的，按照方案6纯化。

## 附加方案 噬菌斑测定法确定杆状病毒原液的滴度

噬菌斑或终点稀释分析法是从原液中分离纯化重组杆状病毒的传统方法，原液进一步衍生并进行定量感染。噬菌斑分析最初是用于动物细胞（Dulbecco 1952），后来被 Lee 和 Miller（1978）修改用于杆状病毒感染的昆虫细胞。在噬菌斑分析中，用病毒感染单层细胞，然后用琼脂糖覆盖以维持细胞的位置，并限制病毒的传播。在非常低的病毒稀释液中，分离感染细胞。感染细胞最终溶解和释放病毒，然后立刻感染邻近的其他细胞。感染细胞的裂解导致感染平板上相应的地方形成一块透明区域，这块区域就是一个杆状病毒的后代。这些噬菌斑既可用于制备一个克隆的原液，也可在不同稀释度下计算测定病毒滴度。

病毒噬菌斑分析通常对于新手来说是一个挑战，特别是通过由目的基因的可读框替代的多角体蛋白基因所形成的不同噬菌斑形态识别重组杆状病毒时。虽然这种差别仅在野生型杆状病毒 DNA（而不是与致死缺陷的 DNA）用于重组病毒时需要，但对于新手来说鉴别病毒噬菌斑通常是比较困难的。中性红染色通过选择性染色活细胞，而受感染的区域仍然清晰，因而可使噬菌斑更加明显。终点稀释法可以替代噬菌斑法（一个很好的方案，请参阅 Harwood 2007）。然而，这两种方法的共同缺点是都需要 6～7 天的时间来完成。更多节省时间的病毒定量方法，包括基于抗体的染色、流式细胞仪、实时定量 PCR（Kitts and Green 1999; Kwon et al. 2002; Shen et al. 2002; Hitchman et al. 2007）已经被开发并流向市场（如 the BacPAK titer kits from ClonTech）。虽然这些商业化的分析方法只要不到 2 天就可以完成，但是不能直接测试病毒感染性，而且不能用于分离病毒克隆。本方案描述了传统的噬菌斑分析方法，该方法是从 King 等（2007）的方法修改获得的。

![](images/page_188_image_3.jpg)

## 附加材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

低熔点的琼脂糖（如 Sigma-Aldrich Type VIII A4018）

5%（m/V）低熔点琼脂糖用去离子蒸馏水配置，高压灭菌后，用 50mL 管分装成每管 5mL，并在室温下储存固化，直到进行该方案的步骤 7。

昆虫细胞培养基

1×培养基按照以下方案使用。如果需要，在步骤6中可以用1.3×或者2×的储备液，通过调节体积（及根据需要添加无菌水），以获得最终浓度为1% m/V琼脂糖和1×培养基的覆盖用培养基。无血清或含有血清的培养基可用于相应适应过的细胞。

中性红溶液（5mg/mL 去离子蒸馏水溶液）

经  $0.22 \mu m$  的膜过滤除菌，并储存于室温。

无菌 PBS (1×)

Sf-9 或 SF-21 细胞（来自方案 2，步骤 2）

X-Gal 的原液[40mg/mL X-Gal（5-溴-4-氯-3-吲哚基-b-D-吡喃半乳糖苷）溶解在二甲基甲酰胺中]

避光储存在-20℃。

## 设备

干燥加热器（可选的；见步骤7）

倒置显微镜

六孔组织培养板

无菌离心管（50mL）

涡旋振荡器

水浴锅（40℃）

![](images/page_188_image_25.jpg)

## 方法

1. 按照方案 2 步骤 2 和 “昆虫细胞培养物的维持与繁殖” 信息栏中（在替代方案 “用于转染昆虫细胞的杆粒 DNA 制备”）中所描述的方法，扩增 SF-9 或 SF-21 细胞。扩增后需要对每个实验组、阳性对照组和阴性对照组（无病毒）提供指数生长期细胞约  $0.5 \times 10^{7}$  个。

SF-21 更适合用于噬菌斑分析，因为它可在较短的时间内产生不同的噬菌斑。使用血清添加培养基也能增强噬菌斑的可见性。病毒滴度应该尽可能使用用于蛋白表达的培养基和细胞株来测定。

2. 为每个实验组样品和阳性对照样品，分别标记两个六孔板。为了易于移液操作，列应该是相同的，因此，板1的顶部和底部的行被标记为 $0, 10^{-8}, 10^{-7}$，板2的顶部和底部的行被标记为 $10^{-6}, 10^{-7}, 10^{-8}$。每孔接种 $0.9 \times 10^{6}$ 个SF-9或 $1.4 \times 10^{6}$ 个SF-21细胞到 $2\mathrm{mL}$ 的培养基中。接种后立即摇动板均匀分散细胞。在室温下使细胞附着 $60\mathrm{min}$，并确定培养皿水平。
3. 在培养期间，准备 $10^{-1} \sim 10^{-8}$ 的10倍系列稀释病毒，包括一个额外的管为阴性对照（无病毒）。将 $900\mu \mathrm{L}$ 的培养基加到无菌标记的微量离心管中。将 $100\mu \mathrm{L}$ 的病毒加到标有“$10^{-1}$”的管中颠倒或轻轻涡旋混匀。用新的吸头将 $100\mu \mathrm{L}$ 的“$10^{-1}$”稀释液转至标有“$10^{-2}$”的管中混匀。继续操作直到完成“$10^{-8}$”稀释。
4. 接种 1h 后，使用倒置显微镜检查细胞附着在一个汇合的单层。
5. 在无菌组织培养工作台，排列病毒系列稀释液和组织培养皿。从每个孔中取出旧的培养基，并立即更换成 0.5mL 适当稀释的病毒（对 P2 或 P3 的原液，如在步骤 3 中标记为  $10^{-4} \sim 10^{-8}$ ）。包括无病毒对照的孔中标记为 “0”。培养细胞与病毒 60min。
6. 对应每组稀释，在 50mL 无菌管中加入 20mL 1× 昆虫细胞培养液，并在 40℃ 的水浴中加热。用微波短暂加热融化一个 5mL 的 5% 低熔点琼脂糖，然后将其放置在 40℃ 水浴。

如果在重组前杆状病毒DNA含有lacZ基因，则加 $240\mu \mathrm{L}$ （最终浓度为 $240\mu \mathrm{g / mL}$ ）的X-Gal到琼脂糖混合物中用于重组病毒的蓝/白斑筛选。

使用适用于 50mL 管的干热块有助于避免污染。否则，请确保水浴的水是干净的，用乙醇擦拭取出管的外壁。

7. 在昆虫细胞/病毒培养结束前约 15min，加入琼脂糖溶液到热培养基，并颠倒彻底混匀，同时避免产生气泡，不能使溶液冷却。混合物最终应为 1% 琼脂糖。
8. 昆虫细胞/病毒培养 1h 后，从单层细胞中小心地从倾斜的板子边上吸出培养基。轻轻吸 2mL 的琼脂糖培养基混合物加到板的一侧以覆盖单层细胞。在水平面上于室温下使覆盖的琼脂糖固化在板子上（30～60min）。
9. 再添加 1mL 昆虫细胞培养基作为覆盖层为培养物提供营养。在  $28^{\circ}$ C 培养直至细胞单层铺满（4～7 天）。
10. 噬菌斑在黑色的表面上在亮光照射下，或者是背对亮光倾斜可见为透明的。用中性红染色会更加明显。这时噬菌斑为红色背景下的透明区。

如果亲本病毒含有 lacZ 基因，而目的基因替代了该基因，那么重组病毒的噬菌斑不应是有色的，但非重组病毒依稀会出现蓝色。

11. 进行中性红染色，需先去除覆盖层液体，更换为 1mL 中性红稀释液，28℃培养几个小时或过夜。中性红稀释液是将 50mL 的中性红（5mg/mL 水溶液）加到 950mL 无菌 1×PBS 中获得的。
12. 第二天清晨，用吸头吸去染液并倒置平板于吸水纸或滤纸上。更换盖子，让平板在暗处倒置几个小时以使噬菌斑清晰可见。
13. 选择产生 $10 \sim 30$ 噬菌斑的稀释度，并对各复孔的噬菌斑计数。测定该稀释度的平均噬菌斑数目，并计算病毒滴度，如下所示:

$$
\text {病毒滴度} (\mathrm{pfu/mL}) = \frac {\text {噬菌斑平均数}}{(\text {Dilution}) \times 0 . 5 \mathrm{mL}},
$$

式中，5mL 是加入板中的稀释病毒的体积，以每毫升计。例如，病毒滴度为  $10^{7}pfu/mL$  时，预计  $10^{-6}$  稀释度的板会产生 20 个噬菌斑。

14. 挑噬菌斑用于制备一个克隆的原液，将一个无菌的巴斯德吸管的尖端插在噬菌斑的中心，然后轻轻地吸出一块琼脂糖。将其放入 1mL 的培养基中，振荡释放病毒颗粒。应选择一些噬菌斑。这些分离株在扩增前可再次用噬菌斑分析复筛。

# 替代方案 用于转染昆虫细胞的杆粒 DNA 制备

本方案是在转染昆虫细胞前使用分子生物学技术在大肠杆菌中产生重组杆状病毒DNA（Luckow et al. 1993）。所有的试剂为商业销售的，BAC-BAC系统来自Life Technologies。

![](images/page_190_image_5.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

感受态的大肠杆菌 DH10Bac 细胞

DH10Bac 细胞中的杆粒 bMON14272（136kb）包含杆状病毒 DNA，并且含有卡那霉素抗性基因。该质粒中还含有一个 lacZ β-半乳糖苷酶基因，该基因表达的产物在 IPTG/X-Gal 存在时显示蓝色。如果该基因与转移质粒重组而被替代则不显示蓝色。

辅助质粒 pMON7124（13.2kb）编码 Tn7 转座酶，并含有四环素抗性基因（Barry 1988）。

肉汤（LB）琼脂平板（含  $50 \mu g/mL$  卡那霉素、 $7 \mu g/mL$  庆大霉素、 $10 \mu g/mL$  四环素、 $100 \mu g/mL$  X-Gal、 $40 \mu g/mL$  的 IPTG）&lt;A&gt;

肉汤（LB）液体培养基（有或没有  $50 \mu g/mL$  卡那霉素、 $7 \mu g/mL$  的庆大霉素和  $10 \mu g/mL$  四环素类抗生素的混合物）&lt;A&gt;

载体 pFastBac，含有目标蛋白的基因（在 TE 缓冲液中  $0.2ng/\mu L$ ）

载体 pFastBac 含有抗庆大霉素和氨苄青霉素基因。

![](images/page_190_image_17.jpg)

## 方法

1. 用第3章中介绍的方法构建和转移含有目标基因的pFastBac质粒到DH10Bac感受态细胞（Life Technologies）。在含有试剂清单中用于筛选的附加试剂的LB琼脂平板上梯度稀释转化体系（$10^{-1} \sim 10^{-3}$）。在 $37^{\circ}\mathrm{C}$ 下培养2天以使非重组子显现出蓝色。

由于在DH10Bac细胞中杆状病毒DNA插入pFastBac，使得β-半乳糖苷酶的编码序列被干扰，重组子在含有X-Gal/IPTG的培养基上不再产生蓝色。

用限制性内切核酸酶、TOPO或Gateway克隆策略得到pFastBac载体。

2. 用菌落 PCR 分析 $3 \sim 5$ 个孤立的、大的白色菌落（第7章），以验证目标基因的存在。

3. 按照第 1 章，方案 1 和方案 2 中所描述的碱性裂解法分离杆粒 DNA。用于重组杆粒细菌生长的 LB 培养基一定要保持有 50mg/mL 卡那霉素和 7mg/mL 庆大霉素。

此外四环素不是严格必需的，因为在这个阶段不再需要转座酶的功能。

含有杆粒 DNA 的溶液应轻弹混匀；反复吹打或涡旋会使较大的 DNA 被切断。

## 昆虫细胞培养物的维持和繁殖

这里概述了昆虫细胞培养技术的实践经验。深入的技术可以从一些优秀的书籍和综述中找到，如 Lynn（2002）和 O'Reilly 等（1994）。昆虫细胞的生长和其他细胞一样都是依次经过滞后期、指数增长期和稳定期阶段。按照经验，昆虫细胞在指数增长期间的倍增时间一般为 1 天，不过确切的时间还是取决于细胞株、培养基和生长条件。昆虫细胞在 27～28℃下培养，在用杀菌剂如 70%乙醇擦拭过的层流通风橱内转移。不需要特殊供应二氧化碳，因为昆虫细胞培养基不依赖于碳酸盐缓冲。

## 培养基

昆虫细胞通常培养在一些基本培养基中，如 Grace 的培养基（Grace 1962）、TNM-FH（HINK 1970），或补充有 5%\~10% 胎牛血清（FBS）的 TC-100（Gardiner and Stockdale 1975）。20 世纪 80 年代开发的无血清培养基现已广泛使用，它有以下优点:脂质体介导的转染相容性较好，减少批次间的差异，用于蛋白质纯化的难度降低，以及在某些情况下成本较低（Agathos 2007）。用于昆虫细胞培养的可靠无血清培养基的来源有:SF-900 III（Life Technologies），HYQ SFX 昆虫（Hyclone），BD BaculoGoldMax-XP（BD Biosciences）等。昆虫细胞应逐渐适应生长培养基的任何变化，如从含 FBS 的培养基转移到无血清培养基中。

## 增殖

虽然昆虫细胞既可以悬浮培养也可以单层细胞培养增殖，但是 SF-10 或 SF-21 细胞种子可方便地在悬浮液中持续维持。即使当昆虫细胞在悬浮培养基中增殖，它仍然有能力很容易地附着到表面，因而可以用于病毒传代的单层细胞培养和生成蛋白的悬浮培养。适应了在无血清培养基中生长的昆虫细胞可以直接从供应商处购买。相反，贴壁培养扩增的昆虫细胞必须逐步适应悬浮培养。每次传代培养，以每传代一次增加 5r/min 来增加摇动或搅拌速率，从 90r/min 到 130r/min 的摇动培养或从 40r/min 到 90r/min 的搅拌培养。

## 设备

用于昆虫细胞悬浮培养的摇床或培养箱和培养瓶与常用于细菌细胞生长的一样，但用于昆虫细胞培养时一定要专用以避免污染。另外，转瓶可购买获得，放置在一个立式培养箱中，靠磁力搅拌驱动。玻璃器皿必须彻底清洗，以去除所有的洗涤剂，因为洗涤剂有可能抑制昆虫细胞生长。为了适当的通气，用于摇床培养的体积不应超过摇瓶体积的1/3（带挡板的摇瓶，为1/2），用于旋转培养的体积不能超过培养瓶体积的2/3。在所有情况下，瓶盖应该是松的。悬浮培养的一个优点是，可以很容易地取样监测细胞密度和活力，最经常使用的是血细胞计数器。对于大多数类型的血细胞计数器，一个单元小正方形区域中的一个细胞对应 $10^{4}$ 个细胞/mL。为了确定细胞活力，1mL的细胞中加入0.1mL 0.4%的台盼蓝使死细胞染成蓝色，用显微镜检查。虽然比较昂贵，但是一般人可能更愿意购买库尔特颗粒计数器或Vi-CELL，以确定细胞密度。

## 培养

昆虫细胞培养应保持在指数增长期（$2 \times 10^{6}$个细胞/mL），大于 $90\%$ 的存活率的条件