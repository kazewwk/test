4. Let X be a continuous r.v. with CDF F and PDF f.

(a) Find the conditional CDF of X given $X > c ,$ for c a constant with $P ( X > c ) \neq 0$ That is, find $P ( X \leq x | X > a )$ for all $c _ { \gamma }$ in terms of F.
(b) Find the conditional PDF of X given $X > c$ (this is the derivative of the conditional CDF).
(c) Check that the conditional PDF from (b) is a valid PDF, by showing directly that it is nonnegative and integrates to 1.

5. A circle with a random radius $R \sim \mathrm { U n i f } ( 0 , 1 )$ is generated. Let A be its area.

(a) Find the mean and variance of A, without first finding the CDF or PDF of A.
(b) Find the CDF and PDF of A.

6. The 68-95-99.7% rule gives approximate probabilities of a Normal r.v. being within 1, 2, and 3 standard deviations of its mean. Derive analogous rules for the following distributions.

(a) Unif(0, 1).
(b) Expo(1).
(c) Expo(1/2). Discuss whether there is one such rule that applies to all Exponential distributions, just as the 68-95-99.7% rule applies to all Normal distributions, not just to the standard Normal.

7. Let

$$
F (x) = \frac {2}{\pi} \sin^ {- 1} \left(\sqrt {x}\right), \text {for} 0 <   x <   1,
$$

F(x) = 0 for $x \leq 0 ,$ and F(x) = 1 for $x \geq 1$

(a) Check that F is a valid CDF, and find the corresponding PDF f. This distribution is called the Arcsine distribution, though it also goes by the name $\mathrm { B e t a } ( 1 / 2 , 1 / 2 )$ (we will explore the Beta in depth in Chapter 8).
(b) Explain how it is possible for f to be a valid PDF even though f(x) goes to ∞ as x approaches 0 from the right and as x approaches 1 from the left.

8. The Beta distribution with parameters $a = 3, b = 2$ has PDF

$$
f (x) = 1 2 x ^ {2} (1 - x), \text {for} 0 <   x <   1.
$$

(We will discuss the Beta in detail in Chapter 8.) Let X have this distribution.

(a) Find the CDF of X.
(b) Find $P ( 0 < X < 1 / 2 )$
(c) Find the mean and variance of X (without quoting results about the Beta distribution).

9. The Cauchy distribution has PDF

$$
f (x) = \frac {1}{\pi (1 + x ^ {2})},
$$

for all real x. (We will introduce the Cauchy from another point of view in Chapter 7.) Find the CDF of a random variable with the Cauchy PDF.

Hint: Recall that the derivative of the inverse tangent function arctan(x) is $\frac { 1 } { 1 { + } x ^ { 2 } }$

# Uniform and universality of the Uniform

10. Let $U \sim \mathrm { U n i f } ( 0 , 8 )$

(a) Find $P ( U \in ( 0 , 2 ) \cup ( 3 , 7 ) )$ without using calculus.
(b) Find the conditional distribution of U given $U \in ( 3 , 7 )$

11. s Let U be a Uniform r.v. on the interval (−1, 1) (be careful about minus signs).

(a) Compute $E ( U ) , \operatorname { V a r } ( U )$ , and $E ( U ^ { 4 } )$
(b) Find the CDF and PDF of $U ^ { 2 }$ . Is the distribution of $U ^ { 2 }$ Uniform on (0, 1)?

12. s A stick is broken into two pieces, at a uniformly random breakpoint. Find the CDF and average of the length of the longer piece.

13. A stick of length 1 is broken at a uniformly random point, yielding two pieces. Let X and Y be the lengths of the shorter and longer pieces, respectively, and let $R = X / Y$ be the ratio of the lengths X and Y .

(a) Find the CDF and PDF of R.
(b) Find the expected value of R (if it exists).
(c) Find the expected value of $1 / R$ (if it exists).

14. Let $U _ { 1 } , \ldots , U _ { n }$ be i.i.d. Unif(0, 1), and $X = \operatorname* { m a x } ( U _ { 1 } , \ldots , U _ { n } )$ . What is the PDF of X? What is EX?

Hint: Find the CDF of X first, by translating the event $X \leq x$ into an event involving $U _ { 1 } , \ldots , U _ { n }$

15. Let $U \sim \mathrm { U n i f } ( 0 , 1 )$ . Using U, construct $X \sim \operatorname { E x p o } ( \lambda )$

16. s Let $U \sim \mathrm { U n i f } ( 0 , 1 )$ , and

$$
X = \log \left(\frac {U}{1 - U}\right).
$$

Then X has the Logistic distribution, as defined in Example 5.1.6.

(a) Write down (but do not compute) an integral giving $E ( X ^ { 2 } )$
(b) Find E(X) without using calculus.

Hint: A useful symmetry property here is that 1 − U has the same distribution as U.

17. Let $U \sim \mathrm { U n i f } ( 0 , 1 )$ . As a function of U, create an r.v. X with CDF $F ( x ) = 1 - e ^ { - x ^ { 3 } }$ for $x > 0 .$

18. The Pareto distribution with parameter $a > 0$ has PDF $f ( x ) = a / x ^ { a + 1 }$ for $x \geq 1$ (and 0 otherwise). This distribution is often used in statistical modeling.

(a) Find the $\mathrm { C D F }$ of a Pareto r.v. with parameter $^ { a ; }$ check that it is a valid CDF.

(b) Suppose that for a simulation you want to run, you need to generate i.i.d. Pareto(a) r.v.s. You have a computer that knows how to generate i.i.d. Unif(0, 1) r.v.s but does not know how to generate Pareto r.v.s. Show how to do this.

## Normal

19. Let $Z \sim \mathcal { N } ( 0 , 1 )$ . Create an r.v. $Y \sim \mathcal { N } ( 1 , 4 )$ , as a simple-looking function of Z. Make sure to check that your Y has the correct mean and variance.

20. Engineers sometimes work with the “error function”

