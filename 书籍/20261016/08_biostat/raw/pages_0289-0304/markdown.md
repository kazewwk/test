**5.47 Prison isolation experiment, Part II.** Exercise 5.35 introduced an experiment that was conducted with the goal of identifying a treatment that reduces subjects’ psychopathic deviant T scores, where this score measures a person’s need for control or his rebellion against control. In Exercise 5.35 you evaluated the success of each treatment individually. An alternative analysis involves comparing the success of treatments. The relevant ANOVA output is given below.

|  | Df | Sum Sq | Mean Sq | F value | Pr(>F) |
| --- | --- | --- | --- | --- | --- |
| treatment | 2 | 639.48 | 319.74 | 3.33 | 0.0461 |
| Residuals | 39 | 3740.43 | 95.91 |  |  |

$$
s _ {p o o l e d} = 9. 7 9 3 \text {on} d f = 3 9
$$

(a) What are the hypotheses?
(b) What is the conclusion of the test? Use a 5% significance level.
(c) If in part (b) you determined that the test is significant, conduct pairwise tests to determine which groups are different from each other. If you did not reject the null hypothesis in part (b), recheck your answer.

**5.48 True / False: ANOVA, Part II.** Determine if the following statements are true or false, and explain your reasoning for statements you identify as false.

If the null hypothesis that the means of four groups are all the same is rejected using ANOVA at a 5% significance level, then ...

(a) we can then conclude that all the means are different from one another.
(b) the standardized variability between groups is higher than the standardized variability within groups.
(c) the pairwise analysis will identify at least one pair of means that are significantly different.
(d) the appropriate α to be used in pairwise comparisons is 0.05 / 4 = 0.0125 since there are four groups.

# Chapter 6

## Simple linear regression

**6.1 Examining scatterplots**
**6.2 Estimating a regression line using least squares**
**6.3 Interpreting a linear model**
**6.4 Statistical inference with regression**
**6.5 Interval estimates with regression**
**6.6 Notes**
**6.7 Exercises**

The relationship between two numerical variables can be visualized using a scatterplot in the xy-plane. The **predictor** or **explanatory variable** is plotted on the horizontal axis, while the **response variable** is plotted on the vertical axis.<sup>1</sup>

This chapter explores simple linear regression, a technique for estimating a straight line that best fits data on a scatterplot.<sup>2</sup> A line of best fit functions as a linear model that can not only be used for prediction, but also for inference. Linear regression should only be used with data that exhibit linear or approximately linear relationships.

For example, scatterplots in Chapter 1 illustrated the linear relationship be tween height and weight in the NHANES data, with height as a predictor of weight. Adding a best-fitting line to these data using regression techniques would allow for prediction of an individual’s weight based on their height. The linear model could also be used to investigate questions about the population-level relationship be tween height and weight, since the data are a random sample from the population of adults in the United States.

Not all relationships in data are linear. For example, the scatterplot in Fig ure 1.28 of Chapter 1 shows a highly non-linear relationship between between annual per capita income and life expectancy for 165 countries in 2011. Relationships are called **strong relationships** if the pattern of the dependence between the predictor and response variables is clear, even if it is nonlinear as in Figure 1.28. A **weak relationship** is one in which the points in the scatterplot are so diffuse as to make it difficult to discern any relationship. Figure 1.29 in Chapter 1 showed relationships progressing from weak to strong moving from left to right in the top and bottom panels. Each of the relationships shown in the second panels from the left are **moderate relationships**. Finally, changing the scale of measurement of one or both variables, such as changing age from age in years to age in months, simply stretches or compresses one or both axes and does not change the nature of the relationship. If a relationship is linear it will remain so, and with a simple change of scale, a nonlinear relationship will remain nonlinear.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Sometimes, the predictor variable is referred to as the independent variable, and the response variable referred to as the dependent variable.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Although the response variable in linear regression is necessarily numerical, the predictor variable can be numerical or categorical.</span></small>

The next chapter covers multiple regression, a statistical model used to estimate the relationship between a single numerical response variable and several predictor variables.

## 6.1 Examining scatterplots

Various demographic and cardiovascular risk factors were collected as a part of the Prevention of REnal and Vascular END-stage Disease (PREVEND) study, which took place in the Netherlands. The initial study population began as 8,592 participants aged 28-75 years who took a first survey in 1997-1998.<sup>3</sup> Participants were followed over time; 6,894 participants took a second survey in 2001-2003, and 5,862 completed the third survey in 2003-2006. In the third survey, measurement of cognitive function was added to the study protocol. Data from 4,095 individuals who completed cognitive testing are in the prevend dataset, available in the R package oibiostat.

