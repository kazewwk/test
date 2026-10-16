# 7 Multiple linear regression

原始 PDF 第 330–385 页。

# Chapter 7

## Multiple linear regression

**7.1 Introduction to multiple linear regression**
**7.2 Simple versus multiple regression**
**7.3 Evaluating the fit of a multiple regression model**
**7.4 The general multiple linear regression model**
**7.5 Categorical predictors with several levels**
**7.6 Reanalyzing the PREVEND data**
**7.7 Interaction in regression**
**7.8 Model selection for explanatory models**
**7.9 The connection between ANOVA and regression**
**7.10 Notes**
**7.11 Exercises**

---

331

In most practical settings, more than one explanatory variable is likely to be associated with a response. This chapter discusses how the ideas behind simple linear regression can be extended to a model with multiple predictor variables.

There are several applications of multiple regression. One of the most common applications in a clinical setting is estimating an association between a re sponse variable and primary predictor of interest while adjusting for possible confounding variables. Sections 7.1 and 7.2 introduce the multiple regression model by examining the possible association between cognitive function and the use of statins after adjusting for potential confounders. Section 7.8 discusses another application of multiple regression—constructing a model that effectively explains the observed variation in the response variable.

The other sections in the chapter outline general principles of multiple re gression, including the statistical model, methods for assessing quality of model fit, categorical predictors with more than two levels, interaction, and the connection between ANOVA and regression. The methods used to conduct hypothesis tests and construct confidence intervals for regression coefficients extend natu rally from simple to multiple linear regression, so the section on the statistical model for multiple regression can be treated as optional.

![](../../raw/pages_0321-0336/images/page_330_image_4.jpg)

For labs, slides, and other resources, please visit

[www.openintro.org/book/biostat](http://www.openintro.org/redirect.php?go=biostat&referrer=biostat1_pdf)

---

332

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.1 Introduction to multiple linear regression

Statins are a class of drugs widely used to lower cholesterol. There are two main types of cholesterol: low density lipoprotein (LDL) and high density lipoprotein (HDL).<sup>1</sup> Research suggests that adults with elevated LDL may be at risk for adverse cardiovascular events such as a heart attack or stroke. In 2013, a panel of experts commissioned by the American College of Cardiology and the American Heart Association recommended that statin therapy be considered in individuals who either have any form of atherosclerotic cardiovascular disease<sup>2</sup> or have LDL cholesterol levels ≥ 190 mg/dL, individuals with Type II diabetes ages 40 to 75 with LDL between 70 to 189 mg/dL, and non-diabetic individuals ages of 40 to 75 with a predicted probability of future clogged arteries of at least 0.075.<sup>3</sup>

Health policy analysts have estimated that if the new guidelines were to be followed, almost half of Americans ages 40 to 75 and nearly all men over 60 would be prescribed a statin. However, some physicians have raised the question of whether treatment with a statin might be associated with an increased risk of cognitive decline.<sup>4</sup>, 5 Older adults are at increased risk for cardiovascular disease, but also for cognitive decline. A study by Joosten, et al. examined the association of statin use and other variables with cognitive ability in an observational cohort of 4,095 participants from the Netherlands who were part of the larger PREVEND study introduced in Section 6.1.<sup>6</sup> The analyses presented in this chapter are based on a random sample of 500 participants from the cohort.<sup>7</sup>

The investigators behind the Joosten study anticipated an issue in the analysis—statins are used more often in older adults than younger adults, and older adults suffer a natural cognitive decline. Age is a potential **confounder** in this setting. If age is not accounted for in the analysis, it may seem that cognitive decline is more common among individuals prescribed statins, simply because those prescribed statins are simply older and more likely to have reduced cognitive ability than those not prescribed statins.

<sup>1</sup>Total cholesterol level is the sum of LDL and HDL levels.
2i.e., arteries thickening and hardening with plaque
<sup>3</sup>Stone NJ, et al. 2013 ACC/AHA Guideline on the Treatment of Blood Cholesterol to Reduce Atherosclerotic Cardiovascular Risk in Adults Circulation. 2014;129:S1-S45. DOI: 10.1161/01.cir.0000437738.63853.7a
<sup>4</sup>Muldoon, Matthew F., et al. Randomized trial of the effects of simvastatin on cognitive functioning in hypercholesterolemic adults. The American journal of medicine 117.11 (2004): 823-829.
<sup>5</sup>King, Deborah S., et al. Cognitive impairment associated with atorvastatin and simvastatin. Pharmacotherapy: The Journal of Human Pharmacology and Drug Therapy 23.12 (2003): 1663-1667.
<sup>6</sup>Joosten H, Visser ST, van Eersel ME, Gansevoort RT, Bilo HJG, et al. (2014) Statin Use and Cognitive Function: Population-Based Observational Study with Long-Term Follow- Up. PLoS ONE 9(12): e115755. doi:10.1371/ journal.pone.0115755
<sup>7</sup>The random sample is accessible as prevend.samp in the oibiostat R package.

---

7.1. INTRODUCTION TO MULTIPLE LINEAR REGRESSION

333

![](../../raw/pages_0321-0336/images/page_332_chart_2.jpg)

<details>
<summary>scatter</summary>

| Series | Age (yrs) (range) | RFFT Score (range) |
| --- | --- | --- |
| Blue | 35~82 | 10~135 |
| Red | 40~82 | 10~135 |
</details>

Figure 7.1: A scatterplot showing age vs. RFFT in prevend.samp. Statin users are represented with red points; participants not using statins are shown as blue points.

Figure 7.1 visually demonstrates why age is a potential confounder for the association between statin use and cognitive function, where cognitive function is measured via the Ruff Figural Fluency Test (RFFT). Scores range from 0 (worst) to 175 (best). The blue points indicate individuals not using statins, while red points indicate statin users. First, it is clear that age and statin use are associated, with statin use becoming more common as age increases; the red points are more prevalent on the right side of the plot. Second, it is also clear that age is associated with lower RFFT scores; ignoring the colors, the point cloud drifts down and to the right. However, a close inspection of the plot suggests that for ages in relatively small ranges (e.g., ages 50-60), statin use may not be strongly associated with RFFT score—there are approximately as many red dots with low RFFT scores as with high RFFT scores in a given age range. In other words, for subsets of participants with approximately similar ages, statin use may not be associated with RFFT. Multiple regression provides a way to estimate the association of statin use with RFFT while adjusting for age; i.e., accounting for the underlying relationship between age and statin use.

---

334

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.2 Simple versus multiple regression

A simple linear regression model can be fit for an initial examination of the association between statin use and RFFT score,

$$
E (\mathrm{RFFT}) = \beta_ {0} + \beta_ {\mathrm{Statin}} (\mathrm{Statin}).
$$

RFFT scores in prevend.samp are approximately normally distributed, ranging between approximately 10 and 140, with no obvious outliers (Figure 7.2(a)). The least squares regression line shown in Figure 7.2(b) has a negative slope, which suggests a possible negative association.

![](../../raw/pages_0321-0336/images/page_333_chart_6.jpg)

<details>
<summary>histogram</summary>

| RFFT Scores (Bin) | Frequency |
| --- | --- |
| 10~20 | ~7 |
| 20~30 | ~28 |
| 30~40 | ~53 |
| 40~50 | ~63 |
| 50~60 | ~60 |
| 60~70 | ~57 |
| 70~80 | ~65 |
| 80~90 | ~55 |
| 90~100 | ~34 |
| 100~110 | ~41 |
| 110~120 | ~22 |
| 120~130 | ~10 |
| 130~140 | ~5 |
</details>

(a)

![](../../raw/pages_0321-0336/images/page_333_chart_8.jpg)

<details>
<summary>scatter</summary>

| Statin Use | RFFT Score (range) |
| --- | --- |
| 0 (No) | ~15 ~138 |
| 1 (Yes) | ~12 ~135 |
</details>

(b)

Figure 7.2: (a) Histogram of RFFT scores. (b) Scatterplot of RFFT score versus statin use in prevend.samp. The variable Statin is coded 1 for statin users, and 0 otherwise.

Figure 7.3 gives the parameter estimates of the least squares line, and indicates that the association between RFFT score and statin use is highly significant. On average, statin users score approximately 10 points lower on the RFFT. However, even though the association is statistically significant, it is potentially misleading since the model does not account for the underlying relationship between age and statin use. The association between age and statin use visible from Figure 7.1 is even more apparent in Figure 7.4, which shows that the median age of statin users is about 10 years higher than the median age of individuals not using statins.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 70.7143 | 1.3808 | 51.21 | 0.0000 |
| Statin | -10.0534 | 2.8792 | -3.49 | 0.0005 |

Figure 7.3: R summary output for the simple regression model of RFFT versus statin use in prevend.samp.

---

7.2. SIMPLE VERSUS MULTIPLE REGRESSION

335

![](../../raw/pages_0321-0336/images/page_334_chart_2.jpg)

<details>
<summary>boxplot</summary>

| Statin Use | Q1 | Q2 (Median) | Q3 | Min | Max |
| --- | --- | --- | --- | --- | --- |
| 0 | ~44 | ~51 | ~61 | ~36 | ~81 |
| 1 | ~54.5 | ~61 | ~69.5 | ~36 | ~81 |
</details>

Figure 7.4: Boxplot of age by statin use in prevend.samp. The variable Statin is coded 1 for statin users, and 0 otherwise.

Multiple regression allows for a model that incorporates both statin use and age,

$$
E (\mathrm{RFFT}) = \beta_ {0} + \beta_ {\text {Statin}} (\text {Statin}) + \beta_ {\text {Age}} (\text {Age}).
$$

In statistical terms, the association between RFFT and Statin is being estimated after adjusting for Age. This is an example of one of the more important applications of multiple regression: estimating an association between a response variable and primary predictor of interest while adjusting for possible confounders. In this setting, statin use is the primary predictor of interest.

The principles and assumptions behind the multiple regression model are introduced more formally in Section 7.4, along with the method used to estimate the coefficients. Figure 7.5 shows the parameter estimates for the model from R.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 137.8822 | 5.1221 | 26.92 | 0.0000 |
| Statin | 0.8509 | 2.5957 | 0.33 | 0.7432 |
| Age | -1.2710 | 0.0943 | -13.48 | 0.0000 |

Figure 7.5: R summary output for the multiple regression model of RFFT versus statin use and age in prevend.samp.

---

336

CHAPTER 7. MULTIPLE LINEAR REGRESSION

E

## EXAMPLE 7.1

Using the parameter estimates in Figure 7.5, write the prediction equation for the linear model. How does the predicted RFFT score for a 67-year-old not using statins compare to that of an individual of the same age who does use statins?

The equation of the linear model is

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 8 8 2 2 + 0. 8 5 0 9 (\text {Statin}) - 1. 2 7 1 0 (\text {Age}).
$$

The predicted RFFT score for a 67-year-old not using statins (Statin = 0) is

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 8 8 2 2 + (0. 8 5 0 9) (0) - (1. 2 7 1 0) (6 7) = 5 2. 7 2 5 2.
$$

The predicted RFFT score for a 67-year-old using statins (Statin = 1) is

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 8 8 2 2 + (0. 8 5 0 9) (1) - (1. 2 7 1 0) (6 7) = 5 3. 5 7 6 1.
$$

The two calculations differ only by the value of the coefficient $\beta _ { \mathrm { S t a t i n } } ,   0 . 8 5 0 9 . ^ { 8 }$ Thus, for two individuals who are the same age, the model predicts that RFFT score will be 0.8509 higher in the individual taking statins; statin use is associated with a small increase in RFFT score.

## EXAMPLE 7.2

Suppose two individuals are both taking statins; one individual is 50 years of age, while the other is 60 years of age. Compare their predicted RFFT scores.

From the model equation, the coefficient of age $\beta _ { \mathrm { A g e } }$ is -1.2710; an increase in one unit of age (i.e., one year) is associated with a decrease in RFFT score of -1.2710, when statin use is the same. Thus, the individual who is 60 years of age is predicted to have an RFFT score that is about 13 points lower $( ( - 1 . 2 7 1 0 ) ( 1 0 ) = - 1 2 . 7 1 0 )$ than the individual who is 50 years of age.

This can be confirmed numerically:

The predicted RFFT score for a 50-year-old using statins is

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 8 8 2 2 + (0. 8 5 0 9) (1) - (1. 2 7 1 0) (5 0) = 7 5. 1 8 3 1.
$$

The predicted RFFT score for a 60-year-old using statins is

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 8 8 2 2 + (0. 8 5 0 9) (1) - (1. 2 7 1 0) (6 0) = 6 2. 4 7 3 1.
$$

The scores differ by 62.4731 − 75.1831 = −12.710.

E

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>In most cases, predictions do not need to be calculated to so many significant digits, since the coefficients are only estimates. This example uses the additional precision to illustrate the role of the coefficients.</span></small>

---

7.2. SIMPLE VERSUS MULTIPLE REGRESSION

337

![](../../raw/pages_0337-0352/images/page_336_image_2.jpg)

## GUIDED PRACTICE 7.3

What does the intercept represent in this model? Does the intercept have interpretive value?<sup>9</sup>

As in simple linear regression, t-statistics can be used to test hypotheses about the slope coefficients; for this model, the two null hypotheses are $H _ { 0 } : \beta _ { \mathrm { S t a t i n } } = 0$ and $H _ { 0 } : \beta _ { \mathrm { A g e } } = 0 .$ . The p-values for the tests indicate that at significance level $\alpha = 0 . 0 5$ , the association between RFFT score and statin use is not statistically significant, but the association between RFFT score and age is significant.

In a clinical setting, the interpretive focus lies on reporting the nature of the association between the primary predictor and the response and specifying which confounders have been adjusted for. The results of the analysis might be summarized as follows—

Although the use of statins appeared to be associated with lower RFFT scores when no adjustment was made for possible confounders, statin use is not significantly associated with RFFT score in a regression model that adjusts for age.

The results shown in Figure 7.5 do not provide information about either the quality of the model fit or its value as a prediction model. The next section describes the residual plots that can be used to check model assumptions and the use of $R ^ { 2 }$ to estimate how much of the variability in the response variable is explained by the model.

There is an important aspect of these data that should not be overlooked. The data do not come from a study in which participants were followed as they aged; i.e., a longitudinal study. Instead, this study was a cross-sectional study, in which patient age, statin use, and RFFT score were recorded for all participants during a short time interval. While the results of the study support the conclusion that older patients tend to have lower RFFT scores, they cannot be used to conclude that scores decline with age in individuals; there were no repeated measurements of RFFT taken as individual participants aged. Older patients come from an earlier birth cohort, and it is possible, for instance, that younger participants have more post-secondary school education or better health practices generally; such a cohort effect may have some explanatory effect on the observed association. The details of how a study is designed and how data are collected should always be taken into account when interpreting study results.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>The intercept represents an individual with value 0 for both Statin and Age; i.e., an individual not using statins with age of 0 years. It is not reasonable to predict RFFT score for a newborn, or to assess statin use; the intercept is meaningless and has no interpretive value.</span></small>

---

338

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.3 Evaluating the fit of a multiple regression model

## 7.3.1 Using residuals to check model assumptions

The assumptions behind multiple regression are essentially the same as the four assumptions listed in Section 6.1 for simple linear regression. The assumption of linearity is extended to multi-ple regression by assuming that when only one predictor variable changes, it is linearly related to the change in the response variable. Assumption 2 becomes the slightly more general assumption that the residuals have approximately constant variance. Assumptions 3 and 4 do not change; it is assumed that the observations on each case are independent and the residuals are approximately normally distributed.

Since it is not possible to make a scatterplot of a response variable against several simultaneous predictors, residual plots become even more essential as tools for checking modeling assumptions.

To assess the linearity assumption, examine plots of residuals against each of the predictors. These plots might show an nonlinear trend that could be corrected with a transformation. The scatterplot of residual values versus age in Figure 7.6 shows no apparent nonlinear trends. It is not necessary to assess linearity against a categorical predictor, since a line drawn through two points (i.e., the means of the two groups) is necessarily linear.

![](../../raw/pages_0337-0352/images/page_337_chart_7.jpg)

<details>
<summary>scatter</summary>

| Age (yrs) | Residual |
| --- | --- |
| ~36 | ~42 |
| ~36 | ~45 |
| ~37 | ~-64 |
| ~38 | ~-30 |
| ~39 | ~-15 |
| ~40 | ~-48 |
| ~41 | ~-35 |
| ~42 | ~-56 |
| ~43 | ~-35 |
| ~44 | ~-35 |
| ~45 | ~-35 |
| ~46 | ~-35 |
| ~47 | ~-35 |
| ~48 | ~-35 |
| ~49 | ~-35 |
| ~50 | ~-35 |
| ~51 | ~-35 |
| ~52 | ~-35 |
| ~53 | ~-35 |
| ~54 | ~-35 |
| ~55 | ~-35 |
| ~56 | ~-35 |
| ~57 | ~-35 |
| ~58 | ~-35 |
| ~59 | ~-35 |
| ~60 | ~-35 |
| ~61 | ~-35 |
| ~62 | ~-35 |
| ~63 | ~-35 |
| ~64 | ~-35 |
| ~65 | ~-35 |
| ~66 | ~-35 |
| ~67 | ~-35 |
| ~68 | ~-35 |
| ~69 | ~-35 |
| ~70 | ~-35 |
| ~71 | ~-35 |
| ~72 | ~-35 |
| ~73 | ~-35 |
| ~74 | ~-35 |
| ~75 | ~-35 |
| ~76 | ~-35 |
| ~77 | ~-35 |
| ~78 | ~-35 |
| ~79 | ~-35 |
| ~80 | ~-35 |
</details>

Figure 7.6: Residuals versus age in the model for RFFT vs statins and age in the PREVEND data.

---

7.3. EVALUATING THE FIT OF A MULTIPLE REGRESSION MODEL

339

Since each case has one predicted value and one residual, regardless of the number of pre dictors, residuals can still be plotted against predicted values to assess the constant variance as sumption. The scatterplot in the left panel of Figure 7.7 shows that the variance of the residuals is slightly smaller for lower predicted values of RFFT, but is otherwise approximately constant.

Just as in simple regression, normal probability plots can be used to check the normality assumption of the residuals. The normal probability plot in the right panel of Figure 7.7 shows that the residuals from the model are reasonably normally distributed, with only slight departures from normality in the tails.

![](../../raw/pages_0337-0352/images/page_338_image_4.jpg)

Figure 7.7: Residual plots from the linear model for RFFT versus statin use and age in prevend.samp.

---

340

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## EXAMPLE 7.4

Section 1.7 featured a case study examining the evidence for ethnic discrimination in the amount of financial support offered by the State of California to individuals with developmental disabilities. Although an initial look at the data suggested an association between expenditures and ethnicity, further analysis suggested that age is a confounding variable for the relationship.

A multiple regression model can be fit to these data to model the association between expenditures, age, and ethnicity in a subset that only includes data from Hispanics and White non-Hispanics. Two residual plots from the model fit for

$$
E (\text {expenditures}) = \beta_ {0} + \beta_ {\text {ethnicity}} (\text {ethnicity}) + \beta_ {\text {age}} (\text {age})
$$

are shown in Figure 7.8. From these plots, assess whether a linear regression model is appropriate for these data.

The model assumptions are clearly violated. The residual versus fitted plot shows obvious patterns; the residuals do not scatter randomly about the $y = 0$ line. Additionally, the variance of the residuals is not constant around the $y = 0$ y = 0 line. As shown in the normal probability plot, the residuals show marked departures from normality, particularly in the upper tail; although this skewing may be partially resolved with a log transformation, the patterns in the residual versus fitted plot are more problematic.

Recall that a residual is the difference between an observed value and expected value; for an observation $i ,$ the residual equals $y _ { i }   -   \hat { y } _ { i }$ . Positive residuals occur when a model’s predictions are smaller that the observed values, and vice versa for negative residuals. In the residual versus fitted plot, it can be seen that in the middle range of predicted values, the model consistently under-predicts expenditures; on the upper and lower ends, the model over-predicts. This is a particularly serious issue with the model fit.

A single linear regression model is not appropriate for these data. For a more detailed examination of the model residuals, refer to Chapter 7, Lab 2. With some subsetting according to age cohort, it can be reasonable to use linear regression for modeling these data.

![](../../raw/pages_0337-0352/images/page_339_image_10.jpg)

Figure 7.8: Residual versus fitted values plot and residual normal probability plot from the linear model for expenditures versus ethnicity and age for a subset of dds.discr.

E

---

7.3. EVALUATING THE FIT OF A MULTIPLE REGRESSION MODEL

341

## 7.3.2 Using $R ^ { 2 }$ and adjusted $R ^ { 2 }$ with multiple regression

Section 6.3.2 provided two definitions of the $R ^ { 2 }$ statistic—it is the square of the correlation coefficient r between a response and the single predictor in simple linear regression, and equivalently, it is the proportion of the variation in the response variable explained by the model. In statistical terms, the second definition can be written as

$$
R ^ {2} = \frac {\mathrm{Var} (y _ {i}) - \mathrm{Var} (e _ {i})}{\mathrm{Var} (y _ {i})} = 1 - \frac {\mathrm{Var} (e _ {i})}{\mathrm{Var} (y _ {i})},
$$

where $y _ { i }$ and $e _ { i }$ denote the response and residual values for the $i ^ { \mathrm { t h } }$ case.

The first definition cannot be used in multiple regression, since there is a correlation coefficient between each predictor and the response variable. However, since there is a single set of residuals, the second definition remains applicable.

Although $R ^ { 2 }$ can be calculated directly from the equation, it is rarely calculated by hand since statistical software includes $R ^ { 2 }$ as a standard part of the summary output for a regression model.<sup>10</sup> In the model with response RFFT and predictors Statin and Age, $R ^ { 2 } = 0 . 2 8 5 2$ . The model explains almost 29% of the variability in RFFT scores, a considerable improvement over the model with Statin alone $( R ^ { 2 } = 0 . 0 2 3 9 )$

Adding a variable to a regression model always increases the value of $R ^ { 2 }$ . Sometimes that increase is large and clearly important, such as when age is added to the model for RFFT scores. In other cases, the increase is small, and may not be worth the added complexity of including another variable. The **adjusted R-squared** is often used to balance predictive ability with complexity in a multiple regression model. Like $R ^ { 2 } ,$ , the adjusted $R ^ { 2 }$ is routinely provided in software output.

## ADJUSTED $\mathbb { R } ^ { 2 }$ AS A TOOL FOR MODEL ASSESSMENT

The adjusted $\mathbf { R } ^ { 2 }$ is computed as

$$
R _ {a d j} ^ {2} = 1 - \frac {\operatorname{Var} (e _ {i}) / (n - p - 1)}{\operatorname{Var} (y _ {i}) / (n - 1)} = 1 - \frac {\operatorname{Var} (e _ {i})}{\operatorname{Var} (y _ {i})} \times \frac {n - 1}{n - p - 1},
$$

where n is the number of cases used to fit the model and $p$ is the number of predictor variables in the model.

Essentially, the adjusted $R ^ { 2 }$ imposes a penalty for including additional predictors that do not contribute much towards explaining the observed variation in the response variable. The value of the adjusted $R ^ { 2 }$ in the model with both Statin and Age is 0.2823, which is essentially the same as the $R ^ { 2 }$ value of 0.2852. The additional predictor Age considerably increases the strength of the model, resulting in only a small penalty to the $R ^ { 2 }$ value.

While the adjusted $R ^ { 2 }$ is useful as a statistic for comparing models, it does not have an inherent interpretation like $R ^ { 2 }$ . Students often confuse the interpretation of $R ^ { 2 }$ and adjusted $R ^ { 2 } )$ while the two are similar, adjusted $R ^ { 2 }$ is not the proportion of variation in the response variable explained by the model. The use of adjusted $R ^ { 2 }$ for model selection will be discussed in Section 7.8.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10<sub>In</sub> R and other software, R<sup>2</sup>is typically labeled ’multiple R-squared’.</span></small>

