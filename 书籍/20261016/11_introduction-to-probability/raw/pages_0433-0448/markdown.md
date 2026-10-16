Similarly, if $Y$ is continuous, $E ( Y )$ is still a weighted average of the possible values of $Y$ , with an integral in place of a sum and the PDF value $f ( y )$ in place of a PMF value. If we learn that $A$ occurred, we update the expectation for $Y$ by replacing $f ( y )$ with the conditional PDF $f ( y | A )$

Definition 9.1.1 (Conditional expectation given an event). Let $A$ be an event with positive probability. If $Y$ is a discrete r.v., then the conditional expectation of $Y$ given A is

$$
E (Y | A) = \sum_ {y} y P (Y = y | A),
$$

where the sum is over the support of Y . If $Y$ is a continuous r.v. with PDF $f ,$ then

$$
E (Y | A) = \int_ {- \infty} ^ {\infty} y f (y | A) d y,
$$

where the conditional PDF $f ( y | A )$ is defined as the derivative of the conditional CDF $F ( y | A )   =   P ( Y   \leq   y | A )$ , and can also be computed by a hybrid version of Bayes’ rule:

$$
f (y | A) = \frac {P (A | Y = y) f (y)}{P (A)}.
$$

Intuition 9.1.2. To gain intuition for $E ( Y | A )$ , let’s consider approximating it via simulation (or via the frequentist perspective, based on repeating the same experiment many times). Imagine generating a large number n of replications of the experiment for which $Y$ is a numerical summary. We then have Y -values $y _ { 1 } , \ldots , y _ { n }$ and we can approximate

$$
E (Y) \approx \frac {1}{n} \sum_ {j = 1} ^ {n} y _ {j}.
$$

To approximate $E ( Y | A )$ , we restrict to the replications where A occurred, and average only those Y -values. This can be written as

$$
E (Y | A) \approx \frac {\sum_ {j = 1} ^ {n} y _ {j} I _ {j}}{\sum_ {j = 1} ^ {n} I _ {j}},
$$

where $I _ { j }$ is the indicator of A occurring in the jth replication. This is undefined if A never occurred in the simulation, which makes sense since then there is no simulation data about what the $^ { \circ } A$ occurred” scenario is like. We would like to have n large enough so that there are many occurrences of $A$ (if A is a rare event, more sophisticated techniques for approximating $E ( Y | A )$ may be needed).

The principle is simple though: $E ( Y | A )$ is approximately the average of $Y$ in a large number of simulation runs in which A occurred. 

h 9.1.3. Confusing conditional expectation and unconditional expectation is a dangerous mistake. More generally, not keeping careful track of what you should be conditioning on and what you are conditioning on is a recipe for disaster.

For a life-or-death example of the previous biohazard, consider life expectancy.

Example 9.1.4 (Life expectancy). Fred is 30 years old, and he hears that the average life expectancy in his country is 80 years. Should he conclude that, on average, he has 50 years of life left? No, there is a crucial piece of information that he must condition on: the fact that he has lived to age 30 already. Letting T be Fred’s lifespan, we have the cheerful news that

$$
E (T) <   E (T | T \geq 3 0).
$$

The left-hand side is Fred’s life expectancy at birth (it implicitly conditions on the fact that he is born), and the right-hand side is Fred’s life expectancy given that he reaches age 30.

A harder question is how to decide on an appropriate estimate to use for $E ( T )$ . Is it just 80, the overall average for his country? In almost every country, women have a longer average life expectancy than men, so it makes sense to condition on Fred being a man. But should we also condition on what city he was born in? Should we condition on racial and financial information about his parents, or the time of day when he was born? Intuitively, we would like estimates that are both accurate and relevant for Fred, but there is a tradeoff since if we condition on more characteristics of Fred, then there are fewer people who match those characteristics to use as data for estimating the life expectancy.

Now consider some specific numbers for the United States. A Social Security Administration study estimated that between 1900 and 2000, the average life expectancy at birth in the U.S. for men increased from 46 to 74, and for women increased from 49 to 79. Tremendous gains! But much of the gain is due to decreases in child mortality. For a 30-year-old person in 1900, the average number of years remaining was 35 for a man and 36 for a woman; in 2000, the corresponding numbers were 46 for a man and 50 for a woman.

There are some subtle statistical issues in obtaining these estimates. For example, how were estimates for life expectancy for someone born in 2000 obtained without waiting at least until the year 2100? Estimating survival distributions is a very important topic in biostatistics and actuarial science. 

The law of total probability allows us to get unconditional probabilities by slicing up the sample space and computing conditional probabilities in each slice. The same idea works for computing unconditional expectations.

Theorem 9.1.5 (Law of total expectation). Let $A _ { 1 } , \ldots , A _ { n }$ be a partition of a sample space, with $P ( A _ { i } )   >   0$ for all i, and let Y be a random variable on this sample space. Then

$$
E (Y) = \sum_ {i = 1} ^ {n} E (Y | A _ {i}) P (A _ {i}).
$$

In fact, since all probabilities are expectations by the fundamental bridge, the law of total probability is a special case of the law of total expectation. To see this, let $Y = I _ { B }$ for an event $B ;$ then the above theorem says

