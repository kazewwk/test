Using the tree diagram allows for the information in the problem to be mapped out in a way that makes it easier to calculate the desired conditional probability. In this case, the diagram makes it clear that there are two scenarios in which someone can test positive: either testing positive when having breast cancer or by testing positive in the absence of breast cancer. To find the probability that a woman has breast cancer given that she tests positive, apply the conditional probability formula: divide the probability of testing positive when having breast cancer by the probability of testing positive.

The probability of a positive test result is the sum of the two corresponding scenarios:

$$
\begin{array}{l} P (\text {mammogram} ^ {+}) = P (\text {mammogram} ^ {+} \text {and has BC}) + P (\text {mammogram} ^ {+} \text {and no BC}) \\ = [ P (\text {mammogram} ^ {+} \mid \text {has BC}) \times P (\text {has BC}) ] + [ P (\text {mammogram} ^ {+} \mid \text {no BC}) \times P (\text {no BC}) ] \\ = (0. 0 0 3 5) (0. 8 9) + (0. 9 9 6 5) (0. 0 7) = 0. 0 7 2 8 8. \\ \end{array}
$$

Thus, if the mammogram screening is positive for a patient, the probability that the patient has breast cancer is given by:

$$
\begin{array}{l} P (\text {has BC} \mid \text {mammogram} ^ {+}) = \frac {P (\text {has BC and mammogram} ^ {+})}{P (\text {mammogram} ^ {+})} \\ = \frac {0 . 0 0 3 1 2}{0 . 0 7 2 8 8} \approx 0. 0 4 2 8. \\ \end{array}
$$

Even with a positive mammogram, there is still only a 4% chance of breast cancer! It may seem surprising that even when the false negative and false positive probabilities of the test are small (0.11 and 0.07, respectively), the conditional probability of disease given a positive test could also be so small. In this population, the probability that a woman does not have breast cancer is high $\left(1 - 0.0035 = 0.9965\right)$ , which results in a relatively high number of false positives in comparison to true positives.

Calculating probabilities for diagnostic tests is done so often in medicine that the topic has some specialized terminology. The **sensitivity** of a test is the probability of a positive test result when disease is present, such as a positive mammogram when a patient has breast cancer. The **specificity** of a test is the probability of a negative test result when disease is absent.<sup>33</sup> The probability of disease in a population is referred to as the **prevalence**. With specificity and sensitivity information for a particular test, along with disease prevalence, the **positive predictive value** (PPV) can be calculated: the probability that disease is present when a test result is positive. Similarly, the **negative predictive value** is the probability that disease is absent when test results are negative. These terms are used for nearly all diagnostic tests used to screen for diseases.

![](images/page_112_image_9.jpg)

## GUIDED PRACTICE 2.45

Identify the prevalence, sensitivity, specificity, and PPV from the scenario in Example $2 . 4 4 . ^ { 3 4 }$ 4

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">33<sub>The</sub> sensitivity and specificity are, respectively, the probability of a true positive test result and the probability of a true negative test result.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">34<sub>The</sub> prevalence of breast cancer is 0.0035. The sensitivity is the probability of a positive test result when disease is present, which is the complement of a false negative: 1 − 0.11 = 0.89. The specificity is the probability of a negative test result when disease is absent, which is the complement of a false positive: 1 − 0.07 = 0.93. The PPV is 0.04, the probability of breast cancer given a positive mammogram.</span></small>

## Example 2.44 Solution 2. Bayes’ Rule.

The process used to solve the problem via the tree diagram can be condensed into a single algebraic expression by substituting the original probability expressions into the numerator and denominator:

$$
\begin{array}{l} P (\text {has BC} \mid \text {mammogram} ^ {+}) = \frac {P (\text {has BC and mammogram} ^ {+})}{P (\text {mammogram} ^ {+})} \\ = \frac {P (\text {mammogram} ^ {+} \mid \text {has BC}) \times P (\text {has BC})}{\left[ P (\text {mammogram} ^ {+} \mid \text {has BC}) \times P (\text {has BC}) \right] + \left[ P (\text {mammogram} ^ {+} \mid \text {no BC}) \times P (\text {no BC}) \right]}. \\ \end{array}
$$

The expression can also be written in terms of diagnostic testing language, where $D = \{ { \tt h a s ~ d i s e a s e } \} ,$ $D ^ { c } = \{ \mathbf { d o e s }$ not have disease}, $T ^ { + } =$ {positive test result}, and $T ^ { - } = \{ \mathrm { { \tt n e g a t i v e } }$ test result}.

$$
\begin{array}{l} P (D | T ^ {+}) = \frac {P (D \text { and } T ^ {+})}{P (T ^ {+})} \\ = \frac {P (T ^ {+} | D) \times P (D)}{[ P (T ^ {+} | D) \times P (D) ] + [ P (T ^ {+} | D ^ {c}) \times P (D ^ {c}) ]} \\ \mathrm{PPV} = \frac {\text {sensitivity} \times \text {prevalence}}{\left[ \text {sensitivity} \times \text {prevalence} \right] + \left[ (1 - \text {specificity}) \times (1 - \text {prevalence}) \right]}\left. \right. \\ \end{array}
$$

The generalization of this formula is known as Bayes’ Theorem or Bayes’ Rule.

## BAYES’ THEOREM

