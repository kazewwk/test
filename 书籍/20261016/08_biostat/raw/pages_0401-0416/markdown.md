## 8.3 Inference for two or more groups

The comparison of the proportion of breast cancer deaths between the two groups can also be approached using a two-way contingency table, which contains counts for combinations of outcomes for two variables. The results for the mammogram study in this format are shown in Figure 8.3.

Previously, the main question of interest was stated as, "Is there evidence of a difference in the proportion of breast cancer deaths between the two screening groups?" If the probability of a death from breast cancer does not depend the method of screening, then screening method and outcome are independent. Thus, the question can be re-phrased: "Is there evidence that screening method is associated with outcome?"

Hypothesis testing in a two-way table assesses whether the two variables of interest are associated (i.e., not independent). The approach can be applied to settings with two or more groups and for responses that have two or more categories. The observed number of counts in each table cell are compared to the number of **expected counts**, where the expected counts are calculated under the assumption that the null hypothesis of no association is true. A $\chi ^ { 2 }$ test of significance is based on the differences between observed and expected values in the cells.

| Death from BC | Yes | No | Total |
| --- | --- | --- | --- |
| Mammogram | 500 | 44,425 | 44,925 |
| Control | 505 | 44,405 | 44,910 |
| Total | 1,005 | 88,830 | 89,835 |

Figure 8.3: Results of the mammogram study, as a contingency table with marginal totals.

## GUIDED PRACTICE 8.16

Formulate hypotheses for a contingency-table approach to analyzing the mammogram data.<sup>13</sup>

## 8.3.1 Expected counts

If type of breast cancer screening had no effect on outcome in the mammogram data, what would the expected results be?

Recall that if two events A and B are independent, then $P(A \cap B) = P(A)P(B)$ . Let A represent assignment to the mammogram group and B the event of death from breast cancer. Under independence, the number of individuals out of 89,835 that are expected to be in the mammogram screening group and die from breast cancer equals:

$$
(8 9, 8 3 5) P (A) P (B) = (8 9, 8 3 5) \bigg (\frac {4 4 , 9 2 5}{8 9 , 8 3 5} \bigg) \bigg (\frac {1 , 0 0 5}{8 9 , 8 3 5} \bigg) = 5 0 2. 6.
$$

Note that the quantities 44,925 and 1,005 are the row and column totals corresponding to the upper left cell of Figure 8.3, and 89,835 is the total number n of observations in the table. A general formula for computing expected counts for any cell can be written from the marginal totals and the total number of observations.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13H0: There is no association between type of breast cancer screening and death from breast cancer. HA: There is an association between type of breast cancer screening and death from breast cancer.</span></small>

## COMPUTING EXPECTED COUNTS IN A TWO-WAY TABLE

To calculate the expected count for the $i ^ { t h }$ row and $j ^ { t h }$ column, compute

$$
\text {Expected Count} _ {\text {row} i, \text {col} j} = \frac {(\text {row} i \text {total}) \times (\text {column} j \text {total})}{\text {table total}}.
$$

## EXAMPLE 8.17

Calculate expected counts for the data in Figure 8.3.

$$
\begin{array}{l} E _ {1, 1} = \frac {4 4 , 9 2 5 \times 1 , 0 0 5}{8 9 , 8 3 5} = 5 0 2. 6 \quad E _ {1, 2} = \frac {4 4 , 9 2 5 \times 8 8 , 8 3 0}{8 9 , 8 3 5} = 4 4, 4 2 2. 4 \\ E _ {2, 1} = \frac {2 , 9 2 2 \times 1 , 0 0 5}{8 9 , 8 3 5} = 5 0 2. 4 \quad E _ {2, 2} = \frac {7 , 0 7 8 \times 8 8 , 8 3 0}{8 9 , 8 3 5} = 4 4, 4 0 7. 6 \\ \end{array}
$$

| Death from BC | Yes | No | Total |
| --- | --- | --- | --- |
| Mammogram | 500 (502.6) | 44,425 (44,422.4) | 44,925 |
| Control | 505 (502.4) | 44,405 (44,407.6) | 44,910 |
| Total | 1,005 | 88,830 | 89,835 |

Figure 8.4: Results of the mammogram study, with (expected counts). The expected counts should also sum to the row and column totals; this can be a useful check for accuracy.

## EXAMPLE 8.18

If a newborn is $\mathrm { H W ^ { + } }$ , should he or she be treated with nevirapine (NVP) or a more expensive drug, lopinarvir (LPV)? In this setting, success means preventing virologic failure; i.e., growth of the virus. A randomized study was conducted to assess whether there is an association between treatment and outcome.14 Of the 147 children administered NVP, about 41% experienced virologic failure; of the 140 children administered LPV, about 19% experienced virologic failure. Construct a table of observed counts and a table of expected counts.

Convert the proportions to count data: 41% of 147 is approximately 60, and 19% of 140 is approximately 27. The observed results are given in Figure 8.5.

Calculate the expected counts for each cell:

$$
\begin{array}{l} E _ {1, 1} = \frac {8 7 \times 1 4 7}{2 8 7} = 4 4. 6 \quad E _ {1, 2} = \frac {8 7 \times 1 4 0}{2 8 7} = 4 2. 4 \\ E _ {2, 1} = \frac {2 0 0 \times 1 4 7}{2 8 7} = 1 0 2. 4 \quad E _ {2, 2} = \frac {2 0 0 \times 1 4 0}{2 8 7} = 9 7. 6 \\ \end{array}
$$

