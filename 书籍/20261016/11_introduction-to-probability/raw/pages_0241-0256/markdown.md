## 5.3 Universality of the Uniform

In this section, we will discuss a remarkable property of the Uniform distribution: given a Unif(0, 1) r.v., we can construct an r.v. with any continuous distribution we want. Conversely, given an r.v. with an arbitrary continuous distribution, we can create a Unif(0, 1) r.v. We call this the universality of the Uniform, because it tells us the Uniform is a universal starting point for building r.v.s with other distributions. Universality of the Uniform also goes by many other names, such as the probability integral transform, inverse transform sampling, the quantile transformation, and even the fundamental theorem of simulation.

To keep the proofs simple, we will state universality of the Uniform for a case where we know the inverse of the desired CDF exists. Similar ideas can be used to simulate a random draw from any desired CDF as a function of a Unif(0, 1) r.v.

Theorem 5.3.1 (Universality of the Uniform). Let F be a CDF which is a continuous function and strictly increasing on the support of the distribution. This ensures that the inverse function $F ^ { - 1 }$ exists, as a function from (0, 1) to R. We then have the following results.

1. Let $U \sim \mathrm { U n i f } ( 0 , 1 )$ and $X = F ^ { - 1 } ( U )$ . Then X is an r.v. with CDF F.
2. Let X be an r.v. with CDF F. Then $F ( X ) \sim \operatorname { U n i f } ( 0 , 1 )$

Let’s make sure we understand what each part of the theorem is saying. The first part says that if we start with $U \sim \mathrm { U n i f } ( 0 , 1 )$ and a CDF F, then we can create an r.v. whose CDF is F by plugging U into the inverse CDF $F ^ { - 1 }$ . Since $F ^ { - 1 }$ is a function (known as the quantile function), U is an r.v., and a function of an r.v. is an r.v., $F ^ { - 1 } ( U )$ is an r.v.; universality of the Uniform says its CDF is F.

The second part of the theorem goes in the reverse direction, starting from an r.v. X whose CDF is F and then creating a Unif(0, 1) r.v. Again, F is a function, X is an r.v., and a function of an r.v. is an r.v., so $F ( X )$ is an r.v. Since any CDF is between 0 and 1 everywhere, $F ( X )$ must take values between 0 and 1. Universality of the Uniform says that the distribution of $F ( X )$ is Uniform on (0, 1).

