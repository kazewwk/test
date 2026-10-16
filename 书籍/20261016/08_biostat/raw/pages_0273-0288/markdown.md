## 5.6. NOTES

Finally, the formula used to approximate degrees of freedom ν for the independent two-group t-test that does not assume equal variance is

$$
\nu = \frac {\left[ (s _ {1} ^ {2} / n _ {1}) + (s _ {2} ^ {2} / n _ {2}) \right] ^ {2}}{\left[ (s _ {1} ^ {2} / n _ {1}) ^ {2} / (n _ {1} - 1) + (s _ {2} ^ {2} / n _ {2}) ^ {2} / (n _ {2} - 1) \right]},
$$

where $n _ { 1 } , s _ { 1 }$ are the sample size and standard deviation for the first sample, and $n _ { 2 } , s _ { 2 }$ are the corresponding values for the second sample. Since ν is routinely provided in the output from statistical software, there is rarely any need to calculate it by hand. The approximate formula $\mathrm{df} = \min(n_1 - 1, n_2 - 1)$ always produces a smaller value for degrees of freedom and hence a larger p-value.

The labs for this chapter are structured around particularly important problems in practice: comparing two groups, such as a treatment and control group (Lab 1); assessing before starting a study whether a sample size is large enough to make it likely that important differences will be detected (Lab 2); comparing more than two groups using analysis of variance (Lab 3); controlling error rates when looking at many comparisons in a dataset (Lab 4); and thinking about hypothesis testing in the larger context of reproducibility (Lab 5). The first four labs provide guidance on how to conduct and interpret specific types of analyses. Students may find the last lab particularly useful in understanding the distinction between a p-value and other probabilities relevant in an inferential setting, such as power.

## 5.7 Exercises

## 5.7.1 Single-sample inference with the t-distribution

**5.1 Identify the critical** t. An independent random sample is selected from an approximately normal population with unknown standard deviation. Find the degrees of freedom and the critical t-value (t?) for the given sample size and confidence level.

(a) n = 6, CL = 90%
(c) n = 29, CL = 95%

**5.2 Find the p-value, Part I.** An independent random sample is selected from an approximately normal population with an unknown standard deviation. Find the p-value for the given sets of alternative hypothesis and test statistic, and determine if the null hypothesis would be rejected at α = 0.05.

(a) $H _ { A } : \mu > \mu _ { 0 } ,   n = 1 1 ,   T = 1 . 9 1$
(c) H<sub>A</sub> : µ , µ<sub>0</sub>, n = 7, T = 0.83

**5.3 Cutoff values.** The following are cutoff values for the upper 5% of a t-distribution with either degrees of freedom 10, 50, or 100: 2.23, 1.98, and 2.01. Identify which value belongs to which distribution and explain your reasoning.

**5.4 Find the p-value, Part II.** An independent random sample is selected from an approximately normal population with an unknown standard deviation. Find the p-value for the given sets of alternative hypothesis and test statistic, and determine if the null hypothesis would be rejected at α = 0.01.

(a) H<sub>A</sub> : µ > 0.5, n = 26, T = 2.485
(b) H<sub>A</sub> : µ < 3, n = 18, T = 0.5

**5.5 Working backwards, Part I.** A 95% confidence interval for a population mean, µ, is given as (18.985, 21.015). This confidence interval is based on a simple random sample of 36 observations. Calculate the sample mean and standard deviation. Assume that all conditions necessary for inference are satisfied. Use the t-distribution in any calculations.

**5.6 Working backwards, Part II.** A 90% confidence interval for a population mean is (65, 77). The population distribution is approximately normal and the population standard deviation is unknown. This confidence interval is based on a simple random sample of 25 observations. Calculate the sample mean, the margin of error, and the sample standard deviation.

**5.7 Sleep habits of New Yorkers.** New York is known as "the city that never sleeps". A random sample of 25 New Yorkers were asked how much sleep they get per night. Statistical summaries of these data are shown below. Do these data provide strong evidence that New Yorkers sleep less than 8 hours a night on average?

| n | $\bar{x}$ | s | min | max |
| --- | --- | --- | --- | --- |
| 25 | 7.73 | 0.77 | 6.17 | 9.78 |

(a) Write the hypotheses in symbols and in words.
(b) Check conditions, then calculate the test statistic, T , and the associated degrees of freedom.
(c) Find and interpret the p-value in this context. Drawing a picture may be helpful.
(d) What is the conclusion of the hypothesis test?
(e) If you were to construct a 90% confidence interval that corresponded to this hypothesis test, would you expect 8 hours to be in the interval?

**5.8 Heights of adults.** Researchers studying anthropometry collected body girth measurements and skeletal diameter measurements, as well as age, weight, height and gender, for 507 physically active individuals. The histogram below shows the sample distribution of heights in centimeters.<sup>24</sup>

![](images/page_274_chart_11.jpg)

<details>
<summary>histogram</summary>

| Metric | Value |
| --- | --- |
| Min | 147.2 |
| Q1 | 163.8 |
| Median | 170.3 |
| Mean | 171.1 |
| SD | 9.4 |
| Q3 | 177.8 |
| Max | 198.1 |
</details>

(a) What is the point estimate for the average height of active individuals? What about the median?
(b) What is the point estimate for the standard deviation of the heights of active individuals? What about the IQR?
(c) Is a person who is 1m 80cm (180 cm) tall considered unusually tall? And is a person who is 1m 55cm (155cm) considered unusually short? Explain your reasoning.
(d) The researchers take another random sample of physically active individuals. Would you expect the mean and the standard deviation of this new sample to be the ones given above? Explain your reasoning.
(e) The sample means obtained are point estimates for the mean height of all active individuals, if the sample of individuals is equivalent to a simple random sample. What measure do we use to quantify the variability of such an estimate? Compute this quantity using the data from the original sample under the condition that the data are a simple random sample.