$$
\mathrm{erf} (z) = \frac {2}{\sqrt {\pi}} \int_ {0} ^ {z} e ^ {- x ^ {2}} d x,
$$

instead of the standard Normal CDF Φ.

(a) Show that the following conversion between Φ and erf holds for all z:

$$
\Phi (z) = \frac {1}{2} + \frac {1}{2} \mathrm{erf} \left(\frac {z}{\sqrt {2}}\right).
$$

(b) Show that erf is an odd function, i.e., er $\operatorname { f } ( - z ) = - \operatorname { e r f } ( z )$

21. (a) Find the points of inflection of the $\mathcal { N } ( 0 , 1 )$ PDF $\varphi ,$ i.e., the points where the curve switches from convex (second derivative positive) to concave (second derivative negative) or vice versa.

(b) Use the result of (a) and a location-scale transformation to find the points of inflection of the $\mathcal { N } ( \mu , \sigma ^ { 2 } )$ PDF.

22. The distance between two points needs to be measured, in meters. The true distance between the points is 10 meters, but due to measurement error we can’t measure the distance exactly. Instead, we will observe a value of $1 0 + \epsilon ,$ where the error  is distributed $\mathcal { N } ( 0 , 0 . 0 4 )$ . Find the probability that the observed distance is within 0.4 meters of the true distance (10 meters). Give both an exact answer in terms of $\Phi$ and an approximate numerical answer.

23. Alice is trying to transmit to Bob the answer to a yes-no question, using a noisy channel. She encodes $\alpha _ { \mathrm { y e s } } ,$ as 1 and $" \mathrm{no} "$ as 0, and sends the appropriate value. However, the channel adds noise; specifically, Bob receives what Alice sends plus a $\mathcal { N } ( 0 , \sigma ^ { 2 } )$ noise term (the noise is independent of what Alice sends). If Bob receives a value greater than $1 / 2$ he interprets it as “yes”; otherwise, he interprets it as $"  no  "$

(a) Find the probability that Bob understands Alice correctly.

(b) What happens to the result from (a) if σ is very small? What about if $\sigma$ is very large? Explain intuitively why the results in these extreme cases make sense.

24. A woman is pregnant, with a due date of January 10, 2020. Of course, the actual date on which she will give birth is not necessarily the due date. On a timeline, define time 0 to be the instant when January 10, 2020 begins. Suppose that the time T when the woman gives birth has a Normal distribution, centered at 0 and with standard deviation 8 days. What is the probability that she gives birth on her due date? (Your answer should be in terms of $\Phi ,$ and simplified.)

25. We will show in the next chapter that if $X _ { 1 }$ and $X _ { 2 }$ are independent with $X _ { i } \sim$ $\mathcal { N } ( \mu _ { i } , \sigma _ { i } ^ { 2 } )$ , then $X _ { 1 } { + } X _ { 2 } { \sim } \mathcal { N } ( \mu _ { 1 } { + } \mu _ { 2 } , \sigma _ { 1 } ^ { 2 } { + } \sigma _ { 2 } ^ { 2 } )$ . Use this result to find $P ( X   <   Y )$ for $X \sim \mathcal { N } ( a , b ) , Y \sim \mathcal { N } ( c , d )$ with X and Y independent.

Hint: Write $P(X < Y) = P(X - Y < 0)$ and then standardize $X - Y$ . Check that your answer makes sense in the special case where X and Y are i.i.d.

26. Walter and Carl both often need to travel from Location A to Location B. Walter walks, and his travel time is Normal with mean w minutes and standard deviation σ minutes (travel time can’t be negative without using a tachyon beam, but assume that w is so much larger than $\sigma$ that the chance of a negative travel time is negligible).

Carl drives his car, and his travel time is Normal with mean c minutes and standard deviation 2σ minutes (the standard deviation is larger for Carl due to variability in traffic conditions). Walter’s travel time is independent of Carl’s. On a certain day, Walter and Carl leave from Location A to Location B at the same time.

(a) Find the probability that Carl arrives first (in terms of Φ and the parameters). For this you can use the important fact, proven in the next chapter, that if $X _ { 1 }$ and $X _ { 2 }$ are independent with $X _ { i } \sim \mathcal { N } ( \mu _ { i } , \sigma _ { i } ^ { 2 } )$ , then $X _ { 1 } + X _ { 2 } \sim \mathcal { N } ( \mu _ { 1 } + \mu _ { 2 } , \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } )$

(b) Give a fully simplified criterion (not in terms of Φ), such that Carl has more than a 50% chance of arriving first if and only if the criterion is satisfied.

(c) Walter and Carl want to make it to a meeting at Location B that is scheduled to begin w +10 minutes after they depart from Location A. Give a fully simplified criterion (not in terms of Φ) such that Carl is more likely than Walter to make it on time for the meeting if and only if the criterion is satisfied.

27. Let $Z \sim \mathcal { N } ( 0 , 1 )$ . We know from the 68-95-99.7% rule that there is a 68% chance of $Z$ being in the interval $( - 1 , 1 )$ . Give a visual explanation of whether or not there is an interval $( a , b )$ that is shorter than the interval (−1, 1), yet which has at least as large a chance as $( - 1 , 1 )$ of containing $Z .$

28. Let $Y \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ . Use the fact that $P ( | Y - \mu | < 1 . 9 6 \sigma ) \approx 0 . 9 5$ to construct a random interval $( a ( Y ) , b ( Y ) )$ (that is, an interval whose endpoints are r.v.s), such that the probability that $\mu$ is in the interval is approximately 0.95. This interval is called a confidence interval for $\mu ;$ such intervals are often desired in statistics when estimating unknown parameters based on data.

29. Let $Y = | X | ,$ with $X \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ . This is a well-defined continuous $\mathbf { r } . \mathbf { v } . ,$ even though the absolute value function is not differentiable at 0 (due to the sharp corner).

(a) Find the CDF of Y in terms of Φ. Be sure to specify the CDF everywhere.

