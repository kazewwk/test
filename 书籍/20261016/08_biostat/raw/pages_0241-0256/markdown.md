## 5.1.2 Using the t-distribution for tests and confidence intervals for a population mean

Chapter 4 provided formulas for tests and confidence intervals for population means in random samples large enough for the t-statistic to have a nearly normal distribution. In samples smaller than 30 from approximately symmetric distributions without large outliers, the t-statistic has a t-distribution with degrees of freedom equal to n − 1. Just like inference in larger samples, inference using the t-distribution also requires that the observations in the sample be independent. Random samples from very large populations always produce independent observations; in smaller populations, observations will be approximately independent as long as the size of the sample is no larger than 10% of the population.

Formulas for tests and intervals using the t−distribution are very similar to those using the normal distribution. For a sample of size n with sample mean x and standard deviation $S ,$ two-sided confidence intervals with confidence coefficient $1 0 0 ( 1 - \alpha ) \%$ have the form

$$
\overline {{x}} \pm t _ {\mathrm{df}} ^ {\star} \times \mathrm{SE},
$$

where SE is the standard error of the sample mean $( s / { \sqrt { n } } )$ and $t _ { \mathrm { d f } } ^ { \star }$ is the point on a t-distribution with $n - 1$ degrees of freedom and area $( 1 - \alpha / 2 )$ to its left.

A one-sided interval with the same confidence coefficient will have the form

$$
\overline {{x}} + t _ {\mathrm{df}} ^ {\star} \times \text {SE (one - sided upper confidence interval), or}
$$

$$
\overline {{x}} - t _ {\mathrm{df}} ^ {\star} \times \text {SE (one - sided lower confidence interval)},
$$

except that in this case $t _ { \mathrm { d f } } ^ { \star }$ is the point on a t-distribution with $n - 1$ degrees of freedom and area $( 1 - \alpha )$ to its left.

With the ability to conveniently calculate $t ^ { \star }$ for any sample size or associated α via computing software, the t-distribution can be used by default over the normal distribution. The rule of thumb that $n > 3 0$ qualifies as a large enough sample size to use the normal distribution dates back to when it was necessary to rely on distribution tables.

## EXAMPLE 5.3

Dolphins are at the top of the oceanic food chain; as a consequence, dangerous substances such as mercury tend to be present in their organs and muscles at high concentrations. In areas where dolphins are regularly consumed, it is important to monitor dolphin mercury levels. This example uses data from a random sample of 19 Risso’s dolphins from the Taiji area in Japan.<sup>2</sup> Calculate the 95% confidence interval for average mercury content in Risso’s dolphins from the Taiji area using the data in Figure 5.6.

The observations are a simple random sample consisting of less than 10% of the population, so independence of the observations is reasonable. The summary statistics in Figure 5.6 do not suggest any skew or outliers; all observations are within 2.5 standard deviations of the mean. Based on this evidence, the approximate normality assumption seems reasonable.

Use the t-distribution to calculate the confidence interval:

$$
\begin{array}{l} \overline {{x}} \pm t _ {\mathrm{df}} ^ {\star} \times \mathrm{SE} = \overline {{x}} \pm t _ {1 8} ^ {\star} \times s / \sqrt {n} \\ = 4. 4 \pm 2. 1 0 \times 2. 3 / \sqrt {1 9} \\ = (3. 2 9, 5. 5 1) \mu \mathrm{g/wet} \mathrm{g}. \\ \end{array}
$$

The $t ^ { \star }$ point can be read from the t-table on page 239, in the column with area totaling 0.05 in the two tails (third column) and the row with 18 degrees of freedom. Based on these data, one can be 95% confident the average mercury content of muscles in Risso’s dolphins is between 3.29 and 5.51 µg/wet gram.

Alternatively, the $t ^ { \star }$ point can be calculated in R with the function qt, which returns a value of 2.1009.

| n | $\overline{x}$ | s | minimum | maximum |
| --- | --- | --- | --- | --- |
| 19 | 4.4 | 2.3 | 1.7 | 9.2 |

Figure 5.6: Summary of mercury content in the muscle of 19 Risso’s dolphins from the Taiji area. Measurements are in $\mu \mathrm { g } / \mathrm { w e t }$ g (micrograms of mercury per wet gram of muscle).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Taiji is a significant source of dolphin and whale meat in Japan. Thousands of dolphins pass through the Taiji area annually; assume that these 19 dolphins represent a simple random sample. Data reference: Endo T and Haraguchi K. 2009. High mercury levels in hair samples from residents of Taiji, a Japanese whaling town. Marine Pollution Bulletin 60(5):743-747.</span></small>

## GUIDED PRACTICE 5.4