As adults age, cognitive function changes over time, largely due to various cerebrovascular and neurodegenerative changes. It is thought that cognitive decline is a long-term process that may start as early as 45 years of age.<sup>4</sup> The Ruff Figural Fluency Test (RFFT) is one measure of cognitive function that provides information about cognitive abilities such as planning and the ability to switch between different tasks. The test consists of drawing as many unique designs as possible from a pattern of dots, under timed conditions; scores range from 0 to 175 points (worst and best score, respectively).

RFFT scores for a random sample of 500 individuals are shown in Figure 6.1, plotted against age at enrollment, which is measured in years. The variables Age and RFFT are negatively associated; older participants tend to have lower cognitive function. There is an approximately linear trend observable in the data, which suggests that adding a line could be useful for summarizing the relationship between the two variables.

It is important to avoid adding straight lines to non-linear data, such as in Figure 1.28.

![](images/page_292_chart_7.jpg)

<details>
<summary>scatter</summary>

| Age (yrs) | RFFT Score |
| --- | --- |
| ~36 | ~135 |
| ~37 | ~105 |
| ~38 | ~125 |
| ~40 | ~115 |
| ~42 | ~95 |
| ~45 | ~135 |
| ~48 | ~115 |
| ~50 | ~105 |
| ~52 | ~120 |
| ~55 | ~125 |
| ~58 | ~105 |
| ~60 | ~90 |
| ~62 | ~115 |
| ~65 | ~90 |
| ~68 | ~105 |
| ~70 | ~85 |
| ~72 | ~80 |
| ~75 | ~80 |
| ~78 | ~75 |
| ~80 | ~70 |
</details>