h 5.3.2. The second part of universality of the Uniform involves plugging a random variable X into its own CDF F. This may seem strangely self-referential, but it makes sense because F is just a function (that satisfies the properties of a valid CDF), and a function of an r.v. is an r.v. There is a potential notational confusion, however: $F(x) = P(X \leq x)$ by definition, but it would be incorrect to say $\text{" }F(X)=$ $P ( X   \leq   X )   =   1$ Rather, we should first find an expression for the CDF as a function of x, then replace x with X to obtain an r.v. For example, if the CDF of X is $F ( x ) = 1 - e ^ { - x }$ for $x > 0$ , then $F ( X ) = 1 - e ^ { - X }$

Understanding the statement of the theorem is the difficult part; the proof is just a couple of lines for each direction.

Proof.

1. Let $U \sim \mathrm { U n i f } ( 0 , 1 )$ and $X = F ^ { - 1 } ( U )$ . For all real $x .$

$$
P (X \leq x) = P (F ^ {- 1} (U) \leq x) = P (U \leq F (x)) = F (x),
$$

so the CDF of X is $F ,$ as claimed. For the last equality, we used the fact that $P ( U \leq u ) = u$ for $u \in ( 0 , 1 )$

2. Let X have CDF $F ,$ and find the CDF of $Y = F ( X )$ . Since Y takes values in $( 0 , 1 )$ $P ( Y \leq y )$ equals 0 for $y \leq 0$ and equals 1 for $y \geq 1$ . For $y \in ( 0 , 1 )$

$$
P (Y \leq y) = P (F (X) \leq y) = P (X \leq F ^ {- 1} (y)) = F (F ^ {- 1} (y)) = y.
$$

Thus Y has the $\mathrm { U n i f } ( 0 , 1 )$ CDF.

To gain more insight into what the quantile function $F ^ { - 1 }$ and universality of the Uniform mean, let’s consider an example that is familiar to millions of students: percentiles on an exam.

Example 5.3.3 (Percentiles). A large number of students take a certain exam, graded on a scale from 0 to 100. Let X be the score of a random student. Continuous distributions are easier to deal with here, so let’s approximate the discrete distribution of scores using a continuous distribution. Suppose that X is continuous, with a CDF F that is strictly increasing on (0, 100). In reality, there are only finitely many students and only finitely many possible scores, but a continuous distribution may be a good approximation.

Suppose that the median score on the exam is 60, i.e., half of the students score above 60 and the other half score below 60 (a convenient aspect of assuming a continuous distribution is that we don’t need to worry about how many students had scores equal to 60). That is, $F ( 6 0 ) = 1 / 2$ , or, equivalently, $F ^ { - 1 } ( 1 / 2 ) = 6 0$

If Fred scores a 72 on the exam, then his percentile is the fraction of students who score below a 72. This is $F ( 7 2 )$ , which is some number in $( 1 / 2 , 1 )$ since 72 is above the median. In general, a student with score x has percentile $F ( x )$ . Going the other way, if we start with a percentile, say 0.95, then $F ^ { - 1 } ( 0 . 9 5 )$ is the score that has that percentile. A percentile is also called a quantile, which is why $F ^ { - 1 }$ is called the quantile function. The function $F$ converts scores to quantiles, and the function $F ^ { - 1 }$ converts quantiles to scores.

The strange operation of plugging X into its own CDF now has a natural interpretation: $F ( X )$ is the percentile attained by a random student. It often happens that the distribution of scores on an exam looks very non-Uniform. For example, there is no reason to think that 10% of the scores are between $7 0$ and 80, even though (70, 80) covers 10% of the range of possible scores.

On the other hand, the distribution of percentiles of the students is Uniform: the universality property says that $F ( X ) \sim \operatorname { U n i f } ( 0 , 1 )$ . For example, 50% of the students have a percentile of at least 0.5. Universality of the Uniform is expressing the fact that 10% of the students have a percentile between 0 and 0.1, 10% have a percentile between 0.1 and 0.2, 10% have a percentile between 0.2 and 0.3, and so on—a fact that is clear from the definition of percentile. 

To illustrate universality of the Uniform, we will apply it to the two distributions we encountered in the previous section, the Logistic and Rayleigh.

Example 5.3.4 (Universality with Logistic). The Logistic CDF is

$$
F (x) = \frac {e ^ {x}}{1 + e ^ {x}}, \quad x \in \mathbb {R}.
$$

Suppose we have $U \sim \mathrm { U n i f } ( 0 , 1 )$ and wish to generate a Logistic r.v. Part 1 of the universality property says that $F ^ { - 1 } ( U ) \sim$ Logistic, so we first invert the CDF to get $F ^ { - 1 }$

$$
F ^ {- 1} (u) = \log \left(\frac {u}{1 - u}\right).
$$

Then we plug in U for u:

$$
F ^ {- 1} (U) = \log \left(\frac {U}{1 - U}\right).
$$

Therefore log $\begin{array} { r } { \left( \frac { U } { 1 - U } \right) \sim \mathrm { L o g i s t i c } } \end{array}$

We can verify directly that log $\left( { \frac { U } { 1 { - } U } } \right)$ has the required CDF: start from the definition of CDF, do some algebra to isolate U on one side of the inequality, and then use the CDF of the Uniform distribution. Let’s work through these calculations once for practice:

$$
\begin{array}{l} P \left(\log \left(\frac {U}{1 - U}\right) \leq x\right) = P \left(\frac {U}{1 - U} \leq e ^ {x}\right) \\ = P \left(U \leq e ^ {x} (1 - U)\right) \\ = P \left(U \leq \frac {e ^ {x}}{1 + e ^ {x}}\right) \\ = \frac {e ^ {x}}{1 + e ^ {x}}, \\ \end{array}
$$

which is indeed the Logistic CDF.

We can also use simulation to visualize how universality of the Uniform works. To this end, we generated 1 million Unif(0, 1) random variables. We then transformed each of these values u into log $\left( { \frac { u } { 1 - u } } \right)$ ; if the universality of the Uniform is correct, the transformed numbers should follow a Logistic distribution.

![](images/page_243_image_2.jpg)

## FIGURE 5.7

Top: Histogram of $1 0 ^ { 6 }$ draws of $U \sim \mathrm { U n i f } ( 0 , 1 )$ , with $\mathrm { U n i f } ( 0 , 1 )$ PDF for comparison. Bottom: Histogram of $1 0 ^ { 6 }$ draws of log $\left( { \frac { U } { 1 { - } U } } \right)$ , with Logistic PDF for comparison.

Figure 5.7 displays a histogram of the realizations of U alongside the $\mathrm { U n i f } ( 0 , 1 )$ PDF; below that, we have a histogram of the realizations of log $\left( { \frac { U } { 1 { - } U } } \right)$ next to the Logistic PDF. As we can see, the second histogram looks very much like the Logistic PDF. Thus, by applying $F ^ { - 1 }$ , we were able to transform our Uniform draws into Logistic draws, exactly as claimed by the universality of the Uniform.

Conversely, Part 2 of the universality property states that if X ∼ Logistic, then

$$
F (X) = \frac {e ^ {X}}{1 + e ^ {X}} \sim \mathrm{Unif} (0, 1).
$$

Example 5.3.5 (Universality with Rayleigh). The Rayleigh CDF is

$$
F (x) = 1 - e ^ {- x ^ {2} / 2}, \quad x > 0.
$$

The quantile function (the inverse of the CDF) is

$$
F ^ {- 1} (u) = \sqrt {- 2 \log (1 - u)},
$$

so if $U \sim \mathrm { U n i f } ( 0 , 1 )$ , then $F ^ { - 1 } ( U ) = { \sqrt { - 2 \log ( 1 - U ) } } \sim \mathrm { R a y l e i g h }$

We again generated 1 million realizations of $U \sim \mathrm { U n i f } ( 0 , 1 )$ and transformed them

![](images/page_244_image_2.jpg)

## FIGURE 5.8

Top: Histogram of 1 million draws from $U \sim \mathrm { U n i f } ( 0 , 1 )$ , with $\mathrm { U n i f } ( 0 , 1 )$ PDF for comparison. Bottom: Histogram of 1 million draws from $\sqrt { - 2 \log ( 1 - U ) }$ , with Rayleigh PDF for comparison.

to produce 1 million realizations of $\sqrt { - 2 \log ( 1 - U ) }$ . As Figure 5.8 shows, the realizations of $\sqrt { - 2 \log ( 1 - U ) }$ look very similar to the Rayleigh PDF, as predicted by the universality of the Uniform.

Conversely, if X ∼ Rayleigh, then $F ( X ) = 1 - e ^ { - X ^ { 2 } / 2 } \sim \mathrm { U n i f } ( 0 , 1 )$

Next, let us consider the extent to which universality of the Uniform holds for discrete random variables. The CDF F of a discrete r.v. has jumps and flat regions, so $F ^ { - 1 }$ does not exist (in the usual sense). But Part 1 still holds in the sense that given a Uniform random variable, we can construct an r.v. with any discrete distribution we want. The difference is that instead of working with the CDF, which is not invertible, it is more straightforward to work with the PMF.

Suppose we want to use $U   \sim   \mathrm { U n i f } ( 0 , 1 )$ to construct a discrete r.v. X with PMF $p _ { j } = P ( X = j )$ for $j = 0 , 1 , 2 , \ldots , n$ . As illustrated in Figure 5.9, we can chop up the interval $( 0 , 1 )$ into pieces of lengths $p _ { 0 } , p _ { 1 } , \ldots , p _ { n }$ . By the properties of a valid PMF, the sum of the ${ p _ { j } } ^ { \prime } \mathrm { s }$ is 1, so this perfectly divides up the interval, without overshooting or undershooting.

Now define X to be the r.v. which equals 0 if U falls into the $p _ { 0 }$ interval, 1 if U falls into the $p _ { 1 }$ interval, 2 if U falls into the $p _ { 2 }$ interval, and so on. Then X is a discrete

![](images/page_245_image_2.jpg)

<details>
<summary>text_image</summary>

0 1 2 ... n-1 n
| | | | | | | |
p₀ p₁ p₂ pₙ₋₁ pₙ
</details>

## FIGURE 5.9

Given a PMF, chop up the interval (0, 1) into pieces, with lengths given by the PMF values.

r.v. taking on values 0 through n. The probability that $X = j$ is the probability that U falls into the interval of length $p _ { j }$ . But for a Unif(0, 1) r.v., probability is length, so $P ( X = j )$ is precisely $p _ { j }$ , as desired!

The same trick will work for a discrete r.v. that can take on infinitely many values, such as a Poisson; we’ll need to chop (0, 1) into infinitely many pieces, but the total length of the pieces is still 1.

We now know how to take an arbitrary PMF and create an r.v. with that PMF. This fulfills our promise from Chapter 3 that any function with the properties given in Theorem 3.2.7 is the PMF of some r.v.

h 5.3.6. Part 2 of universality of the Uniform, on the other hand, fails for discrete r.v.s. A function of a discrete r.v. is still discrete, so if X is discrete, then $F ( X )$ is still discrete. So $F ( X )$ doesn’t have a Uniform distribution. For example, if $X \sim \mathrm { B e r n } ( p )$ then F(X) has only two possible values: $F ( 0 ) = 1 - p$ and $F ( 1 ) = 1$

The upshot of universality is that we can use a Uniform r.v. U to generate r.v.s from both continuous and discrete distributions: in the continuous case, we can plug U into the inverse CDF, and in the discrete case, we can chop up the unit interval according to the desired PMF. Part 1 of universality of the Uniform is often useful in practice when running simulations (since the software being used may know how to generate Uniform r.v.s but not know how to generate r.v.s with the distribution of interest), though the extent to which it is useful depends on how tractable it is to compute the inverse CDF. Part 2 is important for certain widely used techniques in statistical inference, by providing a transformation that converts an r.v. with an unknown distribution to an r.v. with a known, simple distribution: the Uniform.

Using our analogy of distributions as blueprints and r.v.s as houses, the beauty of the universality property is that the Uniform distribution is a very simple blueprint, and it’s easy to create a house from that blueprint; universality of the Uniform then gives us a simple rule for remodeling the Uniform house into a house with any other blueprint, no matter how complicated!

To conclude this section, we give an elegant identity that is often useful for finding the expectation of a nonnegative r.v. The identity also has a neat visual interpretation related to universality of the Uniform, LOTUS, and the relationship between CDFs and quantile functions.

Definition 5.3.7. The survival function of an r.v. X with CDF F is the function G given by $G(x)=1-F(x)=P(X>x)$

Theorem 5.3.8 (Expectation by integrating the survival function). Let X be a nonnegative r.v. Its expectation can be found by integrating its survival function:

$$
E (X) = \int_ {0} ^ {\infty} P (X > x) d x.
$$

This result is the continuous analog of Theorem 4.4.8 (note though that it holds for any nonnegative r.v., not just for continuous nonnegative r.v.s). Actuaries sometimes call it the Darth Vader rule, for obscure reasons; statisticians are more likely to refer to it as finding the expectation by integrating the survival function.

Proof. For any number $x \geq 0$ , we can write

$$
x = \int_ {0} ^ {x} d t = \int_ {0} ^ {\infty} I (x > t) d t,
$$

where $I ( x > t )$ is 1 if $x \geq t$ and 0 otherwise. So

$$
X (s) = \int_ {0} ^ {\infty} I (X (s) > t) d t,
$$

for each s in the sample space. We can write this more compactly as

$$
X = \int_ {0} ^ {\infty} I (X > t) d t.
$$

Taking the expectation of both sides and swapping the E with the integral (which can be justified using results from real analysis), we have

$$
E (X) = E \left(\int_ {0} ^ {\infty} I (X > t) d t\right) = \int_ {0} ^ {\infty} E (I (X > t)) d t = \int_ {0} ^ {\infty} P (X > t) d t.
$$

For a visual explanation of this identity, we can graph a CDF and interpret a certain area in two different ways: as the integral of the survival function, and as the integral of the quantile function.

A prototypical CDF of a nonnegative, continuous r.v. with CDF F is shown in Figure 5.10, with the area between the CDF curve and the horizontal line $p = 1$ shaded. This area can be found by integrating $1 - F ( x )$ , the difference between the line and the curve, from 0 to ∞.

But another way to find this area is to turn your head sideways and integrate with

![](images/page_247_chart_2.jpg)

<details>
<summary>area</summary>

| Point | X | Y |
| --- | --- | --- |
| Intersection of Curve | ~35 | ~0.75 |
</details>

## FIGURE 5.10

The area above a certain CDF and below the line $p = 1$ is shaded. This area can be interpreted in two ways: as the integral of the survival function, or as the integral of the quantile function.

respect to the vertical axis variable p rather than the horizontal axis variable $x .$ This gives the integral of the quantile function, which, letting $U \sim \mathrm { U n i f } ( 0 , 1 )$ , is

$$
\int_ {0} ^ {1} F ^ {- 1} (p) d p = E (F ^ {- 1} (U)) = E (X),
$$

by LOTUS and universality of the Uniform. So again we have

$$
\int_ {0} ^ {\infty} (1 - F (x)) d x = \int_ {0} ^ {1} F ^ {- 1} (p) d p = E (X).
$$

## 5.4 Normal

The Normal distribution is a famous continuous distribution with a bell-shaped PDF. It is extremely widely used in statistics because of a theorem, the central limit theorem, which says that under very weak assumptions, the sum of a large number of i.i.d. random variables has an approximately Normal distribution, regardless of the distribution of the individual r.v.s. This means we can start with independent r.v.s from almost any distribution, discrete or continuous, but once we add up a bunch of them, the distribution of the resulting r.v. looks like a Normal distribution.

The central limit theorem is a topic for Chapter 10, but in the meantime, we’ll introduce the properties of the Normal PDF and CDF and derive the expectation and variance of the Normal distribution. To do this, we will again use the strategy of location-scale transformation by starting with the simplest Normal distribution, the standard Normal, which is centered at 0 and has variance 1. After deriving the properties of the standard Normal, we’ll be able to get to any Normal distribution we want by shifting and scaling.

Definition 5.4.1 (Standard Normal distribution). A continuous r.v. $Z$ is said to have the standard Normal distribution if its PDF $\varphi$ is given by

$$
\varphi (z) = \frac {1}{\sqrt {2 \pi}} e ^ {- z ^ {2} / 2}, \quad - \infty <   z <   \infty .
$$

We write this as $Z \sim \mathcal { N } ( 0 , 1 )$ since, as we will show, $Z$ has mean 0 and variance 1.

The constant $\frac { 1 } { \sqrt { 2 \pi } }$ in front of the PDF may look surprising (why is something with $\pi$ needed in front of something with $e _ { \gamma }$ when there are no circles in sight?), but it’s exactly what is needed to make the PDF integrate to 1. Such constants are called normalizing constants because they normalize the total area under the PDF to 1. We’ll verify soon that this is a valid PDF.

The standard Normal CDF Φ is the accumulated area under the PDF:

$$
\Phi (z) = \int_ {- \infty} ^ {z} \varphi (t) d t = \int_ {- \infty} ^ {z} \frac {1}{\sqrt {2 \pi}} e ^ {- t ^ {2} / 2} d t.
$$

Some people, upon seeing the function $\Phi$ for the first time, express dismay that it is left in terms of an integral. Unfortunately, we have little choice in the matter: it turns out to be mathematically impossible to find a closed-form expression for the antiderivative of $\varphi ,$ meaning that we cannot express $\Phi$ as a finite sum of more familiar functions like polynomials or exponentials. But closed-form or no, it’s still a well-defined function: if we give Φ an input $z ,$ it returns the accumulated area under the PDF from −∞ up to z.

Notation 5.4.2. We can tell the Normal distribution must be special because the standard Normal PDF and CDF get their own Greek letters. By convention, we use $\varphi$ for the standard Normal PDF and Φ for the CDF. We will often use $Z$ to denote a standard Normal random variable.

The standard Normal PDF and CDF are plotted in Figure 5.11. The PDF is bellshaped and symmetric about 0, and the CDF is S-shaped. These have the same general shape as the Logistic PDF and CDF that we saw Example 5.1.6, but the Normal PDF decays to 0 much more quickly.

There are several important symmetry properties that can be deduced from the standard Normal PDF and CDF.

1. Symmetry of PDF: $\varphi$ satisfies $\varphi ( z ) = \varphi ( - z )$ , i.e., $\varphi$ is an even function.

![](images/page_249_image_2.jpg)

FIGURE 5.11 Standard Normal PDF $\varphi$ (left) and CDF Φ (right).

2. Symmetry of tail areas: The area under the PDF curve to the left of $- 2 ,$ which is $P ( Z \leq - 2 ) = \Phi ( - 2 )$ by definition, equals the area to the right of 2, which is $P ( Z \geq 2 ) = 1 - \Phi ( 2 )$ . In general, we have

$$
\Phi (z) = 1 - \Phi (- z)
$$

for all $之 .$ This can be seen visually by looking at the PDF curve, and mathematically by substituting $u   =   - t$ below and using the fact that PDFs integrate to 1:

$$
\Phi (- z) = \int_ {- \infty} ^ {- z} \varphi (t) d t = \int_ {z} ^ {\infty} \varphi (u) d u = 1 - \int_ {- \infty} ^ {z} \varphi (u) d u = 1 - \Phi (z).
$$

3. Symmetry of $Z$ and $- Z ;$ If $Z \sim \mathcal { N } ( 0 , 1 )$ , then $- Z \sim \mathcal { N } ( 0 , 1 )$ as well. To see this, note that the CDF of $- Z$ is

$$
P (- Z \leq z) = P (Z \geq - z) = 1 - \Phi (- z),
$$

but that is $\Phi ( z )$ , according to what we just argued. So $- Z$ has CDF Φ.

We need to prove three key facts about the standard Normal, and then we’ll be ready to handle general Normal distributions: we need to show that $\varphi$ is a valid PDF, that $E ( Z ) = 0$ , and that $\operatorname { V a r } ( Z ) = 1$

To verify the validity of $\varphi ,$ we’ll show that the total area under $e ^ { - z ^ { 2 } / 2 }$ is $\sqrt { 2 \pi }$ However, we can’t find the antiderivative of $e ^ { - z ^ { 2 } / 2 }$ directly, again because of the annoying fact that the antiderivative isn’t expressible in closed form. But this doesn’t mean we can’t do definite integrals, with some ingenuity.

An amazing trick saves the day here: write down the integral twice. Usually, writing down the same problem repeatedly is more a sign of frustration than a problemsolving strategy. But in this case, it allows a neat conversion to polar coordinates:

$$
\begin{array}{l} \left(\int_ {- \infty} ^ {\infty} e ^ {- z ^ {2} / 2} d z\right) \left(\int_ {- \infty} ^ {\infty} e ^ {- z ^ {2} / 2} d z\right) = \left(\int_ {- \infty} ^ {\infty} e ^ {- x ^ {2} / 2} d x\right) \left(\int_ {- \infty} ^ {\infty} e ^ {- y ^ {2} / 2} d y\right) \\ = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} e ^ {- \frac {x ^ {2} + y ^ {2}}{2}} d x d y \\ = \int_ {0} ^ {2 \pi} \int_ {0} ^ {\infty} e ^ {- r ^ {2} / 2} r d r d \theta . \\ \end{array}
$$

