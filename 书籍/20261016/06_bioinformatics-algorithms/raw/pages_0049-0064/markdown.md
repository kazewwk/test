![](images/page_48_image_1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  subgraph Top_Left["#G - #C decreasing"]
    direction TB
  Start((Start)) --> oriC1["oriC"]
  Start --> oriC2["oriC"]
  Start --> TerC1["terC"]
  Start --> TerC2["terC"]
  Start --> TerC3["terC"]
  TerC1 --> TerC3
  TerC2 --> TerC3
  TerC3 --> TerC1
  TerC3 --> TerC2
  TerC3 --> TerC1
  TerC3 --> TerC2
  TerC3 --> TerC1
  TerC3 --> TerC2
  TerC3 --> TerC1
  TerC3 --> TerC2
  TerC3 --> TerC1
  TerC3 --> TerC2
  TerC3 --> TerC1
  TerC3 --> TerC2
  TerC3 --> TerC1
```
</details>

FIGURE 1.11 Because of deamination, each forward half-strand has a shortage of cytosine compared to guanine, and each reverse half-strand has a shortage of guanine compared to cytosine. The dashed blue line illustrates an imaginary walk along the outer strand of the genome counting the difference between the counts of G and C. We assume that the difference between these counts is positive on the forward half-strand and negative on the reverse half-strand.

Note that we can compute $\mathrm{SKEW}_{i+1}  (  Genone )$ from $\mathrm{SKEW}_{i}  (  Greenme )$ according to the nucleotide in position i of Genome. If this nucleotide is G, then $\begin{aligned} & SKEW _{i+1}  (  Genome )   =\\ \end{aligned}$ $\mathrm{SKEW}_{i} (Genome)+1;$ if this nucleotide is C, then $\mathrm{SKEW_{i+1}(Genome) = SKEW_i(Genome) -}$ 1; otherwise, $\mathsf{SKEW}_{i+1}\big(Genome\big)=\mathsf{SKEW}_{i}\big(Genome\big)$

![](images/page_48_chart_4.jpg)

<details>
<summary>line</summary>

| Position | Skew |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | -1 |
| 3 | -1 |
| 4 | 0 |
| 5 | 1 |
| 6 | 2 |
| 7 | 1 |
| 8 | 1 |
| 9 | 1 |
| 10 | 0 |
| 11 | 1 |
| 12 | 2 |
| 13 | 1 |
| 14 | 0 |
| 15 | 0 |
| 16 | 0 |
| 17 | 0 |
| 18 | -1 |
| 19 | 0 |
| 20 | -1 |
| 21 | -2 |
</details>

FIGURE 1.12 The skew diagram for Genome = CATGGGCATCGGCCATACGCC.

Figure 1.13 depicts the skew diagram for a linearized E. coli genome. Notice the very clear pattern! It turns out that the skew diagram for many bacterial genomes has a

similar characteristic shape.

**STOP and Think:** After looking at the skew diagram in Figure 1.13, where do you think that oriC is located in E. coli?

![](images/page_49_image_3.jpg)

![](images/page_49_chart_4.jpg)

<details>
<summary>line</summary>

| position | skew |
| --- | --- |
| 0 | 0 |
| ~1500000 | ~25000 |
| ~3900000 | ~-14000 |
| ~4600000 | ~-2500 |
</details>

FIGURE 1.13 The skew diagram for E. coli achieves a maximum and minimum at positions 1550413 and 3923620, respectively.

Let’s follow the $5 ^ { \prime } \rightarrow 3 ^ { \prime }$ direction of DNA and walk along the chromosome from terC to oriC (along a reverse half-strand), then continue on from oriC to terC (along a forward half-strand). In Figure 1.11, we saw that the skew is decreasing along the reverse half-strand and increasing along the forward half-strand. Thus, the skew should achieve a minimum at the position where the reverse half-strand ends and the forward half-strand begins, which is exactly the location of oriC! We have just developed an algorithm for locating oriC: it should be found where the skew attains a minimum.

## Minimum Skew Problem:

Find a position in a genome where the skew diagram attains a minimum.

**Input**: A DNA string Genome.

**Output**: All integer(s) i minimizing SKEW<sub>i</sub>(Genome) among all values of i (from 0 to |Genome|).

![](images/page_49_image_11.jpg)

![](images/page_50_image_1.jpg)

**STOP and Think:** Note that the skew diagram changes depending on where we start our walk along the circular chromosome. Do you think that the minimum of the skew diagram points to the same position in the genome regardless of where we begin walking to generate the skew diagram?

## Some Hidden Messages are More Elusive than Others

Solving the Minimum Skew Problem now provides us with an approximate location of oriC at position 3923620 in E. coli. In an attempt to confirm this hypothesis, let’s look for a hidden message representing a potential DnaA box near this location. Solving the Frequent Words Problem in a window of length 500 starting at position 3923620 (shown below) reveals no 9-mers (along with their reverse complements) that appear three or more times! Even if we have located oriC in E. coli, it appears that we still have not found the DnaA boxes that jump-start replication in this bacterium . .

aatgatgatgacgtcaaaaggatccggataaaacatggtgattgcctcgcataacgcggt atgaaaatggattgaagcccgggccgtggattctactcaactttgtcggcttgagaaaga cctgggatcctgggtattaaaaagaagatctatttatttagagatctgttctattgtgat ctcttattaggatcgcactgccctgtggataacaaggatccggcttttaagatcaacaac ctggaaaggatcattaactgtgaatgatcggtgatcctggaccgtataagctgggatcag aatgaggggttatacacaactcaaaaactgaacaacagttgttctttggataactaccgg ttgatccaagcttcctgacagagttatccacagtagatcgcacgatctgtatacttattt gagtaaattaacccacgatcccagccattcttctgccggatcttccggaatgtcgtgatc aagaatgttgatcttcagtg

![](images/page_50_image_6.jpg)

## STOP and Think: What would you do next?

Before we give up, let’s examine the oriC of Vibrio cholerae one more time to see if it provides us with any insights on how to alter our algorithm to find DnaA boxes in E. coli. You may have noticed that in addition to the three occurrences of **ATGATCAAG** and three occurrences of its reverse complement **CTTGATCAT**, the Vibrio cholerae oriC contains additional occurrences of **ATGATCAAC** and **CATGATCAT**, which differ from **ATGATCAAG** and **CTTGATCAT** in only a single nucleotide:

atca**ATGATCAAC**gtaagcttctaagc**ATGATCAAG**gtgctcacacagtttatccacaac ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca cggaaag**ATGATCAAG**agaggatgatttcttggccatatcgcaatgaatacttgtgactt gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt acgaaag**CATGATCAT**ggctgttgttctgtttatcttgttttgactgagacttgttagga tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat tgataatgaatttacatgcttccgcgacgatttacct**CTTGATCAT**cgatccgattgaag atcttcaattgttaattctcttgcctcgactcatagccatgatgagct**CTTGATCAT**gtt tccttaaccctctattttttacggaaga**ATGATCAAG**ctgctgct**CTTGATCAT**cgtttc

Finding eight approximate occurrences of our target 9-mer and its reverse complement in a short region is even more statistically surprising than finding the six exact occurrences of **ATGATCAAG** and its reverse complement **CTTGATCAT** that we stumbled upon in the beginning of our investigation. Furthermore, the discovery of these approximate 9-mers makes sense biologically, since DnaA can bind not only to “perfect” DnaA boxes but to their slight variations as well.

We say that position i in k-mers $p _ { 1 } \cdots p _ { k }$ and $q _ { 1 } \cdots q _ { k }$ is a **mismatch** if $p _ { i } \neq q _ { i }$ . The number of mismatches between strings p and q is called the **Hamming distance** between these strings and is denoted HAMMINGDISTANCE $( p , q )$

## Hamming Distance Problem:

Compute the Hamming distance between two strings.

**Input**: Two strings of equal length.

**Output**: The Hamming distance between these strings.

We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern’ of Text having d or fewer mismatches with Pattern, i.e., HAMMINGDISTANCE(Pattern, Pattern0)  d. Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.

## Approximate Pattern Matching Problem:

Find all approximate occurrences of a pattern in a string.

**Input**: Strings Pattern and Text along with an integer d.

**Output**: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

Our goal now is to modify our previous algorithm for the Frequent Words Problem in order to find DnaA boxes by identifying frequent k-mers, possibly with mismatches. Given strings Text and Pattern as well as an integer d, we define COUNT<sub>d</sub>(Text, Pattern) as the number of occurrences of Pattern in Text with at most d mismatches. For example,

$$
\text {COUNT} _ {1} (\text {AACAAGCATAAACATTAAAGAG, AAAAA}) = 4
$$

because **AAAAA** appears four times in this string with at most one mismatch: **AACAA**, **ATAAA**, **AAACA**, and **AAAGA**. Notice that two of these occurrences overlap.

![](images/page_52_image_4.jpg)

**EXERCISE BREAK:** Compute COUNT<sub>2</sub>(AACAAGCATAAACATTAAAGAG, AAAAA).

Computing COUNT<sub>d</sub>(Text, Pattern) simply requires us to compute the Hamming distance between Pattern and every k-mer substring of Text, as follows.

```python
APPROXIMATEPATTERNCOUNT(Text, Pattern, d)
    count ← 0
    for i ← 0 to |Text| - |Pattern|
        Pattern' ← Text(i, |Pattern|)
        if HAMMINGDISTANCE(Pattern, Pattern') ≤ d
            count ← count + 1
    return count
```

![](images/page_52_image_8.jpg)

**EXERCISE BREAK:** Implement **APPROXIMATEPATTERNCOUNT**. What is its running time?

A **most frequent k-mer with up to d mismatches** in Text is simply a string Pattern maximizing COUNT<sub>d</sub>(Text, Pattern) among all k-mers. Note that Pattern does not need to actually appear as a substring of Text; for example, as we saw above, **AAAAA** is the most frequent 5-mer with 1 mismatch in **AACAA**GC**ATAAACA**TT**AAAGA**G, even though it does not appear exactly in this string. Keep this in mind while solving the following problem.

![](images/page_52_image_11.jpg)

## Frequent Words with Mismatches Problem:

Find the most frequent k-mers with mismatches in a string.

**Input**: A string Text as well as integers k and d.

**Output**: All most frequent k-mers with up to d mismatches in Text.

**CHARGING STATION (Solving the Frequent Words with Mismatches Problem):** One way to solve the above problem is to generate all $4 ^ { k } \; k \mathrm { - m e r s } \; P a t t e r n ,$ compute $\mathrm { C O U N T } _ { d } \big ( T _ { } { e x t } , P a t t e r n , d \big )$ for each k-mer, and then output k-mers with the maximum number of approximate occurrences. This is an inefficient approach in practice, since many of the $4 ^ { k }$ k-mers that this method analyzes should not be considered because neither they nor their mutated versions (with up to d mismatches) appear in Text. Check out this Charging Station to learn about a better approach that avoids analyzing such hopeless k-mers.

We now redefine the Frequent Words Problem to account for both mismatches and reverse complements. Recall that Pattern refers to the reverse complement of Pattern.

## Frequent Words with Mismatches and Reverse Complements Problem:

Find the most frequent k-mers (with mismatches and reverse complements) in a string.

**Input**: A DNA string Text as well as integers k and d.

**Output**: All k-mers Pattern that maximize the sum $COUNT _ { d } (Text,Patterm) +$ $\mathrm { C O U N T } _ { d } \big ( T e x t , \overline { { P a t t e r n } } \big )$ over all possible k-mers.

## A Final Attempt at Finding DnaA Boxes in E. coli

We now make a final attempt to find DnaA boxes in E. coli by finding the most frequent 9-mers with mismatches and reverse complements in the region suggested by the minimum skew as oriC. Although the minimum of the skew diagram for E. coli is found at position 3923620, we should not assume that its oriC is found exactly at this position due to random fluctuations in the skew. To remedy this issue, we could choose a larger window size $( \mathrm { e . g . } ,   L = 1 0 0 0 )$ , but expanding the window introduces the risk that we may bring in other clumped 9-mers that do not represent DnaA boxes but appear in this window more often than the true DnaA box. It makes more sense to try a small window either starting, ending, or centered at the position of minimum skew.

Let’s cross our fingers and identify the most frequent 9-mers (with 1 mismatch and reverse complements) within a window of length 500 starting at position 3923620 of the E. coli genome. Bingo! The experimentally confirmed DnaA box in E. coli (**TTATCCACA**) is a most frequent 9-mer with 1 mismatch, along with its reverse complement **TGTGGATAA**:

aatgatgatgacgtcaaaaggatccggataaaacatggtgattgcctcgcataacgcggt atgaaaatggattgaagcccgggccgtggattctactcaactttgtcggcttgagaaaga cctgggatcctgggtattaaaaagaagatctatttatttagagatctgttctattgtgat ctcttattaggatcgcactgccc**TGTGGATAA**caaggatccggcttttaagatcaacaac ctggaaaggatcattaactgtgaatgatcggtgatcctggaccgtataagctgggatcag aatgagggg**TTATACACA**actcaaaaactgaacaacagttgttc**TTTGGATAA**ctaccgg ttgatccaagcttcctgacagag**TTATCCACA**gtagatcgcacgatctgtatacttattt gagtaaattaacccacgatcccagccattcttctgccggatcttccggaatgtcgtgatc aagaatgttgatcttcagtg

You will notice that we highlighted an interior interval of this sequence with darker text. This region is the experimentally verified oriC of E. coli, which starts 37 nucleotides after position 3923620, where the skew reaches its minimum value.

We were fortunate that the DnaA boxes of E. coli are captured in the window that we chose. Moreover, while **TTATCCACA** represents a most frequent 9-mer with 1 mis match and reverse complements in this 500-nucleotide window, it is not the only one: GGATCCTGG, GATCCCAGC, GTTATCCAC, AGCTGGGAT, and CTGGGATCA also appear four times with 1 mismatch and reverse complements.

![](images/page_54_image_4.jpg)

**STOP and Think:** In this chapter, every time we find oriC, we seem to find some other surprisingly frequent 9-mers. Why do you think this is?

We do not know what purpose — if any — these other 9-mers serve in the E. coli genome, but we do know that there are many different types of hidden messages in genomes; these hidden messages have a tendency to cluster within a genome, and most of them have nothing to do with replication. One example is the regulatory DNA motifs responsible for gene expression that we will study in Chapter 2. The important lesson is that existing approaches to oriC prediction remain imperfect and sometimes inconclusive. However, even providing biologists with a small collection of 9-mers as candidate DnaA boxes is a great aid as long as one of these 9-mers is correct.

Thus, the moral of this chapter is that even though computational predictions can be powerful, bioinformaticians should collaborate with biologists to verify their computational predictions. Or improve these predictions: the next question hints at how oriC predictions can be carried out using **comparative genomics**, a bioinformatics approach that uses evolutionary similarities to answer difficult questions about genomes.

![](images/page_54_image_8.jpg)

**STOP and Think:** Salmonella enterica is a close relative of E. coli that causes typhoid fever and foodborne illness. After having learned what DnaA boxes look like in E. coli, how would you search for DnaA boxes in Salmonella enterica?

You will have an opportunity to look for DnaA boxes in Salmonella enterica in the epilogue, which will feature a “Challenge Problem” asking you to apply what you have learned to a real dataset. Some chapters also have an “Open Problems” section outlining unanswered research questions.

## Epilogue: Complications in oriC Predictions

In this chapter, we have considered three genomes and found three different hypoth esized 9-mers encoding DnaA boxes: **ATGATCAAG** in Vibrio cholerae, **CCTACCACC** in Thermotoga petrophila, and **TTATCCACA** in E. coli. We must warn you that finding oriC is often more complex than in the three examples we considered. Some bacteria have even fewer DnaA boxes than E. coli, making it difficult to identify them. The terC region is often located not directly opposite to oriC but may be significantly shifted, resulting in reverse and forward half-strands having substantially different lengths. The position of the skew minimum is often only a rough indicator of oriC position, which forces researchers to expand their windows when searching for DnaA boxes, bringing in extra neous repeated substrings. Finally, skew diagrams do not always look as nice as that of E. coli; for example, the skew diagram for Thermotoga petrophila is shown in Figure 1.14.

![](images/page_55_chart_4.jpg)

<details>
<summary>line</summary>

| position | skew |
| --- | --- |
| 0 | ~0 |
| 500000 | ~-9000 |
| 1000000 | ~-14000 |
| 1500000 | ~-16000 |
| 2000000 | ~-14000 |
</details>

FIGURE 1.14 The skew diagram for Thermotoga petrophila achieves a minimum at position 787199 but does not have the same nice shape as the skew diagram for E. coli.

**STOP and Think:** What evolutionary process could possibly explain the shape of the skew diagram for Thermotoga petrophila?

![](images/page_55_image_7.jpg)

Since the skew diagram for Thermotoga petrophila is complex and the oriC for this genome has not even been experimentally verified, there is a chance that the region predicted by Ori-Finder as the oriC region for Thermotoga petrophila (or even for Vibrio cholerae) is actually incorrect!

You now should have a good sense of how to locate oriC and DnaA boxes computationally. We will take the training wheels off and ask you to solve a challenge problem.

**CHALLENGE PROBLEM:** Find DnaA boxes in Salmonella enterica.

## Open Problems

Multiple replication origins in a bacterial genome

Biologists long believed that each bacterial chromosome has only one oriC. Wang et al., 2011 genetically modified E. coli by inserting a synthetic oriC a million nucleotides away from the bacterium’s known oriC. To their surprise, E. coli continued business as usual, starting replication at both locations!

Following the publication of this paper, the search for naturally occurring bacteria with multiple oriCs immediately started. In 2012, Xia raised doubts about the “single oriC” postulate and gave examples of bacteria with highly unusual skews. In fact, having more than one oriC makes sense in the light of evolution: if the genome is long and replication is slow, then multiple replication origins would decrease the amount of time that the bacterium must spend replicating its DNA.

For example, Wigglesworthia glossinidia, a symbiotic bacterium living in the intestines of tsetse flies, has the atypical skew diagram shown in Figure 1.15. Since this diagram has at least two pronounced local minima, Xia argued that this bacterium may have two or more oriC regions.

We should be careful with Xia’s hypothesis that this bacterium has two oriCs, as there may be alternative explanations for multiple local minima in the skew. For example, **genome rearrangements** (which we will study in Chapter 6) move genes within a genome and often reposition them from the forward to the reverse half-strand and vice-versa, thus resulting in irregularities in the skew diagram. One example of a genome rearrangement is a **reversal**, which flips around a segment of chromosome and switches it to the opposite strand; Figure 1.16 shows what happens to the skew diagram after a reversal.

Another difficulty is presented by the fact that different species of bacteria may exchange genetic material in **horizontal gene transfer**. If a gene from the forward half-strand of one bacterium is transferred to the reverse half-strand of another (or vice-versa), then we will observe an irregularity in the skew diagram. As a result, the question about the number of oriCs of Wigglesworthia glossinidia remains unresolved.

However, if you could demonstrate that there exist two sets of identical DnaA boxes in the vicinity of two local minima in the skew diagram of Wigglesworthia glossinidia, then you would have the first solid evidence in favor of multiple bacterial oriCs. Maybe simply applying your solution for the Frequent Words with Mismatches and Reverse Complements Problem will reveal these DnaA boxes. Can you find other bacterial genomes where a single oriC is in doubt and check whether they indeed have multiple oriCs?

![](images/page_58_chart_1.jpg)

<details>
<summary>line</summary>

| position | skew |
| --- | --- |
| 0 | ~100 |
| 50000 | ~350 |
| 100000 | ~250 |
| 150000 | ~1000 |
| 200000 | ~1200 |
| 250000 | ~250 |
| 300000 | ~600 |
| 350000 | ~300 |
| 400000 | ~800 |
| 450000 | ~1250 |
| 500000 | ~1650 |
| 550000 | ~1850 |
| 600000 | ~2950 |
| 650000 | ~3150 |
| 700000 | ~2950 |
</details>

FIGURE 1.15 The skew diagram for Wigglesworthia glossinidia.

![](images/page_58_image_3.jpg)

FIGURE 1.16 (Left) $\mathsf { A n ^ { \prime } i d e a l ^ { \prime \prime } }$ V-shaped skew diagram that achieves minimum skew at $o r { \dot { I } } C ,$ The skew diagram decreases along the reverse half-strand (shown by a thick line) and increases along the forward half-strand (shown by a thin line). We assume that a circular chromosome was cut at $t e r C ,$ resulting in a linear chromosome that starts and ends at terC. (Right) A skew diagram after a reversal that switches segments between the reverse and forward strands and alters the skew diagram. As before, the skew diagram still decreases along the segments of the genome shown by thick lines and increases along the segments shown by thin lines.

## Finding replication origins in archaea

**Archaea** are unicellular organisms so distinct from other life forms that biologists have placed them into their own **domain of life** separate from bacteria and eukaryotes. Al though archaea are visually similar to bacteria, they have some genomic features that are more closely related to eukaryotes. In particular, the replication machinery of archaea is more similar to eukaryotes than bacteria. Yet archaea use a much greater variety of energy sources than eukaryotes, feeding on ammonia, metals, or even hydrogen gas.

Figure 1.17 shows the skew diagram of Sulfolobus solfataricus, a species of archaea growing in acidic volcanic springs in temperatures over $8 0 ^ { \circ } \; \mathsf { C } .$ In its skew diagram, you can see at least three local minima, represented by deep valleys, in addition to many more shallow valleys.

![](images/page_59_chart_4.jpg)

<details>
<summary>line</summary>

| position | skew |
| --- | --- |
| 0 | ~500 |
| 500000 | ~-3000 |
| 1000000 | ~-2000 |
| 1500000 | ~500 |
| 2000000 | ~6000 |
| 2500000 | ~7500 |
| 3000000 | ~2500 |
</details>

FIGURE 1.17 The skew diagram of Sulfolobus solfataricus.

Lundgren et al., 2004 demonstrated experimentally that Sulfolobus solfataricus indeed has three oriCs. Since then, multiple oriCs have been identified in many other archaea. However, no accurate computational approach has been developed to identify multiple oriCs in a newly sequenced archaea genome. For example, the methane-producing archaea Methanococcus jannaschii is considered the workhorse of archaea genomics, but its oriC(s) still remain unidentified! Its skew diagram (shown in Figure 1.18) suggests that it may have multiple oriCs: can you find them?

![](images/page_60_chart_1.jpg)

<details>
<summary>line</summary>

| position | skew |
| --- | --- |
| 0 | ~0 |
| 400000 | ~-3500 |
| 800000 | ~-6500 |
| 1200000 | ~-2500 |
| 1600000 | ~6000 |
</details>

FIGURE 1.18 The skew diagram for Methanococcus jannaschii.

Finding replication origins in yeast

If you think that finding replication origins in bacteria is a complex problem, wait until you analyze replication origins in more complex organisms like yeast or humans, which have hundreds of replication origins. Among various yeast species, the yeast Saccharomyces cerevisiae has the best characterized replication origins. It has approximately 400 different oriCs, many of which may be used during the replication of any single yeast cell.

Having a large number of oriCs results in dozens of replication forks hurtling towards each other from different locations in the genome in ways that are not yet completely understood. However, researchers have discovered that the replication origins of S. cerevisiae share a (somewhat variable) pattern called the **ARS Consensus Sequence** (**ACS**). The ACS is the binding site for the so-called **Origin Recognition Complex**, which initiates the loading of additional proteins required for origin firing. Many ACSs correspond to the following canonical thymine-rich pattern of length 11.

Here, the notation (X/Y) indicates that either nucleotide X or nucleotide Y may appear in that position.

However, various ACSs may differ from this canonical pattern, with lengths varying from 11 to 17 nucleotides. For example, the 11-nucleotide long pattern shown above is often part of a 17-nucleotide pattern:

$$
(\mathrm{T} / \mathrm{A}) (\mathrm{T} / \mathrm{A}) (\mathrm{T} / \mathrm{A}) (\mathrm{T} / \mathrm{A}) \mathbf {T T T A T} (\mathbf {G} / \mathbf {A}) \mathbf {T T T} (\mathbf {T} / \mathbf {A}) (\mathbf {G} / \mathbf {T}) (\mathrm{T} / \mathrm{G}) (\mathrm{T} / \mathrm{C})
$$

Recently, some progress has been made in characterizing the ACS in a few other yeast species. In some species like S. bayanus, the ACS is almost identical to that of S. cerevisiae, while in others such as K. lactis, it is very different. More alarmingly, at least for bioinformaticians, in some yeast species such as S. pombe, the Origin Recognition Complex binds to loosely defined AT-rich regions, which makes it next to impossible to find replication origins based on sequence analysis alone.

Despite recent efforts, finding oriCs in yeast remains an open problem, and no accurate software exists for predicting origins of replication from the sequence of yeast genomes. Can you explore this problem and devise an algorithm to predict replication origins in yeast?

Computing probabilities of patterns in a string

In the main text, we told you that the probability that a random DNA string of length 500 contains a 9-mer appearing three or more times is approximately 1/1300. In **DETOUR: Probabilities of Patterns in a String**, we describe a method to estimate this probability, but it is rather inaccurate. This open problem is aimed at finding better approximations or even deriving exact formulas for probabilities of patterns in strings.

We start by asking a question: what is the probability that a specific k-mer Pattern will appear (at least once) as a substring of a random string of length N? This question proved to be not so simple and was first addressed by Solov’ev, 1966 (see also Sedgewick and Flajolet, 2013).

The first surprise is that different k-mers may have different probabilities of appearing in a random string. For example, the probability that $P a t t e r n = 0 1$ appears in a random binary string of length 4 is 11/16, while the probability that $P a t t e r n = 1 1$ appears in a random binary string of length 4 is $8 / 1 6 .$ . This phenomenon is called the **overlapping words paradox** because different occurrences of Pattern can overlap each other for some patterns $\left(  e.g. , 11 \right)$ but not others $(  e.g. , 01 )$ . See **DETOUR: The Overlapping Words Paradox**.

We are interested in computing the following probabilities for a random N-letter string in an A-letter alphabet:

$\operatorname* { P r } \bigl ( N , A , P a t t e r n , t \bigr )$ , the probability that a string Pattern appears at least t times in a random string;
$\operatorname* { P r } ^ { * } \bigl ( N , A , P a t t e r n , t \bigr )$ , the probability that a string Pattern and its reverse complement Pattern appear at least t total times in a random string.

Note that the above two probabilities are relatively straightforward to compute. Several variants of these questions are open:

$\operatorname* { P r } _ { d } \bigl ( N , A , P a t t e r n , t \bigr )$ , the probability that a string Pattern approximately appears at least t times in a random string (with at most d mismatches);
$\operatorname* { P r } \bigl ( N , A , k , t \bigr )$ , the probability that there exists any k-mer appearing at least t times in a random string;
$\operatorname* { P r } _ { d }   \left( N , A , k , t \right)$ , the probability that there exists any k-mer with at least t approximate occurrences in a random string (with at most d mismatches).

## Charging Stations

## The frequency array

To make **FREQUENTWORDS** faster, we will think about why this algorithm is slow in the first place. It slides a window of length k down Text, identifying a k-mer Pattern of Text at each step. For each such k-mer, it must slide a window down the entire length of Text in order to compute PATTERNCOUNT(Text, Pattern). Instead of doing all this sliding, we aspire to slide a window down Text only once. As we slide this window, we will keep track of the number of times that each k-mer Pattern has already appeared in Text, updating these numbers as we proceed.

To achieve this goal, we will first order all $4 ^ { k }$ k-mers **lexicographically** (i.e., according to how they would appear in the dictionary) and then convert them into the $4 ^ { k }$ different integers between 0 and $4 ^ { k } - 1$ . Given an integer $k ,$ we define the **frequency array** of a string Text as an array of length $4 ^ { k } )$ , where the i-th element of the array holds the number of times that the i-th k-mer (in the lexicographic order) appears in Text (Figure 1.19).

| k-mer | AA | AC | AG | AT | CA | CC | CG | CT | GA | GC | GG | GT | TA | TC | TG | TT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| frequency | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 3 | 1 | 0 | 0 | 1 | 0 |

FIGURE 1.19 The lexicographic order of DNA 2-mers (top), along with the index of each 2-mer in this order (middle), and the frequency array for AAGCAAAGGTGGG (bottom). For example, the frequency array at index 10 is equal to 3 because GG, the tenth DNA 2-mer according to lexicographic order, occurs three times in AAGCAAAGGTGGG.

To compute the frequency array, we need to determine how to transform a k-mer Pattern into an integer using a function PATTERNTONUMBER(Pattern). We also should know how to reverse this process, transforming an integer between 0 and $4 ^ { k } - 1$ into a k-mer using a function NUMBERTOPATTERN(index, k). Figure 1.19 illustrates that PATTERNTONUMBER(GT) = 11 and NUMBERTOPATTERN(11, 2) = GT.

## EXERCISE BREAK: Compute the following:

1. PATTERNTONUMBER(ATGCAA)
2. NUMBERTOPATTERN(5437, 7)
3. NUMBERTOPATTERN(5437, 8)

![](images/page_63_image_13.jpg)