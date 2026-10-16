![](images/page_224_image_1.jpg)

![](images/page_224_image_2.jpg)

```python
LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N)
    Leaderboard ← set containing only the empty peptide
    LeaderPeptide ← empty peptide
    while Leaderboard is non-empty
        Leaderboard ← EXPAND(Leaderboard)
        for each Peptide in Leaderboard
            if MASS(Peptide) = PARENTMASS(Spectrum)
                if SCORE(Peptide, Spectrum) > SCORE(LeaderPeptide, Spectrum)
                    LeaderPeptide ← Peptide
            else if MASS(Peptide) > PARENTMASS(Spectrum)
                remove Peptide from Leaderboard
        Leaderboard ← TRIM(Leaderboard, Spectrum, N)
    output LeaderPeptide
```

**CHARGING STATION (Trimming the Peptide Leaderboard):** The tricky aspect of implementing **LEADERBOARDCYCLOPEPTIDESEQUENCING** is making sure that the TRIM function is implemented correctly. Check out this Charging Station for some help with trimming Leaderboard.

We point out that because a linear peptide giving rise to the highest-scoring cyclic peptide may be trimmed early on, **LEADERBOARDCYCLOPEPTIDESEQUENCING** is a heuristic, not guaranteed to correctly solve the Cyclopeptide Sequencing Problem. When we develop a heuristic, we must ask: how accurate is it? Consider the simulated spectrum $S p e c t r u m _ { 1 0 }$ of Tyrocidine B1 shown in Figure 4.11 (top), with approximately 10% **missing**/**false** masses. Applying **LEADERBOARDCYCLOPEPTIDESEQUENCING** to this spectrum (with $N = 1 0 0 0 )$ results in the correct cyclic peptide VKLFPWFNQY, which has a score of 86.

So far, **LEADERBOARDCYCLOPEPTIDESEQUENCING** has worked well, but as the number of errors increases, so does the likelihood that this algorithm will return an incorrect peptide. Let’s see how this algorithm performs on a noisier simulated spectrum; in Figure 4.11 (bottom), we show $S p e c t r u m _ { 2 5 }$ for Tyrocidine B1, which has 25% **missing**/**false** masses.

When run on $S p e c t r u m _ { 2 5 } ,$ , **LEADERBOARDCYCLOPEPTIDESEQUENCING** (with $N =$ 1000) identifies VKLFP**AD**FNQY (score: 83) as a highest-scoring cyclic peptide instead of the correct peptide VKLFPWFNQY (score: 82). These two peptides are similar, owing to the fact that the combined mass of A (71) and D (115) is equal to the mass of W (186).

| 0 | 97 | 99 | 113 | 114 | 128 | 128 | 147 | 147 | 163 | 186 | 227 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 241 | 242 | 244 | 260 | 261 | 262 | 283 | 291 | 333 | 340 | 357 | 385 |
| 388 | 389 | 390 | 390 | 405 | 430 | 430 | 447 | 485 | 487 | 503 | 504 |
| 518 | 543 | 544 | 552 | 575 | 577 | 584 | 631 | 632 | 650 | 651 | 671 |
| 672 | 690 | 691 | 738 | 745 | 747 | 770 | 778 | 779 | 804 | 818 | 819 |
| 820 | 835 | 837 | 875 | 892 | 892 | 917 | 932 | 932 | 933 | 934 | 965 |
| 982 | 989 | 1030 | 1031 | 1039 | 1060 | 1061 | 1062 | 1078 | 1080 | 1081 | 1095 |
| 1136 | 1159 | 1175 | 1175 | 1194 | 1194 | 1208 | 1209 | 1223 | 1225 | 1322 |  |
| 0 | 97 | 99 | 113 | 114 | 115 | 128 | 128 | 147 | 147 | 163 | 186 |
| 227 | 241 | 242 | 244 | 244 | 256 | 260 | 261 | 262 | 283 | 291 | 309 |
| 330 | 333 | 340 | 347 | 357 | 385 | 388 | 389 | 390 | 390 | 405 | 430 |
| 430 | 435 | 447 | 485 | 487 | 503 | 504 | 518 | 543 | 544 | 552 | 575 |
| 577 | 584 | 599 | 608 | 631 | 632 | 650 | 651 | 653 | 671 | 672 | 690 |
| 691 | 717 | 738 | 745 | 747 | 770 | 778 | 779 | 804 | 818 | 819 | 827 |
| 835 | 837 | 875 | 892 | 892 | 917 | 932 | 932 | 933 | 934 | 965 | 982 |
| 989 | 1031 | 1039 | 1060 | 1061 | 1062 | 1078 | 1080 | 1081 | 1095 | 1136 | 1159 |
| 1175 | 1175 | 1194 | 1194 | 1208 | 1209 | 1223 | 1225 | 1322 |  |  |  |

FIGURE 4.11 (Top) A simulated experimental spectrum $S p e c t r u m _ { 1 0 }$ of Tyrocidine B1. This spectrum has approximately 10% missing (blue) and false (green) masses. Note that the blue masses are not actually in the spectrum, but we show them so that it is clear which masses are missing. (Bottom) A simulated experimental spectrum $S p e c t r u m _ { 2 5 }$ of Tyrocidine B1, with approximately 25% missing and false masses.

