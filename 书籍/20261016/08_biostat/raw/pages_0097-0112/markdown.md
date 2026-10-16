## 2.1.5 Probability distributions

A **probability distribution** consists of all disjoint outcomes and their associated probabilities. Figure 2.6 shows the probability distribution for the sum of two dice.

| Dice sum | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Probability | $\frac{1}{36}$ | $\frac{2}{36}$ | $\frac{3}{36}$ | $\frac{4}{36}$ | $\frac{5}{36}$ | $\frac{6}{36}$ | $\frac{5}{36}$ | $\frac{4}{36}$ | $\frac{3}{36}$ | $\frac{2}{36}$ | $\frac{1}{36}$ |

Figure 2.6: Probability distribution for the sum of two dice.

## RULES FOR A PROBABILITY DISTRIBUTION

A probability distribution is a list of all possible outcomes and their associated probabilities that satisfies three rules:

1. The outcomes listed must be disjoint.
2. Each probability must be between 0 and 1.
3. The probabilities must total to 1.

![](images/page_96_chart_12.jpg)

<details>
<summary>bar</summary>

| Dice sum | Probability |
| --- | --- |
| 2 | ~0.03 |
| 3 | ~0.055 |
| 4 | ~0.085 |
| 5 | ~0.11 |
| 6 | ~0.14 |
| 7 | ~0.17 |
| 8 | ~0.14 |
| 9 | ~0.11 |
| 10 | ~0.085 |
| 11 | ~0.055 |
| 12 | ~0.03 |
</details>

Figure 2.7: The probability distribution of the sum of two dice.

Probability distributions can be summarized in a bar plot. The probability distribution for the sum of two dice is shown in Figure 2.7, with the bar heights representing the probabilities of outcomes.

Figure 2.8 shows a bar plot of the birth weight data for 3,999,386 live births in the United States in 2010, for which total counts have been converted to proportions. Since birth weight trends do not change much between years, it is valid to consider the plot as a representation of the probability distribution of birth weights for upcoming years, such as 2017. The data are available as part of the US CDC National Vital Statistics System.<sup>11</sup>

The graph shows that while most babies born weighed between 2000 and 5000 grams (2 to 5 kg), there were both small (less than 1000 grams) and large (greater than 5000 grams) babies. Pediatricians consider birth weights between 2.5 and 5 kg as normal.<sup>12</sup> A probability distribution gives a sense of which outcomes can be considered unusual (i.e., outcomes with low probability).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11<a href="http://205.207.175.93/vitalstats/ReportFolders/reportFolders.aspx"><sub>http</sub>://205.207.175.93/vitalstats/ReportFolders/reportFolders.aspx</a></span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12<a href="https://www.nlm.nih.gov/medlineplus/birthweight.html"><sub>https</sub>://www.nlm.nih.gov/medlineplus/birthweight.html</a></span></small>

![](images/page_97_chart_2.jpg)

<details>
<summary>histogram</summary>

| Birth Weight (Grams) | Probability |
| --- | --- |
| 499 or less | ~0.001 |
| 500 – 999 | ~0.005 |
| 1000 – 1499 | ~0.008 |
| 1500 – 1999 | ~0.017 |
| 2000 – 2499 | ~0.052 |
| 2500 – 2999 | ~0.187 |
| 3000 – 3499 | ~0.392 |
| 3500 – 3999 | ~0.265 |
| 4000 – 4499 | ~0.067 |
| 4500 – 4999 | ~0.011 |
| 5000 – 8165 | ~0.001 |
| Not stated | ~0.001 |
</details>

Figure 2.8: Distribution of birth weights (in grams) of babies born in the US in 2010.

## Continuous probability distributions

Probability distributions for events that take on a finite number of possible outcomes, such as the sum of two dice rolls, are referred to as **discrete probability distributions**.

Consider how the probability distribution for adult heights in the US might best be represented. Unlike the sum of two dice rolls, height can occupy any value over a continuous range. Thus, height has a **continuous probability distribution**, which is specified by a **probability density function** rather than a table; Figure 2.9 shows a histogram of the height for 3 million US adults from the mid-1990’s, with an overlaid density curve.<sup>13</sup>

Just as in the discrete case, the probabilities of all possible outcomes must still sum to 1; the total area under a probability density function equals 1.

![](images/page_97_chart_8.jpg)

<details>
<summary>histogram</summary>

| Bin (cm) | Frequency |
| --- | --- |
| 135~140 | ~0.02 |
| 140~145 | ~0.05 |
| 145~150 | ~0.15 |
| 150~155 | ~0.45 |
| 155~160 | ~0.85 |
| 160~165 | ~1.15 |
| 165~170 | ~1.25 |
| 170~175 | ~1.15 |
| 175~180 | ~0.95 |
| 180~185 | ~0.75 |
| 185~190 | ~0.45 |
| 190~195 | ~0.20 |
| 195~200 | ~0.08 |
</details>

