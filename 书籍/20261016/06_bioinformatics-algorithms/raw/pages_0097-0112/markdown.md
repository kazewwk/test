15-mers look similar to the correct motif **AAAAAAAAGGGGGGG**, they are not so similar when compared to each other, having eight mismatches:

![](images/page_96_image_2.jpg)

Since these two implanted patterns are so different, we should be concerned whether we will be able to find them by searching for the most similar k-mers among pairs of strings in Dna.

In the rest of the chapter, we will benchmark our motif finding algorithms by using a particularly challenging instance of the Implanted Motif Problem. The **Subtle Motif Problem** refers to implanting a 15-mer with four random mutations in ten randomly generated 600 nucleotide-long strings (the typical length of many upstream regulatory regions). The instance of the Subtle Motif Problem that we will use has the implanted 15-mer **AAAAAAAAGGGGGGG**.

It turns out that thousands of pairs of randomly occurring 15-mers in our dataset for the Subtle Motif Problem are fewer than 8 nucleotides apart from each other, preventing us from identifying the true implanted motifs by pairwise comparisons.

## Scoring Motifs

From motifs to profile matrices and consensus strings

Although the Implanted Motif Problem offers a useful abstraction of the biological problem of motif finding, it has some limitations. For example, when Steve Kay used a DNA array to infer the set of circadian genes in plants, he did not expect that all genes in the resulting set would have the evening element (or its variants) in their upstream regions. Similarly, biologists do not expect that all genes with an elevated expression level in infected flies must be regulated by NF-kB. DNA array experiments are inherently noisy, and some genes identified by these experiments have nothing to do with the circadian clock in plants or immunity genes in flies. For such noisy datasets, any algorithm for the Implanted Motif Problem would fail, because as long as a single sequence does not contain the transcription factor binding site, a (k, d)-motif does not exist!

A more appropriate problem formulation would score individual instances of motifs depending on how similar they are to an “ideal” motif (i.e., a transcription factor binding site that binds the best to the transcription factor). However, since the ideal motif is unknown, we attempt to select a k-mer from each string and score these k-mers depending on how similar they are to each other.

To define scoring, consider t DNA strings, each of length n, and select a k-mer from each string to form a collection Motifs, which we represent as a t ⇥ k **motif matrix**. In Figure 2.2, which shows the motif matrix for the NF-kB binding sites from Figure 2.1, we indicate the most frequent nucleotide in each column of the motif matrix by upper case letters. If there are multiple most popular nucleotides in a column, then we arbitrarily select one of them to break the tie. Note that positions 2 and 3 are the most conserved (nucleotide G is completely conserved in these positions), whereas position 10 is the least conserved.

By varying the choice of k-mers in each string, we can construct a large number of different motif matrices from a given sample of DNA strings. Our goal is to select k-mers resulting in the most “conserved” motif matrix, meaning the matrix with the most upper case letters (and thus the fewest number of lower case letters). Leaving aside the question of how we select such k-mers, we will first focus on how to score the resulting motif matrices, defining SCORE(Motifs) as the number of unpopular (lower case) letters in the motif matrix Motifs. Our goal is to find a collection of k-mers that minimizes this score.

**EXERCISE BREAK:** The minimum possible value of SCORE(Motifs) is 0 (if all rows in the t ⇥ k matrix Motifs are the same). What is the maximum possible value of SCORE(Motifs) in terms of t and k?

![](images/page_97_image_5.jpg)

We can construct the 4 ⇥ k **count matrix** COUNT(Motifs) counting the number of oc currences of each nucleotide in each column of the motif matrix; the (i, j)-th element of COUNT(Motifs) stores the number of times that nucleotide i appears in column j of Motifs. We will further divide all of the elements in the count matrix by t, the number of rows in Motifs. This results in a **profile matrix** P = PROFILE(Motifs) for which $P _ { i , j }$ is the frequency of the i-th nucleotide in the j-th column of the motif matrix. Note that the elements of any column of the profile matrix sum to 1.

Finally, we form a **consensus string**, denoted CONSENSUS(Motifs), from the most popular nucleotides in each column of the motif matrix (ties are broken arbitrarily). If we select Motifs correctly from the collection of upstream regions, then CONSENSUS(Motifs) provides an ideal candidate regulatory motif for these regions. For example, the consensus string for the NF-kB binding sites in Figure 2.2 is **TCGGGGATTTCC**.

![](images/page_98_chart_1.jpg)

