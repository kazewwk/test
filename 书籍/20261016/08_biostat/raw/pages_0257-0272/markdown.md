## 5.4 Power calculations for a difference of means

Designing a study often involves many complex issues; perhaps the most important statistical issue in study design is the choice of an appropriate sample size. The **power** of a statistical test is the probability that the test will reject the null hypothesis when the alternative hypothesis is true; sample sizes are chosen to make that probability sufficiently large, typically between 80% and 90%.

Two competing considerations arise when choosing a sample size. The sample size should be sufficiently large to allow for important group differences to be detected in a hypothesis test. Practitioners often use the term ‘detecting a difference’ to mean correctly rejecting a null hypothesis, i.e., rejecting a null hypothesis when the alternative is true. If a study is so small that detecting a statistically significant difference is unlikely even when there are potentially important differences, enrolling participants might be unethical, since subjects could potentially be exposed to a dangerous experimental treatment. However, it is also unethical to conduct studies with an overly large sample size, since more participants than necessary would be exposed to an intervention with uncertain value. Additionally, collecting data is typically expensive and time consuming; it would be a waste of valuable resources to design a study with an overly large sample size.

This section begins by illustrating relevant concepts in the context of a hypothetical clinical trial, where the goal is to calculate a sufficient sample size for being 80% likely to detect practically important effects.<sup>17</sup> Afterwards, formulas are provided for directly calculating sample size, as well as references to software that can perform the calculations.

## 5.4.1 Reviewing the concepts of a test

## EXAMPLE 5.13

A company would like to run a clinical trial with participants whose systolic blood pressures are between 140 and 180 mmHg. Suppose previously published studies suggest that the standard deviation of patient blood pressures will be about 12 mmHg, with an approximately symmetric distribution.<sup>18</sup> What would be the approximate standard error for $\overline { { x } } _ { \mathrm { t r m t } } - \overline { { x } } _ { \mathrm { c t r l } }$ if 100 participants were enrolled in each treatment group?

The standard error is calculated as follows:

$$
S E _ {\overline {{x}} _ {\mathrm{trmt}} - \overline {{x}} _ {\mathrm{ctrl}}} = \sqrt {\frac {s _ {\mathrm{trmt}} ^ {2}}{n _ {\mathrm{trmt}}} + \frac {s _ {\mathrm{ctrl}} ^ {2}}{n _ {\mathrm{ctrl}}}} = \sqrt {\frac {1 2 ^ {2}}{1 0 0} + \frac {1 2 ^ {2}}{1 0 0}} = 1. 7 0.
$$

This may be an imperfect estimate of $S E _ { \overline { { x } } _ { \mathrm { t r m t } } - \overline { { x } } _ { \mathrm { c t r l } } } ,$ , since the standard deviation estimate of 12 mmHg from prior data may not be correct. However, it is sufficient for getting started, and making an assumption like this is often the only available option.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">17<sub>While</sub> sample size planning is also important for observational studies, those techniques are not discussed here.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">18<sub>In</sub> many studies like this one, each participant’s blood pressure would be measured at the beginning and end of the study, and the outcome measurement for the study would be the average difference in blood pressure in each of the treatment groups. For this hypothetical study, we assume for simplicity that blood pressure is measured at only the end of the study, and that the randomization ensures that blood pressures at the beginning of the study are equal (on average) between the two groups.</span></small>

Since the degrees of freedom are greater than 30, the distribution of $\overline { { x } } _ { \mathrm { t r m t } } - \overline { { x } } _ { \mathrm { c t r l } }$ will be approximately normal. Under the null hypothesis, the mean is 0 and the standard deviation is 1.70 (from the standard error).

![](images/page_257_chart_3.jpg)

<details>
<summary>violin</summary>

| X | Y |
| --- | --- |
| -9 | ~0 |
| -6 | ~0.05 |
| -3 | ~0.4 |
| 0 | 1 |
| 3 | ~0.4 |
| 6 | ~0.05 |
| 9 | ~0 |
</details>

Figure 5.19: Null distribution for the t-statistic in Example 5.14.

## EXAMPLE 5.14

For what values of $\overline { { x } } _ { \mathrm { t r m t } } - \overline { { x } } _ { \mathrm { c t r l } }$ would the null hypothesis be rejected, using $\alpha = 0 . 0 5 ?$

If the observed difference is in the far left or far right tail of the null distribution, there is sufficient evidence to reject the null hypothesis. For $\alpha = 0 . 0 5 ,   H _ { 0 }$ is rejected if the difference is in the lower 2.5% or upper 2.5% tail:

**Lower 2.5%:** For the normal model, this is 1.96 standard errors below 0, so any difference smaller than $-1.96 \times 1.70 = -3.332$ mmHg.