The FDA’s webpage provides some data on mercury content of various fish species.<sup>3</sup> From a sample of 15 white croaker (Pacific), a sample mean and standard deviation were computed as 0.287 and 0.069 ppm (parts per million), respectively. The 15 observations ranged from 0.18 to 0.41 ppm. Assume that these observations are independent. Based on summary statistics, does the normality assumption seem reasonable? If so, calculate a 90% confidence interval for the average mercury content of white croaker (Pacific).<sup>4</sup>

## EXAMPLE 5.5

According to the EPA, regulatory action should be taken if fish species are found to have a mercury level of 0.5 ppm or higher. Conduct a formal significance test to evaluate whether the average mercury content of croaker white fish (Pacific) is different from 0.50 ppm. Use α = 0.05.

The FDA regulatory guideline is a ‘one-sided’ statement; fish should not be eaten if the mercury level is larger than a certain value. However, without prior information on whether the mercury in this species tends to be high or low, it is best to do a two-sided test.

State the hypotheses: $H _ { 0 } : \mu = 0 . 5 \; \mathrm { v s } \; H _ { A } : \mu \neq 0 . 5 . \; \mathrm { L e t } \; \alpha = 0 . 0 5 .$

Calculate the t-statistic:

$$
t = \frac {\overline {{x}} - \mu_ {0}}{\mathrm{SE}} = \frac {0 . 2 8 7 - 0 . 5 0}{0 . 0 6 9 / \sqrt {1 5}} = - 1 1. 9 6
$$

