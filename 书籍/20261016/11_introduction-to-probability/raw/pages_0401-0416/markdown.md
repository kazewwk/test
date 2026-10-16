posterior distribution after observing k Heads,

$$
\begin{array}{l} f (p | X = k) = \frac {P (X = k | p) f (p)}{P (X = k)} \\ = \frac {\binom {n} {k} p ^ {k} (1 - p) ^ {n - k} \cdot \frac {1}{\beta (a , b)} p ^ {a - 1} (1 - p) ^ {b - 1}}{P (X = k)}. \\ \end{array}
$$

The denominator, which is the marginal PMF of $X$ , is given by

$$
P (X = k) = \int_ {0} ^ {1} P (X = k | p) f (p) d p = \int_ {0} ^ {1} \binom{n}{k} p ^ {k} (1 - p) ^ {n - k} f (p) d p.
$$

For $a = b = 1$ (which gives a Unif(0, 1) prior on $p )$ , we showed in the Bayes’ billiards story that $P(X = k) = 1 / (n + 1)$ , i.e., X is Discrete Uniform on $\{ 0 , 1 , \ldots , n \}$ . For $a$ and $b$ any positive integers, we can again use $\mathrm { B a y e s } ^ { \prime }$ billiards to find $P ( X = k )$ interestingly, $X$ then turns out to have a Negative Hypergeometric distribution (the story and PMF of which we saw in Example 4.4.7).

But it does not seem easy to find $P ( X = k )$ in general for real $a , b .$ Relatedly, we still have not evaluated $\beta ( a , b )$ in general. Are we stuck?

Actually, the calculation is much easier than it appears at first. The conditional PDF $f ( p | X = k )$ is a function of $p ,$ which means everything that doesn’t depend on $p$ is just a constant. We can drop all these constants and find the PDF up to a multiplicative constant (and then the normalizing constant is whatever it needs to be to make the PDF integrate to 1). This gives

$$
f (p | X = k) \propto p ^ {a + k - 1} (1 - p) ^ {b + n - k - 1},
$$

which is the Beta $( a + k , b + n - k )$ PDF, up to a multiplicative constant. Therefore, the posterior distribution of $p$ is

$$
p | X = k \sim \mathrm{Beta} (a + k, b + n - k).
$$

The posterior distribution of $p$ after observing $X = k$ is still a Beta distribution! This is a special relationship between the Beta and Binomial distributions called conjugacy: if we have a Beta prior distribution on $p$ and data that are conditionally Binomial given $p ,$ then when going from prior to posterior, we don’t leave the family of Beta distributions. We say that the Beta is the conjugate prior of the Binomial.

Furthermore, notice the very simple formula for updating the distribution of $p .$ We just add the number of observed successes, $k ,$ to the first parameter of the Beta distribution, and the number of observed failures, $n - k .$ to the second parameter. So $a$ and $b$ have a concrete interpretation in this context, at least when $a$ and $b$ are positive integers: think of $a - 1$ as the number of prior successes and $b - 1$ as the number of prior failures in earlier experiments (these prior experiments could be real or imagined). Adding on $k$ successes and $n - k$ failures from the current experiment, we have $a   +   k   -   1$ successes and $b   +   n   -   k   -   1$ failures, and the $\mathrm { B e t a } ( a , b )$ prior gets updated to a Beta $( a + k , b + n - k )$ posterior.

As in Section 2.6, we can sequentially update our beliefs as we get more and more evidence: we start with a prior distribution and update it to get a posterior distribution, which becomes the new prior distribution, which we update to get a new posterior distribution, etc. The beauty here is that all of this can be done within the Beta family of distributions, with easy updates to the parameters based on tallying the observed successes and failures.

For concreteness, Figure 8.6 shows the case where the prior is $\mathrm { B e t a } ( 1 , 1 )$ (which is equivalent to $\mathrm { U n i f } ( 0 , 1 )$ , as noted earlier), and we observe $n = 5$ coin tosses, all of which happen to land Heads. Then the posterior is Beta(6, 1), which is plotted on the right half of Figure 8.6. Notice how the posterior distribution incorporates the evidence from the coin tosses: larger values of $p$ have higher density, consistent with the fact that we observed all Heads.

![](images/page_401_image_5.jpg)

## FIGURE 8.6

Beta is conjugate prior of Binomial. Left: prior is Unif(0, 1). Right: after observing 5 Heads in 5 tosses, posterior is Beta(6, 1).

This model is a continuous analog of Example 2.3.7, our very first example of $\mathrm { B a y e s } ^ { \prime }$ rule. In that example, we also had a coin whose probability of Heads $p$ was unknown, but our prior information led us to believe that $p$ could only take on one of two possible values, $1 / 2$ or $3 / 4$ . For this reason, our prior distribution on $p -$ though we didn’t call it that at the time!—was discrete. In particular, our prior PMF was

$$
P (p = 1 / 2) = 1 / 2,
$$

$$
P (p = 3 / 4) = 1 / 2.
$$

After observing three Heads in a row, we updated this PMF to obtain the posterior PMF, which assigned a probability of 0.23 to $p   =   1 / 2$ and a probability of 0.77 to $p = 3 / 4$ . The same logic applies to the example in this chapter, except that we now give $p$ a continuous prior distribution, which is appropriate if we believe that $p$ could possibly take on any value between 0 and 1. 

To conclude the section, here are two examples that illustrate how Beta-Binomial conjugacy and Bayes’ billiards can make some seemingly complicated problems much easier.