In the first step, we used the fact that z is just a dummy variable in each integral, so we are allowed to give it a different name (or two different names, one for each integral). The extra $r$ that appears in the final step comes from the Jacobian of the transformation to polar coordinates, as explained in Section A.7.2 of the math appendix. That $r$ is also what saves us from the impossibility of the original integral, since we can now use the substitution $u = r ^ { 2 } / 2 ,   d u = r d r$ . This gives

$$
\begin{array}{l} \int_ {0} ^ {2 \pi} \int_ {0} ^ {\infty} e ^ {- r ^ {2} / 2} r d r d \theta = \int_ {0} ^ {2 \pi} \left(\int_ {0} ^ {\infty} e ^ {- u} d u\right) d \theta \\ = \int_ {0} ^ {2 \pi} 1 d \theta = 2 \pi . \\ \end{array}
$$

Therefore,

$$
\int_ {- \infty} ^ {\infty} e ^ {- z ^ {2} / 2} d z = \sqrt {2 \pi},
$$

as we wanted to show.

The expectation of the standard Normal has to be 0, by the symmetry of the PDF; no other balancing point would make sense. We can also see this symmetry by looking at the definition of $E ( Z )$

$$
E (Z) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} z e ^ {- z ^ {2} / 2} d z,
$$

and since $g ( z ) = z e ^ { - z ^ { 2 } / 2 }$ is an odd function (see Section A.2.3 of the math appendix for more on even and odd functions), the area under $g$ from $- \infty$ to 0 cancels the area under g from 0 to $\infty .$ . Therefore $E ( Z ) = 0$ . In fact, the same argument shows that $E ( Z ^ { n } ) = 0$ for any odd positive integer $n .$ 1

