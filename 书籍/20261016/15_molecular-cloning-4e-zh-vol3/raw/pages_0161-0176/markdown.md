## 融合蛋白的切割

为了获得天然的、具有生物活性形式的目的多肽，较好的方法就是从融合蛋白中切除标签。信号肽通常是跟随着蛋白质的易位而被内源的信号肽酶切除，而与信号肽切割不同，多种切割载体蛋白和目的蛋白之间的肽键的化学和酶学方法已被研发。实际操作中，化学切割方法很少使用，因为大多数目的蛋白都含有一个或者多个潜在的切割位点，而且有可能在苛刻的化学反应中发生变性。取而代之的是，利用特异位点蛋白酶来去除标签或者融合载体蛋白。相应地，大多数商业化载体的多克隆位点都位于编码载体蛋白和蛋白酶水解位点的下游序列中（表19-2）。表19-4中总结了常用于切割融合蛋白的具有特异位点的蛋白酶。

表 19-4 用于切割重组融合蛋白的常用内肽酶

| 蛋白酶 | 识别位点$^a$ | 融合标签 | 参考文献 | 备注 |
| --- | --- | --- | --- | --- |
| 肠激酶 | DDDDK↓ | — | Light et al. 1980; Dykes et al. 1988 | 肠激酶、因子Xa和α-凝血酶可被丝氨酸蛋白酶抑制物抑制,如phenylmethanesulfonyl fluoride (PMSF) |
| 因子$Xa^b$ | I-(E/D)-GR↓ | — | Nagai and Thogersen 1984; Jenny et al. 2003 |  |
| α-凝血酶$^c$ | LVPR↓GS | — | Gearing et al. 1989; Jenny et al. 2003 |  |
| HRV-3$C^d$ | LE-(V/A/T)-LFQ↓GP | GST或His标签 | Cordingley et al. 1990; Walker et al. 1994 | 丝氨酸蛋白酶,受PMSF和$Zn^{2+}$轻度抑制 |
| Genenase I | HY↓或H↓Y | — | Carter and Wells 1987; Carter et al. 1989 | NEB公司工程化的枯草杆菌蛋白酶变异体,可被丝氨酸蛋白酶如PMSF抑制 |
| 烟草蚀纹病毒(TEV)蛋白酶 | ENLYFQ↓(G/S) | His标签 | Parks et al. 1994; Tropea et al. 2009 | 半胱氨酸蛋白酶,对氧化环境敏感,可被$Zn^{2+}$(>5mmol/L)抑制。利用点突变减少野生型TEV蛋白酶的自溶形象(Kapust et al. 2001) |

a. 位点超过一种类型氨基酸时，在括号中表示，氨基酸可互换时，用斜杠表示。

b. 肠激酶和因子 Xa 不能在脯氨酸前切割；因子 Xa 不能在精氨酸前切割。

c. $\alpha$-凝血酶中存在两个较优的切割位点: ①p4-p3-P-(R/K)-p1'-p2', 其中 p3 和 p4 是疏水性氨基酸; ②p2-(R/K)-p1', 其中 p2 或 p1'是 Gly (Chang 1985)。

d. PreScission 蛋白酶是 GST 标记的 HRV-3C 蛋白酶的专有名称，由 GE Healthcare 公司推向市场。

e. Genenase I 可紧接着 His 进行切割，切割速度取决于蛋白质结构和序列组成（Carter et al. 1989）。当紧接着切割位点（p1'位置）的氨基酸是 Asp 或 Glu 时，切割速度最慢；还没有发现在 Pro 或 Ile 前可以实现酶切。

数个外源氨基酸通常会残留在目的蛋白的氨基端。一些蛋白酶，如肠激酶或者 Xa 因子，不需要切割位点羧基端以外的固定氨基酸。HRV-3C、TEV 和大多数其他的特异蛋白酶都会在切割位点的羧基端留下 1～2 个氨基酸，但经常因其在重组蛋白、标记蛋白中的高度序列特异性和有效性而成为优先使用的蛋白酶类。此外，使用克隆至载体中的限制性酶切位点和重组位点常常也会在目的蛋白中引入额外的氨基酸。在特定情形下，可仔细选择符合蛋白酶识别的限制性酶切位点。例如，BamH I 位点编码 Gly-Ser，因此可以将其放在凝血酶和 TEV 切割位点的羧基端。事实上，几个氨基酸的存在（通常在目的蛋白切割的氨基端）并不会显著地干扰蛋白质的功能。尽管如此，能够确保重组蛋白与含单一天然序列的蛋白质具有相似的形式还是很重要的。

除了会在目的蛋白末端引入额外的氨基酸这个潜在的问题之外，还有3个有关于融合标签去除的问题。第一，个别蛋白酶的活性因融合蛋白不同而有所不同。对于许多融合蛋白，如果蛋白酶识别位点位于蛋白折叠结构内部，那么蛋白水解反应效率就会很低。在这些情况中，当融合蛋白发生部分变性，或者通过人为延伸目的蛋白的氨基端而引入了一定“空间”后，就可以利用蛋白酶来切割。第二，因为蛋白酶的特异性不是绝对的，或者因为用于切割的酶受到其他蛋白酶的污染，所以有可能目的蛋白会在内部位点被切开（Nagai and Thogersen 1984, 1987; Dykes et al. 1988; Lauritzen et al. 1991）。这种类型的问题有时可以通过调整消化酶切条件的方式解决（时间、温度，或者蛋白酶与蛋白质的比例）。否则，调整成合适的表达结构，选择不同的蛋白酶就显得很有必要。第三，切开的蛋白质必须从含有载体蛋白和蛋白酶的体系中分离出来。因此为蛋白酶融合一个与载体蛋白匹配的标签就显得极为方便。按照这种方式，蛋白酶和载体蛋白可以通过亲和树脂单独去除。带有6xHis和/或GST标签的HRV 3C或TEV蛋白酶可以在大肠杆菌中表达，或者从其他途径购买。虽然标记的多链形式和二硫键连接的蛋白酶表达困难，如因子Xa、凝血酶或肠激酶，但是运用传统的色谱方法或者免疫学方法还是可以从目的蛋白中去除这些蛋白酶。

![](images/page_161_image_4.jpg)

## 外源蛋白的优化表达

## 翻译效率的优化:翻译的起始

起始密码子上游的核糖体结合位点是翻译高效起始的必要条件（Huttenhofer and Noller 1994）。例如，大肠杆菌的翻译起始阶段，5～9个核苷酸的SD序列与16S RNA的3端相互作用（Shine and Dalgarno 1974; Steitz and Jakes 1975; Steitz 1979）。SD序列与起始密码子ATG之间的距离影响翻译效率。在表达载体中，以起始密码子开始的可读框，其与SD序列之间的距离已经进行了优化。但是，如果克隆基因要从可读框自身的起始密码子起始翻译，那么起始密码子与其上游的SD序列之间的距离应该是5～7个核苷酸（Ringquist et al. 1992）。

翻译起始区的二级结构也影响基因表达的效率（de Smit and van Duin 1994a,b）。某些情况下，通过改变 SD 序列上下游序列来降低二级结构也可增加基因的表达效率(Chen et al. 1994)。类似地，翻译偶联法即将目的基因编码序列置于一个已翻译的序列下游，也使得几个基因的表达水平最高（例如，见 Makoff and Smallwood 1990; Rangwala et al. 1992）。大多数商业化的表达载体的翻译起始点前均有合适的序列。然而，如果目的基因的 5' 区有复杂的二级结构，可以通过基因突变或者与能够高效表达的载体蛋白融合来减少这些二级结构，从而增加表达效率。

## 密码子的使用

遗传密码是冗余的，61种密码子编码特定的20种氨基酸。只有两种氨基酸（Met和Trp）是由唯一的密码子编码，而剩余的18种氨基酸均由数种密码子编码。同义密码子编码某一特定的氨基酸，并且同义密码子的使用频率不同（Grantham et al. 1980a,b, 1981）。

如果目的基因的编码区含有高频率的稀有密码子或者一段序列含有稀有密码子，可以通过基因再合成或基因突变将稀有密码子移除，以提高表达效率（Rangwala et al. 1992）。在大肠杆菌中有些特殊情况，如当目的基因序列中有稀有密码子 AGA 和 AGG 时可以意外形成 SD 序列（Ivanov et al. 1992）。

外源蛋白质的氨基端 DNA 编码序列很大程度上影响其表达水平（Barnes et al. 1991; Bradshaw et al. 1998）。基于这个原因，某些情况下有必要通过 PCR（第 7 章）或位点突变（第 14 章）将编码区的前 7 个或前 8 个密码子的 DNA 序列置换成特定表达系统中常用的密码子（Bennetzen and Hall 1982）。在条件允许的前提下，将目的基因的 5 端的 GC 含量降至 45% 以下。

## 生长条件的优化

无论何种表达系统，所用培养基的不同均可导致表达水平的巨大差异（Weickert et al. 1996）。例如，在培养大肠杆菌时可用标准培养基来确定一般的培养参数，但是，通常只有通过对生长条件作出调整才能达到最佳表达水平，这可能会用到诸如 M9 这样的基本无机盐培养基，或者是删除营养丰富的肉汤培养基、酵母胰蛋白胨（YT）或 NZCYM 培养基（附录 1）。同样，用毕赤巴斯德酵母表达异源蛋白时，像基本盐甘油培养基（MGY）和基本盐培养基（MM）这样的基本培养基对蛋白质表达是有用的，然而，培养基 pH、温度以及培养时间的微调会提高外源蛋白质的产量和质量。用杆状病毒感染的昆虫细胞表达蛋白，病毒感染细胞的时间和其他因素是十分重要的优化参数。更多的详细信息请参阅蛋白质表达方案（方案 1～方案 3）后面的疑难解答部分。

![](images/page_162_image_6.jpg)

## 致谢

感谢 Ellen Hildebrandt 博士对方案 3、方案 8、方案 9、方案 10 的校正工作和技术编辑作出的贡献。

## 参考文献

