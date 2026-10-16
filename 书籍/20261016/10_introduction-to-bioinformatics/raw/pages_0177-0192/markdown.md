## LEARNING GOALS

• Understanding the general kinds of data describing the molecules and processes of life assembled in the data banks supporting research and applications in biology, medicine, agriculture, and technology.
• Knowing the basic infrastructure of bioinformatics, in terms of the sites and responsibilities of the major archival projects.
• Understanding the basic concepts of information retrieval, including how to frame queries.
• Gaining facility with general search engines on the web, and with specific websites for bioinformatics.
• Knowing how to search for specific information about sequences, structures, metabolic pathways, and relationships to disease, and how to launch analyses of the data retrieved.

This chapter introduces the specialized information-retrieval skills that will allow you to make effective use of the data banks in molecular biology. The goal is to give you familiarity with basic operations. It will then be easy to improve and develop your technique, and to learn in more detail the facilities, and interrelationships and interactions, of resources available on the web. Convenient sources of training materials include the tutorials embedded in many data banks. An example is the ENTREZ tutorial site at the US National Center for Biotechnology Information (NCBI): [http://www.ncbi.nlm.nih.gov/education/tutorials/](http://www.ncbi.nlm.nih.gov/education/tutorials/). The European Bioinformatics Institute (EBI) offers many tutorials on various aspects of experiments, databases, and bioinformatics.

## Database indexing and specification of search terms

An index is a set of pointers to information in a database. You have explored the entire worldwide web with a general search engine such as Google, and have visited specialized databases in molecular biology. You proposed one or more search terms, and the retrieval program checked for them in its tables of indices. The model is that the database is composed of entries: discrete, coherent parcels of information. The software identified entries with contents relevant to your interest. An example of the simplest paradigm is that you submit the term ‘horse’ and the program returns a list of entries that contain the term horse.

A full search of the web would turn up information about many different aspects of horses— molecular biology, breeding, racing, poems about horses—most of which you do not want to see. For a successful search, it is not enough to mention what you do want you must specialize your search to ensure that your desired responses don't get buried in a mass of extraneous rubbish. (Of course, rubbish is merely whatever other people are interested in.)

To focus the results, information-retrieval programs accept multiple query terms or keywords. A search for ‘horse liver alcohol dehydrogenase’ would produce responses specialized to this enzyme. The search would, most likely, identify entries that contain all four keywords that you submitted:

horse AND liver AND alcohol AND dehydrogenase. Poems about horses would be unlikely to appear among its top hits.

It is possible to ask for other logical combinations of indexing terms. For instance, if a search engine did not know about transatlantic spelling differences, it would be useful to be able to search for ‘hemoglobin OR haemoglobin’. Note that a search for ‘hemoglobin haemoglobin’ would probably be interpreted as ‘hemoglobin AND haemoglobin’ which would pick up documents written by international committees or orthographically challenged expatriates. (Some websites deliberately include both spellings, using a synonym dictionary.) Similar considerations apply to sulfur/sulphur, for example.

If you wanted to know about other dehydrogenases, you could ask for dehydrogenase NOT alcohol. This would retrieve entries that contain the term dehydrogenase but did not contain the word alcohol. You would find entries about lactate dehydrogenase, malate dehydrogenase, etc. You would miss references to review articles that compared alcohol dehydrogenases with other dehydrogenases, or alignments of the sequences of many dehydrogenases including alcohol dehydrogenase. You might regret missing these.

Many database search engines will allow complex logical expressions such as (haemoglobin OR hemoglobin) AND (dehydrogenase NOT alcohol). Construction of such expressions is an exercise in set theory. Drawing Venn diagrams helps in formulating the query. Although the logic of a search is independent of the software used to query a database, different programs demand different syntax to express the same conditions. For example the query for dehydrogenase NOT alcohol might have to be entered as DEHYDROGENASE -ALCOHOL or DEHYDOGENASE!ALCOHOL.

Specialized databases, including those in molecular biology, impose a structure on the information to separate different categories of data. This is essential. The biomedical scientific community includes people named E(lisabetta) Coli, (John D.) Yeast, (Patrice) Rat, and a large number of Rabbits, as well as several Crystals and Blots. If you wanted to find papers published by these investigators it would be naive to perform a general search of PubMed or some other molecular biology database with any of their names. Many databases provide separate indexing and searching of different categories of information. They permit searching for papers of which E. Coli is an author.

Some categories, such as taxonomy, have controlled vocabularies. Often a query system presents the vocabulary terms to the user as choices from pull-down menus. The structure of taxonomic information is important in retrieval. To do a search for ‘globin NOT mammal’, and pick out the relatively few entries about nonmammalian globins rather than the very many entries about globins, including human haemoglobins, that do not explicitly mention the term mammal, requires an information-retrieval system that ‘understands’ the taxonomic hierarchy. Controlled vocabularies— limited, explicit, and carefully defined sets of terms, known as ontologies—are also important for distributing queries among several databases.

A technical problem that frequently creates difficulty is how to enter terms containing nonstandard characters such as accent marks or umlauts, cedillas, Greek letters, and, as already mentioned, differences between British and US spelling. NCBI's ENTREZ can handle the US/British spelling differences with a synonym dictionary. Programs that index the entire web usually do not. Ignore the accent marks and hope for the best.

## Follow-up questions

When searching in databases, it is rare that you will find exactly what you want on the first round of probing. Usually you have to modify the query on the basis of the results initially returned. Most information-retrieval software permits consecutive, cumulative searches, with altered sets of search terms and/or logical relationships. Conversely, once you find what you were looking for, you will often want to extend your search to find related material. If you find a gene sequence, you might want to know about homologous genes in other organisms, or whether a three-dimensional structure of the corresponding protein is available. Or you might want to read papers published about the sequence.

For these subsidiary queries you need links between entries in the same or different databases. This is an example of the question of how one ‘browses’ in electronic libraries, which is a difficult problem and the subject of current research.

Suppose that you are interested in a particular gene. To find homologous genes you would like links to other items in the same database (a database of gene sequences). To find structures, or bibliographical references, related to that gene you would like links between different databases (from the database of gene sequences to a database of three-dimensional structures, or to a bibliographical database). As the number of databases, and the variety of their contents, grows, intercommunication among them has become a high-priority goal. Indeed, the interactivity of the databases in molecular biology is growing more and more effective, so that these operations are fairly easy now – formerly one had to do separate searches on isolated databases. NCBI's ENTREZ allows selecting a set of databases to search. Alternatively, most entries in molecular biology databases contain large numbers of embedded links. This is a generalization of the original model of a database as a closed set of independent entries that can be selected only by their indexed contents. One must think of the web as a very high-dimensional space.

Database construction in bioinformatics involves activities that can be classified, to some extent, into archiving—with the major goals of conservation and curation of facts—and interpreting and annotating, the compilation of biological information in a form most useful to support research. (Include, within annotation, provision of links to other databases.)

Many archival databases specialize in different kinds of data—nucleic acid sequences, protein sequences, or macromolecular structures—for reasons in part historical and in part because of the different curatorial skills required. In many cases, archival and interpretative projects are carried out at the same institution and even by the same people. However, anyone who wishes to create a new database is free to combine and repackage information from any available sources. Practical laboratory experience and expert knowledge of the experimental techniques used to generate the data are essential for curating an archival database, but are only extremely desirable for an interpretative database.

Two aspects of the recent development of bioinformatics databases stand out. One is the appearance of many projects that recombine the archived data in different ways. The other is the combination of many individual databases into larger and larger conglomerates. These processes overlap and sometimes happen together. Most database unifications are outgrowths of prior collaborations, with varying degrees of intimacy in the result.

## Analysis and processing of retrieved data

Sometimes as a result of a search you will want to launch a program, using the results retrieved for its input. For instance, if you identify a protein sequence of interest, you might want to perform a PSI-BLAST search. This is somewhat different from a strictly keyword-based database entryretrieval problem. Formerly you would have to run one job to search for your data, store the results of your search, and then run a separate, second, job, feeding the retrieved sequence to the application program by hand. However, like searches in multiple databases, several information-retrieval systems in molecular biology provide facilities for initiating such calculations. This makes for very much improved fluency in your sessions at the computer. We saw an example in Chapter 3, retrieving C. elegans serpins and feeding the sequences into a multiple alignment program.

## The archives

Although our knowledge of biological data is very far from complete, it is nevertheless of impressive size, and growing extremely rapidly. Many scientists are working to generate the data, and to carry out research projects analysing the results. There is a smooth and copious flow of results from the laboratory bench to data-banking organizations, for archiving, curation, and distribution to the research laboratory and the clinic.

Archiving of bioinformatics data was originally carried out by individual research groups motivated by an interest in the associated science. As the requirements for equipment and personnel grew—and the nature of the skills required multiplied, to include much more emphasis on computer science—national and in most cases international organizations have taken on the responsibility. To match the high volumes of data production these projects have become very large scale indeed. Anyone who has followed the entire history of the field cannot help being impressed by the replacement of tiny, low-profile, and ill-funded projects carried out by a few dedicated individuals to a multinational heavy industry subject to hostile takeovers and the scientific equivalent of leveraged buyouts.

## Primary data collections related to biological macromolecules

Nucleic acid sequences, including whole-genome projects

• Amino acid sequences of proteins
• Protein and nucleic acid structures
• Small-molecule crystal structures
• Protein functions
• Expression patterns of genes
• Networks: of metabolic pathways, of gene and protein interactions, and of control cascades
• Publications

## Nucleic acid sequence databases

The worldwide nucleic acid sequence archive is a triple partnership of the NCBI (USA), the European Nucleotide Archive (or ENA; at the EBI, UK), and the DNA Data Bank of Japan (National Institute of Genetics, Japan). These projects curate, archive, and distribute DNA and RNA sequences collected from genome projects, scientific publications, and patent applications. The groups exchange data daily. As a result the raw data are identical. However, the format in which they are presented, and the nature of the annotation, vary among these data banks. To ensure that these fundamental data are freely available, scientific journals require deposition of new nucleotide sequences, as a condition for publication of an article. Similar conditions apply to nucleic acid and protein structures.

The nucleic acid sequence databases, as distributed, are collections of entries. Each entry has the form of a text file containing data and annotations for a single contiguous sequence. Some entries are assembled from several published papers reporting overlapping fragments of a complete sequence. More common now are deposition of the results of (a) sequencing and assembly of complete genomes and (b) sequences of fragments, without assembly, from metagenomic samples.

Entries have a life history. Because of the desire on the part of the user community for rapid access to data, new entries are made available before completion of annotation and checking. Entries mature through the classes:

$$
\text {Unannotated} \rightarrow \text {Preliminary} \rightarrow \text {Unreviewed} \rightarrow \text {Standard}
$$

Rarely, an entry ‘dies’: a few have been removed when they are determined to be erroneous.

A sample DNA sequence entry from the European Nucleotide Archive, including annotations as well as sequence data, is the ATP7A gene from the aardvark (see Box 4.1). It encodes a protein involved in regulating copper levels. Mutations in the human homologue are implicated in Menkes syndrome, a progressive neurodegenerative disorder of copper metabolism.

A feature table (lines beginning FT) is a component of the annotation of an entry that reports properties of specific regions, for instance coding sequences (CDS). The aardvark ATP7A gene contains only one exon. Because feature tables are designed to be readable by computer programs— for example, to extract the amino acid sequence (see Exercise 4.4)—they have a more carefully controlled format and a more restricted vocabulary.

The feature table may indicate regions that

perform or affect function;
• interact with other molecules;
• affect replication;
• are involved in recombination;
• are a repeated unit;

Box 4.1 The EMBL Nucleotide Database entry for ATP7A from the aardvark

```txt
ID AAG47427; SV 1; linear; genomic DNA; STD; MAM; 675 BP.
XX
PA AY011392.1
XX
DE Orycteropus afer (aardvark) ATP7A
XX
OS Orycteropus afer (aardvark)
OC Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
Mammalia;
OC Eutheria; Afrotheria; Tubulidentata; Orycteropodidae; Orycteropus.
OX NCBI_TaxID=9818;
XX
FH Key Location/Qualifiers
FH
FT source 1..675
FT /organism="Orycteropus afer"
```

```txt
FT                  /mol_type="genomic DNA"
FT CDS     AY011392.1:\<1..>675
FT                 /codon_start=1
FT                 /gene="ATP7A"
FT                 /product="ATP7A"
FT                 /db_xref="GOA:Q9BFP6"
FT                 /db_xref="HSSP:Q04656"
FT                 /db_xref="InterPro:IPR001757"
FT                 /db_xref="InterPro:IPR006121"
FT                 /db_xref="UniProtKB/TrEMBL:Q9BFP6"
FT                 /protein_id="AAG47427.1"
FT                 /translation="IYQPHLITVEEIKKQIEAVGFPAFIKKQPKYLTLGAIDIERLKN
FT                 TSARSSEGSLQKSPSYTNDSTATFIIDGMHCKSCVNSIESALSTLQYVSSIAISLENRS
FT                 AIVKYNASSVTPETLRKAIEAVSPGQYTVSIISDVESIPNSPFSSSHQKIPLNIVSQPL
FT                 TQETVINISGMTCNSCVQSIEGVISKKAGVKSVQVSLADSSGVVEYDPLLTSPETLREE
FT                 IEN"
XX
SQ Sequence 675 BP; 233 A; 136 C; 124 G; 182 T; 0 other; 264016655 CRC32;
        attgtttatc agcctcatct tatcacagta gaggaaataa aaaagcagat tgaagctgtg 60
        ggttttccag cattcatcaa aaaacagccc aagtacctta cattgggagc tattgacata 120
        gaacgtctaa agaacacatc tgccagatcc tcagaaggat cactgcaaaa gagtccatca 180
        tataccaatg attcaacagc cacttttatc atagatggca tgcattgtaa atcatgtgtg 240
        tcaaatattg aaagtgcttt atctacactc caatatgtaa gcagcatagc aatttcttta 300
        gagaataggt ctgccattgt aaaatataat gcaagctcag tcactccaga aaccctgaga 360
        aaggcaatag aggcaagtatc accagggcaa tatactgtta gtattataag tgatgttgag 420
        agtatcccaa actctccttt tagctcatct catcaaaaaa tccctttgaa catagtgagc 480
        cagcctctga ctcaagaaac tgtaataaac atcagtggca tgacttgtaa ttcttgtgta 540
        cagtctattg agggtgtcat atcaaaaaaag gcaggtgtaa aatccgtaca agtctccctt 600
        gcagatagca gtggagttgt tgaatatgat cctctactaa cctctccaga aaccttgaga 660
        gaagaaatag aaaac 675
//
```

have secondary or tertiary structure;
• are revised or corrected.

## Genome databases and genome browsers

The general nucleic acid databases focus on collecting individual sequences. Associated with many full-genome sequences are genome browsers, databases bringing together all molecular information available about a particular species.

## Ensembl

Ensembl ([http://www.ensembl.org](http://www.ensembl.org)) is intended to be the universal information source for the human and other genomes. A goal is to collect and annotate all available information about human DNA sequences, link it to the master genome sequence, and make it accessible to the many scientists who will approach the data with many different points of view and different requirements. To this end, in addition to collecting and organizing the information, very serious effort has gone into developing computational infrastructure, including establishment of suitable conventions of nomenclature. It is not trivial to devise a scheme for maintaining stable identifiers in the face of data that will be undergoing not only growth but revision. The most visible result of these efforts is the website, very rich in facilities for both general browsing and focusing on details.

Ensembl is a joint project of the EBI and the Wellcome Trust Sanger Institute. However, Ensembl is organized as an open project; encouraging outside contributions. All but the most naive of readers must recognize the great demands that this will place on quality-control procedures.

Data collected in Ensembl includes genes, SNPs, repeats, and homologies. Genes may either be known experimentally or deduced from the sequence. Because the experimental support for annotation of the human genome is so variable, Ensembl records and presents the evidence for identification and annotation of every gene. Very extensive linking to other databases containing related information, such as Online Mendelian Inheritance in Man (OMIM), or expression databases, extend the accessible information.

Ensembl and other genome browsers are structured around the sequences themselves. To focus on a desired region, users have available several avenues of selective entry into the system:

• browsing, starting at the chromosome level then zooming in;
BLAST searches on a sequence or fragment;
• gene name;
relation to diseases, via OMIM;
• Ensembl ID if the user knows it;
• general text search.

A text search in the Ensembl human genome browser for BRCA1 produced the page displayed in Plate IV, showing the region around the BRCA1 locus. The upper frame shows a megabase, mapped to the q21.2 and q21.31 bands of chromosome 17. It reports markers and assigned genes. The bottom frame shows a more detailed view. Note the control panels between the two frames that permit navigation and ‘zooming’. The bottom frame shows a 0.1 megabase region, reporting many more details, including the detailed structure of the BRCA1 gene and the SNPs observed.

![](images/page_183_image_0.jpg)

<details>
<summary>text_image</summary>

e! project Ensembl ContigView
Home ▲ News ▲ BLAST ▲ Disease Browser ▲ Docs ▲ Download ▲
Find Lookup [e.g. U34879, APO00869]
Overview
chr17 band 421.21 421.21
ONH(cont.lgs)
45.45 Mb 44.45 Mb
GENESOME 457243
MARKERS
BETA107a
TURKE 4293
KONTSX 4293
KORNE 4293
KIRKEL 4293
KINEL 4293
KIFL27 4293
KIFL27_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_000
Detailed View
← 2 Mb  ↑ 1 Mb  Zoom  ↑ 1 Mb → 2 Mb
Length 188.89 Kb
SpTREBL 45.51 Mb 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.56 Mb 45.57 Mb 45.58 Mb
mRNA 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.56 Mb 45.57 Mb 45.58 Mb
UniGene 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.56 Mb 45.57 Mb 45.58 Mb
Genscan 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.56 Mb 45.57 Mb 45.58 Mb
Transcript 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.56 Mb 45.57 Mb 45.58 Mb
ONH(cont.lgs) 421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/421.21/4
Transcript 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.56 Mb 45.57 Mb 45.58 Mb
Genscan 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.57 Mb 45.58 Mb
UniGene 45.51 Mb 45.52 Mb 45.53 Mb 45.54 Mb 45.55 Mb 45.56 Mb 45.57 Mb 45.58 Mb
mRNA 45.51Mb 45.52Mb 45.53Mb 45.54Mb 45.55Mb 45.56Mb 45.57Mb 45.58Mb
SpTREBL 45.51Mb 45.52Mb 45.53Mb 45.54Mb 45.55Mb 45.56Mb 45.57Mb 45.58Mb
SNP 45.51Mb 45.52Mb 45.53Mb 45.54Mb 45.55Mb 45.56Mb 45.57Mb 45.58Mb
Mouse trace Repeats
BP16-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CPNOSI BETA-CDKALR
File Path RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPNOSI RP16-CPALER
View as text Dump Mouse Trains Jams to UCSC Customize this view
Chr: 17 Nucleotides: 4S49S312 to S39S312 Turn menu On Off Refresh
</details>

Plate IV Ensembl genome browser showing the region surrounding the BRCA1 locus (See Chapter 4).

![](images/page_183_image_2.jpg)

## See Weblems 4.1 – 4.4

## Protein sequence databases

In 2002, three protein sequence databases—the Protein Information Resource (PIR; at the National Biomedical Research Foundation of the Georgetown University Medical Center in Washington, DC, USA), SWISS-PROT, and TrEMBL (from the Swiss Institute of Bioinformatics in Geneva, Switzerland and the EBI in Hinxton, UK)—coordinated their efforts, to form the UniProtKB consortium. The partners in this enterprise share the database but continue to offer separate information-retrieval tools for access.

The PIR grew out of the very first sequence database, developed by Margaret O. Dayhoff, the pioneer of the field of bioinformatics. SWISS-PROT was developed at the Swiss Institute of Bioinformatics. TrEMBL contains the translations of genes identified within DNA sequences in the European Nucleotide Archive. TrEMBL entries are regarded as preliminary, and are converted— after curation and extended annotation—to mature entries.

Today, almost all amino acid sequence information arises from translation of gene sequences. However, even the amino acid sequence of a protein is not in general inferrable with confidence from the gene sequence. The main reason, in eukaryotes, is ambiguity in splicing. In addition, information about ligands, disulphide bridges, subunit associations, post-translational modifications, effects of mRNA editing, etc., is not available from nucleic acid sequences. For instance, from genetic information alone one would not know that human insulin is a dimer linked by disulphide bridges. Protein-sequence data banks collect this additional information from the literature and

provide suitable annotations.

From UniProtKB, the entry for the amino acid sequence of the protein bovine pancreatic trypsin inhibitor, in SWISS-PROT format, is shown in the box. Note that the sequence itself occupies only a relatively small amount of space in the entry.

## Amino acid sequence entry for bovine pancreatic trypsin inhibitor

NiceProt View of Swiss-Prot: P00974

Entry information

| Entry name | BPT1_BOVIN |
| --- | --- |
| Primary accession number | P00974 |
| Secondary accession numbers | None |
| Entered in Swiss-Prot in | Release 01, July 1986 |
| Sequence was last modified in | Release 10, March 1989 |
| Annotations were last modified in | Release 44, June 2004 |

Name and origin of the protein

| Protein name | Pancreatic trypsin inhibitor [Precursor] |
| --- | --- |
| Synonyms | Basic protease inhibitorBPIBPTIAprotinin |
| Gene name | None |
| From | Bos taurus (Bovine) [TaxID: 9913] |
| Taxonomy | Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;Mammalia; Eutheria; Cetartiodactyla; Ruminantia; Pecora; Bovidae; Bovinae; Bos. |

References

| [1] SEQUENCE FROM NUCLEIC ACID.MEDLINE=87283904; PubMed=2441071; [NCBI, ExPASy, EBI, Israel, Japan]Creighton T.E., Charles I.G.;"Sequences of the genes and polypeptide precursors for two bovine protease inhibitors.";J. Mol. Biol. 194:11-22(1987).REFERENCES 2-13 DELETED |
| --- |

Comments

| FUNCTION: Inhibits trypsin, kallikrein, chymotrypsin, and plasmin.SUBCELLULAR LOCATION: Secreted.PHARMACEUTICAL: Available under the name Trasylol (Mile). Used for inhibiting coagulation so as to reduce blood loss during bypass surgery.SIMILARITY: Contains 1 BPTI/Kunitz inhibitor domain.DATABASE: NAME=Trasylol; NOTE=Clinical information on Trasylol; WWW="http://www.trasylol.com/. |
| --- |

Copyright

| This Swiss-Prot entry is copyright. It is produced through a collaboration between the Swiss Institute of Bioinformatics and the EMBL outstation - the European Bioinformatics Institute. |
| --- |

Cross-references

| EMBL | M20934; AAD13685.1; -.[EMBL / GenBank / DDBJ] [CoDingSequence]5 ADDITIONAL CROSS-REFERENCES DELETED |
| --- | --- |
| PIR | S00277; TIBO.1K09; 10-JUL-02.[ExPASy / RCSB / EBI] |
| PDB | 46 ADDITIONAL STRUCTURES DELETEDDetailed list of linked structures. |
| InterPro | IPR002223; Kunitz_BPTI.Graphical view of domain structure. |
| Pfam | PF00014; Kunitz_BPTI; 1. |

![](images/page_185_image_0.jpg)

<details>
<summary>text_image</summary>

Pfam graphical view of domain structure.
PRINTS PR00759; BASICPTASE.
ProDom PD000222; Kunitz_BPTI; 1.
[Domain structure / List of seq. sharing at least 1 domain]
SMART SM00131; KU; 1.
PS00280; BPTI_KUNITZ_1; 1.
PROSITE PSS0279; BPTI_KUNITZ_2; 1.
PROSITE graphical view of domain structure.
HOVERGEN [Family / Alignment / Tree]
BLOCKS P00974.
ProtoNet P00974.
ProtoMap P00974.
PRESAGE P00974.
DIP P00974.
ModBase P00974.
SMR P00974; 6A778A4AD763FB19.
SWISS-2DPAGE Get region on 2D PAGE.
UniRef View cluster of proteins with at least 50% / 90% identity.
Keywords
Serine protease inhibitor: Signal: Pharmaceutical; 3D-structure.
Features
Feature table viewer Feature aligner
Key From To Length Description
SIGNAL 1_21 21 Potential.
PROPEP 22_35 14
CHAIN 36_93 58 Pancreatic trypsin inhibitor.
PROPEP 94_100 7
DOMAIN 40_90 51 BPTI/Kunitz inhibitor.
SITE 50_51 2 Reactive bond for trypsin.
DISULFID 40_90
DISULFID 49_73
DISULFID 65_86
HELIX 38_41 4
STRAND 53_59 7
TURN 60_63 4
STRAND 64_70 7
STRAND 80_80 1
HELIX 83_90 8
Sequence information
Length: 100 AA [This is the length Molecular weight: 10903 Da [This is the CRC64: 6A778A4AD763FB19 [This is the unprocessed precursor] MW of the unprocessed precursor] is a checksum on the sequence]
10 20 30 40 50 60
| | | | | |
MKMSRLCLSV ALLVLLGTLA ASTPGCOTSN QAKAQRPDFC LEPPYTGPCK ARIIRYFYNA
70 80 90 100
KAGLCQTFVY GGCRAKRNNF KSAEDCMRTC GGAIGPWENL
P00974 in FASTA format
</details>

## The Swiss Institute for Bioinformatics

The Swiss Institute for Bioinformatics originally compiled SWISS-PROT. It carries out a wide range of activities, including additional databases, and collections of bioinformatics tools and links, called the Expert Protein Analysis System (ExPASy; [http://www.expasy.org](http://www.expasy.org)).

PROSITE is a set of signature patterns characteristic of protein families. Such a pattern (or motif, or signature, or fingerprint, or template) is common to related proteins, usually because of the requirements of binding sites that constrain the evolution of the protein family. For instance, the consensus pattern for inorganic pyrophosphatase is D-[SGDN]-D-[PE]-[LIVMF]-D-[LIVMGAC]. The three conserved Ds bind divalent metal cations. Often, such a pattern identifies distant relationships not otherwise detectable by comparing sequences.

ExPASy presents certain bioinformatics tools as servers on its website, and has links to many others. Categories of tools include proteomics, genomics, structural bioinformatics, systems biology, phylogeny/evolution, population genetics, transcriptomics, biophysics, imaging, IT infrastructure, and drug design. The full list of tools contains 325 entries, roughly half of which were created and are maintained ‘in house’, with the others being links to external sites.

## The Protein Information Resource (PIR) and associated databases

The PIR is one of the partners in UniProtKB. In addition, the PIR maintains several databases about

proteins:

PIRSF: the Protein Family Classification System provides clustering of the sequences in UniProtKB according to their evolutionary relationships;
• iProClass, an integrated Protein Knowledgebase, is a gateway providing uniform access to over 90 biological databases, with flexible retrieval and navigation facilities;
• iProLINK (integrated Protein Literature, Information and Knowledge) is a gateway to the literature.

## Databases of protein families

Evolutionary relationships are essential for making sense of biological data. Evolution provides the framework for an integrated appreciation of the properties of molecules and processes, and their similarities and difference in various species. Perhaps less obvious is that comparative studies illuminate, in an essential way, even individual molecules. Knowing only a single sequence, or structure, it is difficult to understand the significance of particular features. Patterns of conservation identify features that nature has found it necessary to retain. (PROSITE signatures are examples.) The challenge then is to figure out why.

Study of evolutionary patterns must begin with assembling a set of homologues. We again emphasize (1) the distinction between homology—descent from a common ancestor—a yes-or-no property, from similarity, which is some quantitative measure of the difference between two objects, and (2) that similarity can always be measured but it is rare to be able to observe homology directly; therefore, in most cases homology is an inference from similarity.

R. Doolittle suggested a general calibration of pairwise sequence similarity for homology detection. Two full-length protein sequences (≥100 residues) that have 25% or more identical residues in an optimal alignment are likely to be related. Below ≈15% identical residues in an optimal alignment and we become mired in the noise. In this range of similarity we have no reason to believe that the sequences are related, although they might be. Doolittle defined the range between 18 and 25% identity as ‘the twilight zone’, where there may be tantalizing suspicion of a relationship, but the evidence falls short of proof. In some cases the active site is better conserved than the bulk of the protein. In these cases the appearance of a motif—such as the PROSITE consensus pattern for inorganic pyrophosphatase, D-[SGDN]-D-[PE]-[LIVMF]-D-[LIVMGAC]—can support the case for homology.

Multiple sequence alignments are much more powerful than pairwise sequence alignments. First, the additional data allow more accurate alignments. Second, the conservation patterns stand out far more sharply. (See Problem 4.1).

Protein structure changes more conservatively than amino acid sequence. Therefore inference of homology from structural similarity can link more distant relatives than sequence similarity can. In cases that lie in the twilight zone where sequence similarity is suggestive but not convincing, structural similarity is the court of last resort. In many cases, structural similarity can identify homologues even if no signal whatever—at least no signal detectable by current techniques— remains in the sequences.

It is common to refer to a group of related proteins as a family. Many databases classify proteins into families. These include sequence-oriented databases such as InterPro, Pfam, and COG and structure-oriented databases such as SCOP and CATH. The assignment of proteins to families is similar but not identical in various sources.

Most protein families contain many clusters of closer relatives. These form subfamilies. Conversely, two or more families can be grouped into superfamilies. Whereas the distinction between homologous and nonhomologous proteins is objective (even if we cannot determine it with confidence in all cases), the clustering of homologues into subfamilies or superfamilies is partially a matter of convention or taste. Definition of subfamilies and superfamilies may legitimately differ among different databases.

## Databases of structures

Structure databases archive, annotate, and distribute sets of atomic coordinates. Started by the late Walter Hamilton at Brookhaven National Laboratories (Long Island, NY, USA) in 1971, the major database for biological macromolecular structures is now the Worldwide Protein Data Bank (wwPDB). It is a joint effort of the Research Collaboratory for Structural Bioinformatics (RCSB; a distributed organization based at Rutgers University in New Jersey, the San Diego Supercomputer Center in California, and the University of Wisconsin, all in the USA), the Protein Data Bank Europe (at the EBI in the UK), and the Protein Data Bank Japan (based at Osaka University). The wwPDB contains structures of proteins, nucleic acids, and a few carbohydrates. The parent website is [http://www.wwpdb.org](http://www.wwpdb.org).

The home pages of the wwPDB partners contain links to the data files themselves, to expository and tutorial material including short news items and the PDB Newsletter, to facilities for deposition of new entries, and to specialized search software for retrieving structures.

Box 4.2 shows part of a Protein Data Bank entry for a structure of spinach chloroplast thioredoxin.<sup>1</sup> The information contained includes:

• what protein is the subject of the entry, and what species it came from;
• who solved the structure, and literature references;
experimental details about the structure determination, including information related to the general quality of the result, such as resolution of an X-ray structure determination, and stereochemical statistics;
• the amino acid sequence;
• the atomic coordinates (lines beginning ATOM);
• what additional molecules appear in the structure, potentially including cofactors, inhibitors, and water molecules (the keyword HETATM identifies the coordinates of these moities);
• assignments of secondary structure: helices and sheets;
• disulphide bridges.

The wwPDB overlaps several other databases. The Cambridge Crystallographic Data Centre (CCDC) archives the structures of small molecules; oligonucleotides appear in both the CCDC and the wwPDB. The combination of structural data from these sources is extremely useful in studies of conformations of the component units of biological macromolecules, and for investigations of macromolecule–ligand interactions, including but not limited to applications to drug design. The Nucleic Acid Structure Databank (NDB) at Rutgers University also complements the wwPDB. The BioMagResBank, at the Department of Biochemistry, University of Wisconsin—a partner in the RCSB—archives protein structures determined by nuclear magnetic resonance.

The archives collect not only the results of structure determination, but also the measurements on which they are based. The wwPDB keeps the data from X-ray structure determinations, and the

Box 4.2 Protein Data Bank entry 1FAA, spinach chloroplast thioredoxin

```proteindb
HEADER ELECTRON TRANSPORT 13-JUL-00 1FAA
TITLE CRYSTAL STRUCTURE OF THIOREDOXIN F FROM SPINACH CHLOROPLAST
TITLE     2 (LONG FORM)
COMPND      MOL_ID: 1;
COMPND   2 MOLECULE: THIOREDOXIN F;
COMPND   3 CHAIN: A;
COMPND   4 FRAGMENT: LONG FORM;
COMPND   5 ENGINEERED: YES;
COMPND   6 MUTATION: YES
SOURCE       MOL_ID: 1;
SOURCE   2 ORGANISM_SCIENTIFIC: SPINACIA OLERACEA;
SOURCE   3 ORGANISM_COMMON: SPINACH;
SOURCE   4 CELLULAR_LOCATION: CHLOROPLAST;
SOURCE   5 EXPRESSION_SYSTEM: ESCHERICHIA COLI;
SOURCE   6 EXPRESSION_SYSTEM_COMMON: BACTERIA;
SOURCE   7 EXPRESSION_SYSTEM_PLASMID: PKK233-2 (MODIFIED)
KEYWDS      ELECTRON TRANSPORT
EXPDTA      X-RAY DIFFRACTION
AUTHOR     G.CAPITANI,Z.MARKOVIC-HOUSLEY,G.DELVAL,M.MORRIS,
AUTHOR   2 J.N.JANSONIUS,P.SCHURMANN
REVDAT    1 20-SEP-00 1FAA     0
JRNL           AUTH    G.CAPITANI,Z.MARKOVIC-HOUSLEY,G.DELVAL,M.MORRIS,
JRNL           AUTH 2 J.N.JANSONIUS,P.SCHURMANN
JRNL           TITL   CRYSTAL STRUCTURES OF TWO FUNCTIONALLY DIFFERENT
JRNL           TITL 2 THIOREDOXINS IN SPINACH CHLOROPLASTS
JRNL           REF     J.MOL.BIOL.                  V. 302   135 2000
JRNL           REFN   ASTM JMOBAK UK ISSN 0022-2836
REMARK    1
REMARK    2
REMARK   2 RESOLUTION. 1.85 ANGSTROMS.
REMARK    3
REMARK   3 REFINEMENT.
REMARK   3 PROGRAM          : X-PLOR 3.851
REMARK   3 AUTHORS          : BRUNGER
REMARK    3
```

Additional information about details of solution of structure omitted

```proteindb
REMARK 900 RELATED ENTRIES
REMARK 900 RELATED ID: 1F9M    RELATED DB: PDB
REMARK 900 THIOREDOXIN F FROM SPINACH CHLOROPLAST (SHORT FORM)
REMARK 900 RELATED ID: 1FB0    RELATED DB: PDB
REMARK 900 THIOREDOXIN M FROM SPINACH CHLOROPLAST (REDUCED FORM)
REMARK 900 RELATED ID: 1FB6    RELATED DB: PDB
REMARK 900 THIOREDOXIN M FROM SPINACH CHLOROPLAST (OXIDIZED FORM)
DBREF 1FAA A      1   121     SWS     P09856    THIF_SPIOL      69    189
SEQADV 1FAA MET A    -2     SWS    P09856             CLONING ARTIFACT
SEQADV 1FAA TYR A    -1     SWS    P09856             CLONING ARTIFACT
SEQADV 1FAA TYR A      0     SWS    P09856             CLONING ARTIFACT
SEQADV 1FAA LEU A      1     SWS    P09856    MET     69 ENGINEERED
```

<table><tr><td>SEQADV</td><td>1FAA</td><td>LEU A</td><td>3</td><td>SWS</td><td>P09856</td><td>GLN</td><td>71</td><td>ENGINEERED</td><td></td><td></td></tr><tr><td>SEQRES</td><td>1 A</td><td>124</td><td>MET</td><td>TYR</td><td>TYR</td><td>LEU</td><td>GLU</td><td>LEU ALA</td><td>LEU GLY</td><td>THR GLN GLU MET</td></tr><tr><td>SEQRES</td><td>2 A</td><td>124</td><td>GLU</td><td>ALA</td><td>ILE</td><td>VAL</td><td>GLY</td><td>LYS VAL</td><td>THR GLU VAL ASN LYS ASP</td><td></td></tr><tr><td>SEQRES</td><td>3 A</td><td>124</td><td>THR</td><td>PHE</td><td>TRP</td><td>PRO</td><td>ILE</td><td>VAL LYS ALA</td><td>ALA ALA GLY ASP LYS PRO</td><td></td></tr><tr><td>SEQRES</td><td>4 A</td><td>124</td><td>VAL</td><td>VAL</td><td>LEU</td><td>ASP</td><td>MET</td><td>PHE THR GLN TRP CYS GLY PRO CYS</td><td></td><td></td></tr><tr><td>SEQRES</td><td>5 A</td><td>124</td><td>LYS</td><td>ALA</td><td>MET</td><td>ALA</td><td>PRO LYS</td><td>TYR GLU LYS LEU ALA GLU GLU</td><td></td><td></td></tr><tr><td>SEQRES</td><td>6 A</td><td>124</td><td>TYR</td><td>LEU</td><td>ASP</td><td>VAL</td><td>ILE</td><td>PHE LEU LYS LEU ASP CYS ASN GLN</td><td></td><td></td></tr><tr><td>SEQRES</td><td>7 A</td><td>124</td><td>GLU</td><td>ASN LYS</td><td>THR</td><td>LEU</td><td>ALA LYS GLU LEU GLY ILE ARG VAL</td><td></td><td></td><td></td></tr><tr><td>SEQRES</td><td>8 A</td><td>124</td><td>VAL</td><td>PRO</td><td>THR</td><td>PHE</td><td>LYS ILE</td><td>LEU LYS GLU ASN SER VAL VAL</td><td></td><td></td></tr><tr><td>SEQRES</td><td>9 A</td><td>124</td><td>GLY</td><td>GLU</td><td>VAL</td><td>THR</td><td>GLY ALA LYS TYR ASP LYS LEU LEU GLU</td><td></td><td></td><td></td></tr><tr><td>SEQRES</td><td>10 A</td><td>124</td><td>ALA</td><td>ILE</td><td>GLN</td><td>ALA</td><td>ALA ARG SER</td><td></td><td></td><td></td></tr><tr><td>FORMUL</td><td>2</td><td>HOH</td><td colspan="8">*34 (H2 O1)</td></tr><tr><td>HELIX</td><td>1</td><td>1 GLY A</td><td>6</td><td>ALA A</td><td>12</td><td>1</td><td></td><td></td><td></td><td>7</td></tr><tr><td>HELIX</td><td>2</td><td>2 THR A</td><td>24</td><td>ALA A</td><td>32</td><td>1</td><td></td><td></td><td></td><td>9</td></tr><tr><td>HELIX</td><td>3</td><td>3 CYS A</td><td>46</td><td>TYR A</td><td>63</td><td>1</td><td></td><td></td><td></td><td>18</td></tr><tr><td>HELIX</td><td>4</td><td>4 ASN A</td><td>77</td><td>GLY A</td><td>85</td><td>1</td><td></td><td></td><td></td><td>9</td></tr><tr><td>HELIX</td><td>5</td><td>5 LYS A</td><td>108</td><td>ARG A</td><td>120</td><td>1</td><td></td><td></td><td></td><td>13</td></tr><tr><td>SHEET</td><td>1</td><td>A 5 VAL A</td><td>17</td><td>GLU A</td><td>19</td><td>0</td><td></td><td></td><td></td><td></td></tr><tr><td>SHEET</td><td>2</td><td>A 5 ILE A</td><td>67</td><td>ASP A</td><td>72</td><td>1</td><td>O PHE A</td><td>68 N</td><td>THR A</td><td>18</td></tr><tr><td>SHEET</td><td>3</td><td>A 5 VAL A</td><td>37</td><td>PHE A</td><td>42</td><td>1</td><td>N VAL A</td><td>38 O</td><td>ILE A</td><td>67</td></tr><tr><td>SHEET</td><td>4</td><td>A 5 THR A</td><td>91</td><td>LYS A</td><td>96</td><td>-1</td><td>O THR A</td><td>91 N</td><td>MET A</td><td>41</td></tr><tr><td>SHEET</td><td>5</td><td>A 5 SER A</td><td>99</td><td>THR A</td><td>105</td><td>-1</td><td>O SER A</td><td>99 N</td><td>LYS A</td><td>96</td></tr><tr><td>SSBOND</td><td>1</td><td>CYS A</td><td>46</td><td>CYS A</td><td>49</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CISPEP</td><td>1</td><td>VAL A</td><td>89</td><td>PRO A</td><td>90</td><td></td><td>0</td><td>-0.06</td><td></td><td></td></tr><tr><td>CRYST1</td><td>30.600</td><td>63.100</td><td colspan="2">31.600</td><td>90.00</td><td>110.70</td><td colspan="3">90.00 P 1 21 1</td><td>2</td></tr><tr><td>ORIGX1</td><td colspan="2">1.000000</td><td colspan="2">0.000000</td><td colspan="2">0.000000</td><td colspan="3">0.00000</td><td></td></tr><tr><td>ORIGX2</td><td colspan="2">0.000000</td><td colspan="2">1.000000</td><td colspan="2">0.000000</td><td colspan="3">0.00000</td><td></td></tr><tr><td>ORIGX3</td><td colspan="2">0.000000</td><td colspan="2">0.000000</td><td colspan="2">1.000000</td><td colspan="3">0.00000</td><td></td></tr><tr><td>SCALE1</td><td colspan="2">0.032680</td><td colspan="2">0.000000</td><td colspan="2">0.012349</td><td colspan="3">0.00000</td><td></td></tr><tr><td>SCALE2</td><td colspan="2">0.000000</td><td colspan="2">0.015848</td><td colspan="2">0.000000</td><td colspan="3">0.00000</td><td></td></tr><tr><td>SCALE3</td><td colspan="2">0.000000</td><td colspan="2">0.000000</td><td colspan="2">0.033829</td><td colspan="3">0.00000</td><td></td></tr><tr><td>ATOM</td><td>1</td><td>N</td><td>LEU A</td><td>1</td><td></td><td></td><td>24.389</td><td>12.172</td><td>22.330</td><td>1.00</td></tr><tr><td>49.98</td><td></td><td></td><td>N</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>2</td><td>CA</td><td>LEU A</td><td>1</td><td></td><td></td><td>23.617</td><td>11.064</td><td>22.997</td><td>1.00</td></tr><tr><td>51.12</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>3</td><td>C</td><td>LEU A</td><td>1</td><td></td><td></td><td>22.228</td><td>10.829</td><td>22.381</td><td>1.00</td></tr><tr><td>51.55</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>4</td><td>O</td><td>LEU A</td><td>1</td><td></td><td></td><td>21.316</td><td>11.634</td><td>22.547</td><td>1.00</td></tr><tr><td>50.88</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>5</td><td>CB</td><td>LEU A</td><td>1</td><td></td><td></td><td>23.447</td><td>11.351</td><td>24.497</td><td>1.00</td></tr><tr><td>49.15</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>6</td><td>CG</td><td>LEU A</td><td>1</td><td></td><td></td><td>24.373</td><td>10.670</td><td>25.513</td><td>1.00</td></tr><tr><td>47.15</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>7</td><td>CD1</td><td>LEU A</td><td>1</td><td></td><td></td><td>23.831</td><td>10.905</td><td>26.924</td><td>1.00</td></tr><tr><td>45.33</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>8</td><td>CD2</td><td>LEU A</td><td>1</td><td></td><td></td><td>24.488</td><td>9.185</td><td>25.215</td><td>1.00</td></tr><tr><td>44.91</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>9</td><td>N</td><td>GLU A</td><td>2</td><td></td><td></td><td>22.076</td><td>9.713</td><td>21.674</td><td>1.00</td></tr><tr><td>53.58</td><td></td><td></td><td>N</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>10</td><td>CA</td><td>GLU A</td><td>2</td><td></td><td></td><td>20.806</td><td>9.358</td><td>21.044</td><td>1.00</td></tr><tr><td>54.60</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>11</td><td>C</td><td>GLU A</td><td>2</td><td></td><td></td><td>20.054</td><td>8.350</td><td>21.907</td><td>1.00</td></tr><tr><td>52.06</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>12</td><td>O</td><td>GLU A</td><td>2</td><td></td><td></td><td>20.550</td><td>7.916</td><td>22.943</td><td>1.00</td></tr></table>

| 53.01 |  |  | O |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ATOM | 13 | CB | GLU A | 2 | 21.043 | 8.762 | 19.650 | 1.00 |  |
| 60.19 |  |  | C |  |  |  |  |  |  |
| ATOM | 14 | CG | GLU A | 2 | 20.884 | 9.756 | 18.502 | 1.00 |  |
| 71.27 |  |  | C |  |  |  |  |  |  |
| ATOM | 15 | CD | GLU A | 2 | 19.687 | 10.694 | 18.678 | 1.00 |  |
| 77.29 |  |  | C |  |  |  |  |  |  |
| ATOM | 16 | OE1 | GLU A | 2 | 19.521 | 11.277 | 19.779 | 1.00 |  |
| 79.51 |  |  | O |  |  |  |  |  |  |
| ATOM | 17 | OE2 | GLU A | 2 | 18.910 | 10.850 | 17.705 | 1.00 |  |
| 81.98 |  |  | O |  |  |  |  |  |  |
| ATOM | 18 | N | LEU A | 3 | 18.857 | 7.975 | 21.477 | 1.00 |  |
| 48.15 |  |  | N |  |  |  |  |  |  |
| ATOM | 19 | CA | LEU A | 3 | 18.047 | 7.029 | 22.227 | 1.00 |  |
| 43.81 |  |  | C |  |  |  |  |  |  |
| ATOM | 20 | C | LEU A | 3 | 18.098 | 5.650 | 21.573 | 1.00 |  |
| 40.93 |  |  | C |  |  |  |  |  |  |
| ATOM | 21 | O | LEU A | 3 | 18.285 | 5.529 | 20.371 | 1.00 |  |
| 40.43 |  |  | O |  |  |  |  |  |  |
| ATOM | 22 | CB | LEU A | 3 | 16.598 | 7.531 | 22.280 | 1.00 |  |
| 44.07 |  |  | C |  |  |  |  |  |  |
| ATOM | 23 | CG | LEU A | 3 | 15.797 | 7.608 | 23.586 | 1.00 |  |
| 44.51 |  |  | C |  |  |  |  |  |  |
| ATOM | 24 | CD1 | LEU A | 3 | 15.534 | 6.207 | 24.087 | 1.00 |  |
| 52.05 |  |  | C |  |  |  |  |  |  |
| ATOM | 25 | CD2 | LEU A | 3 | 16.543 | 8.400 | 24.639 | 1.00 |  |
| 48.17 |  |  | C |  |  |  |  |  |  |

Coordinates of residues 4–121 of protein omitted

<table><tr><td>ATOM</td><td>937</td><td>N</td><td>SER A 121</td><td></td><td>8.850</td><td>-16.291</td><td>7.411</td><td>1.00</td></tr><tr><td>55.56</td><td></td><td></td><td>N</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>938</td><td>CA</td><td>SER A 121</td><td></td><td>9.537</td><td>-17.581</td><td>7.231</td><td>1.00</td></tr><tr><td>60.26</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>939</td><td>C</td><td>SER A 121</td><td></td><td>10.923</td><td>-17.478</td><td>6.558</td><td>1.00</td></tr><tr><td>62.65</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>940</td><td>O</td><td>SER A 121</td><td></td><td>11.870</td><td>-18.086</td><td>7.107</td><td>1.00</td></tr><tr><td>64.76</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>941</td><td>CB</td><td>SER A 121</td><td></td><td>8.656</td><td>-18.556</td><td>6.432</td><td>1.00</td></tr><tr><td>60.35</td><td></td><td></td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>942</td><td>OG</td><td>SER A 121</td><td></td><td>7.280</td><td>-18.401</td><td>6.747</td><td>1.00</td></tr><tr><td>60.82</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ATOM</td><td>943</td><td>OXT</td><td>SER A 121</td><td></td><td>11.059</td><td>-16.809</td><td>5.503</td><td>1.00</td></tr><tr><td>63.39</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TER</td><td>944</td><td colspan="2">SER A 121</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HETATM</td><td>945</td><td>O</td><td>HOH</td><td>1</td><td>2.260</td><td>-3.687</td><td>15.041</td><td>1.00</td></tr><tr><td>21.56</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HETATM</td><td>946</td><td>O</td><td>HOH</td><td>2</td><td>0.884</td><td>-6.116</td><td>15.287</td><td>1.00</td></tr><tr><td>24.15</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HETATM</td><td>947</td><td>O</td><td>HOH</td><td>3</td><td>0.912</td><td>13.888</td><td>2.773</td><td>1.00</td></tr><tr><td>30.06</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HETATM</td><td>948</td><td>O</td><td>HOH</td><td>4</td><td>14.616</td><td>-4.966</td><td>11.156</td><td>1.00</td></tr><tr><td>26.65</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HETATM</td><td>949</td><td>O</td><td>HOH</td><td>5</td><td>4.640</td><td>10.330</td><td>9.025</td><td>1.00</td></tr><tr><td>23.93</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HETATM</td><td>950</td><td>O</td><td>HOH</td><td>6</td><td>3.040</td><td>-0.537</td><td>15.641</td><td>1.00</td></tr><tr><td>28.46</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HETATM</td><td>951</td><td>O</td><td>HOH</td><td>7</td><td>6.246</td><td>-2.378</td><td>27.633</td><td>1.00</td></tr><tr><td>49.34</td><td></td><td></td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Coordinates of additional water molecules omitted

| CONECT | 358 | 375 |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONECT | 375 | 358 |  |  |  |  |  |  |  |  |  |  |  |
| MASTER |  | 211 | 0 | 0 | 5 | 5 | 0 | 0 | 6 | 977 | 1 | 2 | 10 |
| END |  |  |  |  |  |  |  |  |  |  |  |  |  |

The wwPDB assigns a four-character identifier to each structure deposited. The first character is a number from 1 to 9. Do not expect mnemonic significance. In many cases several entries correspond to one protein, solved in different states of ligation, or in different crystal forms, or re-solved using better crystals or more accurate data-collection techniques. For instance, there have been at least four generations of sperm whale myoglobin crystal structures.

It is easy to retrieve a structure if you know its identifier. From the RCSB home page, entering a PDB ID and selecting ‘Explore’ gives a one-page summary of the entry. Figure 4.1 shows part of the summary page for the spinach chloroplast thioredoxin structure, identifier 1FAA. Links from this page take you to:

![](images/page_191_image_5.jpg)

<details>
<summary>text_image</summary>

PDB
An Information Portal for Biological Micro-Interferential Structure
As of Tuesday, 12, 2017
There are 4848 structures
Contact on WIP/PRINT NAME
PDB @ http://www.pdb.org
PDB & Method
AUXIA
File Source
Physical System
Alert: Our data files are changing seen. Please see http://www.expdb.org for more details.
Title: CHEMICAL STRUCTURE OF THEORECOSM FROM SPINACH CHLORoplast LONG FORM
Authors: Captur, C., Harvallou, Mouta, C., Chetak, G., Homi, H., Janshuk, JU., Schyrmann, R.
Primary Litigation: Captur, C., Harvallou, Mouta, C., Chetak, G., Homi, H., Janshuk, JU., Schyrmann, R. Copy annotations if yes; automatically effective information in spinach chloroplast (used as: pp.133-079, pp.133-079, pp.133-079).
Military Department: 2000-07-13 Author: 2000-09-02
Experimental Method: Type: A/B/M DIFFRACTION Form: E1001
Number of entries: Numbered by: 1.05 0.209 (each) 0.269 Space group:
Length (ft): 30.00 10.15 31.80
Angle (°): 90.00 110.70 90.00
Molecular Transcription Assymptomatic script: Pateman T, Mouta, THREOCOSM F Magnment LONG FORM
Huisman MLL QIL Zhao A
Chemical Action: Mechanic Transport
Book#: Pateman | Scientific Name | Ighustic distance | Common Name | Ighustic Expression | Expression system | Ischerichia coli
Avidated: PDB | Pateman | Threobium from spinach chloroplast (reduced form) | Threobium from spinach chloroplast (reduced form) | Threobium from spinach chloroplast (soft form)
BIDP Classification: Domain Info | Data and key problems | Part | Superfamily | Parent | Domain | Species | Ighustic Expression | Intense Expression
CATA Classification: Chain #1000 | Chain #1000 | Chain #1000 | Threobium fast | Threobium fast | Threobium fast | Threobium fast | Threobium fast |
PDA Classification: Chain #1000 to update a copy of PDA | PDA #1000 | Description | Type | Type | Type | Type | Type |
AD Forms: Numbering | Molecular Function | Biological Process | Cellular Component | Cellular Component | Cellular Component | Cellular Component | Cellular Component | Cellular Component |
</details>

Figure 4.1 The summary page for the wwPDB entry 1FAA, spinach chloroplast thioredoxin.

• the publication in which the entry was described, via the bibliographic database PubMed;
• pictures of the structure (some of these may require that you install a viewing program on your computer);
access to the file containing the entry itself;
• lists of related structures, according to several different classifications of protein structures;
stereochemical analysis: the distribution of bond lengths and angles, and conformational angles;
sources of other information about this entry;
• the sequence and secondary structure assignment;