The expected counts are summarized in Figure 8.6.

|  | NVP | LPV | Total |
| --- | --- | --- | --- |
| Virologic Failure | 60 | 27 | 87 |
| Stable Disease | 87 | 113 | 200 |
| Total | 147 | 140 | 287 |

Figure 8.5: Observed counts for the HIV study.

|  | NVP | LPV | Total |
| --- | --- | --- | --- |
| Virologic Failure | 44.6 | 42.4 | 87 |
| Stable Disease | 102.4 | 97.6 | 200 |
| Total | 147 | 140 | 287 |

Figure 8.6: Expected counts for the HIV study.

## 8.3.2 The $\chi ^ { 2 }$ test statistic

Previously, test statistics have been constructed by calculating the difference between a point estimate and a null value, then dividing by the standard error of the point estimate to standardize the difference. The $\chi ^ { 2 }$ statistic is based on a different idea. In each cell of a table, the difference observed - expected is a measure of the discrepancy between what was observed in the data and what should have been observed under the null hypothesis of no association. If the row and column variables are highly associated, that difference will be large. Two adjustments are made to the differences before the final statistic is calculated. First, since both positive and negative differences suggest a lack of independence, the differences are squared to remove the effect of the sign. Second, cells with larger counts may have larger discrepancies by chance alone, so the squared differences in each cell are scaled by the number expected in the cell under the hypothesis of independence. The final $\chi ^ { 2 }$ statistic is the sum of these standardized squared differences, where the sum has one term for each cell in the table.

The $\chi ^ { 2 }$ test statistic is calculated as:

$$
\chi^ {2} = \sum_ {\text {all cells}} \frac {(\text {observed - expected}) ^ {2}}{\text {expected}}.
$$

The theory behind the $\chi ^ { 2 }$ test and its sampling distribution relies on the same normal approximation to the binomial distribution that was introduced earlier. The cases in the dataset must be independent and each expected cell count should be at least 10. The second condition can be relaxed in tables with more than 4 cells.

χ<sup>2</sup> chi-square test statistic

## CONDITIONS FOR THE $\chi ^ { 2 }$ TEST

Two conditions that must be checked before performing a $\chi ^ { 2 }$ test:

**Independence.** Each case that contributes a count to the table must be independent of all the other cases in the table.

**Sample size.** Each expected cell count must be greater than or equal to 10. For tables larger than 2 × 2, it is appropriate to use the test if no more than 1/5 of the expected counts are less than 5, and all expected counts are greater than 1.

## EXAMPLE 8.19

For the mammogram data, check the conditions for the $\chi ^ { 2 }$ test and calculate the $\chi ^ { 2 }$ test statistic.

Independence is a reasonable assumption, since individuals have been randomized to either the treatment or control group. Each expected cell count is greater than 10.

![](images/page_403_image_5.jpg)

$$
\begin{array}{l} \chi^ {2} = \sum_ {\text {all cells}} \frac {(\text {observed - expected}) ^ {2}}{\text {expected}} \\ = \frac {(5 0 0 - 5 0 2 . 6) ^ {2}}{5 0 2 . 6} + \frac {(4 4 , 4 2 5 - 4 4 , 4 2 2 . 4) ^ {2}}{4 4 , 4 2 2 . 4} + \frac {(5 0 5 - 5 0 2 . 4) ^ {2}}{5 0 2 . 4} + \frac {(4 4 , 4 0 5 - 4 4 , 4 0 7 . 6) ^ {2}}{4 4 , 4 0 7 . 6} \\ = 0. 0 2. \\ \end{array}
$$

![](images/page_403_image_7.jpg)

## GUIDED PRACTICE 8.20

For the HIV data, check the conditions for the $\chi ^ { 2 }$ test and calculate the $\chi ^ { 2 }$ test statistic.<sup>15</sup>

## 8.3.3 Calculating p-values for a $\chi ^ { 2 }$ distribution

The **chi-square distribution** is often used with data and statistics that are positive and rightskewed. The distribution is characterized by a single parameter, the degrees of freedom. Figure 8.7 demonstrates three general properties of chi-square distributions as the degrees of freedom increases: the distribution becomes more symmetric, the center moves to the right, and the variability increases.

![](images/page_403_chart_12.jpg)

<details>
<summary>line</summary>

| X | Degrees of Freedom::2 | Degrees of Freedom::4 | Degrees of Freedom::9 |
| --- | --- | --- | --- |
| 0 | ~1.0 | 0 | 0 |
| 5 | ~0.1 | ~0.3 | ~0.2 |
| 10 | ~0.0 | ~0.05 | ~0.2 |
| 15 | ~0.0 | ~0.0 | ~0.1 |
| 20 | ~0.0 | ~0.0 | ~0.05 |
| 25 | ~0.0 | ~0.0 | ~0.0 |
</details>

Figure 8.7: Three chi-square distributions with varying degrees of freedom.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">15Independence holds, since this is a randomized study. The expected counts are greater than 10. $\chi^{2}=\frac{(60-44.6)^{2}}{44.6}+$ (27−42.4)2 (87−102.4)2 (113−97.6)2 42.4 102.4 97.6 = 14.7.</span></small>