- Ailor E, Pathmanathan J, Jongbloed JD, Betenbaugh MJ. 1999. A bacterial signal peptidase enhances processing of a recombinant single chain antibody fragment in insect cells. Biochem Biophys Res Commun 255: 444–450.
- Aller SG, Yu J, Ward A, Weng Y, Chittaboina S, Zhuo R, Harrell PM, Trinh YT, Zhang Q, Urbatsch IL, et al. 2009. Structure of P-glycoprotein reveals a molecular basis for poly-specific drug binding. Science 323: 1718–1722.
- Altmann F, Schwihla H, Staudacher E, Glossl J, Marz L. 1995. Insect cells contain an unusual, membrane-bound β-N-acetylglucosaminidase probably involved in the processing of protein N-glycans. J Biol Chem 270: 17344–17349.
- Amann E, Brosius J. 1985. "ATG vectors" for regulated high-level expression of cloned genes in Escherichia coli. Gene 40: 183–190.
- Amann E, Brosius J, Ptashne M. 1983. Vectors bearing a hybrid trp-lac promoter useful for regulated expression of cloned genes in Escherichia coli. Gene 25: 167–178.
- Amann E, Ochs B, Abel KJ. 1988. Tightly regulated tac promoter vectors useful for the expression of unfused and fused proteins in Escherichia coli. Gene 69: 301–315.
- Andre N, Cherouati N, Prual C, Steffan T, Zeder-Lutz G, Magnin T, Pattus F, Michel H, Wagner R, Reinhart C. 2006. Enhancing functional production of G protein-coupled receptors in Pichia pastoris to levels required for structural studies via a single expression screen. Protein Sci 15: 1115–1126.
- Armstrong RN. 1997. Structure, catalytic mechanism, and evolution of the glutathione transferases. Chem Res Toxicol 10: 2–18.
- Arnau J, Lauritzen C, Petersen GE, Pedersen J. 2006. Current strategies for the use of affinity tags and tag removal for the purification of recombinant proteins. Protein Expr Purif 48: 1–13.
- Barnes HJ, Arlotto MP, Waterman MR. 1991. Expression and enzymatic activity of recombinant cytochrome P450 17 α-hydroxylase in Escherichia coli. Proc Natl Acad Sci 88: 5597–5601.
- Barry GF. 1988. A broad-host-range shuttle system for gene insertion into the chromosomes of Gram-negative bacteria. Gene 71: 75–84.
- Bennetzen JL, Hall BD. 1982. Codon selection in yeast. J Biol Chem 257:3026–3031.
- Bradshaw RA, Brickey WW, Walker KW. 1998. N-Terminal processing: The methionine aminopeptidase and N $^{\alpha}$ -acetyl transferase families. Trends Biochem Sci 23: 263–267.
- Bujard H, Gentz R, Lanzer M, Stueber D, Mueller M, Ibrahim I, Haeuptle MT, Dobberstein B. 1987. A T5 promoter-based transcription–translation system for the analysis of proteins in vitro and in vivo. Methods Enzymol 155: 416–433.
- Cabrita LD, Bottomley SP. 2004. Protein expression and refolding—A practical guide to getting the most out of inclusion bodies. Biotechnol Annu Rev 10: 31–50.
- Carter P, Wells JA. 1987. Engineering enzyme specificity by substrate-assisted catalysis. Science 237: 394–399.
- Carter P, Nilsson B, Burnier JP, Burdick D, Wells JA. 1989. Engineering subtilisin BPN' for site-specific proteolysis. Proteins 6: 240–248.
- Cereghino GP, Cregg JM. 1999. Applications of yeast in biotechnology: Protein production and genetic analysis. Curr Opin Biotechnol 10:422–427.
- Chang JY. 1985. Thrombin specificity. Requirement for apolar amino acids adjacent to the thrombin cleavage site of polypeptide substrate. Eur J Biochem 151: 217–224.
- Chen H, Bjerknes M, Kumar R, Jay E. 1994. Determination of the optimal aligned spacing between the Shine-Dalgarno sequence and the
- translation initiation codon of Escherichia coli mRNAs. Nucleic Acids Res 22: 4953–4957.
- Cordingley MG, Callahan PL, Sardana VV, Garsky VM, Colonno RJ. 1990. Substrate requirements of human rhinovirus 3C protease for peptide cleavage in vitro. J Biol Chem 265: 9062–9065.
- Cregg JM. 2007. Introduction: Distinctions between Pichia pastoris and other expression systems. Methods Mol Biol 389: 1–10.
- Gregg JM, Cereghino JL, Shi J, Higgins DR. 2000. Recombinant protein expression in Pichia pastoris. Mol Biotechnol 16: 23–52.
- Daly R, Hearn MT. 2005. Expression of heterologous proteins in Pichia pastoris: A useful experimental tool in protein engineering and production. J Mol Recognit 18: 119–138.
- Davis TR, Wickham TJ, McKenna KA, Granados RR, Shuler ML, Wood HA. 1993. Comparative recombinant protein production of eight insect cell lines. In Vitro Cell Dev Biol Anim 29A: 388–390.
- de Boer HA, Comstock LJ, Vasser M. 1983. The tac promoter: A functional hybrid derived from the trp and lac promoters. Proc Natl Acad Sci 80:21–25.
- de Smit MH, van Duin J. 1994a. Control of translation by mRNA secondary structure in Escherichia coli. A quantitative analysis of literature data. J Mol Biol 244: 144–150.
- de Smit MH, van Duin J. 1994b. Translational initiation on structured messengers. Another role for the Shine-Dalgarno interaction. J Mol Biol 235: 173–184.
- di Guan C, Li P, Riggs PD, Inouye H. 1988. Vectors that facilitate the expression and purification of foreign peptides in Escherichia coli by fusion to maltose-binding protein. Gene 67: 21–30.
- Dubendorff JW, Studier FW. 1991. Controlling basal expression in an inducible T7 expression system by blocking the target T7 promoter with lac repressor. J Mol Biol 219: 45–59.
- Dykes CW, Bookless AB, Coomber BA, Noble SA, Humber DC, Hobden AN. 1988. Expression of atrial natriuretic factor as a cleavable fusion protein with chloramphenicol acetyltransferase in Escherichia coli. Eur J Biochem 174: 411–416.
- Einhauer A, Jungbauer A. 2001. The FLAG peptide, a versatile fusion tag for the purification of recombinant proteins. J Biochem Biophys Methods 49: 455–465.
- Endo Y, Sawasaki T. 2006. Cell-free expression systems for eukaryotic protein production. Curr Opin Biotechnol 17: 373–380.
- Englesberg E, Sheppard D, Squires C, Meronk F Jr. 1969. An analysis of "revertants" of a deletion mutant in the C gene of the L-arabinose gene complex in Escherichia coli B/r: Isolation of initiator constitutive mutants ( $I^{C}$ ). J Mol Biol 43: 281–298.
- Esposito D, Chatterjee DK. 2006. Enhancement of soluble protein expression through the use of fusion tags. Curr Opin Biotechnol 17: 353–358.
- Falzon L, Suzuki M, Inouye M. 2006. Finding one of a kind: Advances in single-protein production. Curr Opin Biotechnol 17: 347–352.
- Farabaugh PJ. 1978. Sequence of the lacI gene. Nature 274: 765–769.
- Fraser MJ, Smith GE, Summers MD. 1983. Acquisition of host cell DNA sequences by baculoviruses: Relationship between host DNA insertions and FP mutants of Autographa californica and Galleria mellonella nuclear polyhedrosis viruses. J Virol 47: 287–300.
- Friesen PD. 1997. Regulation of baculovirus early gene expression. In The baculoviruses (ed. LK Miller), pp. 141–170. Plenum Press, New York.
- Gaberc-Porekar V, Menart V. 2001. Perspectives of immobilized-metal affinity chromatography. J Biochem Biophys Methods 49: 335–360.
- Gao S-Y. 1958. Culturing all types of silkworm tissues using the monolayer culture. Chin Sci Bull 7: 219–220.
- Gao S-Y, Liu NT, Zia TU. 1959. Tissue culture methods for cultivation of virus grasserie. Acta Virol 3: 55–60.
- Gearing DP, Nicola NA, Metcalf D, Foote S, Willson TA, Gough NM, Williams RL. 1989. Production of leukemia inhibitory factor in Escherichia coli by a novel procedure and its use in maintaining embryonic stem cells in culture. Nat Biotechnol 7: 1157–1161.
- Gentz R, Bujard H. 1985. Promoters recognized by Escherichia coli RNA polymerase selected by function: Highly efficient promoters from bacteriophage T5. J Bacteriol 164: 70–77.
- Ghrayeb J, Kimura H, Takahara M, Hsiung H, Masui Y, Inouye M. 1984. Secretion cloning vectors in Escherichia coli. EMBO J 3: 2437–2442.
- Gibbs PE, Zouzias DC, Freedberg IM. 1985. Differential post-translational modification of human type I keratins synthesized in a rabbit reticulocyte cell-free system. Biochim Biophys Acta 824: 247–255.
- Glocker B, Hoopes RR Jr, Hodges L, Rohrmann GF. 1993. In vitro transcription from baculovirus late gene promoters: Accurate mRNA
- initiation by nuclear extracts prepared from infected Spodoptera frugiperda cells. J Virol 67: 3771–3776.
- Godeau F, Saucier C, Kourilsky P. 1992. Replication inhibition by nucleoside analogues of a recombinant Autographa californica multicapsid nuclear polyhedrosis virus harboring the herpes thymidine kinase gene driven by the IE-1(0) promoter: A new way to select recombinant baculoviruses. Nucleic Acids Res 20: 6239–6246.
- Grace TD. 1962. The development of a cytoplasmic polyhedrosis in insect cells grown in vitro. Virology 18: 33–42.
- Grantham R, Gautier C, Gouy M. 1980a. Codon frequencies in 119 individual genes confirm consistent choices of degenerate bases according to genome type. Nucleic Acids Res 8: 1893–1912.
- Grantham R, Gautier C, Gouy M, Mercier R, Pave A. 1980b. Codon catalog usage and the genome hypothesis. Nucleic Acids Res 8: r49–r62.
- Grantham R, Gautier C, Gouy M, Jacobzone M, Mercier R. 1981. Codon catalog usage is a genome strategy modulated for gene expressivity. Nucleic Acids Res 9: r43–r74.
- Graslund S, Nordlund P, Weigelt J, Hallberg BM, Bray J, Gileadi O, Knapp S, Oppermann U, Arrowsmith C, Hui R, et al. 2008. Protein production and purification. Nat Methods 5: 135–146.
- Gray GL, Baldridge JS, McKeown KS, Heyneker HL, Chang CN. 1985. Periplasmic production of correctly processed human growth hormone in Escherichia coli: Natural and bacterial signal sequences are interchangeable. Gene 39: 247–254.
- Guzman LM, Belin D, Carson MJ, Beckwith J. 1995. Tight regulation, modulation, and high-level expression by vectors containing the arabinose pBAD promoter. J Bacteriol 177: 4121–4130.
- Haggerty DM, Schleif RF. 1975. Kinetics of the onset of catabolite repression in Escherichia coli as determined by lac messenger ribonucleic acid initiations and intracellular cyclic adenosine 3',5'-monophosphate levels. J Bacteriol 123: 946–953.
- Hamilton SR, Davidson RC, Sethuraman N, Nett JH, Jiang Y, Rios S, Bobrowicz P, Stadheim TA, Li H, Choi BK, et al. 2006. Humanization of yeast to produce complex terminally sialylated glycoproteins. Science 313: 1441–1443.
- Hartner FS, Ruth C, Langenegger D, Johnson SN, Hyka P, Lin-Cereghino GP, Lin-Cereghino J, Kovar K, Cregg JM, Glieder A. 2008. Promoter library designed for fine-tuned gene expression in Pichia pastoris. Nucleic Acids Res 36: e76. doi: 10.1093/nar/gkn369.
- Hillebrecht JR, Chong S. 2008. A comparative study of protein synthesis in in vitro systems: From the prokaryotic reconstituted to the eukaryotic extract-based. BMC Biotechnol 8: 58. doi: 10.1186/1472-6750-8-58.
- Hill-Perkins MS, Possee RD. 1990. A baculovirus expression vector derived from the basic protein promoter of Autographa californica nuclear polyhedrosis virus. J Gen Virol 71: 971–976.
- Hino M, Kataoka M, Kajimoto K, Yamamoto T, Kido J, Shinohara Y, Baba Y. 2008. Efficiency of cell-free protein synthesis based on a crude cell extract from Escherichia coli, wheat germ, and rabbit reticulocytes. J Biotechnol 133: 183–189.
- Hirsch JD, Eslamizar L, Filanoski BJ, Malekzadeh N, Haugland RP, Beechem JM, Haugland RP. 2002. Easily reversible desthiobiotin binding to streptavidin, avidin, and other biotin-binding proteins: Uses for protein labeling, detection, and isolation. Anal Biochem 308: 343–357.
- Hoffmann M, Nemetz C, Madin K, Buchberger B. 2004. Rapid translation system: A novel cell-free way from gene to protein. Biotechnol Annu Rev 10: 1–30.
- Hollister J, Grabenhorst E, Nimtz M, Conradt H, Jarvis DL. 2002. Engineering the protein N-glycosylation pathway in insect cells for production of biantennary, complex N-glycans. Biochemistry 41: 15093–15104.
- Hopp TP, Gallis B, Prickett KS. 1988. A short polypeptide marker sequence useful for recombinant protein identification and purification. Bio/Technology 6: 1204–1210.
- Hoss A, Moarefi I, Scheidtmann KH, Cisek LJ, Corden JL, Dornreiter I, Arthur AK, Fanning E. 1990. Altered phosphorylation pattern of simian virus 40 T antigen expressed in insect cells by using a baculovirus vector. J Virol 64: 4799–4807.
- Hsu TA, Betenbaugh MJ. 1997. Coexpression of molecular chaperone BiP improves immunoglobulin solubility and IgG secretion from Trichoplusia ni insect cells. Biotechnol Prog 13: 96–104.
- Huttenhofer A, Noller HF. 1994. Footprinting mRNA-ribosome complexes with chemical probes. EMBO J 13: 3892–3901.
- Iacono-Connors LC, Schmaljohn CS, Dalrymple JM. 1990. Expression of the Bacillus anthracis protective antigen gene by baculovirus and vaccinia virus recombinants. Infect Immun 58: 366–372.
- Inan M, Meagher MM. 2001. Non-repressing carbon sources for alcohol oxidase (AOX1) promoter of Pichia pastoris. J Biosci Bioeng 92:585–589.
- Itakura K, Hirose T, Crea R, Riggs AD, Heyneker HL, Bolivar F, Boyer HW. 1977. Expression in Escherichia coli of a chemically synthesized gene for the hormone somatostatin. Science 198: 1056–1063.
- Ivanov I, Alexandrova R, Dragulev B, Saraffova A, AbouHaidar MG. 1992. Effect of tandemly repeated AGG triplets on the translation of CAT-mRNA in E. coli. FEBS Lett 307: 173–176.
- Jacobs PP, Geysens S, Vervecken W, Contreras R, Callewaert N. 2009. Engineering complex-type N-glycosylation in Pichia pastoris using Glyco-Switch technology. Nat Protoc 4: 58–70.
- Jarvis DL, Summers MD, Garcia A Jr, Bohlmeyer DA. 1993. Influence of different signal peptides and prosequences on expression and secretion of human tissue plasminogen activator in the baculovirus system. J Biol Chem 268: 16754–16762.
- Jenny RJ, Mann KG, Lundblad RL. 2003. A critical review of the methods for cleavage of fusion proteins with thrombin and factor Xa. Protein Expr Purif 31: 1–11.
- Kapust RB, Tözsér J, Fox JD, Anderson DE, Cherry S, Copeland TD, Waugh DS. 2001. Tobacco etch virus protease: Mechanism of autolysis and rational design of stable mutants with wild-type catalytic proficiency. Protein Eng 14: 993–1000.
- Katzen F, Chang G, Kudlicki W. 2005. The past, present and future of cell-free protein synthesis. Trends Biotechnol 23: 150–156.
- Keen NT, Tamaki S. 1986. Structure of two pectate lyase genes from Erwinia chrysanthemi EC16 and their high-level expression in Escherichia coli. J Bacteriol 168: 595–606.
- Khosravi-Far R, Der CJ. 1995. Prenylation analysis of bacterially expressed and insect cell-expressed Ras and Ras-related proteins. Methods Enzymol 255: 46–60.
- Kim JS, Raines RT. 1993. Ribonuclease S-peptide as a carrier in fusion proteins. Protein Sci 2: 348–356.
- Kitts PA, Possee RD. 1993. A method for producing recombinant baculovirus expression vectors at high frequency. BioTechniques 14: 810–817.
- Kitts PA, Ayres MD, Possee RD. 1990. Linearization of baculovirus DNA enhances the recovery of recombinant virus expression vectors. Nucleic Acids Res 18: 5667–5672.
- Kluwe L, Maeda K, Miegel A, Fujita-Becker S, Maeda Y, Talbo G, Houthaeve T, Kellner R. 1995. Rabbit skeletal muscle α α-tropomyosin expressed in baculovirus-infected insect cells possesses the authentic N-terminus structure and functions. J Muscle Res Cell Motil 16: 103–110.
- Kozak M. 1987. At least six nucleotides preceding the AUG initiator codon enhance transplantation in mammalian cells. J Mol Biol 196: 947–950.
- Kuroda K, Geyer H, Geyer R, Doerfler W, Klenk HD. 1990. The oligosaccharides of influenza virus hemagglutinin expressed in insect cells by a baculovirus vector. Virology 174: 418–429.
- Kuroda K, Veit M, Klenk HD. 1991. Retarded processing of influenza virus hemagglutinin in insect cells. Virology 180: 159–165.
- Lauritzen C, Tuchsen E, Hansen PE, Skovgaard O. 1991. BPTI and N-terminal extended analogues generated by factor Xa cleavage and cathepsin C trimming of a fusion protein expressed in Escherichia coli. Protein Expr Purif 2: 372–378.
- LaVallie ER, DiBlasio EA, Kovacic S, Grant KL, Schendel PF, McCoy JM. 1993. A thioredoxin gene fusion expression system that circumvents inclusion body formation in the E. coli cytoplasm. Biotechnology (NY) 11: 187–193.
- LaVallie ER, DiBlasio-Smith EA, Collins-Racie LA, Lu Z, McCoy JM. 2003. Thioredoxin and related proteins as multifunctional fusion tags for soluble expression in E. coli. Methods Mol Biol 205: 119–140.
- Light A, Savithri HS, Liepnieks JJ. 1980. Specificity of bovine enterokinase toward protein substrates. Anal Biochem 106: 199–206.
- Lin-Cereghino J, Lin-Cereghino GP. 2007. Vectors and strains for expression. Methods Mol Biol 389: 11–26.
- Lin-Cereghino J, Hashimoto MD, Moy A, Castelo J, Orazem CC, Kuo P, Xiong S, Gandhi V, Hatae CT, Chan A, et al. 2008. Direct selection of Pichia pastoris expression strains using new G418 resistance vectors. Yeast 25: 293–299.
- Lindorfer MA, Sherman NE, Woodfork KA, Fletcher JE, Hunt DF, Garrison JC. 1996. G protein γ subunits with altered prenylation sequences are properly modified when expressed in Sf9 cells. J Biol Chem 271:18582–18587.
- Long SB, Campbell EB, Mackinnon R. 2005. Crystal structure of a mammalian voltage-dependent Shaker family K+ channel. Science 309:897–893.
- Lowe PN, Page MJ, Bradley S, Rhodes S, Sydenham M, Paterson H, Skinner RH. 1991. Characterization of recombinant human Kirsten-ras (4B) pp21 produced at high levels in Escherichia coli and insect baculovirus expression systems. J Biol Chem 266: 1672–1678.
- Lu Z, DiBlasio-Smith EA, Grant KL, Warne NW, LaVallie ER, Collins-Racie LA, Follettie MT, Williamson MJ, McCoy JM. 1996. Histidine patch thioredoxins. Mutant forms of thioredoxin with metal chelating affinity that provide for convenient purifications of thioredoxin fusion proteins. J Biol Chem 271: 5059–5065.
- Luckow VA, Lee SC, Barry GF, Olins PO. 1993. Efficient generation of infectious recombinant baculoviruses by site-specific transposon-mediated insertion of foreign genes into a baculovirus genome propagated in Escherichia coli. J Virol 67: 4566–4579.
- Lueking A, Horn S, Lehrach H, Cahill DJ. 2003. A dual-expression vector allowing expression in E. coli and P. pastoris, including new modifications. Methods Mol Biol 205: 31–42.
- Lynn DE. 2007b. Available lepidopteran insect cell lines. Methods Mol Biol 388: 117–138.
- Makoff AJ, Smallwood AE. 1990. The use of two-cistron constructions in improving the expression of a heterologous gene in E. coli. Nucleic Acids Res 18: 1711–1718.
- Marston FA. 1986. The purification of eukaryotic polypeptides synthesized in Escherichia coli. Biochem J 240: 1–12.
- Maina CV, Riggs PD, Grandea AG III, Slatko BE, Moran LS, Tagliamonte JA, McReynolds LA, Guan CD. 1988. An Escherichia coli vector to express and purify foreign proteins by fusion to and separation from maltose-binding protein. Gene 74: 365–373.
- McDowell MJ, Joklik WK, Villa-Komaroff L, Lodish HF. 1972. Translation of reovirus messenger RNAs synthesized in vitro into reovirus polypeptides by several mammalian cell-free extracts. Proc Natl Acad Sci 69: 2649–2653.
- Mikami S, Kobayashi T, Masutani M, Yokoyama S, Imataka H. 2008. A human cell-derived in vitro coupled transcription/translation system optimized for production of recombinant proteins. Protein Expr Purif 62: 190–198.
- Miyamoto C, Smith GE, Farrell-Towt J, Chizzonite R, Summers MD, Ju G. 1985. Production of human c-myc protein in insect cells infected with a baculovirus expression vector. Mol Cell Biol 5: 2860–2865.
- Murhammer DW. 2007. Baculovirus and insect cell expression protocols. Humana Press, Totowa, NJ.
- Murphy CI, McIntire JR, Davis DR, Hodgdon H, Seals JR, Young E. 1993. Enhanced expression, secretion, and large-scale purification of recombinant HIV-1 gp120 in insect cell using the baculovirus egt and pp67 signal peptides. Protein Expr Purif 4: 349–357.
- Murthy TV, Wu W, Qiu QQ, Shi Z, LaBaer J, Brizuela L. 2004. Bacterial cell-free system for high-throughput protein expression and a comparative analysis of Escherichia coli cell-free and whole cell expression systems. Protein Expr Purif 36: 217–225.
- Nagai K, Thogersen HC. 1984. Generation of β-globin by sequence-specific proteolysis of a hybrid protein produced in Escherichia coli. Nature 309: 810–812.
- Nagai K, Thogersen HC. 1987. Synthesis and sequence-specific proteolysis of hybrid proteins produced in Escherichia coli. Methods Enzymol 153:461–481.
- Nirenberg MW, Matthaei JH. 1961. The dependence of cell-free protein synthesis in E. coli upon naturally occurring or synthetic polyribonucleotides. Proc Natl Acad Sci 47: 1588–1602.
- Oker-Blom C, Pettersson RF, Summers MD. 1989. Baculovirus polyhedrin promoter-directed expression of rubella virus envelope glycoproteins, E1 and E2, in Spodoptera frugiperda cells. Virology 172: 82–91.
- O'Reilly DR, Miller LK, Luckow VA. 1994. Baculovirus expression vectors. Oxford University Press, New York.
- Parcej DN, Eckhardt-Strelau L. 2003. Structural characterisation of neuronal voltage-sensitive K+ channels heterologously expressed in Pichia pastoris. J Mol Biol 333: 103–116.
- Parks TD, Leuther KK, Howard ED, Johnston SA, Dougherty WG. 1994. Release of proteins and peptides from fusion proteins using a recombinant plant virus proteinase. Anal Biochem 216: 413–417.
- Pelham HR, Jackson RJ. 1976. An efficient mRNA-dependent translation system from reticulocyte lysates. Eur J Biochem 67: 247–256.
- Pennock GD, Shoemaker C, Miller LK. 1984. Strong and regulated expression of Escherichia coli β-galactosidase in insect cells with a baculovirus vector. Mol Cell Biol 4: 399–406.
- Rangwala SH, Finn RF, Smith CE, Berberich SA, Salsgiver WJ, Stallings WC, Glover GI, Olins PO. 1992. High-level production of active HIV-1 protease in Escherichia coli. Gene 122: 263–269.
- Reznikoff WS. 1992. The lactose operon-controlling elements: A complex paradigm. Mol Microbiol 6: 2419–2422.
- Richards FM, Vithayathil PJ. 1959. The preparation of subtilisin-modified ribonuclease and the separation of the peptide and protein components. J Biol Chem 234: 1459–1465.
- Ringquist S, Shinedling S, Barrick D, Green L, Binkley J, Stormo GD, Gold L. 1992. Translation initiation in Escherichia coli: Sequences within the ribosome-binding site. Mol Microbiol 6: 1219–1229.
- Roberts BE, Paterson BM. 1973. Efficient translation of tobacco mosaic virus RNA and rabbit globin 9S RNA in a cell-free system from commercial wheat germ. Proc Natl Acad Sci 70: 2330–2334.
- Rosenberg SJ, Rane MJ, Dean WL, Corpier CL, Hoffman JL, McLeish KR. 1998. Effect of γ subunit carboxyl methylation on the interaction of G protein α subunits with βγ subunits of defined composition. Cell Signal 10: 131–136.
- Saida F. 2007. Overview on the expression of toxic gene products in Escherichia coli. Curr Protoc Protein Sci 5: 5.19.1–5.19.13.
- Schleif R. 2000. Regulation of the L-arabinose operon of Escherichia coli. Trends Genet 16: 559–565.
- Schmidt TG, Skerra A. 1993. The random peptide library-assisted engineering of a C-terminal affinity peptide, useful for the detection and purification of a functional Ig Fv fragment. Protein Eng 6:109–122.
- Schmidt TG, Koepke J, Frank R, Skerra A. 1996. Molecular interaction between the Strep-tag affinity peptide and its cognate target, streptavidin. J Mol Biol 255: 753–766.
- Schuck S, Prinz WA, Thorn KS, Voss C, Walter P. 2009. Membrane expansion alleviates endoplasmic reticulum stress independently of the unfolded protein response. J Cell Biol 187: 525–536.
- Shine J, Dalgarno L. 1974. The 3'-terminal sequence of Escherichia coli 16S ribosomal RNA: Complementarity to nonsense triplets and ribosome binding sites. Proc Natl Acad Sci 71: 1342–1346.
- Smith DB, Johnson KS. 1988. Single-step purification of polypeptides expressed in Escherichia coli as fusions with glutathione S-transferase. Gene 67: 31–40.
- Smith GE, Fraser MJ, Summers MD. 1983a. Molecular engineering of the Autographa californica nuclear polyhedrosis virus genome: Deletion mutations within the polyhedrin gene. J Virol 46: 584–593.
- Smith GE, Summers MD, Fraser MJ. 1983b. Production of human β interferon in insect cells infected with a baculovirus expression vector. Mol Cell Biol 3: 2156–2165.
- Smith GE, Vlak JM, Summers MD. 1983c. Physical analysis of Autographa californica nuclear polyhedrosis virus transcripts for polyhedrin and 10,000-molecular-weight protein. J Virol 45: 215–225.
- Smith GE, Ju G, Ericson BL, Moschera J, Lahm HW, Chizzonite R, Summers MD. 1985. Modification and secretion of human interleukin 2 produced in insect cells by a baculovirus expression vector. Proc Natl Acad Sci 82: 8404–8408.
- Smith MC, Furman TC, Ingolia TD, Pidgeon C. 1988. Chelating peptide-immobilized metal ion affinity chromatography. A new concept in affinity chromatography for recombinant proteins. J Biol Chem 263:7211–7215.
- Spirin AS. 2004. High-throughput cell-free systems for synthesis of functionally active proteins. Trends Biotechnol 22: 538–545.
- Stark MJ. 1987. Multicopy expression vectors carrying the lac repressor gene for regulated high-level expression of genes in Escherichia coli. Gene 51: 255–267.
- Steitz JA. 1979. Prokaryotic ribosome binding sites. Methods Enzymol 60:311–321.
- Steitz JA, Jakes K. 1975. How ribosomes select initiator regions in mRNA: Base pair formation between the 3' terminus of 16S rRNA and the mRNA during initiation of protein synthesis in Escherichia coli. Proc Natl Acad Sci 72: 4734–4738.
- Stiles B, Wood HA. 1983. A study of the glycoproteins of Autographa californica nuclear polyhedrosis virus (AcNPV). Virology 131: 230–241.
- Stofko-Hahn RE, Carr DW, Scott JD. 1992. A single step purification for recombinant proteins. Characterization of a microtubule associated protein (MAP 2) fragment which associates with the type II cAMP-dependent protein kinase. FEBS Lett 302: 274–278.
- Studier FW. 1991. Use of bacteriophage T7 lysozyme to improve an inducible T7 expression system. J Mol Biol 219: 37–44.
- Studier FW, Moffatt BA. 1986. Use of bacteriophage T7 RNA polymerase to direct selective high-level expression of cloned genes. J Mol Biol 189: 113–130.
- Stueber D, Ibrahimi I, Cutler D, Dobberstein B, Bujard H. 1984. A novel in vitro transcription-translation system: Accurate and efficient synthesis of single proteins from cloned DNA sequences. EMBO J 3: 3143–3148.
- Sullivan ML, Youker RT, Watkins SC, Brodsky JL. 2003. Localization of the BiP molecular chaperone with respect to endoplasmic reticulum foci containing the cystic fibrosis transmembrane conductance regulator in yeast. J Histochem Cytochem 51: 545–548.
- Sunga AJ, Tolstorukov I, Cregg JM. 2008. Posttransformational vector amplification in the yeast Pichia pastoris. FEMS Yeast Res 8:870–876.
- Tabor S, Richardson CC. 1985. A bacteriophage T7 RNA polymerase/promoter system for controlled exclusive expression of specific genes. Proc Natl Acad Sci 82: 1074–1078.
- Talmadge K, Kaufman J, Gilbert W. 1980. Bacteria mature preproinsulin to proinsulin. Proc Natl Acad Sci 77: 3988–3992.
- Tessier DC, Thomas DY, Khouri HE, Laliberte F, Vernet T. 1991. Enhanced secretion from insect cells of a foreign protein fused to the honeybee melittin signal peptide. Gene 98: 177–183.
- Thomsen DR, Post LE, Elhammer AP. 1990. Structure of O-glycosidically linked oligosaccharides synthesized by the insect cell line Sf9. J Cell Biochem 43: 67–79.
- Tropea JE, Cherry S, Waugh DS. 2009. Expression and purification of soluble His $_{6}$ -tagged TEV protease. Methods Mol Biol 498: 297–307.
- Vernet T, Tessier DC, Richardson C, Laliberte F, Khouri HE, Bell AW, Storer AC, Thomas DY. 1990. Secretion of functional papain precursor from insect cells. Requirement for N-glycosylation of the pro-region. J Biol Chem 265: 16661–16666.
- Voss S, Skerra A. 1997. Mutagenesis of a flexible loop in streptavidin leads to higher affinity for the Strep-tag II peptide and improved performance in recombinant protein purification. Protein Eng 10: 975–982.
- Walker PA, Leong LE, Ng PW, Tan SH, Waller S, Murphy D, Porter AG. 1994. Efficient and rapid affinity purification of proteins using recombinant fusion proteases. Biotechnology (NY) 12: 601–605.
- Wang Z, Stalcup LD, Harvey BJ, Weber J, Chloupkova M, Dumont ME, Dean M, Urbatsch IL. 2006. Purification and ATP hydrolysis of the putative cholesterol transporters ABCG5 and ABCG8. Biochemistry 45: 9929–9939.
- Weickert MJ, Doherty DH, Best EA, Olins PO. 1996. Optimization of heterologous protein production in Escherichia coli. Curr Opin Biotechnol 7: 494–499.
- Wickham TJ, Davis T, Granados RR, Shuler ML, Wood HA. 1992. Screening of insect cell lines for the production of recombinant proteins and infectious virus in the baculovirus expression system. Biotechnol Prog 8: 391–396.
- Yang C, Mayau V, Godeau F, Goud B. 1992. Characterization of the unprocessed and processed forms of rab6 expressed in baculovirus/insect cell systems. Biochem Biophys Res Commun 182: 1499–1505.
- Yokoyama S. 2003. Protein expression systems for structural genomics and proteomics. Curr Opin Chem Biol 7: 39–43.
- Zhao Y, Chapman DA, Jones IM. 2003. Improving baculovirus recombination. Nucleic Acids Res 31: e66. doi: 10.1093/nar/gng006.
- Zubay G. 1973. In vitro synthesis of protein in microbial systems. Annu Rev Genet 7: 267–287.
- Zuidema D, Schouten A, Usmany M, Maule AJ, Belsham GJ, Roosien J, Klinge-Roode EC, van Lent JW, Vlak JM. 1990. Expression of cauliflower mosaic virus gene I in insect cells using a novel polyhedrin-based baculovirus expression vector. J Gen Virol 71: 2201–2209.