**STOP and Think:** How could we have eliminated the incorrect peptide VKLFP**AD**FNQY from consideration for $S p e c t r u m _ { 2 5 } ?$

Notice that although the correct and incorrect peptides are similar, their amino acid compositions differ. If we could figure out the amino acid composition of Tyrocidine B1 from its spectrum alone and run **LEADERBOARDCYCLOPEPTIDESEQUENCING** on this smaller alphabet (rather than on the alphabet of all amino acids), then we could eliminate the incorrect peptide VKLFP**AD**FNQY from consideration.

## From 20 to More than 100 Amino Acids

Until now, we have assumed that just 20 amino acids form the building blocks of proteins; these building blocks are called **proteinogenic amino acids**. There are actually two additional proteinogenic amino acids, called **selenocysteine** and **pyrrolysine**, which are incorporated into proteins by special biosynthetic mechanisms (see **DETOUR: Selenocysteine and Pyrrolysine**). Yet in addition to the 22 proteinogenic amino acids, NRPs contain **non-proteinogenic amino acids**, which expand the number of possible building blocks for antibiotic peptides from 20 to over 100.

![](images/page_225_image_7.jpg)

Enlarging the amino acid alphabet spells trouble for our current approach to cyclopeptide sequencing. Indeed, the correct peptide now must “compete” with many more incorrect ones for a place on the leaderboard, increasing the chance that the correct peptide will be cut along the way.

For example, although Tyrocidine B1 contains only proteinogenic amino acids, its close relative, Tyrocidine B (Val-**Orn**-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr), contains a non-proteinogenic amino acid called **ornithine** (**Orn**). Because so many non-proteinogenic amino acids exist, bioinformaticians often assume that any integer between 57 and 200 may represent the mass of an amino acid; the “lightest” amino acid, Gly, has mass 57 Da, and most amino acids have masses smaller than 200 Da.

**STOP and Think:** Apply **LEADERBOARDCYCLOPEPTIDESEQUENCING** on the extended amino acid alphabet (containing the 144 integers between 57 and 200) to $S p e c t r u m _ { 1 0 } ,$ and identify the highest-scoring peptides.

When we apply **LEADERBOARDCYCLOPEPTIDESEQUENCING** for the extended alphabet to $S p e c t r u m _ { 1 0 } ,$ one of the highest-scoring peptides is VKLFPWFNQ**XZ**, where X has mass 98 and Z has mass 65. Apparently, non-standard amino acids successfully competed with standard amino acids for the limited number of positions on the leaderboard, resulting in VKLFPWFNQ**XZ** winning over the correct peptide VKLFPWFNQY. Since **LEADERBOARDCYCLOPEPTIDESEQUENCING** fails to identify the correct peptide even with only 10% false and missing masses, our stated aim from the previous section is now even more important. We must determine the amino acid composition of a peptide from its spectrum so that we may run **LEADERBOARDCYCLOPEPTIDESEQUENCING** on this smaller alphabet of amino acids.

**STOP and Think:** How can we determine which amino acids are present in an unknown peptide using only an experimental spectrum?

## The Spectral Convolution Saves the Day

One way to determine the amino acid composition of a peptide from its experimental spectrum would be to take the smallest masses present in the spectrum (between 57 and 200 Da). However, even if only a single amino acid mass is missing, then this approach will fail to reconstruct the peptide’s amino acid composition.

Let’s take a different approach. Say that our experimental spectrum contains the masses of subpeptides NQE and NQ. If we subtract these two masses, then we will obtain the mass E for free, even if it was not present in the experimental spectrum! If the underlying peptide is NQEL, then we can also find the mass of E by subtracting the masses of QE and Q or NQEL and LNQ.

Following this example, we define the **convolution** of a spectrum by taking all positive differences of masses in the spectrum. Figure 4.12 shows the convolutions of the theoretical (top) and simulated (bottom) spectra of NQEL from Figure 4.10.

As predicted, some of the values in Figure 4.12 appear more frequently than others. For example, **113** (the mass of L) has multiplicity 8. Six of the eight occurrences of **113** correspond to subpeptide pairs differing in an L: L and ""; LN and N; EL and E; LNQ and NQ; QEL and QE; NQEL and NQE. Interestingly, **129** (the mass of E) pops up three times in the convolution of the simulated spectrum, even though **129** was missing from the spectrum itself.

We now should feel confident about using the most frequently appearing integers in the convolution as a guess for the amino acid composition of an unknown peptide. In our simulated spectrum for NQEL, the most frequent elements of the convolution in the range from 57 to 200 are (multiplicities in parentheses):

**113** (4), **114** (4), **128** (4), **99** (3), **129** (3) .

Note that these most frequent elements capture all four amino acids in NQEL.

## Spectral Convolution Problem:

Generate the convolution of a spectrum.

**Input**: A collection of integers Spectrum.

