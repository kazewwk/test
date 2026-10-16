• details about the crystal form and methods by which the crystals were produced.

## Searches for structures

Retrieval of a particular structure is easy, provided that you know its identifier. If not, how do you find it? A simple tool accessible from the RCSB home page permits a search for keywords. Entering SPINACH THIOREDOXIN returns 13 entries, including 1FAA and other crystal structures, of the same molecule or mutants, in different oxidation states. However, the search also returns several structures of glyceraldehyde-3-phosphate dehydrogenase. Why? This is because, embedded in the dehydrogenase structure entries is a reference to an article that contains the word thioredoxin in the title. Nevertheless, the information returned would easily permit you to choose structures to look at or analyse, according to your particular interest in this family of molecules.

The RCSB site also offers more complex browsers. Using these, you could insist that the keywords appear in the molecule name. This would exclude the glyceraldehyde-3-phosphate dehydrogenase entries. Or, with other goals, you could constrain the method of structure determination, and set limits on the resolution.

Here we have discussed searching the wwPDB with various types of keywords; that is, a text search. In Chapter 6 we shall treat the problem of searching a structural database with a probe structure.

The Macromolecular Structure Database at the EBI offers a useful list of facilities for searching and browsing the wwPDB. Another useful information source available at the EBI is the database of Probable Quaternary Structures (PQS) of the biologically active forms of proteins. Often the asymmetric unit of the crystal structure, as deposited in the PDB entry, contains only part of the active unit, or alternatively multiple copies of the active unit. For many entries it is not obvious how to go from information in the deposited entry to the active form. The EBI deserves credit and gratitude from the entire field for its success not only in creating databases, but for a large amount of extremely useful and well-documented software for data retrieval and analysis.

![](images/page_192_image_6.jpg)

**See Weblems 4.5 – 4.10**

## Classifications of protein structures

Several websites offer hierarchical classifications of all proteins of known structure according to their folding patterns:

SCOP: Structural Classification of Proteins;
• CATH: Class/Architecture/Topology/Homology;
• DALI: based on extraction of similar structures from distance matrices;
• CE: a database of structural alignments.

These sites are useful general entry points to protein structural data. For instance, SCOP offers facilities for searching on keywords to identify structures, navigation up and down the hierarchy, generation of pictures, access to the annotation records in the PDB entries, and links to related databases (See Chapter 6).

![](images/page_192_image_16.jpg)

**See Weblem 4.11**

## Accuracy and precision of protein structure determinations

## X-ray crystallography

X-ray crystallography produces estimates of the position of the atoms in a molecule. It also produces estimates of their effective sizes, called B factors. An important feature of the experimental data (usually measured are the absolute values of the Fourier coefficients of the electron density) is that all atoms contribute to all observations. It is difficult to estimate errors in individual atomic positions. For small molecules, forming well-ordered crystals, B factors reflect thermal vibrational amplitudes. For protein crystal structures B factors are a useful index of the precision of the position of the individual atoms. B factors for proteins do not report vibrational amplitudes exclusively, but include contributions from conformational variability. (A colleague who read this page in draft muttered darkly that for many protein structure determinations B factors ‘cover a multitude of sins’.) Indeed, crystal structure determinations are at the mercy of the degree of order in different parts of the molecule. (Order is the extent to which different unit cells of the crystal are exact and static copies of one another.) The degree of order governs the available resolution of the experimental data. Resolution is an index of potential quality of an X-ray structure determination, measuring the ratio of the number of parameters to be determined to the number of observations. In structure determinations of small organic molecules or of minerals this ratio is usually generous: ≈10. But for a typical protein crystal:

<table><tr><td></td><td colspan="6">Low resolution ... High</td></tr><tr><td>Resolution in Å</td><td>4.0</td><td>3.5</td><td>3.0</td><td>2.5</td><td>2.0</td><td>1.5</td></tr><tr><td>Ratio of observations to parameters</td><td>0.3</td><td>0.4</td><td>0.6</td><td>1.1</td><td>2.2</td><td>3.8</td></tr></table>

Resolution measures the fineness of the details that can be distinguished; hence, the lower the number, the higher the resolution.

In addition to disorder, errors in crystal structures reflect errors in both data measurement and solving the structure. A comparison of four independently solved structures of interleukin-1β showed an average variation in atomic position of 0.84 Å, higher than the expected experimental error.

