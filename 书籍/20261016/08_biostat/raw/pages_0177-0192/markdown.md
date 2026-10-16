## 3.6 Distributions for pairs of random variables

Example 3.8 calculated the variability in health care costs for an employee and her partner relying on the assumption that the number of health episodes between the two are not related. It could be reasonable to assume that the health status of one person gives no information about the other’s health, given that the two are not physically related and were not previously living together. However, associations between random variables can be subtle. For example, couples are often attracted to each other because of common interests or lifestyles, which suggests that health status may actually be related.

The relationship between a pair of discrete random variables is a feature of the **joint distribution** of the pair. In this example the joint distribution of annual costs is a table of all possible combinations of costs for the employee and her partner, using the probabilities and costs from the last 10 years (these costs were previously calculated in Example 3.6 and Guided Practice 3.7). Entries in the table are probabilities of pairs of annual costs. For example, the entry 0.25 in the second row and second column of Figure 3.24 indicates that in approximately 25% of the last 10 years, the employee paid \$1,008 in costs while her partner paid \$988.

<table><tr><td rowspan="2">Employee costs, X</td><td colspan="2">Partner costs, Y</td></tr><tr><td>$968</td><td>$988</td></tr><tr><td>$968</td><td>0.18</td><td>0.12</td></tr><tr><td>$1,008</td><td>0.15</td><td>0.25</td></tr><tr><td>$1,028</td><td>0.04</td><td>0.16</td></tr><tr><td>$1,108</td><td>0.03</td><td>0.07</td></tr></table>

Figure 3.24: Joint distribution of health care costs.

More generally, the definition of a joint distribution for a pair of random variables X and Y uses the notion of joint probabilities discussed in Section 2.2.1.

## JOINT DISTRIBUTION

The **joint distribution** $p _ { X , Y } ( x , y )$ for a pair of random variables $( X , Y )$ is the collection of prob abilities

$$
p (x _ {i}, y _ {j}) = P (X = x _ {i} \text { and } Y = y _ {j})
$$

for all pairs of values $( x _ { i } , y _ { j } )$ that the random variables X and Y take on.

Joint distributions are often displayed in tabular form as in Figure 3.24. If X and Y have $k _ { 1 }$ and $k _ { 2 }$ possible values respectively, there will be $( k _ { 1 } ) ( k _ { 2 } )$ possible $( x , y )$ pairs. This is unlike pairs of values $( x , y )$ observed in a dataset, where each observed value of x is usually paired with only one value of y. A joint distribution is often best displayed as a table of probabilities, with $( k _ { 1 } ) ( k _ { 2 } )$ entries. Figure 3.25 shows the general form of the table for the joint distribution of two discrete distributions.

<table><tr><td colspan="5">Values of Y</td></tr><tr><td>Values of X</td><td> $y_1$ </td><td> $y_2$ </td><td>...</td><td> $y_{k_2}$ </td></tr><tr><td> $x_1$ </td><td> $p(x_1,y_1)$ </td><td> $p(x_1,y_2)$ </td><td>...</td><td> $p(x_1,y_{k_2})$ </td></tr><tr><td> $x_2$ </td><td> $p(x_2,y_1)$ </td><td> $p(x_2,y_2)$ </td><td>...</td><td> $p(x_2,y_{k_2})$ </td></tr><tr><td> $\vdots$ </td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $x_{k_1}$ </td><td> $p(x_{k_1},y_1)$ </td><td> $p(x_{k_1},y_2)$ </td><td>...</td><td> $p(x_{k_1},y_{k_2})$ </td></tr></table>

Figure 3.25: Table for a joint distribution. Entries are probabilities for pairs $( x _ { i } , y _ { j } )$ These probabilities can be written as $p ( x _ { i } , y _ { j } )$ or more specifically, $p _ { X , Y } ( x _ { i } , y _ { j } )$ .

When two variables X and Y have a joint distribution, the **marginal distribution** of X is the collection of probabilities for X when Y is ignored.<sup>32</sup> If X represents employee costs and Y represents partner costs, the event $( X = \S 9 6 8 )$ consists of the two disjoint events $\left( X = \$968, Y = \right.$ \$968) and $\left( X = \S 9 6 8 , Y = \S 9 8 8 \right)$ , so $P(X = 5968) = 0.18 + 0.12 = 0.30$ , the sum of the first row of the table. The row sums are the values of the marginal distribution of $X ,$ while the column sums are the values of the marginal distributions of Y . The marginal distributions of X and $Y$ are shown in Figure 3.26, along with the joint distribution of X and Y . The term marginal distribution is apt in this setting—the marginal probabilities appear in the table margins.

<table><tr><td></td><td colspan="3">Partner Costs, Y</td></tr><tr><td>Employee costs, X</td><td>$968</td><td>$988</td><td>Marg. Dist., X</td></tr><tr><td>$968</td><td>0.18</td><td>0.12</td><td>0.30</td></tr><tr><td>$1,008</td><td>0.15</td><td>0.25</td><td>0.40</td></tr><tr><td>$1,028</td><td>0.04</td><td>0.16</td><td>0.20</td></tr><tr><td>$1,108</td><td>0.03</td><td>0.07</td><td>0.10</td></tr><tr><td>Marg. Dist., Y</td><td>0.40</td><td>0.60</td><td>1.00</td></tr></table>

Figure 3.26: Joint and marginal distributions of health care costs

For a pair of random variables X and $Y ,$ the **conditional distribution** of Y given a value x of the variable X is the probability distribution of Y when its values are restricted to the value x for X. Just as marginal and joint probabilities are used to calculate conditional probabilities, joint and marginal distributions can be used to obtain conditional distributions. If information is observed about the value of one of the correlated random variables, such as $X ,$ then this information can be used to obtain an updated distribution for $Y ;$ unlike the marginal distribution of $Y ,$ the conditional distribution of Y given X accounts for information from $X .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">32<sub>The</sub> marginal distribution of X can be written as p<sub>X</sub> (x), and a specific value in the marginal distribution written as p<sub>X</sub> (x<sub>i</sub> ).</span></small>