**Output**: The list of elements in the convolution of Spectrum in decreasing order of their multiplicities.

![](images/page_227_image_13.jpg)

|  | ""0 | L113 | N114 | Q128 | E129 | LN227 | NQ242 | EL242 | QE257 | LNQ355 | ELN356 | QEL370 | NQE371 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 113 | 113 |  |  |  |  |  |  |  |  |  |  |  |  |
| 114 | 114 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| 128 | 128 | 15 | 14 |  |  |  |  |  |  |  |  |  |  |
| 129 | 129 | 16 | 15 | 1 |  |  |  |  |  |  |  |  |  |
| 227 | 227 | 114 | 113 | 99 | 98 |  |  |  |  |  |  |  |  |
| 242 | 242 | 129 | 128 | 114 | 113 | 15 |  |  |  |  |  |  |  |
| 242 | 242 | 129 | 128 | 114 | 113 | 15 |  |  |  |  |  |  |  |
| 257 | 257 | 144 | 143 | 129 | 128 | 30 | 15 | 15 |  |  |  |  |  |
| 355 | 355 | 242 | 241 | 227 | 226 | 128 | 113 | 113 | 98 |  |  |  |  |
| 356 | 356 | 243 | 242 | 228 | 227 | 129 | 114 | 114 | 99 | 1 |  |  |  |
| 370 | 370 | 257 | 256 | 242 | 241 | 143 | 128 | 128 | 113 | 15 | 14 |  |  |
| 371 | 371 | 258 | 257 | 243 | 242 | 144 | 129 | 129 | 114 | 16 | 15 | 1 |  |
| 484 | 484 | 371 | 370 | 356 | 355 | 257 | 242 | 242 | 227 | 129 | 128 | 114 | 113 |

|  | " "0 | false99 | L113 | N114 | Q128 | LN227 | QE257 | false299 | LNQ355 | ELN356 | QEL370 | NQE371 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| 99 | 99 |  |  |  |  |  |  |  |  |  |  |  |
| 113 | 113 | 14 |  |  |  |  |  |  |  |  |  |  |
| 114 | 114 | 15 | 1 |  |  |  |  |  |  |  |  |  |
| 128 | 128 | 29 | 15 | 14 |  |  |  |  |  |  |  |  |
| 227 | 227 | 128 | 114 | 113 | 99 |  |  |  |  |  |  |  |
| 257 | 257 | 158 | 144 | 143 | 129 | 30 |  |  |  |  |  |  |
| 299 | 299 | 200 | 186 | 185 | 171 | 72 | 42 |  |  |  |  |  |
| 355 | 355 | 256 | 242 | 241 | 227 | 128 | 98 | 56 |  |  |  |  |
| 356 | 356 | 257 | 243 | 242 | 228 | 129 | 99 | 57 | 1 |  |  |  |
| 370 | 370 | 271 | 257 | 256 | 242 | 143 | 113 | 71 | 15 | 14 |  |  |
| 371 | 371 | 272 | 258 | 257 | 243 | 144 | 114 | 72 | 16 | 15 | 1 |  |
| 484 | 484 | 385 | 371 | 370 | 356 | 257 | 227 | 185 | 129 | 128 | 114 | 113 |

FIGURE 4.12 (Top) Spectral convolution for the theoretical spectrum of NQEL. The most frequent elements in the convolution between 57 and 200 are (multiplicities in parentheses): 113 (8), 114 (8), 128 (8), 129 (8). (Bottom) Spectral convolution for the simulated spectrum of NQEL. The most frequent elements in the convolution between 57 and 200 are (multiplicities in parentheses): 113 (4), 114 (4), 128 (4), 99 (3), 129 (3).

Recall that **LEADERBOARDCYCLOPEPTIDESEQUENCING** failed to reconstruct Tyrocidine B1 from $S p e c t r u m _ { 1 0 }$ when using the extended alphabet of amino acids. The ten most frequent elements of its spectral convolution in the range from 57 to 200 are (multiplicities in parentheses):

| 147 (35) | 128 (31) | 97 (28) | 113 (28) | 114 (26) |
| --- | --- | --- | --- | --- |
| 186 (23) | 57 (21) | 163 (21) | 99 (18) | 145 (18) |

Every mass in this list except for 57 and 145 captures an amino acid in Tyrocidine B1!

We now have the outline for a new cyclopeptide sequencing algorithm. Given an experimental spectrum, we first compute the convolution of an experimental spectrum. We then select the M most frequent elements between 57 and 200 in the convolution to form an extended alphabet of amino acid masses. In order to be fair, we should include the top M elements of the convolution “with ties”. Finally, we run **LEADERBOARDCYCLOPEPTIDESEQUENCING**, where amino acid masses are restricted to this alphabet. We call this algorithm **CONVOLUTIONCYCLOPEPTIDESEQUENCING**.

**STOP and Think:** Run **CONVOLUTIONCYCLOPEPTIDESEQUENCING** on the simulated spectra $S p e c t r u m _ { 1 0 }$ and $S p e c t r u m _ { 2 5 }$ with $N = 1 0 0 0$ and $M = 2 0$ Identify the highest scoring peptides.