Many crystallographers deposit their experimental data along with the solved structures. This permits detailed checks on the results. But in many cases the experimental data are not available. How can one then assess the quality of a structure? B factors provide important clues; high B factors in an entire region suggest that the region is not well determined. This usually reflects imperfect order in the crystal. Programs can flag stereochemical outliers: exceptions to regularities common to well-determined protein structures. The entries corresponding to the wwPDB entries in [http://www.cmbi.kun.nl/gv/pdbreport](http://www.cmbi.kun.nl/gv/pdbreport) describe diagnostic analysis and identification of problems and outliers.

But although outliers are relatively easy to detect, it is difficult to decide whether they are correct but unusual features of the structure, or the result of errors in building the model, or the inevitable result of crystal disorder. Proper assessment requires access to the experimental data; and fixing real errors may well require the attention of an experienced crystallographer. The conclusion seems inescapable that structure factors should be archived and available.

## Nuclear magnetic resonance

Nuclear magnetic resonance (NMR) is the second major technique for determining macromolecular structure. It produces structures that are correct in topology but often not as precise as a good X-ray structure determination. Crystallographers report a single structure, or only a small number. NMR spectroscopists usually produce a family of ≈10–20 related structures or even more, calculated from the same experimental data. Comparison across such an ensemble indicates precision; regions in which the local variation in structure is small are well defined by the data. This is a rough equivalent of the crystallographer's B factor.

There are two sources of structural variation among the models reported by NMR spectroscopists. One is genuine dynamic disorder, arising because the conformation is not locked in by crystal packing forces. The other is an uncomfortably low ratio of measurements to parameters that need to be determined. As a result, several different conformations may fit the experimental data comparably well.

Analysis of NMR measurements can distinguish these effects, but is carried out in only a minority of NMR protein structure determinations.

## Specialized, or ‘boutique’ , databases

Many individuals or groups select, annotate, and recombine data focused on particular topics, and include links affording streamlined access to information about subjects of interest. For instance, the protein kinase resource is a specialized compilation that includes sequences, structures, functional information, laboratory procedures, lists of interested scientists, tools for analysis, a bulletin board, and links.

The HIV protease database archives structures of human immunodeficiency virus 1 proteinases, human immunodeficiency virus 2 proteinases, and simian immunodeficiency virus proteinases, and their complexes, and provides tools for their analysis and links to other sites with AIDS-related information. This database contains some crystal structures not deposited in the PDB.

In the field of immunology:

IMGT, the international immunogenetics database, is a high-quality integrated database specializing in immunoglobulins (Ig), T-cell receptors (TcR), and major histocompatibility complex (MHC) molecules of all vertebrate species. The IMGT server provides a common access to all immunogenetics data. It includes IMGT/LIGM-DB, a comprehensive database of immunoglobulin and TcR gene sequences from human and other vertebrates, with translation for fully annotated sequences, and IMGT/MH-DB, a database of the human MHC, or human leucocyte antigens (HLA). See [http://www.imgt.org](http://www.imgt.org).
IEDB, the Immune Epitope Database and Analysis Resource, curated at the La Jolla Institute for Allergy and Immunology, containing data related to antibody and T-cell epitopes. See [http://www.iedb.org](http://www.iedb.org).
• DIGIT, the Database of Immunoglobulins with Integrated Tools, collects annotated sequences of annotated immunoglobulin variable domains and tools for analysing them. See [http://biocomputing.it/](http://biocomputing.it/).
The site [http://www.antibodyresource.com/antibody-database.html](http://www.antibodyresource.com/antibody-database.html) lists 19 different sites with information related to the databases and software related to antibodies.

## Expression and proteomics databases

Recall the central dogma: DNA makes RNA makes protein. Genomic databases contain DNA sequences. Expression databases record measurements of mRNA levels. Some record expressed sequence tags (ESTs; short terminal sequences of cDNA synthesized from mRNA) describing patterns of gene transcription. Proteomics databases record measurements on proteins, describing patterns of gene translation.

Comparisons of expression patterns give clues to (1) the function and mechanism of action of gene products, (2) how organisms coordinate their control over metabolic processes in different conditions (for instance, yeast under aerobic or anaerobic conditions), (3) the variations in mobilization of genes at different stages of the cell cycle, or of the development of an organism, (4) mechanisms of antibiotic resistance in bacteria and consequent suggestion of targets for drug development, (5) the response to challenge by a parasite, and (6) the response to medications of different types and dosages, to guide effective therapy.

There are many databases of ESTs. In most, the entries contain fields indicating tissue of origin and/or subcellular location, state of development, conditions of growth, and quantitation of expression level. In GenBank the dbEST collection currently contains over 74 million entries, from 2551 species, led by those in Table 4.1.

Table 4.1 Species with largest number of entries in dbEST

| Species | Number of entries |
| --- | --- |
| Homo sapiens (human) | 8 704 790 |
| Mus musculus + domesticus (mouse) | 4 853 570 |
| Zea mays (maize) | 2 019 137 |
| Sus scrofa (pig) | 1 669 337 |
| Bos taurus (cattle) | 1 559 495 |
| Arabidopsis thaliana (thale cress) | 1 529 700 |
| Danio rerio (zebrafish) | 1 488 275 |
| Glycine max (soybean) | 1 461 722 |
| Triticum aestivum (wheat) | 1 286 372 |
| Xenopus (Silurana) tropicalis (western clawed frog) | 1 271 480 |
| Oryza sativa (rice) | 1 253 557 |
| Ciona intestinalis | 1 205 674 |
| Rattus norvegicus + sp. (rat) | 1 162 136 |
| Drosophila melanogaster (fruit fly) | 821 005 |
| Panicum virgatum (switchgrass) | 720 590 |
| Xenopus laevis (African clawed frog) | 677 911 |
| Oryzias latipes (Japanese medaka) | 666 891 |
| Brassica napus (oilseed rape) | 643 881 |
| Gallus gallus (chicken) | 600 434 |
| Bombyx mori (domestic silkworm) | 568 825 |
| Hordeum vulgare + subsp. vulgare (barley) | 501 838 |
| Salmo salar (Atlantic salmon) | 498 245 |
| Vitis vinifera (wine grape) | 446 664 |
| Caenorhabditis elegans (nematode) | 396 687 |
| Phaseolus coccineus | 391 150 |
| Porphyridium cruentum | 386 903 |
| Canis lupus familiaris (dog) | 382 638 |

Some EST collections are specialized to particular tissues (e.g. muscle, tooth) or to species. In many cases there is an effort to link expression patterns to other knowledge of the organism. For instance, the Jackson Lab Gene Expression Information Resource Project for Mouse Development coordinates data on gene expression and developmental anatomy.

Many databases provide connections between ESTs in different species, for instance, linking human and mouse homologues, or relationships between human disease genes and yeast proteins. Other EST collections are specialized to a type of protein, for instance cytokines. A large effort is focused on cancer: integrating information on mutations, chromosomal rearrangements, and changes in expression patterns, to identify changes during tumour formation and progression.

Although of course there is a close relationship between patterns of transcription and patterns of translation, direct measurements of protein contents of cells and tissues—proteomics—provides additional valuable information. Because of differential rates of translation and turnover of different mRNAs, measurements of proteins directly give a more accurate description of patterns of gene expression than measurements of transcription. Post-translational modifications can be detected only by examining the proteins.

Proteome analysis involves separation, identification, and quantitative determination of amounts of proteins present in the sample (See Chapter 9). Proteome databases store images of gels, and their interpretation in terms of protein patterns. For each protein, an entry typically records:

• identification of protein;
relative amount;
• function;
mechanism of action;
• expression pattern;
subcellular localization;
• related proteins;
• post-translational modifications;
• interactions with other proteins;
links to other databases.

![](images/page_196_image_15.jpg)

## See Weblem 4.12

## Bibliographic databases

Medline (based at the US National Library of Medicine) integrates the medical literature, including very many papers dealing with subjects in molecular biology that are not overtly clinical in content. It is included in PubMed, a bibliographical database offering abstracts of scientific articles, integrated with other information-retrieval tools of the NCBI in the National Library of Medicine ([http://www.ncbi.nlm.nih.gov/PubMed/](http://www.ncbi.nlm.nih.gov/PubMed/)).

One very effective feature of PubMed is the option to retrieve related articles. This is a very quick way to ‘get into’ the literature of a topic. Combined with the use of a general search engine for websites that do not correspond to articles published in journals, fairly comprehensive information is readily available about most subjects. Here's a tip: if you are trying to start to learn about an unfamiliar subject, try adding the keyword tutorial to your search in a general search engine, or the keyword review to your search in PubMed.

Almost all scientific journals now place their tables of contents, and in many cases their entire issues, on websites. The US National Institutes of Health have established a centralized web-based library of scientific articles, called PubMed Central ([http://www.pubmedcentral.nih.gov/](http://www.pubmedcentral.nih.gov/)). In collaboration with scientific journals, the NCBI is organizing the electronic distribution of the full texts of published articles.

## Surveys of molecular biology databases and servers

Lists of web resources in molecular biology are very common. It is difficult to explore any topic in molecular biology on the web without quickly bumping into a list of this nature. They contain, to a large extent, the same information, but vary widely in their ‘look and feel’. The real problem is that unless they are curated they tend to degenerate into lists of dead links. (A draft of this section featured a reference to a website that contained a reasonable survey. Returning to it 2 months later, the name of the site had changed and over half of the links had disappeared.)

This book does not contain a long annotated list of relevant and recommended sites, for the following reasons: (1) you don't want a long list, you need a short one and (2) the web is too volatile for such a list to stay useful for very long. It is much more ef ective to use a general search engine to find what you want at the moment you want it.

My advice is this: spend some time browsing; it won't take you long to find a site that appears reasonably stable and has a style compatible with your methods of work. Alternatively, the ExPASy site (see the section on The Swiss Institute for Bioinformatics) is comprehensive and shows signs of a commitment to remaining comprehensive and up to date.

![](images/page_197_image_5.jpg)

**See Weblem 4.13**

## Gateways to archives

Databases in molecular biology maintain facilities for a very wide variety of information-retrieval and -analysis operations. Categories of these operations include the following.

1. Retrieval of sequences from a database. Sequences can be ‘called up’ on the basis of either features of the annotations or patterns found within the sequences themselves.
2. Sequence comparison. This is not a facility, this is a heavy industry! It was introduced in Chapter 1 and will be discussed in detail in Chapter 5. It includes the very important searches for relatives.
3. Identification of genes in genome sequences, and translation of protein-coding gene sequences to amino acid sequences.
4. Simple types of structure analysis and prediction, for example statistical methods for predicting the secondary structure of proteins from sequences alone, including hydrophobicity profiles, from which the transmembrane proteins can generally be identified. Other sites offer full threedimensional sequence-to-structure prediction.
5. Pattern recognition. It is possible to search for all sequences containing a pattern or combination of patterns, expressed as probabilities for finding certain sets of residues at consecutive positions. These patterns may extend over large regions of the sequence. Such patterns reflect the global folding pattern of a protein. Other patterns are short. In DNA sequences these patterns may reflect recognition sites for enzymes such as those responsible for splicing together interrupted genes. In proteins, short and localized patterns generally identify molecules that share a common function.
6. Molecular graphics are necessary to provide intelligible depictions of very complicated systems.

Typical applications of molecular graphics include:

• giving a useful overall impression of a protein folding pattern;
mapping residues believed to be involved in function on to the three-dimensional framework of a protein. Often this will isolate an active site;
• classifying and comparing the folding patterns of proteins;
analysing changes between closely related structures, or between two conformational states of a single molecule, and;
• studying the interaction of a small molecule with a protein, in order to attempt to assign function, or for drug development;
interactive fitting of a model to the noisy and fuzzy image of the molecule that arises initially from the measurements in solving protein structures by X-ray crystallography;
• design and modelling of new structures.

## Access to databases in molecular biology

## How to learn web skills

It would be difficult to learn to ride a bicycle by reading a book describing the sets of movements required, much less a treatise on the theory of the gyroscope. Similarly, the place to learn web skills is at a terminal, running a browser. True enough, but there is always a certain initial period of difficulty and imbalance. Here the goal is only to provide some temporary assistance to get you started. Then, off you go!

This section contains introductions to some of the major data banks and information-retrieval systems in molecular biology. In each case the illustrations show relatively simple searches and applications. When appropriate, unique features of each system will be emphasized.

## ENTREZ

The NCBI maintains databases and avenues of access to them. ENTREZ offers access via 35 database divisions (see Table 4.2).

Table 4.2 The ENTREZ database system of the NCBI

| Name | Contents |
| --- | --- |
| Nucleotide | Core subset of nucleotide sequence records |
| EST | Expressed sequence tag records |
| GSS | Genome Survey Sequence records |
| Protein | Sequence database |
| Genome | Whole-genome sequences |
| Structure | Three-dimensional macromolecular structures |
| Taxonomy | Organisms in GenBank |
| SNP | Short genetic variations |
| dbVar | Genomic structural variation |
| Gene | Gene-centred information |
| SRA | Sequence Read Archive |
| BioSystems | Pathways and systems of interacting molecules |
| HomoloGene | Eukaryotic homology groups |
| OMIM | Online Mendelian Inheritance in Man |
| OMIA | Online Mendelian Inheritance in Animals |
| Probe | Sequence-specific reagents |
| BioProject | Aggregated biological research project data |
| dbGaP | Genotype and phenotype |
| UniGene | Gene-oriented clusters of transcript sequences |
| CDD | Conserved protein domain database |
| Clone | Integrated data for clone resources |
| UniSTS | Markers and mapping data |
| PopSet | Population study data sets |
| GEO Profiles | Expression and molecular abundance profiles |
| GEO DataSets | Experimental sets of Gene Expression Omnibus (GEO) data |
| Epigenomics | Epigenetic maps and data sets |
| PubChem BioAssay | Bioactivity screens of chemical substances |
| PubChem Compound | Unique small molecule chemical structures |
| PubChem Substance | Deposited chemical substance records |
| Protein Clusters | A collection of related protein sequences |
| BioSample | Biological material description |
| PubMed | Biomedical literature citations and abstracts |
| PubMed Central | Free, full-text journal articles |
| Site Search | NCBI web and ftp sites |
| Books | Online books |

For a diagram showing all component ENTREZ databases, and the connections among them, see [http://www.ncbi.nlm.nih.gov/Database/datamodel/index.html](http://www.ncbi.nlm.nih.gov/Database/datamodel/index.html). The integration of the various databases, at least from the point of view of the search engines, are a strong point of NCBI's system.

Let us pick a molecule—human neutrophil elastase—and search for relevant entries in the different sections of ENTREZ.

## Searches in the ENTREZ protein database

Go to [http://www.ncbi.nlm.nih.gov/entrez/](http://www.ncbi.nlm.nih.gov/entrez/). Select Protein, enter the search terms HUMAN ELASTASE, and click on Go.

The results, of course, will change with time as the databases grow. (Disclosure: what is presented here are the results from the time of preparation of the previous edition, which were substantially clearer and more focused than the current ones.)

Box 4.3 shows 14 ‘hits’: the first three, plus selected interesting results from further down the list. The top hit is LEUKOCYTE ELASTASE PRECURSOR. Other responses include elastases from other species, inhibitors, a leech protein, and a transcriptional regulator. (Why should a leech protein and a transcriptional regulator—which presumably interacts with

## Box 4.3 Selected ENTREZ responses to human elastase in the Protein database

## 1: P08246

Leukocyte elastase precursor (Elastase-2) (Neutrophil elastase) (PMN elastase) (Bone marrow serine protease) (Medullasin) (Human leukocyte elastase) (HLE)

$$
\mathrm{gi} - 1 1 9 2 9 2 - \mathrm{sp} - \mathrm{P08246} - \text {ELNE\_HUMAN} [ 1 1 9 2 9 2 ]
$$

## 2: 1HNEE

Chain E, Human Neutrophil Elastase (HNE) (E.C.3.4.21.37) (Also Referred To As Human Leucocyte Elastase

```txt
(HLE)) Complex With Methoxysuccinyl-Ala-Ala-Pro-Ala Chloromethyl Ketone (MSACK) gi-230004-pdb-1HNE-E[230004]
```

## 3: 1PPFE

Chain E, Human Leukocyte Elastase (Hle) (Neutrophil Elastase (Hne)) (E.C.3.4.21.37) Complex With The Third Domain Of Turkey Ovomucoid Inhibitor (Omtky3)

```txt
gi - 809343 - pdb - 1PPF - E[809343]
```

…

## 14: P30740

Leukocyte elastase inhibitor (LEI) (Serpin B1) (Monocyte/neutrophil elastase inhibitor) (M/NEI) (EI)

```json
gi - 266344 - sp - P30740 - ILEU_HUMAN[266344]
```

## 15: AAB20263

Alzheimer's beta-amyloid precursor protein, Kunitz-type protease inhibitor, neutrophil elastase inhibitor, P1-Val-APP-KD [human, Peptide Partial Mutagenesis, 17 aa]

```txt
gi - 238492 - gb - AAB20263.1 -- bbm - 163757 - bbs - 65057[238492]
```

…

## 166: NP\_835455

pancreas specific transcription factor, 1a [Homo sapiens]

```json
gi - 30039710 - ref - NP_835455.1 - [30039710]
```

## 167: P23352

Anosmin-1 precursor (Kallmann syndrome protein) (Adhesion molecule-like X-linked)

```txt
gi - 134048661 - sp - P23352 - KALM_HUMAN[134048661]
```

## 168: NP\_982283

Notch homolog 2 N-terminal like protein [Homo sapiens]

```txt
gi - 46397353 - ref - NP_982283.2 - [46397353]
```

…

## 256: AAH76933

Elastase 2, neutrophil [Xenopus tropicalis]

```txt
gi - 49899920 - gb - AAH76933.1 - [49899920]
```

## 257: 1FZZA

Chain A, The Crystal Structure Of The Complex Of Non-Peptidic Inhibitor Ono-6818 And Porcine Pancreatic Elastase.

```txt
gi - 16975403 - pdb - 1FZZ - A[16975403]
```

## 258: BAA00166

pancreatic elastase 2 precursor [Sus scrofa]

```json
gi - 217686 - dbj - BAA00166.1 - [217686]
```

…

## 262: NP\_493468

human KALlmann syndrome homolog family member (kal-1) [Caenorhabditis elegans]

```json
gi - 25149859 - ref - NP_493468.2 - [25149859]
```

## 263: AAH95070

Elastase 3 like [Danio rerio]

```json
gi-63101424-gb-AAH95070.1-[63101424]
```

…

DNA, not protein—show up in a search for human elastase?) We shall see how to tune the query to eliminate these extraneous responses.

The format of the responses is as follows: in each case, the first line contains an identifier, its form reflecting the source database. For example, in the first response, P08246 is a SWISS-PROT accession number; in the second, 1HNEE signifies chain E of wwPDB entry 1HNE. The next line gives the name and synonyms of the molecule, and the species of origin. Note that Greek letters are spelt out. The last line gives references to the source data banks: gi = geninfo identifier (see Box 1.7); gb = GenBank accession number; sp = SWISS-PROT; pdb = Protein Data Bank; pir = Protein Identification Resource; dbj = DNA Data Bank of Japan; ref = the Reference Sequence project of NCBI. The entries retrieved include elastases from human and other species, and also inhibitors of elastase.

Opening the entry that corresponds to the first hit retrieves a file containing the material shown in the Box 4.4. (The entire file is 469 lines long.) The

Box 4.4 US NCBI ENTREZ Protein database entry for human leukocyte elastase precursor

```csv
LOCUS     P08246 267 aa linear PRI 01-MAY-2007
DEFINITION Leukocyte elastase precursor (Elastase-2) (Neutrophil elastase)
(PMN elastase) (Bone marrow serine protease) (Medullasin) (Human
leukocyte elastase) (HLE).
ACCESSION  P08246
VERSION    P08246 GI:119292
DBSOURCE   swissprot: locus ELNE_HUMAN, accession P08246;
          class: standard.
          extra accessions:P09649,Q6B0D9,Q6LDP5
          created: Aug 1, 1988.
          sequence updated: Aug 1, 1988.
          annotation updated: May 1, 2007.
          xrefs: Y00477.1, CAA68537.1, M20203.1, AAA36359.1, M20199.1,
                  M20200.1, M20201.1, M34379.1, AAA36173.1, AY596461.1,
AAS89303.1,
          BC074816.2, AAH74816.1, BC074817.2, AAH74817.1, D00187.1,
          BAA00128.1, X05875.1, CAA29299.1, CAA29300.1, J03545.1,
AAA52378.1,
          M27783.1, AAA35792.1, ELHUL, 1B0FA, 1H1BA, 1H1BB, 1HNEE, 1PPFE,
          1PPGE
          xrefs (non-sequence databases): UniGene:Hs.99863,
MEROPS:S01.131,
          Ensembl:ENSG00000197561, KEGG:hsa:1991, HGNC:3309, MIM: 130130,
          MIM: 162800, DrugBank:BTD00002, LinkHub:P08246,
          ArrayExpress:P08246, GermOnline:ENSG00000197561,
           RZPD-ProtExp:F0319, GO:0009986, GO:0005576, GO:0008367,
GO:0019955,
          GO:0042708, GO:0006874, GO:0045079, GO:0050922, GO:0050728,
          GO:0045415, GO:0045416, GO:0043406, GO:0048661, GO:0030163,
```

```txt
GO:0009411, InterPro:IPR009003, InterPro:IPR001254,
InterPro:IPR001314, Gene3D:G3DSA:2.40.10.10, PANTHER:PTHR19355,
Pfam:PF00089, PRINTS:PR00722, SMART:SM00020, PROSITE:PS50240,
PROSITE:PS00134, PROSITE:PS00135
KEYWORDS 3D-structure; Direct protein sequencing; Disease mutation;
Glycoprotein; Hydrolase; Polymorphism; Protease; Serine protease;
Signal.
SOURCE Homo sapiens (human)
ORGANISM Homo sapiens
Eukaryota; Metazoa; Chordata; Craniata; Vertebrata;
Euteleostomi;
Mammalia; Eutheria; Euarchontoglires; Primates; Haplorrhini;
Catarrhini; Hominidae; Homo.
REFERENCE 1 (residues 1 to 267)
AUTHORS Nakamura,H., Okano,K., Aoki,Y., Shimizu,H. and Naruto,M.
TITLE Nucleotide sequence of human bone marrow serine protease (medullasin) gene
JOURNAL Nucleic Acids Res. 15 (22), 9601-9602 (1987)
PUBMED 3479752
REMARK NUCLEOTIDE SEQUENCE [GENOMIC DNA].
```

Material omitted …

```txt
COMMENT On or before Mar 21, 2006 this sequence version replaced
gi:74757422, gi:74724761, gi:67584.
[FUNCTION] Modifies the functions of natural killer cells,
monocytes and granulocytes. Inhibits C5a-dependent neutrophil
enzyme release and chemotaxis.
[CATALYTIC ACTIVITY] Hydrolysis of proteins, including elastin.
Preferential cleavage: Val- - -Xaa > Ala- - -Xaa.
[TISSUE SPECIFICITY] Bone marrow cells.
[DISEASE] Defects in ELA2 are a cause of cyclic haematopoiesis
(CH)
[MIM:162800]; also known as cyclic neutropenia. CH is an
autosomal
dominant disease in which blood-cell production from the bone
marrow oscillates with 21-day periodicity. Circulating
neutrophils
vary between almost normal numbers and zero. During intervals of
neutropenia, affected individuals are at risk for opportunistic
infection. Monocytes, platelets, lymphocytes and reticulocytes
also
cycle with the same frequency.
[SIMILARITY] Belongs to the peptidase S1 family. Elastase
subfamily.
[SIMILARITY] Contains 1 peptidase S1 domain.
[WEB RESOURCE] NAME=GeneReviews;
URL='http://www.genetests.org/query?gene=ELA2'.
[WEB RESOURCE] NAME=Wikipedia elastase entry;
URL='http://en.wikipedia.org/wiki/Elastase'.
FEATURES Location/Qualifiers
source 1..267
/organism="Homo sapiens"
/db_xref="taxon:9606"
```

```csv
gene 1..267
/gene="ELA2"
Protein 1..267
/gene="ELA2"
/product="Leukocyte elastase precursor"
/EC_number="3.4.21.37"
Region 30..267
/gene="ELA2"
/region_name="Mature chain"
/experiment="experimental evidence, no additional details recorded"
/note="Leukocyte elastase. /FTId=PRO_0000027704."]
Bond bond (55,71)
/gene="ELA2"
/bond_type="disulfide"
/experiment="experimental evidence, no additional details recorded"
Region 64..67
/gene="ELA2"
/region_name="Beta-strand region"
/experiment="experimental evidence, no additional details recorded"
Site 70
/gene="ELA2"
/site_type="active"
/experiment="experimental evidence, no additional details recorded"
/note="Charge relay system."
ORIGIN
1 mtlgrrlacl flacvlpall lggtalasei vggrrarpha wpfmvslqlr gghfcgatli
61 apnfvmsaah cvanvnvrav rvvlgahnls rreprqvfa vqrifengyd pvnllndivi
121 lqlngsatin anvqvaqlpa qgrrlgngvq clamgwgllg rnrgiasvlq elnvtvvtsl
181 crrsnvctlv rgrqagvcfg dsgsplvcng lihgiasfvr ggcasglypd afapvaqfvn
241 widsiiqrse dnpcphprdp dpasrth
//
```

first lines are mostly database housekeeping, such as accession numbers, molecule name, and date of deposition. Then comes descriptive material such as the source, in this case human, with the full taxonomic classification; credit to the scientists who deposited the entry; and literature references. There are extensive cross-references to other data banks. Finally is the particular scientific information: the location of the gene and its product (CDS = coding sequence), and the sequence (see Exercise 4.2). Again, note that the sequence itself occupies quite a small portion of the entry.

![](images/page_203_image_2.jpg)

## See Weblem 4.14

![](images/page_203_image_4.jpg)

## See Weblem 4.15

Many literature references, and many feature table entries, have been omitted. Keywords (site types or region names) associated with feature table entries include: Helical region, Beta-strand region, Domain, Hydrogen bonded turn, Disulphide bridge, Mature chain, Propeptide, Signal, Tryp\_SPc (signifying membership in the trypsin-like serine protease family), Variant (for example, an observed

SNP), Substrate-binding site, Charge relay system, and Glycosylation site.

## Searches in ENTREZ Gene database

Next we look again for HUMAN ELASTASE, this time in the Gene database. On the ENTREZ page, select Nucleotide from the pulldown menu at the left, type the following into the box following the word for, and then execute the search:

HOMO SAPIENS[ORGANISM] AND LEUKOCYTE[TITLE]

AND ELASTASE[TITLE] NOT INHIBITOR[TEXT WORD]

The search returns two hits, including DNA (see Box 4.5) and mRNA.

Box 4.5 The gene for human neutrophil elastase in the ENTREZ CoreNucleotide database

```txt
LOCUS Y00477 5292 bp DNA linear PRI 14-NOV-2006
DEFINITION Human bone marrow serine protease gene (medullasin) (leukocyte neutrophil elastase gene).
ACCESSION Y00477
VERSION Y00477.1 GI:34529
KEYWORDS elastase; medullasin; serine protease.
SOURCE Homo sapiens (human)
ORGANISM Homo sapiens
Eukaryota; Metazoa; Chordata; Craniata; Vertebrata;
Euteleostomi;
Mammalia; Eutheria; Euarchontoglires; Primates; Haplorrhini;
Catarrhini; Hominidae; Homo.
REFERENCE 1 (bases 1 to 5292)
AUTHORS Nakamura,H., Okano,K., Aoki,Y., Shimizu,H. and Naruto,M.
TITLE Nucleotide sequence of human bone marrow serine protease (medullasin) gene
JOURNAL Nucleic Acids Res. 15 (22), 9601-9602 (1987)
PUBMED 3479752
REFERENCE 2 (bases 1 to 5292)
AUTHORS Naruto,M.
TITLE Direct Submission
JOURNAL Submitted (09-NOV-1987) Naruto M., Basic Research Laboratories, Toray Insustries, Inc., 1111 Tebiro, Kamakura 248, Japan
COMMENT This cDNA encodes the full protein sequence of human leukocyte (neutrophil) elastase (HLE), which was reported by Sinha et al.
in
PNAS USA 84:2228-2232(1987).
FEATURES Location/Qualifiers
source 1..5292
/organism="Homo sapiens"
/mol_type="genomic DNA"
/db_xref="taxon:9606"
/clone_lib="tonsil genomic library in lambda gt WES lambda
```

B"

```txt
repeat_region 287..551
            /note="tandemly arranged direct repeats"
CAAT_signal 1114..1118
TATA_signal 1230..1234
CDS join(1287..1353,1786..1942,2173..2314,4485..4715,
            4882..5088)
            /codon_start=1
            /product=βerine protease"
            /protein_id="CAA68537.1"
            /db_xref="GI:296665"
            /db_xref="GDB:118792"
            /db_xref="GOA:P08246"
            /db_xref="HGNC:3309"
            /db_xref=InterPro:IPR001254"
            /db_xref=InterPro:IPR001314"
            /db_xref=InterPro:IPR009003"
            /db_xref="PDB:1B0F"
            /db_xref="PDB:1H1B"
            /db_xref="PDB:1HNE"
            /db_xref="PDB:1PPF"
            /db_xref="PDB:1PPG"
            /db_xref=UniProtKB/Swiss-Prot:P08246"
            /translation="MTLGRRLACLFLACVLPALLLGGTALASEIVGGRRARPHAWPFM
             VSLQLRGGHFCGATLIAPNFVMSAAHCVANVNVRAVRVVLGAHNLSRREPTRQVFAVQ
             RIFENGYDPVNLLNDIVILQLNGSATINANVQVAQLPAQGRRLGNGVQCLAMGWGLLG
             RNRGIASVLQELNVTVVTSLCRRSNVCTLVRGRQAGVCFGDSGSPLVCNGLIHGIASF
             VRGGCASGLYPDAFAPVAQFVNWIDSIIQRSEDNPCPHPRDPDPASRTH"
sig_peptide join(1287..1353,1786..1805)
mat_peptide join(1806..1942,2173..2314,4485..4715,4882..5085)
            /product=unnamed"
exon <1287..1353
                /number=1
intron 1354..1785
                /number=1
exon 1786..1942
                /number=2
intron 1943..2172
                /number=2
exon 2173..2314
                /number=3
intron 2315..4484
                /number=3
repeat_region 2538..2957
                /note="tandemly arranged direct repeats"
exon 4485..4715
                /number=4
intron 4716..4881
                /number=4
exon 4882..>5088
                /number=5
polyA_signal 5146..5151
ORIGIN
```

1 ttgtcagagc cccagctggt gtccagggac tgaccgtgag cctgggtgaa agtgagttcc

| 61 | ccgttggagg | caccagacga | ggagaggatg | gaaggcctgg | cccccaagaa | tgagccctga |
| --- | --- | --- | --- | --- | --- | --- |
| 121 | ggttcaggag | cggctggagt | gagccgcccc | cagatctccg | tccagctgcg | ggtcccagag |
| 181 | gcctgggtta | cactcggagc | tcctggggga | ggcccttgac | gtgctcagtt | cccaaacagg |
| 241 | aaccctggga | aggaccagag | aagtgcctat | tgcgcagtga | gtgcccgaca | cagctgcatg |
| 301 | tggccggtat | cacagggccc | tgggtaaact | gaggcaggcg | acacagctgc | atgtggccgg |
| 361 | tatcacaggg | ccctgggtaa | actgaggcag | gcgacacagc | tgcatgtggc | cggtatcaca |
| 421 | gggccctggg | taaactgagg | caggcgacac | agctgcatgt | ggccggtatc | acagggccct |
| 481 | gggtaaactg | aggcaggcga | cacagctgca | tgtggccggt | atcacggggc | cctggataaa |
| 541 | cagaggcagg | cgaggccacc | cccatcaagt | ccctcaggtc | taggtttggc | caggtttgga |
| 601 | aaaacacagc | aacgctcggt | aatctgaat | ttcgggtaag | tatatcctgg | gcctcatttg |
| 661 | gaagagactt | agattaaaaa | aaaaacgtcg | agaccagccc | ggccaacacg | tgaaaccccg |
| 721 | tctctactaa | aaatacaaaa | aattagccag | gcgcagtgt | cacgcctgtg | atcccagcac |
| 781 | tctgggaggt | gaggcaggcg | gatcacccga | ggtcagctgt | tcaagaccag | cctggccgag |
| 841 | tgggcgaaac | actgtctcta | ctacaaatac | aaaaattagc | cgggagtgg | ggcaggtgcc |
| 901 | tgtaatctca | gctattcagg | aggctgaggc | aggagaatca | cttgaacctg | ggaggcggag |
| 961 | gttgccgtga | gccgggatca | cgccaccgca | ctccagcctg | ggcgatagag | caagactctg |
| 1021 | tctccaaaaa | aataaattaa | aaaacccaca | ttgattatct | gacatttgaa | tgcgattgtg |
| 1081 | catcctgaat | tttgtctgga | ggccccaccc | gagccaatcc | agcgtcttgt | cccccttctc |
| 1141 | ccccttttca | tcaacgcctg | tgccagggga | gaggaagtgg | agggcgctgg | ccggccgtgg |
| 1201 | ggcaatgcaa | cggcctccca | gcacagggct | ataagaggag | ccgggcgggc | acggaggggc |
| 1261 | agagaccccg | gagccccagc | cccaccatga | ccctcggccg | ccgactcgcg | tgtcttttcc |
| 1321 | tcgcctgtgt | cctgccggcc | ttgctgctgg | ggggtgagtt | tttgagtcca | acctcccgct |
| 1381 | gctccctctg | tcccgggttc | tgttcccacc | tctccataga | gggccccacc | agtgtgggtc |
| 1441 | cctcatcctc | acaggggagg | tgccagctgg | gacaaggaga | ccagaagaga | ctgaggttct |
| 1501 | gagcgtgaa | gccaccacca | ggagcccaga | gttggggttt | gaaaaccggg | gagggggggg |
| 1561 | gtggcaggtc | gccctctggg | ttcaagtcca | ggtctgtctg | tgccttggag | gggcaccgtg |
| 1621 | gggaggtccc | tttgcctctc | cgtgcctcag | tttcctcatc | tgaacaacag | gggtgcgaac |
| 1681 | ggccccgatc | ccgtgggttc | ccggtggggg | atccagaggc | cccgtggccg | ggaggggaca |
| 1741 | ggctccttgg | caggcactca | gcacccgcac | ccggtgtgtc | cccaggcacc | gcgctggcct |
| 1801 | cggagattgt | ggggggccgg | cgagcgcggc | cccacgcgtg | gcccttcatg | gtgtccctgc |
| 1861 | agctgcgcgg | aggccacttc | tgcggcgcca | ccctgattgc | gcccaacttc | gtcatgtcgg |
| 1921 | ccgcgcactg | cgtggcgaat | gtgtgagtag | ccgggagtgt | gcgcgccgg | ctcggacccc |
| 1981 | gcgtccccggt | ctgtgaggtg | ggtggggga | ggccggggcc | ggggctgctg | gcgggggggg |
| 2041 | gtccgtccag | ggcccgcggg | gcccctcgag | caccttcgcc | ctcaggcccg | tcgccggatg |
| 2101 | gggacgacaa | ggcgcggctg | agccccgacc | cccggggccg | cccctgagcc | ccgcctctcc |
| 2161 | ctcttttggc | agaaacgtcc | gcgcggtgcg | ggtggtcctg | ggagcccata | acctctcgcg |
| 2221 | gcgggagccc | acccggcagg | tgttcgccgt | gcagcgcatc | ttcgaaaacg | gctacgaccc |
| 2281 | cgtaaacttg | ctcaacgaca | tcgtgattct | ccaggtgccg | ccgggcgggc | gggggcgagg |
| 2341 | ggcggaggcc | agaggcctgg | ggaggtgga | ggcctgggga | gggtggaggc | tgcgacggag |
| 2401 | gggcgcgtcg | gggccgctcg | tggggacctg | gggtggcatc | gtgggctggg | tggtcccctc |
| 2461 | tccgcgcctc | ggtctgcacc | tctgtgaaac | gggaaaatac | ccgccatggg | ccgttgaggg |
| 2521 | gttaaatgag | atcctgcagg | gaggccccga | tctgctgtca | atcaacaaac | ttactgagaa |
| 2581 | gggaggcccc | gatctgttgt | caatcaacaa | acttactgag | aagggaggcc | ccgatctgtt |
| 2641 | gtcaatcaac | aaacttactg | agaagggagg | ccccgatctg | ctgtcaatca | acaaacttac |
| 2701 | tgagaaggga | ggccccgatg | ttgtcaatca | acaaacttac | tgagaaggga | ggccccgatc |
| 2761 | tgctgtcaat | caaccaaaact | tactgagaag | ggaggccccg | atctgctgtc | aatcatcaaa |
| 2821 | cttactgaga | agggaggccc | cgatctgctg | tcaatcaaca | aacttactga | gaagggaggc |
| 2881 | ccccgatctg | ttgtcaatca | acaaacttac | tgagaaggga | ggccccgatc | tgctgtcaat |
| 2941 | caacaaactt | actgagattc | tgtgtgtctc | tccattcacc | agtcctgtgg | cccagggcag |
| 3001 | gggccgcctc | tgtctttggg | aaaaggggca | aaagtcccca | cctttccacc | cctgtccgcg |
| 3061 | gcttgcagtt | ctggttattt | cctgggcgcc | gggccccgtg | gctcaggcct | gtcatcccag |
| 3121 | cactttggga | ggctgaggcg | ggtggatcac | gaggtcaggt | gttcgagacc | agcctgagca |
| 3181 | acatagtgaa | accccgtctc | tactaaaata | cacaaaaaaa | aaattagccg | agtgtggttg |
| 3241 | tgggtgcctg | taatgccaac | tactcaggag | gctgaggaag | gagaatcgct | tgaaccccgg |
| 3301 | aggcggagat | tgcagtgc | tgagatcaca | ccactgcact | ccagcctggg | tctcaaaaaa |
| 3361 | aaaaaaaaag | attcctccct | gggaaggtt | agagggagag | tttccttgtc | actaagtttt |
| 3421 | ctcatagctc | tcacccagtg | cagtggcgcg | atcgcagctc | actacacctc | catctcctgg |
| 3481 | gctcaagcca | ccctctcagc | ttggaatggg | gggtagctgg | aaccacaggt | gccaccacgt |
| 3541 | ggtccaccac | gtctggctaa | tatatatata | tacacacaca | catacatata | ttataaataa |
| 3601 | taaatatata | ttttatttaa | ataaaatata | taatatttat | aattatttta | taattataat |
| 3661 | aatatttata | taattataaa | tatcatttat | aattataata | tttattattt | tataaaataa |
| 3721 | taaatataaa | atatataaaa | atatttttat | aaataataaa | atatatatat | acacacatat |
| 3781 | atatatattt | tttgagacaa | gtctcgctct | gtcgcccagg | ctggagcgca | gtgcacaatc |
| 3841 | tcactcactg | cacctccgcc | tcccaggttc | aagcgattct | cctgcctcag | cctcccaggt |
| 3901 | agctgggact | acaggcgccc | gccaccacgc | ctggctaatt | tttggtattg | ttagtagaga |
| 3961 | cggggtttaa | ccatgttagc | caggatggtc | ttgatctcct | gaccttttga | ttggcccacc |
| 4021 | tcagcctccc | aaaatgctgg | gattataggc | gtgagcaccg | cacctggcaa | ttttttttta |
| 4081 | ttatttttgt | agacatgggg | ctttgccaca | ttgcccaggc | tggtcttgaa | tgcctggcct |
| 4141 | ggcctaagtg | atcctcctgc | ctcgccctcc | caaagtgctg | ggcttacaag | catgagccac |
| 4201 | cgcgccggc | tgtagttttt | ttgttaactg | agcacctact | gcttcctgca | ctcaagccac |
| 4261 | atccagggac | aacctccaac | gccctgagcc | ttggtgacgg | ctcccactct | acagatgggg |
| 4321 | aaaccgaggc | ttgccttggg | gagcagagtg | tggggtgggt | atcctgccct | gcaggatccc |
| 4381 | agaaccacag | tggaacctga | gatggggaaa | ctgaggcccg | gagaggggag | ggtcatcatc |
| 4441 | actgccccgt | gtgacgcgct | gacgatctgt | ccccaccgcc | acagctcaac | gggtcggcca |
| 4501 | ccatcaacgc | caacgtgcag | gtggcccagc | tgccggctca | gggacgccgc | ctgggcaacg |
| 4561 | gggtgcagtg | cctggccatg | ggctggggcc | ttctgggcag | gaaccgtggg | atcgccagcg |
| 4621 | tcctgcagga | gctcaacgtg | acggtggtga | cgtccctctg | ccgtcgcagc | aacgtctgca |
| 4681 | ctctcgtgag | gggccggcag | gccggcgtct | gtttcgtacg | tgccctgggt | gtccctctgc |
| 4741 | tccccacccg | ctcccagccc | ggtactgcag | caacaggcac | cgtggctaga | ccctaggatg |
| 4801 | ggacttccca | accctgacac | gtcggcgggc | aggtgggcag | ggcctcgcag | tccagcttcc |
| 4861 | ccaccttgtc | tgcctccaca | gggggactcc | ggcagcccct | tggtctgcaa | cgggctaatc |
| 4921 | cacggaattg | cctccttcgt | ccggggaggc | tgcgcctcag | ggctctaccc | cgatgccttt |
| 4981 | gccccggtgg | cacagtttgt | aaactggatc | gactctatca | tccaacgctc | cgaggacaac |
| 5041 | ccctgtcccc | acccccggga | cccgacccg | gccagcagga | cccactgaga | agggctgccc |
| 5101 | gggtcacctc | agctgcccac | acccacactc | tccagcatct | ggcacaataa | acattctctg |
| 5161 | ttttgtagaa | tgtgtttgat | gctccttggc | tgtgtgattg | ggtgttgaaa | atggtcagta |
| 5221 | ggtcgggcgt | ggtggctcac | acctgtaatc | ccagcacttt | gggaggttga | ggcaggcgga |
| 5281 | tcacttgagc | tc |  |  |  |  |

Compare this file with the result of searching in the Protein database (see Exercise 4.5).

## Searches in the bibliographic database PubMed

Perhaps it is time to look at what people have had to say about our molecule. Of course, the literature on elastase is huge. A search in PubMed for HUMAN ELASTASE returns 10 453 entries. To prune the results, let us try to find citations to articles describing the role of elastase in disease. A search for HUMAN ELASTASE DISEASE returns 2447 entries. What about specific elastase mutants related to human disease? A search for HUMAN ELASTASE DISEASE MUTATION returns 114 articles, in reverse chronological order. Here are the first eight.

1. Dickens JA, Lomas DA. Why has it been so difficult to prove the efficacy of alpha-1-antitrypsin replacement therapy? Insights from the study of disease pathogenesis. Drug Des Devel Ther. 2011;5:391–405.
2. Ye Y, Carlsson G, Wondimu B, Fahlén A, Karlsson-Sjöberg J, Andersson M, Engstrand L,