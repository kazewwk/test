## 8.5.2 $\chi ^ { 2 }$ tests of association in case-control studies

In 2006, Chambers, et. al reported a case-control study examining the association of SSRI use and persistent pulmonary hypertension in newborns.<sup>21</sup> The study team enrolled 337 women whose infants suffered from PPHN and 836 women with similar characteristics but whose infants did not have PPHN. Among the women whose infants had PPHN, 14 had taken an SSRI after week 20 of the pregnancy. In the cohort of women whose infants did not have PPHN, 6 had been taking the medication after week 20. In the subset of women who had been taking an SSRI, the infants are considered ‘exposed’ to the medication. The data from the study are summarized in Figure 8.19.

| PPHN present | Yes | No | Total |
| --- | --- | --- | --- |
| SSRI exposed | 14 | 6 | 20 |
| SSRI unexposed | 323 | 830 | 1153 |
| Total | 337 | 836 | 1173 |

Figure 8.19: SSRI exposure vs observed number of PPHN cases in newborns.

The sample of women participating in the study are clearly not a random sample drawn from women who had recently given birth; they were identified according to the disease status of their infants. In this sample, the proportion of newborns with PPHN $\left( 337/1173 = 28.7\% \right)$ is much higher than the disease prevalence in the general population.

Even so, the concept of independence between rows and columns under a null hypothesis of no association still holds. If SSRI use had no effect on the occurrence of PPHN, then the proportions of mothers taking SSRIs among the PPHN and non-PPHN infants should be about the same. In other words, the null hypothesis of equal SSRI use among mothers with/without PPHN affected infants is the hypothesis of no association between SSRI use and PPHN. The test of independence can be conducted using the approach introduced earlier in the chapter.

The expected counts shown in Figure 8.20 suggest that the p-value from a $\chi ^ { 2 }$ test may not be accurate; under the null hypothesis, the expected number of PPHN cases in the SSRI exposed group is less than 10.

| PPHN present | Yes | No | Total |
| --- | --- | --- | --- |
| SSRI exposed | 5.80 | 14.20 | 20 |
| SSRI unexposed | 331.20 | 811.80 | 1153 |
| Total | 337 | 836 | 1173 |

Figure 8.20: SSRI exposure vs expected number of PPHN cases in newborn.

The p-value from Fisher’s exact test is < 0.001 (0.00014, to be precise), so the evidence is strong that SSRI exposure and PPHN are associated. Fisher’s exact test is often used in studies of rare conditions or exposures since one or more expected cell counts are typically less than 10.

## 8.5.3 Estimates of association in case-control studies

For data in a $2 \times 2$ table, correct point estimates of association depend on the mechanism used to gather the data. In the example of a clinical trial of nevirapine versus lopinarvir discussed in Section 8.3.1, the population proportion of children who would experience virologic failure after treatment with one of the drugs can be estimated by the observed proportion of virologic failures while on that drug. For nevirapine, the proportion of children with virologic failure is $60/147 =$ 0.41, while for lopinarvir the proportion is $2 7 / 1 4 0 = 0 . 1 9$ . The difference in outcome between the two groups can be summarized by the difference in these proportions. The proportion experiencing virologic failure when treated with nevirapine was 0.12 larger in nevirapine $(0.41 - 0.29)$ , so if the two drugs were to be used in a large population, approximately 12% more children treated with nevirapine would experience virologic failure as compared to lopinarvir. The confidence intervals discussed in Section 8.2.2 can be used to express the uncertainty in this estimate.

Since the proportion of virologic failures can be estimated from the trial data, the relative risk of virologic failure can also be used to estimate the association between treatment and virologic failure. Relative risk is the ratio of two proportions, and was introduced in Section 1.6.2. The relative risk of virologic failure with nevirapine versus lopinarvir is $0 . 4 1 / 0 . 1 9 = 2 . 1 6 .$ . Children treated with nevirapine are estimated to be more than twice as likely to experience virologic failure.

Statistically, the population parameter for the relative risk in the study of $\mathrm { H W ^ { + } }$ is a ratio of conditional probabilities:

$$
\frac {P (\text {virologic failure} | \text {treatment with nevirapine})}{P (\text {virologic failure} | \text {treatment with lopinarvir})}.
$$

In a study like the PPHN case-control study, the natural population parameter of interest would be the relative risk of PPHN for infants exposed to an SSRI during after week 20 of gesta tion compared to those who were not exposed. However, in the design of this study, participating mothers were sampled and grouped according to whether their infants did or did not suffer from PPHN, rather than assigned to either SSRI exposure or non-exposure. Relative risk of PPHN from exposure to SSRI cannot be estimated from the data because it is not possible to estimate P (PPHN|SSRI exposure) and $P ( \mathrm { P P H N } | \mathrm { n o } )$ SSRI exposure). In case-control studies, association is estimated using **odds** and **odds ratios** rather than relative risk.

The **odds** of SSRI exposure among the cases are given by the fraction

$$
\mathrm{odds} _ {\text {cases}} = \frac {P (\text {SSRI exposure|PPHN})}{P (\text {no SSRI exposure|PPHN})} = \frac {1 4 / 3 3 7}{3 2 3 / 3 3 7} = \frac {1 4}{3 2 3}.
$$

The odds of SSRI exposure among the controls are given by the fraction

$$
\text { odds } _ {\text { controls }} = \frac {P (\text { SSRI   exposure } | \text { no   PPHN })}{P (\text { no   SSRI   exposure } | \text { no   PPHN })} = \frac {6 / 8 3 6}{8 3 0 / 8 3 6} = \frac {6}{8 3 0}.
$$

The ratio of the odds, the odds ratio, compares the odds of exposure among the cases to the odds of exposure among the controls:

$$
O R _ {\text {exposure, cases vs. controls}} = \frac {\text {odds} _ {\text {cases}}}{\text {odds} _ {\text {controls}}} = \frac {1 4 / 3 2 3}{6 / 8 3 0} = \frac {(1 4) (8 3 0)}{(3 2 3) (6)} = 6. 0 0.
$$