Consider the following conditional probability for variable 1 and variable 2:

$$
P (\text { outcome   } A _ {1} \text {   of   variable   1   |   outcome   } B \text {   of   variable   2 }).
$$

Bayes’ Theorem states that this conditional probability can be identified as the following fraction:

$$
\frac {P (B | A _ {1}) P (A _ {1})}{P (B | A _ {1}) P (A _ {1}) + P (B | A _ {2}) P (A _ {2}) + \cdots + P (B | A _ {k}) P (A _ {k})}, \tag {2.46}
$$

where $A _ { 2 } , A _ { 3 } , . . . ,$ and $A _ { k }$ represent all other possible outcomes of the first variable.

The numerator identifies the probability of getting both $A _ { 1 }$ and B. The denominator is the marginal probability of getting B. This bottom component of the fraction describes the adding of probabilities from the different ways to get B.

To apply Bayes’ Theorem correctly, there are two preparatory steps:

(1) First identify the marginal probabilities of each possible outcome of the first variable: $P ( A _ { 1 } )$ $P ( A _ { 2 } ) , . . . , P ( A _ { k } )$
(2) Then identify the probability of the outcome B, conditioned on each possible scenario for the first variable: $P ( B | A _ { 1 } ) , P ( B | A _ { 2 } ) , . . . , P ( B | A _ { k } )$

Once these probabilities are identified, they can be applied directly within the formula.

## Example 2.44 Solution 3. Contingency Table.

The positive predictive value (PPV) of a diagnostic test can be calculated by constructing a two-way contingency table for a large, hypothetical population and calculating conditional probabilities by conditioning on rows or columns. Using a large enough hypothetical population results in an empirical estimate of PPV that is very close to the exact value obtained via using the previously discussed approaches.

Begin by constructing an empty $2 \times 2$ table, with the possible outcomes of the diagnostic test as the rows, and the possible disease statuses as the columns (Figure 2.17). Include cells for the row and column sums.

Choose a large number N, for the hypothetical population size. Typically, N of 100,000 is sufficient for an accurate estimate.

|  | Breast Cancer Present | Breast Cancer Absent | Sum |
| --- | --- | --- | --- |
| Mammogram Positive | - | - | - |
| Mammogram Negative | - | - | - |
| Sum | - | - | 100,000 |

Figure 2.17: A 2 × 2 table for the mammogram example, with hypothetical population size N of 100,000.

Continue populating the table, using the provided information about the prevalence of breast cancer in this population (0.35%), the chance of a false negative mammogram (11%), and the chance of a false positive (7%):

1. Calculate the two column totals (the number of women with and without breast cancer) from P (BC), the disease prevalence:

$$
N \times P (\mathrm{BC}) = 1 0 0, 0 0 0 \times . 0 0 3 5 = 3 5 0 \text {   women   with   BC   }
$$

$$
N \times [ 1 - P (\mathrm{BC}) ] = 1 0 0, 0 0 0 \times [ 1 -. 0 0 3 5 ] = 9 9, 6 5 0 \text {   women   without   BC   }
$$

Alternatively, the number of women without breast cancer can be calculated by subtracting the number of women with breast cancer from N.

2. Calculate the two numbers in the first column: the number of women who have breast cancer and tested either negative (false negative) or positive (true positive).