**Upper 2.5%:** For the normal model, this is 1.96 standard errors above 0, so any difference larger than $1 . 9 6 \times 1 . 7 0 = 3 . 3 3 2 \; \mathrm { m m H g } .$

The boundaries of these **rejection regions** are shown below. Note that if the new treatment is effective, mean blood pressure should be lower in the treatment group than in the control group; i.e., the difference should be in the lower tail.

![](images/page_257_chart_11.jpg)

<details>
<summary>violin</summary>

| Region | Description |
| --- | --- |
| Left | Reject H0 |
| Center | Do not reject H0 |
| Right | Reject H0 |
</details>

The next step is to perform some hypothetical calculations to determine the probability of rejecting the null hypothesis if the alternative hypothesis were true.

## 5.4.2 Computing the power for a 2-sample test

If there is a real effect from an intervention, and the effect is large enough to have practical value, the probability of detecting that effect is referred to as the **power**. Power can be computed for different sample sizes or different effect sizes.

There is no easy way to define when an effect size is large enough to be of value; this is not a statistical issue. For example, in a clinical trial, the scientifically significant effect is the incremental value of the intervention that would justify changing current clinical recommendations from an existing intervention to a new one. In such a setting, the effect size is usually determined from long discussions between the research team and study sponsors.

Suppose that for this hypothetical blood pressure medication study, the researchers are interested in detecting any effect on blood pressure that is 3 mmHg or larger than the standard medication. Here, 3 mmHg is the minimum **population e**ff**ect size** of interest.

## EXAMPLE 5.15

Suppose the study proceeded with 100 patients per treatment group and the new drug does reduce average blood pressure by an additional 3 mmHg relative to the standard medication. What is the probability of detecting this effect?

Determine the sampling distribution for $\overline { { x } } _ { \mathrm { t r m t } }   -   \overline { { x } } _ { \mathrm { c t r l } }$ when the true difference is −3 mmHg; this has the same standard deviation of 1.70 as the null distribution, but the mean is shifted 3 units to the left. Then, calculate the fraction of the distribution for $\overline { { x } } _ { \mathrm { t r m t } } - \overline { { x } } _ { \mathrm { c t r l } }$ that falls within the rejection region for the null distribution, as shown in Figure 5.20.

The probability of being in the left side of the rejection region $(x < -3.332)$ can be calculated by converting to a Z-score and using either the normal probability table or statistical software.<sup>19</sup>

$$
Z = \frac {- 3 . 3 3 2 - (- 3)}{1 . 7} = - 0. 2 0 \quad \rightarrow \quad P (Z \leq - 0. 2 0) = 0. 4 2 0 7.
$$

The power for the test is about 42% when $\mu _ { \mathrm { t r m t } } - \mu _ { \mathrm { c t r l } } = - 3$ mm/Hg and each group has a sample size of 100.

![](images/page_258_chart_12.jpg)

<details>
<summary>violin</summary>

| Category | Distribution with \(\mu_trmt\) - \(\mu_ctrl\) = -3 (Peak) | Null distribution (Peak) |
| --- | --- | --- |
| X-axis range | -9~9 | -3~3 |
</details>

Figure 5.20: The rejection regions are outside of the dotted lines. Recall that the boundaries for $\alpha = 0 . 0 5$ were calculated to be ±3.332 mmHg.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">19<sub>The</sub> probability of being in the right side of the rejection region is negligible and can be ignored.</span></small>

## 5.4.3 Determining a proper sample size

The last example demonstrated that with a sample size of 100 in each group, there is a prob ability of about 0.42 of detecting an effect size of 3 mmHg. If the study were conducted with this sample size, even if the new medication reduced blood pressure by 3 mmHg compared to the control group, there is a less than 50% chance of concluding that the medication is beneficial. Studies with low power are often inconclusive, and there are important reasons to avoid such a situation:

– Participants were subjected to a drug for a study that may have little scientific value.
– The company may have invested hundreds of millions of dollars in developing the new drug, and may now be left with uncertainty about its potential.
– Another clinical trial may need to be conducted to obtain a more conclusive answer as to whether the drug does hold any practical value, and that would require substantial time and expense.

To ensure a higher probability of detecting a clinically important effect, a larger sample size should be chosen. What about a study with 500 patients per group?

## GUIDED PRACTICE 5.16

Calculate the power to detect a change of -3 mmHg using a sample size of 500 per group. Recall that the standard deviation of patient blood pressures was expected to be about 12 mmHg.<sup>20</sup>

(a) Determine the standard error.
(b) Identify the null distribution and rejection regions, as well as the alternative distribution when $\mu _ { t r m t } - \mu _ { c t r l } = - 3 .$
(c) Compute the probability of rejecting the null hypothesis.

With a sample size of 500 per group, the power of the test is much larger than necessary. Not only does this lead to a study that would be overly expensive and time consuming, it also exposes more patients than necessary to the experimental drug.