$$
P (B) = E (I _ {B}) = \sum_ {i = 1} ^ {n} E (I _ {B} | A _ {i}) P (A _ {i}) = \sum_ {i = 1} ^ {n} P (B | A _ {i}) P (A _ {i}),
$$

which is exactly LOTP. The law of total expectation is, in turn, a special case of a major result called Adam’s law (Theorem 9.3.7), so we will not prove it yet.

There are many interesting examples of using wishful thinking to break up an unconditional expectation into conditional expectations. We begin with two cautionary tales about the importance of conditioning carefully and not destroying information without justification.

Example 9.1.6 (Two-envelope paradox). A stranger presents you with two identical-looking, sealed envelopes, each of which contains a check for some positive amount of money. You are informed that one of the envelopes contains exactly twice as much money as the other. You can choose either envelope. Which do you prefer: the one on the left or the one on the right? (Assume that the expected amount of money in each envelope is finite—certainly a good assumption in the real world!)

![](images/page_434_image_7.jpg)

## FIGURE 9.1

Two envelopes, where one contains twice as much money as the other. Either $Y =$ 2X or $Y = X / 2$ , with equal probabilities. Which would you prefer?

## Solution:

Let X and Y be the amounts in the left and right envelopes, respectively. By symmetry, there is no reason to prefer one envelope over the other (we are assuming there is no prior information that the stranger is left-handed and left-handed people prefer putting more money on the left). Concluding by symmetry that $E(X)   =$ $E ( Y )$ , it seems that you should not care which envelope you get.

But as you daydream about what’s inside the envelopes, another argument occurs to you: suppose that the left envelope has \$100. Then the right envelope either has \$50 or \$200. The average of \$50 and \$200 is \$125, so it seems then that the right envelope is better. But there was nothing special about \$100 here; for any value x for the left envelope, the average of 2x and $x / 2$ is greater than $x ,$ suggesting that the right envelope is better. This is bizarre though, since not only does it contradict the symmetry argument, but also the same reasoning could be applied starting with the right envelope, leading to switching back and forth forever!

Let us try to formalize this argument to see what’s going on. We have $Y = 2 X$ or $Y = X / 2 ,$ , with equal probabilities. By Theorem 9.1.5,

$$
E (Y) = E (Y | Y = 2 X) \cdot \frac {1}{2} + E \bigl (Y | Y = X / 2 \bigr) \cdot \frac {1}{2}.
$$

One might then think that this is

$$
E (2 X) \cdot \frac {1}{2} + E (X / 2) \cdot \frac {1}{2} = \frac {5}{4} E (X),
$$

suggesting a 25% gain from switching from the left to the right envelope. But there is a blunder in that calculation: $E ( Y | Y = 2 X ) = E ( 2 X | Y = 2 X )$ , but there is no justification for dropping the $Y = 2 X$ condition after plugging in 2X for $Y .$

To put it another way, let I be the indicator of the event $Y = 2 X$ , so that $E ( Y | Y =$ $2 X ) = E ( 2 X | I = 1 )$ . If we know that X is independent of I, then we can drop the condition $I = 1$ . But in fact we have just proven that X and I can’t be independent: if they were, we’d have a paradox! Surprisingly, observing X gives information about whether X is the bigger value or the smaller value. If we learn that X is very large, we might guess that X is larger than $Y$ , but what is considered very large? Is $1 0 ^ { 1 2 }$ very large, even though it is tiny compared with $1 0 ^ { 1 0 0 } ?$ The two-envelope paradox says that no matter what the distribution of X is, there are reasonable ways to define “very large” relative to that distribution.

In Exercise 8 you will look at a related problem, in which the amounts of money in the two envelopes are i.i.d. random variables. You’ll show that if you are allowed to look inside one of the envelopes and then decide whether to switch, there is a strategy that allows you to get the better envelope more than 50% of the time! 

The next example vividly illustrates the importance of conditioning on all the information. The phenomenon revealed here arises in many real-life decisions about what to buy and what investments to make.

Example 9.1.7 (Mystery prize). You are approached by another stranger, who gives you an opportunity to bid on a mystery box containing a mystery prize! The value of the prize is completely unknown, except that it is worth at least nothing, and at most a million dollars. So the true value $V$ of the prize is considered to be Uniform on [0,1] (measured in millions of dollars).

You can choose to bid any amount b (in millions of dollars). You have the chance to get the prize for considerably less than it is worth, but you could also lose money if you bid too much. Specifically, if $b < 2 V / 3$ , then the bid is rejected and nothing is gained or lost. If $b \geq 2 V / 3$ , then the bid is accepted and your net payoff is $V - b$ (since you pay b to get a prize worth V ). What is your optimal bid $b ,$ to maximize the expected payoff?

## Solution:

Your bid $b   \geq   0$ must be a predetermined constant (not based on $V ,$ since $V$ is

![](images/page_436_image_2.jpg)

<details>
<summary>text_image</summary>

Bid $250,000? If it's rejected, I lose nothing. If it's accepted, I get a prize worth $500,000 on average!
mystery box
</details>

## FIGURE 9.2

When bidding on an unknown asset, beware the winner’s curse, and condition on the relevant information.

unknown!). To find the expected payoff W, condition on whether the bid is accepted. The payoff is $V - b$ if the bid is accepted and 0 if the bid is rejected. So

