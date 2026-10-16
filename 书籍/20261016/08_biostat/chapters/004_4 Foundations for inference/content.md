# 4 Foundations for inference

原始 PDF 第 198–235 页。

## Chapter 4

## Foundations for inference

**4.1 Variability in estimates**
**4.2 Confidence intervals**
**4.3 Hypothesis testing**
**4.4 Notes**
**4.5 Exercises**

---

199

Not surprisingly, many studies are now demonstrating the adverse effect of obe sity on health outcomes. A 2017 study conducted by the consortium studying the global burden of disease estimates that high body mass index (a measure of body fat that adjusts for height and weight) may account for as many as 4.0 million deaths globally.<sup>1</sup>In addition to the physiologic effects of being overweight, other studies have shown that perceived weight status (feeling that one is overweight or underweight) may have a significant effect on self-esteem.<sup>2,3</sup>

As stated in its mission statement, the United States Centers for Disease Con trol and Prevention (US CDC) "serves as the national focus for developing and applying disease prevention and control, environmental health, and health promotion and health education activities designed to improve the health of the people of the United States".<sup>4</sup> Since it is not feasible to measure the health status and outcome of every single US resident, the CDC estimates features of health from samples taken from the population, via large surveys that are repeated periodically. These surveys include the National Health Interview Survey (NHIS), the National Health and Nutrition Examination Survey (NHANES), the Youth Risk Behavior Surveillance System (YRBSS) and the Behavior Risk Factor Surveillance System (BRFSS). In the language of statistics, the average weight of all US adults is a **population parameter**; the mean weight in a sample or survey is an **estimate** of population average weight. The principles of statistical inference provide not only estimates of population parameters, but also measures of uncertainty that account for the fact that different random samples will produce different estimates because of the variability of random sampling; i.e., two different random samples will not include exactly the same people.

