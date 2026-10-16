transformation that sorts observations, turning $X _ { 1 } , \ldots , X _ { n }$ into the order statistics min $( X _ { 1 } , \ldots , X _ { n } ) , \ldots , \operatorname* { m a x } ( X _ { 1 } , \ldots , X _ { n } )$ , is a transformation from $\mathbb { R } ^ { n }$ to $\mathbb { R } ^ { n }$ that is not invertible. Order statistics are addressed in the last section in this chapter.

Furthermore, it is especially important to us to understand transformations because of the approach we’ve taken to learning about the named distributions. Starting from a few basic distributions, we have defined other distributions as transformations of these elementary building blocks, in order to understand how the named distributions are related to one another. We’ll continue in that spirit here as we introduce two new distributions, the Beta and Gamma, which generalize the Uniform and Exponential.

We already have quite a few tools in our toolbox for dealing with transformations, so let’s review those briefly. First, if we are only looking for the expectation of $g ( X )$ , LOTUS shows us the way: it tells us that the PMF or PDF of $X$ is enough for calculating $E ( g ( X ) )$ . LOTUS also applies to functions of several r.v.s, as we learned in the previous chapter.

If we need the full distribution of $g ( X )$ , not just its expectation, our approach depends on whether X is discrete or continuous.

• In the discrete case, we get the PMF of $g ( X )$ by translating the event $g ( X ) = y$ into an equivalent event involving X. To do so, we look for all values x such that $g ( x ) = y ;$ as long as $X$ equals any of these $x ^ { \prime } \mathbf { S } .$ the event $g ( X ) = y$ will occur. This gives the formula

$$
P (g (X) = y) = \sum_ {x: g (x) = y} P (X = x).
$$

For a one-to-one $g ,$ the situation is particularly simple, because there is only one value of x such that $g ( x ) = y$ , namely $g ^ { - 1 } ( y )$ . Then we can use

$$
P (g (X) = y) = P (X = g ^ {- 1} (y))
$$

to convert between the PMFs of X and $g ( X )$ , as also discussed in Section 3.7. For example, it is extremely easy to convert between the Geometric and First Success distributions.

• In the continuous case, a universal approach is to start from the CDF of $g ( X )$ , and translate the event $g ( X ) \leq y$ into an equivalent event involving X. For general $g ,$ we may have to think carefully about how to express $g ( X ) \leq y$ in terms of $X$ , and there is no easy formula we can plug into. But when $g$ is continuous and strictly increasing, the translation is easy: $g ( X ) \leq y$ is the same as $X \leq g ^ { - 1 } ( y )$ , so

$$
F _ {g (X)} (y) = P (g (X) \leq y) = P (X \leq g ^ {- 1} (y)) = F _ {X} (g ^ {- 1} (y)).
$$

We can then differentiate with respect to $y$ to get the PDF of $g ( X )$ . This gives a one-dimensional version of the change of variables formula, which generalizes to invertible transformations in multiple dimensions.

## 8.1 Change of variables

Theorem 8.1.1 (Change of variables in one dimension). Let X be a continuous r.v. with PDF $f _ { X }$ , and let $Y = g ( X )$ , where $g$ is differentiable and strictly increasing (or strictly decreasing). Then the PDF of $Y$ is given by

$$
f _ {Y} (y) = f _ {X} (x) \left| \frac {d x}{d y} \right|,
$$

where $x = g ^ { - 1 } ( y )$ . The support of Y is all $g ( x )$ with x in the support of X.

Proof. Let $g$ be strictly increasing. The CDF of Y is

$$
F _ {Y} (y) = P (Y \leq y) = P (g (X) \leq y) = P (X \leq g ^ {- 1} (y)) = F _ {X} (g ^ {- 1} (y)) = F _ {X} (x),
$$

so by the chain rule, the PDF of $Y$ is

$$
f _ {Y} (y) = f _ {X} (x) \frac {d x}{d y}.
$$

The proof for $g$ strictly decreasing is analogous. In that case the PDF ends up as $\begin{array} { r } { - f _ { X } ( x ) \frac { d x } { d y } } \end{array}$ , which is nonnegative since $\begin{array} { r } { \dot { \frac { d x } { d y } } < 0 } \end{array}$ if g is strictly decreasing. Using $\big | \frac { d x } { d y } \big | .$ as in the statement of the theorem, covers both cases.

When applying the change of variables formula, we can choose whether to compute $\frac { d x } { d y }$ , or compute $\frac { d y } { d x }$ and take the reciprocal. By the chain rule, these give the same result, so we can do whichever is easier.

h 8.1.2. When finding the distribution of $Y$ , be sure to:

• Check the assumptions of the change of variables theorem carefully if you wish to apply it (if it doesn’t apply, a good strategy is to start with the CDF of Y ).
• Express your final answer for the PDF of Y as a function of $y .$
• Specify the support of $Y$ .

The change of variables formula (in the strictly increasing g case) is easy to remember when written in the form

$$
f _ {Y} (y) d y = f _ {X} (x) d x,
$$

