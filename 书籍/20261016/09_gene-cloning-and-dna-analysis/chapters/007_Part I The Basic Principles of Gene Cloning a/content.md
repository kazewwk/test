# Part I The Basic Principles of Gene Cloning and DNA Analysis / Chapter 7 Cloning Vectors for Eukaryotes

原始 PDF 第 139–162 页。

## Chapter 7

# Cloning Vectors for Eukaryotes

## Chapter contents

**7.1** Vectors for yeast and other fungi 121
**7.2** Cloning vectors for higher plants 129
**7.3** Cloning vectors for animals 138

Most cloning experiments are carried out with E. coli as the host, and the widest variety of cloning vectors are available for this organism. E. coli is particularly popular when the aim of the cloning experiment is to study the basic features of molecular biology such as gene structure and function. However, under some circumstances it may be desirable to use a eukaryotic host for a gene cloning experiment. This is especially true in biotechnology (Chapter 14), where the aim may not be to study a gene, but to use cloning to obtain recombinant protein, or to change the properties of an organism (e.g. to introduce herbicide resistance into a crop plant). We must therefore consider cloning vectors for eukaryotes.

## 7.1 Vectors for yeast and other fungi

The yeast Saccharomyces cerevisiae is one of the most important organisms in biotechnology. As well as its role in brewing and breadmaking, yeast is used as a host organism for the production of important pharmaceuticals from cloned genes (Section 14.3.1). Development of cloning vectors for yeast was initially stimulated by the discovery of a plasmid that is

Gene Cloning and DNA Analysis: An Introduction, Eighth Edition. T. A. Brown.

© 2021 John Wiley & Sons Ltd. Published 2021 by John Wiley & Sons Ltd.

121

---

122

Part I The Basic Principles of Gene Cloning and DNA Analysis

## Figure 7.1

The yeast 2 μm plasmid. REP1 and REP2 are involved in replication of the plasmid, and FLP codes for a protein that can convert the A form of the plasmid (shown here) to the B form, in which the gene order has been rearranged by intramolecular recombination. The function of gene D is not exactly known.

![](../../raw/pages_0129-0144/images/page_139_chart_4.jpg)

<details>
<summary>donut</summary>

| Category | Value |
| --- | --- |
| FLP | ~20% |
| REP1 | ~20% |
| D | ~15% |
| ori | ~40% |
| REP2 | ~15% |
</details>

present in most strains of S. cerevisiae (Figure 7.1). The **2 μm plasmid**, as it is called, is one of only a very limited number of plasmids found in eukaryotic cells.

## 7.1.1 Selectable markers for the 2 μm plasmid

The 2 μm plasmid is an excellent basis for a cloning vector. It is 6.3 kb in size, which is ideal for a vector, and has a copy number of about 60 in most yeast cells. Replication makes use of a plasmid origin, several enzymes provided by the host cell, and the proteins coded by the REP1 and REP2 genes carried by the plasmid.

However, all is not perfectly straightforward in using the 2 μm plasmid as a cloning vector. First, there is the question of a selectable marker. Some yeast cloning vectors carry genes conferring resistance to inhibitors such as methotrexate and copper, but most of the popular yeast vectors make use of a radically different type of selection system. In practice, a normal yeast gene is used, generally one that codes for an enzyme involved in amino acid biosynthesis. An example is the gene LEU2, which codes for β‐isopropylmalate dehydrogenase, one of the enzymes involved in the conversion of pyruvic acid to leucine.

In order to use LEU2 as a selectable marker, a special kind of host organism is needed. The host must be an **auxotrophic** mutant that has a non‐functional LEU2 gene. Such a leu2− yeast is unable to synthesize leucine and can survive only if this amino acid is supplied as a nutrient in the growth medium (Figure 7.2a). Selection is possible because transformants contain a plasmid‐borne copy of the LEU2 gene, and so are able to grow in the absence of the amino acid. In a cloning experiment, cells are plated out onto **minimal medium**, which contains no added amino acids. Only transformed cells are able to survive and form colonies (Figure 7.2b).

## 7.1.2 Vectors based on the 2 μm plasmid – yeast episomal plasmids

Vectors derived from the 2 μm plasmid are called **yeast episomal plasmids (YEps)**. Some YEps contain the entire 2 μm plasmid; others include just the 2 μm origin of replication. An example of the latter type is YEp13 (Figure 7.3).

---

Chapter 7 Cloning Vectors for Eukaryotes

123

![](../../raw/pages_0129-0144/images/page_140_image_2.jpg)

Figure 7.2

Using the LEU2 gene as a selectable marker in a yeast cloning experiment.

As well as the 2 μm origin of replication and the selectable LEU2 gene, YEp13 also includes the entire pBR322 sequence. YEp13 is therefore a shuttle vector, and can replicate and be selected for in both yeast and E. coli. Most yeast cloning vectors are shuttle vectors because it is sometimes difficult to recover the recombinant DNA molecule from a transformed yeast colony. This is not such a problem with YEps, which are present in yeast cells primarily as plasmids, but with other yeast vectors, which may integrate into one of the yeast chromosomes, purification might be impossible. This is a disadvantage because in many cloning experiments purification of recombinant DNA is essential in order for the correct construct to be identified by, for example, DNA sequencing.

The standard procedure when cloning in yeast is therefore to perform the initial cloning experiment with E. coli, and to select recombinants in this organism. Recombinant plasmids can then be purified, characterized, and the correct molecule introduced into yeast (Figure 7.4).

![](../../raw/pages_0129-0144/images/page_140_chart_7.jpg)

<details>
<summary>donut</summary>

| Category | Value |
| --- | --- |
| ampR | N/A |
| tetR | N/A |
| ori | N/A |
| LEU2 | N/A |
</details>

Figure 7.3

A yeast episomal plasmid, YEp13.

---

124

Part I The Basic Principles of Gene Cloning and DNA Analysis

Figure 7.4

Cloning with an E. coli–yeast shuttle vector such as YEp13.

Recombinant YEp13 molecules

