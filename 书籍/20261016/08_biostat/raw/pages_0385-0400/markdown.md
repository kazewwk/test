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

# Chapter 8

## Inference for categorical data

**8.1 Inference for a single proportion**
**8.2 Inference for the difference of two proportions**
**8.3 Inference for two or more groups**
**8.4 Chi-square tests for the fit of a distribution**
**8.5 Outcome-based sampling: case-control studies**
**8.6 Notes**
**8.7 Exercises**

Previous chapters discussed methods of inference for numerical data; in this chapter, those methods are extended to categorical data, such as binomial proportions or data in two-way tables. While various details of the methods may change, such as the calculations for a test statistic or the distributions used to find a p-value, the core ideas and principles behind inference remain the same.

Categorical data arise frequently in medical research because disease outcomes and patient characteristics are often recorded in natural categories such as types of treatment received, whether or not disease advanced to a later stage, or whether or not a patient responded initially to a treatment. In the simplest settings, a binary outcome (yes/no, success/failure, etc) is recorded for a single group of participants, in hopes of learning more about the population from which the participants were drawn. The binomial distribution is often used for the statistical model in this setting, and inference about the binomial probability of success provides information about a population proportion p. In more complex settings, participant characteristics are recorded in a categorical variable with two or more levels, and the outcome or response variable itself has two or more levels. In these instances, data are usually summarized in two-way tables with two or more rows and two or more columns.

As with all methods of inference, it is important to understand how the data were collected and whether the data may be viewed as a random sample from a well-identified population, at least approximately. This issue is at least as important as the formulas for test statistics and confidence intervals, and is often overlooked.

Be careful about the notation in this chapter—since p is the standard notation for a population proportion and for a probability, p does double duty in this chapter as a population parameter and significance level.

![](images/page_386_image_5.jpg)

## 8.1 Inference for a single proportion

Advanced melanoma is an aggressive form of skin cancer that until recently was almost uniformly fatal. In rare instances, a patient’s melanoma stopped progressing or disappeared altogether when the patient’s immune system successfully mounted a response to the cancer. Those observations led to research into therapies that might trigger an immune response in cancer. Some of the most notable successes have been in melanoma, particularly with two new therapies, nivolumab and ipilimumab.<sup>1</sup>

A 2013 report in the New England Journal of Medicine by Wolchok et al. reported the results of a study in which patients were treated with both nivolumab and ipilimumab.<sup>2</sup> Fifty-three patients were given the new regimens concurrently, and the response to therapy could be evaluated in 52 of the 53. Of the 52 evaluable patients, 21 (40%) experienced a response according to commonly accepted criteria. In previous studies, the proportion of patients responding to one of these agents was 30% or less. How might one compare the new data to past results?

The data from this study are binomial data, with success defined as a response to therapy. Suppose the number of patients who respond in a study like this is represented by the random variable $X ,$ where X is binomial with parameters n (the number of trials, where each trial is rep resented by a patient) and $p$ (the unknown population proportion of response). From formulas discussed in Chapter 3, the mean of X is np and the standard deviation of $X$ is $\sqrt { n p ( 1 - p ) }$

Inference about $p$ is based on the sample proportion $\hat { p } ,$ where $\hat { p } = X / n$ . In this case, $\hat { p } = 2 1 / 5 2 =$ 0.404. If the sample proportion is nearly normally distributed, the normal approximation to the binomial distribution can be used to conduct inference; this method is commonly used. When X does not have an approximately normal distribution, exact inference can based on the binomial distribution for X. Both the normal approximation and exact methods are covered in this chapter.

## 8.1.1 Inference using the normal approximation

A **sample proportion** can be described as a sample mean. If each success in the melanoma data is represented as a 1 and each failure as a 0, then the sample proportion is the mean of the 52 numerical outcomes:

$$
\hat {p} = \frac {0 + 1 + 1 + \cdots + 0}{5 2} = 0. 4 0 4.
$$

The distribution of $\hat { p }$ is nearly normal when the distribution of successes and failures is not too strongly skewed.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>The -mab suffix in these therapies stands for monoclonal antibody, a therapeutic agent made by identical immune cells that are all clones of a unique parent cell from a patient.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2<sub>N</sub> Engl J Med 2013;369:122-33. DOI: 10.1056/NEJMoa1302369</span></small>

## CONDITIONS FOR THE SAMPLING DISTRIBUTION OF $\hat { p }$ BEING NEARLY NORMAL