$$
\text {women with} \mathrm{BC} \times P (\text {false"} -") = 3 5 0 \times . 1 1 = 3 8. 5 \text {false"} -" \text {results}
$$

$$
\text {women with} \mathrm{BC} \times [ 1 - P (\text {false"} -") ] = 3 5 0 \times [ 1 -. 1 1 ] = 3 1 1. 5 \text {true"} +" \text {results}
$$

3. Calculate the two numbers in the second column: the number of women who do not have breast cancer and tested either positive (false positive) or negative (true negative).

$$
\text {women without BC} \times P (\text {false"} +") = 9 9, 6 5 0 \times . 0 7 = 6, 9 7 5. 5 \text {false"} +" \text {results}
$$

$$
\text {women without BC} \times [ 1 - P (\text {false"} +") ] = 9 9, 6 5 0 \times [ 1 -. 0 7 ] = 9 2, 6 7 4. 5 \text {true}" -" results
$$

4. Complete the table by calculating the two row totals: the number of positive and negative mammograms out of 100,000.

$$
(\text {true}" +" \text {results}) + (\text {false}" +" \text {results}) = 3 1 1. 5 + 6, 9 7 5. 5 = 7, 2 8 7" +" \text {mammograms}
$$

$$
(\text {true}" -" \text {results}) + (\text {false}" -" \text {results}) = 3 8. 5 + 9 2, 6 7 4. 5 = 9 2, 7 1 3" -" \text {mammograms}
$$

5. Finally, calculate the PPV of the mammogram by using the ratio of the number of true positives to the total number of positive mammograms. This estimate is more than accurate enough, with the calculated value differing only in the third decimal place from the exact calculation,

$$
\frac {\text {true}" +" results"}{"+" mammograms} = \frac {3 1 1 . 5}{7 , 2 8 7} = 0. 0 4 2 7.
$$

|  | Breast Cancer Present | Breast Cancer Absent | Sum |
| --- | --- | --- | --- |
| Mammogram Positive | 311.5 | 6,975.5 | 7,287 |
| Mammogram Negative | 38.5 | 92,674.5 | 92,713 |
| Sum | 350 | 99,650 | 100,000 |

Figure 2.18: Completed table for the mammogram example. The table shows again why the PPV of the mammogram is low: almost 7,300 women will have a positive mammogram result in this hypothetical population, but only \~312 of those women actually have breast cancer.

![](images/page_115_image_6.jpg)

## GUIDED PRACTICE 2.47

Some congenital disorders are caused by errors that occur during cell division, resulting in the presence of additional chromosome copies. Trisomy 21 occurs in approximately 1 out of 800 births. Cell-free fetal DNA (cfDNA) testing is one commonly used way to screen fetuses for trisomy 21. The test sensitivity is 0.98 and the specificity is 0.995. Calculate the PPV and NPV of the test.<sup>35</sup>

$$
\begin{array}{c} \overline {{^ {3 5} \mathrm{PPV}}} = \frac {P (T ^ {+} | D) \times P (D)}{[ P (T ^ {+} | D) \times P (D) ] + [ P (T ^ {+} | D ^ {c}) \times P (D ^ {c}) ]} = \frac {(0 . 9 8) (1 / 8 0 0)}{(0 . 9 8) (1 / 8 0 0) + (1 - 0 . 9 9 5) (7 9 9 / 8 0 0)} = 0. 1 9 7. \\ \mathrm{NPV} = \frac {P (T ^ {-} | D ^ {c}) \times P (D ^ {c})}{[ P (T ^ {-} | D) \times P (D) ] + [ P (T ^ {-} | D ^ {c}) \times P (D ^ {c}) ]} = \frac {(0 . 9 9 5) (7 9 9 / 8 0 0)}{(1 - 0 . 9 8) (1 / 8 0 0) + (0 . 9 9 5) (7 9 9 / 8 0 0)} = 0. 9 9 9 9 7 5. \end{array}
$$

## 2.3 Extended example: cat genetics

So far, the principles of probability have only been illustrated with short examples. In a more complex setting, it can be surprisingly difficult to accurately translate a problem scenario into the language of probability. This section demonstrates how the rules of probability can be applied to work through a relatively sophisticated conditioning problem.

## Problem statement

The gene that controls white coat color in cats, KIT , is known to be responsible for multiple phenotypes such as deafness and blue eye color. A dominant allele W at one location in the gene has complete penetrance for white coat color; all cats with the W allele have white coats. There is incomplete penetrance for blue eyes and deafness; not all white cats will have blue eyes and not all white cats will be deaf. However, deafness and blue eye color are strongly linked, such that white cats with blue eyes are much more likely to be deaf. The variation in penetrance for eye color and deafness may be due to other genes as well as environmental factors.

Suppose that 30% of white cats have one blue eye, while 10% of white cats have two blue eyes. About 73% of white cats with two blue eyes are deaf and 40% of white cats with one blue eye are deaf. Only 19% of white cats with other eye colors are deaf.

a) Calculate the prevalence of deafness among white cats.
b) Given that a white cat is deaf, what is the probability that it has two blue eyes?
c) Suppose that deaf, white cats have an increased chance of being blind, but that the prevalence of blindness differs according to eye color. While deaf, white cats with two blue eyes or two non-blue eyes have probability 0.20 of developing blindness, deaf and white cats with one blue eye have probability 0.40 of developing blindness. White cats that are not deaf have probability 0.10 of developing blindness, regardless of their eye color.
i. What is the prevalence of blindness among deaf, white cats?
ii. What is the prevalence of blindness among white cats?
iii. Given that a cat is white and blind, what is the probability that it has two blue eyes?

## Defining notation

Before beginning any calculations, it is essential to clearly define any notation that will be used. For this problem, there are several events of interest: deafness, number of blue eyes (either 0, 1, or 2), and blindness.

– Let D represent the event that a white cat is deaf.
– Let B<sub>0</sub> = {zero blue eyes}, $B _ { 1 } = \{ \mathrm { o n e \; b l u e \; e y e } \} ,$ and $B _ { 2 } = \{ \mathrm { t w o ~ b l u e ~ e y e s } \}$
– Let L represent the event that a white cat is blind.

Note that since all cats mentioned in the problem are white, it is not necessary to define whiteness as an event; white cats represent the sample space.

## Part a) Deafness

The prevalence of deafness among white cats is the proportion of white cats that are deaf; i.e., the probability of deafness among white cats. In the notation of probability, this question asks for the value of $P ( D )$

## EXAMPLE 2.48

The following information has been given in the problem. Re-write the information using the notation defined earlier.

Suppose that 30% of white cats have one blue eye, while 10% of white cats have two blue eyes. About 73% of white cats with two blue eyes are deaf and 40% of white cats with one blue eye are deaf. Only 19% of white cats with other eye colors are deaf.

The first sentence provides information about the prevalence of white cats with one blue eye and white cats with two blue eyes: $P ( B _ { 1 } ) = 0 . 3 0$ and $P ( B _ { 2 } ) = 0 . 1 0 .$ . The only other possible eye color combination is zero blue eyes (i.e., two non-blue eyes); i.e., since $P(B_{0}) + P(B_{1}) + P(B_{2}) = 1,   P(B_{0}) =$ $1 - P ( B _ { 1 } ) - P ( B _ { 2 } ) = 0 . 6 0$ . 60% of white cats have two non-blue eyes.

While it is not difficult to recognize that the second and third sentences provide information about deafness in relation to eye color, it can be easy to miss that these probabilities are conditional probabilities. A close reading should focus on the language—"About 73% of white cats with two blue eyes are deaf...": i.e., out of the white cats that have two blue eyes, 73% are deaf. Thus, these are probabilities of deafness conditioned on eye color. From these sentences, $P ( D | B _ { 2 } ) = 0 . 7 3 ,$ $P ( D | B _ { 1 } ) = 0 . 4 0 ,$ , and $P ( D | B _ { 0 } ) = 0 . 1 9 .$

Consider that there are three possible ways to partition the event $D ,$ that a white cat is deaf: a cat could be deaf and have two blue eyes, be deaf and have one blue eye (and one non-blue eye), or be deaf and have two non-blue eyes. Thus, by the addition rule of disjoint outcomes:

$$
P (D) = P (D \text {and} B _ {2}) + P (D \text {and} B _ {1}) + P (D \text {and} B _ {0}).
$$

Although the joint probabilities of being deaf and having particular eye colors are not given in the problem, these can be solved for based on the given information. The definition of conditional probability $P ( A | B )$ relates the joint probability $P ( A$ and B) with the marginal probability $P ( B )$ 36

$$
P (A | B) = \frac {P (A \text { and } B)}{P (B)} \qquad P (A \text { and } B) = P (A | B) P (B).
$$

Thus, the probability P (D) is given by:

$$
\begin{array}{l} P (D) = P (D \text { and } B _ {2}) + P (D \text { and } B _ {1}) + P (D \text { and } B _ {0}) \\ = P (D | B _ {2}) P (B _ {2}) + P (D | B _ {1}) P (B _ {1}) + P (D | B _ {0}) P (B _ {0}) \\ = (0. 7 3) (0. 1 0) + (0. 4 0) (0. 3 0) + (0. 1 9) (0. 6 0) \\ = 0. 3 0 7. \\ \end{array}
$$

The prevalence of deafness among white cats is 0.307.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">36<sub>This</sub> rearrangement of the definition of conditional probability, P (A and B) = P (A|B)P (B), is also known as the general multiplication rule.</span></small>

## Part b) Deafness and eye color

The probability that a white cat has two blue eyes, given that it is deaf, can be expressed as $P ( B _ { 2 } | D )$

## EXAMPLE 2.49

Using the definition of conditional probability, solve for $P ( B _ { 2 } | D )$

$$
P (B _ {2} | D) = \frac {P (D \text { and } B _ {2})}{P (D)} = \frac {P (D | B _ {2}) P (B _ {2})}{P (D)} = \frac {(0 . 7 3) (0 . 1 0)}{0 . 3 0 7} = 0. 2 3 8.
$$

The probability that a white cat has two blue eyes, given that it is deaf, is 0.238.

It is also possible to think of this as a Bayes’ Rule problem, where there are three possible partitions of the event of deafness, D. In this problem, it is possible to directly solve from the definition of conditional probability since $P ( D )$ was solved for in part a); note that the expanded denominator below matches the earlier work to calculate $P ( D )$

$$
P (B _ {2} | D) = \frac {P (D \text {and} B _ {2})}{P (D)} = \frac {P (D | B _ {2}) P (B _ {2})}{P (D | B _ {2}) P (B _ {2}) + P (D | B _ {1}) P (B _ {1}) + P (D | B _ {0}) P (B _ {0})}.
$$

## Part c) Blindness, deafness, and eye color

## EXAMPLE 2.50

The following information has been given in the problem. Re-write the information using the notation defined earlier.

Suppose that deaf, white cats have an increased chance of being blind, but that the prevalence of blindness differs according to eye color. While deaf, white cats with two blue eyes or two non-blue eyes have probability 0.20 of developing blindness, deaf and white cats with one blue eye have probability 0.40 of developing blindness. White cats that are not deaf have probability 0.10 of developing blindness, regardless of their eye color.

The second sentence gives probabilities of blindness, conditional on eye color and being deaf: $P ( L | B _ { 2 } , D ) = P ( L | B _ { 0 } , D ) = 0 . 2 0 ,$ , and $P ( L | B _ { 1 } , D ) = 0 . 4 0$ . The third sentence gives the probability that a white cat is blind, given that it is not deaf: $P ( L | D ^ { C } ) = 0 . 1 0$

Part i. asks for the prevalence of blindness among deaf, white cats: $P ( L | D )$ . As in part a), the event of blindness given deafness can be partitioned by eye color:

$$
P (L | D) = P (L \text {   and   } B _ {0} | D) + P (L \text {   and   } B _ {1} | D) + P (L \text {   and   } | D).
$$

## EXAMPLE 2.51

Expand the previous expression using the general multiplication rule, $P ( A$ and $B ) = P ( A | B ) P ( B )$

The general multiplication rule may seem difficult to apply when conditioning is present, but the principle remains the same. Think of the conditioning as a way to restrict the sample space; in this context, conditioning on deafness implies that for this part of the problem, all the cats being considered are deaf (and white).

For instance, consider the first term, P (L and $B _ { 0 } | D )$ , the probability of being blind and having two non-blue eyes, given deafness. How could this be rewritten if the probability were simply P (L and $B _ { 0 } ) _ { \cdot } ^ { 2 }$

$$
P (L \text { and } B _ {0}) = P (L | B _ {0}) P (B _ {0})
$$

Now, recall that for this part of the problem, the sample space is restricted to deaf (and white) cats. Thus, all of the terms in the expansion should include conditioning on deafness:

$$
P (L \text {   and   } B _ {0} | D) = P (L | D, B _ {0}) P (B _ {0} | D).
$$

Thus,

$$
P (L | D) = P (L | D, B _ {0}) P (B _ {0} | D) + P (L | D, B _ {1}) P (B _ {1} | D) + P (L | D, B _ {2}) P (B _ {2} | D).
$$

Although $P ( L | D , B _ { 0 } ) , P ( L | D , B _ { 1 } )$ , and $P ( L | D , B _ { 2 } )$ are given from the problem statement, $P ( B _ { 0 } | D )$ $P ( B _ { 1 } | D )$ , and $P ( B _ { 2 } | D )$ are not. However, note that the probability that a white cat has two blue eyes given that it is deaf, $P ( B _ { 2 } | D )$ , was calculated in part b).

## GUIDED PRACTICE 2.52

Calculate $P ( B _ { 0 } | D )$ and $P ( B _ { 1 } | D ) . ^ { 3 7 }$

There is now sufficient information to calculate $P ( L | D )$ ):

$$
\begin{array}{l} P (L | D) = P (L \text { and } B _ {0} | D) + P (L \text { and } B _ {1} | D) + P (L \text { and } B _ {2} | D) \\ = P (L | D, B _ {0}) P (B _ {0} | D) + P (L | D, B _ {1}) P (B _ {1} | D) + P (L | D, B _ {2}) P (B _ {2} | D) \\ = (0. 2 0) (0. 3 7 1) + (0. 4 0) (0. 3 9 1) + (0. 2 0) (0. 2 3 8) \\ = 0. 2 7 8. \\ \end{array}
$$

The prevalence of blindness among deaf, white cats is 0.278.

Part ii. asks for the prevalence of blindness among white cats, $P ( L )$ . Again, partitioning is an effective strategy. Instead of partitioning by eye color, however, partition by deafness.

$$
P (B _ {0} | D) = \frac {P (D \text {and} B _ {0})}{P (D)} = \frac {P (D | B _ {0}) P (B _ {0})}{P (D)} = \frac {(0 . 1 9) (0 . 6 0)}{0 . 3 0 7} = 0. 3 7 1.
$$

$$
P (B _ {1} | D) = \frac {P (D \text { and } B _ {1})}{P (D)} = \frac {P (D | B _ {1}) P (B _ {1})}{P (D)} = \frac {(0 . 4 0) (0 . 3 0)}{0 . 3 0 7} = 0. 3 9 1.
$$

## EXAMPLE 2.53

Calculate the prevalence of blindness among white cats, $P ( L )$

$$
\begin{array}{l} P (L) = P (L \text { and } D) + P (L \text { and } D ^ {C}) \\ = P (L | D) P (D) + P (L | D ^ {C}) P (D ^ {C}) \\ = (0. 2 7 8) (0. 3 0 7) + (0. 1 0) (1 - 0. 3 0 7) \\ = 0. 1 5 5. \\ \end{array}
$$

$P ( D )$ was calculated in part a), while $P ( L | D )$ was calculated in part c, i. The conditioning probability of blindness given a white cat is not deaf is 0.10, as given in the question statement. By the definition of the complement, $P ( D ^ { C } ) = 1 - P ( D )$