$$
\begin{array}{l} E (W) = E (W | b \geq 2 V / 3) P (b \geq 2 V / 3) + E (W | b <   2 V / 3) P (b <   2 V / 3) \\ = E (V - b | b \geq 2 V / 3) P (b \geq 2 V / 3) + 0 \\ = (E (V | V \leq 3 b / 2) - b) P (V \leq 3 b / 2). \\ \end{array}
$$

For $b \geq 2 / 3 ,$ , the event $V \leq 3 b / 2$ has probability 1, so the right-hand side is $1 / 2 - b ,$ which is negative. Now assume $b < 2 / 3$ . Then $V \leq 3 b / 2$ has probability $3 b / 2$ . Given that $V \leq 3 b / 2$ , the conditional distribution of V is Uniform on $[ 0 , 3 b / 2 ]$ . Therefore,

$$
E (W) = \left(E (V | V \leq 3 b / 2) - b\right) P (V \leq 3 b / 2) = (3 b / 4 - b) (3 b / 2) = - 3 b ^ {2} / 8.
$$

The above expression is negative except at $b   =   0 .$ so the optimal bid is 0: you shouldn’t play this game!

Alternatively, condition on which of the following events occurs: $A = \{ V < b / 2 \}$ $B = \{ b / 2 \leq V \leq 3 b / 2 \} ,   C = \{ V > 3 b / 2 \}$ . We have

$$
E (W | A) = E (V - b | A) <   E (b / 2 - b | A) = - b / 2 \leq 0,
$$

$$
E (W | B) = E \left(\frac {b / 2 + 3 b / 2}{2} - b | B\right) = 0,
$$

$$
E (W | C) = 0,
$$

so we should just set $b = 0$ and walk away.

The moral of this story is to condition on all the information. It is crucial in the above calculation to use $E ( V | V \leq 3 b / 2 )$ rather than $E ( V ) = 1 / 2 ;$ knowing that the bid was accepted gives information about how much the mystery prize is worth, so we shouldn’t destroy that information. This problem is related to the so-called win-$n e r   ^ { \prime } s$ curse, which says that the winner in an auction with incomplete information tends to profit less than they expect (unless they understand probability!). This is because in many settings, the expected value of the item that they bid on given that they won the bid is less than the unconditional expected value they originally had in mind. For $b \geq 2 / 3$ , conditioning on $V \leq 3 b / 2$ does nothing since we know in advance that $V \leq 1$ , but such a bid is ludicrously high. For any $b < 2 / 3$ , finding out that your bid is accepted lowers your expectation:

$$
E (V | V \leq 3 b / 2) <   E (V).
$$

The remaining examples use first-step analysis to calculate unconditional expectations. First, as promised in Chapter 4, we derive the expectation of the Geometric distribution using first-step analysis.

Example 9.1.8 (Geometric expectation redux). Let $X \sim \operatorname { G e o m } ( p )$ . Interpret X as the number of Tails before the first Heads in a sequence of coin flips with probability $p$ of Heads. To get $E ( X )$ , we condition on the outcome of the first toss: if it lands Heads, then X is 0 and we’re done; if it lands Tails, then we’ve wasted one toss and are back to where we started, by memorylessness. Therefore,

$$
\begin{array}{l} E (X) = E (X | \text {first toss} H) \cdot p + E (X | \text {first toss} T) \cdot q \\ = 0 \cdot p + (1 + E (X)) \cdot q, \\ \end{array}
$$

which gives $E ( X ) = q / p .$

The next example derives expected waiting times for some more complicated patterns, using two steps of conditioning.

Example 9.1.9 (Time until HH vs. HT). You toss a fair coin repeatedly. What is the expected number of tosses until the pattern HT appears for the first time? What about the expected number of tosses until HH appears for the first time?

## Solution:

Let $W _ { H T }$ be the number of tosses until HT appears. As we can see from Figure $9 . 3 , ~ W _ { H T }$ is the waiting time for the first Heads, which we’ll call $W _ { 1 }$ , plus the additional waiting time for the first Tails after the first Heads, which we’ll call $W _ { 2 }$ By the story of the First Success distribution, $W _ { 1 }$ and $W _ { 2 }$ are i.i.d. $\mathrm { F S } ( 1 / 2 )$ , so $E ( W _ { 1 } ) = E ( W _ { 2 } ) = 2 { \mathrm { ~ a n d ~ } } E ( W _ { H T } ) = 4$

Finding the expected waiting time for HH, $E ( W _ { H H } )$ , is more complicated. We can’t apply the same logic as for $E ( W _ { H T } )$ : as shown in Figure 9.4, if the first Heads is immediately followed by Tails, our progress is destroyed and we must start from scratch. But this is progress for us in solving the problem, since the fact that the

![](images/page_438_image_2.jpg)

<details>
<summary>text_image</summary>

TTTHHHHTHHT...
W₁ W₂
</details>

## FIGURE 9.3