(b) Find the PDF of $Y .$

(c) Is the PDF of $Y$ continuous at 0? If not, is this a problem as far as using the PDF to find probabilities?

30. s Let $Z   \sim   \mathcal { N } ( 0 , 1 )$ and let $S$ be a random sign independent of $Z , \; \mathrm { i . e . } , \; S$ is 1 with probability $1 / 2$ and −1 with probability $1 / 2 .$ Show that $S Z \sim \mathcal { N } ( 0 , 1 )$

31. s Let $Z \sim \mathcal { N } ( 0 , 1 )$ . Find $E \left( \Phi ( Z ) \right)$ without using LOTUS, where Φ is the CDF of $Z .$

32. s Let $Z \sim \mathcal { N } ( 0 , 1 )$ and $X = Z ^ { 2 }$ . Then the distribution of X is called Chi-Square with 1 degree of freedom. This distribution appears in many statistical methods.

(a) Find a good numerical approximation to $P ( 1 \leq X \leq 4 )$ using facts about the Normal distribution, without querying a calculator/computer/table about values of the Normal CDF.

(b) Let Φ and $\varphi$ be the CDF and PDF of $Z ,$ respectively. Show that for any $t > 0$ $I ( Z > t ) \leq ( Z / t ) I ( Z > t )$ . Using this and LOTUS, derive $M i l l s$ inequality, which is the following lower bound on Φ:

$$
\Phi (t) \geq 1 - \varphi (t) / t.
$$

33. Let $Z \sim \mathcal { N } ( 0 , 1 )$ , with CDF Φ. We will show in Chapter 8 that the PDF of $Z ^ { 2 }$ is the function g given by

$$
g (w) = \frac {1}{\sqrt {2 \pi w}} e ^ {- w / 2}
$$

for $w > 0 .$ , and $g ( w ) = 0$ for $w \leq 0$

(a) Find expressions for $E ( Z ^ { 4 } )$ as integrals in two different ways, one based on the PDF of Z and the other based on the PDF of $Z ^ { 2 }$

(b) Find $E ( Z ^ { 2 } + Z + \Phi ( Z ) )$

34. s Let $Z \sim \mathcal { N } ( 0 , 1 )$ . A measuring device is used to observe $Z ,$ but the device can only handle positive values, and gives a reading of 0 if $Z \leq 0 ;$ this is an example of censored data. So assume that $X = Z I _ { Z > 0 }$ is observed rather than $Z ,$ where $I _ { Z > 0 }$ is the indicator of $Z > 0$ . Find $E ( X )$ and $\operatorname { V a r } ( X )$

35. Let $Z \sim \mathcal { N } ( 0 , 1 )$ , and c be a nonnegative constant. Find $E ( \operatorname* { m a x } ( Z - c , 0 ) )$ , in terms of the standard Normal CDF Φ and PDF $\varphi .$ (This kind of calculation often comes up in quantitative finance.)

Hint: Use LOTUS, and handle the max symbol by adjusting the limits of integration appropriately. As a check, make sure that your answer reduces to $1 / \sqrt { 2 \pi }$ <u>wh</u>en $c = 0 ;$ this must be the case since we showed in Example 5.4.7 that $E | Z |   =   { \sqrt { 2 / \pi } } ,$ and we have $| Z | = \operatorname* { m a x } ( Z , 0 ) + \operatorname* { m a x } ( - Z , 0 )$ so by symmetry

$$
E | Z | = E (\max (Z, 0)) + E (\max (- Z, 0)) = 2 E (\max (Z, 0)).
$$

## Exponential

36. s A post office has 2 clerks. Alice enters the post office while 2 other customers, Bob and Claire, are being served by the 2 clerks. She is next in line. Assume that the time a clerk spends serving a customer has an Expo(λ) distribution.

(a) What is the probability that Alice is the last of the 3 customers to be done being served?

Hint: No integrals are needed.

(b) What is the expected total time that Alice needs to spend at the post office?

37. Let T be the time until a radioactive particle decays, and suppose (as is often done in physics and chemistry) that $T \sim \operatorname{Exp}(\lambda)$

(a) The half-life of the particle is the time at which there is a 50% chance that the particle has decayed (in statistical terminology, this is the median of the distribution of T). Find the half-life of the particle.

(b) Show that for $\epsilon \textbf { a }$ small, positive constant, the probability that the particle decays in the time interval $[ t , t + \epsilon ]$ , given that it has survived until time $t ,$ does not depend on t and is approximately proportional to .

Hint: $e ^ { x } \approx 1 + x { \mathrm { ~ i f ~ } } x \approx 0 .$

(c) Now consider n radioactive particles, with i.i.d. times until decay $T _ { 1 } , \ldots , T _ { n } \; \sim$ Expo(λ). Let L be the first time at which one of the particles decays. Find the CDF of L. Also, find E(L) and Var(L).

(d) Continuing (c), find the mean and variance of $M = \operatorname* { m a x } ( T _ { 1 } , \ldots , T _ { n } )$ , the last time at which one of the particles decays, without using calculus.

Hint: Draw a timeline, apply (c), and remember the memoryless property.

38. s Fred wants to sell his car, after moving back to Blissville (where he is happy with the bus system). He decides to sell it to the first person to offer at least \$18,000 for it. Assume that the offers are independent Exponential random variables with mean \$12,000, and that Fred is able to keep getting offers until he obtains one that meets his criterion.

(a) Find the expected number of offers Fred will have.

(b) Find the expected amount of money that Fred will get for the car.

39. As in the previous problem, Fred wants to sell his car, and the offers for his car are i.i.d. Exponential r.v.s with mean \$12,000. Assume now though that he will wait until he has 3 offers (no matter how large or small they are), and then accept the largest of the 3 offers. Find the expected amount of money that Fred will get for his car.