A population odds ratio of, for example, 1.5, implies that the odds of exposure in cases are 50% larger than the odds of exposure in controls. For this study, the odds ratio of 6.00 implies that the odds of SSRI exposure in infants with PPHN are 6 times as large as the odds of exposure in infants without PPHN. Epidemiologists describe this odds ratio as the odds of exposure given presence of PPHN compared to the odds of exposure given absence of PPHN. An OR greater than 1 suggests that the exposure may be a risk factor for the disease or condition under study. Epidemiologists also use the term **relative odds** as a synonym for odds ratio.

Surprisingly, the odds ratio of exposure comparing cases to controls is equivalent to the odds ratio of disease comparing exposed to unexposed.<sup>22</sup> With a specific example, it is easy to see how the fraction for the odds ratios are numerically equivalent:

$$
O R _ {\text {disease, exposed versus unexposed}} = \frac {\mathrm{odds} _ {\text {exposed}}}{\mathrm{odds} _ {\text {unexposed}}} = \frac {1 4 / 6}{3 2 3 / 8 3 0} = \frac {(1 4) (8 3 0)}{(6) (3 2 3)} = 6. 0 0.
$$

Despite the apparently restrictive nature of the case-control sampling design, the odds ratio of interest, the odds ratio for disease given exposure, can be estimated from case-control data.

Epidemiologists rely on one additional result, called the rare disease assumption. When a disease is rare, the odds ratio for the disease given exposure is approximately equal to the relative risk of the disease given exposure. These identities are the reason case-control studies are widely used in settings in which a disease is rare: it allows for the relative risk of disease given exposure to be estimated, even if the study design is based on sampling cases and controls then measuring exposure.

In a general 2×2 table of exposure versus disease status (Figure 8.21) the odds ratio for disease given exposure status is the ad/bc.

| Disease Status | Present | Absent | Total |
| --- | --- | --- | --- |
| Exposed | a | b | a+b |
| Unexposed | c | d | c+d |
| Total | a+c | b+d | n |

Figure 8.21: Exposure vs Disease Status.

In the PPHN case-control data, the odds ratio for PPHN given SSRI exposure status is (14)(830)/(6)(323) = 6.00. Because PPHN is a rare condition, the risk of PPHN among infants exposed to an SSRI is estimated to be approximately 6 times that of the risk among unexposed infants. Infants exposed to an SSRI are 600% more likely to suffer from PPHN.

It can be shown that the p-value used in a test of no association (between exposure and disease) is also the p-value for a test of the null hypothesis that the odds ratio is 1.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">22<sub>This</sub> result can be shown through Bayes’ rule.</span></small>

## 8.6 Notes

Two-way tables are often used to summarize data from medical research studies, and entire texts have been written about methods of analysis for these tables. This chapter covers only the most basic of those methods.

Until recently, Fisher’s exact test could only be calculated for 2×2 tables with small cell counts. Research has produced faster algorithms for enumerating tables and calculating p-values, and the computational power of recent desktop and laptop computers now make it possible to calculate the Fisher test on nearly any $2 \times 2$ table. There are also versions of the test that can be calculated on tables with more than 2 rows and/or columns. The practical result for data analysts is that the sample size condition for the validity of the $\chi ^ { 2 }$ test can be made more restrictive. This chapter recommends using the $\chi ^ { 2 }$ test only when cell counts in a $2 \times 2$ table are greater than 10; some approaches recommend cell counts larger than 10.

For many years, introductory textbooks recommended using a modified version of the $\chi ^ { 2 }$ test, called the Fisher-Yates test, which adjusted the value of the statistic in small sample sizes to increase the accuracy of the $\chi ^ { 2 }$ sampling distribution in calculating p-values. The Fisher-Yates version of the test is no longer used as often because of the widespread availability of the Fisher test.

The Fisher test is not without controversy, at least in the theoretical literature. Conditioning on the row and column totals allows the calculation of a p-value from the hypergeometric distribution, but in principle restricts inference to the set of tables with the same row and column values. In practice, this is less serious than it may seem. For tables of moderate size, the p-values from the $\chi ^ { 2 }$ and Fisher tests are nearly identical and for tables with small counts, the Fisher test guarantees that the Type I error will be no larger than the specified value of $\alpha .$ In small sample sizes, some statisticians argue that the Fisher-Yates correction is preferable to the Fisher test because of the discrete nature of the hypergeometric distribution. In small tables, for example, an observed p-value of 0.04 may be the largest value that is less than 0.05, such that the Type I error of the test in that situation is 0.04, not 0.05.

Section 8.5.3 does not show the derivation that the odds ratio estimated from a case-control is the same as that from a cohort study. It is long and algebraically more complex than other derivations shown in the text, but it is a direct application of Bayes’ rule, applied to each term in the fraction that defines population odds ratio.

The two labs for this chapter examine methods of inference for the success probability in binomial data then generalizes inference for binomial proportions to two-way contingency tables. Lab 2 also discusses measures of association in two-by-two tables. The datasets in the labs are similar to datasets that arise frequently in medical statistics. Lab 1 assesses the evidence for a treatment effect in a single uncontrolled trial of a new drug for melanoma and whether outcomes in stage 1 lung cancer are different among patients treated at Dana-Farber Cancer Institute compared to population based statistics. In Lab 2, students analyze a dataset from a published clinical trial examining the benefit of using a more expensive but potentially more effective drug to treat HIV-positive infants.

## 8.7 Exercises

## 8.7.1 Inference for a single proportion

**8.1 Vegetarian college students.** Suppose that 8% of college students are vegetarians. Determine if the following statements are true or false, and explain your reasoning.

(a) The distribution of the sample proportions of vegetarians in random samples of size 60 is approximately normal since $n \geq 3 0$
(b) The distribution of the sample proportions of vegetarian college students in random samples of size 50 is right skewed.
(c) A random sample of 125 college students where 12% are vegetarians would be considered unusual.
(d) A random sample of 250 college students where 12% are vegetarians would be considered unusual.
(e) The standard error would be reduced by one-half if we increased the sample size from 125 to 250.