<details>
<summary>heatmap</summary>

| Category | Row 1 | Row 2 | Row 3 | Row 4 | Row 5 | Row 6 | Row 7 | Row 8 | Row 9 | Row 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Motifs | T | C | G | G | G | G | g | T | T | t |
| Motifs | c | C | G | G | t | G | A | c | T | a |
| Motifs | a | C | G | G | G | G | A | T | T | t |
| Motifs | T | t | G | G | G | G | A | c | T | t |
| Motifs | a | a | G | G | G | G | A | c | T | C |
| Motifs | T | t | G | G | G | G | A | c | T | C |
| Motifs | T | C | G | G | G | G | A | T | c | a |
| Motifs | T | C | G | G | G | G | A | T | c | C |
| Motifs | T | a | G | G | G | G | A | a | c | a |
| Motifs | T | C | G | G | G | t | A | T | a | C |
</details>

FIGURE 2.2 From motif matrix to count matrix to profile matrix to consensus string to motif logo. The NF-kB binding sites form a $1 0 \times 1 2$ motif matrix, with the most frequent nucleotide in each column shown in upper case letters and all other nucleotides shown in lower case letters. SCORE(Motifs) counts the total number of unpopular (lower case) symbols in the motif matrix. The motif matrix results in $\mathsf { a }   4 \times 1 2$ count matrix holding the nucleotide counts in every column of the motif matrix; a profile matrix holding the frequencies of nucleotides in every column of the motif matrix; and a consensus string formed by the most frequent nucleotide in each column of the count matrix. Finally, the motif logo is a common way to visualize the conservation of various positions within a motif. The total height of the letters depicts the information content of the position.

Towards a more adequate motif scoring function

Consider the second column (containing 6 C, 2 A, and 2 T) and the final column (containing 6 C and 4 T) in the motif matrix from Figure 2.2. Both of these columns contribute 4 to SCORE(Motifs).

**STOP and Think:** Does scoring these two columns equally make sense biologically?

For many biological motifs, certain positions feature two nucleotides with roughly the same ability to bind to a transcription factor. For example, the sixteen nucleotide-long CSRE transcription factor binding site in the yeast S. cerevisiae consists of five strongly conserved positions in addition to eleven weakly conserved positions, each of which features two nucleotides with similar frequencies (Figure 2.3).

![](images/page_99_image_5.jpg)

<details>
<summary>text_image</summary>

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
C G/C G/T T/A C/T G/C C/G A T G/T C/G A T C/T C/T G/T
</details>

FIGURE 2.3 The CSRE transcription factor binding site in S. cerevisiae is 16 nucleotides long, but only five of these positions (1, 8, 9, 12, 13) are strongly conserved. The remaining 11 positions can take one of two different nucleotides.

Following this example, a more appropriate representation of the consensus string **TCGGGGATTTCC** for the NF-kB binding sites should include viable alternatives to the most popular nucleotides in each column (see Figure 2.4). In this sense, the last column $( 6 \mathrm { ~ C , ~ } 4 \mathrm { ~ T ) }$ in the motif matrix from Figure 2.2 is “more conserved” than the second column $( 6 \; \mathbb { C } , 2 \; \mathbb { A } , 2 \; \mathbb { T } )$ and should receive a lower score.

![](images/page_99_image_8.jpg)

<details>
<summary>text_image</summary>

1 2 3 4 5 6 7 8 9 10 11 12
T C G G G G A T/C T T C C/T
</details>

FIGURE 2.4 Taking nucleotides in each column of the NF-kB binding site motif matrix from Figure 2.2 with frequency at least 0.4 yields a representation of the NF-kB binding sites with ten strongly conserved positions and two weakly conserved positions (8 and 12).

![](images/page_99_image_10.jpg)

Entropy and the motif logo

Every column of PROFILE(Motifs) corresponds to a **probability distribution**, or a collection of nonnegative numbers that sum to 1. For example, the second column in Figure 2.2 corresponds to the probabilities 0.2, 0.6, 0.0, and 0.2 for $\mathbb { A } , \mathbb { C } , \mathbb { G } ,$ and $\mathbb { T } ,$ respectively.

**Entropy** is a measure of the uncertainty of a probability distribution $( p _ { 1 } , \cdots , p _ { N } )$ and is defined as

$$
H (p _ {1}, \dots , p _ {N}) = - \sum_ {i = 1} ^ {N} p _ {i} \cdot \log_ {2} (p _ {i}).
$$

