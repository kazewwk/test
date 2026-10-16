their genome. A man-made genome is therefore the starting point for synthetic life, and the story of the first synthetic cellular genome is an excellent example that bottom-up synthetic biology is possible.

## 4.3.1 Genome synthesis

Researchers re-engineer the genomes of a variety of microbes and other cells on a daily basis in laboratories around the world. Swapping DNA parts in and out of existing genomes has been possible for decades, as has the ability to introduce large regions of new DNA into cells. At the same time that molecular biology has developed the techniques to rearrange the DNA inside cells, chemistry has become adept at synthesising new DNA sequences directly from single molecules (see Chapter 3). With the falling cost of DNA synthesis and the increasing improvements in molecular biology, it was inevitable that researchers would consider synthesising whole genomes of cells from single molecules.

The first synthetic genomes constructed were viral genomes, with the 7,500 base pair poliovirus genome synthesised in 2002, and the 5,400 base pair phi X174 phage genome synthesised in 2003. These DNA genomes were assembled in the lab from chemically synthesised DNA oligomers, using the same molecular biology technologies used in gene synthesis. Placing these DNA genomes into appropriate bacterial host cells (by transformation) leads to the production of new copies of functioning viruses, even though the initial DNA encoding the information was assembled in the lab by chemistry. Repeating this same feat, not for viruses but for cells, is a much larger task but one that has been successfully achieved by the same team involved with the minimal genome project.

To synthesise the first complete cellular genome, researchers based at the J. Craig Venter Institute (JCVI) again turned to M. genitalium. To synthesise its circular genome, its 583,000 base pairs of DNA were divided into 101 arbitrary regions, each about 6,000 base pairs long. Each region overlapped slightly with the next, meaning that they both contained a few hundred base pairs of the same DNA sequence. These 101 regions were synthesised chemically by several DNA synthesis companies and were checked by DNA sequencing. Using a cocktail of enzymes in the lab, these regions were assembled together using the overlapping sequence to define which region goes next to which. In rounds of DNA assembly, the 101 regions made 24 larger sections that were stepwise assembled into four quarter-genome pieces. These four pieces were then simultaneously inserted into yeast cells (co-transformation), which uses its own DNA repair enzymes to link overlapping DNA fragments together to form complete circular genomes. The chemically synthesised M. genitalium genome was designed to include a few extra DNA parts to allow it to be hosted in yeast cells, to be selectable using antibiotics and to replicate when yeast cells divide. This assembly and then extraction of this genome from yeast cells, revealed in 2008, resulted in the first chemically synthesised cell genome.

Unlike viral genomes, a chemically synthesised cellular genome cannot simply be added to growing bacteria to create synthetic life. The genome on its own is only a DNA instruction book and requires the enzymes and the environment of a cell to be read. In order to start synthetic life from a synthetic genome, an empty cell is required to ‘boot up’ the system. Creating these empty cells and getting a whole genome into them and working is a technical challenge in itself. It was first demonstrated in 2007, when the natural DNA genome from M. mycoides was taken from its own cell, cleaned and then used to transform M. capricolum cells. Following a complex transformation method, some M. capricolum cells were seen to change and resemble M. mycoides cells, and later these were verified to be indistinguishable from natural M. mycoides. This process of ‘genome transplantation’ was combined with the chemical genome synthesis method described above in 2010 to create the world’s first synthetic life. The JCVI research team assembled the complete 1 million base pair M. mycoides genome from synthesised DNA fragments and then used this to transform M. capricolum into M. mycoides. As well as including a few extra DNA parts to allow the genome to be hosted in yeast and selectable by antibiotics, the researchers included coded messages in the DNA sequence to act as ‘watermarks’ confirming the cells did have a man-made genome (Fig. 4.3).