CONVOLUTIONCYCLOPEPTIDESEQUENCING (with $N = 1 0 0 0$ and $M = 2 0 )$ now correctly reconstructs Tyrocidine B1 from $S p e c t r u m _ { 1 0 }$ . The true test of this algorithm is whether it will work on a noisier spectrum. Recall that our previous algorithm failed on $S p e c t r u m _ { 2 5 } ;$ in contrast, **CONVOLUTIONCYCLOPEPTIDESEQUENCING** (with $N = 1 0 0 0$ and $M = 2 0 )$ now correctly identifies Tyrocidine B1 from this spectrum!

## Epilogue: From Simulated to Real Spectra

In this chapter, we have sheltered you from the gruesome realities of mass spectrometry by providing simulated spectra that are relatively easy to sequence (even those with false and missing masses). We committed a sin of omission by loosely describing the mass spectrometer as a “scale” and assuming that this complex machine simply weighs tiny peptide fragments one at a time. In truth, the mass spectrometer first converts subpeptides into ions $( \mathrm { i . e . } ,$ charged particles). Ionization of particles helps the mass spectrometer sort the ions by using an electromagnetic field; ions are separated not by their mass, but rather according to their **mass/charge ratio**. If fragment ion NQY (integer mass: $1 1 4 + 1 2 8 + 1 6 3 = 4 0 5 )$ has charge +1, then it contains one additional proton, resulting in a total integer mass of 406 and a mass/charge ratio of $4 0 6 / 1 =$ 406. To be more precise, the monoisotopic mass of NQY is approximately $1 1 4 . 0 4 3 \pm$ $128.058 + 163.063 = 405.164;$ , and the mass of a proton is 1.007 Da, which makes the mass charge/ratio more closely equal to $\left( 4 0 5 . 1 6 4 + 1 . 0 0 7 \right) / 1 = 4 0 6 . 1 7 1$ (see **DETOUR: Molecular Mass**).

The mass spectrometer outputs a collection of **peaks**, which are shown in Figure 4.13 for a real Tyrocidine B1 spectrum. Each peak’s x-coordinate represents an ion’s mass/charge ratio, and its height represents the **intensity** (i.e., relative abundance) of ions having that mass/charge ratio. For example, in the experimental spectrum of Tyrocidine B1 shown in Figure 4.13, you will find a small (almost invisible) peak with a mass/charge ratio of 406.30, which corresponds to the fragment ion NQY having mass/charge ratio 406.171, with an error of approximately 0.13 Da.

As you can imagine, we must navigate a few practical barriers in order to analyze real spectra. First, the charge of each peak is unknown, often forcing researchers to try all possible charges from 1 to some parameter maxCharge, where the particular choice of maxCharge depends on the fragmentation technology used. This procedure generates maxCharge masses for each peak, so that the larger the value of maxCharge, the more false masses in the spectrum.

![](images/page_230_chart_5.jpg)

<details>
<summary>spectrogram</summary>

| X | Y |
| --- | --- |
| ~430 | ~0.1 |
| ~540 | ~0.2 |
| ~670 | ~0.3 |
| ~820 | ~0.4 |
| ~920 | ~0.3 |
| ~1060 | ~0.6 |
| ~1170 | ~0.4 |
| ~1280 | ~0.8 |
| ~1300 | ~1.0 |
| ~1370 | ~0.3 |
</details>

FIGURE 4.13 A real spectrum for Tyrocidine B1. A peak’s x-coordinate represents its mass/charge ratio, and its height represents the intensity of ions having that mass/charge ratio.

Second, the spectrum in Figure 4.13 has nearly 1,000 peaks, most of which are **false peaks**, meaning that their mass/charge ratio does not correspond to any subpeptide’s mass/charge ratio (for any charge value). Fortunately, false peaks typically have low intensities, necessitating a pre-processing step that removes low-intensity peaks before applying an algorithm. Figure 4.14 shows the list of the 95 mass/charge ratios for peaks that survived this preprocessing step for the Tyrocidine B1 spectrum in Figure 4.13. Their intensities may nevertheless vary by 2-3 orders of magnitude; for example, the intensity of the peak having mass/charge ratio 372.2 is 300 times smaller than the intensity of the peak with mass/charge ratio 1306.5.

| 372.2 | 397.2 | 402.0 | 406.3 | 415.1 | 431.2 | 448.3 | 449.3 | 452.2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 471.3 | 486.3 | 488.2 | 500.5 | 505.3 | 516.1 | 536.1 | 544.2 | 545.3 |
| 562.5 | 571.3 | 599.2 | 614.4 | 615.4 | 616.4 | 618.2 | 632.0 | 655.5 |
| 656.3 | 672.5 | 673.3 | 677.3 | 691.4 | 692.4 | 712.1 | 722.3 | 746.5 |
| 760.4 | 761.6 | 762.5 | 771.6 | 788.4 | 802.3 | 803.3 | 818.5 | 819.4 |
| 831.4 | 836.3 | 853.3 | 875.5 | 876.5 | 901.5 | 915.9 | 916.5 | 917.8 |
| 918.4 | 933.4 | 934.7 | 935.5 | 949.4 | 966.2 | 995.4 | 1015.6 | 1027.5 |
| 1029.5 | 1031.5 | 1044.5 | 1046.5 | 1061.5 | 1063.4 | 1079.2 | 1083.7 |  |
| 1088.4 | 1093.5 | 1096.5 | 1098.4 | 1158.5 | 1159.5 | 1176.6 | 1177.7 |  |
| 1178.6 | 1192.7 | 1195.4 | 1207.5 | 1210.4 | 1224.6 | 1252.5 | 1270.5 |  |
| 1271.5 | 1278.6 | 1279.6 | 1295.6 | 1305.6 | 1306.5 | 1307.5 | 1309.6 |  |