40. (a) Fred visits Blotchville again. He finds that the city has installed an electronic display at the bus stop, showing the time when the previous bus arrived. The times between arrivals of buses are still independent Exponentials with mean 10 minutes. Fred waits for the next bus, and then records the time between that bus and the previous bus. On average, what length of time between buses does he see?

(b) Fred then visits Blunderville, where the times between buses are also 10 minutes on average, and independent. Yet to his dismay, he finds that on average he has to wait more than 1 hour for the next bus when he arrives at the bus stop! How is it possible that the average Fred-to-bus time is greater than the average bus-to-bus time even though Fred arrives at some time between two bus arrivals? Explain this intuitively, and construct a specific discrete distribution for the times between buses showing that this is possible.

41. Fred and Gretchen are waiting at a bus stop in Blotchville. Two bus routes, Route 1 and Route 2, have buses that stop at this bus stop. For Route i, buses arrive according to a Poisson process with rate $\lambda _ { i }$ buses/minute. The Route 1 process is independent of the Route 2 process. Fred is waiting for a Route 1 bus, and Gretchen is waiting for a Route 2 bus.

(a) Given that Fred has already waited for 20 minutes, on average how much longer will he have to wait for his bus?

(b) Find the probability that at least n Route 1 buses will pass by before the first Route 2 bus arrives. The following result from Chapter 7 may be useful here: for independent random variables $X _ { 1 } \sim \operatorname { E x p o } ( \lambda _ { 1 } ) , X _ { 2 } \sim \operatorname { E x p o } ( \lambda _ { 2 } )$ , we have $P ( X _ { 1 } < X _ { 2 } ) = \lambda _ { 1 } / ( \lambda _ { 1 } { + } \lambda _ { 2 } )$

(c) For this part only, assume that $\lambda_{1} = \lambda_{2} = \lambda$ . Find the expected time it will take until both Fred and Gretchen have caught their buses.

42. s Joe is waiting in continuous time for a book called The Winds of Winter to be released. Suppose that the waiting time T until news of the book’s release is posted, measured in years relative to some starting point, has an Exponential distribution with $\lambda = 1 / 5$

Joe is not so obsessive as to check multiple times a day; instead, he checks the website once at the end of each day. Therefore, he observes the day on which the news was posted, rather than the exact time T. Let X be this measurement, where $X = 0$ means that the news was posted within the first day (after the starting point), X = 1 means it was posted on the second day, etc. (assume that there are 365 days in a year). Find the PMF of X. Is this a named distribution that we have studied?

43. The Exponential is the analog of the Geometric in continuous time. This problem explores the connection between Exponential and Geometric in more detail, asking what happens to a Geometric in a limit where the Bernoulli trials are performed faster and faster but with smaller and smaller success probabilities.

Suppose that Bernoulli trials are being performed in continuous time; rather than only thinking about first trial, second trial, etc., imagine that the trials take place at points on a timeline. Assume that the trials are at regularly spaced times $0 , \Delta t , 2 \Delta t , \ldots ,$ where $\Delta t$ is a small positive number. Let the probability of success of each trial be $\lambda \Delta t ,$ where λ is a positive constant. Let G be the number of failures before the first success (in discrete time), and $T$ be the time of the first success (in continuous time).

(a) Find a simple equation relating G to $T .$

Hint: Draw a timeline and try out a simple example.

(b) Find the CDF of $T .$

Hint: First find $P ( T > t )$

(c) Show that as $\Delta t \to 0 .$ the CDF of $T$ converges to the Expo(λ) CDF, evaluating all the CDFs at a fixed $t \geq 0$

Hint: Use the compound interest limit (see Section A.2.5 of the math appendix).

44. The Laplace distribution has PDF

$$
f (x) = \frac {1}{2} e ^ {- | x |}
$$

for all real $x .$ The Laplace distribution is also called a symmetrized Exponential distribution. Explain this in the following two ways.

(a) Plot the PDFs and explain how they relate.

(b) Let $X \sim \mathrm { E x p o ( 1 ) }$ and S be a random sign (1 or −1, with equal probabilities), with S and X independent. Find the PDF of SX (by first finding the CDF), and compare the PDF of SX and the Laplace PDF.

45. Emails arrive in an inbox according to a Poisson process with rate 20 emails per hour. Let $T$ be the time at which the 3rd email arrives, measured in hours after a certain fixed starting time. Find $P ( T > 0 . 1 )$ without using calculus.

Hint: Apply the count-time duality.

46. Let $T$ be the lifetime of a certain person (how long that person lives), and let $T$ have CDF F and PDF $f .$ The hazard function of $T$ is defined by

$$
h (t) = \frac {f (t)}{1 - F (t)}.
$$

(a) Explain why h is called the hazard function and in particular, why $h ( t )$ is the probability density for death at time t, given that the person survived up until then.
(b) Show that an Exponential r.v. has constant hazard function and conversely, if the hazard function of $T$ is a constant then $T$ must be $\operatorname { E x p o } ( \lambda )$ for some λ.

47. Let $T$ be the lifetime of a person (or animal or gadget), with CDF $F$ and PDF $f .$ Let h be the hazard function, defined as in the previous problem. If we know $F$ then we can calculate $f ,$ and then in turn we can calculate $h .$ In this problem, we consider the reverse problem: how to recover F and f from knowing $h .$

(a) Show that the CDF and hazard function are related by

$$
F (t) = 1 - \exp \left(- \int_ {0} ^ {t} h (s) d s\right),
$$

for all $t > 0$

Hint: Let $G ( t ) = 1   -   F ( t )$ be the survival function, and consider the derivative of log $G ( t )$

(b) Show that the PDF and hazard function are related by

$$
f (t) = h (t) \exp \left(- \int_ {0} ^ {t} h (s) d s\right),
$$

for all $t > 0$

Hint: Apply the result of (a).

48. s Find $E ( X ^ { 3 } )$ for $X   \sim   \mathrm { E x p o } ( \lambda )$ , using LOTUS and the fact that $E ( X )   =   1 / \lambda$ and $\operatorname { V a r } ( X ) = 1 / \lambda ^ { 2 }$ , and integration by parts at most once. In the next chapter, we’ll learn how to find $E ( X ^ { n } )$ for all n.