The sampling distribution for ${ \hat { p } } ,$ calculated from a sample of size n from a population with a success proportion $p ,$ is nearly normal when

1. the sample observations are independent and
2. at least 10 successes and 10 failures are expected in the sample, i.e. $n p \geq 1 0$ and $n ( 1   -   p ) \geq$ 10. This is called the **success-failure condition**.

If these conditions are met, then the sampling distribution of $\hat { p }$ is approximately normal with mean $p$ and standard error

$$
S E _ {\hat {p}} = \sqrt {\frac {p (1 - p)}{n}}. \tag {8.1}
$$

When conducting inference, the population proportion $p$ is unknown. Thus, to construct a confidence interval, the sample proportion $\hat { p }$ can be substituted for $p$ to check the success-failure condition and compute the standard error. In a hypothesis test, $p _ { 0 }$ is substituted for $p .$

## Confidence intervals for a proportion

When using the normal approximation to the sampling distribution of $\hat { p } ,$ a confidence interval for a proportion has the same structure as a confidence interval for a mean; it is centered at the point estimate, with a margin of error calculated from the standard error and appropriate $z ^ { \star }$ value. The formula for a 95% confidence interval is

$$
\hat {p} \pm 1. 9 6 \sqrt {\frac {\hat {p} (1 - \hat {p})}{n}}.
$$

## EXAMPLE 8.2

Using the normal approximation, construct an approximate 95% confidence interval for the response probability for patients with advanced melanoma who were administered the combination of nivolumab and ipilimumab.

The independence and success-failure assumptions should be checked first. Since the outcome of one patient is unlikely to influence that of other patients, the observations are independent. The success-failure condition is satisfied since $n { \hat { p } } = ( 5 2 ) ( . 4 0 4 ) = 2 1 > 1 0$ and $n { \hat { p } } ( 1 - { \hat { p } } ) = ( 5 2 ) ( . 5 9 6 ) =$ $3 1 > 1 0$

The point estimate for the response probability, based on a sample of siz<u>e</u> $n = 5 2 ,$ , is $\hat { p } = 0 . 4 0 4$ <u>. For</u> a 95% confidence interval, $z ^ { \star } = 1 . 9 6$ . The standard error is estimated as: $\begin{array} { r } { \sqrt { \frac { \hat { p } \left( 1 - \hat { p } \right) } { n } } = \sqrt { \frac { \left( 0 . 4 0 4 \right) \left( 1 - 0 . 4 0 4 \right) } { 5 2 } } = } \end{array}$ 0.068. The confidence interval is

$$
0. 4 0 4 \pm 1. 9 6 (0. 0 6 8) \rightarrow (0. 2 7, 0. 5 4)
$$

The approximate 95% confidence interval for $p ,$ the population response probability of melanoma patients to the combination of these new drugs, is (0.27, 0.54) or (27%, 54%).

## GUIDED PRACTICE 8.3

In New York City on October 23rd, 2014, a doctor who had recently been treating Ebola patients in Guinea went to the hospital with a slight fever and was subsequently diagnosed with Ebola. Soon after, a survey conducted by the Marist Poll, an organization with a carefully designed methodology for drawing random samples from identified populations, found that 82% of New Yorkers favored a "mandatory 21-day quarantine for anyone who has come in contact with an Ebola patient."<sup>3</sup> a) Verify that the sampling distribution of $\hat { p }$ is nearly normal. b) Construct a 95% confidence interval for $p ,$ the proportion of New York adults who supported a quarantine for anyone who has come into contact with an Ebola patient.<sup>4</sup>

Did the participants in the melanoma trial constitute a random sample? Patients who participate in clinical trials are unlikely to be a random sample of patients with the disease under study since the patients or their physicians must be aware of the trial, and patients must be well enough to travel to a major medical center and be willing to receive an experimental therapy that may have serious side effects.

Investigators in the melanoma trial were aware that the observed proportion of patients responding in a clinical trial may be different than the hypothetical response probability in the population of patients with advanced melanoma. Study teams try to minimize these systematic differences by following strict specifications for deciding whether patients are eligible for a study. However, there is no guarantee that the results observed in a sample will be replicated in the general population.

Small, initial studies in which there is no control group, like the one described here, are early steps in exploring the value of a new therapy and are used to justify further study of a treatment when the results are substantially different than expected. The largest observed response rate in previous trials of 30% was close to the lower bound of the confidence interval from the study (27%, 54%), so the results were considered adequate justification for continued research on this treatment.