## 方案 1 在大肠杆菌中利用可用 IPTG 诱导的启动子表达克隆化基因

由于乳糖操纵子是原核基因表达调控的典型代表，所以许多大肠杆菌表达载体用乳糖操纵子作为调控单元（Reznikoff 1992）。乳糖启动子是弱启动子，如今杂合的强启动子已经开发出来并用于大肠杆菌中制备外源蛋白（Baneyx 1999）。在本章导言中已经叙述，在大肠杆菌中表达外源蛋白时，所用的启动子通常要么依赖于宿主细胞的 RNA 聚合酶，要么向宿主细胞中引入来源于 T7 噬菌体的 RNA 聚合酶。基于这两种思路设计的载体均需要添加不可水解的乳糖类似物异丙基-1-硫代-β-呋喃半乳糖苷（IPTG）来诱导外源蛋白的表达。本方案旨在利用这类载体或其他可用 IPTG 诱导的载体。其他表达系统在随后讨论中涉及。

![](images/page_166_image_3.jpg)

## 材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

考马斯亮蓝染色液

根据表达载体选择的适合蛋白质表达的大肠杆菌菌株

为了明确宿主细胞的选择要求，参阅构建含有重组表达载体的大肠杆菌菌株部分（也可参阅本方案中的信息栏“大肠杆菌菌株的选择”）。

