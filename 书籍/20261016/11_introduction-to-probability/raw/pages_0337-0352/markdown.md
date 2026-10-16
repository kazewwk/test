if refrigerators have twice the failure rate of stoves, then it says that the odds are 2 to 1 in favor of the refrigerator failing first. As a simple check, note that the answer reduces to $1 / 2$ when $\lambda _ { 1 } = \lambda _ { 2 }$ , which must be true by symmetry.

An alternative method of getting the same result is to use LOTP to condition on $T _ { 1 }$ (or condition on $T _ { 2 } )$ . A third approach, using a story about Poisson processes, is in Chapter 13. 

Our last example in this section demonstrates how we can use the joint distribution of X and Y to derive the distribution of a function of X and $Y$

Example 7.1.25 (Cauchy PDF). Let X and Y be i.i.d. $\mathcal { N } ( 0 , 1 )$ , and let $T = X / Y$ (We can define $T$ arbitrarily in the case $Y = 0 ;$ ; the choice of how to define $T$ in that case has no effect on the distribution of $T ,$ since $P ( Y = 0 ) = 0 . )$ The distribution of $T$ is a famous named distribution called the Cauchy distribution, and we will encounter it again in later chapters. Meanwhile, find the PDF of $T$

## Solution:

We’ll find an expression for the CDF of T first, and then differentiate to get the PDF. We can write

$$
F _ {T} (t) = P (T \leq t) = P \left(\frac {X}{Y} \leq t\right) = P \left(\frac {X}{| Y |} \leq t\right),
$$

since the ${ \mathrm { ~ r . v . s ~ } } { \frac { X } { Y } }$ and $\frac { X } { | | Y | | }$ are identically distributed by the symmetry of the standard Normal distribution. Now $\left| Y \right|$ is nonnegative, so we can multiply by it on both sides without reversing the direction of the inequality. Thus, we are interested in finding

$$
F _ {T} (t) = P (X \leq t | Y |).
$$

We calculate this probability by integrating the joint PDF of X and $Y$ over the region where $X \leq t | Y |$ holds. The joint PDF of X and Y is just the product of the marginal PDFs, by independence. So

$$
\begin{array}{l} F _ {T} (t) = P (X \leq t | Y |) \\ = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {t | y |} \frac {1}{\sqrt {2 \pi}} e ^ {- x ^ {2} / 2} \frac {1}{\sqrt {2 \pi}} e ^ {- y ^ {2} / 2} d x d y. \\ \end{array}
$$

Note that the inner limits of integration (the limits for x) depend on $y ,$ whereas the outer limits of integration (the limits for $y )$ can’t depend on $x$ (see the math appendix for more about limits of integration with multiple integrals). With some manipulations, we can get the double integral down to a single integral:

$$
\begin{array}{l} F _ {T} (t) = \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {2 \pi}} e ^ {- y ^ {2} / 2} \left(\int_ {- \infty} ^ {t | y |} \frac {1}{\sqrt {2 \pi}} e ^ {- x ^ {2} / 2} d x\right) d y \\ = \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {2 \pi}} e ^ {- y ^ {2} / 2} \Phi (t | y |) d y \\ = \sqrt {\frac {2}{\pi}} \int_ {0} ^ {\infty} e ^ {- y ^ {2} / 2} \Phi (t y) d y. \\ \end{array}
$$

Alternatively, we can get the same result without doing a double integral by using one of the versions of LOTP. Letting I be the indicator r.v. for the event $X \leq t | Y |$ we again have

$$
\begin{array}{l} P (I = 1) = \int_ {- \infty} ^ {\infty} P (I = 1 | Y = y) f _ {Y} (y) d y \\ = \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {2 \pi}} e ^ {- y ^ {2} / 2} \Phi (t | y |) d y. \\ \end{array}
$$

At this point we seem to be stuck with an integral we don’t know how to do. Fortunately, we were asked to find the PDF, not the CDF, so instead of evaluating the integral, we can just differentiate it with respect to t (not with respect to $y ,$ which is a dummy variable). We are permitted to interchange the order of integration and differentiation under mild technical conditions, which are met here. (This technique is known as differentiation under the integral sign, or DUThIS for short.) Then

$$
\begin{array}{l} f _ {T} (t) = F _ {T} ^ {\prime} (t) = \sqrt {\frac {2}{\pi}} \int_ {0} ^ {\infty} \frac {\partial}{\partial t} \left(e ^ {- y ^ {2} / 2} \Phi (t y)\right) d y \\ = \sqrt {\frac {2}{\pi}} \int_ {0} ^ {\infty} y e ^ {- y ^ {2} / 2} \varphi (t y) d y \\ = \frac {1}{\pi} \int_ {0} ^ {\infty} y e ^ {- \frac {(1 + t ^ {2}) y ^ {2}}{2}} d y \\ = \frac {1}{\pi (1 + t ^ {2})}, \\ \end{array}
$$

using the substitution $u = ( 1 + t ^ { 2 } ) y ^ { 2 } / 2 ,   d u = ( 1 + t ^ { 2 } ) y d y$ for the final step. So the PDF of $T$ is

$$
f _ {T} (t) = \frac {1}{\pi (1 + t ^ {2})}, \quad t \in \mathbb {R}.
$$

Since

$$
\int_ {- \infty} ^ {\infty} \frac {1}{1 + t ^ {2}} d t = \arctan (\infty) - \arctan (- \infty) = \pi ,
$$

we have obtained a valid PDF. If we want to obtain the CDF too, we can integrate the PDF over the appropriate interval:

$$
F _ {T} (t) = \int_ {- \infty} ^ {t} \frac {1}{\pi (1 + u ^ {2})} d u = \frac {1}{\pi} \arctan (t) + \frac {1}{2}.
$$