This chapter introduces the important ideas in drawing estimates from samples by discussing methods of inference for a population mean, µ, including three widely used tools: point estimates for a population mean, interval estimates that include both a point estimate and a margin of error, and a method for testing scien tific hypotheses about µ. The concepts used in this chapter will appear throughout the rest of the book, which discusses inference for other settings. While particular equations or formulas may change to reflect the details of a problem at hand, the fundamental ideas will not.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>DOI: 10.1056/NEJMoa1614362</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2<sub>J</sub> Ment Health Policy Econ. 2010 Jun;13(2):53-63</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>DOI: 10.1186/1471-2458-7-80</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>[https://www.cdc.gov/maso/pdf/cdcmiss.pdf](https://www.cdc.gov/maso/pdf/cdcmiss.pdf)</span></small>

---

200

The BRFSS was established in 1984 in 15 states to collect data using telephone interviews about health-related risk behaviors, chronic health conditions, and the use of preventive services. It now collects data in all 50 states and the District of Columbia from more than 400,000 interviews conducted each year. The data set cdc contains a small number of variables from a random sample of 20,000 re sponses from the 264,684 interviews from the BRFSS conducted in the year 2000. Part of this dataset is shown in Figure 4.1, with the variables described in Fig ure 4.2.<sup>5</sup>

|  | case | age | gender | weight | wtdesire | height | genhlth |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 77 | m | 175 | 175 | 70 | good |
| 2 | 2 | 33 | f | 125 | 115 | 64 | good |
| 3 | 3 | 49 | f | 105 | 105 | 60 | good |
| 20000 | 20000 | 83 | m | 170 | 165 | 69 | good |

Figure 4.1: Four cases from the cdc dataset.

| Variable | Variable definition. |
| --- | --- |
| case | Case number in the dataset, ranging from 1 to 20,000. |
| age | Age in years. |
| gender | A factor variable, with levels m for male, f for female. |
| weight | Weight in pounds. |
| wtdesire | Weight that the respondent wishes to be, in pounds. |
| height | Height in inches. |
| genhlth | A factor variable describing general health status, with levels excellent, very good, good, fair, poor. |

Figure 4.2: Some variables and their descriptions for the cdc dataset.

Few studies are as large as the original BRFSS dataset (more than 250,000 cases); in fact, few are as large as the 20,000 cases in the dataset cdc. The dataset cdc is large enough that estimates calculated from cdc can be thought of as essen tially equivalent to the population characteristics of the entire US adult popula tion. This chapter uses a random sample of 60 cases from cdc, stored as cdc.samp, to illustrate the effect of sampling variability and the ideas behind inference. In other words, suppose that cdc represents the population, and that cdc.samp is a sample from the population; the goal is to estimate characteristics of the popula tion of 20,000 using only the data from the 60 individuals in the sample.

![](../../raw/pages_0193-0208/images/page_199_image_7.jpg)

For labs, slides, and other resources, please visit

[**www.openintro.org/book/biostat**](http://www.openintro.org/redirect.php?go=biostat&referrer=biostat1_pdf)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>With small modifications (character strings re-coded as factors), the data appears in this text as it does in an OpenIntro lab. [https://www.openintro.org/go?id=statlab\_ r\_core\_ intro\_ to\_data](http://www.openintro.org/redirect.php?go=statlab_r_core_intro_to_data&referrer=biostat1_pdf)</span></small>

---

4.1. VARIABILITY IN ESTIMATES

201

## 4.1 Variability in estimates

A natural way to estimate features of the population, such as the population mean weight, is to use the corresponding summary statistic calculated from the sample.<sup>6</sup> The mean weight in the sample of 60 adults in cdc.samp is $\overline { { x } } _ { \mathrm { w e i g h t } } = 1 7 3 . 3$ lbs; this sample mean is a **point estimate** of the population mean, $\mu _ { \mathrm { w e i g h t } } .$ . If a different random sample of 60 individuals were taken from cdc, the new sample mean would likely be different as a result of **sampling variation**. While estimates generally vary from one sample to another, the population mean is a fixed value.

## GUIDED PRACTICE 4.1

How would one estimate the difference in average weight between men and women? Given that $\overline { { x } } _ { \mathrm { m e n } } = 1 8 5 . 1$ lbs and $\overline { { x } } _ { \mathrm { w o m e n } } = 1 6 2 . 3$ lbs, what is a good point estimate for the population differ-$\mathsf { e n c e ? } ^ { 7 }$

Point estimates become more accurate with increasing sample size. Figure 4.3 shows the sample mean weight calculated for random samples drawn from cdc, where sample size increases by 1 for each draw until sample size equals 500. The red dashed horizontal line in the figure is drawn at the average weight of all adults in cdc, 169.7 lbs, which represents the population mean weight.<sup>8</sup>

![](../../raw/pages_0193-0208/images/page_200_chart_7.jpg)

<details>
<summary>line</summary>

| Sample size | Mean weight |
| --- | --- |
| 0 | ~135 |
| 10 | ~200 |
| 20 | ~165 |
| 30 | ~195 |
| 40 | ~160 |
| 50 | ~185 |
| 60 | ~165 |
| 70 | ~180 |
| 80 | ~165 |
| 90 | ~175 |
| 100 | ~165 |
| 110 | ~175 |
| 120 | ~165 |
| 130 | ~175 |
| 140 | ~165 |
| 150 | ~175 |
| 160 | ~165 |
| 170 | ~175 |
| 180 | ~165 |
| 190 | ~175 |
| 200 | ~165 |
| 210 | ~175 |
| 220 | ~165 |
| 230 | ~175 |
| 240 | ~165 |
| 250 | ~175 |
| 260 | ~165 |
| 270 | ~175 |
| 280 | ~165 |
| 290 | ~175 |
| 300 | ~165 |
| 310 | ~175 |
| 320 | ~165 |
| 330 | ~175 |
| 340 | ~165 |
| 350 | ~175 |
| 360 | ~165 |
| 370 | ~175 |
| 380 | ~165 |
| 390 | ~175 |
| 400 | ~165 |
| 410 | ~175 |
| 420 | ~165 |
| 430 | ~175 |
| 440 | ~165 |
| 450 | ~175 |
| 460 | ~165 |
| 470 | ~175 |
| 480 | ~165 |
| 490 | ~175 |
| 500 | ~165 |
</details>

Figure 4.3: The mean weight computed for a random sample from cdc, increasing sample size one at a time until $n = 5 0 0$ . The sample mean approaches the population mean (i.e., mean weight in cdc) as sample size increases.

Note how a sample size around 50 may produce a sample mean that is as much as 10 lbs higher or lower than the population mean. As sample size increases, the fluctuations around the population mean decrease; in other words, as sample size increases, the sample mean becomes less variable and provides a more reliable estimate of the population mean.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>Other population parameters, such as population median or population standard deviation, can also be estimated using sample versions.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>Given that x<sub>men</sub> = 185.1 lbs and x<sub>women</sub> = 162.3 lbs, the difference of the two sample means, 185.1 − 162.3 = 22.8lbs, is a point estimate of the difference. The data in the random sample suggests that adult males are, on average, about 23 lbs heavier than adult females.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">8It is not exactly the mean weight of all US adults, but will be very close since cdc is so large.</span></small>

---

202

CHAPTER 4. FOUNDATIONS FOR INFERENCE

## 4.1.1 The sampling distribution for the mean

The sample mean weight calculated from cdc.samp is 173.3 lbs. Another random sample of 60 participants might produce a different value of x, such as 169.5 lbs; repeated random sampling could result in additional different values, perhaps 172.1 lbs, 168.5 lbs, and so on. Each sample mean $\overline { { x } }$ can be thought of as a single observation from a random variable ${ \overline { { X } } } .$ The distribution of $\overline { { X } }$ is called the **sampling distribution of the sample mean**, and has its own mean and standard deviation like the random variables discussed in Chapter 3. The concept of a sampling distribution can be illustrated by taking repeated random samples from cdc. Figure 4.4 shows a histogram of sample means from 1,000 random samples of size 60 from cdc. The histogram provides an approximation of the theoretical sampling distribution of X for samples of size 60.

![](../../raw/pages_0193-0208/images/page_201_chart_4.jpg)

<details>
<summary>histogram</summary>

| Sample mean (range) | Frequency |
| --- | --- |
| 152~153 | ~2 |
| 154~155 | ~1 |
| 156~157 | ~3 |
| 157~158 | ~9 |
| 158~159 | ~18 |
| 159~160 | ~14 |
| 160~161 | ~17 |
| 161~162 | ~31 |
| 162~163 | ~44 |
| 163~164 | ~41 |
| 164~165 | ~52 |
| 165~166 | ~86 |
| 166~167 | ~64 |
| 167~168 | ~70 |
| 168~169 | ~100 |
| 169~170 | ~68 |
| 170~171 | ~68 |
| 171~172 | ~66 |
| 172~173 | ~66 |
| 173~174 | ~39 |
| 174~175 | ~41 |
| 175~176 | ~30 |
| 176~177 | ~19 |
| 177~178 | ~17 |
| 178~179 | ~15 |
| 179~180 | ~6 |
| 180~181 | ~4 |
| 181~182 | ~2 |
| 182~183 | ~3 |
| 183~184 | ~2 |
| 184~185 | ~3 |
</details>

Figure 4.4: A histogram of 1000 sample means for weight among US adults, where the samples are of size $n = 6 0$

## SAMPLING DISTRIBUTION

The sampling distribution is the distribution of the point estimates based on samples of a fixed size from a certain population. It is useful to think of a particular point estimate as being drawn from a sampling distribution.

Since the complete sampling distribution consists of means for all possible samples of size 60, drawing a much larger number of samples provides a more accurate view of the distribution; the left panel of Figure 4.5 shows the distribution calculated from 100,000 sample means.

A normal probability plot of these sample means is shown in the right panel of Figure 4.5. All of the points closely fall around a straight line, implying that the distribution of sample means is nearly normal (see Section 3.3). This result follows from the Central Limit Theorem.

## CENTRAL LIMIT THEOREM, INFORMAL DESCRIPTION

If a sample consists of at least 30 independent observations and the data are not strongly skewed, then the distribution of the sample mean is well approximated by a normal model.

---

4.1. VARIABILITY IN ESTIMATES

203

![](../../raw/pages_0193-0208/images/page_202_image_2.jpg)

Figure 4.5: The left panel shows a histogram of the sample means for 100,000 random samples. The right panel shows a normal probability plot of those sample means.

The sampling distribution for the mean is unimodal and symmetric around the mean of the random variable $\overline { { X } } .$ Statistical theory can be used to show that the mean of the sampling distribution for $\overline { { X } }$ is exactly equal to the population mean $\mu .$

However, in almost any study, conclusions about a population parameter must be drawn from the data collected from a single sample. The sampling distribution of X is a theoretical concept, since obtaining repeated samples by conducting a study many times is not possible. In other words, it is not feasible to calculate the population mean $\mu$ by finding the mean of the sampling distribution for $\overline { { X } } .$

## 4.1.2 Standard error of the mean

The **standard error (SE)** of the sample mean measures the sample-to-sample variability of $\overline { { X } } ,$ the extent to which values of the repeated sample means oscillate around the population mean. The theoretical standard error of the sample mean is calculated by dividing the population standard deviation $\left( \sigma _ { x } \right)$ by the square root of the sample size n. Since the population standard deviation σ is typically unknown, the sample standard deviation s is often used in the definition of a standard error; s is a reasonably good estimate of $\sigma   .$ If $\overline { { X } }$ represents the sample mean weight, its standard error (denoted by SE) is

$$
\mathrm{SE} _ {\overline {{X}}} = \frac {s _ {x}}{\sqrt {n}} = \frac {4 9 . 0 4}{\sqrt {6 0}} = 6. 3 3.
$$

This estimate tends to be sufficiently good when the sample size is at least 30 and the population distribution is not strongly skewed. In the case of skewed distributions, a larger sample size is necessary.

SE
standard
error

---

204

CHAPTER 4. FOUNDATIONS FOR INFERENCE

The probability tools of Section 3.1 can be used to derive the formula $\sigma _ { \overline { { { X } } } } = \sigma _ { x } / \sqrt { n } ,$ but the derivation is not shown here. Larger sample sizes produce sampling distributions that have lower variability. Increasing the sample size causes the distribution of $\bar { \bar { X } }$ to be clustered more tightly around the population mean $\mu ,$ allowing for more accurate estimates of $\mu$ from a single sample, as shown in Figure 4.6. When sample size is large, it is more likely that any particular sample will have a mean close to the population mean.

![](../../raw/pages_0193-0208/images/page_203_chart_3.jpg)

<details>
<summary>histogram</summary>

| Bin (Sample mean) | Frequency |
| --- | --- |
| 152~153 | ~1 |
| 154~155 | ~1 |
| 156~157 | ~2 |
| 157~158 | ~8 |
| 158~159 | ~18 |
| 159~160 | ~14 |
| 160~161 | ~16 |
| 161~162 | ~32 |
| 162~163 | ~44 |
| 163~164 | ~42 |
| 164~165 | ~52 |
| 165~166 | ~87 |
| 166~167 | ~65 |
| 167~168 | ~70 |
| 168~169 | ~100 |
| 169~170 | ~68 |
| 170~171 | ~68 |
| 171~172 | ~67 |
| 172~173 | ~67 |
| 173~174 | ~39 |
| 174~175 | ~42 |
| 175~176 | ~30 |
| 176~177 | ~19 |
| 177~178 | ~17 |
| 178~179 | ~15 |
| 179~180 | ~7 |
| 180~181 | ~4 |
| 181~182 | ~2 |
| 182~183 | ~2 |
| 183~184 | ~3 |
| 184~185 | ~2 |
| 185~186 | ~2 |
</details>

(a)

![](../../raw/pages_0193-0208/images/page_203_chart_5.jpg)

<details>
<summary>histogram</summary>

| Bin (Sample mean) | Frequency |
| --- | --- |
| ~157 | ~1 |
| ~158 | ~2 |
| ~159 | ~3 |
| ~160 | ~4 |
| ~161 | ~5 |
| ~162 | ~8 |
| ~163 | ~16 |
| ~164 | ~42 |
| ~165 | ~67 |
| ~166 | ~64 |
| ~167 | ~92 |
| ~168 | ~120 |
| ~169 | ~118 |
| ~170 | ~125 |
| ~171 | ~89 |
| ~172 | ~86 |
| ~173 | ~76 |
| ~174 | ~47 |
| ~175 | ~30 |
| ~176 | ~8 |
| ~177 | ~6 |
| ~178 | ~3 |
| ~179 | ~1 |
| ~180 | ~1 |
</details>

(b)

Figure 4.6: (a) Reproduced from Figure $4 . 4 ,$ an approximation of the sampling distribution of $\overline { { X } }$ with $n = 6 0$ . (b) An approximation of the sampling distribution of $\overline { { X } }$ with $n = 2 0 0$

## THE STANDARD ERROR (SE) OF THE SAMPLE MEAN

Given n independent observations from a population with standard deviation $\sigma ,$ the standard error of the sample mean is equal to

$$
\mathrm{SE}_{\overline{X}} = \frac{s_x}{\sqrt{n}}.
$$

This is an accurate estimate of the theoretical standard deviation of $\overline { { X } }$ when the sample size is at least 30 and the population distribution is not strongly skewed.

## SUMMARY: POINT ESTIMATE TERMINOLOGY

– The population mean and standard deviation are denoted by $\mu$ and $\sigma .$
– The sample mean and standard deviation are denoted by $\overline { { x } }$ and $s .$
The distribution of the random variable $\overline { { X } }$ refers to the collection of sample means if multiple samples of the same size were repeatedly drawn from a population.
The mean of the random variable $\overline { { X } }$ equals the population mean $\mu .$ In the notation of Chapter 3, $\mu _ { \overline { { X } } } = E ( { \overline { { X } } } ) = \mu$
The standard deviation of $\overline { { X } } \left( \sigma _ { \overline { { X } } } \right)$ is called the standard error (SE) of the sample mean.
The theoretical standard error of the sample mean, as calculated from a single sample of size $n ,$ is equal to $\frac { \sigma } { \sqrt { n } }$ The standard error is abbreviated by SE and is usually estimated by using $s ,$ the sample standard deviation, such that $\begin{array} { r } { S E = \frac { s } { \sqrt { n } } } \end{array}$

---

4.2. CONFIDENCE INTERVALS

205

## 4.2 Confidence intervals

## 4.2.1 Interval estimates for a population parameter

While a point estimate consists of a single value, an interval estimate provides a plausible range of values for a parameter. When estimating a population mean $\mu ,$ a **confidence interval** for $\mu$ has the general form

$$
(\overline {{x}} - m, \overline {{x}} + m) = \overline {{x}} \pm m,
$$

where m is the **margin of error**. Intervals that have this form are called **two-sided confidence intervals** because they provide both lower and upper bounds, $\overline { { x } } - m$ and ${ \overline { { x } } } + m ,$ respectively. Onesided sided intervals are discussed in Section 4.2.3.

The standard error of the sample mean is the standard deviation of its distribution; additionally, the distribution of sample means is nearly normal and centered at $\mu .$ Under the normal model, the sample mean x will be within 1.96 standard errors $( \mathbf { i . e . }$ , standard deviations) of the population mean µ approximately 95% of the time.<sup>9</sup> Thus, if an interval is constructed that spans 1.96 standard errors from the point estimate in either direction, a data analyst can be 95% **confident** that the interval

$$
\overline {{x}} \pm 1. 9 6 \times \mathrm{SE} \tag {4.2}
$$

contains the population mean. The value 95% is an approximation, accurate when the sampling distribution for the sample mean is close to a normal distribution. This assumption holds when the sample size is sufficiently large (guidelines for ‘sufficiently large’ are given in Section 4.4).

![](../../raw/pages_0193-0208/images/page_204_chart_10.jpg)

<details>
<summary>forest</summary>

| Study | Mean \((\mu)\) |
| --- | --- |
| 1 | ~0.5 |
| 2 | ~0.8 |
| 3 | ~0.4 |
| 4 | ~0.6 |
| 5 | ~0.7 |
| 6 | ~0.5 |
| 7 | ~0.4 |
| 8 | ~0.3 |
| 9 | ~0.2 |
| 10 | ~0.1 |
| 11 | ~0.1 |
| 12 | ~0.1 |
| 13 | ~0.1 |
| 14 | ~0.1 |
| 15 | ~0.1 |
| 16 | ~0.1 |
| 17 | ~0.1 |
| 18 | ~0.1 |
| 19 | ~0.1 |
| 20 | ~0.1 |
| 21 | ~0.1 |
| 22 | ~0.1 |
| 23 | ~0.1 |
| 24 | ~0.1 |
| 25 | ~0.1 |
| 26 | ~0.1 |
| 27 | ~0.1 |
| 28 | ~0.1 |
| 29 | ~0.1 |
| 30 | ~0.1 |
| 31 | ~0.1 |
| 32 | ~0.1 |
| 33 | ~0.1 |
| 34 | ~0.1 |
| 35 | ~0.1 |
| 36 | ~0.1 |
| 37 | ~0.1 |
| 38 | ~0.1 |
| 39 | ~0.1 |
| 40 | ~0.1 |
| 41 | ~0.1 |
| 42 | ~0.1 |
| 43 | ~0.1 |
| 44 | ~0.1 |
| 45 | ~0.1 |
| 46 | ~0.1 |
| 47 | ~0.1 |
| 48 | ~0.1 |
| 49 | ~0.1 |
| 50 | ~0.1 |
| 51 | ~0.1 |
| 52 | ~0.1 |
| 53 | ~0.1 |
| 54 | ~0.1 |
| 55 | ~0.1 |
| 56 | ~0.1 |
| 57 | ~0.1 |
| 58 | ~0.1 |
| 59 | ~0.1 |
| 60 | ~0.1 |
| 61 | ~0.1 |
| 62 | ~0.1 |
| 63 | ~0.1 |
| 64 | ~0.1 |
| 65 | ~0.1 |
| 66 | ~0.1 |
| 67 | ~0.1 |
| 68 | ~0.1 |
| 69 | ~0.1 |
| 70 | ~0.1 |
| 71 | ~0.1 |
| 72 | ~0.1 |
| 73 | ~0.1 |
| 74 | ~0.1 |
| 75 | ~0.1 |
| 76 | ~0.1 |
| 77 | ~0.1 |
| 78 | ~0.1 |
| 79 | ~0.1 |
| 80 | ~0.1 |
| 81 | ~0.1 |
| 82 | ~0.1 |
| 83 | ~0.1 |
| 84 | ~0.1 |
| 85 | ~0.1 |
| 86 | ~0.1 |
| 87 | ~0.1 |
| 88 | ~0.1 |
| 89 | ~0.1 |
| 90 | ~0.1 |
| 91 | ~0.1 |
| 92 | ~0.1 |
| 93 | ~0.1 |
| 94 | ~0.1 |
| 95 | ~0.1 |
| 96 | ~0.1 |
| 97 | ~0.1 |
| 98 | ~0.1 |
| 99 | ~0.1 |
| 100 | ~0.1 |
</details>

Figure 4.7: Twenty-five samples of size $n = 6 0$ were taken from cdc. For each sample, a 95% confidence interval was calculated for the population average adult weight. Only 1 of these 25 intervals did not contain the population mean, $\mu =$ 169.7 lbs.

The phrase "95% confident" has a subtle interpretation: if many samples were drawn from a population, and a confidence interval is calculated from each one using Equation 4.2, about 95% of those intervals would contain the population mean $\mu .$ Figure 4.7 illustrates this process with 25 samples taken from cdc. Of the 25 samples, 24 contain the mean weight in cdc of 169.7 lbs, while one does not.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>In other words, the Z-score of 1.96 is associated with 2.5% area to the right (and Z = -1.96 has 2.5% area to the left); this can be found on normal probability tables or from using statistical software.</span></small>

---

206

CHAPTER 4. FOUNDATIONS FOR INFERENCE

Just as with the sampling distribution of the sample mean, the interpretation of a confidence interval relies on the abstract construct of repeated sampling. A data analyst, who can only observe one sample, does not know whether the population mean lies within the single interval calculated. The uncertainty is due to random sampling—by chance, it is possible to select a sample from the population that has unusually high (or low) values, resulting in a sample mean $\overline { { x } }$ that is relatively far from $\mu ,$ and by extension, a confidence interval that does not contain $\mu .$

## EXAMPLE 4.3

The sample mean adult weight from the 60 observations in cdc.samp is $\overline { { x } } _ { \mathrm { w e i g h t } } = 1 7 3 . 3$ lbs, and the standard deviation is $s _ { \mathrm { w e i g h t } } = 4 9 . 0 4$ lbs. Use Equation 4.2 to calculate an approximate 95% confidence interval for the average adult weight in the US population.

The standard error for the sample mean is $\begin{array} { r } { \mathrm { S E } _ { \overline { { x } } } = \frac { 4 9 . 0 4 } { \sqrt { 6 0 } } = 6 . 3 3 } \end{array}$ lbs. The 95% confidence interval is

$$
\overline {{x}} _ {\text {weight}} \pm 1. 9 6 \mathrm{SE} _ {\overline {{x}}} = 1 7 3. 3 \pm (1. 9 6) (6. 3 3) = (1 6 0. 8 9, 1 8 5. 7 1) \text {lbs}.
$$

The data support the conclusion that, with 95% confidence, the average weight of US adults is between approximately 161 and 186 lbs.

Figure 4.5 visually shows that the sampling distribution is nearly normal. To assess normality of the sampling distribution without repeated sampling, it is necessary to check whether the data are skewed. Although Figure 4.8 shows some skewing, the sample size is large enough that the confidence interval should be reasonably accurate.

![](../../raw/pages_0193-0208/images/page_205_chart_9.jpg)

<details>
<summary>histogram</summary>

| Weight (lbs) | Frequency |
| --- | --- |
| 100~150 | 20 |
| 150~200 | ~32 |
| 200~250 | 4 |
| 250~300 | 3 |
</details>

Figure 4.8: Histogram of weight in cdc.samp

E

---

4.2. CONFIDENCE INTERVALS

207

![](../../raw/pages_0193-0208/images/page_206_image_2.jpg)

## GUIDED PRACTICE 4.4

There are 31 females in the sample of 60 US adults, and the average and standard deviation of weight for these individuals are 162.3 lbs and 57.74 lbs, respectively. A histogram of weight for the 31 females is shown in Figure 4.9. Calculate an approximate 95% confidence interval for the average weight of US females. Is the interval likely to be accurate?<sup>10</sup>

![](../../raw/pages_0193-0208/images/page_206_chart_5.jpg)

<details>
<summary>histogram</summary>

| Weight of Females (Bin) | Frequency |
| --- | --- |
| 100~150 | ~16 |
| 150~200 | ~12 |
| 200~250 | ~1 |
| 250~300 | ~1 |
| 350~400 | ~1 |
</details>

Figure 4.9: Histogram of weight for the 31 females in cdc.samp.

## 4.2.2 Changing the confidence level

Ninety-five percent confidence intervals are the most commonly used interval estimates, but intervals with confidence levels other than 95% can also be constructed. The general formula for a confidence interval (for the population mean µ) is given by

$$
\overline {{x}} \pm z ^ {\star} \times \mathrm{SE}, \tag {4.5}
$$

where $z ^ { \star }$ is chosen according to the confidence level. When calculating a 95% confidence level, $z ^ { \star }$ is 1.96, since the area within 1.96 standard deviations of the mean captures 95% of the distribution.

To construct a 99% confidence interval, $z ^ { \star }$ must be chosen such that 99% of the normal curve is captured between $- z ^ { \star }$ and $z ^ { \star }$

## EXAMPLE 4.6

Let Y be a normally distributed random variable. Ninety-nine percent of the time, Y will be within how many standard deviations of the mean?

This is equivalent to the z-score with 0.005 area to the right of z and 0.005 to the left of $- z .$ In the normal probability table, this is the z-value that with 0.005 area to its right and 0.995 area to its left. The closest two values are 2.57 and 2.58; for convenience, round up to 2.58. The unobserved random variable Y will be within 2.58 standard deviations of $\mu$ 99% of the time, as shown in Figure 4.10.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10<sub>Applying</sub> Equation 4.2: 162.3 ± (1.96)(57.73/√31) → (149.85,174.67). The usual interpretation would be that a data analyst can be about 95% confident the average weight of US females is between approximately 150 and 175 lbs. However, the histogram of female weights shows substantial right skewing, and several females with recorded weights larger than 200 lbs. The confidence interval is probably not accurate; a larger sample should be collected in order for the sampling distribution of the mean to be approximately normal. Chapter 5 will introduce the t-distribution, which is more reliable with small sample sizes than the z-distribution.</span></small>

![](../../raw/pages_0193-0208/images/page_206_image_16.jpg)

---

208

CHAPTER 4. FOUNDATIONS FOR INFERENCE

![](../../raw/pages_0193-0208/images/page_207_chart_2.jpg)

<details>
<summary>area</summary>

| Interval | Standard Deviations (Mean) |
| --- | --- |
| 95% | -1.96 to 1.96 |
| 99% | -2.58 to 2.58 |
</details>

Figure 4.10: The area between $- z ^ { \star }$ and $z ^ { \star }$ increases as $| z ^ { \star } |$ becomes larger. If the confidence level is 99%, $z ^ { \star }$ is chosen such that 99% of the normal curve is between $- z ^ { \star }$ and $z ^ { \star } ,$ , which corresponds to 0.5% in the lower tail and 0.5% in the upper tail: $z ^ { \star } = 2 . 5 8 .$

A 99% confidence interval will have the form

$$
\overline {{x}} \pm 2. 5 8 \times \mathrm{SE}, \tag {4.7}
$$

and will consequently be wider than a 95% interval for $\mu$ calculated from the same data, since the margin of error m is larger.

## EXAMPLE 4.8

Create a 99% confidence interval for the average adult weight in the US population using the data in cdc.samp. The point estimate is $\overline { { x } } _ { w e i g h t } = 1 7 3 . 3$ and the standard error is $S E _ { \overline { { x } } } = 6 . 3 3$

Apply the 99% confidence interval formula: $\overline { { x } } _ { w e i g h t }   \pm   2 . 5 8   \times   S E _ { \overline { { x } } }   \rightarrow   \left( 1 5 6 . 9 7 , 1 8 9 . 6 3 \right)$ . A data analyst can be 99% confident that the average adult weight is between 156.97 and 189.63 lbs.

The 95% confidence interval for the average adult weight is (160.89, 185.71) lbs. Increasing the confidence level to 99% results in the interval (156.97, 189.63) lbs; this wider interval is more likely to contain the population mean $\mu .$ However, increasing the confidence level comes at a cost: a wider interval is less informative in providing a precise estimate of the population mean. Consider the extreme: to be "100% confident" that an interval contains $\mu ,$ the interval must span all possible values of $\mu .$ For example, with 100% confidence the average weight is between 0 and 1000 lbs; while this interval necessarily contains $\mu ,$ it has no interpretive value and is completely uninformative.<sup>11</sup>

Decreasing the confidence level produces a narrower interval; the estimate is more precise, but also more prone to inaccuracy. For example, consider a 50% confidence interval for average adult weight using cdc.samp: the $z ^ { \star }$ value is $0 . 6 7 ,$ and the confidence interval is (169.06, 177.54) lbs. This interval provides a more precise estimate of the population average weight $\mu$ than the 99% or 95% confidence intervals, but the increased precision comes with less confidence about whether the

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11<sub>Strictly</sub> speaking, to be 100% confident requires an interval spanning all positive numbers; 1000 lbs has been arbitrarily chosen as an upper limit for human weight.</span></small>

E

---

4.2. CONFIDENCE INTERVALS

209

interval contains $\mu .$ In a theoretical setting of repeated sampling, if 100 50% confidence intervals were computed, only half could be expected to contain $\mu .$

The choice of confidence level is a trade-off between obtaining a precise estimate and calculat ing an interval that can be reasonably expected to contain the population parameter. In published literature, the most used confidence intervals are the 90%, 95%, and 99%.

## 4.2.3 One-sided confidence intervals

One-sided confidence intervals for a population mean provide either a lower bound or an upper bound, but not both. One-sided confidence intervals have the form

$$
(\overline {{x}} - m, \infty) \text {or} (- \infty , \overline {{x}} + m).
$$

While the margin of error m for a one-sided interval is still calculated from the standard error of x and a $z ^ { \star }$ value, the choice of $z ^ { \star }$ is a different than for a two-sided interval. For example, the intent of a 95% one-sided upper confidence interval is to provide an upper bound m such that a data analyst can be 95% confident that a population mean $\mu$ is less than ${ \overline { { x } } } + m .$ . The $z ^ { \star }$ value must correspond to the point on the normal distribution that has 0.05 area in the right tail, $z ^ { \star } = 1 . 6 4 5 .$ <sup>12</sup> A one-sided upper 95% confidence interval will have the form

$$
(-\infty ,\overline{x} +1.645\times \mathrm{SE}).
$$

## EXAMPLE 4.9

Calculate a lower 95% confidence interval for the population average adult weight in the United States. In the sample of 60 adults in cdc.samp, the mean and standard error are $\overline { { x } } = 1 7 3 . 3$ and $S E = 6 . 3 3 \; \mathrm { { \bf d a y s } } .$

The lower bound is $173.3-\left(1.645\times6.33\right)=163.89$ . The lower 95% interval (163.89,∞) suggests that one can be 95% confident that the population average adult weight is at least 163.9 lbs.

## GUIDED PRACTICE 4.10

Calculate an upper 99% confidence interval for the population average adult weight in the United States. The mean and standard error for weight in cdc.samp are $\overline { { x } } = 1 7 3 . 3$ and $S E = 6 . 3 3 \; \mathrm { { \bf d a y s } } . ^ { 1 3 }$

## 4.2.4 Interpreting confidence intervals

The correct interpretation of an XX% confidence interval is, "We are XX% confident that the population parameter is between . . . " While it may be tempting to say that a confidence interval captures the population parameter with a certain probability, this is a common error. The confidence level only quantifies how plausible it is that the parameter is within the interval; there is no probability associated with whether a parameter is contained in a specific confidence interval. The confidence coefficient reflects the nature of a procedure that is correct XX% of the time, given that the assumptions behind the calculations are true.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12<sub>Previously</sub>, with a two-sided interval, 1.96 was chosen in order to have a total area of 0.05 from both the right and left tails.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13<sub>For</sub> a one-sided 99% confidence interval, the z? value corresponds to the point with 0.01 area in the right tail, z? = 2.326. Thus, the upper bound for the interval is 173.3 + (2.326 × 6.33) = 188.024. The upper 99% interval (−∞,188.024) suggests that one can be 99% confident that the population average adult weight is at most 188.0 lbs.</span></small>

E

G

---

210

CHAPTER 4. FOUNDATIONS FOR INFERENCE

The conditions regarding the validity of the normal approximation can be checked using the numerical and graphical summaries discussed in Chapter 1. However, the condition that data should be from a random sample is sometimes overlooked. If the data are not from a random sample, then the confidence interval no longer has interpretive value, since there is no population mean to which the confidence interval applies. For example, while only simple arithmetic is needed to calculate a confidence interval for BMI from the famuss dataset in Chapter 1, the participants in the study are almost certainly not a random sample from some population; thus, a confidence interval should not be calculated in this setting.

## EXAMPLE 4.11

Body mass index (BMI) is one measure of body weight that adjusts for height. The National Health and Nutrition Examination Survey (NHANES) consists of a set of surveys and measurements conducted by the US CDC to assess the health and nutritional status of adults and children in the United States. The dataset nhanes.samp contains 76 variables and is a random sample of 200 individuals from the measurements collected in the years 2009-2010 and 2012-2013.<sup>14</sup> Use nhanes.samp to calculate a 95% confidence interval for adult BMI in the US population, and assess whether the data suggest Americans tend to be overweight.

In the random sample of 200 participants, BMI is available for all 135 of the participants that are 21 years of age or older. As shown in the histogram (Figure 4.11), the data are right-skewed, with one large outlier. The outlier corresponds to an implausibly extreme BMI value of 69.0; since it seems likely that the value represents an error from when the data was recorded, this data point is excluded from the following analysis.

The mean and standard deviation in this sample of 134 are 28.8 and 6.7 kg/meter<sup>2</sup>, respectively. The sample size is large enough to justify using the normal approximation when computing the confidence interval. The standard error of the mean is SE = 6.7/√134 = 0.58, so the 95% confidence interval is given by

$$
\begin{array}{l} \overline {{x}} _ {\mathrm{BMI}} \pm (1. 9 6) (\mathrm{SE}) = 2 8. 8 \pm (1. 9 6) (0. 5 8) \\ = (2 7. 7, 2 9. 9). \\ \end{array}
$$

Based on this sample, a data analyst can be 95% confident that the average BMI of US adults is between 27.7 and 29.9 kg/m<sup>2</sup>.

The World Health Organization (WHO) and other agencies use BMI to set normative guidelines for body weight. The current guidelines are shown in Figure 4.12.

The confidence interval (27.7, 29.9) kg/m<sup>2</sup>certainly suggests that the average BMI in the US population is higher than 21.7, the middle of the range for normal BMIs, and even higher than 24.99, the upper limit of the normal weight category. These data indicate that Americans tend to be overweight.

E

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">14<sub>The</sub> sample was drawn from a larger sample of 20,293 participants in the NHANES package, available from The Comprehensive R Archive Network (CRAN). The CDC uses a complex sampling design that samples some demographic subgroups with larger probabilities, but nhanes.samp has been adjusted so that it can be viewed as a random sample of the US population.</span></small>

---

4.2. CONFIDENCE INTERVALS

211

![](../../raw/pages_0209-0224/images/page_210_chart_2.jpg)

<details>
<summary>histogram</summary>

| BMI (Bin) | Frequency |
| --- | --- |
| 15~20 | 10 |
| 20~25 | 31 |
| 25~30 | 45 |
| 30~35 | 25 |
| 35~40 | 14 |
| 40~45 | 5 |
| 45~50 | 4 |
| 65~70 | 1 |
</details>

Figure 4.11: The distribution of BMI for the 135 adults in nhanes.samp.

| Category | BMI range |
| --- | --- |
| Underweight | &lt; 18.50 |
| Normal (healthy weight) | 18.5-24.99 |
| Overweight | ≥ 25 |
| Obese | ≥ 30 |

Figure 4.12: WHO body weight categories based on BMI.

---

212

CHAPTER 4. FOUNDATIONS FOR INFERENCE

## 4.3 Hypothesis testing

Important decisions in science, such as whether a new treatment for a disease should be ap proved for the market, are primarily data-driven. For example, does a clinical study of a new cholesterol-lowering drug provide robust evidence of a beneficial effect in patients at risk for heart disease? A confidence interval can be calculated from the study data to provide a plausible range of values for a population parameter, such as the population average decrease in cholesterol levels. A drug is considered to have a beneficial effect on a population of patients if the population average effect is large enough to be clinically important. It is also necessary to evaluate the strength of the evidence that a drug is effective; in other words, is the observed effect larger than would be expected from chance variation alone?

Hypothesis testing is a method for calculating the probability of making a specific observation under a working hypothesis, called the null hypothesis. By assuming that the data come from a distribution specified by the null hypothesis, it is possible to calculate the likelihood of observing a value as extreme as the one represented by the sample. If the chances of such an extreme observation are small, there is enough evidence to reject the null hypothesis in favor of an alternative hypothesis.

## NULL AND ALTERNATIVE HYPOTHESES

The **null hypothesis** $\left( H _ { 0 } \right)$ often represents either a skeptical perspective or a claim to be tested. The **alternative hypothesis** $( H _ { A } )$ is an alternative claim and is often represented by a range of possible parameter values.

Generally, an investigator suspects that the null hypothesis is not true and performs a hypoth esis test in order to evaluate the strength of the evidence against the null hypothesis. The logic behind rejecting or failing to reject the null hypothesis is similar to the principle of presumption of innocence in many legal systems. In the United States, a defendant is assumed innocent until proven guilty; a verdict of guilty is only returned if it has been established beyond a reasonable doubt that the defendant is not innocent. In the formal approach to hypothesis testing, the null hypothesis $( H _ { 0 } )$ is not rejected unless the evidence contradicting it is so strong that the only reasonable conclusion is to reject $H _ { 0 }$ in favor of $H _ { A }$

The next section presents the steps in formal hypothesis testing, which is applied when data are analyzed to support a decision or make a scientific claim.

## 4.3.1 The Formal Approach to Hypothesis Testing

In this section, hypothesis testing will be used to address the question of whether Americans generally wish to be heavier or lighter than their current weight. In the cdc data, the two variables weight and wtdesire are, respectively, the recorded actual and desired weights for each respondent, measured in pounds.

Suppose that $\mu$ is the population average of the difference weight − wtdesire. Using the observations from cdc.samp, assess the strength of the claim that, on average, there is no systematic preference to be heavier or lighter.

---

4.3. HYPOTHESIS TESTING

213

## Step 1: Formulating null and alternative hypotheses

The claim to be tested is that the population average of the difference between actual and desired weight for US adults is equal to 0.

$$
H _ {0}: \mu = 0.
$$

In the absence of prior evidence that people typically wish to be lighter (or heavier), it is reasonable to begin with an alternative hypothesis that allows for differences in either direction.

$$
H _ {A}: \mu \neq 0.
$$

The alternative hypothesis $H _ { A } : \mu \neq 0$ is called a **two-sided alternative**. A one-sided alternative could be used $\mathrm { i f } ,$ for example, an investigator felt there was prior evidence that people typically wish to weigh less than they currently do: $H _ { A } : \mu > 0$

More generally, when testing a hypothesis about a population mean $\mu ,$ the null and alternative hypotheses are written as follows

– For a two-sided alternative:

$$
H _ {0}: \mu = \mu_ {0}, H _ {A}: \mu \neq \mu_ {0}.
$$

– For a one-sided alternative:

$$
H _ {0}: \mu = \mu_ {0}, H _ {A}: \mu <   \mu_ {0} \quad \text {or} \quad H _ {0}: \mu = \mu_ {0}, H _ {A}: \mu > \mu_ {0}.
$$

The symbol µ denotes a population mean, while $\mu _ { 0 }$ refers to the numeric value specified by the null hypothesis; in this example, $\mu _ { 0 } = 0$ . Note that null and alternative hypotheses are statements about the underlying population, not the observed values from a sample.

## Step 2: Specifying a significance level, α

It is important to specify how rare or unlikely an event must be in order to represent sufficient evidence against the null hypothesis. This should be done during the design phase of a study, to prevent any bias that could result from defining ’rare’ only after analyzing the results.

When testing a statistical hypothesis, an investigator specifies a **significance level**, α, that defines a ’rare’ event. Typically, α is chosen to be 0.05, though it may be larger or smaller, depending on context; this is discussed in more detail in Section 4.3.4. An α level of 0.05 implies that an event occurring with probability lower than 5% will be considered sufficient evidence against $H _ { 0 }$

## Step 3: Calculating the test statistic

Calculating the test statistic t is analogous to standardizing observations with Z-scores as discussed in Chapter 3. The test statistic quantifies the number of standard deviations between the sample mean $\overline { { x } }$ and the population mean $\mu ;$

$$
t = \frac {\overline {{x}} - \mu_ {0}}{s / \sqrt {n}},
$$

where s is the sample standard deviation and n is the number of observations in the sample. $\operatorname { I f } x =$ weight − wtdesire, then for the 60 recorded differences in cdc.samp, $\overline { { x } } = 1 8 . 2$ and $s = 3 3 . 4 6$ . In this sample, respondents weigh on average about 18 lbs more than they wish. The test statistic is

$$
t = \frac {1 8 . 2 - 0}{3 3 . 4 6 / \sqrt {6 0}} = 4. 2 2.
$$

The observed sample mean is 4.22 standard deviations to the right of $\mu _ { 0 } = 0$

---

214

CHAPTER 4. FOUNDATIONS FOR INFERENCE

## Step 4: Calculating the p-value

The p**-value** is the probability of observing a sample mean as or more extreme than the observed value, under the assumption that the null hypothesis is true. In samples of size 40 or more, the t-statistic will have a standard normal distribution unless the data are strongly skewed or extreme outliers are present. Recall that a standard normal distribution has mean 0 and standard deviation 1.

For two-sided tests, with $H _ { A } : \mu \neq \mu _ { 0 } ,$ , the p-value is the sum of the area of the two tails defined by the t-statistic: $2P(Z \geq |t|) = P(Z \leq -|t|) + P(Z \geq |t|)$ (Figure 4.13).

![](../../raw/pages_0209-0224/images/page_213_chart_5.jpg)

<details>
<summary>area</summary>

| Metric | Value |
| --- | --- |
| Mean \((\mu)\) | 0 |
| t-statistic | N/A |
</details>

Figure 4.13: A two-sided p-value for $H _ { A } : \mu \neq \mu _ { 0 }$ on a standard normal distribution. The shaded regions represent observations as or more extreme than x in either direction.

For one-sided tests with $H _ { A } : \mu > \mu _ { 0 }$ , the p-value is given by $P ( Z \geq t )$ , as shown in Figure 4.14. If $H _ { A } : \mu < \mu _ { 0 } ,$ the p-value is the area to the left of the t-statistic, $P ( Z \leq t )$

![](../../raw/pages_0209-0224/images/page_213_chart_8.jpg)

<details>
<summary>area</summary>

| Metric | Value |
| --- | --- |
| Mean \((\mu)\) | 0 |
| t-statistic | N/A |
</details>

Figure 4.14: A one-sided p-value for $H _ { A } : \mu > \mu _ { 0 }$ on a standard normal distribution is represented by the shaded area to the right of the t-statistic. This area equals the probability of making an observation as or more extreme than x, if the null hypothesis is true.

The p-value can either be calculated from software or from the normal probability tables. For the weight-difference example, the p-value is vanishingly small: $p = P(Z \leq -4.22) + P(Z > 4.22) <$ 0.001.

---

4.3. HYPOTHESIS TESTING

215

## Step 5: Drawing a conclusion

To reach a conclusion about the null hypothesis, directly compare $p$ and α. Note that for a conclusion to be informative, it must be presented in the context of the original question; it is not useful to only state whether or not $H _ { 0 }$ is rejected.

If $p > \alpha ,$ , the observed sample mean is not extreme enough to warrant rejecting $H _ { 0 } ;$ more formally stated, there is insufficient evidence to reject $H _ { 0 } .$ . A high p-value suggests that the difference between the observed sample mean and $\mu _ { 0 }$ can reasonably be attributed to random chance.

If $p \leq \alpha ,$ there is sufficient evidence to reject $H _ { 0 }$ and accept $H _ { A }$ . In the cdc.samp weightdifference data, the p-value is very small, with the t-statistic lying to the right of the population mean. The chance of drawing a sample with mean as large or larger than 18.2 if the distribution were centered at 0 is less than 0.001. Thus, the data support the conclusion that on average, the difference between actual and desired weight is not 0 and is positive; people generally seem to feel they are overweight.

## GUIDED PRACTICE 4.12

Suppose that the mean weight difference in the sampled group of 60 adults had been 7 pounds instead of 18.2 pounds, but with the same standard deviation of 33.46 pounds. Would there still be enough evidence at the $\alpha = 0 . 0 5$ level to reject $H _ { 0 } : \mu = 0$ in favor of $H _ { A } : \mu \neq 0 ? ^ { 1 5 }$

G

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">15<sub>Re</sub>-<sub>c</sub>alculate the t-statistic: (7 − 0)/(33.46/√60) = 1.62. The p-value P (Z ≤ −1.62) + P (Z ≥ 1.62) = 0.105. Since p > α, there is insufficient evidence to reject H<sub>0</sub>. In this case, a sample average difference of 7 is not large enough to discount the possibility that the observed difference is due to sampling variation, and that the observations are from a distribution centered at 0.</span></small>

---

216

CHAPTER 4. FOUNDATIONS FOR INFERENCE

## 4.3.2 Two examples

## EXAMPLE 4.13

While fish and other types of seafood are important for a healthy diet, nearly all fish and shellfish contain traces of mercury. Dietary exposure to mercury can be particularly dangerous for young children and unborn babies. Regulatory organizations such as the US Food and Drug Administration (FDA) provide guidelines as to which types of fish have particularly high levels of mercury and should be completely avoided by pregnant women and young children; additionally, certain species known to have low mercury levels are recommended for consumption. While there is no international standard that defines excessive mercury levels in saltwater fish species, general con sensus is that fish with levels above 0.50 parts per million (ppm) should not be consumed. A study conducted to assess mercury levels for saltwater fish caught off the coast of New Jersey found that a sample of 23 bluefin tuna had mean mercury level of 0.52 ppm, with standard deviation 0.16 ppm.<sup>16</sup> Based on these data, should the FDA add bluefin tuna from New Jersey to the list of species recommended for consumption, or should a warning be issued about their mercury levels?

Let µ be the population average mercury content for bluefin tuna caught off the coast of New Jersey. Conduct a two-sided test of the hypothesis $\mu = 0 . 5 0$ ppm in order to assess the evidence for either definitive safety or potential danger.

Formulate the null and alternative hypotheses. $H _ { 0 } : \mu = 0 . 5 0$ ppm vs. $H _ { A } : \mu \neq 0 . 5 0$ ppm

Specify the significance level, α. A significance level of $\alpha = 0 . 0 5$ seems reasonable.

Calculate the test statistic. The t-statistic has value

$$
t = \frac {\overline {{x}} - \mu_ {0}}{s / \sqrt {n}} = \frac {0 . 5 2 - 0 . 5 0}{0 . 1 6 / \sqrt {2 3}} = 0. 5 9 9.
$$

Calculate the p-value. For this two-sided alternative $H _ { A } : \mu \neq 0 . 5 0 ,$ , the p-value is

$$
P (Z \leq - | t |) + P (Z \geq | t |) = 2 \times P (Z \geq 0. 5 9 9) = 0. 5 4 9.
$$

Draw a conclusion. The p-value is larger than the specified significance level α, as shown in Figure 4.15.<sup>17</sup> The data do not show that the mercury content of bluefin tuna caught off the coast of New Jersey differs significantly from 0.50 ppm. Since $p > \alpha ,$ , there is insufficient evidence to reject the null hypothesis that the mean mercury level for the New Jersey coastal population of bluefin tuna is 0.50 ppm.

Note that "failure to reject" is not equivalent to "accepting" the null hypothesis. Recall the earlier analogy related to the principle of "innocent until proven guilty". If there is not enough evidence to prove that the defendant is guilty, the official decision must be "not guilty", since the defendant may not necessarily be innocent. Similarly, while there is not enough evidence to suggest that µ is not equal to 0.5 ppm, it would be incorrect to claim that the evidence states that µ is 0.5 ppm.

From these data, there is not statistically significant evidence to either recommend these fish as clearly safe for consumption or to warn consumers against eating them. Based on these data, the Food and Drug Administration might decide to monitor this species more closely and conduct further studies.

E

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">16<sub>J</sub>. Burger, M. Gochfeld, Science of the Total Environment 409 (2011) 1418–1429</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">17<sub>The</sub> grey shaded regions are bounded by -1.96 and 1.96, since the area within 1.96 standard deviations of the mean captures 95% of the distribution.</span></small>

---

4.3. HYPOTHESIS TESTING

217

![](../../raw/pages_0209-0224/images/page_216_chart_2.jpg)

<details>
<summary>area</summary>

| Metric | Value |
| --- | --- |
| Mean \((\mu)\) | 0 |
| Standard Deviation (t) | 0.599 |
</details>

Figure 4.15: The large blue shaded regions represent the p-value, the area to the right of t = 0.599 and to the left of $- t = - 0 . 5 9 9 .$ . The smaller grey shaded regions represents the rejection region as defined by $\alpha ;$ in this case, an area of 0.025 in each tail. The t-statistic calculated from x would have to lie within either of the extreme tail areas to constitute sufficient evidence against the null hypothesis.

## EXAMPLE 4.14

In 2015, the National Sleep Foundation published new guidelines for the amount of sleep recommended for adults: 7-9 hours of sleep per night.<sup>18</sup> The NHANES survey includes a question asking respondents about how many hours per night they sleep; the responses are available in nhanes.samp. In the sample of 134 adults used in the BMI example, the average reported hours of sleep is 6.90, with standard deviation 1.39. Is there evidence that American adults sleep less than 7 hours per night?

Let µ be the population average of hours of sleep per night for US adults. Conduct a one-sided test, since the question asks whether the average amount of sleep per night might be less than 7 hours.

Formulate the null and alternative hypotheses. $H _ { 0 } : \mu = 7$ hours vs. $H _ { A } : \mu < 7$ hours.

Specify the significance level, α. Let $\alpha = 0 . 0 5 ,$ since the question does not reference a different value.

Calculate the test statistic. The t-statistic has value

$$
t = \frac {\overline {{x}} - \mu_ {0}}{s / \sqrt {n}} = \frac {6 . 9 0 - 7 . 0 0}{1 . 3 3 / \sqrt {1 3 4}} = - 0. 8 6 4.
$$

Calculate the p-value.

For this one-sided alternative $H _ { A } : \mu < 7 ,$ the p-value is

$$
P (Z \leq t) = P (Z <   - 0. 8 6 4) = 0. 1 9.
$$

Since the alternative states that µ0 is less than 7, the p-value is represented by the area to the left $\mu _ { 0 }$ of $t = - 0 . 8 6 4 ,$ , as shown in Figure 4.16.

Draw a conclusion. The p-value is larger than the specified significance level α. The null hypothesis is not rejected since the data do not represent sufficient evidence to support the claim that American adults sleep less than 7 hours per night.

E

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">18<sub>Sleep</sub> Health: Journal of the National Sleep Foundation, Vol. 1, Issue 1, pp. 40 - 43</span></small>

---

218

CHAPTER 4. FOUNDATIONS FOR INFERENCE

![](../../raw/pages_0209-0224/images/page_217_chart_2.jpg)

<details>
<summary>area</summary>

| Metric | Value |
| --- | --- |
| Mean (t) | -0.864 |
| Mean \((\mu)\) | 0 |
</details>

Figure 4.16: The large blue shaded region represents the p-value, the area to the left of $t = - 0 . 8 6 4$ . The smaller grey shaded region represents the rejection region of area 0.05 in the left tail.

![](../../raw/pages_0209-0224/images/page_217_image_4.jpg)

## GUIDED PRACTICE 4.15

From these data, is there sufficient evidence at the $\alpha = 0 . 1 0$ significance level to support the claim that American adults sleep more than 7 hours per night?<sup>19</sup>

## 4.3.3 Hypothesis testing and confidence intervals

The relationship between a hypothesis test and the corresponding confidence interval is defined by the significance level $\alpha ;$ the two approaches are based on the same inferential logic, and differ only in perspective. The hypothesis testing approach asks whether x is far enough away from $\mu _ { 0 }$ to be considered extreme, while the confidence interval approach asks whether $\mu _ { 0 }$ is close enough to x to be plausible. In both cases, "far enough" and "close enough" are defined by α, which determines the $z ^ { \star }$ used to calculate the margin of error $m = z ^ { \star } ( s / { \sqrt { n } } )$

Hypothesis Test. For a two-sided test, x needs to be at least m units away from $\mu _ { 0 }$ in either direction to be considered extreme. The t-points marking off the rejection region are equal to the $z ^ { \star }$ value used in the confidence interval, with the positive and negative t-points accounting for the ± structure in the confidence interval.

Confidence Interval. The plausible range of values for $\mu _ { 0 }$ around x is defined as $( \overline { { x } } - m , \; \overline { { x } } + m )$ If $\mu _ { 0 }$ is plausible, it can at most be m units away in either direction from x. If the interval does not contain $\mu _ { 0 } ,$ then $\mu _ { 0 }$ is implausible according to α and there is sufficient evidence to reject $H _ { 0 }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">19<sub>The</sub> t-statistic does not change from 1.65. Re-calculate the p-value since the alternative hypothesis is now H<sub>A</sub> : µ > 7: P (Z ≥ −0.864) = 0.81. Since p > α, there is insufficient evidence to reject H<sub>0</sub> at α = 0.10. A common error when conducting one-sided tests is to assume that the p-value will always be the area in the smaller of the two tails to the right or left of the observed value. It is important to remember that the area corresponding to the p-value is in the direction specified by the alternative hypothesis.</span></small>

![](../../raw/pages_0209-0224/images/page_217_chart_12.jpg)

<details>
<summary>area</summary>

| Metric | Value |
| --- | --- |
| t | -0.864 |
</details>

---

4.3. HYPOTHESIS TESTING

219

Suppose that a two-sided test is conducted at significance level $\alpha ;$ the confidence level of the matching interval is $(1 - \alpha)\%$ . For example, a two-sided hypothesis test with $\alpha   =   0 . 0 5$ can be compared to a 95% confidence interval. A hypothesis test will reject at $\alpha   =   0 . 0 5$ if the 95% confidence interval does not contain the null hypothesis value of the population mean $( \mu _ { 0 } )$

## THE RELATIONSHIP BETWEEN TWO-SIDED HYPOTHESIS TESTS AND CONFIDENCE INTERVALS

When testing the null hypothesis $H _ { 0 } : \mu = \mu _ { 0 }$ against the two-sided alternative $H _ { A } : \mu \neq \mu _ { 0 } ,   H _ { 0 }$ will be rejected at significance level α when the $1 0 0 ( 1 - \alpha )$ % confidence interval for µ does not contain $\mu _ { 0 }$

## EXAMPLE 4.16

Calculate the confidence interval for the average mercury level for bluefin tuna caught off the coast of New Jersey. The summary statistics for the sample of 21 fish are $\overline { { x } } = 0 . 5 3$ ppm and $s = 0 . 1 6 ~ \mathrm { p p m } .$ Does the interval agree with the results of Example 4.13?

The 95% confidence interval is:

$$
\overline {{x}} \pm 1. 9 6 \frac {s}{\sqrt {n}} = 0. 5 3 \pm 1. 9 6 \frac {0 . 1 6}{\sqrt {2 1}} = (0. 4 6 2, 0. 5 9 8) \mathrm{ppm}.
$$

The confidence interval is relatively wide, containing values below 0.50 ppm that might be regarded as safe, in addition to values that might be regarded as potentially dangerous. This interval supports the conclusion reached from hypothesis testing; the sample data does not suggest that the mercury level differs significantly from 0.50 ppm in either direction.

The same relationship applies for one-sided hypothesis tests. For example, a one-sided hypothesis test with $\alpha = 0 . 0 5$ and $H _ { A } : \mu > \mu _ { 0 }$ corresponds to a one-sided 95% confidence interval that has a lower bound, but no upper bound $( \mathrm { i . e . , } ~ ( \overline { { x } } - m , \infty ) )$

## THE RELATIONSHIP BETWEEN ONE-SIDED HYPOTHESIS TESTS AND CONFIDENCE INTERVALS

When testing the null hypothesis $H _ { 0 } : \mu = \mu _ { 0 }$ against the one-sided alternative $H _ { A } : \mu >$ $\mu _ { 0 } , H _ { 0 }$ will be rejected at significance level α when $\mu _ { 0 }$ is smaller than the lower bound of the $1 0 0 ( 1 - \alpha ) \%$ confidence interval for $\mu .$ This is equivalent to $\mu _ { 0 }$ having a value outside the lower one-sided confidence interval $( { \overline { { x } } } - m , \infty )$
When testing the null hypothesis $H _ { 0 } : \mu = \mu _ { 0 }$ against the one-sided alternative $H _ { A } : \mu <$ $\mu _ { 0 } , H _ { 0 }$ will be rejected at significance level α whenever $\mu _ { 0 }$ is larger than the upper bound of the $100(1 - \alpha)\%$ confidence interval for $\mu .$ This is equivalent to $\mu _ { 0 }$ having a value outside the upper one-sided confidence interval $( - \infty , { \overline { { x } } } + m )$

E

---

220

CHAPTER 4. FOUNDATIONS FOR INFERENCE

## EXAMPLE 4.17

Previously, a hypothesis test was conducted at $\alpha   =   0 . 0 5$ to test the null hypothesis $H _ { 0 } : \mu = 7$ hours against the alternative $H _ { A } : \mu < 7$ hours, for the average sleep per night US adults. Calculate the corresponding one-sided confidence interval and compare the information obtained from a confidence interval versus a hypothesis test. The summary statistics for the sample of 134 adults are $\overline { { x } } = 6 . 9$ and $s = 1 . 3 9$

In theory, a one-sided upper confidence interval extends to ∞ on the left side, but since it is impossible to get negative sleep, it is more sensible to bound this confidence interval by 0. The upper one-sided 95% confidence interval is

$$
(0, \overline {{x}} + 1. 6 4 5 \frac {s}{\sqrt {n}}) = (0, 6. 9 + 1. 6 4 5 \frac {1 . 3 9}{\sqrt {1 3 4}}) = (0,   7. 1) \text {hours}.
$$

From these data, we can be 95% confident that the average sleep per night among US adults is at most 7.1 hours per night. The $\mu _ { 0 }$ value of 7 hours is inside the one-sided interval; thus, there is not sufficient evidence to reject the null hypothesis $H _ { 0 } : \mu = 7$ against the one-sided alternative $H _ { 0 } : \mu < 7$ hours at $\alpha = 0 . 0 5$

The interval provides a range of plausible values for a parameter based on the observed sample; in this case, the data suggest that the population average sleep per night for US adults is no larger than 7.1 hours. The p-value from a hypothesis test represents a measure of the strength of the evidence against the null hypothesis, indicating how unusual the observed sample would be under $H _ { 0 } ;$ the hypothesis test indicated that the data do not seem extreme enough $\left( p = 0 . 1 9 \right)$ to contradict the hypothesis that the population average sleep hours per night is 7.

In practice, both a p-value and a confidence interval are computed when using a sample to make inferences about a population parameter.

## 4.3.4 Decision errors

Hypothesis tests can potentially result in incorrect decisions, such as rejecting the null hypothesis when the null is actually true. Figure 4.17 shows the four possible ways that the conclusion of a test can be right or wrong.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Test conclusion</td></tr><tr><td>Fail to reject  $H_0$ </td><td>Reject  $H_0$  in favor of  $H_A$ </td></tr><tr><td rowspan="2">Reality</td><td> $H_0$  True</td><td>Correct Decision</td><td>Type 1 Error</td></tr><tr><td> $H_A$  True</td><td>Type 2 Error</td><td>Correct Decision</td></tr></table>

Figure 4.17: Four different scenarios for hypothesis tests.

Rejecting the null hypothesis when the null is true represents a **Type I error**, while a **Type II error** refers to failing to reject the null hypothesis when the alternative is true.

E

---

4.3. HYPOTHESIS TESTING

221

E

## EXAMPLE 4.18

In a trial, the defendant is either innocent $( H _ { 0 } )$ or guilty $( H _ { A } )$ . After hearing evidence from both the prosecution and the defense, the court must reach a verdict. What does a Type I Error represent in this context? What does a Type II Error represent?

If the court makes a Type I error, this means the defendant is innocent, but wrongly convicted (rejecting $H _ { 0 }$ when $H _ { 0 }$ is true). A Type II error means the court failed to convict a defendant that was guilty (failing to reject $H _ { 0 }$ when $H _ { 0 }$ is false).

The probability of making a Type I error is the same as the significance level $\alpha ,$ since α determines the cutoff point for rejecting the null hypothesis. For example, if α is chosen to be 0.05, then there is a 5% chance of incorrectly rejecting $H _ { 0 }$

The rate of Type I error can be reduced by lowering α (e.g., to 0.01 instead of 0.05); doing so requires an observation to be more extreme to qualify as sufficient evidence against the null hypothesis. However, this inevitably raises the rate of Type II errors, since the test will now have a higher chance of failing to reject the null hypothesis when the alternative is true.

E

## EXAMPLE 4.19

In a courtroom setting, how might the rate of Type I errors be reduced? What effect would this have on the rate of Type II errors?

Lowering the rate of Type I error is equivalent to raising the standards for conviction such that fewer people are wrongly convicted. This increases Type II error, since higher standards for conviction leads to fewer convictions for people who are actually guilty.

G

## GUIDED PRACTICE 4.20

In a courtroom setting, how might the rate of Type II errors be reduced? What effect would this have on the rate of Type I errors?<sup>20</sup>

## Choosing a significance level

Reducing the error probability of one type of error increases the chance of making the other type. As a result, the significance level is often adjusted based on the consequences of any decisions that might follow from the result of a significance test.

By convention, most scientific studies use a significance level of $\alpha = 0.05;$ small enough such that the chance of a Type I error is relatively rare (occurring on average 5 out of 100 times), but also large enough to prevent the null hypothesis from almost never being rejected. If a Type I error is especially dangerous or costly, a smaller value of α is chosen (e.g., 0.01). Under this scenario, it is better to be cautious about rejecting the null hypothesis, so very strong evidence against $H _ { 0 }$ is required in order to reject the null and accept the alternative. Conversely, if a Type II error is relatively dangerous, then a larger value of α is chosen (e.g., 0.10). Hypothesis tests with larger values of α will reject $H _ { 0 }$ more often.

For example, in the early stages of assessing a drug therapy, it may be important to continue further testing even if there is not very strong initial evidence for a beneficial effect. If the scientists conducting the research know that any initial positive results will eventually be more rigorously tested in a larger study, they might choose to use $\alpha = 0 . 1 0$ to reduce the chances of making a Type II error: prematurely ending research on what might turn out to be a promising drug.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">20<sub>To</sub> lower the rate of Type II error, the court could lower the standards for conviction, or in other words, lower the bar for what constitutes sufficient evidence of guilt (increase α, e.g. to 0.10 instead of 0.05). This will result in more guilty people being convicted, but also increase the rate of wrongful convictions, increasing the Type I error.</span></small>

---

222

CHAPTER 4. FOUNDATIONS FOR INFERENCE

A government agency responsible for approving drugs to be marketed to the general population, however, would likely be biased towards minimizing the chances of making a Type I error—approving a drug that turns out to be unsafe or ineffective. As a result, they might conduct tests at significance level 0.01 in order to reduce the chances of concluding that a drug works when it is in fact ineffective. The US FDA and the European Medical Agency (EMA) customarily require that two independent studies show the efficacy of a new drug or regimen using $\alpha = 0 . 0 5$ , though other values are sometimes used.

## 4.3.5 Choosing between one-sided and two-sided tests

In some cases, the choice of a one-sided or two-sided test can influence whether the null hypothesis is rejected. For example, consider a sample for which the t-statistic is 1.80. If a twosided test is conducted at $\alpha = 0 . 0 5$ , the p-value is

$$
P (Z \leq - | t |) + P (Z \geq | t |) = 2 P (Z \geq 1. 8 0) = 0. 0 7 2.
$$

There is insufficient evidence to reject $H _ { 0 } ,$ since $p > \alpha$ . However, what if a one-sided test is conducted at $\alpha = 0 . 0 5$ , with $H _ { A } : \mu > \mu _ { 0 } ?$ In this case, the p-value is

$$
P (Z \geq t) = P (Z \geq 1. 8 0) = 0. 0 3 6.
$$

The conclusion of the test is different: since $p < \alpha ,$ , there is sufficient evidence to reject $H _ { 0 }$ in favor of the alternative hypothesis. Figure 4.18 illustrates the different outcomes from the tests.

![](../../raw/pages_0209-0224/images/page_221_chart_9.jpg)

<details>
<summary>area</summary>

| Parameter | Value |
| --- | --- |
| \(\alpha/2\) | 0.025 |
| t | 1.80 |
| \(\mu\) | 0 |
</details>

Figure 4.18: Under a one-sided test at significance level $\alpha = 0 . 0 5 ,$ , a t-statistic of 1.80 is within the rejection region (shaded light blue). However, it would not be within the rejection region under a two-sided test with $\alpha = 0 . 0 5$ (darker blue).

Two-sided tests are more "conservative" than one-sided tests; it is more difficult to reject the null hypothesis with a two-sided test. The p-value for a one-sided test is exactly half the p-value for a two-sided test conducted at the same significance level; as a result, it is easier for the p-value from a one-sided test to be smaller than α. Additionally, since the rejection region for a two-sided test is divided between two tails, a test statistic needs to be more extreme in order to fall within a rejection region. While the t-statistic of 1.80 is not within the two-sided rejection region, it is within the one-sided rejection region.<sup>21</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">21<sub>The</sub> two-sided rejection regions are bounded by -1.96 and 1.96, while the one-sided rejection region begins at 1.65.</span></small>

---

4.3. HYPOTHESIS TESTING

223

For a fixed sample size, a one-tailed test will have a smaller probability of Type II error in comparison to a two-tailed test conducted at the same α level. In other words, with a one-sided test, it is easier to reject the null hypothesis if the alternative is actually true.

The choice of test should be driven by context, although it is not always clear which test is appropriate. Since it is easier to reject $H _ { 0 }$ with the one-tailed test, it might be tempting to always use a one-tailed test when a significant result in a particular direction would be interesting or desirable.

However, it is important to consider the potential consequences of missing a significant difference in the untested direction. Generally, a two-sided test is the safest option, since it does not incorporate any existing biases about the direction of the results and can detect a difference at either the upper or lower tail. In the 1980s, researchers were interested in assessing a new set of drugs expected to be more effective at reducing heart arrhythmias than previously available therapies. They designed a one-sided clinical trial, convinced that the newer therapy would reduce mortality. The trial was quickly terminated due to an unanticipated effect of the drug; an independent review board found that the newer therapy was almost 4 times as likely to kill patients as a placebo! In a clinical research setting, it can be dangerous and even unethical to conduct a onesided test under the belief that there is no possibility of patient harm from the drug intervention being tested.

One-sided tests are appropriate if the consequences of missing an effect in the untested direction are negligible, or if a large observed difference in the untested direction and a conclusion of "no difference" lead to the same decision. For example, suppose that a company has developed a drug to reduce blood pressure that is cheaper to produce than current options available on the market. If the drug is shown to be equally effective or more effective than an existing drug, the company will continue investing in it. Thus, they are only interested in testing the alternative hy pothesis that the new drug is less effective than the existing drug, in which case, they will stop the project. It is acceptable to conduct a one-sided test in this situation since missing an effect in the other direction causes no harm.

The decision as to whether to use a one-sided or two-sided test must be made before data analysis begins, in order to avoid biasing conclusions based on the results of a hypothesis test. In particular, changing to a one-sided test after discovering that the results are "almost" significant for the two-sided test is unacceptable. Manipulating analyses in order to achieve low p-values leads to invalid results that are often not replicable. Unfortunately, this kind of "significance-chasing" has become widespread in published science, leading to concern that most current published research findings are false.

---

224

CHAPTER 4. FOUNDATIONS FOR INFERENCE

## 4.3.6 The informal use of p-values

Formal hypothesis tests are designed for settings where a decision or a claim about a hypoth esis follows a test, such as in scientific publications where an investigator wishes to claim that an intervention changes an outcome. However, progress in science is usually based on a collection of studies or experiments, and it is often the case that the results of one study are used as a guide for the next study or experiment.

Sir Ronald Fisher was the first to propose using p-values as one of the statistical tools for evaluating an experiment. In his view, an outcome from an experiment that would only happen 1 in 20 times $\left( p = 0 . 0 5 \right)$ was worth investigating further. The use of p-values for formal decision making came later. While valuable, formal hypothesis testing can often be overused; not all significant results should lead to a definitive claim, but instead prompt further analysis.

The formal use of p-values is emphasized here because of its prominence in the scientific literature, and because the steps outlined are fundamental to the scientific method for empirical research: specify hypotheses, state in advance how strong the evidence should be to constitute sufficient evidence against the null, specify the method of analysis and compute the test statistic, draw a conclusion. These steps are designed to avoid the pitfall of choosing a hypothesis or method of analysis that is biased by the data and hence reaches a conclusion that may not be reproducible.

---

4.4. NOTES

225

## 4.4 Notes

Confidence intervals and hypothesis testing are two of the central concepts in inference for a population based on a sample. The confidence interval shows a range of population parameter values consistent with the observed sample, and is often used to design additional studies. Hypoth esis testing is a useful tool for evaluating the strength of the evidence against a working hypothesis according to a pre-specified standard for accepting or rejecting hypotheses.

The calculation of p-values and confidence intervals is relatively straightforward; given the necessary summary statistics, α, and confidence coefficients, finding any p-value or confidence interval simply involves a set of formulaic steps. However, the more difficult parts of any inference problem are the steps that do not involve any calculations. Specifying appropriate null and alternative hypotheses for a test relies on an understanding of the problem context and the scientific setting of the investigation. Similarly, a choice about a confidence coefficient for an interval relies on judgment as to balancing precision against the chance of possible error. It is also not necessarily obvious when a significance level other than $\alpha = 0 . 0 5$ should be applied. These choices represent the largest distinction between a true statistics problem as compared to a purely mathematical exercise.

Furthermore, in order to rely on the conclusions drawn from making inferences, it is necessary to consider factors such as study design, measurement quality, and the validity of any assumptions made. For example, is it valid to use the normal approximation to calculate p-values? In small to moderate sample sizes $\left( 3 0 \leq n \leq 5 0 \right)$ , it may not be clear that the normal model is accurate. It is even necessary to be cautious about the use and interpretation of the p-value. For example, an article published in Nature about the mis-use of p-values references a published study that showed people who meet their spouses online are more likely to have marital satisfaction, with p-value less than 0.001. However, statistical significance does not measure the importance or practical relevance of a result; in this case, the change in happiness moved from 5.48 to 5.64 on a 7-point scale. A p-value reported without context or other evidence is uninformative and potentially deceptive.

These nuanced issues cannot be adequately covered in any introduction to statistics. It is unrealistic to encourage students to use their own judgment with aspects of inference that even experienced investigators find challenging. At the same time, it would also be misleading to suggest that the choices are always clear-cut in practice. It seems best to offer some practical guidance for getting started:

– The default choice of α is 0.05; similarly, the default confidence coefficient for a confidence interval is 95%.
– Unless it is clear from the context of a problem that change in only one direction from the null hypothesis is of interest, the alternative hypothesis should be two-sided.
The use of a standard normal distribution to calculate p-values is reasonable for sample sizes of 30 or more if the distribution of data are not strongly skewed and there are no large outliers. If there is skew or a few large outliers, sample sizes of 50 or more are usually sufficient.
– Pay attention to the context of a problem, particularly when formulating hypotheses and drawing conclusions.

The next chapters will discuss methods of inference in specific settings, such as comparing two groups. These settings expand on the concepts discussed in this chapter and offer additional opportunities to practice calculating tests and intervals, reading problems for context, and checking underlying assumptions behind methods of inference.

---

226

CHAPTER 4. FOUNDATIONS FOR INFERENCE

The labs for the chapter reinforce conceptual understanding of confidence intervals and hy pothesis tests, and their link to sampling variability using the data from the YRBSS and NHANES. Both datasets are large enough to be viewed in an instructional setting as populations from which repeated samples can be drawn. They are useful platforms for illustrating the conceptual role of hypothetical repeated sampling in the properties of tests and intervals, a topic which many students find difficult. Students may find the last lab for this chapter (Lab 4) particularly helpful for understanding conceptual details of inference, such as the distinction between the significance level α and the p-value, and the definition of α as the Type I error rate.

---

4.5. EXERCISES

227

## 4.5 Exercises

## 4.5.1 Variability in estimates

**4.1 Egg coloration.** The evolutionary role of variation in bird egg coloration remains mysterious to biologists. One hypothesis suggests that egg color may play a role in sexual selection. For example, perhaps healthier females are able to deposit more blue-green pigment into eggshells instead of using it themselves as an antioxidant. Researchers measured the blue-green chroma (BGC) of 70 different collared flycatcher nests in an area of the Czech Republic.

![](../../raw/pages_0225-0240/images/page_226_chart_5.jpg)

<details>
<summary>histogram</summary>

| Statistic | Value |
| --- | --- |
| Min | 0.5675 |
| Q1 | 0.5977 |
| Median | 0.6046 |
| Mean | 0.6052 |
| SD | 0.0131 |
| Q3 | 0.6126 |
| Max | 0.6355 |
</details>

(a) What is the point estimate for the average BGC of nests?

(b) What is the point estimate for the standard deviation of the BGC of eggs across nests?

(c) Would a nest with average BGC of 0.63 be considered unusually high? Explain your reasoning.

(d) Compute the standard error of the sample mean using the summary statistics.

---

228

CHAPTER 4. FOUNDATIONS FOR INFERENCE

**4.2 Heights of adults.** Researchers studying anthropometry collected body girth measurements and skeletal diameter measurements, as well as age, weight, height and gender, for 507 physically active individuals. The histogram below shows the sample distribution of heights in centimeters.<sup>22</sup>

![](../../raw/pages_0225-0240/images/page_227_chart_3.jpg)

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

(a) What is the point estimate for the average height of active individuals?
(b) What is the point estimate for the standard deviation of the heights of active individuals? What about the IQR?
(c) Is a person who is 1m 80cm (180 cm) tall considered unusually tall? And is a person who is 1m 55cm (155cm) considered unusually short? Explain your reasoning.
(d) The researchers take another random sample of physically active individuals. Would you expect the mean and the standard deviation of this new sample to be the ones given above? Explain your reasoning.
(e) The sample means obtained are point estimates for the mean height of all active individuals, if the sample of individuals is equivalent to a simple random sample. What measure is used to quantify the variability of such an estimate? Compute this quantity using the data from the original sample under the condition that the data are a simple random sample.

**4.3 Hen eggs.** The distribution of the number of eggs laid by a certain species of hen during their breeding period is on average, 35 eggs, with a standard deviation of 18.2. Suppose a group of researchers randomly samples 45 hens of this species, counts the number of eggs laid during their breeding period, and records the sample mean. They repeat this 1,000 times, and build a distribution of sample means.

(a) What is this distribution called?
(b) Would you expect the shape of this distribution to be symmetric, right skewed, or left skewed? Explain your reasoning.
(c) Calculate the variability of this distribution and state the appropriate term used to refer to this value.
(d) Suppose the researchers’ budget is reduced and they are only able to collect random samples of 10 hens. The sample mean of the number of eggs is recorded, and we repeat this 1,000 times, and build a new distribution of sample means. How will the variability of this new distribution compare to the variability of the original distribution?

22<sub>G</sub>. Heinz et al. “[Exploring relationships in body dimensions](http://www.openintro.org/redirect.php?go=textbook-body_dim_2003&referrer=biostat1_pdf)”. In: Journal of Statistics Education 11.2 (2003).

---

4.5. EXERCISES

229

## 4.5.2 Confidence intervals

**4.4 Mental health, Part I.** The 2010 General Social Survey asked the question: “For how many days during the past 30 days was your mental health, which includes stress, depression, and problems with emotions, not good?" Based on responses from 1,151 US residents, the survey reported a 95% confidence interval of 3.40 to 4.24 days in 2010.

(a) Interpret this interval in context of the data.
(b) What does “95% confident" mean? Explain in the context of the application.
(c) If a new survey were to be done with 500 Americans, would the standard error of the estimate be larger, smaller, or about the same? Assume the standard deviation has remained constant since 2010.

**4.5 Relaxing after work, Part I.** The 2010 General Social Survey asked the question: “After an average work day, about how many hours do you have to relax or pursue activities that you enjoy?" to a random sample of 1,155 Americans.<sup>23</sup> A 95% confidence interval for the mean number of hours spent relaxing or pursuing activities they enjoy is (1.38, 1.92).

(a) Interpret this interval in context of the data.
(b) Suppose another set of researchers reported a confidence interval with a larger margin of error based on the same sample of 1,155 Americans. How does their confidence level compare to the confidence level of the interval stated above?
(c) Suppose next year a new survey asking the same question is conducted, and this time the sample size is 2,500. Assuming that the population characteristics, with respect to how much time people spend relaxing after work, have not changed much within a year. How will the margin of error of the new 95% confidence interval compare to the margin of error of the interval stated above?
(d) Suppose the researchers think that 90% confidence interval would be more appropriate. Will this new interval be smaller or larger than the original 95% confidence interval? Justify your answer. (Assume that the standard deviation remains constant).

23<sub>National</sub> Opinion Research Center, [General Social Survey, 2010](http://www.openintro.org/redirect.php?go=textbook-gss_2010&referrer=biostat1_pdf).

---

230

CHAPTER 4. FOUNDATIONS FOR INFERENCE

**4.6 Thanksgiving spending, Part I.** The 2009 holiday retail season, which kicked off on November 27, 2009 (the day after Thanksgiving), had been marked by somewhat lower self-reported consumer spending than was seen during the comparable period in 2008. To get an estimate of consumer spending, 436 randomly sampled American adults were surveyed. Daily consumer spending for the six-day period after Thanksgiving, spanning the Black Friday weekend and Cyber Monday, averaged \$84.71. A 95% confidence interval based on this sample is (\$80.31, \$89.11). Determine whether the following statements are true or false, and explain your reasoning.

![](../../raw/pages_0225-0240/images/page_229_chart_3.jpg)

<details>
<summary>histogram</summary>

| Spending (Bin) | Frequency |
| --- | --- |
| 0~25 | ~10 |
| 25~50 | ~48 |
| 50~75 | ~95 |
| 75~100 | ~80 |
| 100~125 | ~73 |
| 125~150 | ~42 |
| 150~175 | ~37 |
| 175~200 | ~19 |
| 200~225 | ~10 |
| 225~250 | ~12 |
| 250~275 | ~5 |
| 275~300 | ~4 |
| 300~325 | ~1 |
| 325~350 | ~1 |
</details>

(a) We are 95% confident that the average spending of these 436 American adults is between \$80.31 and \$89.11.
(b) This confidence interval is not valid since the distribution of spending in the sample is right skewed.
(c) 95% of random samples have a sample mean between \$80.31 and \$89.11.
(d) We are 95% confident that the average spending of all American adults is between \$80.31 and \$89.11.
(e) A 90% confidence interval would be narrower than the 95% confidence interval.
(f) The margin of error is 4.4.

**4.7 Waiting at an ER, Part I.** A hospital administrator hoping to improve wait times decides to estimate the average emergency room waiting time at her hospital. She collects a simple random sample of 64 patients and determines the time (in minutes) between when they checked in to the ER until they were first seen by a doctor. A 95% confidence interval based on this sample is (128 minutes, 147 minutes), which is based on the normal model for the mean. Determine whether the following statements are true or false, and explain your reasoning.

(a) This confidence interval is not valid since we do not know if the population distribution of the ER wait times is nearly Normal.
(b) We are 95% confident that the average waiting time of these 64 emergency room patients is between 128 and 147 minutes.
(c) We are 95% confident that the average waiting time of all patients at this hospital’s emergency room is between 128 and 147 minutes.
(d) 95% of random samples have a sample mean between 128 and 147 minutes.
(e) A 99% confidence interval would be narrower than the 95% confidence interval since we need to be more sure of our estimate.
(f) The margin of error is 9.5 and the sample mean is 137.5.
(g) Halving the margin of error of a 95% confidence interval requires doubling the sample size.

---

4.5. EXERCISES

231

**4.8 Age at first marriage, Part I.** The National Survey of Family Growth conducted by the Centers for Disease Control gathers information on family life, marriage and divorce, pregnancy, infertility, use of contraception, and men’s and women’s health. One of the variables collected on this survey is the age at first marriage. The histogram below shows the distribution of ages at first marriage of 5,534 randomly sampled women between 2006 and 2010. The average age at first marriage among these women is 23.44 with a standard deviation of 4.72.<sup>24</sup>

![](../../raw/pages_0225-0240/images/page_230_chart_3.jpg)

<details>
<summary>histogram</summary>

| Age Range | Frequency |
| --- | --- |
| 10~11 | ~5 |
| 11~12 | ~30 |
| 12~13 | ~160 |
| 13~14 | ~520 |
| 14~15 | ~940 |
| 15~16 | ~980 |
| 16~17 | ~870 |
| 17~18 | ~760 |
| 18~19 | ~490 |
| 19~20 | ~350 |
| 20~21 | ~180 |
| 21~22 | ~130 |
| 22~23 | ~60 |
| 23~24 | ~40 |
| 24~25 | ~25 |
| 25~26 | ~15 |
| 26~27 | ~5 |
</details>

Estimate the average age at first marriage of women using a 95% confidence interval, and interpret this interval in context. Discuss any relevant assumptions.

**4.9 Mental health, Part II.** The General Social Survey (GSS) is a sociological survey used to collect data on demographic characteristics and attitudes of residents of the United States. The 2010 General Social Survey asked the question, "For how many days during the past 30 days was your mental health not good?" Based on responses from 1,151 US adults, the survey reported a 95% confidence interval of (3.40, 4.24) days. Assume that the sampled US adults are representative of all US adults.

(a) Identify each of the following statements as true or false. Justify your answers.

i. The confidence interval of (3.40, 4.24) contains the mean days out of the past 30 days that U.S. adults experienced poor mental health.
ii. There is a 95% chance that the mean days out of the past 30 days that U.S. adults experienced poor mental health is within the confidence interval (3.40, 4.24).
iii. If we repeated this survey 1,000 times and constructed a 95% confidence interval each time, then approximately 950 of those intervals would contain the true mean days out of the past 30 days that U.S. adults experienced poor mental health.
iv. The survey provides statistically significant evidence at the α = 0.05 significance level that the mean days out of the past 30 days that U.S. adults experienced poor mental health is not 4.5 days.
v. We can be 95% confident that the mean days out of the past 30 days that U.S. adults experienced poor mental health is 3.82 days.
vi. We can be 95% confident that the interval (3.40, 4.24) days contains the mean days out of the past 30 days that the sampled adults experienced poor mental health.

(b) Would you expect the 90% confidence interval to be larger or smaller than the 95% confidence interval? Explain your reasoning.

(c) Calculate the 90% confidence interval.

24<sub>Centers</sub> for Disease Control and Prevention, [National Survey of Family Growth, 2010.](http://www.openintro.org/redirect.php?go=textbook-ntnl_survey_family_growth_2010&referrer=biostat1_pdf)

---

232

CHAPTER 4. FOUNDATIONS FOR INFERENCE

**4.10 Leisure time, Part III.** In 2010, the General Social Survey collected responses from 1,154 US residents. The survey is conducted face-to-face with an in-person interview of a randomly selected sample of adults. One of the questions on the survey is "After an average workday, about how many hours do you have to relax or pursue activities that you enjoy?" A 95% confidence interval from the 2010 GSS survey for the collected answers is 3.53 to 3.83 hours. Identify each of the following statements as true or false. Explain your answers.

(a) If the researchers wanted to report a confidence interval with a smaller margin of error based on the same sample of 1,154 Americans, the confidence interval would be larger.
(b) We can be 95% confident that the interval (3.53, 3.83) hours contains the mean hours that the sampled adults have for leisure time after an average workday.
(c) The confidence interval of (3.53, 3.83) hours contains the mean hours that U.S. adults have for leisure time after an average workday.
(d) The survey provides statistically significant evidence at the α = 0.05 significance level that the mean hours U.S. adults have for leisure time after the average workday is 3.6 hours.
(e) There is a 5% chance that the interval (3.53, 3.83) hours does not contain the mean hours that U.S. adults have for leisure time after an average workday.
(f) The interval (3.53, 3.83) hours provides evidence at the α = 0.05 significance level that U.S. adults, on average, have fewer than 3.9 hours of leisure time after a typical workday.

## 4.5.3 Hypothesis testing

**4.11 Identify hypotheses, Part I.** Write the null and alternative hypotheses in words and then symbols for each of the following situations.

(a) New York is known as “the city that never sleeps". A random sample of 25 New Yorkers were asked how much sleep they get per night. Do these data provide convincing evidence that New Yorkers on average sleep less than 8 hours a night?
(b) Employers at a firm are worried about the effect of March Madness, a basketball championship held each spring in the US, on employee productivity. They estimate that on a regular business day employees spend on average 15 minutes of company time checking personal email, making personal phone calls, etc. They also collect data on how much company time employees spend on such non- business activities during March Madness. They want to determine if these data provide convincing evidence that employee productivity decreases during March Madness.

**4.12 Identify hypotheses, Part II.** Write the null and alternative hypotheses in words and using symbols for each of the following situations.

(a) Since 2008, chain restaurants in California have been required to display calorie counts of each menu item. Prior to menus displaying calorie counts, the average calorie intake of diners at a restaurant was 1100 calories. After calorie counts started to be displayed on menus, a nutritionist collected data on the number of calories consumed at this restaurant from a random sample of diners. Do these data provide convincing evidence of a difference in the average calorie intake of a diners at this restaurant?
(b) Based on the performance of those who took the GRE exam between July 1, 2004 and June 30, 2007, the average Verbal Reasoning score was calculated to be 462. In 2011 the average verbal score was slightly higher. Do these data provide convincing evidence that the average GRE Verbal Reasoning score has changed since 2004?

---

4.5. EXERCISES

233

**4.13 Online communication.** A study suggests that the average college student spends 10 hours per week communicating with others online. You believe that this is an underestimate and decide to collect your own sample for a hypothesis test. You randomly sample 60 students from your dorm and find that on average they spent 13.5 hours a week communicating with others online. A friend of yours, who offers to help you with the hypothesis test, comes up with the following set of hypotheses. Indicate any errors you see.

$$
H _ {0}: \bar {x} <   1 0 \text {   hours }
$$

$$
H _ {A}: \bar {x} > 1 3. 5 \text {   hours }
$$

**4.14 Age at first marriage, Part II.** Exercise 4.8 presents the results of a 2006 - 2010 survey showing that the average age of women at first marriage is 23.44. Suppose a social scientist believes that this value has increased in 2012, but she would also be interested if she found a decrease. Below is how she set up her hypotheses. Indicate any errors you see.

$$
H _ {0}: \bar {x} = 2 3. 4 4 \text {years}
$$

$$
H _ {A}: \bar {x} > 2 3. 4 4 \text {years}
$$

**4.15 Waiting at an ER, Part II.** Exercise 4.7 provides a 95% confidence interval for the mean waiting time at an emergency room (ER) of (128 minutes, 147 minutes). Answer the following questions based on this interval.

(a) A local newspaper claims that the average waiting time at this ER exceeds 3 hours. Is this claim supported by the confidence interval? Explain your reasoning.
(b) The Dean of Medicine at this hospital claims the average wait time is 2.2 hours. Is this claim supported by the confidence interval? Explain your reasoning.
(c) Without actually calculating the interval, determine if the claim of the Dean from part (b) would be supported based on a 99% confidence interval?

**4.16 Gifted children, Part I.** Researchers investigating characteristics of gifted children collected data from schools in a large city on a random sample of thirty-six children who were identified as gifted children soon after they reached the age of four. The following histogram shows the distribution of the ages (in months) at which these children first counted to 10 successfully. Also provided are some sample statistics.<sup>25</sup>

![](../../raw/pages_0225-0240/images/page_232_chart_14.jpg)

<details>
<summary>histogram</summary>

| Age (months) | Frequency |
| --- | --- |
| 20~22 | 1 |
| 22~24 | 3 |
| 24~26 | 2 |
| 26~28 | 5 |
| 28~30 | 6 |
| 30~32 | 7 |
| 32~34 | 3 |
| 34~36 | 7 |
| 36~38 | 1 |
| 38~40 | 1 |
</details>

(a) Are conditions for inference satisfied?
(b) Suppose an online survey reports that children first count to 10 successfully when they are 32 months old, on average. Perform a hypothesis test to evaluate if these data provide convincing evidence that the average age at which gifted children first count to 10 successfully is less than the general average of 32 months. Use a significance level of 0.10.
(c) Interpret the p-value in context of the hypothesis test and the data.
(d) Calculate a 90% confidence interval for the average age at which gifted children first count to 10 successfully.
(e) Do your results from the hypothesis test and the confidence interval agree? Explain.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">25<sub>F</sub>.A. Graybill and H.K. Iyer. Regression Analysis: Concepts and Applications. Duxbury Press, 1994, pp. 511–516.</span></small>

---

234

CHAPTER 4. FOUNDATIONS FOR INFERENCE

**4.17 Nutrition labels.** The nutrition label on a bag of potato chips says that a one ounce (28 gram) serving of potato chips has 130 calories and contains ten grams of fat, with three grams of saturated fat. A random sample of 35 bags yielded a sample mean of 134 calories with a standard deviation of 17 calories. Is there evidence that the nutrition label does not provide an accurate measure of calories in the bags of potato chips? We have verified the independence, sample size, and skew conditions are satisfied.
**4.18 Waiting at an ER, Part III.** The hospital administrator mentioned in Exercise 4.7 randomly selected 64 patients and measured the time (in minutes) between when they checked in to the ER and the time they were first seen by a doctor. The average time is 137.5 minutes and the standard deviation is 39 minutes. She is getting grief from her supervisor on the basis that the wait times in the ER has increased greatly from last year’s average of 127 minutes. However, she claims that the increase is probably just due to chance.

(a) Calculate a 95% confidence interval. Is the change in wait times statistically significant at the $\alpha = 0 . 0 5$ level?
(b) Would the conclusion in part (a) change if the significance level were changed to $\alpha = 0 . 0 1 ?$
(c) Is the supervisor justified in criticizing the hospital administrator regarding the change in ER wait times? How might you present an argument in favor of the administrator?

**4.19 Birth weights.** Suppose an investigator takes a random sample of n = 50 birth weights from several teaching hospitals located in an inner-city neighborhood. In her random sample, the sample mean x is 3,150 grams and the standard deviation is 250 grams.

(a) Calculate a 95% confidence interval for the population mean birth weight in these hospitals.
(b) The typical weight of a baby at birth for the US population is 3,250 grams. The investigator suspects that the birth weights of babies in these teaching hospitals is different than 3,250 grams, but she is not sure if it is smaller (from malnutrition) or larger (because of obesity prevalence in mothers giving birth at these hospitals). Carry out the hypothesis test that she would conduct.

**4.20 Gifted children, Part II.** Exercise 4.16 describes a study on gifted children. In this study, along with variables on the children, the researchers also collected data on the mother’s and father’s IQ of the 36 randomly sampled gifted children. The histogram below shows the distribution of mother’s IQ. Also provided are some sample statistics.

![](../../raw/pages_0225-0240/images/page_233_chart_14.jpg)

<details>
<summary>histogram</summary>

| Bin (Mother's IQ) | Frequency |
| --- | --- |
| 100~105 | ~1 |
| 105~110 | ~3 |
| 110~115 | ~7 |
| 115~120 | ~13 |
| 120~125 | ~7 |
| 125~130 | ~4 |
| 130~135 | ~1 |
</details>

(a) Perform a hypothesis test to evaluate if these data provide convincing evidence that the average IQ of mothers of gifted children is different than the average IQ for the population at large, which is 100. Use a significance level of 0.10.
(b) Calculate a 90% confidence interval for the average IQ of mothers of gifted children.
(c) Do your results from the hypothesis test and the confidence interval agree? Explain.

---

4.5. EXERCISES

235

**4.21 Testing for fibromyalgia.** A patient named Diana was diagnosed with fibromyalgia, a long-term syndrome of body pain, and was prescribed anti-depressants. Being the skeptic that she is, Diana didn’t initially believe that anti-depressants would help her symptoms. However after a couple months of being on the medication she decides that the anti-depressants are working, because she feels like her symptoms are in fact getting better.

(a) Write the hypotheses in words for Diana’s skeptical position when she started taking the anti-depressants.
(b) What is a Type 1 Error in this context?
(c) What is a Type 2 Error in this context?

**4.22 Testing for food safety.** A food safety inspector is called upon to investigate a restaurant with a few customer reports of poor sanitation practices. The food safety inspector uses a hypothesis testing framework to evaluate whether regulations are not being met. If he decides the restaurant is in gross violation, its license to serve food will be revoked.

(a) Write the hypotheses in words.
(b) What is a Type 1 Error in this context?
(c) What is a Type 2 Error in this context?
(d) Which error is more problematic for the restaurant owner? Why?
(e) Which error is more problematic for the diners? Why?

(f) As a diner, would you prefer that the food safety inspector requires strong evidence or very strong evidence of health concerns before revoking a restaurant’s license? Explain your reasoning.

**4.23 Which is higher?** In each part below, there is a value of interest and two scenarios (I and II). For each part, report if the value of interest is larger under scenario I, scenario II, or whether the value is equal under the scenarios.

(a) The standard error of x¯ when s = 120 and (I) n = 25 or (II) n = 125.
(b) The margin of error of a confidence interval when the confidence level is (I) 90% or (II) 80%.
(c) The p-value for a Z-statistic of 2.5 when (I) n = 500 or (II) n = 1000.
(d) The probability of making a Type 2 Error when the alternative hypothesis is true and the significance level is (I) 0.05 or (II) 0.10.

**4.24 True or false.** Determine if the following statements are true or false, and explain your reasoning. If false, state how it could be corrected.

(a) If a given value (for example, the null hypothesized value of a parameter) is within a 95% confidence interval, it will also be within a 99% confidence interval.
(b) Decreasing the significance level (α) will increase the probability of making a Type 1 Error.
(c) Suppose the null hypothesis is $\mu = 5$ and we fail to reject $H _ { 0 }$ . Under this scenario, the true population mean is 5.
(d) If the alternative hypothesis is true, then the probability of making a Type 2 Error and the power of a test add up to 1.
(e) With large sample sizes, even small differences between the null value and the true value of the parameter, a difference often called the effect size , will be identified as statistically significant.
