Using the model in Equation 6.12, the prediction equation can be written

$$
\widehat {\log (\text {inf.mortality})} = 4. 0 1 8 - 1. 6 8 1 (\text {sanit.access}).
$$

Exponentiating both sides of the equation yields

$$
\widehat {\text {inf.mortality}} = e ^ {4. 0 1 8 - 1. 6 8 1 (\text {sanit.access})}.
$$

When sanit.access = 0, the equation simplifies to $e ^ { 4 . 0 1 8 } = 5 5 . 5 9 0$ deaths among 1,000 live births; this is the estimated infant mortality rate in the countries with low access to sanitation facilities. When sanit.access = 1, the estimated infant mortality rate is $e ^ { 4 . 0 1 8 - 1 . 6 8 1 { \mathrm { ( 1 ) } } } = e ^ { 2 . 3 3 7 } = 1 0 . 3 5 0$ deaths per 1,000 live births. The infant mortality rate drops by a factor of 0.186; i.e., the mortality rate in the high access countries is approximately 20% of that in the low access countries.<sup>18</sup>

## EXAMPLE 6.13

Check the assumptions of constant variability around the regression line and normality of the residuals in the model for the relationship between the transformed infant mortality variable and access to sanitation variable. Residual plots are shown in Figure 6.13.

While the normal probability plot does show that the residuals are approximately normally dis tributed, the residual plot reveals that variability is far from constant around the two predictors. Another method for assessing the relationship between the two groups is advisable; this is discussed further in Section 6.4.

![](images/page_304_chart_10.jpg)

<details>
<summary>scatter</summary>

| Series | Predicted log(Infant Mortality) (range) | Residuals (range) |
| --- | --- | --- |
| Cluster 1 | ~2.25 ~2.35 | -1.7~2.0 |
| Cluster 2 | ~4.0 ~4.1 | -0.8~0.7 |
</details>

(a)

![](images/page_304_chart_12.jpg)

<details>
<summary>histogram</summary>

| Bin (Residuals) | Frequency |
| --- | --- |
| -2.0~-1.8 | ~0.5 |
| -1.8~-1.6 | ~1.5 |
| -1.6~-1.4 | ~3.5 |
| -1.4~-1.2 | ~2.5 |
| -1.2~-1.0 | ~4.5 |
| -1.0~-0.8 | ~6.5 |
| -0.8~-0.6 | ~7.5 |
| -0.6~-0.4 | ~9.5 |
| -0.4~-0.2 | ~8.5 |
| -0.2~0.0 | ~6.5 |
| 0.0~0.2 | ~3.5 |
| 0.2~0.4 | ~2.5 |
| 0.4~0.6 | ~1.5 |
| 0.6~0.8 | ~0.5 |
| 0.8~1.0 | ~0.2 |
</details>

(b)

![](images/page_304_chart_14.jpg)

<details>
<summary>qq</summary>

| Theoretical Quantiles | Sample Quantiles |
| --- | --- |
| ~-2.5 | ~-1.6 |
| ~-2.4 | ~-1.5 |
| ~-2.3 | ~-1.4 |
| ~-2.2 | ~-1.3 |
| ~-2.1 | ~-1.2 |
| ~-2.0 | ~-1.1 |
| ~-1.9 | ~-1.0 |
| ~-1.8 | ~-0.9 |
| ~-1.7 | ~-0.8 |
| ~-1.6 | ~-0.7 |
| ~-1.5 | ~-0.6 |
| ~-1.4 | ~-0.5 |
| ~-1.3 | ~-0.4 |
| ~-1.2 | ~-0.3 |
| ~-1.1 | ~-0.2 |
| ~-1.0 | ~-0.1 |
| ~-0.9 | 0.0 |
| ~-0.8 | 0.1 |
| ~-0.7 | 0.2 |
| ~-0.6 | 0.3 |
| ~-0.5 | 0.4 |
| ~-0.4 | 0.5 |
| ~-0.3 | 0.6 |
| ~-0.2 | 0.7 |
| ~-0.1 | 0.8 |
| 0.0 | 0.9 |
| 0.1 | 1.0 |
| 0.2 | 1.1 |
| 0.3 | 1.2 |
| 0.4 | 1.3 |
| 0.5 | 1.4 |
| 0.6 | 1.5 |
| 0.7 | 1.6 |
| 0.8 | 1.7 |
| 0.9 | 1.8 |
| 1.0 | 1.9 |
| 1.1 | 2.0 |
</details>

Figure 6.13: (a) Residual plot of log(inf.mortality) and sanit.access. (b) Histogram and normal probability plot of the residuals.

## 6.3.4 Outliers in regression

Depending on their position, data points in a scatterplot have varying degrees of contribution to the estimated parameters of a regression line. Points that are at particularly low or high values of the predictor (x) variable are said to have **high leverage**, and have a large influence on the estimated intercept and slope of the regression line; observations with x values closer to the center of the distribution of x do not have a large effect on the slope.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">18<sub>When</sub> examining event rates in public health, associations are typically measured using rate ratios rather than rate differences.</span></small>

A data point in a scatterplot is considered an **outlier in regression** if its value for the response (y) variable does not follow the general linear trend in the data. Outliers that sit at extreme values of the predictor variable (i.e., have high leverage) have the potential to contribute disproportionately to the estimated parameters of a regression line. If an observation does have a strong effect on the estimates of the line, such that estimates change substantially when the point is omitted, the observation is **influential**. These terms are formally defined in advanced regression courses.

This section examines the relationship between infant mortality and number of doctors, using data for each state and the District of Columbia.<sup>19</sup> Infant mortality is measured as the number of infant deaths in the first year of life per 1,000 live births, and number of doctors is recorded as number of doctors per 100,000 members of the population. Figure 6.14 shows scatterplots with infant mortality on the y-axis and number of doctors on the x-axis.

One point in Figure 6.14(a), marked in red, is clearly distant from the main cluster of points. This point corresponds to the District of Columbia, where there were approximately 807.2 doctors per 100,000 members of the population, and the infant mortality rate was 11.3 per 1,000 live births. Since 807.2 is a high value for the predictor variable, this observation has high leverage. It is also an outlier; the other points exhibit a downward sloping trend as the number of doctors increases, but this point, with an unusually high y-value paired with a high x-value, does not follow the trend.

Figure 6.14(b) illustrates that the DC observation is influential. Not only does the observation simply change the numerical value of the slope parameter, it reverses the direction of the linear trend; the regression line fitted with the complete dataset has a positive slope, but the line re-fitted without the DC observation has a negative slope. The large number of doctors per population is due to the presence of several large medical centers in an area with a population that is much smaller than a typical state.

It seems natural to ask whether or not an influential point should be removed from a dataset, but that may not be the right question. Instead, it is usually more important to assess whether the influential point might be an error in the data, or whether it belongs in the dataset. In this case, the District of Columbia has certain characteristics that may make comparisons with other states inappropriate; this is one argument in favor of excluding the DC observation from the data.

Generally speaking, if an influential point arises from random sampling from a large population and is not a data error, it should be left in the dataset, since it probably represents a small subset of the population from which the data were sampled.

## GUIDED PRACTICE 6.14