**5.9 Find the mean.** You are given the following hypotheses:

$$
H _ {0}: \mu = 6 0
$$

$$
H _ {A}: \mu <   6 0
$$

We know that the sample standard deviation is 8 and the sample size is 20. For what sample mean would the p-value be equal to 0.05? Assume that all conditions necessary for inference are satisfied.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">24<sub>G</sub>. Heinz et al. “[Exploring relationships in body dimensions](http://www.openintro.org/redirect.php?go=textbook-body_dim_2003&referrer=biostat1_pdf)”. In: Journal of Statistics Education 11.2 (2003).</span></small>

**5.10** $t ^ { \star }$ **vs.** $z ^ { \star }$ . For a given confidence level, $t _ { d f } ^ { \star }$ is larger than $z ^ { \star }$ . Explain how $t _ { d f } ^ { * }$ being slightly larger than $z ^ { * }$ affects the width of the confidence interval.
**5.11 Play the piano.** Georgianna claims that in a small city renowned for its music school, the average child takes less than 5 years of piano lessons. We have a random sample of 20 children from the city, with a mean of 4.6 years of piano lessons and a standard deviation of 2.2 years.

(a) Evaluate Georgianna’s claim using a hypothesis test.
(b) Construct a 95% confidence interval for the number of years students in this city take piano lessons, and interpret it in context of the data.
(c) Do your results from the hypothesis test and the confidence interval agree? Explain your reasoning.

**5.12 Auto exhaust and lead exposure.** Researchers interested in lead exposure due to car exhaust sampled the blood of 52 police officers subjected to constant inhalation of automobile exhaust fumes while working traffic enforcement in a primarily urban environment. The blood samples of these officers had an average lead concentration of 124.32 µg/l and a SD of 37.74 µg/l; a previous study of individuals from a nearby suburb, with no history of exposure, found an average blood level concentration of 35 $\mu \mathrm { g } / \mathrm { 1 . } ^ { 2 5 }$

(a) Write down the hypotheses that would be appropriate for testing if the police officers appear to have been exposed to a higher concentration of lead.
(b) Explicitly state and check all conditions necessary for inference on these data.
(c) Test the hypothesis that the downtown police officers have a higher lead exposure than the group in the previous study. Interpret your results in context.
(d) Based on your preceding result, without performing a calculation, would a 99% confidence interval for the average blood concentration level of police officers contain 35 µg/l?
(e) Based on your preceding result, without performing a calculation, would a 99% confidence interval for this difference contain 0? Explain why or why not.

**5.13 Car insurance savings.** A market researcher wants to evaluate car insurance savings at a competing company. Based on past studies he is assuming that the standard deviation of savings is \$100. He wants to collect data such that he can get a margin of error of no more than \$10 at a 95% confidence level. How large of a sample should he collect?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">25<sub>WI</sub> Mortada et al. “Study of lead exposure from automobile exhaust as a risk for nephrotoxicity among traffic policemen.” In: American journal of nephrology 21.4 (2000), pp. 274–279.</span></small>

## 5.7.2 Two-sample test for paired data

**5.14 Air quality.** Air quality measurements were collected in a random sample of 25 country capitals in 2013, and then again in the same cities in 2014. We would like to use these data to compare average air quality between the two years. Should we use a paired or non-paired test? Explain your reasoning.

**5.15 Paired or not, Part I.** In each of the following scenarios, determine if the data are paired.

(a) Compare pre- (beginning of semester) and post-test (end of semester) scores of students.
(b) Assess gender-related salary gap by comparing salaries of randomly sampled men and women.
(c) Compare artery thicknesses at the beginning of a study and after 2 years of taking Vitamin E for the same group of patients.
(d) Assess effectiveness of a diet regimen by comparing the before and after weights of subjects.

**5.16 Paired or not, Part II.** In each of the following scenarios, determine if the data are paired.

(a) We would like to know if Intel’s stock and Southwest Airlines’ stock have similar rates of return. To find out, we take a random sample of 50 days, and record Intel’s and Southwest’s stock on those same days.
(b) We randomly sample 50 items from Target stores and note the price for each. Then we visit Walmart and collect the price for each of those same 50 items.
(c) A school board would like to determine whether there is a difference in average SAT scores for students at one high school versus another high school in the district. To check, they take a simple random sample of 100 students from each high school.

**5.17 Global warming, Part I.** Let’s consider a limited set of climate data, examining temperature differences in 1948 vs 2018. We sampled 197 locations from the National Oceanic and Atmospheric Administration’s (NOAA) historical data, where the data was available for both years of interest. We want to know: were there more days with temperatures exceeding 90°F in 2018 or in 1948?<sup>26</sup> The difference in number of days exceeding 90°F (number of days in 2018 - number of days in 1948) was calculated for each of the 197 locations. The average of these differences was 2.9 days with a standard deviation of 17.2 days. We are interested in determining whether these data provide strong evidence that there were more days in 2018 that exceeded 90°F from NOAA’s weather stations.

(a) Is there a relationship between the observations collected in 1948 and 2018? Or are the observations in the two groups independent? Explain.
(b) Write hypotheses for this research in symbols and in words.
(c) Check the conditions required to complete this test. A histogram of the differences is given to the right.
(d) Calculate the test statistic and find the p-value.
(e) Use α = 0.05 to evaluate the test, and interpret your conclusion in context.
(f) What type of error might we have made? Explain in context what the error means.
(g) Based on the results of this hypothesis test, would you expect a confidence interval for the average difference between the number of days exceeding 90°F from 1948 and 2018 to include 0? Explain your reasoning.

![](images/page_276_chart_24.jpg)

<details>
<summary>histogram</summary>

| Bin (Range) | Frequency |
| --- | --- |
| -70~-65 | ~1 |
| -40~-35 | ~6 |
| -35~-30 | ~15 |
| -30~-25 | ~11 |
| -25~-20 | ~53 |
| -20~-15 | ~57 |
| -15~-10 | ~25 |
| -10~-5 | ~16 |
| -5~0 | ~10 |
| 0~5 | ~2 |
| 5~10 | ~1 |
</details>