The probability that the absolute value of a t-statistic with 14 df is smaller than -11.96 is smaller than 0.01. Thus, $p < 0 . 0 1$ . There is evidence to suggest at the $\alpha = 0 . 0 5$ significance level that the average mercury content of this fish species is lower than 0.50 ppm, since x is less than 0.50.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>[www.fda.gov/food/foodborneillnesscontaminants/metals/ucm115644.htm](http://www.openintro.org/redirect.php?go=textbook-fda_mercury_in_fish_2010&referrer=biostat1_pdf)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>There are no obvious outliers; all observations are within 2 standard deviations of the mean. If there is skew, it is not evident. There are no red flags for the normal model based on this (limited) information. x ± t?14 × SE → 0.287 ± 1.76 × 0.0178 → (0.256,0.318). We are 90% confident that the average mercury content of croaker white fish (Pacific) is between 0.256 and 0.318 ppm.</span></small>

## 5.2 Two-sample test for paired data

In the 2000 Olympics, was the use of a new wetsuit design responsible for an observed increase in swim velocities? In a study designed to investigate this question, twelve competitive swimmers swam 1500 meters at maximal speed, once wearing a wetsuit and once wearing a regular swimsuit.<sup>5</sup> The order of wetsuit versus swimsuit was randomized for each of the 12 swimmers. Figure 5.7 shows the average velocity recorded for each swimmer, measured in meters per second $( \mathbf { m } / \mathbf { s } ) .$ <sup>6</sup>

|  | swimmer.number | wet.suit.velocity | swim.suit.velocity | velocity.diff |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1.57 | 1.49 | 0.08 |
| 2 | 2 | 1.47 | 1.37 | 0.10 |
| 3 | 3 | 1.42 | 1.35 | 0.07 |
| 4 | 4 | 1.35 | 1.27 | 0.08 |
| 5 | 5 | 1.22 | 1.12 | 0.10 |
| 6 | 6 | 1.75 | 1.64 | 0.11 |
| 7 | 7 | 1.64 | 1.59 | 0.05 |
| 8 | 8 | 1.57 | 1.52 | 0.05 |
| 9 | 9 | 1.56 | 1.50 | 0.06 |
| 10 | 10 | 1.53 | 1.45 | 0.08 |
| 11 | 11 | 1.49 | 1.44 | 0.05 |
| 12 | 12 | 1.51 | 1.41 | 0.10 |

Figure 5.7: Paired Swim Suit Data

The swimsuit velocity data are an example of **paired data**, in which two sets of observations are uniquely paired so that an observation in one set matches an observation in the other; in this case, each swimmer has two measured velocities, one with a wetsuit and one with a swimsuit. A natural measure of the effect of the wetsuit on swim velocity is the difference between the measured maximum velocities (velocity.diff = wet.suit.velocity - swim.suit.velocity). Even though there are two measurements per swimmer, using the difference in velocities as the variable of interest allows for the problem to be approached like those in Section 5.1. Although it was not explicitly noted, the data used in Section 4.3.1 were paired; each respondent had both an actual and desired weight.

Suppose the parameter δ is the population average of the difference in maximum velocities during a 1500m swim if all competitive swimmers recorded swim velocities with each suit type. A hypothesis test can then be conducted with the null hypothesis that the mean population difference in swim velocities between suit types equals 0 (i.e., there is no difference in population average swim velocities), $H _ { 0 } : \delta = 0 ,$ against the alternative that the difference is non-zero, $H _ { A } : \delta \neq 0$

## STATING HYPOTHESES FOR PAIRED DATA

When testing a hypothesis about paired data, compare the groups by testing whether the population mean of the differences between the groups equals 0.

– For a two-sided test, $H _ { 0 } : \delta = 0 ;   H _ { A } : \delta \neq 0 .$ .
– For a one-sided test, either $H _ { 0 } : \delta = 0 ;   H _ { A } : \delta > 0 \mathrm { ~ o r ~ } H _ { 0 } : \delta = 0 ;   H _ { A } : \delta < 0 .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>De Lucas et. al, The effects of wetsuits on physiological and biomechanical indices during swimming. Journal of Science and Medicine in Sport, 2000; 3(1): 1-8</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>The data are available as swim in the oibiostat R package. The data are also used in Lock et. al Statistics, Unlocking the Power of Data, Wiley, 2013.</span></small>

Some important assumptions are being made. First, it is assumed that the data are a random sample from the population. While the observations are likely independent, it is more difficult to justify that this sample of 12 swimmers is randomly drawn from the entire population of competitive swimmers. Nevertheless, it is often assumed in problems such as these that the participants are reasonably representative of competitive swimmers. Second, it is assumed that the population of differences is normally distributed. This is a small sample, one in which normality would be difficult to confirm. The dot plot for the difference in velocities in Figure 5.8 shows approximate symmetry.

![](images/page_244_chart_3.jpg)

<details>
<summary>scatter</summary>

| Difference in Swim Velocities (m/s) | Value |
| --- | --- |
| 0.05 | ~0.15 |
| 0.06 | ~0.15 |
| 0.08 | ~0.15 |
| 0.10 | ~0.15 |
| 0.11 | ~0.15 |
</details>

Figure 5.8: A dot plot of differences in swim velocities.

Let $\overline { { x } } _ { \mathrm { d i f f } }$ denote the sample average of the differences in maximum velocity, $s _ { \mathrm { d i f f } }$ the sample standard deviation of the differences, and n the number of pairs in the dataset. The t-statistic used to test $H _ { 0 }$ vs. $H _ { A }$ is:

$$
\frac {\overline {{x}} _ {\mathrm{diff}} - \delta_ {0}}{s _ {\mathrm{diff}} / \sqrt {n}},
$$

where in this case $\delta _ { 0 } = 0 . ^ { 7 }$

## EXAMPLE 5.6

Using the data in Figure 5.7, conduct a two-sided hypothesis test at $\alpha = 0 . 0 5$ to assess whether there is evidence to suggest that wetsuits have an effect on swim velocities during a 1500m swim.

The hypotheses are $H _ { 0 } : \delta = 0$ and $H _ { A } : \delta \neq 0$ . Let $\alpha = 0 . 0 5$

Calculate the t-statistic:

$$
t = \frac {\overline {{x}} _ {\mathrm{diff}} - \delta_ {0}}{s _ {\mathrm{diff}} / \sqrt {n}} = \frac {0 . 0 7 8 - 0}{0 . 0 2 2 / \sqrt {1 2}} = 1 2. 3 2
$$

The two-sided p-value is

$$
p = P (T <   - 1 2. 3 2) + P (T > 1 2. 3 2),
$$

where t has a t-distribution with $n - 1 = 1 1$ degrees of freedom. The t-table shows that $p < 0 . 0 1$ Software can be used to show that $p = 8 . 9 \times 1 0 ^ { - 8 }$ , a very small value indeed.

The data support the claim that the wetsuits changed swim velocity in a 1500m swim. The observed average increase of 0.078 m/s is significantly different than the null hypothesis of no change, and suggests that swim velocities are higher when swimmers wear wetsuits as opposed to swimsuits.

Calculating confidence intervals for paired data is also based on the differences between the values in each pair; the same approach as for single-sample data can be applied on the differences. For example, a two-sided 95% confidence interval for paired data has the form:

$$
\left(\overline {{x}} _ {\mathrm{diff}} - t _ {d f} ^ {\star} \times \frac {s _ {\mathrm{diff}}}{\sqrt {n}}, \overline {{x}} _ {\mathrm{diff}} + t _ {d f} ^ {\star} \times \frac {s _ {\mathrm{diff}}}{\sqrt {n}}\right),
$$

where $t ^ { \star }$ is the point on a t-distribution with $d f = n - 1$ for n pairs, with area 0.025 to its right.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>This value is specified by the null hypothesis of no difference.</span></small>

![](images/page_245_image_2.jpg)

## GUIDED PRACTICE 5.7

Using the data in Figure 5.7, calculate a 95% confidence interval for the average difference in swim velocities during a 1500m swim. Is the interval consistent with the results of the hypothesis test?<sup>8</sup>

The general approach when analyzing paired data is to first calculate the differences between the values in each pair, then use those differences in methods for confidence intervals and tests for a single sample. Any conclusion from an analysis should be stated in terms of the original paired measurements.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>Use the values of <sup>x</sup>diff and <sup>s</sup>diff as calculated previously: 0.078 and 0.022. The t? value of 2.20 has df = 11 and 0.025 area to the right. The confidence interval is (0.078±0.022) → (0.064, 0.091) m/s. With 95% confidence, δ lies between 0.064 √12 m/s and 0.09 m/s. The interval does not include 0 (no change), which is consistent with the result of the hypothesis test.</span></small>

## 5.3 Two-sample test for independent data

Does treatment using embryonic stem cells (ESCs) help improve heart function following a heart attack? New and potentially risky treatments are sometimes tested in animals before studies in humans are conducted. In a 2005 paper in Lancet, Menard, et al. describe an experiment in which 18 sheep with induced heart attacks were randomly assigned to receive cell transplants containing either ESCs or inert material.<sup>9</sup> Various measures of cardiac function were measured 1 month after the transplant.

This design is typical of an intervention study. The analysis of such an experiment is an example of drawing inference about the difference in two population means, $\mu _ { 1 }   -   \mu _ { 2 }$ , when the data are independent, i.e., not paired. The point estimate of the difference, ${ \overline { { x } } } _ { 1 } - { \overline { { x } } } _ { 2 } ,$ , is used to calculate a t-statistic that is the basis of confidence intervals and tests.

## 5.3.1 Confidence interval for a difference of means

Figure 5.9 contains summary statistics for the 18 sheep.<sup>10</sup> Percent change in heart pumping capacity was measured for each sheep. A positive value corresponds to increased pumping capacity, which generally suggests a stronger recovery from the heart attack. Is there evidence for a potential treatment effect of administering stem cells?

|  | n | $\overline{x}$ | s |
| --- | --- | --- | --- |
| ESCs | 9 | 3.50 | 5.17 |
| control | 9 | -4.33 | 2.76 |

Figure 5.9: Summary statistics of the embryonic stem cell study.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>Menard C, et al., Transplantation of cardiac-committed mouse embryonic stem cells to infarcted sheep myocardium: a preclinical 2005; 366:1005-12, doi [https://doi.org/10.1016/S0140-6736(05)67380-1](https://doi.org/10.1016/S0140-6736%2805%2967380-1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10<sub>The</sub> data are accessible as the dataset stem.cells in the openintro R package.</span></small>

![](images/page_247_image_2.jpg)

Figure 5.10: Histograms for both the embryonic stem cell group and the control group. Higher values are associated with greater improvement.

Figure 5.10 shows that the distributions of percent change do not have any prominent outliers, which would indicate a deviation from normality; this suggests that each sample mean can be modeled using a t-distribution. Additionally, the sheep in the study are independent of each other, and the sheep between groups are also independent. Thus, the t-distribution can be used to model the difference of the two sample means.

## USING THE t-DISTRIBUTION FOR A DIFFERENCE IN MEANS

The t-distribution can be used for inference when working with the standardized difference of two means if (1) each sample meets the conditions for using the t-distribution and (2) the samples are independent.

A confidence interval for a difference of two means has the same basic structure as previously discussed confidence intervals:

$$
(\overline {{x}} _ {1} - \overline {{x}} _ {2}) \pm t _ {d f} ^ {\star} \times \mathrm{SE}.
$$

The following formula is used to calculate the standard error of $\overline { { x } } _ { 1 } - \overline { { x } } _ { 2 }$ . Since $\sigma$ is typically unknown, the standard error is estimated by using s in place of σ.

$$
S E _ {\overline {{x}} _ {1} - \overline {{x}} _ {2}} = \sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}} \approx \sqrt {\frac {s _ {1} ^ {2}}{n _ {1}} + \frac {s _ {2} ^ {2}}{n _ {2}}}.
$$