Figure 6.1: A scatterplot showing age vs. RFFT. Age is the predictor variable, while RFFT score is the response variable.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Participants were selected from the city of Groningen on the basis of their urinary albumin excretion; urinary albumin excretion is known to be associated with abnormalities in renal function.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4Joosten H, et al. Cardiovascular risk profile and cognitive function in young, middle-aged, and elderly subjects. Stroke. 2013;44:1543-1549, [https://doi.org/10.1161/STROKEAHA.111.000496](https://doi.org/10.1161/STROKEAHA.111.000496)</span></small>

The following conditions should be true in a scatterplot for a line to be considered a reasonable approximation to the relationship in the plot and for the application of the methods of inference discussed later in the chapter:

**1 Linearity.** The data shows a linear trend. If there is a nonlinear trend, an advanced regression method should be applied; such methods are not covered in this text. Occasionally, a transformation of the data will uncover a linear relationship in the transformed scale.
**2 Constant variability.** The variability of the response variable about the line remains roughly constant as the predictor variable changes.
**3 Independent observations.** The (x,y) pairs are independent; i.e., the value of one pair provides no information about other pairs. Be cautious about applying regression to sequential observations in time (**time series** data), such as height measurements taken over the course of several years. Time series data may have a complex underlying structure, and the relationship between the observations should be accounted for in a model.
**4 Residuals that are approximately normally distributed.** This condition can be checked only after a line has been fit to the data and will be explained in Section 6.3.1, where the term residual is defined. In large datasets, it is sufficient for the residuals to be approximately symmetric with only a few outliers. This condition becomes particularly important when inferences are made about the line, as discussed in Section 6.4.

![](images/page_293_image_8.jpg)

## GUIDED PRACTICE 6.1

Figure 6.2 shows the relationship between clutch.volume and body.size in the frog data. The plot also appears as Figure 1.26 in Chapter 1. Are the first three conditions met for linear regression?<sup>5</sup>

![](images/page_293_chart_11.jpg)

<details>
<summary>scatter</summary>

| Female Body Size (cm) | Clutch Volume \((mm^{3})\) |
| --- | --- |
| ~3.7 | ~250 |
| ~3.7 | ~280 |
| ~3.8 | ~180 |
| ~3.9 | ~250 |
| ~3.9 | ~300 |
| ~4.0 | ~350 |
| ~4.0 | ~400 |
| ~4.1 | ~400 |
| ~4.1 | ~550 |
| ~4.1 | ~750 |
| ~4.2 | ~350 |
| ~4.2 | ~550 |
| ~4.2 | ~600 |
| ~4.3 | ~300 |
| ~4.3 | ~400 |
| ~4.3 | ~600 |
| ~4.4 | ~300 |
| ~4.4 | ~350 |
| ~4.4 | ~600 |
| ~4.5 | ~500 |
| ~4.5 | ~600 |
| ~4.6 | ~450 |
| ~4.6 | ~500 |
| ~4.6 | ~650 |
| ~4.7 | ~450 |
| ~4.7 | ~600 |
| ~4.7 | ~1050 |
| ~4.8 | ~500 |
| ~4.8 | ~650 |
| ~4.8 | ~850 |
| ~4.9 | ~500 |
| ~4.9 | ~600 |
| ~4.9 | ~900 |
| ~5.0 | ~500 |
| ~5.0 | ~750 |
| ~5.0 | ~1150 |
| ~5.1 | ~500 |
| ~5.1 | ~650 |
| ~5.1 | ~850 |
| ~5.1 | ~1150 |
| ~5.2 | ~300 |
| ~5.2 | ~650 |
| ~5.2 | ~850 |
| ~5.2 | ~1150 |
| ~5.3 | ~800 |
| ~5.3 | ~900 |
| ~5.3 | ~1100 |
| ~5.3 | ~1650 |
| ~5.4 | ~750 |
| ~5.4 | ~950 |
| ~5.4 | ~1150 |
| ~5.4 | ~1300 |
| ~5.5 | ~950 |
| ~5.5 | ~1150 |
| ~5.5 | ~1300 |
| ~5.5 | ~1750 |
| ~5.6 | ~750 |
| ~5.6 | ~950 |
| ~5.6 | ~1150 |
| ~5.6 | ~1350 |
| ~5.6 | ~1650 |
| ~5.7 | ~300 |
| ~5.7 | ~650 |
| ~5.7 | ~850 |
| ~5.7 | ~1200 |
| ~5.7 | ~1400 |
| ~5.8 | ~350 |
| ~5.8 | ~650 |
| ~5.8 | ~850 |
| ~5.8 | ~1200 |
| ~5.9 | ~350 |
| ~5.9 | ~800 |
| ~5.9 | ~950 |
| ~6.0 | ~1250 |
| ~6.0 | ~1350 |
| ~6.0 | ~1450 |
| ~6.1 | ~1100 |
| ~6.1 | ~1300 |
| ~6.1 | ~1850 |
</details>

Figure 6.2: A plot of clutch.volume versus body.size in the frog data.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>No. While the relationship appears linear and it is reasonable to assume the observations are independent (based on information about the frogs given in Chapter 1), the variability in clutch.volume is noticeably less for smaller values of body.size than for larger values.</span></small>

## 6.2 Estimating a regression line using least squares

Figure 6.3 shows the scatterplot of age versus RFFT score, with the **least squares regression line** added to the plot; this line can also be referred to as a **linear model** for the data. An RFFT score can be predicted for a given age from the equation of the regression line:

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 5 5 - 1. 2 6 (\text {age}).
$$

The vertical distance between a point in the scatterplot and the predicted value on the regression line is the **residual** for the observation represented by the point; observations below the line have negative residuals, while observations above the line have positive residuals. The size of a residual is usually discussed in terms of its absolute value; for example, a residual of −13 is considered larger than a residual of 5.

For example, consider the predicted RFFT score for an individual of age 56. According to the linear model, this individual has a predicted score of $1 3 7 . 5 5 0 - 1 . 2 6 1 ( 5 6 ) = 6 6 . 9 3 4$ points. In the data, however, there is a participant of age 56 with an RFFT score of 72; their score is about 5 points higher than predicted by the model (this observation is shown on the plot with $\textbf { a } ^ { \prime \prime } \times \mathbf { \" } )$

![](images/page_294_chart_7.jpg)

<details>
<summary>scatter</summary>

| Series | Age (yrs) | RFFT Score |
| --- | --- | --- |
| Blue circles | 35~82 | 10~140 |
| Red crosses | ~40 | ~125 |
| Red crosses | ~56 | ~72 |
| Red triangles | ~77 | ~28 |
</details>

Figure 6.3: A scatterplot showing age (horizontal axis) vs. RFFT (vertical axis) with the regression line added to the plot. Three observations are marked in the figure; the one marked by a $\text{" }+ \text{" }$ has a large residual of about +38, the one marked by a $\text{" } \times  \text{" }$ has a small residual of about $+ 5 ,$ and the one marked by a $"  \triangle  \text{" }$ has a moderate residual of about -13. The vertical dotted lines extending from the observations to the regression line represent the residuals.

## RESIDUAL: DIFFERENCE BETWEEN OBSERVED AND EXPECTED

The residual of the $i ^ { t h }$ observation $( x _ { i } , y _ { i } )$ is the difference of the observed response $( y _ { i } )$ and the response predicted based on the model fit $\widehat { ( y _ { i } ) }$ :

$$
e _ {i} = y _ {i} - \widehat {y _ {i}}
$$

The value $\widehat { y _ { i } }$ is calculated by plugging $x _ { i }$ into the model equation.

The **least squares regression line** is the line which minimizes the sum of the squared residuals for all the points in the plot. Let $\hat { y _ { i } }$ be the predicted value for an observation with value $x _ { i }$ for the explanatory variable. The value $e _ { i } = y _ { i } - \hat { y _ { i } }$ is the residual for a data point $( x _ { i } , y _ { i } )$ in a scatterplot with n pairs of points. The least squares line is the line for which

$$
e _ {1} ^ {2} + e _ {2} ^ {2} + \dots + e _ {n} ^ {2} \tag {6.2}
$$

is smallest.

For a general population of ordered pairs $( x , y )$ , the **population regression model** is

$$
y = \beta_ {0} + \beta_ {1} x + \varepsilon .
$$

The term ε is a normally distributed ‘error term’ that has mean $0$ and standard deviation $\sigma .$ Since $E ( \varepsilon ) = 0 ,$ , the model can also be written

$$
E (Y | x) = \beta_ {0} + \beta_ {1} x,
$$

where the notation $E ( Y | x )$ denotes the expected value of $Y$ when the predictor variable has value $x . ^ { 6 }$ For the PREVEND data, the population regression line can be written as

$$
\mathrm{RFFT} = \beta_ {0} + \beta_ {1} (\mathrm{age}) + \varepsilon , \text {or as} E (\mathrm{RFFT} | \mathrm{age}) = \beta_ {0} + \beta_ {1} (\mathrm{age}).
$$

The term $\beta _ { 0 }$ is the vertical intercept for the line (often referred to simply as the intercept) and $\beta _ { 1 }$ is the slope. The notation $b _ { 0 }$ and $b _ { 1 }$ are used to represent the point estimates of the parameters $\beta _ { 0 }$ and $\beta _ { 1 }$ . The point estimates $b _ { 0 }$ and $b _ { 1 }$ are estimated from data; $\beta _ { 0 }$ and $\beta _ { 1 }$ are parameters from the population model for the regression line.

The regression line can be written as $\hat { y } = b _ { 0 } + b _ { 1 } ( x )$ , where $\hat { y }$ represents the predicted value of the response variable. The slope of the least squares line, $b _ { 1 }$ , is estimated by

$$
b _ {1} = \frac {s _ {y}}{s _ {x}} r, \tag {6.3}
$$

where $r$ is the correlation between the two variables, and $s _ { x }$ and $s _ { y }$ are the sample standard deviations of the explanatory and response variables, respectively. The intercept for the regression line is estimated by

$$
b _ {0} = \overline {{y}} - b _ {1} \overline {{x}}. \tag {6.4}
$$

Typically, regression lines are estimated using statistical software.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>The error term ε can be thought of as a population parameter for the residuals (e). While ε is a theoretical quantity that refers to the deviation between an observed value and E(Y |x), a residual is calculated as the deviation between an observed value and the prediction from the linear model.</span></small>

## EXAMPLE 6.5

From the summary statistics displayed in Figure 6.4 for prevend.samp, calculate the equation of the least-squares regression line for the PREVEND data.

$$
b _ {1} = \frac {s _ {y}}{s _ {x}} r = \frac {2 7 . 4 0}{1 1 . 6 0} (- 0. 5 3 4) = - 1. 2 6
$$

$$
b _ {0} = \overline {{y}} - b _ {1} \overline {{x}} = 6 8. 4 0 - (- 1. 2 6) (5 4. 8 2) = 1 3 7. 5 5.
$$

The results agree with the equation shown at the beginning of this section:

$$
\widehat {\mathrm{RFFT}} = 1 3 7. 5 5 - 1. 2 6 (\text {age}).
$$

|  | Age (yrs) | RFFT score |
| --- | --- | --- |
| mean | $\overline{x} = 54.82$ | $\overline{y} = 68.40$ |
| standard deviation | $s_x = 11.60$ | $s_y = 27.40$ |
|  |  | $r = -0.534$ |

Figure 6.4: Summary statistics for age and RFFT from prevend.samp.

## GUIDED PRACTICE 6.6

Figure 6.5 shows the relationship between height and weight in a sample from the NHANES dataset introduced in Chapter 1. Calculate the equation of the regression line given the summary statistics: $\overline { { x } } = 1 6 8 . 7 8 , \overline { { y } } = 8 3 . 8 3 , s _ { x } = 1 0 . 2 9 , s _ { y } = 2 1 . 0 4 , r = 0 . 4 1 0 . ^ { 7 }$

![](images/page_296_chart_12.jpg)

<details>
<summary>scatter</summary>

| Height (cm) | Weight (kg) |
| --- | --- |
| ~145 | ~40 |
| ~146 | ~55 |
| ~147 | ~60 |
| ~148 | ~85 |
| ~149 | ~105 |
| ~150 | ~120 |
| ~151 | ~110 |
| ~152 | ~70 |
| ~153 | ~65 |
| ~154 | ~75 |
| ~155 | ~80 |
| ~156 | ~90 |
| ~157 | ~100 |
| ~158 | ~135 |
| ~159 | ~115 |
| ~160 | ~105 |
| ~161 | ~145 |
| ~162 | ~190 |
| ~163 | ~140 |
| ~164 | ~120 |
| ~165 | ~135 |
| ~166 | ~125 |
| ~167 | ~140 |
| ~168 | ~130 |
| ~169 | ~120 |
| ~170 | ~135 |
| ~171 | ~125 |
| ~172 | ~130 |
| ~173 | ~140 |
| ~174 | ~155 |
| ~175 | ~145 |
| ~176 | ~130 |
| ~177 | ~120 |
| ~178 | ~130 |
| ~179 | ~125 |
| ~180 | ~135 |
| ~181 | ~140 |
| ~182 | ~130 |
| ~183 | ~125 |
| ~184 | ~120 |
| ~185 | ~220 |
| ~186 | ~120 |
| ~187 | ~120 |
| ~188 | ~120 |
| ~189 | ~85 |
| ~190 | ~75 |
| ~191 | ~80 |
| ~192 | ~75 |
</details>

Figure 6.5: A plot of Height versus Weight in nhanes.samp.adult.500, with a leastsquares regression line

## GUIDED PRACTICE 6.7

Predict the weight in pounds for an adult who is 5 feet, 11 inches tall. $1\  cm  = .3937$ in; $1 \mathrm { l b } =$ 0.454 kg.<sup>8</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>The equation of the line is weight  = −57.738+0.839(height), where height is in centimeters and weight is in kilograms. 8<sub>5</sub> feet, 11 inches equals 71/.3937 = 180.34 centimeters. From the regression equation, the predicted weight is −57.738+ 0.839(180.34) = 93.567 kilograms. In pounds, this weight is 93.567/0.454 = 206.280.</span></small>

## 6.3 Interpreting a linear model

A least squares regression line functions as a statistical model that can be used to estimate the relationship between an explanatory and response variable. While the calculations for constructing a regression line are relatively simple, interpreting the linear model is not always straightforward. In addition to discussing the mathematical interpretation of model parameters, this section also addresses methods for assessing whether a linear model is an appropriate choice, interpreting categorical predictors, and identifying outliers.

The slope parameter of the regression line specifies how much the line rises (positive slope) or declines (negative slope) for one unit of change in the explanatory variable. In the PREVEND data, the line decreases by 1.26 points for every increase of 1 year. However, it is important to clarify that RFFT score tends to decrease as age increases, with average RFFT score decreasing by 1.26 points for each additional year of age. As visible from the scatter of the data around the line, the line does not perfectly predict RFFT score from age; if this were the case, all the data would fall exactly on the line.

When interpreting the slope parameter, it is also necessary to avoid phrasing indicative of a causal relationship, since the line describes an association from data collected in an observational study. From these data, it is not possible to conclude that increased age causes a decline in cognitive function.<sup>9</sup>

Mathematically, the intercept on the vertical axis is a predicted value on the line when the explanatory variable has value 0. In biological or medical examples, 0 is rarely a meaningful value of the explanatory variable. For example, in the PREVEND data, the linear model predicts a score of 137.55 when age is 0—however, it is nonsensical to predict an RFFT score for a newborn infant.

In fact, least squares lines should never be used to extrapolate values outside the range of observed values. Since the PREVEND data only includes participants between ages 36 and 81, it should not be used to predict RFFT scores for people outside that age range. The nature of a relationship may change for very small or very large values of the explanatory variable; for example, if participants between ages 15 and 25 were studied, a different relationship between age and RFFT scores might be observed. Even making predictions for values of the explanatory variable slightly larger than the minimum or slightly smaller than the maximum can be dangerous, since in many datasets, observations near the minimum or maximum values (of the explanatory variable) are sparse.

Linear models are useful tools for summarizing a relationship between two variables, but it is important to be cautious about making potentially misleading claims based on a regression line. The following subsection discusses two commonly used approaches for examining whether a linear model can reasonably be applied to a dataset.

## 6.3.1 Checking residuals from a linear model

Recall that there are four assumptions that must be met for a linear model to be considered reasonable: linearity, constant variability, independent observations, normally distributed residu als. In the PREVEND data, the relationship between RFFT score and age appears approximately linear, and it is reasonable to assume that the data points are independent. To check the assumptions of constant variability around the line and normality of the residuals, it is helpful to consult residual plots and normal probability plots (Section 3.3.7).<sup>10</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>Similarly, avoid language such as increased age leads to or produces lower RFFT scores.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10<sub>While</sub> simple arithmetic can be used to calculate the residuals, the size of most datasets makes hand calculations impractical. The plots here are based on calculations done in R.</span></small>

## Examining patterns in residuals

There are a variety of residual plots used to check the fit of a least squares line. The plots shown in this text are scatterplots in which the residuals are plotted on the vertical axis against predicted values from the model on the horizontal axis. Other residual plots may instead show values of the explanatory variable or the observed response variable on the horizontal axis. When a least squares line fits data very well, the residuals should scatter about the horizontal line $y = 0$ with no apparent pattern.

Figure 6.6 shows three residual plots from simulated data; the plots on the left show data plotted with the least squares regression line, and the plots on the right show residuals on the y axis and predicted values on the x-axis. A linear model is a particularly good fit for the data in the first row, where the residual plot shows random scatter above and below the horizontal line. In the second row, the original data cycles below and above the regression line; this nonlinear pattern is more evident in the residual plot. In the last row, the variability of the residuals is not constant; the residuals are slightly more variable for larger predicted values.

![](images/page_298_image_5.jpg)

Figure 6.6: Sample data with their best fitting lines (left) and their corresponding residual plots (right).

Figure 6.7 shows a residual plot from the estimated linear model $\widehat { \mathrm { R F F T } } = 1 3 7 . 5 5 - 1 . 2 6 ( \mathrm { a g e } )$ While the residuals show scatter around the line, there is less variability for lower predicted RFFT scores. A data analyst might still decide to use the linear model, with the knowledge that pre-dictions of high RFFT scores may not be as accurate as for lower scores. Reading a residual plot critically can reveal weaknesses about a linear model that should be taken into account when interpreting model results. More advanced regression methods beyond the scope of this text may be more suitable for these data.

![](images/page_299_chart_3.jpg)

<details>
<summary>scatter</summary>

| Series | Predicted RFFT Score (range) | Residuals (range) |
| --- | --- | --- |
| Blue circles | 35~92 | -65~60 |
| Red cross | ~40 | ~38 |
| Red cross | ~56 | ~5 |
| Red triangle | ~77 | ~-13 |
</details>

Figure 6.7: Residual plot for the model in Figure 6.3 using prevend.samp.

## EXAMPLE 6.8

Figure 6.8 shows a residual plot for the model predicting weight from height using the sample of 500 adults from the NHANES data, nhanes.samp.adult.500. Assess whether the constant variability assumption holds for the linear model.

The residuals above the line are more variable, taking on more extreme values than those below the line. Larger than expected residuals imply that there are many large weights that are underpredicted; in other words, the model is less accurate at predicting relatively large weights.

![](images/page_299_chart_8.jpg)

<details>
<summary>scatter</summary>

| Predicted Weight (range) | Residuals (range) |
| --- | --- |
| 65~108 | -30~125 |
</details>

Figure 6.8: A residual plot from the linear model for height versus weight in nhanes.samp.adult.500.

## Checking normality of the residuals

The normal probability plot, introduced in Section 3.3.7, is best suited for checking normality of the residuals, since normality can be difficult to assess using histograms alone. Figure 6.9 shows both the histogram and normal probability plot of the residuals after fitting a least squares regression to the age versus RFFT data.

![](images/page_300_image_4.jpg)

Figure 6.9: A histogram and normal probability plot of the residuals from the linear model for RFFT versus Age in prevend.samp.

The normal probability plot shows that the residuals are nearly normally distributed, with only slight deviations from normality in the left and right tails.

## GUIDED PRACTICE 6.9

Figure 6.10 shows a histogram and normal probability plot for the linear model to predict weight from height in nhanes.samp.adult.500. Evaluate the normality of the residuals.<sup>11</sup>

![](images/page_300_image_9.jpg)

Figure 6.10: A histogram and normal probability plot of the residuals from the linear model for height versus weight in nhanes.samp.adult.500.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11<sub>The</sub> data are roughly normal, but there are deviations from normality in the tails, particularly the upper tail. There are some relatively large observations, which is evident from the residual plot shown in Figure 6.8.</span></small>

## 6.3.2 Using $R ^ { 2 }$ to describe the strength of a fit

The correlation coefficient r measures the strength of the linear relationship between two variables. However, it is more common to measure the strength of a linear fit using $r ^ { 2 } ,$ which is commonly written as $R ^ { 2 }$ in the context of regression.<sup>12</sup>

The quantity $R ^ { 2 }$ describes the amount of variation in the response that is explained by the least squares line. While $R ^ { 2 }$ can be easily calculated by simply squaring the correlation coefficient, it is easier to understand the interpretation of $R ^ { 2 }$ by using an alternative formula:

$$
R ^ {2} = \frac {\text { variance   of   predicted   } y \text {-values}}{\text { variance   of   observed   } y \text {-values}}.
$$

It is possible to show that $R ^ { 2 }$ can also be written

$$
R ^ {2} = \frac {s _ {y} ^ {2} - s _ {\mathrm{residuals}} ^ {2}}{s _ {y} ^ {2}}.
$$

In the linear model predicting RFFT scores from age, the predicted values on the least squares line are the values of RFFT that are ’explained’ by the linear model. The variability of the residuals about the line represents the remaining variability after the prediction; i.e., the variability unexplained by the model. For example, if a linear model perfectly captured all the data, then the variance of the predicted y-values would be equal to the variance of the observed y-values, resulting in $R ^ { 2 } = 1$ . In the linear model for $\widehat { R F F T }$ , the proportion of variability explained is

$$
R ^ {2} = \frac {s _ {R F F T} ^ {2} - s _ {\mathrm{residuals}} ^ {2}}{s _ {R F F T} ^ {2}} = \frac {7 5 0 . 5 2 - 5 3 6 . 6 2}{7 5 0 . 5 2} = \frac {2 1 3 . 9 0}{7 5 0 . 5 2} = 0. 2 8 5,
$$

about 29%. This is equal to the square of the correlation coefficient, $r ^ { 2 } = - 0 . 5 3 4 ^ { 2 } = 0 . 2 8 5$

Since $R ^ { 2 }$ in simple linear regression is simply the square of the correlation coefficient between the predictor and the response, it does not add a new tool to regression. It becomes much more useful in models with several predictors, where it has the same interpretation as the proportion of variability explained by a model but is no longer the square of any one of the correlation coefficients between the individual responses and the predictor. Those models are discussed in Chapter 7.

## GUIDED PRACTICE 6.10

In the NHANES data, the variance of Weight is 442.53 $\mathrm { k g } ^ { 2 }$ and the variance of the residuals is 368.1. What proportion of the variability in the data is explained by the model?<sup>13</sup>

## GUIDED PRACTICE 6.11

If a linear model has a very strong negative relationship with a correlation of -0.97, how much of the variation in the response is explained by the explanatory variable?<sup>14</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12<sub>In</sub> software output, R<sup>2</sup>is usually labeled R-squared.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13About 16.8%: s2weight = 442.53−368.1 . 442.53 = 0.168 74 43 442.53</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">14<sub>About</sub> R<sup>2</sup> = (−0.97)<sup>2</sup> = 0.94 or 94% of the variation is explained by the linear model.</span></small>

## 6.3.3 Categorical predictors with two levels

Although the response variable in linear regression is necessarily numerical, the predictor variable may be either numerical or categorical. This section explores the association between a country’s infant mortality rate and whether or not 50% of the population has access to adequate sanitation facilities.

The World Development Indicators (WDI) is a database of country-level variables (i.e., indicators) recording outcomes for a variety of topics, including economics, health, mortality, fertility, and education.<sup>15</sup> The dataset wdi.2011 contains a subset of variables on 165 countries from the year $2 0 1 1 . ^ { 1 6 }$ The infant mortality rate in a country is recorded as the number of deaths in the first year of life per 1,000 live births. Access to sanitation is recorded as the percentage of the population with adequate disposal facilities for human waste. Due to the availability of death certificates, infant mortality is measured reasonably accurately throughout the world. However, it is more difficult to obtain precise measurements of the percentage of a population with access to adequate sanitation facilities; instead, considering whether half the population has such access may be a more reliable measure. The analysis presented here is based on 163 of the 165 countries; the values for access to sanitation are missing for New Zealand and Turkmenistan.

Figure 6.11(a) shows that infant mortality rates are highly right-skewed, with a relatively small number of countries having high infant mortality rates. In 13 countries, infant mortality rates are higher than 70 deaths per thousand live births. Figure 6.11(b) shows infant mortality after a log transformation; the following analysis will use the more nearly symmetric transformed version of inf.mortality.

![](images/page_302_chart_6.jpg)

<details>
<summary>histogram</summary>

| Infant Mortality (deaths/1,000 live births) | Frequency |
| --- | --- |
| 0~10 | ~55 |
| 10~20 | 30 |
| 20~30 | ~16 |
| 30~40 | ~14 |
| 40~50 | ~14 |
| 50~60 | ~11 |
| 60~70 | ~12 |
| 70~80 | ~7 |
| 80~90 | ~2 |
| 90~100 | ~2 |
| 100~110 | ~2 |
</details>

(a)

![](images/page_302_chart_8.jpg)

<details>
<summary>histogram</summary>

| Bin (log scale) | Frequency |
| --- | --- |
| 0.5~1.0 | ~7 |
| 1.0~1.5 | ~21 |
| 1.5~2.0 | ~16 |
| 2.0~2.5 | ~15 |
| 2.5~3.0 | ~26 |
| 3.0~3.5 | ~18 |
| 3.5~4.0 | ~33 |
| 4.0~4.5 | ~25 |
| 4.5~5.0 | ~4 |
</details>

(b)

Figure 6.11: (a) Histogram of infant mortality, measured in deaths per 1,000 live births in the first year of life. (b) Histogram of the log-transformed infant mortality.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">15<a href="http://data.worldbank.org/data-catalog/world-development-indicators"><sub>http</sub>://data.worldbank.org/data-catalog/world-development-indicators</a></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">16<sub>The</sub> data were collected by a Harvard undergraduate in the Statistics department, and are accessible via the oibiostat package.</span></small>

Figure 6.12 shows a scatterplot of log(inf.mortality) against the categorical variable for sanitation access, coded 1 if at least 50% of the population has access to adequate sanitation, and 0 otherwise. Since there are only two values of the predictor, the values of infant mortality are stacked above the two predictor values 0 and 1.17

![](images/page_303_chart_3.jpg)

<details>
<summary>scatter</summary>

| Access to Sanitation | log(Infant Mortality) (range) |
| --- | --- |
| 0 (low) | ~3.3 ~4.7 |
| 1 (high) | ~0.6 ~4.4 |
</details>

Figure 6.12: Country-level infant mortality rates, divided into low access $( x = 0 )$ and high access (x = 1) to sanitation. The least squares regression line is also shown.

The least squares regression line has the form

$$
\log (\text {inf. mortality}) = b _ {0} + b _ {1} (\text {sanit.access}). \tag {6.12}
$$

The estimated least squares regression line has intercept and slope parameters of 4.018 and -1.681, respectively. While the scatterplot appears unlike those for two numerical variables, the interpretation of the parameters remains unchanged. The slope, -1.681, is the estimated change in the logarithm of infant mortality when the categorical predictor changes from low access to sanitation facilities to high access. The intercept term 4.018 is the estimated log infant mortality for the set of countries where less than 50% of the population has access to adequate sanitation facilities (sanit.access = 0).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">17<sub>Typically</sub>, side-by-side boxplots are used to display the relationship between a numerical variable and a categorical variable. In a regression context, it can be useful to use a scatterplot instead, in order to see the variability around the regression line.</span></small>