## CONDITIONAL DISTRIBUTION

The **conditional distribution** $p _ { Y | X } ( y | x )$ for a pair of random variables (X, Y ) is the collection of probabilities

$$
P (Y = y _ {j} | X = x _ {i}) = \frac {P (Y = y _ {j} \text {and} X = x _ {i})}{P (X = x _ {j})}
$$

for all pairs of values $( x _ { i } , y _ { j } )$ that the random variables X and Y take on.

## EXAMPLE 3.48

If it is known that the employee’s annual health care cost is \$968, what is the conditional distribution of the partner’s annual health care cost?

Note that there is a different conditional distribution of Y for every possible value of X; this problem specifically asks for the conditional distribution of Y given that $X = \S 9 6 8$

$$
p _ {Y \mid X} (\$ 9 6 8 \mid \$ 9 6 8) = P (Y = \$ 9 6 8 \mid X = \$ 9 6 8) = \frac {P (Y = \$ 9 6 8 \text {and} X = \$ 9 6 8)}{P (X = \$ 9 6 8)} = \frac {0 . 1 8}{0 . 3 0} = 0. 6 0
$$

$$
p _ {Y \mid X} (\$ 9 8 8 \mid \$ 9 6 8) = P (Y = \$ 9 8 8 \mid X = \$ 9 6 8) = \frac {P (Y = \$ 9 8 8 \text {and} X = \$ 9 6 8)}{P (X = \$ 9 6 8)} = \frac {0 . 1 2}{0 . 3 0} = 0. 4 0
$$

With the knowledge that the employee’s annual health care cost is \$968, there is a probability of 0.60 that the partner’s cost is \$968 and 0.40 that the partner’s cost is \$988.

## GUIDED PRACTICE 3.49

Consider two random variables, X and Y , with the joint distribution shown in Figure 3.27.

(a) Compute the marginal distributions of X and Y .
(b) Identify the joint probability $p _ { X , Y } ( 1 , 2 ) .$
(c) What is the value of $p _ { X , Y } ( 2 , 1 ) ?$
(d) Compute the conditional distribution of X given that $Y = 2 . ^ { 3 3 }$

|  | Y = 1 | Y = 2 |
| --- | --- | --- |
| X = 1 | 0.20 | 0.40 |
| X = 4 | 0.30 | 0.10 |

Figure 3.27: Joint distribution of X and Y

The variance calculation in Example 3.8 relied on the assumption that the patterns of health care expenses for the two partners were unrelated. In Example 3.48, 0.40 is the conditional probability that the partner’s health care costs will be \$988, given that the employee’s cost is \$968. The marginal probability that the partner’s health care cost is \$988 is 0.60, which is different from 0.40. The patterns of health care costs are related in that knowing the value of the employee’s costs changes the probabilities associated with partner’s costs. The marginal and conditional distributions of the partner’s costs are not the same.

The notion of independence of two events discussed in Chapter 2 can be applied to the setting of random variables. Recall that two events A and B are independent if the conditional probability $P ( A | B )$ equals the marginal probability $P ( A )$ or equivalently, if the product of the marginal probabilities P (A) and $P ( B )$ equals the joint probability $P ( A$ and B).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">33(a) The marginal distribution of X: p<sub>X</sub> (1) = 0.60, p<sub>X</sub> (4) = 0.40. The marginal distribution of Y : p<sub>Y</sub> (1) = 0.50, p<sub>Y</sub> (2) = 0.50 (b) p<sub>X</sub>,Y (1, 2) = P (X = 1, Y = 2) = 0.40 (c) Since X cannot take on value 2, p<sub>X</sub>,Y (2, 1) = 0. (d) The conditional distribution of X given that Y = 2: p<sub>X</sub>|Y (1|2) = pX,Y (1,2) pY (2) 0.400.50 = 0.80, p<sub>X</sub>|Y (4|2) = pX,Y (4,2) pY (2) 0.100.50 = 0.20.</span></small>

A pair (X,Y ) of random variables are called **independent random variables** if the conditional distribution for Y , given any value of X, is the same as the marginal distribution of Y . Additionally, if all joint probabilities $P ( X = x _ { i } , Y = y _ { j } )$ that comprise the joint distribution of X and Y can be computed from the product of the marginal probabilities, $P ( X = x _ { i } ) P ( Y = y _ { j } )$ , X and Y are independent.

## INDEPENDENT RANDOM VARIABLES

Two random variables X and Y are independent if the probabilities

$$
P (Y = y _ {j} | X = x _ {i}) = P (Y = y _ {j})
$$

for all pairs of values $( x _ { i } , y _ { j } )$ .

Equivalently, X and Y are independent if the probabilities

$$
P (Y = y _ {j} \text { and } X = x _ {i}) = P (Y = y _ {j}) P (X = x _ {i})
$$

for all pairs of values $( x _ { i } , y _ { j } )$ ).

## EXAMPLE 3.50

Demonstrate that the employee’s health care costs and the partner’s health care costs are not independent random variables.

As shown in Example 3.48, the conditional distribution of the partner’s annual health care cost given that the employee’s annual cost is \$968 is $P(Y = \$968|X = \$968) = 0.60,\; P(Y = \$988|X =$ $\S 9 6 8 ) = 0 . 4 0$ . However, the marginal distribution of the partner’s annual health care cost is $P ( Y =$ $\S 9 6 8 ) = 0 . 4 0 , P ( Y = \S 9 6 8 ) = 0 . 6 0$ . Thus, X and Y are not independent.