Waiting time for HT is the waiting time for the first Heads, $W _ { 1 }$ , plus the additional waiting time for the next Tails, $W _ { 2 }$ . Durable partial progress is possible!

system can get reset suggests the strategy of first-step analysis. Let’s condition on the outcome of the first toss:

$$
E (W _ {H H}) = E (W _ {H H} | \text {first toss} H) \frac {1}{2} + E (W _ {H H} | \text {first toss} T) \frac {1}{2}.
$$

![](images/page_438_image_7.jpg)

<details>
<summary>text_image</summary>

THTTTTHHHH...
↑
start over
</details>

## FIGURE 9.4

When waiting for HH, partial progress can easily be destroyed.

For the second term, $E ( W _ { H H } |$ first toss $\mathrm { T ) } = 1 + E ( W _ { H H } )$ by memorylessness. For the first term, we compute $E ( W _ { H H } |$ 1st toss H) by further conditioning on the outcome of the second toss. If the second toss is Heads, we have obtained HH in two tosses. If the second toss is Tails, $\mathrm { w e } ^ { \mathfrak { z } } \mathrm { v e }$ wasted two tosses and have to start all over! This gives

$$
E (W _ {H H} | \text {first toss} H) = 2 \cdot \frac {1}{2} + (2 + E (W _ {H H})) \cdot \frac {1}{2}.
$$

Therefore,

$$
E (W _ {H H}) = \left(2 \cdot \frac {1}{2} + (2 + E (W _ {H H})) \cdot \frac {1}{2}\right) \frac {1}{2} + (1 + E (W _ {H H})) \frac {1}{2}.
$$

Solving for $E ( W _ { H H } )$ , we get $E ( W _ { H H } ) = 6$

It might seem surprising at first that the expected waiting time for HH is greater than the expected waiting time for HT. How do we reconcile this with the fact that in two tosses of the coin, HH and HT both have a $1 / 4$ chance of appearing? Why aren’t the average waiting times the same by symmetry?

As we solved this problem, we in fact noticed an important asymmetry. When waiting for HT, once we get the first Heads, we’ve achieved partial progress that cannot be destroyed: if the Heads is followed by another Heads, we’re in the same position as before, and if the Heads is followed by a Tails, we’re done. By contrast, when waiting for HH, even after getting the first Heads, we could be sent back to square one if the Heads is followed by a Tails. This suggests the average waiting time for HH should be longer. Symmetry implies that the average waiting time for HH is the same as that for TT, and that for HT is the same as that for TH, but it does not imply that the average waiting times for HH and HT are the same.

More intuition into what’s going on can be obtained by considering a long string of coin flips, as in Figure 9.5. We notice right away that appearances of HH can overlap, while appearances of HT must be disjoint. For example, HHHHHH has 5 occurrences of HH, but HTHTHT has only 3 occurrences of HT. Since there are the same average number of HH s and HTs, but HH s sometimes clump together, the average waiting time for HH must be larger than that of HT to compensate.

![](images/page_439_image_4.jpg)

<details>
<summary>chemical</summary>

Sequence of HHTHHTTHHHHHTHTHTTHTT with overlapping circles, likely representing a DNA or protein sequence
</details>

## FIGURE 9.5

Clumping. (a) Appearances of HH can overlap. (b) Appearances of HT must be disjoint.

Related problems occur in information theory when compressing a message, and in genetics when looking for recurring patterns (called motifs) in DNA sequences. 

Our final example in this section uses wishful thinking for both probabilities and expectations to study a question about a random walk.

Example 9.1.10 (Random walk on the integers). An immortal drunk man wanders around randomly on the integers. He starts at the origin, and at each step he moves 1 unit to the right or 1 unit to the left, with equal probabilities, independently of all his previous steps. Let b be a googolplex (this is 10<sup>g</sup>, where $g = 1 0 ^ { 1 0 0 }$ is a googol).

(a) Find a simple expression for the probability that the immortal drunk visits b before returning to the origin for the first time.
(b) Find the expected number of times that the immortal drunk visits b before returning to the origin for the first time.

## Solution:

(a) Let B be the event that the drunk man visits b before returning to the origin for the first time and let L be the event that his first move is to the left. Then

$P ( B | L ) = 0$ since any path from −1 to b must pass through 0. For $P ( B | L ^ { c } )$ , we are exactly in the setting of the gambler’s ruin problem, where player A starts with \$1, player B starts with $\S ( b - 1 )$ , and the rounds are fair. Applying that result, we have

$$
P (B) = P (B | L) P (L) + P (B | L ^ {c}) P (L ^ {c}) = \frac {1}{b} \cdot \frac {1}{2} = \frac {1}{2 b}.
$$

(b) Let N be the number of visits to b before returning to the origin for the first time, and let $p = 1 / ( 2 b )$ be the probability found in (a). Then

$$
E (N) = E (N | N = 0) P (N = 0) + E (N | N \geq 1) P (N \geq 1) = p E (N | N \geq 1).
$$