In this setting, the t-distribution has a somewhat complicated formula for the degrees of freedom that is usually calculated with software.<sup>11</sup> An alternative approach uses the smaller of $n _ { 1 } - 1$ and $n _ { 2 } - 1$ as the degrees of freedom.<sup>12</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11<sub>See</sub> Section 5.6 for the formula.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12<sub>This</sub> technique for degrees of freedom is conservative with respect to a Type 1 Error; it is more difficult to reject the null hypothesis using this approach for degrees of freedom.</span></small>

## DISTRIBUTION OF A DIFFERENCE OF SAMPLE MEANS

The sample difference of two means, ${ \overline { { x } } } _ { 1 } - { \overline { { x } } } _ { 2 } ,$ can be modeled using the t-distribution and the standard error

$$
S E _ {\overline {{x}} _ {1} - \overline {{x}} _ {2}} = \sqrt {\frac {s _ {1} ^ {2}}{n _ {1}} + \frac {s _ {2} ^ {2}}{n _ {2}}} \tag {5.8}
$$

when each sample mean can itself be modeled using a t-distribution and the samples are independent. To calculate the degrees of freedom without using software, use the smaller of $n _ { 1 } - 1 \mathrm { a n d } n _ { 2 } - 1$

## EXAMPLE 5.9