This can also be demonstrated from examining the joint distribution, as shown in Figure 3.26. The probability that the employee’s cost and partner’s cost are both \$968 is 0.18. The marginal probabilities $P ( X = 5 9 6 8 )$ and $P ( Y = \S 9 6 8 )$ , respectively, are 0.30 and 0.40. Since $(0.40)(0.30) \neq$ 0.18, X and Y are dependent random variables.

Note that demonstrating $P ( Y = y _ { j } | X = x _ { i } ) = P ( Y = y _ { j } )$ or $P ( Y = y _ { j }$ and $X = x _ { i } ) = P ( Y = y _ { j } ) P ( X = x _ { i } )$ does not hold for any one $( x _ { i } , y _ { j } )$ pair is sufficient to prove that X and Y are not independent, since independence requires these conditions to hold over all pairs of values $( x _ { i } , y _ { j } )$

## GUIDED PRACTICE 3.51

Based on Figure 3.27, check whether X and Y are independent.<sup>34</sup>

Two random variables that are not independent are called **correlated random variables**. The correlation between two random variables is a measure of the strength of the relationship between them, just as it was for pairs of data points explored in Section 1.6.1. There are many examples of correlated random variables, such as height and weight in a population of individuals, or the gestational age and birth weight of newborns.

When two random variables are positively correlated, they tend to increase or decrease together. If one of the variables increases while the other decreases (or vice versa) they are negatively correlated. Correlation is easy to identify in a scatterplot, but is more difficult to identify in a table of a joint distribution. Fortunately, there is a formula to calculate correlation for a joint distribution specified in a table.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">34<sub>X</sub> and Y are not independent. One way to demonstrate this is to compare p<sub>X</sub>(1) with p<sub>X</sub>|Y (1|2). If X were independent of Y , then conditioning on Y = 2 should not provide any information about X, and p<sub>X</sub>(1) should equal p<sub>X</sub>|Y (1|2). However, p<sub>X</sub>(1) = 0.60 and p<sub>X</sub>|Y (1|2) = 0.80. Thus, X and Y are not independent.</span></small>

Correlation between random variables is similar to correlation between pairs of observations in a dataset, with some important differences. Calculating a correlation r in a dataset was introduced in Section 1.6.1 and uses the formula:

$$
r = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(\frac {x _ {i} - \overline {{x}}}{s _ {x}}\right) \left(\frac {y _ {i} - \overline {{y}}}{s _ {y}}\right). \tag {3.52}
$$

The correlation coefficient r is an average of products, with each term in the product measuring the distance between x and its mean x and the distance between $y$ and its mean $\overline { { y } } ,$ after the distances have been scaled by respective standard deviations.

The compact formula for the correlation between two random variables X and Y uses the same idea:

$$
\rho_ {X, Y} = E \left(\frac {X - \mu_ {x}}{\sigma_ {X}}\right) \left(\frac {Y - \mu_ {Y}}{\sigma_ {Y}}\right), \tag {3.53}
$$

where $\rho _ { X , Y }$ is the correlation between the two variables, and $\mu _ { X } , \mu _ { Y } , \sigma _ { X } , \sigma _ { Y }$ are the respective means and standard deviations for X and Y . Just as with the mean of a random variable, the expectation in the formula for correlation is a weighted sum of products, with each term weighted by the probability of values for the pair $( X , Y )$ . Equation 3.53 is useful for understanding the analogy between correlation of random variables and correlation of observations in a dataset, but it cannot be used to calculate $\rho _ { X , Y }$ without the probability weights. The weights come from the **joint distribution** of the pair of variables (X, Y ).

Equation 3.54 is an expansion of Equation 3.53. The double summation adds up terms over all combinations of the indices i and j.

$$
\rho_ {X, Y} = \sum_ {i} \sum_ {j} p (i, j) \frac {(x _ {i} - \mu_ {X})}{\mathrm{sd} (X)} \frac {(y _ {j} - \mu_ {Y})}{\mathrm{sd} (Y)}. \tag {3.54}
$$

## EXAMPLE 3.55

Compute the correlation between annual health care costs for the employee and her partner.

As calculated previously, $E(X)=\$1010,\;\mathrm{Var}(X)=1556,\;E(Y)=\$980,$ , and $\mathrm{Var}(Y) = 96$ . Thus, $S D ( X ) = \S 3 9 . 4 5$ and $S D ( Y ) = \S 9 . 8 0$

$$
\begin{array}{l} \rho_ {X, Y} = p (x _ {1}, y _ {1}) \frac {(x _ {1} - \mu_ {X})}{\mathrm{sd} (X)} \frac {(y _ {1} - \mu_ {Y})}{\mathrm{sd} (Y)} + p (x _ {1}, y _ {2}) \frac {(x _ {1} - \mu_ {X})}{\mathrm{sd} (X)} \frac {(y _ {2} - \mu_ {Y})}{\mathrm{sd} (Y)} \\ + \dots + p (x _ {4}, y _ {1}) \frac {(x _ {4} - \mu_ {X})}{\mathrm{sd} (X)} \frac {(y _ {1} - \mu_ {Y})}{\mathrm{sd} (Y)} + p (x _ {4}, y _ {2}) \frac {(x _ {4} - \mu_ {X})}{\mathrm{sd} (X)} \frac {(y _ {2} - \mu_ {Y})}{\mathrm{sd} (Y)} \\ = (0. 1 8) \frac {(9 6 8 - 1 0 1 0)}{3 9 . 4 5} \frac {(9 6 8 - 9 8 0)}{9 . 8} + (0. 1 2) \frac {(9 6 8 - 1 0 1 0)}{3 9 . 4 5} \frac {(9 8 8 - 9 8 0)}{9 . 8} \\ + \dots + (0. 0 3) \frac {(1 1 0 8 - 1 0 1 0)}{3 9 . 4 5} \frac {(9 6 8 - 9 8 0)}{9 . 8} + (0. 0 7) \frac {(1 1 0 8 - 1 0 1 0)}{3 9 . 4 5} \frac {(9 8 8 - 9 8 0)}{9 . 8} \\ = 0. 2 2. \\ \end{array}
$$