目的基因或 cDNA 片段

甘油（80%）

IPTG (1mol/L)

储存液分装后保存于-20℃。反复冻融1次或2次后勿继续使用。

可用 IPTG 诱导的表达载体

对于可用阿拉伯糖诱导的表达载体，见替代方案“在大肠杆菌中利用阿拉伯糖 BAD 启动子表达克隆基因”。

含有适当抗生素的 LB 琼脂平板（如含有  $200 \mu g/mL$  的氨苄青霉素）

含有适当抗生素的LB培养基（如含有 $200\mu \mathrm{g / mL}$ 的氨苄青霉素，用无菌水配制 $200\mathrm{mg / mL}$ 的氨苄青霉素储存液，用前加至培养基中）&lt;A&gt;

核酸和寡核苷酸

含 SDS 的聚丙烯酰胺（方案 8）

阳性质粒

pET 系列载体通常会有对照载体，这些载体带有相同的启动子，并可表达 lacZ 融合蛋白。对于一些可用 IPTG 诱导的载体，并可表达融合有一定分子质量的融合蛋白，它们的亲本载体可作为对照载体。

SDS 上样缓冲液（5×）（方案 8）

不含 DTT 的  $5 \times$  SDS 上样缓冲液可室温保存。用前加入 1mol/L DTT 储存液至终浓度为 100mmol/L。