The $\chi ^ { 2 }$ statistic from a contingency table has a sampling distribution that approximately follows a $\chi ^ { 2 }$ distribution with degrees of freedom $d f = { \big ( } r - 1 { \big ) } { \big ( } c - 1 { \big ) }$ , where r is the number of rows and c is the number of columns. Either statistical software or a table can be used to calculate $p -$ values from the $\chi ^ { 2 }$ distribution. The **chi-square table** is partially shown in Figure 8.8, and a more complete table is presented in Appendix B.3 on page 468. This table is very similar to the t-table: each row provides values for distributions with different degrees of freedom, and a cut-off value is provided for specified tail areas. One important difference from the t-table is that the $\chi ^ { 2 }$ table only provides upper tail values.

<table><tr><td colspan="2">Upper tail</td><td>0.3</td><td>0.2</td><td>0.1</td><td>0.05</td><td>0.02</td><td>0.01</td><td>0.005</td><td>0.001</td></tr><tr><td rowspan="5">df</td><td>1</td><td>1.07</td><td>1.64</td><td>2.71</td><td>3.84</td><td>5.41</td><td>6.63</td><td>7.88</td><td>10.83</td></tr><tr><td>2</td><td>2.41</td><td>3.22</td><td>4.61</td><td>5.99</td><td>7.82</td><td>9.21</td><td>10.60</td><td>13.82</td></tr><tr><td>3</td><td>3.66</td><td>4.64</td><td>6.25</td><td>7.81</td><td>9.84</td><td>11.34</td><td>12.84</td><td>16.27</td></tr><tr><td>4</td><td>4.88</td><td>5.99</td><td>7.78</td><td>9.49</td><td>11.67</td><td>13.28</td><td>14.86</td><td>18.47</td></tr><tr><td>5</td><td>6.06</td><td>7.29</td><td>9.24</td><td>11.07</td><td>13.39</td><td>15.09</td><td>16.75</td><td>20.52</td></tr><tr><td rowspan="2"></td><td>6</td><td>7.23</td><td>8.56</td><td>10.64</td><td>12.59</td><td>15.03</td><td>16.81</td><td>18.55</td><td>22.46</td></tr><tr><td>7</td><td>8.38</td><td>9.80</td><td>12.02</td><td>14.07</td><td>16.62</td><td>18.48</td><td>20.28</td><td>24.32</td></tr></table>

Figure 8.8: A section of the chi-square table. A complete table is in Appendix B.3 on page 468.

## EXAMPLE 8.21

Calculate an approximate p-value for the mammogram data, given that the $\chi ^ { 2 }$ statistic equals 0.02. Assess whether the data provides convincing evidence of an association between screening group and breast cancer death.

The degrees of freedom in a $2 \times 2$ table is 1, so refer to the values in the first column of the probability table. The value 0.02 is less than 1.07, so the p-value is greater than 0.3. The data do not provide convincing evidence of an association between screening group and breast cancer death. This supports the conclusions from Example 8.14, where the p-value was calculated to be 0.8650 and is visualized in Figure 8.9.

![](images/page_404_chart_8.jpg)

<details>
<summary>area</summary>

| X | Y |
| --- | --- |
| 0 | >1.0 |
| 1 | ~0.2 |
| 2 | ~0.1 |
| 3 | ~0.05 |
| 4 | ~0.02 |
| 5 | ~0.01 |
</details>

Figure 8.9: The p-value for the mammogram data is shaded on the $\chi ^ { 2 }$ distribution with $d f = 1$ .The shaded area is to the right of $\mathtt { x } = 0 . 0 2$

## GUIDED PRACTICE 8.22

Calculate an approximate p-value for the HIV data. Assess whether the data provides convincing evidence of an association between treatment and outcome at the $\alpha = 0 . 0 1$ significance level.<sup>16</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^ { 1 6 } \mathrm { T h e } \; \chi ^ { 2 }$ statistic is 14.7. For degrees of freedom 1, the tail area beyond 14.7 is smaller than 0.001. There is evidence to suggest that treatment is not independent of outcome.</span></small>

## 8.3.4 Interpreting the results of a $\chi ^ { 2 }$ test

If the p-value from a $\chi ^ { 2 }$ test is small enough to provide evidence to reject the null hypothe sis of no association, it is important to explore the results further to understand direction of the observed association. This is done by examining the residuals, the standardized differences of the observed - expected, for each cell. Instead of using squared differences, the residuals are based on the differences themselves, and the standardizing or scaling factor is p<sub>expected</sub>. Calculating residuals can be particularly helpful for understanding the results from large tables.

For each cell in a table, the residual equals:

$$
\frac {\text {observed - expected}}{\sqrt {\text {expected}}}.
$$

Residuals with a large magnitude contribute the most to the $\chi ^ { 2 }$ statistic. If a residual is positive, the observed value is greater than the expected value, and vice versa for a negative residual.

## EXAMPLE 8.23

In the FAMuSS study introduced in Chapter 1, researchers measured a variety of demographic and genetic characteristics for about 1,300 participants, including data on race and genotype at a specific locus on the ACTN3 gene (Figure 8.10). Is there evidence of an association between genotype and race?

First, check the assumptions for applying a $\chi ^ { 2 }$ test. It is reasonable to assume independence, since it is unlikely that any participants were related to each other. None of the expected counts, as shown in Figure 8.11, are less than 5.

$H _ { 0 } ;$ Race and genotype are independent.

$H _ { A } \colon$ Race and genotype are not independent.