The conditional distribution of N given $N \geq 1$ is $\operatorname { F S } ( p )$ : given that the man reaches b, by symmetry there is probability p of returning to the origin before visiting b again (call this “success”) and probability $1 - p$ of returning to b again before returning to the origin (call this “failure”). Note that the trials are independent since the situation is the same each time he is at $b ,$ independent of the past history. Thus $E ( N | N \geq 1 ) = 1 / p ,$ and

$$
E (N) = p E (N | N \geq 1) = p \cdot \frac {1}{p} = 1.
$$

Surprisingly, the result doesn’t depend on the value of $b ,$ and our proof didn’t require knowing the value of $p .$ 

## 9.2 Conditional expectation given an r.v.

In this section we introduce conditional expectation given a random variable. That is, we want to understand what it means to write $E ( Y | X )$ for an r.v. X. We will see that $E ( Y | X )$ is a random variable that is, in a certain sense, our best prediction of $Y$ , assuming we get to know X.

The key to understanding $E ( Y | X )$ is first to understand $E ( Y | X = x )$ . Since $X = x$ is an event, $E ( Y | X = x )$ is just the conditional expectation of Y given this event, and it can be computed using the conditional distribution of $Y$ given $X = x$

If $Y$ is discrete, we use the conditional PMF $P ( Y   =   y | X   =   x )$ in place of the unconditional PMF $P ( Y = y )$

$$
E (Y | X = x) = \sum_ {y} y P (Y = y | X = x).
$$

Analogously, if Y is continuous, we use the conditional PDF $f _ { Y | X } ( y | x )$ in place of the unconditional PDF:

$$
E (Y | X = x) = \int_ {- \infty} ^ {\infty} y f _ {Y | X} (y | x) d y.
$$

Notice that because we sum or integrate over y, $E ( Y | X   =   x )$ is a function of x only. We can give this function a name, like $g ;$ let $g ( x ) = E ( Y | X = x )$ . We define $E ( Y | X )$ as the random variable obtained by finding the form of the function $g ( x )$ then $p l u g g i n g$ in $X \; f o r \; x$

Definition 9.2.1 (Conditional expectation given an $\mathrm { r . v . ) }$ . Let $g ( x ) = E ( Y | X = x )$ Then the conditional expectation of Y given $X$ , denoted $E ( Y | X )$ , is defined to be the random variable $g ( X )$ . In other words, if after doing the experiment X crystallizes into x, then $E ( Y | X )$ crystallizes into $g ( x )$

h 9.2.2. The notation in this definition sometimes causes confusion. It does not say $^ { \backprime \backprime } g ( x )   =   E ( Y | X   =   x )$ , so $g ( X )   =   E ( Y | X   =   X )$ , which equals $E ( Y )$ because $X = X$ is always true”. Rather, we should first compute the function $g ( x )$ , then plug in X for x. For example, if $g ( x ) = x ^ { 2 }$ , then $g ( X ) = X ^ { 2 }$ . A similar biohazard is h 5.3.2, about the meaning of $F ( X )$ in the universality of the Uniform.

h 9.2.3. By definition, $E ( Y | X )$ is a function of X, so it is a random variable. (This does not mean there are no examples where $E ( Y | X )$ is a constant. A constant is a degenerate $\mathbf { r } . \mathbf { V } .$ , and a constant function of X. For example, if X and Y are independent then $E ( Y | X ) \; = \; E ( Y )$ , which is a constant.) Thus it makes sense to compute quantities like $E ( E ( Y | X ) )$ and $\operatorname { V a r } ( E ( Y | X ) )$ , the mean and variance of the $r.v.   E(Y|X)$ . It is easy to be ensnared by category errors when working with conditional expectation, so it is important to keep in mind that conditional expectations of the form $E ( Y | A )$ are numbers, while those of the form $E ( Y | X )$ are random variables.

Here are some quick examples of how to calculate conditional expectation. In both examples, we don’t need to do a sum or integral to get $E ( Y | X = x )$ because a more direct approach is available.

Example 9.2.4. A stick of length 1 is broken at a point X chosen uniformly at random. Given that $X = x$ , we then choose another breakpoint $Y$ uniformly on the interval $[ 0 , x ]$ . Find $E ( Y | X )$ , and its mean and variance.

Solution:

From the description of the experiment, $X \sim \mathrm { U n i f } ( 0 , 1 )$ and $Y | X = x \sim \operatorname { U n i f } ( 0 , x )$ Then $E ( Y | X = x ) = x / 2$ , so by plugging in X for x, we have

$$
E (Y | X) = X / 2.
$$

The expected value of $E ( Y | X )$ is

$$
E (E (Y | X)) = E (X / 2) = 1 / 4.
$$

(We will show in the next section that a general property of conditional expectation is that $E ( E ( Y | X ) ) = E ( Y )$ , so it also follows that $E ( Y ) = 1 / 4 . )$ The variance of $E ( Y | X )$ is

$$
\mathrm{Var} (E (Y | X)) = \mathrm{Var} (X / 2) = 1 / 4 8.
$$



Example 9.2.5. For $X , Y \stackrel { \mathrm { i . i . d . } } { \sim } \mathrm { E x p o } ( \lambda )$ , find $E ( \operatorname* { m a x } ( X , Y ) | \operatorname* { m i n } ( X , Y ) )$

Solution:

Let $M = \operatorname* { m a x } ( X , Y )$ and $L = \operatorname* { m i n } ( X , Y )$ . By the memoryless property, $M - L$ is independent of $L ,$ and $M - L \sim \mathrm{Exp}(\lambda)$ (see Example 7.3.6). Therefore

$$
E (M | L = l) = E (L | L = l) + E (M - L | L = l) = l + E (M - L) = l + \frac {1}{\lambda},
$$

and $\begin{array} { r } { E ( M | L ) = L + \frac { 1 } { \lambda } } \end{array}$

## 9.3 Properties of conditional expectation

Conditional expectation has some very useful properties.

• Dropping what’s independent: If X and $Y$ are independent, then $E ( Y | X ) = E ( Y )$
• Taking out what’s known: For any function h, $E ( h ( X ) Y | X ) = h ( X ) E ( Y | X )$
• Linearity: $E ( Y _ { 1 } + Y _ { 2 } | X ) = E ( Y _ { 1 } | X ) + E ( Y _ { 2 } | X )$ , and $E ( c Y | X ) = c E ( Y | X )$ for c a constant (the latter is a special case of taking out what’s known).

• Adam’s law: $E ( E ( Y | X ) ) = E ( Y )$

• Projection interpretation: The $r.v.   Y - E(Y|X)$ , which is called the residual from using $X$ to predict $Y .$ , is uncorrelated with $h ( X )$ for any function $h .$

Let’s discuss each property individually.

Theorem 9.3.1 (Dropping what’s independent). If X and $Y$ are independent, then $E ( Y | X ) = E ( Y )$

This is true because independence implies $E ( Y | X   =   x )   =   E ( Y )$ for all $x ,$ hence $E(Y|X)=E(Y)$ . Intuitively, if X provides no information about $Y$ , then our best guess for $Y$ , even if we get to know $X$ , is still the unconditional mean $E ( Y )$ . However, the converse is false: a counterexample is given in Example 9.3.3 below.

Theorem 9.3.2 (Taking out what’s known). For any function $h .$

$$
E (h (X) Y | X) = h (X) E (Y | X).
$$

Intuitively, when we take expectations given $X$ , we are treating $X$ as if it has crystallized into a known constant. Then any function of $X$ , say $h ( X )$ , also acts like a known constant while we are conditioning on $X$ . Taking out what’s known is the conditional version of the unconditional fact that $E ( c Y ) = c E ( Y )$ . The difference is that $E ( c Y ) = c E ( Y )$ asserts that two numbers are equal, while taking out what’s known asserts that two random variables are equal.

Example 9.3.3. Let $Z \sim \mathcal { N } ( 0 , 1 )$ and $Y = Z ^ { 2 }$ . Find $E ( Y | Z )$ and $E ( Z | Y )$

Solution: Since Y is a function of $Z ,   E ( Y | Z ) = E ( Z ^ { 2 } | Z ) = Z ^ { 2 }$ by taking out what’s known. To get $E ( Z | Y )$ , notice that conditional on $Y = y ,   Z$ equals ${ \sqrt { y } } { \mathrm { ~ o r ~ } } { - { \sqrt { y } } }$ with equal probabilities by the symmetry of the standard Normal, so $\dot { E } ( Z | Y = y ) = 0$ and $E ( Z | Y ) = 0$

In this case, although Y provides a lot of information about $Z ,$ narrowing down the possible values of $Z \mathrm { ~ t o ~ }$ just two values, Y only tells us about the magnitude of $Z$ and not its sign. For this reason, $E ( Z | Y ) = E ( Z )$ despite the dependence between $Z$ and $Y$ . This example illustrates that the converse of Theorem 9.3.1 is false. 

Theorem 9.3.4 (Linearity). $E ( Y _ { 1 } + Y _ { 2 } | X ) = E ( Y _ { 1 } | X ) + E ( Y _ { 2 } | X )$

This result is the conditional version of the unconditional fact that $E(Y_{1} + Y_{2}) =$ $E ( Y _ { 1 } ) + E ( Y _ { 2 } )$ , and is true since conditional probabilities are probabilities.

h 9.3.5. It is incorrect to write $`` E ( Y | X _ { 1 } + X _ { 2 } ) = E ( Y | X _ { 1 } ) + E ( Y | X _ { 2 } )$ ; linearity applies on the left side of the conditioning bar, not on the right side!

Example 9.3.6. Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d., and $S _ { n } = X _ { 1 }   + \cdots + X _ { n }$ . Find $E ( X _ { 1 } | S _ { n } )$

Solution:

By symmetry,

$$
E (X _ {1} | S _ {n}) = E (X _ {2} | S _ {n}) = \dots = E (X _ {n} | S _ {n}),
$$

and by linearity,

$$
E (X _ {1} | S _ {n}) + \dots + E (X _ {n} | S _ {n}) = E (S _ {n} | S _ {n}) = S _ {n}.
$$

Therefore,

$$
E (X _ {1} | S _ {n}) = S _ {n} / n = \bar {X} _ {n},
$$

