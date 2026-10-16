Solution:

Using properties of logs, we have

$$
D (\mathbf {p}, \mathbf {r}) = - \sum_ {j = 1} ^ {n} p _ {j} \log_ {2} \left(\frac {r _ {j}}{p _ {j}}\right).
$$

Let Y be a random variable that takes on values $r _ { j } / p _ { j }$ with probabilities $p _ { j }$ , so that $D ( \mathbf { p } , \mathbf { r } ) = - E ( \log _ { 2 } ( Y ) )$ by LOTUS. Then by Jensen’s inequality,

$$
D (\mathbf {p}, \mathbf {r}) = - E (\log_ {2} (Y)) \geq - \log_ {2} (E (Y)) = - \log_ {2} (1) = 0,
$$

with equality if and only if $\mathbf { p } = \mathbf { r }$ . This result tells us that we’re more surprised on average when we work with the wrong probabilities than when we work with the correct probabilities. 

Example 10.1.9 (Log probability scoring). Imagine that on a multiple-choice exam, instead of circling just one of the answer choices, you are asked to assign a probability of correctness to each choice. Your score on a particular question is the log of the probability that you assign to the correct answer. The maximum score for a particular question is 0, and the minimum score is $- \infty$ , attained if you assign zero probability to the correct answer.<sup>1</sup>

Suppose your personal probabilities of correctness for each of the n answer choices are $p _ { 1 } , \ldots , p _ { n }$ , where the $p _ { j }$ are positive and sum to 1. Show that your expected score on a question is maximized if you report your true probabilities $p _ { j }$ , not any other probabilities. In other words, under log probability scoring, you have no incentive to lie about your beliefs and pretend to be more or less confident than you really are (assuming that your goal is to maximize your expected score).

Solution:

This example is isomorphic to the previous one! Your expected score on a question is $\textstyle \sum _ { j = 1 } ^ { n } p _ { j }$ log $p _ { j }$ if you report your true probabilities p, and $\textstyle \sum _ { j = 1 } ^ { n } p _ { j }$ log $r _ { j }$ if you report false probabilities r. The difference between these two is precisely the Kullback-Leibler divergence between p and r. This is always nonnegative, as we proved in the previous example. Therefore your expected score is maximized when you report your true probabilities. 

## 10.1.3 Markov, Chebyshev, Chernoff: bounds on tail probabilities

The inequalities in this section provide bounds on the probability of an r.v. taking on an “extreme” value in the right or left tail of a distribution.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Joe’s philosophy professor as an undergraduate at Caltech, Alan Hájek, used precisely this system. He warned the class never to put a probability of zero, since a score of −∞ would not only give a −∞ on that exam, but also it would spill through and result in a −∞ for the whole semester, since a weighted average with even a tiny positive weight on a −∞ yields −∞. Despite this warning, some students did put probability zero on the correct answers.</span></small>

Theorem 10.1.10 (Markov). For any r.v. X and constant $a > 0$

$$
P (| X | \geq a) \leq \frac {E | X |}{a}.
$$

Proof. Let $\begin{array} { r } { Y = { \frac { | X | } { a } } } \end{array}$ . We need to show that $P(Y \geq 1) \leq E(Y)$ . Note that

$$
I (Y \geq 1) \leq Y,
$$

since if $I ( Y \geq 1 ) = 0$ then the inequality reduces to $Y \geq 0$ , and if $I ( Y \geq 1 ) = 1$ then $Y \geq 1$ (because the indicator says so). Taking the expectation of both sides, we have Markov’s inequality. 

For an intuitive interpretation, let X be the income of a randomly selected individual from a population. Taking $a \; = \; 2 E ( X )$ , Markov’s inequality says that $P ( X \: \geq \: 2 E ( X ) ) \: \leq \: 1 / 2 ,$ i.e., it is impossible for more than half the population to make at least twice the average income. This is clearly true, since if over half the population were earning at least twice the average income, the average income would be higher! Similarly, $P ( X \geq 3 E ( X ) ) \leq 1 / 3 ;$ you can’t have more than $1 / 3$ of the population making at least three times the average income, since those people would already drive the average above what it is.

Markov’s inequality is a very crude bound because it requires absolutely no assumptions about $X$ . The right-hand side of the inequality could be greater than 1, or even infinite; this is not very helpful when trying to bound a number that we already know to be between 0 and 1. Surprisingly, the following two inequalities, which can be derived from Markov’s inequality with almost no additional work, can often give us bounds that are much better than Markov’s.

Theorem 10.1.11 (Chebyshev). Let X have mean $\mu$ and variance $\sigma ^ { 2 }$ . Then for any $a > 0$ ,

$$
P (| X - \mu | \geq a) \leq \frac {\sigma^ {2}}{a ^ {2}}.
$$

Proof. By Markov’s inequality,

$$
P (| X - \mu | \geq a) = P ((X - \mu) ^ {2} \geq a ^ {2}) \leq \frac {E (X - \mu) ^ {2}}{a ^ {2}} = \frac {\sigma^ {2}}{a ^ {2}}.
$$

Substituting cσ for a, for $c > 0$ , we have the following equivalent form of Chebyshev’s inequality:

$$
P (| X - \mu | \geq c \sigma) \leq \frac {1}{c ^ {2}}.
$$

This gives us an upper bound on the probability of an r.v. being more than c standard deviations away from its mean, e.g., there can’t be more than a 25% chance of being 2 or more standard deviations from the mean.

The idea for proving Chebyshev from Markov was to square $| X - \mu |$ and then apply Markov. Similarly, it is often fruitful to perform other transformations before applying Markov. Chernoff ’s bound, which is widely used in engineering, uses this idea with an exponential function.

Theorem 10.1.12 (Chernoff). For any r.v. X and constants $a > 0$ and $t > 0$ ,

$$
P (X \geq a) \leq \frac {E (e ^ {t X})}{e ^ {t a}}.
$$

Proof. The transformation g with $g ( x )   =   e ^ { t x }$ is invertible and strictly increasing. So by Markov’s inequality, we have

$$
P (X \geq a) = P (e ^ {t X} \geq e ^ {t a}) \leq \frac {E (e ^ {t X})}{e ^ {t a}}.
$$

