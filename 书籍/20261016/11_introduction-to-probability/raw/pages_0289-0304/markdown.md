![](images/page_288_image_2.jpg)

## FIGURE 6.4

Left: $\mathcal { N } ( 0 , 1 )$ PDF (light) and a scaled $t _ { 3 }$ PDF (dark). Both have mean 0 and variance 1, but the latter has a sharper peak and heavier tails. Right: magnified version of right tail behavior.

## 6.2 Interpreting moments

Definition 6.2.1 (Kinds of moments). Let X be an r.v. with mean µ and variance $\sigma ^ { 2 }$ . For any positive integer n, the nth moment of X is $E ( X ^ { n } )$ , the nth central moment is $E ( ( X   -   \mu ) ^ { n } )$ , and the nth standardized moment is $\hat { E } ( \left( \textstyle \frac { X - \mu } { \sigma } \right) ^ { n } )$ . Throughout the previous sentence, “if it exists” is left implicit.

In particular, the mean is the first moment and the variance is the second central moment. The term moment is borrowed from physics. Let X be a discrete r.v. with distinct possible values $x _ { 1 } , \ldots , x _ { n }$ , and imagine a pebble with mass $m _ { j } = P ( X = x _ { j } )$ positioned at $x _ { j }$ on a number line, for each j (as illustrated in Figure 6.5). In physics,

$$
E (X) = \sum_ {j = 1} ^ {n} m _ {j} x _ {j}
$$

is called the center of mass of the system, and

$$
\mathrm{Var} (X) = \sum_ {j = 1} ^ {n} m _ {j} (x _ {j} - E (X)) ^ {2}
$$

is called the moment of inertia about the center of mass.

We’ll now define skewness, a single-number summary of asymmetry which, as alluded to earlier, is based on the third moment. In fact, skewness is defined to be the third standardized moment.

![](images/page_289_image_2.jpg)

<details>
<summary>text_image</summary>

m₁
x₁
m₂
x₂
E(X)
m₃
x₃
m₄
x₄
m₅
x₅
</details>

## FIGURE 6.5

Physics interpretation of moments. The mean (first moment) of an $\mathbf { r } . \mathbf { V } .$ corresponds to the center of mass of a collection of pebbles, and the variance (second central moment) corresponds to the moment of inertia about the center of mass.

Definition 6.2.2 (Skewness). The skewness of an r.v. X with mean $\mu$ and variance $\sigma ^ { 2 }$ is the third standardized moment of $X$ :

$$
\operatorname{Skew} (X) = E \left(\frac {X - \mu}{\sigma}\right) ^ {3}.
$$

By standardizing first, we make the definition of Skew(X) not depend on the location or the scale of $X$ , which is reasonable since we already have $\mu$ and $\sigma$ to provide information about location and scale. Also, standardizing first gives the nice property that the units in which $X$ is measured $( \mathrm { e . g . }$ , inches vs. meters) will not affect the skewness.

To understand how skewness measures asymmetry, we first need to discuss what it means for an r.v. to be symmetric.

Definition 6.2.3 (Symmetry of an $\mathrm { r . v . ) }$ . We say that an $\mathbf { r } . \mathbf { V }$ . X has a symmetric distribution about $\mu$ if $X - \mu$ has the same distribution as $\mu - X$ . We also say that X is symmetric or that the distribution of X is symmetric; these all have the same meaning.

The number $\mu$ in the above definition must be $E ( X )$ if the mean exists, since

$$
E (X) - \mu = E (X - \mu) = E (\mu - X) = \mu - E (X)
$$

simplifies to $E ( X ) = \mu$ . Because of this, it is common to say $^ { \circ } X$ is symmetric” as shorthand for $^ { \circ } X$ is symmetric about its mean” (if the mean exists). The number $\mu$ is also a median of the distribution, since if $X - \mu$ has the same distribution as $\mu - X$ , then

$$
P (X - \mu \leq 0) = P (\mu - X \leq 0),
$$

so

$$
P (X \leq \mu) = P (X \geq \mu),
$$

which implies that

$$
P (X \leq \mu) = 1 - P (X > \mu) \geq 1 - P (X \geq \mu) = 1 - P (X \leq \mu),
$$

showing that $P ( X \leq \mu ) \geq 1 / 2$ and $P ( X \geq \mu ) \geq 1 / 2$ h 6.2.4. Sometimes people say $^ { \circ } X$ is symmetric” to mean $^ { \circ } X$ is symmetric about $0 ^ { \circ }$ . Note that if X is symmetric about $\mu ,$ then $X   -   \mu$ is symmetric about 0. Symmetry about 0 is especially convenient since then $- X$ and X have the same distribution, and the PDF of X (if X is continuous) is an even function, as shown below.

Intuitively, symmetry means that the PDF of X to the left of $\mu$ is the mirror image of the PDF of X to the right of $\mu$ (for X continuous, and the same holds for the PMF if X is discrete). For example, we have seen before that $X   \sim   \mathcal { N } ( \mu , \sigma ^ { 2 } )$ is symmetric; in terms of the definition, this is because $X - \mu$ and $\mu - X$ are both $\mathcal { N } ( 0 , \sigma ^ { 2 } )$ . We have also seen from Corollary 3.3.8 that $X \sim \operatorname { B i n } ( n , p )$ is symmetric when $p = 1 / 2$

We can also give an algebraic description of what the PDF of a symmetric continuous r.v. looks like.

Proposition 6.2.5 (Symmetry in terms of the PDF). Let X be a continuous r.v. with PDF $f .$ Then X is symmetric about $\mu$ if and only if $f(x) = f(2\mu - x)$ for all $x .$ .

Proof. Let $F$ be the CDF of X. If symmetry holds, we have