---

342

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.4 The general multiple linear regression model

This section provides a compact summary of the multiple regression model and contains more mathematical detail than most other sections; the next section, Section 7.5, discusses categorical predictors with more than two levels. The ideas outlined in this section and the next are illustrated with an extended analysis of the PREVEND data in Section 7.6.

## 7.4.1 Model parameters and least squares estimation

For multiple regression, the data consist of a response variable Y and $p$ explanatory variables $X_{1},X_{2},\cdots,X_{p}$ . Instead of the simple regression model

$$
Y = \beta_ {0} + \beta_ {1} X + \varepsilon ,
$$

multiple regression has the form

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \beta_ {3} X _ {3} + \dots + \beta_ {p} X _ {p} + \varepsilon ,
$$

or equivalently

$$
E (Y) = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \beta_ {3} X _ {3} + \dots + \beta_ {p} X _ {p},
$$

since the normally distributed error term ε is assumed to have mean 0. Each predictor $x _ { i }$ has an associated coefficient $\beta _ { i }$ . In simple regression, the slope coefficient $\beta$ captures the change in the response variable $Y$ associated with a one unit change in the predictor $X .$ . In multiple regression, the coefficient $\beta _ { j }$ of a predictor $X _ { j }$ denotes the change in the response variable Y associated with a one unit change in $X _ { j }$ when none of the other predictors change; i.e., each $\beta$ coefficient in multiple regression plays the role of a slope, as long as the other predictors are not changing.

Multiple regression can be thought of as the model for the mean of the response Y in a population where the mean depends on the values of the predictors, rather than being constant. For example, consider a setting with two binary predictors such as statin use and sex; the predictors partition the population into four subgroups, and the four predicted values from the model are estimates of the mean in each of the four groups.

---

7.4. THE GENERAL MULTIPLE LINEAR REGRESSION MODEL

343

![](../../raw/pages_0337-0352/images/page_342_image_2.jpg)

## GUIDED PRACTICE 7.5

Figure 7.9 shows an estimated regression model for RFFT with predictors Statin and Gender, where Gender is coded 0 for males and 1 for females.<sup>11</sup> Based on the model, what are the estimated mean RFFT scores for the four groups defined by these two categorical predictors?<sup>12</sup>

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 70.4068 | 1.8477 | 38.11 | 0.0000 |
| Statin | -9.9700 | 2.9011 | -3.44 | 0.0006 |
| Gender | 0.6133 | 2.4461 | 0.25 | 0.8021 |

Figure 7.9: R summary output for the multiple regression model of RFFT versus statin use and sex in prevend.samp.

Datasets for multiple regression have n cases, usually indexed algebraically by i, where i takes on values from 1 to $n ;$ 1 denotes the first case in the dataset and n denotes the last case. The dataset prevend.samp contains $n = 5 0 0$ observations. Algebraic representations of the data must indicate both the case number and the predictor in the set of p predictors. For case i in the dataset, the variable $X _ { i j }$ denotes predictor $X _ { j } ;$ the response for case i is simply $Y _ { i } ,$ since there can only be one response variable. The dataset prevend.samp has many possible predictors, some of which are examined later in this chapter. The analysis in Section 7.2 used $p = 2$ predictors, Statin and Age.

Just as in Chapter 2, upper case letters are used when thinking of data as a set of random observations subject to sampling from a population, and lower case letters are used for observed values. In a dataset, it is common for each row to contain the information on a single case; the observations in row i of a dataset with p predictors can be written as $( y _ { i } , x _ { i 1 } , x _ { i 2 } , \ldots , x _ { i p } )$

For any given set of estimates $b _ { 1 } , b _ { 2 } , \cdots , b _ { p }$ and predictors $x_{i1},x_{i2},\cdots,x_{ip},$ predicted values of the response can be calculated using

$$
\hat {y} _ {i} = b _ {0} + b _ {1} x _ {i 1} + b _ {2} x _ {i 2} + \dots + b _ {p} x _ {i p},
$$

where $b _ { 0 } , b _ { 1 } , \cdots , b _ { p }$ are estimates of the coefficients $\beta _ { 0 } , \beta _ { 1 } , \ldots , \beta _ { p }$ obtained using the principle of least squares estimation.

As in simple regression, each prediction has an associated residual, which is the difference between the observed value $y _ { i }$ and the predicted value $\hat { y _ { i } }$ , or $e _ { i } = y _ { i } - \hat { y _ { i } }$ . The least squares estimate of the model is the set of estimated coefficients $b _ { 0 } , b _ { 1 } , \cdots b _ { p }$ that minimizes $e _ { 1 } ^ { 2 } + e _ { 2 } ^ { 2 } + \cdots e _ { n } ^ { 2 } .$ . Explicit formulas for the estimates involve advanced matrix theory, but are rarely used in practice. Instead, estimates are calculated using software such as as R, Stata, or Minitab.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11<sub>Until</sub> recently, it was common practice to use gender to denote biological sex. Gender is different than biological sex, but this text uses the original names in published datasets.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12<sub>The</sub> prediction equation for the model is RFFT = 70  .41 − 9.97(Statin) + 0.61(Gender). Both Statin and Gender can take on values of either 0 or 1; the four possible subgroups are statin non-user / male (0, 0), statin non-user / female (0, 1), statin user / male (1, 0), statin user / female (1, 1). Predicted RFFT scores for these groups are 70.41, 71.02, 60.44, and 61.05, respectively.</span></small>

---

344

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.4.2 Hypothesis tests and confidence intervals

## Using t-tests for individual coefficients

The test of the null hypothesis $H _ { 0 } : \beta _ { k } = 0$ is a test of whether the predictor $X _ { k }$ is associated with the response variable. When a coefficient of a predictor equals $0 ,$ the predicted value of the response does not change when the predictor changes; i.e., a value of 0 indicates there is no association between the predictor and response. Due to the inherent variability in observed data, an estimated coefficient $b _ { k }$ will almost never be 0 even when the model coefficient $\beta _ { k }$ is. Hypothesis testing can be used to assess whether the estimated coefficient is significantly different from 0 by examining the ratio of the estimated coefficient to its standard error.

When the assumptions of multiple regression hold, at least approximately, this ratio has a t-distribution with $n - \left( p + 1 \right) = n - p - 1$ degrees of freedom when the model coefficient is $0 .$ The formula for the degrees of freedom follows a general rule that appears throughout statistics—the degrees of freedom for an estimated model is the number of cases in the dataset minus the number of estimated parameters. There are $p + 1$ parameters in the multiple regression model, one for each of the $p$ predictors and one for the intercept.

## SAMPLING DISTRIBUTIONS OF ESTIMATED COEFFICIENTS

Suppose

$$
\hat {y} = b _ {0} + b _ {1} x _ {i} + b _ {2} x _ {i} + \dots + b _ {p} x _ {i}
$$

is an estimated multiple regression model from a dataset with n observations on the response and predictor variables, and let $b _ { k }$ be one of the estimated coefficients. Under the hypothesis $H _ { 0 } : \beta _ { k } = 0 ,$ the standardized statistic

