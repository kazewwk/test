# Chapter 7. Applications of Designed Biological Systems

原始 PDF 第 124–133 页。

# CHAPTER 7

# Applications of Designed Biological Systems

## 7.1 Introduction

Biological systems surround and pervade every aspect of human existence. It is no surprise that the use of synthetic biology to design living systems will find numerous application areas with significant impact on society. In this chapter we highlight current areas of research on real-world applications, and suggest future areas of investigation.

The use of biological technologies for useful purposes dates back to the emergence of human civilisation itself. For example, humans have used yeast to ferment beer and wine for thousands of years. Today biological technologies are found throughout diverse areas of industry. Synthetic biology promises to accelerate the development of optimised and novel biotechnologies that will be integrated in many aspects of industry and life.

## 7.2 The Potential for Developing Applications of Synthetic Biology

It is often stated that the whole purpose of synthetic biology is to produce applications or products. A recent report (BCCC research BIO066A, published in June 2009) on the commercial potential of synthetic biology forecasts that the expected market for synthetic biology in 2013 would exceed \$2.4 billion. Of this, the chemicals and energy sector is the largest share with a predicted market value of \$1.6 billion, followed by the biotechnology and pharmaceuticals sector with a market share of \$0.6 billion. Growth rates are predicted to be 81% and 49% in these areas, respectively. For this reason a number of major industrial corporations are keenly interested in synthetic biology and what it has to offer.

There are also a host of other reasons for the growing interest in synthetic biology. Because devices can be designed for a specific task or application, unlike naturally occurring organisms that may have many functions, they should, as a technology, function more reliably than non-designed systems and can be optimised for the desired application. In addition, the use and reuse of a set of parts means the cost of characterising sub-assemblies can be shared over a number of products, and will thus be lower than dedicated organisms. Finally, interfaces on both the output and input side can be designed to integrate with existing systems, such as optical sensors and CCD cameras, thus permitting conventional instrumentation to be used rather than biological assays.

109

---

110

Synthetic Biology — A Primer

## 7.3 Criteria for Developing Applications in Synthetic Biology

Synthetic biology devices are not suitable for all applications, and it is possible to define some criteria for areas where they will be most suitable for commercial development. First, the application area must be sufficiently homogenous to permit one design to work in a wide range of situations. Thus, for example, chemical synthesis is a suitable area, whilst personalised medicine is less suitable because the latter would require a bespoke device for each person. Second, the application area must have a sufficiently large volume to justify the cost of development. Third, the environment that the synthetic system is used in must be compatible with the chassis in which it has been implemented. This is true of most biologically-based processes and should be considered as one of the initial specifications in the design. For example, since many reactions are exothermic, this has led to interest in thermophilic organisms that can withstand the higher temperatures found in fermentation and other process chambers, which is considered preferable to the other option of actively cooling the chamber, since cooling is costly, inefficient and slows down reaction rates. Fourth, the intended application should ideally be constrained to avoid contamination of the synthetic system by external agents, or migration of the system outside the planned sphere of influence. For this reason, industrial biotechnology applications, which constrain the use of the synthetic biological system to inside a reaction vessel, are ideal. Other methods of constraint include adhesion to a surface, particularly suitable for sensor systems. The danger of accidental release of the synthetic system into unintended areas can be minimised through the use of ‘kill’ or fail-safe switches and/or the use of non-living, abiotic chassis which are unable to grow and replicate.

A final consideration in selecting suitable applications for the commercialisation of synthetic biology is public acceptance or at least the absence of public opposition. Some of the factors surrounding this are covered in Chapter 9 and include considerations of public benefit, potential risk and likelihood of direct exposure to the synthetic biological system.

## 7.4 Commercial and Practical Challengest in Application Development

Even if an application is suitable for the use of synthetic biology devices, there are a number of challenges to overcome before it can be implemented. These challenges include competition from existing processes which will be associated with significant pressures to remain in place in the form of previous investment in development and infrastructure. For this reason, synthetic biology approaches to pharmaceutical synthesis will have a harder time replacing existing synthesis routes, however inefficient these may be, as there is not the cost pressure to change. On the other hand, applications in the synthesis of new chemical entities, areas such as biosensors, where there are not chemical or electronic sensors readily available, or in biofuels, where the volumes are such that small improvements in efficiency can have significant cost advantages, will provide a ready area for synthetic biology applications.

Another challenge to be met is the need for robust and efficient scale-up. Most synthetic biology systems are initially developed in a laboratory environment using basic equipment such as shake flasks or 96 well plates at volumes of the order of a few litres or less. These