For example, the entropy of the probability distribution (0.2, 0.6, 0.0, 0.2) corresponding to the second column of the profile matrix in Figure 2.2 is

$$
- (0. 2 \log_ {2} 0. 2 + 0. 6 \log_ {2} 0. 6 + 0. 0 \log_ {2} 0. 0 + 0. 2 \log_ {2} 0. 2) \approx 1. 3 7 1,
$$

whereas the entropy of the more conserved final column (0.0, 0.6, 0.0, 0.4) is

$$
- (0. 0 \log_ {2} 0. 0 + 0. 6 \log_ {2} 0. 6 + 0. 0 \log_ {2} 0. 0 + 0. 4 \log_ {2} 0. 4) \approx 0. 9 7 1,
$$

and the entropy of the very conserved 5th column (0.0, 0.0, 0.9, 0.1) is

$$
- (0. 0 \log_ {2} 0. 0 + 0. 0 \log_ {2} 0. 0 + 0. 9 \log_ {2} 0. 9 + 0. 1 \log_ {2} 0. 1) \approx 0. 4 6 7.
$$

Note that technically, $\log _ { 2 } 0$ is not defined, but in the computation of entropy, we assume that $0 \cdot \log _ { 2 } 0$ is equal to 0.

![](images/page_100_image_12.jpg)

**STOP and Think:** What are the maximum and minimum possible values for the entropy of a probability distribution containing four values?

The entropy of the completely conserved third column of the profile matrix in Figure 2.2 is 0, which is the minimum possible entropy. On the other hand, a column with equally-likely nucleotides (all probabilities equal to $1 / 4 )$ has maximum possible entropy $- 4 \cdot 1 / 4 \cdot \log _ { 2 } \left( 1 / 4 \right)   =   2$ . In general, the more conserved the column, the smaller its entropy. Thus, entropy offers an improved method of scoring motif matrices: the entropy of a motif matrix is defined as the sum of the entropies of its columns. In this book, we will continue to use SCORE(Motifs) for simplicity, but the entropy score is used more often in practice.

**EXERCISE BREAK:** Compute the entropy of the NF-kB motif matrix from Figure 2.2.

![](images/page_101_image_2.jpg)

Another application of entropy is the **motif logo**, a diagram for visualizing motif conservation that consists of a stack of letters at each position (see the bottom of Figure 2.2). The relative sizes of letters indicate their frequency in the column. The total height of the letters in each column is based on the **information content** of the column, which is defined as $2 - H { \bigl ( } p _ { 1 } , \cdots , p _ { N } { \bigr ) }$ . The lower the entropy, the higher the information content, meaning that tall columns in the motif logo are highly conserved.

## From Motif Finding to Finding a Median String

The Motif Finding Problem

Now that we have a good grasp of scoring a collection of k-mers, we are ready to formulate the Motif Finding Problem.

## Motif Finding Problem:

Given a collection of strings, find a set of k-mers, one from each string, that minimizes the score of the resulting motif.

**Input**: A collection of strings Dna and an integer k.

**Output**: A collection Motifs of k-mers, one from each string in Dna, minimizing SCORE(Motifs) among all possible choices of k-mers.

A brute force algorithm for the Motif Finding Problem, **BRUTEFORCEMOTIFSEARCH**, considers every possible choice of k-mers Motifs from Dna (one k-mer from each string of n nucleotides) and returns the collection Motifs having minimum score. Because there are $n - k + 1$ choices of k-mers in each of t sequences, there are $( n   -   k   +   1 ) ^ { t }$ different ways to form Motifs. For each choice of Motifs, the algorithm calculates SCORE(Motifs), which requires k · t steps. Thus, assuming that k is much smaller than n, the overall running time of the algorithm is $\mathcal { O } \big ( n ^ { t } \cdot k \cdot t \big )$ . We need to come up with a faster algorithm!

Reformulating the Motif Finding Problem

Because **BRUTEFORCEMOTIFSEARCH** is inefficient, we will think about motif finding in a different way. Instead of exploring all Motifs in Dna and deriving the consensus

string from Motifs afterwards,

$$
\text {Motifs} \rightarrow \text {CONSENSUS} (\text {Motifs}),
$$

we will explore all potential k-mer consensus strings first and then find the best possible collection Motifs for each consensus string,

$$
\text {CONSENSUS} (\text {Motifs}) \rightarrow \text {Motifs}.
$$