Getting the mean was easy (one might even say it was EZ), but the variance

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1<sub>A</sub> subtlety is that ∞ − ∞ is undefined, so we also want to check that the area under the curve z<sup>n</sup><sub>e</sub>−z<sup>2</sup>/2from 0 to ∞ is finite. But this is true since e−z<sup>2</sup>/2goes to 0 extremely quickly (faster than exponential decay), more than offsetting the growth of the polynomial z<sup>n</sup>.</span></small>

calculation is a bit more involved. By LOTUS,

$$
\begin{array}{l} \mathrm{Var} (Z) = E (Z ^ {2}) - (E Z) ^ {2} = E (Z ^ {2}) \\ = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} z ^ {2} e ^ {- z ^ {2} / 2} d z \\ = \frac {2}{\sqrt {2 \pi}} \int_ {0} ^ {\infty} z ^ {2} e ^ {- z ^ {2} / 2} d z \\ \end{array}
$$

The last step uses the fact that $z ^ { 2 } e ^ { - z ^ { 2 } / 2 }$ is an even function. Now we use integration by parts with $u = z$ and $d v = z e ^ { - z ^ { 2 } / 2 } d z$ , so $d u = d z$ and $v = - e ^ { - z ^ { 2 } / 2 }$ :

$$
\begin{array}{l} \operatorname{Var} (Z) = \frac {2}{\sqrt {2 \pi}} \left(- z e ^ {- z ^ {2} / 2} \bigg | _ {0} ^ {\infty} + \int_ {0} ^ {\infty} e ^ {- z ^ {2} / 2} d z\right) \\ = \frac {2}{\sqrt {2 \pi}} \left(0 + \frac {\sqrt {2 \pi}}{2}\right) \\ = 1. \\ \end{array}
$$