FIGURE 4.14 The 95 mass/charge ratios having the highest intensity in Figure 4.13. The values shown in bold correspond to masses of subpeptides of Tyrocidine B1, if we allow a mass discrepancy of up to 0.3 Da (see Figure 4.15).

| Mass | Subpeptide | Mass | Subpeptide | Mass | Subpeptide |
| --- | --- | --- | --- | --- | --- |
| 406.2 | NQY | 431.2 | FPW | 448.2 | WFN |
| 486.2 | KLFP | 488.2 | VKLF | 505.2 | NQYV |
| 544.2 | LFPW | 545.2 | PWFN | 632.3 | QYVKL |
| 672.3 | KLFPW | 673.3 | PWFNQ | 691.3 | LFPWF |
| 692.3 | FPWFN | 746.3 | NQYVKL | 771.3 | VKLFPW |
| 819.4 | KLFPWF | 836.4 | PWFNQY | 876.4 | QYVKLFP |
| 918.4 | VKLFPWF | 933.4 | LFPWFNQ | 934.4 | YVKLFPW |
| 935.4 | PWFNQYV | 966.4 | WFNQYVK | 1061.5 | KLFPWFNQ |
| 1063.5 | PWFNQYVK | 1079.5 | WFNQYVKL | 1096.5 | LFPWFNQY |
| 1176.5 | NQYVKLFPW | 1195.6 | LFPWFNQYV | 1210.6 | FPWFNQYVK |
| 1224.6 | KLFPWFNQY |  |  |  |  |

FIGURE 4.15 Values from Figure 4.14 corresponding to masses of subpeptides of Tyrocidine B1, with maxCharge = 1 and an allowable discrepancy of up to 0.3 Da. These 31 masses represent less than a third of the 95 subpeptides in the theoretical spectrum of Tyrocidine B1.

Only 31 of these 95 mass/charge ratios (shown in bold in Figure 4.14) can be matched to subpeptides of Tyrocidine B1, as illustrated in Figure 4.15.

You can now see that sequencing Tyrocidine B1 from a real spectrum, for which twothirds of all masses are false, presents a much more difficult problem than sequencing this peptide from the simulated Spectrum<sub>25</sub>. In the following challenge problem, you will need to further develop the methods we studied in this chapter to analyze a real spectrum.

**CHALLENGE PROBLEM:** Tyrocidine B1 is just one of many known NRPs produced by Bacillus brevis. A single bacterial species may produce dozens of different antibiotics, and even after 70 years of research, there are likely undiscovered antibiotics produced by Bacillus brevis. Try to sequence the tyrocidine corresponding to the real experimental spectrum below. Since the fragmentation technology used for generating this spectrum tends to produce ions with charge +1, you can safely assume that all charges are +1.

| 371.5 | 375.4 | 390.4 | 392.2 | 409.0 | 420.2 | 427.2 | 443.3 | 446.4 | 461.3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 471.4 | 477.4 | 491.3 | 505.3 | 506.4 | 519.2 | 536.1 | 546.5 | 553.3 | 562.3 |
| 588.2 | 600.3 | 616.2 | 617.4 | 618.3 | 633.4 | 634.4 | 636.2 | 651.5 | 652.4 |
| 702.5 | 703.4 | 712.5 | 718.3 | 721.0 | 730.3 | 749.4 | 762.6 | 763.4 | 764.4 |
| 779.6 | 780.4 | 781.4 | 782.4 | 797.3 | 862.4 | 876.4 | 877.4 | 878.6 | 879.4 |
| 893.4 | 894.4 | 895.4 | 896.5 | 927.4 | 944.4 | 975.5 | 976.5 | 977.4 | 979.4 |
| 1005.5 | 1007.5 | 1022.5 | 1023.7 | 1024.5 | 1039.5 | 1040.3 | 1042.5 | 1043.4 | 1057.5 |
| 1119.6 | 1120.6 | 1137.6 | 1138.6 | 1139.5 | 1156.5 | 1157.6 | 1168.6 | 1171.6 | 1185.4 |
| 1220.6 | 1222.5 | 1223.6 | 1239.6 | 1240.6 | 1250.5 | 1256.5 | 1266.5 | 1267.5 | 1268.6 |

**Hint**: since the peptide from which this spectrum was generated is in the tyrocidine family, this peptide should be similar to Tyrocidine B1.