To reformulate the Motif Finding Problem, we need to devise an alternative way of computing SCORE(Motifs). Until now, we have computed SCORE(Motifs), the number of lower case letters in the motif matrix, column-by-column. For example, in Figure 2.2, we computed SCORE(Motifs) for the NF-kB motif matrix as

$$
3 + 4 + 0 + 0 + 1 + 1 + 1 + 5 + 2 + 3 + 6 + 4 = 3 0.
$$

Figure 2.5 illustrates that SCORE(Motifs) can just as easily be computed row-by-row as

$$
3 + 4 + 2 + 4 + 3 + 2 + 3 + 2 + 4 + 3 = 3 0.
$$

Note that each element in the latter sum represents the number of mismatches between the consensus string **TCGGGGATTTCC** and a motif in the corresponding row of the motif matrix, $\mathbf { i . e . } ,$ the Hamming distance between these strings. For the first row of the motif matrix in Figure 2.5, d(**TCGGGGATTTCC**, **TCGGGG**g**TTT**tt) = 3.

Given a collection of k-mers $\mathit { M o t i f s } = \left\{ M o t i f _ { 1 } , . . . , M o t i f _ { t } \right\}$ and a k-mer Pattern, we now define d(Pattern, Motifs) as the sum of Hamming distances between Pattern and each $M o t i f _ { i } ,$

$$
d (\text {Pattern}, \text {Motifs}) = \sum_ {i = 1} ^ {t} \text {HAMMINGDISTANCE} (\text {Pattern}, \text {Motif} _ {i}).
$$

Because SCORE(Motifs) corresponds to counting the lower case elements of Motifs column-by-column and $d \big ( \mathsf { C O N S E N S U S } \big ( M o t i f s \big ) , M o t i f s \big )$ corresponds to counting these elements row-by-row, we obtain that

$$
\text {SCORE} (M o t i f s) = d (\text {CONSENSUS} (M o t i f s), M o t i f s).
$$

![](images/page_103_image_1.jpg)

<details>
<summary>flowchart</summary>

This diagram illustrates a hierarchical motif structure and their corresponding score calculation, showing how individual motifs are summed to produce consensus scores.
</details>

FIGURE 2.5 The motif and score matrices in addition to the consensus string for the NF-kB binding sites, reproduced from Figure 2.2. Rather than count the non-consensus elements (i.e., lower case nucleotides) column-by-column, we can count them row-by-row, as highlighted on the right of the motifs matrix. Each value at the end of a row corresponds to the Hamming distance between that row and the consensus string.

This equation gives us an idea. Instead of searching for a collection of k-mers Motifs minimizing SCORE(Motifs), let’s instead search for a potential consensus string Pattern minimizing d(Pattern, Motifs) among all possible k-mers Pattern and all possible choices of k-mers Motifs in Dna. This problem is equivalent to the Motif Finding Problem.

## Equivalent Motif Finding Problem:

Given a collection of strings, find a pattern and a collection of k-mers (one from each string) that minimizes the distance between all possible patterns and all possible collections of k-mers.

**Input**: A collection of strings Dna and an integer k.

**Output**: A k-mer Pattern and a collection of k-mers Motifs, one from each string in Dna, minimizing d(Pattern, Motifs) among all possible choices of Pattern and Motifs.

## The Median String Problem

But wait a second — have we not just made our task more difficult? Instead of having to search for all $M o t i f _ { S } ,$ , we now have to search all Motifs as well as all k-mers Pattern. The key observation for solving the Equivalent Motif Finding Problem is that, given Pattern, we don’t need to explore all possible collections Motifs in order to minimize $d { \big ( } P a t t e r n , M o t i f s { \big ) }$

To explain how this can be done, we define MOTIFS(Pattern, Dna) as a collection of k-mers that minimizes d(Pattern, Motifs) for a given Pattern and all possible sets of k-mers Motifs in Dna. For example, for the strings Dna shown below, the five colored 3-mers represent MOTIFS(**AAA**, Dna).

```txt
ttaccttAAC
gATAtctgtc
Dna ACGgcgttcg
ccctAAAagag
cgtcAGAggt
```

![](images/page_104_image_5.jpg)

**STOP and Think:** Given a collection of strings Dna and a k-mer Pattern, design a fast algorithm for generating MOTIFS(Pattern, Dna).