Sample sizes are generally chosen such that power is around 80%, although in some cases 90% is the target. Other values may be reasonable for a specific context, but 80% and 90% are most commonly chosen as a good balance between high power and limiting the number of patients exposed to a new treatment (as well as reducing experimental costs).

20(a) The standard error will now be $SE = \sqrt{\frac{12^2}{500} + \frac{12^2}{500}} = 0.76.$ (b) The null distribution, rejection boundaries, and alternative distribution are shown below. The rejection regions are the areas outside the two dotted lines at xtrmt − xctrl ± 0.76 × 1.96 = ±1.49.

![](images/page_259_chart_18.jpg)

<details>
<summary>violin</summary>

| Category | Distribution with \(\mu_trmt\) - \(\mu_ctrl\) = -3 (Peak) | Null distribution (Peak) |
| --- | --- | --- |
| Peak X-value | ~-3 | 0 |
</details>

(c) Compute the Z-score and find the tail area, Z =−1.49−(−3) 0.76 = 1.99 → P (Z ≤ 1.99) = 0.9767, which is the power of the test for a difference of 3 mmHg. With 500 patients per group, the study would be 97.7% likely to detect an effect size of 3 mmHg.

## EXAMPLE 5.17

Identify the sample size that would lead to a power of 80%.

The Z-score that defines a lower tail area of 0.80 is about $Z = 0 . 8 4 .$ . In other words, 0.84 standard errors from -3, the mean of the alternative distribution.

![](images/page_260_chart_5.jpg)

<details>
<summary>violin</summary>

| Metric | Value |
| --- | --- |
| Distribution with \(\mu_trmt\) - \(\mu_ctrl\) | -3 |
| Null distribution (SE) | 1.96 |
| Distribution with \(\mu_trmt\) - \(\mu_ctrl\) | -3 |
| Distribution with \(\mu_trmt\) - \(\mu_ctrl\) (SE) | 0.84 |
</details>

For $\alpha = 0 . 0 5 ,$ the rejection region always extends 1.96 standard errors from 0, the center of the null distribution.

The distance between the centers of the null and alternative distributions can be expressed in terms of the standard error:

$$
(0. 8 4 \times S E) + (1. 9 6 \times S E) = 2. 8 \times S E.
$$

This quantity necessarily equals the minimum effect size of interest, 3 mmHg, which is the distance between -3 and 0. It is then possible to solve for n:

$$
\begin{array}{l} 3 = 2. 8 \times S E \\ 3 = 2. 8 \times \sqrt {\frac {1 2 ^ {2}}{n} + \frac {1 2 ^ {2}}{n}} \\ n = \frac {2 . 8 ^ {2}}{3 ^ {2}} \times \left(1 2 ^ {2} + 1 2 ^ {2}\right) = 2 5 0. 8 8 \\ \end{array}
$$

The study should enroll at least 251 patients per group for 80% power. Note that sample size should always be rounded up in order to achieve the desired power. Even if the calculation had yielded a number closer to 250 (e.g., 250.25), the study should still enroll 251 patients per grou, since having 250 patients per group would result in a power lower than 80%.

## GUIDED PRACTICE 5.18

Suppose the targeted power is 90% and $\alpha = 0 . 0 1$ . How many standard errors should separate the centers of the null and alternative distributions, where the alternative distribution is centered at the minimum effect size of interest? Assume the test is two-sided.<sup>21</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">21<sub>Find</sub> the Z-score such that 90% of the distribution is below it: Z = 1.28. Next, find the cutoffs for the rejection regions: ±2.58. Thus, the centers of the null and alternative distributions should be about 1.28 + 2.58 = 3.86 standard errors apart.</span></small>

Figure 5.21 shows the power for sample sizes from 20 participants to $^ { 5 , 0 0 0 }$ participants when $\alpha = 0 . 0 5$ and the true difference is -3 mmHg. While power increases with sample size, having more than 250-300 participants provides little additional value towards detecting an effect.

![](images/page_261_chart_3.jpg)

<details>
<summary>line</summary>

| Sample Size Per Group | Power |
| --- | --- |
| 20 | ~0.12 |
| 50 | ~0.25 |
| 100 | ~0.45 |
| 200 | ~0.70 |
| 500 | ~0.98 |
| 1000 | 1.0 |
| 2000 | 1.0 |
| 5000 | 1.0 |
</details>

Figure 5.21: The curve shows the power for different sample sizes in the context of the blood pressure example when the true difference is -3.

## 5.4.4 Formulas for power and sample size

The previous sections have illustrated how power and sample size can be calculated from first principles, using the fundamental ideas behind distributions and testing. In practice, power and sample size calculations are so important that statistical software should be the method of choice; there are many commercially available and public domain programs for performing such calculations. However, hand calculations using formulas can provide quick estimates in the early stages of planning a study.