---

Applications of Designed Biological Systems

111

processes must then be transferred first to bench scale reactors and then to pilot plants and industrial scale production, possibly up to tens of thousands of litres per day. Whilst this process occurs regularly in chemical engineering, it is by no means an easy one, often requiring the re-optimisation of experimental conditions at different scales. The cost of this scale-up is part of the investment required to commercialise synthetic biology applications. Fortunately, there are successful examples of how this can be achieved. For example, the biotechnology company Amyris has successfully brought processes for the production of artemisinin and biofuels to an industrial scale. It is important to note that the synthetic biology product must be made in sufficient quantity to meet the whole market, otherwise the market will not be able to rely on the product and will use non-synthetic biology alternatives, eventually eroding the market for the synthetic biology product.

One very pertinent current challenge is the need for validation. In the early years, while synthetic biology is being developed, there is an absence of reliable characterisation data for parts and sub-assemblies, meaning that in early applications, developers will need to perform their own characterisation and absorb the cost that entails. As the field progresses, however, the development of an infrastructure of datasheets for biological parts and chassis will accelerate the commercial development of synthetic systems as lower cost re-use of parts and their associated validation data will be possible.

The presence of a distribution network to transport the product from the factory to the user can also be considered as a potential hurdle. If the synthetic biology product is a living organism, then the environmental constraints for transport and storage will be more demanding than for electronic or chemical products, although not dissimilar to those of packaged sterile medical devices. If the product is a chemical produced by synthetic organisms in the factory, then the compatibility of the synthetic biology-produced chemical with existing distribution networks will aid its substitution. This is a big consideration for potential products such as biofuels, where there is a significant premium for the synthetic biology product to be compatible with existing hydrocarbon fuel stocks. In addition, if the product for distribution is a living synthetic organism, then it must be recognised that public attitudes to risk may demand a greater degree of control over the organism. To this end, a number of groups have introduced parts that stop cell reproduction or can be triggered to cause cell destruction. In summary, activities to overcome these challenges are expected to be a significant element of the continuing development of synthetic biology products and applications in future years. The remainder of this chapter gives details of a number of potential future applications of synthetic biology.

## 7.5 Constructing Microbial Cell Factories

Living systems, from single-celled microbes to complex multicellular organisms, are able to transform simple compounds and nutrients into complex chemicals, materials and structures from the nanoscale to the macroscale. Biological engineers have only just begun to harness natural diversity to produce valuable compounds. The concept of a microbial cell as a ‘factory’ is a useful concept to encapsulate ideas around engineering life as a production

---

112

Synthetic Biology — A Primer

platform. For example, much like a factory, cells are able to take material and energy inputs (for example, glucose) and transform them in a step-wise manner to higher value materials. In this analogy enzymes represent the machines in the factory that process and assemble raw materials into finished goods. Microbial cells have been used as factories to produce a wide spectrum of value-added products.

A number of valuable compounds, from small molecules to proteins, are produced by organisms found in nature. However, these are often made by organisms that are not amenable to large-scale industrial growth and production, and are often produced at low yields. To circumvent these issues, bioengineers will express metabolic pathways or proteins in a heterologous host. These hosts include the baker’s yeast Saccharomyces cerevisiae, the model gram negative bacterium Escherichia coli and model mammalian cell lines such as Chinese hamster ovary cells. These production hosts are able to grow rapidly and to high density in fermenters and are genetically tractable. In addition to producing naturally occurring products in heterologous organisms, synthetic biologists are designing cells to produce chemicals, materials and proteins with no natural analogues. This is an example of using biological systems to produce completely synthetic compounds.

## 7.5.1 Protein products

One of the first uses of microbial cells as production platforms was the heterologous production of insulin in E. coli in 1977. The vast majority of human insulin on the market is now produced by bacteria. Protein-based therapeutics (known as biologics in the pharmaceutical industry) is a rapidly growing area of the industry’s portfolio of products that have been approved for the treatment of cancers, inflammatory diseases and cardiovascular disease. In addition to therapeutic proteins, the production of enzymes is an important focus of several industries. These industrial enzymes include proteases, amylases and lipases for food and animal feed processing.