As we mentioned, the distribution of T is called the Cauchy distribution. The Cauchy PDF is similar in shape to the Normal bell curve, but with tails that decay less quickly to 0. Figure 7.7 superimposes the Cauchy and standard Normal PDFs; the heavier tails of the Cauchy PDF are evident.

An interesting fact about the Cauchy distribution is that although the PDF is symmetric about 0, its expected value does not exist, since the integral $\textstyle \int _ { - \infty } ^ { \infty } { \frac { t } { \pi \left( 1 + t ^ { 2 } \right) } } d t$ diverges: note that for large $\begin{array} { r } { t , \; \frac { t } { 1 + t ^ { 2 } } \approx \frac { 1 } { t } } \end{array}$ , and $\begin{array} { r } { \int _ { 1 } ^ { \infty } \frac { 1 } { t } d t = \infty } \end{array}$ . It would be a blunder to write $\text{" }E(\frac{X}{Y})=E(X)E(\frac{1}{Y})=\overset{\text{" }}{0}\cdot E(\frac{1}{Y})=0 \text{" }$ , since $E ( \frac { 1 } { Y } )$ also does not exist. 

![](images/page_338_chart_2.jpg)

<details>
<summary>violin</summary>

| X | PDF (Black) | PDF (Gray) |
| --- | --- | --- |
| -3 | ~0.02 | ~0.00 |
| -2 | ~0.06 | ~0.05 |
| -1 | ~0.18 | ~0.25 |
| 0 | ~0.32 | ~0.40 |
| 1 | ~0.18 | ~0.25 |
| 2 | ~0.06 | ~0.05 |
| 3 | ~0.02 | ~0.00 |
</details>

## FIGURE 7.7

Cauchy PDF (dark) and $\mathcal { N } ( 0 , 1 )$ PDF (light). The Cauchy distribution has much heavier tails than the Normal distribution.

## 7.1.3 Hybrid

It is also possible that we could be interested in the joint distribution of a discrete r.v. and a continuous r.v. This case was mentioned when discussing the four forms of Bayes’ rule and LOTP. Conceptually it is analogous to the other cases, but since the notation can be tricky, we’ll work through an example that sheds light on it.

Example 7.1.26 (Which company made the lightbulb?). A lightbulb was manufactured by one of two companies. Bulbs that are made by Company 0 last an Expo(λ<sub>0</sub>) amount of time, and bulbs made by Company 1 last an $\mathrm{Exp}(\lambda_1)$ amount of time, with $\lambda _ { 0 }   <   \lambda _ { 1 }$ . The bulb of interest here was made by Company 0 with probability $p _ { 0 }$ and by Company 1 with probability $p _ { 1 } = 1 - p _ { 0 }$ , but from inspecting the bulb we don’t know which company made it.

Let T be how long the bulb lasts, and I be the indicator of it having been made by Company 1.

(a) Find the CDF and PDF of $T .$
(b) Does T have the memoryless property?
(c) Find the conditional distribution of I given T = t. What happens to this as $t \rightarrow \infty ?$

## Solution:

Since T is a continuous r.v. and I is discrete, the joint distribution of $T$ and I is a hybrid, as illustrated in Figure 7.8. In a joint PDF of two continuous r.v.s, there are infinitely many vertical slices of the joint PDF that we can take, each corresponding to a different conditional PDF. Here there are only two conditional PDFs of $T ,$ one for $I = 0$ and one for $I = 1$ . As stated in the problem, the conditional distribution of $T$ given $I = 0$ is Expo(λ<sub>0</sub>) and given I = 1 is $\mathrm{Exp}(\lambda_1)$ . The marginal distribution of I is $\mathrm { B e r n } ( p _ { 1 } )$

![](images/page_339_image_3.jpg)

<details>
<summary>text_image</summary>

I = 0
I = 1
t
</details>

## FIGURE 7.8

Hybrid joint distribution of T and I.

Thus, we are given the joint distribution of T and I in terms of (1) the marginal distribution of I and (2) the conditional distribution of $T$ given I. The problem then asks us to flip it around and find (1) the marginal distribution of $T$ and (2) the conditional distribution of I given $T .$ Phrased in this way, it becomes clear that LOTP and Bayes’ rule will be our friends.

(a) In this part we are asked to derive the marginal distribution of T. For the CDF, we use the law of total probability, conditioning on I:

$$
\begin{array}{l} F _ {T} (t) = P (T \leq t) = P (T \leq t | I = 0) p _ {0} + P (T \leq t | I = 1) p _ {1} \\ = (1 - e ^ {- \lambda_ {0} t}) p _ {0} + (1 - e ^ {- \lambda_ {1} t}) p _ {1} \\ = 1 - p _ {0} e ^ {- \lambda_ {0} t} - p _ {1} e ^ {- \lambda_ {1} t} \\ \end{array}
$$

for $t > 0$ . The marginal PDF is the derivative of the CDF:

$$
f _ {T} (t) = p _ {0} \lambda_ {0} e ^ {- \lambda_ {0} t} + p _ {1} \lambda_ {1} e ^ {- \lambda_ {1} t}, \text {for} t > 0.
$$

We could also have gotten this directly from the $^ { \circ } X$ continuous, Y discrete” version of LOTP, but we did not write out a proof of that version of LOTP, and working through this example helps show why that version of LOTP works.

(b) Since $\lambda _ { 0 } \neq \lambda _ { 1 }$ , the above expression for the PDF does not reduce to the form $\dot { \lambda } e ^ { - \lambda t }$ . So the distribution of $T$ is not Exponential, which implies that it does not have the memoryless property. (The distribution of T is called a mixture of two Exponentials.)

(c) Using a hybrid form of Bayes’ rule, which is the $^ { \circ } X$ continuous, Y discrete” version in the table of versions of Bayes’ rule, we have

$$
P (I = 1 | T = t) = \frac {f _ {T} (t | I = 1) P (I = 1)}{f _ {T} (t)},
$$

where $f _ { T } ( t | I = 1 )$ is the conditional PDF of T given $I = 1$ , evaluated at t. Using the fact that $T | I = 1 \sim \mathrm { E x p o } ( \lambda _ { 1 } )$ and the marginal PDF derived in (a),

$$
P (I = 1 | T = t) = \frac {p _ {1} \lambda_ {1} e ^ {- \lambda_ {1} t}}{p _ {0} \lambda_ {0} e ^ {- \lambda_ {0} t} + p _ {1} \lambda_ {1} e ^ {- \lambda_ {1} t}} = \frac {p _ {1} \lambda_ {1}}{p _ {0} \lambda_ {0} e ^ {(\lambda_ {1} - \lambda_ {0}) t} + p _ {1} \lambda_ {1}}.
$$

Thus the conditional distribution of I given $T = t$ is Bernoulli with this probability of success. This probability goes to 0 as $t \rightarrow \infty$ , which makes sense intuitively: the longer the bulb lasts, the more confident we will be that it was made by Company 0, as their bulbs have a lower failure rate λ and a higher life expectancy $\frac { 1 } { \lambda } .$ 

## 7.2 2D LOTUS

The two-dimensional version of LOTUS lets us calculate the expectation of a random variable that is a function of two random variables X and Y , using the joint distribution of X and Y .

Theorem 7.2.1 (2D LOTUS). Let g be a function from $\mathbb { R } ^ { 2 }$ to $\mathbb { R } .$ If X and $Y$ are discrete, then

$$
E (g (X, Y)) = \sum_ {x} \sum_ {y} g (x, y) P (X = x, Y = y).
$$

If X and Y are continuous with joint PDF $f _ { X , Y }$ , then

$$
E (g (X, Y)) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} g (x, y) f _ {X, Y} (x, y) d x d y.
$$