$$
\frac {b _ {k}}{\text {s.e.} (b _ {k})}
$$

has a t-distribution with $n - p - 1$ degrees of freedom.

This sampling distribution can be used to conduct hypothesis tests and construct confidence intervals.

## TESTING A HYPOTHESIS ABOUT A REGRESSION COEFFICIENT

A test of the two-sided hypothesis

$$
H _ {0}: \beta_ {k} = 0 \text {vs.} H _ {A}: \beta_ {k} \neq 0
$$

is rejected with significance level α when

$$
\frac {| b _ {k} |}{\text {s.e.} (b _ {k})} > t _ {\mathrm{df}} ^ {\star},
$$

where $t _ { \mathrm { d f } } ^ { \star }$ is the point on a t-distribution with $n   -   p   -   1$ degrees of freedom and area $( 1 - \alpha / 2 )$ in the left tail.

---

7.4. THE GENERAL MULTIPLE LINEAR REGRESSION MODEL

345

For one-sided tests, $t _ { \mathrm { d f } } ^ { \star }$ is the point on a t-distribution with $n – p – 1$ degrees of freedom and area $( 1 - \alpha )$ in the left tail. A one-sided test of $H _ { 0 }$ against $H _ { A } : \beta _ { k } > 0$ rejects when the standardized co-efficient is greater than $t _ { \mathrm { d f } } ^ { \star } ;$ a one-sided test of $H _ { 0 }$ against $H _ { A } : \beta _ { k } < 0$ rejects when the standardized coefficient is less than $t _ { \mathrm { d f } } ^ { \star } .$

## CONFIDENCE INTERVALS FOR REGRESSION COEFFICIENT

A two-sided $1 0 0 ( 1 - \alpha )$ % confidence interval for the model coefficient $\beta _ { k }$ is

$$
b _ {k} \pm \text {s.e.} (b _ {k}) \times t _ {\mathrm{df}} ^ {\star}.
$$

All statistical software packages provide an estimate s of the standard deviation of the residuals .

## The F-statistic for an overall test of the model

When all the model coefficients are 0, the predictors in the model, considered as a group, are not associated with the response; i.e., the response variable is not associated with any linear combination of the predictors. The F-statistic is used to test this null hypothesis of no association, using the following idea.

The variability of the predicted values about the overall mean response can be estimated by

$$
\mathrm{MSM} = \frac {\sum_ {i} (\hat {y} _ {i} - \overline {{y}}) ^ {2}}{p}.
$$

In this expression, p is the number of predictors and is the degrees of freedom of the numerator sum of squares (derivation not given here). The term **MSM** is called the model sum of squares because it reflects the variability of the values predicted by the model $( \hat { y _ { i } } )$ about the mean (y) response.<sup>13</sup> In an extreme case, MSM will have value 0 when all the predicted values coincide with the overall mean; in this scenario, a model would be unnecessary for making predictions, since the average of all observations could be used to make a prediction.

The variability in the residuals can be measured by

$$
\mathrm{MSE} = \frac {\sum_ {i} (y _ {i} - \hat {y} _ {i}) ^ {2}}{n - p - 1}.
$$

**MSE** is called the mean square of the errors since residuals are the observed ‘errors’, the differences between predicted and observed values.

When MSM is small compared to MSE, the model has captured little of the variability in the data, and the model is of little or no value. The F-statistic is given by

$$
F = \frac {\mathrm{MSM}}{\mathrm{MSE}}.
$$

The formula is not used for calculation, since the numerical value of the F-statistic is a routine part of the output of regression software.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13<sub>It</sub> turns out that y is also the mean of the predicted values.</span></small>

---

346

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## THE F-STATISTIC IN REGRESSION

The F-statistic in regression is used to test the null hypothesis

$$
H _ {0}: \beta_ {1} = \beta_ {2} = \dots = \beta_ {p} = 0
$$

against the alternative that at least one of the coefficients is not 0.

Under the null hypothesis, the sampling distribution of the F-statistic is an F-distribution with parameters $( p , n - p - 1 )$ and the null hypothesis is rejected if the value of the F-statistic is in the right tail of the distribution of the sampling distribution with area $\alpha ,$ where α is the significance level of the test.

The F-test is inherently one-sided—deviations from the null hypothesis of any form will push the statistic to the right tail of the F-distribution. The $p \cdot$ value from the right tail of the F-distribution should never be doubled. Students also sometimes make the mistake of assuming that if the null hypothesis of the F-test is rejected, all coefficients must be non-zero, instead of at least one. A significant p-value for the F-statistic suggests that the predictor variables in the model, when considered as a group, are associated with the response variable.

In practice, it is rare for the F-test not to reject the null hypothesis, since most regression models are used in settings where a scientist has prior evidence that at least some of the predictors are useful.

## Confidence and Prediction Intervals

The confidence and prediction intervals discussed in Section 6.5 can be extended to multiple regression. Predictions based on specific values of the predictors are made by evaluating the estimated model at those values, and both confidence intervals for the mean and prediction intervals for a new observation are constructed using the corresponding standard errors. The formulas for standard errors in the multiple predictor setting are beyond the scope of this text, and there are no simple approximate formulas that can be calculated by hand. They are always computed in software.

Figure 7.5 shows the estimated regression model used to examine the association of age and statin use with RFFT score in PREVEND. As shown in Example 7.5, the predicted RFFT score for a $6 7$ -year-old statin user is 57.6 points. Software can be used to show that a 95% confidence interval for the mean RFFT score for $6 7 \cdot$ -year-old statin users is (49.2, 58.9) points, while a 95% prediction interval for the RFFT score of a particular $6 7 \cdot$ -year statin user is (7.8, 99.4) points. Just as with simple linear regression, the prediction interval is wider than the confidence interval for the mean because it accounts for both variability in the estimated mean and variability in a new observation of the response, RFFT score.

---

7.5. CATEGORICAL PREDICTORS WITH SEVERAL LEVELS

347

## 7.5 Categorical predictors with several levels

In the initial model fit with the PREVEND data, the variable Statin is coded 0 if the participant was not using statins, and coded 1 if the participant was a statin user. The category coded 0 is referred to as the reference category; in this model, statin non-users (Statin = 0) are the reference category. The estimated coefficient $\beta _ { \mathrm { S t a t i n } }$ is the change in the average response between the reference category and the category Statin = 1.

Since the variable Statin is categorical, the numerical codes 0 and 1 are simply labels for statin non-users and users. The labels can be specified more explicitly in software. For example, in R, categorical variables can be coded as factors; the levels of the variable are displayed as text (such as "NonUser" or "User"), while the data remain stored as integers. The R output with the variable Statin.factor is shown in Figure 7.10, where 0 corresponds to the label "NonUser" and 1 corresponds to "User". The predictor variable is now labeled Statin.factorUser; the estimate -10.05 is the change in mean RFFT from the "NonUser" (reference) category to the "User" category. Note how the reference category is not explicitly labeled; instead, it is contained within the intercept.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 70.7143 | 1.3808 | 51.21 | 0.0000 |
| Statin.factorUser | -10.0534 | 2.8792 | -3.49 | 0.0005 |

Figure 7.10: R summary output for the simple regression model of RFFT versus statin use in prevend.samp, with Statin converted to a factor called Statin.factor that has levels NonUser and User.

For a categorical variable with two levels, estimates from the regression model remain the same regardless of whether the categorical predictor is treated as numerical or not. A "one unit change" in the numerical sense corresponds exactly to the switch between the two categories. However, this is not true for categorical variables with more than two levels.

This idea will be explored with the categorical variable Education, which indicates the highest level of education that an individual completed in the Dutch educational system: primary school, lower secondary school, higher secondary education, or university education. In the PREVEND dataset, educational level is coded as either 0, 1, 2, or 3, where 0 denotes at most a primary school education, 1 a lower secondary school education, 2 a higher secondary education, and 3 a university education. Figure 7.11 shows the distribution of RFFT by education level; RFFT scores tend to increase as education level increases.

In a regression model with a categorical variable with more than two levels, one of the categories is set as the reference category, just as in the setting with two levels for a categorical predictor. The remaining categories each have an estimated coefficient, which corresponds to the estimated change in response relative to the reference category.

---

348

CHAPTER 7. MULTIPLE LINEAR REGRESSION

![](../../raw/pages_0337-0352/images/page_347_chart_2.jpg)

<details>
<summary>boxplot</summary>

| Education level | Q1 | Q2 (Median) | Q3 | IQR |
| --- | --- | --- | --- | --- |
| 0 | ~27 | ~34 | ~51 | ~24 |
| 1 | ~40 | ~53 | ~69 | ~29 |
| 2 | ~55 | ~73 | ~89 | ~34 |
| 3 | ~69 | ~87 | ~105 | ~36 |
</details>

Figure 7.11: Box plots for RFFT score by education level in prevend.samp.

## EXAMPLE 7.6

Is RFFT score associated with educational level? Interpret the coefficients from the following model. Figure 7.12 provides the R output for the regression model of RFFT versus educational level in prevend.samp. The variable Education has been converted to Education.factor, which has levels Primary, LowerSecond, HigherSecond, and Univ.

It is clearest to start with writing the model equation:

$$
\widehat {\mathrm{RFFT}} = 4 0. 9 4 + 1 4. 7 8 (\text {EduLowerSecond}) + 3 2. 1 3 (\text {EduHigherSecond}) + 4 4. 9 6 (\text {EduUniv})
$$

Each of the predictor levels can be thought of as binary variables that can take on either 0 or 1, where only one level at most can be a 1 and the rest must be 0, with 1 corresponding to the category of interest. For example, the predicted mean RFFT score for individuals in the Lower Secondary group is given by

$$
\widehat {\mathrm{RFFT}} = 4 0. 9 4 + 1 4. 7 8 (1) + 3 2. 1 3 (0) + 4 4. 9 6 (0) = 5 5. 7 2.
$$

The value of the LowerSecond coefficient, 14.78, is the change in predicted mean RFFT score from the reference category Primary to the LowerSecond category.

Participants with a higher secondary education scored approximately 32.1 points higher on the RFFT than individuals with only a primary school education, and have estimated mean RFFT score $4 0 . 9 4 + 3 2 . 1 3 = 7 3 . 0 7$ . Those with a university education have estimated mean RFFT score 40.94 + $4 4 . 9 6 = 8 5 . 9 0$

The intercept value, 40.94, corresponds to the estimated mean RFFT score for individuals who at most completed primary school. From the regression equation,

$$
\widehat {\mathrm{RFFT}} = 4 0. 9 4 + 1 4. 7 8 (0) + 3 2. 1 3 (0) + 4 4. 9 6 (0) = 4 0. 9 4.
$$

The p-values indicate that the change in mean score between participants with only a primary school education and any of the other categories is statistically significant.

E

---

7.5. CATEGORICAL PREDICTORS WITH SEVERAL LEVELS

349

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 40.9412 | 3.2027 | 12.78 | 0.0000 |
| Education.factorLowerSecond | 14.7786 | 3.6864 | 4.01 | 0.0001 |
| Education.factorHigherSecond | 32.1335 | 3.7631 | 8.54 | 0.0000 |
| Education.factorUniv | 44.9639 | 3.6835 | 12.21 | 0.0000 |

Figure 7.12: R summary output for the regression model of RFFT versus educational level in prevend.samp, with Education converted to a factor called Education.factor that has levels Primary, LowerSecond, HigherSecond, and Univ.

## EXAMPLE 7.7

Suppose that the model for predicting RFFT score from educational level is fitted with Education, using the original numerical coding with 0, 1, 2, and 3; the R output is shown in Figure 7.13. What does this model imply about the change in mean RFFT between groups? Explain why this model is flawed.

According to this model, the change in mean RFFT between groups increases by 15.158 for any one unit change in Education. For example, the change in means between the groups coded 0 and 1 is necessarily equal to the change in means between the groups coded 2 and 3, since the predictor changes by 1 in both cases.

It is unreasonable to assume that the change in mean RFFT score when comparing the primary school group to the lower secondary group will be equal to the difference in means between the higher secondary group and university group. The numerical codes assigned to the groups are simply short-hand labels, and are assigned arbitrarily. As a consequence, this model would not provide consistent results if the numerical codes were altered; for example, if the primary school group and lower secondary group were relabeled such that the predictor changes by 2, the estimated difference in mean RFFT would change.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 41.148 | 2.104 | 19.55 | 0.0000 |
| Education | 15.158 | 1.023 | 14.81 | 0.0000 |

Figure 7.13: R summary output for the simple regression model of RFFT versus educational level in prevend.samp, where Education is treated as a numerical variable. Note that it would be incorrect to fit this model; Figure 7.12 shows the results from the correct approach.

Categorical variables can be included in multiple regression models with other predictors, as is shown in the next section. Section 7.9 discusses the connection between ANOVA and regression models with only one categorical predictor.

E

---

350

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.6 Reanalyzing the PREVEND data

The earlier models fit to examine the association between cognitive ability and statin use showed that considering statin use alone could be misleading. While older participants tended to have lower RFFT scores, they were also more likely to be taking statins. Age was found to be a **confounder** in this setting—is it the only confounder?

Potential confounders are best identified by considering the larger scientific context of the analysis. For the PREVEND data, there are two natural candidates for potential confounders: education level and presence of cardiovascular disease. The use of medication is known to vary by education levels, often because individuals with more education tend to have higher incomes and consequently, better access to health care; higher educational levels are associated with higher RFFT scores, as shown by model 7.12. Individuals with cardiovascular disease are often prescribed statins to lower cholesterol; cardiovascular disease can lead to vascular dementia and cognitive decline.

Figure 7.14 contains the result of a regression of RFFT with statin use, adding the possible confounders age, educational level, and presence of cardiovascular disease. The variables Statin, Education and CVD have been converted to factors, and Age is a continuous predictor.

The coefficient for statin use shows the importance of adjusting for confounders. In the initial model for RFFT that only included statin use as a predictor, statin use was significantly associated with decreased RFFT scores. After adjusting for age, statins were no longer significantly associated with RFFT scores, but the model suggested that statin use could be associated with increased RFFT scores. This final model suggests that, after adjusting for age, education, and the presence of cardiovascular disease, statin use is associated with an increase in RFFT scores of approximately 4.7 points. The p-value for the slope coefficient for statin use is 0.056, which suggests moderately strong evidence of an association (significant at $\alpha = 0 . 1 0 ,$ but not $\alpha = 0 . 0 5 )$

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 99.0351 | 6.3301 | 15.65 | 0.0000 |
| Statin.factorUser | 4.6905 | 2.4480 | 1.92 | 0.0559 |
| Age | -0.9203 | 0.0904 | -10.18 | 0.0000 |
| Education.factorLowerSecond | 10.0883 | 3.3756 | 2.99 | 0.0029 |
| Education.factorHigherSecond | 21.3015 | 3.5777 | 5.95 | 0.0000 |
| Education.factorUniv | 33.1246 | 3.5471 | 9.34 | 0.0000 |
| CVD.factorPresent | -7.5665 | 3.6516 | -2.07 | 0.0388 |

Figure 7.14: R summary output for the multiple regression model of RFFT versus statin use, age, education, and presence of cardiovascular disease in prevend.samp.

The $R ^ { 2 }$ for the model is 0.4355; a substantial increase from the model with only statin use and age as predictors, which had an $R ^ { 2 }$ of 0.2852. The adjusted $R ^ { 2 }$ for the model is 0.4286, close to the $R ^ { 2 }$ value, which suggests that the additional predictors increase the strength of the model enough to justify the additional complexity.