Differences in Number of Days

**5.18 High School and Beyond, Part I.** The National Center of Education Statistics conducted a survey of high school seniors, collecting test data on reading, writing, and several other subjects. Here we examine a simple random sample of 200 students from this survey. Side-by-side box plots of reading and writing scores as well as a histogram of the differences in scores are shown below.

![](images/page_277_image_3.jpg)

(a) Is there a clear difference in the average reading and writing scores?
(b) Are the reading and writing scores of each student independent of each other?
(c) The average observed difference in scores is $\bar { x } _ { r e a d - w r i t e } = - 0 . 5 4 5 ,$ and the standard deviation of the differences is 8.887 points. Do these data provide convincing evidence of a difference between the average scores on the two exams? Conduct a hypothesis test; interpret your conclusions in context.
(d) Based on the results of this hypothesis test, would you expect a confidence interval for the average difference between the reading and writing scores to include 0? Explain your reasoning.

**5.19 Global warming, Part II.** We considered the change in the number of days exceeding 90°F from 1948 and 2018 at 197 randomly sampled locations from the NOAA database in Exercise 5.17. The mean and standard deviation of the reported differences are 2.9 days and 17.2 days.

(a) Calculate a 90% confidence interval for the average difference between number of days exceeding 90°F between 1948 and 2018. We’ve already checked the conditions for you.
(b) Interpret the interval in context.
(c) Does the confidence interval provide convincing evidence that there were more days exceeding 90°F in 2018 than in 1948 at NOAA stations? Explain.

**5.20 High school and beyond, Part II.** We considered the differences between the reading and writing scores of a random sample of 200 students who took the High School and Beyond Survey in Exercise 5.18. The mean and standard deviation of the differences are $\bar { x } _ { r e a d - w r i t e } = - 0 . 5 4 5$ and 8.887 points.

(a) Calculate a 95% confidence interval for the average difference between the reading and writing scores of all students.
(b) Interpret this interval in context.
(c) Does the confidence interval provide convincing evidence that there is a real difference in the average scores? Explain.

**5.21 Gifted children.** Researchers collected a simple random sample of 36 children who had been identified as gifted in a large city. The following histograms show the distributions of the IQ scores of mothers and fathers of these children. Also provided are some sample statistics.<sup>27</sup>

![](images/page_278_image_3.jpg)

|  | Mother | Father | Diff. |
| --- | --- | --- | --- |
| Mean | 118.2 | 114.8 | 3.4 |
| SD | 6.5 | 3.5 | 7.5 |
| n | 36 | 36 | 36 |

(a) Are the IQs of mothers and the IQs of fathers in this data set related? Explain.
(b) Conduct a hypothesis test to evaluate if the scores are equal on average. Make sure to clearly state your hypotheses, check the relevant conditions, and state your conclusion in the context of the data.

**5.22 DDT exposure.** Suppose that you are interested in determining whether exposure to the organochloride DDT, which has been used extensively as an insecticide for many years, is associated with breast cancer in women. As part of a study that investigated this issue, blood was drawn from a sample of women diagnosed with breast cancer over a six-year period and a sample of healthy control subjects matched to the cancer patients on age, menopausal status, and date of blood donation. Each woman’s blood level of DDE (an important byproduct of DDT in the human body) was measured, and the difference in levels for each patient and her matched control calculated. A sample of 171 such differences has mean $\overline{d} = 2.7    ng/mL$ and standard deviation $s_{d}=15.9    ng/mL$ . Differences were calculated as $D D E _ { c a n c e r } - D D E _ { c o n t r o l }$

(a) Test the null hypothesis that the mean blood levels of DDE are identical for women with breast cancer and for healthy control subjects. What do you conclude?
(b) Would you expect a 95% confidence interval for the true difference in population mean DDE levels to contain the value 0?

**5.23 Blue-green eggshells.** It is hypothesized that the blue-green color of the eggshells of many avian species represents an informational signal as to the health of the female that laid the eggs. To investigate this hypothesis, researchers conducted a study in which birds assigned to the treatment group were provided with supplementary food before and during laying; they predict that if eggshell coloration is related to female health at laying, females given supplementary food will lay more intensely blue-green eggs than control females. Nests were paired according to when nest construction began, and the study examined 16 nest pairs.

(a) The blue-green chroma (BGC) of eggs was measured on the day of laying; BGC refers to the proportion of total reflectance that is in the blue-green region of the spectrum, with a higher value representing a deeper blue-green color. In the food supplemented group, BGC chroma had $\overline { { x } } = 0 . 5 9 4$ and $s = 0 . 0 1 0 ;$ in the control group, BGC chroma had $\overline { { x } } = 0 . 5 8 6$ and $s = 0 . 0 0 9$ . A paired t-test resulted in $t = 2 . 2 8$ and $p = 0 . 0 3 8$ . Interpret the results in the context of the data.

(b) In general, healthier birds are also known to lay heavier eggs. Egg mass was also measured for both groups. In the food supplemented group, egg mass had $\overline { { x } } = 1 . 7 0$ grams and $s = 0 . 1 1$ grams; in the control group, egg mass had $\overline { { x } } = 0 . 5 8 6$ grams and $s = 0 . 0 0 9$ grams. The test statistic from a paired t-test was 2.64 with p-value 0.019. Compute and interpret a 95% confidence interval for δ, the population mean difference in egg mass between the groups.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">27<sub>F</sub>.A. Graybill and H.K. Iyer. Regression Analysis: Concepts and Applications. Duxbury Press, 1994, pp. 511–516.</span></small>

## 5.7.3 Two-sample test for independent data

