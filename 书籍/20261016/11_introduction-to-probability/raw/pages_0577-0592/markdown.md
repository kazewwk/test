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

![](images/page_577_chart_2.jpg)

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

![](images/page_578_image_2.jpg)

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

There is a very natural way to generate a superposition.

Story 13.2.7 (Generative story for superposition). To generate the superposition of two independent Poisson processes, $( N _ { 1 } ( t ) : t > 0 )$ with rate $\lambda _ { 1 }$ and $( N _ { 2 } ( t ) : t > 0 )$ with rate $\lambda _ { 2 }$ :

1. Generate arrivals from the Poisson process $( N _ { 1 } ( t ) : t > 0 )$
2. Generate arrivals from the Poisson process $( N _ { 2 } ( t ) : t > 0 )$
3. Superpose the results of steps 1 and 2.

![](images/page_581_chart_8.jpg)

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

For example, if the average lifetime of his refrigerator is 15 years and the average lifetime of his dishwasher is $7$ years, and then one of these appliances fails after $7$ years, it would be natural to guess that it was the dishwasher that failed. But in fact, we will show that knowing the time of the first appliance failure provides no information about which appliance failed.

Solution: We will use an embedding strategy, using Poisson process ideas even though this problem doesn’t mention Poisson processes anywhere! We will embed the r.v.s $Y _ { 1 }$ and $Y _ { 2 }$ into a Poisson process that we ourselves invent, in order to take advantage of the properties of Poisson processes. So let’s imagine there is an entire Poisson process of refrigerator failures with rate $\lambda _ { 1 }$ and a Poisson process of dishwasher failures with rate $\lambda _ { 2 }$

We can interpret $Y _ { 1 }$ as the waiting time for the first arrival in the refrigerator process and $Y _ { 2 }$ as the waiting time for the first arrival in the dishwasher process. This approach is valid since (min $( Y _ { 1 } , Y _ { 2 } ) , I ( Y _ { 1 } { < } Y _ { 2 } ) )$ is a function of $( Y _ { 1 } , Y _ { 2 } )$ , so what matters is the joint distribution of $( Y _ { 1 } , Y _ { 2 } )$ , and the way we construct $( Y _ { 1 } , Y _ { 2 } )$ does have the correct joint distribution.

Furthermore, min $( Y _ { 1 } , Y _ { 2 } )$ is the waiting time for the first arrival in the superposition of the two Poisson processes, and $I ( Y _ { 1 } < Y _ { 2 } )$ is the indicator of this arrival being a type-1 event. But in the above generative story, the arrival times and event types in the superposed Poisson process are generated completely independently! Hence, min $( Y _ { 1 } , Y _ { 2 } )$ and $I ( Y _ { 1 } < Y _ { 2 } )$ are independent, with min $( Y _ { 1 } , Y _ { 2 } ) \sim \operatorname { E x p o } ( \lambda _ { 1 } + \lambda _ { 2 } )$ and $I ( Y _ { 1 } < Y _ { 2 } ) \sim \operatorname { B e r n } ( \lambda _ { 1 } / ( \lambda _ { 1 } + \lambda _ { 2 } ) )$ 

A direct consequence of Story 13.2.9 is that if we project a superposed Poisson process into discrete time, keeping the sequence of type-1 and type-2 arrivals but not the arrival times themselves, we are left with i.i.d. Bern $( \lambda _ { 1 } / ( \lambda _ { 1 } { + } \lambda _ { 2 } ) )$ r.v.s $I _ { 1 } , I _ { 2 } , \ldots ,$ where $I _ { j }$ is the indicator of the jth arrival being type-1. Figure 13.4 illustrates what it means to remove the continuous-time information from the Poisson process, and Theorem 13.2.11 states the result formally.

![](images/page_583_image_7.jpg)

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

Proof. Let $\lambda _ { \mathrm { 1 } }   =   \lambda p$ and $\lambda _ { 2 }   =   \lambda ( 1   -   p )$ , so $\lambda   =   \lambda _ { \mathrm { 1 } }   +   \lambda _ { \mathrm { 2 } }$ and $p   =   \lambda _ { 1 } / ( \lambda _ { 1 }   +   \lambda _ { 2 } )$ Then we find ourselves in Story 13.2.9. But Story 13.2.7 and Story 13.2.9 are two equivalent generative stories for superposition! The probabilistic structures of the outputs of the two stories are identical, thinking of the arrivals in Story 13.2.7 from $( N _ { i } ( t ) : t > 0 )$ as being type-i. So we can assume instead that Story 13.2.7 was used to generate the process. Happily, in this story we know from the beginning that the type-1 process is independent of the type-2 process. 

Thus we can superpose independent Poisson processes to get a combined Poisson process, or we can split a single Poisson process into independent Poisson processes. Figure 13.5 is an illustration of thinning. We simply flipped Figure 13.3 upside-down, which is appropriate because thinning is the flip side of superposition!

![](images/page_585_chart_4.jpg)

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

Proof. We will induct on c. For $c = 1$ there is nothing to show. For $c = 2$ the result is the thinning theorem that we already proved. Now assume that the result holds for c colors, and show it when there are $c + 1$ colors. Let’s call color 1 green. Use thinning to assign each arrival to be green with probability $p _ { 1 }$ and non-green with probability $1 - p _ { 1 }$ . This splits the Poisson process into 2 independent processes: a green process of rate $\lambda p _ { 1 }$ and a non-green process of rate $\lambda ( 1   -   p _ { 1 } )$ . By the inductive hypothesis, we can then split the non-green process into c independent processes, one for each of colors $2 , 3 , \ldots , c + 1$ , where color $j$ now gets probability

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

![](images/page_588_chart_2.jpg)

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

![](images/page_590_image_2.jpg)

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