Like its 1D counterpart, 2D LOTUS saves us from having to find the distribution of $g ( X , Y )$ in order to calculate its expectation. Instead, having the joint PMF or joint PDF of X and $Y$ is enough.

One use of 2D LOTUS is to find the expected distance between two r.v.s.

Example 7.2.2 (Expected distance between two Uniforms). Let X and $Y$ be i.i.d. Unif(0, 1) r.v.s. Find $E ( | X - Y | )$

Solution:

Since the joint PDF is 1 on the unit square $\{ ( x , y ) : x , y \in [ 0 , 1 ] \}$ , 2D LOTUS gives

$$
\begin{array}{l} E (| X - Y |) = \int_ {0} ^ {1} \int_ {0} ^ {1} | x - y | d x d y \\ = \int_ {0} ^ {1} \int_ {y} ^ {1} (x - y) d x d y + \int_ {0} ^ {1} \int_ {0} ^ {y} (y - x) d x d y \\ = 2 \int_ {0} ^ {1} \int_ {y} ^ {1} (x - y) d x d y = 1 / 3. \\ \end{array}
$$

First we broke up the integral into two parts so we could eliminate the absolute value; then we used symmetry.

Incidentally, by solving this problem, we have also figured out the expected value of $M = \operatorname* { m a x } ( X , Y )$ and $L = \operatorname* { m i n } ( X , Y )$ . Since $M + L$ is the same r.v. as $X + Y$ and $M - L$ is the same r.v. as $| X - Y |$

$$
\begin{array}{l} E (M + L) = E (X + Y) = 1, \\ E (M - L) = E (| X - Y |) = 1 / 3. \\ \end{array}
$$

This is a system of two equations and two unknowns, which we can solve to get $E ( M ) = 2 / 3$ and $E ( L ) = 1 / 3$ . As a check, $E ( M )$ exceeds $E ( L )$ , as it should, and $E ( M )$ and $E ( L )$ are equidistant from $1 / 2$ , as should be the case by symmetry. 

Example 7.2.3 (Expected distance between two Normals). For $X , Y \stackrel { \mathrm { i . i . d . } } { \sim } \mathcal { N } ( 0 , 1 )$ find $E ( | X - Y | )$

Solution:

We could again use 2D LOTUS, giving

$$
E (| X - Y |) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} | x - y | \frac {1}{\sqrt {2 \pi}} e ^ {- x ^ {2} / 2} \frac {1}{\sqrt {2 \pi}} e ^ {- y ^ {2} / 2} d x d y,
$$

but an easier solution uses the fact that the sum or difference of independent $\mathrm { N o r - }$ mals is Normal, as we proved using MGFs in Chapter 6. Then $X - Y \sim \mathcal { N } ( 0 , 2 )$ , so we can write $X - Y = \sqrt{2}Z$ where $Z \sim \mathcal { N } ( 0 , 1 )$ , and $E(|X - Y|) = \sqrt{2}E|Z|$ . Thus, we have reduced a 2D LOTUS to a 1D LOTUS! It was shown in Example 5.4.7 that

$$
E | Z | = \sqrt {\frac {2}{\pi}},
$$

so

$$
E (| X - Y |) = \frac {2}{\sqrt {\pi}}.
$$

We can also use 2D LOTUS to give another proof of linearity of expectation.

Example 7.2.4 (Linearity via 2D LOTUS). Let X and Y be continuous r.v.s (the analogous method also works in the discrete case). By 2D LOTUS,

$$
\begin{array}{l} E (X + Y) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} (x + y) f _ {X, Y} (x, y) d x d y \\ = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} x f _ {X, Y} (x, y) d x d y + \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} y f _ {X, Y} (x, y) d x d y \\ = E (X) + E (Y). \\ \end{array}
$$

This is a short proof of linearity of expectation. For the last step, we used 2D LOTUS and the fact that X is a function of X and $Y$ (that happens to be degenerate in the sense that it doesn’t involve $Y )$ , and similarly for Y . Another way to get the last step is to write