$$
F (x) = P (X - \mu \leq x - \mu) = P (\mu - X \leq x - \mu) = P (X \geq 2 \mu - x) = 1 - F (2 \mu - x).
$$

Taking the derivative of both sides yields $f ( x )   =   f ( 2 \mu - x )$ . Conversely, suppose that $f(x) = f(2\mu - x)$ holds for all x. Integrating both sides, we have

$$
P (X - \mu \leq t) = P (X \leq \mu + t) = \int_ {- \infty} ^ {\mu + t} f (x) d x = \int_ {- \infty} ^ {\mu + t} f (2 \mu - x) d x,
$$

which, after the substitution $w = 2 \mu - x$ , becomes

$$
\int_ {\mu - t} ^ {\infty} f (w) d w = P (X \geq \mu - t) = P (\mu - X \leq t).
$$

Odd central moments give some] information about symmetry.

Proposition 6.2.6 (Odd central moments of a symmetric distribution). Let X be symmetric about its mean $\mu .$ Then for any odd number $m ,$ the mth central moment $E ( X - \mu ) ^ { m }$ is 0 if it exists.

Proof. Since $X - \mu$ has the same distribution as $\mu - X$ , they have the same mth moment (if it exists):

$$
E (X - \mu) ^ {m} = E (\mu - X) ^ {m}.
$$

Let $Y = ( X - \mu ) ^ { m }$ . Then $( \mu - X ) ^ { m } = ( - ( X - \mu ) ) ^ { m } = ( - 1 ) ^ { m } Y = - Y$ , so the above equation just says $E(Y) = -E(Y)$ . So $E ( Y ) = 0$ 

This leads us to consider using an odd standardized moment as a measure of the skew of a distribution. The first standardized moment is always 0, so the third standardized moment is taken as the definition of skewness. Positive skewness is indicative of having a long right tail relative to the left tail, and negative skewness is indicative of the reverse. (The converse of the above proposition is false, though: there exist asymmetric distributions whose odd central moments are all 0.)

Why not use, say, the fifth standardized moment instead of the third? One reason is that the third standardized moment is usually easier to calculate. Another reason is that we may want to estimate skewness from a data set. It is usually easier to estimate lower moments than higher moments in a stable way since, for example, a large, noisy observation will have a very large, very noisy fifth power. Nevertheless, just as the mean isn’t the only useful notion of average and the variance isn’t the only useful notion of spread, the third standardized moment isn’t the only useful notion of skew.

Another important descriptive feature of a distribution is how heavy its tails are. For a given variance, is the variability explained more by a few rare (extreme) events or by a moderate number of moderate deviations from the mean? This is an important consideration for risk management in finance: for many financial assets, the distribution of returns has a heavy left tail caused by rare but severe crisis events, and failure to account for these rare events can have disastrous consequences, as demonstrated by the 2008 financial crisis.

As with measuring skew, no single measure can perfectly capture the tail behavior, but there is a widely used summary based on the fourth standardized moment.

Definition 6.2.7 (Kurtosis). The kurtosis of an r.v. X with mean $\mu$ and variance $\sigma ^ { 2 }$ is a shifted version of the fourth standardized moment of X:

$$
\operatorname{Kurt} (X) = E \left(\frac {X - \mu}{\sigma}\right) ^ {4} - 3.
$$

h 6.2.8. The reason for subtracting 3 is that this makes any Normal distribution have kurtosis 0 (as shown in Section 6.5). This provides a convenient basis for comparison. However, some sources define the kurtosis without the 3, in which case they call our version “excess kurtosis”.

Figure 6.6 shows three named distributions and lists the skewness and kurtosis of each. The Expo(1) and Pois(4) distributions (left and middle) both have positive skewness and positive kurtosis, indicating that they are right-skewed and their tails are heavier than those of a Normal distribution. The $\mathrm { U n i f } ( 0 , 1 )$ distribution (right) has zero skewness and negative kurtosis: zero skewness because the distribution is symmetric about its mean, and negative kurtosis because it has no tails!

![](images/page_292_image_2.jpg)

## FIGURE 6.6

Skewness and kurtosis of some named distributions. Left: Expo(1) PDF, skewness = 2, kurtosis = 6. Middle: Pois(4) PMF, skewness = 0.5, kurtosis = 0.25. Right: Unif(0, 1) PDF, skewness = 0, kurtosis = −1.2.

## 6.3 Sample moments

In statistical inference, a central problem is how to use data to estimate unknown parameters of a distribution, or functions of unknown parameters. It is especially common to want to estimate the mean and variance of a distribution. If the data are i.i.d. random variables $X _ { 1 } , \ldots , X _ { n }$ where the mean $E ( X _ { j } )$ is unknown, then the most obvious way to estimate the mean is simply to average the $X _ { j }$ , taking the arithmetic mean.

For example, if the observed data are 3, 1, 1, 5, then a simple, natural way to estimate the mean of the distribution that generated the data is to use $( 3   +   1   +   1   +   5 ) / 4 = 2 . 5$ This is called the sample mean. Similarly, if we want to estimate the second moment of the distribution that generated the data 3, 1, 1, 5, then a simple, natural way is to use $( 3 ^ { 2 } + 1 ^ { 2 } + 1 ^ { 2 } + 5 ^ { 2 } ) / \dot { 4 } = 9$ . This is called the sample second moment. In general, sample moments are defined as follows.

Definition 6.3.1 (Sample moments). Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d. random variables. The kth sample moment is the r.v.

$$
M _ {k} = \frac {1}{n} \sum_ {j = 1} ^ {n} X _ {j} ^ {k}.
$$

The sample mean ${ \bar { X } } _ { n }$ is the first sample moment:

$$
\bar {X} _ {n} = \frac {1}{n} \sum_ {j = 1} ^ {n} X _ {j}.
$$

In contrast, the population mean or true mean is $E ( X _ { j } )$ , the mean of the distribution from which the $X _ { j }$ were drawn.