Figure 2.9: The continuous probability distribution of heights for US adults.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13<sub>This</sub> sample can be considered a simple random sample from the US population. It relies on the USDA Food Commodity Intake Database.</span></small>

## EXAMPLE 2.16

Estimate the probability that a randomly selected adult from the US population has height between 180 and 185 centimeters. In Figure 2.10(a), the two bins between 180 and 185 centimeters have counts of 195,307 and 156,239 people.

Find the proportion of the histogram’s area that falls in the range 180 cm and 185: add the heights of the bins in the range and divide by the sample size:

$$
\frac {1 9 5 , 3 0 7 + 1 5 6 , 2 3 9}{3 , 0 0 0 , 0 0 0} = 0. 1 1 7 2.
$$

The probability can be calculated precisely with the use of computing software, by finding the area of the shaded region under the curve between 180 and 185:

![](images/page_98_image_7.jpg)

Figure 2.10: (a) A histogram with bin sizes of 2.5 cm, with bars between 180 and 185 cm shaded. (b) Density for heights in the US adult population with the area between 180 and 185 cm shaded.

## EXAMPLE 2.17

What is the probability that a randomly selected person is **exactly** 180 cm? Assume that height can be measured perfectly.

This probability is zero. A person might be close to 180 cm, but not exactly 180 cm tall. This also coheres with the definition of probability as an area under the density curve; there is no area captured between 180 cm and 180 cm.

## GUIDED PRACTICE 2.18

Suppose a person’s height is rounded to the nearest centimeter. Is there a chance that a random person’s **measured** height will be 180 cm?14

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">14<sub>This</sub> has positive probability. Anyone between 179.5 cm and 180.5 cm will have a measured height of 180 cm. This a more realistic scenario to encounter in practice versus Example 2.17.</span></small>

## 2.1.6 Complement of an event

S Sample space A<sup>c</sup> Complement of outcome A

Rolling a die produces a value in the set $\{ 1 ,   2 ,   3 ,   4 ,   5 ,   6 \}$ . This set of all possible outcomes is called the **sample space** (S) for rolling a die.

Let $D = \{ 2 ,   3 \}$ represent the event that the outcome of a die roll is 2 or 3. The **complement** of D represents all outcomes in the sample space that are not in $D ,$ which is denoted by $D ^ { c } = \{ 1 ,   4 ,   5 ,$ $6 \}$ . That is, $D ^ { c }$ is the set of all possible outcomes not already included in D. Figure 2.11 shows the relationship between $D , D ^ { c }$ , and the sample space S.

![](images/page_99_image_6.jpg)

<details>
<summary>text_image</summary>

SAMPLE SPACE
EVENT D
EVENT Dᶜ
</details>

Figure 2.11: Event $D = \{ 2 ,   3 \}$ and its complement, $D ^ { c } = \{ 1 ,   4 ,   5 ,   6 \}$ . S represents the sample space, which is the set of all possible events.

![](images/page_99_image_8.jpg)

## GUIDED PRACTICE 2.19

(a) Compute P (D<sup>c</sup>) = P (rolling a 1, 4, 5, or 6). (b) What is $P ( D ) + P ( D ^ { c } ) ? ^ { 1 5 }$

![](images/page_99_image_11.jpg)

## GUIDED PRACTICE 2.20

Events $A = \{ 1 ,   2 \}$ and $B = \{ 4 ,   6 \}$ are shown in Figure 2.3 on page 94. (a) Write out what $A ^ { c }$ and $B ^ { c }$ represent. (b) Compute $P ( A ^ { c } )$ and $P ( B ^ { c } )$ . (c) Compute $P ( A ) + P ( A ^ { c } )$ and $P ( B ) + P ( B ^ { c } )$ 16

A complement of an event A is constructed to have two very important properties: every possible outcome not in A is in $A ^ { c } ,$ and A and $A ^ { c }$ are disjoint. If every possible outcome not in A is in $A ^ { c } ,$ , this implies that

$$
P (A \text {or} A ^ {c}) = 1. \tag {2.21}
$$

Then, by Addition Rule for disjoint events,

$$
P (A \text {or} A ^ {c}) = P (A) + P (A ^ {c}). \tag {2.22}
$$

Combining Equations (2.21) and (2.22) yields a useful relationship between the probability of an event and its complement.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">$^ { 1 5 } ( \mathtt { a } )$ The outcomes are disjoint and each has probability 1/6, so the total probability is $4 / 6 = 2 / 3 .$ (b) We can also see that $P(D)=\frac{1}{6}+\frac{1}{6}=1/3$ . Since D and $D ^ { c }$ are disjoint, $P ( D ) + P ( D ^ { c } ) = 1$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">16<sub>Br</sub>i<sub>ef</sub> solutions: (a) $A ^ { c } = \{ 3 ,   4 ,   5 ,   6 \}$ and $B ^ { c } = \{ 1 ,   2 ,   3 ,   5 \}$ (b) Noting that each outcome is disjoint, add the individual outcome probabilities to get $P ( A ^ { c } ) = 2 / 3$ and $P ( B ^ { c } ) = 2 / 3 .$ (c) A and $\check { A } ^ { c }$ are disjoint, and the same is true of B and $B ^ { c } .$ Therefore, $P(A)+P(A^{c})=1\mathrm{~and~}P(B)+P(B^{c})=1$</span></small>

