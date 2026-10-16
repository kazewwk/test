Finally,

$$
E (X ^ {2}) = e ^ {- \lambda} \sum_ {k = 0} ^ {\infty} k ^ {2} \frac {\lambda^ {k}}{k !} = e ^ {- \lambda} e ^ {\lambda} \lambda (1 + \lambda) = \lambda (1 + \lambda),
$$

so

$$
\mathrm{Var} (X) = E (X ^ {2}) - (E X) ^ {2} = \lambda (1 + \lambda) - \lambda^ {2} = \lambda .
$$

Thus, the mean and variance of a Pois(λ) r.v. are both equal to λ.

![](images/page_192_image_7.jpg)

Figure 4.7 shows the PMF and CDF of the Pois(2) and Pois(5) distributions from k = 0 to k = 10. It appears that the mean of the Pois(2) is around 2 and the mean of the Pois(5) is around 5, consistent with our findings above. The PMF of the Pois(2) is highly skewed, but as λ grows larger, the skewness is reduced and the PMF becomes more bell-shaped.

![](images/page_192_image_9.jpg)

FIGURE 4.7

Top: Pois(2) PMF and CDF. Bottom: Pois(5) PMF and CDF.

The Poisson distribution is often used in situations where we are counting the number of successes in a particular region or interval of time, and there are a large number of trials, each with a small probability of success. For example, the following random variables could follow a distribution that is approximately Poisson.

• The number of emails you receive in an hour. There are a lot of people who could potentially email you in that hour, but it is unlikely that any specific person will actually email you in that hour. Alternatively, imagine subdividing the hour into milliseconds. There are $3 . 6   \times   1 0 ^ { 6 }$ seconds in an hour, but in any specific millisecond it is unlikely that you will get an email.
• The number of chips in a chocolate chip cookie. Imagine subdividing the cookie into small cubes; the probability of getting a chocolate chip in a single cube is small, but the number of cubes is large.
• The number of earthquakes in a year in some region of the world. At any given time and location, the probability of an earthquake is small, but there are a large number of possible times and locations for earthquakes to occur over the course of the year.

The parameter λ is interpreted as the rate of occurrence of these rare events; in the examples above, λ could be 20 (emails per hour), 10 (chips per cookie), and 2 (earthquakes per year). The Poisson paradigm says that in applications similar to the ones above, we can approximate the distribution of the number of events that occur by a Poisson distribution.

Approximation 4.7.3 (Poisson paradigm). Let $A _ { 1 } , \ldots , A _ { n }$ be events with $p _ { j } =$ $P ( A _ { j } )$ , where $n$ is large, the $p _ { j }$ are small, and the $A _ { j }$ are independent or weakly dependent. Let

$$
X = \sum_ {j = 1} ^ {n} I (A _ {j})
$$

count how many of the $A _ { j }$ occur. Then X is approximately distributed as Pois(λ), with $\begin{array} { r } { \lambda = \sum _ { j = 1 } ^ { n } p _ { j } } \end{array}$

Proving that the above approximation is good is difficult, and would require first giving precise definitions of weak dependence (there are various ways to measure dependence of r.v.s) and of good approximations (there are various ways to measure how good an approximation is). A remarkable theorem is that if the $A _ { j }$ are independent, $N \sim  Pois (\lambda)$ , and B is any set of nonnegative integers, then

$$
| P (X \in B) - P (N \in B) | \leq \min \left(1, \frac {1}{\lambda}\right) \sum_ {j = 1} ^ {n} p _ {j} ^ {2}.
$$

This gives an upper bound on how much error is incurred from using a Poisson approximation. It also makes more precise how small the $p _ { j }$ should be: we want $\textstyle \sum _ { j = 1 } ^ { n } p _ { j } ^ { 2 }$ to be very small, or at least very small compared to λ. The result can be shown using an advanced technique known as the Stein-Chen method.

The Poisson paradigm is also called the law of rare events. The interpretation of “rare” is that the $p _ { j }$ are small, not that λ is small. For example, in the email example, the low probability of getting an email from a specific person in a particular hour is offset by the large number of people who could send you an email in that hour.

In the examples we gave above, the number of events that occur isn’t exactly Poisson because a Poisson random variable has no upper bound, whereas how many of $A _ { 1 } , \ldots , A _ { n }$ occur is at most $n ,$ and there is a limit to how many chocolate chips can be crammed into a cookie. But the Poisson distribution often gives good approximations. Note that the conditions for the Poisson paradigm to hold are fairly flexible: the n trials can have different success probabilities, and the trials don’t have to be independent, though they should not be very dependent. So there are a wide variety of situations that can be cast in terms of the Poisson paradigm. This makes the Poisson a popular model, or at least a starting point, for data whose values are nonnegative integers (called count data in statistics).

Example 4.7.4 (Balls in boxes). There are k distinguishable balls and n distinguishable boxes. The balls are randomly placed in the boxes, with all $n ^ { k }$ possibilities equally likely. Problems in this setting are called occupancy problems, and are at the core of many widely used algorithms in computer science.