Calculate and interpret a 95% confidence interval for the effect of ESCs on the change in heart pumping capacity of sheep following a heart attack.

The point estimate for the difference is $\overline { { x } } _ { 1 } - \overline { { x } } _ { 2 } = \overline { { x } } _ { \mathrm { e s c } } - \overline { { x } } _ { \mathrm { c o n t r o l } } = 7 . 8 3 .$

The standard error is:

$$
\sqrt {\frac {s _ {1} ^ {2}}{n _ {1}} + \frac {s _ {2} ^ {2}}{n _ {2}}} = \sqrt {\frac {5 . 1 7 ^ {2}}{9} + \frac {2 . 7 6 ^ {2}}{9}} = 1. 9 5.
$$

Since $n _ { 1 } = n _ { 2 } = 9 ,$ , use $df = 8; t_{8}^{\star} = 2.31$ for a 95% confidence interval. Alternatively, computer software can provide more accurate values: $d f = 1 2 . 2 2 5 , t ^ { \star } = 2 . 1 7 4 .$

The confidence interval is given by:

$$
(\overline {{x}} _ {1} - \overline {{x}} _ {2}) \pm t _ {d f} ^ {\star} \times \text {SE} \quad \rightarrow \quad 7. 8 3 \pm 2. 3 1 \times 1. 9 5 \quad \rightarrow \quad (3. 3 8, 1 2. 3 8).
$$

With 95% confidence, the average amount that ESCs improve heart pumping capacity lies between 3.38% to 12.38%.<sup>13</sup> The data provide evidence for a treatment effect of administering stem cells.

## 5.3.2 Hypothesis tests for a difference in means

Is there evidence that newborns from mothers who smoke have a different average birth weight than newborns from mothers who do not smoke? The dataset births contains data from a random sample of 150 cases of mothers and their newborns in North Carolina over a year; there are 50 cases in the smoking group and 100 cases in the nonsmoking group.<sup>14</sup>

|  | fAge | mAge | weeks | weight | sexBaby | smoke |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | NA | 13 | 37 | 5.00 | female | nonsmoker |
| 2 | NA | 14 | 36 | 5.88 | female | nonsmoker |
| 3 | 19 | 15 | 41 | 8.13 | male | smoker |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |  |
| 150 | 45 | 50 | 36 | 9.25 | female | nonsmoker |

Figure 5.11: Four cases from the births dataset.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13<sub>From</sub> software, the confidence interval is (3.58, 12.08).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">14<sub>This</sub> dataset is available in the openintro R package.</span></small>

![](images/page_249_image_2.jpg)

## EXAMPLE 5.10

Evaluate whether it is appropriate to apply the t-distribution to the difference in sample means between the two groups.

Since the data come from a simple random sample and consist of less than 10% of all such cases, the observations are independent. While each distribution is strongly skewed, the large sample sizes of 50 and 100 allow for the use of the t-distribution to model each mean separately. Thus, the difference in sample means may be modeled using a t-distribution.

![](images/page_249_image_6.jpg)

Figure 5.12: The top panel represents birth weights for infants whose mothers smoked. The bottom panel represents the birth weights for infants whose mothers who did not smoke. The distributions exhibit moderate-to-strong and strong skew, respectively.

A hypothesis test can be conducted to evaluate whether there is a relationship between mother’s smoking status and average newborn birth weight. The null hypothesis represents the case of no difference between the groups, $H _ { 0 } : \mu _ { n s } - \mu _ { s } = 0 ,$ , where $\mu _ { n s }$ represents the population mean of newborn birthweight for infants with mothers who did not smoke, and $\mu _ { s }$ represents mean newborn birthweight for infants with mothers who smoked. Under the alternative hypothesis, there is some difference in average newborn birth weight between the groups, $H _ { A } : \mu _ { n s } - \mu _ { s } \neq 0$ . The hypotheses can also be written as $H _ { 0 } : \mu _ { n s } = \mu _ { s }$ and $H _ { A } : \mu _ { n s } \neq \mu _ { s }$

## STATING HYPOTHESES FOR TWO-GROUP DATA

When testing a hypothesis about two independent groups, directly compare the two population means and state hypotheses in terms of $\mu _ { 1 }$ and $\mu _ { 2 }$

– For a two-sided test, $H _ { 0 } : \mu _ { 1 } = \mu _ { 2 } ;   H _ { A } : \mu _ { 1 } \neq \mu _ { 2 } .$
– For a one-sided test, either $H _ { 0 } : \mu _ { 1 } = \mu _ { 2 } ;   H _ { A } : \mu _ { 1 } > \mu _ { 2 } \; \mathrm { o r } \; H _ { 0 } : \mu _ { 1 } = \mu _ { 2 } ;   H _ { A } : \mu _ { 1 } < \mu _ { 2 } .$