49. s The Gumbel distribution is the distribution of − log X with X ∼ Expo(1).

(a) Find the CDF of the Gumbel distribution.

(b) Let $X _ { 1 } , X _ { 2 } , \ldots$ . be i.i.d. Expo(1) and let $M _ { n } = \operatorname* { m a x } ( X _ { 1 } , \ldots , X _ { n } )$ . Show that $M _ { n } -$ log n converges in distribution to the Gumbel distribution, i.e., as $n \to \infty$ the CDF of $M _ { n } - \log n$ converges to the Gumbel CDF.

## Mixed practice

50. Explain intuitively why $P(X < Y) = P(Y < X)$ if X and Y are i.i.d., but equality may not hold if X and Y are not independent or not identically distributed.

51. Let X be an r.v. (discrete or continuous) such that $0 \; \leq \; X \; \leq \; 1$ always holds. Let $\mu = E ( X )$

(a) Show that

$$
\mathrm{Var} (X) \leq \mu - \mu^ {2} \leq \frac {1}{4}.
$$

Hint: With probability 1, we have $X ^ { 2 } \leq X$

(b) Show that there is only one possible distribution for X for which $\operatorname { V a r } ( X )   =   1 / 4$ What is the name of this distribution?

52. The Rayleigh distribution from Example 5.1.7 has PDF

$$
f (x) = x e ^ {- x ^ {2} / 2}, \quad x > 0.
$$

Let X have the Rayleigh distribution.

(a) Find $E ( X )$ without using much calculus, by interpreting the integral in terms of known results about the Normal distribution.

(b) Find $E ( X ^ { 2 } )$

Hint: A nice approach is to use LOTUS and the substitution $u = x ^ { 2 } / 2$ , and then interpret the resulting integral in terms of known results about the Exponential distribution.

53. s Consider an experiment where we observe the value of a random variable X, and estimate the value of an unknown constant θ using some random variable $T = g ( X )$ that is a function of X. The r.v. T is called an estimator. Think of X as the data observed in the experiment, and θ as an unknown parameter related to the distribution of X.

For example, consider the experiment of flipping a coin n times, where the coin has an unknown probability θ of Heads. After the experiment is performed, we have observed the value of $X \sim \operatorname { B i n } ( n , \theta )$ . The most natural estimator for θ is then $X / n .$

The bias of an estimator T for θ is defined as $b ( T ) = E ( T ) - \theta$ . The mean squared error is the average squared error when using $T ( X )$ to estimate θ:

$$
\mathrm{MSE} (T) = E (T - \theta) ^ {2}.
$$

Show that

$$
\mathrm{MSE} (T) = \mathrm{Var} (T) + (b (T)) ^ {2}.
$$

This implies that for fixed MSE, lower bias can only be attained at the cost of higher variance and vice versa; this is a form of the bias-variance tradeoff, a phenomenon which arises throughout statistics.

54. s (a) Suppose that we have a list of the populations of every country in the world.

Guess, without looking at data yet, what percentage of the populations have the digit 1 as their first digit (e.g., a country with a population of 1,234,567 has first digit 1 and a country with population 89,012,345 does not).

(b) After having done $( \mathrm { a } )$ , look through a list of populations and count how many start with a 1. What percentage of countries is this? Benford’s law states that in a very large variety of real-life data sets, the first digit approximately follows a particular distribution with about a 30% chance of a 1, an 18% chance of a 2, and in general

$$
P (D = j) = \log_ {1 0} \left(\frac {j + 1}{j}\right), \text {for} j \in \{1, 2, 3, \dots , 9 \},
$$

where $D$ is the first digit of a randomly chosen element. (Exercise 6 from Chapter 3 asks for a proof that this is a valid PMF.) How closely does the percentage found in the data agree with that predicted by Benford’s law?

(c) Suppose that we write the random value in some problem $( \mathbf { e . g . }$ , the population of a random country) in scientific notation as $X \times 1 0 ^ { N }$ , where N is a nonnegative integer and $1 \leq X < 1 0$ . Assume that X is a continuous r.v. with PDF

$$
f (x) = c / x, \text {for} 1 \leq x \leq 1 0,
$$

and 0 otherwise, with c a constant. What is the value of c (be careful with the bases of $\mathrm { l o g s ) ? }$ Intuitively, we might hope that the distribution of X does not depend on the choice of units in which $X$ is measured. $\mathrm { T o }$ see whether this holds, let $Y = a X$ with $a > 0$ . What is the PDF of $Y$ (specifying where it is nonzero)?

(d) Show that if we have a random number $X \times 1 0 ^ { N }$ (written in scientific notation) and X has the PDF $f$ from (c), then the first digit (which is also the first digit of $X )$ has Benford’s law as its PMF.

Hint: What does $D = j$ correspond to in terms of the values of X?

55. $\textcircled{s} \mathrm{~(a)}$ Let $X _ { 1 } , X _ { 2 } , \ldots$ . be independent $\mathcal { N } ( 0 , 4 ) \; \operatorname { r . v . s . }$ , and let J be the smallest value of $j$ such that $X _ { j } > 4 { \mathrm { ( i . e . } }$ , the index of the first $X _ { j }$ exceeding 4). In terms of Φ, find $E ( J )$

(b) Let $f$ and $g$ be PDFs with $f ( x )   >   0$ and $g ( x )   >   0$ for all x. Let X be a random variable with PDF $f .$ Find the expected value of the ratio

$$
R = \frac {g (X)}{f (X)}.
$$

Such ratios come up very often in statistics, when working with a quantity known as a likelihood ratio and when using a computational technique known as importance sampling.

(c) Define

$$
F (x) = e ^ {- e ^ {- x}}.
$$