![](images/page_81_image_3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Asc I"] --> B["BssH II"]
  C["701-799"] --> D["811-900"]
  E["94D"] --> F["901-1000"]
  G["601-700"] --> H["1,077,947"]
  I["501-600"] --> J["200,000"]
  K["1001-1104"] --> L["2,100"]
  M["10,080 bp cassettes (1,078) (Assemble109X)"] --> N["Yeast"]
  O["10,080 bp assemblies (109) (Assemble 11X)"] --> P["100,000 bp assemblies (11) (Assemble 1X)"]
  Q["1,077,947 bp"] --> R["1,077,947 bp"]
  S["301-400"] --> T["201-300"]
  U["21-300"] --> V["101-200"]
  W["WM3"] --> X["Asc I"]
  Y["BssH II"] --> Z["BssH II"]
  AA["BssH II"] --> AB["BssH II"]
  AC["Asc I"] --> AD["WM2"]
  AE["811-900"] --> AF["94D"]
  AG["701-799"] --> AH["811-900"]
  AI["901-1000"] --> AJ["1,077,947"]
  AK["501-600"] --> AL["800,000"]
  AM["2,100"] --> AN["400,000"]
  AO["21-300"] --> AP["600,000"]
  AQ["301-400"] --> AR["2,10,300"]
  AS["811-900"] --> AT["94D"]
  AU["701-799"] --> AV["811-900"]
  AW["601-700"] --> AX["501-600"]
  AZ["501-600"] --> BA["800,000"]
  BB["21-300"] --> BC["2,1,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99
  AC --> AD
  AE --> AF
  AF --> AG
  AH --> AI
  AI --> AJ
  AJ --> AK
  AK --> AL
  AL --> AM
  AM --> AN
  AN --> AO
  AO --> AP
  AP --> AQ
  AQ --> AR
  AR --> AS
  AS --> AT
  AT --> AU
  AU --> AV
  AV --> AW
  AW --> AX
  AX --> AY
  AY --> AB
  AB --> AC
  AC --> AD
  AD --> AE
  AE --> AF
  AF --> AG
  AG --> AH
  AH --> AI
  AI --> AJ
  AJ --> AK
  AK --> AL
  AL --> AM
  AM --> AN
  AN --> AO
  AO --> AP
  AP --> AQ
  AQ --> AR
  AR --> AS
  AS --> AT
  AT --> AU
  AU --> AV
  AV --> AW
  AW --> AX
  AX --> AY
  AY --> AB
  AB --> AC
  AY --> AD
  AD --> AE
  AE --> AF
  AF --> AG
  AG --> AH
  AH --> AI
  AI --> AJ
  AJ --> AK
  AK --> AL
  AL --> AM
  AM --> AN
  AN --> AO
  AO --> AP
  AP --> AQ
  AQ --> AR
  AR --> AS
  AS --> AT
  AT --> AU
  AU --> AV
  AV --> AW
  AY -.->|bp=2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+2x+<nl>
```
</details>

Fig. 4.3 Construction of a synthetic M. mycoides genome. The outer circle represents the 1 million base pair circular DNA genome. The genome has been edited in a number of places to include watermarks (WM). (Courtesy: Science, 2 July 2010, 329(5987): 52–56. Reproduced with permission.)

## 4.3.2 Designer cells

Synthetic life means more than just the chemical synthesis of existing bacterial genomes; it opens up the possibility of creating whole new organisms containing genomes never before seen in nature. While researchers have already shown that a synthetic genome containing a few extra DNA parts and watermark sequences can become the genome of a Mycoplasma cell, the next step for synthetic life is to produce cells with tailor-made genomes. An early target for such a ‘designer’ cell is the theoretical M. laboratorium from the minimal genome project described above. Synthesis of a Mycoplasma containing this reduced genome will give a new minimal cell and greatly improve our understanding of what is required for cellular life. If the synthesis and construction of the genome is done using a rational partsbased approach, it should be easy to remove genes further from this cell or to add new ones as needed. The cell and its genome would be an ideal chassis for synthetic biology as its reduced number of genes would mean less complexity and would be, therefore, more straightforward to mathematically model and simulate. To such a chassis it could be possible to predictably add many new genes, such as pathway genes that direct the resources of the cell into the production of fuel compounds. With the technology of complete genome synthesis, these new functions could be written into the genome of the cell and designed from the bottom up.

The rational engineering approach of synthetic biology and the ability to have customised cell chassis fit hand-in-hand. From these the logical future is designer cells, synthesised or modified to have the necessary attributes for specialised functions. While the early achievements in this field have been with Mycoplasma bacteria, the methods should be applicable to a range of bacteria and other microbes like yeast. Indeed, genome engineering has already been used to produce the world’s first Genomically Recoded Organism (GRO); an E. coli cell that does not recognise TAG as a stop codon. This novel strain provides a chassis for programming nonstandard amino acids to be added to proteins, allowing researchers to go beyond the central dogma and develop enzymes made from 21 amino acids, not just the standard 20. This will also be possible in yeast in the future, as an ambitious genome synthesis project, Sc2.0, is underway to construct a recoded synthetic version of the 11 million bp S. cerevisiae genome with many sequence changes that will benefit research and biotechnology. One of the 16 chromosomes of this genome was completed in 2014 with much of the work done by undergraduate students.

As well as adding new functions to custom cells in a logical approach, bottom-up synthetic biology can give us chassis cells with other useful properties. Minimal cells are inherently streamlined and can potentially grow with greater efficiency than those containing more genes. For the production of fuels, drugs and other high value compounds using synthetic biology, it will be advantageous to have the chassis cell take up as little energy as possible for its own growth and maintenance. This allows the resources, such as sugars, to be maximally converted into product. Designer cells also offer the possibility of more stable engineering for synthetic biology. By constructing genomes with recombination sites and transposon sequences removed and added DNA repair enzymes, it should be possible to create a cell chassis more robust against evolution due to DNA mutating and moving around in cells. For synthetic biology applications like biosensors it is desirable that the genetic structure of the engineered cells remains stable over many generations, so specialised chassis cells that do not mutate would be a useful option. Contrary to this, it would also be desirable in other circumstances to have custom cells that had little protection against mutation. Chassis cells could be engineered specifically for fast evolution, containing many recombination hotspots and lacking DNA repair mechanisms. Directed evolution is already a key technology in drug discovery and metabolic engineering, using mutation and selection to create new genes that encode for specialised enzymes. This evolution could be programmed into designer cells to enable drug discovery to be optimised in cells by synthetic biology.

## 4.4 Origins of Life in Nature and in the Lab

## 4.4.1 The RNA world

Contemporary theories on biological origins suggest that life arose via a self-replicating molecule or assembly of self-replicating molecules. It has been suggested that nucleic acids or nucleic acid-like molecules were the first self-replicators because their inherent complementarity gives an automatic template from which to copy the next generation (although some researchers hold that self-replicating peptides or lipid systems may have preceded or emerged in parallel with nucleic acids). An early nucleic acid replicator is also tempting because of the prevalence of molecules in modern cells that are related to nucleic acids, such as ATP and other cofactors. Given the fact that the ribosome is at its core a ribozyme, it seems highly likely that there was a complex RNA world that preceded the modern world of protein catalysts. This RNA world may have in turn descended from an early nucleic acid replicator by duplication, parasitism and diversification.

Researchers have recapitulated the Darwinian evolution of RNA self-replicators as well as other functional RNAs. One of the earliest examples of extracellular evolution of molecules is the work done by the Spiegelman group. In this work, the researchers discovered that the bacteriophage Qβ utilised an RNA-dependent RNA polymerase to replicate its own RNA genome. In this simple system (containing replicase, template RNA and nucleotides) the researchers found that the system showed autocatalytic kinetics, indicating that self-propagation of the viral genome was occurring and could do so in vitro with the necessary components. Furthermore, the Qβ system was used to set up an extracellular evolution experiment where mutant templates could ‘compete’ with one another for the limited pool of replicases and nucleotides, eventually selecting for template sequences that were able to replicate faster than the original (parent) template.

## 4.4.2 Chemical replicating systems

The ability to evolve functional and catalytic molecules from libraries of synthesised variants has inspired efforts towards the development of chemical replicating systems. Several groups have shown that chemically synthesised lipid vesicles are able to grow by accumulation of additional lipid material and divide under gentle shear forces. This work demonstrates that what appears to be a very biological phenomenon (cellular compartment growth and division) can be achieved by simple chemical and physical systems. There are ongoing efforts to include molecules capable of self-templating and replication in these vesicles. A likely candidate for a self-templating and self-replicating molecule is a ribozyme capable of polymerising RNA. In this case, a single ribozyme can act as the template and the catalyst for copying itself.

![](images/page_84_image_2.jpg)

Fig. 4.4 Communication between a chemical ‘cell’ and a living bacteria. The encapsulated formose reaction produces carbohydrates able to trigger the V. harveyi quorum-sensing mechanism, which induces bioluminescence in the bacteria. (Courtesy: Nature Chemistry 1, 377–383, 2009. Reproduced with permission.)

The development of chemical replicating systems will be useful for studying the minimal set of matter and information that can constitute self-replication and may shed insights on the origins of the first forms of life. There is also nascent work to engineer chemical replicating systems to interact with biological systems. Researchers have recently engineered a membrane-encapsulated chemical ‘metabolism’ that is able to synthesise complex carbohydrates from the feedstock formaldehyde, and trigger the quorum-sensing mechanism of the bacteria Vibrio harveyi (Fig. 4.4). The chemical cell was able to trigger quorum sensing and bioluminescence in bacteria, indicating that a completely artificial ‘lifelike’ system was able to interact with a living system. The interaction between living and non-living systems will be an important area for synthetic biology in the future.

## Reading

- Annaluru N, Muller H, Mitchell LA, et al. (2014). Total synthesis of a functional designer eukaryotic chromosome. Science 344(6179): 55–58.
- Forster, AC and Church, GM. (2006). Towards synthesis of a minimal cell. Mol Syst Biol 2(45). Available at: http://www.nature.com/msb/journal/v2/n1/pdf/msb4100090.pdf [Accessed 24 July 2015].
- Gibson, DG, Glass, JI, Lartigue, C, et al. (2010). Creation of a bacterial cell controlled by a chemically synthesized genome. Science 329(5987): 52–56.
- Glass, JI, Assad-Garcia, N, Alperovich, N, et al. (2006). Essential genes of a minimal bacterium. Proc Natl Acad Sci U S A 103(2): 425–430.
- Jewett, MC and Forster, AC. (2010). Update on designing and building minimal cells. Curr Opin Biotechnol 21(5): 697–703.
- Kuhner, S, van Noort, V, Betts, MJ, et al. (2009). Proteome organization in a genome-reduced bacterium. Science 326(5957): 1235–1240.
- Lajoie MJ, Rovner AJ, Goodman DB, et al. (2013). Genomically recoded organisms expand biological functions. Science 342(6156): 357–360.
- Moya, A, Gil, R, Latorre, A, et al. (2009). Toward minimal bacterial cells: evolution vs. design. FEMS Microbiol Rev 33(1): 225–235.
- Ochman, H and Raghavan, R. (2009). Excavating the functional landscape of bacterial cells. Science 326(5957): 1200–1201.

This page intentionally left blank

# CHAPTER 5

# Parts, Devices and Systems

## 5.1 Introduction

Synthetic biology follows a hierarchical structure, building up systems from smaller components. At the lowest level are the parts, which are pieces of DNA that encode for a single biological function such as an enzyme or promoter. These parts are then combined into the next layer, a device, which is a collection of parts that performs a desired higher order function, for example production of a protein. Devices are further combined into a system, which can be defined as the minimum number of devices necessary to perform the behaviour specified in the design phase. Systems can have fairly simple behaviour (e.g. an oscillator) or more complicated behaviour (e.g. a set of metabolic pathways to synthesise a product). Parts and devices are usually treated as modular entities in design and modelling. This means that it is assumed that they can be exchanged without affecting the behaviour of other system components that are left untouched, which is problematic in biological systems. Systems must be implemented in a chassis, which provides the underlying biology necessary to transcribe and translate the system as well as any enzymatic substrates that would be nec essary. The chassis can be a living organism (also called in vivo implementation), or it can be abiotic, providing only the necessary biochemical components for in vitro transcription and translation.

## 5.2 Parts

A part is a piece of DNA that encodes a biological function. In synthetic biology, parts are usually not used singly, but instead are combined into devices. When following the design cycle outlined in Chapter 2, the part is the unit which undergoes extensive characterisation and testing in different conditions to make a datasheet in order to enable modelling and model-based design. Some commonly encountered parts, along with their functions, are listed in Table 5.1 and Fig. 5.1 (which shows the symbols used to denote each part in the Synthetic Biology Open Language (SBOL) Visual notation.

Table 5.1 Some common biological parts.

| Part | Function | BioBricks Example |
| --- | --- | --- |
| Promoter | Initiate transcription | BBa_J23101E.coli constitutive |
| Operator | Regulate transcription | BBa_J64987LacI binding site |
| Ribosome binding site | Initiate translation | BBa_J63003S cerevisiae designed |
| Protein coding sequence | Encode for a protein | BBa_E0040GFPmut3b |
| Terminator | Attenuate transcription | BBa_B1001E.coli, artificial, small |

Parts

![](images/page_88_image_5.jpg)

<details>
<summary>text_image</summary>

Promoter
Ribosome Entry Site
Protein Coding Sequence
Terminator
</details>

Example Devices

![](images/page_88_image_7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  Input["Input"] --> A["Protein Generator"]
  A --> B["Inverter"]
  B --> C["Receiver"]
```
</details>

Fig. 5.1 SBOL Visual for parts and some example devices.

## 5.2.1 Promoter

A promoter is a sequence of DNA that recruits RNA polymerase and other accessory proteins to prime the transcription of messenger RNA (the molecular details of this process are described in Chapter 1). There are two common types of promoters — regulated and constitutive. Constitutive promoters are not regulated by any DNA binding proteins and, therefore, are always ‘on’. Constitutive promoters are useful in synthetic biology for providing a constant level of a protein of interest to a system. By varying the sequence of the DNA encoding the RNA polymerase binding site, it is possible to vary the strength of the promoter and to increase or decrease the number of mRNA copies that are made from it per second. This, in turn, will lead to a different steady-state concentration of protein after the effects of translation and degradation are applied.

Regulated promoters often contain additional DNA sequences, known as operators (see below), which allow other protein factors to bind to the DNA and modulate the transcription rate. Thus, the timing of transcription can be controlled, either through the addition of a small molecule, which affects the recruitment of accessory factors to the operator, or by using a second genetic circuit to produce the accessory proteins at specific times. Regulated promoters can be either positively regulated (factors binding to the DNA increase transcription rate) or negatively regulated (factors binding to the DNA decrease transcription rate). In many cases negative regulators are present within the cell and will prevent transcription from the promoter under normal conditions. In this case, the default state of the promoter is ‘off’. However, perturbing the biochemistry of the chassis (by adding small molecules or changing the temperature, pH, etc. of the system) can sometimes affect the interaction of the regulator with the operator, turning the promoter to the ‘on’ state. In this case, the promoter would be termed inducible.

## 5.2.2 Operator

Classically, a DNA sequence is termed an operator if it recruits the binding of factors that negatively regulate the promoter, also known as repressors. However, DNA sequences that bind positive regulators, also called activators, are sometimes also referred to as operators. Often in synthetic biology, the operator will not be considered as a separate part, but rather as a part of the promoter and the promoter/operator set will be characterised together as a single unit. The strength of repressor or activator binding is influenced by the DNA sequence of the operator. In addition, sequences near the operator site can also alter DNA–protein interactions, changing promoter behavior. This can be manipulated to tune the level of repression or activation and, thus, the strength of the promoter.

## 5.2.3 Ribosome binding site

A ribosome binding site or ribosome entry site is a sequence of mRNA that recruits ribosomes for the initiation of protein translation. In prokaryotes, the ribosome binding site is also called the Shine–Dalgarno sequence (named after Dr John Shine and Dr Linda Dalgarno who discovered the sequence in 1975) and in eukaryotes it is known as the Kozak consensus sequence (after discoverer Dr Marilyn Kozak). Like promoters and operators, the sequence of the ribosome binding site affects the strength of ribosome binding and, therefore, the amount of protein synthesised.

## 5.2.4 Protein coding sequence

A protein coding sequence is a sequence of DNA that encodes for a protein. It begins with a start codon (ATG) to initiate protein translation, and ends with one of three stop codons (TAA, TAG or TGA) to indicate the end of the translation region. In between are the DNA triplets (codons) which denote the amino acids that make up the protein. Three types of protein coding sequences are commonly used in synthetic biology: reporters, repressors and enzymes.

Reporters are used as readouts of dynamic biological events and usually consist of a protein that produces a visual or fluorescent output. The green fluorescent protein (GFP) and its derivatives are often used as reporters because they gain fluorescence spontaneously upon protein folding and do not require the addition of any exogenous reagents such as enzymatic substrates. Other reporters include enzymes which catalyse a reaction leading to a coloured or fluorescent product. One classic example is the enzyme β-galactosidase (also known as LacZ) which is the enzyme utilised in blue–white screening schemes for cloning. LacZ naturally catalyses the degradation of lactose into glucose plus galactose, but also hydrolyses galactose residues from a variety of chemical substrates. Several chemical analogues have been designed such that upon cleavage of the galactose residue a coloured or fluorescent product is released which serves as an indicator and allows for the calculation of the amount of LacZ present in the sample. Luciferase, an enzyme whose action upon a substrate results in the production of light (photons), is also commonly used.

Repressors are very often used as components of synthetic devices such as logic gates, switches and oscillators (discussed below). Their natural function is to bind to the operator region of promoters and prevent (repress) transcription. In addition to their DNA binding sites, repressors also contain binding sites for small molecules (inducers) that can influence their ability to bind DNA. The small molecules can be used to control the action of the repressor, switching it on and off. The final type of coding region used in synthetic biology is an enzyme, which performs an interesting chemical reaction for building systems. For example, a set of enzymes that perform sequential reactions form a metabolic pathway.

## 5.2.5 Terminators

A terminator is a sequence of DNA that signals the end of a transcriptional unit by causing the RNA polymerase to cease transcription and disengage. Terminators are placed past the 3’ end of a protein coding sequence. In prokaryotes, terminators are often palindromic in DNA sequence, which leads to the formation of strong secondary structure (e.g. hairpins) that help to weaken the interaction between the RNA polymerase and the DNA strand being copied. Often devices will incorporate two tandem terminators to reduce the chance of transcriptional read through.

## 5.3 Devices

Parts are assembled into devices which perform simple, user-defined functions. Figure 5.1 depicts a schematic of a few common devices using the same symbols to describe common DNA parts. Note that devices can have similar architecture but perform different functions, depending on the function of the individual parts. For example, the schematics for an inverter and a receiver are largely the same. However, their functions are different. In this case, the difference in function comes from the fact that the protein generated in the first half of the device has a different interaction with the promoter in the second half of the device. In the case of the inverter it represses the promoter, whereas in the case of the receiver it binds and helps initiate transcription from it.

## 5.3.1 Reporters and protein generators

The simplest device is a protein generator which combines a promoter, ribosome binding site, protein coding region and terminator. As a unit these function to produce a protein via transcription (promoter, terminator) and then translation (ribosome binding site, protein coding region).

## 5.3.2 Logic gates

The term ‘logic gate’ comes from electronic circuits and is used to denote a device where multiple inputs are assessed together in order to control a single output. These simple circuits can be combined to create more complex electrical circuits. They also form the basis of modern computers, which contain hundreds of thousands of logic gates. The operations performed by logic gates can be described with Boolean algebra using binary states: 1 if a condition is satisfied, 0 if it is not. A logic gate takes multiple binary inputs, assesses them according to a predefined rule and produces a single binary output: 1 for on, 0 for off. The identity of the predefined rule determines the type of logic gate. In synthetic biology, logic gates have been constructed from genetic circuits, biochemical networks and free nucleic acids.

## 5.3.2.1 AND

In an AND gate all conditions must be satisfied in order for the output to be switched on. The simplest AND gate is controlled by two inputs, both of which must be present in order to produce the output. The logic applied to this gate can be formulated as ‘If A AND B then “ON”, Else “OFF”’. In synthetic biology there have been a wide variety of AND gate designs. For example, an AND gate can be constructed as a hybrid promoter in which two different operator sites are used to control transcription (Fig. 5.2). Two different repressors can then bind to these sites and block transcription. The presence of both inducers is required to relieve repression, making the output dependent on the presence of two small molecules.

![](images/page_92_image_2.jpg)

<details>
<summary>text_image</summary>

Inducer A Inducer B Output
0 0 0
1 0 0
0 1 0
1 1 1
</details>

Fig. 5.2 AND gate promoter constructed from two operators (grey and black), which are bound by two repressors. The promoter remains off unless both inducers are present.

## 5.3.2.2 OR

OR gates follow the logic rule, ‘If A OR B, then “ON”, Else, “OFF”’. Therefore, for an OR gate to be switched on, only one of the input conditions must be satisfied. A very rudimentary OR gate can be constructed from a parallel set of reporter genes, each controlled by a single inducible promoter (Fig. 5.3). The presence of either molecule will turn the circuit on. Many other OR gate designs are possible.

## 5.3.2.3 NOT (Inverter)

A NOT gate takes a single input and inverts it. Therefore, it is also known as an inverter. When a signal is present, then the output of the NOT gate is ‘off’, whereas if the signal is absent, then the output is ‘on’. NOT gates in synthetic biology have been constructed from compatible promoter/repressor pairs, like the example in Fig. 5.4. An inducible promoter that responds to the desired input signal controls the production of a repressor which controls the production of the output signal. The input signal causes the production of the repressor, which in turn represses the promoter that controls the output signal, turning it off. In the absence of the signal, the output signal remains on.

## 5.3.2.4 Negated gates

Logic gates are modular and can be combined to produce more complex behaviours. Connecting a NOT gate to any other gate will invert the function of that gate. A NOT gate can be combined with an AND gate to produce a NAND gate, which has behaviour the opposite of the AND gate depicted in Fig. 5.2. In other words, the NAND gate produces an output unless two signals are present. Similarly, a NOT gate can be combined with an OR gate to produce a NOR gate, whose behaviour is opposite of the OR gate in Fig. 5.3. A NOR gate will only produce a signal when both signals are absent.

![](images/page_93_chart_2.jpg)

<details>
<summary>bar</summary>

| Condition | Inducer A | Inducer B | Output |
| --- | --- | --- | --- |
| 1 | Yes | No | No |
| 2 | Yes | No | No |
| 3 | Yes | No | No |
| 4 | Yes | No | No |
| 5 | Yes | No | No |
| 6 | Yes | No | No |
| 7 | Yes | No | No |
| 8 | Yes | No | No |
| 9 | Yes | No | No |
| 10 | Yes | No | No |
| 11 | Yes | No | No |
| 12 | Yes | No | No |
| 13 | Yes | No | No |
| 14 | Yes | No | No |
| 15 | Yes | No | No |
| 16 | Yes | No | No |
| 17 | Yes | No | No |
| 18 | Yes | No | No |
| 19 | Yes | No | No |
| 20 | Yes | No | No |
| 21 | Yes | No | No |
| 22 | Yes | No | No |
| 23 | Yes | No | No |
| 24 | Yes | No | No |
| 25 | Yes | No | No |
| 26 | Yes | No | No |
| 27 | Yes | No | No |
| 28 | Yes | No | No |
| 29 | Yes | No | No |
| 30 | Yes | No | No |
| 31 | Yes | No | No |
| 32 | Yes | No | No |
| 33 | Yes | No | No |
| 34 | Yes | No | No |
| 35 | Yes | No | No |
| 36 | Yes | No | No |
| 37 | Yes | No | No |
| 38 | Yes | No | No |
| 39 | Yes | No | No |
| 40 | Yes | No | No |
| 41 | Yes | No | No |
| 42 | Yes | No | No |
| 43 | Yes | No | No |
| 44 | Yes | No | No |
| 45 | Yes | No | No |
| 46 | Yes | No | No |
| 47 | Yes | No | No |
| 48 | Yes | No | No |
| 49 | Yes | No | No |
| 50 | Yes | No | No |
</details>

Fig. 5.3 OR gate constructed from two separate promoters (grey and black), which are bound by two repressors. The presence of either inducer is enough to switch the circuit on by allowing transcription from one of the promoters.

![](images/page_94_image_2.jpg)

Fig. 5.4 A NOT gate based on a compatible promoter/repressor (grey) whose production is controlled by an input signal. The output is inverted, meaning it is absent when the signal is present and present when the signal is absent.

## 5.3.3 Cell signalling senders and receivers

Cell–cell signalling devices are useful in synthetic biology for coordinating the behaviour of populations. Most of these devices have been implemented in bacteria and rely on a bacterial signalling mechanism known as quorum sensing. Quorum sensing is used by cells to sense the population density and coordinate gene expression and other behaviours. Quorum sensing is accomplished via the synthesis, secretion and uptake of small molecules, the concentration of which affects the behaviour of the cell population. Thus, two types of device can be created from quorum sensing for cell–cell communication: senders, those that synthesise and secrete the molecule; and receivers, those that take up the signal and produce an output in response.

Natural quorum sensing is built around small organic molecules called acyl-homoserine lactones (AHLs). Different species of bacteria synthesise different AHL molecules that vary in the length of the acyl chain or in the chemical functional groups it contains. Thus, it is possible to create sender devices that synthesise and secrete AHL molecules that are not normally secreted by a given chassis, leading to an orthogonal system for behaviour coordination. Placing this device under the control of a regulated promoter allows the system to respond to environmental signals.

Receiver devices are based on transcription factors that bind the AHL molecules and turn on target gene expression in response. In natural quorum sensing these transcription factors are continually produced, but are unstable in the absence of the AHL molecule which they bind. When the AHL is present, they are stabilised, bind to the operator region of a target promoter and turn on transcription. Synthetic receiver devices consist of the promoter, which is controlled by the AHL responsive transcription factor upstream of genes for the desired response. Orthogonal receiver devices can be constructed by using transcription factors and promoters from quorum-sensing signalling pathways from other species. These are supplied as an additional part of the genetic circuit either under the control of a constitutive promoter or under the control of another inducible one.

## 5.3.4 Light control devices

Building complex systems requires control over the timing of gene expression. This can be achieved with some of the parts and devices described above. Inducible promoters (see Section 5.2.1) can be activated through the addition of small molecules to the growth medium, and receiver devices (see 5.3.3) can be activated through manipulating the sender devices. However, light offers a means of controlling expression that is non-invasive and potentially has a higher degree of spatial control. Thus, the development of devices to manipulate chassis in response to light has received a lot of attention with devices implemented in many of the commonly used chassis including bacteria, yeast and mammalian cells.

In basic terms a device for light control consists of a light-gathering element and an effector that controls transcription in response to the light input. Light-gathering elements to date have mostly been photoreceptors from organisms that naturally respond to light, usually plants or cyanobacteria, heterologously expressed in the chassis in question. These usually contain a chemical chromophore element that harvests the light itself, contained within a protein receptor. Often the absorption of photons by the chromophore results in a conformational change in the protein receptor, which helps to signal to the effector that light has been received.

Once the effector has received a signal from the light-gathering element, it then controls gene expression in response. To do this, the effector must interact with the native genetic machinery of the chassis, so in most cases natural elements from the host have been used and fused to the protein receptors to form chimeras. Two strategies, phosphorylation of transcription factors and dimerisation of proteins, have been used for light control to date, but in principle any strategy can be developed.

## 5.4 Simple Systems

A number of simple systems have been developed that are composed of one or more devices. These are discussed below. More complex systems, i.e. those that synthesise a product or vastly alter cellular behaviour, are discussed in Chapter 8.

## 5.4.1 Feedback loops

Feedback occurs when the output from a device influences the future behaviour of that device. These effects can be either negative (reducing the future output) or positive (increasing the future output). Feedback systems are inherent to biological organisms and theoretical analysis shows that they are necessary to reduce the noise or biological variability within a