![](../../raw/pages_0129-0144/images/page_141_image_5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["The desired recombinant"] --> B["Self-ligated vector"]
  C["LEU2 / ampR"] --> D["Transform E. coli"]
  B --> D
  D --> E["E. coli clones"]
  E --> F["Ampicillin medium"]
  F --> G["Purify DNA from several clones, identify correct molecule"]
  G --> H["Yeast recombinant"]
  H --> I["Transform yeast"]
  I --> J["Minimal medium – no leucine"]
```
</details>

## 7.1.3 A YEp may insert into yeast chromosomal DNA

The word ‘episomal’ indicates that a YEp can replicate as an independent plasmid, but also implies that integration into one of the yeast chromosomes can occur (see the definition of ‘episome’ in Section 2.1). Integration occurs because the gene carried on the vector as a selectable marker is very similar to the mutant version of the gene present in the yeast chromosomal DNA. With YEp13, for example, **homologous recombination** can occur between the plasmid LEU2 gene and the yeast mutant LEU2 gene, resulting in insertion of the entire plasmid into one of the yeast chromosomes (Figure 7.5). The plasmid may remain integrated, or a later recombination event may result in it being excised again.

## 7.1.4 Other types of yeast cloning vector

In addition to YEps, there are several other types of cloning vector for use with S. cerevisiae. Three important ones are as follows:

**Yeast integrative plasmids (YIps)** are basically bacterial plasmids carrying a yeast gene. An example is YIp5, which is pBR322 with an inserted URA3 gene (Figure 7.6a). This gene codes for orotidine‐5′‐ phosphate decarboxylase (an enzyme that catalyses one of the steps in the biosynthesis pathway for pyrimidine nucleotides) and is used as a selectable marker in exactly the same way as LEU2. A YIp cannot

---

Chapter 7 Cloning Vectors for Eukaryotes

125

![](../../raw/pages_0129-0144/images/page_142_image_2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["YEp13"] --> B["Mutated LEU2"]
  B --> C["Recombination"]
  C --> D["LEU2"]
  D --> E["Plasmid DNA"]
```
</details>

Figure 7.5

Recombination between the plasmid and chromosomal LEU2 genes can integrate YEp13 into yeast chromosomal DNA. After integration there are two copies of the LEU2 gene. Usually one of these copies is functional, and the other mutated.

replicate independently as it does not contain any parts of the 2 μm plasmid, and instead depends for its survival on integration into yeast chromosomal DNA. Integration occurs just as described for a YEp (see Figure 7.5).

**Yeast replicative plasmids (YRps)** are able to multiply as independent plasmids because they carry a chromosomal DNA sequence that includes an origin of replication. Replication origins are known to be located very close to several yeast genes, including one or two which can be used as selectable markers. YRp7 (Figure 7.6b) is an example of a replicative plasmid. It is made up of pBR322 plus the yeast gene TRP1. This gene, which is involved in tryptophan biosynthesis, is located adjacent to a chromosomal origin of replication. The yeast DNA fragment present in YRp7 contains both TRP1 and the origin.

![](../../raw/pages_0129-0144/images/page_142_image_7.jpg)

Figure 7.6

Three types of yeast cloning vector. (a) YIp5; (b) YRp7; (c) YCp50.

---

126

Part I The Basic Principles of Gene Cloning and DNA Analysis

**Yeast centromeric plasmids (YCps)** contain a replication origin and also a **centromere** sequence that binds yeast proteins to form a **kinetochore**, the structure that acts as the attachment point for the microtubules that draw chromosomes into the daughter nuclei during cell division. A YCp is therefore non‐integrative and behaves like a minichromosome. An example is YCp50 (Figure 7.6c), which contains the URA3 gene as the selective marker, as well as a DNA fragment from yeast chromosome 4 containing the CEN4 sequence (the centromere from yeast chromosome 4), and an adjacent origin of replication.

Three factors come into play when deciding which type of yeast vector is most suitable for a particular cloning experiment. The first of these is **transformation frequency**, a measure of the number of transformants that can be obtained per microgram of plasmid DNA. A high transformation frequency is necessary if a large number of recombinants are needed, or if the starting DNA is in short supply. YEps have the highest transformation frequency, providing between 10 000 and 100 000 transformed cells per μg. YRps and YCps are also quite productive, giving between 1000 and 10 000 transformants per μg, but a YIp yields less than 1000 transformants per μg, and only 1–10 unless special procedures are used. The low transformation frequency of a YIp reflects the fact that the rather rare chromosomal integration event is necessary before the vector can be retained in a yeast cell.

The second important factor is copy number. YEps and YRps have the highest copy numbers: 20–50 and 5–100, respectively. In contrast, a YCp or YIp is usually present at just one copy per cell. These figures are important if the objective is to obtain protein from the cloned gene, as the more copies there are of the gene the greater the expected yield of the protein product.

So why would one ever wish to use a YIp? With such a low transformation frequency yielding just one vector copy per cell, a YIp might appear to be a bad choice for any cloning experiment. The answer is because YIps produce very stable recombinants, as loss of a YIp that has become integrated into a chromosome occurs at only a very low frequency. In contrast, when a YCp is used, some of the daughter cells  –  about one in every 100 – will be non‐recombinant because they will fail to receive a YCp vector molecule when the parent cell divides. YRp recombinants are even more unstable, the plasmids tending to congregate in the mother cell when a daughter cell buds off, so the daughter cell does not receive any vectors. YEp recombinants suffer from similar problems, though an improved understanding of the biology of the 2 μm plasmid has enabled more stable YEps to be developed in recent years. Nevertheless, a YIp is the vector of choice if the needs of the experiment dictate that the recombinant yeast cells must retain the cloned gene for long periods in culture.

## 7.1.5 Artificial chromosomes can be used to clone long pieces of DNA in yeast

The final type of yeast cloning vector to consider is the **yeast artificial chromosome (YAC)**, which presents a totally different approach to gene cloning. The development of YACs was a spin‐off from fundamental

---

Chapter 7 Cloning Vectors for Eukaryotes

127

![](../../raw/pages_0145-0160/images/page_144_image_2.jpg)

<details>
<summary>text_image</summary>

Telomere
Centromere
Telomere
Positions of origins
of replication
</details>

Figure 7.7 Chromosome structure.

research into the structure of eukaryotic chromosomes, work that has identified the key components of a chromosome as being (Figure 7.7):

• The centromere, which is required for the chromosome to be distributed correctly to daughter cells during cell division.
Two telomeres, the structures at the ends of a chromosome, which are needed in order for the ends to be replicated correctly and which also prevent the chromosome from being nibbled away by exonucleases.
• The origins of replication, which are the positions along the chromosome at which DNA replication initiates, similar to the origin of replication of a plasmid.

Once chromosome structure had been defined in this way, the possibility arose that the individual components might be isolated by recombinant DNA techniques and then joined together again in the test tube, creating an artificial chromosome. As the DNA molecules present in natural yeast chromosomes are several hundred kilobases in length, it might be possible with an artificial chromosome to clone long pieces of DNA.

## The structure and use of a YAC vector

Several YAC vectors have been developed but each one is constructed along the same lines, with pYAC3 being a typical example (Figure 7.8a). At first glance, pYAC3 does not look much like an artificial chromosome, but on closer examination its unique features become apparent. pYAC3 is essentially a pBR322 plasmid into which a number of yeast sequences have been inserted. Two of these are the genes, URA3 and TRP1, that we have encountered already as the selectable markers for YIp5 and YRp7, respectively. As in YRp7, the DNA fragment that carries TRP1 also contains an origin of replication, but in pYAC3 this fragment is extended even further to include CEN4, the centromeric DNA sequence also carried by YCp50. The TRP1–origin–CEN4 fragment therefore contains two of the three components of the artificial chromosome.

The third component, the telomeres, is provided by the two sequences called TEL. These are not themselves complete telomere sequences, but once inside the yeast nucleus they act as seeding sequences onto which telomeres will be built. This just leaves one other part of pYAC3 that has not been mentioned: SUP4, which is the selectable marker into which new DNA is inserted during the cloning experiment.

The cloning strategy with pYAC3 is as follows (Figure 7.8b). The vector is first restricted with a combination of BamHI and SnaBI, cutting the molecule into three fragments. The fragment flanked by BamHI sites is discarded, leaving two arms, each bounded by one TEL sequence and one

---

128

Part I The Basic Principles of Gene Cloning and DNA Analysis

Figure 7.8

A YAC vector and the way it is used to clone large pieces of DNA.

![](../../raw/pages_0145-0160/images/page_145_image_4.jpg)

SnaBI site. The DNA to be cloned, which must have blunt ends (SnaBI is a blunt end cutter, recognizing the sequence TACGTA), is ligated between the two arms, producing the artificial chromosome. Protoplast transformation (Section 5.4.1) is then used to introduce the artificial chromosome into S. cerevisiae. The yeast strain that is used is a double auxotrophic mutant, $t r p 1 ^ { - } u r a 3 ^ { - }$ , which is converted to $t r p 1 ^ { + } u r a 3 ^ { + }$ by the two markers on the artificial chromosome. Transformants are therefore selected by plating onto minimal medium, on which only cells containing a correctly constructed artificial chromosome are able to grow. Any cell transformed with an incorrect artificial chromosome, containing two left or two right arms rather than one of each, is not able to grow on minimal medium as one of the markers is absent. The presence of the insert DNA in the vector can be checked by testing for insertional inactivation of SUP4, which is carried out by a simple colour test. Red colonies are recombinants, white colonies are not.

## Applications for YAC vectors

The initial stimulus in designing artificial chromosomes came from yeast geneticists who wanted to use them to study various aspects of chromosome structure and behaviour, for instance to examine the segregation of chromosomes during meiosis. These experiments established that artificial

---

Chapter 7 Cloning Vectors for Eukaryotes

129

chromosomes are stable during propagation in yeast cells and raised the possibility that they might be used as vectors for genes that are too long to be cloned as a single fragment in an E. coli vector. In fact, YACs are the highest‐capacity cloning vectors that have so far been developed, routinely being used to clone fragments between 200 and 500 kb in length, and even being able to handle DNA inserts as long as 1000 kb. Several important mammalian genes are greater than 100 kb in length (e.g. the human cystic fibrosis gene is 250 kb), beyond the capacity of all but the most sophisticated E. coli cloning systems (Section 6.2.6), but well within the range of a YAC vector. Yeast artificial chromosomes therefore opened the way to studies of the functions and modes of expression of genes that had previously been intractable to analysis by recombinant DNA techniques. A new dimension to these experiments was provided by the discovery that under some circumstances YACs can be propagated in mammalian cells, enabling the functional analysis to be carried out in the organism in which the gene normally resides.

Yeast artificial chromosomes are equally important in the production of genomic libraries. Recall that with fragments of 300 kb, the maximum insert size for the highest capacity E. coli vector, some 30 000 clones are needed for a human gene library (Section 6.2.6). With a YAC vector carrying 500 kb fragments, the size of a human genomic library is reduced to just 19 000 clones. Unfortunately, YACs have run into problems with insert stability, the cloned DNA sometimes becoming rearranged by intramolecular recombination. Nevertheless, YACs have been of immense value in providing long pieces of cloned DNA for use in large‐scale DNA sequencing projects.

## 7.1.6 Vectors for other yeasts and fungi

Cloning vectors for other species of yeast and fungi are needed for basic studies of the molecular biology of these organisms and to extend the possible uses of yeasts and fungi in biotechnology. Episomal plasmids based on the S. cerevisiae 2 μm plasmid are able to replicate in a few other types of yeast, but the range of species is not broad enough for 2 μm vectors to be of general value. Replicative, centromeric and integrative plasmids, similar in design to YRps, YCps, and YIps, have been designed for a second type of yeast, Pichia pastoris, and integrative vectors are available for filamentous fungi such as Aspergillus nidulans and Neurospora crassa. We will look at these vectors in more detail when we study the use of yeasts and fungi in recombinant protein production (Section 14.3.1).

## 7.2 Cloning vectors for higher plants

Cloning vectors for higher plants were developed in the 1980s and their use has led to the **genetically modified (GM) crops** that are in the headlines today. We will examine the genetic modification of crops and other plants in Chapter 16. Here we look at the cloning vectors and how they are used.

---

130

Part I The Basic Principles of Gene Cloning and DNA Analysis

Three types of vector system have been used with varying degrees of success with higher plants:

• Vectors based on the Ti plasmid of Agrobacterium tumefaciens.
• Direct gene transfer using various types of plasmid DNA.
• Vectors based on plant viruses.

## 7.2.1 Agrobacterium tumefaciens – nature’s smallest genetic engineer

Although no naturally occurring plasmids are known in higher plants, one bacterial plasmid is of great importance in gene cloning. This is the Ti plasmid of Agrobacterium tumefaciens. The species is now called Rhizobium rhizogenes by microbiologists, but we will use the old‐fashioned name that is familiar to plant genetic engineers.

A. tumefaciens is a soil microorganism that causes crown gall disease in many species of dicotyledonous plants. Crown gall occurs when a wound on the stem allows A. tumefaciens bacteria to invade the plant. After infection the bacteria cause a cancerous proliferation of the stem tissue in the region of the crown (Figure 7.9).

The ability to cause crown gall disease is associated with the presence of the Ti (tumour inducing) plasmid within the bacterial cell. This is a large (greater than 200 kb) plasmid that carries numerous genes involved in the infective process (Figure  7.10a). A remarkable feature of the Ti plasmid is that, after infection, part of the molecule is integrated into the  plant chromosomal DNA (Figure  7.10b). This segment, called the **T‐DNA**, is between 15 and 30 kb in size, depending on the strain. It is maintained in a stable form in the plant cell and is passed on to daughter cells as an integral part of the chromosomes. But the most remarkable feature of the Ti plasmid is that the T‐DNA contains eight or so genes that are expressed in the plant cell and are responsible for the cancerous properties of the transformed cells. These genes also direct synthesis of unusual compounds, called opines, that the bacteria use as nutrients (Figure  7.10c). In short, A. tumefaciens genetically engineers the plant cell for its own purposes.

![](../../raw/pages_0145-0160/images/page_147_image_11.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Healthy plant"] --> B["Agrobacterium tumefaciens"]
  B --> C["Wound in stem"]
  C --> D["Bacteria invade the wound"]
  D --> E["Rapid cell division – crown gall"]
  E --> F["Crown gall"]
```
</details>

Figure 7.9

Crown gall disease.

---

Chapter 7 Cloning Vectors for Eukaryotes

131

![](../../raw/pages_0145-0160/images/page_148_chart_2.jpg)

<details>
<summary>donut</summary>

| Region | Description |
| --- | --- |
| Top | T-DNA (oncogenes) |
| Bottom Left | Virulence region |
| Bottom Right | Host specificity region |
</details>

Figure 7.10

The Ti plasmid and its integration into the plant chromosomal DNA after A. tumefaciens infection.

![](../../raw/pages_0145-0160/images/page_148_image_5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Ti"] -->|Recombination transfers T-DNA| B["Integrated T-DNA"]
  B --> C["Plant chromosomal DNA"]
  B --> D["T-DNA"]
  D --> E["Rapid cell division"]
  D --> F["Synthesis of opines"]
```
</details>

## Using the Ti plasmid to introduce new genes into a plant cell

It was realized very quickly that the Ti plasmid could be used to transport new genes into plant cells. All that would be necessary would be to insert the new genes into the T‐DNA and then the bacterium could do the hard work of integrating them into the plant chromosomal DNA. In practice this has proved a tricky proposition, mainly because the large size of the Ti plasmid makes manipulation of the molecule very difficult.

The main problem is, of course, that it is very unlikely that there would be any single‐copy restriction sites in a plasmid 200 kb in size, and modifying the plasmid to change all but one of the, for example, BamHI sites would be impracticable. Novel strategies therefore had to be developed for inserting new DNA into the plasmid. Two are in general use:

• The **binary vector strategy** (Figure 7.11) is based on the observation that the T‐DNA does not need to be physically attached to the rest of

---

132

Part I The Basic Principles of Gene Cloning and DNA Analysis

Figure 7.11

The binary vector strategy. Plasmids A and B complement each other when present together in the same A. tumefaciens cell. The T‐DNA carried by plasmid B is transferred to the plant chromosomal DNA by proteins coded by genes carried by plasmid A.

![](../../raw/pages_0145-0160/images/page_149_image_4.jpg)

<details>
<summary>text_image</summary>

Virulence
region
Host
specificity
region
Plasmid A
~170 kb
</details>

![](../../raw/pages_0145-0160/images/page_149_image_5.jpg)

<details>
<summary>text_image</summary>

Unique
restriction site
T-DNA
Plasmid B
~20 kb
</details>

the Ti plasmid. A two‐plasmid system, with the T‐DNA on a relatively small molecule, and the rest of the plasmid in normal form, is just as effective at transforming plant cells. In fact, some strains of A. tumefaciens, and related agrobacteria, have natural binary plasmid systems. The T‐DNA plasmid is small enough to have single‐copy restriction sites and to be manipulated using standard techniques.

The **co‐integration strategy** (Figure 7.12) uses an entirely new plasmid, based on an E. coli vector, but carrying a small portion of the T‐DNA. The homology between the new molecule and the Ti plasmid means that if both are present in the same A. tumefaciens cell, recombination

![](../../raw/pages_0145-0160/images/page_149_image_8.jpg)

Figure 7.12

The co‐integration strategy.

---

Chapter 7 Cloning Vectors for Eukaryotes

133

(a) Wound infection by recombinant A. tumefaciens

![](../../raw/pages_0145-0160/images/page_150_image_3.jpg)

<details>
<summary>text_image</summary>

Apply recombinant
bacteria
Cloned gene only
present in the
crown gall
</details>

(b) Transformation of cultured plant cells

![](../../raw/pages_0145-0160/images/page_150_image_5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Plant cell suspension"] --> B["Bacterium"]
  B --> C["Plate onto solid medium"]
  C --> D["Transformed callus"]
  D --> E["Transfer to medium with different growth hormone balance"]
  E --> F["Shoots form"]
  F --> G["Plant into soil"]
  G --> H["Transformed plant"]
```
</details>

Figure 7.13

Transformation of plant cells by recombinant A. tumefaciens. (a) Infection of a wound: transformed plant cells are present only in the crown gall. (b) Transformation of a cell suspension: all the cells in the resulting plant are transformed.

can integrate the E. coli plasmid into the T‐DNA region. The gene to be cloned is therefore inserted into a restriction site on the small E. coli plasmid, introduced into A. tumefaciens cells carrying a Ti plasmid, and the natural recombination process left to integrate the new gene into the T‐DNA. Infection of the plant leads to insertion of the new gene, along with the rest of the T‐DNA, into the plant chromosomes.

## Production of transformed plants with the Ti plasmid

If A. tumefaciens bacteria that contain an engineered Ti plasmid are introduced into a plant in the natural way, by infection of a wound in the stem, then only the cells in the resulting crown gall will possess the cloned gene (Figure  7.13a). This is obviously of little value to the biotechnologist. Instead, a way of introducing the new gene into every cell in the plant is needed.

There are several solutions, the simplest being to infect not the mature plant but a culture of plant cells or protoplasts (Section  5.4.1) in liquid medium (Figure 7.13b). Plant cells and protoplasts whose cell walls have re‐formed can be treated in the same way as microorganisms. In particular, they can be plated onto a selective medium in order to isolate transformants. A mature plant regenerated from transformed cells will contain the cloned gene in every cell and will pass the cloned gene to its offspring.

---

134

Part I The Basic Principles of Gene Cloning and DNA Analysis

Figure 7.14

The binary Ti vector pBIN19. kan<sup>R</sup> = kanamycin resistance gene.

![](../../raw/pages_0145-0160/images/page_151_chart_4.jpg)

<details>
<summary>donut</summary>

| Category | Value |
| --- | --- |
| Left repeat | N/A |
| lacZ' | N/A |
| ranR | N/A |
| Right repeat | N/A |
</details>

However, regeneration of a transformed plant can occur only if the Ti vector has been ‘**disarmed**’ so that the transformed cells do not display cancerous properties. Disarming is possible because the cancer genes, all of which lie in the T‐DNA, are not needed for the infection process, infectivity being controlled mainly by the virulence region of the Ti plasmid. In fact, the only parts of the T‐DNA that are involved in infection are two 25 bp repeat sequences found at the left and right borders of the region integrated into the plant DNA. Any DNA placed between these two repeat sequences will be treated as T‐DNA and transferred to the plant. It is therefore possible to remove all the cancer genes from the normal T‐DNA and replace them with an entirely new set of genes, without disturbing the infection process.

A number of disarmed Ti cloning vectors are now available, a typical example being the binary vector pBIN19 (Figure 7.14). The left and right T‐DNA borders present in this vector flank a copy of the lacZ′ gene, containing a number of cloning sites, as well as a kanamycin resistance gene that functions after integration of the vector sequences into the plant chromosome. As with a yeast shuttle vector, the initial manipulations that result in insertion of the gene to be cloned into pBIN19 are carried out in E. coli, the correct recombinant pBIN19 molecule then being transferred to A. tumefaciens and thence into the plant. Transformed plant cells are selected by plating onto agar medium containing kanamycin.

## Limitations of cloning with the Ti plasmid

Higher plants are divided into two broad categories: the monocotyledons (monocots) and the dicotyledons (dicots). Several factors have combined to make it much easier to use the Ti plasmid to clone genes in dicots such as tomato, tobacco, potato, peas, and beans, but much more difficult to obtain the same results with monocots. This has been frustrating because monocots include wheat, barley, rice, and maize, which are the most important crop plants and hence the most desirable targets for genetic engineering projects.

One difficulty stems from the fact that in nature A. tumefaciens only infects dicotyledonous plants. Monocots are therefore outside of the normal host range. At one time it was thought that this natural barrier was insurmountable and that monocots were totally resistant to transformation with Ti vectors, but eventually techniques for achieving T‐DNA transfer

---

Chapter 7 Cloning Vectors for Eukaryotes

135

![](../../raw/pages_0145-0160/images/page_152_image_2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Embryo"] --> B["Soak in solution with A. tumefaciens, plate onto solid medium"]
  B --> C["Normal agar medium"]
  C --> D["Transfer callus segments"]
  D --> E["Selective agar medium"]
  E --> F["Transformed plant"]
```
</details>

Figure 7.15

Embryo transformation.

were devised. However, this was not the end of the story. Transformation with an Agrobacterium vector normally involves regeneration of an intact plant from a transformed protoplast, cell, or callus culture. The ease with which a plant can be regenerated depends very much on the particular species involved and, once again, the most difficult plants are the monocots. With monocots, callus derived from embryos is often used, as it is easier to regenerate plants from embryogenic callus than it is from callus derived from somatic tissues. An embryo is first soaked in a solution containing recombinant A. tumefaciens, and then placed on an agar medium that induces callus formation (Figure 7.15). Not all of the cells in the embryo become transformed, so pieces of callus are cultured on a selective medium on which only the transformants can grow. Mature plants are then regenerated from the transformed callus. The approach has been successful with maize, wheat, barley, and several other important monocots.

## 7.2.2 Cloning genes in plants by direct gene transfer

Although the Ti plasmid has always been looked on as the most promising system for cloning genes in plants, the limitations with the natural host range of A. tumefaciens has stimulated the search for alternative methods for introducing new DNA into plant cells. **Direct gene transfer** is one such method.

## Direct gene transfer into the nucleus

Direct gene transfer is based on the observation, first made in 1984, that a supercoiled bacterial plasmid, although unable to replicate in a plant cell on its own, can become integrated by recombination into one of the plant chromosomes. The recombination event is poorly understood but is almost certainly distinct from the processes responsible for T‐DNA integration.

---

136

Part I The Basic Principles of Gene Cloning and DNA Analysis

Figure 7.16 Direct gene transfer.

![](../../raw/pages_0145-0160/images/page_153_image_3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["New gene"] --> B["Plasmid"]
  B --> C["Transform plant cells"]
  C --> D["Supercoiled plasmid"]
  D --> E["Non-homologous recombination"]
  E --> F["Plasmid"]
  F --> G["New gene inserted into plant DNA"]
```
</details>

It  is also distinct from the chromosomal integration of a yeast vector (Section 7.1.3), as there is no requirement for a region of similarity between the bacterial plasmid and the plant DNA. Integration appears to occur randomly at any position in any of the plant chromosomes (Figure 7.16).

Direct gene transfer therefore makes use of supercoiled plasmid DNA, possibly a simple bacterial plasmid, into which an appropriate selectable marker (e.g. a kanamycin resistance gene) and the gene to be cloned have been inserted. Biolistics (Section 5.4.1) is frequently used to introduce the plasmid DNA into plant embryos, which are then regenerated as described above for Agrobacterium transformation. Alternatively, if the species being engineered can be regenerated from protoplasts or single cells, then other strategies, possibly more efficient than biolistics, are possible. One such method involves resuspending protoplasts in a viscous solution of polyethylene glycol. This is a polymeric, negatively charged compound that is thought to precipitate DNA onto the surfaces of the protoplasts and to induce uptake by endocytosis (Figure  7.17). Electroporation is also sometimes used to increase transformation frequency. After treatment, protoplasts are left for a few days in a solution that encourages regeneration of the cell walls. The cells are then spread onto selective medium to identify transformants and to provide callus cultures from which intact plants can be grown.

Figure 7.17

Direct gene transfer by precipitation of DNA onto the surfaces of protoplasts.

![](../../raw/pages_0145-0160/images/page_153_image_8.jpg)

<details>
<summary>text_image</summary>

DNA
Plant protoplasts
</details>

---

Chapter 7 Cloning Vectors for Eukaryotes

137

## Transfer of genes into the chloroplast genome

If biolistics is used to introduce DNA in a plant embryo, then some particles may penetrate one or more of the chloroplasts present in the cells. Chloroplasts contain their own genomes, distinct from (and much shorter) than the DNA molecules in the nucleus, and under some circumstances, plasmid DNA can become integrated into this chloroplast genome. Unlike the integration of DNA into nuclear chromosomes, integration into the chloroplast genome will not occur randomly. Instead the DNA to be cloned must be flanked by sequences similar to the region of the chloroplast genome into which the DNA is to be inserted, so that insertion can take place by homologous recombination (Section 7.1.3). Each of these flanking sequences must be 500 bp or so in length. A low level of chloroplast transformation can also be achieved after PEG‐induced DNA delivery into protoplasts if the plasmid that is taken up carries these flanking sequences.

A plant cell contains tens of chloroplasts, but probably only one per cell becomes transformed, so the inserted DNA must carry a selectable marker such as the kanamycin resistance gene, and the embryos must be treated with the antibiotic for a considerable period to ensure that the transformed genomes propagate within the cell. Although this means that chloroplast transformation is a difficult method to carry out successfully, it is becoming an important adjunct to the more traditional methods for obtaining GM crops. As each cell has many chloroplasts, but only one nucleus, a gene inserted into the chloroplast genome is likely to be expressed at a higher level than one placed in the nucleus. This is particularly important when the engineered plants are to be used for production of pharmaceutical proteins (Section  15.1.5). So far, the  approach has been most successful with tobacco, but chloroplast transformation has also been achieved with more useful crops such as soybean and cotton.

## 7.2.3 Attempts to use plant viruses as cloning vectors

Modified versions of λ and M13 bacteriophages are important cloning vectors for E. coli (Chapter 6). Most plants are subject to viral infection, so could viruses be used to clone genes in plants? If they could, then they would be much more convenient to use than other types of vector, because with many viruses, transformation can be achieved simply by rubbing the virus nucleic acid onto the surface of a leaf. The natural infection process then spreads the virus throughout the plant.

The potential of plant viruses as cloning vectors has been explored for several years but without great success. One problem is that the vast majority of plant viruses have genomes not of DNA but of RNA. RNA viruses are not so useful as potential cloning vectors because manipulations with RNA are more difficult to carry out. Only two classes of DNA virus are known to infect higher plants, the **caulimoviruses** and **geminiviruses**, and neither is ideally suited for gene cloning.

---

138

Part I The Basic Principles of Gene Cloning and DNA Analysis

## Caulimovirus vectors

Although one of the first successful plant genetic engineering experiments, back in 1984, used a caulimovirus vector to clone a new gene into turnip plants, two general difficulties with these viruses have limited their usefulness.

The first is that the total size of a caulimovirus genome is, like that of λ, constrained by the need to package it into its protein coat. Even after deletion of non‐essential sections of the virus genome, the capacity for carrying inserted DNA is still very limited. Recent research has shown that it might be possible to circumvent this problem by adopting a helper virus strategy, similar to that used with phagemids (Section  6.3.2). In this strategy, the cloning vector is a **cauliflower mosaic virus (CaMV)** genome that lacks several of the essential genes, which means that it can carry a large DNA insert but cannot by itself direct infection. Plants are inoculated with the vector DNA along with a normal CaMV genome. The normal viral genome provides the genes needed for the cloning vector to be packaged into virus proteins and spread through the plant.

This approach has considerable potential, but does not solve the second problem, which is the extremely narrow host range of caulimoviruses. This restricts cloning experiments to just a few plants, mainly brassicas such as turnips, cabbages, and cauliflowers. Caulimoviruses have, however, been important in genetic engineering as the source of highly active promoters that work in all plants and that are used to obtain expression of genes introduced by Ti plasmid cloning or direct gene transfer.

## Geminivirus vectors

What of the geminiviruses? These are particularly interesting because their natural hosts include plants such as maize and wheat, and they could therefore be potential vectors for these and other monocots. But geminiviruses have presented their own set of difficulties, one problem being that during the infection cycle the genomes of some geminiviruses undergo rearrangements and deletions, which would scramble up any additional DNA that has been inserted, an obvious disadvantage for a cloning vector. Research over the years has addressed these problems, and geminiviruses are beginning to find some specialist applications in plant gene cloning. One of these is in **virus‐induced gene silencing (VIGS)**, a technique used to investigate the functions of individual plant genes. This method exploits one of the natural defence mechanisms that plants use to protect themselves against viral attack. This method, called RNA silencing, results in degradation of viral mRNAs. If one of the viral RNAs is transcribed from a cloned gene contained within a geminivirus genome, then not only the viral transcripts but also the cellular mRNAs derived from the plant’s copy of the gene are degraded (Figure 7.18). The plant gene therefore becomes silenced and the effect of its inactivation on the phenotype of the plant can be studied.

## 7.3 Cloning vectors for animals

Considerable effort has been put into the development of vector systems for cloning genes in animal cells. These vectors are needed in biotechnology for the synthesis of recombinant protein from genes that are not

---

Chapter 7 Cloning Vectors for Eukaryotes

139

![](../../raw/pages_0145-0160/images/page_156_image_2.jpg)

Figure 7.18

The use of a geminivirus vector to silence a plant gene via virus‐induced gene silencing.

expressed correctly when cloned in E. coli or yeast (Chapter  14), and methods for cloning in humans are being sought by clinical molecular biologists attempting to devise techniques for **gene therapy** (Section 15.3), in which a disease is treated by introduction of a cloned gene into the patient.

The clinical aspect has meant that most attention has been directed at cloning systems for mammals, but important progress has also been made with insects. Cloning in insects is interesting because it makes use of a novel type of vector that we have not met so far. We will therefore examine insect vectors before concluding the chapter with an overview of the cloning methods used with mammals.

## 7.3.1 Cloning vectors for insects

The fruit fly, Drosophila melanogaster, has been and still is one of the most important model organisms used by biologists. Its potential was first recognized by the famous geneticist Thomas Hunt Morgan, who in 1910 started to carry out genetic crosses between fruit flies with different eye colours, body shapes, and other inherited characteristics. These experiments led to the techniques still used today for gene mapping in insects and other animals. More recently, the discovery that the homeotic selector genes of Drosophila – the genes that control the overall body plan of the fly  –  are closely related to equivalent genes in mammals, has led to D. melanogaster being used as a model for the study of human developmental processes. The importance of the fruit fly in modern biology makes it imperative that vectors for cloning genes in this organism are available.

## P elements as cloning vectors for Drosophila

The development of cloning vectors for Drosophila has taken a different route to that followed with bacteria, yeast, plants, and mammals. No plasmids are known in Drosophila and although fruit flies are, like all organisms, susceptible to infection with viruses, these have not been used as the basis for cloning vectors. Instead, cloning in Drosophila makes use of a **transposon** called the **P element**.

Transposons are common in all types of organism. They are short pieces of DNA (usually less than 10 kb in length) that can move from one position

---

140

Part I The Basic Principles of Gene Cloning and DNA Analysis

Figure 7.19

Cloning in Drosophila with a P element vector. (a) The structure of a P element. (b) Transposition of a P element from a plasmid to a fly chromosome. (c) The structure of a P element cloning vector. The left‐hand P element contains a cloning site (R) that disrupts its transposase gene. The right‐hand P element has an intact transposase gene but cannot itself transpose because it is ‘wings‐clipped’ – it lacks terminal inverted repeats.

(a) The structure of a P element

![](../../raw/pages_0145-0160/images/page_157_image_5.jpg)

<details>
<summary>text_image</summary>

Genes
Terminal inverted repeat
</details>

(b) P element transposition

![](../../raw/pages_0145-0160/images/page_157_image_7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["P element carried by a plasmid"] -->|"Transposition"| B["P element inserted in a fly chromosome"]
```
</details>

(c) The structure of a P element cloning vector

![](../../raw/pages_0145-0160/images/page_157_image_9.jpg)

<details>
<summary>text_image</summary>

R
'Wings-clipped' element
Inverted repeats
Plasmid DNA
</details>

to another in the chromosomes of a cell. P elements, which are one of several types of transposon in Drosophila, are 2.9 kb in length and contain three genes flanked by short inverted repeat sequences at either end of the element (Figure 7.19a). The genes code for transposase, the enzyme that carries out the transposition process, and the inverted repeats form the recognition sequences that enable the enzyme to identify the two ends of the inserted transposon.

As well as moving from one site to another within a single chromosome, P elements can also jump between chromosomes, or between a plasmid carrying a P element and one of the fly’s chromosomes (Figure 7.19b). The latter is the key to the use of P elements as cloning vectors. The vector is a plasmid that carries two P elements, one of which contains the insertion site for the DNA that will be cloned. Insertion of the new DNA into this P element results in disruption of its transposase gene, so this element is inactive. The second P element carried by the plasmid is therefore one that has an intact version of the transposase gene. Ideally this second element should not itself be transferred to the Drosophila chromosomes, so it has its ‘wings clipped’, which means that its inverted repeats are removed so that the transposase does not recognize it as being a real P element (Figure 7.19c). Once the gene to be cloned has been inserted into the vector, the plasmid DNA is microinjected into fruit fly embryos. The transposase from the wings‐clipped P element directs transfer of the engineered P element into one of the fruit fly chromosomes. If this happens within a germline nucleus, then the adult fly that develops from the embryo will carry copies of the cloned gene in all its cells. P element cloning was first developed in the 1980s and has made a number of important contributions to Drosophila genetics.

---

Chapter 7 Cloning Vectors for Eukaryotes

141

## Cloning vectors based on insect viruses

Although virus vectors have not been developed for cloning genes in Drosophila, one type of virus, the **baculovirus**, has played an important role in gene cloning with other insects. The main use of baculovirus vectors is in the production of recombinant protein, and we will return to them when we consider this topic in Section 14.3.2.

## 7.3.2 Cloning in mammals

At present, gene cloning in mammals is carried out for one of three reasons:

• To achieve a **gene knockout**, which is an important technique used to help determine the function of an unidentified gene (Section 12.2.2). These experiments are usually carried out with rodents such as mice.
For production of recombinant protein in a mammalian cell culture, and in the related technique of **pharming**, which involves genetic engineering of a farm animal so that it synthesizes an important protein such as a pharmaceutical, often in its milk (Section 14.3.3).
• In **gene therapy**, in which human cells are engineered in order to treat a disease (Section 15.3).

## Viruses as cloning vectors for mammals

For many years it was thought that viruses would prove to be the key to cloning in mammals. This expectation has only partially been realized. The first cloning experiment involving mammalian cells was carried out in 1979 with a vector based on simian virus 40 (SV40). This virus is capable of infecting several mammalian species, following a lytic cycle in some hosts and a lysogenic cycle in others. The genome is 5.2 kb in size (Figure 7.20a) and contains two sets of genes: the ‘early’ genes, expressed early in the infection cycle and coding for proteins involved in viral DNA replication, and the ‘late’ genes, coding for viral capsid proteins. SV40 suffers from the same problem as λ and the plant caulimoviruses, in that

![](../../raw/pages_0145-0160/images/page_158_image_12.jpg)

Figure 7.20

SV40 and an example of its use as a cloning vector. To clone the rabbit β‐globin gene the HindIII to BamHI restriction fragment was deleted (resulting in SVGT‐5) and replaced with the rabbit gene.

---

142

Part I The Basic Principles of Gene Cloning and DNA Analysis

packaging constraints limit the amount of new DNA that can be inserted into the genome. Cloning with SV40 therefore involves replacing one or more of the existing genes with the DNA to be cloned. In the original experiment a segment of the late gene region was replaced (Figure 7.20b), but early gene replacement is also an option.

In the years since 1979, a number of other types of virus have been used to clone genes in mammals. These include:

• **Adenoviruses**, which enable DNA fragments of up to 8 kb to be cloned, longer than is possible with an SV40 vector, though adenoviruses are more difficult to handle because their genomes are bigger.
**Papillomaviruses**, which also have a relatively high capacity for inserted DNA. Bovine papillomavirus (BPV), which causes warts on cattle, is particularly attractive because it has an unusual infection cycle in mouse cells, taking the form of a multicopy plasmid with about 100 molecules present per cell. It does not cause the death of the mouse cell, and BPV molecules are passed to daughter cells on cell division, giving rise to a permanently transformed cell line. Shuttle vectors consisting of BPV and E. coli sequences, and capable of replication in both mouse and bacterial cells, have been used for the production of recombinant proteins in mouse cell lines.
**Adeno‐associated virus (AAV)**, which is unrelated to adenovirus but often found in the same infected tissues, because AAV makes use of some of the proteins synthesized by adenovirus in order to complete its replication cycle. In the absence of this helper virus, the AAV genome inserts into its host’s DNA. With most integrative viruses this is a random event, but AAV has the unusual property of always inserting at the same position, within human chromosome 19. Knowing exactly where the cloned gene will be in the host genome is important if the outcome of the cloning experiment must be checked rigorously, as is the case in applications such as gene therapy. AAV vectors are therefore looked on as having major potential in this area.
• **Retroviruses**, which are the most commonly used vectors for gene therapy. Although they insert at random positions, the resulting integrants are very stable, which means that the therapeutic effects of the cloned gene will persist for some time. We will return to gene therapy in Section 15.3.

## Gene cloning without a vector

One of the reasons why virus vectors have not become widespread in mammalian gene cloning is because it was discovered in the early 1990s that the most effective way of transferring new genes into mammalian cells is by microinjection. Although a difficult procedure to carry out, microinjection of bacterial plasmids, or linear DNA copies of genes, into mammalian nuclei results in the DNA being inserted into the chromosomes, possibly as multiple copies in a tandem, head‐to‐tail arrangement (Figure 7.21). This procedure is generally looked on as more satisfactory than the use of a viral vector because it avoids the possibility that viral DNA will infect the cells and cause defects of one kind or another.

---

Chapter 7 Cloning Vectors for Eukaryotes

143

![](../../raw/pages_0161-0176/images/page_160_image_2.jpg)

<details>
<summary>text_image</summary>

Multiple copies of the cloned DNA
Chromosomal DNA
</details>

Figure 7.21

Multiple copies of cloned DNA molecules inserted as a tandem array in a chromosomal DNA molecule.

Microinjection of DNA is the basis to creation of a **transgenic animal**, one that contains a cloned gene in all of its cells. A transgenic mouse can be generated by microinjection of a fertilized egg cell which is subsequently cultured in vitro for several cell divisions and then implanted into a foster mother. Alternatively, an **embryonic stem (ES) cell** can be used. These are obtained from within an early embryo and, unlike most mammalian cells, are **totipotent**, meaning that their developmental pattern is not preset and cells descended from them can form many different structures in the adult mouse. After microinjection, the ES cell is placed back in an embryo which is implanted into the foster mother. The resulting mouse is a **chimera**, comprising a mixture of engineered and non‐engineered cells, because the embryo that receives the ES cell also contains a number of ordinary cells that contribute, along with the ES cell, to the make‐up of the adult mouse. Non‐chimeric mice, which contain the cloned gene in all their cells, are obtained by allowing the chimera to reproduce, as some of the offspring will be derived from egg cells that contain the cloned gene.

## Further reading

- Bock, R. (2015) Engineering plastid genomes: methods, tools, and applications in basic research and biotechnology. Annual Review of Plant Biology, 66, 211–241. [Information on and context for chloroplast transformation.]
- Brisson, N., Paszkowski, J., Penswick, J.R., et al. (1984) Expression of a bacterial gene in plants by using a viral vector. Nature, 310, 511–114. [The first cloning experiment with a caulimovirus.]
- Burke, D.T., Carle, G.F., and Olson, M.V. (1987) Cloning of large segments of exogenous DNA into yeast by means of artificial chromosome vectors. Science, 236, 806–812.
- Carrillo‐Tripp, J., Shimada‐Beltrán, H., and Rivera‐Bustamante, R. (2006) Use of geminiviral vectors for functional genomics. Current Opinion in Plant Biology, 9, 209–215. [Virus‐induced gene silencing.]
- Chan, K.M., Liu, Y.T., Ma, C.H., et al. (2013) The 2 micron plasmid of Saccharomyces cerevisiae: a miniaturized selfish genome with optimized functional competence. Plasmid, 70, 2–17. [Reviews the features of the 2 μm plasmid.]

---

144

Part I The Basic Principles of Gene Cloning and DNA Analysis

- Colosimo, A., Goncz, K.K., Holmes, A.R., et al. (2000) Transfer and expression of foreign genes in mammalian cells. Biotechniques, 29, 314–321.
- Crystal, R.G. (2014) Adenovirus: the first effective in vivo gene delivery vector. Human Gene Therapy, 25, 3–11.
- Evans, M. (2011) Discovering pluripotency: 30 years of mouse embryonic stem cells. Nature Reviews Molecular Cell Biology, 12, 680–686.
- Gnügge, R. and Rudolf, F. (2017) Saccharomyces cerevisiae shuttle vectors. Yeast, 34, 205–221. [Details of different yeast cloning vectors.]
- Gordon, J.E. and Christie, P.J. (2014) The Agrobacterium Ti plasmids. Microbiology Spectrum, 2, 6.
- Hamer, D.H. and Leder, P. (1979) Expression of the chromosomal mouse β‐maj‐globin gene cloned in SV40. Nature, 281, 35–40.
- Hayta, S., Smedley, M.A., Demir, S.U., et al. (2019) An efficient and reproducible Agrobacterium‐mediated transformation method for hexaploid wheat (Triticum aestivum L.). Plant Methods, 15, 121. [Describes the transformation of wheat embryos.]
- Lee, L.‐Y. and Gelvin, S.B. (2008) T‐DNA binary vectors and systems. Plant Physiology, 146, 325–332.
- Nakamura, Y., Nishi, T., Noguchi, R., et al. (2018) A stable, autonomously replicating plasmid vector containing Pichia pastoris centromeric DNA. Applied and Environmental Microbiology, 84, e02882–17.
- Păcurar, D.I., Thordal‐Christensen, H., Păcurer, M.L., et al. (2011) Agrobacterium tumefaciens: from crown gall tumors to genetic transformation. Physiological and Molecular Plant Pathology, 76, 76–81.
- Paszkowski, J., Shillito, R.D., Saul, M., et al. (1984) Direct gene transfer to plants. EMBO Journal, 3, 2717–2722.
- Rubin, G.M. and Spradling, A.C. (1982) Genetic transformation of Drosophila with transposable element vectors. Science, 218, 348–353. [Cloning with P elements.]