(a) Find the expected number of empty boxes (fully simplified, not as a sum).
(b) Find the probability that at least one box is empty. Express your answer as a sum of at most n terms.
(c) Now let $n   =   1 0 0 0 ,   k   =   5 8 0 6$ . The expected number of empty boxes is then approximately 3. Find a good approximation as a decimal for the probability that at least one box is empty. The handy fact $e ^ { 3 } \approx 2 0$ may help.

Solution:

(a) Let $I _ { j }$ be the indicator r.v. for the jth box being empty. Then

$$
E (I _ {j}) = P (I _ {j} = 1) = \left(1 - \frac {1}{n}\right) ^ {k}.
$$

By linearity,

$$
E \left(\sum_ {j = 1} ^ {n} I _ {j}\right) = \sum_ {j = 1} ^ {n} E (I _ {j}) = n \left(1 - \frac {1}{n}\right) ^ {k}.
$$

(b) The probability is 1 for $k   <   n$ . In general, let $A _ { j }$ be the event that box $j$ is empty. By inclusion-exclusion,

$$
\begin{array}{l} P (A _ {1} \cup A _ {2} \cup \dots \cup A _ {n}) = \sum_ {j = 1} ^ {n} (- 1) ^ {j + 1} \binom {n} {j} P (A _ {1} \cap A _ {2} \cap \dots \cap A _ {j}) \\ = \sum_ {j = 1} ^ {n - 1} (- 1) ^ {j + 1} \binom {n} {j} \left(1 - \frac {j}{n}\right) ^ {k}. \\ \end{array}
$$

(c) The number X of empty boxes is approximately Pois(3), since there are a lot of boxes but each is very unlikely to be empty; the probability that a specific box is empty is $(1 - \frac{1}{n})^k = \frac{1}{n} \cdot E(X) \approx 0.003$ . So

$$
P (X \geq 1) = 1 - P (X = 0) \approx 1 - e ^ {- 3} \approx 1 - \frac {1}{2 0} = 0. 9 5.
$$

Poisson approximation greatly simplifies obtaining a good approximate solution to the birthday problem discussed in Chapter 1, and makes it possible to obtain good approximations to various variations which would be hard to solve exactly.

Example 4.7.5 (Birthday problem continued). If we have m people and make the usual assumptions about birthdays, then each pair of people has probability $p   =   1 / 3 6 5$ of having the same birthday, and there are $\binom { m } { 2 }$ pairs. By the Poisson paradigm the distribution of the number X of birthday matches is approximately Pois(λ), where $\lambda = { \binom { m } { 2 } } { \frac { 1 } { 3 6 5 } }$ . Then the probability of at least one match is

$$
P (X \geq 1) = 1 - P (X = 0) \approx 1 - e ^ {- \lambda}.
$$

For $m = 2 3 , \lambda = 2 5 3 / 3 6 5$ and $1   -   e ^ { - \lambda } \approx 0 . 5 0 0 0 0 2$ , which agrees with our finding from Chapter 1 that we need 23 people to have a 50-50 chance of a matching birthday.

Note that even though m = 23 is fairly small, the relevant quantity in this problem is actually $\binom { m } { 2 }$ , which is the total number of “trials” for a successful birthday match, so the Poisson approximation still performs well. 

Example 4.7.6 (Near-birthday problem). What if we want to find the number of people required in order to have a 50-50 chance that two people would have birthdays within one day of each other (i.e., on the same day or one day apart)? Unlike the original birthday problem, this is difficult to obtain an exact answer for, but the Poisson paradigm still applies. The probability that any two people have birthdays within one day of each other is 3/365 (choose a birthday for the first person, and then the second person needs to be born on that day, the day before, or the day after). Again there are $\binom { m } { 2 }$ possible pairs, so the number of within-one-day matches is approximately Pois(λ) where $\lambda = { \binom { m } { 2 } } { \textstyle \frac { 3 } { 3 6 5 } }$ . Then a calculation similar to the one above tells us that we need m = 14 or more. This was a quick approximation, but it turns out that $m = 1 4$ is the exact answer! 

Example 4.7.7 (Birth-minute and birth-hour). There are 1600 sophomores at a certain college. Throughout this example, make the usual assumptions as in the birthday problem.

(a) Find a Poisson approximation for the probability that there are two sophomores who were born not only on the same day of the year, but also at the same hour and the same minute (e.g., both sophomores were born at 8:20 pm on March 31, not necessarily in the same year).

(b) With assumptions as in (a), what is the probability that there are four sophomores who were born not only on the same day, but also at the same hour (e.g., all were born between 2 pm and 3 pm on March 31, not necessarily in the same year)?

Give two different Poisson approximations for this value, one based on creating an indicator r.v. for each quadruplet of sophomores, and the other based on creating an indicator r.v. for each possible day-hour. Which do you think is more accurate?

## Solution:

(a) This is the birthday problem, with $c = 3 6 5 \cdot 2 4 \cdot 6 0 = 5 2 5 6 0 0$ categories rather than 365 categories.<sup>1</sup> Let $n   =   1 6 0 0$ . Creating an indicator r.v. for each pair of sophomores, by linearity the expected number of pairs born on the same day-hourminute is

$$
\lambda_ {1} = \binom{n}{2} \frac {1}{c}.
$$

By Poisson approximation, the probability of at least one match is approximately