Let $\alpha = 0 . 0 5 .$

Calculate the $\chi ^ { 2 }$ statistic:

$$
\begin{array}{l} \chi^ {2} = \sum_ {\text {all cells}} \frac {(\text {observed} - \text {expected}) ^ {2}}{\text {expected}} \\ = \frac {(1 6 - 7 . 8 5) ^ {2}}{7 . 8 5} + \frac {(6 - 1 1 . 8 4) ^ {2}}{1 1 . 8 4} + \dots + \frac {(5 - 6 . 2 2) ^ {2}}{6 . 2 2} \\ = 1 9. 4. \\ \end{array}
$$

Calculate the p-value: for a table with 3 rows and 5 columns, the $\chi ^ { 2 }$ statistic is distributed with $(3 - 1)(5 - 1) = 8$ degrees of freedom. From the table, a $\chi ^ { 2 }$ value of 19.4 corresponds to a tail area between 0.01 and 0.02. Thus, there is sufficient evidence to reject the null hypothesis of independence between race and genotype.

The p-value can be obtained using the R function pchisq (pchisq(19.4, df = 8, lower.tail = FALSE)), which returns a value of 0.012861.

To further explore the differences in genotype distribution between races, calculate residuals for each cell (Figure 8.12). The largest residuals are in the first row; there are many more African Americans with the CC genotype than expected under independence, and fewer with the CT genotype than expected. The residuals in the second row indicate a similar trend for Asians, but with a less pronounced difference. These results suggest further directions for research; a future study could enroll a larger number of African American and Asian participants to examine whether the observed trend holds with a more representative sample. Geneticists might also be interested in exploring whether this genetic difference between populations has an observable phenotypic effect.

|  | CC | CT | TT | Sum |
| --- | --- | --- | --- | --- |
| African American | 16 | 6 | 5 | 27 |
| Asian | 21 | 18 | 16 | 55 |
| Caucasian | 125 | 216 | 126 | 467 |
| Hispanic | 4 | 10 | 9 | 23 |
| Other | 7 | 11 | 5 | 23 |
| Sum | 173 | 261 | 161 | 595 |

Figure 8.10: Observed counts for race and genotype data from the FAMuSS study.

|  | CC | CT | TT | Sum |
| --- | --- | --- | --- | --- |
| African Am | 7.85 | 11.84 | 7.31 | 27.00 |
| Asian | 15.99 | 24.13 | 14.88 | 55.00 |
| Caucasian | 135.78 | 204.85 | 126.36 | 467.00 |
| Hispanic | 6.69 | 10.09 | 6.22 | 23.00 |
| Other | 6.69 | 10.09 | 6.22 | 23.00 |
| Sum | 173.00 | 261.00 | 161.00 | 595.00 |

Figure 8.11: Expected counts for race and genotype data from the FAMuSS study.

|  | CC | CT | TT | Sum |
| --- | --- | --- | --- | --- |
| African Am | 2.91 | -1.70 | -0.85 | 0.00 |
| Asian | 1.25 | -1.25 | 0.29 | 0.00 |
| Caucasian | -0.93 | 0.78 | -0.03 | 0.00 |
| Hispanic | -1.04 | -0.03 | 1.11 | 0.00 |
| Other | 0.12 | 0.29 | -0.49 | 0.00 |
| Sum | 0.00 | 0.00 | 0.00 | 0.00 |

Figure 8.12: Residuals for race and genotype data from the FAMuSS study.

## EXAMPLE 8.24

In Guided Practice 8.22, the p-value was found to be smaller than 0.001, suggesting that treatment is not independent of outcome. Does the evidence suggest that infants should be given nevirapine or lopinarvir?

In a $2 \times 2$ table, it is relatively easy to directly compare observed and expected counts. For nevirapine, more infants than expected experienced virologic failure $( 60 > 44.6 ) ,$ , while fewer than expected reached a stable disease state $( 8 7 < 1 0 2 . 4 )$ . For lopinarvir, fewer infants than expected experienced virologic failure $(27 < 42.4)$ , and more infants than expected reached a stable disease state $( 113>97.6 )$ (Figure 8.13). The outcomes for infants on lopinarvir are better than for those on nevirapine; combined with the results of the significance test, the data suggest that lopinarvir is associated with better treatment outcomes.

|  | NVP | LPV | Total |
| --- | --- | --- | --- |
| Virologic Failure | 60 44.6 | 27 42.4 | 87 |
| Stable Disease | 87 102.4 | 113 97.6 | 200 |
| Total | 147 | 140 | 287 |

Figure 8.13: Observed and (expected) counts for the HIV study.

## GUIDED PRACTICE 8.25

Confirm the conclusions reached in Example 8.24 by analyzing the residuals.<sup>17</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^{17}R_{1,1}=\frac{(44.6{-}60)}{\sqrt{44.6}}=2.31;\;R_{1,2}=\frac{(42.4{-}27)}{\sqrt{27}}=-2.37;\;R_{2,1}=\frac{(87{-}102.4)}{\sqrt{102.4}}=-1.53;\;R_{2,2}=\frac{(113{-}97.6)}{\sqrt{97.6}}=1.56.$ The positive residuals for the upper left and lower right cells indicate that more infants than expected experienced virologic failure on NVP and stable disease on LPV; vice versa for the upper right and lower left cells. The larger magnitude of the residuals for the two NVP cells indicates that most of the discrepancy between observed and expected counts is for outcomes related to NVP.</span></small>