Once the influential DC point is removed, assess whether it is appropriate to use linear regression on these data by checking the four assumptions behind least squares regression: linearity, constant variability, independent observations, and approximate normality of the residuals. Refer to the residual plots shown in Figure 6.15.<sup>20</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">19<sub>Data</sub> are from the Statistical Abstract of the United States, published by the US Census Bureau. Data are for 2010, and available as census.2010 in the oibiostat package.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">20<sub>The</sub> scatterplot in Figure 6.14(b) does not show any nonlinear trends. Similarly, Figure 6.15(a) does not indicate any nonlinear trends or noticeable difference in the variability of the residuals, although it does show that there are relatively few observations for low values of predicted infant mortality. From Figure 6.15(b), the residuals are approximately normally distributed. Infant mortality across the states reflects a complex mix of different levels of income, access to health care, and individual state initiatives in health care; these and other state-specific features probably act independently across the states, although there is some dependence from federal influence such as funding for pre-natal care. Overall, independence seems like a reasonable assumption.</span></small>

![](images/page_306_chart_2.jpg)

<details>
<summary>scatter</summary>

| Doctors (per 100,000 members of pop.) | Infant Mortality |
| --- | --- |
| ~180 | ~6.8 |
| ~190 | ~10.6 |
| ~200 | ~5.1 |
| ~200 | ~6.4 |
| ~210 | ~7.0 |
| ~210 | ~8.5 |
| ~220 | ~5.1 |
| ~220 | ~6.3 |
| ~220 | ~8.1 |
| ~230 | ~9.0 |
| ~230 | ~8.4 |
| ~240 | ~7.5 |
| ~240 | ~7.4 |
| ~240 | ~6.9 |
| ~250 | ~7.4 |
| ~250 | ~7.3 |
| ~260 | ~9.9 |
| ~260 | ~8.7 |
| ~260 | ~8.2 |
| ~260 | ~7.8 |
| ~260 | ~6.4 |
| ~270 | ~5.8 |
| ~270 | ~5.7 |
| ~270 | ~5.5 |
| ~270 | ~4.7 |
| ~280 | ~6.3 |
| ~280 | ~6.1 |
| ~280 | ~5.5 |
| ~290 | ~7.3 |
| ~300 | ~5.2 |
| ~310 | ~7.6 |
| ~320 | ~5.6 |
| ~380 | ~6.1 |
| ~380 | ~6.2 |
| ~390 | ~5.5 |
| ~400 | ~5.6 |
| ~420 | ~8.0 |
| ~470 | ~4.8 |
| ~810 | ~11.3 |
</details>

(a)

![](images/page_306_chart_4.jpg)

<details>
<summary>scatter</summary>

| Doctors (per 100,000 members of pop.) | Infant Mortality |
| --- | --- |
| ~185 | ~10.6 |
| ~185 | ~8.0 |
| ~190 | ~7.0 |
| ~190 | ~6.4 |
| ~190 | ~5.1 |
| ~205 | ~8.5 |
| ~210 | ~6.4 |
| ~215 | ~9.0 |
| ~215 | ~8.1 |
| ~215 | ~7.1 |
| ~215 | ~6.9 |
| ~220 | ~7.5 |
| ~220 | ~6.9 |
| ~220 | ~5.8 |
| ~230 | ~8.4 |
| ~245 | ~7.4 |
| ~245 | ~7.4 |
| ~245 | ~5.8 |
| ~250 | ~7.4 |
| ~255 | ~8.3 |
| ~260 | ~9.9 |
| ~260 | ~8.7 |
| ~260 | ~7.8 |
| ~265 | ~6.4 |
| ~265 | ~5.7 |
| ~265 | ~5.0 |
| ~265 | ~4.7 |
| ~270 | ~7.1 |
| ~270 | ~6.3 |
| ~270 | ~5.5 |
| ~280 | ~7.3 |
| ~295 | ~5.2 |
| ~305 | ~7.6 |
| ~315 | ~5.6 |
| ~315 | ~5.5 |
| ~375 | ~6.2 |
| ~375 | ~6.1 |
| ~375 | ~5.5 |
| ~395 | ~5.6 |
| ~420 | ~8.0 |
| ~465 | ~4.8 |
</details>

(b)

Figure 6.14: (a) Plot including District of Columbia data point. (b) Plot without influential District of Columbia data point.

![](images/page_306_chart_7.jpg)

<details>
<summary>scatter</summary>

| Predicted Infant Mortality | Residuals |
| --- | --- |
| ~5.4 | ~-0.6 |
| ~5.7 | ~2.3 |
| ~5.9 | ~-0.3 |
| ~6.0 | ~0.1 |
| ~6.0 | ~-0.5 |
| ~6.4 | ~-0.9 |
| ~6.4 | ~-0.8 |
| ~6.5 | ~1.1 |
| ~6.6 | ~-1.4 |
| ~6.7 | ~0.6 |
| ~6.7 | ~-0.4 |
| ~6.7 | ~-0.6 |
| ~6.7 | ~-1.2 |
| ~6.8 | ~-2.0 |
| ~6.8 | ~-1.9 |
| ~6.8 | ~1.0 |
| ~6.8 | ~1.9 |
| ~6.8 | ~3.1 |
| ~6.9 | ~1.2 |
| ~6.9 | ~1.4 |
| ~6.9 | ~0.5 |
| ~6.9 | ~0.4 |
| ~6.9 | ~-1.1 |
| ~6.9 | ~-1.3 |
| ~7.0 | ~0.5 |
| ~7.0 | ~0.4 |
| ~7.0 | ~-0.2 |
| ~7.0 | ~-1.3 |
| ~7.1 | ~1.4 |
| ~7.1 | ~0.9 |
| ~7.1 | ~0.0 |
| ~7.1 | ~-0.8 |
| ~7.1 | ~-1.3 |
| ~7.1 | ~-2.1 |
| ~7.2 | ~1.9 |
| ~7.2 | ~1.3 |
| ~7.3 | ~-0.9 |
| ~7.3 | ~-2.2 |
| ~7.4 | ~3.2 |
| ~7.4 | ~0.6 |
| ~7.4 | ~-0.6 |
</details>

(a)

![](images/page_306_chart_9.jpg)

<details>
<summary>histogram</summary>

| Bin (Residuals) | Frequency |
| --- | --- |
| -3.5~-2.5 | ~1 |
| -2.5~-1.5 | ~2 |
| -1.5~-0.5 | ~4 |
| -0.5~0.5 | ~6 |
| 0.5~1.5 | ~4 |
| 1.5~2.5 | ~2 |
| 2.5~3.5 | ~0.5 |
| 3.5~4.5 | ~1 |
</details>

(b)

![](images/page_306_chart_11.jpg)

<details>
<summary>qq</summary>