转化的载体和阳性对照载体

参阅本方案中信息栏“基因克隆策略”。

## 仪器

Beckman JA10、Sorvall GS3或SLA3000转子，也可使用离心力相当的、能容纳 $500\mathrm{mL}$ 离心管的转子

Beckman JA20、Sorvall SS34 或 SA600 转子，也可使用离心力相当的、能容纳 40～50mL 离心管的转子

三角烧瓶（125mL 和 1L），高压蒸汽灭菌锅

玻璃器皿或塑料制品

接种针

液氮

无菌微量离心管（1.5mL）

无菌吸头和无菌移液管

无菌旋盖管（50mL）

恒温摇床

匙状小竹板

分光光度计

涡旋振荡器

![](images/page_167_image_12.jpg)

## 方法

## 构建含有重组载体的大肠杆菌菌株

1. 将包含目的基因或 cDNA 的 DNA 片段插入到表达载体（第 3 章）。确保克隆策略使得目的蛋白的编码序列位于表达载体的可读框内，并且与翻译信号正确兼容。目的蛋白的编码序列的 3'端必须有翻译终止密码子。

## 基因克隆策略

- 大多数利用 IPTG 诱导的表达载体都包含了表达外源蛋白所需的所有调控元件，所以在构建表达载体时不需要额外的侧翼 DNA 序列。根据载体和预实验结果，可以在目的基因的 3'端添加其他调控序列以促进表达（参阅替代方案“少量制备可溶性蛋白”后的疑难解答部分）。
- 有些表达载体可与不依赖连接反应的克隆方法或 TOPO TA 克隆相兼容（如 Life Technologies 公司提供的 pET 变种表达载体）。
- 大多数表达载体的多克隆位点下游都包含了终止密码子，然而，这样的序列会向目的蛋白的 C 端引入另外的氨基酸。
- 利用宿主大肠杆菌的 RNA 聚合酶的 IPTG 诱导启动子的表达载体(如 pQE 载体)应当在 DNA 聚合酶和内切核酸酶缺陷的宿主菌（ $recA^{-}$ ， $endA^{-}$ ）中扩增，同时宿主菌中应当包含 lacIq 的等位基因（如 JM109 菌株）。
- 如果载体中含有 lacI 基因（如 pGEX 系列载体），那么任何 $recA^{-}$、$endA^{-}$大肠杆菌菌株（如 DH5α）均可用于扩增。
- 对于利用 T7 RNA 聚合酶转录的表达载体（如 pET 系列载体），任何 $recA^{-}$、$endA^{-}$大肠杆菌菌株可用于质粒扩增（如 DH5α）。通常，由于宿主 RNA 聚合酶不能识别 T7 启动子，所以这类表载体在以克隆为目的时，在宿主菌中的本底表达十分低。
- 通过 PCR 扩增得到的序列必须经过测序，以确保在扩增过程中没有引入突变。

2. 将来自阳性克隆的质粒 DNA（质粒提取方法见第 1 章）转化至适合用所选载体表达蛋白的大肠杆菌（如 pGEX 载体应转化 BL21，pET 载体应转化 BL21DE3）。为了对照试验和后续步骤，应当向对应的菌株中转化阳性质粒（如向 BL21 菌株中转化 pGEX 空载体，向 BL21DE3 菌株中转化只表达 lacZ 的 pET 载体)。将转化反应液涂布含有相应抗生素的 LB 琼脂平板（抗生素浓度参阅附录 1），于 37℃过夜培养。

## 大肠杆菌菌株的选择

应当选用胞质蛋白酶缺陷的大肠杆菌菌株，以降低目的蛋白的降解。常用的 BL21 菌株为 Lon 和 OmpT 蛋白酶缺陷。

基于 T7 启动子的表达载体应当选用含有 T7 RNA 聚合酶基因的大肠杆菌菌株，如 BL21（DE3）。

一些其他载体系统（如 pQE, pRSET）对大肠杆菌菌株的要求参阅本章导言中的表19-2。

用于蛋白质表达的大肠杆菌菌株，其转化效率往往比以克隆为目的的菌株要低。

目前已经开发了多种大肠杆菌菌株，以满足不同蛋白表达的需求。这些菌株优化的特性包括:引入稀有密码子、二硫键形成、基因可调表达，以及改善对毒性基因的忍耐力。在某些情况下，这些改变带有氯霉素抗性，如含有 pLysS/pLysE 的 BL21（DE3）菌株常用于降低 T7 启动子的渗漏表达。

3. 翌日，立即冻存大肠杆菌转化子备用。向冷冻管中加 $800\mu \mathrm{L}$ 含有抗生素的LB培养基，向培养基中接种 $3\sim 5$ 个新鲜的单克隆，$37^{\circ}C$ 振荡 $20\mathrm{min}$，并加入 $200\mu \mathrm{L}80\%$ 甘油，轻轻振荡混匀，混匀 $1\sim 2\mathrm{min}$ 后将冷冻管快速放入液氮冷冻，并置于 $-80^{\circ}C$ 保存。

对于大多数构建的菌株来说，冷冻保存的表达菌株可反复使用数次。用于在平板上划线培养的冷冻菌株不能冻融，应该用接种环从冻存表面刮取。

通常，用于蛋白质表达的菌株应使用新鲜长出的克隆，否则蛋白质的渗漏表达会杀死细胞，所以，菌种必须是新转化的，或从冷冻保存的菌种划线培养的。

冷冻前与甘油长时间的孵育会降低菌种的存活率。

## 利用大肠杆菌小量制备目标蛋白

很多研究发现在细胞生长的对数中期诱导的重要性。而且，有时明显的外源蛋白低表达是由其对宿主的不良反应引起的。最后，细胞的光密度（OD）将在随后的表达试验中，进行蛋白质水平比较时，被用于调整样品的体积。因此应仔细记录细菌接入培养基的数量、诱导前培养时间、诱导后细菌密度。