$$
\int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} y f _ {X, Y} (x, y) d x d y = \int_ {- \infty} ^ {\infty} y \int_ {- \infty} ^ {\infty} f _ {X, Y} (x, y) d x d y = \int_ {- \infty} ^ {\infty} y f _ {Y} (y) d y = E (Y),
$$

where we took y out from the inner integral (since y is held constant when integrating with respect to $x )$ and then recognized the marginal PDF of Y . For the $E ( X )$ term we can first swap the order of integration, from dxdy to dydx, and then the same argument that we used for the $E ( Y )$ term can be applied. 

## 7.3 Covariance and correlation

Just as the mean and variance provided single-number summaries of the distribution of a single $\mathbf { r } . \mathbf { v } . ,$ covariance is a single-number summary of the joint distribution of two r.v.s. Roughly speaking, covariance measures a tendency of two r.v.s to go up or down together, relative to their means: positive covariance between X and Y indicates that when X goes up, $Y$ also tends to go up, and negative covariance indicates that when X goes up, $Y$ tends to go down. Here is the precise definition.

Definition 7.3.1 (Covariance). The covariance between r.v.s X and Y is

$$
\mathrm{Cov} (X, Y) = E ((X - E X) (Y - E Y)).
$$

Multiplying this out and using linearity, we have an equivalent expression:

$$
\operatorname{Cov} (X, Y) = E (X Y) - E (X) E (Y).
$$

Let’s think about the definition intuitively. If X and Y tend to move in the same direction, then $X - E X$ and $Y - E Y$ will tend to be either both positive or both negative, so $( X - E X ) ( Y - E Y )$ will be positive on average, giving a positive covariance. If X and Y tend to move in opposite directions, then $X - E X$ and $Y - E Y$ will tend to have opposite signs, giving a negative covariance.

If X and Y are independent, then their covariance is zero. We say that r.v.s with zero covariance are uncorrelated.

Theorem 7.3.2. If X and Y are independent, then they are uncorrelated.

Proof. We’ll show this in the case where X and $Y$ are continuous, with PDFs $f _ { X }$ and $f _ { Y }$ . Since X and Y are independent, their joint PDF is the product of the marginal PDFs. By 2D LOTUS,

$$
\begin{array}{l} E (X Y) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} x y f _ {X} (x) f _ {Y} (y) d x d y \\ = \int_ {- \infty} ^ {\infty} y f _ {Y} (y) \left(\int_ {- \infty} ^ {\infty} x f _ {X} (x) d x\right) d y \\ = \int_ {- \infty} ^ {\infty} x f _ {X} (x) d x \int_ {- \infty} ^ {\infty} y f _ {Y} (y) d y \\ = E (X) E (Y). \\ \end{array}
$$

The proof in the discrete case is the same, with PMFs instead of PDFs.

The converse of this theorem is false: just because X and Y are uncorrelated does not mean they are independent. For example, let $X \sim \mathcal { N } ( 0 , 1 )$ , and let $Y = X ^ { 2 }$ Then $E ( X Y )   =   E ( X ^ { 3 } )   =   0$ because the odd moments of the standard Normal distribution are equal to 0 by symmetry. Thus X and Y are uncorrelated,

$$
\operatorname{Cov} (X, Y) = E (X Y) - E (X) E (Y) = 0 - 0 = 0,
$$

but they are certainly not independent: Y is a function of X, so knowing X gives us perfect information about $Y$ . Covariance is a measure of linear association, so r.v.s can be dependent in nonlinear ways and still have zero covariance, as this example demonstrates. The bottom right plot of Figure 7.9 shows draws from the joint distribution of X and Y in this example. The other three plots illustrate positive correlation, negative correlation, and independence.

Covariance has the following key properties.

1. $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$
2. $\mathrm{Cov}(X,Y)=\mathrm{Cov}(Y,X)$
3. $\mathrm { C o v } ( X , c ) = 0$ for any constant c.
4. $\mathrm{Cov}(aX,Y)=a\mathrm{Cov}(X,Y)$ for any constant a.
5. $\mathrm{Cov}(X + Y,Z) = \mathrm{Cov}(X,Z) + \mathrm{Cov}(Y,Z)$
6. $\operatorname { C o v } ( X + Y , Z + W ) = \operatorname { C o v } ( X , Z ) + \operatorname { C o v } ( X , W ) + \operatorname { C o v } ( Y , Z ) + \operatorname { C o v } ( Y , W ) .$
7. $\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\mathrm{Cov}(X,Y)$ . For n r.v.s $X _ { 1 } , \ldots , X _ { n } ,$ ,

$$
\mathrm{Var} (X _ {1} + \dots + X _ {n}) = \mathrm{Var} (X _ {1}) + \dots + \mathrm{Var} (X _ {n}) + 2 \sum_ {i <   j} \mathrm{Cov} (X _ {i}, X _ {j}).
$$

![](images/page_344_image_2.jpg)

FIGURE 7.9

Draws from the joint distribution of $( X , Y )$ under various dependence structures. Top left: X and $Y$ are positively correlated. Top right: X and $Y$ are negatively correlated. Bottom left: X and $Y$ are independent, hence uncorrelated. Bottom right: $Y$ is a deterministic function of $X$ , but $X$ and $Y$ are uncorrelated.

The first five properties follow readily from the definition and basic properties of expectation. Property 6 follows from Property 2 and Property 5, by expanding

$$
\begin{array}{l} \operatorname{Cov} (X + Y, Z + W) = \operatorname{Cov} (X, Z + W) + \operatorname{Cov} (Y, Z + W) \\ = \operatorname{Cov} (Z + W, X) + \operatorname{Cov} (Z + W, Y) \\ = \operatorname{Cov} (Z, X) + \operatorname{Cov} (W, X) + \operatorname{Cov} (Z, Y) + \operatorname{Cov} (W, Y) \\ = \operatorname{Cov} (X, Z) + \operatorname{Cov} (X, W) + \operatorname{Cov} (Y, Z) + \operatorname{Cov} (Y, W). \\ \end{array}
$$