Example 8.3.4 (Bayes’ serum). A new treatment, Bayes’ serum, has just been developed for the disease conditionitis. A clinical trial is about to be conducted, to study how effective the treatment is. Bayes’ serum will be applied to n patients who have conditionitis. Given $p ,$ the patients’ outcomes are independent, with each patient having probability $p$ of being cured by the treatment. But $p$ is unknown. To quantify our uncertainty about $p ,$ we model $p$ as a random variable, with prior distribution $p \sim \mathrm { U n i f } ( 0 , 1 )$

(a) Find the probability that exactly k out of the n patients will be cured by the treatment (unconditionally, not given p).

(b) Now suppose that the treatment is extremely effective in the clinical trial: all n patients are cured! Given this information, find the probability that $p$ exceeds $1 / 2$ Your answer should be fully simplified, and expressed only in terms of $n .$

## Solution:

(a) By LOTP followed by Bayes’ billiards or pattern-matching to a Beta PDF, the probability is

$$
\int_ {0} ^ {1} \binom{n}{k} p ^ {k} (1 - p) ^ {n - k} d p = \frac {1}{n + 1}.
$$

(b) $\mathrm { B y }$ Beta-Binomial conjugacy, the posterior distribution of $p$ given the data is Beta $\l _ { \cdot } ( 1 + n , 1 )$ , which has PDF $( n + 1 ) p ^ { n }$ for $0 < p < 1$ . Thus,

$$
P \left(p > \frac {1}{2}\right) = \int_ {1 / 2} ^ {1} (n + 1) p ^ {n} d p = p ^ {n + 1} \Big | _ {1 / 2} ^ {1} = 1 - \frac {1}{2 ^ {n + 1}}.
$$

Example 8.3.5. A basketball player will shoot $N \; \sim \; \mathrm { P o i s } ( \lambda )$ free throws in a game tomorrow. Let $X _ { j }$ be the indicator of her making their jth free throw, and $X = X _ { 1 } + \cdots + X _ { N }$ be the total number of free throws she makes in the game (so $\overline { { X } } = 0 \; \mathrm { i f } \; N = 0 )$ To model our uncertainty about how good a free throw shooter she is, let $p \sim \mathrm { B e t a } ( a , b )$ . Given $p ,$ the player has probability $p$ of making a free throw and probability $q = 1 - p$ of missing it. Assume that $X _ { 1 } , X _ { 2 } , \ldots$ are conditionally independent given $p ,$ and that N is independent of $p , X _ { 1 } , X _ { 2 } , \ldots .$

(a) Find the conditional distribution of X given $N , p .$
(b) Find the conditional distribution of X given $p .$
(c) Find the conditional distribution of X given N, for the case $a = b = 1$
(d) Find the conditional distribution of p given X, N.

Solution:

(a) By the story of the Binomial, $X | ( N , p ) \sim \mathrm { B i n } ( N , p )$
(b) By the chicken-egg story, $X | p \sim \mathrm { P o i s } ( \lambda p )$
(c) For $k = 0 , 1 , \ldots , n$ , by LOTP and Bayes’ billiards we have

$$
P (X = k | N = n) = \int_ {0} ^ {1} \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} d p = \frac {1}{n + 1}.
$$

So the conditional distribution of X given N is Discrete Uniform on $\{ 0 , 1 , \ldots , N \}$

(d) By Beta-Binomial conjugacy, $p | ( X , N ) \sim \mathrm { B e t a } ( a + X , b + N - X )$

## 8.4 Gamma

The Gamma distribution is a continuous distribution on the positive real line; it is a generalization of the Exponential distribution. While an Exponential r.v. represents the waiting time for the first success under conditions of memorylessness, we shall see that a Gamma r.v. represents the total waiting time for multiple successes.

Before writing down the PDF, we first introduce the gamma function, a very famous function in mathematics that extends the factorial function beyond the realm of nonnegative integers.

Definition 8.4.1 (Gamma function). The gamma function Γ is defined by

$$
\Gamma (a) = \int_ {0} ^ {\infty} x ^ {a} e ^ {- x} \frac {d x}{x},
$$

for real numbers $a > 0$

We could also cancel an x and write the integrand as $x ^ { a - 1 } e ^ { - x }$ , but it turns out to be convenient having the $\frac { d x } { x }$ since it is common to make a transformation of the form $u = c x$ , and then we have the handy fact that $\begin{array} { r } { \frac { d u } { u }   =   \frac { d x } { x } } \end{array}$ . Here are two important properties of the gamma function.

$\Gamma ( a + 1 ) = a \Gamma ( a )$ for all $a > 0$ . This follows from integration by parts:

$$
\Gamma (a + 1) = \int_ {0} ^ {\infty} x ^ {a} e ^ {- x} d x = - x ^ {a} e ^ {- x} \bigg | _ {0} ^ {\infty} + a \int_ {0} ^ {\infty} x ^ {a - 1} e ^ {- x} d x = 0 + a \Gamma (a).
$$

$\Gamma ( n ) = ( n - 1 ) ! { \mathrm { ~ i f ~ } } n$ is a positive integer. This can be proved by induction, starting with $n = 1$ and using the recursive relation $\Gamma ( a   +   1 ) = a \Gamma ( a )$ . Thus, if we evaluate the gamma function at positive integer values, we recover the factorial function (albeit shifted by 1).

Now let’s suppose that on a whim, we decide to divide both sides of the above definition by $\Gamma ( a )$ . We have

$$
1 = \int_ {0} ^ {\infty} \frac {1}{\Gamma (a)} x ^ {a} e ^ {- x} \frac {d x}{x},
$$

so the function under the integral is a valid PDF supported on $( 0 , \infty )$ . This is the definition of the PDF of the Gamma distribution. Specifically, we say that X has the Gamma distribution with parameters a and 1, denoted $X \sim \mathrm { G a m m a } ( a , 1 )$ , if its PDF is