## GUIDED PRACTICE 8.26

Chapter 1 started with the discussion of a study examining whether exposure to peanut products reduce the rate of a child developing peanut allergies. Children were randomized either to the peanut avoidance or the peanut consumption group; at 5 years of age, each child was tested for peanut allergy using an oral food challenge (OFC). The results of the OFC are reproduced in Fig ure 8.14; failing the food challenge indicates an allergic reaction. Assess whether there is evidence for exposure to peanut allergy reducing the chance of developing peanut allergies.<sup>18</sup>

|  | FAIL OFC | PASS OFC | Sum |
| --- | --- | --- | --- |
| Peanut Avoidance | 36 | 227 | 263 |
| Peanut Consumption | 5 | 262 | 267 |
| Sum | 41 | 489 | 530 |

Figure 8.14: LEAP Study Results.

## 8.3.5 Fisher’s exact test

If sample sizes are too small, the $\chi ^ { 2 }$ distribution does not yield accurate p-values for assessing independence of the row and column variables in a table. When expected counts in a table are less than 10, **Fisher’s exact test** is often used to calculate exact levels of significance. This test is usually applied to 2 × 2 tables. It can be applied to larger tables, but the logic behind the test is complex and the calculations involved are computationally intensive, so this section covers only $2   \times   2$ tables.

Clostridium difficile is a bacterium that causes inflammation of the colon. Antibiotic treatment is typically not effective, particularly for patients who experience multiple recurrences of infection. Infusion of feces from healthy donors has been reported as an effective treatment for recurrent infection. A randomized trial was conducted to compare the efficacy of donor-feces infusion versus vancomycin, the antibiotic typically prescribed to treat C. difficile infection. The results of the trial are shown in Figure 8.15.<sup>19</sup> A brief calculation shows that all of the expected cell counts are less than 10, so the $\chi ^ { 2 }$ test should not be used as a test for association.

Under the null hypothesis, the probabilities of cure in the fecal infusion and vancomycin groups are equal; i.e., individuals in one group are just as likely to be cured as individuals in the other group. Suppose the probability that an individual is cured, given that he or she was assigned to the fecal infusion group, is $p _ { 1 }$ and the probability an individual is cured in the vancomycin group is $p _ { 2 }$ . Researchers were interested in testing the null hypothesis H0: $p _ { 1 } = p _ { 2 }$

|  | Cured | Uncured | Sum |
| --- | --- | --- | --- |
| Fecal Infusion | 13 | 3 | 16 |
| Vancomycin | 4 | 9 | 13 |
| Sum | 17 | 12 | 29 |

Figure 8.15: Fecal Infusion Study Results.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">18The assumptions for conducting a χ2test are satisfied. Calculate a χ2test statistic: 24.29. The associated p-value is 8.3×10<sup>−7</sup>. There is evidence to suggest that treatment group is not independent of outcome. Specifically, a residual analysis shows that in the peanut avoidance group, more children than expected failed the OFC; in the peanut consumption group, more children than expected passed the OFC.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">19<sub>These</sub> results correspond to the number of patients cured after the first infusion of donor feces and the number of patients cured in the vancomycin-alone group.</span></small>

The p-value is the probability of observing results as or more extreme than those observed in the study under the assumption that the null hypothesis is true. Previously discussed methods for significance testing have relied on calculating a test statistic associated with a defined sampling distribution, then obtaining p-values from tail areas on the distribution. Fisher’s exact test uses a similar approach, but introduces a new sampling distribution.

The p-value for Fisher’s exact test is calculated by adding together the individual conditional probabilities of obtaining each table that is as or more extreme than the one observed, under the null hypothesis and given that the marginal totals are considered fixed.

– When the row and column totals are held constant, the value of any one cell in the table determines the rest of the entries. For example, if the marginal sums in Figure 8.15 are known, along with the value in one cell (e.g., the upper right equals 3), it is possible to calculate the values in the other three cells. Thus, when marginal totals are considered fixed, each table represents a unique set of results.
– Extreme tables are those which contradict the null hypothesis of $p _ { 1 } = p _ { 2 }$ . In the fecal infusion group, under the null hypothesis of no difference in the population proportion cured, one would expect $\textstyle { \frac { 1 6 \times 1 7 } { 2 9 } } = 9 . 3 8$ cured individuals. The 13 observed cured individuals is extreme in the direction of more being cured than expected under the null hypothesis. An extreme result in the other direction would be, for instance, 1 cured patient in the fecal infusion group and 16 in the vancomycin group.

## EXAMPLE 8.27

Of the 17 patients cured, 13 were in the fecal infusion group and 4 were in the vancomycin group. Assume that the marginal totals are fixed (i.e., 17 patients were cured, 12 were uncured, and 16 patients were in the fecal infusion group, while 13 were in the vancomycin group). Enumerate all possible sets of results that are more extreme than what was observed, in the same direction.

The observed results show a case of $\hat { p } _ { 1 } > \hat { p } _ { 2 } ;$ results that are more extreme consist of cases where more than 13 cured patients were in the fecal infusion group. Under the assumption that the total number of cured patients is constant at 17 and that only 16 patients were assigned to the fecal infusion group (out of 29 patients total), more extreme results are represented by cases where 14, 15, or 16 cured patients were in the fecal infusion group. The following tables illustrate the unique combinations of values for the 4 table cells corresponding to those extreme results.