The first term of the integration by parts equals 0 because $e ^ { - z ^ { 2 } / 2 }$ decays much faster than z grows, and the second term is $\sqrt { 2 \pi } / 2$ because it’s half of the total area under $e ^ { - z ^ { 2 } / 2 }$ , which we’ve already proved is $\sqrt { 2 \pi }$ . So indeed, the standard Normal distribution has mean 0 and variance 1.

The general Normal distribution has two parameters, denoted $\mu$ and $\sigma ^ { 2 }$ , which correspond to the mean and variance (so the standard Normal is the special case where $\mu = 0$ and $\sigma ^ { 2 } = 1 )$ . Starting with a standard Normal r.v. $Z \sim \mathcal { N } ( 0 , 1 )$ , we can get a Normal r.v. with any mean and variance by a location-scale transformation (shifting and scaling).

Definition 5.4.3 (Normal distribution). If $Z \sim \mathcal { N } ( 0 , 1 )$ , then

$$
X = \mu + \sigma Z
$$

is said to have the Normal distribution with mean $\mu$ and variance $\sigma ^ { 2 }$ , for any real $\mu$ and $\sigma ^ { 2 }$ with $\sigma > 0$ . We denote this by $X \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$

It’s clear by properties of expectation and variance that X does in fact have mean $\mu$ and variance $\sigma ^ { 2 }$ :