In this setting, the formula for a t-statistic is:

$$
t = \frac {(\overline {{x}} _ {1} - \overline {{x}} _ {2}) - (\mu_ {1} - \mu_ {2})}{S E _ {\overline {{x}} _ {1} - \overline {{x}} _ {2}}} = \frac {(\overline {{x}} _ {1} - \overline {{x}} _ {2}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {s _ {1} ^ {2}}{n _ {1}} + \frac {s _ {2} ^ {2}}{n _ {2}}}}.
$$

Under the null hypothesis of no difference between the groups, $H _ { 0 } : \mu _ { 1 } - \mu _ { 2 } = 0 ,$ , the formula simplifies to

$$
t = \frac {(\overline {{x}} _ {1} - \overline {{x}} _ {2})}{\sqrt {\frac {s _ {1} ^ {2}}{n _ {1}} + \frac {s _ {2} ^ {2}}{n _ {2}}}}.
$$

## EXAMPLE 5.11

Using Figure 5.13, conduct a hypothesis test to evaluate whether there is evidence that newborns from mothers who smoke have a different average birth weight than newborns from mothers who do not smoke.

The hypotheses are $H _ { 0 } : \mu _ { 1 } = \mu _ { 2 }$ and $H _ { A } : \mu _ { 1 } \neq \mu _ { 2 } ,$ where $\mu _ { 1 }$ represents the average newborn birth weight for nonsmoking mothers and $\mu _ { 2 }$ represents average newborn birth weight for mothers who smoke. Let $\alpha = 0 . 0 5$

Calculate the t-statistic:

$$
t = \frac {(\overline {{x}} _ {1} - \overline {{x}} _ {2})}{\sqrt {\frac {s _ {1} ^ {2}}{n _ {1}} + \frac {s _ {2} ^ {2}}{n _ {2}}}} = \frac {7 . 1 8 - 6 . 7 8}{\sqrt {\frac {1 . 6 0 ^ {2}}{1 0 0} + \frac {1 . 4 3 ^ {2}}{5 0}}} = 1. 5 4.
$$

Approximate the degrees of freedom as $50 - 1 = 49$ . The t-score of 1.49 falls between the first and second columns in the $d f = 4 9$ row of the t-table, so the two-sided p-value is between 0.10 and 0.20.<sup>15</sup>

This p-value is larger than the significance value, 0.05, so the null hypothesis is not rejected. There is insufficient evidence to state there is a difference in average birth weight of newborns from North Carolina mothers who did smoke during pregnancy and newborns from North Carolina mothers who did not smoke during pregnancy.

|  | smoker | nonsmoker |
| --- | --- | --- |
| mean | 6.78 | 7.18 |
| st. dev. | 1.43 | 1.60 |
| samp. size | 50 | 100 |

Figure 5.13: Summary statistics for the births dataset.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">15<sub>From</sub> R, df = 89.277 and p = 0.138.</span></small>

## 5.3.3 The paired test vs. independent group test

In the two-sample setting, students often find it difficult to determine whether a paired test or an independent group test should be used. The paired test applies only in situations where there is a natural pairing of observations between groups, such as in the swim data. Pairing can be obvious, such as the two measurements for each swimmer, or more subtle, such as measurements of respiratory function in twins, where one member of the twin pair is treated with an experimental treatment and the other with a control. In the case of two independent groups, there is no natural way to pair observations.

A common error is to overlook pairing in data and assume that two groups are independent. The swimsuit data can be used to illustrate the possible harm in conducting an independent group test rather than a paired test. In Section 5.2, the paired t-test showed a significant difference in the swim velocities between swimmers wearing wetsuits versus regular swimsuits. Suppose the analysis had been conducted without accounting for the fact that the measurements were paired.

The mean and standard deviation for the 12 wet suit velocities are 1.51 and 0.14 (m/sec), respectively, and 1.43 and 0.14 (m/sec) for the 12 swim suit velocities. A two-group test statistic is:

$$
t = \frac {1 . 5 2 - 1 . 4 3}{\sqrt {0 . 1 4 ^ {2} / 1 2 + 0 . 1 4 ^ {2} / 1 2}} = 1. 3 7.
$$

If the degrees of freedom are approximated as $1 1 = 1 2   -   1$ , the two-sided p-value as calculated from software is 0.20. According to this method, the null hypothesis of equal mean velocities for the two suit types would not be rejected.

It is not difficult to show that the numerator of the paired test (the average of the within swimmer differences) and the numerator of the two-group test (the difference of the average times for the two groups) are identical. The values of the test statistics differ because the denominators are different—specifically, the standard errors associated with each statistic are different. For the paired test statistic, the standard error uses the standard deviation of the within pair differences (0.22) and has value $0 . 0 2 2 / \sqrt { 1 2 } = 0 . 0 0 6$ . The two-group test statistic combines the standard deviations for the original measurements and has value $\sqrt { 0 . 1 4 ^ { 2 } / 1 2 + 0 . 1 4 ^ { 2 } / 1 2 } = 0 . 0 6$ . The standard error for the two-group test is 10-fold larger than for the paired test.