<table><tr><td></td><td>Cured</td><td>Uncured</td><td>Sum</td></tr><tr><td>Fecal Infusion</td><td>14</td><td>2</td><td>16</td></tr><tr><td>Vancomycin</td><td>3</td><td>10</td><td>13</td></tr><tr><td>Sum</td><td>17</td><td>12</td><td>29</td></tr><tr><td colspan="4"></td></tr><tr><td></td><td>Cured</td><td>Uncured</td><td>Sum</td></tr><tr><td>Fecal Infusion</td><td>15</td><td>1</td><td>16</td></tr><tr><td>Vancomycin</td><td>2</td><td>11</td><td>13</td></tr><tr><td>Sum</td><td>17</td><td>12</td><td>29</td></tr><tr><td colspan="4"></td></tr><tr><td></td><td>Cured</td><td>Uncured</td><td>Sum</td></tr><tr><td>Fecal Infusion</td><td>16</td><td>0</td><td>16</td></tr><tr><td>Vancomycin</td><td>1</td><td>12</td><td>13</td></tr><tr><td>Sum</td><td>17</td><td>12</td><td>29</td></tr></table>

## Calculating a one-sided p-value

Suppose that researchers were interested in testing the null hypothesis against the one-sided alternative, $H _ { A } : p _ { 1 } > p _ { 2 }$ . To calculate the one-sided p-value, sum the probabilities of each table representing results as or more extreme than those observed; specifically, sum the probabilities of observing Figure 8.15 and the tables in Example 8.27.

|  | Cured | Uncured | Sum |
| --- | --- | --- | --- |
| Fecal Infusion | a | b | a+b |
| Vancomycin | c | d | c+d |
| Sum | a+c | b+d | n |

Figure 8.16: General Layout of Data in Fecal Infusion Study.

The probability of observing a table with cells $a , b , c , d$ given fixed marginal totals $a + b ,   c + d ,$ $a + c ,$ and $b + d$ follows the hypergeometric distribution. The hypergeometric distribution was introduced in Section 3.5.3.

$$
P (a, b, c, d) = \mathrm{HGeom} (a + b, c + d, a + c) = \frac {\binom {a + b} {a} \binom {c + d} {c}}{\binom {n} {a + c}} = \frac {(a + b) ! (c + d) ! (a + c) ! (b + d) !}{a ! b ! c ! d ! n !}.
$$

## EXAMPLE 8.28

Calculate the probability of observing Figure 8.15, assuming the margin totals are fixed.

$$
P (1 3, 3, 4, 9) = \frac {\binom {1 6} {1 3} \binom {1 3} {4}}{\binom {2 9} {1 7}} = \frac {1 6 ! 1 3 ! 1 7 ! 1 2 !}{1 3 ! 3 ! 4 ! 9 ! 2 9 !} = 7. 7 1 \times 1 0 ^ {- 3}.
$$

The value 0.0077 represents the probability of observing 13 cured patients out of 16 individuals in the fecal infusion group and 1 cured in the vancomycin group, given that there are a total of 29 patients and 17 were cured overall.

## EXAMPLE 8.29

Evaluate the statistical significance of the observed data in Figure 8.15 using the one-sided alternative $H _ { A } : p _ { 1 } > p _ { 2 }$

Calculate the probability of the tables from Example 8.27. Generally, the formula for these tables is

$$
P (a, b, c, d) = \frac {\binom {a + b} {a} \binom {c + d} {c}}{\binom {n} {a + c}} = \frac {\binom {1 6} {a} \binom {1 3} {c}}{\binom {2 9} {1 7}},
$$

since the marginal totals from Figure 8.15 are fixed. The value a ranges from 14, 15, 16, while c ranges from 3, 2, 1.

$$
P (1 4, 2, 3, 1 0) = \frac {\binom {1 6} {1 4} \binom {1 3} {3}}{\binom {2 9} {1 7}} = 6. 6 1 \times 1 0 ^ {- 4}
$$

$$
P (1 5, 1, 2, 1 1) = \frac {\binom {1 6} {1 5} \binom {1 3} {2}}{\binom {2 9} {1 7}} = 2. 4 0 \times 1 0 ^ {- 5}
$$

$$
P (1 6, 0, 1, 1 2) = \frac {\binom {1 6} {1 6} \binom {1 3} {1}}{\binom {2 9} {1 7}} = 2. 5 1 \times 1 0 ^ {- 7}
$$

The probability of the observed table is $7 . 7 1 \times 1 0 ^ { - 3 }$ , as calculated in the previous example.

The one-sided p-value is the sum of these table probabilities: $( 7 . 7 1 \times 1 0 ^ { - 3 } ) + ( 6 . 6 1 \times 1 0 ^ { - 4 } ) + ( 2 . 4 0 \times$ $1 0 ^ { - 5 } ) + ( 2 . 5 1 \times 1 0 ^ { - 7 } ) = 0 . 0 0 8 4$

The results are significant at the $\alpha = 0 . 0 5$ significance level. There is evidence to support the one sided alternative that the proportion of cured patients in the fecal infusion group is higher than the proportion of cured patients in the vancomycin group. However, it is important to note that two-sided alternatives are the standard in medical literature. Conducting a two-sided test would be especially desirable when evaluating a treatment which lacks randomized trials supporting its efficacy, such as donor-feces infusion.