the sample mean of the $X _ { j } { } ^ { \prime } \mathrm { s } .$ This is an intuitive result: if we have 2 i.i.d. r.v.s $X _ { 1 } , X _ { 2 }$ and learn that $X _ { 1 } + X _ { 2 } = 1 0$ , it makes sense to guess that $X _ { 1 }$ is 5 (accounting for half of the total). Similarly, if we have n i.i.d. r.v.s and get to know their sum, our best guess for any one of them is the sample mean. 

The next theorem connects conditional expectation to unconditional expectation. It goes by many names, including the law of total expectation, the law of iterated expectation (which has a terrible acronym for something glowing with truth), and the tower property. We call it Adam’s law because it is used so frequently that it deserves a pithy name, and since it is often used in conjunction with another law we’ll encounter soon, which has a complementary name.

Theorem 9.3.7 (Adam’s law). For any r.v.s X and $Y .$

$$
E (E (Y | X)) = E (Y).
$$

Proof. We present the proof in the case where X and $Y$ are both discrete (the proofs for other cases are analogous). Let $E ( Y | X ) = g ( X )$ . We proceed by applying

LOTUS, expanding the definition of $g ( x )$ to get a double sum, and then swapping the order of summation:

$$
\begin{array}{l} E (g (X)) = \sum_ {x} g (x) P (X = x) \\ = \sum_ {x} \left(\sum_ {y} y P (Y = y | X = x)\right) P (X = x) \\ = \sum_ {x} \sum_ {y} y P (X = x) P (Y = y | X = x) \\ = \sum_ {y} y \sum_ {x} P (X = x, Y = y) \\ = \sum_ {y} y P (Y = y) = E (Y). \\ \end{array}
$$

Adam’s law is a more compact, more general version of the law of total expectation (Theorem 9.1.5). For X discrete, the statements

$$
E (Y) = \sum_ {x} E (Y | X = x) P (X = x)
$$

and

$$
E (Y) = E (E (Y | X))
$$

mean the same thing, since if we let $E ( Y | X = x ) = g ( x )$ , then

$$
E (E (Y | X)) = E (g (X)) = \sum_ {x} g (x) P (X = x) = \sum_ {x} E (Y | X = x) P (X = x).
$$

Armed with Adam’s law, we have a powerful strategy for finding an expectation $E ( Y )$ , by conditioning on an r.v. X that we wish we knew. First obtain $E ( Y | X )$ by treating X as known, and then take the expectation of $E ( Y | X )$ . We will see various examples of this later in the chapter.

Just as there are forms of Bayes’ rule and LOTP with extra conditioning, as discussed in Chapter 2, there is a version of Adam’s law with extra conditioning.

Theorem 9.3.8 (Adam’s law with extra conditioning). For any r.v.s $X , Y , Z ,$

$$
E (E (Y | X, Z) | Z) = E (Y | Z).
$$

The above equation is Adam’s law, except with extra conditioning on $Z$ inserted everywhere. It is true because conditional probabilities are probabilities. So we are free to use Adam’s law to help us find both unconditional expectations and conditional expectations.

Using Adam’s law, we can also prove the last item on our list of properties of conditional expectation.

Theorem 9.3.9 (Projection interpretation). For any function $h ,$ the random variable $Y - E ( Y | X )$ is uncorrelated with $h ( X )$ . Equivalently,

$$
E ((Y - E (Y | X)) h (X)) = 0.
$$

(This is equivalent since $E ( Y - E ( Y | X ) ) = 0$ , by linearity and Adam’s law.)

Proof. We have

$$
\begin{array}{l} E ((Y - E (Y | X)) h (X)) = E (h (X) Y) - E (h (X) E (Y | X)) \\ = E (h (X) Y) - E (E (h (X) Y | X)) \\ \end{array}
$$

by Theorem 9.3.2 (here we’re “putting back what’s known” in the inner expectation). By Adam’s law, the second term is equal to $E ( h ( X ) Y )$ 

![](images/page_445_image_8.jpg)

<details>
<summary>text_image</summary>

Y
}Y - E(Y | X)
E(Y | X)
</details>

## FIGURE 9.6

The conditional expectation $E ( Y | X )$ is the projection of $Y$ onto the space of all functions of $X$ , shown here as a plane. The residual $Y - E ( Y | X )$ is orthogonal to the plane: it’s perpendicular to (uncorrelated with) any function of $X$

From a geometric perspective, we can visualize Theorem 9.3.9 as in Figure 9.6. In a certain sense (described below), $E ( Y | X )$ is the function of $X$ that is closest to $Y ;$ we say that $E ( Y | X )$ is the projection of $Y$ into the space of all functions of $X$ The “line” from $Y$ to $E ( Y | X )$ in the figure is orthogonal (perpendicular) to the $``  plane$ since any other route from $Y$ to $E ( Y | X )$ would be longer. This orthogonality turns out to be the geometric interpretation of Theorem 9.3.9.

The details of this perspective are given in the next section, which is starred since it requires knowledge of linear algebra. But even without delving into the linear algebra, the projection picture gives some useful intuition. As mentioned earlier, we can think of $E ( Y | X )$ as a prediction for Y based on $X$ . This is an extremely common problem in statistics: predict or estimate the future observations or unknown parameters based on data. The projection interpretation of conditional expectation implies that $E ( Y | X )$ is the best predictor of $Y$ based on $X$ , in the sense that it is the function of X with the lowest mean squared error (expected squared difference between $Y$ and the prediction of $Y )$