---

7.6. REANALYZING THE PREVEND DATA

351

Figure 7.15 shows a plot of residuals vs predicted RFFT scores from the model in Figure 7.14 and a normal probability plot of the residuals. These plots show that the model fits the data reasonably well. The residuals show a slight increase in variability for larger predicted values, and the normal probability plot shows the residuals depart slightly from normality in the extreme tails. Model assumptions never hold exactly, and the possible violations shown in this figure are not sufficient reasons to discard the model.

![](../../raw/pages_0337-0352/images/page_350_image_3.jpg)

Figure 7.15: A histogram and normal probability plot of the residuals from the linear model for RFFT vs. statin use, age, educational level and presence of cardiovascular disease in the PREVEND data.

It is quite possible that even the model summarized in Figure 7.14 is not the best one to understand the association of cognitive ability with statin use. There be other confounders that are not accounted for. Possible predictors that may be confounders but have not been examined are called **residual confounders**. Residual confounders can be other variables in a dataset that have not been examined, or variables that were not measured in the study. Residual confounders exist in almost all observational studies, and represent one of the main reasons that observational studies should be interpreted with caution. A randomized experiment is the best way to eliminate residual confounders. Randomization ensures that, at least on average, all predictors are not associated with the randomized intervention, which eliminates one of the conditions for confounding. A randomized trial may be possible in some settings; there have been many randomized trials examining the effect of using statins. However, in many other settings, such as a study of the association of marijuana use and later addiction to controlled substances, randomization may not be possible or ethical. In those instances, observational studies may be the best available approach.

---

352

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.7 Interaction in regression

An important assumption in the multiple regression model

$$
y = \beta_ {0} + \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \dots + \beta_ {p} x _ {p} + \varepsilon
$$

is that when one of the predictor variables $x _ { j }$ changes by 1 unit and none of the other variables change, the predicted response changes by $\beta _ { j } ,$ regardless of the values of the other variables. A statistical **interaction** occurs when this assumption is not true, such that the relationship of one explanatory variable $x _ { j }$ with the response depends on the particular value(s) of one or more other explanatory variables.

Interaction is most easily demonstrated in a model with two predictors, where one of the predictors is categorical and the other is numerical.<sup>14</sup> Consider a model that might be used to predict total cholesterol level from age and diabetes status (either diabetic or non-diabetic):

$$
E (\text {TotChol}) = \beta_ {0} + \beta_ {1} (\text {Age}) + \beta_ {2} (\text {Diabetes}). \tag {7.8}
$$

Figure 7.16 shows the R output for a regression estimating model 7.8, using data from a sample of 500 adults from the NHANES dataset (nhanes.samp.adult.500). Total cholesterol (TotChol) is measured in mmol/L, Age is recorded in years, and Diabetes is a factor level with the levels No (non-diabetic) and Yes (diabetic) where 0 corresponds to No and 1 corresponds to Yes.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 4.8000 | 0.1561 | 30.75 | 0.0000 |
| Age | 0.0075 | 0.0030 | 2.47 | 0.0137 |
| DiabetesYes | -0.3177 | 0.1607 | -1.98 | 0.0487 |

Figure 7.16: Regression of total cholesterol on age and diabetes, using nhanes.samp.adult.500.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">14<sub>Interaction</sub> effects between numerical variables and between more than two variables can be complicated to interpret. A more complete treatment of interaction is best left to a more advanced course; this text will only examine interaction in the setting of models with one categorical variable and one numerical variable.</span></small>

---

7.7. INTERACTION IN REGRESSION

353

E

E

## EXAMPLE 7.9

Using the output in Figure 7.16, write the model equation and interpret the coefficients for age and diabetes. How does the predicted total cholesterol for a 60-year-old individual compare to that of a 50-year-old individual, if both have diabetes? What if both individuals do not have diabetes?

$$
\widehat {T o t C h o l} = 4. 8 0 + 0. 0 0 7 5 (A g e) - 0. 3 2 (D i a b e t e s Y e s)
$$

The coefficient for age indicates that with each increasing year of age, predicted total cholesterol increases by 0.0075 mmol/L. The coefficient for diabetes indicates that diabetics have an average total cholesterol that is 0.32 mmol/L lower than non-diabetic individuals.

If both individuals have diabetes, then the change in predicted total cholesterol level can be determined directly from the coefficient for Age. An increase in one year of age is associated with a 0.0075 increase in total cholesterol; thus, an increase in ten years of age is associated with $1 0 ( 0 . 0 0 7 5 ) = 0 . 0 7 5$ mmol/L increase in predicted total cholesterol.

The calculation does not differ if both individuals are non-diabetic. According to the model, the relationship between age and total cholesterol remains the same regardless of the values of the other variable in the model.

## EXAMPLE 7.10

Using the output in Figure 7.16, write two separate model equations: one for diabetic individuals and one for non-diabetic individuals. Compare the two models.

For non-diabetics (  Diabetes = 0), the linear relationship between average cholesterol and age is $\widehat{\mathrm{TotChol}}=4.80+0.0075(\mathrm{Age})-0.32(0)=4.80+0.0075(\mathrm{Age})$

For diabetics (  Diabetes = 1), the linear relationship between average cholesterol and age is $\mathrm{TotChol}=4.80+0.0075(\mathrm{Age})-0.32(1)=4.48+0.0075(\mathrm{Age}).$

The lines predicting average cholesterol as a function of age in diabetics and non-diabetics are parallel, with the same slope and different intercepts. While predicted total cholesterol is higher overall in non-diabetics (as indicated by the higher intercept), the rate of change in predicted average total cholesterol by age is the same for both diabetics and non-diabetics.

This relationship can be expressed directly from the model equation 7.8. For non-diabetics, the population regression line is $E(\mathrm{TotChol}) = \beta_{0} + \beta_{1}(\mathrm{Age})$ . For diabetics, the line is $E(\mathrm{Total}) =$ $\beta _ { 0 } + \beta _ { 1 } ( \mathrm { A g e } ) + \beta _ { 2 } = \beta _ { 0 } + \beta _ { 2 } + \beta _ { 1 } ( \mathrm { A g e } )$ . The lines have the same slope $\beta _ { 1 }$ but intercepts $\beta _ { 0 }$ and $\beta _ { 0 }   +   \beta _ { 2 }$

---

354

CHAPTER 7. MULTIPLE LINEAR REGRESSION

However, a model that assumes the relationship between cholesterol and age does not depend on diabetes status might be overly simple and potentially misleading. Figure 7.17(b) shows a scatterplot of total cholesterol versus age where the least squares models have been fit separately for non-diabetic and diabetic individuals. The blue line in the plot is estimated using only non-diabetic individuals, while the red line was fit using data from diabetic individuals. The lines are not parallel, and in fact, have slopes with different signs. The plot suggests that among non-diabetics, age is positively associated with total cholesterol. Among diabetics, however, age is negatively associated with total cholesterol.

![](../../raw/pages_0353-0368/images/page_353_chart_3.jpg)

<details>
<summary>scatter</summary>

| Series | Age (yrs) (range) | Total Cholesterol (mmol/L) (range) |
| --- | --- | --- |
| Blue | 20~80 | 3.0~9.5 |
| Red | 33~80 | 3.0~8.1 |
</details>

(a)

![](../../raw/pages_0353-0368/images/page_353_chart_5.jpg)

<details>
<summary>scatter</summary>

| Series | Age (yrs) (range) | Total Cholesterol (mmol/L) (range) |
| --- | --- | --- |
| Blue | 20~80 | 3.0~9.5 |
| Red | 30~80 | 3.0~8.1 |
</details>

(b)

Figure 7.17: Scatterplots of total cholesterol versus age in nhanes.samp.adult.500, where blue represents non-diabetics and red represents diabetics. Plot (a) shows the model equations written out in Example 7.10, estimated from the entire sample of 500 individuals. Plot (b) shows least squares models that are fit separately; coefficients of the blue line are estimated using only data from non-diabetics, while those of the red line are estimated using only data from diabetics.

---

7.7. INTERACTION IN REGRESSION

355

With the addition of another parameter (commonly referred to as an interaction term), a linear regression model can be extended to allow the relationship of one explanatory variable with the response to vary based on the values of other variables in the model. Consider the model

$$
E (\text {TotChol}) = \beta_ {0} + \beta_ {1} (\text {Age}) + \beta_ {2} (\text {Diabetes}) + \beta_ {3} (\text {Diabetes} \times \text {Age}). \tag {7.11}
$$

The interaction term allows the slope of the association with age to differ by diabetes status. Among non-diabetics (Diabetes = 0), the model reduces to the earlier one,

$$
E (\text {TotChol}) = \beta_ {0} + \beta_ {1} (\text {Age}).
$$

Among the diabetic participants, the model becomes

$$
\begin{array}{l} E (\text {TotChol}) = \beta_ {0} + \beta_ {1} (\text {Age}) + \beta_ {2} + \beta_ {3} (\text {Age}) \\ = \beta_ {0} + \beta_ {2} + (\beta_ {1} + \beta_ {3}) (\mathrm{Age}). \\ \end{array}
$$

Unlike in the original model, the slopes of the population regression lines for non-diabetics and diabetics are now different: $\beta _ { 1 }$ versus $\beta _ { 1 } + \beta _ { 3 }$

Figure 7.18 shows the R output for a regression estimating model 7.11. In R, the syntax Age:DiabetesYes represents the $( \mathrm { A g e } \times \mathrm { D i a b e t e s } )$ interaction term.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 4.6957 | 0.1597 | 29.40 | 0.0000 |
| Age | 0.0096 | 0.0031 | 3.10 | 0.0020 |
| DiabetesYes | 1.7187 | 0.7639 | 2.25 | 0.0249 |
| Age:DiabetesYes | -0.0335 | 0.0123 | -2.73 | 0.0067 |

Figure 7.18: Regression of total cholesterol on age and diabetes with an interaction term, using nhanes.samp.adult.500

## EXAMPLE 7.12

Using the output in Figure 7.18, write the overall model equation, the model equation for non-diabetics, and the model equation for diabetics.

The overall model equation is

$$
\widehat {\text {TotChol}} = 4. 7 0 + 0. 0 0 9 6 (\text {Age}) + 1. 7 2 (\text {DiabetesYes}) - 0. 0 3 4 (\text {Age} \times \text {DiabetesYes}).
$$

For non-diabetics (Diabetes = 0), the linear relationship between average cholesterol and age is

$$
\widehat {\text {TotChol}} = 4. 7 0 + 0. 0 0 9 6 (\text {Age}) + 1. 7 2 (0) - 0. 0 3 4 (\text {Age} \times 0) = 4. 7 0 + 0. 0 0 9 6 (\text {Age}).
$$

For diabetics (Diabetes = 1), the linear relationship between average cholesterol and age is

$$
\widehat {\text {TotChol}} = 4. 7 0 + 0. 0 0 9 6 (\text {Age}) + 1. 7 2 (1) - 0. 0 3 4 (\text {Age} \times 1) = 6. 4 2 - 0. 0 2 4 (\text {Age}).
$$

E

---

356

CHAPTER 7. MULTIPLE LINEAR REGRESSION

The estimated equations for non-diabetic and diabetic individuals show the same qualitative behavior seen in Figure 7.17(b), where the slope is positive in non-diabetics and negative in diabetics. However, note that the lines plotted in the figure were estimated from two separate model fits on non-diabetics and diabetics; in contrast, the equations from the interaction model are fit using data from all individuals.

It is more efficient to model the data using a single model with an interaction term than working with subsets of the data.<sup>15</sup> Additionally, using a single model allows for the calculation of a t-statistic and p-value that indicates whether there is statistical evidence of an interaction. The pvalue for the Age:Diabetes interaction term is significant at the $\alpha = 0 . 0 5$ level. Thus, the estimated model suggests there is strong evidence for an interaction between age and diabetes status when predicting total cholesterol.

Residual plots can be used to assess the quality of the model fit. Figure 7.19 shows that the residuals have roughly constant variance in the region with the majority of the data (predicted values between 4.9 and 5.4 mmol/L). However, there are more large positive residuals than large negative residuals, which suggests that the model tends to underpredict; i.e., predict values of TotChol that are smaller than the observed values.<sup>16</sup> Figure 7.20 shows that the residuals do not fit a normal distribution in the tails. In the right tails, the sample quantiles are larger than the theoretical quantiles, implying that there are too many large residuals. The left tail is a better fit; however, there are too few large negative residuals since the sample quantiles in the left tail are closer to 0 than the theoretical quantiles.

![](../../raw/pages_0353-0368/images/page_355_chart_5.jpg)

<details>
<summary>scatter</summary>

| Predicted Value (range) | Residual (range) |
| --- | --- |
| 4.5~5.6 | -2.3~4.3 |
</details>

Figure 7.19: A scatterplot of residuals versus predicted values in the model for total cholesterol that includes age, diabetes status, and the interaction of age and diabetes status.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">15<sub>In</sub> more complex settings, such as those with potential interaction between several variables or between two numerical variables, it may not be clear how to subset the data in a way that reveals interactions. This is another advantage to using an interaction term and single model fit to the entire dataset.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">16<sub>Recall</sub> that model residuals are calculated as yi − ŷi ; i.e., TotChol<sub>i</sub> − TotChol  i .</span></small>

---

7.7. INTERACTION IN REGRESSION

357

![](../../raw/pages_0353-0368/images/page_356_image_2.jpg)

Figure 7.20: A histogram of the residuals and a normal probability plot of the residuals from the linear model for total cholesterol versus age, diabetes status, and the interaction of age and diabetes status.

It is also important to note that the model explains very little of the observed variability in total cholesterol—the multiple $R ^ { 2 }$ of the model is 0.032. While the model falls well short of perfection, it may be reasonably adequate in applied settings. In the setting of a large study, such as one to examine factors affecting cholesterol levels in adults, a model like the one discussed here is typically a starting point for building a more refined model. Given these results, a research team might proceed by collecting more data. Regression models are commonly used as tools to work towards understanding a phenomenon, and rarely represent a ’final answer’.

There are some important general points that should not be overlooked when interpreting this model. The data cannot be used to infer causality; the data simply show associations between total cholesterol, age, and diabetes status. Each of the NHANES surveys are cross-sectional; they are administered to a sample of US residents with various ages and other demographic features during a relatively short period of time. No single individual has had his or her cholesterol levels measured over a period of many years, so the model slope for diabetes is not indicative of an individual’s cholesterol level declining (or increasing) with age.

Finally, the interpretation of a model often requires additional contextual information that is relevant to the study population but not captured in the dataset. What might explain increased age being associated with lower cholesterol for diabetics, but higher cholesterol for non-diabetics? The guidelines for the use of cholesterol-lowering statins suggest that these drugs should be prescribed more often in older individuals, and even more so in diabetic individuals. It is a reasonable speculation that the interaction between age and diabetes status seen in the NHANES data is a result of more frequent statin use in diabetic individuals.

---

358

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.8 Model selection for explanatory models

Previously, multiple regression modeling was shown in the context of estimating an association while adjusting for possible confounders. Another application of multiple regression is explanatory modeling, in which the goal is to construct a model that explains the observed variation in the response variable. In this context, there is no pre-specified primary predictor of interest; explanatory modeling is concerned with identifying predictors associated with the response. It is typically desirable to have a small model that avoids including variables which do not contribute much towards the $R ^ { 2 }$