## COMPLEMENT

The complement of event A is denoted $A ^ { c } ,$ and $A ^ { c }$ represents all outcomes not in A. A and $A ^ { c }$ are mathematically related:

$$
P (A) + P (A ^ {c}) = 1, \quad \text {i.e.} \quad P (A) = 1 - P (A ^ {c}). \tag {2.23}
$$

In simple examples, computing either A or $A ^ { c }$ is feasible in a few steps. However, as problems grow in complexity, using the relationship between an event and its complement can be a useful strategy.

## GUIDED PRACTICE 2.24

Let A represent the event of selecting an adult from the US population with height between 180 and 185 cm, as calculated in Example 2.16. What is $P ( A ^ { c } ) ? ^ { 1 7 }$

![](images/page_100_image_8.jpg)

## GUIDED PRACTICE 2.25

![](images/page_100_image_10.jpg)

Let A represent the event in which two dice are rolled and their total is less than 12. (a) What does the event $A ^ { c }$ represent? (b) Determine $P ( A ^ { c } )$ from Figure 2.6 on page 97. (c) Determine $P ( A )$ 18

![](images/page_100_image_12.jpg)

## GUIDED PRACTICE 2.26

Consider again the probabilities from Figure 2.6 and rolling two dice. Find the following probabilities: (a) The sum of the dice is not 6. (b) The sum is at least 4. That is, determine the probability of the event $B = \{ 4 ,   5 ,   . . . ,   1 2 \}$ . (c) The sum is no more than 10. That is, determine the probability of the event $D = \{ 2 ,   3 ,   . . . ,   1 \emptyset \} .$ <sup>19</sup>

## 2.1.7 Independence

Just as variables and observations can be independent, random phenomena can also be independent. Two processes are **independent** if knowing the outcome of one provides no information about the outcome of the other. For instance, flipping a coin and rolling a die are two independent processes – knowing that the coin lands heads up does not help determine the outcome of the die roll. On the other hand, stock prices usually move up or down together, so they are not independent.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">17<sub>P</sub> (A<sup>c</sup>) = 1 − P (A) = 1 − 0.1157 = 0.8843.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">18(a) The complement of A: when the total is equal to 12. (b) P (A<sup>c</sup>) = 1/36. (c) Use the probability of the complement from part (b), P (A<sup>c</sup>) = 1/36, and Equation (2.23): P (less than 12) = 1 − P (12) = 1 − 1/36 = 35/36.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">19(a) First find P (6) = 5/36, then use the complement: P (not 6) = 1 − P (6) = 31/36.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(b) First find the complement, which requires much less effort: P (2 or 3) = 1/36 + 2/36 = 1/12. Then calculate P (B) = 1 − P (B<sup>c</sup>) = 1 − 1/12 = 11/12.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(c) As before, finding the complement is the more direct way to determine P (D). First find P (D<sup>c</sup>) = P (11 or 12) = 2/36 + 1/36 = 1/12. Then calculate P (D) = 1 − P (D<sup>c</sup>) = 11/12.</span></small>

Example 2.3 provides a basic example of two independent processes: rolling two dice. What is the probability that both will be 1? Suppose one of the dice is blue and the other green. If the outcome of the blue die is a 1, it provides no information about the outcome of the green die. This question was first encountered in Example 2.3: $1 / 6 ^ { t h }$ of the time the blue die is a 1, and $1 / 6 ^ { t h }$ of those times the green die will also be 1. This is illustrated in Figure 2.12. Because the rolls are independent, the probabilities of the corresponding outcomes can be multiplied to obtain the final answer: ${ \big ( } 1 / 6 { \big ) } { \big ( } 1 / 6 { \big ) } = 1 / 3 6$ . This can be generalized to many independent processes.

![](images/page_101_chart_3.jpg)

<details>
<summary>bar</summary>

| Category | Outcomes of the Green Die |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 1 |
| 6 | 1 |
</details>

Figure 2.12: $1 / 6 ^ { t h }$ of the time, the first roll is a 1. Then $1 / 6 ^ { t h }$ of those times, the second roll will also be a 1.

Complicated probability problems, such as those that arise in biology or medicine, are often solved with the simple ideas used in the dice example. For instance, independence was used implicitly in the second solution to Example 2.4, when calculating the probability that two carriers will have an affected child with cystic fibrosis. Genes are typically passed along from the mother and father independently. This allows for the assumption that, on average, half of the offspring who receive a mutated gene copy from the mother will also receive a mutated copy from the father.