$$
1 - \exp (- \lambda_ {1}) \approx 0. 9 1 2 2.
$$

This approximation is very accurate: typing pbirthday(1600, cl $^ { 1 } { \tt { a s s e s } } { \tt { = } } 3 6 5 { \tt { * } } 2 4 { \tt { * } } 6 0 )$ in R yields 0.9125.

(b) Now there are $b = 3 6 5 \cdotp 2 4 = 8 7 6 0$ categories. Let’s explore two different methods of Poisson approximation.

Method 1 : Create an indicator for each set of 4 sophomores. By linearity, the expected number of sets of 4 sophomores born on the same day-hour is

$$
\lambda_ {2} = \binom{n}{4} \frac {1}{b ^ {3}}.
$$

Poisson approximation gives that the desired probability is approximately

$$
1 - \exp (- \lambda_ {2}) \approx 0. 3 3 3.
$$

Method 2 : Create an indicator for each possible day-hour. Let $I _ { j }$ be the indicator for at least 4 people having been born on the jth day-hour of the year (ordered chronologically), for $1 \leq j \leq b .$ Let $p = 1 / b$ and $q = 1 - p .$ Then

$$
\begin{array}{l} E (I _ {j}) = P (I _ {j} = 1) \\ = 1 - P (\text {at most 3 people born on the jth day - hour}) \\ = 1 - q ^ {n} - n p q ^ {n - 1} - \binom {n} {2} p ^ {2} q ^ {n - 2} - \binom {n} {3} p ^ {3} q ^ {n - 3}. \\ \end{array}
$$

The expected number of day-hours on which at least 4 sophomores were born is

$$
\lambda_ {3} = b \cdot E (I _ {1}),
$$

with $E ( I _ { 1 } )$ as above. We then have the Poisson approximation

$$
1 - \exp (- \lambda_ {3}) \approx 0. 2 9 5.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>The song “Seasons of Love” from Rent gives a musical interpretation of this fact.</span></small>

The command pbirthday(1600, classes = 8760, coincident=4) in R gives that the correct answer is 0.296. So Method 2 is more accurate than Method 1.

An intuitive explanation for why Method 1 is less accurate is that there is a more substantial dependence in the indicators in that method. For example, being given that sophomores 1, 2, 3, 4 share the same birth day-hour greatly increases the chance that sophomores 1, 2, 3, 5 share the same birth day-hour. In contrast, knowing that at least 4 sophomores were born on a specific day-hour provides very little information about whether at least 4 were born on a different specific day-hour. 

## 4.8 Connections between Poisson and Binomial

The Poisson and Binomial distributions are closely connected, and their relationship is exactly parallel to the relationship between the Binomial and Hypergeometric distributions that we examined in the previous chapter: we can get from the Poisson to the Binomial by conditioning, and we can get from the Binomial to the Poisson by taking a limit.

Our results will rely on the fact that the sum of independent Poissons is Poisson, just as the sum of independent Binomials is Binomial. We’ll prove this result using the law of total probability for now; in Chapter 6 we’ll learn a faster method that uses a tool called the moment generating function. Chapter 13 gives further insight into these results.

Theorem 4.8.1 (Sum of independent Poissons). If $X \sim \mathrm{Poisson}(\lambda_1), Y \sim \mathrm{Poisson}(\lambda_2)$ and X is independent of $Y$ , then $X + Y \sim  Pois (\lambda_1 + \lambda_2)$

Proof. To get the PMF of $X   +   Y$ , condition on X and use the law of total probability:

$$
\begin{array}{l} P (X + Y = k) = \sum_ {j = 0} ^ {k} P (X + Y = k | X = j) P (X = j) \\ = \sum_ {j = 0} ^ {k} P (Y = k - j) P (X = j) \\ = \sum_ {j = 0} ^ {k} \frac {e ^ {- \lambda_ {2}} \lambda_ {2} ^ {k - j}}{(k - j) !} \frac {e ^ {- \lambda_ {1}} \lambda_ {1} ^ {j}}{j !} \\ = \frac {e ^ {- (\lambda_ {1} + \lambda_ {2})}}{k !} \sum_ {j = 0} ^ {k} \binom{k}{j} \lambda_ {1} ^ {j} \lambda_ {2} ^ {k - j} \\ = \frac {e ^ {- (\lambda_ {1} + \lambda_ {2})} (\lambda_ {1} + \lambda_ {2}) ^ {k}}{k !}. \\ \end{array}
$$

The last step used the binomial theorem. Since we’ve arrived at the $\mathrm{Poisson}(\lambda_1 + \lambda_2)$ PMF, we have $X + Y \sim  Pois (\lambda_1 + \lambda_2)$

The story of the Poisson distribution provides intuition for this result. If there are two different types of events occurring at rates $\lambda _ { 1 }$ and $\lambda _ { 2 }$ , independently, then the overall event rate is $\lambda _ { 1 } + \lambda _ { 2 }$ 

Theorem 4.8.2 (Poisson given a sum of Poissons). If $X \sim  Pois (\lambda_1), Y \sim  Pois (\lambda_2)$ and X is independent of $Y$ , then the conditional distribution of X given $X + Y = n$ is Bin $( n , \lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } ) )$