The law of large numbers, which we prove in Chapter 10, shows that the kth sample moment of i.i.d. random variables $X _ { 1 } , \ldots , X _ { n }$ converges to the kth moment $E ( X _ { 1 } ^ { k } )$ as $n \to \infty$ . Also, the expected value of the kth sample moment is the kth moment. In statistical terms, we say that the kth sample moment is unbiased for estimating the kth moment. It is easy to check this by linearity:

$$
E \left(\frac {1}{n} \sum_ {j = 1} ^ {n} X _ {j} ^ {k}\right) = \frac {1}{n} \left(E (X _ {1} ^ {k}) + \dots + E (X _ {n} ^ {k})\right) = E (X _ {1} ^ {k}).
$$

The mean and variance of the sample mean are often needed, and have nice expressions that are often needed in statistics.

Theorem 6.3.2 (Mean and variance of sample mean). Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d. r.v.s with mean $\mu$ and variance $\sigma ^ { 2 }$ . Then the sample mean ${ \bar { X } } _ { n }$ is unbiased for estimating $\mu .$ That is,

$$
E (\bar {X} _ {n}) = \mu .
$$

The variance of ${ \bar { X } } _ { n }$ is given by

$$
\mathrm{Var} (\bar {X} _ {n}) = \frac {\sigma^ {2}}{n}.
$$

Proof. We have $E ( { \bar { X } } _ { n } )   =   \mu$ since we showed above that the kth sample moment is unbiased for estimating the kth moment. For the variance, we will use the fact (shown in the next chapter) that the variance of the sum of independent r.v.s is the sum of the variances:

$$
\mathrm{Var} (\bar {X} _ {n}) = \frac {1}{n ^ {2}} \mathrm{Var} (X _ {1} + \dots + X _ {n}) = \frac {n}{n ^ {2}} \mathrm{Var} (X _ {1}) = \frac {\sigma^ {2}}{n}.
$$

For estimating the variance of the distribution of i.i.d. r.v.s $X _ { 1 } , \ldots , X _ { n } ,$ a natural approach building on the above concepts is to mimic the formula $\operatorname { V a r } ( X ) = E ( X ^ { 2 } ) -$ $( E X ) ^ { 2 }$ by taking the second sample moment and subtracting the square of the sample mean. There are advantages to this method, but a more common method is as follows.

Definition 6.3.3 (Sample variance and sample standard deviation). Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d. random variables. The sample variance is the r.v.

$$
S _ {n} ^ {2} = \frac {1}{n - 1} \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2}.
$$

The sample standard deviation is the square root of the sample variance.

The idea of the above definition is to mimic the formula $\operatorname { V a r } ( X ) = E ( X   -   E ( X ) ) ^ { 2 }$ by averaging the squared distances of the $X _ { j }$ from the sample mean, except with $n - 1$ rather than $n$ in the denominator. The motivation for the $n - 1$ is that this makes the sample variance $S _ { n } ^ { 2 }$ unbiased for estimating $\sigma ^ { 2 } , \; \mathrm { i . e . }$ , it is correct on average. However, the sample standard deviation $S _ { n }$ is not unbiased for estimating $\sigma ;$ we will see in Chapter 10 which way the inequality goes. In any case, unbiasedness is only one of several criteria by which to judge an estimation procedure. For example, in some problems we can get a lower mean squared error in return for allowing a little bit of bias, and this tradeoff may be worthwhile.

Theorem 6.3.4 (Unbiasedness of sample variance). Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d. r.v.s with mean $\mu$ and variance $\sigma ^ { 2 }$ . Then the sample variance $S _ { n } ^ { 2 }$ is unbiased for estimating $\sigma ^ { 2 }$ , i.e.,

$$
E (S _ {n} ^ {2}) = \sigma^ {2}.
$$

Proof. The key to the proof is the handy identity

$$
\sum_ {j = 1} ^ {n} (X _ {j} - c) ^ {2} = \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2} + n (\bar {X} _ {n} - c) ^ {2},
$$

which holds for all $c .$ To verify the identity, add and subtract ${ \bar { X } } _ { n }$ in the left-hand sum:

$$
\begin{array}{l} \sum_ {j = 1} ^ {n} (X _ {j} - c) ^ {2} = \sum_ {j = 1} ^ {n} \left((X _ {j} - \bar {X} _ {n}) + (\bar {X} _ {n} - c)\right) ^ {2} \\ = \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2} + 2 \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) (\bar {X} _ {n} - c) + \sum_ {j = 1} ^ {n} (\bar {X} _ {n} - c) ^ {2} \\ = \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2} + n (\bar {X} _ {n} - c) ^ {2}. \\ \end{array}
$$

For the last line, we used the fact that $\bar { X } _ { n } - c$ does not depend on $j$ and the fact that

$$
\sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) = \sum_ {j = 1} ^ {n} X _ {j} - \sum_ {j = 1} ^ {n} \bar {X} _ {n} = n \bar {X} _ {n} - n \bar {X} _ {n} = 0.
$$

Now let us apply the identity, choosing $c = \mu$ . Taking the expectation of both sides,

$$
n E (X _ {1} - \mu) ^ {2} = E \left(\sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {2}\right) + n E (\bar {X} _ {n} - \mu) ^ {2}.
$$

By definition of variance, $E ( X _ { 1 } - \mu ) ^ { 2 } = \operatorname { V a r } ( X _ { 1 } ) = \sigma ^ { 2 }$ , and $E ( \bar { X } _ { n } - \mu ) ^ { 2 } = \operatorname { V a r } ( \bar { X } _ { n } ) =$ $\sigma ^ { 2 } / n$ . Plugging these results in above and simplifying, we have $E ( S _ { n } ^ { 2 } ) = \sigma ^ { 2 }$ 