The reason why we don’t need to consider all possible collections Motifs in Dna = $\left\{ D n a _ { 1 } , . . . , D n a _ { t } \right\}$ is that we can generate the k-mers in MOTIFS(Pattern, Dna) one at a time; that is, we can select a k-mer in $D n a _ { i }$ independently of selecting k-mers in all other strings in Dna. Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to denote the minimum Hamming distance between Pattern and any k-mer in Text,

$$
d (\text {Pattern}, \text {Text}) = \min _ {\text {all} k \text {-mers Pattern' in Text}} \text {HAMMINGDISTANCE} (\text {Pattern}, \text {Pattern'}).
$$

For example,

$$
d (\text {GATTCTCA, gcaaaGACGCTGAccaa}) = 3.
$$

A k-mer in Text that achieves the minimum Hamming distance with Pattern is denoted MOTIF(Pattern, Text). For the above example,

$$
\text {Motif} (\text {GATTCTCA,gcaaaGACGCTGAccaa}) = \text {GACGCTGA}.
$$

We note that the notation MOTIF(Pattern, Text) is ambiguous because there may be multiple k-mers in Text that achieve the minimum Hamming distance with Pattern. For example, MOTIF(**AAG**, gc**AAT**cct**CAG**c) could be either **AAT** or **CAG**. However, this ambiguity does not affect the following analysis.

Given a k-mer Pattern and a set of strings $D n a = \left\{ D n a _ { 1 } , . . . , D n a _ { t } \right\}$ , we define $d { \big ( } P a t t e r n , D n a { \big ) }$ as the sum of distances between Pattern and all strings in Dna,

$$
d (P a t t e r n, D n a) = \sum_ {i = 1} ^ {t} d (P a t t e r n, D n a _ {i}).
$$

For example, for the strings Dna shown below, $d(\mathbb{A}\mathbb{A}\mathbb{A},Dna)=1+1+2+0+1=5$

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
        ttaccttAAC 1
        gATAtctgtc 1
Dna     ACGgcgttcg 2
        ccctAAAgag 0
        cgtcAGAggt 1
</div>

Our goal is to find a k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern, the same task that the Equivalent Motif Finding Problem is trying to achieve. We call such a k-mer a **median string** for Dna.

## Median String Problem:

Find a median string.

**Input**: A collection of strings Dna and an integer k.

**Output**: A k-mer Pattern minimizing d(Pattern, Dna) among all k-mers Pattern.

Notice that finding a median string requires solving a double minimization problem. We must find a k-mer Pattern that minimizes $d { \big ( } P a t t e r n , D n a { \big ) }$ , where this function is itself computed by taking a minimum over all choices of k-mers from each string in Dna. The pseudocode for a brute-force algorithm, **MEDIANSTRING**, is given below.

![](images/page_105_image_12.jpg)

![](images/page_106_image_1.jpg)

![](images/page_106_image_2.jpg)

```python
MEDIANSTRING(Dna, k)
    distance ← ∞
    for each k-mer Pattern from AA . . .AA to TT . . .TT
        if distance > d(Pattern, Dna)
            distance ← d(Pattern, Dna)
            Median ← Pattern
    return Median
```

**CHARGING STATION (Solving the Median String Problem):** Although this pseudocode is short, it is not without potential pitfalls. Check out this Charging Station if you fall into one of them.

**STOP and Think:** Instead of making a time-consuming search through all possible k-mers in **MEDIANSTRING**, can you only search through all k-mers that appear in Dna?

Why have we reformulated the Motif Finding Problem?

To see why we reformulated the Motif Finding Problem as the equivalent Median String Problem, consider the runtimes of **MEDIANSTRING** and **BRUTEFORCEMOTIFS**. The former algorithm computes d(Pattern, Dna) for each of the $4 ^ { k } \; k \mathrm { - m e r s }$ Pattern. Each computation of $d { \big ( } P a t t e r n , D n a { \big ) }$ requires a single pass over each string in Dna, which requires approximately k · n · t operations for t strings of length n in Dna. Therefore, **MEDIANSTRING** has a running time of $\mathcal { O } \Big ( 4 ^ { k } \cdot n \cdot k \cdot t \Big )$ , which in practice compares favorably with the $\mathcal { O } \big ( n ^ { t } \cdot k \cdot t \big )$ running time of **BRUTEFORCEMOTIFSEARCH** because the length of a motif (k) typically does not exceed 20 nucleotides, whereas t is measured in the thousands.