## GUIDED PRACTICE 2.27

What if there were also a red die independent of the other two? What is the probability of rolling the three dice and getting all $1 s _ { * } ^ { 2 0 }$

## GUIDED PRACTICE 2.28

Three US adults are randomly selected. The probability the height of a single adult is between 180 and 185 cm is 0.1157.<sup>21</sup>

(a) What is the probability that all three are between 180 and 185 cm tall?
(b) What is the probability that none are between 180 and 185 cm tall?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">20<sub>The</sub> same logic applies from Example 2.3. If 1/36<sup>th</sup> of the time the blue and green dice are both 1, then 1/6<sup>th</sup> of those times the red die will also be 1, so multiply:</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">P (blue = 1 and green = 1 and red = 1) = P (blue = 1)P (green = 1)P (red = 1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">= (1/6)(1/6)(1/6) = 1/216.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">21<sub>Brief</sub> answers: (a) 0.1157 × 0.1157 × 0.1157 = 0.0015. (b) (1 − 0.1157)<sup>3</sup> = 0.692.</span></small>

## MULTIPLICATION RULE FOR INDEPENDENT PROCESSES

If A and B represent events from two different and independent processes, then the probability that both A and B occur is given by:

$$
P (A \text {and} B) = P (A) P (B). \tag {2.29}
$$

Similarly, if there are $k$ events $A _ { 1 } ,   . . . ,   A _ { k }$ from k independent processes, then the probability they all occur is

$$
P (A _ {1}) P (A _ {2}) \dots P (A _ {k}).
$$

## EXAMPLE 2.30

**Mandatory drug testing.** Mandatory drug testing in the workplace is common practice for certain professions, such as air traffic controllers and transportation workers. A false positive in a drug screening test occurs when the test incorrectly indicates that a screened person is an illegal drug user. Suppose a mandatory drug test has a false positive rate of 1.2% (i.e., has probability 0.012 of indicating that an employee is using illegal drugs when that is not the case). Given 150 employees who are in reality drug free, what is the probability that at least one will (falsely) test positive? Assume that the outcome of one drug test has no effect on the others.

First, note that the complement of at least 1 person testing positive is that no one tests positive (i.e., all employees test negative). The multiplication rule can then be used to calculate the probability of 150 negative tests.

$$
\begin{array}{l} P (\text {At least 1"} +") = P (1 \text {or} 2 \text {or} 3 \dots \text {or} 1 5 0 \text {are"} +") \\ = 1 - P (\text {None are"} +") \\ = 1 - P (1 5 0 \text { are }" -") \\ = 1 - P ({" -"}) ^ {1 5 0} \\ = 1 - (0. 9 8 8) ^ {1 5 0} = 1 - 0. 1 6 = 0. 8 4. \\ \end{array}
$$

Even when using a test with a small probability of a false positive, the company is more than 80% likely to incorrectly claim at least one employee is an illegal drug user!

## GUIDED PRACTICE 2.31

Because of the high likelihood of at least one false positive in company wide drug screening programs, an individual with a positive test is almost always re-tested with a different screening test: one that is more expensive than the first, but has a lower false positive probability. Suppose the second test has a false positive rate of 0.8%. What is the probability that an employee who is not using illegal drugs will test positive on both tests?<sup>22</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">22<sub>The</sub> outcomes of the two tests are independent of one another; P (A and B) = P (A) × P (B), where events A and B are the results of the two tests. The probability of a false positive with the first test is 0.012 and 0.008 with the second. Thus, the probability of an employee who is not using illegal drugs testing positive on both tests is 0.012 × 0.008 = 9.6 × 10<sup>−5</sup></span></small>

![](images/page_103_chart_2.jpg)

Figure 2.13: Inheritance of ABO blood groups.

## EXAMPLE 2.32

**ABO blood groups.** There are four different common blood types (A, B, AB, and O), which are determined by the presence of certain antigens located on cell surfaces. Antigens are substances used by the immune system to recognize self versus non-self; if the immune system encounters antigens not normally found on the body’s own cells, it will attack the foreign cells. When patients receive blood transfusions, it is critical that the antigens of transfused cells match those of the patient’s, or else an immune system response will be triggered.

The ABO blood group system consists of four different blood groups, which describe whether an individual’s red blood cells carry the A antigen, B antigen, both, or neither. The ABO gene has three alleles: $I ^ { A } ,   I ^ { B } ,$ , and i. The i allele is recessive to both $I ^ { A }$ and $I ^ { B } ,$ , and does not produce antigens; thus, an individual with genotype $I ^ { A } i$ is blood group A and an individual with genotype $I ^ { B } i$ is blood group B. The $I ^ { A }$ and $I ^ { B }$ alleles are codominant, such that individuals of $I ^ { A } I ^ { B }$ genotype are AB. Individuals homozygous for the i allele are known as blood group $\mathrm { O } ,$ with neither A nor B antigens.

Suppose that both members of a couple have Group AB blood.

a) What is the probability that a child of this couple will have Group A blood?
b) What is the probability that they have two children with Group A blood?

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">a) An individual with Group AB blood is genotype $I ^ { A } I ^ { B }$ . Two $I ^ { A } I ^ { B }$ parents can produce children with genotypes $I ^ { A } I ^ { B } , \; I ^ { A } I ^ { A } , \; \mathrm { o r } ~ I ^ { B } I ^ { B }$ . Of these possibilities, only children with genotype $I ^ { A } I ^ { A }$ have Group A blood. Each parent has 0.5 probability of passing down their $I ^ { A }$ allele. Thus, the probability that a child of this couple will have Group A blood is P(parent 1 passes down $I ^ { A }$ allele) × P(parent 2 passes down $I ^ { A } { \mathrm { ~ a l l e l e } } ) = 0 . 5 \times 0 . 5 = 0 . 2 5$</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">b) Inheritance of alleles is independent between children. Thus, the probability of two children having Group A blood equals P(child 1 has Group A blood) × P(child 2 has group A blood). The probability of a child of this couple having Group A blood was previously calculated as 0.25. The answer is given by 0.25 × 0.25 = 0.0625.</span></small>

The previous examples in this section have used independence to solve probability problems. The definition of independence can also be used to check whether two events are independent – two events A and B are independent if they satisfy Equation (2.29).

## EXAMPLE 2.33

Is the event of drawing a heart from a deck of cards independent of drawing an ace?

The probability the card is a heart is $1 / 4   \left( 1 3 / 5 2   =   1 / 4 \right)$ and the probability that it is an ace is $1 / 1 3 \; \left( 4 / 5 2 = 1 / 1 3 \right)$ . The probability that the card is the ace of hearts (A♥) is 1/52. Check whether Equation 2.29 is satisfied:

$$
P (\heartsuit) P (\mathsf {A}) = \bigg (\frac {1}{4} \bigg) \bigg (\frac {1}{1 3} \bigg) = \frac {1}{5 2} = P (\heartsuit \text {and} \mathsf {A}).
$$

Since the equation holds, the event that the card is a heart and the event that the card is an ace are independent events.

## EXAMPLE 2.34

In the general population, about 15% of adults between 25 and 40 years of age are hypertensive. Suppose that among males of this age, hypertension occurs about 18% of the time. Is hypertension independent of sex?

Assume that the population is 50% male, 50% female; it is given in the problem that hypertension occurs about 15% of the time in adults between ages 25 and 40.

$$
P (\text {hypertension}) \times P (\text {male}) = (0. 1 5) (0. 5 0) = 0. 0 7 5 \neq 0. 1 8.
$$

Equation 2.29 is not satisfied, therefore hypertension is not independent of sex. In other words, knowing whether an individual is male or female is informative as to whether they are hypertensive. If hypertension and sex were independent, then we would expect hypertension to occur at an equal rate in males as in females.

## 2.2 Conditional probability

While it is difficult to obtain precise estimates, the US CDC estimated that in 2012, approximately 29.1 million Americans had type 2 diabetes – about 9.3% of the population.<sup>23</sup> A health care practitioner seeing a new patient would expect a 9.3% chance that the patient might have diabetes.

However, this is only the case if nothing is known about the patient. The prevalence of type 2 diabetes varies with age. Between the ages of 20 and 44, only about 4% of the population have diabetes, but almost 27% of people age 65 and older have the disease. Knowing the age of a patient provides information about the chance of diabetes; age and diabetes status are not independent. While the probability of diabetes in a randomly chosen member of the population is 0.093, the conditional probability of diabetes in a person known to be 65 or older is 0.27.

Conditional probability is used to characterize how the probability of an outcome varies with the knowledge of another factor or condition, and is closely related to the concepts of marginal and joint probabilities.

## 2.2.1 Marginal and joint probabilities

Figures 2.14 and 2.15 provide additional information about the relationship between diabetes prevalence and age.<sup>24</sup> Figure 2.14 is a contingency table for the entire US population in 2012; the values in the table are in thousands (to make the table more readable).

|  | Diabetes | No Diabetes | Sum |
| --- | --- | --- | --- |
| Less than 20 years | 200 | 86,664 | 86,864 |
| 20 to 44 years | 4,300 | 98,724 | 103,024 |
| 45 to 64 years | 13,400 | 68,526 | 81,926 |
| Greater than 64 years | 11,200 | 30,306 | 41,506 |
| Sum | 29,100 | 284,220 | 313,320 |

Figure 2.14: Contingency table showing type 2 diabetes status and age group, in thousands.

In the first row, for instance, Figure 2.14 shows that in the entire population of approximately 313,320,000 people, approximately 200,000 individuals were in the less than 20 years age group and diagnosed with diabetes – about 0.1%. The table also indicates that among the approximately 86,864,000 individuals less than 20 years of age, only 200,000 suffered from type 2 diabetes, approximately 0.2%. The distinction between these two statements is small but important. The first provides information about the size of the group with type 2 diabetes population that is less than 20 years of age, relative to the entire population. In contrast, the second statement is about the size of the diabetes population within the less than 20 years of age group, relative to the size of that age group.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">23<sub>21</sub> million of these cases are diagnosed, while the CDC predicts that 8.1 million cases are undiagnosed; that is, approximately 8.1 million people are living with diabetes, but they (and their physicians) are unaware that they have the condition.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">24<sub>Because</sub> the CDC provides only approximate numbers for diabetes prevalence, the numbers in the table are approximations of actual population counts.</span></small>

![](images/page_106_image_2.jpg)

## GUIDED PRACTICE 2.35

What fraction of the US population are 45 to 64 years of age and have diabetes? What fraction of the population age 45 to 64 have diabetes?<sup>25</sup>

The entries in Figure 2.15 show the proportions of the population in each of the eight categories defined by diabetes status and age, obtained by dividing each value in the cells of Figure 2.14 by the total population size.

|  | Diabetes | No Diabetes | Sum |
| --- | --- | --- | --- |
| Less than 20 years | 0.001 | 0.277 | 0.277 |
| 20 to 44 years | 0.014 | 0.315 | 0.329 |
| 45 to 64 years | 0.043 | 0.219 | 0.261 |
| Greater than 64 years | 0.036 | 0.097 | 0.132 |
| Sum | 0.093 | 0.907 | 1.000 |

Figure 2.15: Probability table summarizing diabetes status and age group.

If these proportions are interpreted as probabilities for randomly chosen individuals from the population, the value 0.014 in the first column of the second row implies that the probability of selecting someone at random who has diabetes and whose age is between 20 and 44 is 0.014, or 1.4%. The entries in the eight main table cells (i.e., excluding the values in the margins) are **joint probabilities**, which specify the probability of two events happening at the same time – in this case, diabetes and a particular age group. In probability notation, this joint probability can be expressed as 0.014 = P (diabetes and age 20 to 44).<sup>26</sup>

The values in the last row and column of the table are the sums of the corresponding rows or columns. The sum of the of the probabilities of the disjoint events (diabetes, age 20 to 44) and (no diabetes, age 20 to 44), 0.329, is the probability of being in the age group 20 to 44. The row and column sums are **marginal probabilities**; they are probabilities about only one type of event, such as age. For example, the sum of the first column (0.093) is the marginal probability of a member of the population having diabetes.

## MARGINAL AND JOINT PROBABILITIES

A marginal probability is a probability only related to a single event or process, such as P (A). A joint probability is the probability that two or more events or processes occur jointly, such as P (A and B).

![](images/page_106_image_12.jpg)

## GUIDED PRACTICE 2.36

What is the interpretation of the value 0.907 in the last row of the table? And of the value 0.097 directly above it?<sup>27</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">25<sub>The</sub> first value is given by the intersection of "45 - 64 years of age" and "diabetes", divided by the total population number: 13,400,000/313,320,000 = 0.043. The second value is given by dividing 13,400,000 by 81,926,000, the number of individuals in that age group: 13,400,000/81,926,000 = 0.164.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">26<sub>Alternatively</sub>, this is commonly written as as P (diabetes, age 20 to 44), with a comma replacing “and”.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">27<sub>The</sub> value 0.907 in the last row indicates the total proportion of individuals in the population who do not have diabetes. The value 0.097 indicates the joint probability of not having diabetes and being in the greater than 64 years age group.</span></small>

## 2.2.2 Defining conditional probability

The probability that a randomly selected individual from the US has diabetes is 0.093, the sum of the first column in Figure 2.15. How does that probability change if it is known that the individual’s age is 64 or greater?

The conditional probability can be calculated from Figure 2.14, which shows that 11,200,000 of the 41,506,000 people in that age group have diabetes, so the likelihood that someone from that age group has diabetes is:

$$
\frac {1 1 , 2 0 0 , 0 0 0}{4 1 , 5 0 6 , 0 0 0} = 0. 2 7,
$$

or 27%. The additional information about a patient’s age allows for a more accurate estimate of the probability of diabetes.

Similarly, the conditional probability can be calculated from the joint and marginal proportions in Figure 2.15. Consider the main difference between the conditional probability versus the joint and marginal probabilities. Both the joint probability and marginal probabilities are proba bilities relative to the entire population. However, the conditional probability is the probability of having diabetes, relative only to the segment of the population greater than the age of 64.

Intuitively, the denominator in the calculation of a conditional probability must account for the fact that only a segment of the population is being considered, rather than the entire population. The conditional probability of diabetes given age 64 or older is simply the joint probability of having diabetes and being greater than 64 years of age divided by the marginal probability of being in that age group:

$$
\begin{array}{l} \frac {\text {prop. of population with diabetes, age 64 or greater}}{\text {prop. of population greater than age 64}} = \frac {1 1 , 2 0 0 , 0 0 0 / 3 1 3 , 3 2 0 , 0 0 0}{4 1 , 5 0 6 , 0 0 0 / 3 1 3 , 3 2 0 , 0 0 0} \\ = \frac {0 . 0 3 6}{0 . 1 3 2} \\ = 0. 2 7 0. \\ \end{array}
$$

This leads to the mathematical definition of conditional probability.

## CONDITIONAL PROBABILITY

The conditional probability of an event A given an event or condition B is:

$$
P (A | B) = \frac {P (A \text {and} B)}{P (B)}. \tag {2.37}
$$

![](images/page_107_image_14.jpg)

## GUIDED PRACTICE 2.38

Calculate the probability that a randomly selected person has diabetes, given that their age is between 45 and 64.<sup>28</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">28<sub>Let</sub> A be the event a person has diabetes, and B the event that their age is between 45 and 64. Use the information in P (A and B) 0.043 Figure 2.15 to calculate P (A|B). P (A|B) = = 0.165. P (B) 0.261</span></small>

![](images/page_108_image_2.jpg)

## GUIDED PRACTICE 2.39

Calculate the probability that a randomly selected person is between 45 and 64 years old, given that the person has diabetes.<sup>29</sup>

Conditional probabilities have similar properties to regular (unconditional) probabilities.

## SUM OF CONDITIONAL PROBABILITIES

Let $A _ { 1 } , . . . , A _ { k }$ represent all the disjoint outcomes for a variable or process. Then if B is an event, possibly for another variable or process, we have:

$$
P (A _ {1} | B) + \dots + P (A _ {k} | B) = 1.
$$

The rule for complements also holds when an event and its complement are conditioned on the same information:

$$
P (A | B) = 1 - P (A ^ {c} | B).
$$

![](images/page_108_image_11.jpg)

## GUIDED PRACTICE 2.40

Calculate the probability a randomly selected person is older than 20 years of age, given that the person has diabetes.<sup>30</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">29<sub>Again</sub>, let A be the event a person has diabetes, and B the event that their age is between 45 and 64. Find P (B|A). P (B|A) = P (A and B)= 0.043= 0.462. P (A) 0.093</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">30<sub>Let</sub> A be the event that a person has diabetes, and B be the event that their age is less than 20 years. The desired probability is P (B<sup>c</sup>|A) = 1 − P (B|A) = 1 −0.001. = 0.989. 0 093</span></small>

## 2.2.3 General multiplication rule

Section 2.1.7 introduced the Multiplication Rule for independent processes. Here, the **General Multiplication Rule** is introduced for events that might not be independent.

## GENERAL MULTIPLICATION RULE

If A and B represent two outcomes or events, then

$$
P (A \text {   and   } B) = P (A | B) P (B).
$$

It is useful to think of A as the outcome of interest and B as the condition.

This General Multiplication Rule is simply a rearrangement of the definition for conditional probability in Equation (2.37) on page 108.

## EXAMPLE 2.41

Suppose that among male adults between 25 and 40 years of age, hypertension occurs about 18% of the time. Assume that the population is 50% male, 50% female. What is the probability of randomly selecting a male with hypertension from the population of individuals 25-40 years of age?

Let A be the event that a person has hypertension, and B the event that they are a male adult between 25 and 40 years of age. P (A|B), the probability of hypertension given male sex, is 0.18. Thus, P (A and $B ) = ( 0 . 1 8 ) ( 0 . 5 0 ) = 0 . 0 9$

## 2.2.4 Independence and conditional probability

If two events are independent, knowing the outcome of one should provide no information about the other.

## EXAMPLE 2.42

Let X and Y represent the outcomes of rolling two dice. Use the formula for conditional probability to compute $P ( Y = 1 \mid X = 1 )$ . What is $P ( Y = 1 ) ?$ Is this different from $P ( Y = 1 \mid X = 1 ) ?$

$$
\frac {P (Y = 1 \text {and} X = 1)}{P (X = 1)} = \frac {1 / 3 6}{1 / 6} = 1 / 6.
$$

The probability $P ( Y = 1 ) = 1 / 6$ is the same as the conditional probability. The probability that $Y = 1$ was unchanged by knowledge about $X ,$ since the events $X$ and Y are independent.

Using the Multiplication Rule for independent events allows for a mathematical illustration of why the condition information has no influence in Example 2.42:

$$
\begin{array}{l} P (Y = 1 \mid X = 1) = \frac {P (Y = 1 \text {and} X = 1)}{P (X = 1)} \\ = \frac {P (Y = 1) P (X = 1)}{P (X = 1)} \\ = \quad P (Y = 1). \\ \end{array}
$$

This is a specific instance of the more general result that if two events A and B are independent, $P ( A | B ) = P ( A )$ as long as $P ( B ) > 0$ :

$$
\begin{array}{l} P (A | B) = \frac {P (A \text { and } B)}{P (B)} \\ = \frac {P (A) P (B)}{P (B)} \\ = P (A). \\ \end{array}
$$

G

## GUIDED PRACTICE 2.43

In the US population, about 45% of people are blood group O. Suppose that 40% of Asian people living in the US are blood group O, and that the Asian population in the United States is approximately 4%. Do these data suggest that blood group is independent of ethnicity?<sup>31</sup>

## 2.2.5 Bayes’ Theorem

This chapter began with a straightforward question – what are the chances that a woman with an abnormal (i.e., positive) mammogram has breast cancer? For a clinician, this question can be rephrased as the conditional probability that a woman has breast cancer, given that her mammogram is abnormal. This conditional probability is called the **positive predictive value** (PPV) of a mammogram. More concisely, if $A = \{ \mathbf { a }$ woman has breast cancer}, and $B = \left\{ \begin{aligned} { \mathfrak { a } } \end{aligned} \right.$ mammogram is positive}, the PPV of a mammogram is $P ( A | B )$

The characteristics of a mammogram (and other diagnostic tests) are given with the reverse conditional probabilities—the probability that the mammogram correctly returns a positive result if a woman has breast cancer, as well as the probability that the mammogram correctly returns a negative result if a woman does not have breast cancer. These are the probabilities $P ( B | A )$ and $P ( B ^ { c } | A ^ { c } )$ , respectively.

Given the probabilities $P ( B | A )$ and $P ( B ^ { c } | A ^ { c } )$ , as well as the marginal probability of disease $P ( A ) ,$ , how can the positive predictive value $P ( A | B )$ be calculated?

There are several possible strategies for approaching this type of problem—1) constructing tree diagrams, 2) using a purely algebraic approach using Bayes’ Theorem, and 3) creating contingency tables based on calculating conditional probabilities from a large, hypothetical population.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">31<sub>Let</sub> A represent blood group O, and B represent Asian ethnicity. Since P (A|B) = 0.40 does not equal P (A) = 0.45, the two events are not independent. Blood group does not seem to be independent of ethnicity.</span></small>