A key step in biologics and protein manufacturing is the production of full-length, functional proteins with high yields in a controlled fermentation process. Proteins are post-translationally modified in many organisms, but the nature and abundance of these modifications differs greatly between organisms. These modifications are important for protein function, and can be complex to implement, so developing production microbes that are able to make the modifications correctly for a given application is a key challenge. The incorporation of synthetic genetic circuits to sense fermenter conditions and control cell growth and metabolism may have significant impact on biologics and enzyme manufacturing. For example, genetically encoded sensors of dissolved oxygen or pH could control the expression of genes involved in central metabolism, rerouting carbon flow to avoid excessive acidification of the process.

## 7.5.2 Fuels

The derivation of liquid transportation fuels from petroleum is one of the most pressing challenges society faces today. Concerns over climate change, limited supplies and the geopolitical costs of oil extraction have driven the search for technologies to transform

---

Applications of Designed Biological Systems

113

renewable biomass into fuels. Many organisms, notably baker’s yeast, are able to ferment sugars into ethanol and do so with high productivities. The fermentation of corn sugars to ethanol is currently used to supplement gasoline. However, ethanol has a relatively low energy density and is hygroscopic (takes up water), which presents problems in its distribution and use.

Synthetic biology offers the chance to reprogram organisms to make natural or non-natural compounds which have more favourable fuel characteristics. Recent work has increased the yields of naturally produced compounds such as butanol, but also shown that non-natural fuel compounds can be produced biologically using non-natural combinations of enzymes. These include long-chain diesel-like compounds, short-chain petroleum-like compounds, and gaseous propane.

## 7.5.3 Commodity chemicals

In addition to liquid transportation fuels, there is a demand for renewable sources of commodity chemicals. Commodity chemicals are broadly defined as low molecular weight precursors of high value industrial chemicals. These are also known as ‘platform chemicals’, because they provide a common set of building blocks that the chemical industry can use to produce a diverse range of valuable products. Examples include ethylene, propylene and butadiene, which are produced in millions of tons per year to synthesise plastics, resins and other materials.

There have been several synthetic approaches to producing commodity chemicals from renewable biomass. DuPont has commercialised a genetically modified E. coli that produces 1,3-propanediol (1,3-PDO) from corn syrup. 1,3-PDO is used to make polyesters, composites, laminates and coatings. The biological process uses a renewable carbon source and uses 40% less energy than the conventional process. Synthetic biological routes to valuable compounds often have advantages in process energy costs, due to the fact that biological systems (enzymes and metabolic processes) operate close to room temperature and at standard pressure.

## 7.5.4 Materials

Many protein-based biological materials have physical properties that exceed even the most high performance man-made polymers. Some of the most well-known examples are spider silks. Spider silks are made from proteins containing highly repetitive proline-rich helical domains. Silks are able to stretch to many times their length without failure and have tensile strengths exceeding that of Kevlar®. Due to the difficulties in farming and harvesting silk protein from spiders, there is significant interest in producing silks in microbial cells. This presents particular challenges: highly repetitive proteins often express poorly in recombinant hosts due to inefficient codon usage. To solve this, several researchers have used chemical gene synthesis to construct synthetic spider silk genes for expression in bacteria. These genes have identical amino acid sequences to native spider silks, but are computationally codon-optimised for production in fast-growing microbes such as E. coli. The ‘recoding

---

114

Synthetic Biology — A Primer

and chemical synthesis of genes is a way to eliminate the need to extract DNA from a source organism and is a strategy to circumvent difficulties in heterologous expression as well.

## 7.5.5 Specialty chemicals and drugs

Living systems produce a number of highly complex chemical structures, especially through secondary metabolism. For example, plants produce a wide range of structures with multiple chiral centres that are involved in chemical defence of the organism. Many of these natural products are bioactive in humans or are able to kill microorganisms and thus have therapeutic value. In fact, over half of all pharmaceuticals on the market are based on natural compounds. It is no wonder that synthetic biologists would seek to construct organisms to overproduce these valuable and often life-saving products.

Several groups have engineered microbes to produce fine chemicals for therapeutic purposes. Saccharomyces cerevisiae has been engineered to produce artemisinic acid, a precursor to artemisinin, a potent anti-malarial naturally found in the plant Artemisia annua. Currently, the chemical synthesis of artemisinin is cost prohibitive to the population of the Third World, where it is needed most. The researchers were able to use an engineered mevalonate pathway, an amorphadiene synthase and a cytochrome P450 monooxygenase from A. annua to produce artemisinic acid. The engineered yeast produced higher artemisinin yields than A. annua itself, although industrial scale-up and optimisation was required to make this route to production cost effective (see above).

## 7.6 Medical and Health Applications