4. 分别向 $3 \mathrm{~mL}$ 培养基（含 $200 \mu \mathrm{g} / \mathrm{mL}$ 氨苄青霉素的LB培养基）分别接入含空载体对照、阳性对照以及重组表达载体的新鲜生长单克隆1或2个。$37^{\circ} \mathrm{C}$ 过夜培养。

我们推荐使用氨苄青霉素的浓度比一般情况下的浓度要高，因为β-内酰胺酶可释放到培养基中并且积累，它可在对数生长中期前就将氨苄青霉素分解。另外，由于菌体代谢，培养物呈酸性，氨苄青霉素在酸性条件下易水解。因此，在诱导时应向培养物中再次添加氨苄青霉素。

5. 在 50mL 旋盖管中加 10mL 的含 200μg/mL 氨苄青霉素的 LB 培养基，并分别接种 100μL 的过夜培养物。旋盖打开 1/4，以保证通气量。置于摇床 37℃ 培养大于 2h 至对数生长中期（A$_{550}$ 值为 0.5～1.0），A$_{550}$ 值在步骤 8 中用到。
6. 每个吸取 1mL 未诱导的培养物（诱导 0 点）至微量离心管，按步骤 9 和步骤 10 迅速制备诱导 0 点样品。
7. 向剩余的培养物中加 IPTG 至终浓度为 0.5mmol/L（5μL 的 1mmol/L IPTG 储存液），37℃继续振荡培养（参阅如下信息栏）。

## 优化诱导温度和 IPTG 浓度

## 诱导温度

用大肠杆菌高表达外源蛋白，最重要的变量或许就是诱导表达的温度。测定最佳表达温度对实验有决定性作用。能够成功表达目的蛋白的温度范围是15～42℃。蛋白质表达的最佳温度范围很窄，一般在2～4℃。有时温度对蛋白质表达有影响或无任何影响的原因还不明确，但是，蛋白质表达受诸多因素影响，这种影响可能是单个因素作用，也可能是多个因素共同作用。影响蛋白质表达的因素包括菌体生长速率、目的蛋白在胞内折叠、营养素（如血红素、FAD、生物素等）的可用量、外源蛋白的热变性、细胞分泌装置或蛋白折叠装置过载、细胞内蛋白酶活性或者是其他溶菌酶活性、细菌SOS应急系统活性或其他因素。由于这些不确定因素，Gedanken（“认为”）预测最佳生长温度所起的作用极小，需要反复试验确定。

## IPTG 浓度

lac 启动子诱导所用的 IPTG 浓度影响表达水平。推荐诱导的 IPTG 起始浓度为 0.5mmol/L，并可相应提高浓度。IPTG 最佳浓度一般依经验而定，其浓度范围为 0.01～2.0mmol/L。使用无 lac 透性酶（lacY⁻，如 Merck Biosciences 公司的 Tuner 系列菌株）的大肠杆菌宿主可方便 IPTG 浓度的优化。对于某些蛋白质，应缓慢诱导表达载体的转录（低 IPTG 浓度），以免使细菌生物合成系统过载。

8. 在不同的诱导时间点取样（如在诱导 $1\mathrm{h}$ 、 $2\mathrm{h}$ 、 $3\mathrm{h}$ 、 $4\mathrm{h}$ 、 $5\mathrm{h}$ 、 $6\mathrm{h}$ 取样）。首先，用分光光度计测量各取样点培养物的 $\mathrm{A}_{550}$ 值，将诱导零点时培养物的 $\mathrm{A}_{550}$ 值除以当前时间点培养物的 $\mathrm{A}_{550}$ 值，计算得出当前时间点应取培养物的体积。将在各诱导时间点的培养物转移至微量离心管。例如，如果在培养物的 $\mathrm{A}_{550} = 0.6$ 时开始诱导，培养 $2\mathrm{h}$ 后 $\mathrm{A}_{550} = 1.0$ ，吸取 $0.6 / 1.0 = 0.6\mathrm{mL}$ 的培养物至微量离心管。此步骤是为了使各时间点取的培养物有相等的细胞蛋白质量。
9. 用微型离心机将微量离心管于室温最大转速离心 $1\mathrm{min}$，吸弃上清。确保分光光度计的读数在其线性范围内（$0.1 \sim 1.0 \mathrm{OD}_{550}$）。根据实际情况，可用LB培养基将样品稀释至分光光度计读数范围。
10. 用  $50 \mu L$   $5 \times$  SDS 加样缓冲液重悬菌体，并置于  $85^{\circ}C$  水浴 2min，同时剧烈振荡。用微型离心机将微量离心管于室温最大转速离心 1min，将样品置于冰上，待所有样品制备完成后进行凝胶电泳分析。
11. 将样品于  $85^{\circ}$ C 短时重加热，每种上清取约  $40\mu g$  用合适浓度的 SDS-PAGE 分析（参阅方案 8 “SDS-PAGE 分析”）。大多数情况下，约  $15\mu L$  的样品即为合适的上样量。用考马斯亮蓝染液将凝胶染色，或是进行免疫印迹实验使蛋白质可见。进一步分析表达蛋白是否在可溶性组分中，可参阅以下附加方案“可溶性蛋白表达的小规模分析”。

在以谷胱甘肽-S-转移酶（GST）为对照（如含有 pGEX 载体的细胞）的样品中，在  $37^{\circ}$ C 诱导约 30min 后即可看到 29kDa 的蛋白质条带（由于表达载体上有额外的氨基酸序列，导致比 26kDa 的 GST 略大）。在诱导期间，GST 的量逐渐增加。lacZ 基因的表达产物是  $\beta$ -半乳糖苷酶，含有 lacZ 基因的细胞可诱导出其 116kDa 的蛋白质（增加的分子质量是载体上的蛋白标签）。在含有重组基因的细胞中，诱导相同时间后可看到与预期分子质量一致的重组蛋白。外源蛋白诱导的动力学和稳定性可能与对照蛋白有所不同。

## 利用大肠杆菌大量制备目标蛋白

12. 为了大量表达、纯化目的蛋白，在 $125\mathrm{mL}$ 摇瓶中加 $25\mathrm{mL}$ 的含 $200\mu \mathrm{g / mL}$ 氨苄青

霉素的LB培养基，并接种重组大肠杆菌单克隆菌落。 $37^{\circ}C$ 培养过夜。

13. 在 4L 的摇瓶中加 1L 含有抗生素（200μg/mL 氨苄青霉素）的 LB 培养基，并接种 10mL 的大肠杆菌过夜培养物，37℃培养至对数生长中期（A$_{550}$=0.5～1.0）。

在向培养基中接种较大体积的过夜培养物时，培养物必须至少稀释100倍，以避免过夜培养过程中，释放到培养基中的β-内酰胺酶转移至新鲜培养基中，除非将过夜培养物离心，并用新鲜的LB培养基重悬。

为了优化通气，培养体积应小于摇瓶体积的 20～25%，如果没有 4L 摇瓶，可用 2 个 2L 摇瓶，每个装 500mL LB、抗生素和 5mL 过夜培养物。

14. 目的蛋白的诱导表达基于之前获得的最佳培养时间、IPTG 浓度以及培养温度。

如果所用抗生素是氨苄青霉素，在诱导表达时需要再次添加抗生素。

15. 诱导表达适当时间后，4℃ 5000g 离心 15min，收集菌体并转移至 50mL 的离心管中。在液氮中快速冷冻，并保存于-80℃，或者立即将菌体裂解（参阅方案 4），随后的纯化步骤是:如果目的蛋白带有 His 标签，纯化方法参阅方案 5；如果目的蛋白带有谷胱甘肽-S-转移酶，纯化方法参阅方案 6。

![](images/page_170_image_9.jpg)

## 讨论

在大肠杆菌中，除了 lac 操纵子系统，许多利用营养物质诱导的启动子已应用于控制外源蛋白表达。这包括利用色氨酸诱导的 trp 启动子、限制离子强度诱导的 proU 启动子（Nichols and Yanofsky 1983; Tacon et al. 1983; Herbst et al. 1994）。目前，商业化的可替代 lac 操纵子的是 L-阿拉伯糖诱导的 araBAD 启动子，可用的表达载体是 pBAD 系列载体（Guzman et al. 1995）（Life Technologies 公司提供）。替代方案“在大肠杆菌中利用阿拉伯糖 BAD 启动子表达克隆基因”描述了诱导包含 araBAD 启动子载体的方法。

T7 RNA 聚合酶有一个优点便是它能与 T7 启动子特异性相互作用，而大肠杆菌染色体 DNA 无 T7 启动子。然而，大肠杆菌宿主细胞中必须表达 T7 RNA 聚合酶，以实现相应表达载体的功能。通常选用染色体 DNA 上有编码 T7 RNA 聚合酶基因 T7 gene 1 的  $\lambda$ -DE3 溶原菌作为宿主菌。T7 RNA 聚合酶的表达受 IPTG 诱导的 lacUV5 启动子调控，以避免 T7 RNA 聚合酶和外源蛋白在细胞生长阶段就有表达。另外，可同时共表达 T7 溶菌酶进一步抑制 T7 RNA 聚合酶的活性，详见附加方案“目标蛋白可溶性表达的小量试验”后的疑难解答部分。在表达有特别毒性的基因产物时，必须选用在诱导外源基因前 T7 RNA 聚合酶完全被抑制表达的宿主菌。这可通过向对数生长后期的含有表达载体的宿主菌（如 HMS174）中转染携带 T7 gene 1 基因的 CE6（ $\lambda$ cIts857 Sam7）噬菌体实现。

我们必须知道,不是所有的含有 T7 启动子的载体都含有蛋白质在大肠杆菌中翻译的信号序列。例如，pET24 载体设计为需要通过克隆插入细菌翻译信号。相比之下，pET24a～c 系列载体在转录起始位点下游提供了核糖体结合位点和 ATG 翻译起始位点。另外，T7 启动子常存在于诸如 pCDNAtm 系列的真核表达载体，这是为了体外转录而不是翻译目标 RNA。

广泛应用的 pET 系列载体的操作手册（Merck Technical Bulletin #TB055）详细介绍了此系列的表达载体和各种大肠杆菌宿主菌，同时给出了表达外源蛋白的优化方法。T7 系统能高水平表达外源蛋白，从而导致细菌自身的生物合成和加工装置超负荷。基于这个原因，降低诱导速度和生长速度可提高外源蛋白的产量。除了这个因素外，其他因素均可影响外源蛋白在大肠杆菌中的表达效率，这在附加方案“目标蛋白可溶性表达的小量试验”后的疑难解答部分有详细的讨论。