$$
f _ {X} (x) = \frac {1}{\Gamma (a)} x ^ {a} e ^ {- x} \frac {1}{x}, \quad x > 0.
$$

From the $\mathrm { G a m m a } ( a , 1 )$ distribution, we obtain the general Gamma distribution by a scale transformation: if $X \sim \mathrm { G a m m a } ( a , 1 )$ and $\lambda > 0$ , then the distribution of $Y = X / \lambda$ is called the Gamma $( a , \lambda )$ distribution. By the change of variables formula with $x = \lambda y$ and $d x / d y = \lambda$ , the PDF of Y is

$$
f _ {Y} (y) = f _ {X} (x) \left| \frac {d x}{d y} \right| = \frac {1}{\Gamma (a)} (\lambda y) ^ {a} e ^ {- \lambda y} \frac {1}{\lambda y} \lambda = \frac {1}{\Gamma (a)} (\lambda y) ^ {a} e ^ {- \lambda y} \frac {1}{y}, \quad y > 0.
$$

This is summarized in the following definition.

Definition 8.4.2 (Gamma distribution). An r.v. Y is said to have the Gamma distribution with parameters a and λ, where $a > 0$ and $\lambda > 0$ , if its PDF is

$$
f (y) = \frac {1}{\Gamma (a)} (\lambda y) ^ {a} e ^ {- \lambda y} \frac {1}{y}, \quad y > 0.
$$

We write $Y \sim  Gamma (a, \lambda)$

Taking $a = 1$ , the Gamma(1, λ) PDF is $f(y) = \lambda e^{-\lambda y}$ for $y > 0$ , so the Gamma $( 1 , \lambda )$ and $\operatorname { E x p o } ( \lambda )$ distributions are the same. The extra parameter a allows Gamma PDFs to have a greater variety of shapes. Figure 8.7 shows four Gamma PDFs. For small values of $a ,$ the PDF is skewed, but as a increases, the PDF starts to look more symmetrical and bell-shaped; we will learn the reason for this in Chapter 10. Increasing λ compresses the PDF toward smaller values, as we can see by comparing the Gamma(3, 1) and Gamma(3, 0.5) PDFs.

Let’s find the mean, variance, and other moments of the Gamma distribution, starting with $X \sim \mathrm { G a m m a } ( a , 1 )$ . We’ll use properties of the gamma function as well as the technique of doing integrals by pattern recognition. For the mean, we write down the definition of $E ( X )$

$$
E (X) = \int_ {0} ^ {\infty} \frac {1}{\Gamma (a)} x ^ {a + 1} e ^ {- x} \frac {d x}{x},
$$

but instead of attempting a gruesome integration by parts, we recognize that after taking out $1 / \Gamma ( a )$ , what’s left is precisely the gamma function evaluated at $a + 1$ Therefore

$$
E (X) = \frac {\Gamma (a + 1)}{\Gamma (a)} = \frac {a \Gamma (a)}{\Gamma (a)} = a.
$$

![](images/page_405_image_2.jpg)

FIGURE 8.7

Gamma PDFs for various values of a and λ. Clockwise from top left: Gamma(3, 1), Gamma(3, 0.5), Gamma(5, 0.5), Gamma(10, 1).

Similarly, for the variance, LOTUS gives us an integral expression for the second moment,

$$
E (X ^ {2}) = \int_ {0} ^ {\infty} \frac {1}{\Gamma (a)} x ^ {a + 2} e ^ {- x} \frac {d x}{x},
$$

and we recognize the gamma function evaluated at $a + 2$ . Therefore

$$
E (X ^ {2}) = \frac {\Gamma (a + 2)}{\Gamma (a)} = \frac {(a + 1) a \Gamma (a)}{\Gamma (a)} = (a + 1) a
$$

and

$$
\mathrm{Var} (X) = (a + 1) a - a ^ {2} = a.
$$

So for $X \sim \operatorname { G a m m a } ( a , 1 ) ,   E ( X ) = \operatorname { V a r } ( X ) = a .$

The cth moment is no harder than the second moment; we just use LOTUS and recognize the definition of $\Gamma ( a + c )$ . This gives

$$
E (X ^ {c}) = \int_ {0} ^ {\infty} \frac {1}{\Gamma (a)} x ^ {a + c} e ^ {- x} \frac {d x}{x} = \frac {\Gamma (a + c)}{\Gamma (a)}
$$

for all real c such that the integral converges, i.e., for $c > - a$

We can now transform to $Y = X / \lambda \sim  Gamma (a, \lambda)$ to get

$$
E (Y) = \frac {1}{\lambda} E (X) = \frac {a}{\lambda},
$$

$$
\mathrm{Var} (Y) = \frac {1}{\lambda^ {2}} \mathrm{Var} (X) = \frac {a}{\lambda^ {2}},
$$

$$
E (Y ^ {c}) = \frac {1}{\lambda^ {c}} E (X ^ {c}) = \frac {1}{\lambda^ {c}} \cdot \frac {\Gamma (a + c)}{\Gamma (a)}, \quad c > - a.
$$

Looking back at the Gamma PDF plots, they are consistent with our finding that the mean and variance are increasing in a and decreasing in λ.

So far, we’ve been learning about the Gamma distribution using the PDF, which allowed us to discern general patterns from PDF plots and to derive the mean and variance. But the PDF doesn’t provide much insight about why we’d ever use the Gamma distribution, and it doesn’t give us much of an interpretation for the parameters a and λ. For this, we need to connect the Gamma to other named distributions through stories. The rest of this section is devoted to stories for the Gamma distribution.

In the special case where a is an integer, we can represent a Gamma $( a , \lambda )$ r.v. as a sum (convolution) of i.i.d. Expo(λ) r.v.s.