The correlation between annual health care costs for these two individuals is positive. It is reasonable to expect that there might be a positive correlation in health care costs for two individuals in a relationship; for example, if one person contracts the flu, then it is likely the other person will also contract the flu, and both may need to see a doctor.

![](images/page_181_image_2.jpg)

## GUIDED PRACTICE 3.56

Based on Figure 3.27, compute the correlation between X and Y . For your convenience, the following values are provided: $E(X)=2.2,\mathrm{Var}(X)=2.16,E(Y)=1.5,\mathrm{Var}(Y)=0.25.^{35}$

When two random variables X and Y are correlated:

$$
\text {Variance} (X + Y) = \text {Variance} (X) + \text {Variance} (Y) + 2 \sigma_ {X} \sigma_ {Y} \text {Correlation} (X, Y) \tag {3.57}
$$

$$
\text {Variance} (X - Y) = \text {Variance} (X) + \text {Variance} (Y) - 2 \sigma_ {X} \sigma_ {Y} \text {Correlation} (X, Y). \tag {3.58}
$$

When random variables are positively correlated the variance of the sum or the difference of two variables will be larger than the sum of the two variances. When they are negatively correlated the variance of the sum or difference will be smaller than the sum of the two variances.

The standard deviation for the sum or difference will always be the square root of the variance.

## EXAMPLE 3.59

Calculate the standard deviation of the sum of the health care costs for the couple.

This calculation uses Equation 3.57 to calculate the variance of the sum. The standard deviation will be the square root of the variance.

![](images/page_181_image_13.jpg)

$$
\begin{array}{l} \mathrm{Var} (X + Y) = \mathrm{Var} (X) + \mathrm{Var} (Y) + 2 \sigma_ {X} \sigma_ {Y} \rho_ {X, Y} \\ = (1 5 5 6 + 9 6) + (2) (3 9. 4 5) (9. 8 0) (0. 2 2) \\ = 1 8 2 2. 1 0. \\ \end{array}
$$

The standard deviation is ${ \sqrt { 1 8 2 2 . 1 0 } } = 5 4 2 . 6 9 .$ . Because the health care costs are correlated, the standard deviation of the total cost is larger than the value calculated in Example 3.8 under the assumption that the annual costs were independent.

![](images/page_181_image_16.jpg)

## GUIDED PRACTICE 3.60

Compute the standard deviation of X − Y for the pair of random variables shown in Figure 3.27.<sup>36</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">35The correlation between X and Y is ρX,Y = (0.20) (1−2.2)(1−1.5)+ · · · + (0.10) (4−2.2)(2−1.5) = −0.0208. √2.16 √0.25 √2.16 √0.25 36<sub>Var</sub>(X − Y ) = Var(X) + Var(Y ) − 2σ<sub>X</sub>σ<sub>Y</sub> ρ<sub>X</sub>,Y = 2.16 + 0.25 − 2(√2.16)(√0.25)(−0.0208) = 2.44. Thus, SD(X − Y ) = √2.44 = 1.56.</span></small>

## EXAMPLE 3.61

The Association of American Medical Colleges (AAMC) introduced a new version of the Medical College Admission Test (MCAT) in the spring of 2015. Data from the scores were recently released by $\dot{ AAMC. }^{37}$ The test consists of 4 components: chemical and physical foundations of biological systems; critical analysis and reasoning skills; biological and biochemical foundations of living systems; psychological, social and biological foundations of behavior. The overall score is the sum of the individual component scores. The grading for each of the four components is scaled so that the mean score is 125. The means and standard deviations for the four components and the total scores for the population taking the exam in May 2015 exam are shown in Figure 3.28.

Show that the standard deviation in the table for the total score does not agree with that obtained under the assumption of independence.

The variance of each component of the score is the square of each standard deviation. Under the assumption of independence, the variance of the total score would be

$$
\begin{array}{l} \text {Var(Total Score)} = 3. 0 ^ {2} + 3. 0 ^ {2} + 3. 0 ^ {2} + 3. 1 ^ {2} \\ = 3 6. 6 1, \\ \end{array}
$$

so the standard deviation is 6.05, which is less than 10.6.

Since the observed standard deviation is larger than that calculated under independence, this suggests the component scores are positively correlated.

It would not be reasonable to expect that the component scores are independent. Think about a student taking the MCAT exam: someone who scores well on one component of the exam is likely to score well on the other parts.

| Component | Mean | Standard Deviation |
| --- | --- | --- |
| Chem. Phys. Found. | 125 | 3.0 |
| Crit. Analysis | 125 | 3.0 |
| Living Systems | 125 | 3.0 |
| Found. Behavior | 125 | 3.1 |
| Total Score | 500 | 10.6 |

Figure 3.28: Means and Standard Deviations for MCAT Scores

## 3.7 Notes

Thinking in terms of random variables and distributions of probabilities makes it easier to describe all possible outcomes of an experiment or process of interest, versus only considering probabilities on the scale of individual outcomes or sets of outcomes. Several of the fundamental concepts of probability can naturally be extended to probability distributions. For example, the process of obtaining a conditional distribution is analogous to the one for calculating a conditional probability.

Many processes can be modeled using a specific named distribution. The statistical techniques discussed in later chapters, such as hypothesis testing and regression, are often based on particular distributional assumptions. In particular, many methods rely on the assumption that data are normally distributed.

The discussion of random variables and their distribution provided in this chapter only represents an introduction to the topic. In this text, properties of random variables such as expected value or correlation are presented in the context of discrete random variables; these concepts are also applicable to continuous random variables. A course in probability theory will cover additional named distributions as well as more advanced methods for working with distributions.