## 附加方案 目标蛋白可溶性表达的小量试验

方案 1 类似于蛋白质的 “小量制备”。本附加方案不仅检测细胞总蛋白中目标蛋白的表达水平，而且检测蛋白质是可溶性的还是存在于包含体中。可溶部分和不可溶部分分离后可用 SDS-PAGE 分析。在最后一个步骤中，偶联蛋白珠可以被处理用来洗脱天然蛋白，也可以直接在 SDS-PAGE 上样缓冲液中加热后做凝胶电泳分析。

![](images/page_171_image_4.jpg)

## 附加材料

为正确使用本方案中的器材和危险试剂，必须查阅相应的材料安全数据表并咨询所在机构的环境卫生和安全办公室。

本方案的专用试剂标注&lt;R&gt;，配方在本方案末提供。常用储备溶液、缓冲液和试剂标注&lt;A&gt;，配方见附录1。储备溶液应稀释至适用浓度后使用。

## 试剂

## 含 DNase I 和蛋白酶抑制剂的细菌细胞裂解液

一些细菌细胞裂解液可以从公司获得，如 BugBuster（Merck Biosciences）和 B-PER（Thermo Scientific Pierce）。可以选择方案 4 所介绍的其他细胞裂解方法。

细胞裂解液可以添加终浓度为  $50 \mu g/mL$  DNase I、 $0.5 mmol/L MgCl_{2}$  和  $100 \mu g/mL$  卵清溶菌酶，以减少细胞裂解液的黏稠度。100 倍的 DNase I 储存液（5 mg/mL）溶菌酶（10 mg/mL）可以溶解于水中，按 1 mL/支分装， $-20^{\circ}C$  储存。分装液溶化后不应重复使用。

为减少蛋白质降解，可以添加终浓度 1mmol/L 苯甲磺酰基氟化物（PMSF）。蛋白酶抑制剂混合试剂提供了更为全面的方法。配置 100mmol/L PMSF 储存液，可将 1.74g PMSF 溶解于无水异丙醇或者二甲基亚砜（DMSO）中。PMSF 储存液应保存于 4℃。

▲PMSF 是一种具有高度毒性的丝氨酸蛋白酶抑制剂。称取干粉 PMSF 时应该戴口罩，在使用含有 PMSF 的液体时应戴手套。因为 PMSF 可以在水溶液中水解，所以在配制储存液后，称量区域应该用水彻底擦拭干净。

## 连接有载体融合蛋白亲和配基的层析介质

GST 融合蛋白:建议使用谷胱甘肽-琼脂糖珠（可从 Sigma-Aldrich、Thermo Scientific Pierce、Life Technologies 公司，或者其他来源获得）。

His 标签融合蛋白:建议使用螯合  $Ni^{2+}$  或者  $Co^{2+}$  的琼脂糖珠（可从 Sigma-Aldrich、Thermo Scientific Pierce、QIAGEN、Life Technologies 公司，或者其他来源获得）。在运用方案 5 中的描述之前，需要使琼脂糖珠与金属离子螯合（根据生产厂家的说明修改）。

## 添加蛋白酶抑制剂的磷酸盐 PBS 漂洗缓冲液（1×）

1×PBS 配置:用无菌水稀释  $10 \times$  PBS 储存液，保存于  $4^{\circ}$ C。使用之前直接加终浓度为 1mmol/L 的 PMSF。

配置 1L 10×PBS 储存液:溶解 80g NaCl、2g KCl、14.4g  $Na_{2}HPO_{4}$  和 2.4g  $KH_{2}PO_{4}$  至 800mL 水中。如果需要，可使用 1mol/L HCl 调 pH 至 7.3。定容至 1L 体积，过滤除菌或者高压灭菌。最终 10×PBS 储存液含 1.37mol/L NaCl、27mmol/L KCl、100mmol/L  $Na_{2}HPO_{4}$  和 18mmol/L  $KH_{2}PO_{4}$ 。

## SDS-PAGE 上样缓冲液（5×）含 100mmol/L 二硫苏糖醇（DTT）（方案 8）

SDS-PAGE 上样缓冲液可以添加配体以增加洗脱效率。然而，这是不必要的，因为加热可以使绝大部分融合蛋白（如 GST）变性，DTT 可以还原  $Ni^{2+}$  或  $Co^{2+}$ ，这些都可以使 His 标签融合蛋白释放。

## 仪器

## SDS-PAGE 设备（方案 8）

![](images/page_172_image_2.jpg)

## 方法

1. 按照方案 1 的步骤 1～步骤 5。添加 0.5mmol/L IPTG，37℃振荡培养 2～4h 诱导蛋白质表达（如果需要可添加终浓度为  $100 \mu g/mL$  的氨苄青霉素）。设未诱导的阴性和阳性的平行对照。
2. 将 $10\mathrm{mL}$ 培养物于 $4^{\circ}\mathrm{C} 5000\mathrm{g}$，离心 $15\mathrm{min}$ 以沉淀细胞。弃上清，进行下一步或者冻存于 $-80^{\circ}\mathrm{C}$。
3. 用已添加 DNase I、溶菌酶和蛋白酶抑制剂的 1mL 细胞裂解液重悬解冻的细胞沉淀。转移细胞裂解组分至微量离心管中，室温下轻微混合 20min。
4. 同时，用  $1 \times$  PBS 溶胀谷胱甘肽或者  $Ni^{2+}$  琼脂糖珠。转移至微量离心管中，每个样品含  $25 \mu L$  珠（每个样品  $50 \mu L$  的 50% 琼脂糖珠悬液；1 个样品和 2 个对照共  $150 \mu L$  混合悬液）。加入 10 倍体积  $1 \times$  PBS。颠倒混匀。室温 500g，离心 3min 沉淀琼脂糖珠（2500r/min Eppendorf 5418 型离心机），除去大部分 PBS 上清。
5. 将步骤 3 获得的细胞裂解物于  $4^{\circ}$ C 20 000g，离心 30min，分离可溶解组分和不溶组分。取样品上清（可溶组分）做 SDS-PAGE 分析（ $25\mu L + 5\mu L$  SDS-PAGE 上样缓冲液）， $85^{\circ}$ C 下加热 2min，分析前置于冰上。

见“疑难解答”。

6. 将来源于步骤 5 的剩余离心上清转移至步骤 4 中的琼脂糖珠。 $4^{\circ}$ C 下轻微混合孵育 20min。将不溶性沉淀用于下一步处理。
7. 在不溶性的细胞碎片中加入  $30 \mu L$   $5 \times$  SDS-PAGE 上样缓冲液。剧烈漩涡振荡 30s， $85^{\circ}C$  加热 2min，重复漩涡振荡大于 30s，最后在室温下，15 000g，微量离心机离心 1min，去除残留的不可溶部分。冰上保存直至 SDS-PAGE（不可溶解部分）。
8. 琼脂糖珠与细胞裂解物孵育后，以 500g 离心 3min 沉淀琼脂糖珠。去掉上清（未结合部分），留样进行 SDS-PAGE 分析。用  $1 \times$  PBS 250 $\mu$ L 重悬琼脂糖珠，轻微混匀于 4℃ 孵育 10min。
9. 500g 3min 离心沉淀琼脂糖珠，去掉上清并留样进行 SDS-PAGE 分析（漂洗部分）。用微量移液器尽量地小心去除上清。
10. 用 $20 \mu \mathrm{L}$ 的 $5 \times$ SDS-PAGE 上样缓冲液重悬琼脂糖珠(结合部分), $85^{\circ} \mathrm{C}$ 下加热 $2 \mathrm{~min}$, 剧烈振荡 $30 \mathrm{~s}$ 。最后, 室温下以 $15000 \mathrm{~g}$, 离心沉淀树脂 $1 \mathrm{~min}$ 。如果有必要, 在 SDS-PAGE 分析前样品置于冰上保存。所有样品上样前 $85^{\circ} \mathrm{C}$ 重新稍作加热。
11. 利用 SDS-PAGE 分析可溶性部分、不可溶解部分，未结合部分，漂洗部分和结合部分。在用考马斯亮蓝染色后，应该在样品的结合部分中和阳性对照中观察到预期大小的主要条带。聚集的或者不可溶性蛋白（如在包含体中的蛋白质）将会出现在不可溶解部分中。

![](images/page_172_image_18.jpg)

## 疑难解答

目前大多数细菌表达载体包括一个高效的 Shine-Dalgarno 序列（Shine and Dalgarno 1974）使核糖体与 mRNA 结合，此外还包括一个强细菌启动子。有几个因素可能会降低目标蛋白的表达（综述见 Berrow et al. 2006；更多信息见 pET 系统手册，Merck Technical Bulletin #TB055）。

除了下面给出的一些特殊问题的指导方法外，在不同培养基中，表达水平可能存在差异。LB 培养基可以用来确定上述的主要表达参数，但是，为了优化表达，或者在 LB 培养基中没有表达或表达极低时，也可以尝试使用其他的培养基。这包括基本盐培养基，如 M9，确定成分培养基如诱导培养基，以及其他营养丰富的培养基，如 Terrific Broth、YT、NZCYM。

问题（步骤 11）:目的蛋白为包含体蛋白。

解决方案:在大肠杆菌中，蛋白表达过程可能会在细胞质中形成不溶解的聚集物。尽管可以依据方案7纯化这些包含体蛋白，但是以活性和正确折叠形式蛋白回收这些蛋白质常常很困难。