Similarly, we can define the sample skewness to be

$$
\frac {\frac {1}{n} \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {3}}{S _ {n} ^ {3}},
$$

and the sample kurtosis to be

$$
\frac {\frac {1}{n} \sum_ {j = 1} ^ {n} (X _ {j} - \bar {X} _ {n}) ^ {4}}{S _ {n} ^ {4}} - 3.
$$

Beyond the fourth moment, it rapidly gets harder to interpret moments graphically and harder to estimate them well from data if they are unknown. However, in the rest of this chapter we will see that it can still be useful to know all the moments of a distribution. We will also study a way of computing moments that is often easier than LOTUS. Both the usefulness and the computation of moments are closely connected to a blueprint called the moment generating function, to which we devote most of the rest of this chapter.

## 6.4 Moment generating functions

A generating function is a clothesline on which we hang up a sequence of numbers for display. – Herbert Wilf [28]

Generating functions are a powerful tool in combinatorics and probability, bridging between sequences of numbers and the world of calculus. In probability, they are useful for studying both discrete and continuous distributions. The general idea behind a generating function is as follows: starting with a sequence of numbers, create a continuous function—the generating function—that encodes the sequence. We then have all the tools of calculus at our disposal for manipulating the generating function.

A moment generating function, as its name suggests, is a generating function that encodes the moments of a distribution. Here is the definition, followed by a few examples.

Definition 6.4.1 (Moment generating function). The moment generating function (MGF) of an r.v. X is $M ( t ) = E ( e ^ { t X } )$ , as a function of $t ,$ if this is finite on some open interval $( - a , a )$ containing 0. Otherwise we say the MGF of X does not exist.

A natural question at this point is “What is the interpretation of $t ? ^ { \flat \flat }$ The answer is that t has no interpretation in particular; it’s just a bookkeeping device that we introduce in order to be able to use calculus instead of working with a discrete sequence of moments.

Note that $M ( 0 ) = 1$ for any valid MGF $M ;$ whenever you compute an MGF, plug in 0 and see if you get 1, as a quick check!

Example 6.4.2 (Bernoulli MGF). For $X \sim \operatorname { B e r n } ( p ) ,   e ^ { t X }$ takes on the value $e ^ { t }$ with probability $p$ and the value 1 with probability $q ,$ so $M ( t ) = E ( e ^ { t X } ) = p e ^ { t } + q$ . Since this is finite for all values of $t ,$ the MGF is defined on the entire real line. 

Example 6.4.3 (Geometric MGF). For $X \sim \operatorname { G e o m } ( p )$

$$
M (t) = E (e ^ {t X}) = \sum_ {k = 0} ^ {\infty} e ^ {t k} q ^ {k} p = p \sum_ {k = 0} ^ {\infty} (q e ^ {t}) ^ {k} = \frac {p}{1 - q e ^ {t}}
$$

for $q e ^ { t } < 1$ , i.e., for t in $( - \infty , \log ( 1 / q ) )$ , which is an open interval containing 0. 

Example 6.4.4 (Uniform MGF). Let $U \sim \operatorname { U n i f } ( a , b )$ . Then the MGF of U is

$$
M (t) = E (e ^ {t U}) = \frac {1}{b - a} \int_ {a} ^ {b} e ^ {t u} d u = \frac {e ^ {t b} - e ^ {t a}}{t (b - a)}
$$

for $t \neq 0$ , and $M ( 0 ) = 1$

The next three theorems give three reasons why the MGF is important. First, the MGF encodes the moments of an r.v. Second, the MGF of an r.v. determines its distribution, like the CDF and PMF/PDF. Third, MGFs make it easy to find the distribution of a sum of independent r.v.s. Let’s take these one by one.

Theorem 6.4.5 (Moments via derivatives of the MGF). Given the MGF of X, we can get the nth moment of X by evaluating the nth derivative of the MGF at 0: $E ( X ^ { n } ) = M ^ { ( n ) } ( 0 )$

Proof. This can be seen by noting that the Taylor expansion of $M ( t )$ about 0 is

$$
M (t) = \sum_ {n = 0} ^ {\infty} M ^ {(n)} (0) \frac {t ^ {n}}{n !},
$$

while on the other hand, we also have

$$
M (t) = E (e ^ {t X}) = E \left(\sum_ {n = 0} ^ {\infty} X ^ {n} \frac {t ^ {n}}{n !}\right).
$$

We are allowed to interchange the expectation and the infinite sum because certain technical conditions are satisfied (this is where we invoke the condition that $E ( e ^ { t X } )$ is finite in an interval around 0), so

$$
M (t) = \sum_ {n = 0} ^ {\infty} E (X ^ {n}) \frac {t ^ {n}}{n !}.
$$

Matching the coefficients of the two expansions, we get $E ( X ^ { n } ) = M ^ { ( n ) } ( 0 )$

The above theorem is surprising in that for a continuous r.v. X, to compute moments would seemingly require doing integrals with LOTUS, but with the MGF it is possible to find moments by taking derivatives rather than doing integrals!

Theorem 6.4.6 (MGF determines the distribution). The MGF of a random variable determines its distribution: if two r.v.s have the same MGF, they must have the same distribution. In fact, if there is even a tiny interval $( - a , a )$ containing 0 on which the MGFs are equal, then the r.v.s must have the same distribution.

The above theorem is a difficult result in analysis, so we will not prove it here.

Theorem 6.4.7 (MGF of a sum of independent $\mathrm { r . v . s ) }$ . If X and $Y$ are independent, then the MGF of $X + Y$ is the product of the individual MGFs:

$$
M _ {X + Y} (t) = M _ {X} (t) M _ {Y} (t).
$$