At first it may not be clear what Chernoff’s bound has to offer that Markov’s inequality doesn’t, but it has two very nice features:

1. The right-hand side can be optimized over t to give the tightest upper bound, as in the proof of Cauchy-Schwarz.
2. If the MGF of X exists, then the numerator in the bound is the MGF, and some of the useful properties of MGFs can come into play.

Let’s now compare the three bounds just discussed by applying them to a simple example where the true probability is known.

Example 10.1.13 (Bounds on a Normal tail probability). Let $Z \sim \mathcal { N } ( 0 , 1 )$ . By the 68-95-99.7% rule, we know that $P ( | Z | > 3 )$ is approximately 0.003; the exact value is $2 \cdot \Phi ( - 3 )$ . Let’s see what upper bounds are obtained from Markov’s, Chebyshev’s, and Chernoff’s inequalities.

• Markov: In Chapter 5, we found that $E | Z | = { \sqrt { 2 / \pi } }$ . Then

$$
P (| Z | > 3) \leq \frac {E | Z |}{3} = \frac {1}{3} \cdot \sqrt {\frac {2}{\pi}} \approx 0. 2 7.
$$

• Chebyshev:

$$
P (| Z | > 3) \leq \frac {1}{9} \approx 0. 1 1.
$$

• Chernoff (after using symmetry of the Normal):

$$
P (| Z | > 3) = 2 P (Z > 3) \leq 2 e ^ {- 3 t} E (e ^ {t Z}) = 2 e ^ {- 3 t} \cdot e ^ {t ^ {2} / 2},
$$

using the MGF of the standard Normal distribution.

The right-hand side is minimized at $t = 3$ , as found by setting the derivative equal to 0, possibly after taking the log first (which is a good idea since it doesn’t affect where the minimum occurs and it means we just have to minimize a quadratic polynomial). Plugging in $t = 3$ , we have

$$
P (| Z | > 3) \leq 2 e ^ {- 9 / 2} \approx 0. 0 2 2.
$$

All of these upper bounds are correct, but Chernoff’s bound is the best by far. This example also illustrates the distinction between a bound and an approximation, as we explained in the introduction to this chapter. Markov’s inequality tells us that the tail probability $P ( | Z | > 3 )$ is at most 0.27, but it would be a blunder to say that $P ( | Z | > 3 )$ is approximately $0.27  \text{— }  we  \text{°d }$ be off by a factor of about 100. 

## 10.2 Law of large numbers

We turn next to two theorems, the law of large numbers and the central limit theorem, which describe the behavior of the sample mean of i.i.d. r.v.s as the sample size grows. Throughout this section and the next, assume we have i.i.d. $X _ { 1 } , X _ { 2 } , X _ { 3 } , \ldots$ with finite mean $\mu$ and finite variance $\sigma ^ { 2 }$ . For all positive integers n, let

$$
\bar {X} _ {n} = \frac {X _ {1} + \cdots + X _ {n}}{n}
$$

be the sample mean of $X _ { 1 }$ through $X _ { n }$ . The sample mean is itself an $\mathbf { r } . \mathbf { V } .$ , with mean $\mu$ and variance $\sigma ^ { 2 } / n { \mathrm { : } }$

$$
E (\bar {X} _ {n}) = \frac {1}{n} E (X _ {1} + \dots + X _ {n}) = \frac {1}{n} (E (X _ {1}) + \dots + E (X _ {n})) = \mu ,
$$

$$
\mathrm{Var} (\bar {X} _ {n}) = \frac {1}{n ^ {2}} \mathrm{Var} (X _ {1} + \dots + X _ {n}) = \frac {1}{n ^ {2}} (\mathrm{Var} (X _ {1}) + \dots + \mathrm{Var} (X _ {n})) = \frac {\sigma^ {2}}{n}.
$$

The law of large numbers (LLN) says that as n grows, the sample mean ${ \bar { X } } _ { n }$ converges to the true mean $\mu$ (in a sense that is explained below). The LLN comes in two versions, “strong” (SLLN) and “weak” (WLLN), which use slightly different definitions of what it means for a sequence of r.v.s to converge to a number. We will state both versions, and prove the second using Chebyshev’s inequality.

Theorem 10.2.1 (Strong law of large numbers). The sample mean ${ \bar { X } } _ { n }$ converges to the true mean $\mu$ pointwise, with probability 1. Recalling that r.v.s are functions from the sample space S to R, this form of convergence says that $\bar { X } _ { n } ( s ) \to \mu$ for each point $s \in S$ , except that the convergence is allowed to fail on some set $B _ { 0 }$ of exceptions, as long as $P ( B _ { 0 } ) = 0$ . In short, $P ( \bar { X } _ { n } \rightarrow \mu ) = 1$

Theorem 10.2.2 (Weak law of large numbers). For all $\epsilon > 0 ,   P ( | \bar { X } _ { n } - \mu | > \epsilon ) \rightarrow 0$ as $n \to \infty$ . (This form of convergence is called convergence in probability.)

Proof. Fix $\epsilon > 0$ . By Chebyshev’s inequality,

$$
P (| \bar {X} _ {n} - \mu | > \epsilon) \leq \frac {\sigma^ {2}}{n \epsilon^ {2}}.
$$

As $n \to \infty$ , the right-hand side goes to 0, and so must the left-hand side.

The law of large numbers is essential for simulations, statistics, and science. Consider generating “data” from a large number of independent replications of an experiment, performed either by computer simulation or in the real world. Every time we use the average value in the replications of some quantity to approximate its theoretical average, we are implicitly appealing to the LLN.

Example 10.2.3 (Running proportion of Heads). Let $X _ { 1 } , X _ { 2 } , \ldots$ be i.i.d. Bern(1/2). Interpreting the $X _ { j }$ as indicators of Heads in a string of fair coin tosses, ${ \bar { X } } _ { n }$ is the proportion of Heads after n tosses. The SLLN says that with probability 1, when the sequence of r.v.s $\bar { X } _ { 1 } , \bar { X } _ { 2 } , \bar { X } _ { 3 } , \ldots$ . crystallizes into a sequence of numbers, the sequence of numbers will converge to 1/2. Mathematically, there are bizarre outcomes such as HHHHHH . . . and HHTHHTHHTHHT. . . , but collectively they have zero probability of occurring. The WLLN says that for any $\epsilon > 0$ , the probability of ${ \bar { X } } _ { n }$ being more than  away from $1 / 2$ can be made as small as we like by letting n grow.