which has an aesthetically pleasing symmetry to it. This formula also makes sense if we think about units. For example, let X be a measurement in inches and $Y = 2 . 5 4 X$ be the conversion into centimeters (cm). Then the units of $f _ { X } ( x )$ are inches<sup>−1</sup> and the units of $f _ { Y } ( y )$ are $\mathrm { c m } ^ { - 1 }$ , so it would be absurd to say something like $\text{" }f_{Y}(y)=f_{X}(x) \text{" }$ . But dx is measured in inches and dy is measured in cm, so $f _ { Y } ( y ) d y$ and $f _ { X } ( x ) d x$ are unitless quantities, and it makes sense to equate them. Better yet, $f _ { X } ( x ) d x$ and $f _ { Y } ( y ) d y$ have probability interpretations (recall from Chapter 5 that $f _ { X } ( x ) d x$ is essentially the probability that X is in a tiny interval of length dx, centered at $x )$ , which makes it easier to think intuitively about what the change of variables formula is saying.

The next two examples derive the PDFs of two r.v.s that are defined as transformations of a standard Normal r.v. In the first example the change of variables formula applies; in the second example it does not.

Example 8.1.3 (Log-Normal PDF). Let $X   \sim   \mathcal { N } ( 0 , 1 ) , \; Y   =   e ^ { X }$ . In Chapter 6 we named the distribution of $Y$ the Log-Normal, and we found all of its moments using the MGF of the Normal distribution. Now we can use the change of variables formula to find the PDF of $Y .$ since $g ( x ) = e ^ { x }$ is strictly increasing. Let $y = e ^ { x }$ , so $x = \log y$ and $d y / d x = e ^ { x }$ . Then

$$
f _ {Y} (y) = f _ {X} (x) \bigg | \frac {d x}{d y} \bigg | = \varphi (x) \frac {1}{e ^ {x}} = \varphi (\log y) \frac {1}{y}, \quad y > 0.
$$

Note that after applying the change of variables formula, we write everything on the right-hand side in terms of $y ,$ and we specify the support of the distribution. To determine the support, we just observe that as x ranges from $- \infty$ to ∞, $e ^ { x }$ ranges from 0 to $\infty$

We can get the same result by working from the definition of the CDF, translating the event $Y \leq y$ into an equivalent event involving X. For $y > 0$

$$
F _ {Y} (y) = P (Y \leq y) = P (e ^ {X} \leq y) = P (X \leq \log y) = \Phi (\log y),
$$

so the PDF is again

$$
f _ {Y} (y) = \frac {d}{d y} \Phi (\log y) = \varphi (\log y) \frac {1}{y}, \quad y > 0.
$$

Example 8.1.4 (Chi-Square PDF). Let $X \sim \mathcal { N } ( 0 , 1 ) ,   Y   =   X ^ { 2 }$ . The distribution of $Y$ is an example of a Chi-Square distribution, which is formally introduced in Chapter 10. To find the PDF of $Y$ , we can no longer apply the change of variables formula because $g ( x ) = x ^ { 2 }$ is not one-to-one; instead we start from the CDF.

By drawing the graph of $y = x ^ { 2 }$ , we can see that the event $X ^ { 2 } \leq y$ is equivalent to the event $- { \sqrt { y } } \leq X \leq { \sqrt { y } }$ . Then

$$
F _ {Y} (y) = P (X ^ {2} \leq y) = P (- \sqrt {y} \leq X \leq \sqrt {y}) = \Phi (\sqrt {y}) - \Phi (- \sqrt {y}) = 2 \Phi (\sqrt {y}) - 1,
$$

so

$$
f _ {Y} (y) = 2 \varphi (\sqrt {y}) \cdot \frac {1}{2} y ^ {- 1 / 2} = \varphi (\sqrt {y}) y ^ {- 1 / 2}, \quad y > 0.
$$

The following example sheds light on an unexpected appearance of a decidedly non-Normal distribution.

Example 8.1.5 (Lighthouse). A lighthouse on a shore is shining light toward the ocean at a random angle U (measured in radians), where

$$
U \sim \mathrm{Unif} \left(\frac {- \pi}{2}, \frac {\pi}{2}\right).
$$

Consider a line which is parallel to the shore and 1 mile away from the shore, as illustrated in Figure 8.1. An angle of 0 would mean the ray of light is perpendicular to the shore, while an angle of $\pi / 2$ would mean the ray is along the shore, shining to the right from the perspective of the figure.

Let X be the point that the light hits on the line, where the line’s origin is the point on the line that is closest to the lighthouse. Find the distribution of $X$

![](images/page_387_image_6.jpg)

<details>
<summary>text_image</summary>

beach
lighthouse
ocean
1 mile
U
0
X
</details>

## FIGURE 8.1

A lighthouse shining light at a random angle U, viewed from above.

Solution: Looking at the right triangle in Figure 8.1, the length of the opposite side of U divided by the length of the adjacent side of $U$ is $X / 1 = X$ , so

$$
X = \tan (U).
$$

(The figure illustrates a case where $U > 0$ and, correspondingly, $X > 0$ , but the same relationship holds when $U \leq 0 . )$ Let x be a possible value of X and u be the corresponding possible value of $U$ , so

$$
x = \tan (u) \text {and} u = \arctan (x).
$$