## Calculating a two-sided p-value

There are various methods for calculating a two-sided p-value in the Fisher’s exact test setting. When the test is calculated by hand, the most common way to calculate a two-sided p-value is to double the smaller of the one-sided p-values. One other common method used by various statisti cal computing packages such as R is to classify "more extreme" tables as all tables with probabilities less than that of the observed table, in both directions. The two-sided p-value is the sum of proba bilities for the qualifying tables. That approach is illustrated in the next example.

## EXAMPLE 8.30

Evaluate the statistical significance of the observed data in Figure 8.15 using the two-sided alternative $H _ { A } : p _ { 1 } \neq p _ { 2 }$

Identify tables that are more extreme in the other direction of the observed result, i.e. where the proportion of cured patients in the vancomycin group are higher than in the fecal infusion group. Start with the most extreme cases and calculate probabilities until a table has a p-value higher than $7 . 7 1 \times 1 0 ^ { - 3 }$ , the probability of the observed table.

The most extreme result in the $\hat { p } _ { 1 } < \hat { p } _ { 2 }$ direction would be if all patients in the vancomycin group were cured; then 13 of the cured patients would be in the vancomycin group and 4 would be in the fecal transplant group. This table has probability $3 . 5 \times 1 0 ^ { - 5 }$

|  | Cured | Uncured | Sum |
| --- | --- | --- | --- |
| Fecal Infusion | 4 | 12 | 16 |
| Vancomycin | 13 | 0 | 13 |
| Sum | 17 | 12 | 29 |

Continue enumerating tables by decreasing the number of cured patients in the vancomycin group. The table with 5 cured patients in the fecal infusion group has probability $1 . 0 9 \times 1 0 ^ { - 3 }$

|  | Cured | Uncured | Sum |
| --- | --- | --- | --- |
| Fecal Infusion | 5 | 11 | 16 |
| Vancomycin | 12 | 1 | 13 |
| Sum | 17 | 12 | 29 |

The table with 6 cured patients in the fecal infusion group has probability 0.012. This value is greater than $7 . 7 1 \times 1 0 ^ { - 3 }$ , so it will not be part of the sum to calculate the two-sided p-value.

|  | Cured | Uncured | Sum |
| --- | --- | --- | --- |
| Fecal Infusion | 6 | 10 | 16 |
| Vancomycin | 11 | 2 | 13 |
| Sum | 17 | 12 | 29 |

As calculated in the previous example, the one-sided p-value is 0.0084. Thus, the two-sided p-value for these data equals $0 . 0 0 8 4 + ( 3 . 5 \times 1 0 ^ { - 5 } ) + ( 1 . 0 9 \times 1 0 ^ { - 3 } ) = 0 . 0 0 9 5$ . The results are significant at the $\alpha = 0 . 0 1$ significance level, and there is evidence to support the efficacy of donor-feces infusion as a treatment for recurrent C. difficile infection.

## 8.4 Chi-square tests for the fit of a distribution

The $\chi ^ { 2 }$ test can also be used to examine the appropriateness of hypothesized distribution for a dataset, most commonly when a set of observations falls naturally into categories as in the examples discussed in this section. As with testing in the two-way table setting, expected counts are calculated based on the assumption that the hypothesized distribution is correct, and the statistic is based on the discrepancies between observed and expected counts. The $\chi ^ { 2 }$ sampling distribution for the test statistic is reasonably accurate when each expected count is at least 5 and follows a $\chi ^ { 2 }$ distribution with k − 1 degrees of freedom, where k is the number of categories. Some guidelines recommend that no more than 1/5 of the cells have expected counts less than 5, but the stricter requirement that all cells have expected counts greater than 5 is safer.

When used in this setting, the $\chi ^ { 2 }$ test is often called a **‘goodness-of-fit’ test**, a term that is often misunderstood. Small p-values of the test suggest evidence that a hypothesized distribution is not a good model, but non-significant p-values do not imply that the hypothesized distribution is the best model for the data, or even a good one. In the logic of hypothesis testing, failure to reject a null hypothesis cannot be viewed as evidence that the null hypothesis is true.

## EXAMPLE 8.31

The participants in the FAMuSS study were volunteers at a university, and so did not come from a random sample of the US population. The participants may not be representative of the general United States population. The $\chi ^ { 2 }$ test can be used to test the null hypothesis that the participants are racially representative of the general population. Figure 8.17 shows the number observed by racial category in FAMuSS and the proportions of the US population in each of those categories.<sup>20</sup>

Under the null hypothesis, the sample proportions should equal the population proportions. For example, since African Americans are 0.128 of the general proportion, (0.128)(595) = 76.16 African Americans would be expected in the sample. The rest of the expected counts are shown in Fig ure 8.18.

Since each expected count is greater than or equal to 5, the $\chi ^ { 2 }$ distribution can be used to calculate a p-value for the test.

$$
\begin{array}{l} \chi^ {2} = \sum_ {\text {all cells}} \frac {(\text {observed - expected}) ^ {2}}{\text {expected}} \\ = \frac {(2 7 - 7 6 . 1 6) ^ {2}}{7 6 . 1 6} + \frac {(5 5 - 5 . 9 5) ^ {2}}{5 . 9 5} + \frac {(4 6 7 - 4 7 8 . 3 8) ^ {2}}{4 7 8 . 3 8} + \frac {(4 6 - 3 4 . 5 1) ^ {2}}{3 4 . 5 1} \\ = 4 4 0. 1 8. \\ \end{array}
$$

