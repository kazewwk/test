## 3.1.4 Linear combinations of random variables

Sums of random variables arise naturally in many problems. In the health insurance example, the amount spent by the employee during her next five years of employment can be represented as $X _ { 1 } + X _ { 2 } + X _ { 3 } + X _ { 4 } + X _ { 5 }$ , where $X _ { 1 }$ is the cost of the first $\mathtt { y e a r } , X _ { 2 }$ the second year, etc. If the employee’s domestic partner has health insurance with another employer, the total annual cost to the couple would be the sum of the costs for the employee (X) and for her partner (Y ), or $X + Y$ . In each of these examples, it is intuitively clear that the average cost would be the sum of the average of each term.

Sums of random variables represent a special case of linear combinations of variables.

## LINEAR COMBINATIONS OF RANDOM VARIABLES AND THEIR EXPECTED VALUES

If X and Y are random variables, then a linear combination of the random variables is given by

$$
a X + b Y,
$$

where a and b are constants. The mean of a linear combination of random variables is

$$
E (a X + b Y) = a E (X) + b E (Y) = a \mu_ {X} + b \mu_ {Y}.
$$

The formula easily generalizes to a sum of any number of random variables. For example, the average health care cost for 5 years, given that the cost for services remains the same, is

$$
E (X _ {1} + X _ {2} + X _ {3} + X _ {4} + X _ {5}) = E (5 X _ {1}) = 5 E (X _ {1}) = (5) (1 0 1 0) = \$ 5, 0 5 0.
$$

The formula implies that for a random variable $Z ,   E ( a + Z ) = a + E ( Z )$ . This could have been used when calculating the average health costs for the employee by defining a as the fixed cost of the premium $\left( a = \$948 \right)$ and $Z$ as the cost of the physician visits. Thus, the total annual cost for a year could be calculated as: $E(a+Z)=a+E(Z)=\$948+E(Z)=\$948+.30(1\times\$20)+.40(3\times\$20)$ + $20(4 \times \$20) + 0.10(8 \times \$20) = \$1,010.00.$

## GUIDED PRACTICE 3.7

Suppose the employee will begin a domestic partnership in the next year. Although she and her companion will begin living together and sharing expenses, they will each keep their existing health insurance plans; both, in fact, have the same plan from the same employer. In the last five years, her partner visited a physician only once in four of the ten years, and twice in the other six years. Calculate the expected total cost of health insurance to the couple in the next year.

Calculating the variance and standard deviation of a linear combination of random variables requires more care. The formula given here requires that the random variables in the linear combination be independent, such that an observation on one of the variables provides no information about the value of the other variable.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>Let X represent the costs for the employee and Y represent the costs for her partner. E(X) = \$1,010.00, as previously calculated. E(Y ) = 948+0.4(1×\$20)+0.6(2×\$20) = \$980.00. Thus, E(X+Y ) = E(X)+E(Y ) = \$1,010.00+\$980.00 = \$1,990.00.</span></small>

## VARIABILITY OF LINEAR COMBINATIONS OF RANDOM VARIABLES

$$
\mathrm{Var} (a X + b Y) = a ^ {2} \mathrm{Var} (X) + b ^ {2} \mathrm{Var} (Y).
$$

This equation is valid only if the random variables are independent of each other.

For the transformation $a + b Z ,$ , the variance is $b ^ { 2 } \mathrm { V a r } ( Z )$ , since a constant a has variance 0. When $b = 1$ , variance of $a + Z$ is $\operatorname { V a r } ( Z ) \cdot$ —adding a constant to a random variable has no effect on the variability of the random variable.

## EXAMPLE 3.8

Calculate the variance and standard deviation for the combined cost of next year’s health care for the two partners, assuming that the costs for each person are independent.

Let X represent the sum of costs for the employee and Y the sum of costs for her partner.

First, calculate the variance of health care costs for the partner. The partner’s costs are the sum of the annual fixed cost and the variable annual costs, so the variance will simply be the variance of the variable costs. If Z represents the component of the variable costs, $E(Z)=0.4(1 \times \$20)+0.6(2 \times \$20)=$ $\S 8 + \S 2 4 = \S 3 2$ . Thus, the variance of Z equals

$$
\mathrm{Var} (Z) = 0. 4 (2 0 - 3 2) ^ {2} + 0. 6 (4 0 - 3 2) ^ {2} = 9 6.
$$

Under the assumption of independence, $\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) = 1556 + 96 = 1652$ , and the standard deviation is ${ \sqrt { 1 6 5 2 } } = { \mathfrak { H } } 4 0 . 6 4 .$

The example of health insurance costs has been simplified to make the calculations clearer. It ignores the fact that many plans have a deductible amount, and that plan members pay for services at different rates before and after the deductible has been reached. Often, insured individuals no longer need to pay for services at all once a maximum amount has been reached in a year. The example also assumes that the proportions of number of physician visits per year, estimated from the last 10 years, can be treated as probabilities measured without error. Had a different timespan been chosen, the proportions might well have been different.