One of the primary reasons for society to become proficient in engineering biological systems is for enhancing human health and well-being. The healthcare industry is one of the largest markets in the world, and directly impacts quality of life. As discussed above, synthetic biologists are working to engineer cells as factories to produce affordable drugs, protein therapeutics and enhanced materials. There are significant efforts in interfacing synthetic biological systems directly with patients to improve diagnosis, prevention and treatment of diseases and disorders.

## 7.6.1 Biosensors

The molecular and cellular processes in living organisms rely on the specific recognition of molecules, ranging from small metabolites to nucleic acids, lipids and proteins. This recognition can be exploited to sense, detect and measure biomolecules in a research, clinical or field setting and has been heavily exploited by the biotechnology industry. For example, antibody-based assays for biomolecules (such as the ELISA assay) are widespread and commercially available.

Synthetic biologists aim to make the design of biosensing materials and organisms rapid and amenable to forward design. Analytical devices capable of measuring biomolecular species in patients are invaluable in characterising normal and pathological processes and

---

Applications of Designed Biological Systems

115

to alert clinicians to appropriate medical treatment. The most widespread and developed example is the blood glucose sensors, which are used by millions of people daily. However, these technologies are limited to the detection of one compound (glucose) and cannot be tailored to sense other biomolecules. The generation of biosensors remains very much a research project, where significant amounts of resources are required to develop unique solutions for each compound one desires to detect. Given the explosion in biomolecular data from laboratory and clinical studies, the lack of a platform for tailoring biomolecular detection is a fundamental bottleneck to the era of personalised medicine. A detection platform that could be rapidly tailored for nucleic acids or proteins would enable clinicians to take advantage of the wealth of genomic and proteomic data available.

## 7.6.2 Smart therapeutics

In addition to engineering microbes to produce therapeutics, several groups are exploring the use of live cells as therapeutics. Microbes in their natural state are endowed with many functions that could be utilised to discriminate between healthy and disease states (such as receptors and environmental sensing components) and act in a therapeutic manner (such as synthesising therapeutic proteins, invading diseased cells or synthesising chemicals, as above). Towards these aims, E. coli has been engineered to sense and destroy cancer cells by environment-dependent control of invasion. Invasin from the pathogen Yersinia pseudotuberculosis was used as an output that allowed E. coli to invade mammalian cells. To render the bacteria cancer cell-specific, invasin expression was controlled by several heterologous sensors: the Vibrio fisheri quorum-sensing circuit, the hypoxia responsive promoter or the arabinose- responsive promoter. Each of these is designed to induce invasin expression and bacterial invasion only in the presence of tumour cell environments. These engineered bacteria were shown to successfully invade several cancer-derived cell lines, demonstrating that cells can be programmed with sensors and outputs to achieve therapeutic functionality. Alternative approaches to develop tumour-targeting bacteria are also being investigated using Clostridium, anaerobic bacteria which can grow in low-oxygen tumour cores but not in oxygenated healthy tissues. These bacteria have been engineered to sensitise tumours to chemotherapy, and shown to cause regression and cure of tumours in mice.

## 7.6.3 Tissue engineering and patterning

The coordinated organisation of cells in specific patterns is a classic example of complex function in many organisms and is central to the development of multicellular organisms from a single fertilised oocyte. Pattern formation typically involves signalling and communication between cells, processing of these signals and modulation of the expression of a variety of genes. The ability to design pattern formation will hold great utility in applications such as tissue engineering and biomaterials. Towards these aims, several groups have explored how collections of cells can be programmed to form user-specified patterns.

‘Traditional’ tissue engineering has focused on the development of three-dimensional extracellular scaffolds to direct the differentiation and patterning of cells into functioning

---

116

Synthetic Biology — A Primer

tissues. A synthetic biology approach would also include the ‘bottom-up’ patterning of cell fate and position. In one example, researchers enabled E. coli cells to communicate with each other using the quorum-sensing system from Vibrio cholerae. Engineered ‘receiver cells were designed to express fluorescent proteins based on the concentration of the signalling molecule synthesised by a ‘sender’cell. The receiver cells were designed such that they were responsive only to a defined range of signalling molecules, analogous to a bandpass filter. The range of signalling molecules the receiver cells was responsive to was tuned by changing the kinetic parameters of the underlying information processing circuit. Combinations of sender and receiver cells can be used to create two-dimensional patterns on a lawn of cells such as a bullseye, ellipses and clovers. Thus, the engineering of underlying functionality (i.e. quorum sensing) and gene circuits allowed spontaneous pattern formation in a population of cells.