The Median String Problem teaches an important lesson, which is that sometimes rethinking how a problem is formulated can lead to dramatic improvements in the runtime required to solve it. In this case, our simple observation that SCORE(Motifs) could just as easily be computed row-by-row as column-by-column produced the faster **MEDIANSTRING** algorithm.

Of course, the ultimate test of a bioinformatics algorithm is how it performs in practice. Unfortunately, since **MEDIANSTRING** has to consider $4 ^ { k }$ k-mers, it becomes too slow for the Subtle Motif Problem, for which k = 15. We will run **MEDIANSTRING** with k = 13 in the hope that it will capture a substring of the correct 15-mer motif. The algorithm still requires half a day to run on our computer and returns the median string **AAAAAtAGaGGGG** (with distance 29). This 13-mer is not a substring of the implanted pattern **AAAAAAAAGGGGGGG**, but it does come close.

**STOP and Think:** How can a slightly incorrect median string of length 13 help us find the correct median string of length 15?

We have thus far assumed that the value of k is known in advance, which is not the case in practice. As a result, we are forced to run our motif finding algorithms for different values of k and then try to deduce the correct motif length. Since some regulatory motifs are rather long — later in the chapter, we will search for a biologically important motif of length 20 — **MEDIANSTRING** may be too slow to find them.

## Greedy Motif Search

Using the profile matrix to roll dice

Many algorithms are iterative procedures that must choose among many alternatives at each iteration. Some of these alternatives may lead to correct solutions, whereas others may not. **Greedy algorithms** select the “most attractive” alternative at each iteration. For example, a greedy algorithm in chess might attempt to capture an opponent’s most valuable piece at every move. Yet anyone who has played chess knows that this strategy of looking only one move ahead will likely produce disastrous results. In general, most greedy algorithms typically fail to find an exact solution of the problem; instead, they are often fast **heuristics** that trade accuracy for speed in order to find an approximate solution. Nevertheless, for many biological problems that we will study in this book, greedy algorithms will prove quite useful.

In this section, we will explore a greedy approach to motif finding. Again, let Motifs be a collection of k-mers taken from t strings Dna. Recall from our discussion of entropy that we can view each column of PROFILE(Motifs) as a four-sided biased die. Thus, a profile matrix with k columns can be viewed as a collection of k dice, which we will roll to randomly generate a k-mer. For example, if the first column of the profile matrix is (**0.2**, **0.1**, **0.0**, **0.7**), then we generate A as the first nucleotide with probability **0.2**, C with probability **0.1**, G with probability **0.0**, and T with probability **0.7**.

In Figure 2.6, we reproduce the profile matrix for the NF-kB binding sites from Figure 2.2, where the lone colored entry in the i-th column corresponds to the i-th nucleotide in **ACGGGGATTACC**. The probability Pr(**ACGGGGATTACC**|Profile) that Profile generates **ACGGGGATTACC** is computed by simply multiplying the highlighted entries in the profile matrix.

![](images/page_107_image_9.jpg)

$$
\begin{array}{l l} & \text {A: .2 .2 .0 .0 .0 .0 .9 .1 .1 .1 .3 .0} \\ \text {Profile} & \text {C: .1 .6 .0 .0 .0 .0 .0 .0 .4 .1 .2 .4 .6} \\ & \text {G: .0 .0 1 1 .9 .9 .1 .0 .0 .0 .0 .0 .0} \\ & \text {T: .7 .2 .0 .0 .1 .1 .0 .5 .8 .7 .3 .4} \end{array}
$$

$$
\Pr (\text {ACGGGGATTACC} | \text {Profile}) = . 2 \cdot . 6 \cdot 1 \cdot 1 \cdot . 9 \cdot . 9 \cdot . 9 \cdot . 5 \cdot . 8 \cdot . 1 \cdot . 4 \cdot . 6 = 0. 0 0 0 8 3 9 8 0 8
$$

**FIGURE 2.6** We can generate a random string based on a profile matrix by selecting the i-th nucleotide in the string with the probability corresponding to that nucleotide in the i-th column of the profile matrix. The probability that a profile matrix will produce a given string is given by the product of individual nucleotide probabilities.

A k-mer tends to have a higher probability when it is more similar to the consensus string of a profile. For example, for the NF-kB profile matrix shown in Figure 2.6 and its consensus string **TCGGGGATTTCC**,