Example 9.3.10 (Linear regression). An extremely widely used method for data analysis in statistics is linear regression. In its most basic form, the linear regression model uses a single explanatory variable X to predict a response variable $Y .$ and it assumes that the conditional expectation of $Y$ is linear in $X$

$$
E (Y | X) = a + b X.
$$

(a) Show that an equivalent way to express this is to write

$$
Y = a + b X + \epsilon ,
$$

where  is an r.v. (called the error ) with $E ( \epsilon | X ) = 0$

(b) Solve for the constants a and b in terms of $E(X),E(Y),\mathrm{Cov}(X,Y)$ , and $\operatorname { V a r } ( X )$

Solution:

(a) Let $Y = a + b X + \epsilon$ , with $E ( \epsilon | X ) = 0$ . Then by linearity,

$$
E (Y | X) = E (a | X) + E (b X | X) + E (\epsilon | X) = a + b X.
$$

Conversely, suppose that $E ( Y | X ) = a + b X$ , and define

$$
\epsilon = Y - (a + b X).
$$

Then $Y = a + b X + \epsilon$ , with

$$
E (\epsilon | X) = E (Y | X) - E (a + b X | X) = E (Y | X) - (a + b X) = 0.
$$

(b) First, by Adam’s law, taking the expectation of both sides gives

$$
E (Y) = a + b E (X).
$$

Note that  has mean 0 and X and  are uncorrelated, since

$$
E (\epsilon) = E (E (\epsilon | X)) = E (0) = 0
$$

and

$$
E (\epsilon X) = E (E (\epsilon X | X)) = E (X E (\epsilon | X)) = E (0) = 0.
$$

Taking the covariance with X of both sides in $Y = a + b X + \epsilon ,$ we have

$$
\operatorname{Cov} (X, Y) = \operatorname{Cov} (X, a) + b \operatorname{Cov} (X, X) + \operatorname{Cov} (X, \epsilon) = b \operatorname{Var} (X).
$$

Thus,

$$
b = \frac {\operatorname{Cov} (X , Y)}{\operatorname{Var} (X)},
$$

$$
a = E (Y) - b   E (X) = E (Y) - \frac {\operatorname{Cov} (X , Y)}{\operatorname{Var} (X)} \cdot E (X).
$$



## 9.4 \*Geometric interpretation of conditional expectation

This section explains in more detail the geometric perspective shown in Figure 9.6, using some concepts from linear algebra. Consider the vector space consisting of all random variables on a certain probability space, such that the random variables all have finite variance. Each vector or point in the space is a random variable (here we are using “vector” in the linear algebra sense, not in the sense of a random vector from Chapter $7 )$ . Define the inner product of two r.v.s U and $V$ to be

$$
\langle U, V \rangle = E (U V).
$$

(For this definition to satisfy the axioms for an inner product, we need the convention that two r.v.s are considered the same if they are equal with probability 1.)

The squared length of an r.v. X is

$$
| | X | | ^ {2} = \langle X, X \rangle = E X ^ {2},
$$

and the squared distance between two r.v.s $U$ and $V$ is

$$
| | U - V | | ^ {2} = E (U - V) ^ {2}.
$$

The interpretations become especially nice if $E ( U ) = E ( V ) = 0$ , since then:

$| | U | | ^ { 2 } = \operatorname { V a r } ( U )$ , and $| | U | | = \operatorname { S D } ( U )$
$\langle U , V \rangle = \mathrm { C o v } ( U , V )$ , and the cosine of the “angle” between U and V is $\operatorname { C o r r } ( U , V )$
• $U$ and V are orthogonal $( \mathrm { i . e . , } ~ \langle U , V \rangle = 0 )$ if and only if they are uncorrelated.

To interpret $E ( Y | X )$ geometrically, consider the space of all random variables (with finite variance) that can be expressed as functions of $X$ . This is a subspace of the vector space. In Figure $9 . 6 ,$ the subspace of random variables of the form $h ( X )$ is represented by a plane. To get $E ( Y | X )$ , we project $Y$ onto the plane. Then the residual $Y - E ( Y | X )$ is orthogonal to $h ( X )$ for all functions $h ,$ and $E ( Y | X )$ is the function of X that best predicts $Y .$ where $`` \mathrm{best''}$ here means that the mean squared error $E ( Y - g ( X ) ) ^ { 2 }$ is minimized by choosing $g ( X ) = E ( Y | X )$

The projection interpretation is a helpful way to think about many of the properties of conditional expectation. For example, if $Y = h ( X )$ is a function of $X$ , then $Y$ itself is already in the plane, so it is its own projection; this explains why

$$
E (h (X) | X) = h (X).
$$

We can think of unconditional expectation as a projection too: $E ( Y )$ can be thought of as $E ( Y | 0 )$ , the projection of $Y$ onto the space of all constants (and indeed, $E ( Y )$ is the constant c that minimizes $E ( Y - c ) ^ { 2 }$ , as we proved in Theorem 6.1.4).