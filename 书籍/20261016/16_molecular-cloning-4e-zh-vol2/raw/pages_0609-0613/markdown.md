![](images/page_608_image_2.jpg)

<details>
<summary>text_image</summary>

启动子
SD SA
外源基因
Poly(A)
</details>

在表达盒中通常存在内含子以加强转基因表达，包括人工及天然内含子（如 RBG 内含子）。

![](images/page_608_image_4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["启动子"] --> B["外源基因"]
  B --> C["PRE"]
  C --> D["Poly(A)"]
```
</details>

插入转录后调控元件已被证明能提高转基因表达效率。最常用的元件来源于 WPRE（Donello et al. 1998）。

![](images/page_608_image_6.jpg)

<details>
<summary>text_image</summary>

启动子
外源基因
4×miRNA 靶点
Poly(A)
</details>

将 miRNA 的靶序列插入到病毒载体的 3'UTR 区将导致外源基因在特定 miRNA 高表达的细胞中转录中止。这种方法成功用于阻止体内抗原提呈细胞中外源基因的表达，进而减轻了外源基因诱发的获得性免疫反应。

![](images/page_608_image_8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["启动子"] --> B["终止"]
  B --> C["外源基因"]
  C --> D["Poly(A)"]
```
</details>

插入 loxP-stop-loxP 盒使在特定细胞类型表达 Cre 重组酶的转基因小鼠中进行细胞类型特异性表达。

![](images/page_608_image_10.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Poly(A)"] --> B["外源基因"]
  B --> C["双向启动子"]
  C --> D["外源基因"]
  D --> E["Poly(A)"]
```
</details>

上图所示载体中在同一启动子下表达两个外源基因。启动子两侧外源基因的表达效率不一定完全相同。这可能不是使两个基因表达效率相同的最好设计（见其他设计），但就研究 miRNA 对基因表达的调控来说却是一个很好的设计(Brown and Naldini 2009)。在一个转基因的 3'UTR 区引入 miRNA 靶序列，在第二个外源基因，可能是标记基因（如 GFP）基础转录时，实现 miRNA 调控研究。

![](images/page_608_image_12.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["启动子"] --> B["外源基因"]
  B --> C["IRES"]
  C --> D["外源基因"]
  D --> E["Poly(A)"]
```
</details>

在这个载体中，一个转录物中的外源基因表达为天然状态的独立蛋白质。通常情况下，内部核糖体进入位点（IRES）下游的基因表达效率低于上游基因，但这种情况还是取决于 IRES 元件。最常用的 IRES 元件来源于脑心肌炎病毒。最近出现的 IRES 元件比以前更加高效（Chappell et al. 2000; Wang et al. 2005）。这类表达盒通常设计为是将目的基因与毒性药物抗性标记基因（如嘌呤霉素、潮霉素、新霉素）或使转导细胞易于鉴定的荧光蛋白共表达。目前，已经开发出多种能够进行荧光和生物发光成像的蛋白质（Wurdinger et al. 2008; Tannous 2009）。

![](images/page_608_image_14.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["启动子"] --> B["外源基因"]
  B --> C["2A"]
  C --> D["外源基因"]
  D --> E["Poly(A)"]
```
</details>

在以上图示中，一个编码多个蛋白的外源基因被2A序列/sec隔开。多聚蛋白质在翻译过程中可自我加工成几个独立的蛋白质，即多个蛋白质的表达可以源于一个多聚蛋白[例如，产生iPS细胞的4个必需转录因子（Sommer et al. 2009），抗体轻重链可同时表达（Fang et al. 2005）]。

![](images/page_609_image_3.jpg)

该系统利用双重转录因子复合物调控基因表达。一种质粒/载体携带的外源基因在12个ZFHD-1结合位点构成诱导性启动子下，再上游是最小IL-2启动子，另一种质粒/载体是双顺反子，其编码两个融合蛋白，分别作为转录激活因子和DNA结合蛋白。雷帕霉素存在时，人FKBP12和FKBP-雷帕霉素-相关蛋白（FRAP）结构域二聚体化，形成转录复合物。转录激活因子（Tf1）由人FRAP蛋白的FRB结构域与人NF-κB p65亚基来源的激活结构域融合构成。DNA结合蛋白（Tf2）由ZFHD1的DNA结合结构域与3个拷贝的人FKBP12融合构成（Ye et al. 1999; Rivera et al. 1999）。

![](images/page_609_image_5.jpg)

四环素调控的基因表达系统是最早开发用于哺乳动物细胞/组织的表达系统之一，继续被广泛应用于生物学中药物调控的基因表达。该系统应用细菌来源的四环素响应转录因子，由细菌的四环素结合结构域（TetR）与HSV-1 VP16的转录激活结构域融合而成。开发了tTA和rtTA这2个转录因子，在四环素或其衍生抗生素如多西环素(doxycycline)存在时，Tet-On系统（Gossen et al. 1995）可以结合Tet同源操纵子（tetO）；而其不存在时，则Tet-Off系统（Gossen and Bujard 1992）可以结合Tet同源操纵子（tetO）。优化的Tet-响应转录因子rtTA2 $^{S}$ -M2，表现出极低的tetO残余结合，且低浓度多西环素就可以最大限度地诱导基因表达（Urlinger et al. 2000）。

![](images/page_610_image_3.jpg)

该 Tet 调控系统是 Tet 响应转录沉默因子（tTS $^{Kid}$ ）和 rtTA 转录激活因子的组合，能够严谨控制几个数量级水平的基因表达（Freundlieb et al. 1999）。在关闭状态时，tTS $^{Kid}$ 使转录活性处于抑制状态。对于存在其他增强子元件可能反式激活 Tet-响应启动子从而导致外源基因的高水平基础表达的病毒载体而言，该设计非常重要。目前，该设计已成功应用于多种病毒载体系统（Pluta et al. 2005; Candolfi et al. 2007）。

![](images/page_610_image_5.jpg)

用于 RNA 干扰（RNAi）病毒载体的常见设计基于 RNA 聚合酶 III（Pol III）的启动子，如 U6 和 H1（Sibley et al. 2010）。shRNA 的下游是由 5 个 T 串联组成的终止序列。经剪切酶（Dicer）加工，shRNA 失去了 6bp 环，留下含 2bp 突出端的 21bp 双链分子。TetO 序列和 H1 或 U6 的组合可实现药物调控的 shRNA 表达（Pluta et al. 2007）。

![](images/page_610_image_7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["启动子"] --> B["外源基因"]
  B --> C["Poly(A)"]
  C -.-> B
```
</details>

嵌入shRNA的miR

位于已插入外源基因表达盒3'UTR区的miRNA中的shRNA的表达（Stegmeier et al. 2005）似乎表现出较低的体内毒性（McBride et al. 2008; Boudreau et al. 2009）。此外，该设计与大多数外源基因表达盒使用的RNA聚合酶II的启动子相容，可以实现许多目标，如组织特异性表达、发育控制或药物控制的表达。

## 参考文献

- Boudreau RL, Martins I, Davidson BL. 2009. Artificial microRNAs as siRNA shuttles: Improved safety as compared to shRNAs in vitro and in vivo. Mol Ther 17: 169–175.
- Brown BD, Naldini L. 2009. Exploiting and antagonizing microRNA regulation for therapeutic and experimental applications. Nat Rev Genet 10: 578–585.
- Candolfi M, Pluhar GE, Kroeger K, Puntel M, Curtin J, Barcia C, Muhammad AK, Xiong W, Liu C, Mondkar S, et al. 2007. Optimization of adenoviral vector-mediated transgene expression in the canine brain in vivo, and in canine glioma cells in vitro. Neuro Oncol 9: 245–258.
- Chappell SA, Edelman GM, Mauro VP. 2000. A 9-nt segment of a cellular mRNA can function as an internal ribosome entry site (IRES) and when present in linked multiple copies greatly enhances IRES activity. Proc Natl Acad Sci 97: 1536–1541.
- Donello JE, Loeb JE, Hope TJ. 1998. Woodchuck hepatitis virus contains a tripartite posttranscriptional regulatory element. J Virol 72: 5085–5092.
- Fang J, Qian JJ, Yi S, Harding TC, Tu GH, VanRoey M, Jooss K. 2005. Stable antibody expression at therapeutic levels using the 2A peptide. Nat Biotechnol 23: 584–590.
- Freundlieb S, Schirra-Muller C, Bujard H. 1999. A tetracycline controlled activation/repression system with increased potential for gene transfer into mammalian cells. J Gene Med 1: 4–12.
- Gossen M, Bujard H. 1992. Tight control of gene expression in mammalian cells by tetracycline-responsive promoters. Proc Natl Acad Sci 89:5547–5551.
- Gossen M, Freundlieb S, Bender G, Muller G, Hillen W, Bujard H. 1995. Transcriptional activation by tetracyclines in mammalian cells. Science 268: 1766–1769.
- McBride JL, Boudreau RL, Harper SQ, Staber PD, Monteys AM, Martins I, Gilmore BL, Burstein H, Peluso RW, Polisky B, et al. 2008. Artificial miRNAs mitigate shRNA-mediated toxicity in the brain: Implications for the therapeutic development of RNAi. Proc Natl Acad Sci 105:5868–5873.
- Pluta K, Luce MJ, Bao L, Agha-Mohammadi S, Reiser J. 2005. Tight control of transgene expression by lentivirus vectors containing second-generation tetracycline-responsive promoters. J Gene Med 7: 803–817.
- Pluta K, Diehl W, Zhang XY, Kutner R, Bialkowska A, Reiser J. 2007. Lentiviral vectors encoding tetracycline-dependent repressors and transactivators for reversible knockdown of gene expression: A comparative study. BMC Biotechnol 7: 41.
- Rivera VM, Ye X, Courage NL, Sachar J, Cerasoli F Jr, Wilson JM, Gilman M. 1999. Long-term regulated expression of growth hormone in mice after intramuscular gene transfer. Proc Natl Acad Sci 96: 8657–8662.
- Sibley CR, Seow Y, Wood MJ. 2010. Novel RNA-based strategies for therapeutic gene silencing. Mol Ther 18: 466–476.
- Sommer CA, Stadtfeld M, Murphy GJ, Hochedlinger K, Kotton DN, Mostoslavsky G. 2009. Induced pluripotent stem cell generation using a single lentiviral stem cell cassette. Stem Cells 27: 543–549.
- Stegmeier F, Hu G, Rickles RJ, Hannon GJ, Elledge SJ. 2005. A lentiviral microRNA-based system for single-copy polymerase II-regulated RNA interference in mammalian cells. Proc Natl Acad Sci 102: 13212–13217.
- Tannous BA. 2009. Gaussia luciferase reporter assay for monitoring biological processes in culture and in vivo. Nat Protoc 4: 582–591.
- Urlinger S, Baron U, Thellmann M, Hasan MT, Bujard H, Hillen W. 2000. Exploring the sequence space for tetracycline-dependent transcriptional activators: Novel mutations yield expanded range and sensitivity. Proc Natl Acad Sci 97: 7963–7968.
- Wang Y, Iyer M, Annala AJ, Chappell S, Mauro V, Gambhir SS. 2005. Noninvasive monitoring of target gene expression by imaging reporter gene expression in living animals using improved bicistronic vectors. J Nucl Med 46: 667–674.
- Wurdinger T, Badr C, Pike L, de Kleine R, Weissleder R, Breakefield XO, Tannous BA. 2008. A secreted luciferase for ex vivo monitoring of in vivo processes. Nat Meth 5: 171–173.
- Ye X, Rivera VM, Zoltick P, Cerasoli F Jr, Schnell MA, Gao G, Hughes JV, Gilman M, Wilson JM. 1999. Regulated delivery of therapeutic proteins after in vivo somatic cell gene transfer. Science 283: 88–91.

(王俊 于学玲 译, 叶玲玲 孙强 校)

![](images/page_612_image_1.jpg)

<details>
<summary>text_image</summary>

FOURTH ED
MOLECUL
CL
A LABORATORY
GREEN AND SAMROCK
3
FOURTH EDIT
MOLECUL
CLO
A LABORATORY A
GREEN AND SAMROCK
2
FOURTH EDITION
MOLECULAR
CLONING
A LABORATORY MANUAL
GREEN AND SAMBROCK
1
</details>

时隔十年，美国冷泉港实验室出版社推出了全新的《分子克隆实验指南》第四版，新版修订了第三版中的核心章节，以突出现有的核酸制备和克隆、基因转移及表达分析的策略和方法等内容。同时还增加了12个新章节，专门介绍最激动人心的研究策略，包括利用DNA甲基化技术和染色质免疫沉淀的表观遗传学分析、RNAi、新一代测序技术，以及如何处理数据生成和分析的生物信息学等。全书22章，包含247个实验操作主题。本书还保留了必不可少的附录:试剂和缓冲液、常用技术、检测系统、一般安全原则和危险材料。

基于30余年的可靠性和权威性，第四版《分子克隆实验指南》将成为新的“金标准”，并再次成为一部无法绕过的分子生物学实验手册和参考指南！

任何使用分子生物学技术的基础研究实验室都将因拥有一册《分子克隆实验指南》而受益。

—— 美国 The Scientist 杂志