**5.24 Diamond prices, Part I.** A diamond’s price is determined by various measures of quality, including carat weight. The price of diamonds increases as carat weight increases. While the difference between the size of a 0.99 carat diamond and a 1 carat diamond is undetectable to the human eye, the price difference can be substantial.<sup>28</sup>

|  | 0.99 carats | 1 carat |
| --- | --- | --- |
| Mean | $ 44.51 | $ 56.81 |
| SD | $ 13.32 | $ 16.13 |
| n | 23 | 23 |

![](images/page_279_chart_5.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 | Min | Max |
| --- | --- | --- | --- | --- | --- |
| 0.99 carats | ~35 | ~48 | ~56 | ~18 | ~62 |
| 1 carat | ~45 | ~53 | ~73 | ~33 | ~87 |
</details>

(a) Use the data to assess whether there is a difference between the average standardized prices of 0.99 and 1 carat diamonds.
(b) Construct a 95% confidence interval for the average difference between the standardized prices of 0.99 and 1 carat diamonds.

**5.25 Friday the** $1 3 ^ { \mathrm { t h } }$ **, Part I.** In the early 1990’s, researchers in the UK collected data on traffic flow, number of shoppers, and traffic accident related emergency room admissions on Friday the $1 3 ^ { \mathrm { t h } }$ and the previous Friday, Friday the $6 ^ { \mathrm { t h } }$ . The histograms below show the distribution of number of cars passing by a specific intersection on Friday the $6 ^ { \mathrm { t h } }$ and Friday the $1 3 ^ { \mathrm { t h } }$ for many such date pairs. Also given are some sample statistics, where the difference is the number of cars on the $6 ^ { \mathrm { t h } }$ minus the number of cars on the $1 3 ^ { \mathrm { t h } } ,$ th.29

![](images/page_279_chart_10.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --- | --- |
| <115000 | 1 |
| 115000~120000 | 4 |
| 120000~125000 | 1 |
| 125000~130000 | 2 |
| 130000~135000 | 2 |
| 135000~140000 | 2 |
</details>

Friday the 6th

![](images/page_279_chart_12.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --- | --- |
| <115000 | 2 |
| 115000~120000 | 3 |
| 120000~125000 | 1 |
| 125000~130000 | 2 |
| 130000~135000 | 2 |
| 135000~140000 | 2 |
</details>

Friday the 13th

![](images/page_279_chart_14.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --- | --- |
| 0~1000 | 2 |
| 1000~2000 | 5 |
| 2000~3000 | 2 |
| 4000~5000 | 1 |
</details>

Difference

|  | $6^{th}$ | $13^{th}$ | Diff. |
| --- | --- | --- | --- |
| $\bar{x}$ | 128,385 | 126,550 | 1,835 |
| $s$ | 7,259 | 7,664 | 1,176 |
| $n$ | 10 | 10 | 10 |

(a) Are there any underlying structures in these data that should be considered in an analysis? Explain.
(b) What are the hypotheses for evaluating whether the number of people out on Friday the $6 ^ { \mathrm { t h } }$ is different than the number out on Friday the $1 3 ^ { \mathrm { t h } } ?$
(c) Check conditions to carry out the hypothesis test from part (b).
(d) Calculate the test statistic and the p-value.
(e) What is the conclusion of the hypothesis test?
(f) Interpret the p-value in this context.
(g) What type of error might have been made in the conclusion of your test? Explain.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">28<sub>H</sub>. Wickham. [ggplot2: elegant graphics for data analysis](http://www.openintro.org/redirect.php?go=textbook-ggplot2_book&referrer=biostat1_pdf). Springer New York, 2009.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">29<sub>T</sub>.J. Scanlon et al. “[Is Friday the 13th Bad For Your Health?](http://www.openintro.org/redirect.php?go=textbook-Friday13_1993&referrer=biostat1_pdf)” In: BMJ 307 (1993), pp. 1584–1586.</span></small>

**5.26 Egg volume.** In a study examining 131 collared flycatcher eggs, researchers measured various characteristics in order to study their relationship to egg size (assayed as egg volume, in $m m ^ { 3 } )$ . These characteristics included nestling sex and survival. A single pair of collared flycatchers generally lays around 6 eggs per breeding season; laying order of the eggs was also recorded.

(a) Is there evidence at the $\alpha = 0 . 1 0$ significance level to suggest that egg size differs between male and female chicks? If so, do heavier eggs tend to contain males or females? For male chicks, $\overline { { x } } = 1 6 1 9 . 9 5 ,   s = 1 2 7 . 5 4 ,$ and $n = 8 0$ . For female chicks, $\overline { { x } } = 1 5 8 4 . 2 0 ,   s = 1 0 2 . 5 1$ , and $n = 4 8 .$ . Sex was only recorded for eggs that hatched.
(b) Construct a 95% confidence interval for the difference in egg size between chicks that successfully fledged (developed capacity to $\mathrm { f l y ) }$ and chicks that died in the nest. From the interval, is there evidence of a size difference in eggs between these two groups? For chicks that fledged, $\overline { { x } } = 1 6 0 5 . 8 7 ,   s = 1 2 6 . 3 2$ , and $n = 8 9$ For chicks that died in the nest, $\overline{x}=1606.91,s=103.46,n=42$
(c) Are eggs that are laid first a significantly different size compared to eggs that are laid sixth? For eggs laid first, $\overline { { x } } = 1 5 8 1 . 9 8 ,   s = 1 5 5 . 9 5$ , and $n = 2 2$ . For eggs laid sixth, $\overline { { x } } = 1 6 5 9 . 6 2 ,   s = 1 2 4 . 5 9$ , and $n = 2 0$

**5.27 Friday the** $1 3 ^ { \mathrm { t h } }$ **, Part II.** The Friday the $1 3 ^ { t h }$ study reported in Exercise 5.25 also provides data on traffic accident related emergency room admissions. The distributions of these counts from Friday the $6 ^ { \mathrm { t h } }$ and Friday the $1 3 ^ { \mathrm { t h } }$ are shown below for six such paired dates along with summary statistics. You may assume that conditions for inference are met.

![](images/page_280_chart_8.jpg)

<details>
<summary>bar</summary>

| Category | Value |
| --- | --- |
| 5 | 1 |
| 5 | 2 |
| 10 | 1 |
| 10 | 2 |
</details>

Friday the 6th

![](images/page_280_chart_10.jpg)

<details>
<summary>histogram</summary>

| Category | Value |
| --- | --- |
| 5 | 1 |
| 10 | 1 |
| 12 | 2 |
| 14 | 2 |
</details>

Friday the 13th

![](images/page_280_chart_12.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --- | --- |
| -8~-6 | 2 |
| -6~-4 | 1 |
| -4~-2 | 1 |
| -2~0 | 1 |
| 0~2 | 1 |
</details>

Difference

|  | $6^{th}$ | $13^{th}$ | diff |
| --- | --- | --- | --- |
| Mean | 7.5 | 10.83 | -3.33 |
| SD | 3.33 | 3.6 | 3.01 |
| n | 6 | 6 | 6 |

(a) Conduct a hypothesis test to evaluate if there is a difference between the average numbers of traffic accident related emergency room admissions between Friday the $6 ^ { \mathrm { t h } }$ and Friday the $1 3 ^ { \mathrm { t h } }$
(b) Calculate a 95% confidence interval for the difference between the average numbers of traffic accident related emergency room admissions between Friday the $6 ^ { \mathrm { t h } }$ and Friday the $1 3 ^ { \mathrm { t h } }$
(c) The conclusion of the original study states, “Friday 13th is unlucky for some. The risk of hospital ad mission as a result of a transport accident may be increased by as much as 52%. Staying at home is recommended.” Do you agree with this statement? Explain your reasoning.

**5.28 Avian influenza, Part I.** In recent years, widespread outbreaks of avian influenza have posed a global threat to both poultry production and human health. One strategy being explored by researchers involves developing chickens that are genetically resistant to infection. In 2011, a team of investigators reported in Science that they had successfully generated transgenic chickens that are resistant to the virus. As a part of assessing whether the genetic modification might be hazardous to the health of the chicks, hatch weights between transgenic chicks and non-transgenic chicks were collected. Does the following data suggest that there <u>is a difference in hatch weights between transgenic and</u> non-transgenic chickens?

|  | transgenic chicks (g) | non-transgenic chicks (g) |
| --- | --- | --- |
| $\bar{x}$ | 45.14 | 44.99 |
| s | 3.32 | 4.57 |
| n | 54 | 54 |

**5.29 Chicken diet and weight, Part I.** Chicken farming is a multi-billion dollar industry, and any methods that increase the growth rate of young chicks can reduce consumer costs while increasing company profits, possibly by millions of dollars. An experiment was conducted to measure and compare the effectiveness of various feed supplements on the growth rate of chickens. Newly hatched chicks were randomly allocated into six groups, and each group was given a different feed supplement. Below are some summary statistics from this data set along with box plots showing the distribution of weights by feed type.<sup>30</sup>

![](images/page_281_chart_5.jpg)

<details>
<summary>boxplot</summary>

| Category | Min | Q1 | Q2 (Median) | Q3 | Max |
| --- | --- | --- | --- | --- | --- |
| casein | ~217 | ~278 | ~342 | ~370 | ~405 |
| horsebean | ~109 | ~139 | ~152 | ~177 | ~227 |
| linseed | ~142 | ~179 | ~222 | ~259 | ~309 |
| meatmeal | ~154 | ~251 | ~264 | ~320 | ~380 |
| soybean | ~159 | ~207 | ~249 | ~270 | ~329 |
| sunflower | ~295 | ~314 | ~328 | ~341 | ~341 |
</details>

|  | Mean | SD | n |
| --- | --- | --- | --- |
| casein | 323.58 | 64.43 | 12 |
| horsebean | 160.20 | 38.63 | 10 |
| linseed | 218.75 | 52.24 | 12 |
| meatmeal | 276.91 | 64.90 | 11 |
| soybean | 246.43 | 54.13 | 14 |
| sunflower | 328.92 | 48.84 | 12 |

(a) Describe the distributions of weights of chickens that were fed linseed and horsebean.

(b) Do these data provide strong evidence that the average weights of chickens that were fed linseed and horsebean are different? Use a 5% significance level.

(c) What type of error might we have committed? Explain.

(d) Would your conclusion change if we used $\alpha = 0 . 0 1 ?$

**5.30 Fuel efficiency of manual and automatic cars, Part I.** Each year the US Environmental Protection Agency (EPA) releases fuel economy data on cars manufactured in that year. Below are summary statistics on fuel efficiency (in miles/gallon) from random samples of cars with manual and automatic transmissions manufactured in 2012. Do these data provide strong evidence of a difference between the average fuel efficiency of cars with manual and automatic transmissions in terms of their average city mileage? Assume that conditions for inference are satisfied.<sup>31</sup>

<table><tr><td></td><td colspan="2">City MPG</td></tr><tr><td></td><td>Automatic</td><td>Manual</td></tr><tr><td>Mean</td><td>16.12</td><td>19.85</td></tr><tr><td>SD</td><td>3.58</td><td>4.51</td></tr><tr><td>n</td><td>26</td><td>26</td></tr></table>

![](images/page_281_chart_14.jpg)

<details>
<summary>boxplot</summary>

| Category | Min | Q1 | Median (Q2) | Q3 | Max |
| --- | --- | --- | --- | --- | --- |
| automatic | ~10 | ~14.5 | ~16 | ~19 | ~23 |
| manual | ~10 | ~17 | ~20 | ~23 | ~30 |
</details>

City MPG

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">30<a href="http://www.openintro.org/redirect.php?go=textbook-feed_and_chicken_weights&amp;referrer=biostat1_pdf"><sub>Chicken</sub> Weights by Feed Type</a>, from the datasets package in R..</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">31<sub>U</sub>.S. Department of Energy, [Fuel Economy Data, 2012 Datafile](http://www.openintro.org/redirect.php?go=textbook-fuel_economy_data_2012&referrer=biostat1_pdf).</span></small>

**5.31 Chicken diet and weight, Part II.** Casein is a common weight gain supplement for humans. Does it have an effect on chickens? Using data provided in Exercise 5.29, test the hypothesis that the average weight of chickens that were fed casein is different than the average weight of chickens that were fed soybean. If your hypothesis test yields a statistically significant result, discuss whether or not the higher average weight of chickens can be attributed to the casein diet. Assume that conditions for inference are satisfied.

**5.32 Fuel efficiency of manual and automatic cars, Part II.** The table provides summary statistics on highway fuel economy of cars manufactured in 2012 (from Exercise 5.30). Use these statistics to calculate a 98% confidence interval for the difference between average highway mileage of manual and automatic cars, and interpret this interval in the context of the data.<sup>32</sup>

<table><tr><td></td><td colspan="2">Hwy MPG</td></tr><tr><td></td><td>Automatic</td><td>Manual</td></tr><tr><td>Mean</td><td>22.92</td><td>27.88</td></tr><tr><td>SD</td><td>5.29</td><td>5.01</td></tr><tr><td>n</td><td>26</td><td>26</td></tr></table>

![](images/page_282_chart_5.jpg)

<details>
<summary>boxplot</summary>

| Category | Min | Q1 | Median (Q2) | Q3 | Max |
| --- | --- | --- | --- | --- | --- |
| automatic | ~14.5 | ~19.5 | ~23.5 | ~26 | ~34 |
| manual | ~17 | ~25 | ~28 | ~31 | ~38 |
</details>

**5.33 Gaming and distracted eating.** A group of researchers are interested in the possible effects of distracting stimuli during eating, such as an increase or decrease in the amount of food consumption. To test this hypothesis, they monitored food intake for a group of 44 patients who were randomized into two equal groups. The treatment group ate lunch while playing solitaire, and the control group ate lunch without any added distractions. Patients in the treatment group ate 52.1 grams of biscuits, with a standard deviation of 45.1 grams, and patients in the control group ate 27.1 grams of biscuits, with a standard deviation of 26.4 grams. Do these data provide convincing evidence that the average food intake (measured in amount of biscuits consumed) is different for the patients in the treatment group? Assume that conditions for inference are satisfied.<sup>33</sup>

**5.34 Placebos without deception.** While placebo treatment can influence subjective symptoms, it is typically believed that patient response to placebo requires concealment or deception; in other words, a patient must believe that they are receiving an effective treatment in order to experience the benefits of being treated with an inert substance. Researchers recruited patients suffering from irritable bowel syndrome (IBS) to test whether placebo responses are neutralized by awareness that the treatment is a placebo.

Patients were randomly assigned to either the treatment arm or control arm. Those in the treatment arm were given placebo pills, which were described as "something like sugar pills, which have been shown in rigorous clinical testing to produce significant mind-body self-healing processes". Those in the control arm did not receive treatment. At the end of the study, all participants answered a questionnaire called the IBS Global Improvement Scale (IBS-GIS) which measures whether IBS symptoms have improved; higher scores are indicative of more improvement.

At the end of the study, the 37 participants in the open placebo group had IBS-GIS scores with $\overline { { x } } = 5 . 0$ and $s = 1 . 5 ,$ while the 43 participants in the no treatment group had IBS-GIS scores with $\overline { { x } } = 3 . 9$ and $s = 1 . 3$

Based on an analysis of the data, summarize whether the study demonstrates evidence that placebos administered without deception may be an effective treatment for IBS.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">32<sub>U</sub>.S. Department of Energy, [Fuel Economy Data, 2012 Datafile](http://www.openintro.org/redirect.php?go=textbook-fuel_economy_data_2012&referrer=biostat1_pdf).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">33<sub>R</sub>.E. Oldham-Cooper et al. “[Playing a computer game during lunch affects fullness, memory for lunch, and later snack intake](http://www.openintro.org/redirect.php?go=textbook-playing_computer_games_2011&referrer=biostat1_pdf)”. In: The American Journal of Clinical Nutrition 93.2 (2011), p. 308.</span></small>

**5.35 Prison isolation experiment, Part I.** Subjects from Central Prison in Raleigh, NC, volunteered for an experiment involving an “isolation” experience. The goal of the experiment was to find a treatment that reduces subjects’ psychopathic deviant T scores. This score measures a person’s need for control or their rebellion against control, and it is part of a commonly used mental health test called the Minnesota Multiphasic Personality Inventory (MMPI) test. The experiment had three treatment groups:

(1) Four hours of sensory restriction plus a 15 minute “therapeutic" tape advising that professional help is available.
(2) Four hours of sensory restriction plus a 15 minute “emotionally neutral” tape on training hunting dogs.
(3) Four hours of sensory restriction but no taped message.

Forty-two subjects were randomly assigned to these treatment groups, and an MMPI test was administered before and after the treatment. Distributions of the differences between pre and post treatment scores (pre - post) are shown below, along with some sample statistics. Use this information to independently test the effectiveness of each treatment. Make sure to clearly state your hypotheses, check conditions, and interpret results in the context of the data.<sup>34</sup>

![](images/page_283_chart_8.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --- | --- |
| -10~0 | 7 |
| 0~10 | 2 |
| 10~20 | 4 |
| 30~40 | 1 |
</details>

Treatment 1

![](images/page_283_chart_10.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --- | --- |
| -20~-15 | 1 |
| -15~-10 | 0 |
| -10~-5 | 1 |
| -5~0 | 2 |
| 0~5 | 5 |
| 5~10 | 4 |
| 10~15 | 0 |
| 15~20 | 1 |
</details>

Treatment 2

![](images/page_283_chart_12.jpg)

<details>
<summary>histogram</summary>

| Bin Range | Frequency |
| --- | --- |
| -25~-20 | 2 |
| -15~-10 | 1 |
| -10~-5 | 1 |
| -5~0 | 5 |
| 0~5 | 5 |
</details>

Treatment 3

|  | Tr 1 | Tr 2 | Tr 3 |
| --- | --- | --- | --- |
| Mean | 6.21 | 2.86 | -3.21 |
| SD | 12.3 | 7.94 | 8.57 |
| n | 14 | 14 | 14 |

## 5.7.4 Power calculations for a difference of means

**5.36 Email outreach efforts.** A medical research group is recruiting people to complete short surveys about their medical history. For example, one survey asks for information on a person’s family history in regards to cancer. Another survey asks about what topics were discussed during the person’s last visit to a hospital. So far, as people sign up, they complete an average of just 4 surveys, and the standard deviation of the number of surveys is about 2.2. The research group wants to try a new interface that they think will encourage new enrollees to complete more surveys, where they will randomize each enrollee to either get the new interface or the current interface. How many new enrollees do they need for each interface to detect an effect size of 0.5 surveys per enrollee, if the desired power level is 80%?

**5.37 Increasing corn yield.** A large farm wants to try out a new type of fertilizer to evaluate whether it will improve the farm’s corn production. The land is broken into plots that produce an average of 1,215 pounds of corn with a standard deviation of 94 pounds per plot. The owner is interested in detecting any average difference of at least 40 pounds per plot. How many plots of land would be needed for the experiment if the desired power level is 90%? Assume each plot of land gets treated with either the current fertilizer or the new fertilizer.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">34<a href="http://www.openintro.org/redirect.php?go=textbook-prison_isolation_exp&amp;referrer=biostat1_pdf"><sub>Prison</sub> isolation experiment, stat.duke.edu/resources/datasets/prison-isolation</a>.</span></small>

## 5.7.5 Comparing means with ANOVA

**5.38 Fill in the blank.** When doing an ANOVA, you observe large differences in means between groups. Within the ANOVA framework, this would most likely be interpreted as evidence strongly favoring the hypothesis.
**5.39 Chicken diet and weight, Part III.** In Exercises 5.29 and 5.31 we compared the effects of two types of feed at a time. A better analysis would first consider all feed types at once: casein, horsebean, linseed, meat meal, soybean, and sunflower. The ANOVA output below can be used to test for differences between the average weights of chicks on different diets.

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| feed | 5 | 231,129.16 | 46,225.83 | 15.36 | 0.0000 |
| Residuals | 65 | 195,556.02 | 3,008.55 |  |  |

Conduct a hypothesis test to determine if these data provide convincing evidence that the average weight of chicks varies across some (or all) groups. Make sure to check relevant conditions. Figures and summary statistics are shown below.

![](images/page_284_chart_8.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 | IQR |
| --- | --- | --- | --- | --- |
| casein | ~278 | ~342 | ~372 | ~104 |
| horsebean | ~138 | ~152 | ~178 | ~40 |
| linseed | ~180 | ~222 | ~258 | ~78 |
| meatmeal | ~250 | ~264 | ~320 | ~70 |
| soybean | ~208 | ~248 | ~270 | ~62 |
| sunflower | ~312 | ~330 | ~342 | ~20 |
</details>

|  | Mean | SD | n |
| --- | --- | --- | --- |
| casein | 323.58 | 64.43 | 12 |
| horsebean | 160.20 | 38.63 | 10 |
| linseed | 218.75 | 52.24 | 12 |
| meatmeal | 276.91 | 64.90 | 11 |
| soybean | 246.43 | 54.13 | 14 |
| sunflower | 328.92 | 48.84 | 12 |

**5.40 Teaching descriptive statistics.** A study compared five different methods for teaching descriptive statistics. The five methods were traditional lecture and discussion, programmed textbook instruction, programmed text with lectures, computer instruction, and computer instruction with lectures. 45 students were randomly assigned, 9 to each method. After completing the course, students took a 1-hour exam.

(a) What are the hypotheses for evaluating if the average test scores are different for the different teaching methods?
(b) What are the degrees of freedom associated with the F-test for evaluating these hypotheses?
(c) Suppose the p-value for this test is 0.0168. What is the conclusion?

**5.41 Coffee, depression, and physical activity.** Caffeine is the world’s most widely used stimulant, with approximately 80% consumed in the form of coffee. Participants in a study investigating the relationship between coffee consumption and exercise were asked to report the number of hours they spent per week on moderate (e.g., brisk walking) and vigorous (e.g., strenuous sports and jogging) exercise. Based on these data the researchers estimated the total hours of metabolic equivalent tasks (MET) per week, a value always greater than 0. The table below gives summary statistics of MET for women in this study based on the amount of coffee consumed.35

Caffeinated coffee consumption

|  | ≤ 1 cup/week | 2-6 cups/week | 1 cup/day | 2-3 cups/day | ≥ 4 cups/day | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Mean | 18.7 | 19.6 | 19.3 | 18.9 | 17.5 |  |
| SD | 21.1 | 25.5 | 22.5 | 22.0 | 22.0 |  |
| n | 12,215 | 6,617 | 17,234 | 12,290 | 2,383 | 50,739 |

(a) Write the hypotheses for evaluating if the average physical activity level varies among the different levels of coffee consumption.

(b) Check conditions and describe any assumptions you must make to proceed with the test.

(c) Below is part of the output associated with this test. Fill in the empty cells.

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| coffee |  |  |  |  | 0.0003 |
| Residuals |  | 25,564,819 |  |  |  |
| Total |  | 25,575,327 |  |  |  |

(d) What is the conclusion of the test?

**5.42 Student performance across discussion sections.** A professor who teaches a large introductory statistics class (197 students) with eight discussion sections would like to test if student performance differs by discussion section, where each discussion section has a different teaching assistant. The summary table below shows the average final exam score for each discussion section as well as the standard deviation of scores and the number of students in each section.

|  | Sec 1 | Sec 2 | Sec 3 | Sec 4 | Sec 5 | Sec 6 | Sec 7 | Sec 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $n_i$ | 33 | 19 | 10 | 29 | 33 | 10 | 32 | 31 |
| $\bar{x}_i$ | 92.94 | 91.11 | 91.80 | 92.45 | 89.30 | 88.30 | 90.12 | 93.35 |
| $s_i$ | 4.21 | 5.58 | 3.43 | 5.92 | 9.32 | 7.27 | 6.93 | 4.57 |

The ANOVA output below can be used to test for differences between the average scores from the different discussion sections.

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| section | 7 | 525.01 | 75.00 | 1.87 | 0.0767 |
| Residuals | 189 | 7584.11 | 40.13 |  |  |

Conduct a hypothesis test to determine if these data provide convincing evidence that the average score varies across some (or all) groups. Check conditions and describe any assumptions you must make to proceed with the test.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">35<sub>M</sub>. Lucas et al. “[Coffee, caffeine, and risk of depression among women](http://www.openintro.org/redirect.php?go=textbook-coffee_caffeine_depression_2011&referrer=biostat1_pdf)”. In: Archives of internal medicine 171.17 (2011), p. 1571.</span></small>

**5.43 GPA and major.** Undergraduate students taking an introductory statistics course at Duke University conducted a survey about GPA and major. The side-by-side box plots show the distribution of GPA among three groups of majors. Also provided is the ANOVA output.

![](images/page_286_chart_3.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 | Min | Max |
| --- | --- | --- | --- | --- | --- |
| Arts and Humanities | ~3.3 | 3.6 | ~3.8 | ~3.1 | ~4.0 |
| Natural Sciences | ~3.4 | ~3.65 | ~3.8 | ~2.95 | ~4.0 |
| Social Sciences | ~3.4 | ~3.65 | ~3.8 | ~2.85 | ~4.0 |
</details>

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| major | 2 | 0.03 | 0.015 | 0.185 | 0.8313 |
| Residuals | 195 | 15.77 | 0.081 |  |  |

(a) Write the hypotheses for testing for a difference between average GPA across majors.
(b) What is the conclusion of the hypothesis test?
(c) How many students answered these questions on the survey, i.e. what is the sample size?

**5.44 Work hours and education.** The General Social Survey collects data on demographics, education, and work, among many other characteristics of US residents.<sup>36</sup> Using ANOVA, we can consider educational attainment levels for all 1,172 respondents at once. Below are the distributions of hours worked by educational attainment and relevant summary statistics that will be helpful in carrying out this analysis.

Educational attainment

|  | Less than HS | HS | Jr Coll | Bachelor's | Graduate | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Mean | 38.67 | 39.6 | 41.39 | 42.55 | 40.85 | 40.45 |
| SD | 15.81 | 14.97 | 18.1 | 13.62 | 15.51 | 15.17 |
| n | 121 | 546 | 97 | 253 | 155 | 1,172 |

![](images/page_286_chart_12.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 | IQR |
| --- | --- | --- | --- | --- |
| Less than HS | ~30 | 40 | ~46 | ~26 |
| HS | ~32 | 40 | ~48 | ~26 |
| Jr Coll | ~30 | 40 | 50 | ~20 |
| Bachelor's | 40 | 40 | 50 | 20 |
| Graduate | ~35 | 40 | 50 | ~25 |
</details>

(a) Write hypotheses for evaluating whether the average number of hours worked varies across the five groups.
(b) Check conditions and describe any assumptions you must make to proceed with the test.
(c) Below is part of the output associated with this test. Fill in the empty cells.

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| degree |  |  | 501.54 |  | 0.0682 |
| Residuals |  | 267,382 |  |  |  |
| Total |  |  |  |  |  |

(d) What is the conclusion of the test?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">36<sub>National</sub> Opinion Research Center, [General Social Survey, 2010](http://www.openintro.org/redirect.php?go=textbook-gss_2010&referrer=biostat1_pdf).</span></small>

**5.45 True / False: ANOVA, Part I.** Determine if the following statements are true or false in ANOVA, and explain your reasoning for statements you identify as false.

(a) As the number of groups increases, the modified significance level for pairwise tests increases as well.
(b) As the total sample size increases, the degrees of freedom for the residuals increases as well.
(c) The constant variance condition can be somewhat relaxed when the sample sizes are relatively consistent across groups.
(d) The independence assumption can be relaxed when the total sample size is large.

**5.46 Child care hours.** The China Health and Nutrition Survey aims to examine the effects of the health, nutrition, and family planning policies and programs implemented by national and local governments.<sup>37</sup> It, for example, collects information on number of hours Chinese parents spend taking care of their children under age 6. The side-by-side box plots below show the distribution of this variable by educational attainment of the parent. Also provided below is the ANOVA output for comparing average hours across educational attainment categories.

![](images/page_287_chart_9.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 | IQR |
| --- | --- | --- | --- | --- |
| Primary school | ~10 | ~15 | ~30 | ~20 |
| Lower middle school | ~10 | ~15 | ~30 | ~20 |
| Upper middle school | ~10 | ~10 | ~30 | ~20 |
| Technical or vocational | ~10 | ~18 | ~48 | ~38 |
| College | ~10 | ~15 | ~30 | ~20 |
</details>

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| education | 4 | 4142.09 | 1035.52 | 1.26 | 0.2846 |
| Residuals | 794 | 653047.83 | 822.48 |  |  |

(a) Write the hypotheses for testing for a difference between the average number of hours spent on child care across educational attainment levels.
(b) What is the conclusion of the hypothesis test?