$$
\begin{array}{l} E (\mu + \sigma Z) = E (\mu) + \sigma E (Z) = \mu , \\ \operatorname{Var} (\mu + \sigma Z) = \operatorname{Var} (\sigma Z) = \sigma^ {2} \operatorname{Var} (Z) = \sigma^ {2}. \\ \end{array}
$$

Note that we multiply $Z$ by the standard deviation $\sigma ,$ not $\sigma ^ { 2 }$ ; else the units would be wrong and $X$ would have variance $\sigma ^ { 4 }$

Of course, if we can get from $Z$ to $X .$ , then we can get from X back to $Z .$ The process of getting a standard Normal from a non-standard Normal is called, appropriately enough, standardization. For $X \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ , the standardized version of X is

$$
\frac {X - \mu}{\sigma} \sim \mathcal {N} (0, 1).
$$

We can use standardization to find the CDF and PDF of X in terms of the standard Normal CDF and PDF.

Theorem 5.4.4 (Normal CDF and PDF). Let $X \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ . Then the CDF of X is

$$
F (x) = \Phi \left(\frac {x - \mu}{\sigma}\right),
$$

and the PDF of X is

$$
f (x) = \varphi \left(\frac {x - \mu}{\sigma}\right) \frac {1}{\sigma}.
$$