The intended use of a regression model influences the way in which a model is selected. Ap proaches to model selection vary from those based on careful study of a relatively small set of predictors to purely algorithmic methods that screen a large set of predictors and choose a final model by optimizing a numerical criterion. Algorithmic selection methods have gained popularity as researchers have been able to collect larger datasets, but the choice of an algorithm and the optimization criterion require more advanced material and are not covered here. This section illustrates model selection in the context of a small set of potential predictors using only the tools and ideas that have been discussed earlier in this chapter and in Chapter $6 .$

Generally, model selection for explanatory modeling follows these steps:

1. Data exploration. Using numerical and graphical approaches, examine both the distributions of individual variables and the relationships between variables.
2. Initial model fitting. Fit an initial model with the predictors that seem most highly associated with the response variable, based on the data exploration.
3. Model comparison. Work towards a model that has the highest adjusted $R ^ { 2 }$

– Fit new models without predictors that were either not statistically significant or only marginally so and compare the adjusted $R ^ { 2 }$ between models; drop variables that decrease the adjusted $R ^ { 2 }$
– If the initial set of variables is relatively small, it is prudent to add variables not in the initial model and check the adjusted $R ^ { 2 } ;$ add variables that increase the adjusted $R ^ { 2 }$
– Examine whether interaction terms may improve the adjusted $R ^ { 2 }$

4. Model assessment. Use residual plots to assess the fit of the final model.

The process behind model selection will be illustrated with a case study in which a regression model is built to examine the association between the abundance of forest birds in a habitat patch and features of a patch.

---

7.8. MODEL SELECTION FOR EXPLANATORY MODELS

359

## Abundance of forest birds: introduction

Habitat fragmentation is the process by which a habitat in a large contiguous space is divided into smaller, isolated pieces; human activities such as agricultural development can result in habitat fragmentation. Smaller patches of habitat are only able to support limited populations of organisms, which reduces genetic diversity and overall population fitness. Ecologists study habitat fragmentation to understand its effect on species abundance. The forest.birds dataset in the oibiostat package contains a subset of the variables from a 1987 study analyzing the effect of habitat fragmentation on bird abundance in the Latrobe Valley of southeastern Victoria, Australia.<sup>17</sup>

The dataset consists of the following variables, measured for each of the 57 patches.

– abundance: average number of forest birds observed in the patch, as calculated from several independent 20-minute counting sessions.
– patch.area: patch area, measured in hectares. 1 hectare is 10,000 square meters and approximately 2.47 acres.
– dist.nearest: distance to the nearest patch, measured in kilometers.
– dist.larger: distance to the nearest patch larger than the current patch, measured in kilometers.
– altitude: patch altitude, measured in meters above sea level.
– grazing.intensity: extent of livestock grazing, recorded as either "light", "less than average", "average", "moderately heavy", or "heavy".
– year.of.isolation: year in which the patch became isolated due to habitat fragmentation.
– yrs.isolation: number of years since patch became isolated due to habitat fragmentation.<sup>18</sup>

The following analysis is similar to analyses that appear in Logan (2011)<sup>19</sup> and Quinn & Keough (2002).<sup>20</sup> In the approach here, the grazing intensity variable is treated as a categorical variable; Logan and Quinn & Keough treat grazing intensity as a numerical variable, with values 1-5 corresponding to the categories. The implications of these approaches are discussed at the end of the section.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">17<sub>Loyn</sub>, R.H. 1987. "Effects of patch area and habitat on bird abundances, species numbers and tree health in fragmented Victorian forests." Printed in Nature Conservation: The Role of Remnants of Native Vegetation. Saunders DA, Arnold GW, Burbridge AA, and Hopkins AJM eds. Surrey Beatty and Sons, Chipping Norton, NSW, 65-77, 1987.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">18<sub>The</sub> Loyn study completed data collection in 1983; yrs.isolation = 1983 − year.of.isolation.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">19<sub>Logan</sub>, M., 2011. Biostatistical design and analysis using R: a practical guide. John Wiley & Sons, Ch. 9.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">20<sub>Quinn</sub>, G.P. and Keough, M.J., 2002. Experimental design and data analysis for biologists. Cambridge University Press, Ch. 6.</span></small>

---

360

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## Data exploration

The response variable for the model is abundance. Numerical summaries calculated from software show that abundance ranges from 1.5 to 39.6. Figure 7.21 shows that the distribution of abundance is bimodal, with modes at small values of abundance and at between 25 and 30 birds. The median (21.0) and mean (19.5) are reasonably close, which confirms the distribution is near enough to symmetric to be used in the model without a transformation. The boxplot confirms that the distribution has no outliers.

![](../../raw/pages_0353-0368/images/page_359_chart_4.jpg)

<details>
<summary>histogram</summary>

| Bin (Abundance) | Frequency |
| --- | --- |
| 0~5 | 10 |
| 5~10 | 3 |
| 10~15 | 6 |
| 15~20 | 8 |
| 20~25 | 7 |
| 25~30 | 13 |
| 30~35 | 7 |
| 35~40 | 2 |
</details>

(a)

![](../../raw/pages_0353-0368/images/page_359_image_6.jpg)

![](../../raw/pages_0353-0368/images/page_359_image_7.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a box with a horizontal median line (no text or symbols)
</details>

(b)

Figure 7.21: A histogram (a) and boxplot (b) of abundance in the forest.birds data.

There are six potential predictors in the model; the variable year.of.isolation is only used to calculate the more informative variable yrs.isolation. The plots in Figure 7.22 reveal right skewing in patch.area, dist.nearest, dist.larger, and yrs.isolation; these might benefit from a log transformation. The variable altitude is reasonably symmetric, and the predictor grazing.factor is categorical and so does not take transformations. Figure 7.23 shows the distributions of log.patch.area, log.dist.nearest, log.dist.larger, and log.yrs.isolation, which were created through a natural log transformation of the original variables. All four are more nearly symmetric. These will be more suitable for inclusion in a model than the untransformed versions.

---

7.8. MODEL SELECTION FOR EXPLANATORY MODELS

361

![](../../raw/pages_0353-0368/images/page_360_image_2.jpg)

Figure 7.22: Histograms and a barplot for the potential predictors of abundance.

![](../../raw/pages_0353-0368/images/page_360_image_4.jpg)

Figure 7.23: Histograms of the log-transformed versions of patch.area, dist.nearest, dist.larger, and yrs.isolation.

---

362

CHAPTER 7. MULTIPLE LINEAR REGRESSION

A **scatterplot matrix** can be useful for visualizing the relationships between the predictor and response variables, as well as the relationships between predictors. Each subplot in the matrix is a simple scatterplot; all possible plots are shown, except for the plots of a variable versus itself. The variable names are listed along the diagonal of the matrix, and the diagonal divides the matrix into symmetric plots. For instance, the first plot in the first row shows abundance on the vertical axis and log.area on the horizontal axis; the first plot in the first column shows abundance on the horizontal axis and log.area on the vertical axis. Note that for readability, grazing.intensity appears with values 1 - 5, with 1 denoting "light" and 5 denoting "heavy" grazing intensity.

The plots in the first row of Figure 7.24 show the relationships between abundance and the predictors.<sup>21</sup> There is a strong positive association between abundance with log.area, and a strong negative association between abundance and log.yrs.isolation. The variables log.dist.near.patch and log.dist.larger seem weakly positively associated with abundance. There is high variance of abundance and somewhat similar centers for the first four categories, but abundance does clearly tend to be lower in the "high grazing" category versus the others.

![](../../raw/pages_0353-0368/images/page_361_chart_4.jpg)

<details>
<summary>scatter</summary>

| Variable | X-axis Range | Y-axis Range |
| :--- | :--- | :--- |
| abundance | -2~6 | -2~6 |
| log.area | -2~6 | -2~6 |
| log.dist.nearest | -2~6 | -2~6 |
| log.dist.larger | -2~6 | -2~8 |
| altitude | 100~200 | 100~250 |
| log.yrs.isolation | 1~5 | 1~4.5 |
| grazing.intensity | 0~30 | 0~5 |
</details>

Figure 7.24: Scatterplot matrix of abundance and the possible predictors: log.area, log.dist.near.patch, log.dist.larger.patch, altitude, log.yrs.isolation, and grazing.intensity.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">21<sub>Traditionally</sub>, the response variable (i.e., the dependent variable) is plotted on the vertical axis; as a result, it seems more natural to look at the first row where abundance is on the y-axis. It is equally valid, however, to assess the association of abundance with the predictors from the plots in the first column.</span></small>

---

7.8. MODEL SELECTION FOR EXPLANATORY MODELS

363

The variables log.dist.nearest and log.dist.larger appear strongly associated; a model may only need one of the two, as they may be essentially "redundant" in explaining the variabil ity in the response variable.<sup>22</sup> In this case, however, since both are only weakly associated with abundance, both may be unnecessary in a model.

A numerical approach confirms some of the features observable from the scatterplot matrix. Figure 7.25 shows the correlations between pairs of numerical variables in the dataset. Correlations between abundance and log.area and between abundance and log.yrs.isolation are relatively high, at 0.74 and -0.48, respectively. In contrast, the correlation between abundance and the two variables log.dist.nearest and log.dist.larger are much smaller, at 0.13 and 0.12. Additionally, the two potential predictors log.dist.nearest and log.dist.larger have a relatively high correlation of 0.60.

|  | abundance | log.area | log.dist.nearest | log.dist.larger | altitude | log.yrs.isolation |
| --- | --- | --- | --- | --- | --- | --- |
| abundance | 1.00 | 0.74 | 0.13 | 0.12 | 0.39 | -0.48 |
| log.area | 0.74 | 1.00 | 0.30 | 0.38 | 0.28 | -0.25 |
| log.dist.nearest | 0.13 | 0.30 | 1.00 | 0.60 | -0.22 | 0.02 |
| log.dist.larger | 0.12 | 0.38 | 0.60 | 1.00 | -0.27 | 0.15 |
| altitude | 0.39 | 0.28 | -0.22 | -0.27 | 1.00 | -0.29 |
| log.yrs.isolation | -0.48 | -0.25 | 0.02 | 0.15 | -0.29 | 1.00 |

Figure 7.25: A correlation matrix for the numerical variables in forest.birds.

## Initial model fitting

Based on the data exploration, the initial model should include the variables log.area, altitude, log.yrs.isolation, and grazing.intensity; a summary of this model is shown in Figure 7.26. The $R ^ { 2 }$ and adjusted $R ^ { 2 }$ for this model are, respectively, 0.728 and 0.688. The model explains about 73% of the variability in abundance.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 14.1509 | 6.3006 | 2.25 | 0.0293 |
| log.area | 3.1222 | 0.5648 | 5.53 | 0.0000 |
| altitude | 0.0080 | 0.0216 | 0.37 | 0.7126 |
| log.yrs.isolation | 0.1300 | 1.9193 | 0.07 | 0.9463 |
| grazing.intensityless than average | 0.2967 | 2.9921 | 0.10 | 0.9214 |
| grazing.intensityaverage | -0.1617 | 2.7535 | -0.06 | 0.9534 |
| grazing.intensitymoderately heavy | -1.5936 | 3.0350 | -0.53 | 0.6019 |
| grazing.intensityheavy | -11.7435 | 4.3370 | -2.71 | 0.0094 |

Figure 7.26: Initial model: regression of abundance on log.area, altitude, log.yrs.isolation and grazing.intensity.

Two of the variables in the model are not statistically significant at the $\alpha = 0 . 0 5$ level: altitude and log.yrs.isolation. Only one of the categories of grazing.intensity (heavy grazing) is highly significant.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">22<sub>Typically</sub>, the predictor that is less strongly correlated with the response variable is the one that is "redundant" and will be statistically insignificant when included in a model with the more strongly correlated predictor. This is not always the case, and depends on the other variables in the model.</span></small>

---

364

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## Model comparison

First, fit models excluding the predictors that were not statistically significant: altitude and log.yrs.isolation. Models excluding either variable have adjusted $R ^ { 2 }$ of 0.69, and a model excluding both variables has an adjusted $R ^ { 2 }$ of 0.70, a small but noticeable increase from the initial model. This suggests that these two variables can be dropped. At this point, the working model includes only log.area and grazing.intensity; this model has $R ^ { 2 } = 0 . 7 2 7$ and is shown in Figure 7.27.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 15.7164 | 2.7674 | 5.68 | 0.0000 |
| log.area | 3.1474 | 0.5451 | 5.77 | 0.0000 |
| grazing.intensityless than average | 0.3826 | 2.9123 | 0.13 | 0.8960 |
| grazing.intensityaverage | -0.1893 | 2.5498 | -0.07 | 0.9411 |
| grazing.intensitymoderately heavy | -1.5916 | 2.9762 | -0.53 | 0.5952 |
| grazing.intensityheavy | -11.8938 | 2.9311 | -4.06 | 0.0002 |

Figure 7.27: Working model: regression of abundance on log.area and grazing.intensity.

It is prudent to check whether the two distance-related variables that were initially excluded might increase the adjusted $R ^ { 2 }$ , even though this seems unlikely. When either or both of these variables are added, the adjusted $R ^ { 2 }$ decreases from 0.70 to 0.69. Thus, these variables are not added to the working model.

In this working model, only one of the coefficients associated with grazing intensity is statistically significant; when compared to the baseline grazing category (light grazing), heavy grazing is associated with a reduced predicted mean abundance of 11.9 birds (assuming that log.area is held constant). Individual categories of a categorical variable cannot be dropped, so a data analyst has the choice of leaving the variable as is, or collapsing the variable into fewer categories. For this model, it might be useful to collapse grazing intensity into a two-level variable, with one category corresponding to the original classification of heavy, and another category corresponding to the other four categories; i.e., creating a version of grazing intensity that only has the levels "heavy" and "not heavy". This is supported by the data exploration; a plot of abundance versus grazing.intensity shows that the centers of the distributions of abundance in the lowest four grazing intensity categories are roughly similar, relative to the center in the heavy grazing category. The model with the binary version of grazing intensity, grazing.binary, is shown in Figure 7.28. The model with grazing.binary has adjusted $R ^ { 2 } = 0 . 7 1$ , which is slightly larger than 0.70 in the more complex model with grazing.intensity; the model explains 72% of the variability in abundance $( R ^ { 2 } = 0 . 7 2 4 )$

Incorporating an interaction term did not improve the model; adding a parameter for the interaction between log.area and grazing.binary decreased the adjusted $R ^ { 2 }$ to 0.709. Thus, the model shown in Figure 7.28 is the final model.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 15.3736 | 1.4507 | 10.60 | 0.0000 |
| log.area | 3.1822 | 0.4523 | 7.04 | 0.0000 |
| grazing.binaryheavy | -11.5783 | 1.9862 | -5.83 | 0.0000 |

Figure 7.28: Final model: regression of abundance on log.area and grazing.binary.

---

7.8. MODEL SELECTION FOR EXPLANATORY MODELS

365

## Model assessment

The fit of a model can be assessed using various residual plots. Figure 7.29 shows a histogram and normal probability plot of the residuals for the final model. Both show that the residuals follow the shape of a normal density in the middle range (between -10 and 10) but fit less well in the tails. There are too many large positive and large negative values) residuals.

![](../../raw/pages_0353-0368/images/page_364_image_4.jpg)

Figure 7.29: Histogram and normal probability plot of residuals in the model for abundance with predictors log.area and grazing.binary.