There are 3 degrees of freedom, since k = 4. The $\chi ^ { 2 }$ statistic is extremely large, and the associated tail area is smaller than 0.001. There is more than sufficient evidence to reject the null hypothesis that the sample is representative of the general population. A comparison of the observed and expected values (or the residuals) indicates that the largest discrepancy is with the over-representation of Asian participants.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">20<sub>The</sub> US Census Bureau considers Hispanic as a classification separate from race, on the basis that Hispanic individuals can be any race. In order to facilitate the comparison with the FAMuSS data, participants identified as "Hispanic" have been merged with the "Other" category.</span></small>

| Race | African American | Asian | Caucasian | Other | Total |
| --- | --- | --- | --- | --- | --- |
| FAMuSS | 27 | 55 | 467 | 46 | 595 |
| US Census | 0.128 | 0.01 | 0.804 | 0.058 | 1.00 |

Figure 8.17: Representation by race in the FAMuSS study versus the general population.

| Race | African American | Asian | Caucasian | Other | Total |
| --- | --- | --- | --- | --- | --- |
| Observed | 27 | 55 | 467 | 46 | 595 |
| Expected | 76.16 | 5.95 | 478.38 | 34.51 | 595 |

Figure 8.18: Actual and expected counts in the FAMuSS data.

## EXAMPLE 8.32

According to Mendelian genetics, alleles segregate independently; if an individual is heterozygous for a gene and has alleles A and B, then the alleles have an equal chance of being passed to an offspring. Under this framework, if two individuals with genotype AB mate, then their offspring are expected to exhibit a 1:2:1 genotypic ratio; 25% of the offspring will be AA, 50% will be AB, and 50% will be BB. The term "segregation distortion" refers to a deviation from expected Mendelian frequencies.

At a specific gene locus in the plant Arabidopsis thaliana, researchers have observed 84 AA indi viduals, 233 AB individuals, and 134 BB individuals. Is there evidence of segregation disorder at this locus? Conduct the test at $\alpha = 0 . 0 0 0 1$ to account for multiple testing, since the original study examined approximately 250 locations across the genome.

The Mendelian proportions are 25%, 50%, and 25%. Thus, the expected counts in a group of 451 individuals are: 112.75 AA, 225.50 AB, and 112.75 BB. No expected count is less than 5.

$$
\begin{array}{l} \chi^ {2} = \sum_ {\text {all cells}} \frac {(\text {observed} - \text {expected}) ^ {2}}{\text {expected}} \\ = \frac {(8 4 - 1 1 2 . 7 5) ^ {2}}{1 1 2 . 7 5} + \frac {(2 3 3 - 2 2 5 . 5 0) ^ {2}}{2 2 5 . 5 0} + \frac {(1 3 4 - 1 1 2 . 7 5) ^ {2}}{1 1 2 . 7 5} \\ = 1 1. 5 9. \\ \end{array}
$$

There are 2 degrees of freedom, since k = 3. The p-value is between 0.005 and 0.001, which is greater than $\alpha = 0 . 0 0 0 1$ . There is insufficient evidence to reject the null hypothesis that the offspring ratios correspond to expected Mendelian frequencies; i.e., there is not evidence of segregation distortion at this locus.

## 8.5 Outcome-based sampling: case-control studies

## 8.5.1 Introduction

The techniques so far in this chapter have often relied on the assumption that the data were collected using random sampling from a population. When cases come from a random sample, the sample proportion of observations with a particular outcome should accurately estimate the population proportion, given that the sample size is large enough. When studying rare outcomes, however, moderate sized samples may contain few or none of the outcomes. Persistent pulmonary hypertension of the newborn (PPHN) is a dangerous condition in which the blood vessels in the lungs of a newborn do not relax immediately after birth, leading to inadequate oxygenation. The condition is rare, occurring in about 1.9 per 1,000 live births, so it is difficult to study using random sampling. In the early 2000s, anecdotal evidence began to accumulate that the risk of the condi tion might be increased if the mother of the newborn had been taking a particular medication for depression, a selective serotonin reuptake inhibitor (SSRI) during the third trimester of pregnancy or even as early as during week 20 of the pregnancy.

One design for studying the issue would enroll two cohorts of women, one in which women were taking SSRIs for depression and one in which they were not. However, if the chance of PPHN was 1.9/1,000 in newborns of a control cohort of 1,000 women, then the probability of observing no cases of PPHN is about 0.15. If the probability of PPHN is elevated among infants born to women taking SSRIs, such as to 3.0/1,000, the chance of observing no cases among 1,000 women is approximately 0.05. Precise measures of the probability of PPHN occurring would require very large cohorts.

An alternative design for studies like this reverses the sampling scheme so that the two cohorts are determined by outcome, rather than exposure; a cohort with the condition and a cohort without the condition are sampled, then exposure to a possible cause is recorded. To apply this design for studying PPHN, a registry of live births could be used to sort births by presence or absence of PPHN. The number in each group in which the mother had been taking SSRIs could then be recorded (based on medical records). Such a design would have the advantage of sufficient numbers of cases with and without PPHN, but it has other limitations which will be discussed later in this section. Traditionally, these studies have been called case-control studies because of the original sampling of individuals with and without a condition. More generally, it is an example of outcomedependent sampling.