This striking difference in the standard errors is caused by the much lower variability of the individual velocity differences compared to the variability of the original measurements. Due to the correlation between swim velocities for a single swimmer, the differences in the two velocity measurements for each swimmer are consistently small, resulting in low variability. Pairing has allowed for increased precision in estimating the difference between groups.

The swim suit data illustrates the importance of context, which distinguishes a statistical problem from a purely mathematical one. While both the paired and two-group tests are numerically feasible to calculate, without an apparent error, the context of the problem dictates that the correct approach is to use a paired test.

## GUIDED PRACTICE 5.12

Propose an experimental design for the embryonic stem cell study in sheep that would have required analysis with a paired t-test.<sup>16</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">16<sub>The</sub> experiment could have been done on pairs of siblings, with one assigned to the treatment group and one assigned to the control group. Alternatively, sheep could be matched up based on particular characteristics relevant to the experiment; for example, sheep could be paired based on similar weight or age. Note that in this study, a design involving two measurements taken on each sheep would be impractical.</span></small>

## 5.3.4 Case study: discrimination in developmental disability support

Section 1.7.1 presented an analysis of the relationship between age, ethnicity, and amount of expenditures for supporting developmentally disabled residents in the state of California, using the dds.discr dataset. When the variable age is ignored, the expenditures per consumer is larger on average for White non-Hispanics than Hispanics, but Figure 1.53 showed that average differences by ethnicity were much smaller within age cohorts. This section demonstrates the use of t-tests to conduct a more formal analysis of possible differences in expenditure by ethnicity, both overall (i.e., ignoring age) and within age cohorts.

## Comparing expenditures overall

When ignoring age, expenditures within the ethnicity groups Hispanic and White non-Hispanic show substantial right-skewing (Figure 1.45). A transformation is advisable before conducting a t-test. As shown in Figure 5.14, a natural log transformation effectively eliminates skewing.

![](images/page_252_chart_6.jpg)

<details>
<summary>boxplot</summary>

| Ethnicity | Q1 | Q2 (Median) | Q3 | Min | Max |
| --- | --- | --- | --- | --- | --- |
| Hispanic | ~7.8 | ~8.3 | ~9.3 | ~6.1 | ~11.1 |
| White not Hispanic | ~8.3 | ~9.7 | ~10.7 | ~5.8 | ~11.2 |
</details>

Figure 5.14: A plot of log(expenditures) by ethnicity.

Is there evidence of a difference in mean expenditures by ethnic group? Conduct a t-test of the null hypothesis $H _ { 0 } : \mu _ { 1 } = \mu _ { 2 }$ versus the two-sided alternative $H _ { A } : \mu _ { 1 } \neq \mu _ { 2 }$ , where $\mu _ { 1 }$ is the population mean log expenditure in Hispanics and $\mu _ { 2 }$ is the population mean log expenditure in White non-Hispanics.

|  | Ethnicity | n | $\overline{x}$ | s |
| --- | --- | --- | --- | --- |
| 1 | Hispanic | 376 | 8.56 | 1.17 |
| 2 | White non Hispanic | 401 | 9.47 | 1.35 |

Figure 5.15: Summary statistics for the transformed variable log(expenditures) in the dds.discr data.

The summary statistics required to calculate the t-statistic are shown in Figure 5.15. The t-statistic for the test is

$$
t = \frac {9 . 4 7 - 8 . 5 6}{\sqrt {1 . 3 5 ^ {2} / 4 0 1 + 1 . 1 7 ^ {2} / 3 7 6}} = 1 0. 1.
$$

The degrees of freedom of the test can be approximated as $376 - 1 = 375;$ the p-value can be calculated using a normal approximation. Regardless of whether a t or normal distribution is used, the probability of a test statistic with absolute value larger than 10 is vanishingly small—the p-value is less than 0.001. When ignoring age, there is significant evidence of a difference in mean expenditures between Hispanics and White non-Hispanics. It appears that on average, White non-Hispanics receive a higher amount of developmental disability support from the state of California $\left( \overline { { x } } _ { 1 } < \overline { { x } } _ { 2 } \right)$

However, as indicated in Section 1.7.1, this is a misleading result. The analysis as conducted does not account for the confounding effect of age, which is associated with both expenditures and ethnicity. As individuals age, they typically require more support from the government. In this dataset, White non-Hispanics tend to be older than Hispanics; this difference in age distribution contributes to the apparent difference in expenditures between two groups.

## Comparing expenditures within age cohorts

One way to account for the effect of age is to compare mean expenditures within age cohorts. When comparing individuals of similar ages but different ethnic groups, are the differences in mean expenditures larger than would be expected by chance alone?