## Open Problems

The Beltway and Turnpike Problems

In the case of the alphabet of arbitrary integers, the Cyclopeptide Sequencing Problem corresponds to a computer science problem known as the **Beltway Problem**. The Beltway Problem asks you to find a set of points on a circle such that the distances between all pairs of points (where distance is measured around the circle) match a given collection of integers.

The Beltway Problem’s analogue in the case when the points lie along a line segment instead of on a circle is called the **Turnpike Problem**. The terms “beltway” and “turnpike” arise from an analogy with exits on circular and linear roads, respectively. In the case of n points on a circle and line, the inputs for the Beltway and Turnpike Problems consist of $n ( n - 1 ) + 2$ and $\frac{n(n - 1)}{2} + 2$ distances, respectively (these formulas include the distance 0 as well as the length of the entire segment).

Various attempts to design polynomial algorithms for the Beltway and Turnpike Problems (or to prove that they are intractable) have failed. However, there is a **pseudo**polynomial algorithm for the Turnpike Problem (see **DETOUR: Pseudo-polynomial Algorithm for the Turnpike Problem**). In contrast to a truly polynomial algorithm, which can be bounded by a polynomial in the length of the input, a pseudo-polynomial algorithm for the Turnpike Problem is polynomial in the total length of the line segment. For example, if n points are separated by huge distances, say on the order of $2 ^ { 1 0 0 }$ , then a polynomial algorithm would still be fast, whereas a pseudo-polynomial algorithm would be prohibitively slow. Note that although the distances themselves will be huge, each distance can be stored using only about 100 bits, implying that the length of the input is small even for such large distances.

Pseudo-polynomial algorithms are useful in practice because practical instances of the problems typically do not include huge distances. Interestingly, although a pseudo-polynomial algorithm exists for the Turnpike Problem, such an algorithm for the seemingly similar Beltway Problem remains undiscovered. Can you develop such an algorithm?

## Sequencing cyclic peptides in primates

Bacteria and fungi do not have a monopoly on producing cyclic peptides; animals and plants make them too (albeit through a completely different mechanism). The first cyclic peptide found in animals (called ✓**-defensin**) was discovered in 1999 in macaques. ✓-defensin prevents viruses from entering cells and has strong anti-HIV activity. Yet the question of how primates make ✓-defensin remains a mystery.

Needless to say, there is no 54-mer in the macaque genome encoding the 18 amino acid-long ✓-defensin. Instead, this cyclic peptide is formed by concatenating two 9 amino acid-long peptides excised from two different proteins called RTD1a and RTD1b, as shown in Figure 4.16. It remains unclear which enzymes do this elaborate cutting and pasting.

Interestingly, macaques and baboons produce ✓-defensin, whereas humans and chimpanzees do not. This discrepancy makes us wonder whether a mutation occurred in the human-chimpanzee ancestor that resulted in the loss of this very useful peptide. Interestingly, genes very similar to RTD1a and RTD1b do exist in humans, but a codon in one of these genes mutated into a stop codon, thus shortening the encoded protein. Since this stop codon is located before the 9 amino acid-long peptide contributing to ✓-defensin, humans do not produce this peptide and thus cannot produce ✓-defensin.