![](images/page_111_image_2.jpg)

## EXAMPLE 2.44

In Canada, about 0.35% of women over 40 will develop breast cancer in any given year. A common screening test for cancer is the mammogram, but it is not perfect. In about 11% of patients with breast cancer, the test gives a **false negative**: it indicates a woman does not have breast cancer when she does have breast cancer. Similarly, the test gives a **false positive** in 7% of patients who do not have breast cancer: it indicates these patients have breast cancer when they actually do not.32<sub>If</sub> a randomly selected woman over 40 is tested for breast cancer using a mammogram and the test is positive – that is, the test suggests the woman has cancer – what is the probability she has breast cancer?

Read on in the text for three solutions to this example.

## Example 2.44 Solution 1. Tree Diagram.

![](images/page_111_chart_7.jpg)

<details>
<summary>funnel</summary>

| Cancer Status | Mammogram | P-value |
| --- | --- | --- |
| cancer | positive | 0.89 |
| cancer | negative | 0.11 |
| no cancer | positive | 0.07 |
| no cancer | negative | 0.93 |
</details>

Figure 2.16: A tree diagram for breast cancer screening.

A **tree diagram** is a tool to organize outcomes and probabilities around the structure of data, and is especially useful when two or more processes occur in a sequence, with each process conditioned on its predecessors.