This is a CDF and is a continuous, strictly increasing function. Let X have CDF $F ,$ and define $W = F ( X )$ . What are the mean and variance of $W ?$

56. Let $X , Y , Z \sim \mathcal { N } ( 0 , 1 )$ be i.i.d.

(a) Find an expression for $E \left( Z ^ { 2 }   \Phi ( Z ) \right)$ as an integral.
(b) Find $P ( \Phi ( Z ) < 2 / 3 )$
(c) Find $P(X < Y < Z)$

57. Let $X , Y , Z \sim \mathcal { N } ( 0 , 1 )$ be i.i.d., and $W = ( \Phi ( Z ) ) ^ { 2 }$

(a) Find the CDF and PDF of W.
(b) Let $f _ { W }$ be the PDF of $W$ and $\varphi$ be the PDF of Z. Find unsimplified expressions for $E ( W ^ { 3 } )$ as integrals in two different ways, one based on $f _ { W }$ and one based on $\varphi .$
(c) Find $P(X + 2Y < 2Z + 3)$ , in terms of Φ.

Hint: Move all of the r.v.s to one side of the inequality.

58. Let $Z \sim \mathcal { N } ( 0 , 1 )$ and $Y = \operatorname* { m a x } ( Z , 0 )$ . So $Y$ is $Z$ if $Z > 0 ,$ and $Y$ is 0 if $Z \leq 0$

(a) Find an expression for $E ( Y )$ as an integral (which can be unsimplified).

(b) Let $Y _ { 1 } , Y _ { 2 } , \ldots$ be independent $\mathbf { r . v . s , }$ each with the same distribution as $Y$ Let $N = \operatorname* { m i n } \{ n : Y _ { n } = 0 \}$ , i.e., N is the smallest value such that $Y _ { N } = 0$ . Find $E ( N )$

(c) Find the CDF of Y in terms of Φ. (Be sure to specify it for all real numbers.)

59. The unit circle $\{ ( x , y ) : x ^ { 2 } + y ^ { 2 } = 1 \}$ is divided into three arcs by choosing three random points A, B, C on the circle (independently and uniformly), forming arcs between A and $B ,$ between A and C, and between B and C. Let L be the length of the arc containing the point (1, 0). What is $E ( L ) ?$ Study this by working through the following steps.

(a) Explain what is wrong with the following argument: “The total length of the arcs is 2π, the circumference of the circle. So by symmetry and linearity, each arc has length $2 \pi / 3$ on average. Referring to the arc containing $( 1 , 0 )$ is just a way to specify one of the arcs (it wouldn’t matter if $( 1 , 0 )$ were replaced by $( 0 , - 1 )$ or any other specific point on the circle in the statement of the problem). So the expected value of $L$ is $2 \pi / 3 . ^ { \circ }$

(b) Let the arc containing $( 1 , 0 )$ be divided into two pieces: the piece extending counterclockwise from $( 1 , 0 )$ and the piece extending clockwise from (1, 0). Write $L = L _ { 1 } + L _ { 2 }$ where $L _ { 1 }$ and $L _ { 2 }$ are the lengths of the counterclockwise and clockwise pieces, respectively. Find the CDF, PDF, and expected value of $L _ { 1 }$

(c) Use (b) to find $E ( L )$

60. s As in Example 5.7.4, athletes compete one at a time at the high jump. Let $X _ { j }$ be how high the jth jumper jumped, with $X _ { 1 } , X _ { 2 } , \ldots$ i.i.d. with a continuous distribution. We say that the jth jumper is “best in recent memory” if they jump higher than the previous 2 jumpers (for $j \geq 3 ;$ the first 2 jumpers don’t qualify).

(a) Find the expected number of best in recent memory jumpers among the 3rd through nth jumpers.

(b) Let $A _ { j }$ be the event that the jth jumper is the best in recent memory. Find $\widetilde { P } ( A _ { 3 } ) , P ( \widetilde { A } _ { 4 } )$ , and $P ( A _ { 3 } \cap A _ { 4 } )$ . Are $A _ { 3 }$ and $A _ { 4 }$ independent?

61. Tyrion, Cersei, and n other guests arrive at a party at i.i.d. times drawn from a continuous distribution with support [0, 1], and stay until the end (time 0 is the party’s start time and time 1 is the end time). The party will be boring at times when neither Tyrion nor Cersei is there, fun when exactly one of them is there, and awkward when both $\mathrm { T y }$ rion and Cersei are there.

(a) On average, how many of the n other guests will arrive at times when the party is fun?

(b) Jaime and Robert are two of the other guests. $\mathrm { B y }$ computing both sides in the definition of independence, determine whether the event “Jaime arrives at a fun time” is independent of the event “Robert arrives at a fun time”.

(c) Give a clear intuitive explanation of whether the two events from (b) are independent, and whether they are conditionally independent given the arrival times of everyone else, i.e., everyone except Jaime and Robert.

62. Let $X _ { 1 } , X _ { 2 } , \ldots$ . be the annual rainfalls in Boston (measured in inches) in the years 2101, $2 1 0 2 ,   \ldots ,$ respectively. Assume that annual rainfalls are i.i.d. draws from a continuous distribution. A rainfall value is a record high if it is greater than those in all previous years (starting with 2101), and a record low if it is lower than those in all previous years.

(a) In the 22nd century (the years 2101 through 2200, inclusive), find the expected number of years that have either a record low or a record high rainfall.
(b) On average, in how many years in the 22nd century is there a record low followed in the next year by a record high? (Only the record low is required to be in the 22nd century, not the record high.)
(c) By definition, the year 2101 is a record high (and record low). Let N be the number of years required to get a new record high. Find $P ( N > n )$ for all positive integers n, and use this to find the PMF of N.

Hint: Note that $P(N = n) + P(N > n) = P(N > n - 1)$

(d) With notation as above, show that $E ( N )$ is infinite.

## Moments