By the change of variables formula, which applies since tan is a differentiable, strictly increasing function on $( - \pi / 2 , \pi / 2 )$ ,

$$
f _ {X} (x) = f _ {U} (u) \frac {d u}{d x} = \frac {1}{\pi} \cdot \frac {1}{1 + x ^ {2}},
$$

which shows that X is Cauchy. In particular, this implies that $E [ X ]$ is infinite (since the expected value of a Cauchy does not exist), so on average X is infinitely far from the origin of the line!

The fact that X is Cauchy also makes sense in light of universality of the Uniform. As shown in Example 7.1.25, the Cauchy CDF is

$$
F (x) = \frac {1}{\pi} \arctan (x) + 0. 5.
$$

The inverse is $F ^ { - 1 } ( v ) = \tan \left( \pi \left( v - 0 . 5 \right) \right)$ , so for $V \sim \mathrm { U n i f } ( 0 , 1 )$ we have

$$
F ^ {- 1} (V) = \tan \left(\pi \left(V - 0. 5\right)\right) \sim \text {Cauchy}.
$$

This agrees with our earlier result since $\pi \left( V - 0 . 5 \right) \sim \mathrm { U n i f } ( - \pi / 2 , \pi / 2 ) .$

We can also use the change of variables formula to find the PDF of a location-scale transformation.

Example 8.1.6 (PDF of a location-scale transformation). Let X have PDF $f _ { X }$ and let $Y = a + b X$ , with $b \neq 0$ . Let $y = a + b x$ , to mirror the relationship between $Y$ and X. Then $\begin{array} { r } { \frac { d y } { d x } = b , } \end{array}$ so the PDF of $Y$ is

$$
f _ {Y} (y) = f _ {X} (x) \bigg | \frac {d x}{d y} \bigg | = f _ {X} \left(\frac {y - a}{b}\right) \frac {1}{| b |}.
$$

The change of variables formula generalizes to n dimensions, where it tells us how to use the joint PDF of a random vector $\mathbf { X }$ to get the joint PDF of the transformed random vector $\mathbf { Y } = g ( \mathbf { X } )$ . The formula is analogous to the one-dimensional version, but it involves a multivariate generalization of the derivative called a Jacobian matrix ; see sections A.6 and A.7 of the math appendix for more about Jacobians.

Theorem 8.1.7 (Change of variables). Let $\mathbf { X }   =   ( X _ { 1 } , \ldots , X _ { n } )$ be a continuous random vector with joint PDF $f _ { \mathbf { X } }$ . Let $g   :   A _ { 0 }   \rightarrow   B _ { 0 }$ be an invertible function, where $A _ { 0 }$ and $B _ { 0 }$ are $\mathrm { o p e n ^ { 1 } }$ subsets of $\mathbb { R } ^ { n } ,   A _ { 0 }$ contains the support of $\mathbf { X } ,$ and $B _ { 0 }$ is the range of $g .$

Let $\mathbf { Y } = g ( \mathbf { X } )$ , and mirror this by letting $\mathbf { y } = g ( \mathbf { x } )$ . Since $g$ is invertible, we also have $\mathbf { X } = g ^ { - 1 } ( \mathbf { Y } )$ and $\mathbf { x } = g ^ { - 1 } ( \mathbf { y } )$

Suppose that all the partial derivatives $\frac { \partial x _ { i } } { \partial y _ { j } }$ exist and are continuous, so we can form the Jacobian matrix

$$
\frac {\partial \mathbf {x}}{\partial \mathbf {y}} = \left( \begin{array}{c c c c} \frac {\partial x _ {1}}{\partial y _ {1}} & \frac {\partial x _ {1}}{\partial y _ {2}} & \dots & \frac {\partial x _ {1}}{\partial y _ {n}} \\ \vdots & & & \vdots \\ \frac {\partial x _ {n}}{\partial y _ {1}} & \frac {\partial x _ {n}}{\partial y _ {2}} & \dots & \frac {\partial x _ {n}}{\partial y _ {n}} \end{array} \right).
$$

Also assume that the determinant of this Jacobian matrix is never 0. Then the joint PDF of $\mathbf { Y }$ is

$$
f _ {\mathbf {Y}} (\mathbf {y}) = f _ {\mathbf {X}} \left(\mathbf {g} ^ {- 1} (\mathbf {y})\right) \cdot \left| \frac {\partial \mathbf {x}}{\partial \mathbf {y}} \right| \quad \text {for} \mathbf {y} \in B _ {0},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1<sub>A</sub> set C ⊂ R<sup>n</sup>is open if for each x ∈ C, there exists  > 0 such that all points with distance less than  from x are contained in C. Sometimes we take A<sub>0</sub> = B<sub>0</sub> = R<sup>n</sup>, but often we would like more flexibility for the domain and range of g. For example, if n = 2, and X<sub>1</sub> and X<sub>2</sub> have support (0, ∞), we may want to work with the open set A<sub>0</sub> = (0, ∞) × (0, ∞) rather than all of R<sup>2</sup>.</span></small>

and 0 otherwise. (The inner bars around the Jacobian say to take the determinant and the outer bars say to take the absolute value.)