| Theoretical Quantiles | Sample Quantiles |
| --- | --- |
| ~-2.3 | ~-2.2 |
| ~-1.9 | ~-1.9 |
| ~-1.6 | ~-1.4 |
| ~-1.5 | ~-1.3 |
| ~-1.4 | ~-1.2 |
| ~-1.3 | ~-1.1 |
| ~-1.2 | ~-1.0 |
| ~-1.1 | ~-0.9 |
| ~-0.8 | ~-0.7 |
| ~-0.7 | ~-0.6 |
| ~-0.6 | ~-0.5 |
| ~-0.5 | ~-0.4 |
| ~-0.4 | ~-0.3 |
| ~-0.3 | ~-0.2 |
| ~-0.2 | ~-0.1 |
| ~-0.1 | 0.0 |
| 0.0 | 0.1 |
| 0.1 | 0.2 |
| 0.2 | 0.3 |
| 0.3 | 0.4 |
| 0.4 | 0.5 |
| 0.5 | 0.6 |
| 0.6 | 0.7 |
| 0.7 | 0.8 |
| 0.8 | 0.9 |
| 0.9 | 1.0 |
| 1.0 | 1.1 |
| 1.1 | 1.2 |
| 1.2 | 1.3 |
| 1.3 | 1.4 |
| 1.4 | 1.5 |
| 1.5 | 1.6 |
| 1.6 | 1.7 |
| 1.7 | 1.8 |
| 1.8 | 1.9 |
| 1.9 | 2.0 |
| 2.0 | 2.2 |
| 2.1 | 3.1 |
| 2.2 | 3.2 |
</details>

Figure 6.15: (a) Residual plot of inf.mortality and doctors. (b) Histogram and normal probability plot of the residuals.

## 6.4 Statistical inference with regression

The previous sections in this chapter have focused on linear regression as a tool for summarizing trends in data and making predictions. These numerical summaries are analogous to the methods discussed in Chapter 1 for displaying and summarizing data. Regression is also used to make inferences about a population.

The same ideas covered in Chapters 4 and 5 about using data from a sample to draw inferences about population parameters apply with regression. Previously, the goal was to draw inference about the population parameter $\mu ;$ in regression, the population parameter of interest is typically the slope parameter $\beta _ { 1 }$ . Inference about the intercept term is rare, and limited to the few problems where the vertical intercept has scientific meaning.

Inference in regression relies on the population linear model for the relationship between an explanatory variable X and a response variable Y given by

$$
Y = \beta_ {0} + \beta_ {1} X + \varepsilon , \tag {6.15}
$$

where ε is assumed to have a normal distribution with mean 0 and standard deviation $\sigma   \left( \varepsilon   \sim \right.$ $N ( 0 , \sigma ) )$ . This population model specifies that a response Y has value $\beta _ { 0 } + \beta _ { 1 } X$ plus a random term that pushes Y symmetrically above or below the value specified by the line.<sup>22</sup>

The set of ordered pairs $( x _ { i } , y _ { i } )$ used when fitting a least squares regression line are assumed to have been sampled from a population in which the relationship between the explanatory and response variables follows Equation 6.15. Under this assumption, the slope and intercept values of the least squares regression line, $b _ { 0 }$ and $b _ { 1 } ,$ , are estimates of the population parameters $\beta _ { 0 }$ and $\beta _ { 1 } ; b _ { 0 }$ and $b _ { 1 }$ have sampling distributions, just as $\overline { { X } }$ does when thought of as an estimate of a population mean $\mu .$ A more advanced treatment of regression would demonstrate that the sampling distribution of $b _ { 1 }$ is normal with mean $E ( b _ { 1 } ) = \beta _ { 1 }$ and standard deviation

$$
\sigma_ {b _ {1}} = \frac {\sigma}{\sqrt {\sum (x _ {i} - \overline {{x}}) ^ {2}}}.
$$

The sampling distribution of $b _ { 0 }$ has mean $E ( b _ { 0 } ) = \beta _ { 0 }$ and standard deviation

$$
\sigma_ {b _ {0}} = \sigma \sqrt {\frac {1}{n} + \frac {\overline {{x}} ^ {2}}{\sum (x _ {i} - \overline {{x}}) ^ {2}}}.
$$

In both of these expressions, $\sigma$ is the standard deviation of $\varepsilon .$

Hypothesis tests and confidence intervals for regression parameters have the same basic form as tests and intervals about population means. The test statistic for a null hypothesis $H _ { 0 } : \beta _ { 1 } = \beta _ { 1 } ^ { 0 }$ about a slope parameter is

$$
t = \frac {b _ {1} - \beta_ {1} ^ {0}}{\mathrm{s.e.} (b _ {1})},
$$

where the formula for $\mathsf { s . e . } ( b _ { 1 } )$ is given below. In this setting, t has a t-distribution with $n   -   2$ degrees of freedom, where n is the number of ordered pairs used to estimate the least squares line.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">21<sub>In</sub> some applications of regression, the predictor x is replaced by x<sup>∗</sup> = x − x. In that case, the vertical intercept is the value of the line when x<sup>∗</sup> = 0, or x = x.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">22<sub>Since</sub> E(ε) = 0, this model can also be written as Y ∼ N(µ<sub>x</sub>), with µ<sub>x</sub> = E(Y ) = β<sub>0</sub> + β<sub>1</sub>X. The term ε is the population model for the observed residuals e<sub>i</sub> in regression.</span></small>

Typically, hypothesis testing in regression involves tests of whether the x and y variables are associated; in other words, whether the slope is significantly different from 0. In these settings, the null hypothesis is that there is no association between the explanatory and response variables, or $H _ { 0 } : \beta _ { 1 } = 0 = \beta _ { 1 } ^ { 0 }$ , in which case

$$
t = \frac {b _ {1}}{\text {s.e.} (b _ {1})}.
$$

The hypothesis is rejected in favor of the two-sided alternative $H _ { A } : \beta _ { 1 } \neq 0$ with significance level α when $| t | \geq t _ { \mathrm { d f } } ^ { \star } ,$ , where $t _ { \mathrm { d f } } ^ { \star }$ is the point on a t-distribution with $n - 2$ degrees of freedom that has $\alpha / 2$ area to its right $( \mathbf { i } . \mathbf { e } . )$ , when $p \leq \alpha )$

A two-sided confidence interval for $\beta _ { 1 }$ is given by

$$
b _ {1} \pm \text {s.e.} (b _ {1}) \times t _ {\mathrm{df}} ^ {\star}.
$$

Tests for one-sided alternatives and one-sided confidence intervals make the usual adjustments to the rejection rule and confidence interval, and $p _ { 1 }$ -values are interpreted just as in Chapters 4 and 5.

## Formulas for calculating standard errors

Statistical software is typically used to obtain t-statistics and p-values for inference with regression, since using the formulas for calculating standard error can be cumbersome.

The standard errors of $b _ { 0 }$ and $b _ { 1 }$ used in confidence intervals and hypothesis tests replace σ with $S ,$ the standard deviation of the residuals from a fitted line. Formally,

$$
s = \sqrt {\frac {\sum e _ {i} ^ {2}}{n - 2}} = \sqrt {\frac {\sum (y _ {i} - \hat {y} _ {i}) ^ {2}}{n - 2}}. \tag {6.16}
$$

The term $s ^ { 2 }$ is often called the mean squared error from the regression, and s the root mean squared error.

The two standard errors are