- 在某些情况下，蛋白质的错误折叠与过量表达引起的局部浓度过高或者分子伴侣被饱和有关。在这些情况中，降低蛋白质产出速率能够增加可溶性的活性蛋白表达量。这可以通过在诱导过程中降低细胞培养温度来实现，例如，降低至 $30^{\circ}\mathrm{C}$ 诱导 $2\sim 4\mathrm{h}$，或者降低至室温，或者更低温度下过夜诱导。也可以降低IPTG浓度，尤其是当lacY1缺失突变体如Tuner（Merck）作为宿主菌时。
- 运用具有相容的复制起始点载体共表达分子伴侣也有助于目标蛋白的折叠（Tresaugues et al. 2004）。融合可溶性标签（如下所述）也可能降低包含体的形成。
- 通常，包含体的形成是因为缺乏二硫键、辅因子，如血红素，或者是由于缺乏对于外源蛋白折叠必需的翻译后修饰造成的。尽管大肠杆菌胞内蛋白一般不形成二硫键，但 $trxB/gor$ 突变体（如 Origami, Merck Biosciences 的 Rosetta-gami）作为宿主菌时，其具有的胞内氧化环境会促进二硫键的形成。
- 可以选择的是，通过融合一段信号肽，目标蛋白可以输出至周质的氧化环境中。此外，pET-39b 或 pET-40b 载体中，目标蛋白可与 DsbA 酶或 DsbC 分子伴侣形成融合形式，从而促进在周质中二硫键的形成（Bardwell et al. 1991; Missiakas et al. 1994）。
- 在某些情况下, 当与适合的转运受体共表达, 诱导时可在生长培养基中添加辅因子, 如血红素。
- 与合适的酶共表达，也可以实现某些翻译后修饰如磷酸化修饰（如 Yue et al. 2000）。对于复杂的修饰，如糖基化修饰，昆虫（方案 2）或者酵母（方案 3）宿主可以生产适当的折叠蛋白，尽管需要用哺乳动物表达系统来实现哺乳动物蛋白真实的糖基化修饰。

问题（步骤11）:蛋白质溶解度低。在其他一些情况下，蛋白质折叠了但在裂解缓冲液中溶解度低。

## 解决方案:

- 改变裂解缓冲液的成分可能会改善蛋白质的回收，如通过增加盐浓度，包括添加低浓度的非离子化去污剂（如 0.1%～2%聚乙二醇苯基醚 Igepal CA-630），或者改变纯化方法中的 pH。
- 蛋白质等电点（pI，蛋白质表面所带电荷数为零时的 pH）可能提供裂解缓冲液是否需要优化的依据。几种在线工具可以用来计算理论等电点（http://ca.expasy.org/tools/pi\_tool.html），但也应谨记实际的等电点取决于带电基团所处的环境。对于中性蛋白质，通过保证 pH 偏离 pI 至少一个单位可能提高溶解度（限定在蛋白质化学稳定性范围之内，pH 5～9）。
- 表达带有融合标签的目标蛋白可以提高蛋白质的可溶性，减少包含体的形成（见Esposito and Chatterjee 2006; Panavas et al. 2009 综述）。通常用于提高蛋白质溶解度的标签包括 NusA、硫氧还蛋白 thioredoxin, Sumo 和用于亲和层析纯化的较大的标签（如 MBP、GST）。包含这些标签的载体是可以购买得到的（见导言中的表 19-2）。在某些情况下，可溶性标签被认为在增强蛋白质折叠中发挥作用（Englander et al. 2007）。但有时，高度可溶性标签只不过“运载”融合的目标蛋白进入溶液中，结果在标签去除后，目的蛋白依然为相对不可溶性和失活状态（Hammarstrom et al. 2006）。在这些案例中，可能需要研究其他的表达方法以改善折叠效率。

问题（步骤 11）:靶基因的编码序列在选择的表达系统中没有被优化，结果导致低表达或者截短的表达蛋白产物。大肠杆菌 tRNA 群中缺乏个别简并密码子。

## 解决方案:

- 当这些稀有密码子出现在外源基因中，表达水平可能低且出现截短的产物。例如，在一些案例中，稀有精氨酸密码子 AGA 和 AGG 接近靶基因氨基端，能极大地降低蛋白质产量（Brinkmann et al. 1989; Schenk et al. 1995）。能够表达稀有 tRNA 的相容性质粒的大肠杆菌菌株是可以购买到的。特别是来自 Merck 的 Rosetta2 和相关的变异体补充了 AUA、AGG、AGA、CUA、CCC、GGA 和 CGG 密码子。可选择的是，密码子优化的靶基因能够从一些基因合成公司购买（如 GeneArt, http://www.geneart.com; 或 GenScript, http://www.genscript.com），或者仅有少数密码子是稀有的，则可通过定点突变构建。
- 在某些情况下，转录物含二级结构会抑制翻译。可以使用二级结构预测服务器，如RNAfold分析加上目标基因5'区表达载体的转录区（http://rna.tbi.univie.ac.at/cgi-bin/RNAfold.cgi）（Gruber et al. 2008）或者Mfold（http://mfold.bioinfo.rpi.edu/cgi-bin/rna-form1.cgi）（Mathews et al. 1999; Zuker 2003）。如果观察到大范围的二级结构，尤其是遮蔽了ATG起始密码子，那么可运用定点突变来改变编码序列以改善表达。

问题（步骤 5）:因为基因产物毒性或者质粒不稳定引起的生长缓慢和（或）宿主细胞死亡。

解决方案:有毒性的基因产物会造成质粒的不稳定或者宿主细胞死亡。其中一个征兆就是生长缓慢，这在一定程度上取决于基因产物的毒性程度。

\- 当氨苄青霉素作为抗生素使用时，生长可能先变慢，然后加速。带着毒性基因并使用氨苄青霉素可能是有问题的，因为β-内酰胺酶抗性酶被分泌至培养基中，而它分解氨苄青霉素。此外，氨苄青霉素在高密度大肠杆菌培养物的低pH环境中还会被酸水解。一旦氨苄青霉素的浓度降低超过一定的阈值，这将允许丢失质粒的细胞在培养基中过度生长。可能解决的方法是用更为稳定的羧苄西林或者替卡西林来替代，或者转变载体使其含有卡那霉素抗性。

\- 为阻止毒性基因的表达，靶基因的合成应当被抑制直至大肠杆菌达到足够的细胞密度。当运用pET系统的T7-lac启动子，一般策略是使用具有共表达T7溶菌酶的相容载体的宿主菌。T7溶菌酶能够抑制在诱导前渗漏表达而出现的T7RNA聚合酶。pLysS菌株表达适量的T7溶菌酶，而pLysE菌株表达高水平的T7溶菌酶，这更适合于强毒性基因的表达。因为T7RNA聚合酶在溶菌酶的抑制作用被克服前必须实现相对高水平的表达，所以这些菌株在诱导和表达之间的滞留时间就会增加。此外，BL21(DE3)标准株已经衍生出能够更加耐受毒性基因的宿主菌株，包括C41(DE3)、C43(DE3)、C41(DE3)pLysS或C43(DE3)pLysS(Lucigen)。在非常极端的案例中，pET 载体在完全缺失 T7 RNA 聚合酶的菌株中，能够被感染的  $\lambda$  或者 M13 噬菌体衍生物所诱导（Unnithan et al. 1990; Komai et al. 1997）。

- pET 载体的 T7-lac 启动子具有 cAMP 激活蛋白（CAP）调控的位点，其在葡萄糖缺乏时被激活。生长培养基中加入 2% 葡萄糖（可用高压灭菌的 40% 葡萄糖储存液），可在诱导之前减少在 T7-lac 启动子下的毒性基因漏表达。另外一个运用 pET 系统减少毒性基因表达的方法是，使用极低拷贝数的载体，如 pETcoco（Merck）。与其他 pET 载体类似，pETcoco 载体也是通过添加 IPTG 诱导目的基因表达的，但是在诱导之前可使用阿拉伯糖实现质粒扩增。
- 关于其他的毒性基因表达方法，包括竞争性和反向启动子参见 Saida（2007）的讨论。

问题（步骤 11）:出现截短表达产物。

解决方案:表达蛋白中出现变短的目标蛋白可能有以下几个原因。

- 尽管常用的 BL21 宿主菌是 lon 和 ompT 蛋白酶基因缺失的，但是待纯化蛋白在细胞裂解前后仍会发生降解。这些降解可以通过比较用 SDS-PAGE 上样缓冲液加热处理的全细胞和细胞裂解物的 Western 杂交加以辨别。
- 细胞裂解之前的蛋白产物降解反映了其对宿主细胞的毒性，可以利用上面提到的措施加以改善。细胞裂解时应当添加蛋白酶抑制剂（1mmol/L PMSF，1～5mmol/L EDTA，1～5mmol/L EGTA，1～20mmol/L 苯甲醚，1～10μg/mL 亮抑酶肽，5μg/mL 胃酶抑素 A，1～10μg/mL 抑肽酶，1～20mmol/L tosyl-lysine-chloromethyl ketone，等等），还应当如方案 4 中所述保持细胞裂解物低温。
- 另外一种截短蛋白出现的可能是在靶基因内存在第二个翻译起始点（Preibisch et al. 1988）。当有一个序列与翻译起始密码子 ATG（Met）上游 5～13 核苷酸处的 Shine-Dalgarno 核糖体结合位点（AGGAGGU）类似时，这种现象就会发生。一种可行的方法是，在靶蛋白 N 端和 C 端加入不同的亲和标签，这样在第一步中分离具有同一氨基端的蛋白质，然后在第二步亲和层析中纯化具有同一羧基端的蛋白质。

问题（步骤 11）:mRNA 或者蛋白质不稳定，导致表达水平低。

## 解决方案:

- 在某些情况下，外源 mRNA 或者蛋白质有可能不稳定，在宿主细胞中很快被降解。在插入的 DNA 下游加入能够稳定 mRNA 的序列，或者改善翻译效率（如转录终止子，或者 RNase III 位点）也能增加表达（Panayotatos and Truong 1981；Studier and Moffatt 1986；Rosenberg et al. 1987）。
- 表达蛋白的倒数第二位氨基酸可能会造成蛋白质的降解。如果蛋白质的倒数第二位氨基酸含有大量的疏水侧链，如亮氨酸或异亮氨酸，那么氨基端的甲酰甲硫氨酸就会被氨肽酶切除（Hirel et al. 1989; Lathrop et al. 1992）。当残留的氨基端的氨基酸恰好是亮氨酸，那么残余蛋白的半衰期仅约 $2\mathrm{min}$ （Tobias et al. 1991）。因此，当目标基因中插入天然甲硫氨酸Met作为翻译起始点时，要注意蛋白质序列的第二个氨基酸不是亮氨酸。
- 一些经特殊设计以消弱 mRNA 前体降解的商业化的细胞系也可用于增加整体信息的稳定性。例如，BL21Star（Life Technologies 公司）包含一个编码 RNase E（me131）基因的突变，它可以增加 T7 启动子类载体的 mRNA 转录稳定性，提高蛋白质表达产量。如果 mRNA 的稳定性似乎是一个问题的话，那么运用这个表达菌株，或者类似的菌株，是有可能提高表达产量的。