The nth moment of an r.v. X is $E ( X ^ { n } )$ . In this chapter, we explore how the moments of an r.v. shed light on its distribution. We have already seen that the first two moments are useful since they provide the mean $E ( X )$ and variance $E ( X ^ { 2 } ) - ( E X ) ^ { 2 }$ which are important summaries of the average value of X and how spread out its distribution is. But there is much more to a distribution than its mean and variance. We’ll see that the third and fourth moments tell us about the asymmetry of a distribution and the behavior of the tails or extreme values, two properties that are not captured by the mean and variance. After introducing moments, we’ll discuss the moment generating function (MGF), which not only helps us compute moments but also provides a useful alternative way to specify a distribution.

## 6.1 Summaries of a distribution

The mean is called a measure of central tendency because it tells us something about the center of a distribution, specifically its center of mass. Other measures of central tendency that are commonly used in statistics are the median and the mode, which we now define.

Definition 6.1.1 (Median). We say that c is a median of a random variable X if $P ( X \leq c ) \geq 1 / 2$ and $P ( X \geq c ) \geq 1 / 2$ . (The simplest way this can happen is if the CDF of X hits 1/2 exactly at $c _ { \gamma }$ but we know that some CDFs have jumps.)

Definition 6.1.2 (Mode). For a discrete r.v. X, we say that c is a mode of X if it maximizes the PMF: $P(X = c) \geq P(X = x)$ for all x. For a continuous r.v. X with PDF $f ,$ we say that c is a mode if it maximizes the PDF: $f ( c ) \geq f ( x )$ for all x.

As with the mean, the median and mode of an r.v. depend only on its distribution, so we can talk about the mean, median, or mode of a distribution without referring to any particular r.v. that has that distribution. For example, if $Z \sim \mathcal { N } ( 0 , 1 )$ then the median of $Z$ is 0 (since $\Phi ( 0 )   =   1 / 2$ by symmetry), and we also say that the standard Normal distribution has median 0.

Intuitively, the median is a value c such that half the mass of the distribution falls on either side of c (or as close to half as possible, for discrete r.v.s), and the mode is a value that has the greatest mass or density out of all values in the support of

X. If the CDF F is a continuous, strictly increasing function, then $F ^ { - 1 } ( 1 / 2 )$ is the median (and is unique).

Note that a distribution can have multiple medians and multiple modes. Medians have to occur side by side; modes can occur all over the distribution. In Figure 6.1, we show a distribution supported on $[ - 5 , - 1 ] \cup [ 1 , 5 ]$ that has two modes and infinitely many medians. The PDF is 0 between −1 and 1, so all values between −1 and 1 are medians of the distribution because half of the mass falls on either side. The two modes are at −3 and 3.

![](images/page_284_chart_4.jpg)

<details>
<summary>line</summary>

| X | PDF |
| --- | --- |
| -5 | ~0.00 |
| -4 | ~0.12 |
| -3 | 0.40 |
| -2 | ~0.08 |
| -1 | ~0.00 |
| 0 | ~0.00 |
| 1 | ~0.00 |
| 2 | ~0.12 |
| 3 | 0.40 |
| 4 | ~0.12 |
| 5 | ~0.00 |
</details>

## FIGURE 6.1

A distribution with two modes (−3 and 3) and infinitely many medians (all x in the interval [−1, 1]).

Example 6.1.3 (Mean, median, and mode for salaries). A certain company has 100 employees. Let $s _ { 1 } , s _ { 2 } , \ldots , s _ { 1 0 0 }$ be their salaries, sorted in increasing order (we can still do this even if some salaries appear more than once). Let X be the salary of a randomly selected employee (chosen uniformly). The mean, median, and mode for the data set $s _ { 1 } , s _ { 2 } , \ldots , s _ { 1 0 0 }$ are defined to be the corresponding quantities for X.

What is a typical salary? What is the most useful one-number summary of the salary data? The answer, as is often the case, is it depends on the goal. Different summaries reveal different characteristics of the data, so it may be hard to choose just one number—and it is often unnecessary to do so, since usually we can provide several summaries (and plot the data too). Here we briefly compare the mean, median, and mode, though often it makes sense to report all three (and other summaries too).

If the salaries are all different, the mode doesn’t give a useful one-number summary since there are 100 modes. If there are only a few possible salaries in the company, the mode becomes more useful. But even then it could happen that, for example, 34 people receive salary a, 33 receive salary b, and 33 receive salary c. Then a is the unique mode, but if we only report a we are ignoring b and $c _ { \gamma }$ which just barely missed being modes and which together account for almost $2 / 3$ of the data.

Next, let’s consider the median. There are two numbers $\mathrm { { ^ { \circ } i n } }$ the $\mathrm { m i d d l e  , ~ } s _ { 5 0 }$ and $s _ { 5 1 }$ . In fact, any number $m$ with $s _ { 5 0 } \leq m \leq s _ { 5 1 }$ is a median, since there is at least a 50% chance that the random employee’s salary is in $\{ s _ { 1 } , \ldots , s _ { 5 0 } \}$ (in which case it is at most $m )$ and at least a 50% chance that it is in $\{ s _ { 5 1 } , \ldots , s _ { 1 0 0 } \}$ (in which case it is at least $m )$ . The usual convention is to choose $m   =   ( s _ { 5 0 }   +   s _ { 5 1 } ) / 2$ , the mean of the two numbers in the middle. If the number of employees had been odd, this issue would not have come up; in that case, there is a unique median, the number in the middle when all the salaries are listed in increasing order.

Compared with the mean, the median is much less sensitive to extreme values. For example, if the $\mathrm { C E O ^ { \circ } s }$ salary is changed from being slightly more than anyone else’s to vastly more than anyone else’s, that could have a large impact on the mean but it has no impact on the median. This robustness is a reason that the median could be a more sensible summary than the mean of what the typical salary is. On the other hand, suppose that we want to know the total cost the company is paying for its employees’ salaries. If we only know a mode or a median, we can’t extract this information, but if we know the mean we can just multiply it by 100. 