$$
\text {s.e.} (b _ {1}) = \frac {s}{\sqrt {\sum (x _ {i} - \bar {x}) ^ {2}}} \quad \text {and} \quad \text {s.e.} (b _ {0}) = s \sqrt {\frac {1}{n} + \frac {\bar {x} ^ {2}}{\sum (x _ {i} - \bar {x}) ^ {2}}}.
$$

## EXAMPLE 6.17

Is there evidence of a significant association between number of doctors per 100,000 members of the population in a state and infant mortality rate?

The numerical output that R returns is shown in Figure 6.16.<sup>23</sup>

The question implies that the District of Columbia should not be included in the analysis. The assumptions for applying a least squares regression have been verified in Exercise 6.14. Whenever possible, formal inference should be preceded by a check of the assumptions for regression.

The null and alternative hypotheses are $H _ { 0 } : \beta _ { 1 } = 0$ and $H _ { A } : \beta _ { 1 } \neq 0 .$

The estimated slope of the least squares line is -0.0068, with standard error 0.0028. The t-statistic equals -2.40, and the probability that the absolute value of a t-statistic with $50 - 2 = 48$ degrees of freedom is smaller than −2.40 or larger than 2.40 is 0.021.

Since $p = 0 . 0 2 1 < 0 . 0 5 ,$ the data support the alternative hypothesis that the number of physicians is associated with infant mortality at the 0.05 significance level. The sign of the slope implies that the association is negative; states with more doctors tend to have lower rates of infant mortality.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 8.5991 | 0.7603 | 11.31 | 0.0000 |
| Doctors Per 100,000 | -0.0068 | 0.0028 | -2.40 | 0.0206 |

Figure 6.16: Summary of regression output from R for the model predicting infant mortality from number of doctors, using the census.2010 dataset.

Care should be taken in interpreting the above results. The $R ^ { 2 }$ for the model is 0.107; the model explains only about 10% of the state-to-state variability in infant mortality, which suggests there are several other factors affecting infant mortality that are not accounted for in the model.<sup>24</sup> Additionally, an important implicit assumption being made in this example is that data from the year 2010 are representative; in other words, that the relationship between number of physicians and infant mortality is constant over time, and that the data from 2010 can be used to make inference about other years.

Note that it would be incorrect to make claims of causality from these data, such as stating that an additional 100 physicians (per 100,000 residents) would lead to a decrease of 0.68 in the infant mortality rate.

## GUIDED PRACTICE 6.18

Calculate a 95% two-sided confidence interval for the slope parameter $\beta _ { 1 }$ in the state-level infant mortality data.<sup>25</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">23<sub>Other</sub> software packages, such as Stata or Minitab, provide similar information but with slightly different labeling.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">24<sub>Calculations</sub> of the R<sup>2</sup> value are not shown here.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">25<sub>The</sub> t? value for a t-distribution with 48 degrees of freedom is 2.01, and the standard error of b<sub>1</sub> is 0.0028. The 95% confidence interval is −0.0068 ± 2.01(0.0028) = (-0.0124, -0.0012).</span></small>

## Connection to two-group hypothesis testing

Conducting a regression analysis with a numerical response variable and a categorical predictor with two levels is analogous to conducting a two-group hypothesis test.

For example, Section 6.3.3 shows a regression model that compares the average infant mortality rate in countries with low access to sanitation facilities versus high access.<sup>26</sup> In other words, the purpose of the analysis is to compare mean infant mortality rate between the two groups: countries with low access versus countries with high access. Recall that the slope parameter $b _ { 1 }$ is the difference between the means of log(mortality rate). A test of the null hypothesis $H _ { 0 } : \beta _ { 1 } = 0$ in the context of a categorical predictor with two levels is a test of whether the two means are different, just as for the two-group null hypothesis, $H _ { 0 } : \mu _ { 1 } = \mu _ { 2 }$

When the pooled standard deviation assumption (Section 5.3.5) is used, the t-statistic and p-value from a two-group hypothesis test are equivalent to that returned from a regression model.

Figure 6.17 shows the R output from a regression model in the wdi.2011 data, in which sanit.access = 1 for countries where at least 50% of the population has access to adequate sanitation and 0 otherwise. The abbreviated R output from two-group t-tests are shown in Figure 6.18. The version of the t-test that does not assume equal standard deviations and uses non-integer degrees of freedom is often referred to as the Welch test.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 4.0184 | 0.1100 | 36.52 | &lt; 0.001 |
| High Access | -1.6806 | 0.1322 | -12.72 | 0.001 |

Figure 6.17: Regression of log(infant mortality) versus sanitation access.

| Test | df | t value | Pr(>\|t\|) |
| --- | --- | --- | --- |
| Two-group t-test | 161 | 12.72 | &lt;0.001 |
| Welch two-group t-test | 155.82 | 17.36 | &lt;0.001 |

Figure 6.18: Results from the independent two-group t-test, under differing assumptions about standard deviations between groups, for mean log(infant mortality) between sanitation access groups.

The sign of the t-statistic differs because for the two-group test, the difference in mean log(infant mortality) was calculated by subtracting the mean in the high access group from the mean in the low access group; in the regression model, the negative sign reflects the reduction in mean log(infant mortality) when changing from low access to high access. Since the t-distribution is symmetric, the two-sided p-value is equal. In this case, p is a small number less than 0.001, as calculated from a t-distribution with 163 − 2 = 161 degrees of freedom (recall that 163 countries are represented in the dataset). The degrees of freedom for the pooled two-group test and linear regression are equivalent.

Example 6.13 showed that the constant variability assumption does not hold for these data. As a result, it might be advisable for a researcher interested in comparing the infant mortality rates between these two groups to conduct a two-group hypothesis test without using the pooled standard deviation assumption. Since this test uses a different formula for calculating the standard error of the difference in means, the t-statistic is different; additionally, the degrees of freedom are not equivalent. In this particular example, there is not a noticeable effect on the p-value.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">26<sub>Recall</sub> that a log transformation was used on the infant mortality rate.</span></small>

## 6.5 Interval estimates with regression

Section 6.4 introduced interval estimates for regression parameters, such as the population slope $\beta _ { 1 }$ . An estimated regression line can also be used to construct interval estimates for the regression line itself and to calculate prediction intervals for a new observation.

## 6.5.1 Confidence intervals

As initially discussed in Section 6.2, the estimated regression line for the association between RFFT score and age from the 500 individuals in prevend.samp is

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 5 5 - 1. 2 6 (\text {age}).
$$

Figure 6.19 shows the summary output from R when the regression model is fit. R also provides the value of $R ^ { 2 }$ as 0.285 and the value of s, the estimated standard deviation of the residuals, as 23.2.

<table><tr><td></td><td>Estimate</td><td>Std. Error</td><td>t value</td><td>Pr(&gt;|t|)</td></tr><tr><td>(Intercept)</td><td>137.55</td><td>5.02</td><td>27.42</td><td>0.000</td></tr><tr><td>Age</td><td>-1.26</td><td>0.09</td><td>-14.09</td><td>0.000</td></tr><tr><td colspan="5"> $df = 498$ </td></tr></table>

Figure 6.19: Summary of regression output from R for the model predicting RFFT score from age, using the prevend.samp dataset.