Property 7 follows from writing the variance of an r.v. as its covariance with itself (by Property 1) and then using Property 6 repeatedly.

We have now fulfilled our promise from Chapter 4 that for independent r.v.s, the variance of the sum is the sum of the variances:

$$
\mathrm{Var} \left(\sum_ {j = 1} ^ {n} X _ {j}\right) = \sum_ {j = 1} ^ {n} \mathrm{Var} (X _ {j}) \text {if} X _ {1}, \dots , X _ {n} \text {are independent}.
$$

By Theorem 7.3.2, independent r.v.s are uncorrelated, so in that case all the covariance terms drop out of the expression in Property 7.

h 7.3.3. If X and Y are independent, then the properties of covariance give

$$
\operatorname{Var} (X - Y) = \operatorname{Var} (X) + \operatorname{Var} (- Y) = \operatorname{Var} (X) + \operatorname{Var} (Y).
$$

It is a common mistake to claim $``  Var (X - Y) =  Var (X) -  Var (Y)$ ; this is a category error since $\operatorname { V a r } ( X ) - \operatorname { V a r } ( Y )$ could be negative. For general X and Y , we have

$$
\operatorname{Var} (X - Y) = \operatorname{Var} (X) + \operatorname{Var} (Y) - 2 \operatorname{Cov} (X, Y).
$$

Since covariance depends on the units in which X and Y are measured—if we decide to measure X in centimeters rather than meters, the covariance is multiplied by 100—it is easier to interpret a unitless version of covariance called correlation.

Definition 7.3.4 (Correlation). The correlation between r.v.s X and Y is

$$
\mathrm{Corr} (X, Y) = \frac {\mathrm{Cov} (X , Y)}{\sqrt {\mathrm{Var} (X) \mathrm{Var} (Y)}}.
$$

(This is undefined in the degenerate cases $\operatorname { V a r } ( X ) = 0 { \mathrm { ~ o r ~ } } \operatorname { V a r } ( Y ) = 0 . )$

Notice that shifting and scaling X and Y has no effect on their correlation. Shifting does not affect Cov(X, Y ), Var(X), or $\operatorname { V a r } ( Y )$ , so the correlation is unchanged. As for scaling, the fact that we divide by the standard deviations of X and Y ensures that the scale factor cancels out:

$$
\operatorname{Corr} (c X, Y) = \frac {\operatorname{Cov} (c X , Y)}{\sqrt {\operatorname{Var} (c X) \operatorname{Var} (Y)}} = \frac {c \operatorname{Cov} (X , Y)}{\sqrt {c ^ {2} \operatorname{Var} (X) \operatorname{Var} (Y)}} = \operatorname{Corr} (X, Y).
$$

Correlation is convenient to interpret because it does not depend on the units of measurement and is always between −1 and 1.

Theorem 7.3.5 (Correlation bounds). For any r.v.s X and Y ,

$$
- 1 \leq \operatorname{Corr} (X, Y) \leq 1.
$$

Proof. Without loss of generality we can assume X and Y have variance 1, since scaling does not change the correlation. Let $\rho   =   \mathrm { C o r r } ( X , Y )   =   \mathrm { C o v } ( X , Y )$ . Using the fact that variance is nonnegative, along with Property 7 of covariance, we have

$$
\operatorname{Var} (X + Y) = \operatorname{Var} (X) + \operatorname{Var} (Y) + 2 \operatorname{Cov} (X, Y) = 2 + 2 \rho \geq 0,
$$

$$
\mathrm{Var} (X - Y) = \mathrm{Var} (X) + \mathrm{Var} (Y) - 2 \mathrm{Cov} (X, Y) = 2 - 2 \rho \geq 0.
$$

Thus, $- 1 \leq \rho \leq 1$

Here is an example of how to calculate covariance and correlation.

Example 7.3.6 (Exponential max and min). Let X and Y be i.i.d. Expo(1) r.v.s. Find the correlation between max $( X , Y )$ and min(X, Y ).

Solution:

Let $M = \operatorname* { m a x } ( X , Y )$ and $L = \operatorname* { m i n } ( X , Y )$ . By the memoryless property and results from Chapter 5, we know that $L   \sim   \mathrm { E x p o } ( 2 ) , \; M   -   L   \sim   \mathrm { E x p o } ( 1 )$ , and $M - L$ is independent of L (see Example 5.6.5). Therefore,

$$
\mathrm{Cov} (M, L) = \mathrm{Cov} (M - L + L, L) = \mathrm{Cov} (M - L, L) + \mathrm{Cov} (L, L) = 0 + \mathrm{Var} (L) = \frac {1}{4},
$$

$$
\operatorname{Var} (M) = \operatorname{Var} (M - L + L) = \operatorname{Var} (M - L) + \operatorname{Var} (L) = 1 + \frac {1}{4} = \frac {5}{4},
$$

and

$$
\mathrm{Corr} (M, L) = \frac {\mathrm{Cov} (M , L)}{\sqrt {\mathrm{Var} (M) \mathrm{Var} (L)}} = \frac {\frac {1}{4}}{\sqrt {\frac {5}{4} \cdot \frac {1}{4}}} = \frac {1}{\sqrt {5}}.
$$

h 7.3.7. In the above example, it makes sense that the correlation is positive because M is constrained to be at least as large as L. The following argument would be a blunder: $``Either $M = X , \thinspace L = Y$ or $M = Y , \thinspace L = X$$ , so either $\mathrm{Cov}(M, L) =$ $\mathrm{Cov}(X,Y)$ or $\mathrm{Cov}(M, L) = \mathrm{Cov}(Y, X)$ . But Cov $( Y , X ) = \operatorname { C o v } ( X , Y )$ so we always have $\mathrm{Cov}(M,L)=\mathrm{Cov}(X,Y)=0.$ It is true that either $M = X ,   L = Y$ will occur or $M   =   Y ,   L   =   X$ will occur, but these are events, not deterministic cases. The argument would fall apart if if were written carefully using conditional probability.