Figure 7.30 gives a more detailed look at the residuals, plotting the residuals against predicted values and against the two predictors in the model, log.area and grazing.level. Recall that residual values closer to 0 are indicative of a more accurate prediction; positive values occur when the predicted value from the model is smaller than the observed value, and vice versa for negative values. Residuals are a measure of the prediction error of a model.

![](../../raw/pages_0353-0368/images/page_364_image_7.jpg)

Figure 7.30: Scatterplots of residuals versus predicted values and residuals versus log.area, and a side-by-side boxplot of residuals by grazing.binary. In the middle plot, red points correspond to values where grazing level is "heavy" and blue points correspond to "not heavy".

---

366

CHAPTER 7. MULTIPLE LINEAR REGRESSION

In the left plot, the large positive and large negative residuals visible from Figure 7.29 are evident; the large positive residuals occur across the range of predicted values, while the large negative residuals occur around 20 (predicted birds). The middle plot shows that the large positive and negative residuals occur at intermediate values of log.area; i.e., for values of log.area between 0 and 4, or equivalently for values of area between $\exp ( 0 )   =   1$ and $\exp ( 4 )   =   5 4 . 5$ hectares. In the same range, there are also relatively accurate predictions; most residuals are between -5 and 5. Both the middle plot and the right plot show that the prediction error is smaller for patches with heavy grazing than for patches where grazing intensity was between "light" and "moderately heavy". Patches with heavy grazing are represented with red points; note how the red points mostly cluster around the $y = 0$ line, with the exception of one outlier with a residual value of about 10.

## Conclusions

The relatively large $R ^ { 2 }$ for the final model (0.72) suggests that patch area and extent of grazing (either heavy or not) explain a large amount of the observed variability in bird abundance. Of the features measured in the study, these two are the most highly associated with bird abundance. Larger area is associated with an increase in abundance; when grazing intensity does not change, the model predicts an increase in average abundance by 3.18 birds for every one unit increase in log area (or equivalently, when area is increased by a factor of $\exp ( 1 ) = 2 . 7 )$ . A patch with heavy grazing is estimated to have a mean abundance of about 11.58 birds lower than a patch that has not been heavily grazed.

The residual plots imply that the final model may not be particularly accurate. For most observations, the predictions are accurate between ±5 birds, but there are several instances of overpredictions as high as around 10 and under-predictions of about 15. Additionally, the accurate and inaccurate predictions occur at similar ranges of of log.area; if the model only tended to be inaccurate at a specific range, such as for patches with low area, it would be possible to provide clearer advice about when the model is unreliable. The residuals plots do suggest that the model is more reliable for patches with heavy grazing, although there is a slight tendency towards overprediction.

Based on these results, the ecologists might decide to proceed by collecting more data. Currently, the model seems to adequately explain the variability in bird abundance for patches that have been heavily grazed, but perhaps there are additional variables that are associated with bird abundance, especially in patches that are not heavily grazed. Adding these variables might improve model residuals, in addition to raising $R ^ { 2 }$

## Final considerations

Might a model including all the predictor variables be better than the final model with only log.area and grazing.binary? The model is shown in Figure 7.31. The $R ^ { 2 }$ for this model is 0.729 and the adjusted $R ^ { 2 }$ is 0.676. While the $R ^ { 2 }$ is essentially the same as for the final model, the adjusted $R ^ { 2 }$ is noticeably lower. The residual plots in Figure 7.32 do not indicate that this model is an especially better fit, although the residuals are slightly closer to normality. There would be little gained from using the larger model.

In fact, there is an additional reason to avoid the larger model. When building regression models, it is important to consider that the complexity of a model is limited by sample size (i.e., the number of observations in the data). Attempting to estimate too many parameters from a small dataset can produce a model with unreliable estimates; the model may be ’overfit’, in the sense that it fits the data used to build it particularly well, but will fail to generalize to a new set of data. Methods for exploring these issues are covered in more advanced regression courses.

---

7.8. MODEL SELECTION FOR EXPLANATORY MODELS

367

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 10.8120 | 9.9985 | 1.08 | 0.2852 |
| log.area | 2.9720 | 0.6587 | 4.51 | 0.0000 |
| log.dist.near.patch | 0.1390 | 1.1937 | 0.12 | 0.9078 |
| log.dist.larger.patch | 0.3496 | 0.9301 | 0.38 | 0.7087 |
| altitude | 0.0117 | 0.0233 | 0.50 | 0.6169 |
| log.yrs.isolation | 0.2155 | 1.9635 | 0.11 | 0.9131 |
| grazing.intensityless than average | 0.5163 | 3.2631 | 0.16 | 0.8750 |
| grazing.intensityaverage | 0.1344 | 2.9870 | 0.04 | 0.9643 |
| grazing.intensitymoderately heavy | -1.2535 | 3.2000 | -0.39 | 0.6971 |
| grazing.intensityheavy | -12.0642 | 4.5657 | -2.64 | 0.0112 |

Figure 7.31: Full model: regression of abundance on all 6 predictors in forest.birds.

![](../../raw/pages_0353-0368/images/page_366_image_4.jpg)

Figure 7.32: Residual plots for the full model of abundance that includes all pre-dictors.

A general rule of thumb is to avoid fitting a model where there are fewer than 10 observations per parameter; e.g., to fit a model with 3 parameters, there should be at least 30 observations in the data. In a regression context, all of the following are considered parameters: an intercept term, a slope term for a numerical predictor, a slope term for each level of a categorical predictor, and an interaction term. In forest.birds, there are 56 cases, but fitting the full model involves estimating 10 parameters. The rule of thumb suggests that for these data, a model can safely support at most 5 parameters.

As mentioned earlier, other analyses of forest.birds have treated grazing.intensity as a nu merical variable with five values. One advantage to doing so is to produce a more stable model; only one slope parameter needs to be estimated, rather than four. However, treating grazing.intensity as a numerical variable requires assuming that any one unit change is associated with the same change in population mean abundance; under this assumption, a change between "light" and "less than average" (codes 1 to 2) is associated with the same change in population mean abundance as between "moderately heavy" to "heavy" (codes 4 to 5) grazing. Previous model fitting has shown that this assumption is not supported by the data, and that changes in mean abundance between adjacent levels in grazing intensity are not constant. In this text, it is our recommendation that categorical variables should not be treated as numerical variables.

---

368

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.9 The connection between ANOVA and regression

Regression with categorical variables and ANOVA are essentially the same method, but with some important differences in the information provided by the analysis. Earlier in this chapter, the strength of the association between RFFT scores and educational level was assessed with regression. Figure 7.33 shows the results of an ANOVA to analyze the difference in RFFT scores between education groups.

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| as.factor(Education) | 3 | 115040.88 | 38346.96 | 73.30 | 0.0000 |
| Residuals | 496 | 259469.32 | 523.12 |  |  |

Figure 7.33: Summary of ANOVA of RFFT by Education Levels

In this setting, the F-statistic is used to test the null hypothesis of no difference in mean RFFT score by educational level against the alternative that at least two of the means are different. The F-statistic is 73.3 and highly significant.

The F-statistic can also be calculated for regression models, although it has not been shown in the regression model summaries in this chapter. In regression, the F-statistic tests the null hypothesis that all regression coefficients are equal to 0 against the alternative that least one of the coefficients is not equal to 0.

Although the phrasing of the hypotheses in ANOVA versus regression may seem different initially, they are equivalent. Consider the regression model for predicting RFFT from educational level—each of the coefficients in the model is an estimate of the difference in mean RFFT for a particular education level versus the baseline category of Education = 0. A significant F-statistic indicates that at least one of the coefficients is not zero; i.e., that at least one of the mean levels of RFFT differs from the baseline category. If all the coefficients were to equal zero, then the differences between the means would be zero, implying all the mean RFFT levels are equal. It is reasonable, then, that the F-statistic associated with the RFFT versus Education regression model is also 73.3.

The assumptions behind the two approaches are identical. Both ANOVA and linear regression assume that the groups are independent, that the observations within each group are independent, that the response variable is approximately normally distributed, and that the standard deviations of the response are the same across the groups.

The regression approach provides estimates of the mean at the baseline category (the intercept) and the differences of the means between each category and the baseline, along with a tstatistic and p-value for each comparison. From regression output, it is easy to calculate all the estimated means; to do the same with ANOVA requires calculating summary statistics for each group. Additionally, diagnostic plots to check model assumptions are generally easily accessible in most computing software.

---

7.9. THE CONNECTION BETWEEN ANOVA AND REGRESSION

369

Why use ANOVA at all if fitting a linear regression model seems to provide more information? A case can be be made that the most important first step in analyzing the association between a response and a categorical variable is to compute and examine the F-statistic for evidence of any effect, and that only when the F-statistic is significant does it become appropriate to proceed to examine the nature of the differences. ANOVA displays the F-statistic prominently, emphasizing its importance. It is available in regression output, but may not always be easy to locate; the focus of regression is on the significance of the individual coefficients. ANOVA has traditionally been used in carefully designed experiments. There are complex versions of ANOVA that are appropriate for experiments in which several different factors are set at a range of levels. More complex versions of ANOVA are beyond the scope of this text and are covered in more advanced books.

Section 5.5 discussed the use of Bonferroni corrections when testing hypotheses about pairwise differences among the group means when conducting ANOVA. In principle, Bonferroni corrections can be applied in regression with categorical variables, but that is not often done. In designed experiments in which ANOVA has historically been used, the goal was typically to show definitively that a categorical predictor, often a treatment or intervention, was associated with a response variable so that the treatment could be adopted for clinical use. In experiments where the predictor can be manipulated by a scientist and cases are randomized to one of several levels of a predictor, the association can be interpreted as causal. It can be particularly important to control Type I error probabilities in those settings. Regression is often thought of as an exploratory technique, used in observational studies to discover associations that can be explored in further studies. Strict control of Type I error probabilities may be less critical in such settings.

At the introductory level, ANOVA is useful in that it provides more direct access to Type I error control and pairwise comparisons with t-tests. In practice, with the use of techniques not covered in this text, any analysis done via the ANOVA approach can also be approached with regression modeling.

---

370

CHAPTER 7. MULTIPLE LINEAR REGRESSION

## 7.10 Notes

This chapter and the previous chapter cover only the basic principles behind linear regression, and are meant to provide useful tools for getting started with data analysis. This section summarizes the most important ideas in the chapter and makes reference to some related topics that have not been discussed in detail.

## Important ideas

Keep a clear view of the purpose. Is the goal of constructing the model to understand the relationship between the response and a particular predictor after adjusting for confounders? Or is the goal to understand the joint association between a response and a set of predictors?

Avoid rushing into model fitting. Before fitting models, examine the data. Assess whether the response variable has an approximate normal distribution, or at least a symmetric distribution; a log transformation will often produce approximate normality. Examine the relationships between the response and predictors, as well as the relationships between predictors; check for nonlinear trends or outliers.

Remember the context of the problem. Context is important at each stage of a regression analysis. The best approach for constructing a model from a small number of potential predictors is based on considering the context of the problem and including predictors that have either been shown in the past to be associated with the response or for which there is a plausible working hypothesis about association with the response. When interpreting coefficients, consider whether the model results cohere with the underlying biological or medical context.

Critically examine residual plots. All models are approximations, so it is not necessary to be concerned about relatively minor violations of assumptions; residual plots are seldom as well behaved as those for the PREVEND data. In some cases, like with the California DDS data, residual plots show obvious major violations. With intermediate cases such as in the forest.birds plots, examine the plots closely and provide a detailed assessment of where the model seems less reliable.

---

7.10. NOTES

371

## Related topics

Stepwise model selection. Many introductory texts recommend using “stepwise” regression. Forward stepwise regression adds predictors one by one according to a set criterion (usually by smallest p-value). Backward stepwise regression eliminates variables one by one from a larger model until a criterion is met. Stepwise methods can be useful, and are usually automated in statistical software. However, there are weaknesses—the final models are data-dependent and chance alone can lead to spurious variables being included. In very large datasets, stepwise regression can lead to substantially incorrect models.

Prediction models. An application of regression not discussed in this chapter is predictive modeling, in which the goal is to construct a model that best predicts outcomes. The focus is on overall predictive accuracy; significance of individual coefficients is less important. Evaluating a model’s predictive accuracy involves advanced methods such as cross-validation, in which the original data sample is divided into a training set and a test set, similar to the approach used with the Golub leukemia data in Chapter 1. Prediction models are typically built from large datasets, using automated model selection procedures like stepwise regression.

Prediction intervals. Predicted values from regression have an inherent uncertainty because model parameters are only estimates. There are two types of interval estimates used with prediction: confidence intervals for a predicted mean response from a set of values for the predictors, and prediction intervals that show the variability in the predicted value for a new response (i.e., for a case not in the dataset) given a set of values for the predictor variables. Prediction intervals are wider than confidence intervals for a predicted mean because prediction intervals are subject to both the variability in a predicted mean response and the variability of an individual observation about its mean.

Controlling Type I error in regression. Control of Type I error probabilities becomes more critical in regression models with very large numbers of potential predictors. Datasets containing measurements on genetic data often contain large numbers of potential predictors for a response for many cases; a stricter significance level is used to maintain an overall error rate of $\alpha = 0 . 0 5$ . For example, in genome-wide association studies, the accepted "genome-wide significance $\mathbf { r a t e } ^ { \mathsf { n } }$ for an individual marker to be considered significantly associated with an outcome is $5 \times 1 0 ^ { - 8 }$

Because there are so many tools available in multiple regression, this chapter has a larger collection of labs than most other chapters. Lab 1 introduces the multiple regression model, illustrating one its most common uses—estimating an association between a response variable and predictor of interest while adjusting for possible confounding. Lab 2 discusses the residual plots used to check assumptions for multiple regression and introduces adjusted $R ^ { 2 }$ using the California DDS dataset initially introduced in Chapter 1.

Lab 3 explores how the association between a response variable and categorical predictors with more than two levels can be be estimated using multiple regression. This topic extends the earlier material in Chapter 6, Lab 4. Lab 4 introduces the concept of a statistical interaction using the NHANES dataset, examining whether the association between BMI and age among women is different than that among men.

Multiple regression is often used to examine associations between response variables and a small set of pre-specified predictors. It can also be used to explore and select models between a response variable and a set of candidate predictors. Lab 5 discusses explanatory modeling, in which the goal is to construct a model that effectively explains the observed variation in the response variable.

---

372

CHAPTER 7. MULTIPLE LINEAR REGRESSION

# 7.11 Exercises

## 7.11.1 Introduction to multiple linear regression

There are not currently exercises available for this section.

## 7.11.2 Simple versus multiple regression

**7.1 PREVEND, Part I.** The summary table below shows the results of a multiple regression model of RFFT score versus statin use and age.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 137.8822 | 5.1221 | 26.92 | 0.0000 |
| Statin | 0.8509 | 2.5957 | 0.33 | 0.7432 |
| Age | -1.2710 | 0.0943 | -13.48 | 0.0000 |

In a clinical setting, the interpretive focus lies on reporting the nature of the association between the primary predictor and the response, while specifying which potential confounders have been adjusted for. Briefly respond to a clinician who is concerned about a possible association between statin use and decreased cognitive function, based on the above analysis.