## Hypothesis testing for a proportion

Just as with inference for population means, confidence intervals for population proportions can be used when deciding whether to reject a null hypothesis. It is useful in most settings, however, to calculate the p-value for a test as a measure of the strength of the evidence contradicting the null hypothesis.

When using the normal approximation for the distribution of $\hat { p }$ to conduct a hypothesis test, one should always verify that $\hat { p }$ is nearly normal under $H _ { 0 }$ by checking the independence and success-failure conditions. Since a hypothesis test is based on the distribution of the test statistic under the null hypothesis, the success-failure condition is checked using the null proportion $p _ { 0 } ,$ not the estimate ${ \hat { p } } .$

According to the normal approximation to the binomial distribution, the number of successes in n trials is normally distributed with mean $n p _ { 0 }$ and standard deviation $\sqrt { n p ( 1 - p _ { 0 } ) }$ . This approximation is valid when $n p _ { 0 }$ and $n ( 1 - p _ { 0 } )$ are both at least $1 0 . ^ { 5 }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>[Poll ID NY141026 on maristpoll.marist.edu](http://www.openintro.org/redirect.php?go=textbook-maristpoll_ebola_201410&referrer=biostat1_pdf).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4<sub>a</sub>) The poll is based on a simple random sample and consists of fewer than 10% of the adult population of New York, which makes independence a reasonable assumption. The success-failure condition is satisfied since, 1042(0.82) > 5 and 1042(1 − 0.82) > 5. b) 0.82 ± 1.96<sup>q</sup> 0.82(1−0.82)1042 → (0.796,0.844).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>The normal approximation to the binomial distribution was discussed in Section 3.2 of Chapter 3.</span></small>

Under the null hypothesis, the sample proportion $\hat { p } = X / n$ is approximately distributed as

$$
N \left(p _ {0}, \sqrt {\frac {p _ {0} (1 - p _ {0})}{n}}\right).
$$

The test statistic z for the null hypothesis $H _ { 0 } : p = p _ { 0 }$ based on a sample of size n is

$$
\begin{array}{l} z = \frac {\text { point   estimate - null   value }}{S E} \\ = \frac {\hat {p} - p _ {0}}{\sqrt {\frac {(p _ {0}) (1 - p _ {0})}{n}}}. \\ \end{array}
$$

## EXAMPLE 8.4

Suppose that out of a cohort of 120 patients with stage 1 lung cancer at the Dana-Farber Cancer Institute (DFCI) treated with a new surgical approach, 80 of the patients survive at least 5 years, and suppose that National Cancer Institute statistics indicate that the 5-year survival probability for stage 1 lung cancer patients nationally is 0.60. Do the data collected from 120 patients support the claim that the DFCI population treated with this new form of surgery has a different 5-year survival probability than the national population? Let $\alpha = 0 . 1 0 ,$ , since this is an early study of the new surgery.

Test the hypothesis $H _ { 0 } : p = 0 . 6 0$ versus the alternative, $H _ { A } : p \neq 0 . 6 0 ,$ , using $\alpha = 0 . 1 0 .$ . If we assume that the outcome of one patient at DFCI does not influence the outcome of other patients, the independence condition is met, and the success-failure condition is satisfied since $(120)(0.60)=$ $8 0 > 5$ and $(120)(1 - 0.60) = 40 > 5.$ The test statistic is the z-score of the point estimate:

$$
z = \frac {\text {point estimate - null value}}{S E} = \frac {0 . 6 7 - 0 . 6 0}{\sqrt {\frac {(0 . 6 0) (1 - 0 . 6 0)}{1 2 0}}} = 1. 5 7.
$$

The p-value is the probability that a standard normal variable is larger than 1.57 or smaller than $-1.57,   P(|Z| > 1.57) = 0.12$ ; since the p-value is greater than 0.10, there is insufficient evidence to reject $H _ { 0 }$ in favor of $H _ { A }$ . There is not convincing evidence that the survival probability at DFCI differs from the national survival probability. Had a more traditional 0.05 significance level been used, the data would be even less convincing.

## EXAMPLE 8.5

Using the data from the study in advanced melanoma, use the normal approximation to the sampling distribution of $\hat { p }$ to test the null hypothesis that the response probability to the novel combined therapy is 30% against a one-sided alternative that the response proportion is greater than 30%. Let $\alpha = 0 . 1 0$

The test statistic has value

$$
z = (0. 4 0 4 - 0. 3 0) / \sqrt {(0 . 3 0) (0 . 7 0) / 5 2} = 1. 6 4.
$$

The one-sided p-value is $P(Z \geq 1.64) = 0.05;$ there is sufficient evidence to reject the null hypothesis at $\alpha   =   0 . 1 0 .$ . This is an example of where a two-sided test and a one-sided test yield different conclusions.

![](images/page_391_image_2.jpg)

## GUIDED PRACTICE 8.6

One of the questions on the National Health and Nutrition Examination Survey (introduced in Chapter 5) asked participants whether they participated in moderate or vigorous intensity sports, fitness, or recreational activities. In a random sample of 135 adults, 76 answered "Yes" to the question. Based on this evidence, are a majority of American adults physically active?<sup>6</sup>

## 8.1.2 Inference using exact methods

When the normal approximation to the distribution of pˆ may not be accurate, inference is based on exact binomial probabilities. Calculating confidence intervals and p-values based on the binomial distribution can be done by hand, with tables of the binomial distribution, or (more easily and accurately) with statistical software. The logic behind computing a p-value is discussed here, but the formulas for a confidence interval are complicated and are not shown.

The p-value for a hypothesis test corresponds to the sum of the probabilities of all events that are as or more extreme than the sample result. Let X be a binomial random variable with parameters n and $p _ { 0 } ,$ where $\hat { p } = x / n$ and x is the observed number of events. If $\hat { p } \leq p _ { 0 } ,$ , then the one-tail probability equals $P ( X \leq x ) ; { \mathrm { ~ i f ~ } } { \hat { p } } > p _ { 0 } ,$ , then the one-tail probability equals $P ( X \geq x )$ . These probabilities are calculated using the approaches from Chapter 3. Two-tailed probabilities are calculated by doubling the appropriate one-tailed value.

## EXAMPLE 8.7

In 2009, the FDA Oncology Drug Advisory Committee (ODAC) recommended that the drug Avastin be approved for use in glioblastoma, a form of brain cancer. Tumor shrinkage after taking a drug is called a response; out of 85 patients, 24 exhibited a response. Historically, response probabilities for brain cancer drugs were approximately 0.05, or about 5%. Assess whether there is evidence that the response probability for Avastin is different from previous drugs.

$$
H _ {0}: p = 0. 0 5; H _ {A}: p \neq 0. 0 5. \text {Let} \alpha = 0. 0 5.
$$

The independence condition is satisfied, but the success-failure condition is not, since $n p _ { 0 } =$ $( 8 5 ) ( 0 . 0 5 )   =   4 . 2 5   <   5 ,$ so this is a setting where exact binomial probabilities should be used to calculate a $p -$ value.

The sample proportion $\hat { p }$ equals $x / n = 2 4 / 8 5 = 0 . 2 8 .$ . Since $\hat { p } \geq p _ { 0 }$ , calculate the two-sided p-value from $2 \times P ( X \geq 2 4 )$ , where X ∼ Binom(85,0.05).

Calculating the p-value is best done in software; the R command pbinom returns a value of 5.3486× $1 0 ^ { - 1 2 } .$ <sup>7</sup>

The p-value is highly significant and suggests that the response probability for Avastin is higher than for previous brain cancer drugs. The FDA staff considered this evidence sufficiently strong to justify approval for the use of the drug, even though the FDA normally requires evidence from two independently conducted randomized trials.

![](images/page_391_image_15.jpg)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>The observations are independent. Check success-failure: np<sub>0</sub> = n(1 − p<sub>0</sub>) = 135(0.5) > 10. H<sub>0</sub> : p = 0.5; H<sub>A</sub> : p > 0.5. 0.56−0.50 Calculate the z-score: z = = 1.39. The p-value is 0.08. Since the p-value is larger than 0.05, there is insufficient 0.5(1−0.5) 135</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">evidence to reject H<sub>0</sub>; there is not convincing evidence that a majority of Americans are physically active, although the data suggest that may be the case.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">7<sub>2</sub>\*pbinom(q = 23, size = 85, p = 0.05, lower.tail = FALSE)</span></small>

## GUIDED PRACTICE 8.8

Medical consultants assist patients with all aspects of an organ donation surgery, with the goal of reducing the possibility of complications during the medical procedure and recovery. To attract customers, one consultant noted that while the usual proportion of complications in liver donation surgeries in the United States is about 10%, only 3 out of her 62 clients experienced complications with liver donor surgeries. Is there evidence to suggest that the proportion of complications in her patients is lower than the national average?

## 8.1.3 Choosing a sample size when estimating a proportion

Whenever possible, a sample size for a study should be estimated before data collection be gins. Section 5.4 explored the calculation of sample sizes that allow a hypothesis test comparing two groups to have adequate power. When estimating a proportion, preliminary sample size calculations are often done to estimate a sample size large enough to make the **margin of error** m in a confidence interval sufficiently small for the interval to be useful. Recall that the margin of error m is the term that is added to and subtracted from the point estimate. Statistically, this means estimating a sample size n so that the sample proportion is within some margin of error m of the actual proportion with a certain level of confidence. When the normal approximation is used for a binomial proportion, a sample size sufficiently large to have a margin of error of m will satisfy

$$
m = (z ^ {\star}) (\mathrm{s.e.} (\hat {p})) = z ^ {\star} \sqrt {\frac {(p) (1 - p)}{n}}.
$$

Algebra can be used to show that the above equation implies

$$
n = \frac {(z ^ {\star}) ^ {2} (p) (1 - p)}{m ^ {2}}.
$$

In some settings a preliminary estimate for p can be used to calculate n. When no estimate is available, calculus can be used to show that $p ( 1 - p )$ has its largest value when $p = 0 . 5 0 ,$ , and that conservative value for $p$ is often used to ensure that n is sufficiently large regardless of the value of the unknown population proportion $p .$ In that case, n satisfies

$$
n \geq \frac {(z ^ {\star}) ^ {2} (0 . 5 0) (1 - 0 . 5 0)}{m ^ {2}} = \frac {(z ^ {\star}) ^ {2}}{4 m ^ {2}}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">8<sub>Assume</sub> that the 62 patients in her dataset may be viewed as a random sample from patients receiving a donated liver. The sample proportion pˆ = 3/62 = 0.048. Under the null hypothesis, the expected number of complications is 62(0.10) = 6.2, so the normal approximation may not be accurate and it is best to use exact binomial probabilities. Since pˆ ≤ p<sub>0</sub>, find the pvalue by calculating P (X ≤ 3) when X has a binomial distribution with parameters n = 62, p = 0.10: P (X ≤ 3) = 0.121. There is not sufficient evidence to suggest that the proportion of complications among her patients is lower than the national average.</span></small>

## EXAMPLE 8.9

Donor organs for organ transplant are scarce. Studies are conducted to explore whether the pop ulation of eligible organs can be expanded. Suppose a research team is studying the possibility of transplanting lungs from hepatitis C positive individuals; recipients can be treated with one of the new drugs that cures hepatitis C. Preliminary studies in organ transplant are often designed to estimate the probability of a successful organ graft 6 months after the transplant. How large should a study be so that the 95% confidence interval for the probability of a successful graft at 6 months is no wider than 20%?

A confidence interval no wider than 20% has a margin of error of 10%, or 0.10. Using the conservative value p = 0.50,

$$
n = \frac {(1 . 9 6) ^ {2}}{(4) (0 . 1 0 ^ {2})} = 9 6. 0 4.
$$

Sample sizes are always rounded up, so the study should have 97 patients.

Since the study will likely yield a value $\hat { p }$ different from 0.50, the final margin of error will be smaller than ±0.10.

When the confidence coefficient is 95%, 1.96 can replaced by 2 and the sample size formula reduces to

$$
n = 1 / m ^ {2}.
$$

This remarkably simple formula is often used by practitioners for a quick estimate of sample size.

## GUIDED PRACTICE 8.10

A 2015 estimate of Congress’ approval rating was 19%.<sup>9</sup> Using this estimate, how large should an additional survey be to produce a margin of error of 0.04 with 95% confidence?<sup>10</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>[www.gallup.com/poll/183128/five-months-gop-congress-approval-remains-low.aspx](http://www.openintro.org/redirect.php?go=textbook-congress_at_19_in_May2015&referrer=biostat1_pdf)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10<sub>Apply</sub> the formula</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p(1 − p) 0.19(1 − 0.19) 1.96 ×r ≈ 1.96 ×r ≤ 0.04 → n ≥ 369.5. n n</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">A sample size of 370 or more would be reasonable.</span></small>

## 8.2 Inference for the difference of two proportions

Just as inference can be done for the difference of two population means, conclusions can also be drawn about the difference of two population proportions: $p _ { 1 } - p _ { 2 }$

## 8.2.1 Sampling distribution of the difference of two proportions

The normal model can be applied to $\hat { p } _ { 1 } - \hat { p } _ { 2 }$ if the sampling distribution for each sample proportion is nearly normal and if the samples are independent random samples from the relevant populations.

## CONDITIONS FOR THE SAMPLING DISTRIBUTION OF $\hat { P } _ { 1 } - \hat { P } _ { 2 }$ TO BE APPROXIMATELY NORMAL

The difference $\hat { p } _ { 1 } - \hat { p } _ { 2 }$ tends to follow a normal model when

– each of the two samples are random samples from a population,
– the two samples are independent of each other, and
each sample proportion follows (approximately) a normal model. This condition is satisfied when $n _ { 1 } p _ { 1 } , n _ { 1 } \big ( 1 - p _ { 1 } \big ) , n _ { 2 } p _ { 2 }$ and $n _ { 2 } ( 1 - p _ { 2 } )$ are all $\geq 1 0$

The standard error of the difference in sample proportions is

$$
S E _ {\hat {p} _ {1} - \hat {p} _ {2}} = \sqrt {S E _ {\hat {p} _ {1}} ^ {2} + S E _ {\hat {p} _ {2}} ^ {2}} = \sqrt {\frac {p _ {1} (1 - p _ {1})}{n _ {1}} + \frac {p _ {2} (1 - p _ {2})}{n _ {2}}}, \tag {8.11}
$$

where $p _ { 1 }$ and $p _ { 2 }$ are the population proportions, and $n _ { 1 }$ and $n _ { 2 }$ are the two sample sizes.

## 8.2.2 Confidence intervals for $p _ { 1 } - p _ { 2 }$

When calculating confidence intervals for a difference of two proportions using the normal approximation to the binomial, the two sample proportions are used to verify the success-failure condition and to compute the standard error.

## EXAMPLE 8.12

The way a question is phrased can influence a person’s response. For example, Pew Research Center conducted a survey with the following question:<sup>11</sup>

As you may know, by 2014 nearly all Americans will be required to have health insurance. [People who do not buy insurance will pay a penalty] while [People who cannot afford it will receive financial help from the government]. Do you approve or disapprove of this policy?

For each randomly sampled respondent, the statements in brackets were randomized: either they were kept in the order given above, or the order of the two statements was reversed. Figure 8.1 shows the results of this experiment. Calculate and interpret a 90% confidence interval of the difference in the probability of approval of the policy.

First the conditions for the use of a normal model must be verified. The Pew Research Center uses sampling methods that produce random samples of the US population (at least approximately) and because each group was a simple random sample from less than 10% of the population, the observations are independent, both within the samples and between the samples. The success-failure condition also holds for each sample, so the normal model can be used for confidence intervals for the difference in approval proportions. The point estimate of the difference in support, where $\hat { p } _ { 1 }$ corresponds to the original ordering and $\hat { p } _ { 2 }$ to the reversed ordering:

$$
\hat {p} _ {1} - \hat {p} _ {2} = 0. 4 7 - 0. 3 4 = 0. 1 3.
$$

The standard error can be computed from Equation (8.11) using the sample proportions:

$$
S E \approx \sqrt {\frac {0 . 4 7 (1 - 0 . 4 7)}{7 7 1} + \frac {0 . 3 4 (1 - 0 . 3 4)}{7 3 2}} = 0. 0 2 5.
$$

For a 90% confidence interval, $z ^ { \star } = 1 . 6 5 ;$

$$
\text {point estimate} \pm z ^ {\star} \times S E \quad \rightarrow \quad 0. 1 3 \pm 1. 6 5 \times 0. 0 2 5 \quad \rightarrow \quad (0. 0 9, 0. 1 7).
$$

With 90% confidence, the proportion approving the 2010 health care law ranged between 9% and 17% depending on the phrasing of the question. The Pew Research Center interpreted this modestly large difference as an indication that for most of the public, opinions were still fluid on the health insurance mandate. The law eventually passed as the Affordable Health Care Act (ACA).

|  | Sample size ($n_i$) | Approve (%) | Disapprove (%) | Other |
| --- | --- | --- | --- | --- |
| Original ordering | 771 | 47 | 49 | 3 |
| Reversed ordering | 732 | 34 | 63 | 3 |

Figure 8.1: Results for a Pew Research Center poll where the ordering of two statements in a question regarding healthcare were randomized.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11<a href="http://www.openintro.org/redirect.php?go=textbook-health_care_bill_2012&amp;referrer=biostat1_pdf"><sub>www</sub>.people-press.org/2012/03/26/public-remains-split-on-health-care-bill-opposed-to-mandate</a>. Sample sizes for each polling group are approximate.</span></small>

## 8.2.3 Hypothesis testing for $p _ { 1 } - p _ { 2 }$

Hypothesis tests for $p _ { 1 }   -   p _ { 2 }$ are usually testing the null hypothesis of no difference between $p _ { 1 }$ and $p _ { 2 } ;$ i.e. $H _ { 0 } : p _ { 1 } - p _ { 2 } = 0$ <u>. Under the nul</u>l hypothesis, $\hat { p } _ { 1 }   -   \hat { p } _ { 2 }$ is normally distributed with mean 0 and standard deviation $\sqrt { p ( 1 - p ) ( \textstyle { \frac { 1 } { n _ { 1 } } } + { \frac { 1 } { n _ { 2 } } } ) }$ , where under the null hypothesis $p = p _ { 1 } = p _ { 2 }$

Since $p$ is unknown, an estimate is used to compute the standard error of $\hat { p } _ { 1 } - \hat { p } _ { 2 } ; \; p$ can be estimated by $\hat { p } ,$ the weighted average of the sample proportions $\hat { p } _ { 1 }$ and ${ \hat { p } } _ { 2 } ;$

$$
\hat {p} = \frac {n _ {1} \hat {p} _ {1} + n _ {2} \hat {p} _ {2}}{n _ {1} + n _ {2}} = \frac {x _ {1} + x _ {2}}{n _ {1} + n _ {2}},
$$

where $x _ { 1 }$ is the number of observed events in the first sample and $x _ { 2 }$ is the number of observed events in the second sample. This pooled proportion $\hat { p }$ is also used to check the success-failure condition.

The test statistic $z$ for testing $H _ { 0 } : p _ { 1 } = p _ { 2 }$ versus $H _ { A } : p _ { 1 } \neq p _ { 2 }$ equals:

$$
z = \frac {\hat {p} _ {1} - \hat {p} _ {2}}{\sqrt {\hat {p} (1 - \hat {p}) \left(\frac {1}{n _ {1}} + \frac {1}{n _ {2}}\right)}}.
$$

## EXAMPLE 8.13

The use of screening mammograms for breast cancer has been controversial for decades because the overall benefit on breast cancer mortality is uncertain. Several large randomized studies have been conducted in an attempt to estimate the effect of mammogram screening. A 30-year study to investigate the effectiveness of mammograms versus a standard non-mammogram breast cancer exam was conducted in Canada with 89,835 female participants.<sup>12</sup> During a 5-year screening period, each woman was randomized to either receive annual mammograms or standard physical exams for breast cancer. During the 25 years following the screening period, each woman was screened for breast cancer according to the standard of care at her health care center.

At the end of the 25 year follow-up period, 1,005 women died from breast cancer. The results by intervention are summarized in Figure 8.2.

Assess whether the normal model can be used to analyze the study results.

Since the participants were randomly assigned to each group, the groups can be treated as inde pendent, and it is reasonable to assume independence of patients within each group. Participants in randomized studies are rarely random samples from a population, but the investigators in the Canadian trial recruited participants using a general publicity campaign, by sending personal invitation letters to women identified from general population lists, and through contacting family doctors. In this study, the participants can reasonably be thought of as a random sample.

The pooled proportion $\hat { p }$ is

$$
\hat {p} = \frac {x _ {1} + x _ {2}}{n _ {1} + n _ {2}} = \frac {5 0 0 + 5 0 5}{5 0 0 + 4 4 , 4 2 5 + 5 0 5 + 4 4 , 4 0 5} = 0. 0 1 1 2.
$$

Checking the success-failure condition for each group:

$$
\hat {p} \times n _ {m g m} = 0. 0 1 1 2 \times 4 4, 9 2 5 = 5 0 3
$$

$$
(1 - \hat {p}) \times n _ {m g m} = 0. 9 8 8 8 \times 4 4, 9 2 5 = 4 4, 4 2 2
$$

$$
\hat {p} \times n _ {c t r l} = 0. 0 1 1 2 \times 4 4, 9 1 0 = 5 0 3
$$

$$
(1 - \hat {p}) \times n _ {c t r l} = 0. 9 8 8 8 \times 4 4, 9 1 0 = 4 4, 4 0 7
$$

All values are at least 10.

The normal model can be used to analyze the study results.

<table><tr><td rowspan="2"></td><td colspan="2">Death from breast cancer?</td></tr><tr><td>Yes</td><td>No</td></tr><tr><td>Mammogram</td><td>500</td><td>44,425</td></tr><tr><td>Control</td><td>505</td><td>44,405</td></tr></table>

Figure 8.2: Summary results for the mammogram study.

## EXAMPLE 8.14

Do the results from the study provide convincing evidence of a difference in the proportion of breast cancer deaths between women who had annual mammograms during the screening period versus women who received annual screening with physical exams?

The null hypothesis is that the probability of a breast cancer death is the same for the women in the two groups. If group 1 represents the mammogram group and group 2 the control group, $H _ { 0 } : p _ { 1 } = p _ { 2 }$ and $H _ { A } : p _ { 1 } \neq p _ { 2 }$ . Let $\alpha = 0 . 0 5$

Calculate the test statistic z:

$$
z = \frac {0 . 0 1 1 1 3 - 0 . 0 1 1 2 5}{\sqrt {(0 . 0 1 1 2) (1 - 0 . 0 1 1 2) \left(\frac {1}{4 4 , 9 2 5} + \frac {1}{4 4 , 9 1 0}\right)}} = - 0. 1 7.
$$

The two-sided p-value is $P | Z | \geq 0 . 1 7 = 0 . 8 6 5 0 ,$ , which is greater than 0.05. There is insufficient evidence to reject the null hypothesis; the observed difference in breast cancer death rates is reasonably explained by chance.

Evaluating medical treatments typically requires accounting for additional evidence that cannot be evaluated from a statistical test. For example, if mammograms are much more expensive than a standard screening and do not offer clear benefits, there is reason to recommend standard screenings over mammograms. This study also found that a higher proportion of diagnosed breast cancer cases in the mammogram screening arm (3250 in the mammogram group vs 3133 in the physical exam group), despite the nearly equal number of breast cancer deaths. The investigators inferred that mammograms may cause over-diagnosis of breast cancer, a phenomenon in which a breast cancer diagnosed with mammogram and subsequent biopsy may never become symptomatic. The possibility of over-diagnosis is one of the reasons mammogram screening remains controversial.

## EXAMPLE 8.15

Calculate a 95% confidence interval for the difference in proportions of deaths from breast cancer from the Canadian study.

The independence and random sampling conditions have already been discussed. The success failure condition should be checked for each sample, since this is not a hypothesis testing context (i.e., there is no null hypothesis). For the mammogram group, $\hat { p } _ { 1 } = 0 . 0 1 1 1 3 ;   n _ { 1 } \hat { p } _ { 1 } = ( 0 . 1 1 1 3 ) ( 4 4 , 9 2 5 ) =$ 500 and $n _ { 1 } \big ( 1 - \hat { p } _ { 1 } \big ) = 3 9 , 9 2 5$ . It is easy to show that the success failure condition is holds for the control group as well.

The point estimate for the difference in the probability of death is

$$
\hat {p} _ {1} - \hat {p} _ {2} = 0. 0 1 1 1 3 - 0. 0 1 1 2 5 = - 0. 0 0 0 1 2,
$$

or 0.012%.

The standard error for the estimated difference uses the individual estimates of the probability of a death:

$$
S E \approx \sqrt {\frac {0 . 0 1 1 1 3 (1 - 0 . 0 1 1 1 3)}{4 4 , 9 2 5} + \frac {0 . 0 1 1 2 5 (1 - 0 . 0 1 1 2 5)}{4 4 , 9 1 0}} = 0. 0 0 0 7.
$$

The 95% confidence interval is given by

$$
- 0. 0 0 0 1 2 \pm (1. 9 6) (0. 0 0 0 7) = (- 0. 0 0 1 5, 0. 0 0 1 3).
$$

With 95% confidence, the difference in the probability of death is between -0.15% and 0.13%. As expected from the large p-value, the confidence interval contains the null value 0.