Suppose that we are trying to guess what a not-yet-observed r.v. X will be, by making a prediction $c .$ The mean and the median both seem like natural guesses for $c _ { \gamma }$ but which is better? That depends on how “better” is defined. Two natural ways to judge how good c is are the mean squared error $E ( X - c ) ^ { 2 }$ and the mean absolute error $E | X - c |$ . The following result says what the best guesses are in both cases.

Theorem 6.1.4. Let X be an r.v. with mean $\mu ,$ and let m be a median of $X$ .

• The value of $c$ that minimizes the mean squared error $E ( X - c ) ^ { 2 } { \mathrm { ~ i s ~ } } c = \mu .$
• A value of $c$ that minimizes the mean absolute error $E | X - c |   is   c = m$

Proof. We will first prove a useful identity:

$$
E (X - c) ^ {2} = \mathrm{Var} (X) + (\mu - c) ^ {2}.
$$

This can be checked by expanding everything out, but a faster way is to use the fact that adding a constant doesn’t affect the variance:

$$
\operatorname{Var} (X) = \operatorname{Var} (X - c) = E (X - c) ^ {2} - (E (X - c)) ^ {2} = E (X - c) ^ {2} - (\mu - c) ^ {2}.
$$

It follows that $c   =   \mu$ is the unique choice that minimizes $E ( X - c ) ^ { 2 }$ , since that choice makes $( \mu - c ) ^ { 2 } = 0$ and any other choice makes $( \mu - c ) ^ { 2 } > 0$

Next, let’s consider the mean absolute error. Let $a \neq m$ . We need to show that $E | X - m | \leq E | X - a |$ , which is equivalent to $E ( | X - a | - | X - m | ) \geq 0$ . Assume that $m < a$ (the case $m > a$ can be handled similarly). If $X \leq m$ then

$$
| X - a | - | X - m | = a - X - (m - X) = a - m,
$$

and if $X > m$ then

$$
| X - a | - | X - m | \geq X - a - (X - m) = m - a.
$$

Let

$$
Y = | X - a | - | X - m |.
$$

We can split the definition of $E ( Y )$ into 2 parts based on whether $X \leq m$ occurs, using indicator r.v.s. Let I be the indicator r.v. for $X \leq m$ , so $1 - I$ is the indicator r.v. for $X > m$ . Then

$$
\begin{array}{l} E (Y) = E (Y I) + E (Y (1 - I)) \\ \geq (a - m) E (I) + (m - a) E (1 - I) \\ = (a - m) P (X \leq m) + (m - a) P (X > m) \\ = (a - m) P (X \leq m) - (a - m) (1 - P (X \leq m)) \\ = (a - m) (2 P (X \leq m) - 1). \\ \end{array}
$$

By definition of median, we have $2 P ( X   \leq   m ) - 1   \geq   0$ . Thus, $E ( Y )   \geq   0 ,$ which implies $E ( | X - m | ) \leq E ( | X - a | )$ 

![](images/page_286_chart_9.jpg)

<details>
<summary>violin</summary>

| x | PDF (Black Line) | PDF (Grey Line) |
| --- | --- | --- |
| -5 | 0 | ~0.01 |
| 0 | 0 | ~0.10 |
| 0.2 | ~0.68 | ~0.11 |
| 2.5 | ~0.12 | ~0.12 |
| 5 | ~0.03 | ~0.09 |
| 10 | 0 | ~0.02 |
</details>

## FIGURE 6.2

Two PDFs with mean 2 and variance 12. The light curve is Normal and symmetric; the dark curve is Log-Normal and right-skewed.

Regardless of which measure of central tendency we use in a particular application, it is usually important also to know about the spread of the distribution as measured by, for example, the variance. However, there are also major features of a distribution that are not captured by the mean and variance. For example, the two PDFs in Figure 6.2 both have mean 2 and variance 12. The light curve is the $\mathcal { N } ( 2 , 1 2 )$ PDF and the dark curve belongs to the Log-Normal family of distributions (the Log-Normal is defined later in this chapter). The Normal curve is symmetric about 2, so its mean, median, and mode are all 2. In contrast, the Log-Normal is heavily skewed to the right; this means its right tail is very long compared to its left tail. It has mean 2, but median 1 and mode 0.25. From the mean and variance alone, we would not be able to capture the difference between the asymmetry of the Log-Normal and the symmetry of the Normal.

Now consider Figure 6.3, which shows the PMF of a $\mathrm { B i n } ( 1 0 , 0 . 9 )$ r.v. on the left and the PMF of 8 plus a Bin(10, 0.1) r.v. on the right. Both of these distributions have mean, median, and mode equal to 9 and variance equal to 0.9, but they look drastically different. We say that the PMF on the left is left-skewed and the PMF on the right is right-skewed. In this chapter we’ll learn that a standard measure of the asymmetry of a distribution is based on the third moment.

![](images/page_287_image_4.jpg)

FIGURE 6.3

Left: Bin(10, 0.9) is left-skewed. Right: Bin(10, 0.1), shifted to the right by 8, is right-skewed but has the same mean, median, mode, and variance as Bin(10, 0.9).

The previous two examples considered asymmetric distributions, but symmetric distributions with the same mean and variance can also look very different. The left plot in Figure 6.4 shows two symmetric PDFs with mean 0 and variance 1. The light curve is the $\mathcal { N } ( 0 , 1 )$ PDF and the dark curve is the t<sub>3</sub> PDF, scaling it to have variance 1 (we’ll define the $t _ { 3 }$ distribution in Chapter 10). The dark curve has a sharper peak and heavier tails than the light curve. The tail behavior is magnified in the right plot, where it is easy to see that the dark curve decays to 0 much more gradually, making outcomes far out in the tail much more likely than for the light curve. As we’ll learn in this chapter, a standard measure of the heaviness of the tails of a distribution is based on the fourth moment.

In the next section, we will go into further detail of how to interpret moments, especially the first four moments.