**7.2 PREVEND, Part II.** Can the results of the analysis in Exercise 7.1 be used to conclude that as one ages, one’s cognitive function (as measured by RFFT score) declines? Explain your answer.
**7.3 Baby weights, Part I.** The Child Health and Development Studies investigate a range of topics. One study considered all pregnancies between 1960 and 1967 among women in the Kaiser Foundation Health Plan in the San Francisco East Bay area. The variable smoke is coded 1 if the mother is a smoker, and 0 if not. The variable parity is 1 if the child is the first born, and 0 otherwise. The summary table below shows the results of a linear regression model for predicting the average birth weight of babies, measured in ounces, based on the smoking status of the mother and whether the child is the first born.<sup>23</sup>

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 123.57 | 0.72 | 172.75 | 0.0000 |
| smoke | -8.96 | 1.03 | -8.68 | 0.0000 |
| parity | -1.98 | 1.15 | -1.72 | 0.0859 |

(a) Write the equation of the regression model.
(b) Interpret the model slopes in the context of the data.
(c) Calculate the estimated difference in mean birth weight for two infants born to non-smoking mothers, if one is first born and the other is not.
(d) Calculate the estimated difference in mean birth weight for two infants born to mothers who are smokers, if one is first born and the other is not.
(e) Calculate the predicted mean birth weight for a first born baby born to a mother who is not a smoker.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">23<sub>Child</sub> Health and Development Studies, [Baby weights data set](http://www.ma.hw.ac.uk/~stan/aod/library).</span></small>

---

7.11. EXERCISES

373

**7.4 Wolbachia, Part I.** Wolbachia is a microbial symbiont estimated to be hosted by about 40% of all arthro pod species, transmitted primarily from females to their offspring through the eggs. Researchers conducted a study on a wasp species to understand the effect of Wolbachia on the lifetime reproductive success of an insect host. They estimated the realized lifetime reproductive success of female wasps by collecting them soon after they die naturally in the field, counting the number of eggs remaining in their ovaries and quantifying Wolbachia density in their body.

In the first stage of the experiment, researchers estimated potential reproductive success by collecting female wasps as they emerged from eggs then dissecting them to count the number of eggs in their ovaries. These data were used to create a predictive model for initial number of eggs based on tibia length (an indicator of body size) and Wolbachia density. Tibia length was measured in µm, and Wolbachia density in units of -ddCt.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | -18.82 | 27.26 | -0.69 | 0.497 |
| wolbachia | 1.77 | 1.07 | -1.65 | 0.111 |
| tibia | 0.357 | 0.15 | 2.38 | 0.0258 |

(a) Write the model equation.
(b) Interpret the model coefficients in the context of the data.
(c) Predict mean initial egg count for a wasp with tibia length of 171.4286 µm and Wolbachia density of -3.435 -ddCt.

## 7.11.3 Evaluating the fit of a multiple regression model

**7.5 Baby weights, Part III.** We considered the variables smoke and parity, one at a time, in modeling birth weights of babies in Exercise 7.3. A more realistic approach to modeling infant weights is to consider all possibly related variables at once. Other variables of interest include length of pregnancy in days (gestation), mother’s age in years (age), mother’s height in inches (height), and mother’s pregnancy weight in pounds (weight). Below are three observations from this data set.

|  | bwt | gestation | parity | age | height | weight | smoke |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 120 | 284 | 0 | 27 | 62 | 100 | 0 |
| 2 | 113 | 282 | 0 | 33 | 64 | 135 | 0 |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| 1236 | 117 | 297 | 0 | 38 | 65 | 129 | 0 |

The summary table below shows the results of a regression model for predicting the average birth weight of babies based on all of the variables included in the data set.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | -80.41 | 14.35 | -5.60 | 0.0000 |
| gestation | 0.44 | 0.03 | 15.26 | 0.0000 |
| parity | -3.33 | 1.13 | -2.95 | 0.0033 |
| age | -0.01 | 0.09 | -0.10 | 0.9170 |
| height | 1.15 | 0.21 | 5.63 | 0.0000 |
| weight | 0.05 | 0.03 | 1.99 | 0.0471 |
| smoke | -8.40 | 0.95 | -8.81 | 0.0000 |

(a) Write the equation of the regression model that includes all of the variables.
(b) Interpret the slopes of gestation and age in this context.
(c) The coefficient for parity is different than in the linear model shown in Exercise 7.3. Why might there be a difference?
(d) Calculate the residual for the first observation in the data set.
(e) The variance of the residuals is 249.28, and the variance of the birth weights of all babies in the data set is 332.57. Calculate the $R ^ { 2 }$ and the adjusted $R ^ { 2 }$ . Note that there are 1,236 observations in the data set.

---

374

CHAPTER 7. MULTIPLE LINEAR REGRESSION

**7.6 Absenteeism, Part I.** Researchers interested in the relationship between absenteeism from school and certain demographic characteristics of children collected data from 146 randomly sampled students in rural New South Wales, Australia, in a particular school year. Below are three observations from this data set.

|  | eth | sex | lrn | days |
| --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 1 | 2 |
| 2 | 0 | 1 | 1 | 11 |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| 146 | 1 | 0 | 0 | 37 |

The summary table below shows the results of a linear regression model for predicting the average number of days absent based on ethnic background (eth: 0 - aboriginal, 1 - not aboriginal), sex (sex: 0 - female, 1 - male), and learner status (lrn: 0 - average learner, 1 - slow l<sub>earner</sub>).24

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 18.93 | 2.57 | 7.37 | 0.0000 |
| eth | -9.11 | 2.60 | -3.51 | 0.0000 |
| sex | 3.10 | 2.64 | 1.18 | 0.2411 |
| lrn | 2.15 | 2.65 | 0.81 | 0.4177 |

(a) Write the equation of the regression model.
(b) Interpret each one of the slopes in this context.
(c) Calculate the residual for the first observation in the data set: a student who is aboriginal, male, a slow learner, and missed 2 days of school.
(d) The variance of the residuals is 240.57, and the variance of the number of absent days for all students in the data set is 264.17. Calculate the $R ^ { 2 }$ and the adjusted $R ^ { 2 }$ . Note that there are 146 observations in the data set.

24<sub>W</sub>. N. Venables and B. D. Ripley. Modern Applied Statistics with S. Fourth Edition. [Data can also be found in the R MASS package](http://www.stats.ox.ac.uk/pub/MASS4). New York: Springer, 2002.

---

7.11. EXERCISES

375

**7.7 Baby weights, Part VI.** Exercise 7.5 presents a regression model for predicting the average birth weight of babies based on length of gestation, parity, height, weight, and smoking status of the mother. Use the following plots to assess whether the assumptions for linear regression are reasonably met. Discuss your reasoning.

![](../../raw/pages_0369-0384/images/page_374_image_3.jpg)

---

376

CHAPTER 7. MULTIPLE LINEAR REGRESSION

**7.8 Toxemia and birth weight.** A model was fit for a random sample of 100 low birth weight infants born in two teaching hospitals in Boston, Massachusetts, regressing birthweight on the predictors gestational age and toxemia status. The condition toxemia, also known as preeclampsia, is characterized by high blood pressure and protein in urine by the $2 0 ^ { t h }$ week of pregnancy; left untreated, toxemia can be life-threatening. Birth weight was measured in grams and gestational age measured in weeks.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | -1286.200 | 234.918 | -5.475 | 0.0000 |
| toxemiaYes | -206.591 | 51.078 | -4.045 | 0.0001 |
| gestage | 84.048 | 8.251 | 10.188 | 0.0000 |

![](../../raw/pages_0369-0384/images/page_375_image_4.jpg)

(a) Write the model equation.
(b) Interpret the coefficients of the model, and comment on whether the intercept has a meaningful interpretation.
(c) Predict the average birth weight for an infant born to a mother diagnosed with toxemia with gestational age 31 weeks.
(d) Evaluate whether the assumptions for linear regression are reasonably satisfied.
(e) A simple regression model with only toxemia status as a predictor had $R ^ { 2 } = 0 . 0 0 0 1$ and $R _ { a d j } ^ { 2 } = 0 . 0 1 0 ;$ in this model, the slope estimate for toxemia status is 7.785, with $p = 0 . 9 0 7$ . The simple regression model and multiple regression model disagree regarding the nature of the association between birth weight and toxemia. Briefly explain a potential reason behind the discrepancy. Which model do you prefer for understanding the relationship between birth weight and toxemia, and why?

**7.9 Multiple regression fact checking.** Determine which of the following statements are true and false. For each statement that is false, explain why it is false.

(a) Suppose a numerical variable x has a coefficient of $b _ { 1 } = 2 . 5$ in the multiple regression model. Suppose also that the first observation has $x _ { 1 }   =   7 . 2 ,$ , the second observation has a value of $x _ { 1 }   =   8 . 2$ , and these two observations have the same values for all other predictors. Then the predicted value of the second observation will be 2.5 higher than the prediction of the first observation based on the multiple regression model.
(b) If a regression model’s first variable has a coefficient of $b _ { 1 } = 5 . 7 ,$ , then if we are able to influence the data so that an observation will have its $x _ { 1 }$ be 1 larger than it would otherwise, the value $y _ { 1 }$ for this observation would increase by 5.7.
(c) Suppose we fit a multiple regression model based on a data set of 472 observations. We also notice that the distribution of the residuals includes some skew but does not include any particularly extreme outliers. Because the residuals are not nearly normal, we should not use this model and require more advanced methods to model these data.

---

7.11. EXERCISES

377

## 7.11.4 The general multiple linear regression model

**7.10 Cherry trees.** Timber yield is approximately equal to the volume of a tree, however, this value is difficult to measure without first cutting the tree down. Instead, other variables, such as height and diameter, may be used to predict a tree’s volume and yield. Researchers wanting to understand the relationship between these variables for black cherry trees collected data from 31 such trees in the Allegheny National Forest, Pennsylvania. Height is measured in feet, diameter in inches (at 54 inches above ground), and volume in cubic feet.<sup>25</sup>

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | -57.99 | 8.64 | -6.71 | 0.00 |
| height | 0.34 | 0.13 | 2.61 | 0.01 |
| diameter | 4.71 | 0.26 | 17.82 | 0.00 |

(a) Calculate a 95% confidence interval for the coefficient of height, and interpret it in the context of the data.
(b) One tree in this sample is 79 feet tall, has a diameter of 11.3 inches, and is 24.2 cubic feet in volume. Determine if the model overestimates or underestimates the volume of this tree, and by how much.

**7.11 GPA.** A survey of 55 Duke University students asked about their GPA, number of hours they study at night, number of nights they go out, and their gender. Summary output of the regression model is shown below. Note that male is coded as 1.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 3.45 | 0.35 | 9.85 | 0.00 |
| studyweek | 0.00 | 0.00 | 0.27 | 0.79 |
| sleepnight | 0.01 | 0.05 | 0.11 | 0.91 |
| outnight | 0.05 | 0.05 | 1.01 | 0.32 |
| gender | -0.08 | 0.12 | -0.68 | 0.50 |

(a) Calculate a 95% confidence interval for the coefficient of gender in the model, and interpret it in the context of the data.
(b) Would you expect a 95% confidence interval for the slope of the remaining variables to include 0? Explain

**7.12 Trait inheritance of high blood pressure.** One research question of public health interest is to determine the extent to which high blood pressure is a genetic phenomenon. In 20 families, the systolic blood pressure of the mother, father, and first-born child in the family were measured (in units of mm Hg). A multi-ple linear regression model using $Y = \mathrm{c h i l d}' \mathrm{s}$ blood pressure, $X_{1} = \mathrm{mother's}$ blood pressure, and $X _ { 2 } = \mathrm { f a t h e r ^ { \prime } s }$ blood pressure led to the following estimate of a least squares line: $E ( Y ) = - 1 5 . 6 9 + 0 . 4 1 5 X _ { 1 } + 0 . 4 2 3 X _ { 2 }$ . The standard errors associated with $b _ { 0 } , b _ { 1 }$ , and $b _ { 2 } ,$ respectively, are 23.65, 0.125, and 0.119. The least squares fit produced $R ^ { 2 } = 0 . 5 9 7$ and $M S E = 1 1 3 . 8$

(a) What proportion of the variability of a child’s systolic blood pressure is explained by this model?
(b) Does the least squares line indicate statistically significant associations between each of the parent’s systolic blood pressures and that of the child? Explain your answer.
(c) What is the predicted systolic blood pressure for a child whose mother’s and father’s systolic blood pressure is 125 mm Hg and 140 mm Hg, respectively?
(d) A colleague tells you that something must be wrong with your model because your fitted intercept is negative, but blood pressures are never negative. How do you respond?
(e) Briefly describe three different plots for assessing the appropriateness or fit of the above regression model.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">25<sub>D</sub>.J. Hand. A handbook of small data sets. Chapman & Hall/CRC, 1994.</span></small>

---

378

CHAPTER 7. MULTIPLE LINEAR REGRESSION

**7.13 Wolbachia, Part II.** Exercise 7.4 introduced a study about Wolbachia and reproductive success in a wasp host. The following table shows the model coefficients for a model predicting the number of eggs laid over a lifetime from the predictor variables wolbachia density and tibia length. A higher number of eggs laid over a lifetime is indicative of greater reproductive success. The model has $R ^ { 2 } = 0 . 3 1 4$ and degrees of freedom 34. The F-statistic is 7.782, with p-value 0.0016.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | -17.88 | 28.63 | -0.62 | 0.537 |
| wolbachia | 4.28 | 1.25 | 3.42 | 0.002 |
| tibia | 0.272 | 0.16 | 1.69 | 0.010 |

(a) Write the model equation.
(b) Interpret the slope coefficient of wolbachia.
(c) Assess the evidence for whether Wolbachia is beneficial for its host in nature, based on these data.
(d) Compute and interpret a 95% confidence interval for the population slope of wolbachia.
(e) Interpret the significance of the F-statistic.

**7.14 Difficult encounters, Part I.** A study was conducted at a university outpatient primary care clinic in Switzerland to identify factors associated with difficult doctor-patient encounters. The data consist of 527 patient encounters, conducted by the 27 medical residents employed at the clinic. After each encounter, the attending physician completed two questionnaires: the Difficult Doctor Patient Relationship Questionnaire (DDPRQ-10) and the patient’s vulnerability grid (PVG).

A higher score on the DDPRQ-10 indicates a more difficult encounter. The maximum possible score is 60 and encounters with score 30 and higher are considered difficult.

A model was fit for the association of DDPRQ-10 score with features of the attending physician: age, sex, and years of training. The model has F-statistic of 0.23 on 3 and 286 degrees of freedom, with p-value 0.876.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 30.594 | 2.886 | 10.601 | 0.0000 |
| age | -0.016 | 0.104 | -0.157 | 0.876 |
| sexM | -0.535 | 0.781 | -0.686 | 0.494 |
| yrs.train | 0.096 | 0.215 | 0.445 | 0.656 |

(a) As a group, are these physician features useful for predicting DDPRQ-10 score?
(b) Is there evidence of a significant association between DDPRQ-10 score and any of the physician features?

---

7.11. EXERCISES

379

## 7.11.5 Categorical predictors with several levels

## 7.15 Prison isolation experiment, Part III.

Exercises 5.35 and 5.47 introduced an experiment conducted with the goal of identifying a treatment that reduces subjects’ psychopathic deviant T scores on the MMPI test. Exercise 5.35 evaluated the success of each individual treatment, and in exercise 5.47, ANOVA was used to compare the success of the three treatments. This exercise uses multiple regression to examine the intervention effect.

For this problem, a treatment variable (labeled treatment) has been constructed with three levels:

(1) Therapeutic for sensory restriction plus the 15 minute "therapeutic" tape advising that professional help is available.
(2) Neutral for sensory restriction plus a 15 minute "emotionally neutral" tap on training hunting dogs.
(3) Absent for sensory restriction but no taped message.