Covariance properties can also be a helpful tool for finding variances, especially when the r.v. of interest is a sum of dependent random variables. The next example uses properties of covariance to derive the variance of the Hypergeometric distribution. If you did Exercise 48 from Chapter 4, you can compare the two derivations.

Example 7.3.8 (Hypergeometric variance). Find $\operatorname { V a r } ( X )$ for $X \sim \operatorname { H G e o m } ( w , b , n )$

Solution:

Interpret X as the number of white balls in a sample of size n from an urn with w white and b black balls. We can represent $X$ as a sum of indicator random variables, $X   =   I _ { 1 } + \cdots + I _ { n }$ , where $I _ { j }$ is the indicator of the jth ball in the sample being white. Each $I _ { j }$ has mean $p = w / ( w + b )$ and variance $p ( 1 - p )$ , but because the $I _ { j }$ are dependent, we cannot simply add their variances. Instead, we apply properties of covariance:

$$
\begin{array}{l} \operatorname{Var} (X) = \operatorname{Var} \left(\sum_ {j = 1} ^ {n} I _ {j}\right) \\ = \operatorname{Var} (I _ {1}) + \dots + \operatorname{Var} (I _ {n}) + 2 \sum_ {i <   j} \operatorname{Cov} (I _ {i}, I _ {j}) \\ = n p (1 - p) + 2 \binom {n} {2} \mathrm{Cov} (I _ {1}, I _ {2}), \\ \end{array}
$$

since all $\textstyle { \binom { n } { 2 } }$ pairs of indicators have the same covariance by symmetry. Now we just need to find $\mathrm{Cov}(I_{1},I_{2})$ . By the fundamental bridge,

$$
\begin{array}{l} \mathrm{Cov} (I _ {1}, I _ {2}) = E (I _ {1} I _ {2}) - E (I _ {1}) E (I _ {2}) \\ = P (1 \text {st and 2nd balls both white}) - P (1 \text {st ball white}) P (2 \text {nd ball white}) \\ = \frac {w}{w + b} \cdot \frac {w - 1}{w + b - 1} - p ^ {2}. \\ \end{array}
$$

Plugging this into the above formula and simplifying, we eventually obtain

$$
\mathrm{Var} (X) = \frac {N - n}{N - 1} n p (1 - p),
$$

where $N = w + b .$ This differs from the Binomial variance of $n p ( 1 - p )$ by a factor of $\frac { N   -   n } { N   -   1 }$ , which is known as the finite population correction. The discrepancy arises from the fact that in the Binomial story, we sample with replacement, so the same ball can be drawn multiple times; in the Hypergeometric story, we sample without replacement, so each ball appears in the sample at most once.

If we consider N to be the “population size” of the urn, then as N grows very large relative to the sample size $n ,$ it becomes extremely unlikely that in sampling with replacement, we would draw the same ball more than once. Thus sampling with replacement and sampling without replacement become equivalent in the limit as $N \to \infty$ with n fixed, and the finite population correction approaches 1.

The other case where sampling with and without replacement are equivalent is the simple case where we only draw one ball from the urn, and indeed, the finite population correction also equals 1 when $n = 1$ 

The last two sections in this chapter introduce the Multinomial and Multivariate Normal distributions. The Multinomial is the most famous discrete multivariate distribution, and the Multivariate Normal is the most famous continuous multivariate distribution.

## 7.4 Multinomial

The Multinomial distribution is a generalization of the Binomial. Whereas the Binomial distribution counts the successes in a fixed number of trials that can only be categorized as success or failure, the Multinomial distribution keeps track of trials whose outcomes can fall into multiple categories, such as excellent, adequate, poor; or red, yellow, green, blue.

Story 7.4.1 (Multinomial distribution). Each of n objects is independently placed into one of $k$ categories. An object is placed into category $j$ with probability $p _ { j }$ where the $p _ { j }$ are nonnegative and $\textstyle \sum _ { j = 1 } ^ { k } p _ { j } = 1$ . Let $X _ { 1 }$ be the number of objects in category 1, $X _ { 2 }$ the number of objects in category 2, etc., so that $X _ { 1 }   +   \cdots   +   X _ { k } = n$ Then $\mathbf { X } = ( X _ { 1 } , \ldots , X _ { k } )$ is said to have the Multinomial distribution with parameters n and $\mathbf { p } = ( p _ { 1 } , \ldots , p _ { k } )$ . We write this as $\mathbf { X } \sim \operatorname { M u l t } _ { k } ( n , \mathbf { p } )$ 

We call X a random vector because it is a vector of random variables. The joint PMF of X can be derived from the story.

Theorem 7.4.2 (Multinomial joint PMF). I $\operatorname { f } \mathbf { X } \sim \operatorname { M u l t } _ { k } ( n , \mathbf { p } )$ , then the joint PMF of X is

$$
P (X _ {1} = n _ {1}, \dots , X _ {k} = n _ {k}) = \frac {n !}{n _ {1} ! n _ {2} ! \dots n _ {k} !} \cdot p _ {1} ^ {n _ {1}} p _ {2} ^ {n _ {2}} \dots p _ {k} ^ {n _ {k}},
$$

for $n _ { 1 } , \ldots , n _ { k }$ satisfying $n _ { 1 } + \cdots + n _ { k } = n$