This is true because if X and Y are independent, then $E(e^{t(X+Y)}) = E(e^{tX})E(e^{tY})$ (this follows from results discussed in Chapter 7). Using this fact, we can get the MGFs of the Binomial and Negative Binomial, which are sums of independent Bernoullis and Geometrics, respectively.

Example 6.4.8 (Binomial MGF). The MGF of a Bern(p) r.v. is $p e ^ { t } + q ,$ so the MGF of a Bin $( n , p )$ r.v. is

$$
M (t) = (p e ^ {t} + q) ^ {n}.
$$

![](images/page_297_chart_8.jpg)

<details>
<summary>line</summary>

| t | MGF |
| --- | --- |
| -1.0 | ~0.5 |
| -0.5 | ~0.7 |
| 0.0 | ~1.0 |
| 0.5 | ~1.8 |
| 1.0 | ~3.5 |
</details>

## FIGURE 6.7

Bin $( 2 , 1 / 2 )$ MGF, $\begin{array} { r } { M ( t ) = \left( \frac { 1 } { 2 } e ^ { t } + \frac { 1 } { 2 } \right) ^ { 2 } } \end{array}$ . The slope of the MGF at $t = 0$ is 1, so the mean of the distribution is 1. The concavity or second derivative of the MGF at $t = 0   is   3/2$ , so the second moment of the distribution is $3 / 2$

Figure 6.7 plots the MGF of the $\mathrm { B i n } ( 2 , 1 / 2 )$ distribution, $\begin{array} { r } { M ( t )   =   \left( \frac { 1 } { 2 } e ^ { t } + \frac { 1 } { 2 } \right) ^ { 2 } } \end{array}$ , between $t = - 1$ and $t = 1$ . As with all MGFs, the value of the MGF is 1 at $t = 0$ . The first and second moments of the distribution are the first and second derivatives of the MGF, evaluated at $t = 0$ ; these correspond to the slope and concavity of the plotted curve at $t = 0$ . These two derivatives are 1 and $3 / 2$ , corresponding to the fact that the Bin $\left| ( 2 , 1 / 2 ) \right.$ distribution has mean 1 and variance $3 / 2 - 1 ^ { 2 } = 1 / 2$ 

Example 6.4.9 (Negative Binomial MGF). We know the MGF of a Geom(p) r.v. is $\frac { p } { 1 { - } q e ^ { t } }$ for $q e ^ { t } < 1$ , so the MGF of $X \sim \mathrm { N B i n } ( r , p )$ is

$$
M (t) = \left(\frac {p}{1 - q e ^ {t}}\right) ^ {r}, \text {for} q e ^ {t} <   1.
$$

![](images/page_297_image_14.jpg)

h 6.4.10. Not all $\mathbf { r } . \mathbf { v } . \mathbf { S }$ have an MGF. Some r.v.s X don’t even have $E ( X )$ exist, or don’t have $E ( X ^ { n } )$ exist for some $n > 1$ , in which case the MGF clearly will not exist. But even if all the moments of X exist, the MGF may not exist if the moments grow too quickly. Luckily, there is a way to fix this: inserting an imaginary number! The function $\psi ( t )   =   E ( e ^ { i t X } )$ with $i   =   \sqrt { - 1 }$ is called the characteristic function by statisticians and the Fourier transform by everyone else. It turns out that the characteristic function always exists. In this book we will focus on the MGF rather than the characteristic function, to avoid having to handle imaginary numbers.

As we saw in the previous chapter, location and scale transformations are a fundamental way to build a family of distributions from an initial distribution. For example, starting with $Z   \sim   \mathcal { N } ( 0 , 1 )$ , we can scale by $\sigma$ and shift by $\mu$ to obtain $X = \mu + \sigma Z \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ . In general, if we have an r.v. X with mean $\mu$ and standard deviation $\sigma > 0$ , we can create the standardized version $( X - \mu ) / \sigma$ , and vice versa. Conveniently, it is easy to relate the MGFs of two r.v.s connected by such a transformation.

Proposition 6.4.11 (MGF of location-scale transformation). If X has MGF $M ( t )$ then the MGF of $a + b X$ is

$$
E (e ^ {t (a + b X)}) = e ^ {a t} E (e ^ {b t X}) = e ^ {a t} M (b t).
$$

For example, let’s use this proposition to help obtain the MGFs of the Normal and Exponential distributions.

Example 6.4.12 (Normal MGF). The MGF of a standard Normal r.v. Z is

$$
M _ {Z} (t) = E (e ^ {t Z}) = \int_ {- \infty} ^ {\infty} e ^ {t z} \frac {1}{\sqrt {2 \pi}} e ^ {- z ^ {2} / 2} d z.
$$

After completing the square, we have

$$
M _ {Z} (t) = e ^ {t ^ {2} / 2} \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {2 \pi}} e ^ {- (z - t) ^ {2} / 2} d z = e ^ {t ^ {2} / 2},
$$

since the $\mathcal { N } ( t , 1 )$ PDF integrates to 1. Thus, the MGF of $X = \mu + \sigma Z \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ is

$$
M _ {X} (t) = e ^ {\mu t} M _ {Z} (\sigma t) = e ^ {\mu t} e ^ {(\sigma t) ^ {2} / 2} = e ^ {\mu t + \frac {1}{2} \sigma^ {2} t ^ {2}}.
$$

Example 6.4.13 (Exponential MGF). The MGF of $X \sim \mathrm { E x p o ( 1 ) }$ is

$$
M (t) = E (e ^ {t X}) = \int_ {0} ^ {\infty} e ^ {t x} e ^ {- x} d x = \int_ {0} ^ {\infty} e ^ {- x (1 - t)} d x = \frac {1}{1 - t} \quad \text {for} t <   1.
$$

So the MGF of $Y = X / \lambda \sim \operatorname { E x p o } ( \lambda )$ is

