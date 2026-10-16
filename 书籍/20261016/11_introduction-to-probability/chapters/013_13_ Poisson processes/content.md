# 13: Poisson processes

原始 PDF 第 576–625 页。

## Poisson processes

Poisson processes serve as a simple model for events occurring in time or space: in one dimension, cars passing by a highway checkpoint; in two dimensions, flowers in a meadow; in three dimensions, stars in a region of the galaxy. Poisson processes are a primary building block for more complicated processes in time and space, which are the focus of a branch of statistics called spatial statistics.

Poisson processes are also useful in probability, as they tie together many of the named distributions and provide us with insightful story proofs for results that might otherwise be tedious to show. This leads to a new problem-solving strategy, which we will demonstrate: even when a problem makes no mention of Poisson processes, there are sometimes ways to pretend the r.v.s are coming from a Poisson process so that we can use convenient Poisson process properties.

In this chapter, we’ll review the already familiar definition of the 1D Poisson process, derive and discuss three important properties of the 1D Poisson process, and then extend these properties to Poisson processes in higher dimensions.

## 13.1 Poisson processes in one dimension

In Section 5.6, we defined a one-dimensional Poisson process and showed that the interarrival times are i.i.d. Exponentials. In Chapter 8 we showed that the time of the jth arrival (relative to some fixed starting time) is Gamma. Let’s review these results, with notation that will help us generalize to higher dimensions.

Definition 13.1.1 (1D Poisson process). A sequence of arrivals in continuous time is a Poisson process with rate λ if the following conditions hold:

1. The number of arrivals in an interval of length t is distributed Pois(λt).
2. The numbers of arrivals in disjoint time intervals are independent.

Usually we will assume that the timeline starts at t = 0, in which case we have a Poisson process on $( 0 , \infty )$ , but we can use the same conditions to define a Poisson process on $( - \infty , \infty )$ if we want the timeline to be infinite in both directions.

559

---

560

Introduction to Probability

Consider a Poisson process on $( 0 , \infty )$ . Departing slightly from our notation in pre-vious chapters, let $N ( t )$ be the number of arrivals in $( 0 , t ]$ . Then the number of arrivals in $( t _ { 1 } , t _ { 2 } ]$ is $N ( t _ { 2 } ) - N ( t _ { 1 } )$ , for $0 < t _ { 1 } < t _ { 2 }$ . Let $T _ { j }$ be the time of the jth arrival. Since $T _ { 1 } > t$ is the same event as $N ( t ) = 0$ (by the count-time duality, as discussed in Section 5.6),

$$
P (T _ {1} > t) = P (N (t) = 0) = e ^ {- \lambda t},
$$

so $T _ { 1 } \sim \operatorname { E x p o } ( \lambda )$ . Next let’s condition on the first arrival time $T _ { 1 }$ and look at the additional time $T _ { 2 } - T _ { 1 }$ until the second arrival. Then

$$
(T _ {2} - T _ {1}) | T _ {1} \sim \mathrm{Expo} (\lambda)
$$

by the same argument as above, since we have a fresh Poisson process starting at $T _ { 1 }$ . Since the conditional distribution of $( T _ { 2 }   -   T _ { 1 } ) | T _ { 1 }$ does not depend on $T _ { 1 }$ , we have that $T _ { 2 } - T _ { 1 }$ is independent of $T _ { 1 }$ , so $T _ { 2 } - T _ { 1 } \sim \mathrm { E x p o } ( \lambda )$ unconditionally too.

Continuing in this way, the interarrival times $T _ { j }   -   T _ { j - 1 }$ are independent, with

$$
T _ {j} - T _ {j - 1} \sim \mathrm{Expo} (\lambda).
$$

So a Poisson process can be described dually as a process in which arrival counts are Poissons or a process in which interarrival times are Exponentials. Also note that since $T _ { j }$ is the sum of j i.i.d. Expo(λ) r.v.s,

$$
T _ {j} \sim \mathrm{Gamma} (j, \lambda).
$$

The connection with the Exponential gives us a simple way to generate n arrivals from a Poisson process.

Story 13.1.2 (Generative story for 1D Poisson process). To generate n arrivals from a Poisson process on $( 0 , \infty )$ with rate λ:

1. Generate n i.i.d. Expo(λ) r.v.s $X _ { 1 } , \ldots , X _ { n } .$
2. For j = 1, . . . , n, set Tj = X<sub>1</sub> + · · · + Xj .

Then we can take $T _ { 1 } , \ldots , T _ { n }$ to be the arrival times.

Figure 13.1 depicts three realizations of Poisson processes with rates 1, 2, and $^ { 5 , }$ respectively, plotted up to time 10. In all three cases, we can see that despite the interarrival times being i.i.d., the arrivals are not evenly spaced. Rather, there is a lot of variability in the interarrival times, which produces clumps of arrivals. This phenomenon is known as Poisson clumping. It might seem like an amazing coincidence to observe a cluster of several arrivals that are close together in time, but Poisson clumping says that having such clusters is common with Poisson processes.

---

Poisson processes

561

![](../../raw/pages_0577-0592/images/page_577_chart_2.jpg)

<details>
<summary>scatter</summary>

| \(\lambda\) | X-axis Position |
| --- | --- |
| 1 | ~0.5, ~1.5, ~2.5, ~3.5, ~4.5, ~5.5, ~6.5, ~7.5, ~8.5, ~9.5 |
| 2 | ~0.5, ~1.5, ~2.5, ~3.5, ~4.5, ~5.5, ~6.5, ~7.5, ~8.5, ~9.5 |
| 5 | ~0.5, ~1.5, ~2.5, ~3.5, ~4.5, ~5.5, ~6.5, ~7.5, ~8.5, ~9.5 |
</details>

FIGURE 13.1

Simulated Poisson process in one dimension, for $\lambda   =   1 , 2 , 5 .$ The arrivals are far from evenly spaced from each other, and in fact they sometimes clump together,

## 13.2 Conditioning, superposition, and thinning

The three most important properties to understand about the Poisson process are conditioning, superposition, and thinning. These correspond to properties we’ve already seen about the Poisson distribution, so they should already be plausible.

## 13.2.1 Conditioning

What happens when we take a Poisson process and condition on the total number of events in an interval? Our first result is that conditional on the total number of events in an interval, the number of events in a fixed subinterval is Binomial. This follows from Theorem 4.8.2, where we showed that we can get from the Poisson to the Binomial by conditioning.

Theorem 13.2.1 (Conditional counts). Let $( N ( t )   :   t   >   0 )$ be a Poisson process with rate $\lambda ,$ and $t _ { 1 } < t _ { 2 }$ . The conditional distribution of $N ( t _ { 1 } )$ given $N ( t _ { 2 } ) = n$ is

$$
N (t _ {1}) \mid N (t _ {2}) = n \sim \mathrm{Bin} \left(n, \frac {t _ {1}}{t _ {2}}\right).
$$

Proof. Figure 13.2 illustrates the setup. The claim is that conditional on having a total of n arrivals in $( 0 , t _ { 2 } ]$ , the number of arrivals in $( 0 , t _ { 1 } ]$ is Binomial, with n trials and success probability proportional to $t _ { 1 }$

Since $( 0 , t _ { 1 } ]$ and $( t _ { 1 } , t _ { 2 } ]$ are disjoint, $N ( t _ { 1 } )$ is independent of $N ( t _ { 2 } )   -   N ( t _ { 1 } )$ . The first is distributed $\mathrm { P o i s } ( \lambda t _ { 1 } )$ , the second is distributed $Pois (\lambda(t_{2}-t_{1}))$ , and their sum is

---

562

Introduction to Probability

![](../../raw/pages_0577-0592/images/page_578_image_2.jpg)

<details>
<summary>text_image</summary>

0
N(t₁)
t₁
N(t₂) - N(t₁)
t₂
</details>

## FIGURE 13.2

Conditioning. Given that n arrivals occurred in $( 0 , t _ { 2 } ]$ , the conditional distribution of the number of arrivals in $( 0 , t _ { 1 } ]$ is Binomial with parameters n and $t _ { 1 } / t _ { 2 }$

the number of arrivals in $( 0 , t _ { 2 } ]$ , namely $N ( t _ { 2 } )$ . By Theorem 4.8.2,

$$
N (t _ {1}) \mid N (t _ {2}) = n \sim \mathrm{Bin} \left(n, \frac {\lambda t _ {1}}{\lambda t _ {1} + \lambda (t _ {2} - t _ {1})}\right),
$$

which is precisely what we wanted to show.

Carrying the idea of conditioning on the number of arrivals further, we have the following striking result: in a Poisson process, given that $N ( t ) = n$ , the arrival times are distributed as if we threw down n i.i.d. $\mathrm { U n i f } ( 0 , t )$ points.

First let’s look at a simple case, where there has been only one arrival.

Proposition 13.2.2. In a Poisson process of rate $\lambda ,$ conditional on $N ( t ) = 1$ , the first arrival time $T _ { 1 }$ has the $\mathrm { U n i f } ( 0 , t )$ distribution.

Proof. Let $0 < s < t$ . By a form of the count-time duality,

$$
\begin{array}{l} P (T _ {1} \leq s | N (t) = 1) = \frac {P (T _ {1} \leq s , N (t) = 1)}{P (N (t) = 1)} \\ = \frac {P (N (s) = 1 , N (t) - N (s) = 0)}{P (N (t) = 1)} \\ = \frac {(e ^ {- \lambda s} \lambda s) (e ^ {- \lambda (t - s)})}{e ^ {- \lambda t} \lambda t} \\ = \frac {s}{t}. \\ \end{array}
$$

Thus, the conditional CDF of $T _ { 1 }$ given $N ( t ) = 1$ is the $\mathrm { U n i f } ( 0 , t )$ CDF.

More generally, given that $N ( t ) = n$ , the arrival times $T _ { j }$ look like the order statistics of n i.i.d. Unif(0, t) r.v.s. We omit the proof since in introducing order statistics in Chapter 8, we focused on their marginal distributions.

Theorem 13.2.3 (Conditional times). In a Poisson process of rate $\lambda ,$ conditional on $N ( t ) = n ,$ the joint distribution of the arrival times $T _ { 1 } , \ldots , T _ { n }$ is the same as the joint distribution of the order statistics of n i.i.d. Unif(0, t) r.v.s.

---

Poisson processes

563

From Chapter 8, we know that the order statistics of $\mathrm { U n i f } ( 0 , 1 )$ r.v.s are Betas, so the conditional distributions of the $T _ { j }$ are scaled Betas; to get Beta distributions, we can just divide the $T _ { j }$ by t so that their support is $( 0 , 1 )$

$$
t ^ {- 1} T _ {j} \mid N (t) = n \sim \mathrm{Beta} (j, n - j + 1).
$$

We now have another way to generate arrivals from a Poisson process, this time for a specific interval instead of a specific number of arrivals.

Story 13.2.4 (Generative story for Poisson process, take 2). To generate arrivals from a Poisson process with rate λ in an interval $( 0 , t ]$

1. Generate the total number of events in the interval, $N ( t ) \sim \mathrm { P o i s } ( \lambda t )$
2. Given $N ( t ) = n$ , generate n i.i.d. Unif $\mathrm { f } ( 0 , t ) \mathrm { ~ r . v . s ~ } U _ { 1 } , \ldots , U _ { n }$
3. For $j = 1 , \ldots , n , \mathrm { s e t } T _ { j } = U _ { ( j ) } .$

This is actually the generative story we used to create Figure 13.1, since we knew we wanted to simulate in the interval (0, 10].

Example 13.2.5 (Users on a website). Users visit a certain website according to a Poisson process with rate $\lambda _ { 1 }$ users per minute, where an “arrival” at a certain time means that at that time someone starts browsing the site. After arriving at the site, each user browses the site for an $\mathrm { E x p o } ( \lambda _ { 2 } )$ amount of time (and then leaves), independent of other users.

Suppose that at time 0, no one is using the site. Let $N _ { t }$ be the number of users who arrive in the interval $( 0 , t ]$ , and let $C _ { t }$ be the number of users who are currently browsing the site at time t.

(a) Let $X$ be the time of arrival and Y be the time of departure for a user who arrives at a Uniform time point in $[ 0 , t ]$ . Find the joint PDF of X and $Y$

(b) Let $p _ { t }$ be the probability that a user who arrives at a Uniform time point in (0, t] is still browsing the site at time t. Find $p _ { t }$

(c) Find the distribution of $C _ { t }$ in terms of $\lambda _ { 1 } , \lambda _ { 2 }$ , and t.

(d) Little’s law is a very general result, which says the following:

The long-run average number of customers in a stable system is the long-term average arrival rate multiplied by the average time a customer spends in the system.

Explain what happens to $E ( C _ { t } )$ for t large, and how this can be interpreted in terms of Little’s law.

## Solution:

(a) We have $X \sim \mathrm { U n i f } ( 0 , t )$ . Given $X = x ,   Y$ is an $\mathrm { E x p o } ( \lambda _ { 2 } )$ shifted to start at $x .$ $i.e.,   (Y - x)|(X = x) \sim  Expo (\lambda_2)$ . So the joint PDF of X and Y is

$$
f (x, y) = f _ {X} (x) f _ {Y | X} (y | x) = \frac {\lambda_ {2}}{t} e ^ {- \lambda_ {2} (y - x)}, \text {   for   } 0 <   x <   t \text {   and   } x <   y.
$$

---

564

Introduction to Probability

(b) With notation as in $( \mathrm { a } )$ , we want to find $p _ { t } = P ( Y > t )$ . This can be done by integrating the joint PDF over all $( x , y )$ with $y > t \cdot$

$$
\begin{array}{l} P (Y > t) = \frac {1}{t} \int_ {0} ^ {t} \int_ {t} ^ {\infty} \lambda_ {2} e ^ {- \lambda_ {2} (y - x)} d y d x \\ = \frac {1}{t} \int_ {0} ^ {t} e ^ {\lambda_ {2} x} \left(\int_ {t} ^ {\infty} \lambda_ {2} e ^ {- \lambda_ {2} y} d y\right) d x \\ = \frac {e ^ {- \lambda_ {2} t}}{t} \int_ {0} ^ {t} e ^ {\lambda_ {2} x} d x \\ = \frac {1 - e ^ {- \lambda_ {2} t}}{\lambda_ {2} t}. \\ \end{array}
$$

(c) By Theorem 13.2.3, given $N _ { t } = n$ we have that the n arrival times in $( 0 , t ]$ are $\mathrm { i . i . d . }$ . and uniform in that interval. Therefore, $C _ { t } | N _ { t } \sim \operatorname { B i n } ( N _ { t } , p _ { t } )$ , with $p _ { t }$ as above, and $N _ { t } \sim \operatorname { P o i s } ( \lambda _ { 1 } t )$ . So by the chicken-egg story (Story 7.1.9),

$$
C _ {t} \sim \mathrm{Pois} (\lambda_ {1} p _ {t} t).
$$

That is,

$$
C _ {t} \sim \mathrm{Pois} \left(\frac {\lambda_ {1} (1 - e ^ {- \lambda_ {2} t})}{\lambda_ {2}}\right).
$$

(d) As $t \to \infty,   E(C_t) \to \lambda_1/\lambda_2$ . This agrees with Little’s law since it says the longrun average number of users in the system (browsing the site) is the rate at which users arrive $\left( \lambda _ { 1 } \right)$ times the average time a user browses in a session $( 1 / \lambda _ { 2 } )$ 

## 13.2.2 Superposition