Proof. Exactly as in the corresponding proof for the Binomial and Hypergeometric, we use Bayes’ rule to compute the conditional PMF $P(X = k|X + Y = n)$

$$
\begin{array}{l} P (X = k | X + Y = n) = \frac {P (X + Y = n | X = k) P (X = k)}{P (X + Y = n)} \\ = \frac {P (Y = n - k) P (X = k)}{P (X + Y = n)}. \\ \end{array}
$$

Now we plug in the PMFs of $X , \; Y$ , and $X + Y;$ the last of these is distributed $\mathrm{Poisson}(\lambda_1 + \lambda_2)$ by the previous theorem. This gives

$$
\begin{array}{l} P (X = k | X + Y = n) = \frac {\left(\frac {e ^ {- \lambda_ {2}} \lambda_ {2} ^ {n - k}}{(n - k) !}\right) \left(\frac {e ^ {- \lambda_ {1}} \lambda_ {1} ^ {k}}{k !}\right)}{\frac {e ^ {- (\lambda_ {1} + \lambda_ {2})} (\lambda_ {1} + \lambda_ {2}) ^ {n}}{n !}} \\ = \binom{n}{k} \frac {\lambda_ {1} ^ {k} \lambda_ {2} ^ {n - k}}{(\lambda_ {1} + \lambda_ {2}) ^ {n}} \\ = \binom {n} {k} \left(\frac {\lambda_ {1}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {k} \left(\frac {\lambda_ {2}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {n - k}, \\ \end{array}
$$

which is the Bin $\left( n , \lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } ) \right)$ PMF, as desired.

Conversely, if we take the limit of the $\operatorname { B i n } ( n , p )$ distribution as $n \to \infty$ and $p \rightarrow 0$ with np fixed, we arrive at a Poisson distribution. This provides the basis for the Poisson approximation to the Binomial distribution.

Theorem 4.8.3 (Poisson approximation to Binomial). If $X \sim \mathrm { B i n } ( n , p )$ and we let $n \to \infty$ and $p \rightarrow 0$ such that $\lambda = n p$ remains fixed, then the PMF of X converges to the Pois(λ) PMF. More generally, the same conclusion holds if $n \to \infty$ and $p \rightarrow 0$ in such a way that np converges to a constant λ.

This is a special case of the Poisson paradigm, where the $A _ { j }$ are independent with the same probabilities, so that $\textstyle \sum _ { j = 1 } ^ { n } I ( A _ { j } )$ has a Binomial distribution. In this special case, we can prove that the Poisson approximation makes sense just by taking a limit of the Binomial PMF.

Proof. We will prove this for the case that $\lambda = n p$ is fixed while $n \to \infty$ and $p \rightarrow 0$ by showing that the Bin $( n , p )$ PMF converges to the $\operatorname { P o i s } ( \lambda )$ PMF. For $0 \leq k \leq n$

$$
\begin{array}{l} P (X = k) = \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} \\ = \frac {n (n - 1) \dots (n - k + 1)}{k !} \left(\frac {\lambda}{n}\right) ^ {k} \left(1 - \frac {\lambda}{n}\right) ^ {n} \left(1 - \frac {\lambda}{n}\right) ^ {- k} \\ = \frac {\lambda^ {k}}{k !} \frac {n (n - 1) \dots (n - k + 1)}{n ^ {k}} \left(1 - \frac {\lambda}{n}\right) ^ {n} \left(1 - \frac {\lambda}{n}\right) ^ {- k}. \\ \end{array}
$$

Letting $n \to \infty$ with k fixed,

$$
\begin{array}{l} \frac {n (n - 1) \dots (n - k + 1)}{n ^ {k}} \rightarrow 1, \\ \left(1 - \frac {\lambda}{n}\right) ^ {n} \rightarrow e ^ {- \lambda}, \\ \left(1 - \frac {\lambda}{n}\right) ^ {- k} \rightarrow 1, \\ \end{array}
$$

where the $e ^ { - \lambda }$ comes from the compound interest formula from Section A.2.5 of the math appendix. So

$$
P (X = k) \rightarrow \frac {e ^ {- \lambda} \lambda^ {k}}{k !},
$$

which is the Pois(λ) PMF.

This theorem implies that if $n$ is large, $p$ is small, and $n p$ is moderate, we can approximate the $\operatorname { B i n } ( n , p )$ PMF by the ${ \mathrm { P o i s } } ( n p )$ PMF. The main thing that matters here is that $p$ should be small; in fact, the result mentioned after the statement of the Poisson paradigm says in this case that the error in approximating $P ( X \in B ) \approx$ $P ( N \in B )$ for $X \sim \mathrm { B i n } ( n , p ) , N \sim \mathrm { P o i s } ( n p )$ is at most min $( p , n p ^ { 2 } )$

Example 4.8.4 (Visitors to a website). The owner of $\mathbf { a }$ certain website is studying the distribution of the number of visitors to the site. Every day, a million people independently decide whether to visit the site, with probability $p   =   2 \times 1 0 ^ { - 6 }$ of visiting. Give a good approximation for the probability of getting at least three visitors on a particular day.

## Solution:

Let $X   \sim   \mathrm { B i n } ( n , p )$ be the number of visitors, where $n   =   1 0 ^ { 6 }$ . It is easy to run into computational difficulties or numerical errors in exact calculations with this distribution since $n$ is so large and $p$ is so small. But since $n$ is large, $p$ is small, and $n p = 2$ is moderate, Pois(2) is a good approximation. This gives

$$
P (X \geq 3) = 1 - P (X <   3) \approx 1 - e ^ {- 2} - e ^ {- 2} \cdot 2 - e ^ {- 2} \cdot \frac {2 ^ {2}}{2 !} = 1 - 5 e ^ {- 2} \approx 0. 3 2 3 3,
$$

which turns out to be extremely accurate.



## 4.9 \*Using probability and expectation to prove existence

An amazing and beautiful fact is that we can use probability and expectation to prove the existence of objects with properties we care about. This technique is called the probabilistic method, and it is based on two simple but surprisingly powerful ideas. Suppose I want to show that there exists an object in a collection with a certain property. This desire seems at first to have nothing to do with probability; I could simply examine each object in the collection one by one until finding an object with the desired property.

The probabilistic method rejects such painstaking inspection in favor of random selection: our strategy is to pick an object at random from the collection and show that there is a positive probability of the random object having the desired property. Note that we are not required to compute the exact probability, but merely to show it is greater than 0. If we can show that the probability of the property holding is positive, then we know that there must exist an object with the property—even if we don’t know how to explicitly construct such an object.

Similarly, suppose each object has a score, and I want to show that there exists an object with a “good” score—that is, a score exceeding a particular threshold. Again, we proceed by choosing a random object and considering its score, X. We know there is an object in the collection whose score is at least E(X)—it’s impossible for every object to be below average! If E(X) is already a good score, then there must also be an object in the collection with a good score. Thus we can show the existence of an object with a good score by showing that the average score is already good.

Let’s state the two key ideas formally.

• The possibility principle: Let A be the event that a randomly chosen object in a collection has a certain property. If $P ( A ) > 0$ , then there exists an object with the property.
• The good score principle: Let X be the score of a randomly chosen object. If $E ( X ) \geq c ,$ then there is an object with a score of at least c.

To see why the possibility principle is true, consider its contrapositive: if there is no object with the desired property, then the probability of a randomly chosen object having the property is 0. Similarly, the contrapositive of the good score principle is “if all objects have a score below c, then the average score is below c”, which is true since a weighted average of numbers less than c is a number less than c.

The probabilistic method doesn’t tell us how to find an object with the desired property; it only assures us that one exists.

Example 4.9.1. A group of 100 people are assigned to 15 committees of size 20, such that each person serves on 3 committees. Show that there exist 2 committees that have at least 3 people in common.

## Solution:

A direct approach is inadvisable here: one would have to list all possible committee assignments and compute, for each one, the number of people in common in every pair of committees. The probabilistic method lets us bypass brute-force calculations. To prove the existence of two committees with an overlap of at least three people, we’ll calculate the average overlap of two randomly chosen committees in an arbitrary committee assignment. So choose two committees at random, and let X be the number of people on both committees. We can represent $X = I _ { 1 }   +   I _ { 2 }   +   \cdots   +   I _ { 1 0 0 }$ where $I _ { j } = 1$ if the jth person is on both committees and 0 otherwise. By symmetry, all of the indicators have the same expected value, so $E ( X ) = 1 0 0 E ( I _ { 1 } )$ , and we just need to find $E ( I _ { 1 } )$

By the fundamental bridge, $E ( I _ { 1 } )$ is the probability that person 1 (whom we’ll name Bob) is on both committees (which we’ll call A and B). There are a variety of ways to calculate this probability; one way is to think of Bob’s committees as 3 tagged elk in a population of 15. Then A and B are a sample of 2 elk, made without replacement. Using the HGeom(3, 12, 2) PMF, the probability that both of these elk are tagged (i.e., the probability that both committees contain Bob) is ${ \textstyle { \binom { 3 } { 2 } } { \binom { 1 2 } { 0 } } / { \binom { 1 5 } { 2 } } = 1 / 3 5 }$ Therefore,

$$
E (X) = 1 0 0 / 3 5 = 2 0 / 7,
$$

which is just shy of the desired “good score” of 3. But hope is not lost! The good score principle says there exist two committees with an overlap of at least $2 0 / 7 ,$ but since the overlap between two committees must be an integer, an overlap of at least $2 0 / 7$ implies an overlap of at least 3. Thus, there exist two committees with at least 3 people in common. 

## 4.9.1 \*Communicating over a noisy channel

Another major application of the probabilistic method is in information theory, the subject which studies (among other things) how to achieve reliable communication across a noisy channel. Consider the problem of trying to send a message when there is noise. This problem is encountered by millions of people every day, such as when talking on the phone (you may be misheard). Suppose that the message you want to send is represented as a binary vector $x \in \{ 0 , 1 \} ^ { k }$ , and that you want to use a code to improve the chance that your message will get through successfully.

Definition 4.9.2 (Codes and rates). Given positive integers k and n, a code is a function c that assigns to each input message $x \in \{ 0 , 1 \} ^ { k }$ a codeword $c ( x ) \in \{ 0 , 1 \} ^ { n }$ The rate of this code is $k / n$ (the number of input bits per output bit). After $c ( x )$ is sent, a decoder takes the received message, which may be a corrupted version of $c ( x )$ , and attempts to recover the correct x.

For example, an obvious code would be to repeat yourself a bunch of times, sending x a bunch of times in a row, say m (with m odd); this is called a repetition code. The receiver could then decode by going with the majority, e.g., decoding the first bit of x as a 1 if that bit was received more times as a 1 than as a 0. But this code may be very inefficient; to get the probability of failure very small, you may need to repeat yourself many times, resulting in a very low rate $1 / m$ of communication.

Claude Shannon, the founder of information theory, showed something amazing: even in a very noisy channel, there is a code allowing for very reliable communication at a rate that does not go to 0 as we require the probability of failure to be lower and lower. His proof was even more amazing: he studied the performance of a completely random code. Richard Hamming, who worked with Shannon at Bell Labs, described Shannon’s approach as follows.

Courage is another attribute of those who do great things. Shannon is a good example. For some time he would come to work at about 10:00 am, play chess until about 2:00 pm and go home.

The important point is how he played chess. When attacked he seldom, if ever, defended his position, rather he attacked back. Such a method of playing soon produces a very interrelated board. He would then pause a bit, think and advance his queen saying, “I ain’t [scared] of nothin’.” It took me a while to realize that of course that is why he was able to prove the existence of good coding methods. Who but Shannon would think to average over all random codes and expect to find that the average was close to ideal? I learned from him to say the same to myself when stuck, and on some occasions his approach enabled me to get significant results. [15]

We will prove a version of Shannon’s result, for the case of a channel where each transmitted bit gets flipped (from 0 to 1 or from 1 to 0) with probability p, independently. First we need two definitions. A natural measure of distance between binary vectors, named after Hamming, is as follows.

Definition 4.9.3 (Hamming distance). For two binary vectors v and w of the same length, the Hamming distance $d ( v , w )$ is the number of positions in which they differ. We can write this as

$$
d (v, w) = \sum_ {i} | v _ {i} - w _ {i} |.
$$

The following function arises very frequently in information theory.

Definition 4.9.4 (Binary entropy function). For $0   <   p   <   1$ , the binary entropy function H is given by

$$
H (p) = - p \log_ {2} p - (1 - p) \log_ {2} (1 - p).
$$

We also define $H ( 0 ) = H ( 1 ) = 0 .$

The interpretation of $H ( p )$ in information theory is that it is a measure of how much information we get from observing a Bern(p) r.v.; $H ( 1 / 2 ) = 1$ says that a fair coin flip provides 1 bit of information, while $H ( 1 ) = 0$ says that with a coin that always lands Heads, there’s no information gained from being told the result of the flip, since we already know the result.

Now consider a channel where each transmitted bit gets flipped with probability $p ,$ independently. Intuitively, it may seem that smaller $p$ is always better, but note that $p = 1 / 2$ is actually the worst-case scenario. In that case, technically known as a useless channel, it is impossible to send information over the channel: the output will be independent of the input! Analogously, in deciding whether to watch a movie, would you rather hear a review from someone you always disagree with or someone you agree with half the time? We now prove that for $0 < p < 1 / 2$ , it is possible to communicate very reliably with rate very close to $1 - H ( p )$

Theorem 4.9.5 (Shannon). Consider a channel where each transmitted bit gets flipped with probability $p ,$ independently. Let $0 < p < 1 / 2$ and $\epsilon > 0$ . There exists a code with rate at least $1 - H ( p ) - \epsilon$ that can be decoded with probability of error less than .

Proof. We can assume that $1 - H ( p ) - \epsilon > 0$ , since otherwise there is no constraint on the rate. Let n be a large positive integer (chosen according to conditions given below), and

$$
k = \lceil n (1 - H (p) - \epsilon) \rceil + 1.
$$

The ceiling function is there since k must be an integer. Choose $p ^ { \prime } \in ( p , 1 / 2 )$ such that $| H ( p ^ { \prime } ) - H ( p ) | < \epsilon / 2$ (this can be done since $H$ is continuous). We will now study the performance of a random code C. To generate a random code $C ,$ we need to generate a random encoded message $C ( x )$ for all possible input messages x.

For each $x \in \{ 0 , 1 \} ^ { k }$ , choose $C ( x )$ to be a uniformly random vector in $\{ 0 , 1 \} ^ { n }$ (making these choices independently). So we can think of $C ( x )$ as a vector consisting of n i.i.d. Bern $( 1 / 2 )$ r.v.s. The rate $k / n$ exceeds $1 - H ( p ) - \epsilon$ by definition, but let’s see how well we can decode the received message!

Let $x \in \{ 0 , 1 \} ^ { k }$ be the input message, $C ( x )$ be the encoded message, and $Y \in \{ 0 , 1 \} ^ { n }$ be the received message. For now, treat x as deterministic. But $C ( x )$ is random since the codewords are chosen randomly, and $Y$ is random since $C ( x )$ is random and due to the random noise in the channel. Intuitively, we hope that $C ( x )$ will be close to $Y$ (in Hamming distance) and $C ( z )$ will be far from $Y$ for all $z \neq x$ , in which case it will be clear how to decode $Y$ and the decoding will succeed. To make this precise, decode $Y$ as follows:

If there exists a unique $z \in \{ 0 , 1 \} ^ { k }$ such that $d ( C ( z ) , Y ) \leq n p ^ { \prime }$ , decode $Y$ to that $z ;$ otherwise, declare decoder failure.

We will show that for n large enough, the probability of the decoder failing to recover the correct x is less than . There are two things that could go wrong:

(a) $d ( C ( x ) , Y ) > n p ^ { \prime } ,$ or
(b) There could be some impostor $z \neq$ x with $d ( C ( z ) , Y ) \leq n p ^ { \prime }$

Note that $d ( C ( x ) , Y )$ is an $\mathbf { r } . \mathbf { v } . ,$ so $d ( C ( x ) , Y )   >   n p ^ { \prime }$ is an event. To handle (a), represent

$$
d (C (x), Y) = B _ {1} + \dots + B _ {n} \sim \mathrm{Bin} (n, p),
$$

where $B _ { i }$ is the indicator of the ith bit being flipped. The law of large numbers (see Chapter 10) says that as n grows, the r.v. $d ( C ( x ) , Y ) / n$ will get very close to $p$ (its expected value), and so will be very unlikely to exceed $p ^ { \prime } ;$

$$
P (d (C (x), Y) > n p ^ {\prime}) = P \left(\frac {B _ {1} + \cdots + B _ {n}}{n} > p ^ {\prime}\right) \to 0 \text {as} n \to \infty .
$$

So by choosing n large enough, we can make

$$
P (d (C (x), Y) > n p ^ {\prime}) <   \epsilon / 4.
$$

To handle (b), note that $d ( C ( z ) , Y )   \sim   \mathrm { B i n } ( n , 1 / 2 )$ for $z \neq x ,$ since the $n$ bits in $C ( z )$ are i.i.d. Bern $( 1 / 2 )$ , independent of $Y$ (to show this in more detail, condition on $Y$ using LOTP). Let $B \sim \mathrm { B i n } ( n , 1 / 2 )$ . By Boole’s inequality,

$$
P (d (C (z), Y) \leq n p ^ {\prime} \text {for some} z \neq x) \leq (2 ^ {k} - 1) P (B \leq n p ^ {\prime}).
$$

To simplify notation, suppose that $n p ^ { \prime }$ is an integer. A crude way to upper bound a sum of m terms is to use m times the largest term, and a crude way to upper bound a binomial coefficient ${ \binom { n } { j } }$ is to use $r ^ { - j } ( 1 - r ) ^ { - ( n - j ) }$ for any $r \in ( 0 , 1 )$ . Combining these two crudities,

$$
P (B \leq n p ^ {\prime}) = \frac {1}{2 ^ {n}} \sum_ {j = 0} ^ {n p ^ {\prime}} \binom {n} {j} \leq \frac {n p ^ {\prime} + 1}{2 ^ {n}} \binom {n} {n p ^ {\prime}} \leq (n p ^ {\prime} + 1) 2 ^ {n H (p ^ {\prime}) - n},
$$

using the fact that $( p ^ { \prime } ) ^ { - n p ^ { \prime } } ( q ^ { \prime } ) ^ { - n q ^ { \prime } } = 2 ^ { n H ( p ^ { \prime } ) }$ for $q ^ { \prime } = 1 - p ^ { \prime }$ . Thus,

$$
2 ^ {k} P (B \leq n p ^ {\prime}) \leq (n p ^ {\prime} + 1) 2 ^ {n (1 - H (p) - \epsilon) + 2 + n (H (p) + \epsilon / 2) - n} = 4 (n p ^ {\prime} + 1) 2 ^ {- n \epsilon / 2} \rightarrow 0,
$$

so we can choose n to make $P ( d ( C ( z ) , Y ) \leq n p ^ { \prime }$ for some $z \neq x ) < \epsilon / 4 .$

Assume that k and n have been chosen in accordance with the above, and let $F ( c , x )$ be the event of failure when code c is used with input message x. Putting together the above results, we have shown that for a random $C$ and any fixed $x ,$

$$
P (F (C, x)) <   \epsilon / 2.
$$

It follows that for each $x ,$ there is a code c with $P ( F ( c , x ) ) < \epsilon / 2$ , but this is not good enough: we want one code that works well for all x! Let X be a uniformly random input message in $\{ 0 , 1 \} ^ { k }$ , independent of C. By LOTP, we have

$$
P (F (C, X)) = \sum_ {x} P (F (C, x)) P (X = x) <   \epsilon / 2.
$$

Again using LOTP, but this time conditioning on $C ,$ we have

$$
\sum_ {c} P (F (c, X)) P (C = c) = P (F (C, X)) <   \epsilon / 2.
$$

Therefore, there exists a code c such that $P ( F ( c , X ) ) < \epsilon / 2 , \mathrm { i . e . }$ , a code c such that the probability of failure for a random input message X is less than $\epsilon / 2$ . Lastly, we will improve $c _ { \gamma }$ obtaining a code that works well for all x, not just a random x. We do this by expurgating the worst $5 0 \%$ of the $x ^ { \prime } \mathrm { s }$ . That is, remove as legal input messages the $2 ^ { k - 1 }$ values of x with the highest failure probabilities for code c. For all remaining $x ,$ we have $P ( F ( c , x ) ) < \epsilon ,$ since otherwise more than half of the $x \in \{ 0 , 1 \} ^ { k }$ would have more than double the average failure probability (see Markov’s inequality in Chapter 10 for more about this kind of argument). By relabeling the remaining x using vectors in $\{ 0 , 1 \} ^ { k - 1 }$ , we obtain a code $c ^ { \prime }   :   \{ 0 , 1 \} ^ { k - 1 }   \to   \{ 0 , 1 \} ^ { n }$ with rate $( k - 1 ) / n \geq 1 - H ( p ) - \epsilon$ and probability less than  of failure for all input messages in $\{ 0 , 1 \} ^ { k - 1 }$ 

There is also a converse to the above theorem, showing that if we require the rate to be at least $1 - H ( p ) + \epsilon ,$ it is impossible to find codes that make the probability of error arbitrarily small. This is why $1 - H ( p )$ is called the capacity of the channel. Shannon also obtained analogous results for much more general channels. These results give theoretical bounds on what can be achieved, without saying explicitly which codes to use. Decades of subsequent work have been devoted to developing specific codes that work well in practice, by coming close to the Shannon bound and allowing for efficient encoding and decoding.

## 4.10 Recap

The expectation of a discrete r.v. X is

$$
E (X) = \sum_ {x} x P (X = x).
$$

An equivalent “ungrouped” way of calculating expectation is

$$
E (X) = \sum_ {s} X (s) P (\{s \}),
$$

where the sum is taken over pebbles in the sample space. Expectation is a single number summarizing the center of mass of a distribution. A single-number summary of the spread of a distribution is the variance, defined by

$$
\mathrm{Var} (X) = E (X - E X) ^ {2} = E (X ^ {2}) - (E X) ^ {2}.
$$

The square root of the variance is called the standard deviation.

Expectation is linear:

$$
E (c X) = c E (X) \text {and} E (X + Y) = E (X) + E (Y),
$$

regardless of whether X and Y are independent or not. Variance is not linear:

$$
\mathrm{Var} (c X) = c ^ {2} \mathrm{Var} (X),
$$

and

$$
\operatorname{Var} (X + Y) \neq \operatorname{Var} (X) + \operatorname{Var} (Y)
$$

in general (an important exception is when X and Y are independent).

A very important strategy for calculating the expectation of a discrete r.v. X is to express it as a sum of indicator r.v.s, and then apply linearity and the fundamental bridge. This technique is especially powerful because the indicator r.v.s need not be independent; linearity holds even for dependent r.v.s. The strategy can be summarized in the following three steps.

1. Represent the r.v. X as a sum of indicator r.v.s. To decide how to define the indicators, think about what X is counting. For example, if X is the number of local maxima, as in the Putnam problem, then we should create an indicator for each local maximum that could occur.
2. Use the fundamental bridge to calculate the expected value of each indicator. When applicable, symmetry may be very helpful at this stage.
3. By linearity of expectation, $E ( X )$ can be obtained by adding up the expectations of the indicators.

Another tool for computing expectations is LOTUS, which says we can calculate the expectation of $g ( X )$ using only the PMF of X, via

$$
E (g (X)) = \sum_ {x} g (x) P (X = x).
$$

If g is non-linear, it is a grave mistake to attempt to calculate $E ( g ( X ) )$ by swapping the E and the g.

Four new discrete distributions to add to our list are the Geometric, Negative Binomial, Negative Hypergeometric, and Poisson distributions. A Geom(p) r.v. is the number of failures before the first success in a sequence of independent Bernoulli trials with probability p of success, and an $\mathrm { N B i n } ( r , p )$ r.v. is the number of failures before r successes. The Negative Hypergeometric is similar to the Negative Binomial except, in terms of drawing balls from an urn, the Negative Hypergeometric samples without replacement and the Negative Binomial samples with replacement. (We also introduced the First Success distribution, which is just a Geometric shifted so that the success is included.)

A Poisson r.v. is often used as an approximation for the number of successes that occur when there are many independent or weakly dependent trials, where each trial has a small probability of success. In the Binomial story, all the trials have the same probability $p$ of success, but in the Poisson approximation, different trials can have different (but small) probabilities $p _ { j }$ of success.

The Poisson, Binomial, and Hypergeometric distributions are mutually connected via the operations of conditioning and taking limits, as illustrated in Figure 4.8. In the rest of this book, we’ll continue to introduce new named distributions and add them to this family tree, until everything is connected!

![](images/page_207_image_4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Pois"] -->|"Limit"| B["Bin"]
  B -->|"Conditioning"| A
  B -->|"Limit"| C["HGeom"]
```
</details>

FIGURE 4.8

Relationships between the Poisson, Binomial, and Hypergeometric.

Figure 4.9 expands upon the corresponding figure from the previous chapter, further exploring the connections between the four fundamental objects we have considered: distributions, random variables, events, and numbers.