That is, to convert $f _ { \mathbf { X } } ( \mathbf { x } )$ to $f _ { \mathbf { Y } } ( \mathbf { y } )$ we express the x in $f _ { \mathbf { X } } ( \mathbf { x } )$ in terms of y and then multiply by the absolute value of the determinant of the Jacobian $\partial \mathbf { x } / \partial \mathbf { y }$

As in the 1D case,

$$
\left| \frac {\partial \mathbf {x}}{\partial \mathbf {y}} \right| = \left| \frac {\partial \mathbf {y}}{\partial \mathbf {x}} \right| ^ {- 1},
$$

so we can compute whichever of the two Jacobians is easier, and then at the end express the joint PDF of Y as a function of $\mathbf { y }$

We will not prove the change of variables formula here, but the idea is to apply the change of variables formula from multivariable calculus and the fact that if A is a region in $A _ { 0 }$ and $B = \{ g ( \mathbf { x } ) : \mathbf { x } \in A \}$ is the corresponding region in $B _ { 0 }$ , then $\mathbf { X } \in A$ is equivalent to $\mathbf { Y } \in B { \mathrm {  —  { t h e y } } }$ are the same event. So $P ( \mathbf { X } \in A ) = P ( \mathbf { Y } \in B )$ , which shows that

$$
\int_ {A} f _ {\mathbf {X}} (\mathbf {x}) d \mathbf {x} = \int_ {B} f _ {\mathbf {Y}} (\mathbf {y}) d \mathbf {y}.
$$

The change of variables formula from multivariable calculus (which is reviewed in the math appendix) can then be applied to the integral on the left-hand side, with the substitution $\mathbf { x } = g ^ { - 1 } ( \mathbf { y } )$

h 8.1.8. A crucial conceptual difference between transformations of discrete r.v.s and transformations of continuous r.v.s is that with discrete r.v.s we don’t need a Jacobian, while with continuous r.v.s we do need a Jacobian. For example, let X be a positive r.v. and $Y = X ^ { 3 }$ . If X is discrete, then

$$
P (Y = y) = P (X = y ^ {1 / 3})
$$

converts between the PMFs. But if X is continuous, we need a Jacobian (which in one dimension is just a derivative) to convert between the PDFs:

$$
f _ {Y} (y) = f _ {X} (x) \frac {d x}{d y} = f _ {X} (y ^ {1 / 3}) \frac {1}{3 y ^ {2 / 3}}.
$$

Exercise 23 is a cautionary tale about someone who failed to use a Jacobian when it was needed.

The next two examples apply the 2D change of variables formula.

Example 8.1.9 (Box-Muller). Let $U \sim \mathrm { U n i f } ( 0 , 2 \pi )$ , and let $T \sim \mathrm { E x p o ( 1 ) }$ be independent of U. Define

$$
X = \sqrt {2 T} \cos U \text {and} Y = \sqrt {2 T} \sin U.
$$

Find the joint PDF of $( X , Y )$ . Are they independent? What are their marginal distributions?

Solution:

The joint PDF of U and $T$ is

$$
f _ {U, T} (u, t) = \frac {1}{2 \pi} e ^ {- t},
$$

for $u \in ( 0 , 2 \pi )$ and $t > 0$ . Viewing $( X , Y )$ as a point in the plane,

$$
X ^ {2} + Y ^ {2} = 2 T (\cos^ {2} U + \sin^ {2} U) = 2 T
$$

is the squared distance from the origin and $U$ is the angle; that is, $( { \sqrt { 2 T } } , U )$ expresses $( X , Y )$ in polar coordinates.

Since we can recover $( U , T )$ from $( X , Y )$ , the transformation is invertible. The Jacobian matrix

$$
\frac {\partial (x , y)}{\partial (u , t)} = \left( \begin{array}{l l} - \sqrt {2 t} \sin u & \frac {1}{\sqrt {2 t}} \cos u \\ \sqrt {2 t} \cos u & \frac {1}{\sqrt {2 t}} \sin u \end{array} \right)
$$

exists, has continuous entries, and has absolute determinant

$$
\mid - \sin^ {2} u - \cos^ {2} u \mid = 1
$$

(which is never 0). Then letting $x = { \sqrt { 2 t } }$ cos u, $y = { \sqrt { 2 t } }$ sin u to mirror the transformation from $( U , T )$ to $( X , Y )$ , we have

$$
\begin{array}{l} f _ {X, Y} (x, y) = f _ {U, T} (u, t) \cdot | \left| \frac {\partial (u , t)}{\partial (x , y)} \right| | \\ = \frac {1}{2 \pi} e ^ {- t} \cdot 1 \\ = \frac {1}{2 \pi} e ^ {- \frac {1}{2} (x ^ {2} + y ^ {2})} \\ = \frac {1}{\sqrt {2 \pi}} e ^ {- x ^ {2} / 2} \cdot \frac {1}{\sqrt {2 \pi}} e ^ {- y ^ {2} / 2}, \\ \end{array}
$$

for all real x and $y .$