Lab 1 introduces the general notion of a random variable and its distribution using a simulation, then discusses the binomial distribution. Lab 2 discusses the normal distribution and working with normal probabilities, as well as the Poisson distribution. Lab 3 covers the geometric, negative binomial, and hypergeometric distributions. All three labs include practice problems that illustrate the use of R functions for probability distributions and introduce additional features of the R programming language. Lab 4 discusses distributions for pairs of random variables and some R functions useful for matrix calculations.

## 3.8 Exercises

## 3.8.1 Random variables

**3.1 College smokers.** At a university, 13% of students smoke.

(a) Calculate the expected number of smokers in a random sample of 100 students from this university.
(b) The university gym opens at 9 am on Saturday mornings. One Saturday morning at 8:55 am there are 27 students outside the gym waiting for it to open. Should you use the same approach from part (a) to calculate the expected number of smokers among these 27 students?

**3.2 Ace of clubs wins.** Consider the following card game with a well-shuffled deck of cards. If you draw a red card, you win nothing. If you get a spade, you win \$5. For any club, you win \$10 plus an extra \$20 for the ace of clubs.

(a) Create a probability model for the amount you win at this game. Also, find the expected winnings for a single game and the standard deviation of the winnings.
(b) What is the maximum amount you would be willing to pay to play this game? Explain your reasoning.

**3.3 Hearts win.** In a new card game, you start with a well-shuffled full deck and draw 3 cards without replacement. If you draw 3 hearts, you win \$50. If you draw 3 black cards, you win \$25. For any other draws, you win nothing.

(a) Create a probability model for the amount you win at this game, and find the expected winnings. Also compute the standard deviation of this distribution.
(b) If the game costs \$5 to play, what would be the expected value and standard deviation of the net profit (or loss)?
(c) If the game costs \$5 to play, should you play this game? Explain.

**3.4 Baggage fees.** An airline charges the following baggage fees: \$25 for the first bag and \$35 for the second. Suppose 54% of passengers have no checked luggage, 34% have one piece of checked luggage and 12% have two pieces. We suppose a negligible portion of people check more than two bags.

(a) Build a probability model, compute the average revenue per passenger, and compute the corresponding standard deviation.
(b) About how much revenue should the airline expect for a flight of 120 passengers? With what standard deviation? Note any assumptions you make and if you think they are justified.

**3.5 Gull clutch size.** Large black-tailed gulls usually lay one to three eggs, and rarely have a fourth egg clutch. It is thought that clutch sizes are effectively limited by how effectively parents can incubate their eggs. Suppose that on average, gulls have a 25% of laying 1 egg, 40% of laying 2 eggs, 30% chance of laying 3 eggs, and 5% chance of laying 4 eggs.

(a) Calculate the expected number of eggs laid by a random sample of 100 gulls.
(b) Calculate the standard deviation of the number of eggs laid by a random sample of 100 gulls.

**3.6 Scooping ice cream.** Ice cream usually comes in 1.5 quart boxes (48 fluid ounces), and ice cream scoops hold about 2 ounces. However, there is some variability in the amount of ice cream in a box as well as the amount of ice cream scooped out. We represent the amount of ice cream in the box as X and the amount scooped out as Y . Suppose these random variables have the following means, standard deviations, and variances:

|  | mean | SD | variance |
| --- | --- | --- | --- |
| X | 48 | 1 | 1 |
| Y | 2 | 0.25 | 0.0625 |

(a) An entire box of ice cream, plus 3 scoops from a second box is served at a party. How much ice cream do you expect to have been served at this party? What is the standard deviation of the amount of ice cream served?
(b) How much ice cream would you expect to be left in the box after scooping out one scoop of ice cream? That is, find the expected value of X − Y . What is the standard deviation of the amount left in the box?
(c) Using the context of this exercise, explain why we add variances when we subtract one random variable from another.

## 3.8.2 Binomial distribution

**3.7 Underage drinking, Part I.** Data collected by the Substance Abuse and Mental Health Services Adminis tration (SAMSHA) suggests that 69.7% of 18-20 year olds consumed alcoholic beverages in any given year.<sup>38</sup>

(a) Suppose a random sample of ten 18-20 year olds is taken. Is the use of the binomial distribution appropriate for calculating the probability that exactly six consumed alcoholic beverages? Explain.
(b) Calculate the probability that exactly 6 out of 10 randomly sampled 18- 20 year olds consumed an alcoholic drink.
(c) What is the probability that exactly four out of ten 18-20 year olds have not consumed an alcoholic beverage?
(d) What is the probability that at most 2 out of 5 randomly sampled 18-20 year olds have consumed alcoholic beverages?
(e) What is the probability that at least 1 out of 5 randomly sampled 18-20 year olds have consumed alcoholic beverages?

**3.8 Chickenpox, Part I.** The US CDC estimates that 90% of Americans have had chickenpox by the time they reach adulthood.

(a) Suppose we take a random sample of 100 American adults. Is the use of the binomial distribution appropriate for calculating the probability that exactly 97 out of 100 randomly sampled American adults had chickenpox during childhood? Explain.
(b) Calculate the probability that exactly 97 out of 100 randomly sampled American adults had chickenpox during childhood.
(c) What is the probability that exactly 3 out of a new sample of 100 American adults have not had chickenpox in their childhood?
(d) What is the probability that at least 1 out of 10 randomly sampled American adults have had chickenpox?
(e) What is the probability that at most 3 out of 10 randomly sampled American adults have not had chickenpox?

**3.9 Underage drinking, Part II.** We learned in Exercise 3.7 that about 70% of 18-20 year olds consumed alcoholic beverages in any given year. We now consider a random sample of fifty 18-20 year olds.