$$
M _ {Y} (t) = M _ {X} \left(\frac {t}{\lambda}\right) = \frac {\lambda}{\lambda - t} \quad \text {for} t <   \lambda .
$$



## 6.5 Generating moments with MGFs

We now give some examples of using an MGF to find moments. . Theorem 6.4.5 shows that we can get moments by differentiating the MGF and evaluating at 0, rather than doing a complicated sum or integral by LOTUS. Better yet, in some cases we can simultaneously find all the moments of a distribution via a Taylor expansion, rather than differentiating over and over again.

Example 6.5.1 (Exponential moments). In this example we will show how to use the Exponential MGF to get all the moments of the Exponential distribution simultaneously! Let $X \sim \mathrm { E x p o ( 1 ) }$ . The MGF of X is $M ( t ) = 1 / ( 1 - t )$ for $t < 1$

As shown in Theorem 6.4.5, we could obtain the moments by taking derivatives of the MGF and evaluating at 0. In this case, though, we recognize $1 / ( 1 - t )$ a s a geometric series, valid in an interval around 0. For $| t | < 1$ ,

$$
M (t) = \frac {1}{1 - t} = \sum_ {n = 0} ^ {\infty} t ^ {n} = \sum_ {n = 0} ^ {\infty} n! \frac {t ^ {n}}{n !}.
$$

On the other hand, we know that $E ( X ^ { n } )$ is the coefficient of the term involving $t ^ { n }$ in the Taylor expansion of $M ( t )$

$$
M (t) = \sum_ {n = 0} ^ {\infty} E (X ^ {n}) \frac {t ^ {n}}{n !}.
$$

Thus we can match coefficients to conclude that $E ( X ^ { n } ) = n !$ for all $n .$ We not only did not have to do a LOTUS integral, but also we did not, for example, have to take 10 derivatives to get the 10th moment—we got the moments all at once.

To find the moments of $Y \sim \operatorname { E x p o } ( \lambda )$ , use a scale transformation: we can express $Y = X / \lambda$ where $X \sim \mathrm { E x p o ( 1 ) }$ . Therefore $Y ^ { n } = X ^ { n } / \lambda ^ { n }$ and

$$
E (Y ^ {n}) = \frac {n !}{\lambda^ {n}}.
$$

In particular, we have found the mean and variance of $Y$ , making good on our promise from Chapter $5 ;$

$$
E (Y) = \frac {1}{\lambda},
$$

$$
\mathrm{Var} (Y) = E (Y ^ {2}) - (E Y) ^ {2} = \frac {2}{\lambda^ {2}} - \frac {1}{\lambda^ {2}} = \frac {1}{\lambda^ {2}}.
$$

Example 6.5.2 (Standard Normal moments). In this example we will find all the moments of the standard Normal distribution. Let $Z   \sim   \mathcal { N } ( 0 , 1 )$ . We can use the same trick of matching the coefficients of the Taylor expansion.

$$
M (t) = e ^ {t ^ {2} / 2} = \sum_ {n = 0} ^ {\infty} \frac {(t ^ {2} / 2) ^ {n}}{n !} = \sum_ {n = 0} ^ {\infty} \frac {t ^ {2 n}}{2 ^ {n} \cdot n !} = \sum_ {n = 0} ^ {\infty} \frac {(2 n) !}{2 ^ {n} \cdot n !} \frac {t ^ {2 n}}{(2 n) !}.
$$

Therefore

$$
E (Z ^ {2 n}) = \frac {(2 n) !}{2 ^ {n} \cdot n !},
$$

and the odd moments of $Z$ are equal to $0 ,$ which must be true due to the symmetry of the standard Normal. From the story proof about partnerships in Example 1.5.4, we know that $\frac { ( 2 n ) ! } { 2 ^ { n } { \cdot } n ! }$ is the product of the odd numbers from 1 through $2 n - 1$ , so

$$
E (Z ^ {2}) = 1, E (Z ^ {4}) = 1 \cdot 3, E (Z ^ {6}) = 1 \cdot 3 \cdot 5, \dots
$$

This result also shows that the kurtosis of a Normal r.v. is 0. For $X \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$

$$
\operatorname{Kurt} (X) = E \left(\frac {X - \mu}{\sigma}\right) ^ {4} - 3 = E (Z ^ {4}) - 3 = 3 - 3 = 0.
$$

Example 6.5.3 (Log-Normal moments). Now let’s consider the Log-Normal distribution. We say that Y is Log-Normal with parameters $\mu$ and $\sigma ^ { 2 }$ , denoted by $Y \sim \mathcal { L N } ( \mu , \sigma ^ { 2 } ) , \mathrm { i f } Y = e ^ { X }$ where X $\sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$

h 6.5.4. Log-Normal does not mean “log of a Normal”, since a Normal can be negative. Rather, Log-Normal means “log is Normal”. It is important to distinguish between the mean and variance of the Log-Normal and the mean and variance of the underlying Normal. Here we are defining $\mu$ and $\sigma ^ { 2 }$ to be the mean and variance of the underlying Normal, which is the most common convention.

Interestingly, the Log-Normal MGF does not exist, since $E ( e ^ { t Y } )$ is infinite for all $t > 0$ . Consider the case where $Y = e ^ { Z }$ for $Z \sim \mathcal { N } ( 0 , 1 )$ ; by LOTUS,

$$
E (e ^ {t Y}) = E (e ^ {t e ^ {Z}}) = \int_ {- \infty} ^ {\infty} e ^ {t e ^ {z}} \frac {1}{\sqrt {2 \pi}} e ^ {- z ^ {2} / 2} d z = \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {2 \pi}} e ^ {t e ^ {z} - z ^ {2} / 2} d z.
$$