Use the following formula to calculate sample size for comparing two means, assuming each group will have n participants:

$$
n = \frac {(\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}) (z _ {1 - \alpha / 2} + z _ {1 - \beta}) ^ {2}}{\Delta^ {2}}.
$$

In this formula:

$- ~ \mu _ { 1 } , \mu _ { 2 } , \sigma _ { 1 }$ , and $\sigma _ { 2 }$ are the population means and standard deviations of the two groups.
$\Delta = \mu _ { 1 } - \mu _ { 2 }$ is the minimally important difference that investigators wish to detect.
– The null and alternative hypotheses are $H _ { 0 } : \Delta = 0 \; ( \mathrm { i . e . }$ , no difference between the means) and $H _ { A } : \Delta \neq 0 ,$ i.e., a two-sided alternative.
– The two-sided significance level is $\alpha$ , and $z _ { 1 - \alpha / 2 }$ is the point on a standard normal distribution with area $1 - \alpha / 2$ to its left and $\alpha / 2$ area to its right.
$\beta$ is the probability of incorrectly failing to reject $H _ { 0 }$ for a specified value of $\Delta ;   1 - \beta$ is the power. The value $z _ { 1 - \beta }$ is the point on a standard normal distribution with area $1 - \beta$ to its left.

For a study with sample size n per group, where $Z$ is a normal random variable with mean 0 and standard deviation 1, power is given by:

$$
\text {Power} = P \left(Z <   - z _ {1 - \alpha / 2} + \frac {\Delta}{\sqrt {\sigma_ {1} ^ {2} / n + \sigma_ {2} ^ {2} / n}}\right).
$$

These formulas could have been used to do the earlier power and sample size calculations for the hypothetical study of blood pressure lowering medication. To calculate the sample size needed for 80% power in detecting a change of 3 mmHg, $\alpha = 0 . 0 5 ,   1 - \beta = 0 . 8 0 ,   \Delta = 3$ mmHg, and $\sigma _ { 1 } = \sigma _ { 2 } = 1 2$ mmHg. The formula yields a sample size n per group of

$$
n = \frac {(1 2 ^ {2} + 1 2 ^ {2}) (1 . 9 6 + 0 . 8 4) ^ {2}}{(- 3 . 0) ^ {2}} = 2 5 0. 8 8,
$$

which can be rounded up to 251.

The formula for power can be used to verify the sample size of 251:

$$
\begin{array}{l} \text {Power} = P \left(Z <   - 1. 9 6 + \frac {3}{\sqrt {1 2 ^ {2} / 2 5 1 + 1 2 ^ {2} / 2 5 1}}\right) \\ = P (Z <   1. 2 5) \\ = 0. 8 5. \\ \end{array}
$$

The calculated power is slightly larger than 80% because of the rounding to 251.

The sample size calculations done before any data are collected are one of the most critical aspects of conducting a study. If an analysis is done incorrectly, it can be redone once the error is discovered. However, if data were collected for a sample size that is either too large or too small, it can be impossible to correct the error, especially in studies with human subjects. As a result, sample size calculations are nearly always done using software. For two-sample t-tests, the R function power.t.test is both freely available and easy to use.

## 5.5 Comparing means with ANOVA

In some settings, it is useful to compare means across several groups. It might be tempting to do pairwise comparisons between groups; for example, if there are three groups $( A , B , C )$ , why not conduct three separate t-tests (A vs. B, A vs. C, B vs. C)? Conducting multiple tests on the same data increases the rate of Type I error, making it more likely that a difference will be found by chance, even if there is no difference among the population means. Multiple testing is discussed further in Section 5.5.3.

Instead, the methodology behind a t-test can be generalized to a procedure called **analysis of variance (ANOVA)**, which uses a single hypothesis test to assess whether the means across several groups are equal. Strong evidence favoring the alternative hypothesis in ANOVA is described by unusually large differences among the group means.

$H _ { 0 } ;$ The mean outcome is the same across all k groups. In statistical notation, $\mu _ { 1 } = \mu _ { 2 } = \cdots = \mu _ { k }$ where $\mu _ { i }$ represents the mean of the outcome for observations in category i.

$H _ { A } \colon$ At least one mean is different.

There are three conditions on the data that must be checked before performing ANOVA: 1) observations are independent within and across groups, 2) the data within each group are nearly normal, and 3) the variability across the groups is about equal.

## EXAMPLE 5.19

Examine Figure 5.22. Compare groups I, II, and III. Is it possible to visually determine if the differences in the group centers is due to chance or not? Now compare groups IV, V, and VI. Do the differences in these group centers appear to be due to chance?