The joint PDF $f _ { X , Y }$ factors into a function of x times a function of $y ,$ so $X$ and $Y$ are independent. Furthermore, we recognize the joint PDF as the product of two standard Normal PDFs, so X and Y are i.i.d. $\mathcal { N } ( 0 , 1 )$ r.v.s! This result is called the Box-Muller method for generating Normal r.v.s. 

Example 8.1.10 (Bivariate Normal joint PDF). In Chapter $7 ,$ we saw some properties of the Bivariate Normal distribution and found its joint MGF. Now let’s find its joint PDF.

Let $( Z , W )$ be BVN with $\mathcal { N } ( 0 , 1 )$ marginals and $\operatorname { C o r r } ( Z , W ) = \rho .$ (If we want the joint PDF when the marginals are not standard Normal, we can standardize both components separately and use the result below.) Assume that $- 1 < \rho < 1$ since otherwise the distribution is degenerate (with $Z$ and W perfectly correlated).

As shown in Example 7.5.10, we can construct (Z, W) as

$$
Z = X
$$

$$
W = \rho X + \tau Y,
$$

with $\tau = \sqrt { 1 - \rho ^ { 2 } }$ and X, Y i.i.d. $\mathcal { N } ( 0 , 1 )$ . We also need the inverse transformation. Solving $Z = X$ for X, we have $X = Z .$ Plugging this into $W = \rho X   +   \tau Y$ and solving for $Y ,$ we have

$$
X = Z
$$

$$
Y = - \frac {\rho}{\tau} Z + \frac {1}{\tau} W.
$$

The Jacobian is

$$
\frac {\partial (x , y)}{\partial (z , w)} = \left( \begin{array}{c c} 1 & 0 \\ - \frac {\rho}{\tau} & \frac {1}{\tau} \end{array} \right),
$$

which has absolute determinant $1 / \tau$ . So by the change of variables formula,

$$
\begin{array}{l} f _ {Z, W} (z, w) = f _ {X, Y} (x, y) \cdot | \left| \frac {\partial (x , y)}{\partial (z , w)} \right| | \\ = \frac {1}{2 \pi \tau} \exp \left(- \frac {1}{2} (x ^ {2} + y ^ {2})\right) \\ = \frac {1}{2 \pi \tau} \exp \left(- \frac {1}{2} (z ^ {2} + (- \frac {\rho}{\tau} z + \frac {1}{\tau} w) ^ {2})\right) \\ = \frac {1}{2 \pi \tau} \exp \left(- \frac {1}{2 \tau^ {2}} (z ^ {2} + w ^ {2} - 2 \rho z w)\right), \text {for all real} z, w. \\ \end{array}
$$

In the last step we multiplied things out and used the fact that $\rho ^ { 2 } + \tau ^ { 2 } = 1$

## 8.2 Convolutions

A convolution is a sum of independent random variables. As we mentioned earlier, we often add independent r.v.s because the sum is a useful summary of an experiment (in n Bernoulli trials, we may only care about the total number of successes), and because sums lead to averages, which are also useful (in n Bernoulli trials, the proportion of successes).

The main task in this section is to determine the distribution of $T   =   X + Y$ where X and Y are independent r.v.s whose distributions are known. In previous chapters, we’ve already seen how stories and MGFs can help us accomplish this task. For example, we used stories to show that the sum of independent Binomials with the same success probability is Binomial, and that the sum of i.i.d. Geometrics is Negative Binomial. We used MGFs to show that a sum of independent Normals is Normal.

A third method for obtaining the distribution of $T$ is by using a convolution sum $o r$ integral. The formulas are given in the following theorem. As we’ll see, a convolution sum is nothing more than the law of total probability, conditioning on the value of either $X$ or $Y ;$ a convolution integral is analogous.

Theorem 8.2.1 (Convolution sums and integrals). Let X and $Y$ be independent r.v.s and $T = X + Y$ be their sum. If X and $Y$ are discrete, then the PMF of $T$ is

$$
\begin{array}{l} P (T = t) = \sum_ {x} P (Y = t - x) P (X = x) \\ = \sum_ {y} P (X = t - y) P (Y = y). \\ \end{array}
$$

If X and $Y$ are continuous, then the PDF of $T$ is

$$
\begin{array}{l} f _ {T} (t) = \int_ {- \infty} ^ {\infty} f _ {Y} (t - x) f _ {X} (x) d x \\ = \int_ {- \infty} ^ {\infty} f _ {X} (t - y) f _ {Y} (y) d y. \\ \end{array}
$$

Proof. For the discrete case, we use LOTP, conditioning on $X$ :

$$
\begin{array}{l} P (T = t) = \sum_ {x} P (X + Y = t | X = x) P (X = x) \\ = \sum_ {x} P (Y = t - x | X = x) P (X = x) \\ = \sum_ {x} P (Y = t - x) P (X = x). \\ \end{array}
$$

Conditioning on $Y$ instead, we obtain the second formula for the PMF of $T .$

h 8.2.2. We use the assumption that X and $Y$ are independent in order to get from $P ( Y = t - x | X = x )$ to $P ( Y = t - x )$ in the last step. We are only justified in dropping the condition $X = x$ if the conditional distribution of $Y$ given $X = x$ is the same as the marginal distribution of $Y$ , i.e., X and $Y$ are independent. A common mistake is to assume that after plugging in x for $X$ , we’ve “already used the information” that $X = x$ , when in fact we need an independence assumption to drop the condition. Otherwise we destroy information without justification.