The prevalence of blindness among white cats is 0.155.

Part iii. asks for the probability that a cat has two blue eyes, given that it is white and blind. This probability can be expressed as $P ( B _ { 2 } | L )$ . Recall that since all cats being discussed in the problem are white, it is not necessary to condition on coat color.

Start out with the definition of conditional probability:

$$
P (B _ {2} | L) = \frac {P (B _ {2} \text { and } L)}{P (L)}.
$$

The key to calculating $P ( B _ { 2 } | L )$ relies on recognizing that the event a cat is blind and has two blue eyes can be partitioned by whether or not the cat is also deaf:

$$
P (B _ {2} | L) = \frac {P (B _ {2} \text {and} L \text {and} D) + P (B _ {2} \text {and} L \text {and} D ^ {C})}{P (L)}. \tag {2.54}
$$

## EXAMPLE 2.55

Draw a tree diagram to organize the events involved in this problem. Identify the branches that represent the possible paths for a white cat to both have two blue eyes and be blind.

When drawing a tree diagram, remember that each branch is conditioned on the previous branches. While there are various possible trees, the goal is to construct a tree for which as many of the branches as possible have known probabilities.

The tree for this problem will have three branch points, corresponding to either deafness, blindness, or eye color. The first set of branches contain unconditional probabilities, the second set contains conditional probabilities given one event, and the third set contains conditional probabilities given two events.