It is difficult to discern a difference in the centers of groups I, II, and III, because the data within each group are quite variable relative to any differences in the average outcome. However, there appear to be differences in the centers of groups IV, V, and VI. For instance, group V appears to have a higher mean than that of the other two groups. The differences in centers for groups IV, V, and VI are noticeable because those differences are large relative to the variability in the individual observations within each group.

![](images/page_263_chart_11.jpg)

<details>
<summary>scatter</summary>

| Category | Outcome (range) |
| --- | --- |
| I | -1.2~4.6 |
| II | -0.4~3.7 |
| III | -1.1~3.9 |
| IV | 0.4~2.4 |
| V | 1.3~2.7 |
| VI | 0.7~2.4 |
</details>

Figure 5.22: Side-by-side dot plot for the outcomes for six groups.

## 5.5.1 Analysis of variance (ANOVA) and the F-test

The famuss dataset was introduced in Chapter 1, Section 1.2.2. In the FAMuSS study, researchers examined the relationship between muscle strength and genotype at a location on the ACTN3 gene. The measure for muscle strength is percent change in strength in the non-dominant arm (ndrm.ch). Is there a difference in muscle strength across the three genotype categories (CC, CT, TT)?

## GUIDED PRACTICE 5.20

The null hypothesis under consideration is the following: $\mu _ { \mathtt { C C } }   =   \mu _ { \mathtt { C T } }   =   \mu _ { \mathtt { T T } }$ . Write the null and corresponding alternative hypotheses in plain language.<sup>22</sup>

Figure 5.23 provides summary statistics for each group. A side-by-side boxplot for the change in non-dominant arm strength is shown in Figure 5.24; Figure 5.25 shows the Q-Q plots by each genotype. Notice that the variability appears to be approximately constant across groups; nearly constant variance across groups is an important assumption that must be satisfied for using ANOVA. Based on the Q-Q plots, there is evidence of moderate right skew; the data do not follow a normal distribution very closely, but could be considered to ’loosely’ follow a normal distribution.<sup>23</sup> It is reasonable to assume that the observations are independent within and across groups; it is unlikely that participants in the study were related, or that data collection was carried out in a way that one participant’s change in arm strength could influence another’s.

|  | CC | CT | TT |
| --- | --- | --- | --- |
| Sample size ($n_i$) | 173 | 261 | 161 |
| Sample mean ($\bar{x}_i$) | 48.89 | 53.25 | 58.08 |
| Sample SD ($s_i$) | 29.96 | 33.23 | 35.69 |

Figure 5.23: Summary statistics of change in non-dominant arm strength, split by genotype.

![](images/page_264_chart_9.jpg)

<details>
<summary>boxplot</summary>

| Genotype | Q1 | Q2 (Median) | Q3 | IQR |
| --- | --- | --- | --- | --- |
| CC | ~30 | ~45 | ~68 | ~38 |
| CT | ~30 | ~47 | ~72 | ~32 |
| TT | ~35 | ~51 | ~76 | ~41 |
</details>

Figure 5.24: Side-by-side box plot of the change in non-dominant arm strength for 595 participants across three groups.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">22H0: The average percent change in non-dominant arm strength is equal across the three genotypes. HA: The average percent change in non-dominant arm strength varies across some (or all) groups.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">23<sub>In</sub> a more advanced course, it can be shown that the ANOVA procedure still holds with deviations from normality when sample sizes are moderately large. Additionally, a more advanced course would discuss appropriate transformations to induce normality.</span></small>

![](images/page_265_image_2.jpg)

Figure 5.25: Q-Q plots of the change in non-dominant arm strength for 595 participants across three groups.

## EXAMPLE 5.21

The largest difference between the sample means is between the CC and TT groups. Consider again the original hypotheses:

$$
H _ {0}: \mu_ {\mathrm{CC}} = \mu_ {\mathrm{CT}} = \mu_ {\mathrm{TT}}
$$

$H _ { A } \colon$ The average percent change in non-dominant arm strength $( \mu _ { i } )$ varies across some (or all) groups.

Why might it be inappropriate to run the test by simply estimating whether the difference of $\mu _ { \mathrm { C C } }$ and $\mu _ { \mathrm { T T } }$ is statistically significant at a 0.05 significance level?

It is inappropriate to informally examine the data and decide which groups to formally test. This is a form of **data fishing**; choosing the groups with the largest differences for the formal test will lead to an increased chance of incorrectly rejecting the null hypothesis (i.e., an inflation in the Type I error rate). Instead, all the groups should be tested using a single hypothesis test.

Analysis of variance focuses on answering one question: is the variability in the sample means large enough that it seems unlikely to be from chance alone? The variation between groups is referred to as the **mean square between groups (**MSG); the MSG is a measure of how much each group mean varies from the overall mean. Let x represent the mean of outcomes across all groups, where ${ \overline { { x } } } _ { i }$ is the mean of outcomes in a particular group i and $n _ { i }$ is the sample size of group i. The mean square between groups is:

$$
M S G = \frac {1}{k - 1} \sum_ {i = 1} ^ {k} n _ {i} \left(\overline {{x}} _ {i} - \overline {{x}}\right) ^ {2} = \frac {1}{\mathrm{df} _ {G}} S S G,
$$

where SSG is the **sum of squares between groups**, $\textstyle \sum _ { i = 1 } ^ { k } n _ { i }   ( { \overline { { x } } } _ { i } - { \overline { { x } } } ) ^ { 2 }$ , and $\mathbf { d f } _ { G } = k - 1$ is the degrees of freedom associated with the MSG when there are k groups.

Under the null hypothesis, any observed variation in group means is due to chance and there is no real difference between the groups. In other words, the null hypothesis assumes that the groupings are non-informative, such that all observations can be thought of as belonging to a single group. If this scenario is true, then it is reasonable to expect that the variability between the group means should be equal to the variability observed within a single group. The **mean square error** (MSE) is a pooled variance estimate with associated degrees of freedom $\mathbf { d f } _ { E } = n   -   k$ that provides a measure of variability within the groups. The mean square error is computed as:

$$
M S E = \frac {1}{n - k} \sum_ {i = 1} ^ {k} (n _ {i} - 1) s _ {i} ^ {2} = \frac {1}{\mathrm{df} _ {E}} S S E,
$$

where the SSE is the **sum of squared errors**, $n _ { i }$ is the sample size of group $i ,$ and $s _ { i }$ is the standard deviation of group i.

Under the null hypothesis that all the group means are equal, any differences among the sample means are only due to chance; thus, the MSG and MSE should also be equal. ANOVA is based on comparing the MSG and MSE. The test statistic for ANOVA, the **F-statistic**, is the ratio of the between-group variability to the within-group variability:

$$
F = \frac {M S G}{M S E}. \tag {5.22}
$$

## EXAMPLE 5.23

Calculate the F-statistic for the famuss data summarized in Figure 5.23. The overall mean x across all observations is 53.29.

First, calculate the MSG and MSE.

$$
\begin{array}{l} M S G = \frac {1}{k - 1} \sum_ {i = 1} ^ {k} n _ {i} \left(\bar {x} _ {i} - \bar {x}\right) ^ {2} \\ = \frac {1}{3 - 1} \left[ (1 7 3) (4 8. 8 9 - 5 3. 2 9) ^ {2} + (2 6 1) (5 3. 2 5 - 5 3. 2 9) ^ {2} + (1 6 1) (5 8. 0 8 - 5 3. 2 9) ^ {2} \right] \\ = 3 5 2 1. 6 9 \\ M S E = \frac {1}{n - k} \sum_ {i = 1} ^ {k} (n _ {i} - 1) s _ {i} ^ {2} \\ = \frac {1}{5 9 5 - 3} \left[ (1 7 3 - 1) (2 9. 9 6 ^ {2}) + (2 6 1 - 1) (3 3. 2 3 ^ {2}) + (1 6 1 - 1) (3 5. 6 9 ^ {2}) \right] \\ = 1 0 9 0. 0 2 \\ \end{array}
$$

The F-statistic is the ratio:

$$
\frac {M S G}{M S E} = \frac {3 5 2 1 . 6 9}{1 0 9 0 . 0 2} = 3. 2 3.
$$

A p-value can be computed from the F-statistic using an F-distribution, which has two associated parameters: $\mathrm { d f _ { 1 } }$ and $\mathrm { d f } _ { 2 }$ . For the F-statistic in ANOVA, $\mathrm { d f _ { 1 } } = \mathrm { d f } _ { G }$ and $\mathbf { d f } _ { 2 } = \mathbf { d f } _ { E }$ . An F distribution with 2 and 592 degrees of freedom, corresponding to the F-statistic for the genotype and muscle strength hypothesis test, is shown in Figure 5.26.

![](images/page_267_chart_3.jpg)

<details>
<summary>area</summary>

| X | Y |
| --- | --- |
| 0 | ~1.0 |
| 1 | ~0.3 |
| 2 | ~0.1 |
| 3 | ~0.05 |
| 4 | ~0.02 |
| 5 | ~0.01 |
| 6 | ~0.005 |
</details>

Figure 5.26: An F-distribution with $\mathrm { d f _ { 1 } } = 2$ and $\mathbf { d f } _ { 2 } = 5 9 2$ . The tail area greater than $F = 3 . 2 3$ is shaded.

The larger the observed variability in the sample means (MSG) relative to the within-group variability (MSE), the larger F will be. Larger values of F represent stronger evidence against the null hypothesis. The upper tail of the distribution is used to compute a p-value, which is typically done using statistical software.

## EXAMPLE 5.24

The p-value corresponding to the test statistic is equal to about 0.04. Does this provide strong evidence against the null hypothesis at significance level $\alpha = 0 . 0 5 ?$