![](images/page_234_image_1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["RTD1a"] --> B["...KGLRCICTRGFCRLL"]
  B --> C["...RGLRCLCRRGVCQLL"]
```
</details>

-defensin

![](images/page_234_image_3.jpg)

FIGURE 4.16 The 18 amino acid-long ✓-defensin peptide is formed by cutting two 9 amino acid-long peptides RCICTRGFC and RCLCRRGVC from the RTD1a and RTD1b proteins, concatenating them, and then circularizing the resulting peptide (along with introducing three disulfide bridges that form bonds across the peptide).

In a remarkable experiment, Alexander Cole demonstrated that humans could get ✓- defensin back! Certain drugs can force the ribosome to ignore stop codons and continue translating RNA, even after encountering a stop codon. The researchers demonstrated that after treatment with such a drug, human cells began producing the human version of ✓-defensin. The surprising conclusion of this experiment is that although humans and chimpanzees lost ✓-defensin millions of years ago, we still possess the mysterious enzymes required to cut and paste its constituent peptides.

Some biologists believe that since the enzymes making ✓-defensin still work in humans, they must be needed for something else. If these enzymes did not provide some selective advantage, then over time, mutations would cause their genes to become **pseudogenes**, or non-functional remnants of previously working genes. The most natural explanation for why these enzymes are still functional is that humans produce still undiscovered cyclic peptides, and that the enzymes needed for ✓-defensin are also used to “cut-and-paste” other (still undiscovered) cyclic peptides. The hypothesis that we may possess undiscovered cyclic peptides is not as improbable as you might think because biologists still lack robust algorithms for cyclopeptide discovery from the billions of spectra generated in hundreds of labs analyzing the human proteome.

By default, researchers assume that all spectra ever acquired in human proteome studies originated from linear peptides. Could they be wrong? Can you devise a fast cyclopeptide sequencing algorithm that can analyze all these spectra and hopefully discover human cyclopeptides?

## Charging Stations

Generating the theoretical spectrum of a peptide

Given an amino acid string Peptide, we will begin by assuming that it represents a linear peptide. Our approach to generating its theoretical spectrum is based on the assumption that the mass of any subpeptide is equal to the difference between the masses of two prefixes of Peptide. We can compute an array PREFIXMASS storing the masses of each prefix of Peptide in increasing order, e.g., for Peptide = NQEL, PREFIXMASS = (0, 114, 242, 371, 484). Then, the mass of the subpeptide of Peptide beginning at position i + 1 and ending at position j can be computed as PREFIXMASS(j)   PREFIXMASS(i). For example, when Peptide = NQEL,

$$
\mathrm{MASS} (\mathrm{QE}) = \mathrm{PREFIXMASS} (3) - \mathrm{PREFIXMASS} (1) = 3 7 1 - 1 1 4 = 2 5 7.
$$

The following pseudocode implements this idea. It also represents the alphabet of 20 amino acids and their integer masses as a pair of 20-element arrays AMINOACID and AMINOACIDMASS, corresponding to the top and bottom rows of Figure 4.6, respectively.

```python
LINEARSPECTRUM(Peptide, AMINOACID, AMINOACIDMASS)
    PREFIXMASS(0) ← 0
    for i ← 1 to |Peptide|
        for j ← 1 to 20
            if AMINOACID(j) = i-th amino acid in Peptide
                PREFIXMASS(i) ← PREFIXMASS(i - 1) + AMINOACIDMASS(j)
    LinearSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| - 1
        for j ← i + 1 to |Peptide|
            add PREFIXMASS(j) - PREFIXMASS(i) to LinearSpectrum
    return the sorted list LinearSpectrum
```

If the amino acid string Peptide represents a cyclic peptide instead, then the masses in its theoretical spectrum can be divided into those found by **LINEARSPECTRUM** and those corresponding to subpeptides wrapping around the end of the linearized version of Peptide. Furthermore, each such subpeptide has mass equal to the difference between MASS(Peptide) and a subpeptide mass identified by **LINEARSPECTRUM**. For example, when Peptide = **NQEL**,

![](images/page_235_image_9.jpg)

$$
\mathrm{MASS} (\mathbf {L N}) = \mathrm{MASS} (\mathbf {N Q E L}) - \mathrm{MASS} (\mathbf {Q E}) = 4 8 4 - 2 5 7 = 2 2 7.
$$

Thus, we can generate a cyclic spectrum by making only a small modification to the pseudocode of **LINEARSPECTRUM**.

```python
CYCLICSPECTRUM(Peptide, AMINOACID, AMINOACIDMASS)
    PREFIXMASS(0) ← 0
    for i ← 1 to Peptide
        for j ← 1 to 20
            if AMINOACID(j) = i-th amino acid in Peptide
                PREFIXMASS(i) ← PREFIXMASS(i - 1) + AMINOACIDMASS(j)
    peptideMass ← PREFIXMASS(|Peptide|)
    CyclicSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| - 1
        for j ← i + 1 to |Peptide|
            add PREFIXMASS(j) - PREFIXMASS(i) to CyclicSpectrum
            if i > 0 and j < |Peptide|
                add peptideMass - (PREFIXMASS(j) - PREFIXMASS(i)) to CyclicSpectrum
    return sorted list CyclicSpectrum
```

How fast is **CYCLOPEPTIDESEQUENCING**?

Let’s run **CYCLOPEPTIDESEQUENCING** on the following Spectrum:

| 0 | 97 | 97 | 99 | 101 | 103 | 196 | 198 | 198 | 200 | 202 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 295 | 297 | 299 | 299 | 301 | 394 | 396 | 398 | 400 | 400 | 497 |

**CYCLOPEPTIDESEQUENCING** first expands the set Peptides into the set of all 1-mers consistent with Spectrum:

| 97 | 99 | 101 | 103 |
| --- | --- | --- | --- |
| P | V | T | C |

The algorithm next appends each of the 18 amino acid masses to each of the 1-mers above. The resulting set Peptides containing 4 · 18 = 72 peptides of length 2 is then trimmed to keep only the 10 peptides that are consistent with Spectrum:

| 97-99 | 97-101 | 97-103 | 99-97 | 99-101 |
| --- | --- | --- | --- | --- |
| PV | PT | PC | VP | VT |
| 99-103 | 101-97 | 101-99 | 103-97 | 103-99 |
| VC | TP | TV | CP | CV |

After expansion and trimming in the next iteration, the set Peptides contains 15 consistent 3-mers:

| 97-99-103 | 97-99-101 | 97-101-97 | 97-101-99 | 97-103-99 |
| --- | --- | --- | --- | --- |
| PVC | PVT | PTP | PTV | PCV |
| 99-97-103 | 99-97-101 | 99-101-97 | 99-103-97 | 101-97-99 |
| VPC | VPT | VTP | VCP | TPV |
| 101-97-103 | 101-99-97 | 103-97-101 | 103-97-99 | 103-99-97 |
| TPC | TVP | CPT | CPV | CVP |

With one more iteration, the set Peptides contains ten consistent 4-mers. Observe that the six 3-mers highlighted in red above failed to expand into any 4-mers below, and so we now know that **CYCLOPEPTIDESEQUENCING** may generate some incorrect k-mers at intermediate iterations.

| 97-99-103-97 | 97-101-97-99 | 97-101-97-103 | 97-103-99-97 |
| --- | --- | --- | --- |
| PVCP | PTPV | PTPC | PCVP |
| 99-97-101-97 | 99-103-97-101 | 101-97-99-103 | 101-97-103-99 |
| VPTP | VCPT | TPVC | TPCV |
|  | 103-97-101-97 | 103-99-97-101 |  |
|  | CPTP | CVPT |  |

In the final iteration, we generate ten consistent 5-mers:

| 97-99-103-97-101PVCPT | 97-101-97-99-103PTPVC | 97-101-97-103-99PTPCV |
| --- | --- | --- |
| 97-103-99-97-101PCVPT | 99-97-101-97-103VPTPC | 99-103-97-101-97VCPTP |
| 101-97-99-103-97TPVCP | 101-97-103-99-97TPCVP | 103-97-101-97-99CPTPV |
|  | 103-99-97-101-97CVPTP |  |

All these linear peptides correspond to the same cyclic peptide PVCPT, thus solving the Cyclopeptide Sequencing Problem. You can verify that **CYCLOPEPTIDESEQUENCING** also quickly reconstructs Tyrocidine B1 from the spectrum in Figure 4.7.

Trimming the peptide leaderboard

Note: This Charging Station uses some notation from CHARGING STATION: Gener**ating the Theoretical Spectrum of a Peptide**.

To implement the TRIM function in **LEADERBOARDCYCLOPEPTIDESEQUENCING**, we first will generate the theoretical spectra of all linear peptides from Leaderboard. Then, we will compute the scores of each theoretical spectrum against an experimental spectrum Spectrum. This requires implementing LINEARSCORE(Peptide, Spectrum).

Figure 4.17 shows a leaderboard of ten linear peptides represented as a list Leaderboard along with a ten-element array LINEARSCORES containing their scores.

| Leaderboard | PVT | PTP | PTV | PCP | VPC | VTP | VCP | TPV | TPC | TVP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINEARSCORES | 6 | 2 | 4 | 6 | 5 | 2 | 5 | 4 | 4 | 3 |

FIGURE 4.17 A collection of peptides Leaderboard (top) along with an array LINEARSCORES (bottom) holding the score of each peptide.

The **TRIM** algorithm, shown below, sorts all peptides in Leaderboard according to their scores, resulting in a sorted Leaderboard (Figure 4.18). **TRIM** then retains the top N scoring peptides including ties (e.g., for N = 5, the seven top-scoring peptides shown in blue will be retained), and removes all other peptides from Leaderboard.

![](images/page_238_image_10.jpg)

![](images/page_238_image_11.jpg)

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
TRIM(Leaderboard, Spectrum, N, AMINOACID, AMINOACIDMASS)
    for $j \leftarrow 1$ to |Leaderboard|
        Peptide $\leftarrow j$-th peptide in Leaderboard
        LINEARSCORES($j$) $\leftarrow$ LINEARSCORE(Peptide, Spectrum)
    sort Leaderboard according to the decreasing order of scores in LINEARSCORES
    sort LINEARSCORES in decreasing order
    for $j \leftarrow N + 1$ to |Leaderboard|
        if LINEARSCORES($j$) &lt; LINEARSCORES(N)
            remove all peptides starting from the $j$-th peptide from Leaderboard
            return Leaderboard
    return Leaderboard
</div>

| Leaderboard | PVT | PCP | VPC | VCP | PTV | TPV | TPC | TVP | PTP | VTP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LINEARSCORES | 6 | 6 | 5 | 5 | 4 | 4 | 4 | 3 | 2 | 2 |

FIGURE 4.18 Arrays Leaderboard and LINEARSCORES from Figure 4.17 sorted according to score. The seven highest-scoring peptides, which will be retained after applying TRIM with N = 5, are shown in blue; remaining peptides are shown in red and will be removed from the leaderboard.

## Detours

## Gause and Lysenkoism

The term **Lysenkoism** refers to the politicization of genetics in the Soviet Union that began in the late 1920s and lasted for three decades until the death of Stalin. Lysenkoism was built on theories of inheritance by acquired characteristics, which ran counter to Mendelian laws.

In 1928, Trofim Lysenko, the son of Ukrainian peasants, claimed to have found a way to vastly increase the crop yield of wheat. During Stalin’s rule, Soviet propaganda focused on inspirational stories of working class citizens, and it portrayed Lysenko as a genius, even though he had manufactured his experimental data. Empowered by his sudden hero status, Lysenko denounced genetics and started promoting his own “scientific” views. He called geneticists “fly lovers and people haters” and claimed that they were trying to undermine the onward march of Soviet agriculture.

![](images/page_239_image_8.jpg)