Figure 1.52 shows that the age cohort 13-17 is the largest among the Hispanic consumers, while the cohort 22-50 is the largest among White non-Hispanics. This section will examine the evidence against the null hypothesis of no difference in mean expenditures within these two co-horts.

Figure 5.16 shows that within both the age cohorts of 13-17 years and 22-50 years, the distribution of expenditures is reasonably symmetric; there is no need to apply a transformation before conducting a t-test. The skewing evident when age was ignored is due to the differing distributions of age within ethnicities.

![](images/page_253_image_8.jpg)

Figure 5.16: (a)A plot of expenditures by ethnicity in the age cohort 13 - 17. (b) A plot of expenditures by ethnicity in the age cohort 22 - 50.

Figure 5.17 contains the summary statistics for computing the test statistic to compare expenditures in the two groups within this age cohort. The test statistic has value t = 0.318, with degrees of freedom 66. The two-sided p-value is 0.75. There is not evidence of a difference between mean expenditures in Hispanics and White non-Hispanics ages 13-17.

|  | Ethnicity | n | $\overline{x}$ | s |
| --- | --- | --- | --- | --- |
| 1 | Hispanic | 103 | 3955.28 | 938.82 |
| 2 | White not Hispanic | 67 | 3904.36 | 1071.02 |

Figure 5.17: Summary statistics for expenditures, Ages 13-17.

The analysis of the age cohort 22 - 50 years shows the same qualitative result. The t-statistic calculated from the summary statistics in Figure 5.18 has value t = 0.659 and p-value 0.51. Just as in the 13-17 age cohort, there is insufficient evidence to reject the null hypothesis of no difference between the means.

|  | Ethnicity | n | $\overline{x}$ | s |
| --- | --- | --- | --- | --- |
| 1 | Hispanic | 43 | 40924.12 | 6467.09 |
| 2 | White not Hispanic | 133 | 40187.62 | 6081.33 |

Figure 5.18: Summary statistics for expenditures, Ages 22 - 50.

The inference-based analyses for these two age cohorts support the conclusions reached through the exploratory approach used in Section 1.7.1—comparing individuals of similar ages shows that there are not large differences between mean expenditures for White non-Hispanics versus Hispanics. An analysis that accounts for age as a confounding variable does not suggest there is evidence of ethnic discrimination in developmental disability support provided by the State of California.

## 5.3.5 Pooled standard deviation estimate

Occasionally, two populations will have standard deviations that are so similar that they can be treated as identical. For example, historical data or a well-understood biological mechanism may justify this strong assumption. In such cases, it can be more precise to use a pooled standard deviation to make inferences about the difference in population means.

The **pooled standard deviation** of two groups uses data from both samples to estimate the common standard deviation and standard error. If there are good reasons to believe that the population standard deviations are equal, an improved estimate of the group variances can be obtained by pooling the data from the two groups:

$$
s _ {\mathrm{pooled}} ^ {2} = \frac {s _ {1} ^ {2} (n _ {1} - 1) + s _ {2} ^ {2} (n _ {2} - 1)}{n _ {1} + n _ {2} - 2},
$$

where $n _ { 1 }$ and $n _ { 2 }$ are the sample sizes, and $s _ { 1 }$ and $s _ { 2 }$ represent the sample standard deviations. In this setting, the t-statistic uses $s _ { \mathrm { p o o l e d } } ^ { 2 }$ in place of $s _ { 1 } ^ { 2 }$ and $s _ { 2 } ^ { 2 }$ in the standard error formula, and the degrees of freedom for the t−statistic is the sum of the degrees of freedom for the two sample variances:

$$
\mathrm{df} = (n _ {1} - 1) + (n _ {2} - 1) = n _ {1} + n _ {2} - 2.
$$

The t-statistic for testing the null hypothesis of no difference between population means becomes

$$
t = \frac {\overline {{x}} _ {1} - \overline {{x}} _ {2}}{s _ {\mathrm{pooled}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}}.
$$

The formula for the two-sided confidence interval for the difference in population means is

$$
(\overline {{x}} _ {1} - \overline {{x}} _ {2}) \pm t ^ {\star} \times s _ {\mathrm{pooled}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}},
$$

where $t ^ { \star }$ is the point on a t-distribution with $n _ { 1 }   +   n _ { 2 }   -   2$ degrees of freedom chosen according to the confidence coefficient.

The benefits of pooling the standard deviation are realized through obtaining a better estimate of the standard deviation for each group and using a larger degrees of freedom parameter for the tdistribution. Both of these changes may permit a more accurate model of the sampling distribution of $\overline { { x } } _ { 1 } - \overline { { x } } _ { 2 }$ , if the standard deviations of the two groups are indeed equal. In most applications, however, it is difficult to verify the assumption of equal population standard deviations, and thus safer to use the methods discussed in Sections 5.3.1 and 5.3.2.