Proof. For the CDF, we start from the definition $F ( x ) = P ( X \leq x )$ , standardize, and use the CDF of the standard Normal:

$$
F (x) = P (X \leq x) = P \left(\frac {X - \mu}{\sigma} \leq \frac {x - \mu}{\sigma}\right) = \Phi \left(\frac {x - \mu}{\sigma}\right).
$$

Then we differentiate to get the PDF, remembering to apply the chain rule:

$$
\begin{array}{l} f (x) = \frac {d}{d x} \Phi \left(\frac {x - \mu}{\sigma}\right) \\ = \varphi \left(\frac {x - \mu}{\sigma}\right) \frac {1}{\sigma}. \\ \end{array}
$$

We can also write out the PDF as

$$
f (x) = \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}\right).
$$

Finally, three important benchmarks for the Normal distribution are the probabilities of falling within one, two, and three standard deviations of the mean. The 68-95-99.7% rule tells us that these probabilities are what the name suggests.

Theorem 5.4.5 (68-95-99.7% rule). If $X \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ , then

$$
\begin{array}{l} P (| X - \mu | <   \sigma) \approx 0. 6 8, \\ P (| X - \mu | <   2 \sigma) \approx 0. 9 5, \\ P (| X - \mu | <   3 \sigma) \approx 0. 9 9 7. \\ \end{array}
$$

We can use this rule to get quick approximations of Normal probabilities.<sup>2</sup> Often it is easier to apply the rule after standardizing, in which case we have

$$
\begin{array}{l} P (| Z | <   1) \approx 0. 6 8, \\ P (| Z | <   2) \approx 0. 9 5, \\ P (| Z | <   3) \approx 0. 9 9 7. \\ \end{array}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>The 68-95-99.7% rule says that 95% of the time, a Normal random variable will fall within ±2 standard deviations of its mean. An even more accurate approximation says that 95% of the time, a Normal r.v. is within ±1.96 SDs of its mean. This explains why the number 1.96 comes up very often in statistics in the context of 95% confidence intervals, which are often created by taking an estimate and putting a buffer zone of 1.96 SDs on either side.</span></small>

Example 5.4.6 (Practice with the standard Normal CDF). Let $X \sim \mathcal { N } ( - 1 , 4 )$ What is $P ( | X | < 3 )$ , exactly (in terms of Φ) and approximately?

## Solution:

The event $| X | < 3$ is the same as the event $- 3 < X < 3$ . We use standardization to express this event in terms of the standard Normal r.v. $Z = ( X - ( - 1 ) ) / 2$ , then apply the 68-95-99.7% rule to get an approximation. The exact answer is

$$
P (- 3 <   X <   3) = P \left(\frac {- 3 - (- 1)}{2} <   \frac {X - (- 1)}{2} <   \frac {3 - (- 1)}{2}\right) = P (- 1 <   Z <   2),
$$

which is $\Phi ( 2 ) - \Phi ( - 1 )$ . The $68 - 95 - 99.7\%$ rule tells us that $P ( - 1 < Z < 1 ) \approx 0 . 6 8$ and $P ( - 2 < Z < 2 ) \approx 0 . 9 5$ . In other words, going from ±1 standard deviation to ±2 standard deviations adds approximately $0 . 9 5 - 0 . 6 8 = 0 . 2 7$ to the area under the curve. By symmetry, this is evenly divided between the areas $P(-2 < Z < -1)$ and $P ( 1 < Z < 2 )$ . Therefore,

$$
P (- 1 <   Z <   2) = P (- 1 <   Z <   1) + P (1 <   Z <   2) \approx 0. 6 8 + \frac {0 . 2 7}{2} = 0. 8 1 5.
$$

This is close to the correct value, $\Phi ( 2 ) - \Phi ( - 1 ) \approx 0 . 8 1 8 6 .$

As we will see later in the book, several important distributions can be obtained through transforming Normal r.v.s in natural ways, e.g., squaring or exponentiating. Chapter 8 delves into transformations in depth, but meanwhile there is a lot that we can do just using LOTUS and properties of CDFs.

Example 5.4.7 (Folded Normal). Let $Y = | Z |$ with $Z \sim \mathcal { N } ( 0 , 1 )$ The distribution of Y is called a Folded Normal with parameters $\mu = 0$ and $\sigma ^ { 2 } = 1$ . In this example, we will derive the mean, variance, and distribution of Y . At first sight, Y may seem tricky to deal with since the absolute value function is not differentiable at 0 (due to its sharp corner), but Y has a perfectly valid continuous distribution.

(a) Find $E ( Y )$
(b) Find Var(Y ).
(c) Find the CDF and PDF of Y .

## Solution:

(a) We will derive the PDF of Y later in this example, but to find $E ( Y )$ , LOTUS says we can work directly with the PDF of $Z ;$