(a) How many people would you expect to have consumed alcoholic beverages? And with what standard deviation?
(b) Would you be surprised if there were 45 or more people who have consumed alcoholic beverages?
(c) What is the probability that 45 or more people in this sample have consumed alcoholic beverages? How does this probability relate to your answer to part (b)?

**3.10 Chickenpox, Part II.** We learned in Exercise 3.8 that about 90% of American adults had chickenpox before adulthood. We now consider a random sample of 120 American adults.

(a) How many people in this sample would you expect to have had chickenpox in their childhood? And with what standard deviation?
(b) Would you be surprised if there were 105 people who have had chickenpox in their childhood?
(c) What is the probability that 105 or fewer people in this sample have had chickenpox in their childhood? How does this probability relate to your answer to part (b)?

**3.11 Donating blood.** When patients receive blood transfusions, it is critical that the blood type of the donor is compatible with the patients, or else an immune system response will be triggered. For example, a patient with Type O- blood can only receive Type O- blood, but a patient with Type O+ blood can receive either Type O+ or Type O-. Furthermore, if a blood donor and recipient are of the same ethnic background, the chance of an adverse reaction may be reduced. According to a 10-year donor database, 0.37 of white, non-Hispanic donors are O+ and 0.08 are O-.

(a) Consider a random sample of 15 white, non-Hispanic donors. Calculate the expected value of individuals who could be a donor to a patient with Type O+ blood. With what standard deviation?
(b) What is the probability that 3 or more of the people in this sample could donate blood to a patient with Type O- blood?

**3.12 Sickle cell anemia.** Sickle cell anemia is a genetic blood disorder where red blood cells lose their flexibility and assume an abnormal, rigid, “sickle" shape, which results in a risk of various complications. If both parents are carriers of the disease, then a child has a 25% chance of having the disease, 50% chance of being a carrier, and 25% chance of neither having the disease nor being a carrier. If two parents who are carriers of the disease have 3 children, what is the probability that

(a) two will have the disease?
(b) none will have the disease?
(c) at least one will neither have the disease nor be a carrier?
(d) the first child with the disease will the be 3<sup>rd</sup> child?

**3.13 Hepatitis C.** Hepatitis C is spread primarily through contact with the blood of an infected person, and is nearly always transmitted through needle sharing among intravenous drug users. Suppose that in a month’s time, an IV drug user has a 30% chance of contracting hepatitis C through needle sharing. What is the probability that 3 out of 5 IV drug users contract hepatitis C in a month? Assume that the drug users live in different parts of the country.

**3.14 Arachnophobia.** A Gallup Poll found that 7% of teenagers (ages 13 to 17) suffer from arachnophobia and are extremely afraid of spiders. At a summer camp there are 10 teenagers sleeping in each tent. Assume that these 10 teenagers are independent of each other.<sup>39</sup>

(a) Calculate the probability that at least one of them suffers from arachnophobia.
(b) Calculate the probability that exactly 2 of them suffer from arachnophobia.
(c) Calculate the probability that at most 1 of them suffers from arachnophobia.
(d) If the camp counselor wants to make sure no more than 1 teenager in each tent is afraid of spiders, does it seem reasonable for him to randomly assign teenagers to tents?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">39<sub>Gallup</sub> Poll, [What Frightens America’s Youth?](http://www.openintro.org/redirect.php?go=textbook-frightens_youth_2005&referrer=biostat1_pdf), March 29, 2005.</span></small>

**3.15 Wolbachia infection.** Approximately 12,500 stocks of Drosophila melanogaster flies are kept at The Bloomington Drosophila Stock Center for research purposes. A 2006 study examined how many stocks were infected with Wolbachia, an intracellular microbe that can manipulate host reproduction for its own benefit. About 30% of stocks were identified as infected. Researchers working with infected stocks should be cautious of the potential confounding effects that Wolbachia infection may have on experiments. Consider a random sample of 250 stocks.

(a) Calculate the probability that exactly 60 stocks are infected.
(b) Calculate the probability that at most 60 stocks are infected.
(c) Calculate the probability that at least 80 stocks are infected.
(d) If a researcher wants to make sure that no more than 40% of the stocks used for an experiment are infected, does it seem reasonable to take a random sample of 250?

**3.16 Male children.** While it is often assumed that the probabilities of having a boy or a girl are the same, the actual probability of having a boy is slightly higher at 0.51. Suppose a couple plans to have 3 kids.

(a) Use the binomial model to calculate the probability that two of them will be boys.
(b) Write out all possible orderings of 3 children, 2 of whom are boys. Use these scenarios to calculate the same probability from part (a) but using the addition rule for disjoint outcomes. Confirm that your answers from parts (a) and (b) match.
(c) If we wanted to calculate the probability that a couple who plans to have 8 kids will have 3 boys, briefly describe why the approach from part (b) would be more tedious than the approach from part (a).

**3.17 Hyponatremia.** Hyponatremia (low sodium levels) occurs in a certain proportion of marathon runners during a race. Suppose that historically, the proportion of runners who develop hyponatremia is 0.12. In a certain marathon, there are 200 runners participating.

(a) How many cases of hyponatremia are expected during the marathon?
(b) What is the probability of more than 30 cases of hyponatremia occurring?

**3.18 Sleep deprivation.** Consider a senior Statistics concentrator with a packed extracurricular schedule, taking five classes, and writing a thesis. Each time she takes an exam, she either scores very well (at least two standard deviations above the mean) or does not. Her performance on any given exam depends on whether she is operating on a reasonable amount of sleep the night before (more than 7 hours), relatively little sleep (between 4 - 7 hours, inclusive), or practically no sleep (less than 4 hours).