As an illustration, we simulated six sequences of fair coin tosses and, for each sequence, computed ${ \bar { X } } _ { n }$ as a function of n. Of course, in real life we cannot simulate infinitely many coin tosses, so we stopped after 300 tosses. Figure 10.2 plots ${ \bar { X } } _ { n }$ as a function of n for each sequence.

![](images/page_484_chart_8.jpg)

<details>
<summary>line</summary>

| number of tosses | Running proportion of Heads (Series 1) | Running proportion of Heads (Series 2) | Running proportion of Heads (Series 3) | Running proportion of Heads (Series 4) | Running proportion of Heads (Series 5) | Running proportion of Heads (Series 6) | Running proportion of Heads (Series 7) | Running proportion of Heads (Series 8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ~0.0 | ~0.0 | ~0.0 | ~0.0 | ~0.0 | ~0.0 | ~0.0 | ~0.0 |
| 50 | ~0.55 | ~0.52 | ~0.48 | ~0.45 | ~0.42 | ~0.40 | ~0.38 | ~0.35 |
| 100 | ~0.52 | ~0.50 | ~0.48 | ~0.46 | ~0.44 | ~0.42 | ~0.40 | ~0.38 |
| 150 | ~0.51 | ~0.49 | ~0.47 | ~0.45 | ~0.43 | ~0.41 | ~0.40 | ~0.38 |
| 200 | ~0.51 | ~0.49 | ~0.47 | ~0.45 | ~0.43 | ~0.41 | ~0.40 | ~0.38 |
| 250 | ~0.51 | ~0.49 | ~0.47 | ~0.45 | ~0.43 | ~0.41 | ~0.40 | ~0.38 |
| 300 | ~0.51 | ~0.49 | ~0.47 | ~0.45 | ~0.43 | ~0.41 | ~0.40 | ~0.38 |
</details>

FIGURE 10.2

Running proportion of Heads in 6 sequences of fair coin tosses. Dashed lines at 0.6 and 0.4 are plotted for reference. As the number of tosses increases, the proportion of Heads approaches $1 / 2 .$

At the beginning, we can see that there is quite a bit of fluctuation in the running proportion of Heads. As the number of coin tosses increases, however, $\operatorname { V a r } ( { \bar { X } } _ { n } )$ gets smaller and smaller, and ${ \bar { X } } _ { n }$ approaches $1 / 2$ 

h 10.2.4 (LLN does not contradict the fact that a coin is memoryless). In the above example, the law of large numbers states that the proportion of Heads converges to $1 / 2$ , but this does not imply that after a long string of Heads, the coin is “due” for a Tails to balance things out. Rather, the convergence takes place through swamping: past tosses are swamped by the infinitely many tosses that are yet to come.

A sequence of i.i.d. Bernoullis is the simplest possible example of the LLN, but this simple case forms the basis for extremely useful methods in statistics, as the following examples illustrate.

Example 10.2.5 (Monte Carlo integration). Let f be a complicated function whose integral $\begin{array} { r } { \int _ { a } ^ { b } f ( x ) d x } \end{array}$ we want to approximate. Assume that $0 \leq f ( x ) \leq c { \mathrm { ~ s o ~ } }$ that we know the integral is finite. On the surface, this problem doesn’t involve probability, as $\textstyle \int _ { a } ^ { b } f ( x ) d x$ is just a number. But where there is no randomness, we can create our own! The technique of Monte Carlo integration uses random samples to obtain approximations of definite integrals when exact integration methods are unavailable.

Let A be the rectangle in the $( x , y )$ -plane given by $a \leq x \leq b$ and $0 \leq y \leq c$ Let B be the region under the curve $y = f(x)$ (and above the x-axis) for $a \leq x \leq b$ so the desired integral is the area of region B. Our strategy will be to take random samples from A, then calculate the proportion of the samples that also fall into the area B. This is depicted in Figure 10.3: points in B are in black, and points not in B are in white.

![](images/page_485_chart_7.jpg)

<details>
<summary>scatter</summary>

| Series | X (range) | Y (range) |
| --- | --- | --- |
| Open Circles | a~b | ~0.2 ~1.0 |
| Filled Circles | a~b | ~0.05 ~0.8 |
</details>

FIGURE 10.3

Monte Carlo integration. To approximate the area under $f ( x )$ from $x = a$ to $x = b .$ generate random points in the rectangle $[ a , b ] \times [ 0 , c ]$ , and approximate the area under $f ( x )$ by the proportion of points falling underneath the curve, multiplied by the total area of the rectangle.

To see why this works, suppose we pick i.i.d. points $( X _ { 1 } , Y _ { 1 } ) , ( X _ { 2 } , Y _ { 2 } ) , \ldots , ( X _ { n } , Y _ { n } )$ uniformly in the rectangle $A$ . Define indicator r.v.s $I _ { 1 } , \ldots , I _ { n }$ by letting $I _ { j }   =   1$ if $( X _ { j } , Y _ { j } )$ is in $B$ and $I _ { j } = 0$ otherwise. Then the $I _ { j }$ are Bernoulli r.v.s whose success probability is precisely the ratio of the area of $B$ to the area of A. Letting $p = E ( I _ { j } )$ ,

$$
p = E (I _ {j}) = P (I _ {j} = 1) = \frac {\int_ {a} ^ {b} f (x) d x}{c (b - a)}.
$$

We can estimate $p$ using ${ \textstyle { \frac { 1 } { n } } \sum _ { j = 1 } ^ { n } I _ { j } }$ , and then estimate the desired integral by

$$
\int_ {a} ^ {b} f (x) d x \approx c (b - a) \frac {1}{n} \sum_ {j = 1} ^ {n} I _ {j}.
$$

Since the $I _ { j }$ are i.i.d. with mean $p ,$ it follows from the law of large numbers that with probability 1, the estimate converges to the true value of the integral as the number of points approaches infinity. 

Example 10.2.6 (Convergence of empirical CDF). Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d. random variables with CDF $F .$ For every number $x ,$ let $R _ { n } ( x )$ count how many of $X _ { 1 } , \ldots , X _ { n }$ are less than or equal to $x ;$ that is,

$$
R _ {n} (x) = \sum_ {j = 1} ^ {n} I (X _ {j} \leq x).
$$

Since the indicators $I ( X _ { j } \leq x )$ are i.i.d. with probability of success $F ( x )$ , we know $R _ { n } ( x )$ is Binomial with parameters n and $F ( x )$

The empirical CDF of $X _ { 1 } , \ldots , X _ { n }$ is defined as

$$
\hat {F} _ {n} (x) = \frac {R _ {n} (x)}{n},
$$

considered as a function of $x .$ Before we observe $X _ { 1 } , \ldots , X _ { n } , \; \hat { F } _ { n } ( x )$ is a random variable for each $x .$ . After we observe $X _ { 1 } , \ldots , X _ { n } , \thinspace \hat { F } _ { n } ( x )$ crystallizes into a particular value at each $x ,$ so $\hat { F } _ { n }$ crystallizes into a particular CDF, which can be used to estimate the true CDF F if the latter is unknown.

For example, suppose $n = 4$ and we observe $X _ { 1 } = x _ { 1 } , X _ { 2 } = x _ { 2 } , X _ { 3 } = x _ { 3 } , X _ { 4 } = x _ { 4 }$ Then the graph of $\frac { R _ { 4 } ( x ) } { 4 }$ starts at 0 and then jumps by $1 / 4$ every time one of the $x _ { j } { } ^ { \prime } \mathrm { s }$ is reached. In other words, $\frac { R _ { 4 } ( x ) } { 4 }$ is the CDF of a discrete random variable taking on values $x _ { 1 } , \ldots , x _ { 4 }$ , each with probability $1 / 4$ . This is illustrated in Figure 10.4.

Now we can ask, what happens to $\hat { F } _ { n }$ as $n \rightarrow \infty ?$ This is a natural question if we are using $\hat { F } _ { n }$ as an estimate of the true $F ;$ does the approximation fare well in the limit? The law of large numbers provides the answer: for every $x ,   R _ { n } ( x )$ is the sum of n i.i.d. Bern(p) r.v.s, where $p   =   F ( x )$ . So by the SLLN, ${ \hat { F } } _ { n } ( x )   \to   F ( x )$ with probability 1 as $n \to \infty$

![](images/page_487_chart_2.jpg)

<details>
<summary>scatter</summary>

| X | Value |
| --- | --- |
| 0 | 0 |
| 0 | 1 |
| 1 | 1 |
| 1 | 2 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
</details>

## FIGURE 10.4

Empirical CDF after observing $X _ { 1 } { = } x _ { 1 } , X _ { 2 } { = } x _ { 2 } , X _ { 3 } { = } x _ { 3 } , X _ { 4 } { = } x _ { 4 }$ . The graph jumps by $1 / 4$ every time one of the $x _ { j } { } ^ { \prime } \mathrm { s }$ is reached.

The empirical CDF is commonly used in nonparametric statistics, a branch of statistics that tries to understand a random sample without making strong assumptions about the family of distributions from which it originated. For example, instead of assuming $X _ { 1 } , \ldots , X _ { n } \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ , a nonparametric method would allow $X _ { 1 } , \ldots , X _ { n } \sim F$ for an arbitrary CDF $F .$ , then use the empirical CDF as an approximation for $F$ . The law of large numbers is what assures us that this approximation is valid in the limit as we collect more and more samples: at every value of $x ,$ the empirical CDF converges to the true CDF. 

## 10.3 Central limit theorem

As in the previous section, let $X _ { 1 } , X _ { 2 } , X _ { 3 } , \ldots$ be i.i.d. with mean $\mu$ and variance $\sigma ^ { 2 }$ . The law of large numbers says that as $n \to \infty ,   \bar { X } _ { n }$ converges to the constant $\mu$ (with probability 1). But what is its distribution along the way to becoming a constant? This is addressed by the central limit theorem (CLT), which, as its name suggests, is a limit theorem of central importance in statistics.

The CLT states that for large $n ,$ the distribution of $X _ { n }$ after standardization approaches a standard Normal distribution. By standardization, we mean that we subtract $\mu ,$ the mean of ${ \bar { X } } _ { n }$ , and divide by $\sigma / \sqrt { n }$ , the standard deviation of ${ \bar { X } } _ { n }$

Theorem 10.3.1 (Central limit theorem). As $n \to \infty$

$$
\sqrt {n} \left(\frac {\bar {X} _ {n} - \mu}{\sigma}\right) \to \mathcal {N} (0, 1) \text {in distribution.}
$$

In words, this means that the CDF of the left-hand side converges to $\Phi ,$ the CDF of the standard Normal distribution.

Proof. We will prove the CLT assuming that the MGF of the $X _ { j }$ exists, though the theorem holds much more generally. Let $M ( t ) = E ( e ^ { t X _ { j } } )$ , and without loss of generality let $\mu = 0 ,   \sigma ^ { 2 } = 1$ (since we end up standardizing ${ \bar { X } } _ { n }$ for the theorem, we might as well standardize the $X _ { j }$ in the first place). Then $M(0) = 1,   M'(0) = \mu = 0$ and $M ^ { \prime \prime } ( 0 ) = \sigma ^ { 2 } = 1$

We wish to show that the MGF of $\sqrt { n } \bar { X } _ { n } = ( X _ { 1 } + \cdots + X _ { n } ) / \sqrt { n }$ converges to the MGF of the $\mathcal { N } ( 0 , 1 )$ distribution, which is $e ^ { t ^ { 2 } / 2 }$ . This is a valid strategy because of a theorem that says that if $Z _ { 1 } , Z _ { 2 } , \ldots$ . are r.v.s whose MGFs converge to the MGF of a continuous r.v. $Z ,$ then the CDF of $Z _ { n }$ converges to the CDF of $Z .$ (We omit the proof of this result since it requires some difficult analysis. But it should at least seem plausible, in view of the fact that the MGF of an r.v. determines its distribution.)

By properties of MGFs,

$$
\begin{array}{l} E (e ^ {t (X _ {1} + \dots + X _ {n}) / \sqrt {n}}) = E (e ^ {t X _ {1} / \sqrt {n}}) E (e ^ {t X _ {2} / \sqrt {n}}) \dots E (e ^ {t X _ {n} / \sqrt {n}}) \\ = \left(M \left(\frac {t}{\sqrt {n}}\right)\right) ^ {n}. \\ \end{array}
$$

Letting $n \to \infty$ , we get the indeterminate form $1 ^ { \infty }$ , so instead we should take the limit of the logarithm, n log $\textstyle M ( { \frac { t } { \sqrt { n } } } )$ , and then exponentiate at the end. This gives

$$
\begin{array}{l} \lim _ {n \to \infty} n \log M \left(\frac {t}{\sqrt {n}}\right) = \lim _ {y \to 0} \frac {\log M (y t)}{y ^ {2}} \quad \text {where} y = 1 / \sqrt {n} \\ = \lim _ {y \rightarrow 0} \frac {t M ^ {\prime} (y t)}{2 y M (y t)} \quad \text {by L'Hôpital's rule} \\ = \frac {t}{2} \lim _ {y \to 0} \frac {M ^ {\prime} (y t)}{y} \quad \text {since} M (y t) \to 1 \\ = \frac {t ^ {2}}{2} \lim _ {y \rightarrow 0} M ^ {\prime \prime} (y t) \quad \text {by L'Hôpital's rule} \\ = \frac {t ^ {2}}{2}. \\ \end{array}
$$

Therefore $\textstyle { \left( M ( { \frac { t } { \sqrt { n } } } ) \right) ^ { n } }$ , the MGF of ${ \sqrt { n } } { \bar { X } } _ { n }$ , approaches $e ^ { t ^ { 2 } / 2 }$ , the $\mathcal { N } ( 0 , 1 )$ MGF.

The CLT is an asymptotic result, telling us about the limiting distribution of ${ \bar { X } } _ { n }$ as $n \to \infty$ , but it also suggests an approximation for the distribution of ${ \bar { X } } _ { n }$ when n is large but finite.

Approximation 10.3.2 (Central limit theorem, approximation form). For large $n ,$ the distribution of ${ \bar { X } } _ { n }$ is approximately $\mathcal { N } ( \mu , \sigma ^ { 2 } / n )$

Proof. Change the arrow in the CLT to $\dot { \sim } ,$ an approximate distribution sign:

$$
\sqrt {n} \left(\frac {\bar {X} _ {n} - \mu}{\sigma}\right) \dot {\sim} \mathcal {N} (0, 1).
$$

Then by a location-scale transformation,

$$
\bar {X} _ {n} \dot {\sim} \mathcal {N} (\mu , \sigma^ {2} / n).
$$

Of course, we already knew from properties of expectation and variance that ${ \bar { X } } _ { n }$ has mean $\mu$ and variance $\sigma ^ { 2 } / n ;$ the central limit theorem gives us the additional information that ${ \bar { X } } _ { n }$ is approximately Normal with said mean and variance.

Let’s take a moment to admire the generality of this result. The distribution of the individual $X _ { j }$ can be anything in the world, as long as the mean and variance are finite. We could have a discrete distribution like the Binomial, a bounded distribution like the Beta, a skewed distribution like the Log-Normal, or a distribution with multiple peaks and valleys. No matter what, the act of averaging will cause Normality to emerge. In Figure 10.5 we show histograms of the distribution of ${ \bar { X } } _ { n }$ for 4 different starting distributions and for $n = 1 , 5 , 3 0 , 1 0 0$ . As n increases, the distribution of ${ \bar { X } } _ { n }$ starts to look Normal, regardless of the distribution of the $X _ { j }$

This does not mean that the distribution of the $X _ { j }$ is irrelevant, however. If the $X _ { j }$ have a highly skewed or multimodal distribution, we may need $n$ to be very large before the Normal approximation becomes accurate; at the other extreme, if the $X _ { j }$ are already i.i.d. Normals, the distribution of ${ \bar { X } } _ { n }$ is exactly $\mathcal { N } ( \mu , \sigma ^ { 2 } / n )$ for all n. Since there are no infinite datasets in the real world, the quality of the Normal approximation for finite n is an important consideration.

Example 10.3.3 (Running proportion of Heads, revisited). As in Example 10.2.3, let $X _ { 1 } , X _ { 2 } , \ldots$ . be i.i.d. $\mathrm { B e r n } ( 1 / 2 )$ . Before, we used the law of large numbers to conclude that $\bar { X } _ { n } \rightarrow 1 / 2$ as $n \to \infty$ . Now, using the central limit theorem, we can say more: $E ( \bar { X } _ { n } ) = 1 / 2$ and $\operatorname { V a r } ( { \bar { X } } _ { n } ) = 1 / ( 4 n )$ , so for large $n ,$

$$
\bar {X} _ {n} \dot {\sim} \mathcal {N} \left(\frac {1}{2}, \frac {1}{4 n}\right).
$$

This additional information allows us to quantify what kind of deviation from the mean is typical for a given n. For example, when $n = 1 0 0 ,   \mathrm { S D } ( \bar { X } _ { n } ) = 1 / 2 0 = 0 . 0 5$ so if the Normal approximation is valid, then by the 68-95-99.7% rule there’s a 95% chance that ${ \bar { X } } _ { n }$ will be in the interval [0.40, 0.60]. 

The CLT says that the sample mean ${ \bar { X } } _ { n }$ is approximately Normal, but since the sum $W _ { n } = X _ { 1 }   +   \cdots   +   X _ { n } = n \bar { X } _ { n }$ is just a scaled version of ${ \bar { X } } _ { n }$ , the CLT also implies $W _ { n }$ is approximately Normal. If the $X _ { j }$ have mean $\mu$ and variance $\sigma ^ { 2 } ,   W _ { n }$ has mean $n \mu$ and variance $n \sigma ^ { 2 }$ . The CLT then states that for large $n .$

$$
W _ {n} \dot {\sim} \mathcal {N} (n \mu , n \sigma^ {2}).
$$

![](images/page_490_chart_2.jpg)

<details>
<summary>histogram</summary>

| Method | n | Bin(10, 0.9) Range | n=1 Frequency | n=5 Frequency | n=30 Frequency | n=100 Frequency |
| --- | --- | --- | --- | --- | --- | --- |
| Bin(10, 0.9) | 1 | ~5.0 ~10.0 | N/A | N/A | N/A | N/A |
| Pois(2) | 2 | ~0.0 ~8.5 | N/A | N/A | N/A | N/A |
| Expo(1) | 1 | ~0.0 ~10.0 | N/A | N/A | N/A | N/A |
| Beta(0.8, 0.8) | 0.8 | ~0.0 ~9.5 | N/A | N/A | N/A | N/A |
</details>

FIGURE 10.5

Central limit theorem. Histograms of the distribution of ${ \bar { X } } _ { n }$ for different starting distributions of the $X _ { j }$ (indicated by the rows) and increasing values of $n$ (indicated by the columns). Each histogram is based on 10,000 simulated values of ${ \bar { X } } _ { n }$ . Regardless of the starting distribution of the $X _ { j }$ , the distribution of ${ \bar { X } } _ { n }$ approaches a Normal distribution as n grows.

This is completely equivalent to the approximation for ${ \bar { X } } _ { n }$ , but it can be useful to write it in this form because many of the named distributions we have studied can be considered as a sum of i.i.d. r.v.s. Here are three quick examples.

Example 10.3.4 (Poisson convergence to Normal). Let $Y \sim \mathrm { P o i s } ( n )$ . By Theorem 4.8.1, we can consider Y to be a sum of n i.i.d. Pois(1) r.v.s. Therefore, for large n,

$$
Y \dot {\sim} \mathcal {N} (n, n).
$$

Example 10.3.5 (Gamma convergence to Normal). Let $Y   \sim   \mathrm { G a m m a } ( n , \lambda )$ . By Theorem 8.4.3, we can consider Y to be a sum of n i.i.d. Expo(λ) r.v.s. Therefore, for large n,

$$
Y \dot {\sim} \mathcal {N} \left(\frac {n}{\lambda}, \frac {n}{\lambda^ {2}}\right).
$$

Example 10.3.6 (Binomial convergence to Normal). Let $Y \sim \mathrm { B i n } ( n , p )$ . By Theorem 3.8.8, we can consider $Y$ to be a sum of n i.i.d. Bern(p) r.v.s. Therefore, for large $n ,$

$$
Y \dot {\sim} \mathcal {N} (n p, n p (1 - p)).
$$

This is probably the most widely used Normal approximation in statistics. To account for the discreteness of $Y$ , we write the probability $P ( Y = k )$ (which would be exactly 0 under the Normal approximation) as $P(k - 1/2 < Y < k + 1/2)$ (so that it becomes an interval of non-zero width) and apply the Normal approximation to the latter. This is known as the continuity correction, and it yields the following approximation for the PMF of $Y ;$

$$
P (Y = k) = P (k - 1 / 2 <   Y <   k + 1 / 2) \approx \Phi \left(\frac {k + 1 / 2 - n p}{\sqrt {n p (1 - p)}}\right) - \Phi \left(\frac {k - 1 / 2 - n p}{\sqrt {n p (1 - p)}}\right).
$$

The Normal approximation to the Binomial distribution is complementary to the Poisson approximation discussed in Chapter 4. The Poisson approximation works best when $p$ is small, while the Normal approximation works best when $n$ is large and $p$ is around $1 / 2 ,$ , so that the distribution of $Y$ is symmetric or nearly so.

We’ll conclude with an example that uses both the LLN and the CLT.

Example 10.3.7 (Volatile stock). Each day, a very volatile stock rises $7 0 \%$ or drops 50% in price, with equal probabilities and with different days independent. Let $Y _ { n }$ be the stock price after n days, starting from an initial value of $Y _ { 0 } = 1 0 0$

(a) Explain why log $Y _ { n }$ is approximately Normal for n large, and state its parameters.
(b) What happens to $E ( Y _ { n } )$ as $n \rightarrow \infty ?$
(c) Use the law of large numbers to find out what happens to $Y _ { n }$ as $n \to \infty$

Solution:

(a) We can write $Y _ { n } = Y _ { 0 } ( 0 . 5 ) ^ { n - U _ { n } } ( 1 . 7 ) ^ { U _ { n } }$ where $U _ { n } \sim \operatorname { B i n } ( n , { \textstyle { \frac { 1 } { 2 } } } )$ is the number of times the stock rises in the first n days. This gives

$$
\log Y _ {n} = \log Y _ {0} - n \log 2 + U _ {n} \log 3. 4,
$$

which is a location-scale transformation of $U _ { n }$ . By the CLT, $U _ { n }$ is approximately $\mathcal { N } ( \textstyle { \frac { n } { 2 } } , \textstyle { \frac { n } { 4 } } )$ for large n, so log $Y _ { n }$ is approximately Normal with mean

$$
E (\log Y _ {n}) = \log 1 0 0 - n \log 2 + (\log 3. 4) \cdot E (U _ {n}) \approx \log 1 0 0 - 0. 0 8 1 n
$$

and variance

$$
\mathrm{Var} (\log Y _ {n}) = (\log 3. 4) ^ {2} \cdot \mathrm{Var} (U _ {n}) \approx 0. 3 7 4 n.
$$

(b) We have $E(Y_{1}) = (170 + 50)/2 = 110$ . Similarly,

$$
E (Y _ {n + 1} | Y _ {n}) = \frac {1}{2} (1. 7 Y _ {n}) + \frac {1}{2} (0. 5 Y _ {n}) = 1. 1 Y _ {n},
$$

so

$$
E (Y _ {n + 1}) = E (E (Y _ {n + 1} | Y _ {n})) = 1. 1 E (Y _ {n}).
$$

Thus $E(Y_{n}) = 1.1^{n}E(Y_{0}) = 100 \cdot 1.1^{n}$ , which goes to $\infty$ as $n \to \infty$

(c) As in (a), let $U _ { n } \sim \operatorname { B i n } ( n , { \textstyle { \frac { 1 } { 2 } } } )$ be the number of times the stock rises in the first n days. Note that even though $E ( Y _ { n } ) \to \infty$ , if the stock goes up 70% one day and then drops 50% the next day, then overall it has dropped 15% since $1 . 7 \cdot 0 . 5 = 0 . 8 5$ So after many days, $Y _ { n }$ will be very small if about half the time the stock rose 70% and about half the time the stock dropped 50%—and the law of large numbers ensures that this will be the case! Writing $Y _ { n }$ in terms of $U _ { n } / n$ in order to apply the LLN, we have

$$
Y _ {n} = Y _ {0} (0. 5) ^ {n - U _ {n}} (1. 7) ^ {U _ {n}} = Y _ {0} \left(\frac {(3 . 4) ^ {U _ {n} / n}}{2}\right) ^ {n}.
$$

Since $U _ { n } / n \to 0 . 5$ with probability 1, $( 3 . 4 ) ^ { U _ { n } / n } \rightarrow \sqrt { 3 . 4 } < 2$ with probability 1, so $Y _ { n } \to 0$ with probability 1.

Paradoxically, $E ( Y _ { n } ) \to \infty$ but $Y _ { n } \to 0$ with probability 1. To gain some intuition for this result, consider the extreme example where a gambler starts with \$100 and each day either quadruples their money or loses their entire fortune, with equal probabilities. Then on average the gambler’s wealth doubles each day, which sounds good until one notices that eventually there will be a day when the gambler goes broke. The gambler’s actual fortune goes to 0 with probability 1, whereas the expected value goes to infinity due to tiny probabilities of getting extremely large amounts of money, as in the St. Petersburg paradox. 

h 10.3.8 (The evil Cauchy). The central limit theorem requires that the mean and variance of the $X _ { j }$ be finite, and our proof of the WLLN relied on the same conditions. The Cauchy distribution introduced in Example 7.1.25 has no mean or variance, so the Cauchy distribution obeys neither the law of large numbers nor the central limit theorem. It can be shown that the sample mean of $n$ Cauchys is still Cauchy, no matter how large n gets. So the sample mean never approaches a Normal distribution, contrary to the behavior seen in the CLT. There is also no true mean for ${ \bar { X } } _ { n }$ to converge to, so the LLN does not apply either.

## 10.4 Chi-Square and Student-t

We’ll round out the chapter by introducing the last two continuous distributions in this book, both of which are closely related to the Normal distribution.

Definition 10.4.1 (Chi-Square distribution). Let $V = Z _ { 1 } ^ { 2 }   +   \cdots   +   Z _ { n } ^ { 2 }$ where $Z _ { 1 } , Z _ { 2 } , \ldots , Z _ { n }$ are i.i.d. $\mathcal { N } ( 0 , 1 )$ . Then V is said to have the Chi-Square distribution with n degrees of freedom. We write this as $V \sim \chi _ { n } ^ { 2 }$

$\mathrm { A s }$ it turns out, the $\chi _ { n } ^ { 2 }$ distribution is a special case of the Gamma.

Theorem 10.4.2. The $\chi _ { n } ^ { 2 }$ distribution is the Gamma $( \frac { n } { 2 } , \frac { 1 } { 2 } )$ distribution.

Proof. First, we verify that the PDF of $Z _ { 1 } ^ { 2 } \sim \chi _ { 1 } ^ { 2 }$ equals the PDF of the Gamma $( \frac { 1 } { 2 } , \frac { 1 } { 2 } )$ : for $x > 0$ ,

$$
F (x) = P (Z _ {1} ^ {2} \leq x) = P (- \sqrt {x} \leq Z _ {1} \leq \sqrt {x}) = \Phi (\sqrt {x}) - \Phi (- \sqrt {x}) = 2 \Phi (\sqrt {x}) - 1,
$$

so

$$
f (x) = \frac {d}{d x} F (x) = 2 \varphi (\sqrt {x}) \frac {1}{2} x ^ {- 1 / 2} = \frac {1}{\sqrt {2 \pi x}} e ^ {- x / 2},
$$

which is indeed the Gamma $( \frac { 1 } { 2 } , \frac { 1 } { 2 } )$ PDF. Then, because $V = Z _ { 1 } ^ { 2 } + \cdots + Z _ { n } ^ { 2 } \sim \chi _ { n } ^ { 2 }$ is the sum of n independent $$\mathrm { \overset { \cdot } { G a m m a } } ( \frac { 1 } { 2 } , \frac { 1 } { 2 } )$ r.v.s$ , we have $\textstyle V \sim \operatorname { G a m m a } ( { \frac { n } { 2 } } , { \frac { 1 } { 2 } } )$ 

From our knowledge of the mean and variance of a Gamma distribution, we have $E ( V ) = n$ and $\operatorname { V a r } ( V ) = 2 n$ . We can also obtain the mean and variance using the fact that V is the sum of i.i.d. squared Normals, along with the Normal moments derived in Chapter 6:

$$
E (V) = n E (Z _ {1} ^ {2}) = n,
$$

$$
\mathrm{Var} (V) = n \mathrm{Var} (Z _ {1} ^ {2}) = n \left(E (Z _ {1} ^ {4}) - (E Z _ {1} ^ {2}) ^ {2}\right) = n (3 - 1) = 2 n.
$$

To get the MGF of the Chi-Square distribution, just plug $n / 2$ and $1 / 2$ into the more general Gamma $( a , \lambda )$ MGF, which we found in Theorem 8.4.3 to be $\left( { \frac { \lambda } { \lambda { - } t } } \right) ^ { a }$ for $t < \lambda$ . This gives

$$
M _ {V} (t) = \left(\frac {1}{1 - 2 t}\right) ^ {n / 2}, \quad t <   1 / 2.
$$

The Chi-Square distribution is important in statistics because it is related to the distribution of the sample variance, which can be used to estimate the true variance of a distribution. When our random variables are i.i.d. Normals, the distribution of the sample variance after appropriate scaling is Chi-Square.

Example 10.4.3 (Distribution of sample variance). For i.i.d. $X _ { 1 } , \ldots , X _ { n } \sim$ $\mathcal { N } ( \mu , \sigma ^ { 2 } )$ , the sample variance is the r.v.

$$
S _ {n} ^ {2} = \frac {1}{n - 1} \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2}.
$$