Theorem 8.4.3. Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d. Expo(λ). Then

$$
X _ {1} + \dots + X _ {n} \sim \operatorname{Gamma} (n, \lambda).
$$

Proof. The Expo(λ) MGF is $\frac { \lambda } { \lambda - t }$ for $t < \lambda$ , so the MGF of $X _ { 1 } + \dots + X _ { n }$ is

$$
M _ {n} (t) = \left(\frac {\lambda}{\lambda - t}\right) ^ {n}
$$

for $t < \lambda$ . Let $Y \sim  Gamma (n,\lambda)$ ; we’ll show that the MGF of $Y$ is the same as that of $X _ { 1 } + \dots + X _ { n }$ . By LOTUS,

$$
E (e ^ {t Y}) = \int_ {0} ^ {\infty} e ^ {t y} \frac {1}{\Gamma (n)} (\lambda y) ^ {n} e ^ {- \lambda y} \frac {d y}{y}.
$$

Again, we’ll use pattern recognition to do the integral. We just need to do algebraic manipulations until what’s left inside the integral is a recognizable Gamma PDF:

$$
\begin{array}{l} E (e ^ {t Y}) = \int_ {0} ^ {\infty} e ^ {t y} \frac {1}{\Gamma (n)} (\lambda y) ^ {n} e ^ {- \lambda y} \frac {d y}{y} \\ = \frac {\lambda^ {n}}{(\lambda - t) ^ {n}} \int_ {0} ^ {\infty} \frac {1}{\Gamma (n)} e ^ {- (\lambda - t) y} ((\lambda - t) y) ^ {n} \frac {d y}{y}. \\ \end{array}
$$

We pulled $\lambda ^ { n }$ out of the integral, then multiplied by $( \lambda   -   t ) ^ { n }$ on the inside while dividing by it on the outside. Now the expression inside the integral is the $Gamma (n,\lambda {-} t)$ PDF, assuming $t < \lambda$ . Since PDFs integrate to 1, we have

$$
E (e ^ {t Y}) = \left(\frac {\lambda}{\lambda - t}\right) ^ {n}
$$

for $t < \lambda;   if   t \geq \lambda$ the integral fails to converge.

We have shown that $X _ { 1 } + \dots + X _ { n }$ and $Y \sim  Gamma (n, \lambda)$ have the same MGF. Since the MGF determines the distribution, $X _ { 1 } + \cdots + X _ { n } \sim \operatorname { G a m m a } ( n , \lambda )$

Alternatively, we can compute the convolution integral inductively. It suffices to consider the case $\lambda = 1$ , since after having done that case we can rescale the r.v.s to prove the result for general λ. Let $T _ { n } = X _ { 1 } + \cdots + X _ { n }$ . We will show by induction that $T _ { n } \sim \mathrm { G a m m a } ( n , 1 )$ for all $n \geq 1$ . For $n = 1$ , this is true since the Gamma $( 1 , 1 )$ PDF is $e ^ { - x }$ (for $x \; > \; 0 )$ , which is the same as the Expo(1) PDF. Now assume that $T _ { n }   \sim   \mathrm { G a m m a } ( n , 1 )$ , and show that $T _ { n + 1 } \sim$ Gamma $( n + 1 , 1 )$ . The PDF of $T _ { n + 1 } = T _ { n } + X _ { n + 1 }$ is given by the convolution integral

$$
\int_ {0} ^ {\infty} f _ {T _ {n}} (x) f _ {X _ {n + 1}} (t - x) d x = \frac {1}{\Gamma (n)} \int_ {0} ^ {t} x ^ {n - 1} e ^ {- x} e ^ {- (t - x)} d x = \frac {e ^ {- t}}{\Gamma (n)} \int_ {0} ^ {t} x ^ {n - 1} d x = \frac {t ^ {n} e ^ {- t}}{\Gamma (n + 1)}
$$

for $t > 0$ , which completes the induction.

Thus, if $Y   \sim    Gamma (a, \lambda)$ with a an integer, we can represent $Y$ as a sum of i.i.d. $\operatorname { E x p o } ( \lambda ) { \mathrm { ~ r . v . s . , ~ } } X _ { 1 } + \cdots + X _ { a }$ , and get the mean and variance right away:

$$
\begin{array}{l} E (Y) = E (X _ {1} + \dots + X _ {a}) = a E (X _ {1}) = \frac {a}{\lambda}, \\ \mathrm{Var} (Y) = \mathrm{Var} (X _ {1} + \dots + X _ {a}) = a \mathrm{Var} (X _ {1}) = \frac {a}{\lambda^ {2}}, \\ \end{array}
$$

in agreement with the results we derived earlier for general a.

Theorem 8.4.3 also allows us to connect the Gamma distribution to the story of the Poisson process. We showed in Chapter 5 that in a Poisson process of rate λ, the interarrival times are i.i.d. Expo(λ) r.v.s. But the total waiting time $T _ { n }$ for the nth arrival is the sum of the first n interarrival times; for instance, Figure 8.8 illustrates how $T _ { 3 }$ is the sum of the 3 interarrival times $X _ { 1 } , X _ { 2 } , X _ { 3 }$ . Therefore, by the theorem, $T _ { n }   \sim   \mathrm { G a m m a } ( n , \lambda )$ . The interarrival times in a Poisson process are Exponential r.v.s, while the raw arrival times are Gamma r.v.s.

![](images/page_408_image_4.jpg)

<details>
<summary>text_image</summary>

0
X₁ T₁ T₂ T₃ ... T₄ T₅
</details>

## FIGURE 8.8