Recall that the probabilities $P ( L | D , B _ { 0 } ) , \; P ( L | D , B _ { 1 } )$ , and $P ( L | D , B _ { 2 } )$ were provided in the problem statement. These are the only probabilities conditioned on two events that have previously appeared in the problem, so blindness is the most convenient choice of third branch point.

It is not immediately obvious whether it will be more efficient to start with deafness or eye color, since unconditional and conditional probabilities related to both have appeared in the problem. Figure 2.19 shows two trees, one starting with deafness and the other starting with eye color. The two possible paths for a white cat to both have two blue eyes and be blind are shown in green.

![](images/page_121_image_2.jpg)

Figure 2.19: In (a), the first branch is based on deafness, while in (b), the first branch is based on eye color.

## EXAMPLE 2.56

Expand Equation 2.54 according to the tree shown in Figure 2.19(a), and solve for $P ( B _ { 2 } | L )$

$$
\begin{array}{l} P (B _ {2} | L) = \frac {P (B _ {2} \text { and } L \text { and } D) + P (B _ {2} \text { and } L \text { and } D ^ {C})}{P (L)} \\ = \frac {P (L | B _ {2} , D) P (B _ {2} | D) P (D) + P (L | B _ {2} , D ^ {C}) P (B _ {2} | D ^ {C}) P (D ^ {C})}{P (L)} \\ = \frac {(0 . 2 0) (0 . 2 3 8) (0 . 3 0 7) + (0 . 1 0) P (B _ {2} | D ^ {C}) P (D ^ {C})}{0 . 1 5 5}. \\ \end{array}
$$