Other approaches have been used to programme pattern formations that are inspired more by lithographic and printing techniques than developmental pattern formation. In a stunning example of engineering synthetic functions into organisms, a strain of bacteria that can sense red light and control gene expression was constructed. To accomplish this, the researchers constructed a chimeric two-component photorhodopsin system from the cyanobacteria Synechocystis in E. coli. When coupled to the expression of a chemical output, this function allowed a lawn of bacteria to act as a photographic film — projection of an image onto the lawn results in the recording of a high-definition two-dimensional chemical image at resolutions up to 100 megapixels per square inch. The control of pattern formation in living cells will have important applications in constructing complex patterned biomaterials, tissue engineering and parallel biological computation. In an extension of this work, synthetic biologists have enabled massively parallel ‘edge detection’ of a projected image such that cells communicate to discriminate and delineate boundaries between cells sensing light and dark regions of the image. These efforts hold great potential to explore how biology uses large numbers of computational elements (in this case cells) to compute complex problems and to combine ‘top-down’ lithographic-style patterning with ‘bottom-up’ parallel computation to specify patterns. This work was initiated as part of the International Genetically Engineered Machine (iGEM) student competition and is discussed further in Chapter 8.

## 7.7 Synthetic Biology for a Sustainable World

Living systems have evolved to gather resources from their environment for survival and replication. In doing so, they often drastically change the local or global environment. The ability of organisms to alter the environment and act ‘beyond the bioreactor’ is a frontier area of research in synthetic biology, but holds immense promise for tackling problems in sustainability.

## 7.7.1 Bioremediation

Bioremediation is the use of natural and engineered organisms to remove pollution from contaminated environments. This is usually accomplished by microbes that are able to mineralise (oxidise completely to $\mathrm { C O } _ { 2 } )$ contaminating compounds. Although a number of

---

Applications of Designed Biological Systems

117

bacteria have been identified that can degrade a wide variety of toxins and xenobiotics, Pseudomonas species have been the most intensively studied. One of the major bottlenecks to widespread adoption of bioremediation is a lack of understanding of microbial physiology and microbial community diversity in the field. Because of this, synthetic organisms engineered for purpose may be a useful approach to remediation. A future vision of bioremediation is to develop synthetic organisms that could persist in the environment, monitor their surroundings for toxins and pollutants and execute a programme of remedial steps. These synthetic organisms would act as persistent ‘sentinels’ in the environment but would clearly need to be considered in terms of public acceptance.

## 7.7.2 Biomining

The extraction of metals from ores is a major economic activity in virtually all parts of the world. The involvement of microbes in metal extraction (known as biomining) has a long history, although early miners likely did not know microbes were participating in the liberation of metals from ores. In modern biomining, acidophilic bacteria are used to solubilise metal sulphides or metal oxides by providing sulphuric acid, or to provide a pretreatment to break down the structure of ores such that chemical leaching can take place. So far, there have been few efforts in engineering biomining organisms for enhanced metal leaching, making this an area ripe for synthetic biology approaches.

## 7.7.3 Engineering crops and commensal soil organisms

One of the major problems facing society today is the availability of food, especially given projections of a rapidly growing global population, climate change and destruction of arable land worldwide. One of the frontiers of synthetic biology is the design and engineering of crops able to survive drought, high salinity soil and heavy metal exposure while producing high yields of safe produce. This vision would be a dramatic extension of the technology in genetically modified crops found today. Another possible route is the engineering of microbial commensal organisms in the soil of farmland to increase nutrient availability and cycling. For example, recent progress in this area has shown that refactoring and systematic re-design of a complex nitrogenase gene cluster allows it to be successfully re-implemented in another microbe. This paves the way to future engineered microbes that could supply nitrogen to cereal crops, providing a sustainable alternative to supplying nitrogen using chemical fertilisers. The development of these types of technologies will have to be closely integrated with local community needs within a regulatory framework.

## Reading

- Alper, H and Stephanopoulos, G. (2009). Engineering for biofuels: exploiting innate microbial capacity or importing biosynthetic potential? Nat Rev Microbiol 7(10): 715–723.
- Anderson, JC, Clarke, EJ, Arkin, AP, et al. (2006). Environmentally controlled invasion of cancer cells by engineered bacteria. J Mol Biol 355(4): 619–627.
- Bayer, TS. (2010). Transforming biosynthesis into an information science. Nat Chem Biol 6(12): 859–861.

---

118