$$
\begin{array}{l} \Pr (\mathbf {T C G G G A T T T C C} | \text {Profile}) = 0. 7 \cdot 0. 6 \cdot 1. 0 \cdot 1. 0 \cdot 0. 9 \cdot 0. 9 \cdot 0. 9 \cdot 0. 5 \cdot 0. 8 \cdot 0. 7 \cdot 0. 4 \cdot 0. 6 \\ = 0. 0 2 0 5 7 5 3, \\ \end{array}
$$

which is larger than the value of Pr(**ACGGGGATTACC**|Profile) = 0.000839808 that we computed in Figure 2.6.

![](images/page_108_image_8.jpg)

**EXERCISE BREAK:** Compute Pr(**TCGTGGATTTCC**|Profile), where Profile is the matrix shown in Figure 2.6.

Given a profile matrix Profile, we can evaluate the probability of every k-mer in a string Text and find a **Profile-most probable** k-mer in Text, i.e., a k-mer that was most likely to have been generated by Profile among all k-mers in Text. For the NF-kB profile matrix, **ACGGGGATTACC** is the Profile-most probable 12-mer in ggt**ACGGGGATTACC**t. Indeed, every other 12-mer in this string has probability 0. In general, if there are multiple Profile-most probable k-mers in Text, then we select the first such k-mer occurring in Text.

## Profile-most Probable k-mer Problem:

Find a Profile-most probable k-mer in a string.

**Input**: A string Text, an integer $k ,$ and a $4 \times k$ matrix Profile.

**Output**: A Profile-most probable k-mer in $T e x t .$

Our proposed greedy motif search algorithm, **GREEDYMOTIFSEARCH**, tries each of the k-mers in $D n a _ { 1 }$ as the first motif. For a given choice of k-mer $M o t i f _ { 1 }$ in $D n a _ { 1 }$ , it then builds a profile matrix Profile for this lone k-mer, and sets $M o t i f _ { 2 }$ equal to the Profile-most probable k-mer in $D n a _ { 2 }$ . It then iterates by updating Profile as the profile matrix formed from $M o t i f _ { 1 }$ and $M o t i f _ { 2 } ,$ and sets $M o t i f _ { 2 }$ equal to the Profile-most probable k-mer in $D n a _ { 3 }$ . In general, after finding $i - 1$ k-mers Motifs in the first $i - 1$ strings of Dna, **GREEDYMOTIFSEARCH** constructs Profile(Motifs) and selects the Profile-most probable k-mer from $D n a _ { i }$ based on this profile matrix. After obtaining a k-mer from each string to generate a collection Motifs, **GREEDYMOTIFSEARCH** tests to see whether Motifs outscores the current best scoring collection of motifs and then moves $M o t i f _ { 1 }$ one symbol over in $D n a _ { 1 . }$ , beginning the entire process of generating Motifs again.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
GREEDYMOTIFSEARCH(Dna, k, t)
    BestMotifs ← motif matrix formed by first k-mers in each string from Dna
    for each k-mer Motif in the first string from Dna
        Motif₁ ← Motif
        for i = 2 to t
            form Profile from motifs Motif₁, ..., Motifᵢ₋₁
            Motifᵢ ← Profile-most probable k-mer in the i-th string in Dna
        Motifs ← (Motif₁, ..., Motifₜ)
        if SCORE(Motifs) &lt; SCORE(BestMotifs)
            BestMotifs ← Motifs
    return BestMotifs
</div>

If you are not satisfied with the performance of **GREEDYMOTIFSEARCH** — even if you implemented it correctly — then wait until we discuss this algorithm in the next section.

## Analyzing greedy motif finding

In contrast to **MEDIANSTRING**, **GREEDYMOTIFSEARCH** is fast and can be run with $k   =   1 5$ to solve the Subtle Motif Problem (recall that we settled for $k   =   1 3$ in the case of **MEDIANSTRING**). However, it trades speed for accuracy and returns the 15- mer **gtAAAtAgaGatGtG** (total distance: 58), which is very different from the true implanted motif **AAAAAAAAGGGGGGG**.

![](images/page_109_image_10.jpg)

![](images/page_109_image_11.jpg)

![](images/page_110_image_1.jpg)

**STOP and Think:** Why does **GREEDYMOTIFSEARCH** perform so poorly?

At first glance, **GREEDYMOTIFSEARCH** may seem like a reasonable algorithm, but it is not! Let’s see whether **GREEDYMOTIFSEARCH** will find the (4, 1)-motif **ACGT** implanted in the following strings Dna:

```txt
ttACCTtaac
gATGTctgtc
acgGCGTtag
ccctaACGAg
cgtcagAGGT
```

We will assume that the algorithm has already correctly chosen the implanted 4-mer **ACCT** from the first string in Dna and constructed the corresponding Profile:

```yaml
A: 1 0 0 0
C: 0 1 1 0
G: 0 0 0 0
T: 0 0 0 1
```

The algorithm is now ready to search for a Profile-most probable 4-mer in the second sequence. The issue, however, is that there are so many zeros in the profile matrix that the probability of every 4-mer but **ACCT** is zero! Thus, unless **ACCT** is present in every string in Dna, there is little chance that **GREEDYMOTIFSEARCH** will find the implanted motif. Zeroes in the profile matrix are not just a minor annoyance but rather a persistent problem that we must address.

## Motif Finding Meets Oliver Cromwell

What is the probability that the sun will not rise tomorrow?

In 1650, after the Scots proclaimed Charles II as king during the English Civil War, Oliver Cromwell made a famous appeal to the Church of Scotland. Urging them to see the error of their royal alliance, he pleaded,

I beseech you, in the bowels of Christ, think it possible that you may be mistaken.

The Scots rejected the appeal, and Cromwell invaded Scotland in response. His quotation later inspired the statistical maxim called **Cromwell’s rule**, which states that we should not use probabilities of 0 or 1 unless we are talking about logical statements that can only be true or false. In other words, we should allow a small probability for extremely unlikely events, such as “this book was written by aliens” or “the sun will not rise tomorrow”. We cannot speak to the likelihood of the former event, but in the 18th Century, the French mathematician Pierre-Simon Laplace actually estimated the probability that the sun will not rise tomorrow (1/1826251), given that it has risen every day for the past 5000 years. Although this estimate was ridiculed by his contemporaries, Laplace’s approach to this question now plays an important role in statistics.

In any observed data set, there is the possibility, especially with low-probability events or small data sets, that an event with nonzero probability does not occur. Its observed frequency is therefore zero; however, setting the empirical probability of the event equal to zero represents an inaccurate oversimplification that may cause problems. By artificially adjusting the probability of rare events, these problems can be mitigated.

## Laplace’s Rule of Succession

Cromwell’s rule is relevant to the calculation of the probability of a string based on a profile matrix. For example, consider the following Profile:

$$
\begin{array}{l l} \text {Profile} & \mathbf {A}: \quad . 2 \quad . 2 \quad . 0 \quad . 0 \quad . 0 \quad . 0 \quad . 9 \quad . 1 \quad . 1 \quad . 1 \quad . 3 \quad . 0 \\ & \mathbf {C}: \quad . 1 \quad . 6 \quad . 0 \quad . 0 \quad . 0 \quad . 0 \quad . 0 \quad . 4 \quad . 1 \quad . 2 \quad . 4 \quad . 6 \\ & \mathbf {G}: \quad . 0 \quad . 0 \quad \mathbf {1} \quad 1 \quad . \mathbf {9} \quad . \mathbf {9} \quad . 1 \quad . 0 \quad . 0 \quad . 0 \quad . 0 \quad . 0 \\ & \mathbf {T}: \quad . 7 \quad . 2 \quad . 0 \quad . \mathbf {0} \quad . 1 \quad . 1 \quad . 0 \quad . 5 \quad . 8 \quad . 7 \quad . 3 \quad . 4 \\ | P r o f i l e) & = \quad . 7 \cdot . 6 \cdot \mathbf {1} \cdot . \mathbf {0} \cdot . \mathbf {9} \cdot . \mathbf {9} \cdot . 5 \cdot . 8 \cdot . 7 \cdot . 4 \cdot . 6 = 0 \end{array}
$$

The fourth symbol of **TCGTGGATTTCC** causes Pr(**TCGTGGATTTCC**|Profile) to equal zero. As a result, the entire string is assigned a zero probability, even though **TCGTGGATTTCC** differs from the consensus string at only one position. For that matter, **TCGTGGATTTCC** has the same low probability as **AAATCTTGGAA**, which is very different from the consensus string.

In order to improve this unfair scoring, bioinformaticians often substitute zeroes with small numbers called **pseudocounts**. The simplest approach to introducing pseudocounts, called **Laplace’s Rule of Succession**, is similar to the principle that Laplace