When she has had practically no sleep, she scores very well about 30% of the time. When she has had relatively little sleep, she scores very well 40% of the time. When she has had a reasonable amount of sleep, she scores very well 42% of the time. Over the course of a semester, she has a reasonable amount of sleep 50% of nights, and practically no sleep 30% of nights.

(a) What is her overall probability of scoring very well on an exam?
(b) What is the probability she had practically no sleep the night before an exam where she scored very well?
(c) Suppose that one day she has three exams scheduled. What is the probability that she scores very well on exactly two of the exams, under the assumption that her performance on each exam is independent of her performance on another exam?
(d) What is the probability that she had practically no sleep the night prior to a day when she scored very well on exactly two out of three exams?

## 3.8.3 Normal distribution

**3.19 Area under the curve, Part I.** What percent of a standard normal distribution $N ( \mu = 0 , \sigma = 1 )$ is found in each region? Be sure to draw a graph.

(a) $Z < - 1 . 3 5$

(b) $Z > 1 . 4 8$

(c) $- 0 . 4   <   Z   <   1 . 5$

(d) $| Z | > 2$

**3.20 Area under the curve, Part II.** What percent of a standard normal distribution $N ( \mu = 0 , \sigma = 1 )$ is found in each region? Be sure to draw a graph.

(a) $Z > - 1 . 1 3$

(b) $Z < 0 . 1 8$

(c) $Z > 8$

(d) $| Z | < 0 . 5$

**3.21 The standard normal distribution.** Consider the standard normal distribution with mean $\mu = 0$ and standard deviation $\sigma = 1$

(a) What is the probability that an outcome Z is greater than 2.60?
(b) What is the probability that Z is less than 1.35?
(c) What is the probability that Z is between -1.70 and 3.10?
(d) What value of Z cuts off the upper 15% of the distribution?
(e) What value of Z marks off the lower 20% of the distribution?

**3.22 Triathlon times.** In triathlons, it is common for racers to be placed into age and gender groups. The finishing times of men ages 30-34 has mean of 4,313 seconds with a standard deviation of 583 seconds. The finishing times of the women ages 25-29 has a mean of 5,261 seconds with a standard deviation of 807 seconds. The distribution of finishing times for both groups is approximately normal. Note that a better performance corresponds to a faster finish.

(a) If a man of the 30-34 age group finishes the race in 4,948 seconds, what percent of the triathletes in the group did he finish faster than?
(b) If a woman of the 25-29 age group finishes the race in 5,513 seconds, what percent of the triathletes in the group did she finish faster than?
(c) Calculate the cutoff time for the fastest 5% of athletes in the men’s group.
(d) Calculate the cutoff time for the slowest 10% of athletes in the women’s group.

**3.23 GRE scores.** The Graduate Record Examination (GRE) is a standardized test commonly taken by graduate school applicants in the United States. The total score is comprised of three components: Quantitative Reasoning, Verbal Reasoning, and Analytical Writing. The first two components are scored from 130 - 170. The mean score for Verbal Reasoning section for all test takers was 151 with a standard deviation of 7, and the mean score for the Quantitative Reasoning was 153 with a standard deviation of 7.67. Suppose that both distributions are nearly normal.

(a) A student scores 160 on the Verbal Reasoning section and 157 on the Quantitative Reasoning section. Relative to the scores of other students, which section did the student perform better on?
(b) Calculate the student’s percentile scores for the two sections. What percent of test takers performed better on the Verbal Reasoning section?
(c) Compute the score of a student who scored in the $8 0 ^ { t h }$ percentile on the Quantitative Reasoning section.
(d) Compute the score of a student who scored worse than 70% of the test takers on the Verbal Reasoning section.

**3.24 Osteoporosis.** The World Health Organization defines osteoporosis in young adults as a measured bone mineral density 2.5 or more standard deviations below the mean for young adults. Assume that bone mineral density follows a normal distribution in young adults. What percentage of young adults suffer from osteoporosis according to this criterion?

**3.25 LA weather.** The average daily high temperature in June in LA is $7 7 ^ { \circ } \mathrm { F }$ with a standard deviation of 5◦F. Suppose that the temperatures in June closely follow a normal distribution.

(a) What is the probability of observing an $8 3 ^ { \circ } \mathrm { F }$ temperature or higher in LA during a randomly chosen day in June?
(b) How cold are the coldest 10% of the days during June in LA?

**3.26 Clutch volume.** A study investigating maternal investment in a frog species found on the Tibetan Plateau reported data on the volume of egg clutches measured across 11 study sites. The distribution is roughly normal, with approximate distribution N(882.5,380) mm<sup>3</sup>.

(a) What is the probability of observing an egg clutch between volume 700-800 $m m ^ { 3 } ?$

(b) How large are the largest 5% of egg clutches?

**3.27 Glucose levels.** Fasting blood glucose levels for normal non-diabetic individuals are normally distributed in the population, with mean $\mu = 85\  mg/dL$ and standard deviation $\sigma = 7 . 5 \; \mathrm { m g / d L }$

(a) What is the probability that a randomly chosen member of the population has a fasting glucose level higher than 100 mg/dL?
(b) What value of fasting glucose level defines the lower $5 ^ { t h }$ percentile of the distribution?

**3.28 Arsenic poisoning.** Arsenic blood concentration is normally distributed with mean $\mu = 3 . 2 \; \mu \mathrm { g / d l }$ and standard deviation $\sigma = 1 . 5 ~ \mu \mathrm { g / d l }$ . What range of arsenic blood concentration defines the middle 95% of this distribution?

**3.29 Age at childbirth.** In the last decade, the average age of a mother at childbirth is 26.4 years, with standard deviation 5.8 years. The distribution of age at childbirth is approximately normal.

(a) What proportion of women who give birth are 21 years of age or older?
(b) Giving birth at what age puts a woman in the upper 2.5% of the age distribution?

**3.30 Find the SD.** Find the standard deviation of the distribution in the following situations.