Two of the probabilities have not been calculated previously: $P ( B _ { 2 } | D ^ { C } )$ and $P ( D ^ { C } )$ . From the definition of the complement, $P ( D ^ { C } ) = 1 - P ( D ) = 0 . 6 9 3 ;   P ( D )$ was calculated in part a). To calculate $P ( B _ { 2 } | D ^ { C } )$ , apply the definition of conditional probability as in part b), where $P ( B _ { 2 } | D )$ was calculated:

$$
P (B _ {2} | D ^ {C}) = \frac {P (D ^ {C} \text {and} B _ {2})}{P (D ^ {C})} = \frac {P (D ^ {C} | B _ {2}) (P (B _ {2})}{P (D ^ {C})} = \frac {(1 - 0 . 7 3) (0 . 1 0)}{0 . 6 9 3} = 0. 0 3 9 0.
$$

$$
P (B _ {2} | L) = \frac {(0 . 2 0) (0 . 2 3 8) (0 . 3 0 7) + (0 . 1 0) (0 . 0 3 9 0) (0 . 6 9 3)}{0 . 1 5 5}
$$

$$
= 0. 1 1 2
$$

The probability that a white cat has two blue eyes, given that it is blind, is 0.112.

![](images/page_122_image_2.jpg)

## GUIDED PRACTICE 2.57

Expand Equation 2.54 according to the tree shown in Figure 2.19(b), and solve for $P ( B _ { 2 } | L ) . ^ { 3 8 }$

A tree diagram is useful for visualizing the different possible ways that a certain set of outcomes can occur. Although conditional probabilities can certainly be calculated without the help of tree diagrams, it is often easy to make errors with a strictly algebraic approach. Once a tree is constructed, it can be used to solve for several probabilities of interest. The following example shows how one of the previous trees can be applied to answer a different question than the one posed in part c), iii.

$$
P (B _ {2} | L) = \frac {P (L | B _ {2} , D) P (D | B _ {2}) P (B _ {2}) + P (L | B _ {2} , D ^ {C}) P (D ^ {C} | B _ {2}) P (B _ {2})}{P (L)} = \frac {(0 . 2 0) (0 . 7 3) (0 . 1 0) + (0 . 1 0) (1 - 0 . 7 3) (0 . 1 0)}{0 . 1 5 5} = 0. 1 1 2.
$$

## EXAMPLE 2.58

What is the probability that a white cat has one blue eye and one non-blue eye, given that it is not blind?

Calculate $P ( B _ { 1 } | L ^ { C } )$ . Start with the definition of conditional probability, then expand.

$$
P (B _ {1} | L ^ {C}) = \frac {P (B _ {1} \text {and} L ^ {C})}{P (L ^ {C})} = \frac {P (B _ {1} \text {and} L ^ {C} \text {and} D) + P (B _ {1} \text {and} L ^ {C} \text {and} D ^ {C})}{P (L ^ {C})}.
$$

Figure 2.20 is a reproduction of the earlier tree diagram (Figure 2.19(b)), with yellow arrows showing the two paths of interest.

As before, expand the numerator and fill in the known values.

$$
\begin{array}{l} P (B _ {1} | L ^ {C}) = \frac {P (B _ {1} \text { and } L ^ {C} \text { and } D) + P (B _ {1} \text { and } L ^ {C} \text { and } D ^ {C})}{P (L ^ {C})} \\ = \frac {P (L ^ {C} | D , B _ {1}) P (D | B _ {1}) P (B _ {1}) + P (L ^ {C} | D ^ {C} , B _ {1}) P (D ^ {C} | B _ {1}) P (B _ {1})}{P (L ^ {C})} \\ = \frac {\mathbf {P} (\mathbf {L} ^ {\mathrm{C}} | \mathbf {D} , \mathbf {B _ {1}}) (0 . 4 0) (0 . 3 0) + \mathbf {P} (\mathbf {L} ^ {\mathrm{C}} | \mathbf {D} ^ {\mathrm{C}} , \mathbf {B _ {1}}) \mathbf {P} (\mathbf {D} ^ {\mathrm{C}} | \mathbf {B _ {1}}) (0 . 3 0)}{\mathbf {P} (\mathbf {L} ^ {\mathrm{C}})}. \\ \end{array}
$$