For any $t > 0 ,   t e ^ { z } - z ^ { 2 } / 2$ goes to infinity as $z \mathrm { g r o w s }$ , so the above integral diverges. Since $E ( e ^ { t Y } )$ is not finite on an open interval around $0 ,$ the MGF of $Y$ does not exist. The same reasoning holds for a general Log-Normal distribution.

However, even though the Log-Normal MGF does not exist, we can still obtain all the moments of the Log-Normal, using the MGF of the Normal. For $Y = e ^ { X }$ with $X \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ ,

$$
E (Y ^ {n}) = E (e ^ {n X}) = M _ {X} (n) = e ^ {n \mu + \frac {1}{2} n ^ {2} \sigma^ {2}}.
$$

In other words, the nth moment of the Log-Normal is the MGF of the Normal evaluated at $t = n$ . Letting

$$
m = E (Y) = e ^ {\mu + \frac {1}{2} \sigma^ {2}},
$$

we have, after some algebra,

$$
\mathrm{Var} (Y) = E (Y ^ {2}) - m ^ {2} = m ^ {2} (e ^ {\sigma^ {2}} - 1).
$$

All Log-Normal distributions are right-skewed. For example, Figure 6.2 shows a

Log-Normal PDF in dark, with mean 2 and variance 12. This is the distribution of $e ^ { X }$ for $X \sim \mathcal { N } ( 0 , 2 \log 2 )$ , and it is clearly right-skewed. To quantify this, let us compute the skewness of the Log-Normal r.v. $Y = e ^ { X }$ for $X \sim \mathcal { N } ( 0 , \sigma ^ { 2 } )$ . Letting $m = E(Y) = e^{\frac{1}{2}\sigma^{2}}$ , we have $E ( Y ^ { n } ) = m ^ { n ^ { 2 } }$ and $\operatorname { V a r } ( Y ) = m ^ { 2 } ( m ^ { 2 } - 1 )$ , and the third central moment is

$$
\begin{array}{l} E (Y - m) ^ {3} = E (Y ^ {3} - 3 m Y ^ {2} + 3 m ^ {2} Y - m ^ {3}) \\ = E (Y ^ {3}) - 3 m E (Y ^ {2}) + 2 m ^ {3} \\ = m ^ {9} - 3 m ^ {5} + 2 m ^ {3}. \\ \end{array}
$$

Thus, the skewness is

$$
\mathrm{Skew} (Y) = \frac {E (Y - m) ^ {3}}{\mathrm{SD} ^ {3} (Y)} = \frac {m ^ {9} - 3 m ^ {5} + 2 m ^ {3}}{m ^ {3} (m ^ {2} - 1) ^ {3 / 2}} = (m ^ {2} + 2) \sqrt {m ^ {2} - 1},
$$

where in the last step we factored $m^{6}-3m^{2}+2=(m^{2}+2)(m-1)^{2}(m+1)^{2}$ . The skewness is positive since $m > 1$ , and it increases very quickly as σ grows. 

In the next example, we introduce the Weibull distribution, which is one of the most widely used distributions in survival analysis (the study of the duration of time until an event occurs, e.g., modeling how long someone with a particular disease will live).

Example 6.5.5 (Weibull distribution). As you may remember from the previous chapter, the Exponential distribution is memoryless, which makes it unrealistic for, $\mathbf { e . g . }$ , modeling a human lifetime. Remarkably, simply raising an Exponential r.v. to a power dramatically improves the flexibility and applicability of the distribution.

Let $T = X ^ { 1 / \gamma }$ , with $X   \sim   \mathrm { E x p o } ( \lambda )$ and $\lambda , \gamma > 0$ . The distribution of $T$ is called the Weibull distribution, and we denote this by $T \sim \operatorname { W e i } ( \lambda , \gamma )$ . This generalizes the Exponential, with the case $\gamma = 1$ reducing back to the Exponential.

Weibull distributions are widely used in biostatistics, epidemiology, and engineering; there is even an 800-page book devoted to this distribution: The Weibull Distribution: A Handbook by Horst Rinne [21].

The PDF of $T$ is

$$
f (t) = \gamma \lambda e ^ {- \lambda t ^ {\gamma}} t ^ {\gamma - 1}
$$

for $t > 0$ , as can be shown by relating the CDF of $T$ to the CDF of $X ,$ or by using transformation results from Chapter 8. The PDF looks somewhat complicated, but often when working with a Weibull random variable we can use the strategy of first transforming it back to an Exponential.

For simplicity and concreteness, let’s look at a specific Weibull distribution, letting $\lambda = 1$ and $\gamma = 1 / 3$

(a) Find $P ( T > s + t | T > s )$ for $s , t > 0$ . Does T have the memoryless property?
(b) Find the mean and variance of $T ,$ and the nth moment $E ( T ^ { n } )$ for $n = 1 , 2 , \ldots .$

(c) Determine whether or not the MGF of T exists.

Solution:

(a) The CDF of $T$ is

$$
P (T \leq t) = P (X ^ {3} \leq t) = P (X \leq t ^ {1 / 3}) = 1 - e ^ {- t ^ {1 / 3}},
$$

for $t > 0$ . So

$$
P (T > s + t | T > s) = \frac {P (T > s + t)}{P (T > s)} = \frac {e ^ {- (s + t) ^ {1 / 3}}}{e ^ {- s ^ {1 / 3}}},
$$

which is not the same as $P ( T > t ) = e ^ { - t ^ { 1 / 3 } }$ . Thus, $T$ does not have the memoryless property. Nor could it, since it is not Exponential.

(b) Example 6.5.1 shows that the moments of X are given by $E ( X ^ { n } )   =   n !$ . This allows us to find the moments of $T$ without doing any additional work! Specifically,

$$
E (T ^ {n}) = E (X ^ {3 n}) = (3 n)!.
$$

The mean and variance of $T$ are

$$
E (T) = 3! = 6, \mathrm{Var} (T) = 6! - 6 ^ {2} = 6 8 4.
$$