(a) MENSA is an organization whose members have IQs in the top 2% of the population. IQs are normally distributed with mean 100, and the minimum IQ score required for admission to MENSA is 132.
(b) Cholesterol levels for women aged 20 to 34 follow an approximately normal distribution with mean 185 milligrams per deciliter (mg/dl). Women with cholesterol levels above 220 mg/dl are considered to have high cholesterol and about 18.5% of women fall into this category.

**3.31 Underage drinking, Part III.** As first referenced in Exercise 3.7, about 70% of 18-20 year olds consumed alcoholic beverages in 2008. Consider a random sample of fifty 18-20 year olds.

(a) Of these fifty people, how many would be expected to have consumed alcoholic beverages? With what standard deviation?
(b) Evaluate the conditions for using the normal approximation to the binomial. What is the probability that 45 or more people in this sample have consumed alcoholic beverages?

**3.32 Chickenpox, Part III.** As first referenced in Exercise 3.8, about 90% of American adults had chickenpox before adulthood. Consider a random sample of 120 American adults.

(a) How many people in this sample would be expected to have had chickenpox in their childhood? With what standard deviation?
(b) Evaluate the conditions for using the normal approximation to the binomial. What is the probability that 105 or fewer people in this sample have had chickenpox in their childhood?

**3.33 University admissions.** Suppose a university announced that it admitted 2,500 students for the following year’s freshman class. However, the university has dorm room spots for only 1,786 freshman students. If there is a 70% chance that an admitted student will decide to accept the offer and attend this university, what is the approximate probability that the university will not have enough dormitory room spots for the freshman class?
**3.34 SAT scores.** SAT scores (out of 2400) are distributed normally with a mean of 1500 and a standard deviation of 300. Suppose a school council awards a certificate of excellence to all students who score at least 1900 on the SAT, and suppose we pick one of the recognized students at random. What is the probability this student’s score will be at least 2100? (The material covered in Section 2.2 would be useful for this question.)
**3.35 Scores on stats final.** The final exam scores of 20 introductory statistics students are plotted below. Do these data appear to follow a normal distribution? Explain your reasoning.

![](images/page_190_image_6.jpg)

**3.36 Heights of female college students.** The heights of 25 female college students are plotted below. Do these data appear to follow a normal distribution? Explain your reasoning.

![](images/page_190_image_8.jpg)

## 3.8.4 Poisson distribution

**3.37 Computing Poisson probabilities.** This is a simple exercise in computing probabilities for a Poisson random variable. Suppose that X is a Poisson random variable with rate parameter $\lambda = 2 .$ Calculate $P ( X = 2 )$ $P ( X \leq 2 )$ , and $P ( X \geq 3 )$
**3.38 Stenographer’s typos.** A very skilled court stenographer makes one typographical error (typo) per hour on average.

(a) What are the mean and the standard deviation of the number of typos this stenographer makes in an hour?
(b) Calculate the probability that this stenographer makes at most 3 typos in a given hour.
(c) Calculate the probability that this stenographer makes at least 5 typos over 3 hours.

**3.39 Customers at a coffee shop.** A coffee shop serves an average of 75 customers per hour during the morning rush.

(a) What are the mean and the standard deviation of the number of customers this coffee shop serves in one hour during this time of day?
(b) Would it be considered unusually low if only 60 customers showed up to this coffee shop in one hour during this time of day?
(c) Calculate the probability that this coffee shop serves 70 customers in one hour during this time of day.

**3.40 Osteosarcoma in NYC.** Osteosarcoma is a relatively rare type of bone cancer. It occurs most often in young adults, age 10 - 19; it is diagnosed in approximately 8 per 1,000,000 individuals per year in that age group. In New York City (including all five boroughs), the number of young adults in this age range is approximately 1,400,000.

(a) What is the expected number of cases of osteosarcoma in NYC in a given year?
(b) What is the probability that 15 or more cases will be diagnosed in a given year?
(c) The largest concentration of young adults in NYC is in the borough of Brooklyn, where the population in that age range is approximately 450,000. What is the probability of 10 or more cases in Brooklyn in a given year?
(d) Suppose that in a given year, 10 cases of osteosarcoma were observed in NYC, with all 10 cases occurring among young adults living in Brooklyn. An official from the NYC Public Health Department claims that the probability of this event (that is, the probability of 10 or more cases being observed, and all of them occurring in Brooklyn) is what was calculated in part c). Is the official correct? Explain your answer. You may assume that your answer to part c) is correct. This question can be answered without doing any calculations.
(e) Suppose that over five years, there was one year in which 10 or more cases of osteosarcoma were observed in Brooklyn. Is the probability of this event equal to the probability calculated in part c)? Explain your answer.

**3.41 How many cars show up?** For Monday through Thursday when there isn’t a holiday, the average number of vehicles that visit a particular retailer between 2pm and 3pm each afternoon is 6.5, and the number of cars that show up on any given day follows a Poisson distribution.

(a) What is the probability that exactly 5 cars will show up next Monday?
(b) What is the probability that 0, 1, or 2 cars will show up next Monday between 2pm and 3pm?
(c) There is an average of 11.7 people who visit during those same hours from vehicles. Is it likely that the number of people visiting by car during this hour is also Poisson? Explain.

**3.42 Lost baggage.** Occasionally an airline will lose a bag. Suppose a small airline has found it can reasonably model the number of bags lost each weekday using a Poisson model with a mean of 2.2 bags.

(a) What is the probability that the airline will lose no bags next Monday?
(b) What is the probability that the airline will lose 0, 1, or 2 bags on next Monday?
(c) Suppose the airline expands over the course of the next 3 years, doubling the number of flights it makes, and the CEO asks you if it’s reasonable for them to continue using the Poisson model with a mean of 2.2. What is an appropriate recommendation? Explain.