The probabilities in **bold** are not known. Apply the definition of the complement; recall that the rule for complements holds when an event and its complement are conditioned on the same information: $P ( A | B ) = 1 - P ( A ^ { C } | B )$

$$
\begin{array}{l} - P (L ^ {C}) = 1 - P (L) = 1 - 0. 1 5 5 = 0. 8 4 5 \\ - P (D ^ {C} | B _ {1}) = 1 - P (D | B _ {1}) = 1 - 0. 4 0 = 0. 6 0 \\ - P (L ^ {C} | D, B _ {1}) = 1 - P (L | D, B _ {1}) = 1 - 0. 4 0 = 0. 6 0 \\ \end{array}
$$

The definition of the complement can also be applied to calculate $P ( L ^ { C } | D ^ { C } , B _ { 1 } )$ . The problem statement originally specified that white cats that are not deaf have probability 0.10 of developing blindness regardless of eye color: $P ( L | D ^ { C } ) = 0 . 1 0$ . Thus, $P ( L ^ { C } | D ^ { C } , B _ { 1 } ) = P ( L ^ { C } | D ^ { C } )$ . By the definition of the complement, $P ( L ^ { C } | D ^ { C } ) = 1 - P ( L | D ^ { C } ) = 1 - 0 . 1 0 = 0 . 9 0 .$

$$
\begin{array}{l} P (B _ {1} | L ^ {C}) = \frac {P (B _ {1} \text { and } L ^ {C} \text { and } D) + P (B _ {1} \text { and } L ^ {C} \text { and } D ^ {C})}{P (L ^ {C})} \\ = \frac {P (L ^ {C} | D , B _ {1}) P (D | B _ {1}) P (B _ {1}) + P (L ^ {C} | D ^ {C} , B _ {1}) P (D ^ {C} | B _ {1}) P (B _ {1})}{P (L ^ {C})} \\ = \frac {(0 . 6 0) (0 . 4 0) (0 . 3 0) + (0 . 9 0) (0 . 6 0) (0 . 3 0)}{0 . 8 4 5} \\ = 0. 2 7 7. \\ \end{array}
$$

The probability that a white cat has one blue eye and one non-blue eye, given that it is not blind, is 0.277.

![](images/page_124_image_2.jpg)

<details>
<summary>flowchart</summary>

This diagram illustrates a hierarchical or branching process with nodes labeled B0, B1, and B2, showing directional relationships between sub-processes (L, Lc) and intermediate states (D).
</details>

Figure 2.20: The two possible paths for a white cat to both have one blue eye (and one non-blue eye) and to not be blind are shown in yellow.

## 2.4 Notes

Probability is a powerful framework for quantifying uncertainty and randomness. In particular, conditional probability represents a way to update the uncertainty associated with an event given that specific information has been observed. For example, the probability that a person has a particular disease can be adjusted based on observed information, such as age, sex, or the results of a diagnostic test.

As discussed in the text, there are several possible approaches to solving conditional probability problems, including the use of tree diagrams or contingency tables. It can also be intuitive to use a simulation approach in computing software; refer to the labs for details about this method. Regardless of the specific approach that will be used for calculation, it is always advisable to start any problem by understanding the problem context (i.e., the sample space, given information, probabilities of interest) and reading the problem carefully, in order to avoid mistakes when translating between words and probability notation. A common mistake is to confuse joint and conditional probabilities.

Probability distributions were briefly introduced in Section 2.1.5. This topic will be discussed in greater detail in the next chapter.

Probability forms the foundation for data analysis and statistical inference, since nearly every conclusion to a study should be accompanied by a measure of uncertainty. For example, the publication reporting the results of the LEAP study discussed in Chapter 1 included the probability that the observed results could have been due to chance variation. This aspect of probability will be discussed in later chapters.

The four labs for Chapter 2 cover basic principles of probability, conditional probability, pos itive predictive value of a diagnostic test (via Bayes’ Theorem), and the calculation of probabilities conditional on several events in the context of genetic inheritance. Probabilities can be calculated algebraically, using formulas given in this and other texts, but can also be calculated with simple simulations, since a probability represents a proportion of times an event happens when an experiment is repeated many times. Computers are particularly good at keeping track of events during many replications of an experiment. The labs for this chapter use both algebraic and simulation methods, and are particularly useful for building programming skills with the R language.

In medicine, the positive predictive value of a diagnostic test may be one of the most important applications of probability theory. It is certainly the most common. The positive predictive value of a test is the conditional probability of the presence of a disease or condition, given a positive test for the condition, and is often used when counseling patients about their risk for being diagnosed with a disease in the future. The lab on positive predictive value examines the conditional probability of a trisomy 21 genetic mutation (Down syndrome) given that a test based on cell-free DNA suggests its presence.

## 2.5 Exercises

## 2.5.1 Defining probability

**2.1 True or false.** Determine if the statements below are true or false, and explain your reasoning.

(a) Assume that a couple has an equal chance of having a boy or a girl. If a couple’s previous three children have all been boys, then the chance that their next child is a boy is somewhat less than 50%.
(b) Drawing a face card (jack, queen, or king) and drawing a red card from a full deck of playing cards are mutually exclusive events.
(c) Drawing a face card and drawing an ace from a full deck of playing cards are mutually exclusive events.