A confidence interval for the slope parameter $\beta _ { 1 }$ is centered at the point estimate $b _ { 1 } ,$ , with a width based on the standard error for the slope. For this model, the 95% confidence interval for age is $-1.26 \pm (1.96)(0.09) = (-1.44, -1.09)$ years.<sup>27</sup> With 95% confidence, each additional year of age is associated with between a 1.1 and 1.4 point lower RFFT score.

A confidence interval can also be calculated for a specific point on a least squares line. Consider a specific value of the predictor variable, $x ^ { * } ,$ , such as 60 years of age. At age 60 years, the predicted value of RFFT score is $1 3 7 . 5 5 - 1 . 2 6 { \bigl ( } 6 0 { \bigr ) } = 6 1 . 9 5$ points. The fitted line suggests that individuals from this population who are 60 years of age score, on average, about 62 points on the RFFT. Each point on the estimated regression line represents the predicted average RFFT score for a certain age.

More generally, the population model for a regression line is $E ( Y | x ) = \beta _ { 0 } + \beta _ { 1 } x ,$ and at a value $x ^ { * }$ of the predictor $x ,$ the fitted regression line

$$
\widehat {E (Y | x ^ {*})} = b _ {0} + b _ {1} x ^ {*}
$$

estimates the mean of Y for members of the population with predictor value $x ^ { * }$ .

Thus, each point on a fitted regression line represents a point estimate for $E ( Y | x ^ { * } )$ . The corresponding interval estimate for $E ( Y | x ^ { * } )$ measures the uncertainty in the estimated mean of $Y$ at predictor value $x ^ { * } ,$ , just as how an interval estimate for the population slope $\beta _ { 1 }$ represents the uncertainty around $b _ { 1 }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">27<sub>The</sub> critical value 1.96 is used here because at degrees of freedom 498, the t-distribution is very close to a normal distribution. From software, t?0.975,df =498 = 1.9647.</span></small>

The confidence interval for $E ( Y | x ^ { * } )$ is computed using the standard error of the estimated mean of the regression model at a value of the predictor:

$$
\mathrm{s.e.} (\widehat {E (Y | x ^ {*})}) = \sqrt {s ^ {2} \left(\frac {1}{n} + \frac {(x ^ {*} - \overline {{x}}) ^ {2}}{\sum (x _ {i} - \overline {{x}}) ^ {2}}\right)} = s \sqrt {\frac {1}{n} + \frac {(x ^ {*} - \overline {{x}}) ^ {2}}{\sum (x _ {i} - \overline {{x}}) ^ {2}}}.
$$

In this expression, s is given by Equation 6.16, the usual estimate of $\sigma ,$ the standard deviation of the error term  in the population linear model $Y = \beta _ { 0 } + \beta _ { 1 } X + \epsilon .$

The standard error of an estimated mean in regression is rarely calculated by hand; with all but the smallest datasets, the calculations are long and best left to software. When necessary, it can be calculated from basic features of the data and summary statistics.

Consider computing a 95% confidence interval for $E ( R F F T | a g e = 6 0 )$

– The sample size is $n = 5 0 0$
$- s = 2 3 . 2$ appears in the regression output.
– The sample mean $\overline { { x } }$ of the predictor is $\overline { { a g e } } = 5 4 . 8 \; \mathrm { y e a r s }$
$( x ^ { * } - { \overline { { x } } } ) ^ { 2 }$ is the squared distance between the predictor value of interest and the sample mean of the predictors: $(60 - 54.8)^{2} = 27.04$
– The sum $\textstyle \sum ( x _ { i } - { \overline { { x } } } ) ^ { 2 }$ is the numerator in the calculation of the variance of the predictor, and equals $(n - 1) Var (x) = (499)(134.4445) = 67,088$

Using these values, the standard error of the estimated mean RFFT score at age 60 is

$$
\text {s.e.} (E (\widehat {R F F T | a g e} = 6 0)) = 2 3. 2 \sqrt {\frac {1}{5 0 0} + \frac {2 7 . 0 4}{6 7 , 0 8 8}} = 1. 1 4.
$$

Thus, a 95% confidence interval for the estimated mean is $6 1 . 9 5 \pm ( 1 . 9 6 ) ( 1 . 1 4 )   =   ( 5 9 . 7 2 , 6 4 . 1 8 )$ points. With 95% confidence, the interval (59.72, 64.18) points contains the average RFFT score of a 60-year-old individual.

It is also possible to calculate approximate confidence intervals for the estimated mean at a specific value of a predictor. When $x ^ { * } = { \overline { { x } } } ,$ the second term in the square root will be $0 ,$ and the standard error of the estimated mean at the average value $\overline { { x } }$ will have the simple form $s / { \sqrt { n } } .$ For values close to ${ \overline { { x } } } ,$ approximating the standard error as $s / { \sqrt { n } }$ is often sufficient. In the PREVEND data, 60 years is reasonably close to the average age 54.8 years, and the approximate value of the standard error is $2 3 . 2 / \sqrt { 5 0 0 } = 1 . 0 3$ . For values $x ^ { * }$ that are more distant from the mean, the second term in the square root cannot be reasonably ignored.

The approximate form of the standard error for the mean at a predictor value, $s / { \sqrt { n } } ,$ makes it easier to see that for large $n ,$ the standard error approaches $0 ;$ thus, the confidence interval narrows as sample size increases, allowing the estimates to become more precise. This behavior is identical to the confidence interval for a simple mean, as one would expect. It is possible to show algebraically that the confidence intervals at any value of the predictor become increasingly narrow as the sample size increases.

## 6.5.2 Prediction intervals

After fitting a regression line, a **prediction interval** is used to estimate a range of values for a new observation of the response variable Y with predictor value $x ^ { * } ;$ that is, an observation not in the data used to estimate the line. The point estimate ${ \widehat { Y | x ^ { * } } } = b _ { 0 } + b _ { 1 } x ^ { * }$ is the same as $\widehat { \overline { { E ( Y | x ^ { * } ) } } }$ , but the corresponding interval estimate is wider than a confidence interval for the mean.

The width of the interval reflects both the uncertainty in the estimate of the mean, $\widehat { \overline { { E ( Y | x ^ { * } ) } } }$ and the inherent variability of the response variable. The standard error for a predicted value $\widehat { Y | x ^ { * } }$ at predictor $x ^ { * }$ is

$$
\text {s.e.} (\widehat {Y | x ^ {*}}) = \sqrt {s ^ {2} + s ^ {2} \left(\frac {1}{n} + \frac {(x ^ {*} - \overline {{x}}) ^ {2}}{\sum (x _ {i} - \overline {{x}}) ^ {2}}\right)} = s \sqrt {1 + \frac {1}{n} + \frac {(x ^ {*} - \overline {{x}}) ^ {2}}{\sum (x _ {i} - \overline {{x}}) ^ {2}}}.
$$

The increased variability when estimating $Y | x ^ { * }$ versus $E ( Y | x ^ { * } )$ is accounted for by the additional $s ^ { 2 }$ term inside the square root.

The standard error for a prediction can also be calculated from summary statistics; the calculation is similar to that for the standard error for a mean. From the values of the summary statistics,