Show that

$$
\frac {(n - 1) S _ {n} ^ {2}}{\sigma^ {2}} \sim \chi_ {n - 1} ^ {2}.
$$

Solution:

First let’s show that $\begin{array} { r } { \sum _ { j = 1 } ^ { n } ( Z _ { j } - \bar { Z } _ { n } ) ^ { 2 } \sim \chi _ { n - 1 } ^ { 2 } } \end{array}$ for standard Normal r.v.s $Z _ { 1 } , \ldots , Z _ { n }$ this is consistent with the more general result we are asked to prove and also serves as a useful stepping stone. Let’s start with the following useful identity, which is a special case of the identity from the proof of Theorem 6.3.4:

$$
\sum_ {j = 1} ^ {n} Z _ {j} ^ {2} = \sum_ {j = 1} ^ {n} (Z _ {j} - \bar {Z} _ {n}) ^ {2} + n \bar {Z} _ {n} ^ {2}.
$$

Now take the MGF of both sides. By Example 7.5.9, $\begin{array} { r } { \sum _ { j = 1 } ^ { n } ( Z _ { j } - \bar { Z } _ { n } ) ^ { 2 } } \end{array}$ and $n \bar { Z } _ { n } ^ { 2 }$ are independent, so the MGF of their sum is the product of the individual MGFs. Also,

