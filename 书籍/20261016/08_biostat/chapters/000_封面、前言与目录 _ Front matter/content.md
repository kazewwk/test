# 封面、前言与目录 / Front matter

原始 PDF 第 1–9 页。

# Introductory Statistics for the Life and Biomedical Sciences

First Edition

Julie Vu

Preceptor in Statistics

Harvard University

David Harrington

Professor of Biostatistics (Emeritus)

Harvard T.H. Chan School of Public Health

Dana-Farber Cancer Institute

A tablet-friendly version of this PDF where margins have been minimized

---

Copyright © 2020. First Edition.

Version date: August 8th, 2021.

This textbook and its supplements, including slides and labs, may be downloaded for free at [**openintro.org/book/biostat**](http://www.openintro.org/redirect.php?go=biostat&referrer=biostat1_pdf).

This textbook is a derivative of OpenIntro Statistics 3rd Edition by Diez, Barr, and Çetinkaya Rundel, and it is available under a Creative Commons Attribution-ShareAlike 3.0 Unported United States license. License details are available at the Creative Commons website:

[**creativecommons.org**](http://www.openintro.org/redirect.php?go=creativecommons_org&referrer=biostat1_pdf).

Source files for this book may be found on Github at [**github.com/OI-Biostat/oi\_biostat\_text**](http://www.openintro.org/redirect.php?go=biostat_source&referrer=biostat1_pdf).

---

3

## Table of Contents

## 1 Introduction to data 10

1.1 Case study . . . . 12
1.2 Data basics . . . . . . . . . . 14
1.3 Data collection principles . . . . . . . 18
1.4 Numerical data . . . . 30
1.5 Categorical data . . . . 37
1.6 Relationships between two variables . . 38
1.7 Exploratory data analysis . . . . . . 50
1.8 Notes . . . . . . . . 74
1.9 Exercises . . . . . . . . . . . 75

## 2 Probability 88

2.1 Defining probability . . . . . 90
2.2 Conditional probability . . . . . . . . 106
2.3 Extended example . . . . . . . 117
2.4 Notes . . . . . . . . . . 126
2.5 Exercises . . . . . . . . . 127

## 3 Distributions of random variables 138

3.1 Random variables . . . . 140
3.2 Binomial distribution . . . . . . . . 147
3.3 Normal distribution . . . . . . . 152
3.4 Poisson distribution . . . . . . . 168
3.5 Distributions related to Bernoulli trials . . . . 170
3.6 Distributions for pairs of random variables . . 177
3.7 Notes . . . . . . . 184
3.8 Exercises . . . . . . 185

## 4 Foundations for inference 198

4.1 Variability in estimates . . . . . . . 201
4.2 Confidence intervals . . . . 205
4.3 Hypothesis testing . . . . . . . 212
4.4 Notes . . . . . . . . 225
4.5 Exercises . . . . . . 227

---

4

TABLE OF CONTENTS

## 5 Inference for numerical data 236

5.1 Single-sample inference with the t-distribution . . . 238
5.2 Two-sample test for paired data . . . . 244
5.3 Two-sample test for independent data . . 247
5.4 Power calculations for a difference of means . . . 257
5.5 Comparing means with ANOVA . . . . 264
5.6 Notes . . . . . . 272
5.7 Exercises . . . . . . . . . 274

## 6 Simple linear regression 290

6.1 Examining scatterplots . . . . 293
6.2 Estimating a regression line using least squares . . . 295
6.3 Interpreting a linear model . . . . . . 298
6.4 Statistical inference with regression . . . . 308
6.5 Interval estimates with regression . . . . . 312
6.6 Notes . . . . . . . . 316
6.7 Exercises . . . . . . . . . . . 317

## 7 Multiple linear regression 330

7.1 Introduction to multiple linear regression . . . . 332
7.2 Simple versus multiple regression . . . . 334
7.3 Evaluating the fit of a multiple regression model . . . . 338
7.4 The general multiple linear regression model . . 342
7.5 Categorical predictors with several levels . . . . . 347
7.6 Reanalyzing the PREVEND data . . . . . 350
7.7 Interaction in regression . . 352
7.8 Model selection for explanatory models . . 358
7.9 The connection between ANOVA and regression . . 368
7.10 Notes . . . . . . . 370
7.11 Exercises . . . . . . . . . . 372

## 8 Inference for categorical data 386

8.1 Inference for a single proportion . . . . . . 388
8.2 Inference for the difference of two proportions . . 395
8.3 Inference for two or more groups . . . . 401
8.4 Chi-square tests for the fit of a distribution . . . 414
8.5 Outcome-based sampling: case-control studies . . 416
8.6 Notes . . . . . 420
8.7 Exercises . . . . . . 421

**A End of chapter exercise solutions 435**
**B Distribution tables 463**

**Index 469**

---

5

# Foreword

The past year has been challenging for the health sciences in ways that we could not have imagined when we started writing 5 years ago. The rapid spread of the SARS coronavirus (SARS-CoV-2) worldwide has upended the scientific research process and highlighted the need for maintaining a balance between speed and reliability. Major medical journals have dramatically increased the pace of publication; the urgency of the situation necessitates that data and research findings be made available as quickly as possible to inform public policy and clinical practice. Yet it remains essential that studies undergo rigorous review; the retraction of two high-profile coronavirus studies<sup>1</sup>, 2 sparked widespread concerns about data integrity, reproducibility, and the editorial process.

In parallel, deepening public awareness of structural racism has caused a re-examination of the role of race in published studies in health and medicine. A recent review of algorithms used to direct treatment in areas such as cardiology, obstetrics and oncology uncovered examples of race used in ways that may lead to substandard care for people of color.<sup>3</sup> The SARS-CoV-2 pandemic has reminded us once again that marginalized populations are disproportionately at risk for bad health outcomes. Data on 17 million patients in England<sup>4</sup>suggest that Blacks and South Asians have a death rate that is approximately 50% higher than white members of the population.

Understanding the SARS coronavirus and tackling racial disparities in health outcomes are but two of the many areas in which Biostatistics will play an important role in the coming decades. Much of that work will be done by those now beginning their study of Biostatistics. We hope this book provides an accessible point of entry for students planning to begin work in biology, medicine, or public health. While the material presented in this book is essential for understanding the foundations of the discipline, we advise readers to remember that a mastery of technical details is secondary to choosing important scientific questions, examining data without bias, and reporting results that transparently display the strengths and weaknesses of a study.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Mandeep R. Mehra et al. “Retraction: Cardiovascular Disease, Drug Therapy, and Mortality in Covid-19. N Engl J Med. DOI: 10.1056/NEJMoa2007621.” In: New England Journal of Medicine 382.26 (2020), pp. 2582–2582. doi: [10.1056/ NEJMc2021225](https://doi.org/10.1056/NEJMc2021225).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Mandeep R Mehra et al. “RETRACTED:Hydroxychloroquine or chloroquine with or without a macrolide for treatment of COVID-19: a multinational registry analysis”. In: The Lancet (2020). doi: [https://doi.org/10.1016/S0140- 6736(20) 31180-6](https://doi.org/https://doi.org/10.1016/S0140-6736%2820%2931180-6).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Darshali A. Vyas et al. “Hidden in Plain Sight — Reconsidering the Use of Race Correction in Clinical Algorithms”. In: New England Journal of Medicine (2020). doi: [10.1056/NEJMms2004740](https://doi.org/10.1056/NEJMms2004740).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>Elizabeth J. Williamson et al. “OpenSAFELY: factors associated with COVID-19 death in 17 million patients”. In: Nature (2020). issn: 1476-4687.</span></small>

---

6

# Preface

This text introduces statistics and its applications in the life sciences and biomedical research. It is based on the freely available OpenIntro Statistics, and, like OpenIntro, it may be downloaded at no cost.<sup>5</sup>In writing Introduction to Statistics for the Life and Biomedical Sciences, we have added substantial new material, but also retained some examples and exercises from OpenIntro that illustrate important ideas even if they do not relate directly to medicine or the life sciences. Because of its link to the original OpenIntro project, this text is often referred to as OpenIntro Biostatistics in the supplementary materials.

This text is intended for undergraduate and graduate students interested in careers in biology or medicine, and may also be profitably read by students of public health or medicine. It covers many of the traditional introductory topics in statistics, in addition to discussing some newer methods being used in molecular biology.

Statistics has become an integral part of research in medicine and biology, and the tools for summarizing data and drawing inferences from data are essential both for understanding the outcomes of studies and for incorporating measures of uncertainty into that understanding. An introductory text in statistics for students who will work in medicine, public health, or the life sciences should be more than simply the usual introduction, supplemented with an occasional example from biology or medical science. By drawing the majority of examples and exercises in this text from published data, we hope to convey the value of statistics in medical and biological research. In cases where examples draw on important material in biology or medicine, the problem statement contains the necessary background information.

Computing is an essential part of the practice of statistics. Nearly everyone entering the biomedical sciences will need to interpret the results of analyses conducted in software; many will also need to be capable of conducting such analyses. The text and associated materials separate those two activities to allow students and instructors to emphasize either or both skills. The text discusses the important features of figures and tables used to support an interpretation, rather than the process of generating such material from data. This allows students whose main focus is understanding statistical concepts not to be distracted by the details of a particular software package. In our experience, however, we have found that many students enter a research setting after only a single course in statistics. These students benefit from a practical introduction to data analysis that incorporates the use of a statistical computing language. The‘ self-paced learning labs associated with the text provide such an introduction; these are described in more detail later in this preface. The datasets used in this book are available via the R openintro package available on CRAN<sup>6</sup> and the R oibiostat package available via [GitHub](https://github.com/OI-Biostat/oi_biostat_data).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>PDF available at [https://www.openintro.org/book/biostat/](https://www.openintro.org/book/biostat/) and source available at [https://github.com/OI-Biostat/oi\_biostat\_text](https://github.com/OI-Biostat/oi_biostat_text).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>Diez DM, Barr CD, Çetinkaya-Rundel M. 2012. openintro: OpenIntro data sets and supplement functions. [http://cran.r-project.org/web/packages/openintro](http://cran.r-project.org/web/packages/openintro).</span></small>

---

7

## Textbook overview

The chapters of this book are as follows:

**1. Introduction to data.** Data structures, basic data collection principles, numerical and graphical summaries, and exploratory data analysis.
**2. Probability.** The basic principles of probability.
**3. Distributions of random variables.** Introduction to random variables, distributions of discrete and continuous random variables, and distributions for pairs of random variables.
**4. Foundations for inference.** General ideas for statistical inference in the context of estimating a population mean.
**5. Inference for numerical data.** Inference for one-sample and two-sample means with the t-distribution, power calculations for a difference of means, and ANOVA.
**6. Simple linear regression.** An introduction to linear regression with a single explanatory variable, evaluating model assumptions, and inference in a regression context.
**7. Multiple linear regression.** General multiple regression model, categorical predictors with more than two values, interaction, and model selection.
**8. Inference for categorical data.** Inference for single proportions, inference for two or more groups, and outcome-based sampling.

## Examples, exercises, and appendices

Examples in the text help with an understanding of how to apply methods:

## EXAMPLE 0.1

This is an example. When a question is asked here, where can the answer be found?

The answer can be found here, in the solution section of the example.

When we think the reader would benefit from working out the solution to an example, we frame it as Guided Practice.

## GUIDED PRACTICE 0.2

The reader may check or learn the answer to any Guided Practice problem by reviewing the full solution in a footnote.

There are exercises at the end of each chapter that are useful for practice or homework assignments. Solutions to odd numbered problems can be found in Appendix A. Readers will notice that there are fewer end of chapter exercises in the last three chapters. The more complicated methods, such as multiple regression, do not always lend themselves to hand calculation, and computing is increasingly important both to gain practical experience with these methods and to explore complex datasets. For students more interested in concepts than computing, however, we have included useful end of chapter exercises that emphasize the interpretation of output from statistical software.

Probability tables for the normal, t, and chi-square distributions are in Appendix B, and PDF copies of these tables are also available from [**openintro.org**](http://www.openintro.org) for anyone to download, print, share, or modify. The labs and the text also illustrate the use of simple R commands to calculate probabilities from common distributions.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>Guided Practice problems are intended to stretch your thinking, and you can check yourself by reviewing the footnote solution for any Guided Practice.</span></small>

E

G

---

8

CHAPTER 0. PREFACE

## Self-paced learning labs

The labs associated with the text can be downloaded from github.com/OI-Biostat/oi\_biostat labs. They provide guidance on conducting data analysis and visualization with the R statistical language and the computing environment RStudio, while building understanding of statistical concepts. The labs begin from first principles and require no previous experience with statistical software. Both R and RStudio are freely available for all major computing operating systems, and the Unit 0 labs (00\_getting\_started) provide information on downloading and installing them. Information on downloading and installing the packages may also be found at [**openintro.org**](http://www.openintro.org).

The labs for each chapter all have the same structure. Each lab consists of a set of three documents: a handout with the problem statements, a template to be used for working through the lab, and a solution set with the problem solutions. The handout and solution set are most easily read in PDF format (although Rmd files are also provided), while the template is an Rmd file that can be loaded into RStudio. Each chapter of labs is accompanied by a set of "Lab Notes", which provides a reference guide of all new R functions discussed in the labs.

Learning is best done, of course, if a student attempts the lab exercises before reading the solutions. The "Lab Notes" may be a useful resource to refer to while working through problems.

## OpenIntro, online resources, and getting involved

OpenIntro is an organization focused on developing free and affordable education materials. The first project, OpenIntro Statistics, is intended for introductory statistics courses at the high school through university levels. Other projects examine the use of randomization methods for learning about statistics and conducting analyses (Introductory Statistics with Randomization and Simulation) and advanced statistics that may be taught at the high school level (Advanced High School Statistics).

We encourage anyone learning or teaching statistics to visit **openintro.org** and get involved by using the many online resources, which are all free, or by creating new material. Students can test their knowledge with practice quizzes, or try an application of concepts learned in each chapter using real data and the free statistical software R. Teachers can download the source for course materials, labs, slides, datasets, R figures, or create their own custom quizzes and problem sets for students to take on the website. Everyone is also welcome to download the book’s source files to create a custom version of this textbook or to simply share a PDF copy with a friend or on a website. All of these products are free, and anyone is welcome to use these online tools and resources with or without this textbook as a companion.

## Acknowledgements

The OpenIntro project would not have been possible without the dedication of many people, including the authors of OpenIntro Statistics, the [OpenIntro team](http://www.openintro.org/redirect.php?go=textbook-openintro_about&referrer=biostat1_pdf) and the many faculty, students, and readers who commented on all the editions of OpenIntro Statistics.

This text has benefited from feedback from Andrea Foulkes, Raji Balasubramanian, Curry Hilton, Michael Parzen, Kevin Rader, and the many excellent teaching fellows at Harvard College who assisted in courses using the book. The cover design was provided by Pierre Baduel.

---

9