$$
\text {s.e.} (\widehat {R F F T | a g e} = 6 0) = 2 3. 2 \sqrt {1 + \frac {1}{5 0 0} + \frac {2 7 . 0 4}{6 7 , 0 8 8}} = 2 3. 2 3.
$$

The 95% prediction interval is $6 1 . 9 5 \pm ( 1 . 9 6 ) ( 2 3 . 2 3 ) = ( 1 6 . 4 2 , 1 0 7 . 6 8 )$ points. These data and the model suggest that with 95% confidence, a newly selected 60-year-old will score between 16 and 108 points on the RFFT. This interval is wider than the confidence interval for the mean RFFT score (at age 60 years).

Just as with confidence intervals, an approximate prediction interval for a predictor near the average of the predictors can be constructed by considering the case when $x ^ { * } = { \overline { { x } } }$ and the standard error reduces to $s { \sqrt { 1 + 1 / n } }$ . This approximate standard error shows why prediction intervals are wider than confidence intervals and do not become narrower as sample size increases. For large sample sizes, the term $1 / n$ is close to $0 ,$ and the standard error is close to $s ,$ the standard deviation of the residuals about the line. Even when the mean is estimated perfectly, a prediction interval will reflect the variability in the data (specifically, the variability in the response variable).

![](images/page_313_chart_11.jpg)

<details>
<summary>scatter</summary>

| Age (yrs) | RFFT Score |
| --- | --- |
| ~35 | ~135 |
| ~36 | ~105 |
| ~37 | ~108 |
| ~38 | ~95 |
| ~39 | ~102 |
| ~40 | ~115 |
| ~41 | ~105 |
| ~42 | ~118 |
| ~43 | ~108 |
| ~44 | ~115 |
| ~45 | ~105 |
| ~46 | ~118 |
| ~47 | ~105 |
| ~48 | ~115 |
| ~49 | ~105 |
| ~50 | ~115 |
| ~51 | ~105 |
| ~52 | ~115 |
| ~53 | ~105 |
| ~54 | ~115 |
| ~55 | ~105 |
| ~56 | ~115 |
| ~57 | ~105 |
| ~58 | ~115 |
| ~59 | ~105 |
| ~60 | ~115 |
| ~61 | ~105 |
| ~62 | ~115 |
| ~63 | ~105 |
| ~64 | ~115 |
| ~65 | ~105 |
| ~66 | ~115 |
| ~67 | ~105 |
| ~68 | ~115 |
| ~69 | ~105 |
| ~70 | ~115 |
| ~71 | ~105 |
| ~72 | ~115 |
| ~73 | ~105 |
| ~74 | ~115 |
| ~75 | ~105 |
| ~76 | ~115 |
| ~77 | ~105 |
| ~78 | ~115 |
| ~79 | ~105 |
| ~80 | ~115 |
</details>

Figure 6.20: A scatterplot showing RFFT versus age, with the regression line in blue. The confidence intervals are marked by solid red lines, while the prediction intervals are shown in dashed red lines.

Figure 6.20 visually demonstrates confidence intervals and prediction intervals in the PRE-VEND example; the regression line is shown in blue, while the 95% confidence intervals and pre-diction intervals for each value of age are shown in red. At any value of age, the width of the interval estimate at that value is represented by the vertical distance between the two red lines. For example, the width of the confidence interval at age 60 years is represented by the distance be tween the points (60, 59.72) and (60, 64.18); the solid red lines pass through the upper and lower confidence bounds calculated in the earlier example. Similarly, the dashed red lines that represent prediction intervals pass through (60, 16.42) and (60, 107.68), the 95% upper and lower bounds for the predicted RFFT score of a 60-year-old.

The plot shows how the confidence intervals are most narrow at the mean age, 54.8 years, and become wider at values of age further from the mean. The prediction intervals are always wider than the confidence intervals. While the mean can be estimated with relative precision along the regression line, prediction intervals reflect the scatter of RFFT scores about the line (which is directly related to the inherent variability of RFFT scores within the study participants). While larger sample sizes can lead to narrower confidence intervals, the width of the prediction intervals will remain essentially unchanged unless the sampling scheme is changed in a way that reduces the variability of the response. A sample of individuals restricted to ages 60 - 70 years, for example, would be expected to have less variable RFFT scores, which would allow for narrower prediction intervals.

The distinction between confidence and prediction intervals is important and often overlooked. A clinical practitioner interested in the expected outcomes of a test generally should rely on confidence intervals for the mean along a regression line. The PREVEND data suggest that 60 year olds will score on average about 62 points on the test, and the average score is between 59.7 points and 62.2 points. When the RFFT is administered to a new 60 year old, however, the likely range of responses will be between 16.4 and 107.7. The prediction interval is wide because the scores on the test are quite variable.

## 6.6 Notes

This chapter provides only an introduction to simple linear regression; the next chapter, Chapter $^ { 7 , }$ expands on the principles of simple regression to models with more than one predictor variable.

When fitting a simple regression, be sure to visually assess whether the model is appropriate. Nonlinear trends or outliers are often obvious in a scatterplot with the least squares line plotted. If outliers are evident, the data source should be consulted when possible, since outliers may be indicative of errors in data collection. It is also important to consider whether observed outliers belong to the target population of inference, and assess whether the outliers should be included in the analysis.

There are several variants of residual plots used for model diagnostics. The ones shown in Section 6.3.1, which plot the predicted values on the horizontal axis, easily generalize to settings with multiple predictors, since there is always a single predicted value even when there is more than one predictor. If the only model used is a simple regression, plotting residuals against predictor values may make it easier to identify a case with a notable residual. Additionally, data analysts will sometimes plot residuals against case number of the predictor, since runs of large or small residuals may indicate that adjacent cases are correlated.

The $R ^ { 2 }$ statistic is widely used in the social sciences, where the unexplained variability in the data is typically much larger than the variability captured or explained by a model. It is important to be aware of what information $R ^ { 2 }$ does and does not provide. Even though a model may have a low proportion of explained variability, regression coefficients in the model can still be highly statistically significant. The $R ^ { 2 }$ should not be interpreted as a measure of the quality of the fit of the model. It is possible for $R ^ { 2 }$ to be large even when the data do not show a linear relationship.

Linear regression models are often estimated after an investigator has noticed a linear relationship in data, and experienced investigators can often guess correctly that regression coefficients will be significant before calculating a p-value. Unlike with two-sample hypothesis tests, regression models are rarely specified in advance at the design stage. In practice, it is best to be skeptical about a small p-value in a regression setting, and wait to see whether the observed statistically significant relationship can be confirmed in an independent dataset. The issue of model validation and assessing whether results of a regression analysis will generalize to other datasets is often discussed at length in advanced courses.

In more advanced texts, substantial attention is devoted to the subtleties of fitting straight line models. For instance, there are strategies for adjusting an analysis when one or more of the assumptions for regression do not hold. There are also specific methods to numerically assess the leverage or influence that each observation has on a fitted model.