Poisson process. The interarrival times $X _ { j }$ are i.i.d. Expo(λ), while the raw arrival times $T _ { j }$ are Gamma(j, λ).

h 8.4.4. Unlike the $X _ { j }$ , the $T _ { j }$ are not independent, since they are constrained to be increasing; nor are they identically distributed.

At last, we have an interpretation for the parameters of the Gamma $( a , \lambda )$ distribution. In the Poisson process story, a is the number of successes we are waiting for, and λ is the rate at which successes arrive; $Y \sim  Gamma (a, \lambda)$ is the total waiting time for the ath arrival in a Poisson process of rate λ.

A consequence of this story is that a convolution of Gammas with the same λ is still Gamma. Exercise 29 explores this fact from several perspectives.

When we introduced the Exponential distribution, we viewed it as the continuous analog of the Geometric distribution: the Geometric waits for the first success in discrete time, and the Exponential waits for the first success in continuous time. Likewise, we can now say that the Gamma distribution is the continuous analog of the Negative Binomial distribution: the Negative Binomial is a sum of Geometric waiting times, and the Gamma is a sum of Exponential waiting times. In Exercise 54 you will use MGFs to show that the Gamma distribution can be obtained as a continuous limit of the Negative Binomial distribution.

A final story about the Gamma is that it shares the same special relationship with the Poisson that the Beta shares with the Binomial: the Gamma is the conjugate prior of the Poisson. Earlier we saw that the Beta distribution can represent an unknown probability of success because its support is (0, 1). The Gamma distribution, on the other hand, can represent an unknown rate in a Poisson process because its support is (0, ∞).

To investigate, we’ll return to Blotchville, where buses arrive in a Poisson process of rate λ. Previously it was assumed that $\lambda = 1 / 1 0$ , so that the times between buses were i.i.d. Exponentials with mean 10 minutes, but now we’ll assume Fred doesn’t know the rate λ at which buses arrive and needs to figure it out. Fred will follow the Bayesian approach and treat the unknown rate as a random variable.

Story 8.4.5 (Gamma-Poisson conjugacy). In Blotchville, buses arrive at a certain bus stop according to a Poisson process with rate λ buses per hour, where λ is unknown. Based on his very memorable adventures in Blotchville, Fred quantifies his uncertainty about λ using the prior $\lambda   \sim   \mathrm { G a m m a } ( r _ { 0 } , b _ { 0 } )$ , where $r _ { 0 }$ and $b _ { 0 }$ are known, positive constants with $r _ { 0 }$ an integer.

To better understand the bus system, Fred wants to learn more about λ. He is a very patient person, and decides that he will sit at the bus stop for t hours and count how many buses arrive in this time interval. Let Y be the number of buses in this time interval, and suppose Fred observes that $Y = y$

(a) Find Fred’s hybrid joint distribution for Y and λ.
(b) Find Fred’s marginal distribution for $Y .$
(c) Find Fred’s posterior distribution for λ, i.e., his conditional distribution of λ given the data y.
(d) Find Fred’s posterior mean $E ( \lambda | Y = y )$ and posterior variance $\operatorname { V a r } ( \lambda | Y = y )$

Solution: Notice the similarities between the structure of this problem and that of the hybrid joint distribution from Example 7.1.26. We know that $\lambda \sim \mathrm { G a m m a } ( r _ { 0 } , b _ { 0 } )$ marginally, and by definition of Poisson process, conditional on knowing the true rate $\lambda ,$ the number of buses in an interval of length t is distributed Pois(λt). In other words, what we’re given is

$$
\begin{array}{l} \lambda \sim \mathrm{Gamma} (r _ {0}, b _ {0}) \\ Y | \lambda \sim \mathrm{Pois} (\lambda t). \\ \end{array}
$$

Then we are asked to flip it around: find the marginal distribution of Y and the conditional distribution of λ given $Y = y$ , which is the posterior distribution. This is characteristic of Bayesian inference: we have a prior distribution for the unknown parameters (in this case, a Gamma distribution for λ) and a model for the data conditional on the unknown parameters (in this case, a Poisson distribution for Y given λ), and we use Bayes’ rule to get the distribution of the unknowns conditional on the observed data. So let’s get started.

(a) Let $f _ { 0 }$ be the prior PDF of λ. The hybrid joint distribution of $Y$ and λ is

$$
f (y, \lambda) = P (Y = y | \lambda) f _ {0} (\lambda) = \frac {e ^ {- \lambda t} (\lambda t) ^ {y}}{y !} \frac {(b _ {0} \lambda) ^ {r _ {0}} e ^ {- b _ {0} \lambda}}{\lambda \Gamma (r _ {0})},
$$

for $y = 0 , 1 , 2 , \ldots$ . and $\lambda > 0$ . The hybrid joint distribution is plotted in Figure 8.9;

![](images/page_410_image_2.jpg)

## FIGURE 8.9

Hybrid joint distribution of Y and λ. (a) Conditioning on a particular value of $\lambda ,$ the relative heights form a Poisson PMF. (b) In the other direction, conditioning on $Y = y$ gives the posterior distribution of λ.

there is a conditional PMF of Y for every value of λ and a conditional PDF of λ for every value of $Y$

(b) To get the marginal PMF of $Y .$ , we integrate out λ from the hybrid joint distribution; this is also a form of LOTP. This gives

$$
\begin{array}{l} P (Y = y) = \int_ {0} ^ {\infty} P (Y = y | \lambda) f _ {0} (\lambda) d \lambda \\ = \int_ {0} ^ {\infty} \frac {e ^ {- \lambda t} (\lambda t) ^ {y}}{y !} \frac {(b _ {0} \lambda) ^ {r _ {0}} e ^ {- b _ {0} \lambda}}{\Gamma (r _ {0})} \frac {d \lambda}{\lambda}. \\ \end{array}
$$

