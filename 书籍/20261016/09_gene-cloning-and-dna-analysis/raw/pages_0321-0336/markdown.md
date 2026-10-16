![](images/page_320_image_2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["The insulin molecule"] --> B["30 amino acids"]
  B --> C["B chain"]
  B --> D["A chain"]
  C --> E["21 amino acids"]
  D --> E
  E --> F["Leader"]
  F --> G["Preproinsulin"]
  G --> H["Spontaneous folding"]
  H --> I["L"]
  I --> J["B"]
  J --> K["S"]
  K --> L["S"]
  L --> M["C"]
  M --> N["A"]
  N --> O["Cleavage"]
  O --> P["B"]
  P --> Q["S"]
  Q --> R["S"]
  R --> S["S"]
  S --> T["Insulin"]
```
</details>

Figure 15.1

The structure of the insulin molecule and a summary of its synthesis by processing from preproinsulin.

amino acid sequences of the A and B chains. The artificial genes would not necessarily have the same nucleotide sequences as the real gene segments coding for the A and B chains, but they would still specify the correct polypeptides. Two recombinant plasmids were constructed, one carrying the artificial gene for the A chain, and one the gene for the B chain.

In each case the artificial gene was ligated to a lacZ′ reading frame pre-sent in a pBR322‐type vector (Figure 15.2a). The insulin genes were therefore under the control of the strong lac promoter (Section  14.1.1), and were expressed as fusion proteins, consisting of the first few amino acids of β‐galactosidase followed by the A or B polypeptides (Figure  15.2b). Each gene was designed so that its β‐galactosidase and insulin segments were separated by a methionine residue, so that the insulin polypeptides could be cleaved from the β‐galactosidase segments by treatment with cyanogen bromide (Section 14.1.2). The purified A and B chains were then attached to each other by disulphide bond formation in the test tube.

The final step, involving disulphide bond formation, is actually rather  inefficient. A subsequent improvement was to synthesize not the individual  A and B genes, but the entire proinsulin reading frame,

Figure 15.2

The synthesis of recombinant insulin from artificial A and B chain genes.

![](images/page_321_image_4.jpg)

specifying B chain–C chain–A chain (see Figure 15.1). Although this is a more daunting proposition in terms of DNA synthesis, the prohormone has the big advantage of folding spontaneously into the correct disulphidebonded structure. The C chain segment can then be excised relatively easily by proteolytic cleavage.

## 15.1.2 Synthesis of human growth hormones in E. coli

At about the same time that recombinant insulin was first being made in E. coli, other researchers were working on similar projects with the human growth hormones somatostatin and somatotrophin. These two proteins act in conjunction to control growth processes in the human body, their malfunction leading to painful and disabling disorders such as acromegaly (uncontrolled bone growth) and dwarfism.

Somatostatin was the first human protein to be synthesized in E. coli. Being a very short protein, only 14 amino acids in length, it was ideally suited for artificial gene synthesis. The strategy used was the same as described for recombinant insulin, involving insertion of the artificial gene into a lacZ′ vector (Figure 15.3), synthesis of a fusion protein, and cleavage with cyanogen bromide.

![](images/page_322_image_2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["lac promoter"] --> B["lacZ'"]
  B --> C["Artificial somatostatin gene"]
  C --> D["Transform E. coli"]
  D --> E["Fusion protein"]
  E --> F["met"]
  F --> G["Somatostatin"]
  G --> H["Cyanogen bromide"]
  H --> I["Somatostatin"]
```
</details>

Figure 15.3

Production of recombinant somatostatin.

Somatotrophin presented a more difficult problem. This protein is 191 amino acids in length, equivalent to almost 600 bp of DNA, an impossible prospect for the DNA synthesis capabilities of the late 1970s. Instead, a combination of artificial gene synthesis and complementary DNA (cDNA) cloning was used to obtain a somatotrophin‐producing E. coli strain. Messenger RNA was obtained from the pituitary, the gland that produces somatotrophin in the human body, and a cDNA library prepared. The somatotrophin cDNA contained a single site for the restriction endonuclease HaeIII, which therefore cuts the cDNA into two segments (Figure 15.4a). The longer segment, consisting of codons 24–191, was retained for use in construction of the recombinant plasmid. The smaller segment was replaced by an artificial DNA molecule that reproduced the start of the somatotrophin gene and provided the correct signals for translation in E. coli (Figure 15.4b). The modified gene was then ligated into an expression vector carrying the lac promoter.

## 15.1.3 Recombinant factor VIII

Although a number of important pharmaceutical compounds have been obtained from genes cloned in E. coli, the general problems associated with using bacteria to synthesize foreign proteins (Section 14.2) have led in many cases to these organisms being replaced by eukaryotes. An example of a recombinant pharmaceutical produced in eukaryotic cells is human factor VIII, a protein that plays a central role in blood clotting. The commonest form of haemophilia in humans results from an inability to synthesize factor VIII, leading to a breakdown in the blood clotting path way and the well‐known symptoms associated with the disease.

Figure 15.4

Production of recombinant somatotrophin.

(a) Preparation of the somatotrophin cDNA fragment

![](images/page_323_image_5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Codons"] --> B{"HaeIII"}
  B -->|Restrict with HaeIII| C["Retain"]
  C --> D["Discard"]
  D -.-> E["0 24 24 191"]
```
</details>

(b) Expression

![](images/page_323_image_7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Synthetic leader"] -->|"Insert into an expression vector"| B((" ))
  C["lac promoter"] --> B
  B --> D["Transform E. coli"]
  D --> E["Somatotrophin is synthesized"]
```
</details>

Until recently the only way to treat haemophilia was by injection of purified factor VIII protein, obtained from human blood provided by donors. Purification of factor VIII is a complex procedure and the treatment is expensive. More critically, the purification is beset with difficulties, in particular in removing virus particles that may be present in the blood. Hepatitis and human immunodeficiency viruses can be and have been passed on to haemophiliacs via factor VIII injections. Recombinant factor VIII, free from contamination problems, would be a significant achievement for biotechnology.

The factor VIII gene is very large, over 186 kb in length, and is split into 26 exons and 25 introns (Figure 15.5a). The mRNA codes for a large polypeptide (2351 amino acids), which undergoes a complex series of posttranslational processing events, eventually resulting in a dimeric protein consisting of a large subunit, derived from the upstream region of the initial polypeptide, and a small subunit from the downstream segment (Figure 15.5b). The two subunits contain a total of 17 disulphide bonds and a number of glycosylated sites. As might be anticipated for such a large and complex protein, it has not been possible to synthesize an active version in E. coli.

![](images/page_324_image_2.jpg)

Figure 15.5

The factor VIII gene and its translation product.

Initial attempts to obtain recombinant factor VIII therefore involved mammalian cells. In the first experiments to be carried out the entire cDNA was cloned in hamster cells but yields of protein were disappointingly low. This was probably because the post‐translational events, although carried out correctly in hamster cells, did not convert all the initial product into an active form, limiting the overall yield. As an alternative, two separate fragments from the cDNA were used, one fragment coding for the large subunit polypeptide, and the second for the small subunit. Each cDNA fragment was ligated into an expression vector, downstream of the Ag promoter (a hybrid between the chicken β‐actin and rabbit β‐globin sequences) and upstream of a polyadenylation signal from SV40 virus (Figure 15.6). The plasmid was introduced into a hamster cell line and recombinant protein obtained. The yields were over ten times greater than those from cells containing the complete cDNA, and the resulting factor VIII protein was indistinguishable in terms of function from the native form.

Pharming (Section 14.3.3) has also been used for production of recombinant factor VIII. The complete human cDNA has been attached to the promoter for the whey acidic protein gene of pig, leading to synthesis of human factor VIII in pig mammary tissue and subsequent secretion of the protein in the milk. The factor VIII produced in this way appears to be exactly the same as the native protein and is fully functional in blood clotting assays. Similar results have been obtained with transgenic rabbits.

![](images/page_324_image_7.jpg)

<details>
<summary>text_image</summary>

Factor VIII cDNA
Ag promoter
SV40 polyadenylation
sequence
</details>

Figure 15.6

The expression signals used in production of recombinant factor VIII. The promoter is an artificial hybrid of the chicken β‐actin and rabbit β‐globin sequences, and the polyadenylation signal (needed for correct processing of the mRNA before translation into protein) is obtained from SV40 virus.

## 15.1.4 Synthesis of other recombinant human proteins

The list of human proteins synthesized by recombinant technology continues to grow (Table 15.1). As well as proteins used to treat disorders by replacement or supplementation of the dysfunctional versions, the list includes a number of growth factors (e.g. interferons and interleukins) with potential uses in cancer therapy. These proteins are synthesized in very limited amounts in the body, so recombinant technology is the only viable means of obtaining them in the quantities needed for clinical purposes. Other proteins, such as serum albumin, are more easily obtained, but are needed in such large quantities that production in microorganisms is still a more attractive option.

## 15.1.5 Recombinant vaccines

The final category of recombinant protein is slightly different from the examples given in Table 15.1. A vaccine is an antigenic preparation that, after injection into the bloodstream, stimulates the immune system to synthesize antibodies that protect the body against infection. The antigenic material present in a vaccine is normally an inactivated form of the infectious agent. For example, antiviral vaccines often consist of virus particles

Table 15.1

Some of the human proteins that have been synthesized from genes cloned in bacteria and/or eukaryotic cells or by pharming.

| PROTEIN | USED IN THE TREATMENT OF |
| --- | --- |
| $\alpha_{1}$-Antitrypsin | Emphysema |
| Deoxyribonuclease | Cystic fibrosis |
| Epidermal growth factor | Ulcers |
| Erythropoietin | Anaemia |
| Factor IX | Christmas disease |
| Factor VIII | Haemophilia |
| Fibroblast growth factor | Ulcers |
| Follicle stimulating hormone | Infertility treatment |
| Granulocyte colony stimulating factor | Cancers |
| Insulin | Diabetes |
| Insulin-like growth factor 1 | Growth disorders |
| Interferon-β | Cancers, AIDS |
| Interferon-γ | Cancers, rheumatoid arthritis |
| Interferon-α | Leukaemia and other cancers |
| Interleukins | Cancers, immune disorders |
| Lung surfactant protein | Respiratory distress |
| Relaxin | Used to aid childbirth |
| Serum albumin | Used as a plasma supplement |
| Somatostatin | Growth disorders |
| Somatotrophin | Growth disorders |
| Superoxide dismutase | Free radical damage in kidney transplants |
| Tissue plasminogen activator | Heart attack |
| Tumour necrosis factor | Cancers |

that have been attenuated by heating or a similar treatment. In the past, two problems have hindered the preparation of attenuated viral vaccines:

• The inactivation process must be 100% efficient, as the presence in a vaccine of just one live virus particle could result in infection. This has been a problem with vaccines for the cattle disease foot‐and‐mouth.
• The large amounts of virus particles needed for vaccine production are usually obtained from tissue cultures. Unfortunately, some viruses do not grow in tissue culture.

## Producing vaccines as recombinant proteins

The use of gene cloning in this field centres on the discovery that virusspecific antibodies are sometimes synthesized in response not only to the whole virus particle, but also to isolated components of the virus. This is particularly true of purified preparations of the proteins present in the virus coat (Figure 15.7). If the genes coding for the antigenic proteins of a particular virus could be identified and inserted into an expression vector, the methods described above for the synthesis of animal proteins could be employed in the production of recombinant proteins that might be used as vaccines. These vaccines would have the advantages that they would be free of intact virus particles and they could be obtained in large quantities.

The first success with this approach was with hepatitis B virus. Hepatitis B is endemic in many tropical parts of the world and leads to liver disease and possibly, after chronic infection, to cancer of the liver. A person who recovers from hepatitis B is immune to future infection because their blood contains antibodies to the hepatitis B surface antigen (HBsAg), which is one of the virus coat proteins. This protein has been synthesized in both

![](images/page_326_image_9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Isolated virus coat proteins"] -->|Inject into the bloodstream| B["Antibodies specific to the coat protein"]
  B --> C["Later infection by a complete virus"]
  C --> D["Antibodies can bind to the complete virus"]
```
</details>

Figure 15.7

The principle behind the use of a preparation of isolated virus coat proteins as a vaccine.

Saccharomyces cerevisiae, using a vector based on the 2 μm plasmid (Section 7.1), and in Chinese hamster ovary (CHO) cells. In both cases, the protein was obtained in reasonably high quantities, and when injected into test animals provided protection against hepatitis B.

The key to the success of recombinant HbsAg as a vaccine is provided by an unusual feature of the natural infection process for the virus. The bloodstream of infected individuals contains not only intact hepatitis B virus particles, which are 42 nm in diameter, but also smaller, 22 nm spheres made up entirely of HBsAg protein molecules. Assembly of these 22 nm spheres occurs during HbsAg synthesis in both yeast and hamster cells and it is almost certainly these spheres, rather than single HbsAg molecules, that are the effective component of the recombinant vaccine. The recombinant vaccine therefore mimics part of the natural infection process and stimulates antibody production, but as the spheres are not viable viruses the vaccine does not itself cause the disease. Both the yeast and hamster cell vaccines have been approved for use in humans, and the World Health Organization is promoting their use in national vaccination programmes.

Recombinant vaccines have also been successfully developed for human papillomavirus (HPV), different subtypes of which are responsible for a variety of cancers. The L1 coat protein gene has been expressed in S. cerevisiae, giving rise to virus‐like particles made up of aggregates of the L1 protein. Just like the HbsAg vaccines, these particles lack any nucleic acid and so are not infectious. To broaden the effectiveness of recombinant HPV vaccines, a variety of recombinant yeast strains have been produced, each synthesizing the L1 protein from a different HPV subtype. The viruslike particles from these strains are then combined to make a divalent or quadrivalent vaccine (Figure  15.8). These vaccines provide protection against cervical cancer in women and a range of sexually transmitted infections in men.

Figure 15.8

Synthesis of a quadrivalent HPV vaccine. The four recombinant yeast strains synthesize L1 proteins from HPV subtypes 6, 11, 16, and 18.

![](images/page_327_image_7.jpg)

<details>
<summary>flowchart</summary>

This flowchart illustrates the progression of yeast cultures expressing L1 genes from different HPV subtypes through a virus-like vaccine to produce quadrivalent vaccines.
</details>

## Recombinant vaccines in transgenic plants

The advent of pharming (Section 14.3.3) has led to the possibility of using transgenic plants as the hosts for synthesis of recombinant vaccines. The ease with which plants can be grown and harvested means that this technology might be applicable for developing parts of the world where the more expensive approaches to recombinant protein production might be difficult to sustain. If the recombinant vaccine is effective after oral administration, then immunity could be acquired simply by eating part or all of the transgenic plant. A simpler and cheaper means of carrying out a mass vaccination programme would be hard to imagine.

The feasibility of this approach has been demonstrated by trials with vaccines such as HbsAg and the coat proteins of measles virus and respiratory syncytial virus. In each case, immunity was conferred by feeding the transgenic plant to test animals. Attempts are also being made to engineer plants that express a variety of vaccines, so that immunity against a range of diseases can be acquired from a single source. The main problem currently faced by the companies developing this technology is that the amount of recombinant protein synthesized by the plant is often insufficient to stimulate complete immunity against the target disease. To be completely effective, the vaccine needs to make up 8–10% of the soluble protein content of the part of the plant which is eaten, but in practice yields are much less than this, usually not more than 0.5%. Variability in the yields between different plants in a single crop is also a concern. A possible solution is to place the cloned gene in the chloroplast genome rather than the plant nucleus (Section  7.2.2), as this generally results in much higher yields of recombinant protein. Chloroplast synthesis of various vaccine proteins has been achieved, including ones active against anthrax, plague, smallpox, and the parasitic protozoan Entamoeba histolytica. Tobacco and lettuce chloroplasts have also been used to synthesize fusions between surface proteins from Vibrio cholerae and the malaria parasite Plasmodium falciparum. When fed to mice these plants provided protection against cholera toxin and also stimulated synthesis of antibodies that reduced the ability of P. falciparum parasites to invade human red blood cells (effectiveness against malaria could not be directed tested in mice because P. falciparum does not infect mice). Cholera and malaria are major diseases in many parts of the world, and development of an easily administered vaccine that confers dual protection would be an important advance for human health.

Plants are also being used in a radically different approach to disease protection, one in which the goal is not to make a protein that will stimulate an immune response, but instead to use the plant to synthesize the antibody that is the product of the immune response. Four transgenic tobacco lines have been engineered, each producing a different component of an antibody specific for the surface protein antigen A gene of Streptococcus mutans. After crosses between these lines, a single variety of  transgenic tobacco containing all four cloned genes was obtained (Figure 15.9). These plants assembled functional antibodies in their cells. S. mutans inhabits the human oral cavity and is a major cause of dental caries, which affects over 60% of schoolchildren in most industrialized

Figure 15.9

Transgenic tobacco that synthesizes an antibody active against S. mutans.

![](images/page_329_image_4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Tobacco plants synthesizing different antibody components"] --> B["Kappa chain"]
  A --> C["A-G heavy chain"]
  A --> D["Joining chain"]
  A --> E["Secretory factor"]
  B --> F["Secretory immunoglobulin recognizing S. mutans"]
  C --> F
  D --> F
  E -->|Crosses between lines| F
```
</details>

countries. A cheap source of S. mutans antibodies which might provide protection against caries, and which could be administered by rubbing on to the surface of the teeth rather than by injection, has been sought for many years.

## Live recombinant virus vaccines

The use of live vaccinia virus as a vaccine for smallpox dates back to 1796, when Edward Jenner first realized that this virus, harmless to humans, could stimulate immunity against the related and much more dangerous smallpox virus. The term ‘vaccine’ comes from vaccinia. Its use resulted in the worldwide eradication of smallpox in 1980.

A more recent idea is that recombinant vaccinia viruses could be used as live vaccines against other diseases. If a gene coding for a virus coat protein, for example HBsAg, is ligated into the vaccinia genome under control of a vaccinia promoter, then the gene will be expressed (Figure  15.10). After injection into the bloodstream, replication of the recombinant virus results not only in new vaccinia particles, but also in significant quantities of the major surface antigen. Immunity against both smallpox and hepatitis B would result.

This remarkable technique has considerable potential. Recombinant vaccinia viruses expressing a number of foreign genes have been constructed and shown to confer immunity against the relevant diseases in experimental animals (Table 15.2). The possibility of broad‐spectrum vaccines is raised by the demonstration that a single recombinant vaccinia, expressing the genes for influenza virus haemagglutinin, HBsAg, and herpes simplex virus glycoprotein, confers immunity against each disease in monkeys. Studies of vaccinia viruses expressing the rabies glycoprotein have shown that deletion of the vaccinia gene for the enzyme thymidine

![](images/page_330_image_2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Vaccinia promoter"] --> B["Recombinant vaccinia genome"]
  C["Hepatitis B major surface antigen gene"] --> B
  B --> D["Inject recombinant vaccinia particles into the bloodstream"]
  D --> E["Hepatitis B protein"]
  D --> F["Vaccinia virus"]
  E --> G["Immune system synthesizes antibodies against both vaccinia and hepatitis B"]
  F --> G
  G --> H["Anti-hepatitis B"]
  G --> I["Anti-vaccinia"]
```
</details>

Figure 15.10

Table 15.2

The rationale behind the use of a recombinant vaccinia virus.

Some of the foreign genes that have been expressed in recombinant vaccinia viruses.

## GENE

## Human diseases

Plasmodium falciparum (malaria parasite) surface antigen

Influenza virus coat proteins

Hepatitis B surface antigen

Herpes simplex glycoproteins

Human immunodeficiency virus (HIV) envelope proteins

Leishmania membrane glycoprotein

Vesicular somatitis coat proteins

Sindbis virus proteins

## Animal diseases

Rabies virus G protein

Rinderpest virus F and H proteins

Feline leukaemia virus envelope protein

Newcastle disease virus F glycoprotein

kinase prevents the virus from replicating. This avoids the possibility that animals treated with the live vaccine will develop any form of cowpox, the disease caused by normal vaccinia. This particular live virus vaccine is now being used in rabies control in Europe and North America.

## 15.2 Identification of genes responsible for human diseases

A second major area of medical research in which gene cloning is having an impact is in the identification and isolation of genes responsible for human diseases. A genetic or inherited disease is one that is caused by a defect in a specific gene (Table 15.3), individuals carrying the defective gene being predisposed toward developing the disease at some stage of their lives. With some inherited diseases, such as haemophilia, the gene is present on the X chromosome, so all males carrying the gene express the disease state. Females with one defective gene and one correct gene are healthy but can pass the disease on to their male offspring. Genes for other diseases are present on autosomes and in most cases are recessive, so both chromosomes of the pair must carry a defective version for the disease to occur. A few diseases, including Huntington’s chorea, are autosomal dominant, so a single copy of the defective gene is enough to lead to the disease state.

With some genetic diseases, the symptoms manifest themselves early in life, but with others the disease may not be expressed until the individual is middle‐aged or elderly. Cystic fibrosis is an example of the former, and neurodegenerative diseases such as Alzheimer’s and Huntington’s are examples of the latter. With a number of diseases that appear to have a genetic component, cancers in particular, the overall syndrome is complex with the disease remaining dormant until triggered by some metabolic or  environmental stimulus. If predisposition to these diseases can be diagnosed, the risk factor can be reduced by careful management of the patient’s lifestyle to minimize the chances of the disease being triggered.

Table 15.3

Some of the commonest genetic diseases in the UK.

| DISEASE | SYMPTOMS | FREQUENCY (BIRTHS PER YEAR) |
| --- | --- | --- |
| Inherited breast cancer | Cancer | 1 in 300 females |
| Cystic fibrosis | Lung disease | 1 in 2000 |
| Huntington's chorea | Neurodegeneration | 1 in 2000 |
| Duchenne muscular dystrophy | Progressive muscle weakness | 1 in 3000 males |
| Haemophilia A | Blood disorder | 1 in 4000 males |
| Sickle cell anaemia | Blood disorder | 1 in 10,000 |
| Phenylketonuria | Mental retardation | 1 in 12,000 |
| β-Thalassaemia | Blood disorder | 1 in 20,000 |
| Retinoblastoma | Cancer of the eye | 1 in 20,000 |
| Haemophilia B | Blood disorder | 1 in 25,000 males |
| Tay-Sachs disease | Blindness, loss of motor control | 1 in 200,000 |

Genetic diseases have always been present in the human population, but their importance has increased in recent decades. This is because vaccination programs, antibiotics, and improved sanitation have reduced the prevalence of infectious diseases such as smallpox, tuberculosis, and cholera, which were major killers up to the mid‐20<sup>th</sup> century. The result is that a greater proportion of the population now dies from a disease that has a genetic component, especially the late‐onset diseases that are now more common because of increased life expectancies. Medical research has been successful in controlling many infectious diseases; can it be equally successful with genetic disease?

## 15.2.1 How to identify a gene for a genetic disease

There are a number of reasons why identifying the gene responsible for a genetic disease is important:

Gene identification may provide an indication of the biochemical basis to the disease, enabling therapies to be designed.
Identification of the mutation present in a defective gene can be used to devise a screening programme so that the mutant gene can be identified in individuals who are carriers or who have not yet developed the disease. Carriers can receive counselling regarding the chances of their children inheriting the disease. Early identification of individuals who have not yet developed the disease allows appropriate precautions to be taken to reduce the risk of the disease becoming expressed.
• Identification of the gene is a prerequisite for gene therapy (Section 15.3).

There is no single strategy for identification of genes that cause diseases; the best approach depends on the information that is available about the disease. To gain an understanding of the principles of this type of work, we will consider the most common and most difficult scenario. This is when all that is known about the disease is that certain people have it. Even with such an unpromising starting point, DNA techniques can locate the relevant gene.

Locating the approximate position of the gene in the human genome If there is no information about the desired gene, how can it be located in the human genome? The answer is to use basic genetics to determine the approximate position of the gene on the human genetic map. Genetic mapping is usually carried out by **linkage analysis**, in which the inheritance pattern for the target gene is compared with the inheritance patterns for genetic loci whose map positions are already known. If two loci are inherited together, they must be very close on the same chromosome (Figure  15.11a). If they are on different chromosomes, then random

Inheritance patterns for linked and unlinked genes. Three families are shown, circles representing females and squares representing males. (a) Two closely linked genes are almost always inherited together. (b) Two genes on different chromosomes display random segregation. (c) Two genes that are far apart on a single chromosome are often inherited together, but recombination may unlink them.

Figure 15.11

(a) Genes are linked

![](images/page_333_image_5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["A"] --> B["B"]
  B --> C["a"]
  C --> D["a b"]
  D --> E["a b"]
  E --> F["A"]
  F --> G["A"]
  G --> H["A"]
  H --> I["a b"]
```
</details>

(b) Genes are on different chromosomes

![](images/page_333_image_7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["A"] --> B["B"]
  B --> C["a"]
  C --> D["b"]
  D --> E["A"]
  E --> F["b"]
  F --> G["a"]
  G --> H["b"]
  H --> I["a"]
```
</details>

(c) Genes are on the same chromosome, but far apart

![](images/page_333_image_9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["A"] --> B["B"]
  B --> C["a"]
  C --> D["b"]
  D --> E["A"]
  E --> F["a"]
  F --> G["b"]
  G --> H["A"]
  H --> I["b"]
```
</details>

Product of recombination

segregation during meiosis will result in the loci displaying different inheritance patterns (Figure 15.11b). If they are on the same chromosome but not close together, then recombination events will occasionally unlink them (Figure 15.11c). Demonstration of linkage with one or more mapped genetic loci is therefore the key to understanding the chromosomal position of an unmapped gene.

With humans it is not possible to carry out directed breeding programs aimed at determining the map position of a desired gene. Instead, mapping of disease genes must make use of data available from **pedigree analysis**, in which inheritance of the gene is examined in families with a high incidence of the disease being studied. It is important to be able to obtain DNA samples from at least three generations of each family, and the more family members there are the better, but unless the disease is very uncommon it is usually possible to find suitable pedigrees. Linkage is studied between the presence/absence of the disease and the inheritance of **DNA markers**. A DNA marker is simply a DNA sequence that is variable and so exists in two or more allelic forms, and whose location in the genome is known. To illustrate how linkage analysis is used with DNA markers we will look at the way in which one of the genes conferring susceptibility to human breast cancer was mapped.

## Linkage analysis of the human BRCA1 gene

The first breakthrough in mapping the human breast cancer susceptibility gene BRCA1 occurred in 1990 as a result of **restriction fragment length polymorphism (RFLP) linkage analyses**. This study showed that in families with a high incidence of breast cancer, a significant number of the women who suffered from the disease all possessed the same version of an RFLP called D17S74. An RFLP results from a DNA sequence variation that causes a change in a restriction site (Figure 15.12a). When digested with a restriction endonuclease the loss of the site is revealed because two fragments remain joined together. Originally, RFLPs were typed by Southern hybridization of restricted genomic DNA, but this is a time‐consuming process, so nowadays the presence or absence of the restriction site is usually determined by PCR (Figure 15.12b). The D17S74 RFLP had previously been mapped to the long arm of chromosome 17; the gene being sought  –  BRCA1  –  must therefore also be located on the long arm of chromosome 17.

![](images/page_334_image_2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["(a) An RFLP"] --> B["...AGTGAATTCGTAC..."]
  B --> C["...AGTGATTCGTAC..."]
  C --> D["Sequence variation results in loss of EcoRI site"]
  E["(b) Typing an RFLP by PCR"] --> F["Restriction site"]
  F --> G["Markers"]
  F --> H["PCR, restrict"]
  G --> I["PCR, restrict"]
  H --> I
  J["PCR primers"] --> I
```
</details>

Figure 15.12

Restriction fragment length polymorphisms. (a) An RFLP is a sequence variation that changes a restriction site. (b) Typing an RFLP by PCR. In the middle lane the PCR product gives two bands because it is cut by treatment with the restriction enzyme. In the right‐hand lane there is just one band because the template DNA lacks the restriction site.

This initial linkage result was extremely important, as it indicated in which region of the human genome the BRCA1 gene was to be found, but it was far from the end of the story. In fact, over 1000 genes are thought to lie in this particular stretch of chromosome 17. The next objective was therefore to carry out more linkage studies to try to pinpoint BRCA1 more accurately. This was achieved by examining the region containing BRCA1 for **short tandem repeats (STRs)**. These sequences, also called **microsatellites**, are made up of short repetitive sequences of 1–13 nucleotides in length, linked head to tail (Figure 15.13a). The number of repeats present in a particular STR varies, usually between 5 and 20. The number can be determined by carrying out a PCR using primers that anneal either side of the STR, and then examining the size of the resulting product by agarose or polyacrylamide gel electrophoresis (Figure 15.13b). STRs are useful for fine scale mapping because many of them exist in three or more allelic forms, rather than just the two alleles that are possible for an RFLP.

## Figure 15.13

Short tandem repeats. (a) An STR is a repetitive sequence made up of short units 1–13 nucleotides in length. (b) Typing an STR by PCR. The PCR product in the right‐hand lane is slightly longer than that in the middle lane, because the template DNA from which it is generated contains an additional CA unit.

(a) Two versions of an STR

![](images/page_335_image_5.jpg)

(b) Typing an STR by PCR

![](images/page_335_image_7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Markers"] --> B["PCR"]
  C["PCR primers"] --> D["PCR"]
  B --> D
  D --> E["Final Product"]
```
</details>

Several  alleles of an STR might therefore be present within a single pedigree, enabling more detailed mapping to be carried out. STR linkage mapping placed BRCA1 between two STRs called D17S1321 and D17S1325, reducing the size of the BRCA1 region from 20 Mb down to just 600 kb (Figure  15.14). This approach to locating a gene is called **positional cloning**.

## Identification of candidates for the disease gene

One might imagine that once the map location of the disease gene has been determined the next step is simply to refer to the genome sequence in order to identify the gene. Unfortunately, a great deal of work still has to be done. Genetic mapping, even in its most precise form, only gives an approximate indication of the location of a gene. In the breast cancer project the researchers were fortunate in being able to narrow the search area down to just 600 kb – often 10 Mb or more of DNA sequence has to be examined. Such large stretches of DNA could contain many genes: the 600 kb breast cancer region contained over 60 genes, any one of which could have been BRCA1.

A variety of approaches can be used to identify which of the genes in a mapped region is the disease gene:

• The expression profiles of the **candidate genes** can be examined by hybridization analysis or RT–PCR of RNA from different tissues. For example, BRCA1 would be expected to hybridize to RNA prepared from breast tissue, and also to ovary tissue RNA, ovarian cancer frequently being associated with inherited breast cancer.
• The presence of homologues of the candidate gene in other mammalian species can be tested by searching their genome sequences using BLAST