It also relies on the assumption that health care costs for the two partners are independent. Two individuals living together may pass on infectious diseases like the flu, or may participate together in activities that lead to similar injuries, such as skiing or long distance running. Section 3.6 shows how to adjust a variance calculation when independence is unrealistic.

## 3.2 Binomial distribution

The hypothetical clinical study and coin tossing example discussed earlier in this chapter are both examples of experiments that can be modeled with a binomial distribution. The binomial distribution is a more general case of another named distribution, the Bernoulli distribution.

## 3.2.1 Bernoulli distribution

Psychologist Stanley Milgram began a series of experiments in 1963 to study the effect of authority on obedience. In a typical experiment, a participant would be ordered by an authority figure to give a series of increasingly severe shocks to a stranger. Milgram found that only about 35% of people would resist the authority and stop giving shocks before the maximum voltage was reached. Over the years, additional research suggested this number is approximately consistent across communities and time.

Each person in Milgram’s experiment can be thought of as a **trial**. Suppose that a trial is labeled a **success** if the person refuses to administer the worst shock. If the person does administer the worst shock, the trial is a **failure**. The **probability of a success** can be written as $p = 0 . 3 5$ . The probability of a failure is sometimes denoted with $q = 1 - p .$

When an individual trial only has two possible outcomes, it is called a **Bernoulli random variable**. It is arbitrary as to which outcome is labeled success.

Bernoulli random variables are often denoted as 1 for a success and 0 for a failure. Suppose that ten trials are observed, of which 6 are successes and 4 are failures:

$$
0 1 1 1 1 0 1 1 0 0.
$$

The **sample proportion**, $\hat { p } ,$ is the sample mean of these observations:

$$
\hat {p} = \frac {\# \text {of successes}}{\# \text {of trials}} = \frac {0 + 1 + 1 + 1 + 1 + 0 + 1 + 1 + 0 + 0}{1 0} = 0. 6.
$$

Since 0 and 1 are numerical outcomes, the mean and standard deviation of a Bernoulli random variable can be defined. If $p$ is the true probability of a success, then the mean of a Bernoulli random variable X is given by

$$
\begin{array}{l} \mu = E [ X ] = P (X = 0) \times 0 + P (X = 1) \times 1 \\ = (1 - p) \times 0 + p \times 1 = 0 + p = p. \\ \end{array}
$$

Similarly, the variance of X can be computed:

$$
\sigma^ {2} = P (X = 0) (0 - p) ^ {2} + P (X = 1) (1 - p) ^ {2}
$$

$$
= (1 - p) p ^ {2} + p (1 - p) ^ {2} = p (1 - p).
$$

The standard deviation is $\sigma = \sqrt { p ( 1 - p ) }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>Find further information on Milgram’s experiment at [www.cnr.berkeley.edu/ucce50/ag-labor/7article/article35.htm](http://www.openintro.org/redirect.php?go=textbook-milgram&referrer=biostat1_pdf).</span></small>

## BERNOULLI RANDOM VARIABLE

If X is a random variable that takes value 1 with probability of success p and 0 with probability $1 - p ,$ then X is a Bernoulli random variable with mean p and standard deviation $\sqrt { p ( 1 - p ) }$

Suppose X represents the outcome of a single toss of a fair coin, where heads is labeled success. X is a Bernoulli random variable with probability of success $p   =   0.50;$ this can be expressed as $X \sim \operatorname { \mathtt { B e r n } } ( p )$ , or specifically, X ∼ Bern(0.50). It is essential to specify the probability of success when characterizing a Bernoulli random variable. For example, although the outcome of a single toss of an unfair coin can also be represented by a Bernoulli, it will have a different probability distribution since p does not equal 0.50 for an unfair coin.

The success probability p is the **parameter** of the distribution, and identifies a specific Bernoulli distribution out of the entire family of Bernoulli distributions where p can be any value between 0 and 1 (inclusive).

Bern(p) Bernoulli dist. with p prob. of success

![](images/page_147_image_7.jpg)

## EXAMPLE 3.9

Suppose that four individuals are randomly selected to participate in Milgram’s experiment. What is the chance that there will be exactly one successful trial, assuming independence between trials? Suppose that the probability of success remains 0.35.

Consider a scenario in which there is one success (i.e., one person refuses to give the strongest shock). Label the individuals as A, B, C, and D:

$$
\begin{array}{l} P (A = \text {refuse}, B = \text {shock}, C = \text {shock}, D = \text {shock}) \\ = P (A = \text {refuse}) P (B = \text {shock}) P (C = \text {shock}) P (D = \text {shock}) \\ = (0. 3 5) (0. 6 5) (0. 6 5) (0. 6 5) = (0. 3 5) ^ {1} (0. 6 5) ^ {3} = 0. 0 9 6. \\ \end{array}
$$

However, there are three other possible scenarios: either B, C, or D could have been the one to refuse. In each of these cases, the probability is also $( 0 . 3 5 ) ^ { 1 } ( 0 . 6 5 ) ^ { 3 }$ . These four scenarios exhaust all the possible ways that exactly one of these four people could refuse to administer the most severe shock, so the total probability of one success is $(4)(0.35)^{1}(0.65)^{3}=0.38$

## 3.2.2 The binomial distribution

The Bernoulli distribution is unrealistic in all but the simplest of settings. However, it is a useful building block for other distributions. The **binomial distribution** describes the probability of having exactly k successes in n independent Bernoulli trials with probability of a success $p .$ In Example 3.9, the goal was to calculate the probability of 1 success out of 4 trials, with probability of success $0 . 3 5 \; ( n = 4 ,   k = 1 ,   p = 0 . 3 5 )$

Like the Bernoulli distribution, the binomial is a discrete distribution, and can take on only a finite number of values. A binomial variable has values $0 ,   1 ,   2 ,   \cdots ,   n .$

A general formula for the binomial distribution can be developed from re-examining Example 3.9. There were four individuals who could have been the one to refuse, and each of these four scenarios had the same probability. Thus, the final probability can be written as:

$$
[ \# \text {of scenarios} ] \times P (\text {single scenario.}) \tag {3.10}
$$

The first component of this equation is the number of ways to arrange the $k = 1$ successes among the $n = 4$ trials. The second component is the probability of any of the four (equally probable) scenarios.

Consider P (single scenario) under the general case of k successes and $n - k$ failures in the n trials. In any such scenario, the Multiplication Rule for independent events can be applied:

$$
p ^ {k} (1 - p) ^ {n - k}.
$$

Secondly, there is a general formula for the number of ways to choose k successes in n trials, i.e. arrange k successes and $n - k$ failures:

$$
\binom{n}{k} = \frac{n!}{k!(n - k)!}.
$$

The quantity ${ \binom { n } { k } }$ is read n choose ${ \bf k } . ^ { 9 }$ The exclamation point notation (e.g. k!) denotes a **factorial** expression.<sup>10</sup>

Using the formula, the number of ways to choose $k = 1$ successes in $n = 4$ trials can be computed as:

$$
\binom {4} {1} = \frac {4 !}{1 ! (4 - 1) !} = \frac {4 !}{1 ! 3 !} = \frac {4 \times 3 \times 2 \times 1}{(1) (3 \times 2 \times 1)} = 4.
$$

Substituting n choose k for the number of scenarios and $p ^ { k } ( 1 - p ) ^ { n - k }$ for the single scenario probability in Equation (3.10) yields the general binomial formula.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">9Other notation for n choose k includes nCk, Ckn, and C(n, k).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10<sub>0</sub>! = 1 , 1! = 1, 2! = 2 × 1 = 2, . . . , n! = n × (n − 1) × . . . 2 × 1.</span></small>

## BINOMIAL DISTRIBUTION

Suppose the probability of a single trial being a success is $p .$ The probability of observing exactly k successes in n independent trials is given by

$$
P (X = k) = \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} = \frac {n !}{k ! (n - k) !} p ^ {k} (1 - p) ^ {n - k}. \tag {3.11}
$$

Additionally, the mean, variance, and standard deviation of the number of observed successes are, respectively

$$
\mu = n p \quad \sigma^ {2} = n p (1 - p) \quad \sigma = \sqrt {n p (1 - p)}. \tag {3.12}
$$

A binomial random variable X can be expressed as $X \sim \operatorname { B i n } ( n , p )$

## IS IT BINOMIAL? FOUR CONDITIONS TO CHECK.

(1) The trials are independent.
(2) The number of trials, n, is fixed.
(3) Each trial outcome can be classified as a success or failure.
(4) The probability of a success, $p ,$ is the same for each trial.

## EXAMPLE 3.13

What is the probability that 3 of 8 randomly selected participants will refuse to administer the worst shock?

First, check the conditions for applying the binomial model. The number of trials is fixed $( n = 8 )$ and each trial outcome can be classified as either success or failure. The sample is random, so the trials are independent, and the probability of success is the same for each trial.

For the outcome of interest, $k = 3$ successes occur in $n = 8$ trials, and the probability of a success is $p = 0 . 3 5$ . Thus, the probability that 3 of 8 will refuse is given by

$$
\begin{array}{l} P (X = 3) = \binom {8} {3} (0. 3 5) ^ {3} (1 - 0. 3 5) ^ {8 - 3} \quad = \quad \frac {8 !}{3 ! (8 - 3) !} (0. 3 5) ^ {3} (1 - 0. 3 5) ^ {8 - 3} \\ = \quad (5 6) (0. 3 5) ^ {3} (0. 6 5) ^ {5} \\ = \quad 0. 2 8. \\ \end{array}
$$

## EXAMPLE 3.14

What is the probability that at most 3 of 8 randomly selected participants will refuse to administer the worst shock?

The event of at most 3 out of 8 successes can be thought of as the combined probability of 0, 1, 2, and 3 successes. Thus, the probability that at most 3 of 8 will refuse is given by:

$$
\begin{array}{l} P (X \leq 3) = P (X = 0) + P (X = 1) + P (X = 2) + P (X = 3) \\ = \binom {8} {0} (0. 3 5) ^ {0} (1 - 0. 3 5) ^ {8 - 0} + \binom {8} {1} (0. 3 5) ^ {1} (1 - 0. 3 5) ^ {8 - 1} \\ + \binom {8} {2} (0. 3 5) ^ {2} (1 - 0. 3 5) ^ {8 - 2} + \binom {8} {3} (0. 3 5) ^ {3} (1 - 0. 3 5) ^ {8 - 3} \\ = (1) (0. 3 5) ^ {0} (1 - 0. 3 5) ^ {8} + (8) (0. 3 5) ^ {1} (1 - 0. 3 5) ^ {7} \\ + (2 8) (0. 3 5) ^ {2} (1 - 0. 3 5) ^ {6} + (5 6) (0. 3 5) ^ {3} (1 - 0. 3 5) ^ {5} \\ = 0. 7 0 6. \\ \end{array}
$$

## EXAMPLE 3.15

If 40 individuals were randomly selected to participate in the experiment, how many individuals would be expected to refuse to administer the worst shock? What is the standard deviation of the number of people expected to refuse?

Both quantities can directly be computed from the formulas in Equation (3.12). The expected value (mean) is given by: $\mu = n p = 4 0 \times 0 . 3 5 = 1 4$ . The standard deviation is: $\sigma = { \sqrt { n p ( 1 - p ) } } =$ $\sqrt { 4 0 \times 0 . 3 5 \times 0 . 6 5 } = 3 . 0 2$

## GUIDED PRACTICE 3.16

The probability that a smoker will develop a severe lung condition in their lifetime is about 0.30. Suppose that 5 smokers are randomly selected from the population. What is the probability that (a) one will develop a severe lung condition? (b) that no more than one will develop a severe lung condition? (c) that at least one will develop a severe lung condition?<sup>11</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11Let p = 0.30; X ∼ Bin(5, 0.30). (a) P (X = 1) =  5(0.30)1(1 − 0.30)5−1 = 0.36 (b) P (X ≤ 1) = P (X = 0) + P (X = 1) =  50(0.30)0(1 − 0.30)<sup>5−0</sup> + 0.36 = 0.53 (c) P (X ≥ 1) = 1 − P (X = 0) = 1 − 0.36 = 0.83</span></small>

## 3.3 Normal distribution

Among the many distributions seen in practice, one is by far the most common: the **normal distribution**, which has the shape of a symmetric, unimodal bell curve. Many variables are nearly normal, which makes the normal distribution useful for a variety of problems. For example, characteristics such as human height closely follow the normal distribution.

## 3.3.1 Normal distribution model

The normal distribution model always describes a symmetric, unimodal, bell-shaped curve. However, the curves can differ in center and spread; the model can be adjusted using mean and standard deviation. Changing the mean shifts the bell curve to the left or the right, while changing the standard deviation stretches or constricts the curve. Figure 3.5 shows the normal distribution with mean 0 and standard deviation 1 in the left panel and the normal distribution with mean 19 and standard deviation 4 in the right panel. Figure 3.6 shows these distributions on the same axis.

![](images/page_151_image_6.jpg)

Figure 3.5: Both curves represent the normal distribution; however, they differ in their center and spread. The normal distribution with mean 0 and standard deviation 1 is called the standard normal distribution.

![](images/page_151_chart_8.jpg)

<details>
<summary>violin</summary>

| X | Y |
| --- | --- |
| ~0 | Peak |
| ~19 | Peak |
</details>

Figure 3.6: The normal models shown in Figure 3.5 but plotted together and on the same scale.

For any given normal distribution with mean $\mu$ and standard deviation $\sigma ,$ the distribution can be written as $N ( \mu , \sigma ) ;   \mu$ and $\sigma$ are the parameters of the normal distribution. For example, $N ( 0 , 1 )$ refers to the standard normal distribution, as shown in Figure 3.5.

Unlike the Bernoulli and binomial distributions, the normal distribution is a continuous distribution.

## 3.3.2 Standardizing with Z-scores

The **Z-score** of an observation quantifies how far the observation is from the mean, in units of standard deviation(s). If x is an observation from a distribution $N ( \mu , \sigma )$ , the Z-score is mathematically defined as:

$$
Z = \frac {x - \mu}{\sigma}.
$$

An observation equal to the mean has a Z-score of 0. Observations above the mean have positive Z-scores, while observations below the mean have negative Z-scores. For example, if an observation is one standard deviation above the mean, it has a Z-score of 1; if it is 1.5 standard deviations below the mean, its Z-score is -1.5.

Z-scores can be used to identify which observations are more extreme than others, and are especially useful when comparing observations from different normal distributions. One observation $x _ { 1 }$ is said to be more unusual than another observation $x _ { 2 }$ if the absolute value of its Z-score is larger than the absolute value of the other observation’s Z-score: $| Z _ { 1 } | > | Z _ { 2 } |$ . In other words, the further an observation is from the mean in either direction, the more extreme it is.

## EXAMPLE 3.17

The SAT and the ACT are two standardized tests commonly used for college admissions in the United States. The distribution of test scores are both nearly normal. For the SAT, N(1500, 300); for the ACT, N(21, 5). While some colleges request that students submit scores from both tests, others allow students the choice of either the ACT or the SAT. Suppose that one student scores an 1800 on the SAT (Student A) and another scores a 24 on the ACT (Student B). A college admissions officer would like to compare the scores of the two students to determine which student performed better.

Calculate a Z-score for each student; i.e., convert x to Z.

Using $\mu _ { S A T } = 1 5 0 0 ,   \sigma _ { S A T } = 3 0 0 ,$ and $x _ { A } = 1 8 0 0 ,$ , find Student A’s Z-score:

$$
Z _ {A} = \frac {x _ {A} - \mu_ {S A T}}{\sigma_ {S A T}} = \frac {1 8 0 0 - 1 5 0 0}{3 0 0} = 1.
$$

For Student B:

$$
Z _ {B} = \frac {x _ {B} - \mu_ {A C T}}{\sigma_ {A C T}} = \frac {2 4 - 2 1}{5} = 0. 6.
$$

Student A’s score is 1 standard deviation above average on the SAT, while Student B’s score is 0.6 standard deviations above the mean on the ACT. As illustrated in Figure 3.7, Student A’s score is more extreme, indicating that Student A has scored higher with respect to other scores than Student B.

## THE Z-SCORE

The Z-score of an observation quantifies how far the observation is from the mean, in units of standard deviation(s). The Z-score for an observation x that follows a distribution with mean µ and standard deviation σ can be calculated using

$$
Z = \frac {x - \mu}{\sigma}.
$$

![](images/page_153_image_2.jpg)

Figure 3.7: Scores of Students A and B plotted on the distributions of SAT and ACT scores.

## EXAMPLE 3.18

How high would a student need to score on the ACT to have a score equivalent to Student A’s score of 1800 on the SAT?

As shown in Example 3.7, a score of 1800 on the SAT is 1 standard deviation above the mean. ACT scores are normally distributed with mean 21 and standard deviation 5. To convert a value from the standard normal curve (Z) to one on a normal distribution $N ( \mu , \sigma )$ :

$$
x = \mu + Z \sigma .
$$

Thus, a student would need a score of $2 1 + 1 { \bigl ( } 5 { \bigr ) } = 2 6$ on the ACT to have a score equivalent to 1800 on the SAT.

## GUIDED PRACTICE 3.19

Systolic blood pressure (SBP) for adults in the United States aged 18-39 follow an approximate normal distribution, N(115, 17.5). As age increases, systolic blood pressure also tends to increase. Mean systolic blood pressure for adults 60 years of age and older is 136 mm Hg, with standard deviation 40 mm Hg. Systolic blood pressure of 140 mm Hg or higher is indicative of hypertension (high blood pressure). (a) How many standard deviations away from the mean is a 30-year-old with systolic blood pressure of 125 mm Hg? (b) Compare how unusual a systolic blood pressure of 140 mm Hg is for a 65-year-old, versus a 30-year-old.<sup>12</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12(a) Calculate the Z-score: $\begin{array} { r } { \frac { \overline { { x } } - \mu } { \sigma } = \frac { 1 2 5 - 1 1 5 } { 1 7 . 5 } = 0 . 5 7 1 } \end{array}$ . A 30-year-old with systolic blood pressure of 125 mm Hg is about 0.6 standard deviations above the mean. (b) For x1 = 140 mm Hg: Z1 =x1−µσ =140−11517.5 = 1.43. For x2 = 140 mm Hg: Z2 =x2−µ=140−136= 0.1. While an SBP of 140 mm Hg is almost 1.5 standard deviations above the mean for a 30-year-old, it is only 0.1 standard deviations above the mean for a 65-year-old.</span></small>

## 3.3.3 The empirical rule

The empirical rule (also known as the 68-95-99.7 rule) states that for a normal distribution, almost all observations will fall within three standard deviations of the mean. Specifically, 68% of observations are within one standard deviation of the mean, 95% are within two SD’s, and 99.7% are within three SD’s.

![](images/page_154_chart_4.jpg)

<details>
<summary>violin</summary>

| Interval | Percentage |
| --- | --- |
| \(\mu - 3\sigma\) to μ - 2σ | 68% |
| \(\mu - 2\sigma\) to μ - σ | 95% |
| \(\mu - \sigma\) to μ | 99.7% |
| \(\mu + \sigma\) to μ + 2σ | N/A |
| \(\mu + 2\sigma\) to μ + 3σ | N/A |
</details>

Figure 3.8: Probabilities for falling within 1, 2, and 3 standard deviations of the mean in a normal distribution.

While it is possible for a normal random variable to take on values 4, 5, or even more standard deviations from the mean, these occurrences are extremely rare if the data are nearly normal. For example, the probability of being further than 4 standard deviations from the mean is about 1-in-30,000.

## 3.3.4 Calculating normal probabilities

The normal distribution is a continuous probability distribution. Recall from Section 2.1.5 that the total area under the density curve is always equal to 1, and the probability that a variable has a value within a specified interval is the area under the curve over that interval. By using either statistical software or normal probability tables, the normal model can be used to identify a probability or percentile based on the corresponding Z-score (and vice versa).

![](images/page_154_image_9.jpg)

Figure 3.9: The area to the left of Z represents the percentile of the observation.

<table><tr><td rowspan="2">Z</td><td colspan="10">Second decimal place of Z</td></tr><tr><td>0.00</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td><td>0.07</td><td>0.08</td><td>0.09</td></tr><tr><td>0.0</td><td>0.5000</td><td>0.5040</td><td>0.5080</td><td>0.5120</td><td>0.5160</td><td>0.5199</td><td>0.5239</td><td>0.5279</td><td>0.5319</td><td>0.5359</td></tr><tr><td>0.1</td><td>0.5398</td><td>0.5438</td><td>0.5478</td><td>0.5517</td><td>0.5557</td><td>0.5596</td><td>0.5636</td><td>0.5675</td><td>0.5714</td><td>0.5753</td></tr><tr><td>0.2</td><td>0.5793</td><td>0.5832</td><td>0.5871</td><td>0.5910</td><td>0.5948</td><td>0.5987</td><td>0.6026</td><td>0.6064</td><td>0.6103</td><td>0.6141</td></tr><tr><td>0.3</td><td>0.6179</td><td>0.6217</td><td>0.6255</td><td>0.6293</td><td>0.6331</td><td>0.6368</td><td>0.6406</td><td>0.6443</td><td>0.6480</td><td>0.6517</td></tr><tr><td>0.4</td><td>0.6554</td><td>0.6591</td><td>0.6628</td><td>0.6664</td><td>0.6700</td><td>0.6736</td><td>0.6772</td><td>0.6808</td><td>0.6844</td><td>0.6879</td></tr><tr><td>0.5</td><td>0.6915</td><td>0.6950</td><td>0.6985</td><td>0.7019</td><td>0.7054</td><td>0.7088</td><td>0.7123</td><td>0.7157</td><td>0.7190</td><td>0.7224</td></tr><tr><td>0.6</td><td>0.7257</td><td>0.7291</td><td>0.7324</td><td>0.7357</td><td>0.7389</td><td>0.7422</td><td>0.7454</td><td>0.7486</td><td>0.7517</td><td>0.7549</td></tr><tr><td>0.7</td><td>0.7580</td><td>0.7611</td><td>0.7642</td><td>0.7673</td><td>0.7704</td><td>0.7734</td><td>0.7764</td><td>0.7794</td><td>0.7823</td><td>0.7852</td></tr><tr><td>0.8</td><td>0.7881</td><td>0.7910</td><td>0.7939</td><td>0.7967</td><td>0.7995</td><td>0.8023</td><td>0.8051</td><td>0.8078</td><td>0.8106</td><td>0.8133</td></tr><tr><td>0.9</td><td>0.8159</td><td>0.8186</td><td>0.8212</td><td>0.8238</td><td>0.8264</td><td>0.8289</td><td>0.8315</td><td>0.8340</td><td>0.8365</td><td>0.8389</td></tr><tr><td>1.0</td><td>0.8413</td><td>0.8438</td><td>0.8461</td><td>0.8485</td><td>0.8508</td><td>0.8531</td><td>0.8554</td><td>0.8577</td><td>0.8599</td><td>0.8621</td></tr><tr><td>1.1</td><td>0.8643</td><td>0.8665</td><td>0.8686</td><td>0.8708</td><td>0.8729</td><td>0.8749</td><td>0.8770</td><td>0.8790</td><td>0.8810</td><td>0.8830</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr></table>

Figure 3.10: A section of the normal probability table. The percentile for a normal random variable with $Z = 0 . 4 3$ has been highlighted, and the percentile closest to 0.8000 has also been highlighted.

A **normal probability table** is given in Appendix B.1 on page 463 and abbreviated in Figure 3.10. This table can be used to identify the **percentile** corresponding to any particular Zscore; for instance, the percentile of $Z = 0 . 4 3$ is shown in row 0.4 and column 0.03 in Figure 3.10: 0.6664, or the $6 6 . 6 4 ^ { t h }$ percentile. First, find the proper row in the normal probability table up through the first decimal, and then determine the column representing the second decimal value. The intersection of this row and column is the percentile of the observation. This value also represents the probability that the standard normal variable Z takes on a value of 0.43 or less; i.e. $P ( Z \leq 0 . 4 3 ) = 0 . 6 6 6 4 .$

The table can also be used to find the Z-score associated with a percentile. For example, to identify Z for the $8 0 ^ { t h }$ percentile, look for the value closest to 0.8000 in the middle portion of the table: 0.7995. The Z-score for the $8 0 ^ { t h }$ percentile is given by combining the row and column Z values: 0.84.

## EXAMPLE 3.20

Student A from Example 3.17 earned a score of 1800 on the SAT, which corresponds to $Z = 1$ . What percentile is this score associated with?

In this context, the **percentile** is the percentage of people who earned a lower SAT score than Student A. From the normal table, Z of 1.00 is 0.8413. Thus, the student is in the $8 4 ^ { t h }$ percentile of test takers. This area is shaded in Figure 3.11.

## GUIDED PRACTICE 3.21

Determine the proportion of SAT test takers who scored better than Student A on the SAT.<sup>13</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13<sub>If</sub> 84% had lower scores than Student A, the number of people who had better scores must be 16%.</span></small>

![](images/page_156_chart_2.jpg)

<details>
<summary>area</summary>

| X | Y |
| --- | --- |
| 600 | ~0.05 |
| 900 | ~0.25 |
| 1200 | ~0.75 |
| 1500 | ~1.0 |
| 1800 | ~0.75 |
| 2100 | ~0.25 |
| 2400 | ~0.05 |
</details>

Figure 3.11: The normal model for SAT scores, with shaded area representing scores below 1800.

## 3.3.5 Normal probability examples

There are two main types of problems that involve the normal distribution: calculating probabilities from a given value (whether X or Z), or identifying the observation that corresponds to a particular probability.

## EXAMPLE 3.22

Cumulative SAT scores are well-approximated by a normal model, N(1500,300). What is the probability that a randomly selected test taker scores at least 1630 on the SAT?

For any normal probability problem, it can be helpful to start out by drawing the normal curve and shading the area of interest.

![](images/page_156_chart_9.jpg)

<details>
<summary>violin</summary>

| Metric | Value |
| --- | --- |
| Peak Area | 1630 |
</details>

To find the shaded area under the curve, convert 1630 to a Z-score:

$$
Z = \frac {x - \mu}{\sigma} = \frac {1 6 3 0 - 1 5 0 0}{3 0 0} = \frac {1 3 0}{3 0 0} = 0. 4 3.
$$

Look up the percentile of $Z   =   0 . 4 3$ in the normal probability table shown in Figure 3.10 or in Appendix B.1 on page 463: 0.6664. However, note that the percentile describes those who had a Z-score lower than 0.43, or in other words, the area below 0.43. To find the area above $Z = 0 . 4 3 ,$ subtract the area of the lower tail from the total area under the curve, 1:

![](images/page_156_chart_13.jpg)

<details>
<summary>violin</summary>

| Metric | Value |
| --- | --- |
| Difference (1.0000 - 0.6664) | 1.0000 |
| Mean Difference | 0.6664 |
| Cumulative Difference | 0.3336 |
</details>

The probability that a student scores at least 1630 on the SAT is 0.3336.

## DISCRETE VERSUS CONTINUOUS PROBABILITIES

Recall that the probability of a continuous random variable equaling some exact value is always 0. As a result, for a continuous random variable $X , P ( X   \leq   x )   =   P ( X   <   x )$ and $P(X \geq x) = P(X > x)$ . It is valid to state that $P(X \geq x) = 1 - P(X \leq x) = 1 - P(X < x)$

This is not the case for discrete random variables. For example, for a discrete random variable $Y , P ( Y \geq 2 ) = 1 - P ( Y < 2 ) = 1 - P ( Y \leq 1 )$ It would be incorrect to claim that $P(Y \geq 2) = 1 - P(Y \leq$ 2).

![](images/page_157_image_5.jpg)

## GUIDED PRACTICE 3.23

What is the probability of a student scoring at most 1630 on the $\mathrm { S A T 2 ^ { 1 4 } }$

![](images/page_157_image_8.jpg)

## GUIDED PRACTICE 3.24

Systolic blood pressure for adults 60 years of age and older in the United States is approximately normally distributed: N(136,40). What is the probability of an adult in this age group having systolic blood pressure of 140 mm Hg or greater?<sup>15</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">14<sub>This</sub> probability was calculated as part of Example 3.22: 0.6664. A picture for this exercise is represented by the shaded area below “0.6664” in Example 3.22.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">15<sub>The</sub> Z-score for this observation was calculated in Exercise 3.19 as 0.1. From the table, the P (Z ≥ 0.1) = 1 − 0.54 = 0.46.</span></small>

## EXAMPLE 3.25

The height of adult males in the United States between the ages of 20 and 62 is nearly normal, with mean 70 inches and standard deviation 3.3 inches.<sup>16</sup> What is the probability that a random adult male is between $5 ^ { \prime } 9 ^ { \prime \prime }$ and $6 2 \%$

These heights correspond to 69 inches and 74 inches. First, draw the figure. The area of interest is an interval, rather than a tail area.

![](images/page_158_chart_5.jpg)

<details>
<summary>area</summary>

| Metric | Value |
| --- | --- |
| Lower Bound (Percentile) | 69 |
| Upper Bound (Percentile) | 74 |
</details>

![](images/page_158_image_6.jpg)

To find the middle area, find the area to the left of 74; from that area, subtract the area to the left of 69.

First, convert to Z-scores:

$$
Z _ {7 4} = \frac {x - \mu}{\sigma} = \frac {7 4 - 7 0}{3 . 3} = 1. 2 1, \quad Z _ {6 2} = \frac {x - \mu}{\sigma} = \frac {6 9 - 7 0}{3 . 3} = - 0. 3 0.
$$

From the normal probability table, the areas are respectively, 0.8868 and 0.3821. The middle area is $0 . 8 8 6 8 - 0 . 3 8 2 1 = 0 . 5 0 4 8$ . The probability of being between heights $5 ^ { \prime } 9 ^ { \prime \prime }$ and $6 ^ { \prime } 2 ^ { \prime \prime }$ is 0.5048.

![](images/page_158_chart_11.jpg)

<details>
<summary>violin</summary>

| Metric | Value |
| --- | --- |
| Difference (Blue) | 0.8868 |
| Difference (White) | -0.3821 |
| Mean Difference | 0.5048 |
</details>

![](images/page_158_image_12.jpg)

## GUIDED PRACTICE 3.26

What percentage of adults in the United States ages 60 and older have blood pressure between 145 and 130 mm $\mathrm { H g } \mathfrak { g } ^ { 1 7 }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">16<sub>As</sub> based on a sample of 100 men, from the USDA Food Commodity Intake Database.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">17<sub>First</sub> calculate Z-scores, then find the percent below 145 mm Hg and below 130 mm Hg: Z<sub>145</sub> = 0.23 → 0.5890, Z<sub>130</sub> = −0.15 → 0.4404 (area above). Final answer: 0.5890 − 0.4404 = 0.1486.</span></small>

## EXAMPLE 3.27

How tall is a man with height in the $4 0 ^ { t h }$ percentile?

First, draw a picture. The lower tail probability is 0.40, so the shaded area must start before the mean.

![](images/page_159_chart_5.jpg)

<details>
<summary>area</summary>

| Metric | Value |
| --- | --- |
| Mean (Percentile) | 40% |
| Lower Bound (Percentile) | 0.40 |
| Upper Bound (Percentile) | 70 |
</details>

![](images/page_159_image_6.jpg)

Determine the Z-score associated with the $4 0 ^ { t h }$ percentile. Because the percentile is below 50%, Z will be negative. Look for the probability inside the negative part of table that is closest to 0.40: 0.40 falls in row −0.2 and between columns 0.05 and 0.06. Since it falls closer to 0.05, choose $Z = - 0 . 2 5 .$

Convert the Z-score to X, where $X \sim N ( 7 0 , 3 . 3 )$

$$
X = \mu + \sigma Z = 7 0 + (- 0. 2 5) (3. 3) = 6 9. 1 8.
$$

A man with height in the $4 0 ^ { t h }$ percentile is 69.18 inches tall, or about $5   ^ { \prime }   9   ^ { \prime \prime }$

![](images/page_159_image_11.jpg)

## GUIDED PRACTICE 3.28

(a) What is the $9 5 ^ { t h }$ percentile for SAT scores? (b) What is the $9 7 . 5 ^ { t h }$ percentile of the male heights?<sup>18</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">18(a) Look for 0.95 in the probability portion (middle part) of the normal probability table: row 1.6 and (about) column 0.05, i.e. Z<sub>95</sub> = 1.65. Knowing Z<sub>95</sub> = 1.65, µ = 1500, and σ = 300, convert Z to x: 1500 + (1.65)(300) = 1995. (b) Similarly, find Z<sub>97.5</sub> = 1.96, and convert to x: x<sub>97</sub>.5 = 76.5 inches.</span></small>