Let’s do the integral by pattern recognition, focusing in on the terms involving λ. We spot $\lambda ^ { r _ { 0 } + y }$ and $e ^ { - ( b _ { 0 } + t ) \lambda }$ lurking in the integrand, which suggests patternmatching to a Gamma $( r _ { 0 }   +   y , b _ { 0 }   +   t )$ PDF. Pull out all the terms that don’t depend on λ, then multiply by whatever it takes to get the desired PDF inside the integral, remembering to multiply by the reciprocal on the outside:

$$
\begin{array}{l} P (Y = y) = \frac {t ^ {y} b _ {0} ^ {r _ {0}}}{y ! \Gamma (r _ {0})} \int_ {0} ^ {\infty} e ^ {- (b _ {0} + t) \lambda} \lambda^ {r _ {0} + y} \frac {d \lambda}{\lambda} \\ = \frac {\Gamma (r _ {0} + y)}{y ! \Gamma (r _ {0})} \frac {t ^ {y} b _ {0} ^ {r _ {0}}}{(b _ {0} + t) ^ {r _ {0} + y}} \int_ {0} ^ {\infty} \frac {1}{\Gamma (r _ {0} + y)} e ^ {- (b _ {0} + t) \lambda} ((b _ {0} + t) \lambda) ^ {r _ {0} + y} \frac {d \lambda}{\lambda} \\ = \frac {(r _ {0} + y - 1) !}{(r _ {0} - 1) ! y !} \left(\frac {t}{b _ {0} + t}\right) ^ {y} \left(\frac {b _ {0}}{b _ {0} + t}\right) ^ {r _ {0}}. \\ \end{array}
$$

In the last step, we used the property $\Gamma ( n ) = ( n - 1 ) !$ , which is applicable because $r _ { 0 }$ is an integer. This is the NBin $( r _ { 0 } , b _ { 0 } / ( b _ { 0 } + t ) )$ PMF, so the marginal distribution of $Y$ is Negative Binomial with parameters $r _ { 0 }$ and $b _ { 0 } / ( b _ { 0 } + t )$

(c) By Bayes’ rule, the posterior PDF of λ is given by

$$
f _ {1} (\lambda | y) = \frac {P (Y = y | \lambda) f _ {0} (\lambda)}{P (Y = y)}.
$$

We found $P ( Y = y )$ in the previous part, but since it does not depend on $\lambda ,$ we can just treat it as part of the normalizing constant. Absorbing this and other multiplicative factors that don’t depend on λ into the normalizing constant,

$$
f _ {1} (\lambda | y) \propto e ^ {- \lambda t} \lambda^ {y} \lambda^ {r _ {0}} e ^ {- b _ {0} \lambda} \frac {1}{\lambda} = e ^ {- (b _ {0} + t) \lambda} \lambda^ {r _ {0} + y} \frac {1}{\lambda},
$$

which shows that the posterior distribution of $\lambda$ is $\operatorname { G a m m a } ( r _ { 0 } + y , b _ { 0 } + t )$

When going from prior to posterior, the distribution of $\lambda$ stays in the Gamma family, so the Gamma is indeed the conjugate prior for the Poisson.

Now that we have the posterior PDF of $\lambda ,$ we have a more elegant approach to solving (b). Rearranging Bayes’ rule, the marginal PMF of $Y$ is

$$
P (Y = y) = \frac {P (Y = y | \lambda) f _ {0} (\lambda)}{f _ {1} (\lambda | y)},
$$

where we know the numerator from the statement of the problem and the denominator from the calculation we just did. Plugging in these ingredients and simplifying again yields

$$
Y \sim \mathrm{NBin} (r _ {0}, b _ {0} / (b _ {0} + t)).
$$

(d) Since conditional PDFs are PDFs, it is perfectly fine to calculate the expectation and variance of $\lambda$ with respect to the posterior distribution. The mean and variance of the Gamma $. ( r _ { 0 } + y , b _ { 0 } + t )$ distribution give us

$$
E (\lambda | Y = y) = \frac {r _ {0} + y}{b _ {0} + t} \quad \text {and} \quad \operatorname{Var} (\lambda | Y = y) = \frac {r _ {0} + y}{(b _ {0} + t) ^ {2}}.
$$

This example gives another interpretation for the parameters in a Gamma when it is being used as a conjugate prior. Fred’s $\operatorname { G a m m a } ( r _ { 0 } , b _ { 0 } )$ prior got updated to a Gamma $( r _ { 0 }   +   y , b _ { 0 }   +   t )$ posterior after observing y arrivals in t hours. We can imagine that in the past, Fred observed $r _ { 0 }$ buses arrive in $b _ { 0 }$ hours; then after the new data, he has observed $r _ { 0 } + y$ buses in $b _ { 0 } + t$ hours. So we can interpret $r _ { 0 }$ as the number of prior arrivals and $b _ { 0 }$ as the total time required for those prior arrivals. 

## 8.5 Beta-Gamma connections

In this section, we will unite the Beta and Gamma distributions with a common story. As an added bonus, the story will give us an expression for the normalizing constant of the Beta $( a , b )$ PDF in terms of gamma functions, and it will allow us to easily find the expectation of the Beta $( a , b )$ distribution.

Story 8.5.1 (Bank–post office). While running errands, you need to go to the bank, then to the post office. Let $X \sim  Gamma (a, \lambda)$ be your waiting time in line at the bank, and let $Y   \sim    Gamma (b, \lambda)$ be your waiting time in line at the post office (with the same λ for both). Assume X and $Y$ are independent. What is the joint distribution of $T = X + Y$ (your total wait at the bank and post office) and $\begin{array} { r } { W = \frac { X } { X + Y } } \end{array}$ (the fraction of your waiting time spent at the bank)?