**2.2 Dice rolls.** If you roll a pair of fair dice, what is the probability of

(a) getting a sum of 1?
(b) getting a sum of 5?
(c) getting a sum of 12?

**2.3 Colorblindness.** Red-green colorblindness is a commonly inherited form of colorblindness; the gene involved is transmitted on the X chromosome in a recessive manner. If a male inherits an affected X chromosome, he is necessarily colorblind (genotype $X ^ { - } Y )$ . However, a female can only be colorblind if she inherits two defective copies (genotype $X ^ { - } X ^ { - } ) ;$ heterozygous females are not colorblind. Suppose that a couple consists of a genotype $X ^ { + } Y$ male and a genotype $X ^ { + } X ^ { - }$ − female.

(a) What is the probability of the couple producing a colorblind male?
(b) True or false: Among the couple’s offspring, colorblindness and female sex are mutually exclusive events.

**2.4 Diabetes and hypertension.** Diabetes and hypertension are two of the most common diseases in Western, industrialized nations. In the United States, approximately 9% of the population have diabetes, while about 30% of adults have high blood pressure. The two diseases frequently occur together: an estimated 6% of the population have both diabetes and hypertension.

(a) Are having diabetes and having hypertension disjoint?
(b) Draw a Venn diagram summarizing the variables and their associated probabilities.
(c) Let A represent the event of having diabetes, and B the event of having hypertension. Calculate P (A or B).
(d) What percent of Americans have neither hypertension nor diabetes?
(e) Is the event of someone being hypertensive independent of the event that someone has diabetes?

**2.5 Educational attainment by gender.** The table below shows the distribution of education level attained by US residents by gender based on data collected during the 2010 American Community Survey.<sup>39</sup>

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Gender</td></tr><tr><td>Male</td><td>Female</td></tr><tr><td rowspan="8">Highest education attained</td><td>Less than 9th grade</td><td>0.07</td><td>0.13</td></tr><tr><td>9th to 12th grade, no diploma</td><td>0.10</td><td>0.09</td></tr><tr><td>HS graduate (or equivalent)</td><td>0.30</td><td>0.20</td></tr><tr><td>Some college, no degree</td><td>0.22</td><td>0.24</td></tr><tr><td>Associate&#x27;s degree</td><td>0.06</td><td>0.08</td></tr><tr><td>Bachelor&#x27;s degree</td><td>0.16</td><td>0.17</td></tr><tr><td>Graduate or professional degree</td><td>0.09</td><td>0.09</td></tr><tr><td>Total</td><td>1.00</td><td>1.00</td></tr></table>

(a) What is the probability that a randomly chosen individual is a high school graduate? Assume that there is an equal proportion of males and females in the population.
(b) Define Event A as having a graduate or professional degree. Calculate the probability of the complement, A<sup>c</sup>.
(c) What is the probability that a randomly chosen man has at least a Bachelor’s degree?
(d) What is the probability that a randomly chosen woman has at least a Bachelor’s degree?
(e) What is the probability that a man and a woman getting married both have at least a Bachelor’s degree? Note any assumptions made – are they reasonable?

**2.6 Poverty and language.** The American Community Survey is an ongoing survey that provides data every year to give communities the current information they need to plan investments and services. The 2010 American Community Survey estimates that 14.6% of Americans live below the poverty line, 20.7% speak a language other than English (foreign language) at home, and 4.2% fall into both categories.<sup>40</sup>

(a) Are living below the poverty line and speaking a foreign language at home disjoint?
(b) Draw a Venn diagram summarizing the variables and their associated probabilities.
(c) What percent of Americans live below the poverty line and only speak English at home?
(d) What percent of Americans live below the poverty line or speak a foreign language at home?
(e) What percent of Americans live above the poverty line and only speak English at home?
(f) Is the event that someone lives below the poverty line independent of the event that the person speaks a foreign language at home?

**2.7 Urgent care visits.** Urgent care centers are open beyond typical office hours and provide a broader range of services than that of many primary care offices. A study conducted to collect information about urgent care centers in the United States reported that in one week, 15.8% of centers saw 0-149 patients, 33.7% saw 150-299 patients, 28.8% saw 300-449 patients, and 21.7% saw 450 or more patients. Assume that the data can be treated as a probability distribution of patient visits for any given week.

(a) What is the probability that three random urgent care centers in a county all see between 300-449 patients in a week? Note any assumptions made. Are the assumptions reasonable?
(b) What is the probability that ten random urgent care centers throughout a state all see 450 or more patients in a week? Note any assumptions made. Are the assumptions reasonable?
(c) With the information provided, is it possible to compute the probability that one urgent care center sees between 150-299 patients in one week and 300-449 patients in the next week? Explain why or why not.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">39<sub>U</sub>.S. Census Bureau, 2010 American Community Survey 1-Year Estimates, [Educational Attainment](http://www.openintro.org/redirect.php?go=textbook-acs_educational_2010&referrer=biostat1_pdf).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">40<sub>U</sub>.S. Census Bureau, 2010 American Community Survey 1-Year Estimates, [Characteristics of People by Language Spoken at Home](http://www.openintro.org/redirect.php?go=textbook-acs_language_2010&referrer=biostat1_pdf).</span></small>