In the continuous case, since the value of a PDF at a point is not a probability, we

first find the CDF, and then differentiate to get the PDF. By LOTP,

$$
\begin{array}{l} F _ {T} (t) = P (X + Y \leq t) = \int_ {- \infty} ^ {\infty} P (X + Y \leq t | X = x) f _ {X} (x) d x \\ = \int_ {- \infty} ^ {\infty} P (Y \leq t - x) f _ {X} (x) d x \\ = \int_ {- \infty} ^ {\infty} F _ {Y} (t - x) f _ {X} (x) d x. \\ \end{array}
$$

Again, we need independence to drop the condition $X = x$ . To get the PDF, we then differentiate with respect to $t ,$ interchanging the order of integration and differentiation. This gives

$$
f _ {T} (t) = \int_ {- \infty} ^ {\infty} f _ {Y} (t - x) f _ {X} (x) d x.
$$

Conditioning on $Y$ instead, we get the second formula for $f _ { T }$

An alternative derivation uses the change of variables formula in two dimensions. The only snag is that the change of variables formula requires an invertible transformation from $\mathbb { R } ^ { 2 }$ to $\mathbb { R } ^ { 2 }$ , but $( X , Y ) \mapsto X + Y$ maps $\mathbb { R } ^ { 2 }$ to R and is not invertible. We can get around this by adding a redundant component to the transformation, in order to make it invertible. Accordingly, we consider the invertible transformation $( X , Y ) \mapsto ( X + Y , X )$ (using $( X , Y ) \mapsto ( X + Y , Y )$ would be equally valid). Once we have the joint PDF of $X + Y$ and $X$ , we integrate out $X$ to get the marginal PDF of $X + Y$

Let $T   =   X + Y ,   W   =   X$ , and let $t   =   x   +   y ,   w   =   x$ . It may seem redundant to give X the new name ${ } ^ { \backprime } W ^ { \flat }$ , but doing this makes it easier to distinguish between pre-transformation variables and post-transformation variables: we are transforming $( X , Y ) \mapsto ( T , W )$ . Then

$$
\frac {\partial (t , w)}{\partial (x , y)} = \left( \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right)
$$

has absolute determinant equal to 1, so $\mid \left[ \frac { \partial ( x ,   y ) } { \partial ( t ,   w ) } \right] \mid$ is also 1. Thus, the joint PDF of $T$ and $W$ is

$$
f _ {T, W} (t, w) = f _ {X, Y} (x, y) = f _ {X} (x) f _ {Y} (y) = f _ {X} (w) f _ {Y} (t - w),
$$

and the marginal PDF of $T$ is

$$
f _ {T} (t) = \int_ {- \infty} ^ {\infty} f _ {T, W} (t, w) d w = \int_ {- \infty} ^ {\infty} f _ {X} (x) f _ {Y} (t - x) d x,
$$

in agreement with our result above.

h 8.2.3. It is not hard to remember the convolution integral formula by reasoning by analogy from

$$
P (T = t) = \sum_ {x} P (Y = t - x) P (X = x)
$$

to

$$
f _ {T} (t) = \int_ {- \infty} ^ {\infty} f _ {Y} (t - x) f _ {X} (x) d x.
$$

But care is still needed. For example, Exercise 23 shows that an analogous-looking formula for the PDF of the product of two independent continuous r.v.s is wrong: a Jacobian is needed (for convolutions, the absolute Jacobian determinant is 1 so it isn’t noticeable in the convolution integral formula).

Since convolution sums are just the law of total probability, we have already used them in previous chapters without mentioning the word convolution; see, for example, the first and most tedious proof of Theorem 3.8.9 (sum of independent Binomials), as well as the proof of Theorem 4.8.1 (sum of independent Poissons). In the following examples, we find the distribution of a sum of Exponentials and a sum of Uniforms using a convolution integral.

Example 8.2.4 (Exponential convolution). Let $X , Y \stackrel { \mathrm { i . i . d . } } { \sim } \operatorname { E x p o } ( \lambda )$ . Find the distribution of $T = X + Y$

Solution:

For $t > 0$ , the convolution formula gives

$$
f _ {T} (t) = \int_ {- \infty} ^ {\infty} f _ {Y} (t - x) f _ {X} (x) d x = \int_ {0} ^ {t} \lambda e ^ {- \lambda (t - x)} \lambda e ^ {- \lambda x} d x,
$$

where we restricted the integral to be from 0 to t since we need $t - x > 0$ and $x > 0$ for the PDFs inside the integral to be nonzero. Simplifying, we have

$$
f _ {T} (t) = \lambda^ {2} \int_ {0} ^ {t} e ^ {- \lambda t} d x = \lambda^ {2} t e ^ {- \lambda t}, \text {for} t > 0.
$$

This is known as the Gamma(2, λ) distribution. We will introduce the Gamma distribution in detail in Section 8.4. 