In Figure 2.16, the primary branches split the population by cancer status, and show the marginal probabilities 0.0035 and 0.9965 of having cancer or not, respectively. The secondary branches are conditioned on the primary branch and show conditional probabilities; for example, the top branch is the probability that a mammogram is positive given that an individual has cancer. The problem provides enough information to compute the probability of testing positive if breast cancer is present, since this probability is the complement of the probability of a false negative: $1 - 0 . 1 1 = 0 . 8 9$

Joint probabilities can be constructed at the end of each branch by multiplying the numbers from right to left, such as the probability that a woman tests positive given that she has breast cancer (abbreviated as BC), times the probability she has breast cancer:

$$
\begin{array}{l} P (\mathrm{BC} \text {and mammogram} ^ {+}) = P (\mathrm{mammogram} ^ {+} \mid \mathrm{BC}) \times P (\mathrm{BC}) \\ = (0. 8 9) (0. 0 0 3 5) = 0. 0 0 3 1 2. \\ \end{array}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">32<sub>The</sub> probabilities reported here were obtained using studies reported at [www.breastcancer.org](http://www.openintro.org/redirect.php?go=textbook-breastCancerDotOrg_20090831b&referrer=biostat1_pdf) and [www.ncbi.nlm.nih.gov/pmc/articles/PMC1173421](http://www.openintro.org/redirect.php?go=textbook-ncbi_nih_breast_cancer&referrer=biostat1_pdf).</span></small>