Lab 1 explores the relationship between cognitive function and age in adults by fitting and interpreting a straight line to these variables in the PREVEND dataset, in addition to discussing the statistical model for least squares regression and residual plots used to assess the assumptions for linear regression. The lab is a useful reminder that least squares regression is much more than the mechanics of finding a line that best fits a dataset. Lab 2 uses simulated data to explore the quantity $R ^ { 2 } ,$ . Lab 3 explores the use of binary categorical predictor variables in regression and shows how two-sample t-tests can be calculated using linear regression, in addition to introducing inference in a regression context. Categorical predictor variables are common in medicine and the life sciences.

## 6.7 Exercises

## 6.7.1 Examining scatterplots

**6.1 Identify relationships, Part I.** For each of the six plots, identify the strength of the relationship (e.g. weak, moderate, or strong) in the data and whether fitting a linear model would be reasonable.

![](images/page_316_chart_5.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(a)

![](images/page_316_chart_7.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(b)

![](images/page_316_chart_9.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(c)

![](images/page_316_chart_11.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(d)

![](images/page_316_chart_13.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(e)

![](images/page_316_chart_15.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(f)

**6.2 Identify relationships, Part II.** For each of the six plots, identify the strength of the relationship (e.g. weak, moderate, or strong) in the data and whether fitting a linear model would be reasonable.

![](images/page_316_chart_18.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(a)

![](images/page_316_chart_20.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(b)

![](images/page_316_chart_22.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(c)

![](images/page_316_chart_24.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(d)

![](images/page_316_chart_26.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(e)

![](images/page_316_chart_28.jpg)

<details>
<summary>scatter</summary>

| X (range) | Y (range) |
| --- | --- |
| 0~100 | 0~100 |
</details>

(f)

## 6.7.2 Estimating a regression line using least squares

**6.3 Body measurements, Part I.** Researchers studying anthropometry collected body girth measurements and skeletal diameter measurements, as well as age, weight, height and gender for 507 physically active individuals.<sup>28</sup> The scatterplot below shows the relationship between height and shoulder girth (over deltoid muscles), both measured in centimeters.

(a) Describe the relationship between shoulder girth and height.
(b) How would the relationship change if shoulder girth was measured in inches while the units of height remained in centimeters?

![](images/page_317_chart_7.jpg)

<details>
<summary>scatter</summary>

| Shoulder girth (cm) (range) | Height (cm) (range) |
| --- | --- |
| 85~135 | 147~199 |
</details>

**6.4 Body measurements, Part II.** The scatterplot below shows the relationship between weight measured in kilograms and hip girth measured in centimeters from the data described in Exercise 6.3.

(a) Describe the relationship between hip girth and weight.
(b) How would the relationship change if weight was measured in pounds while the units for hip girth remained in centimeters?

![](images/page_317_chart_12.jpg)

<details>
<summary>scatter</summary>

| Hip girth (cm) (range) | Weight (kg) (range) |
| --- | --- |
| 78~129 | 43~115 |
</details>

**6.5 Over-under, Part I.** Suppose we fit a regression line to predict the shelf life of an apple based on its weight. For a particular apple, we predict the shelf life to be 4.6 days. The apple’s residual is -0.6 days. Did we over or under estimate the shelf-life of the apple? Explain your reasoning.
**6.6 Over-under, Part II.** Suppose we fit a regression line to predict the number of incidents of skin cancer per 1,000 people from the number of sunny days in a year. For a particular year, we predict the incidence of skin cancer to be 1.5 per 1,000 people, and the residual for this year is 0.5. Did we over or under estimate the incidence of skin cancer? Explain your reasoning.
**6.7 Murders and poverty, Part I.** The following regression output is for predicting annual murders per million from percentage living in poverty in a random sample of 20 metropolitan areas.

<table><tr><td></td><td>Estimate</td><td>Std. Error</td><td>t value</td><td>Pr(&gt;|t|)</td></tr><tr><td>(Intercept)</td><td>-29.901</td><td>7.789</td><td>-3.839</td><td>0.001</td></tr><tr><td>poverty%</td><td>2.559</td><td>0.390</td><td>6.562</td><td>0.000</td></tr><tr><td>s = 5.512</td><td colspan="2"> $R^2$ = 70.52%</td><td colspan="2"> $R^{2}_{adj}$ = 68.89%</td></tr></table>

(a) Write out the linear model.
(b) Interpret the intercept.
(c) Interpret the slope.
(d) Calculate the correlation coefficient.

![](images/page_318_chart_12.jpg)

<details>
<summary>scatter</summary>

| Percent in Poverty | Annual Murders per Million |
| --- | --- |
| ~14.2% | ~9.8 |
| ~16.5% | ~5.5 |
| ~16.5% | ~11.2 |
| ~16.5% | ~12.8 |
| ~17.0% | ~8.8 |
| ~17.0% | ~25.8 |
| ~17.8% | ~14.8 |
| ~18.2% | ~14.5 |
| ~18.5% | ~18.2 |
| ~19.0% | ~15.8 |
| ~19.2% | ~24.8 |
| ~20.2% | ~21.0 |
| ~20.2% | ~21.8 |
| ~20.5% | ~13.5 |
| ~21.5% | ~35.8 |
| ~22.5% | ~26.0 |
| ~23.0% | ~27.0 |
| ~24.5% | ~36.2 |
| ~24.8% | ~29.0 |
| ~26.5% | ~40.8 |
</details>

**6.8 Cats, Part I.** The following regression output is for predicting the heart weight (in g) of cats from their body weight (in kg). The coefficients are estimated using a dataset of 144 domestic cats.

<table><tr><td></td><td>Estimate</td><td>Std. Error</td><td>t value</td><td>Pr(&gt;|t|)</td></tr><tr><td>(Intercept)</td><td>-0.357</td><td>0.692</td><td>-0.515</td><td>0.607</td></tr><tr><td>body wt</td><td>4.034</td><td>0.250</td><td>16.119</td><td>0.000</td></tr><tr><td>s = 1.452</td><td colspan="2"> $R^2$ = 64.66%</td><td colspan="2"> $R^{2}_{adj}$ = 64.41%</td></tr></table>

(a) Write out the linear model.
(b) Interpret the intercept.
(c) Interpret the slope.
(d) Calculate the correlation coefficient.

![](images/page_318_chart_20.jpg)

<details>
<summary>scatter</summary>

| Body weight (kg) | Heart weight (g) |
| --- | --- |
| ~2.0 | ~6.5 |
| ~2.0 | ~7.3 |
| ~2.0 | ~9.5 |
| ~2.1 | ~7.2 |
| ~2.1 | ~8.5 |
| ~2.1 | ~8.8 |
| ~2.1 | ~10.0 |
| ~2.2 | ~7.2 |
| ~2.2 | ~8.5 |
| ~2.2 | ~9.5 |
| ~2.2 | ~11.0 |
| ~2.3 | ~7.2 |
| ~2.3 | ~8.5 |
| ~2.3 | ~9.5 |
| ~2.3 | ~10.5 |
| ~2.3 | ~11.2 |
| ~2.4 | ~6.3 |
| ~2.4 | ~7.5 |
| ~2.4 | ~8.5 |
| ~2.4 | ~9.0 |
| ~2.4 | ~10.0 |
| ~2.5 | ~8.0 |
| ~2.5 | ~9.0 |
| ~2.5 | ~11.0 |
| ~2.5 | ~12.8 |
| ~2.6 | ~7.8 |
| ~2.6 | ~8.5 |
| ~2.6 | ~9.5 |
| ~2.6 | ~10.5 |
| ~2.6 | ~11.5 |
| ~2.7 | ~8.0 |
| ~2.7 | ~9.0 |
| ~2.7 | ~10.0 |
| ~2.7 | ~11.0 |
| ~2.7 | ~12.5 |
| ~2.8 | ~9.0 |
| ~2.8 | ~10.0 |
| ~2.8 | ~11.5 |
| ~2.8 | ~13.5 |
| ~2.9 | ~9.5 |
| ~2.9 | ~10.0 |
| ~2.9 | ~11.5 |
| ~3.0 | ~10.0 |
| ~3.0 | ~10.5 |
| ~3.0 | ~11.5 |
| ~3.0 | ~13.5 |
| ~3.1 | ~10.0 |
| ~3.1 | ~11.5 |
| ~3.1 | ~12.5 |
| ~3.1 | ~13.5 |
| ~3.1 | ~14.2 |
| ~3.2 | ~11.5 |
| ~3.2 | ~12.5 |
| ~3.2 | ~13.5 |
| ~3.3 | ~11.5 |
| ~3.3 | ~14.0 |
| ~3.3 | ~14.5 |
| ~3.3 | ~15.5 |
| ~3.4 | ~11.5 |
| ~3.4 | ~12.5 |
| ~3.4 | ~14.5 |
| ~3.4 | ~17.2 |
| ~3.5 | ~11.8 |
| ~3.5 | ~13.0 |
| ~3.5 | ~15.8 |
| ~3.6 | ~11.8 |
| ~3.6 | ~13.5 |
| ~3.6 | ~15.0 |
| ~3.7 | ~11.0 |
| ~3.8 | ~14.8 |
| ~3.8 | ~16.8 |
| ~3.9 | ~14.5 |
| ~3.9 | ~20.5 |
</details>

**6.9 Age and RFFT score, Part I.** A linear model fit to RFFT scores and age for 500 randomly sampled individuals from the PREVEND data has equation $\widehat { R F F T } = 1 3 7 . 5 5 - 1 . 2 6 ( A g e )$

(a) Interpret the slope and intercept values in the context of the data; i.e., explain the linear model in terms that a non-statistician would understand. Comment on whether the intercept value has any interpretive meaning in this setting.
(b) Based on the linear model, how much does RFFT score differ, on average, between an individual who is 60 years old versus an individual who is 50 years old?
(c) According to the linear model, what is the average RFFT score for an individual who is 70 years old?
(d) Examine Figure 6.1. Is it valid to use the linear model to estimate RFFT score for an individual who is 20 years old? Explain your answer.

**6.10 Guppies, Part I.** Guppies are small, brightly colored tropical fish often seen in freshwater fish aquariums. A study was conducted in 147 male guppies to examine the relationship between coloration and heterozygosity; heterozygosity refers to the condition of having different alleles at a given genetic locus. The guppies were randomly sampled from a river in the wild.

In an initial stage of the study, researchers examined whether length and height are linearly associated. The mean length is 1261.21 cm, with standard deviation 95.62 cm. The mean height is 201.75 cm, with standard deviation 20.68. The correlation between length and height is 0.85.

(a) From a visual inspection, does it seem like the line is a reasonable fit for the data?
(b) Write the equation of the regression line for predicting length from height.
(c) Estimate the predicted mean length of a guppy with height 180 cm.

![](images/page_319_chart_14.jpg)

<details>
<summary>scatter</summary>

| Height (cm) | Length (cm) |
| --- | --- |
| ~150 | ~1095 |
| ~163 | ~1130 |
| ~165 | ~1085 |
| ~172 | ~1145 |
| ~173 | ~1120 |
| ~174 | ~1175 |
| ~175 | ~1180 |
| ~176 | ~1200 |
| ~177 | ~1250 |
| ~178 | ~1230 |
| ~179 | ~1240 |
| ~180 | ~1220 |
| ~181 | ~1250 |
| ~182 | ~1230 |
| ~183 | ~1240 |
| ~184 | ~1260 |
| ~185 | ~1250 |
| ~186 | ~1240 |
| ~187 | ~1260 |
| ~188 | ~1250 |
| ~189 | ~1240 |
| ~190 | ~1260 |
| ~191 | ~1250 |
| ~192 | ~1240 |
| ~193 | ~1260 |
| ~194 | ~1250 |
| ~195 | ~1240 |
| ~196 | ~1260 |
| ~197 | ~1250 |
| ~198 | ~1240 |
| ~199 | ~1260 |
| ~200 | ~1250 |
| ~201 | ~1240 |
| ~202 | ~1260 |
| ~203 | ~1250 |
| ~204 | ~1240 |
| ~205 | ~1260 |
| ~206 | ~1250 |
| ~207 | ~1240 |
| ~208 | ~1260 |
| ~209 | ~1250 |
| ~210 | ~1240 |
| ~211 | ~1260 |
| ~212 | ~1250 |
| ~213 | ~1240 |
| ~214 | ~1260 |
| ~215 | ~1250 |
| ~216 | ~1240 |
| ~217 | ~1260 |
| ~218 | ~1250 |
| ~219 | ~1240 |
| ~220 | ~1260 |
| ~221 | ~1250 |
| ~222 | ~1240 |
| ~223 | ~1260 |
| ~224 | ~1250 |
| ~225 | ~1240 |
| ~226 | ~1260 |
| ~227 | ~1250 |
| ~228 | ~1240 |
| ~229 | ~1260 |
| ~230 | ~1250 |
| ~231 | ~1240 |
| ~232 | ~1260 |
| ~233 | ~1250 |
| ~234 | ~1240 |
| ~235 | ~1260 |
| ~236 | ~1250 |
| ~237 | ~1240 |
| ~238 | ~1260 |
| ~239 | ~1250 |
| ~240 | ~1240 |
| ~241 | ~1260 |
| ~242 | ~1250 |
| ~243 | ~1240 |
| ~244 | ~1260 |
| ~245 | ~1250 |
| ~246 | ~1240 |
| ~247 | ~1260 |
| ~248 | ~1250 |
| ~249 | ~1240 |
| ~250 | ~1260 |
| ~251 | ~1250 |
| ~252 | ~1240 |
| ~253 | ~1260 |
| ~254 | ~1250 |
| ~255 | ~1240 |
| ~256 | ~1260 |
| ~257 | ~1250 |
| ~258 | ~1240 |
| ~259 | ~1260 |
| ~260 | ~1250 |
| ~261 | ~1240 |
| ~262 | ~1260 |
| ~263 | ~1250 |
| ~264 | ~1240 |
| ~265 | ~1260 |
| ~266 | ~1250 |
| ~267 | ~1240 |
| ~268 | ~1260 |
| ~269 | ~1250 |
| ~270 | ~1240 |
| ~271 | ~1260 |
| ~272 | ~1250 |
| ~273 | ~1240 |
| ~274 | ~1260 |
| ~275 | 1600 |
</details>