Example 8.2.5 (Uniform convolution). Let $X , Y { \overset { \mathrm { ~ i . i . d . ~ } } { \sim } } \mathrm { U n i f } ( 0 , 1 )$ . Find the distribution of $T = X + Y$

Solution:

The PDF of X (and of Y ) is

$$
g (x) = \left\{ \begin{array}{l l} 1, & x \in (0, 1), \\ 0, & \text {otherwise}. \end{array} \right.
$$

The convolution formula gives

$$
f _ {T} (t) = \int_ {- \infty} ^ {\infty} f _ {Y} (t - x) f _ {X} (x) d x = \int_ {- \infty} ^ {\infty} g (t - x) g (x) d x.
$$

The integrand is 1 if and only if $0 < t   -   x < 1$ and $0 < x < 1$ ; this is a parallelogramshaped constraint. Equivalently, the constraint is max $( 0 , t - 1 ) < x < \operatorname* { m i n } ( t , 1 )$

![](images/page_395_chart_2.jpg)

<details>
<summary>area</summary>

| t | x (Lower Bound) | x (Upper Bound) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 1.0 | 0.0 | 1.0 |
| 2.0 | 1.0 | 1.0 |
</details>

## FIGURE 8.2

Region in the (t, x)-plane where $g(t - x)g(x)$ is 1.

From Figure 8.2, we see that for $0 < t \leq 1$ , x is constrained to be in $( 0 , t )$ , and for $1 < t < 2 ,$ x is constrained to be in $( t   -   1 , 1 )$ . Therefore, the PDF of T is a piecewise linear function:

$$
f _ {T} (t) = \left\{ \begin{array}{l l} \int_ {0} ^ {t} d x = t & \text {for} 0 <   t \leq 1, \\ \int_ {t - 1} ^ {1} d x = 2 - t & \text {for} 1 <   t <   2. \end{array} \right.
$$

Figure 8.3 plots the PDF of T. It is shaped like a triangle with vertices at 0, 1, and 2, so it is called the Triangle(0, 1, 2) distribution.

Heuristically, it makes sense that T is more likely to take on values near the middle than near the extremes: a value near 1 can be obtained if both X and Y are moderate, if X is large but Y is small, or if Y is large but X is small. In contrast, a value near 2 is only possible if both X and Y are large. Thinking back to Example 3.2.5, the PMF of the sum of two die rolls was also shaped like a triangle. A single die roll has a Discrete Uniform distribution on the integers 1 through 6, so in that problem we were looking at a convolution of two Discrete Uniforms. It makes sense that the PDF we obtained here is similar in shape. 

## 8.3 Beta

In this section and the next, we will introduce two continuous distributions, the Beta and Gamma, which are related to several named distributions we have already

![](images/page_396_chart_2.jpg)

<details>
<summary>line</summary>

| t | PDF |
| --- | --- |
| 0.0 | 0.0 |
| 1.0 | 1.0 |
| 2.0 | 0.0 |
</details>

## FIGURE 8.3

PDF of $T = X + Y$ , where X and Y are i.i.d. Unif(0, 1).

studied and are also related to each other via a shared story. This is an interlude from the subject of transformations, but we’ll eventually need to use a change of variables to tie the Beta and Gamma distributions together.

The Beta distribution is a continuous distribution on the interval $( 0 , 1 )$ . It is a generalization of the $\mathrm { U n i f } ( 0 , 1 )$ distribution, allowing the PDF to be non-constant on (0, 1).

Definition 8.3.1 (Beta distribution). An r.v. X is said to have the Beta distribution with parameters a and b, where $a > 0$ and $b > 0$ , if its PDF is

$$
f (x) = \frac {1}{\beta (a , b)} x ^ {a - 1} (1 - x) ^ {b - 1}, \quad 0 <   x <   1,
$$

where the constant $\beta ( a , b )$ is chosen to make the PDF integrate to 1. We write this as $X \sim \mathrm { B e t a } ( a , b )$

Taking $a = b = 1$ , the $\mathrm { B e t a } ( 1 , 1 )$ PDF is constant on $( 0 , 1 )$ , so the Beta(1, 1) and $\mathrm { U n i f } ( 0 , 1 )$ distributions are the same. By varying the values of $a$ and $b ,$ we get PDFs with a variety of shapes; Figure 8.4 shows four examples. Here are a couple of general patterns:

• If $a < 1$ and $b < 1$ , the PDF is U-shaped and opens upward. If $a > 1$ and $b > 1$ the PDF opens down.
• If $a = b .$ the PDF is symmetric about $1 / 2$ . If $a > b ,$ the PDF favors values larger than $1 / 2 ; { \mathrm { ~ i f ~ } } a < b$ , the PDF favors values smaller than $1 / 2$

By definition, the constant $\beta ( a , b )$ satisfies

$$
\beta (a, b) = \int_ {0} ^ {1} x ^ {a - 1} (1 - x) ^ {b - 1} d x.
$$

![](images/page_397_image_2.jpg)

FIGURE 8.4

Beta PDFs for various values of a and b. Clockwise from top left: Beta(0.5, 0.5), Beta(2, 1), Beta(5, 5), Beta(2, 8).

An integral of this form is called a beta integral, and we will need to do some calculus to derive a general formula for $\beta ( a , b )$ . But in the special case where a and b are positive integers, Thomas Bayes figured out how to do the integral using a story proof rather than calculus!

Story 8.3.2 (Bayes’ billiards). Show without using calculus that for any integers k and n with $0 \leq k \leq n$

$$
\int_ {0} ^ {1} \binom {n} {k} x ^ {k} (1 - x) ^ {n - k} d x = \frac {1}{n + 1}.
$$

## Solution:

By telling two stories, we will show that the left-hand and right-hand sides are both equal to $P ( X = k )$ , where X is an r.v. that we will construct.

Story 1 : Start with $n { + } 1$ balls, n white and 1 gray. Randomly throw each ball onto the unit interval [0, 1], such that the positions of the balls are i.i.d. $\mathrm { U n i f } ( 0 , 1 )$ . Let X be the number of white balls to the left of the gray ball; X is a discrete r.v. with possible values $0 , 1 , \ldots , n$ . Figure 8.5 illustrates the setup of our experiment.

To get the probability of the event $X = k$ , we use LOTP, conditioning on the position of the gray ball, which we’ll call B. Conditional on $B = p ,$ the number of white balls landing to the left of $p$ has a $\operatorname { B i n } ( n , p )$ distribution, since we can consider each of the white balls to be an independent Bernoulli trial, where success is defined as landing to the left of $p .$ Let $f$ be the PDF of $B ;   f ( p ) = 1$ since $B \sim \mathrm { U n i f } ( 0 , 1 )$ . So

$$
P (X = k) = \int_ {0} ^ {1} P (X = k | B = p) f (p) d p = \int_ {0} ^ {1} \binom{n}{k} p ^ {k} (1 - p) ^ {n - k} d p.
$$

![](images/page_398_image_10.jpg)

<details>
<summary>text_image</summary>

0
1
</details>

## FIGURE 8.5

Bayes’ billiards. Here we throw $n = 6$ white balls and one gray ball onto the unit interval, and we observe $X = 2$ balls to the left of the gray ball.

Story 2 : Start with $n + 1$ balls, all white. Randomly throw each ball onto the unit interval; then choose one ball at random and paint it gray. Again, let X be the number of white balls to the left of the gray ball. By symmetry, any one of the $n + 1$ balls is equally likely to be painted gray, so

$$
P (X = k) = \frac {1}{n + 1}
$$

for $k = 0 , 1 , \ldots , n .$

Here’s the crux: X has the same distribution in the two stories! It does not matter whether we paint the gray ball first and then throw, or whether we throw first and then paint the gray ball. So $P ( X = k )$ is the same in Story 1 and Story 2, and

$$
\int_ {0} ^ {1} \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} d p = \frac {1}{n + 1}
$$

for $k = 0 , 1 , \ldots , n$ . Despite the $k ^ { \prime } \mathrm { s }$ in the integrand, the value of the integral doesn’t depend on k. Substituting $a   -   1$ for k and $b   -   1$ for $n - k$ , this shows that for positive integer values of a and $b ,$

$$
\beta (a, b) = \frac {1}{(a + b - 1) \binom {a + b - 2} {a - 1}} = \frac {(a - 1) ! (b - 1) !}{(a + b - 1) !}.
$$

Later in this chapter, we’ll learn what $\beta ( a , b )$ is for general $a$ and $b .$

![](images/page_399_image_7.jpg)

The Beta is a flexible family of distributions on (0, 1), and has many stories. One of these stories is that a Beta r.v. is often used to represent an unknown probability. That is, we can use the Beta to put probabilities on unknown probabilities!

Story 8.3.3 (Beta-Binomial conjugacy). We have a coin that lands Heads with probability $p ,$ but we don’t know what $p$ is. Our goal is to $i n f e r$ the value of $p$ after observing the outcomes of $n$ tosses of the coin. The larger that $n$ is, the more accurately we should be able to estimate $p .$

There are several ways to go about doing this. One major approach is Bayesian inference, which treats all unknown quantities as random variables. In the Bayesian approach, we would treat the unknown probability $p$ as a random variable and give $p$ a distribution. This is called a prior distribution, and it reflects our uncertainty about the true value of $p$ before observing the coin tosses. After the experiment is performed and the data are gathered, the prior distribution is updated using Bayes rule; this yields the posterior distribution, which reflects our new beliefs about $p .$

Let’s see what happens if the prior distribution on $p$ is a Beta distribution. Let $p \sim \mathrm { B e t a } ( a , b )$ for known constants $a$ and $b ,$ and let X be the number of Heads in n tosses of the coin. Conditional on knowing the true value of $p ,$ the tosses would just be independent Bernoulli trials with probability $p$ of success, so

$$
X | p \sim \operatorname{Bin} (n, p).
$$

Note that X is not marginally Binomial; it is conditionally Binomial, given $p .$ The marginal distribution of X is called the Beta-Binomial distribution. To get the posterior distribution of $p ,$ we use Bayes’ rule (in a hybrid form, since X is discrete and $p$ is continuous). Letting $f ( p )$ be the prior distribution and $f ( p | X = k )$ be the