Proof. If $n _ { 1 } , \ldots , n _ { k }$ don’t add up to $n ,$ then the event $\{ X _ { 1 } = n _ { 1 } , \ldots , X _ { k } = n _ { k } \}$ is impossible: every object has to go somewhere, and new objects can’t appear out of nowhere. If $n _ { 1 } , \ldots , n _ { k }$ do add up to $n ,$ then any particular way of putting $n _ { 1 }$ objects into category 1, $n _ { 2 }$ objects into category 2, etc., has probability $p _ { 1 } ^ { n _ { 1 } } p _ { 2 } ^ { n _ { 2 } } \ldots p _ { k } ^ { n _ { k } }$ , and there are

$$
\frac {n !}{n _ {1} ! n _ {2} ! \ldots n _ {k} !}
$$

ways to do this, as discussed in Example 1.4.18 in the context of rearranging the letters in STATISTICS. So the joint PMF is as claimed. 

Since we’ve specified the joint distribution of $\mathbf { X } ,$ we have enough information to determine the marginal and conditional distributions, as well as the covariance between any two components of $\mathbf { X }$

Let’s take these one by one, starting with the marginal distribution of $X _ { j }$ , which is the jth component of X. Were we to blindly apply the definition, we would have to sum the joint PMF over all components of X other than $X _ { j }$ . The prospect of $k - 1$ summations is an unpleasant one, to say the least. Fortunately, we can avoid tedious calculations if we instead use the story of the Multinomial distribution: $X _ { j }$ is the number of objects in category $j ,$ where each of the $n$ objects independently belongs to category $j$ with probability $p _ { j }$ . Define success as landing in category $j .$ Then we just have n independent Bernoulli trials, so the marginal distribution of $X _ { j }$ is $\mathrm { B i n } ( n , p _ { j } )$

Theorem 7.4.3 (Multinomial marginals). The marginals of a Multinomial are Binomial. Specifically, if $\mathbf { X } \sim \operatorname { M u l t } _ { k } ( n , \mathbf { p } )$ , then $X _ { j } \sim \operatorname { B i n } ( n , p _ { j } )$

More generally, whenever we merge multiple categories together in a Multinomial random vector, we get another Multinomial random vector. For example, suppose we randomly sample n people in a country with 5 political parties. (If the sampling is done without replacement, the $n$ trials are not independent, but independence is a good approximation as long as the population is large relative to the sample, as we discussed in Theorem 3.9.3 and Example 7.3.8.) Let

$$
\mathbf {X} = (X _ {1}, \dots , X _ {5}) \sim \mathrm{Mult} _ {5} (n, (p _ {1}, \dots , p _ {5}))
$$

represent the political party affiliations of the sample, i.e., $X _ { j }$ is the number of people in the sample who support party $j$ .

Suppose that parties 1 and 2 are the dominant parties, while parties 3 through 5 are minor third parties. If we decide that instead of keeping track of all 5 parties, we only want to count the number of people in party 1, party 2, or “other”, then we can define a new random vector that lumps all the third parties into one category:

$$
\mathbf {Y} = (X _ {1}, X _ {2}, X _ {3} + X _ {4} + X _ {5}).
$$

By the story of the Multinomial,

$$
\mathbf {Y} \sim \mathrm{Mult} _ {3} (n, (p _ {1}, p _ {2}, p _ {3} + p _ {4} + p _ {5})).
$$

Of course, this idea applies to merging categories in any Multinomial, not just in the context of political parties.

Theorem 7.4.4 (Multinomial lumping). If $\mathbf { X } \sim \operatorname { M u l t } _ { k } ( n , \mathbf { p } )$ , then for any distinct $i$ and $j , \; X _ { i } + X _ { j } \; \sim \; \mathrm { B i n } ( n , p _ { i } + p _ { j } )$ . The random vector of counts obtained from merging categories i and $j$ is still Multinomial. For example, merging categories 1 and 2 gives

$$
(X _ {1} + X _ {2}, X _ {3}, \dots , X _ {k}) \sim \mathrm{Mult} _ {k - 1} (n, (p _ {1} + p _ {2}, p _ {3}, \dots , p _ {k})).
$$

Now for the conditional distributions. Suppose we get to observe $X _ { 1 }$ , the number of objects in category 1, and we wish to update our distribution for the other categories $( X _ { 2 } , \ldots , X _ { k } )$ . One way to do this is with the definition of conditional PMF:

$$
P (X _ {2} = n _ {2}, \dots , X _ {k} = n _ {k} | X _ {1} = n _ {1}) = \frac {P (X _ {1} = n _ {1} , X _ {2} = n _ {2} , \dots , X _ {k} = n _ {k})}{P (X _ {1} = n _ {1})}.
$$

The numerator is the joint PMF of the Multinomial, and the denominator is the marginal PMF of $X _ { 1 }$ , both of which we have already derived. However, we prefer to use the Multinomial story to deduce the conditional distribution of $( X _ { 2 } , \ldots , X _ { k } )$ without algebra. Given that there are $n _ { 1 }$ objects in category 1, the remaining $n   -   n _ { 1 }$ objects fall into categories 2 through k, independently of one another. By Bayes’ rule, the conditional probability of falling into category $j$ is

$$
P (\text {in category} j \mid \text {not in category 1}) = \frac {P (\text {in category} j)}{P (\text {not in category 1})} = \frac {p _ {j}}{p _ {2} + \cdots + p _ {k}},
$$

for $j \; = \; 2 , \ldots , k$ . This makes intuitive sense: the updated probabilities are proportional to the original probabilities $( p _ { 2 } , \ldots , p _ { k } )$ , but these must be renormalized to yield a valid probability vector. Putting it all together, we have the following result.

Theorem 7.4.5 (Multinomial conditioning). If $\mathbf { X } \sim \operatorname { M u l t } _ { k } ( n , \mathbf { p } )$ , then

$$
(X _ {2}, \dots , X _ {k}) \big | X _ {1} = n _ {1} \sim \mathrm{Mult} _ {k - 1} (n - n _ {1}, (p _ {2} ^ {\prime}, \dots , p _ {k} ^ {\prime})),
$$