$$
\sum_ {j = 1} ^ {n} Z _ {j} ^ {2} \sim \chi_ {n} ^ {2} \mathrm{and} n \bar {Z} _ {n} ^ {2} \sim \chi_ {1} ^ {2},
$$

so

$$
\left(\frac {1}{1 - 2 t}\right) ^ {n / 2} = \left(\text {MGF of} \sum_ {j = 1} ^ {n} (Z _ {j} - \bar {Z} _ {n}) ^ {2}\right) \cdot \left(\frac {1}{1 - 2 t}\right) ^ {1 / 2}.
$$

This implies

$$
\left(\text {MGF of} \sum_ {j = 1} ^ {n} (Z _ {j} - \bar {Z} _ {n}) ^ {2}\right) = \left(\frac {1}{1 - 2 t}\right) ^ {(n - 1) / 2},
$$

which is the $\chi _ { n - 1 } ^ { 2 }$ MGF. Since the MGF determines the distribution, we have

$$
\sum_ {j = 1} ^ {n} (Z _ {j} - \bar {Z} _ {n}) ^ {2} \sim \chi_ {n - 1} ^ {2}.
$$

For general $X _ { 1 } , \ldots , X _ { n }$ , use a location-scale transformation to write $X _ { j } = \mu + \sigma Z _ { j }$ and $\bar { X } _ { n }   =   \mu + \sigma \bar { Z } _ { n }$ . When we express $\textstyle \sum _ { j = 1 } ^ { n } ( X _ { j } - { \bar { X } } _ { n } ) ^ { 2 }$ in terms of the $Z _ { j }$ , the $\mu$ cancels and the $\sigma$ comes out squared:

$$
\sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2} = \sum_ {j = 1} ^ {n} (\mu + \sigma Z _ {j} - (\mu + \sigma \bar {Z} _ {n})) ^ {2} = \sigma^ {2} \sum_ {j = 1} ^ {n} (Z _ {j} - \bar {Z} _ {n}) ^ {2}.
$$

All in all,

$$
\frac {(n - 1) S _ {n} ^ {2}}{\sigma^ {2}} = \frac {1}{\sigma^ {2}} \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2} = \frac {1}{\sigma^ {2}} \cdot \sigma^ {2} \sum_ {j = 1} ^ {n} (Z _ {j} - \bar {Z} _ {n}) ^ {2} \sim \chi_ {n - 1} ^ {2},
$$

which is what we wanted. This also implies that $E ( S _ { n } ^ { 2 } )   =   \sigma ^ { 2 }$ , which agrees with what we showed in Theorem 6.3.4: the sample variance is unbiased for estimating the true variance. 

The Student-t distribution is defined by representing it in terms of a standard Normal r.v. and a $\chi _ { n } ^ { 2 } \mathrm {  ~ r . v . }$

Definition 10.4.4 (Student-t distribution). Let

$$
T = \frac {Z}{\sqrt {V / n}},
$$

where $Z \sim \mathcal { N } ( 0 , 1 ) ,   V \sim \chi _ { n } ^ { 2 }$ , and Z is independent of V . Then T is said to have the Student-t distribution with n degrees of freedom. We write this as $T \sim t _ { n }$ . Often “Student-t distribution” is abbreviated to “t distribution”.