$$
E (Y) = E | Z | = \int_ {- \infty} ^ {\infty} | z | \frac {1}{\sqrt {2 \pi}} e ^ {- z ^ {2} / 2} d z = 2 \int_ {0} ^ {\infty} z \frac {1}{\sqrt {2 \pi}} e ^ {- z ^ {2} / 2} d z = \sqrt {\frac {2}{\pi}}.
$$

(b) Note that $Y ^ { 2 } = Z ^ { 2 }$ , so we do not need to do another integral! We have

$$
E (Y ^ {2}) = E (Z ^ {2}) = \mathrm{Var} (Z) = 1,
$$

so

$$
\mathrm{Var} (Y) = E (Y ^ {2}) - (E (Y)) ^ {2} = 1 - \frac {2}{\pi}.
$$

(c) For $y \leq 0$ , the CDF of Y is $F_Y(y) = P(Y \leq y) = 0$ . For $y > 0$ , the CDF is

$$
F _ {Y} (y) = P (Y \leq y) = P (| Z | \leq y) = P (- y \leq Z \leq y) = \Phi (y) - \Phi (- y) = 2 \Phi (y) - 1.
$$

So the PDF of $Y$ is $2 \varphi ( y )$ for $y \geq 0$ , and 0 otherwise, where $\varphi$ is the $\mathcal { N } ( 0 , 1 )$ PDF.

Sanity check: Note that $2 \Phi ( y ) - 1   \to   2 - 1   =   1 { \mathrm { ~ a s ~ } } y   \to   \infty ,$ as it must, and that the CDF of Y is a continuous function since Φ is continuous and at 0 there is not a jump: $2\Phi(0) - 1 = 0$ . Also, the PDF of Y makes sense since taking the absolute value of $Z { \mathrm { ~ ` f o l d s  } }$ the probability mass of a negative range of values of $Z$ over to the positive side, $\mathbf { e . g . }$ , the probability for $Z$ values between −2 and −1 contributes to the probability for $Y$ values between 1 and 2. This results in zero density for negative values and double the density for positive values. 

## 5.5 Exponential

The Exponential distribution is the continuous counterpart to the Geometric distribution. Recall that a Geometric random variable counts the number of failures before the first success in a sequence of Bernoulli trials. The story of the Exponential distribution is analogous, but we are now waiting for a success in continuous time, where successes arrive at a rate of λ successes per unit of time. The average number of successes in a time interval of length t is $\lambda t ,$ though the actual number of successes varies randomly. An Exponential random variable represents the waiting time until the first arrival of a success.

Definition 5.5.1 (Exponential distribution). A continuous r.v. X is said to have the Exponential distribution with parameter λ, where $\lambda > 0 .$ if its PDF is

$$
f (x) = \lambda e ^ {- \lambda x}, \quad x > 0.
$$

We denote this by $X \sim \operatorname { E x p o } ( \lambda )$

The corresponding CDF is

$$
F (x) = 1 - e ^ {- \lambda x}, \quad x > 0.
$$

The $\mathrm { E x p o ( 1 ) }$ PDF and CDF are plotted in Figure 5.12. Note the resemblance to the Geometric PMF and CDF pictured in Chapter 4. Exercise 43 explores the sense in which the Geometric converges to the Exponential, in the limit where the Bernoulli trials are performed faster and faster but with smaller and smaller success probabilities.

![](images/page_255_image_2.jpg)

## FIGURE 5.12

Expo(1) PDF and CDF.

We’ve seen how all Uniform and Normal distributions are related to one another via location-scale transformations, and we might wonder whether the Exponential distribution allows this too. Exponential r.v.s are defined to have support $( 0 , \infty )$ and shifting would change the left endpoint. But scale transformations work nicely, and we can use scaling to get from the simple Expo(1) to the general Expo(λ): if $X \sim \mathrm { E x p o ( 1 ) }$ , then

$$
Y = \frac {X}{\lambda} \sim \mathrm{Expo} (\lambda),
$$

since

$$
P (Y \leq y) = P \left(\frac {X}{\lambda} \leq y\right) = P (X \leq \lambda y) = 1 - e ^ {- \lambda y}, \quad y > 0.
$$

Conversely, if $Y \sim \operatorname { E x p o } ( \lambda )$ , then $\lambda Y \sim  Expo (1)$

This means that just as we did for the Uniform and the Normal, we can get the mean and variance of the Exponential distribution by starting with $X \sim \mathrm { E x p o ( 1 ) }$ . Both $E ( X )$ and $\operatorname { V a r } ( X )$ are obtained using standard integration by parts calculations. This gives

$$
\begin{array}{l} E (X) = \int_ {0} ^ {\infty} x e ^ {- x} d x = 1, \\ E (X ^ {2}) = \int_ {0} ^ {\infty} x ^ {2} e ^ {- x} d x = 2, \\ \mathrm{Var} (X) = E (X ^ {2}) - (E X) ^ {2} = 1. \\ \end{array}
$$

In the next chapter we’ll introduce a new tool called the moment generating function, which will let us get these results without integration.