Forty-two subjects were randomly assigned to these treatment groups, and an MMPI test was administered before and after the treatment. Investigators hoped that the interventions would lower MMPI scores. The table below shows the result of a multiple regression in R where the response variable trt.effect is the change in MMPI score (pre-intervention - post-intervention) and the predictor variable is treatment.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | -3.2143 | 2.6174 | -1.23 | 0.2268 |
| treatmentNeutral | 6.0714 | 3.7015 | 1.64 | 0.1090 |
| treatmentTherapeutic | 9.4286 | 3.7015 | 2.55 | 0.0149 |

In this model, the residual standard error is 9.79, the F-statistic is 3.33 with 2 and 39 degrees of freedom; $P ( F _ { 2 , 3 9 } > 3 . 3 3 ) = 0 . 0 4 6 1$

(a) Interpret the meaning of a positive value for trt.effect versus a negative value.
(b) Write the estimated model equation.
(c) Calculate the predicted value for trt.effect for a patient in the neutral tape group.
(d) Does the intercept have a meaningful interpretation in this model?
(e) What is the interpretation of the two slope coefficients in the regression model?
(f) Describe the tested hypotheses that correspond to each of the p-values in the last column of the table.

**7.16 Poverty and educational level.** This question uses data from 500 randomly selected adults in the larger NHANES dataset. Poverty is measured as a ratio of family income to poverty guidelines. Smaller numbers indicate more poverty, and ratios of 5 or larger were recorded as 5. The Education variable indicates the highest level of education achieved: either 8th grade, 9 - 11th grade, high school, some college, or college grad.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 1.4555 | 0.2703 | 5.38 | 0.0000 |
| Education9 - 11th Grade | 0.9931 | 0.3302 | 3.01 | 0.0028 |
| EducationHigh School | 1.0900 | 0.3113 | 3.50 | 0.0005 |
| EducationSome College | 1.4943 | 0.2976 | 5.02 | 0.0000 |
| EducationCollege Grad | 2.4948 | 0.2958 | 8.43 | 0.0000 |

In this model, the residual standard error is 1.46, the F-statistic is 28.09 with 4 and 456 degrees of freedom; $P ( F _ { 4 , 4 5 6 } > 2 8 . 0 9 ) < 0 . 0 0 0 1$

(a) Write the estimated model equation.
(b) Calculate the predicted poverty ratio for an individual who at most completed high school.
(c) Interpret the estimated intercept value.
(d) Interpret the slope coefficient for EducationCollege Grad, and describe the tested hypotheses that correspond to the p-value for this slope coefficient.
(e) Assess whether educational level, overall, is associated with poverty. Be sure to include any relevant numerical evidence as part of your answer.

---

380

CHAPTER 7. MULTIPLE LINEAR REGRESSION

**7.17 Prison isolation experiment, Part IV.** Exercise 7.15 used regression to examine the effect of three interventions on prisoner MMPI scores. The response variable in the regression was trt.effect, the change in MMPI score (pre-intervention - post-intervention).

Instead of estimating the intervention effect through the change in scores, suppose one is interested in predicting a post-intervention score based on the pre-intervention score for an individual and a particular intervention.

(a) The table below shows an alternative regression model that can be fit to the data. In this model, the response variable is the post-intervention MMPI value (post, not shown explicitly in the table) and the predictors are the pre-intervention score (pre) and the treatment, coded as in problem 7.15.

Write the estimated equation for this model.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 28.4053 | 12.2949 | 2.31 | 0.0264 |
| pre | 0.6593 | 0.1628 | 4.05 | 0.0002 |
| treatmentNeutral | -5.7307 | 3.5545 | -1.61 | 0.1152 |
| treatmentTherapeutic | -9.7450 | 3.5540 | -2.74 | 0.0093 |

(b) In this model, describe in general terms the association of the pre-intervention and post-intervention scores.
(c) Does the pre-intervention score appear to be an important predictor of a post intervention score?
(d) What is the predicted post-intervention score for an individual with a pre-intervention score of 73 and receiving no tape after the isolation?
(e) Explain the interpretation of the coefficients for coefficient of treatmentNeutral. Is there strong statistical evidence that it is an important predictor?

**7.18 Resilience, Part I.** The American Psychological Association defines resilience as "the process of adapting well in the face of adversity, trauma, tragedy, threats, or even significant sources of stress". Studies have suggested that resilience is an important factor in contributing to how medical students perceive their qualit of life and educational environment.

Survey data were collected from 1,350 students across 25 medical schools. At each school, 54 students were randomly selected to participate in the study. Participants completed questionnaires measuring resilience, quality of life, perception of educational environment, depression symptoms, and anxiety symptoms.

The following regression model was fit to analyze the relationship between resilience and depressive symptoms. Resilience was categorized as: very low, low, moderately low, moderately high, high, and very high. Depressive symptoms were measured on a scale of 0 to 63 points, with higher scores indicating either more numerous or more severe depressive symptoms; this questionnaire is called the Beck Depression Inventory (BDI).

In this model, the residual standard error is 5.867, the F-statistic is 118.1 with 5 and 1344 degrees of freedom; $P ( F _ { 5 , 1 3 4 4 }   >   1 1 8 . 1 )   <   0 . 0 0 0 1$

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 4.9754 | 0.4118 | 12.08 | 0.0000 |
| resHigh | 2.2936 | 0.4987 | 4.60 | 0.0000 |
| resModHigh | 4.3005 | 0.5181 | 8.30 | 0.0000 |
| resModLow | 6.7108 | 0.5938 | 11.30 | 0.0000 |
| resLow | 9.6538 | 0.7458 | 12.94 | 0.0000 |
| resVeryLow | 15.6453 | 0.7518 | 20.81 | 0.0000 |

(a) Describe the overall trend in language accessible to someone who has not taken a statistics course.
(b) Does the intercept have a meaningful interpretation? Explain your answer.
(c) Compare the predicted mean BDI score for someone with low resilience to that of someone with very low resilience.
(d) + (e) **Continue to the next page for parts (d) and (e).**

---

7.11. EXERCISES

381

(d) Assess whether level of resilience, overall, is associated with depressive symptoms as measured by BDI score. Be sure to include any relevant numerical evidence as part of your answer.
(e) A model was fitted predicting BDI score from resilience, with the categories numerically coded from 1 to 6, with 1 being very high resilience and 6 being very low resilience. This model has a single slope estimate of 2.76 with p-value < 0.0001.

i. Using this model, compare the predicted mean BDI score for someone with low resilience to that of someone with very low resilience. Compare this answer to the one from part (c).
ii. What does this model imply about the change in mean BDI score between groups?
iii. Explain why this model is flawed.

## 7.11.6 Reanalyzing the PREVEND data

There are not currently exercises available for this section.

## 7.11.7 Interaction in regression

**7.19 Prison isolation experiment, Part V.** Exercise 7.17 used regression to predict a post-intervention score based on pre-intervention score and a particular intervention.

The following table shows a model incorporating interaction between pre-intervention score and intervention.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | -17.5790 | 17.7090 | -0.99 | 0.3275 |
| pre | 1.2813 | 0.2376 | 5.39 | 0.0000 |
| treatmentNeutral | 67.7518 | 30.6168 | 2.21 | 0.0333 |
| treatmentTherapeutic | 64.4183 | 24.2124 | 2.66 | 0.0116 |
| pre:treatmentNeutral | -0.9890 | 0.4082 | -2.42 | 0.0206 |
| pre:treatmentTherapeutic | -1.0080 | 0.3266 | -3.09 | 0.0039 |

(a) Write the model equation.
(b) Interpret the model coefficients.
(c) Write a separate model equation for each intervention group.
(d) Do these data suggest that there is a statistically significant difference in association between pre- and post-intervention scores by treatment group? Explain your answer.

**7.20 Vitamin D.** A study was conducted to evaluate Vitamin D status among schoolchildren in Thailand. Exposure to sunlight allows the body to produce serum 25(OH)D, which is a marker of Vitamin D status; serum level is measured in units of nmol/L and having serum level below 50 nmol/L is indicative of Vitamin D deficiency. The following model was fit to predict serum 25(OH)D level from age, sex, and their interaction.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 97.7709 | 4.7732 | 20.48 | 0.0000 |
| age | -3.0156 | 0.4774 | -6.32 | 0.0000 |
| sexM | -16.2848 | 7.0740 | -2.30 | 0.0217 |
| age:sexM | 2.9369 | 0.7054 | 4.16 | 0.0000 |

(a) Write the model equation.
(b) Interpret the model coefficients.
(c) Is there statistically significant evidence that the association between serum 25(OH)D level and age differs by sex? Explain your answer.

---

382

CHAPTER 7. MULTIPLE LINEAR REGRESSION

**7.21 PREVEND, Part III.** Exercise 7.1 showed a multiple regression model predicting RFFT score from statin use and age. For this problem, an interaction term is added between statin use and age.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 140.2031 | 5.6209 | 24.94 | 0.0000 |
| Statin | -13.9720 | 15.0113 | -0.93 | 0.3524 |
| Age | -1.3149 | 0.1040 | -12.65 | 0.0000 |
| Statin:Age | 0.2474 | 0.2468 | 1.00 | 0.3166 |

(a) Write the model equation.
(b) Interpret the model coefficients.
(c) Is there statistically significant evidence that the association between RFFT score and age differs by whether someone is a statin user? Explain your answer.

**7.22 Antibiotic consumption, Part I.** Antibiotic resistance represents a major public health challenge. Overuse of antibiotics in clinical settings is thought to be a major contributor to increased antibiotic resis tance. A study was conducted across several regions in China to investigate the impact of a 2011 law prohibiting over-the-counter (OTC) sales of antibiotics in private pharmacies. The study team collected data on average monthly antibiotic consumption in 621 counties, in addition to information on socioeconomic determinants such as percentage of population illiterate.

The following model was fit to investigate whether the relationship between monthly antibiotic consumption and percentage of population (over 25 years of age) with an advanced degree differs between counties that are located in a metropolitan area and those that are not.

|  | Estimate | Std. Error | t value | Pr(>\|t\|) |
| --- | --- | --- | --- | --- |
| (Intercept) | 0.8482 | 0.3311 | 2.56 | 0.0107 |
| metroYes | 2.3035 | 0.9612 | 2.40 | 0.0169 |
| edu | 0.5711 | 0.0319 | 17.90 | 0.0000 |
| metroYes:edu | -0.1838 | 0.0752 | -2.44 | 0.0148 |

(a) Interpret the model coefficients, including any relevant inferential results.
(b) Make a prediction of average monthly antibiotic consumption for a county in a metropolitan area where 10% of the population over 25 years old has an advanced degree.

## 7.11.8 Model selection for explanatory variables

**7.23 Baby weights, Part VII.** Suppose the starting point for model selection for the birth weight data were the full model, with all variables. The table below shows the adjusted $R ^ { 2 }$ for the full model as well as the adjusted $R ^ { 2 }$ values for all models with one fewer predictor variable. Based on examining the table from Exercise 7.5 and the following table, identify which variable, if any, should be removed from the model first. Explain your answer.

|  | Model | Adjusted $R^{2}$ |
| --- | --- | --- |
| 1 | Full model | 0.2541 |
| 2 | No gestation | 0.1031 |
| 3 | No parity | 0.2492 |
| 4 | No age | 0.2547 |
| 5 | No height | 0.2311 |
| 6 | No weight | 0.2536 |
| 7 | No smoking status | 0.2072 |

---

7.11. EXERCISES

383

**7.24 Absenteeism, Part II.** Suppose the starting point for model selection for the absenteeism data were the full model, with all variables. The table below shows the adjusted $R ^ { 2 }$ for the full model as well as the adjusted $R ^ { 2 }$ values for all models with one fewer predictor variable. Based on examining the table from Exercise 7.6 and the following table, identify which variable, if any, should be removed from the model first. Explain your answer.

|  | Model | Adjusted $R^{2}$ |
| --- | --- | --- |
| 1 | Full model | 0.0701 |
| 2 | No ethnicity | -0.0033 |
| 3 | No sex | 0.0676 |
| 4 | No learner status | 0.0723 |

**7.25 Baby weights, Part VIII.** Exercise 7.5 shows a regression model for predicting the average birth weight of babies based on all variables included in the dataset: length of pregnancy in days (gestation), mother’s age in years (age), mother’s height in inches (height), and mother’s pregnancy weight in pounds (weight).

The following plots show the relationships between the response and the numerical predictor variables, in addition to the relationships between the response and two categorical predictor variables.

![](../../raw/pages_0369-0384/images/page_382_chart_6.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 | IQR |
| --- | --- | --- | --- | --- |
| not first born | ~110 | ~121 | ~132 | ~22 |
| first born | ~107 | ~118 | ~128 | ~21 |
</details>

Birth Order

![](../../raw/pages_0369-0384/images/page_382_chart_8.jpg)

<details>
<summary>boxplot</summary>

| Category | Q1 | Q2 (Median) | Q3 | IQR |
| --- | --- | --- | --- | --- |
| nonsmoker | ~113 | ~123 | ~134 | ~21 |
| smoker | ~102 | ~115 | ~126 | ~24 |
</details>

Mother Smoking Status

![](../../raw/pages_0369-0384/images/page_382_image_10.jpg)

(a) Examine the relationship between the response variable and the predictor variables. Describe what you see. Which predictor variables seem like they would be useful to include in an initial model?
(b) Identify any predictors that seem related to each other.

---

384

CHAPTER 7. MULTIPLE LINEAR REGRESSION

**7.26 Antibiotic consumption, Part II.** Exercise 7.22 introduced a study conducted about antibiotic consumption in China. One aim of the study was to develop a prediction model for predicting monthly average antibiotic consumption based on county-level data. The following plots show the association between monthly average antibiotic consumption and four potential predictor variables: proportion female inhabitants (female), average life expectancy in years (lifeexp), proportion of population illiterate (illiterate), and population density in 1,000 people $/ \; k m ^ { 2 }$ (popdensity).

![](../../raw/pages_0369-0384/images/page_383_image_3.jpg)

(a) Summarize what you see.

(b) Identify any predictor variables that might benefit from a natural log transformation and briefly justify your choices.

---

7.11. EXERCISES

385

## 7.11.9 The connection between ANOVA and regression

**7.27 Prison isolation experiment, Part VI.** Problem 7.15 used a regression model to examine the effect of the interventions on possibly reducing psychopathic deviant T scores on prisoners. The regression model is shown in the problem statement.

(a) The value of the F-statistic is 3.33 with 2 and 39 degrees of freedom and $P ( F _ { 2 , 3 9 } > 3 . 3 3 ) = 0 . 0 4 6 1$ . In terms of the variables in the regression model, state the null hypothesis that corresponds to the F-statistic.
(b) Describe the relationship between the coefficients from the linear model and the usual summary statistics for the three sets of difference scores.
(c) Explain why the null hypothesis in this regression model is equivalent to the null hypothesis when these data were analyzed using ANOVA in Problem 5.47.
(d) Explain whether the assumptions for this regression model differ from those used in ANOVA.

**7.28 Resilience, Part II.** Exercise 7.18 shows a regression model for the association of BDI score with resilience level.

(a) In terms of the variables in the regression model, state the null hypothesis that corresponds to the Fstatistic.
(b) Describe the relationship between the coefficients from the linear model and the usual summary statistics for the six sets of BDI scores.
(c) Explain why the null hypothesis used in this regression model is equivalent to the null hypothesis that would be used if these data were analyzed with an ANOVA approach.