**8.2 Young Americans, Part I.** About 77% of young adults think they can achieve the American dream. Determine if the following statements are true or false, and explain your reasoning.<sup>23</sup>

(a) The distribution of sample proportions of young Americans who think they can achieve the American dream in samples of size 20 is left skewed.
(b) The distribution of sample proportions of young Americans who think they can achieve the American dream in random samples of size 40 is approximately normal since $n \geq 3 0$
(c) A random sample of 60 young Americans where 85% think they can achieve the American dream would be considered unusual.
(d) A random sample of 120 young Americans where 85% think they can achieve the American dream would be considered unusual.

**8.3 Gender equality.** The General Social Survey asked a random sample of 1,390 Americans the following question: “On the whole, do you think it should or should not be the government’s responsibility to promote equality between men and women?” 82% of the respondents said it “should be”. At a 95% confidence level, this sample has 2% margin of error. Based on this information, determine if the following statements are true or false, and explain your reasoning. <sup>24</sup>

(a) We are 95% confident that between 80% and 84% of Americans in this sample think it’s the government’s responsibility to promote equality between men and women.
(b) We are 95% confident that between 80% and 84% of all Americans think it’s the government’s responsibility to promote equality between men and women.
(c) If we considered many random samples of 1,390 Americans, and we calculated 95% confidence intervals for each, 95% of these intervals would include the true population proportion of Americans who think it’s the government’s responsibility to promote equality between men and women.
(d) In order to decrease the margin of error to 1%, we would need to quadruple (multiply by 4) the sample size.
(e) Based on this confidence interval, there is sufficient evidence to conclude that a majority of Americans think it’s the government’s responsibility to promote equality between men and women.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">23<sub>A</sub>. Vaughn. “[Poll finds young adults optimistic, but not about money](http://www.openintro.org/redirect.php?go=textbook-young_americans_2011&referrer=biostat1_pdf)”. In: Los Angeles Times (2011).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">24<sub>National</sub> Opinion Research Center, [General Social Survey, 2018](http://www.openintro.org/redirect.php?go=textbook-gss-data&referrer=biostat1_pdf).</span></small>

**8.4 Elderly drivers.** The Marist Poll published a report stating that 66% of adults nationally think licensed drivers should be required to retake their road test once they reach 65 years of age. It was also reported that interviews were conducted on 1,018 American adults, and that the margin of error was 3% using a 95% confidence level.<sup>25</sup>

(a) Verify the margin of error reported by The Marist Poll.
(b) Based on a 95% confidence interval, does the poll provide convincing evidence that more than 70% of the population think that licensed drivers should be required to retake their road test once they turn 65?

**8.5 Fireworks on July 4**<strong><sup>th</sup></strong>**.** A local news outlet reported that 56% of 600 randomly sampled Kansas residents planned to set off fireworks on July 4<sup>th</sup>. Determine the margin of error for the 56% point estimate using a 95% confidence level.<sup>26</sup>

**8.6 Life rating in Greece.** Greece has faced a severe economic crisis since the end of 2009. A Gallup poll surveyed 1,000 randomly sampled Greeks in 2011 and found that 25% of them said they would rate their lives poorly enough to be considered “suffering”.<sup>27</sup>

(a) Describe the population parameter of interest. What is the value of the point estimate of this parameter?
(b) Check if the conditions required for constructing a confidence interval based on these data are met.
(c) Construct a 95% confidence interval for the proportion of Greeks who are “suffering".
(d) Without doing any calculations, describe what would happen to the confidence interval if we decided to use a higher confidence level.
(e) Without doing any calculations, describe what would happen to the confidence interval if we used a larger sample.

**8.7 Study abroad.** A survey on 1,509 high school seniors who took the SAT and who completed an optional web survey shows that 55% of high school seniors are fairly certain that they will participate in a study abroad program in college.<sup>28</sup>

(a) Is this sample a representative sample from the population of all high school seniors in the US? Explain your reasoning.
(b) Let’s suppose the conditions for inference are met. Even if your answer to part (a) indicated that this approach would not be reliable, this analysis may still be interesting to carry out (though not report). Construct a 90% confidence interval for the proportion of high school seniors (of those who took the SAT) who are fairly certain they will participate in a study abroad program in college, and interpret this interval in context.
(c) What does “90% confidence" mean?
(d) Based on this interval, would it be appropriate to claim that the majority of high school seniors are fairly certain that they will participate in a study abroad program in college?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">25<sub>Marist</sub> Poll, [Road Rules: Re-Testing Drivers at Age 65?](http://www.openintro.org/redirect.php?go=textbook-drivers_at_65_2011&referrer=biostat1_pdf), March 4, 2011.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">26<sub>Survey</sub> USA, [News Poll #19333](http://www.openintro.org/redirect.php?go=textbook-SurveyUSA_19333&referrer=biostat1_pdf), data collected on June 27, 2012.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">27<sub>Gallup</sub> World, [More Than One in 10 “Suffering" Worldwide](http://www.openintro.org/redirect.php?go=textbook-1_in_10_suffering_2011&referrer=biostat1_pdf), data collected throughout 2011.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">28<sub>studentPOLL</sub>, [College-Bound Students’ Interests in Study Abroad and Other International Learning Activities](http://www.openintro.org/redirect.php?go=textbook-Interests_in_Study_Abroad_2008&referrer=biostat1_pdf), January 2008.</span></small>

**8.8 Legalization of marijuana, Part I.** The General Social Survey asked 1,578 US residents: “Do you think the use of marijuana should be made legal, or not?” 61% of the respondents said it should be made legal.<sup>29</sup>

(a) Is 61% a sample statistic or a population parameter? Explain.
(b) Construct a 95% confidence interval for the proportion of US residents who think marijuana should be made legal, and interpret it in the context of the data.
(c) A critic points out that this 95% confidence interval is only accurate if the statistic follows a normal distribution, or if the normal model is a good approximation. Is this true for these data? Explain.
(d) A news piece on this survey’s findings states, “Majority of Americans think marijuana should be legalized.” Based on your confidence interval, is this news piece’s statement justified?

**8.9 National Health Plan, Part I.** A Kaiser Family Foundation poll for US adults in 2019 found that 79% of Democrats, 55% of Independents, and 24% of Republicans supported a generic “National Health Plan”. There were 347 Democrats, 298 Republicans, and 617 Independents surveyed.<sup>30</sup>

(a) A political pundit on TV claims that a majority of Independents support a National Health Plan. Do these data provide strong evidence to support this type of statement?
(b) Would you expect a confidence interval for the proportion of Independents who oppose the public option plan to include 0.5? Explain.

**8.10 Legalize Marijuana, Part II.** As discussed in Exercise 8.8, the General Social Survey reported a sample where about 61% of US residents thought marijuana should be made legal. If we wanted to limit the margin of error of a 95% confidence interval to 2%, about how many Americans would we need to survey?

**8.11 National Health Plan, Part II.** Exercise 8.9 presents the results of a poll evaluating support for a generic “National Health Plan” in the US in 2019, reporting that 55% of Independents are supportive. If we wanted to estimate this number to within 1% with 90% confidence, what would be an appropriate sample size?

**8.12 Acetaminophen and liver damage.** It is believed that large doses of acetaminophen (the active ingredient in over the counter pain relievers like Tylenol) may cause damage to the liver. A researcher wants to conduct a study to estimate the proportion of acetaminophen users who have liver damage. For participating in this study, he will pay each subject \$20 and provide a free medical consultation if the patient has liver damage.

(a) If he wants to limit the margin of error of his 98% confidence interval to 2%, what is the minimum amount of money he needs to set aside to pay his subjects?
(b) The amount you calculated in part (a) is substantially over his budget so he decides to use fewer subjects. How will this affect the width of his confidence interval?

**8.13 College smokers.** We are interested in estimating the proportion of students at a university who smoke. Out of a random sample of 200 students from this university, 40 students smoke.

(a) Calculate a 95% confidence interval for the proportion of students at this university who smoke, and interpret this interval in context. (Reminder: Check conditions.)
(b) If we wanted the margin of error to be no larger than 2% at a 95% confidence level for the proportion of students who smoke, how big of a sample would we need?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">29<sub>National</sub> Opinion Research Center, [General Social Survey, 2018](http://www.openintro.org/redirect.php?go=textbook-gss-data&referrer=biostat1_pdf).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">30<sub>Kaiser</sub> Family Foundation, [The Public On Next Steps For The ACA And Proposals To Expand Coverage](http://www.openintro.org/redirect.php?go=textbook-kff_nat_health_plan_2019&referrer=biostat1_pdf), data collected between Jan 9-14, 2019.</span></small>

**8.14 2010 Healthcare Law.** On June 28, 2012 the U.S. Supreme Court upheld the much debated 2010 healthcare law, declaring it constitutional. A Gallup poll released the day after this decision indicates that 46% of 1,012 Americans agree with this decision. At a 95% confidence level, this sample has a 3% margin of error. Based on this information, determine if the following statements are true or false, and explain your reasoning.<sup>31</sup>

(a) We are 95% confident that between 43% and 49% of Americans in this sample support the decision of the U.S. Supreme Court on the 2010 healthcare law.
(b) We are 95% confident that between 43% and 49% of Americans support the decision of the U.S. Supreme Court on the 2010 healthcare law.
(c) If we considered many random samples of 1,012 Americans, and we calculated the sample proportions of those who support the decision of the U.S. Supreme Court, 95% of those sample proportions will be between 43% and 49%.
(d) The margin of error at a 90% confidence level would be higher than 3%.

**8.15 Oral contraceptive use, Part I.** In a study of 100 randomly sampled 18 year-old women in an inner city neighborhood, 15 reported that they were taking birth control pills.

(a) Can the normal approximation to the binomial distribution be used to calculate a confidence interval for proportion of women using birth control pills in this neighborhood? Explain your answer.
(b) Compute an approximate 95% confidence interval for the population proportion of women age 18 in this neighborhood taking birth control pills.
(c) Does the interval from part (b) support the claim that, for the young women in this neighborhood, the percentage who use birth control is not significantly different from the national average of 5%? Justify your answer.

**8.16 Oral contraceptive use, Part II.** Suppose that the study were repeated in a different inner city neighborhood and that out of 50 randomly sampled 18-year-old women, 6 reported that they were taking birth control pills. The researchers would like to assess the evidence that the proportion of 18-year-old women using birth control pills in this neighborhood is greater than the national average of 5%.

(a) Can the normal approximation to the binomial distribution be used to conduct a hypothesis test of the null hypothesis that the proportion of women using birth control pills in this neighborhood is equal to 0.05? Explain your answer.
(b) State the hypotheses for the analysis of interest and compute the p-value.
(c) Interpret the results from part (b) in the context of the data.

## 8.7.2 Inference for the difference of two proportions

**8.17 Social experiment, Part I.** A “social experiment" conducted by a TV program questioned what people do when they see a very obviously bruised woman getting picked on by her boyfriend. On two different occasions at the same restaurant, the same couple was depicted. In one scenario the woman was dressed “provocatively” and in the other scenario the woman was dressed “conservatively”. The table below shows how many restaurant diners were present under each scenario, and whether or not they intervened.

<table><tr><td rowspan="5">Intervene</td><td rowspan="2"></td><td colspan="2">Scenario</td><td rowspan="2">Total</td></tr><tr><td>Provocative</td><td>Conservative</td></tr><tr><td>Yes</td><td>5</td><td>15</td><td>20</td></tr><tr><td>No</td><td>15</td><td>10</td><td>25</td></tr><tr><td>Total</td><td>20</td><td>25</td><td>45</td></tr></table>

Explain why the sampling distribution of the difference between the proportions of interventions under provocative and conservative scenarios does not follow an approximately normal distribution.

**8.18 Heart transplant success.** The Stanford University Heart Transplant Study was conducted to determine whether an experimental heart transplant program increased lifespan. Each patient entering the program was officially designated a heart transplant candidate, meaning that he was gravely ill and might benefit from a new heart. Patients were randomly assigned into treatment and control groups. Patients in the treatment group received a transplant, and those in the control group did not. The table below displays how many patients survived and died in each group.<sup>32</sup>

|  | control | treatment |
| --- | --- | --- |
| alive | 4 | 24 |
| dead | 30 | 45 |

Suppose we are interested in estimating the difference in survival rate between the control and treatment groups using a confidence interval. Explain why we cannot construct such an interval using the normal approximation. What might go wrong if we constructed the confidence interval despite this problem?

**8.19 National Health Plan, Part III.** Exercise 8.9 presents the results of a poll evaluating support for a generically branded “National Health Plan” in the United States. 79% of 347 Democrats and 55% of 617 Independents support a National Health Plan.

(a) Calculate a 95% confidence interval for the difference between the proportion of Democrats and Independents who support a National Health Plan $( p _ { D } - p _ { I } )$ , and interpret it in this context. We have already checked conditions for you.
(b) True or false: If we had picked a random Democrat and a random Independent at the time of this poll, it is more likely that the Democrat would support the National Health Plan than the Independent.

**8.20 Sleep deprivation, CA vs. OR, Part I.** According to a report on sleep deprivation by the Centers for Disease Control and Prevention, the proportion of California residents who reported insufficient rest or sleep during each of the preceding 30 days is 8.0%, while this proportion is 8.8% for Oregon residents. These data are based on simple random samples of 11,545 California and 4,691 Oregon residents. Calculate a 95% confidence interval for the difference between the proportions of Californians and Oregonians who are sleep deprived and interpret it in context of the data.<sup>33</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">32<sub>B</sub>. Turnbull et al. “[Survivorship of Heart Transplant Data](http://www.openintro.org/redirect.php?go=textbook-heart_transplant_1974&referrer=biostat1_pdf)”. In: Journal of the American Statistical Association 69 (1974), pp. 74–80.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">33<sub>CDC</sub>, [Perceived Insufficient Rest or Sleep Among Adults — United States, 2008](http://www.openintro.org/redirect.php?go=textbook-Perceived_Insufficient_Rest_or_Sleep_Among_Adults&referrer=biostat1_pdf).</span></small>

**8.21 Remdesivir in COVID-19.** Remdesivir is an antiviral drug previously tested in animal models infected with coronaviruses like SARS and MERS. As of May 2020, remdesivir has temporary approval from the FDA for use in severely ill COVID-10 patients. A randomized controlled trial conducted in China enrolled 236 patients with severe COVID-19; 158 were assigned to receive remdesivir and 78 to receive a placebo. In the remdesivir group, 103 patients showed clinical improvement; in the placebo group, 45 patients showed clinical improvement.

(a) Conduct a formal comparison of the clinical improvement rates and summarize your findings.
(b) Report and interpret an appropriate confidence interval.

**8.22 Sleep deprivation, CA vs. OR, Part II.** Exercise 8.20 provides data on sleep deprivation rates of Californians and Oregonians. The proportion of California residents who reported insufficient rest or sleep during each of the preceding 30 days is 8.0%, while this proportion is 8.8% for Oregon residents. These data are based on simple random samples of 11,545 California and 4,691 Oregon residents.

(a) Conduct a hypothesis test to determine if these data provide strong evidence the rate of sleep deprivation is different for the two states. (Reminder: Check conditions)
(b) It is possible the conclusion of the test in part (a) is incorrect. If this is the case, what type of error was made?

**8.23 Gender and color preference.** A study asked 1,924 male and 3,666 female undergraduate college students their favorite color. A 95% confidence interval for the difference between the proportions of males and females whose favorite color is black $( p _ { m a l e } - p _ { f e m a l e } )$ was calculated to be (0.02, 0.06). Based on this information, determine if the following statements are true or false, and explain your reasoning for each statement you identify as false.<sup>34</sup>

(a) We are 95% confident that the true proportion of males whose favorite color is black is 2% lower to 6% higher than the true proportion of females whose favorite color is black.
(b) We are 95% confident that the true proportion of males whose favorite color is black is 2% to 6% higher than the true proportion of females whose favorite color is black.
(c) 95% of random samples will produce 95% confidence intervals that include the true difference between the population proportions of males and females whose favorite color is black.
(d) We can conclude that there is a significant difference between the proportions of males and females whose favorite color is black and that the difference between the two sample proportions is too large to plausibly be due to chance.
(e) The 95% confidence interval for $( p _ { f e m a l e }   -   p _ { m a l e } )$ cannot be calculated with only the information given in this exercise.

**8.24 Prenatal vitamins and Autism.** Researchers studying the link between prenatal vitamin use and autism surveyed the mothers of a random sample of children aged 24 - 60 months with autism and conducted another separate random sample for children with typical development. The table below shows the number of mothers in each group who did and did not use prenatal vitamins during the three months before pregnancy (periconceptional period).<sup>35</sup>

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Autism</td><td rowspan="2">Total</td></tr><tr><td>Autism</td><td>Typical development</td></tr><tr><td rowspan="3">Periconceptional prenatal vitamin</td><td>No vitamin</td><td>111</td><td>70</td><td>181</td></tr><tr><td>Vitamin</td><td>143</td><td>159</td><td>302</td></tr><tr><td>Total</td><td>254</td><td>229</td><td>483</td></tr></table>

(a) State appropriate hypotheses to test for independence of use of prenatal vitamins during the three months before pregnancy and autism.
(b) Complete the hypothesis test and state an appropriate conclusion. (Reminder: Verify any necessary conditions for the test.)
(c) A New York Times article reporting on this study was titled “Prenatal Vitamins May Ward Off Autism". Do you find the title of this article to be appropriate? Explain your answer. Additionally, propose an alternative title.<sup>36</sup>

**8.25 Sleep deprived transportation workers.** The National Sleep Foundation conducted a survey on the sleep habits of randomly sampled transportation workers and a control sample of non-transportation workers. The results of the survey are shown below.<sup>37</sup>

Transportation Professionals

|  | Control | Pilots | Truck Drivers | Train Operators | Bus/Taxi/Limo Drivers |
| --- | --- | --- | --- | --- | --- |
| Less than 6 hours of sleep | 35 | 19 | 35 | 29 | 21 |
| 6 to 8 hours of sleep | 193 | 132 | 117 | 119 | 131 |
| More than 8 hours | 64 | 51 | 51 | 32 | 58 |
| Total | 292 | 202 | 203 | 180 | 210 |

Conduct a hypothesis test to evaluate if these data provide evidence of a difference between the proportions of truck drivers and non-transportation workers (the control group) who get less than 6 hours of sleep per day, i.e. are considered sleep deprived.

**8.26 An apple a day keeps the doctor away.** A physical education teacher at a high school wanting to increase awareness on issues of nutrition and health asked her students at the beginning of the semester whether they believed the expression “an apple a day keeps the doctor away”, and 40% of the students responded yes. Throughout the semester she started each class with a brief discussion of a study highlighting positive effects of eating more fruits and vegetables. She conducted the same apple-a-day survey at the end of the semester, and this time 60% of the students responded yes. Can she used a two-proportion method from this section for this analysis? Explain your reasoning.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">35<sub>R</sub>.J. Schmidt et al. “[Prenatal vitamins, one-carbon metabolism gene variants, and risk for autism](http://www.openintro.org/redirect.php?go=textbook-prenatal_vitamins_autism_2011&referrer=biostat1_pdf)”. In: Epidemiology 22.4 (2011), p. 476.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">36<sub>R</sub>.C. Rabin. “[Patterns: Prenatal Vitamins May Ward Off Autism](http://www.openintro.org/redirect.php?go=textbook-nytimes_prenatal_vitamins_autism_2011&referrer=biostat1_pdf)”. In: New York Times (2011).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">37<sub>National</sub> Sleep Foundation, [2012 Sleep in America Poll: Transportation Workers’ Sleep](http://www.openintro.org/redirect.php?go=textbook-trans_workers_sleep_2012&referrer=biostat1_pdf), 2012.</span></small>

## 8.7.3 Inference for two or more groups

**8.27 True or false, Part I.** Determine if the statements below are true or false. For each false statement, suggest an alternative wording to make it a true statement.

(a) The chi-square distribution, just like the normal distribution, has two parameters, mean and standard deviation.
(b) The chi-square distribution is always right skewed, regardless of the value of the degrees of freedom parameter.
(c) The chi-square statistic is always positive.
(d) As the degrees of freedom increases, the shape of the chi-square distribution becomes more skewed.

**8.28 True or false, Part II.** Determine if the statements below are true or false. For each false statement, suggest an alternative wording to make it a true statement.

(a) As the degrees of freedom increases, the mean of the chi-square distribution increases.
(b) If you found $\chi ^ { 2 } = 1 0$ with $d f = 5$ you would fail to reject $H _ { 0 }$ at the 5% significance level.
(c) When finding the p-value of a chi-square test, we always shade the tail areas in both tails.
(d) As the degrees of freedom increases, the variability of the chi-square distribution decreases.

**8.29 Quitters.** Does being part of a support group affect the ability of people to quit smoking? A county health department enrolled 300 smokers in a randomized experiment. 150 participants were assigned to a group that used a nicotine patch and met weekly with a support group; the other 150 received the patch and did not meet with a support group. At the end of the study, 40 of the participants in the patch plus support group had quit smoking while only 30 smokers had quit in the other group.

(a) Create a two-way table presenting the results of this study.
(b) Answer each of the following questions under the null hypothesis that being part of a support group does not affect the ability of people to quit smoking, and indicate whether the expected values are higher or lower than the observed values.

i. How many subjects in the “patch + support" group would you expect to quit?

ii. How many subjects in the “patch only" group would you expect to not quit?

**8.30 Parasitic worm.** Lymphatic filariasis is a disease caused by a parasitic worm. Complications of the disease can lead to extreme swelling and other complications. Here we consider results from a randomized experiment that compared three different drug treatment options to clear people of the this parasite, which people are working to eliminate entirely. The results for the second year of the study are given below:<sup>38</sup>

|  | Clear at Year 2 | Not Clear at Year 2 |
| --- | --- | --- |
| Three drugs | 52 | 2 |
| Two drugs | 31 | 24 |
| Two drugs annually | 42 | 14 |

(a) Set up hypotheses for evaluating whether there is any difference in the performance of the treatments, and also check conditions.

(b) Statistical software was used to run a chi-square test, which output:

$$
X ^ {2} = 2 3. 7
$$

$$
d f = 2
$$

$$
\mathrm{p-value} = 7. 2 \mathrm{e-6}
$$

Use these results to evaluate the hypotheses from part (a), and provide a conclusion in the context of the problem.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">38<sub>Christopher</sub> King et al. “[A Trial of a Triple-Drug Treatment for Lymphatic Filariasis](http://www.openintro.org/redirect.php?go=textbook-King_Suamani_2018&referrer=biostat1_pdf)”. In: New England Journal of Medicine 379 (2018), pp. 1801–1810.</span></small>

**8.31 PREVEND, Part IV.** In the PREVEND data, researchers measured various features of study participants, including data on statin use and highest level of education attained. A two-way table of education level and statin use is shown below.

|  | Primary | LowerSec | UpperSec | Univ | Sum |
| --- | --- | --- | --- | --- | --- |
| NonUser | 31 | 111 | 107 | 136 | 385 |
| User | 20 | 46 | 27 | 22 | 115 |
| Sum | 51 | 157 | 134 | 158 | 500 |

(a) Set up hypotheses for evaluating whether there is an association between statin use and educational level.
(b) Check assumptions required for an analysis of these data.
(c) Statistical software was used to conduct a $\chi ^ { 2 }$ test: the test statistic is 19.054, with p-value 0.0027. Summarize the conclusions in context of the data, and be sure to comment on the direction of association.

**8.32 Diabetes and unemployment.** A Gallup poll surveyed Americans about their employment status and whether or not they have diabetes. The survey results indicate that 1.5% of the 47,774 employed (full or part time) and 2.5% of the 5,855 unemployed 18-29 year olds have diabetes.<sup>39</sup>

(a) Create a two-way table presenting the results of this study.
(b) State appropriate hypotheses to test for difference in proportions of diabetes between employed and unemployed Americans.
(c) The sample difference is about 1%. If we completed the hypothesis test, we would find that the p-value is very small (about 0), meaning the difference is statistically significant. Use this result to explain the difference between statistically significant and practically significant findings.

**8.33 TB Treatment.** Tuberculosis (TB) is an infectious disease caused by the Mycobacterium tuberculosis bac teria. Active TB can be cured by adhering to a treatment regimen of several drugs for 6-9 months. A major bar rier to eliminating TB worldwide is failure to adhere to treatment; this is known as defaulting from treatment. A study was conducted in Thailand to identify factors associated with default from treatment. The study results indicate that out of 54 diabetic participants, 0 defaulted from treatment; out of 1,180 non-diabetic participants, 54 defaulted from treatment. Participants were recruited at health centers upon diagnosis of TB.

(a) Create a two-way table presenting the results of this study.
(b) State appropriate hypotheses to test for difference in proportions of treatment default between diabetics and non-diabetics.
(c) Check assumptions. You may use a less stringent version of the success-failure condition: the expected number of successes per group should be greater than or equal to 5 (rather than 10).
(d) Formally test whether the proportion of patients who default from treatment differs between diabetics and non-diabetics. Summarize your findings.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">39<sub>Gallup</sub> Wellbeing, [Employed Americans in Better Health Than the Unemployed](http://www.openintro.org/redirect.php?go=textbook-employed_americans_in_better_health_2012&referrer=biostat1_pdf), data collected Jan. 2, 2011 - May 21, 2012.</span></small>

**8.34 Coffee and Depression.** Researchers conducted a study investigating the relationship between caffeinated coffee consumption and risk of depression in women. They collected data on 50,739 women free of depression symptoms at the start of the study in the year 1996, and these women were followed through 2006. The researchers used questionnaires to collect data on caffeinated coffee consumption, asked each individual about physician- diagnosed depression, and also asked about the use of antidepressants. The table below shows the distribution of incidences of depression by amount of caffeinated coffee consumption.<sup>40</sup>

Caffeinated coffee consumption

<table><tr><td colspan="2"></td><td>≤1 cup/week</td><td>2-6 cups/week</td><td>1 cup/day</td><td>2-3 cups/day</td><td>≥4 cups/day</td><td>Total</td></tr><tr><td rowspan="3">Clinical depression</td><td>Yes</td><td>670</td><td>373</td><td>905</td><td>564</td><td>95</td><td>2,607</td></tr><tr><td>No</td><td>11,545</td><td>6,244</td><td>16,329</td><td>11,726</td><td>2,288</td><td>48,132</td></tr><tr><td>Total</td><td>12,215</td><td>6,617</td><td>17,234</td><td>12,290</td><td>2,383</td><td>50,739</td></tr></table>

(a) What type of test is appropriate for evaluating if there is an association between coffee intake and depression?
(b) Write the hypotheses for the test you identified in part (a).
(c) Calculate the overall proportion of women who do and do not suffer from depression.
(d) Identify the expected count for the highlighted cell, and calculate the contribution of this cell to the test statistic.
(e) The test statistic is $\chi ^ { 2 } = 2 0 . 9 3$ . What is the p-value?
(f) What is the conclusion of the hypothesis test?
(g) One of the authors of this study was quoted on the NYTimes as saying it was “too early to recommend that women load up on extra coffee" based on just this study.<sup>41</sup> Do you agree with this statement? Explain your reasoning.

**8.35 Mosquito nets and malaria.** This problem examines a hypothetical prospective study about an important problem in the developing world: the use of mosquito nets to prevent malaria in children. The nets are typically used to protect children from mosquitoes while sleeping.

Suppose that in a large region of an African country, 100 households with one child are randomized to receive free mosquito nets for the child in the household and 100 households with one child are randomized to a control group where families do not receive the nets.

You are given the following information:

– In the 100 households receiving the nets, 22 children became infected with malaria.
– In the 100 households without the nets, 30 children became infected with malaria.
– The 200 families selected to participate in the study may be regarded as a random sample from the families in the region, so the 100 families in each group may be regarded as random samples from the population.
– Malaria among children is common in this region, with a prevalence of approximately 25%.

(a) Write down the 2 × 2 contingency table that corresponds to the data from the trial, labeling the table clearly and including the row and column totals.
(b) Under the hypothesis of no association between use of a mosquito net and malaria infection, calculate the expected number of infected children among 100 families who did receive a net.
(c) The $\chi ^ { 2 }$ statistic for this 2 × 2 table is 1.66. Use this information to conduct a test of the null hypothesis of no effect of the use of a mosquito net on malaria infection in children.
(d) Compute and interpret the estimated relative risk of malaria infection, comparing the households without a net to those with a net.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">40<sub>M</sub>. Lucas et al. “[Coffee, caffeine, and risk of depression among women](http://www.openintro.org/redirect.php?go=textbook-coffee_caffeine_depression_2011&referrer=biostat1_pdf)”. In: Archives of internal medicine 171.17 (2011), p. 1571.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">41<sub>A</sub>. O’Connor. “[Coffee Drinking Linked to Less Depression in Women](http://www.openintro.org/redirect.php?go=textbook-coffee_depression_2011&referrer=biostat1_pdf)”. In: New York Times (2011).</span></small>

**8.36 Health care fraud.** Most errors in billing insurance providers for health care services involve honest mistakes by patients, physicians, or others involved in the health care system. However, fraud is a serious problem. The National Health Care Anti-Fraud Association estimates that approximately \$68 billion is lost to health care fraud each year. Often when fraud is suspected, an audit of randomly selected billings is conducted. The selected claims are reviewed by experts and each claim is classified as allowed or not allowed. The claims not allowed are considered to be potentially fraudulent.

In general, the distribution of claims is highly skewed such that the majority of claims filed are small claims and only a few are large claims. Since simple random sampling would likely be overwhelmed by small claims, claims chosen for auditing are sampled in a stratified way: a set number of claims are sampled from each category of claim size: small, medium, and large. Here are data from an audit that used stratified sampling from three strata based on the claim size (i.e., monetary amount of the claim).

| Stratum | Sampled Claims | Not Allowed |
| --- | --- | --- |
| Small | 100 | 10 |
| Medium | 50 | 17 |
| Large | 20 | 4 |

(a) Can these data be used to estimate the proportion of large claims for which fraud might be expected?
(b) Can these data be used to estimate the proportion of possibly fraudulent claims that are large claims?
(c) Construct a 2 × 3 contingency table of counts for these data and include the marginal totals, with the rows being the classification of claims and the columns being the size of the claim.
(d) Calculate the expected number of claims that would not be allowed among the large claims, under the hypothesis of no association of between size of claim and the claim not being allowed.
(e) Is the use of the chi-square statistic justified for these data?
(f) A chi-square test of no association between size of claim and whether it was allowed has value 12.93. How many degrees of freedom does the chi-square statistic have and what is the p-value for a test of no association?
(g) Compute the $\chi ^ { 2 }$ residuals. Based on the residuals, interpret the findings in the context of the data.

**8.37 Anxiety.** Psychologists conducted an experiment to investigate the effect of anxiety on a person’s desire to be alone or in the company of others (Schacter 1959; Lehmann 1975). A group of 30 individuals were randomly assigned into two groups; one group was designated the "high anxiety" group and the other the "low anxiety" group. Those in the high-anxiety group were told that in the "upcoming experiment", they would be subjected to painful electric shocks, while those in the low-anxiety group were told that the shocks would be mild and painless.<sup>42</sup> All individuals were informed that there would be a 10 minute wait before the experiment began, and that they could choose whether to wait alone or with other participants.

The following table summarizes the results:

|  | Wait Together | Wait Alone | Sum |
| --- | --- | --- | --- |
| High-Anxiety | 12 | 5 | 17 |
| Low-Anxiety | 4 | 9 | 13 |
| Sum | 16 | 14 | 30 |

(a) Under the null hypothesis of no association, what are the expected cell counts?
(b) Under the assumption that the marginal totals are fixed and the null hypothesis is true, what is the probability of the observed set of results?
(c) Enumerate the tables that are more extreme than what was observed, in the same direction.
(d) Conduct a formal test of association for the results and summarize your findings. Let $\alpha = 0 . 0 5$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">42<sub>Individuals</sub> were not actually subjected to electric shocks of any kind</span></small>

**8.38 Salt intake and CVD.** Suppose we are interested in investigating the relationship between high salt intake and death from cardiovascular disease (CVD). One possible study design is to identify a group of highand low-salt users then follow them over time to compare the relative frequency of CVD death in the two groups. In contrast, a less expensive study design is to look at death records, identify CVD deaths from non-CVD deaths, collect information about the dietary habits of the deceased, then compare salt intake between individuals who died of CVD versus those who died of other causes. This design is called a retrospective design.

Suppose a retrospective study is done in a specific county of Massachusetts; data are collected on men ages 50-54 who died over a 1-month period. Of 35 men who died from CVD, 5 had a diet with high salt intake before they died, while of the 25 men who died from other causes, 2 had a diet with high salt intake. These data are summarized in the following table.

|  | CVD Death | Non-CVD Death | Total |
| --- | --- | --- | --- |
| High Salt Diet | 5 | 2 | 7 |
| Low Salt Diet | 30 | 23 | 53 |
| Total | 35 | 25 | 60 |

(a) Under the null hypothesis of no association, what are the expected cell counts?
(b) Of the 35 CVD deaths, 5 were in the high salt diet group and 30 were in the low salt diet group. Under the assumption that the marginal totals are fixed, enumerate all possible sets of results (i.e., the table counts) that are more extreme than what was observed, in the same direction.
(c) Calculate the probability of observing each set of results from part (b).
(d) Evaluate the statistical significance of the observed data with a two-sided alternative. Let α = 0.05. Summarize your results.

## 8.7.4 Chi-square tests for the fit of a distribution

**8.39 Open source textbook.** A professor using an open source introductory statistics book predicts that 60% of the students will purchase a hard copy of the book, 25% will print it out from the web, and 15% will read it online. At the end of the semester he asks his students to complete a survey where they indicate what format of the book they used. Of the 126 students, 71 said they bought a hard copy of the book, 30 said they printed it out from the web, and 25 said they read it online.

(a) State the hypotheses for testing if the professor’s predictions were inaccurate.
(b) How many students did the professor expect to buy the book, print the book, and read the book exclusively online?
(c) This is an appropriate setting for a chi-square test. List the conditions required for a test and verify they are satisfied.
(d) Calculate the chi-squared statistic, the degrees of freedom associated with it, and the p-value.
(e) Based on the p-value calculated in part (d), what is the conclusion of the hypothesis test? Interpret your conclusion in this context.

**8.40 Barking Deer.** Microhabitat factors associated with foraging sites of barking deer in Hainan Island, China were examined. In this region, woods make up 4.8% of the land, cultivated grass plots make up 14.7%, and deciduous forests make up 39.6%. Of the 426 sites where the deer forage, 4 were categorized as woods, 16 as cultivated grass plots, and 61 as deciduous forests. The table below summarizes these data.<sup>43</sup>

| woods | cultivated grassplot | deciduous forests | other | total |
| --- | --- | --- | --- | --- |
| 4 | 16 | 61 | 345 | 426 |

(a) Write the hypotheses for testing if barking deer prefer to forage in certain habitats over others.
(b) Check if the assumptions and conditions required for testing these hypotheses are reasonably met.
(c) Do these data provide convincing evidence that barking deer prefer to forage in certain habitats over others? Conduct an analysis and summarize your findings.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">43<sub>Liwei</sub> Teng et al. “Forage and bed sites characteristics of Indian muntjac (Muntiacus muntjak) in Hainan Island, China”. In: Ecological Research 19.6 (2004), pp. 675–681.</span></small>