The p-value is smaller than 0.05, indicating the evidence is strong enough to reject the null hypothesis at a significance level of 0.05. The data suggest that average change in strength in the non-dominant arm varies by participant genotype.

## THE F-STATISTIC AND THE F-TEST

Analysis of variance (ANOVA) is used to test whether the mean outcome differs across two or more groups. ANOVA uses a test statistic F, which represents a standardized ratio of variability in the sample means relative to the variability within the groups. If $H _ { 0 }$ is true and the model assumptions are satisfied, the statistic F follows an F distribution with parameters $\mathbf { d f } _ { 1 } = k   -   1$ and $\mathbf { d } \mathbf { f } _ { 2 } = n   -   k .$ The upper tail of the F-distribution is used to calculate the p-value.

## 5.5.2 Reading an ANOVA table from software

The calculations required to perform an ANOVA by hand are tedious and prone to human error. Instead, it is common to use statistical software to calculate the F-statistic and associated p-value. The results of an ANOVA can be summarized in a table similar to that of a regression summary, which will be discussed in Chapters 6 and 7.

Figure 5.27 shows an ANOVA summary to test whether the mean change in non-dominant arm strength varies by genotype. Many of these values should look familiar; in particular, the F-statistic and p-value can be retrieved from the last two columns.

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| famuss$actn3.r577x | 2 | 7043 | 3522 | 3.231 | 0.0402 |
| Residuals | 592 | 645293 | 1090 |  |  |

Figure 5.27: ANOVA summary for testing whether the mean change in non-dominant arm strength varies by genotype at the actn3.r577x location on the ACTN3 gene.

## 5.5.3 Multiple comparisons and controlling Type I Error rate

Rejecting the null hypothesis in an ANOVA analysis only allows for a conclusion that there is evidence for a difference in group means. In order to identify the groups with different means, it is necessary to perform further testing. For example, in the famuss analysis, there are three comparisons to make: CC to CT, CC to TT, and CT to TT. While these comparisons can be made using two sample t-tests, it is important to control the Type I error rate. One of the simplest ways to reduce the overall probability of identifying a significant difference by chance in a multiple comparisons setting is to use the Bonferroni correction procedure.

In the Bonferroni correction procedure, the p-value from a two-sample t-test is compared to a modified significance level, $\alpha ^ { \star } ; \; \alpha ^ { \star } = \alpha / K ,$ , where K is the total number of comparisons being considered. For k groups, $\begin{array} { r } { K   =   \frac { k ( k - 1 ) } { 2 } } \end{array}$ When calculating the t-statistic, use the pooled estimate of standard deviation between groups (which equals ${ \sqrt { M S E } } ) ;$ to calculate the p-value, use a tdistribution with df<sub>2</sub>. It is typically more convenient to do these calculations using software.

## BONFERRONI CORRECTION

The **Bonferroni correction** suggests that a more stringent significance level is appropriate when conducting multiple tests:

$$
\alpha^ {\star} = \alpha / K
$$

where K is the number of comparisons being considered. For k groups, $\begin{array} { r } { K = \frac { k ( k - 1 ) } { 2 } } \end{array}$ .

## EXAMPLE 5.25

The ANOVA conducted on the famuss dataset showed strong evidence of differences in the mean strength change in the non-dominant arm between the three genotypes. Complete the three possible pairwise comparisons using the Bonferroni correction and report any differences.

Use a modified significance level of $\alpha ^ { \star } = 0 . 0 5 / 3 = 0 . 0 1 6 7$ . The pooled estimate of the standard deviation is ${ \sqrt { M S E } } = { \sqrt { 1 0 9 0 . 0 2 } } = 3 3 . 0 2$

Genotype CC versus Genotype CT:

$$
t = \frac {\overline {{x}} _ {1} - \overline {{x}} _ {2}}{s _ {\text {pooled}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}} = \frac {4 8 . 8 9 - 5 3 . 2 5}{3 3 . 0 2 \sqrt {\frac {1}{1 7 3} + \frac {1}{2 6 1}}} = - 1. 3 5.
$$

This results in a p-value of 0.18 on $d f = 5 9 2 .$ . This p-value is larger than $\alpha ^ { \star } = 0 . 0 1 6 7 ,$ so there is not evidence of a difference in the means of genotypes CC and CT.

Genotype CC versus Genotype TT:

$$
t = \frac {\overline {{x}} _ {1} - \overline {{x}} _ {2}}{s _ {\text {pooled}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}} = \frac {4 8 . 8 9 - 5 8 . 0 8}{3 3 . 0 2 \sqrt {\frac {1}{1 7 3} + \frac {1}{1 6 1}}} = - 2. 5 4.
$$