The next property we will examine is superposition: if we take two independent Poisson processes and overlay them, we get another Poisson process. (The combined process is a Poisson process in its own right, but we can imagine that the arrivals are tagged to indicate which of the underlying processes they came from.)

Theorem 13.2.6 (Superposition). Let $( N _ { 1 } ( t )   :   t   >   0 )$ and $( N _ { 2 } ( t )   :   t   >   0 )$ b e independent Poisson processes with rates $\lambda _ { 1 }$ and $\lambda _ { 2 }$ , respectively. Then the combined process $N ( t ) = N _ { 1 } ( t ) + N _ { 2 } ( t )$ is a Poisson process with rate $\lambda _ { 1 } + \lambda _ { 2 }$

Proof. Let’s verify the two properties in the definition of Poisson process.

1. For all $t > 0,   N_1(t) \sim  Pois (\lambda_1 t)$ and $N _ { 2 } ( t ) \sim \operatorname { P o i s } ( \lambda _ { 2 } t )$ , independently, so $N ( t ) \sim$ $\operatorname { P o i s } ( ( \lambda _ { 1 } + \lambda _ { 2 } ) t )$ , by Theorem 4.8.1. The same argument applies for any interval of length t, not just intervals of the form $( 0 , t ]$

2. Arrivals in disjoint intervals are independent in the combined process because they are independent in the two individual processes, and the individual processes are independent of each other. 

---

Poisson processes

565

There is a very natural way to generate a superposition.

Story 13.2.7 (Generative story for superposition). To generate the superposition of two independent Poisson processes, $( N _ { 1 } ( t ) : t > 0 )$ with rate $\lambda _ { 1 }$ and $( N _ { 2 } ( t ) : t > 0 )$ with rate $\lambda _ { 2 }$ :

1. Generate arrivals from the Poisson process $( N _ { 1 } ( t ) : t > 0 )$
2. Generate arrivals from the Poisson process $( N _ { 2 } ( t ) : t > 0 )$
3. Superpose the results of steps 1 and 2.

![](../../raw/pages_0577-0592/images/page_581_chart_8.jpg)

<details>
<summary>wireframe</summary>

| Function | Segment 1 (X) | Segment 2 (Y) |
| --- | --- | --- |
| \(\lambda_{1} = 0.5\) | ~3.5, ~7.5, ~8.5 | N/A |
| \(\lambda_{2} = 0.5\) | ~1.5, ~4.5, ~5.5, ~6.5, ~7.5, ~8.5 | N/A |
| \(\lambda_{1} + \lambda_{2} = 1\) | ~1.5, ~3.5, ~4.5, ~5.5, ~6.5, ~7.5, ~8.5 | N/A |
</details>

## FIGURE 13.3

Superposition. The superposition of independent Poisson processes is a Poisson process, and the rates add. The top two timelines are independent Poisson processes, each with rate 0.5. The bottom timeline is the superposition of the top two Poisson processes and is itself a Poisson process with rate 1.

Figure 13.3 depicts a superposed Poisson process consisting of $\times   ^ { \prime } \mathrm { s }$ and ${ \diamondsuit } ^ { \flat } \mathbf { S } .$ Let’s call the $\times   ^ { \prime } \mathrm { s }$ “type-1 events” and the $\diamondsuit ^ { \prime } \mathrm { S }$ “type-2 events”. A natural question to ask is: what is the probability of observing a type-1 event before a type-2 event?

Theorem 13.2.8 (Probability of type-1 event before type-2 event). Consider two independent Poisson processes: a Poisson process of type-1 arrivals, with rate $\lambda _ { 1 }$ and a Poisson process of type-2 arrivals, with rate $\lambda _ { 2 }$ . In the superposition of these two processes, the probability of the first arrival being type-1 is $\lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } )$

Proof. Let $T$ be the time until the first type-1 event and let V be the time until the first type-2 event. We seek $P ( T   \leq   V )$ . We could do this with 2D LOTUS, integrating the joint PDF of $T$ and V over the region of interest in the 2D plane. But it turns out we can avoid calculus altogether.

We have $T \sim \mathrm{Exp}(\lambda_1)$ and $V \sim \mathrm{Exp}(\lambda_2)$ , independently. Rescaling, let

$$
\tilde {T} = \lambda_ {1} T, \tilde {V} = \lambda_ {2} V.
$$

Then $\tilde { T } , \tilde { V }$ are i.i.d. Expo(1).

---

566

Introduction to Probability

Letting $U = \tilde { T } / ( \tilde { T } + \tilde { V } )$ , we have

$$
\begin{array}{l} P (T \leq V) = P \left(\frac {\tilde {T}}{\lambda_ {1}} \leq \frac {\tilde {V}}{\lambda_ {2}}\right) \\ = P \left(\frac {\tilde {T}}{\tilde {T} + \tilde {V}} \leq \frac {\tilde {V}}{\tilde {T} + \tilde {V}} \cdot \frac {\lambda_ {1}}{\lambda_ {2}}\right) \\ = P \left(U \leq (1 - U) \cdot \frac {\lambda_ {1}}{\lambda_ {2}}\right) \\ = P \left(U \leq \frac {\lambda_ {1}}{\lambda_ {1} + \lambda_ {2}}\right). \\ \end{array}
$$

Since $\tilde { T } , \tilde { V } \sim \mathrm { E x p o ( 1 ) }$ , the bank–post office story tells us that $U \sim \mathrm { B e t a } ( 1 , 1 )$ . In other words, U is standard Uniform! Thus, $P ( T   \leq   V )   =   \lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } )$ . Note that when $\lambda _ { 1 } = \lambda _ { 2 }$ this reduces to $1 / 2$ , as it should by symmetry. 

The above result applies to the first arrival in the combined Poisson process. After the first arrival, however, the same reasoning applies to the second arrival: by the memoryless property, the time to the next type-1 event is $\mathrm{Exp}(\lambda_1)$ and the time to the next type-2 event is $\mathrm { E x p o } ( \lambda _ { 2 } )$ , independent of the past. Therefore the second arrival is a type-1 arrival with probability $\lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } )$ , independent of the first arrival. Similarly, all of the arrival types can be viewed as i.i.d. coin tosses with probability $\lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } )$ of Heads, where Heads corresponds to type-1.

This yields an alternative generative story for the superposition of two independent Poisson processes: we can first generate an $\mathrm{Exp}(\lambda_1 + \lambda_2)$ r.v. to decide when the next arrival occurs, and then independently flip a coin with probability $\lambda _ { 1 } / ( \lambda _ { 1 }   +   \lambda _ { 2 } )$ of Heads to decide what kind of arrival it is.

Story 13.2.9 (Generative story for superposition, take 2). To generate the superposition of two independent Poisson processes, with rates $\lambda _ { 1 }$ and $\lambda _ { 2 } !$

1. Generate i.i.d. $\mathrm{Exp}(\lambda_1 + \lambda_2)$ r.v.s $X _ { 1 } , X _ { 2 } , \ldots$ , and let the jth arrival be at time $T _ { j } = X _ { 1 } + \cdots + X _ { j }$
2. Generate i.i.d. r.v.s $I _ { 1 } , I _ { 2 } , \cdots \sim$ Bern $( \lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } ) )$ , independent of $X _ { 1 } , X _ { 2 } , \ldots .$ Let the jth arrival be type-1 if $I _ { j } = 1$ , and type-2 otherwise.



This story provides us with a quick proof of a result known as the competing risks theorem, which seems like a surprising independence result when stated on its own but becomes very intuitive when viewed in the context of Poisson processes.

Example 13.2.10 (Competing risks). The lifetime of Fred’s refrigerator is $Y _ { 1 } \sim$ $\mathrm{Exp}(\lambda_1)$ , and the lifetime of his dishwasher is $Y _ { 2 } \; \sim \; \mathrm { E x p o } ( \lambda _ { 2 } )$ , independent of $Y _ { 1 }$ . Show that min $( Y _ { 1 } , Y _ { 2 } )$ , the time of the first appliance failure, is independent of $I ( Y _ { 1 } < Y _ { 2 } )$ , the indicator that the refrigerator failed first. This may seem surprising.

---

Poisson processes

567

For example, if the average lifetime of his refrigerator is 15 years and the average lifetime of his dishwasher is $7$ years, and then one of these appliances fails after $7$ years, it would be natural to guess that it was the dishwasher that failed. But in fact, we will show that knowing the time of the first appliance failure provides no information about which appliance failed.

Solution: We will use an embedding strategy, using Poisson process ideas even though this problem doesn’t mention Poisson processes anywhere! We will embed the r.v.s $Y _ { 1 }$ and $Y _ { 2 }$ into a Poisson process that we ourselves invent, in order to take advantage of the properties of Poisson processes. So let’s imagine there is an entire Poisson process of refrigerator failures with rate $\lambda _ { 1 }$ and a Poisson process of dishwasher failures with rate $\lambda _ { 2 }$

We can interpret $Y _ { 1 }$ as the waiting time for the first arrival in the refrigerator process and $Y _ { 2 }$ as the waiting time for the first arrival in the dishwasher process. This approach is valid since (min $( Y _ { 1 } , Y _ { 2 } ) , I ( Y _ { 1 } { < } Y _ { 2 } ) )$ is a function of $( Y _ { 1 } , Y _ { 2 } )$ , so what matters is the joint distribution of $( Y _ { 1 } , Y _ { 2 } )$ , and the way we construct $( Y _ { 1 } , Y _ { 2 } )$ does have the correct joint distribution.

Furthermore, min $( Y _ { 1 } , Y _ { 2 } )$ is the waiting time for the first arrival in the superposition of the two Poisson processes, and $I ( Y _ { 1 } < Y _ { 2 } )$ is the indicator of this arrival being a type-1 event. But in the above generative story, the arrival times and event types in the superposed Poisson process are generated completely independently! Hence, min $( Y _ { 1 } , Y _ { 2 } )$ and $I ( Y _ { 1 } < Y _ { 2 } )$ are independent, with min $( Y _ { 1 } , Y _ { 2 } ) \sim \operatorname { E x p o } ( \lambda _ { 1 } + \lambda _ { 2 } )$ and $I ( Y _ { 1 } < Y _ { 2 } ) \sim \operatorname { B e r n } ( \lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } ) )$ 

A direct consequence of Story 13.2.9 is that if we project a superposed Poisson process into discrete time, keeping the sequence of type-1 and type-2 arrivals but not the arrival times themselves, we are left with i.i.d. Bern $( \lambda _ { 1 } / ( \lambda _ { 1 } { + } \lambda _ { 2 } ) )$ r.v.s $I _ { 1 } , I _ { 2 } , \ldots ,$ where $I _ { j }$ is the indicator of the jth arrival being type-1. Figure 13.4 illustrates what it means to remove the continuous-time information from the Poisson process, and Theorem 13.2.11 states the result formally.