(c) By LOTUS,

$$
E (e ^ {t T}) = E (e ^ {t X ^ {3}}) = \int_ {0} ^ {\infty} e ^ {t x ^ {3} - x} d x.
$$

This integral diverges for $t \; > \; 0$ since the $t x ^ { 3 }$ term dominates over the $x ;$ more precisely, we have $t x ^ { 3 } - x > x$ for all x sufficiently large (specifically, for $x > \sqrt { 2 / t } )$ so this integral diverges by comparison with the divergent integral $\textstyle \int _ { 0 } ^ { \infty } e ^ { x } d x$ . So the MGF of $T$ does not exist, even though all the moments of $T$ do exist. 

h 6.5.6. Several different parameterizations of the Weibull are commonly used, e.g., we are including a scale in the Exponential and then raising to a power, but it is also common to take an Expo(1) to a power and then rescale. So care is needed when reading various references: always check which convention is being used. Our parameterization here is widely used in medical statistics, and is convenient to work with since we are just raising an Expo(λ) r.v. to a power.

## 6.6 Sums of independent r.v.s via MGFs

Since the MGF of a sum of independent r.v.s is just the product of the individual MGFs, we now have a new strategy for finding the distribution of a sum of independent r.v.s: multiply the individual MGFs together and see if the product is recognizable as the MGF of a named distribution. The next two examples illustrate this strategy.

Example 6.6.1 (Sum of independent Poissons). Using MGFs, we can easily show that the sum of independent Poissons is Poisson. First let’s find the MGF of $X \sim$ Pois(λ):

$$
E (e ^ {t X}) = \sum_ {k = 0} ^ {\infty} e ^ {t k} \frac {e ^ {- \lambda} \lambda^ {k}}{k !} = e ^ {- \lambda} \sum_ {k = 0} ^ {\infty} \frac {(\lambda e ^ {t}) ^ {k}}{k !} = e ^ {- \lambda} e ^ {\lambda e ^ {t}} = e ^ {\lambda (e ^ {t} - 1)}.
$$

Now let $Y \sim \mathrm { P o i s } ( \mu )$ be independent of $X$ . The MGF of $X + Y$ is

$$
E (e ^ {t X}) E (e ^ {t Y}) = e ^ {\lambda (e ^ {t} - 1)} e ^ {\mu (e ^ {t} - 1)} = e ^ {(\lambda + \mu) (e ^ {t} - 1)},
$$

which is the $\operatorname { P o i s } ( \lambda   +   \mu )$ MGF. Since the MGF determines the distribution, we have proven that $X + Y \sim \mathrm { P o i s } ( \lambda + \mu )$ . Contrast this with the proof from Chapter 4 (Theorem 4.8.1), which required using the law of total probability and summing over all possible values of X. The proof using MGFs is far less tedious. 

h 6.6.2. It is important that X and Y be independent in the above example. To see why, consider an extreme form of dependence: $X = Y$ . In that case, $X + Y = 2X$ which can’t possibly be Poisson since its value is always an even number!

Example 6.6.3 (Sum of independent Normals). If we have $X _ { 1 } \sim \mathcal { N } ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } )$ and $X _ { 2 } \sim \mathcal { N } ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$ independently, then the MGF of $X _ { 1 } + X _ { 2 }$ is

$$
M _ {X _ {1} + X _ {2}} (t) = M _ {X _ {1}} (t) M _ {X _ {2}} (t) = e ^ {\mu_ {1} t + \frac {1}{2} \sigma_ {1} ^ {2} t ^ {2}} \cdot e ^ {\mu_ {2} t + \frac {1}{2} \sigma_ {2} ^ {2} t ^ {2}} = e ^ {(\mu_ {1} + \mu_ {2}) t + \frac {1}{2} (\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}) t ^ {2}},
$$

which is the $\mathcal { N } ( \mu _ { 1 } + \mu _ { 2 } , \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } )$ MGF. Again, because the MGF determines the distribution, it must be the case that $X _ { 1 } + X _ { 2 } \sim \mathcal { N } ( \mu _ { 1 } + \mu _ { 2 } , \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } )$ . Thus the sum of independent Normals is Normal, and the means and variances simply add. 

Example 6.6.4 (Sum is Normal). A converse to the previous example also holds: if $X _ { 1 }$ and $X _ { 2 }$ are independent and $X _ { 1 } { + } X _ { 2 }$ is Normal, then $X _ { 1 }$ and $X _ { 2 }$ must be Normal! This is known as Cramér’s theorem. Proving this in full generality is difficult, but it becomes much easier if $X _ { 1 }$ and $X _ { 2 }$ are i.i.d. with MGF $M ( t )$ . Without loss of generality, we can assume $X _ { 1 } + X _ { 2 } \sim \mathcal { N } ( 0 , 1 )$ , and then its MGF is

$$
e ^ {t ^ {2} / 2} = E (e ^ {t (X _ {1} + X _ {2})}) = E (e ^ {t X _ {1}}) E (e ^ {t X _ {2}}) = (M (t)) ^ {2},
$$

so $M ( t ) = e ^ { t ^ { 2 } / 4 }$ , which is the $\mathcal { N } ( 0 , 1 / 2 )$ MGF. Thus, $X _ { 1 } , X _ { 2 } \sim \mathcal { N } ( 0 , 1 / 2 )$

In Chapter 8 we’ll discuss a more general technique for finding the distribution of a sum of r.v.s, which applies when the individual MGFs don’t exist, or when the product of the individual MGFs is not recognizable and we would like to get the PMF/PDF instead.

## 6.7 \*Probability generating functions

In this section we discuss probability generating functions, which are similar to MGFs but are guaranteed to exist for nonnegative integer-valued r.v.s. First we’ll use PGFs