where $p _ { j } ^ { \prime } = p _ { j } / ( p _ { 2 } + \cdots + p _ { k } )$

Finally, we know that components within a Multinomial random vector are dependent since they are constrained by $X _ { 1 } + \cdots + X _ { k } = n$ . To find the covariance between $X _ { i }$ and $X _ { j }$ , we can use the marginal and lumping properties we have just discussed.

Theorem 7.4.6 (Covariance in a Multinomial). Let $( X _ { 1 } , \ldots , X _ { k } ) { \sim } { \operatorname { M u l t } } _ { k } ( n , \mathbf { p } )$ where $\mathbf { p } = ( p _ { 1 } , \ldots , p _ { k } )$ . For $i \neq j, \mathrm{Cov}(X_i, X_j) = -np_i p_j$

Proof. For concreteness, let $i \; = \; 1$ and $j \; = \; 2$ . Using the lumping property and the marginal distributions of a Multinomial, we know $X _ { 1 } + X _ { 2 } \sim \operatorname { B i n } ( n , p _ { 1 } + p _ { 2 } )$ $X _ { 1 } \sim \operatorname { B i n } ( n , p _ { 1 } )$ , and $X _ { 2 } \sim \operatorname { B i n } ( n , p _ { 2 } )$ . Therefore

$$
\mathrm{Var} (X _ {1} + X _ {2}) = \mathrm{Var} (X _ {1}) + \mathrm{Var} (X _ {2}) + 2 \mathrm{Cov} (X _ {1}, X _ {2})
$$

becomes

$$
n (p _ {1} + p _ {2}) (1 - (p _ {1} + p _ {2})) = n p _ {1} (1 - p _ {1}) + n p _ {2} (1 - p _ {2}) + 2 \mathrm{Cov} (X _ {1}, X _ {2}).
$$

Solving for $\mathrm{Cov}(X_{1},X_{2})$ gives $\mathrm{Cov}(X_{1},X_{2}) = -np_{1}p_{2}$ . By the same logic, for $i \neq j$ we have $\mathrm{Cov}(X_{i},X_{j}) = -np_{i}p_{j}$

The components are negatively correlated, as we would expect: if we know there are a lot of objects in category i, then there aren’t as many objects left over that could possibly be in category $j .$ Exercise 65 asks for a different proof of this result, using indicators.  h 7.4.7 (Independent trials but dependent components). The k components of a Multinomial are dependent, but the n objects in the story of the Multinomial are independently categorized. In the extreme case $k = 2 ,$ a $\mathrm { M u l t } _ { k } ( n , \mathbf { p } )$ random vector looks like $( X , n - X )$ with $X \sim \operatorname { B i n } ( n , p _ { 1 } )$ , which we can think of as (number of successes, number of failures), where “success” is defined as getting category 1. The number of successes is perfectly negatively correlated with the number of failures, even though the trials are independent.

We conclude this section with a heroic example that ties together many of the most important concepts for the Multinomial.

Example 7.4.8 (Statwoman). The superhero Statwoman uses probability and statistics to fight crime. She has battled with countless foes, sometimes even fighting several at the same time. For simplicity though, assume that each of her battles is with exactly one of the following adversaries: the Confounder, the Extrapolator, and the Overfitter.

Suppose that Statwoman will have n battles next year (with n a positive integer), and that each battle is with the Confounder with probability $p _ { 1 }$ , the Extrapolator with probability $p _ { 2 }$ , and the Overfitter with probability $p _ { 3 }$ , independently. Here $p _ { 1 } , p _ { 2 } , p _ { 3 }$ are nonnegative and sum to 1. Let $X _ { 1 } , X _ { 2 } , X _ { 3 }$ be the numbers of battles Statwoman will have with the Confounder, the Extrapolator, and the Overfitter next year, respectively.

(a) Find the joint distribution of $X _ { 1 } , X _ { 2 } , X _ { 3 }$
(b) Find the correlation between $X _ { 1 }$ and $X _ { 2 }$
(c) Suppose for this part only that it turns out that the Extrapolator and the Overfitter have been devising evil plots together, so it is of interest to study their combined number of skirmishes with Statwoman. Let $X _ { 2 3 } = X _ { 2 }   +   X _ { 3 }$ . Find the joint distribution of $X _ { 1 } , X _ { 2 3 }$
(d) Suppose for this part only that the parameters $p _ { 1 } , p _ { 2 } , p _ { 3 }$ are unknown, $n = 3 6 0$ and it is observed that exactly 36 of Statwoman’s battles are with the Overfitter. A natural way to estimate $p _ { 3 }$ would be to use $3 6 / 3 6 0 = 0 . 1$ . The maximum likelihood estimate (MLE) of $p _ { 3 }$ is the value of $p _ { 3 }$ that makes the observed data, $X _ { 3 } = 3 6$ , as likely as possible. That is, the MLE is the value of $p _ { 3 }$ that maximizes $P ( X _ { 3 } = 3 6 )$ Show that the MLE is the natural estimate, 0.1.
(e) Assume for this part only that the Overfitter has been captured, through heroic efforts! So assume that all of Statwoman’s battles next year will be with one of her other two adversaries. Find the joint PMF of $X _ { 1 } , X _ { 2 }$ , given that $X _ { 3 } = 0$
(f) Now suppose that, instead of the number of battles being a constant $n ,$ the number of battles is $N \sim  Pois (\lambda)$ . Find the joint distribution of $X _ { 1 } , X _ { 2 } , X _ { 3 }$

## Solution:

(a) By the story of the Multinomial, $( X _ { 1 } , X _ { 2 } , X _ { 3 } ) \sim \operatorname { M u l t } _ { 3 } ( n , ( p _ { 1 } , p _ { 2 } , p _ { 3 } ) )$