![](../../raw/pages_0577-0592/images/page_583_image_7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
  A["Initial Step"] --> B["Path with Diamonds"]
  B --> C["Path with Crosses"]
  C --> D["Final State"]
```
</details>

## FIGURE 13.4

Projection into discrete time. Stripping out the continuous-time information from a superposed Poisson process produces a sequence of i.i.d. indicators of type-1 versus type-2 events. Here × represents type-1 events and  represents type-2 events.

Theorem 13.2.11 (Projection of superposition into discrete time). Consider the superposition $( N ( t ) : t > 0 )$ of two independent Poisson processes with rates $\lambda _ { 1 }$ and $\lambda _ { 2 }$ . For $j = 1 , 2 , \ldots ,$ let $I _ { j }$ be the indicator of the jth event being from the Poisson process with rate $\lambda _ { 1 }$ . Then the $I _ { j }$ are i.i.d. Bern $( \lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } ) )$ .

---

568

Introduction to Probability

Using this result, we can prove with a story that a Gamma mixture of Poissons is Negative Binomial, which we first learned from Fred’s adventures in Blotchville (Story 8.4.5). We’ll consider a special case first.

Theorem 13.2.12 (Exponential mixture of Poissons is Geometric). Suppose that $X \sim \operatorname { E x p o } ( \lambda )$ and $Y | X = x \sim \operatorname { P o i s } ( x )$ . Then $Y \sim \operatorname { G e o m } ( \lambda / ( \lambda + 1 ) )$

Proof. $\mathrm { A s }$ with the competing risks theorem, we embed X and $Y$ into Poisson processes. Consider two independent Poisson processes, a process of failures arriving at rate 1 and another of successes arriving at rate λ. Let X be the time of the first success; then $X \sim \operatorname { E x p o } ( \lambda )$ . Let $Y$ be the number of failures before the time of the first success. By the definition of a Poisson process with rate 1, $Y | X = x \sim \operatorname { P o i s } ( x )$ Therefore X and Y satisfy the conditions of the theorem.

To get the marginal distribution of $Y ,$ strip out the continuous-time information! In discrete time we have i.i.d. Bernoulli trials with success probability $\lambda / ( \lambda + 1 )$ and $Y$ is defined as the number of failures before the first success, so by the story of the Geometric distribution, $Y \sim \operatorname { G e o m } ( \lambda / ( \lambda + 1 ) )$ 

The reasoning for the general case is analogous.

Theorem 13.2.13 (Gamma mixture of Poissons is Negative Binomial). Suppose that $X \sim  Gamma (r, \lambda)$ and $Y | X = x \sim \operatorname { P o i s } ( x )$ . Then $Y \sim \mathrm { N B i n } ( r , \lambda / ( \lambda + 1 ) )$

Proof. Consider two independent Poisson processes, a process of failures arriving at rate 1 and another of successes arriving at rate λ. Let X be the time of the rth success, so $X \sim  Gamma (r, \lambda)$ . Let Y be the number of failures before the time of the rth success. Then $Y | X = x \sim \operatorname { P o i s } ( x )$ by definition of Poisson process. We have that $Y$ is the number of failures before the rth success in a sequence of i.i.d. Bernoulli trials with success probability $\lambda / ( \lambda + 1 )$ , so $Y \sim \mathrm { N B i n } ( r , \lambda / ( \lambda + 1 ) )$ 

## 13.2.3 Thinning

The last property of Poisson processes we will discuss is thinning: if we take a Poisson process and, for each arrival, independently flip a coin to decide whether it is a type-1 event or type-2 event, we end up with two independent Poisson processes.

Theorem 13.2.14 (Thinning). Let $( N ( t ) : t > 0 )$ be a Poisson process with rate λ, and classify each arrival as a type-1 event with probability $p$ and a type-2 event with probability $1 - p ,$ where these classifications are independent of each other and independent of the arrival times. Then the type-1 events form a Poisson process with rate $\lambda p ,$ the type-2 events form a Poisson process with rate $\lambda ( 1 - p )$ , and these two processes are independent.

Proof. Let $\lambda _ { \mathrm { 1 } }   =   \lambda p$ and $\lambda _ { 2 }   =   \lambda ( 1   -   p )$ , so $\lambda   =   \lambda _ { \mathrm { 1 } }   +   \lambda _ { \mathrm { 2 } }$ and $p   =   \lambda _ { 1 } / ( \lambda _ { 1 }   +   \lambda _ { 2 } )$ Then we find ourselves in Story 13.2.9. But Story 13.2.7 and Story 13.2.9 are two

---

Poisson processes

569

equivalent generative stories for superposition! The probabilistic structures of the outputs of the two stories are identical, thinking of the arrivals in Story 13.2.7 from $( N _ { i } ( t ) : t > 0 )$ as being type-i. So we can assume instead that Story 13.2.7 was used to generate the process. Happily, in this story we know from the beginning that the type-1 process is independent of the type-2 process. 

Thus we can superpose independent Poisson processes to get a combined Poisson process, or we can split a single Poisson process into independent Poisson processes. Figure 13.5 is an illustration of thinning. We simply flipped Figure 13.3 upside-down, which is appropriate because thinning is the flip side of superposition!

![](../../raw/pages_0577-0592/images/page_585_chart_4.jpg)

<details>
<summary>wireframe</summary>

| Parameter | Segment 1 | Segment 2 | Segment 3 | Segment 4 | Segment 5 |
| --- | --- | --- | --- | --- | --- |
| \(\lambda = 1\) | Diamond | Cross | Diamond | Diamond | Cross |
| \(\lambda(1 - p) = 0.5\) | Diamond | — | Diamond | Diamond | — |
| \(\lambda p = 0.5\) | — | Cross | — | — | Cross |
</details>

## FIGURE 13.5

Thinning. Starting with a single Poisson process, if we let each arrival be type-1 with probability $p$ and type-2 with probability $1 - p ,$ we obtain two independent Poisson processes with rates $\lambda p$ and $\lambda ( 1 - p )$ . Here × represents type-1 events and  represents type-2 events, and we take $p = 0 . 5$

Thinning is the Poisson process analog of the chicken-egg story. Suppose that we thin a Poisson process $( N ( t ) : t > 0 )$ of rate λ as in the statement of Theorem 13.2.14, and let $( N _ { i } ( t ) : t > 0 )$ be the process of type-i arrivals. Thinking of type-1 arrivals as eggs that hatch, it follows immediately from the chicken-egg story that we have $N _ { 1 } ( t ) \sim \operatorname { P o i s } ( \lambda p t ) ,   N _ { 2 } ( t ) \sim \operatorname { P o i s } ( \lambda ( 1 - p ) t )$ , with $N _ { 1 } ( t )$ independent of $N _ { 2 } ( t )$

For practice and as an example of the elegance of thinning, let’s find the distribution of a random sum in two different ways: using MGFs and conditional expectation, and using thinning.

Example 13.2.15 (First Success sum of Exponentials). Let $X _ { 1 } , X _ { 2 } , \ldots$ be i.i.d. Expo(λ) and $N   \sim   \mathrm { F S } ( p )$ , independent of the $X _ { j }$ . Find the distribution of the random sum

$$
Y = \sum_ {j = 1} ^ {N} X _ {j}.
$$

## Solution:

We’ll solve this problem twice, first with tools from Chapter 9 and then with a Poisson process story that uses thinning. For the first method, we recognize $Y$ as the sum of a random number of random variables, so we can find the MGF of

---

570

Introduction to Probability

Y using Adam’s law, conditioning on N. Recalling that the MGF of the Expo(λ) distribution is $\lambda / ( \lambda - t )$ for $t < \lambda$ , we have

$$
\begin{array}{l} E \left(e ^ {t Y}\right) = E \left(E \left(e ^ {t \sum_ {j = 1} ^ {N} X _ {j}} | N\right)\right) \\ = E \left(E \left(e ^ {t X _ {1}}\right) E \left(e ^ {t X _ {2}}\right) \dots E \left(e ^ {t X _ {N}}\right) | N\right) \\ = E \left(E \left(e ^ {t X _ {1}}\right) ^ {N}\right) \\ = E \left(\left(\frac {\lambda}{\lambda - t}\right) ^ {N}\right). \\ \end{array}
$$

Now we can use LOTUS with the $\operatorname { F S } ( p )$ PMF,

$$
P (N = k) = q ^ {k - 1} p \text {for} k = 1, 2, \dots
$$

The LOTUS sum is

$$
E \left(\left(\frac {\lambda}{\lambda - t}\right) ^ {N}\right) = \sum_ {k = 1} ^ {\infty} \left(\frac {\lambda}{\lambda - t}\right) ^ {k} q ^ {k - 1} p,
$$

which simplifies to $\lambda p / ( \lambda p - t )$ for $t < \lambda p$ , after doing some algebra and summing a geometric series. This is the $\operatorname { E x p o } ( \lambda p )$ MGF, so $Y \sim \mathrm{Exp}(\lambda p)$

Now let’s see how Poisson processes can spare us from algebra while also providing insight into why $Y$ is Exponential. Using the embedding strategy, since the $X _ { j }$ are i.i.d. Expo(λ) we are free to interpret the $X _ { j }$ as interarrival times in a Poisson process with rate λ. So let’s imagine such a Poisson process, and let’s further imagine that each of the arrivals is a special arrival with probability $p ,$ independently. Then we can interpret N as the number of arrivals until the first special arrival and $Y$ as the waiting time for the first special arrival. But by the thinning property, the special arrivals form a Poisson process with rate $\lambda p$ . The waiting time for the first special arrival is thus distributed $\operatorname { E x p o } ( \lambda p )$ 

Thinning works analogously with more than 2 types. In this setting, thinning is sometimes called the coloring theorem.

Theorem 13.2.16 (Coloring). Let $( N ( t ) : t > 0 )$ be a Poisson process with rate λ, and C be a finite set of $`` colors''$ , labeled from 1 through c. Suppose that each arrival gets randomly assigned a color from $C ,$ with color i having probability $p _ { i }$ The color assignments are independent of each other and independent of the arrival times. Let $( N _ { i } ( t ) : t > 0 )$ be the color i process, i.e., $N _ { i } ( t )$ is the number of arrivals with color i in $( 0 , t ]$ . Then $( N _ { i } ( t )   :   t   >   0 )$ is a Poisson process with rate $\lambda p _ { i }$ , for $i = 1 , 2 , \ldots , c ,$ and these c monochromatic processes are independent.

Proof. We will induct on c. For $c = 1$ there is nothing to show. For $c = 2$ the result is the thinning theorem that we already proved. Now assume that the result holds

---

Poisson processes

571

for c colors, and show it when there are $c + 1$ colors. Let’s call color 1 green. Use thinning to assign each arrival to be green with probability $p _ { 1 }$ and non-green with probability $1 - p _ { 1 }$ . This splits the Poisson process into 2 independent processes: a green process of rate $\lambda p _ { 1 }$ and a non-green process of rate $\lambda ( 1   -   p _ { 1 } )$ . By the inductive hypothesis, we can then split the non-green process into c independent processes, one for each of colors $2 , 3 , \ldots , c + 1$ , where color $j$ now gets probability

$$
\tilde {p} _ {j} = \frac {p _ {j}}{1 - p _ {1}} = \frac {p _ {j}}{p _ {2} + p _ {3} + \cdots + p _ {c + 1}},
$$

for $j = 2 , 3 , \ldots , c + 1$ . We then have $c + 1$ independent Poisson processes, one for each color, such that the process for color $j$ has rate $\lambda p _ { j }$ for $j = 1 , 2 , \ldots , c + 1$ 

The next example shows how coloring can help us decompose a complicated Poisson process into more manageable components.

Example 13.2.17 (Cars on a highway). Suppose cars enter a one-way highway from a common entrance, following a Poisson process with rate $\lambda .$ The ith car has velocity $V _ { i }$ and travels at this velocity forever; no time is lost when one car overtakes another car. Assume the $V _ { i }$ are i.i.d. discrete r.v.s whose support is a finite set of positive values. The process starts at time 0, and we’ll consider the highway entrance to be at location 0.

For fixed locations a and b on the highway with $0 < a < b$ , let $Z _ { t }$ be the number of cars located in the interval $[ a , b ]$ at time t. (For instance, on an interstate highway running west to east through the midwestern United States, $a$ could be Kansas City and $b$ could be St. Louis; then $Z _ { t }$ would be the number of cars on the highway that are in the state of Missouri at time t.) Figure 13.6 illustrates the setup of the problem and the definition of $Z _ { t }$

Assume that t is large enough that $t > b / V _ { i }$ for all possible values of $V _ { i }$ . Show that $Z _ { t }$ has a Poisson distribution with mean $\lambda ( b - a ) E ( V _ { i } ^ { - 1 } )$

## Solution:

Since the $V _ { i }$ are discrete with finite support, we can enumerate the set of possible velocities $v _ { 1 } , \ldots , v _ { m }$ and their probabilities $p _ { 1 } , \ldots , p _ { m }$ . After doing so, we realize that the cars entering the highway represent m types of arrivals, each corresponding to a different velocity. This suggests breaking up our overall Poisson process into simpler ones. Let’s color the Poisson process m ways according to the velocity of the cars, resulting in a Poisson process with rate $\lambda p _ { 1 }$ for cars of velocity $v _ { 1 }$ , a Poisson process with rate $\lambda p _ { 2 }$ for cars of velocity $v _ { 2 }$ , and so forth.

For each of these m separate Poisson processes, we can ask: within what time interval do cars from this process have to enter the highway in order to be in $[ a , b ]$ at time $t ?$ This is a matter of physics, not statistics:

$$
\text {distance} = \text {velocity} \cdot \text {time},
$$

so a car that enters the highway at time s with velocity v will be at position $( t - s ) v$

---

572

Introduction to Probability

![](../../raw/pages_0577-0592/images/page_588_chart_2.jpg)

<details>
<summary>scatter</summary>

| Time | Distance along highway |
| --- | --- |
| 0 | 0 |
| ~0.25 | 0 |
| ~0.4 | 0 |
| ~0.6 | 0 |
| ~0.8 | 0 |
| t | b |
| t | a |
| t | a |
| t | b |
</details>

## FIGURE 13.6

Cars enter a highway. Their entrance times form a Poisson process and are indicated by $\times   ^ { \prime } \mathrm { s }$ on the time axis. The ith car has velocity $V _ { i }$ , represented by the slope of the line emanating from the ith × symbol. We are interested in $Z _ { t }$ , the number of cars located in the interval $[ a , b ]$ at time t. Here we observe $Z _ { t } = 3$ , depicted by the three stars.

at time t. Thus, in order for the car’s position to be between $a$ and $b ,$ we require its arrival time to be between $t - b / v$ and $t - a / v$ . (By our assumption that $t$ is sufficiently large, we don’t need to worry about $t - b / v$ being negative.) If the car arrives prior to time $t   -   b / v$ , it will already have passed b by time $t ;$ if the car arrives after time $t - a / v$ , it won’t have reached a by time t.

We now have the answer for each of the separate Poisson processes. Within the process where cars have velocity $v _ { j }$ , the number of cars arriving between $t - b / v _ { j }$ and $t - a / v _ { j }$ , which we’ll call $Z _ { t j }$ , is distributed $\mathrm { P o i s } ( \lambda p _ { j } ( b - a ) / v _ { j } )$ : the rate of the process is $\lambda p _ { j }$ , and the length of the interval $[ t - b / v _ { j } , t - a / v _ { j } ]$ is $( b - a ) / v _ { j }$

Since the separate processes are independent, $Z _ { t 1 }$ through $Z _ { t m }$ are independent Poisson r.v.s. Thus,

$$
Z _ {t} = Z _ {t 1} + \dots + Z _ {t m} \sim \mathrm{Pois} \left(\lambda (b - a) \sum_ {j = 1} ^ {m} \frac {p _ {j}}{v _ {j}}\right),
$$

and $\textstyle \sum _ { j = 1 } ^ { m } p _ { j } / v _ { j }$ is the expectation of $V _ { i } ^ { - 1 }$ by LOTUS. This is what we wanted. 

---

Poisson processes

573

To wrap up this section, here is a table describing the correspondences between properties of the Poisson process and properties of the Poisson distribution. In the second column, $Y _ { 1 } \sim \operatorname { P o i s } ( \lambda _ { 1 } )$ and $Y _ { 2 } \sim \operatorname { P o i s } ( \lambda _ { 2 } )$ are independent.

| Poisson process | Poisson distribution |
| --- | --- |
| conditioning | $Y_1\|Y_1 + Y_2 = n \sim \text{Bin}(n, \lambda_1/(\lambda_1 + \lambda_2))$ |
| superposition | $Y_1 + Y_2 \sim \text{Pois}(\lambda_1 + \lambda_2)$ |
| thinning | chicken-egg story |

## 13.3 Poisson processes in multiple dimensions

Poisson processes in multiple dimensions are defined analogously to the 1D Poisson process: we just replace the notion of length with the notion of area or volume. For concreteness, we will now define 2D Poisson processes, after which it should also be clear by analogy how to define Poisson processes in higher dimensions.

Definition 13.3.1 (2D Poisson process). Events in the plane $\mathbb { R } ^ { 2 }$ are a 2D Poisson process with intensity λ if the following conditions hold:

1. The number of events in a region A is distributed $Pois (\lambda \cdot  area (A))$
2. The numbers of events in disjoint regions are independent of each other.

As one might guess, conditioning, superposition, and thinning properties apply to 2D Poisson processes. Let $N ( A )$ be the number of events in a region A, and let $B \subseteq A$ . Given $N ( A ) = n$ , the conditional distribution of $N ( B )$ is Binomial:

$$
N (B) | N (A) = n \sim \mathrm{Bin} \left(n, \frac {\mathrm{area} (B)}{\mathrm{area} (A)}\right).
$$

Conditional on the total number of events in the larger region $A ,$ the probability of an event falling into a subregion is proportional to the area of the subregion; thus the locations of the events are conditionally Uniform, and we can generate a 2D Poisson process in A by first generating the number of events $N ( A ) \sim \operatorname { P o i s } ( \lambda \cdot \operatorname { a r e a } ( A ) )$ and then placing the events uniformly at random in $A .$ Figure 13.7 shows simulated 2D Poisson processes in the square $[ 0 , 5 ] \times [ 0 , 5 ]$ for intensities $\lambda = 1 , 2 , 5$

As in the 1D case, the superposition of independent 2D Poisson processes is a 2D Poisson process, and the intensities add. We can also thin a 2D Poisson process to get independent 2D Poisson processes.

One property of 1D Poisson processes for which we haven’t asserted a higherdimensional analog is the count-time duality. The next example, the last in this chapter, will lead us to a spatial analog: a count-distance duality.

---

574

Introduction to Probability

![](../../raw/pages_0577-0592/images/page_590_image_2.jpg)

## FIGURE 13.7

Simulated 2D Poisson process in the square $[ 0 , 5 ] \times [ 0 , 5 ]$ , for $\lambda = 1 , 2 , 5 .$

Example 13.3.2 (Nearest star). Stars in a certain universe are distributed according to a 3D Poisson process with intensity λ. If you live in this universe, what is the distribution of the distance from you to the nearest star?

## Solution:

In a 3D Poisson process with intensity λ, the number of events in a region of space V is Poisson with mean λ·volume(V ). Let R be the distance from you to the nearest star. The key observation is that in order for the event $R > r$ to occur, there must be no stars within a sphere of radius r around you; in fact, these two events are equivalent. For any $r > 0$ , let $N _ { r }$ be the number of events within radius r of you, so $\begin{array} { r } { N _ { r } \sim \mathrm { P o i s } ( \lambda \cdot \frac { 4 } { 3 } \pi r ^ { 3 } ) } \end{array}$ . Then we have a count-distance duality:

$$
R > r \text {is the same event as} N _ {r} = 0,
$$

Therefore,

$$
P (R > r) = P (N _ {r} = 0) = e ^ {- \frac {4}{3} \lambda \pi r ^ {3}},
$$

which gives that the CDF of R is

$$
P (R \leq r) = 1 - e ^ {- \frac {4}{3} \lambda \pi r ^ {3}},
$$

for $r > 0$ (and 0 otherwise). This is a Weibull (see Example 6.5.5). Specifically,

$$
R \sim \mathrm{Wei} \left(\frac {4 \pi \lambda}{3}, 3\right).
$$

Poisson processes have numerous extensions, some of which are explored in the exercises. We can allow λ to vary as a function of time or space instead of remaining constant; this is called an inhomogeneous Poisson process. We can allow λ to be a random variable; this is called a Cox process. Finally, we can allow the rate to increase by λ after each successive arrival; this is called a Yule process.

---

Poisson processes

575

## 13.4 Recap

A Poisson process in one dimension is a sequence of arrivals such that the number of arrivals in any interval is Poisson (with mean proportional to the length of the interval) and disjoint intervals have independent numbers of arrivals. Some operations that we can perform with Poisson processes are conditioning, superposition, and thinning. Conditioning on the total number of arrivals in an interval allows us to view the arrivals as independent Uniforms on the interval. Superposition and thinning are complementary, and they allow us to split and merge Poisson processes when convenient. All of these properties have analogs for higher dimensions.

Poisson processes tie together many of the named distributions we have studied in this book:

• Poisson for the arrival counts,
• Exponential and Gamma for the interarrival times and arrival times,
• Binomial for the conditional counts,
• Uniform and (scaled) Beta for the conditional arrival times,
• Geometric and Negative Binomial for the discrete waiting times for special arrivals.

Poisson processes are also especially amenable to story proofs. A problem-solving strategy we used several times in this chapter is to embed r.v.s into a Poisson process in the hopes of discovering a story proof, even when the original problem appears to be unrelated to Poisson processes.

Poisson processes unite two of the important themes of this book, named distributions and stories, in a natural way. We think it is fitting to end with a topic that weaves together the story threads from throughout the book.

## 13.5 R

## 1D Poisson process

In Chapter 5, we discussed how to simulate a specified number of arrivals from a one-dimensional Poisson process by using the fact that the interarrival times are i.i.d. Exponentials. In this chapter, Story 13.2.4 tells us how to simulate a Poisson process within a specified interval (0, L]. We first generate the number of arrivals N(L), which is distributed Pois(λL). Conditional on N(L) = n, the arrival times

---

576

Introduction to Probability

are distributed as the order statistics of n i.i.d. Unif(0, L) r.v.s. The following code simulates arrivals from a Poisson process with rate 10 in the interval (0, 5]:

```r
L <- 5
lambda <- 10
n <- rpois(1,lambda*L)
t <- sort(runif(n,0,L))
```

To visualize the Poisson process we have generated, we can plot the cumulative number of arrivals N(t) as a function of t:

```txt
plot(t,1:n,type="s")
```

This produces a staircase plot as in Figure 13.8.

![](../../raw/pages_0593-0608/images/page_592_chart_7.jpg)

<details>
<summary>line</summary>

| t | N(t) |
| --- | --- |
| 0.2 | 1 |
| 0.3 | 4 |
| 0.5 | 6 |
| 0.6 | 8 |
| 0.7 | 9 |
| 0.8 | 10 |
| 0.9 | 11 |
| 1.0 | 12 |
| 1.1 | 13 |
| 1.2 | 14 |
| 1.3 | 15 |
| 1.4 | 16 |
| 1.5 | 17 |
| 1.6 | 18 |
| 1.7 | 19 |
| 1.8 | 20 |
| 1.9 | 21 |
| 2.0 | 22 |
| 2.1 | 23 |
| 2.2 | 24 |
| 2.3 | 25 |
| 2.4 | 26 |
| 2.5 | 27 |
| 2.6 | 28 |
| 2.7 | 29 |
| 2.8 | 30 |
| 2.9 | 31 |
| 3.0 | 32 |
| 3.1 | 33 |
| 3.2 | 34 |
| 3.3 | 35 |
| 3.4 | 36 |
| 3.5 | 37 |
| 3.6 | 38 |
| 3.7 | 39 |
| 3.8 | 40 |
| 3.9 | 41 |
| 4.0 | 42 |
| 4.1 | 43 |
| 4.2 | 44 |
| 4.3 | 45 |
| 4.4 | 46 |
| 4.5 | 47 |
| 4.6 | 48 |
| 4.7 | 49 |
| 4.8 | 50 |
| 4.9 | 51 |
</details>

FIGURE 13.8

Number of arrivals in a Poisson process with rate 10 in the interval (0, 5].

## Thinning

It is straightforward to thin a Poisson process in R. The following code starts with a vector of arrival times t and the corresponding number of arrivals n from a Poisson process of rate λ on some interval, generated as above. For each arrival, we flip a coin with probability $p$ of Heads; these coin tosses are stored in the vector $\mathbf { y } .$ Finally, the arrivals for which the coin landed Heads are labeled as type-1; the rest are labeled as type-2. The resulting vectors of arrival times, $\mathbf { t } _ { 1 }$ and $\mathbf { t } _ { 2 }$ , are realizations of independent Poisson processes of rates $\lambda p$ and $\lambda ( 1   -   p )$ , by Theorem 13.2.14.

---

Poisson processes

577

We can carry out this procedure for $p = 0 . 3$ as follows:

```txt
p <- 0.3
y <- rbinom(n,1,p)
t1 <- t[y==1]
t2 <- t[y==0]
```

## 2D Poisson process

Simulating a 2D Poisson process of rate λ on a square is nearly as easy as simulating a 1D Poisson process. In the square $( 0 , L ] \times ( 0 , L ]$ , the number of arrivals is distributed $\mathrm { P o i s } ( \lambda L ^ { 2 } )$ . Conditional on the number of arrivals, the locations of the arrivals are i.i.d. Uniform points in the square. By Example 7.1.23, the coordinates for each of these points are i.i.d. Unif(0, L). So for L = 5, λ = 10, we can type:

```r
L <- 5
lambda <- 10
n <- rpois(1,lambda*L^2)
x <- runif(n,0,L)
y <- runif(n,0,L)
```

## 13.6 Exercises

1. Passengers arrive at a bus stop according to a Poisson process with rate λ. The arrivals of buses are exactly t minutes apart. Show that on average, the sum of the waiting times of the riders on one of the buses is ${ \textstyle { \frac { 1 } { 2 } } } \lambda t ^ { 2 }$
2. Earthquakes occur over time according to a Poisson process with rate λ. The jth earthquake has intensity $Z _ { j }$ , where the $Z _ { j }$ are i.i.d. with mean $\mu$ and variance $\sigma ^ { 2 }$ . Find the mean and variance of the cumulative intensity of all the earthquakes up to time t.
3. Alice receives phone calls according to a Poisson process with rate λ. Unfortunately she has lost her cell phone charger. The battery’s remaining life is a random variable T with mean µ and variance $\sigma ^ { 2 }$ . Let $N ( T )$ be the number of phone calls she receives before the battery dies; find $E ( N ( T ) )$ , Var(N(T)), and $\mathrm{Cov}(T, N(T))$
4. Emails arrive in Bob’s inbox according to a Poisson process with rate $\lambda ,$ measured in emails per hour; each email is work-related with probability p and personal with probability $1 - p .$ The amount of time it takes to answer a work-related email is a random variable with mean $\mu _ { W }$ and variance $\sigma _ { W } ^ { 2 }$ , the amount of time it takes to answer a personal email has mean $\mu _ { P }$ and variance $\sigma _ { P } ^ { 2 }$ , and the response times for different emails are independent.
What is the average amount of time Bob has to spend answering all the emails that arrive in a t-hour interval? What about the variance?
5. In an endless soccer match, goals are scored according to a Poisson process with rate λ. Each goal is made by team A with probability p and team B with probability $1 - p .$ For $j > 1$ , the jth goal is a turnaround if it is made by a different team than the $( j - 1 ) \mathrm { s }$ t goal; for example, in the sequence AABBA. . . , the 3rd and 5th goals are turnarounds.

---

578

Introduction to Probability

(a) In n goals, what is the expected number of turnarounds?
(b) If an A-to-B turnaround has just occurred, what is the expected time until the next B-to-A turnaround?

6. Let $N _ { t }$ be the number of arrivals up until time t in a Poisson process of rate $\lambda ,$ and let $T _ { n }$ be the time of the nth arrival. Consider statements of the form

$$
P \left(N _ {t} \lessgtr 1 n\right) = P \left(T _ {n} \lessgtr 2 t\right),
$$

where $\lessgtr$ and $\lessgtr 2$ are replaced by symbols from the list $< , \leq , \geq , >$ . Which of these statements are true?

7. Claims against an insurance company follow a Poisson process with rate $\lambda > 0 .$ A total of $N$ claims were received over two disjoint time periods of combined length $t = t _ { 1 } + t _ { 2 }$ with $t _ { i }$ the length of period i.

(a) Given this information, derive the conditional probability distribution of $N _ { 1 }$ , the number of claims made in the first period, given N.

(b) The amount paid for the ith claim is $X _ { i } ,$ with $X _ { 1 } , X _ { 2 } , \ldots { ~ \operatorname { i . i . d . } }$ and independent of the claims process. Let $E(X_{i}) = \mu, \mathrm{Var}(X_{i}) = \sigma^{2}$ , for $i = 1 , \ldots , N$ . Given N, find the mean and variance of the total claims paid in period 1. That is, find these two conditional moments of the quantity

$$
W _ {1} = \sum_ {i = 1} ^ {N _ {1}} X _ {i},
$$

where (by convention) $W_{1}=0\  if \ N_{1}=0$

8. On a certain question-and-answer website, $N \sim \mathrm{Poisson}(\lambda_1)$ questions will be posted tomorrow, with $\lambda _ { 1 }$ measured in questions/day. Given N, the post times are i.i.d. and uniformly distributed over the day (a day begins and ends at midnight). When a question is posted, it takes an $\mathrm{Exp}(\lambda_{2})$ amount of time (in days) for an answer to be posted, independent of what happens with other questions.

(a) Find the probability that a question posted at a uniformly random time tomorrow will not yet have been answered by the end of that day.
(b) Find the joint distribution of how many answered and unanswered questions posted tomorrow there will be at the end of that day.

9. An inhomogeneous Poisson process in one dimension is a Poisson process whose rate, instead of being constant, is a nonnegative function $\lambda ( t )$ of time. Formally, we require that the number of arrivals in the interval $[ t _ { 1 } , t _ { 2 } )$ be Poisson-distributed with mean $\textstyle \int _ { t _ { 1 } } ^ { t _ { 2 } } \lambda ( t ) d t$ and that disjoint intervals be independent. When $\lambda ( t )$ is constant, this reduces to the definition of the ordinary or homogeneous Poisson process.

(a) Show that we can generate arrivals from an inhomogeneous Poisson process in the interval $[ t _ { 1 } , t _ { 2 } )$ using the following procedure.

1. Let $\lambda _ { \mathrm { m a x } }$ be the maximum value of $\lambda ( t )$ in the interval $[ t _ { 1 } , t _ { 2 } )$ . Create a 2D rectangle $[ t _ { 1 } , t _ { 2 } ) \times [ 0 , \lambda _ { \operatorname* { m a x } } ]$ , and plot the function $\lambda ( t )$ in the rectangle.

2. Generate $N \sim \operatorname { P o i s } ( \lambda _ { \operatorname* { m a x } } ( t _ { 2 } - t _ { 1 } ) )$ , and place N points uniformly at random in the rectangle.

3. For each of the N points: if the point falls below the curve $\lambda ( t )$ , accept it as an arrival in the process, and take its horizontal coordinate to be its arrival time. If the point falls above the curve $\lambda ( t )$ , reject it.

Hint: Verify that the two conditions in the definition are satisfied.

(b) Suppose we have an inhomogeneous Poisson process with rate function $\lambda ( t )$ . Let

---

Poisson processes

579

N(t) be the number of arrivals up to time t and $T _ { j }$ be the time of the jth arrival. Explain why the hybrid joint PDF of $N ( t )$ and $T _ { 1 } , \ldots , T _ { N ( t ) }$ , which constitute all the data observed up to time t, is given by

$$
f (n, t _ {1}, \ldots , t _ {n}) = \frac {e ^ {- \lambda_ {\mathrm{total}}} \lambda_ {\mathrm{total}} ^ {n}}{n !} \cdot n! \frac {\lambda (t _ {1}) \ldots \lambda (t _ {n})}{\lambda_ {\mathrm{total}} ^ {n}} = e ^ {- \lambda_ {\mathrm{total}}} \lambda (t _ {1}) \ldots \lambda (t _ {n})
$$

for $0 < t _ { 1 } < t _ { 2 } < \cdots < t _ { n }$ and nonnegative integer n, where $\begin{array} { r } { \lambda _ { \mathrm { t o t a l } } = \int _ { 0 } ^ { t } \lambda ( u ) d u . } \end{array}$

10. A Cox process is a generalization of a Poisson process, where the rate λ is a random variable. That is, λ is generated according to some distribution on $( 0 , \infty )$ and then, given that value of λ, a Poisson process with that rate is generated.

(a) Explain intuitively why disjoint intervals in a 1D Cox process are not independent.

(b) In a 1D Cox process where $\lambda   \sim   \mathrm { G a m m a } ( \alpha , \beta )$ , find the covariance between the number of arrivals in [0, t) and the number of arrivals in $[ t , t + s )$

Hint: Condition on λ.

11. In a Yule process with rate λ, the rate of arrivals increases after each new arrival, so that the time of the first arrival is $\operatorname { E x p o } ( \lambda )$ and the time between the $( j - 1 )$ st and jth arrivals is $\operatorname{Expo}(j\lambda)$ for $j = 2 , 3 , \ldots . \mathrm { S o }$ interarrival times are independent but not i.i.d.

(a) Show that the superposition of two independent Yule processes with the same rate λ is a Yule process, except shifted so that the interarrival times are Expo(2λ), Expo(3λ), Expo(4λ), . . . rather than Expo(λ), Expo(2λ), Expo(3λ), . . .

(b) Show that if we project the process from Part (a) into discrete time, the resulting sequence of type-1 and type-2 arrivals is equivalent to the following discrete-time process:

1. Start with two balls in an urn, labeled 1 and 2.

2. Draw a ball out of the urn at random, note its number, and replace it along with another ball with the same number.

3. Repeat step 2 over and over.

12. Consider the coupon collector problem: there are n toy types, and toys are collected one by one, sampling with replacement from the set of toy types each time. We solved this problem in Chapter 4, assuming that all toy types are equally likely. Now suppose that at each stage, the jth toy type is collected with probability $p _ { j }$ , where the $p _ { j }$ are not necessarily equal. Let N be the number of toys needed until we have a full set; we wish to find $E ( N )$ . This problem outlines an embedding method for calculating $E ( N )$

(a) Suppose that the toys arrive according to a Poisson process with rate 1, so that the interarrival times between toys are i.i.d. $X _ { j } \sim \operatorname { E x p o ( 1 ) }$ . For $j = 1 , \ldots , n$ let $Y _ { j }$ be the waiting time until the first toy of type $j .$ What are the distributions of the $Y _ { j } ?$ Are the $Y _ { j }$ independent?

(b) Explain why $T = \operatorname* { m a x } ( Y _ { 1 } , \ldots , Y _ { n } )$ , the waiting time until all toy types are collected, can also be written as $X _ { 1 } + \dots + X _ { N }$ , where the $X _ { j }$ are defined as in Part (a). Use this to show that $E ( T ) = E ( N )$

(c) Show that $E ( T )$ , and hence $E ( N )$ , can be found by computing the integral

$$
\int_ {0} ^ {\infty} \left(1 - \prod_ {j = 1} ^ {n} (1 - e ^ {- p _ {j} t})\right) d t.
$$

Hint: Use the identity $\begin{array} { r } { E ( T ) = \int _ { 0 } ^ { \infty } P ( T > t ) d t } \end{array}$ , which was shown in Example 5.3.8.

---

![](../../raw/pages_0593-0608/images/page_596_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

---

Math

## A.1 Sets

A set is a Many that allows itself to be thought of as a One.

– Georg Cantor

A set is a collection of objects. The objects can be anything: numbers, people, cats, courses, even other sets! The language of sets allows us to talk precisely about events. If S is a set, then the notation $x   \in   S$ indicates that x is an element or member of the set S (and x /∈ S indicates that x is not in S). We can think of the set as a club, with precisely defined criteria for membership. For example:

1. {1, 3, 5, 7, . . . } is the set of all odd numbers;
2. R is the set of all real numbers;
3. {Worf, Jack, Tobey} is the set of Joe’s cats;
4. [3, 7] is the closed interval consisting of all real numbers between 3 and 7;
5. {HH, HT, T H, T T} is the set of all possible outcomes if a coin is flipped twice (where, for example, HT means the first flip lands Heads and the second lands Tails).

To describe a set (when it’s tedious or impossible to list out its elements), we can give a rule that says whether each possible object is or isn’t in the set. For example, $\{ ( x , y ) \in \mathbb { R } ^ { 2 } : x ^ { 2 } + y ^ { 2 } \leq 1 \}$ is the disk of radius 1 in the plane $\mathbb { R } ^ { 2 }$ , centered at the origin. In this expression, the “:” is read as “such that”.

## A.1.1 The empty set

The smallest set, which is both subtle and important, is the empty set, which is the set that has no elements whatsoever. It is denoted by ∅ or by {}. Make sure not to confuse ∅ with {∅}. The former has no elements, while the latter has one element. If we visualize the empty set as an empty paper bag, then we can visualize {∅} as a paper bag inside of a paper bag.

581

---

582

Introduction to Probability

## A.1.2 Subsets

If A and B are sets, then we say A is a subset of B (and write $A \subseteq B )$ if every element of A is also an element of B. For example, the set of all integers is a subset of the set of all real numbers. It is always true that $\varnothing$ and A itself are subsets of A; these are the extreme cases for subsets. A general strategy for showing that $A \subseteq B$ is to let x be an arbitrary element of A, and then show that x must also be an element of B. A general strategy for showing that $A = B$ for two sets A and B is to show that each is a subset of the other.

## A.1.3 Unions, intersections, and complements

The union of two sets A and B, written as $A \cup B$ , is the set of all objects that are in A or B (or both). The intersection of A and B, written as $A \cap B$ , is the set of all objects that are in both A and B. We say that A and $B$ are disjoint if ${ \overline { { A } } } \cap B = \emptyset$ For n sets $A _ { 1 } , \ldots , A _ { n }$ , the union $A _ { 1 } \cup A _ { 2 } \cup \cdots \cup A _ { n }$ is the set of all objects that are in at least one of the $A _ { j } { } ^ { \gamma } \mathrm { s } _ { 1 }$ while the intersection $A _ { 1 } \cap A _ { 2 } \cap \cdots \cap A _ { n }$ is the set of all objects that are in all of the $A _ { j } { } ^ { \mathfrak { j } } \mathrm { s }$

In many applications, all the sets we’re working with are subsets of some set $S$ (in probability, this may be the set of all possible outcomes of some experiment). When S is clear from the context, we define the complement of a set A to be the set of all objects in $S$ that are not in $A ;$ this is denoted by $A ^ { c }$

Unions, intersections, and complements can be visualized easily using Venn diagrams, such as the one shown below. The union is the entire shaded region, while the intersection is the football-shaped region of points that are in both A and B. The complement of A is all points in the rectangle that are outside of A.

![](../../raw/pages_0593-0608/images/page_598_image_8.jpg)

<details>
<summary>text_image</summary>

S
A∩B
A
B
</details>

FIGURE A.1

A Venn diagram.

Note that the area of the region $A \cup B$ is the area of A plus the area of $B ,$ minus the area of $A \cap B$ (this is a basic form of the inclusion-exclusion principle).

---

Math

583

De Morgan’s laws give an elegant, useful duality between unions and intersections:

$$
(A _ {1} \cup A _ {2} \cup \dots \cup A _ {n}) ^ {c} = A _ {1} ^ {c} \cap A _ {2} ^ {c} \cap \dots \cap A _ {n} ^ {c}
$$

$$
(A _ {1} \cap A _ {2} \cap \dots \cap A _ {n}) ^ {c} = A _ {1} ^ {c} \cup A _ {2} ^ {c} \cup \dots \cup A _ {n} ^ {c}
$$

It is much more important to understand De Morgan’s laws than to memorize them! The first law says that not being in at least one of the $A _ { j }$ is the same thing as not being in $A _ { 1 }$ , nor being in $A _ { 2 }$ , nor being in $A _ { 3 }$ , etc.

For example, let $A _ { j }$ be the set of people who like the jth Star Wars prequel, for $j \in \{ 1 , 2 , 3 \}$ . Then $\bar { ( } A _ { 1 } \cup A _ { 2 } \cup A _ { 3 } ) ^ { c }$ is the set of people for whom it is not the case that they like at least one of the prequels, but that is the same as $A _ { 1 } ^ { c } \cap A _ { 2 } ^ { c } \cap A _ { 3 } ^ { c }$ , the set of people who don’t like The Phantom Menace, don’t like Attack of the Clones, and don’t like Revenge of the Sith.

The second law says that not being in all of the $A _ { j }$ is the same thing as being outside at least one of the $A _ { j }$ . For example, let the $A _ { j }$ be defined as in the previous paragraph. If it is not the case that you like all of the Star Wars prequels (making you a member of the set $( A _ { 1 } { \cap } A _ { 2 } { \cap } A _ { 3 } ) ^ { c } )$ , then there must be at least one prequel that you don’t like (making you a member of the set $A _ { 1 } ^ { c } \cup A _ { 2 } ^ { c } \cup A _ { 3 } ^ { c } )$ , and vice versa.

Proving the following facts about sets (not just drawing Venn diagrams, though they are very helpful for building intuition) is good practice:

1. $A \cap B$ and $A \cap B ^ { c }$ are disjoint, with $(A \cap B) \cup (A \cap B^c) = A$
2. $A \cap B = A$ if and only if $A \subseteq B$
3. $A \subseteq B$ if and only if $B ^ { c } \subseteq A ^ { c }$

## A.1.4 Partitions

A collection of subsets $A _ { 1 } , \ldots , A _ { n }$ of a set $S$ is a partition of S if $A _ { 1 } \cup \cdots \cup A _ { n } = S$ and $A _ { i } \cap A _ { j }   =   \emptyset$ for all $i   \neq   j$ . In words, a partition of a set is a collection of disjoint subsets whose union is the entire set. For example, the set of even numbers $\{ 0 , 2 , 4 , \dots \}$ and the set of odd numbers $\{ 1 , 3 , 5 , \dots \}$ form a partition of the set of nonnegative integers.

## A.1.5 Cardinality

A set may be finite or infinite. If A is a finite set, we write $| A |$ for the number of elements in $A ,$ which is called its size or cardinality. For example, $| \{ 2 , 4 , 6 , 8 , 1 0 \} | = 5$ since there are 5 elements in this set. A very useful fact is that A and $B$ are finite sets, then

$$
| A \cup B | = | A | + | B | - | A \cap B |.
$$

---

584

Introduction to Probability

This is a form of the inclusion-exclusion theorem from Chapter 1. It says that to count how many elements are in the union of A and B, we can add the separate counts for each, and then adjust for the fact that we have double-counted the elements (if any) that are in both A and B.

Two sets A and B are said to have the same size or same cardinality if they can be put into one-to-one correspondence, i.e., if each element of A can be paired up with exactly one element of $B ,$ with no unpaired elements in either set. We say that A is smaller than B if there is not a one-to-one correspondence between A and B, but there is a one-to-one correspondence between A and some subset of B.

For example, suppose that we want to count the number of people in a movie theater with 100 seats. Assume that no one in the theater is standing, and no seat has more than one person in it. The obvious thing to do is to go around counting people one by one (though it’s surprisingly easy to miss someone or accidentally count someone twice). But if every seat is occupied, then a much easier method is to note that there must be 100 people, since there are 100 seats and there is a one-to-one correspondence between people and seats. If some seats are empty, then there must be fewer than 100 people there.

This idea of looking at one-to-one correspondences makes sense both for finite and for infinite sets. Consider the perfect squares $1 ^ { 2 } , 2 ^ { 2 } , 3 ^ { 2 } , \ldots .$ . Galileo pointed out the paradoxical result that on the one hand it seems like there are fewer perfect squares than positive integers (since every perfect square is a positive integer, but lots of positive integers aren’t perfect squares), but on the other hand it seems like these two sets have the same size since they can be put into one-to-one correspondence: pair $1 ^ { 2 }$ with 1, pair $2 ^ { 2 }$ with 2, pair $3 ^ { 2 }$ with 3, etc.

The resolution of Galileo’s paradox is to realize that intuitions about finite sets don’t necessarily carry over to infinite sets. By definition, the set of all perfect squares and the set of all positive integers do have the same size. Another famous example of this is Hilbert’s hotel. For any hotel in the real world the number of rooms is finite. If every room is occupied, there is no way to accommodate more guests, other than by cramming more people into already occupied rooms.

Now consider an imaginary hotel with an infinite sequence of rooms, numbered 1, 2, 3, . . . . Assume that all the rooms are occupied, and that a weary traveler arrives, looking for a room. Can the hotel give the traveler a room, without leaving any of the current guests without a room? Yes, one way is to have the guest in room n move to room $n + 1$ , for all $n = 1 , 2 , 3 , \ldots$ . This frees up room 1, so the traveler can stay there.

What if infinitely many travelers arrive at the same time, such that their cardinality is the same as that of the positive integers (so we can label the travelers as traveler 1, traveler $2 , \ldots ) ?$ The hotel could fit them in one by one by repeating the above procedure over and over again, but it would take forever (infinitely many moves) to accommodate everyone, and it would be bad for business to make the current guests keep moving over and over again. Can the room assignments be updated just once

---

Math

585

so that everyone has a room? Yes, one way is to have the guest in room n move to room to 2n for all $n = 1 , 2 , 3 , \ldots$ , and then have traveler n move into room $2 n - 1$ In this way, the current guests occupy all the even-numbered rooms, and the new guests occupy all the odd-numbered rooms.

An infinite set is called countably infinite if it has the same cardinality as the set of all positive integers. A set is called countable if it is finite or countably infinite, and uncountable otherwise. The mathematician Cantor showed that not all infinite sets are the same size. In particular, the set of all real numbers is uncountable, as is any interval in the real line of positive length.

## A.1.6 Cartesian product

The Cartesian product of two sets A and B is the set

$$
A \times B = \{(a, b): a \in A,   b \in B \}.
$$

For example, $[ 0 , 1 ] \times [ 0 , 1 ]$ is the square $\{ ( x , y ) : x , y \in [ 0 , 1 ] \}$ , and $\mathbb { R } \times \mathbb { R } = \mathbb { R } ^ { 2 }$ is two-dimensional Euclidean space.

## A.2 Functions

Let A and B be sets. A function from A to B is a deterministic rule that, given an element of A as input, provides an element of B as an output. That is, a function from A to B is a machine that takes an x in A and “maps” it to some y in B. Different x’s can map to the same y, but each x only maps to one y. Here A is called the domain and B is called the target. The notation $f : A \to B$ says that f is a function mapping A into B. The range of f is $\{ y \in B : f ( x ) = y$ for some $x \in A \}$

It is important to distinguish between f (the function) and $f ( x )$ (the value of the function when evaluated at x). That is, f is a rule, while $f ( x )$ is a number for each number x. The function g given by $g ( x ) = e ^ { - x ^ { 2 } / 2 }$ is exactly the same as the function g given by $g ( t ) = e ^ { - t ^ { 2 } / 2 }$ ; what matters is the rule, not the name we use for the input. For this example, the rule is that x gets mapped to $e ^ { - x ^ { 2 } / 2 }$ ; this rule is also denoted by $x \mapsto e ^ { - x ^ { 2 } / 2 }$

A function f from the real line to the real line is continuous if $f ( x ) \rightarrow f ( a )$ as $x \rightarrow a$ for any value of a. It is called right-continuous if this is true when approaching from the right, i.e., $f ( x ) \to f ( a )$ as $x \rightarrow a$ while ranging over values with $x > a$

The set A may not be a set of numbers. In probability, it is extremely common and useful to consider functions whose domains are the set of all possible outcomes of some experiment. It may be difficult to write down a formula for the function, but the function is still valid as long as it’s defined unambiguously.

---

586

Introduction to Probability

## A.2.1 One-to-one functions

Let $f$ be a function from A to B. Then f is a one-to-one function if $f(x) \neq f(y)$ whenever $x \neq y$ . That is, any two distinct inputs in A get mapped to two distinct outputs in $B ;$ for each $y$ in $B ,$ there can be at most one x in A that maps to it.

Let $f$ be a one-to-one function from A to B, and let C be the range of $f ,$ i.e.,

$$
C = \{b \in B: f (a) = b \text {for some} x \in A \}.
$$

Then there is an inverse function $f ^ { - 1 } : C \to A$ , defined by letting $f ^ { - 1 } ( y )$ be the unique element $x \in A$ such that $f ( x ) = y$ . A function that has an inverse is called an invertible function.

For example, let $f ( x ) = x ^ { 2 }$ for all real x. This is not a one-to-one function since, for example, $f(3) = f(-3)$ . But now assume instead that the domain of f is chosen to be $[ 0 , \infty )$ , so we are defining $f$ as a function from $[ 0 , \infty )$ to $[ 0 , \infty )$ . Then $f$ is one-to-one, and its inverse function is given by $f ^ { - 1 } ( y ) = { \sqrt { y } }$ for all $y \in [ 0 , \infty )$

The pigeonhole principle says that if A and B are finite sets with $| A | > | B |$ , then there does not exist a one-to-one function from A to B. In other words, if k objects are placed into n boxes, where $k   >   n$ , then there must be at least one box that contains more than one object.

For example, in the birthday problem from Chapter 1 (assuming there are 365 days in a year), with 366 or more people there is guaranteed to be at least one birthday match. There is no one-to-one function assigning a birthday to each of the people, when there are more people than there are days in a year.

## A.2.2 Increasing and decreasing functions

Let $f : A \to \mathbb { R }$ , where A is a set of real numbers. Then f is an increasing function if $x \leq y$ implies $f ( x ) \leq f ( y )$ (for all $x , y \in A )$ . Note that this definition allows there to be regions where $f$ is flat, e.g., the constant function that is equal to 42 everywhere is an increasing function, and any CDF (see Section 3.6) is an increasing function. We say that $f$ is strictly increasing if $x   <   y$ implies $f ( x )   <   f ( y )$ . For example, $f : \mathbb { R } \rightarrow \mathbb { R }$ with $f ( x ) = x ^ { 3 }$ is a strictly increasing function.

Similarly, f is a decreasing function if $x \leq y$ implies $f ( x ) \geq f ( y )$ , and is a strictly decreasing function if $x < y$ implies $f(x) > f(y)$ . For example, $f : ( 0 , \infty ) \to ( 0 , \infty )$ with $f ( x ) = 1 / x$ is a strictly decreasing function.

A monotone function is a function that is either increasing or decreasing. A strictly monotone function is a function that is either strictly increasing or strictly decreasing. Note that any strictly monotone function is one-to-one.

---

Math

587

## A.2.3 Even and odd functions

Let $f$ be a function from R to R. We say $f$ is an even function if $f(x) = f(-x)$ for all x, and we say $f$ is an odd function if $-f(x)=f(-x)$ for all x. If neither of these conditions is satisfied, then $f$ is neither even nor odd. Figure A.2 shows the graphs of two even functions and two odd functions.

![](../../raw/pages_0593-0608/images/page_603_image_4.jpg)

## FIGURE A.2

Even and odd functions. The graphs on the left are even functions: $f ( x ) = x ^ { 2 }$ on the top and $f ( x ) = e ^ { - x ^ { 2 } / 2 }$ on the bottom. The graphs on the right are odd functions: $f ( x ) = x ^ { 3 }$ on the top and $f ( x ) = x e ^ { - x ^ { 2 } / 2 }$ on the bottom.

Even and odd functions have nice symmetry properties. The graph of an even function remains the same if you reflect it about the vertical axis, and the graph of an odd function remains the same if you rotate it 180 degrees around the origin.

---

588

Introduction to Probability

Even functions have the property that for any $a ,$

$$
\int_ {- a} ^ {a} f (x) d x = 2 \int_ {0} ^ {a} f (x) d x,
$$

assuming the integral exists. This is because the area under the function from $- a$ to $0$ is equal to the area under the function from 0 to $a .$ Odd functions have the property that for any $a ,$

$$
\int_ {- a} ^ {a} f (x) d x = 0,
$$

again assuming the integral exists. This is because the area under the function from $- a$ to $0$ cancels the area under the function from $0$ to $a .$

## A.2.4 Convex and concave functions

A function g whose domain is an interval I is convex if

$$
g (p x _ {1} + (1 - p) x _ {2}) \leq p g (x _ {1}) + (1 - p) g (x _ {2})
$$

for all $x _ { 1 } , x _ { 2 }   \in   I$ and $p   \in   ( 0 , 1 )$ . Geometrically, this says that if we draw a line segment connecting two points on the graph of $g ,$ then the line segment lies above the graph of $g .$ If the derivative $g ^ { \prime }$ exists, then an equivalent definition is that every tangent line to the graph of $g$ lies below the graph. If $g ^ { \prime \prime }$ exists, then an equivalent definition is that $g ^ { \prime \prime } ( x ) \geq 0$ for all $x \in I$ . An example is shown in Figure A.3. A simple example is $g ( x ) = x ^ { 2 }$ , whose second derivative is $g^{\prime\prime}(x) = 2 > 0$

![](../../raw/pages_0593-0608/images/page_604_image_11.jpg)

<details>
<summary>text_image</summary>

y = g(x)
</details>

## FIGURE A.3

Graph of a convex function $g .$ We have $g ^ { \prime \prime } ( x ) \geq 0$ . Any line segment connecting two points on the curve lies above the curve. Any tangent line lies below the curve.

A function $g$ is concave ${ \mathrm { i f ~ } } { - g }$ is convex. If $g ^ { \prime \prime }$ exists, then $g$ is concave if and only if $g ^ { \prime \prime } ( x ) \leq 0$ for all $x$ in the domain. For example, $g ( x ) = \log ( x )$ defines a concave function on $( 0 , \infty )$ since $g''(x) = -1/x^2 < 0$ for all $x \in ( 0 , \infty )$

---

Math

589

## A.2.5 Exponential and logarithmic functions

An exponential function is a function of the form $f ( x ) = a ^ { x }$ for some number $a > 0$ If $a > 1$ , the function is increasing, and if $0 < a < 1$ , the function is decreasing. The most common exponential function we’ll work with is $f ( x ) = e ^ { x }$ , and a very useful limit result to know is that

$$
\left(1 + \frac {x}{n}\right) ^ {n} \rightarrow e ^ {x}
$$

as $n \to \infty$ , for any real number x. This has an interpretation in terms of a bank paying compound interest on a deposit: as compounding occurs more and more times per year, the growth rate approaches exponential growth.

Here are some properties of exponential functions:

1. $a ^ { x } a ^ { y } = a ^ { x + y } .$
2. $a ^ { x } b ^ { x } = ( a b ) ^ { x } .$
3. $( a ^ { x } ) ^ { y } = a ^ { x y } .$

The inverse of an exponential function is a logarithmic function: for positive $y , \log _ { a } y$ is defined to be the number x such that $a ^ { x } = y$ . Throughout this book, when we write log y without explicitly specifying the base, we are referring to the natural logarithm (base e).

Here are some properties of logarithms:

1. $\log _ { a } x + \log _ { a } y = \log _ { a } x y .$
2. $\log _ { a } x ^ { n } = n \log _ { a } x .$
3. lo $\begin{array} { r } { \operatorname { g } _ { a } x = { \frac { \log x } { \log a } } } \end{array}$

## A.2.6 Floor function and ceiling function

The floor function is defined by letting $\lfloor x \rfloor$ be the greatest integer less than or equal to x. That is, it says to round down to an integer. For example, $[ 3 . 1 4 ] = 3 ,$ $\left[ -1.3 \right] = -2$ , and $[ 5 ] = 5$ . (Some books denote the floor function by [x] but this is bad notation since it does not suggest a corresponding notation for the ceiling function, and since square brackets are also used for other purposes.)

The ceiling function is defined by letting $\lceil x \rceil$ be the smallest integer greater than or equal to x. For example, $\lceil 3.14 \rceil = 4,   \lceil -1.3 \rceil = -1$ , and $\lceil 5 \rceil = 5$

---

590

Introduction to Probability

## A.2.7 Factorial function and gamma function

The factorial function takes a positive integer n and returns the product of the integers from 1 to n, denoted n! and read $^ { \mathfrak { a } } n$ factorial”:

$$
n! = n (n - 1) (n - 2) \dots 1.
$$

Also, we define $0 ! = 1$ . This convention makes sense since if we think of n! as the number of ways in which n people can line up, there is 1 way for $n = 0$ (this just means there is no one there, so the line is empty). It is also very helpful since, for example, we can then say that $n ! / ( n - 1 ) ! = n$ for all positive integers n without running into trouble when $n = 1$

The factorial function grows extremely quickly as n grows. A famous, useful approximation for factorials is Stirling’s formula,

$$
n! \approx \sqrt {2 \pi n} \left(\frac {n}{e}\right) ^ {n}.
$$

The ratio of the two sides converges to 1 as $n \to \infty$ . For example, direct calculation gives $5 2 ! \approx 8 . 0 6 6 \times 1 0 ^ { 6 7 }$ , while Stirling’s formula says $5 2 ! \approx 8 . 0 5 3 \times 1 0 ^ { 6 7 }$

The gamma function Γ generalizes the factorial function to positive real numbers; it is defined by

$$
\Gamma (a) = \int_ {0} ^ {\infty} x ^ {a} e ^ {- x} \frac {d x}{x}, \quad a > 0,
$$

and has the property that

$$
\Gamma (n) = (n - 1)!
$$

for all positive integers n. Also, $\Gamma ( 1 / 2 ) = { \sqrt { \pi } } .$

An important property of the gamma function, which generalizes the fact that $n ! = n \cdot ( n - 1 ) !$ , is that

$$
\Gamma (a + 1) = a \Gamma (a)
$$

for all $a > 0$ . See Chapter 8 for more about the gamma function.

## A.3 Matrices

Neo: What is the Matrix?

Trinity: The answer is out there, Neo, and it’s looking for you, and it will find you if you want it to.

– The Matrix (film from 1999)

A matrix is a rectangular array of numbers, such as ${ \binom { 3 \quad 1 / e } { 2 \pi \quad 1 } } { \mathrm { ~ o r ~ } } { \binom { 1 \quad 1 \quad 0 } { 1 \quad 2 \quad 3 } }$ . We

---

Math

591

say that the dimensions of a matrix are m by n (also written $m \times n )$ if it has m rows and n columns (so the former example is 2 by 2, while the latter is 2 by 3). The matrix is called square if $m = n$ . If $m = 1$ , we have a row vector ; if $n = 1$ , we have a column vector. We write $A = ( a _ { i j } )$ to indicate that the row $i ,$ column $j$ entry of A is $a _ { i j }$

## A.3.1 Matrix addition and multiplication

To add two matrices A and B with the same dimensions, just add the corresponding entries, e.g.,

$$
\left( \begin{array}{c c c} 1 & 1 & 0 \\ 1 & 1 & 1 \end{array} \right) + \left( \begin{array}{c c c} 1 & 0 & 0 \\ 1 & 1 & 0 \end{array} \right) = \left( \begin{array}{c c c} 2 & 1 & 0 \\ 2 & 2 & 1 \end{array} \right).
$$

When we multiply an $m \times n$ matrix A by an $n \times r$ matrix $B .$ we obtain an $m \times r$ matrix $A B$ . The product AB is undefined if the number of columns of A does not equal the number of rows of B.

The row $i ,$ column $j$ entry of AB is $\textstyle \sum _ { k = 1 } ^ { n } a _ { i k } b _ { k j }$ , where $a _ { i j }$ and $b _ { i j }$ are the row $i ,$ column $j$ entries of A and $B ,$ respectively. For example, here is how to multiply a $2 \times 3$ matrix by a $3 \times 1$ vector:

$$
\left( \begin{array}{c c c} 1 & 2 & 3 \\ 4 & 5 & 6 \end{array} \right) \left( \begin{array}{c} 7 \\ 8 \\ 9 \end{array} \right) = \binom{1 \cdot 7 + 2 \cdot 8 + 3 \cdot 9}{4 \cdot 7 + 5 \cdot 8 + 6 \cdot 9} = \binom{5 0}{1 2 2}.
$$

Note that AB may not equal $B A$ , even if both are defined. To multiply a matrix A by a scalar, just multiply each entry by that scalar.

The transpose of a matrix A is the matrix whose row $i ,$ column $j$ entry is the row $j ,$ column i entry of A. It is denoted by $A ^ { \prime }$ and read as $^ { \circ } A$ transpose”. The rows of A are the columns of $A ^ { \prime } ,$ and the columns of A are the rows of $A ^ { \prime } ,$ A square matrix A is symmetric if $A ^ { \prime } = A$ . A useful property of transposes is that if A and B are matrices such that the product AB is defined, then $( A B ) ^ { \prime } = B ^ { \prime } A ^ { \prime }$

The determinant of a $2 \times 2$ matrix is defined by

$$
\left| \begin{array}{c c} a & b \\ c & d \end{array} \right| = a d - b c.
$$

Determinants can also be defined for $n \times n$ matrices, in a recursive manner not reviewed here.

## A.3.2 Eigenvalues and eigenvectors

An eigenvalue of an $n \times n$ matrix A is a number λ such that

$$
A \mathbf {v} = \lambda \mathbf {v}
$$

---

592

Introduction to Probability

for some $n \times 1$ column vector v, where the elements of v are not all zero. The vector v is called an eigenvector of A, or a right eigenvector. (Similarly, a left eigenvector of A is a row vector w satisfying $\mathbf { w } A = \lambda \mathbf { w }$ for some λ.) This definition says that when A and v are multiplied, v just gets stretched by the constant λ.

Some matrices have no real eigenvalues, but the Perron-Frobenius theorem tells us that in a special case that is of particular interest to us in Chapter 11, eigenvalues exist and have nice properties. Let A be a square matrix whose entries are nonnegative and whose rows sum to 1. Further assume that for all i and $j ,$ there exists $k \geq 1$ such that the row i, column $j$ entry of $A ^ { k }$ is positive. Then the Perron-Frobenius theorem says that 1 is an eigenvalue of A, which is in fact the largest eigenvalue of $A ,$ and there is a corresponding eigenvector whose entries are all positive.

## A.4 Difference equations

A difference equation describes a sequence of numbers recursively in terms of earlier terms in the sequence. For example, $a _ { 0 } , a _ { 1 } , \ldots$ is a Fibonacci sequence if

$$
a _ {i} = a _ {i - 1} + a _ {i - 2}
$$

for all $i \geq 2$ . There are infinitely many Fibonacci sequences, but such a sequence is uniquely determined after $a _ { 0 }$ and $a _ { 1 }$ are specified (these are called the initial conditions or boundary conditions). For example, $a_{0}=0,a_{1}=1$ yields the Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, . . . .

Difference equations often arise in probability, especially when applying LOTP. In this section, we will show how to solve difference equations of the form

$$
p _ {i} = p \cdot p _ {i + 1} + q \cdot p _ {i - 1},
$$

where $p \neq 0$ and $q = 1 - p .$ (This equation comes up in the gambler’s ruin problem.) The first step is to guess a solution of the form $p _ { i } = x ^ { i }$ . Plugging this into the above, we have

$$
x ^ {i} = p \cdot x ^ {i + 1} + q \cdot x ^ {i - 1},
$$

which reduces to $p x ^ { 2 } - x + q = 0$ . This is called the characteristic equation, and the solution to the difference equation depends on whether the characteristic equation has one or two distinct roots. If there are two distinct roots $r _ { 1 }$ and $r _ { 2 }$ , then the solution is of the form

$$
p _ {i} = a r _ {1} ^ {i} + b r _ {2} ^ {i},
$$

for some constants a and b. If there is only one distinct root $r ,$ then the solution is of the form

$$
p _ {i} = a r ^ {i} + b i r ^ {i}.
$$

---

Math

593

In our case, the characteristic equation has roots 1 and $q / p ,$ since

$$
\frac {1 \pm \sqrt {1 - 4 p (1 - p)}}{2 p} = \frac {1 \pm \sqrt {(2 p - 1) ^ {2}}}{2 p} = \frac {1 \pm | 2 p - 1 |}{2 p}
$$

is $( 1 + 2 p - 1 ) / ( 2 p ) = 1 { \mathrm { ~ o r ~ } } ( 2 - 2 p ) / ( 2 p ) = q / p .$ The roots are distinct if $p \neq q$ and are both equal to 1 if $p = q$ . So we have

$$
p _ {i} = \left\{ \begin{array}{l l} a + b \left(\frac {q}{p}\right) ^ {i}, & p \neq q, \\ a + b i, & p = q. \end{array} \right.
$$

This is called the general solution of the difference equation, since we have not yet specified the constants a and b. To get a specific solution, we need to know two points in the sequence in order to solve for $a$ and b.

## A.5 Differential equations

Differential equations are the continuous version of difference equations. A differential equation uses derivatives to describe a function or collection of functions. For example, the differential equation

$$
\frac {d y}{d x} = 3 y
$$

describes a collection of functions that have the following property: the instantaneous rate of change of the function at any point $( x , y )$ is equal to $3 y$ . This is an example of a separable differential equation because we can separate the $x ^ { \prime } \mathrm { s }$ and $y ^ { \flat } \mathrm { S } _ { 1 }$ , putting them on opposite sides of the equation:

$$
\frac {d y}{y} = 3 d x.
$$

Now we can integrate both sides, giving log $y = 3 x + c ,$ or equivalently,

$$
y = C e ^ {3 x},
$$

where $C$ is any constant. This is called the general solution of the differential equation, and it tells us that all functions satisfying the differential equation are of the form $y = C e ^ { 3 x }$ for some $C .$ To get a specific solution, we need to specify one point on the graph, which allows us to solve for $C .$

---

594

Introduction to Probability

## A.6 Partial derivatives

If you can do ordinary derivatives, you can do partial derivatives: just hold all the other input variables constant except for the one you’re differentiating with respect to. For example, let $f ( x , y ) = y \sin ( x ^ { 2 }   +   y ^ { 3 } )$ . Then the partial derivative with respect to x is

$$
\frac {\partial f (x , y)}{\partial x} = 2 x y \cos (x ^ {2} + y ^ {3}),
$$

and the partial derivative with respect to y is

$$
\frac {\partial f (x , y)}{\partial y} = \sin (x ^ {2} + y ^ {3}) + 3 y ^ {3} \cos (x ^ {2} + y ^ {3}).
$$

These are first order partial derivatives. If we take a partial derivative of a first order partial derivative, we get a second order partial derivative, such as

$$
\frac {\partial^ {2} f (x , y)}{\partial y \partial x} = \frac {\partial}{\partial y} \left(\frac {\partial f (x , y)}{\partial x}\right) = 2 x (\cos (x ^ {2} + y ^ {3}) - 3 y ^ {3} \sin (x ^ {2} + y ^ {3})).
$$

We get the same result if we take the partial derivatives in the opposite order (with respect to y and then with respect to x):

$$
\frac {\partial^ {2} f (x , y)}{\partial x \partial y} = \frac {\partial}{\partial x} \left(\frac {\partial f (x , y)}{\partial y}\right) = 2 x (\cos (x ^ {2} + y ^ {3}) - 3 y ^ {3} \sin (x ^ {2} + y ^ {3})).
$$

Under mild technical assumptions, it is also true for general f that

$$
\frac {\partial^ {2} f (x , y)}{\partial x \partial y} = \frac {\partial^ {2} f (x , y)}{\partial y \partial x}.
$$

The Jacobian of a transformation which maps $( x _ { 1 } , \ldots , x _ { n } )$ to $( y _ { 1 } , \ldots , y _ { n } )$ is the $n \times n$ matrix of all possible first order partial derivatives, given by

$$
\frac {\partial \mathbf {y}}{\partial \mathbf {x}} = \left( \begin{array}{c c c c} \frac {\partial y _ {1}}{\partial x _ {1}} & \frac {\partial y _ {1}}{\partial x _ {2}} & \dots & \frac {\partial y _ {1}}{\partial x _ {n}} \\ \vdots & \vdots & & \vdots \\ \frac {\partial y _ {n}}{\partial x _ {1}} & \frac {\partial y _ {n}}{\partial x _ {2}} & \dots & \frac {\partial y _ {n}}{\partial x _ {n}} \end{array} \right).
$$

## A.7 Multiple integrals

If you can do single integrals, you can do multiple integrals: just do more than one integral, holding variables other than the current variable of integration constant.

---

Math

595

For example,

$$
\begin{array}{l} \int_ {0} ^ {1} \int_ {0} ^ {y} (x - y) ^ {2} d x d y = \int_ {0} ^ {1} \int_ {0} ^ {y} (x ^ {2} - 2 x y + y ^ {2}) d x d y \\ = \int_ {0} ^ {1} \left(\left(x ^ {3} / 3 - x ^ {2} y + x y ^ {2}\right) \bigg | _ {0} ^ {y}\right) d y \\ = \int_ {0} ^ {1} (y ^ {3} / 3 - y ^ {3} + y ^ {3}) d y \\ = \frac {1}{1 2}. \\ \end{array}
$$

## A.7.1 Change of order of integration

We can also integrate in the other order, dydx rather than $d x d y ,$ as long as we are careful about the limits of integration. Since we’re integrating over all $( x , y )$ with x and y between 0 and 1 such that $x \leq y$ , to integrate the other way we write

$$
\begin{array}{l} \int_ {0} ^ {1} \int_ {x} ^ {1} (x - y) ^ {2} d y d x = \int_ {0} ^ {1} \int_ {x} ^ {1} (x ^ {2} - 2 x y + y ^ {2}) d y d x \\ = \int_ {0} ^ {1} \left(\left(x ^ {2} y - x y ^ {2} + y ^ {3} / 3\right) \Bigg | _ {x} ^ {1}\right) d x \\ = \int_ {0} ^ {1} (x ^ {2} - x + 1 / 3 - x ^ {3} + x ^ {3} - x ^ {3} / 3) d x \\ = \frac {1}{1 2}. \\ \end{array}
$$

## A.7.2 Change of variables

In making a change of variables with multiple integrals, a Jacobian is needed. To simplify notation, we will discuss the two-dimensional version; the n-dimensional version is analogous. Suppose we make an invertible transformation from $( x , y )$ to $( u , v )$ , where the inverse transformation is given by

$$
x = g (u, v), y = h (u, v).
$$

Let A be a region in the $(x,y)  -plane$ and B be the corresponding region in the $(u, v)  -plane$ . Then the change of variables formulas says that

$$
\iint_ {A} f (x, y) d x d y = \iint_ {B} f (g (u, v), h (u, v)) \cdot | \left| \frac {\partial (x , y)}{\partial (u , v)} \right| | d u d v,
$$

where $\mid \left[ \frac { \partial ( x ,   y ) } { \partial ( u ,   v ) } \right] \mid$ is the absolute value of the determinant of the Jacobian matrix. A few technical assumptions are needed for this result, such as that the partial

---

596

Introduction to Probability

derivatives that appear in the Jacobian matrix exist and are continuous, and that the determinant of the Jacobian matrix is never 0.

For example, let’s find the area of a circle of radius 1. To find the area of a region, we just need to integrate 1 over that region (so the part that may be tricky is the limits of integration; the integrand is just 1). So the area is

$$
\iint_ {x ^ {2} + y ^ {2} \leq 1} 1 d x d y = \int_ {- 1} ^ {1} \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} 1 d x d y = 2 \int_ {- 1} ^ {1} \sqrt {1 - y ^ {2}} d y.
$$

Note that the limits for the inner variable $( x )$ of the double integral can depend on the outer variable $( y )$ , while the outer limits are constants. The last integral can be done with a trigonometric substitution, but instead let’s simplify the problem by transforming to polar coordinates: let

$$
x = r \cos \theta , y = r \sin \theta ,
$$

where $r$ is the distance from $( x , y )$ to the origin and $\theta \in [ 0 , 2 \pi )$ is the angle. The Jacobian matrix of this transformation is

$$
\frac {\partial (x , y)}{\partial (r , \theta)} = \left( \begin{array}{c c} \cos \theta & - r \sin \theta \\ \sin \theta & r \cos \theta , \end{array} \right)
$$

so the absolute value of the determinant of the Jacobian is $r ( \cos ^ { 2 } \theta + \sin ^ { 2 } \theta ) = r$ That is, dxdy becomes rdrdθ. So the area of the circle is

$$
\int_ {0} ^ {2 \pi} \int_ {0} ^ {1} r d r d \theta = \int_ {0} ^ {2 \pi} \frac {1}{2} d \theta = \pi .
$$

For a circle of radius $r ,$ it follows immediately that the area is $\pi r ^ { 2 }$ since we can convert our units of measurement to the unit for which the radius is 1.

This may seem like a lot of work just to get such a familiar result, but it served as illustration and with similar methods we can get the volume of a ball in any number of dimensions! It turns out that the volume of a ball of radius 1 in $\mathbb { R } ^ { n }$ is

$$
V _ {n} = \frac {\pi^ {n / 2}}{\Gamma (n / 2 + 1)},
$$

where Γ is the gamma function (see Section A.2.7).

## A.8 Sums

There are several kinds of sums that come up frequently in probability.

---

Math

597

## A.8.1 Binomial theorem

The binomial theorem states that

$$
(x + y) ^ {n} = \sum_ {k = 0} ^ {n} \binom {n} {k} x ^ {k} y ^ {n - k},
$$

for any nonnegative integer n. Here $\left( \begin{matrix} { n } \\ { k } \\ \end{matrix} \right)$ is a binomial coefficient, defined as the number of ways to choose k objects out of $n ,$ with order not mattering. An explicit formula for $\left( \begin{matrix} { n } \\ { k } \\ \end{matrix} \right)$ in terms of factorials for $0 \leq k \leq n$ is

$$
\binom{n}{k} = \frac{n!}{(n - k)!k!}.
$$

A proof of the binomial theorem is given in Example 1.4.19.

Sometimes $0 ^ { 0 }$ is said to be undefined, but there are several strong arguments for defining it to be 1, and we will take $0 ^ { 0 } = 1$ in this book. For one simple reason for doing so, consider the case $x = 0,   y = 1$ in the binomial theorem. Then the left-hand side is $1 ^ { n } = 1$ , and we need to have $0 ^ { 0 } = 1$ in order to make the right-hand side also equal to 1.

## A.8.2 Geometric series

A series of the form $\textstyle \sum _ { n = 0 } ^ { \infty } x ^ { n }$ is called a geometric series. For $| x | < 1$ , the series converges and we have

$$
\sum_ {n = 0} ^ {\infty} x ^ {n} = \frac {1}{1 - x}.
$$

The series diverges if $| x | \geq 1$ . A series of the same form except with finitely many terms is called a finite geometric series. For $x \neq 1$ , the sum is

$$
\sum_ {k = 0} ^ {n} x ^ {k} = \frac {1 - x ^ {n + 1}}{1 - x}.
$$

Note that the $n + 1$ in the exponent is the number of terms in the sum. If the sum starts at $k = m$ rather than $k = 0$ (where m is an integer with $0 \leq m \leq n )$ , then we can easily reduce to the case where the sum starts at 0. Making the substitution $j = k - m$ , we have

$$
\sum_ {k = m} ^ {n} x ^ {k} = \sum_ {j = 0} ^ {n - m} x ^ {j + m} = x ^ {m} \sum_ {j = 0} ^ {n - m} x ^ {j} = x ^ {m} \cdot \frac {1 - x ^ {n - m + 1}}{1 - x}.
$$

---

598

Introduction to Probability

## A.8.3 Taylor series for $e ^ { x }$

The Taylor series for $e ^ { x }$ is

$$
\sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{n !} = e ^ {x}, \text {for all} x.
$$

## A.8.4 Harmonic series and other sums with a fixed exponent

It is also useful to know that $\textstyle \sum _ { n = 1 } ^ { \infty } 1 / n ^ { c }$ converges for $c > 1$ and diverges for $c \leq 1$ For $c = 1$ , this is called the harmonic series. The sum of the first n terms of the harmonic series can be approximated using

$$
\sum_ {k = 1} ^ {n} \frac {1}{k} \approx \log (n) + \gamma
$$

for n large, where $\gamma \approx 0 . 5 7 7$ is the Euler-Mascheroni constant.

The sum of the first n positive integers is

$$
\sum_ {k = 1} ^ {n} k = n (n + 1) / 2 = \binom{n + 1}{2}.
$$

It follows from this identity, for example, that the sum of the first n odd positive integers is

$$
\sum_ {k = 1} ^ {n} (2 k - 1) = 2 \sum_ {k = 1} ^ {n} k - \sum_ {k = 1} ^ {n} 1 = n (n + 1) - n = n ^ {2}.
$$

For squares of integers, we have

$$
\sum_ {k = 1} ^ {n} k ^ {2} = n (n + 1) (2 n + 1) / 6.
$$

For cubes of integers, amazingly, the sum is the square of the sum of the first n positive integers! That is,

$$
\sum_ {k = 1} ^ {n} k ^ {3} = (n (n + 1) / 2) ^ {2}.
$$

Exercise 22 from Chapter 1 asks for a story proof of this result.

---

Math

599

## A.9 Pattern recognition

Much of math and statistics is really about pattern recognition: seeing the essential structure of a problem, recognizing when one problem is essentially the same as another problem (just in a different guise), noticing symmetry, and so on. We will see many examples of this kind of thinking in this book. For example, suppose we have the series $\begin{array} { r } { \sum _ { k = 0 } ^ { \infty } e ^ { t k } e ^ { - \lambda } \lambda ^ { k } / k ! } \end{array}$ , with λ a positive constant. The $e ^ { - \lambda }$ <sub>can</sub> be taken out from the sum, and then the structure of the series exactly matches up with the structure of the Taylor series for $e ^ { x }$ . Therefore

$$
\sum_ {k = 0} ^ {\infty} \frac {e ^ {t k} e ^ {- \lambda} \lambda^ {k}}{k !} = e ^ {- \lambda} \sum_ {k = 0} ^ {\infty} \frac {(\lambda e ^ {t}) ^ {k}}{k !} = e ^ {- \lambda} e ^ {\lambda e ^ {t}} = e ^ {\lambda (e ^ {t} - 1)},
$$

valid for all real t.

Similarly, suppose we want the Taylor series for $1 / ( 1 - x ^ { 3 } )$ about $x = 0$ . It would be tedious to start taking derivatives of this function. Instead, note that this function is reminiscent of the result of summing a geometric series. Therefore

$$
\frac {1}{1 - x ^ {3}} = \sum_ {n = 0} ^ {\infty} x ^ {3 n},
$$

for $| x ^ { 3 } |   <   1$ (which is equivalent to $| x |   <   1 )$ . What matters is the structure, not what names we use for variables!

## A.10 Common sense and checking answers

It is very easy to make mistakes in probability, so checking answers is especially important. Some useful strategies for checking answers are:

• seeing whether the answer makes sense intuitively (though as we have often seen in this book, probability has many results that seem counterintuitive at first);
• making sure your answer isn’t a category error;
• making sure you’re avoiding biohazards;
• trying out simple cases;
• trying out extreme cases;
• looking for alternative methods to solve the problem (including methods that may only give a bound or approximation, such as applying one of the inequalities from Chapter 10 or using R to run a simulation).

---

![](../../raw/pages_0609-0624/images/page_616_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

---

R

## B.1 Vectors

| Command | What it does |
| --- | --- |
| c(1,1,0,2.7,3.1) | creates the vector (1,1,0,2.7,3.1) |
| 1:100 | creates the vector (1,2,...,100) |
| (1:100)^3 | creates the vector ($1^3$,$2^3$,...,$100^3$) |
| rep(0,50) | creates the vector (0,0,...,0) of length 50 |
| seq(0,99,3) | creates the vector (0,3,6,9,...,99) |
| v[5] | 5th entry of vector v (index starts at 1) |
| v[-5] | all but the 5th entry of v |
| v[c(3,1,4)] | 3rd, 1st, 4th entries of vector v |
| v[v>2] | entries of v that exceed 2 |
| which(v>2) | indices of v such that entry exceeds 2 |
| which(v==7) | indices of v such that entry equals 7 |
| min(v) | minimum of v |
| max(v) | maximum of v |
| which.max(v) | indices where max(v) is achieved |
| sum(v) | sum of the entries in v |
| cumsum(v) | cumulative sums of the entries in v |
| prod(v) | product of the entries in v |
| rank(v) | ranks of the entries in v |
| length(v) | length of vector v |
| sort(v) | sorts vector v (in increasing order) |
| unique(v) | lists each element of v once, without duplicates |
| tabulate(v) | tallies how many times each element of v occurs |
| table(v) | same as tabulate(v), except in table format |
| c(v,w) | concatenates vectors v and w |
| union(v,w) | union of v and w as sets |
| intersect(v,w) | intersection of v and w as sets |
| v+w | adds v and w entrywise (recycling if needed) |
| v*w | multiplies v and w entrywise (recycling if needed) |

601

---

602

Introduction to Probability

B.2 Matrices

| Command | What it does |
| --- | --- |
| matrix(c(1,3,5,7), nrow=2, ncol=2) | creates the matrix $\begin{pmatrix} 1 & 5 \\ 3 & 7 \end{pmatrix}$ |
| dim(A) | gives the dimensions of matrix A |
| diag(A) | extracts the diagonal of matrix A |
| diag(c(1,7)) | creates the diagonal matrix $\begin{pmatrix} 1 & 0 \\ 0 & 7 \end{pmatrix}$ |
| rbind(u,v,w) | binds vectors u,v,w into a matrix, as rows |
| cbind(u,v,w) | binds vectors u,v,w into a matrix, as columns |
| t(A) | transpose of matrix A |
| A[2,3] | row 2, column 3 entry of matrix A |
| A[2,] | row 2 of matrix A (as a vector) |
| A[,3] | column 3 of matrix A (as a vector) |
| A[c(1,3),c(2,4)] | submatrix of A, keeping rows 1,3 and columns 2,4 |
| rowSums(A) | row sums of matrix A |
| rowMeans(A) | row averages of matrix A |
| colSums(A) | column averages of matrix A |
| colMeans(A) | column means of matrix A |
| eigen(A) | eigenvalues and eigenvectors of matrix A |
| solve(A) | $A^{-1}$ |
| solve(A,b) | solves Ax = b for x (where b is a column vector) |
| A %*% B | matrix multiplication AB |
| A %~% k | matrix power $A^{k}$ (using expm package) |

B.3 Math

| Command | What it does |
| --- | --- |
| abs(x) | $\|x\|$ |
| exp(x) | $e^{x}$ |
| log(x) | $\log(n)$ |
| log(x,b) | $\log_{b}(n)$ |
| sqrt(x) | $\sqrt{x}$ |
| floor(x) | $\lfloor x \rfloor$ |
| ceiling(x) | $\lceil x \rceil$ |
| factorial(n) | $n!$ |
| lfactorial(n) | $\log(n!)$ (helps prevent overflow) |
| gamma(a) | $\Gamma(a)$ |
| lgamma(a) | $\log(\Gamma(a))$ (helps prevent overflow) |
| choose(n,k) | binomial coefficient $\binom{n}{k}$ |
| pbirthday(k) | solves birthday problem for k people |
| if (x>0) x^2 else x^3 | $x^{2}$ if $x > 0$, $x^{3}$ otherwise (piecewise) |
| f &lt;- function(x) exp(-x) | defines the function f by $f(x) = e^{-x}$ |
| integrate(f, lower=0, upper=Inf) | finds $\int_{0}^{\infty} f(x) dx$ numerically |
| optimize(f,lower=0,upper=5,maximum=TRUE) | maximizes f numerically on [0,5] |
| uniroot(f, lower=0, upper=5) | searches numerically for a zero of f in [0,5] |

---

R

603

## B.4 Sampling and simulation

| Command | What it does |
| --- | --- |
| sample(7) | random permutation of 1,2,...,7 |
| sample(52,5) | picks 5 times from 1,2,...,52 (don’t replace) |
| sample(letters,5) | picks 5 random letters of the alphabet (don’t replace) |
| sample(3,5,replace=TRUE,prob=p) | picks 5 times from 1,2,3 with probabilities p (replace) |
| replicate(10^4,experiment) | simulates 10^4 runs of experiment |

## B.5 Plotting

| Command | What it does |
| --- | --- |
| curve(f, from=a, to=b) | graphs the function f from a to b |
| plot(x,y) | creates scatter plot of the points (xi,yi) |
| plot(x,y,type="l") | creates line plot of the points (xi,yi) |
| points(x,y) | adds the points (xi,yi) to the plot |
| lines(x,y) | adds line segments through the (xi,yi) to the plot |
| abline(a,b) | adds the line with intercept a, slope b to the plot |
| hist(x, breaks=b, col="blue") | blue histogram of the values in x, with b bins suggested |
| par(new=TRUE) | tells R not to clear the palette when we make our next plot |
| par(mfrow=c(1,2)) | tells R we want 2 side-by-side plots (a 1 by 2 array of plots) |

## B.6 Programming

| Command | What it does |
| --- | --- |
| x &lt;- pi | sets x equal to π |
| x>3 &amp;&amp; x&lt;5 | Is x > 3 and x &lt; 5? (TRUE/FALSE) |
| x>3 \|\| x&lt;5 | Is x > 3 or x &lt; 5? (TRUE/FALSE) |
| if (n>3) x &lt;- x+1 | adds 1 to x if n > 3 |
| if (n==0) x &lt;- x+1 else x &lt;- x+2 | adds 1 to x if n = 0, else adds 2 |
| v&lt;-rep(0,50); for (k in 1:50) v[k]&lt;-pbirthday(k) | solves birthday problem up to 50 people |

---

604

Introduction to Probability

## B.7 Summary statistics

| Command | What it does |
| --- | --- |
| mean(v) | sample mean of vector v |
| var(v) | sample variance of vector v |
| sd(v) | sample standard deviation of vector v |
| median(v) | sample median of vector v |
| summary(v) | min, 1st quartile, median, mean, 3rd quartile, max of v |
| quantile(v,p) | pth sample quantile of vector v |
| cov(v,w) | sample covariance of vectors v and w |
| cor(v,w) | sample correlation of vectors v and w |

## B.8 Distributions

| Command | What it does |
| --- | --- |
| help(distributions) | shows documentation on distributions |
| dbinom(k,n,p) | PMF $P(X = k)$ for $X \sim \text{Bin}(n, p)$ |
| pbinom(x,n,p) | CDF $P(X \leq x)$ for $X \sim \text{Bin}(n, p)$ |
| qbinom(a,n,p) | quantile $\min\{x : P(X \leq x) \geq a\}$ for $X \sim \text{Bin}(n, p)$ |
| rbinom(r,n,p) | vector of r i.i.d. Bin(n,p) r.v.s |
| dgeom(k,p) | PMF $P(X = k)$ for $X \sim \text{Geom}(p)$ |
| dhyper(k,w,b,n) | PMF $P(X = k)$ for $X \sim \text{HGeom}(w, b, n)$ |
| dnbinom(k,r,p) | PMF $P(X = k)$ for $X \sim \text{NBin}(r, p)$ |
| dpois(k,r) | PMF $P(X = k)$ for $X \sim \text{Pois}(r)$ |
| dbeta(x,a,b) | PDF $f(x)$ for $X \sim \text{Beta}(a, b)$ |
| dcauchy(x) | PDF $f(x)$ for $X \sim \text{Cauchy}$ |
| dchisq(x,n) | PDF $f(x)$ for $X \sim \chi_{n}^{2}$ |
| dexp(x,r) | PDF $f(x)$ for $X \sim \text{Expo}(r)$ |
| dgamma(x,a,r) | PDF $f(x)$ for $X \sim \text{Gamma}(a, r)$ |
| dlnorm(x,m,s) | PDF $f(x)$ for $X \sim \mathcal{LN}(m, s^{2})$ |
| dnorm(x,m,s) | PDF $f(x)$ for $X \sim \mathcal{N}(m, s^{2})$ |
| dt(x,n) | PDF $f(x)$ for $X \sim t_{n}$ |
| dunif(x,a,b) | PDF $f(x)$ for $X \sim \text{Unif}(a, b)$ |
| dweibull(x,a,b) | PDF $f(x)$ for $X \sim \text{Weibull}(b^{-a}, a)$ |

There are commands that are completely analogous to pbinom, qbinom, and rbinom for the other distributions appearing in the above table. For example, pnorm, qnorm, and rnorm can be used to get the CDF, the quantiles, and random generation for the Normal (note that the mean and standard deviation need to be provided as the parameters, rather than the mean and variance).

For the Multinomial, dmultinom can be used for calculating the joint PMF and rmultinom can be used for generating random vectors. For the Multivariate Normal, after installing and loading the mvtnorm package, dmvnorm can be used for calculating the joint PDF and rmvnorm can be used for random generation.

---

Table of distributions

| Name | Param. | PMF or PDF | Mean | Variance |
| --- | --- | --- | --- | --- |
| Bernoulli | $p$ | $P(X = 1) = p, P(X = 0) = q$ | $p$ | $pq$ |
| Binomial | $n, p$ | $\binom{n}{k} p^{k} q^{n-k}, k \in \{0, 1, \dots, n\}$ | $np$ | $npq$ |
| FS | $p$ | $pq^{k-1}, k \in \{1, 2, \dots\}$ | $1/p$ | $q/p^{2}$ |
| Geom | $p$ | $pq^{k}, k \in \{0, 1, 2, \dots\}$ | $q/p$ | $q/p^{2}$ |
| NBin | $r, p$ | $\binom{r+k-1}{r-1} p^{r} q^{k}, k \in \{0, 1, 2, \dots\}$ | $rq/p$ | $rq/p^{2}$ |
| HGeom | $w, b, n$ | $\frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}, k \in \{0, 1, \dots, n\}$ | $\mu = \frac{nw}{w+b}$ | $(\frac{w+b-n}{w+b-1}) \mu (1 - \frac{\mu}{n})$ |
| NHGeom | $w, b, r$ | $\frac{\binom{r+k-1}{r-1}\binom{w+b-r-k}{w-r}}{\binom{w+b}{w}}, k \in \{0, 1, \dots, b\}$ | $\frac{rb}{w+1}$ | $\frac{rb(w+b+1)(w-r+1)}{(w+1)^{2}(w+2)}$ |
| Poisson | $\lambda$ | $\frac{e^{-\lambda} \lambda^{k}}{k!}, k \in \{0, 1, 2, \dots\}$ | $\lambda$ | $\lambda$ |
| Uniform | $a < b$ | $\frac{1}{b-a}, x \in (a, b)$ | $\frac{a+b}{2}$ | $\frac{(b-a)^{2}}{12}$ |
| Normal | $\mu, \sigma^{2}$ | $\frac{1}{\sigma \sqrt{2\pi}} e^{-(x-\mu)^{2}/(2\sigma^{2})}$ | $\mu$ | $\sigma^{2}$ |
| Log-Normal | $\mu, \sigma^{2}$ | $\frac{1}{x\sigma\sqrt{2\pi}} e^{-(\log x-\mu)^{2}/(2\sigma^{2})}, x > 0$ | $\theta = e^{\mu+\sigma^{2}/2}$ | $\theta^{2}(e^{\sigma^{2}} - 1)$ |
| Expo | $\lambda$ | $\lambda e^{-\lambda x}, x > 0$ | $1/\lambda$ | $1/\lambda^{2}$ |
| Weibull | $\lambda, \gamma$ | $\gamma \lambda e^{-\lambda x^{\gamma}} x^{\gamma-1}, x > 0$ | $\mu = \frac{\Gamma(1+1/\gamma)}{\lambda^{1/\gamma}}$ | $\frac{\Gamma(1+2/\gamma)}{\lambda^{2/\gamma}} - \mu^{2}$ |
| Gamma | $a, \lambda$ | $\Gamma(a)^{-1}(\lambda x)^{a} e^{-\lambda x} x^{-1}, x > 0$ | $a/\lambda$ | $a/\lambda^{2}$ |
| Beta | $a, b$ | $\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)} x^{a-1}(1 - x)^{b-1}, 0 < x < 1$ | $\mu = \frac{a}{a+b}$ | $\frac{\mu(1-\mu)}{a+b+1}$ |
| Chi-Square | $n$ | $\frac{1}{2^{n/2}\Gamma(n/2)} x^{n/2-1} e^{-x/2}, x > 0$ | $n$ | $2n$ |
| Student-$t$ | $n$ | $\frac{\Gamma((n+1)/2)}{\sqrt{n\pi}\Gamma(n/2)} (1 + x^{2}/n)^{-(n+1)/2}$ | $0$ if $n > 1$ | $\frac{n}{n-2}$ if $n > 2$ |

605

---

![](../../raw/pages_0609-0624/images/page_622_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

---

## References

[1] Donald J. Albers and Gerald L. Alexanderson. More Mathematical People: Contemporary Conversations. Academic Press, 1990.
[2] Steve Brooks, Andrew Gelman, Galin Jones, and Xiao-Li Meng. Handbook of Markov Chain Monte Carlo. CRC Press, 2011.
[3] Jian Chen and Jeffrey S. Rosenthal. Decrypting classical cipher text using Markov chain Monte Carlo. Statistics and Computing, 22(2):397–413, 2012.
[4] William G. Cochran. The effectiveness of adjustment by subclassification in removing bias in observational studies. Biometrics, 1968.
[5] Persi Diaconis. Statistical problems in ESP research. Science, 201(4351):131–136, 1978.
[6] Persi Diaconis. The Markov chain Monte Carlo revolution. Bulletin of the American Mathematical Society, 46(2):179–205, 2009.
[7] Persi Diaconis, Susan Holmes, and Richard Montgomery. Dynamical bias in the coin toss. SIAM Review, 49(2):211–235, 2007.
[8] Bradley Efron and Ronald Thisted. Estimating the number of unseen species: How many words did Shakespeare know? Biometrika, 63(3):435, 1976.
[9] Bradley Efron and Ronald Thisted. Did Shakespeare write a newly-discovered poem? Biometrika, 74:445–455, 1987.
[10] Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari, and Donald B. Rubin. Bayesian Data Analysis. CRC Press, 2013.
[11] Andrew Gelman and Deborah Nolan. You can load a die, but you can’t bias a coin. The American Statistician, 56(4):308–311, 2002.
[12] Andrew Gelman, Boris Shor, Joseph Bafumi, and David K. Park. Red State, Blue State, Rich State, Poor State: Why Americans Vote the Way They Do (Expanded Edition). Princeton University Press, 2009.
[13] Gerd Gigerenzer and Ulrich Hoffrage. How to improve Bayesian reasoning without instruction: Frequency formats. Psychological Review, 102(4):684, 1995.
[14] Prakash Gorroochurn. Classic Problems of Probability. John Wiley & Sons, 2012.

607

---

608

References

[15] Richard Hamming. You and your research. IEEE Potentials, pages 37–40, October 1993.
[16] David P. Harrington. The randomized clinical trial. Journal of the American Statistical Association, 95(449):312–315, 2000.
[17] David J.C. MacKay. Information Theory, Inference, and Learning Algorithms. Cambridge University Press, 2003.
[18] Richard McElreath. Statistical Rethinking: A Bayesian Course with Examples in R and Stan. Chapman & Hall/CRC Press, 2015.
[19] Pierre Rémond de Montmort. Essay d’Analyse sur les Jeux de Hazard. Quilau, Paris, 1708.
[20] John Allen Paulos. Innumeracy: Mathematical Illiteracy and Its Consequences. Macmillan, 1988.
[21] Horst Rinne. The Weibull Distribution: A Handbook. CRC Press, 2008.
[22] James G. Sanderson. Testing ecological patterns. American Scientist, 88:332–339, 2000.
[23] Tom W. Smith, Peter Marsden, Michael Hout, and Jibum Kim. General social surveys, 1972–2012. Sponsored by National Science Foundation. NORC, Chicago: National Opinion Research Center, 2013.
[24] Stephen M. Stigler. Isaac Newton as a probabilist. Statistical Science, 21(3):400–403, 2006.
[25] Tom Stoppard. Rosencrantz & Guildenstern Are Dead. Samuel French, Inc., 1967.
[26] R.J. Stroeker. On the sum of consecutive cubes being a perfect square. Compositio Mathematica, 97:295–307, 1995.
[27] Amos Tversky and Daniel Kahneman. Causal schemas in judgments under uncertainty. In Daniel Kahneman, Paul Slovic, and Amos Tversky, editors, Judgment under Uncertainty: Heuristics and Biases. Cambridge University Press, 1982.
[28] Herbert S. Wilf. generatingfunctionology. A K Peters/CRC Press, 3rd edition, 2005.
[29] Elizabeth Wrigley-Field. Length-biased sampling. Online article at [https://www.edge.org/response-detail/27022](https://www.edge.org), 2017.
[30] Lisa Zyga. Why too much evidence can be a bad thing. Online article at [https://phys.org/news/2016-01-evidence-bad.html](https://phys.org), 2016.