Solution:

We’ll do a change of variables in two dimensions to get the joint PDF of $T$ and $W$ Let $\begin{array} { r } { t = x + y ,   w = \frac { x } { x + y } } \end{array}$ . Then $x = t w , y = t ( 1 - w )$ , and

$$
\frac {\partial (x , y)}{\partial (t , w)} = \left( \begin{array}{c c} w & t \\ 1 - w & - t \end{array} \right),
$$

which has an absolute determinant of t. Therefore

$$
\begin{array}{l} f _ {T, W} (t, w) = f _ {X, Y} (x, y) \cdot | \left| \frac {\partial (x , y)}{\partial (t , w)} \right| | \\ = f _ {X} (x) f _ {Y} (y) \cdot t \\ = \frac {1}{\Gamma (a)} (\lambda x) ^ {a} e ^ {- \lambda x} \frac {1}{x} \cdot \frac {1}{\Gamma (b)} (\lambda y) ^ {b} e ^ {- \lambda y} \frac {1}{y} \cdot t \\ = \frac {1}{\Gamma (a)} (\lambda t w) ^ {a} e ^ {- \lambda t w} \frac {1}{t w} \cdot \frac {1}{\Gamma (b)} (\lambda t (1 - w)) ^ {b} e ^ {- \lambda t (1 - w)} \frac {1}{t (1 - w)} \cdot t. \\ \end{array}
$$

Let’s group all the terms involving w together, and all the terms involving t together:

$$
\begin{array}{l} f _ {T, W} (t, w) = \frac {1}{\Gamma (a) \Gamma (b)} w ^ {a - 1} (1 - w) ^ {b - 1} (\lambda t) ^ {a + b} e ^ {- \lambda t} \frac {1}{t} \\ = \left(\frac {\Gamma (a + b)}{\Gamma (a) \Gamma (b)} w ^ {a - 1} (1 - w) ^ {b - 1}\right) \left(\frac {1}{\Gamma (a + b)} (\lambda t) ^ {a + b} e ^ {- \lambda t} \frac {1}{t}\right), \\ \end{array}
$$

for $0   <   w   <   1$ and $t \; > \; 0$ . The form of the joint PDF, together with Proposition 7.1.21, tells us several things:

1. Since the joint PDF factors into a function of t times a function of $w ,$ we have that T and W are independent: the total waiting time is independent of the fraction of time spent at the bank.
2. We recognize the marginal PDF of T and deduce that $T \sim  Gamma (a + b, \lambda)$
3. The PDF of W is

$$
f _ {W} (w) = \frac {\Gamma (a + b)}{\Gamma (a) \Gamma (b)} w ^ {a - 1} (1 - w) ^ {b - 1}, \quad 0 <   w <   1,
$$

by Proposition 7.1.21 or just by integrating out $T$ from the joint PDF of $T$ and $W$ . This PDF is proportional to the $\mathrm { B e t a } ( a , b )$ PDF, so it is the $\mathrm { B e t a } ( a , b )$ PDF! Note that as a byproduct of the calculation we have just done, we have found the normalizing constant of the Beta distribution:

$$
\frac {1}{\beta (a , b)} = \frac {\Gamma (a + b)}{\Gamma (a) \Gamma (b)}
$$

is the constant that goes in front of the Beta(a, b) PDF.

To summarize, the bank–post office story tells us that when we add independent Gamma r.v.s X and Y with the same rate λ, the total $X   +   Y$ has a Gamma distribution, the fraction $X / ( X + Y )$ has a Beta distribution, and the total is independent of the fraction.

We can use this result to find the mean of $W   \sim   \mathrm { B e t a } ( a , b )$ without the slightest trace of calculus.

Example 8.5.2 (Beta expectation). With notation as above, note that since $T$ and $W$ are independent, they are uncorrelated: $E ( T W ) = E ( T ) E ( W )$ . Writing this in terms of X and Y , we have

$$
\begin{array}{l} E \left((X + Y) \cdot \frac {X}{X + Y}\right) = E (X + Y) E \left(\frac {X}{X + Y}\right), \\ E (X) = E (X + Y) E \left(\frac {X}{X + Y}\right), \\ \frac {E (X)}{E (X + Y)} = E \left(\frac {X}{X + Y}\right). \\ \end{array}
$$

Ordinarily, the last equality would be a horrendous blunder: faced with an expectation like $E ( X / ( X + Y ) )$ , we are not generally permitted to move the E into the numerator and denominator as we please. In this case, however, the bank–post office story justifies the move, so finding the expectation of $W$ happily reduces to finding the expectations of $X$ and $X + Y$

$$
E (W) = E \left(\frac {X}{X + Y}\right) = \frac {E (X)}{E (X + Y)} = \frac {a / \lambda}{a / \lambda + b / \lambda} = \frac {a}{a + b}.
$$

Another approach is to proceed from the definition of expectation:

$$
E (W) = \int_ {0} ^ {1} \frac {\Gamma (a + b)}{\Gamma (a) \Gamma (b)} w ^ {a} (1 - w) ^ {b - 1} d w.
$$

By pattern recognition, the integrand is a $\mathrm { B e t a } ( a + 1 , b )$ PDF, up to a normalizing constant. After obtaining an exact match for the PDF, we apply properties of the gamma function:

$$
\begin{array}{l} E (W) = \frac {\Gamma (a + b)}{\Gamma (a)} \frac {\Gamma (a + 1)}{\Gamma (a + b + 1)} \int_ {0} ^ {1} \frac {\Gamma (a + b + 1)}{\Gamma (a + 1) \Gamma (b)} w ^ {a} (1 - w) ^ {b - 1} d w \\ = \frac {\Gamma (a + b)}{\Gamma (a)} \frac {a \Gamma (a)}{(a + b) \Gamma (a + b)} \\ = \frac {a}{a + b}. \\ \end{array}
$$

In Exercise 30, you will use this approach to find the variance and the other moments of the Beta distribution. 

Now that we know the Beta normalizing constant, we can also quickly obtain the PMF of the Beta-Binomial distribution.

Example 8.5.3 (Beta-Binomial PMF). Let $X | p \sim \operatorname { B i n } ( n , p )$ , with $p \sim \mathrm { B e t a } ( a , b )$ As mentioned in Story 8.3.3, X has a Beta-Binomial distribution. Find the marginal distribution of X.

Solution: Let $f ( p )$ be the Beta $( a , b )$ PDF. Then

$$
\begin{array}{l} P (X = k) = \int_ {0} ^ {1} P (X = k | p) f (p) d p \\ = \frac {1}{\beta (a , b)} \int_ {0} ^ {1} \binom{n}{k} p ^ {k} (1 - p) ^ {n - k} p ^ {a - 1} (1 - p) ^ {b - 1} d p \\ = \frac {\binom {n} {k}}{\beta (a , b)} \int_ {0} ^ {1} p ^ {a + k - 1} (1 - p) ^ {b + n - k - 1} d p \\ = \binom {n} {k} \frac {\beta (a + k , b + n - k)}{\beta (a , b)}, \\ \end{array}
$$

for $k = 0 , 1 , \ldots , n .$

## 8.6 Order statistics

The final transformation we will consider in this chapter is the transformation that takes n random variables $X _ { 1 } , \ldots , X _ { n }$ and sorts them in order, producing the transformed r.v.s min $( X _ { 1 } , \ldots , X _ { n } ) , \ldots , \operatorname* { m a x } ( X _ { 1 } , \ldots , X _ { n } )$ . The transformed r.v.s are called the order statistics,<sup>2</sup> and they are often useful when we are concerned with the distribution of extreme values, as we alluded to earlier.

Furthermore, like the sample mean ${ \bar { X } } _ { n } ,$ the order statistics serve as useful summaries of an experiment, since we can use them to determine the cutoffs for the worst 5% of observations, the worst 25%, the best 25%, and so forth (such cutoffs are called the quantiles of the sample).

Definition 8.6.1 (Order statistics). For r.v.s $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ , the order statistics are the random variables $X _ { ( 1 ) } , X _ { ( 2 ) } , \ldots , X _ { ( n ) }$ , where

$$
\begin{array}{l} X _ {(1)} = \min (X _ {1}, \dots , X _ {n}), \\ X _ {(2)} \text {is the second - smallest of} X _ {1}, \dots , X _ {n}, \\ \begin{array}{c}\bullet \\ \bullet \\ \bullet \end{array} \\ X _ {(n - 1)} \text {   is   the   second - largest   of   } X _ {1}, \dots , X _ {n}, \\ X _ {(n)} = \max (X _ {1}, \dots , X _ {n}). \\ \end{array}
$$

Note that $X _ { ( 1 ) } \; \leq \; X _ { ( 2 ) } \; \leq \; \ldots \; \leq \; X _ { ( n ) }$ by definition. We call $X _ { ( j ) }$ the $j t h$ order statistic. If n is odd, $X _ { ( ( n + 1 ) / 2 ) }$ is called the sample median of $X _ { 1 } , \ldots , X _ { n }$

h 8.6.2. The order statistics $X _ { ( 1 ) } , \ldots , X _ { ( n ) }$ are r.v.s, and each $X _ { ( j ) }$ is a function of $X _ { 1 } , \ldots , X _ { n }$ . Even if the original r.v.s are independent, the order statistics are dependent: if we know that $X _ { ( 1 ) } = 1 0 0$ , then $X _ { ( n ) }$ is forced to be at least 100.

We will focus our attention on the case where $X _ { 1 } , \ldots , X _ { n }$ are i.i.d. continuous r.v.s. The reason is that with discrete r.v.s, there is a positive probability of tied values; with continuous r.v.s, the probability of a tie is exactly 0, which makes matters much easier. Thus, for the rest of this section, assume $X _ { 1 } , \ldots , X _ { n }$ are i.i.d. and continuous, with CDF $F$ and PDF f. We will derive the marginal CDF and PDF of each individual order statistic $X _ { ( j ) }$ , as well as the joint PDF of $( X _ { ( 1 ) } , \ldots , X _ { ( n ) } )$

A complication we run into right away is that the transformation to order statistics is not invertible: starting with min $( X , Y )   =   3$ and max $( X , Y )   =   5$ , we can’t tell whether the original values of X and Y were 3 and 5, respectively, or 5 and 3. Therefore the change of variables formula from $\mathbb { R } ^ { n }$ to $\mathbb { R } ^ { n }$ does not apply. Instead we will take a direct approach, using pictures to guide us when necessary.

Let’s start with the CDF of $X _ { ( n ) } { = } \operatorname* { m a x } ( X _ { 1 } , \ldots X _ { n } )$ . Since $X _ { ( n ) }$ is less than x if

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>This term sometimes causes confusion. In statistics (the field of study), any function of the data is called a statistic. If X<sub>1</sub>, . . . , X<sub>n</sub> are the data, then min(X<sub>1</sub>, . . . , X<sub>n</sub>) is a statistic, and so is max(X<sub>1</sub>, . . . , X<sub>n</sub>). They are called order statistics because we get them by sorting the data in order (from smallest to largest).</span></small>