This results in a p-value of 0.01 on $d f = 5 9 2$ . This p-value is smaller than $\alpha ^ { \star } = 0 . 0 1 6 7$ , so there is evidence of a difference in the means of genotypes CC and TT.

Genotype CT versus Genotype TT:

$$
t = \frac {\overline {{x}} _ {1} - \overline {{x}} _ {2}}{s _ {\text {pooled}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}} = \frac {5 3 . 2 5 - 5 8 . 0 8}{3 3 . 0 2 \sqrt {\frac {1}{2 6 1} + \frac {1}{1 6 1}}} = - 1. 4 6.
$$

This results in a p-value of 0.14 on $d f = 5 9 2 .$ . This p-value is larger than $\alpha ^ { \star } = 0 . 0 1 6 7 ,$ so there is not evidence of a difference in the means of genotypes CT and TT.

In summary, the mean percent strength change in the non-dominant arm for genotype CT individuals is not statistically distinguishable from those of genotype CC and TT individuals. However, there is evidence that mean percent strength change in the non-dominant arm differs between individu als of genotype CC and TT are different.

## 5.5.4 Reading the results of pairwise t-tests from software

Statistical software can be used to calculate the p-values associated with each possible pairwise comparison of the groups in ANOVA. The results of the pairwise tests are summarized in a table that shows the p-value for each two-group test.

Figure 5.28 shows the p-values from the three possible two-group t-tests comparing change in non-dominant arm strengths between individuals with genotypes CC, CT, and TT. For example, the table indicates that when comparing mean change in non-dominant arm strength between TT and CC individuals, the p-value is 0.01. This coheres with the calculations above, and these unadjusted p-values should be compared to $\alpha ^ { \star } = 0 . 0 1 6 7$

|  | CC | CT |
| --- | --- | --- |
| CT | 0.18 | - |
| TT | 0.01 | 0.14 |

Figure 5.28: Unadjusted p-values for pairwise comparisons testing whether the mean change in non-dominant arm strength varies by genotype at the actn3.r577x location on ACTN3 gene.

The use of statistical software makes it easier to apply corrections for multiple testing, such that it is not necessary to explicitly calculate the value of $\alpha ^ { \star }$ . Figure 5.29 shows the Bonferroniadjusted p-values from the three possible tests. When statistical software applies the Bonferroni correction, the unadjusted p-value is multiplied by $K ,$ the number of comparisons, allowing for the values to be directly compared to α, not $\alpha ^ { \star } ,$ . Comparing an unadjusted p-value to α/K is equivalent to comparing the quantity $( K \times p -  value  )$ to α .

|  | CC | CT |
| --- | --- | --- |
| CT | 0.54 | - |
| TT | 0.03 | 0.43 |

Figure 5.29: Bonferroni-adjusted p-values for pairwise comparisons testing whether the mean change in non-dominant arm strength varies by genotype at the actn3.r577x location on ACTN3 gene.

## 5.6 Notes

The material in this chapter is particularly important. For many applications, t-tests and Analysis of Variance (ANOVA) are an essential part of the core of statistics in medicine and the life sciences. The comparison of two or more groups is often the primary aim of experiments both in the laboratory and in studies with human subjects. More generally, the approaches to interpreting and drawing conclusions from testing demonstrated in this chapter are used throughout the rest of the text and, indeed, in much of statistics.

While it is important to master the details of the techniques of testing for differences in two or more groups, it is even more critical to not lose sight of the fundamental principles behind the tests. A statistically significant difference in group means does not necessarily imply that group membership is the reason for the observed association. A significant association does not neces sarily imply causation, even if it is highly significant; confounding variables may be involved. In most cases, causation can only be inferred in controlled experiments when interventions have been assigned randomly. It is also essential to carefully consider the context of a problem. For instance, students often find the distinction between paired and independent group comparisons confusing; understanding the problem context is the only reliable way to choose the correct approach.

It is generally prudent to use the form of the t-test that does not assume equal standard de viations, but the power calculations described in Section 5.4 assume models with equal standard deviations. The formulas are simpler when standard deviations are equal, and software is more widely available for that case. The differences in sample sizes are usually minor and less important than assumptions about target differences or the values of the standard deviations. If the standard deviations are expected to be very different, then more specialized software for computing sample size and power should be used. The analysis done after the study has been completed should then use the t-test for unequal standard deviations.

Tests for significant differences are sometimes overused in science, with not enough attention paid to estimates and confidence intervals. Confidence intervals for the difference of two population means show a range of underlying differences in means that are consistent with the data, and often lead to insights not possible from only the test statistic and p-value. Wide confidence intervals may show that a non-significant test is the result of high variability in the test statistic, perhaps caused by a sample size that was too small. Conversely, a highly significant p-value may be the result of such a large sample size that the observed differences are not scientifically meaningful; that may be evident from confidence intervals with very narrow width.