Synthetic Biology — A Primer

- BCC Research: Synthetic Biology: Emerging Global Markets. Available at: http://www.bccresearch.com/report/BIO066A.html [Accessed 6 September 2011].
- Chang, MCY, Eachus, RA, Trieu, W, et al. (2007). Engineering Escherichia coli for production of functionalized terpenoids using plant P450s. Nat Chem Biol 3(5): 274–277.
- Chang, MCY and Keasling, JD. (2006). Production of isoprenoid pharmaceuticals by engineered microbes. Nat Chem Biol 2(12): 674–681.
- Choi, YJ and Lee, SY (2013). Microbial production of short-chain alkanes. Nature 502(7472): 571–574.
- Ferrer-Miralles, N, Domingo-Espin, J, Corchero, JL, et al. (2009). Microbial factories for recombinant pharmaceuticals. Microb Cell Fact 8(17). Available at: http://www.microbialcellfactories.com/content/pdf/1475-2859-8-17.pdf [Accessed 24 July 2015].
- Heap, JT, Theys, J, Ehsaan, M, et al. (2014). Spores of Clostridium engineered for clinical efficacy and safety cause regression and cure of tumours in vivo. Oncotarget 5(7): 1761–1769.
- Howard, TP, Middlehaufe, S, Moore, K, et al. (2013). Synthesis of customized petroleum-replica fuel molecules by targeted modification of free fatty acid pools in Escherichia coli. Proc Natl Acad Sci USA 110(19): 7636–7641.
- Jang, YS, Lee, J, Park, JH, et al. (2012). Enhanced butanol production obtained by reinforcing the direct butanol-forming route in Clostridium acetobutylicum. MBio 3(5): e00314-12.
- Kallio, P, Pásztor, A, Thiel, K, et al. (2014). An engineered pathway for the biosynthesis of renewable propane. Nat Commun 5: 4731.
- Keasling, JD. (2010). Manufacturing molecules through metabolic engineering. Science 330: 1355–1358.
- Lee, SK, Chou, H, Ham, TS, et al. (2008). Metabolic engineering of microorganisms for biofuels production: from bugs to synthetic biology to fuels. Curr Opin Biotechnol 19(6): 556–563.
- Levskaya, A, Weiner, OD, Lim, WA, et al. (2009). Spatiotemporal control of cell signalling using a light-switchable protein interaction. Nature 461: 997–1001.
- Prather, KLJ and Martin, CH. (2008). De novo biosynthetic pathways: rational design of microbial chemical factories. Curr Opin Biotechnol 19(5): 468–474.
- Ro, DK, Paradise, EM, Ouellet, M, et al. (2006). Production of the antimalarial drug precursor artemisinic acid in engineered yeast. Nature 440: 940–943.
- Rude, MA and Schirmer, A. (2009). New microbial fuels: a biotech perspective. Curr Opin Microbiol 12(3): 274–281.
- Smanski, MJ, Bhatia, S, Zhao, D, et al. (2014). Functional optimisation of gene clusters by combinatorial design and assembly. Nat Biotechnol 32(212): 1241–1249.
- Steen, EJ, Kang, YS, Bokinsky, G, et al. (2010). Microbial production of fatty-acid-derived fuels and chemicals from plant biomass. Nature 463: 559–U182.
- Tabor, JJ, Levskaya,A andVoigt, CA. (2011). Multichromatic control of gene expression in Escherichia coli. J Mol Biol 405(2): 315–324.
- Temme, K, Zhao, D and Voigt, CA (2012). Refactoring the nitrogen fixation gene cluster from Klebsiella oxytoca. Prc Natl Acad Sci USA 109(18): 7085–7090.
- Topp, S and Gallivan, JP. (2007). Guiding bacteria with small molecules and RNA. J Am Chem Soc 129(21): 6807–6811.
- van der Meer, JR and Belkin, S. (2010). Where microbiology meets microengineering: design and applications of reporter bacteria. Nat Rev Microbiol 8(7): 511–522.
- Verpoorte, R, van der Heijden, R and Memelink, J. (2000). Engineering the plant cell factory for secondary metabolite production. Transgenic Res 9(4–5): 323–343.
- Widmaier, DM, Tullman-Ercek, D, Mirsky, EA, et al. (2009). Engineering the Salmonella type III secretion system to export spider silk monomers. Mol Syst Biol 5. Available at: http://www.nature.com/msb/journal/v5/n1/pdf/msb200962.pdf [Accessed 24 July 2015].