The Student-t distribution was introduced in 1908 by William Gosset, a Master Brewer at Guinness, while working on quality control for beer. He was required by the company to publish his work under a pseudonym, and he chose the name Student. The t distribution forms the basis for hypothesis testing procedures known as t-tests, which are extremely widely used in practice (we do not introduce the details of t-tests here since they are better left for a course on statistical inference).

The PDF of the Student-t distribution with n degrees of freedom looks similar to that of a standard Normal, except with heavier tails (much heavier if n is small, and not much heavier if n is large). The formula for the PDF is

$$
f _ {T} (t) = \frac {\Gamma ((n + 1) / 2)}{\sqrt {n \pi} \Gamma (n / 2)} (1 + t ^ {2} / n) ^ {- (n + 1) / 2},
$$

though we will not prove this since the derivation is messy and anyway many of the most important properties of the Student-t distribution are easier to understand by thinking about how we defined it in terms of a Normal and a $\chi _ { n } ^ { 2 } \mathrm {  ~ r . v . }$ , rather than by doing tedious calculations with the PDF. Here are some of these properties.

Theorem 10.4.5 (Student-t properties). The Student-t distribution $t _ { n }$ has the following properties.

1. Symmetry: If $T \sim t _ { n }$ , then $- T \sim t _ { n }$ as well.
2. Cauchy as special case: The $t _ { 1 }$ distribution is the same as the Cauchy distribution, introduced in Example 7.1.25.
3. Convergence to Normal: As $n \to \infty$ , the $t _ { n }$ distribution approaches the standard Normal distribution.