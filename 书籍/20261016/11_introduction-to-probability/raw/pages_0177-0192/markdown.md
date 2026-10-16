Finally, if we multiply both sides by $p q$ , we recover the original sum we wanted to find:

$$
E (X) = \sum_ {k = 0} ^ {\infty} k q ^ {k} p = p q \sum_ {k = 0} ^ {\infty} k q ^ {k - 1} = p q \frac {1}{(1 - q) ^ {2}} = \frac {q}{p}.
$$

In Example 9.1.8, we will give a story proof of the same result, based on first-step analysis: condition on the result of the first trial in the story interpretation of X. If the first trial is a success, we know $X = 0$ and if it’s a failure, we have one wasted trial and then are back where we started. 

Example 4.3.7 (First Success expectation). Since we can write $Y   \sim   \mathrm { F S } ( p )$ as $Y = X + 1$ where $X \sim \operatorname { G e o m } ( p )$ , we have

$$
E (Y) = E (X + 1) = \frac {q}{p} + 1 = \frac {1}{p}.
$$

The Negative Binomial distribution generalizes the Geometric distribution: instead of waiting for just one success, we can wait for any predetermined number r of successes.

Story 4.3.8 (Negative Binomial distribution). In a sequence of independent Bernoulli trials with success probability p, if X is the number of failures before the rth success, then X is said to have the Negative Binomial distribution with parameters r and p, denoted $X \sim \mathrm { N B i n } ( r , p )$ 

Both the Binomial and the Negative Binomial distributions are based on independent Bernoulli trials; they differ in the stopping rule and in what they are counting. The Binomial counts the number of successes in a fixed number of trials; the Negative Binomial counts the number of failures until a fixed number of successes.

In light of these similarities, it comes as no surprise that the derivation of the Negative Binomial PMF bears a resemblance to the corresponding derivation for the Binomial.

Theorem 4.3.9 (Negative Binomial PMF). If $X \sim \mathrm { N B i n } ( r , p )$ , then the PMF of X is

$$
P (X = n) = \binom{n + r - 1}{r - 1} p ^ {r} q ^ {n}
$$

for $n = 0 , 1 , 2 \ldots$ , where $q = 1 - p$

Proof. Imagine a string of 0’s and 1’s, with 1’s representing successes. The probability of any specific string of n 0’s and r 1’s is $p ^ { r } q ^ { n }$ . How many such strings are there? Because we stop as soon as we hit the rth success, the string must terminate in a 1. Among the other $n   +   r   -   1$ positions, we choose $r - 1$ places for the remaining 1’s to go. So the overall probability of exactly n failures before the rth success is

$$
P (X = n) = \binom {n + r - 1} {r - 1} p ^ {r} q ^ {n}, \quad n = 0, 1, 2, \dots .
$$

Just as a Binomial r.v. can be represented as a sum of i.i.d. Bernoullis, a Negative Binomial r.v. can be represented as a sum of i.i.d. Geometrics.

Theorem 4.3.10. Let $X \sim \mathrm { N B i n } ( r , p )$ , viewed as the number of failures before the rth success in a sequence of independent Bernoulli trials with success probability $p .$ Then we can write $X = X _ { 1 } + \cdots + X _ { r }$ where the $X _ { i }$ are i.i.d. Geom(p).

Proof. Let $X _ { 1 }$ be the number of failures until the first success, $X _ { 2 }$ be the number of failures between the first success and the second success, and in general, $X _ { i }$ be the number of failures between the $( i - 1 )$ st success and the ith success.

Then $X _ { 1 }   \sim   \mathrm { G e o m } ( p )$ by the story of the Geometric distribution. After the first success, the number of additional failures until the next success is still Geometric! So $X _ { 2 } \sim \operatorname { G e o m } ( p )$ , and similarly for all the $X _ { i }$ . Furthermore, the $X _ { i }$ are independent because the trials are all independent of each other. Adding the $X _ { i }$ , we get the total number of failures before the rth success, which is X. 

Using linearity, the expectation of the Negative Binomial now follows without any additional calculations.

Example 4.3.11 (Negative Binomial expectation). Let $X   \sim   \mathrm { N B i n } ( r , p )$ . By the previous theorem, we can write $X = X _ { 1 }   + \cdots + X _ { r }$ , where the $X _ { i }$ are i.i.d. Geom(p). By linearity,

$$
E (X) = E (X _ {1}) + \dots + E (X _ {r}) = r \cdot \frac {q}{p}.
$$

The next example is a famous problem in probability and an instructive application of the Geometric and First Success distributions. It is usually stated as a problem about collecting coupons, hence its name, but we’ll use toys instead of coupons.

Example 4.3.12 (Coupon collector). Suppose there are n types of toys, which you are collecting one by one, with the goal of getting a complete set. When collecting toys, the toy types are random (as is sometimes the case, for example, with toys included in cereal boxes or included with kids’ meals from a fast food restaurant). Assume that each time you collect a toy, it is equally likely to be any of the n types. What is the expected number of toys needed until you have a complete set?

## Solution:

Let N be the number of toys needed; we want to find $E ( N )$ . Our strategy will be to break up N into a sum of simpler r.v.s so that we can apply linearity. So write

$$
N = N _ {1} + N _ {2} + \dots + N _ {n},
$$

where $N _ { 1 }$ is the number of toys until the first toy type you haven’t seen before (which is always 1, as the first toy is always a new type), $N _ { 2 }$ is the additional number of toys until the second toy type you haven’t seen before, and so forth. Figure 4.6 illustrates these definitions with $n = 3$ toy types.

![](images/page_178_image_2.jpg)

<details>
<summary>text_image</summary>

N₁
↑
N₂
N₃
</details>

## FIGURE 4.6

Coupon collector, $n = 3$ . Here $N _ { 1 }$ is the time (number of toys collected) until the first new toy type, $N _ { 2 }$ is the additional time until the second new type, and $N _ { 3 }$ is the additional time until the third new type. The total number of toys for a complete set is $N _ { 1 } + N _ { 2 } + N _ { 3 }$

By the story of the FS distribution, $N _ { 2 } \sim \mathrm { F S } ( ( n   -   1 ) / n )$ : after collecting the first toy type, there’s a $1 / n$ chance of getting the same toy you already had (failure) and an $( n - 1 ) / n$ chance you’ll get something new (success). Similarly, $N _ { 3 }$ , the additional number of toys until the third new toy type, is distributed $\operatorname { F S } ( ( n   -   2 ) / n )$ . In general,

$$
N _ {j} \sim \mathrm{FS} ((n - j + 1) / n).
$$

By linearity,

$$
\begin{array}{l} E (N) = E (N _ {1}) + E (N _ {2}) + E (N _ {3}) + \dots + E (N _ {n}) \\ = 1 + \frac {n}{n - 1} + \frac {n}{n - 2} + \dots + n \\ = n \sum_ {j = 1} ^ {n} \frac {1}{j}. \\ \end{array}
$$

For large n, this is very close to $n ( \log n + 0 . 5 7 7 )$

Before we leave this example, let’s take a moment to connect it to our proof of Theorem 4.3.10, the representation of the Negative Binomial as a sum of i.i.d. Geometrics. In both problems, we are waiting for a specified number of successes, and we approach the problem by considering the intervals between successes. There are two major differences:

• In Theorem 4.3.10, we exclude the successes themselves, so the number of failures between two successes is Geometric. In the coupon collector problem, we include the successes because we want to count the total number of toys, so we have First Success r.v.s instead.
• In Theorem 4.3.10, the probability of success in each trial never changes, so the total number of failures is a sum of i.i.d. Geometrics. In the coupon collector problem, the probability of success decreases after each success, since it becomes harder and harder to find a new toy type you haven’t seen before; so the $N _ { j }$ are not identically distributed, though they are independent. 

h 4.3.13 (Expectation of a nonlinear function of an r.v.). Expectation is linear, but in general we do not have $E ( g ( X ) )   =   g ( E ( X ) )$ for arbitrary functions $g .$ We must be careful not to move the E around when g is not linear. The next example shows a situation in which $E ( g ( X ) )$ is very different from $g ( E ( X ) )$ .

Example 4.3.14 (St. Petersburg paradox). Suppose a wealthy stranger offers to play the following game with you. You will flip a fair coin until it lands Heads for the first time, and you will receive \$2 if the game lasts for 1 round, \$4 if the game lasts for 2 rounds, \$8 if the game lasts for 3 rounds, and in general, $\mathbb { S } 2 ^ { n }$ if the game lasts for n rounds. What is the fair value of this game (the expected payoff)? How much would you be willing to pay to play this game once?

## Solution:

Let X be your winnings from playing the game. By definition, $X = 2 ^ { N }$ where N is the number of rounds that the game lasts. Then X is 2 with probability $1 / 2 ,$ 4 with probability $1 / 4 ,$ , 8 with probability $1 / 8 ,$ , and so on, so

$$
E (X) = \frac {1}{2} \cdot 2 + \frac {1}{4} \cdot 4 + \frac {1}{8} \cdot 8 + \dots = \infty .
$$

The expected winnings are infinite! On the other hand, the number of rounds N that the game lasts is the number of tosses until the first Heads, so $N \sim \mathrm { F S } ( 1 / 2 )$ and $E ( N ) = 2$ . Thus $E ( 2 ^ { N } ) = \infty$ while $2 ^ { E ( N ) } = 4$ . Infinity certainly does not equal 4, illustrating the danger of confusing $E ( g ( X ) )$ with $g ( E ( X ) )$ when $g$ is not linear.

This problem is often considered a paradox because although the game’s expected payoff is infinite, most people would not be willing to pay very much to play the game (even if they could afford to lose the money). One explanation is to note that the amount of money in the real world is finite. Suppose that if the game lasts longer than 40 rounds, the wealthy stranger flees the country and you get nothing. Since $2 ^ { 4 0 } \approx 1 . 1 \times 1 0 ^ { 1 2 }$ , this still gives you the potential to earn over a trillion dollars, and anyway it’s incredibly unlikely that the game will last longer than 40 rounds. But in this setting, your expected value is

$$
E (X) = \sum_ {n = 1} ^ {4 0} \frac {1}{2 ^ {n}} \cdot 2 ^ {n} + \sum_ {n = 4 1} ^ {\infty} \frac {1}{2 ^ {n}} \cdot 0 = 4 0.
$$

Is this drastic reduction because the wealthy stranger may flee the country? Let’s suppose instead that the wealthy stranger caps your winnings at $2 ^ { 4 0 }$ , so if the game lasts more than 40 rounds you will get this amount rather than walking away empty-handed. Now your expected value is

$$
E (X) = \sum_ {n = 1} ^ {4 0} \frac {1}{2 ^ {n}} \cdot 2 ^ {n} + \sum_ {n = 4 1} ^ {\infty} \frac {1}{2 ^ {n}} \cdot 2 ^ {4 0} = 4 0 + 1 = 4 1,
$$

an increase of only \$1 from the previous scenario. The $\infty$ in the St. Petersburg paradox is driven by an infinite “tail” of extremely rare events where you get extremely large payoffs. Cutting off this tail at some point, which makes sense in the real world, dramatically reduces the expected value of the game. 

## 4.4 Indicator r.v.s and the fundamental bridge

This section is devoted to indicator random variables, which we already encountered in the previous chapter but will treat in much greater detail here. In particular, we will show that indicator r.v.s are an extremely useful tool for calculating expected values.

Recall from the previous chapter that the indicator r.v. $I _ { A }$ (or $I ( A ) )$ for an event A is defined to be 1 if A occurs and 0 otherwise. So $I _ { A }$ is a Bernoulli random variable, where success is defined as $^ { \circ } A$ occurs” and failure is defined as $^ { \circ } A$ does not occur”. Some useful properties of indicator r.v.s are summarized below.

Theorem 4.4.1 (Indicator r.v. properties). Let A and B be events. Then the following properties hold.

1. $( I _ { A } ) ^ { k } = I _ { A }$ for any positive integer $k .$
2. $I _ { A ^ { c } } = 1 - I _ { A } .$
3. $I _ { A \cap B } = I _ { A } I _ { B } .$

Proof. Property 1 holds since $0 ^ { k } = 0$ and $1 ^ { k } = 1$ for any positive integer k. Property 2 holds since $1 - I _ { A }$ is 1 if A does not occur and 0 if A occurs. Property 3 holds since $I _ { A } I _ { B }$ is 1 if both $I _ { A }$ and $I _ { B }$ are 1, and 0 otherwise. Property 4 holds since

$$
I _ {A \cup B} = 1 - I _ {A ^ {c} \cap B ^ {c}} = 1 - I _ {A ^ {c}} I _ {B ^ {c}} = 1 - (1 - I _ {A}) (1 - I _ {B}) = I _ {A} + I _ {B} - I _ {A} I _ {B}.
$$

Indicator r.v.s provide a link between probability and expectation; we call this fact the fundamental bridge.

Theorem 4.4.2 (Fundamental bridge between probability and expectation). There is a one-to-one correspondence between events and indicator r.v.s, and the probability of an event A is the expected value of its indicator r.v. $I _ { A }$

$$
P (A) = E (I _ {A}).
$$

Proof. For any event A, we have an indicator r.v. $I _ { A }$ . This is a one-to-one correspondence since A uniquely determines $I _ { A }$ and vice versa (to get from $I _ { A }$ back to $A ,$ we can use the fact that $A   =   \{ s   \in   S   :   I _ { A } ( s )   =   1 \} )$ . Since $I _ { A } \sim \mathrm { B e r n } ( p )$ with $p = P ( A )$ , we have $E ( I _ { A } ) = P ( A )$ 

The fundamental bridge connects events to their indicator r.v.s, and allows us to express any probability as an expectation. As an example, we give a short proof of inclusion-exclusion and a related inequality known as Boole’s inequality or Bonferroni’s inequality using indicator r.v.s.

Example 4.4.3 (Boole, Bonferroni, and inclusion-exclusion). Let $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ be events. Note that

$$
I (A _ {1} \cup \dots \cup A _ {n}) \leq I (A _ {1}) + \dots + I (A _ {n}),
$$

since if the left-hand side is 0 this is immediate, and if the left-hand side is 1 then at least one term on the right-hand side must be 1. Taking the expectation of both sides and using linearity and the fundamental bridge, we have

$$
P (A _ {1} \cup \dots \cup A _ {n}) \leq P (A _ {1}) + \dots + P (A _ {n}),
$$

which is called Boole’s inequality or Bonferroni’s inequality. To prove inclusionexclusion for $n   =   2$ , we can take the expectation of both sides in Property 4 of Theorem 4.4.1. For general n, we can use properties of indicator r.v.s as follows:

$$
\begin{array}{l} 1 - I (A _ {1} \cup \dots \cup A _ {n}) = I (A _ {1} ^ {c} \cap \dots \cap A _ {n} ^ {c}) \\ = (1 - I (A _ {1})) \dots (1 - I (A _ {n})) \\ = 1 - \sum_ {i} I \left(A _ {i}\right) + \sum_ {i <   j} I \left(A _ {i}\right) I \left(A _ {j}\right) - \dots + (- 1) ^ {n} I \left(A _ {1}\right) \dots I \left(A _ {n}\right). \\ \end{array}
$$

Taking the expectation of both sides, by the fundamental bridge we have proven the inclusion-exclusion theorem. 

Conversely, the fundamental bridge is also extremely useful in many expected value problems. We can often express a complicated discrete r.v. whose distribution we don’t know as a sum of indicator r.v.s, which are extremely simple. The fundamental bridge lets us find the expectation of the indicators; then, using linearity, we obtain the expectation of our original r.v. This strategy is extremely useful and versatile— in fact, we already used it when deriving the expectations of the Binomial and Hypergeometric distributions earlier in this chapter!

Recognizing problems that are amenable to this strategy and then defining the indicator r.v.s takes practice, so it is important to study a lot of examples and solve a lot of problems. In applying the strategy to a random variable that counts the number of [noun]s, we should have an indicator for each potential [noun]. This [noun] could be a person, place, or thing; we will see examples of all three types.

We’ll start by revisiting two problems from Chapter 1, de Montmort’s matching problem and the birthday problem.

Example 4.4.4 (Matching continued). We have a well-shuffled deck of n cards, labeled 1 through n. A card is a match if the card’s position in the deck matches the card’s label. Let X be the number of matches; find E(X).

## Solution:

First let’s check whether X could have any of the named distributions we have studied. The Binomial and Hypergeometric are the only two candidates since the value of X must be an integer between 0 and n. But neither of these distributions has the right support because X can’t take on the value $n - 1 { \mathrm { : ~ i f ~ } } n - 1$ cards are matches, then the nth card must be a match as well. So X does not follow a named distribution we have studied, but we can readily find its mean using indicator r.v.s: let’s write $X = I _ { 1 } + I _ { 2 } + \cdots + I _ { n }$ , where

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text {if the jth card in the deck is a match,} \\ 0 & \text {otherwise.} \end{array} \right.
$$

In other words, $I _ { j }$ is the indicator for $A _ { j }$ , the event that the jth card in the deck is a match. We can imagine that each $I _ { j }$ “raises its hand” to be counted if its card is a match; adding up the raised hands, we get the total number of matches, $X$

By the fundamental bridge,

$$
E (I _ {j}) = P (A _ {j}) = \frac {1}{n}
$$

for all $j$ . So by linearity,

$$
E (X) = E (I _ {1}) + \dots + E (I _ {n}) = n \cdot \frac {1}{n} = 1.
$$

The expected number of matched cards is 1, regardless of $n .$ Even though the $I _ { j }$ are dependent in a complicated way that makes the distribution of X neither Binomial nor Hypergeometric, linearity still holds. 

Example 4.4.5 (Distinct birthdays, birthday matches). In a group of $n$ people, under the usual assumptions about birthdays, what is the expected number of distinct birthdays among the n people, i.e., the expected number of days on which at least one of the people was born? What is the expected number of birthday matches, i.e., pairs of people with the same birthday?

Solution:

Let X be the number of distinct birthdays, and write $X = I _ { 1 } + \dots + I _ { 3 6 5 }$ , where

$$
I _ {j} = \left\{ \begin{array}{l l} 1 & \text {if the jth day is represented,} \\ 0 & \text {otherwise.} \end{array} \right.
$$

We create an indicator for each day of the year because X counts the number of days of the year that are represented. By the fundamental bridge,

$$
E (I _ {j}) = P (j \text {th day is represented}) = 1 - P (\text {no one born on day} j) = 1 - \left(\frac {3 6 4}{3 6 5}\right) ^ {n}
$$

for all $j .$ Then by linearity,

$$
E (X) = 3 6 5 \left(1 - \left(\frac {3 6 4}{3 6 5}\right) ^ {n}\right).
$$

Now let $Y$ be the number of birthday matches. Label the people as $1 , 2 , \ldots , n$ , and order the $\textstyle { \binom { n } { 2 } }$ pairs of people in some definite way. Then we can write

$$
Y = J _ {1} + \dots + J _ {\binom {n} {2}},
$$

where $J _ { i }$ is the indicator of the ith pair of people having the same birthday. We create an indicator for each pair of people since Y counts the number of pairs of people with the same birthday. The probability of any two people having the same birthday is $1 / 3 6 5$ , so again by the fundamental bridge and linearity,

$$
E (Y) = \frac {\binom {n} {2}}{3 6 5}.
$$

In addition to the fundamental bridge and linearity, the last two examples used a basic form of symmetry to simplify the calculations greatly: within each sum of indicator r.v.s, each indicator had the same expected value. For example, in the matching problem the probability of the jth card being a match does not depend on $j ,$ so we can just take n times the expected value of the first indicator r.v.

Other forms of symmetry can also be extremely helpful when available. The next two examples showcase a form of symmetry that stems from having equally likely permutations. Note how symmetry, linearity, and the fundamental bridge are used in tandem to make seemingly very hard problems manageable.

Example 4.4.6 (Putnam problem). A permutation $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ of $1 , 2 , \ldots , n$ has a local maximum at j if $a _ { j } > a _ { j - 1 }$ and $a _ { j } > a _ { j + 1 }$ (for $2 \leq j \leq n - 1$ ; for $j = 1$ a local maximum at j means $a _ { 1 } > a _ { 2 }$ while for $j = n$ , it means $a _ { n }   >   a _ { n - 1 } )$ . For example, 4, 2, 5, 3, 6, 1 has 3 local maxima, at positions 1, 3, and 5. The Putnam exam (a famous, hard math competition, on which the median score is often a 0) from 2006 posed the following question: for $n \geq 2$ , what is the average number of local maxima of a random permutation of $1 , 2 , \ldots , n$ , with all n! permutations equally likely?

## Solution:

This problem can be solved quickly using indicator r.v.s, symmetry, and the fundamental bridge. Let $I _ { 1 } , \ldots , I _ { n }$ be indicator r.v.s, where $I _ { j }$ is 1 if there is a local maximum at position $j ,$ and 0 otherwise. We are interested in the expected value of $\textstyle \sum _ { j = 1 } ^ { n } I _ { j }$ . For $1 < j < n ,   E I _ { j } = 1 / 3$ since having a local maximum at $j$ is equivalent to $a _ { j }$ being the largest of $a _ { j - 1 } , a _ { j } , a _ { j + 1 }$ , which has probability $1 / 3$ since all orders are equally likely. For $j = 1$ or $j = n$ , we have $E I _ { j } = 1 / 2$ since then there is only one neighbor. Thus, by linearity,

$$
E \left(\sum_ {j = 1} ^ {n} I _ {j}\right) = 2 \cdot \frac {1}{2} + (n - 2) \cdot \frac {1}{3} = \frac {n + 1}{3}.
$$

The next example introduces the Negative Hypergeometric distribution, which completes the following table. The table shows the distributions for four sampling schemes: the sampling can be done with or without replacement, and the stopping rule can require a fixed number of draws or a fixed number of successes.

|  | With replacement | Without replacement |
| --- | --- | --- |
| Fixed number of trials | Binomial | Hypergeometric |
| Fixed number of successes | Negative Binomial | Negative Hypergeometric |

Example 4.4.7 (Negative Hypergeometric). An urn contains w white balls and b black balls, which are randomly drawn one by one without replacement, until r white balls have been obtained. The number of black balls drawn before drawing the rth white ball has a Negative Hypergeometric distribution with parameters $w , b , r$ . We denote this distribution by $\mathrm { N H G e o m } ( w , b , r )$ . Of course, we assume that $r \leq w$ . For example, if we shuffle a deck of cards and deal them one at a time, the number of cards dealt before uncovering the first ace is NHGeom(4, 48, 1).

As another example, suppose a college offers g good courses and b bad courses (for some definition of “good” and “bad”), and a student wants to find 4 good courses to take. Not having any idea which of the courses are good, the student randomly tries out courses one at a time, stopping when they have obtained 4 good courses. Then the number of bad courses the student tries out is $\mathrm { N H G e o m } ( g , b , 4 )$

We can obtain the PMF of $X \sim \operatorname { N H G e o m } ( w , b , r )$ by noting that, in the urn context, $X = k$ means that the $( r + k )$ th ball chosen is white and exactly $r - 1$ of the first $r + k - 1$ balls chosen are white. This gives

$$
P (X = k) = \frac {\binom {w} {r - 1} \binom {b} {k}}{\binom {w + b} {r + k - 1}} \cdot \frac {w - r + 1}{w + b - r - k + 1}
$$

for $k = 0 , 1 , \ldots , b$ (and 0 otherwise).

Alternatively, we can imagine that we continue drawing balls until the urn has been emptied out; this is valid since whether or not we continue to draw balls after obtaining the rth white ball has no effect on X. Think of the $w + b$ balls as lined up in a random order, the order in which they will be drawn.

Then $X = k$ means that among the first $r + k - 1$ balls there are exactly $r - 1$ white balls, then there is a white ball, and then among the last $w + b - r - k$ balls there are exactly $w - r$ white balls. All ${ \binom { w + b } { w } }$ possibilities for the locations of the white balls in the line are equally likely. So by the naive definition of probability, we have the following slightly simpler expression for the PMF:

$$
P (X = k) = \frac {\binom {r + k - 1} {r - 1} \binom {w + b - r - k} {w - r}}{\binom {w + b} {w}},
$$

for $k = 0 , 1 , \ldots , b$ (and 0 otherwise).

Finding the expected value of a Negative Hypergeometric r.v. directly from the definition of expectation results in complicated sums. But the answer is very simple: for $X \sim \operatorname { N H G e o m } ( w , b , r )$ , we have $E ( X ) = r b / ( w + 1 )$

Let’s prove this using indicator r.v.s. As explained above, we can assume that we continue drawing balls until the urn is empty. First consider the case $r = 1$ . Label the black balls as $1 , 2 , \ldots , b ,$ and let $I _ { j }$ be the indicator of black ball $j$ being drawn before any white balls have been drawn. Then $P ( I _ { j } = 1 ) = 1 / ( w + 1 )$ since, listing out the order in which black ball $j$ and the white balls are drawn (ignoring the other balls), all orders are equally likely by symmetry, and $I _ { j } = 1$ is equivalent to black ball $j$ being first in this list. So by linearity,

$$
E \left(\sum_ {j = 1} ^ {b} I _ {j}\right) = \sum_ {j = 1} ^ {b} E (I _ {j}) = b / (w + 1).
$$

Sanity check: This answer makes sense since it is increasing in $b ,$ decreasing in $w ,$ and correct in the extreme cases $b   =   0$ (when no black balls will be drawn) and $w   =   0$ (when all the black balls will be exhausted before drawing a nonexistent white ball). Moreover, note that $b / ( w + 1 )$ looks similar to, but is strictly smaller than, $b / w ,$ which is the expected value of a Geom $( w / ( w + b ) ) { \mathrm { ~ r . v ~ } }$ . It makes sense that sampling without replacement should give a smaller expected waiting time than sampling with replacement. Similarly, if you are searching for something you lost, it makes more sense to choose locations to check without replacement, rather than wasting time looking over and over again in locations you already ruled out.

For general $r ,$ write $X = X _ { 1 } + X _ { 2 } + \cdots + X _ { r }$ , where $X _ { 1 }$ is the number of black balls before the first white ball, $X _ { 2 }$ is the number of black balls after the first white ball but before the second white ball, etc. By essentially the same argument we used to handle the $r = 1 { \mathrm { ~ c a s e } } .$ we have $E ( X _ { j } ) = b / ( w + 1 )$ for each $j .$ So by linearity,

$$
E (X) = r b / (w + 1).
$$

Closely related to indicator r.v.s is an alternative expression for the expectation of a nonnegative integer-valued r.v. X. Rather than summing up values of X times values of the PMF of X, we can sum up probabilities of the form $P ( X > n )$ (known as tail probabilities), over nonnegative integers $n .$

Theorem 4.4.8 (Expectation via survival function). Let X be a nonnegative integer-valued r.v. Let F be the CDF of $X ,$ and $G ( x ) = 1 - F ( x ) = P ( X > x )$ . The function $G$ is called the survival function of X. Then

$$
E (X) = \sum_ {n = 0} ^ {\infty} G (n).
$$

That is, we can obtain the expectation of X by summing up the survival function (or, stated otherwise, summing up tail probabilities of the distribution).

Proof. For simplicity, we will prove the result only for the case that X is bounded, i.e., there is a nonnegative integer b such that X is always at most b. We can represent X as a sum of indicator r.v.s: $X = I _ { 1 } + I _ { 2 } + \cdots + I _ { b }$ , where $I _ { n } = I ( X \geq n )$ . For example, if $X   =   7$ occurs, then $I _ { 1 }$ through $I _ { 7 }$ equal 1 while the other indicators equal 0.

By linearity and the fundamental bridge, and the fact that $\{ X \geq k \}$ is the same event as $\{ X > k - 1 \}$ ,

$$
E (X) = \sum_ {k = 1} ^ {b} E (I _ {k}) = \sum_ {k = 1} ^ {b} P (X \geq k) = \sum_ {n = 0} ^ {b - 1} P (X > n) = \sum_ {n = 0} ^ {\infty} G (n).
$$

As a quick example, we use the above result to give another derivation of the mean of a Geometric r.v.

Example 4.4.9 (Geometric expectation redux). Let $X \sim \operatorname { G e o m } ( p )$ , and $q = 1 - p .$ Using the Geometric story, $\{ X > n \}$ is the event that the first $n + 1$ trials are all failures. So by Theorem 4.4.8,

$$
E (X) = \sum_ {n = 0} ^ {\infty} P (X > n) = \sum_ {n = 0} ^ {\infty} q ^ {n + 1} = \frac {q}{1 - q} = \frac {q}{p},
$$

confirming what we already knew about the mean of a Geometric.

## 4.5 Law of the unconscious statistician (LOTUS)

As we saw in the St. Petersburg paradox, $E ( g ( X ) )$ does not equal $g ( E ( X ) )$ in general if $g$ is not linear. So how do we correctly calculate $E(g(X))?$ Since $g ( X )$ is an r.v., one way is to first find the distribution of $g ( X )$ and then use the definition of expectation. Perhaps surprisingly, it turns out that it is possible to find $E ( g ( X ) )$ directly using the distribution of $X$ , without first having to find the distribution of $g ( X )$ . This is done using the law of the unconscious statistician (LOTUS).

Theorem 4.5.1 (LOTUS). If X is a discrete r.v. and $g$ is a function from R to R, then

$$
E (g (X)) = \sum_ {x} g (x) P (X = x),
$$

where the sum is taken over all possible values of $X$ .

This means that we can get the expected value of $g ( X )$ knowing only $P ( X = x )$ the PMF of $X$ ; we don’t need to know the PMF of $g ( X )$ . The name comes from the fact that in going from $E ( X )$ to $E ( g ( X ) )$ it is tempting just to change x to $g ( x )$ in the definition, which can be done very easily and mechanically, perhaps in a state of unconsciousness. On second thought, it may sound too good to be true that finding the distribution of $g ( X )$ is not needed for this calculation, but LOTUS says it is true.

Before proving LOTUS in general, let’s see why it is true in some special cases. Let X have support $0 , 1 , 2 , \ldots$ . with probabilities $p _ { 0 } , p _ { 1 } , p _ { 2 } , \ldots$ , so the $\mathrm { P M F }$ is $P(X = n) =$ $p _ { n }$ . Then $X ^ { 3 }$ has support $0 ^ { 3 } , 1 ^ { 3 } , 2 ^ { 3 } , \ldots$ . with probabilities $p _ { 0 } , p _ { 1 } , p _ { 2 } , \ldots ,$ so

$$
E (X) = \sum_ {n = 0} ^ {\infty} n p _ {n},
$$

$$
E (X ^ {3}) = \sum_ {n = 0} ^ {\infty} n ^ {3} p _ {n}.
$$

As claimed by LOTUS, to edit the expression for $E ( X )$ into an expression for $E ( X ^ { 3 } )$ we can just change the n in front of the $p _ { n }$ to an $n ^ { 3 }$ . This was an easy example since the function $g ( x ) = x ^ { 3 }$ is one-to-one. But LOTUS holds much more generally. The key insight needed for the proof of LOTUS for general $g$ is the same as the one we used for the proof of linearity: the expectation of $g ( X )$ can be written in ungrouped form as

$$
E (g (X)) = \sum_ {s} g (X (s)) P (\{s \}),
$$

where the sum is over all the pebbles in the sample space, but we can also group the pebbles into super-pebbles according to the value that X assigns to them. Within the super-pebble $X = x ,   g ( X )$ always takes on the value $g ( x )$ . Therefore,

$$
\begin{array}{l} E (g (X)) = \sum_ {s} g (X (s)) P (\{s \}) \\ = \sum_ {x} \sum_ {s: X (s) = x} g (X (s)) P (\{s \}) \\ = \sum_ {x} g (x) \sum_ {s: X (s) = x} P (\{s \}) \\ = \sum_ {x} g (x) P (X = x). \\ \end{array}
$$

In the last step, we used the fact that $\textstyle \sum _ { s : X ( s ) = x } P ( \{ s \} )$ is the weight of the superpebble $X = x$

## 4.6 Variance

One important application of LOTUS is for finding the variance of a random variable. Like expected value, variance is a single-number summary of the distribution of a random variable. While the expected value tells us the center of mass of a distribution, the variance tells us how spread out the distribution is.

Definition 4.6.1 (Variance and standard deviation). The variance of an r.v. X is

$$
\mathrm{Var} (X) = E (X - E X) ^ {2}.
$$

The square root of the variance is called the standard deviation (SD):

$$
\mathrm{SD} (X) = \sqrt {\mathrm{Var} (X)}.
$$

Recall that when we write $E(X - EX)^{2}$ , we mean the expectation of the random variable $(X - EX)^{2}$ , not $(E(\dot{X} - EX))^2$ (which is 0 by linearity).

The variance of X measures how far X is from its mean on average, but instead of simply taking the average difference between X and its mean EX, we take the average squared difference. To see why, note that the average deviation from the mean, $E(X - EX)$ , always equals 0 by linearity; positive and negative deviations cancel each other out. By squaring the deviations, we ensure that both positive and negative deviations contribute to the overall variability. However, because variance is an average squared distance, it has the wrong units: if X is in dollars, Var(X) is in squared dollars. To get back to our original units, we take the square root; this gives us the standard deviation.

One might wonder why variance isn’t defined as $E [ X { - } E X ]$ which would achieve the goal of counting both positive and negative deviations while maintaining the same units as X. This measure of variability isn’t nearly as popular as $E(X - EX)^{2}$ , for a variety of reasons. Most notably, the absolute value function isn’t differentiable at 0, whereas the squaring function is differentiable everywhere and is central in various fundamental mathematical results such as the Pythagorean theorem.

An equivalent expression for variance is $\operatorname { V a r } ( X ) = E ( X ^ { 2 } ) - ( E X ) ^ { 2 }$ . This formula is often easier to work with when doing actual calculations. Since this is the variance formula we will use over and over again, we state it as its own theorem.

Theorem 4.6.2. For any r.v. X,

$$
\mathrm{Var} (X) = E (X ^ {2}) - (E X) ^ {2}.
$$

Proof. Let $\mu = E X$ . Expanding $( X - \mu ) ^ { 2 }$ and using linearity, the variance of X is

$$
E (X - \mu) ^ {2} = E (X ^ {2} - 2 \mu X + \mu^ {2}) = E (X ^ {2}) - 2 \mu E X + \mu^ {2} = E (X ^ {2}) - \mu^ {2}.
$$

Variance has the following properties. The first two are easily verified from the definition, the third will be addressed in a later chapter, and the last one is proven just after stating it.

$\operatorname { V a r } ( X + c ) = \operatorname { V a r } ( X )$ for any constant c. Intuitively, if we shift a distribution to the left or right, that should affect the center of mass of the distribution but not its spread.
$\operatorname { V a r } ( c X ) = c ^ { 2 } \operatorname { V a r } ( X )$ for any constant c.
• If X and Y are independent, then $\operatorname { V a r } ( X + Y )   =   \operatorname { V a r } ( X ) + \operatorname { V a r } ( Y )$ We prove this and discuss it more in Chapter 7. This is not true in general if X and Y are dependent. For example, in the extreme case where X always equals Y , we have

$$
\operatorname{Var} (X + Y) = \operatorname{Var} (2 X) = 4 \operatorname{Var} (X) > 2 \operatorname{Var} (X) = \operatorname{Var} (X) + \operatorname{Var} (Y)
$$

if $\operatorname { V a r } ( X ) > 0$ (which will be true unless X is a constant, as the next property shows).

$\operatorname { V a r } ( X )   \geq   0 ,$ , with equality if and only if $P ( X   =   a )   =   1$ for some constant a. In other words, the only random variables that have zero variance are constants (which can be thought of as degenerate $\mathrm { r . v . s ) }$ ; all other r.v.s have positive variance.

To prove the last property, note that Var(X) is the expectation of the nonnegative $\mathrm { r . v . } \quad ( X \mathrm { ~ - ~ } E X ) ^ { 2 }$ , so $\operatorname { V a r } ( X )   \geq   0$ . If $P ( X   =   a )   =   1$ for some constant $a ,$ then $E ( X ) = a$ and $E ( X ^ { 2 } ) = { \dot { a } } ^ { 2 }$ , so $\operatorname { V a r } ( X ) = 0$ . Conversely, suppose that $\operatorname { V a r } ( X ) = 0$ Then $E ( X - E X ) ^ { 2 } = 0$ , which shows that $( X - E X ) ^ { 2 } = 0$ has probability 1, which in turn shows that X equals its mean with probability 1.

h 4.6.3 (Variance is not linear). Unlike expectation, variance is not linear. The constant comes out squared in $\operatorname { V a r } ( c X ) = c ^ { 2 } \operatorname { V a r } ( X )$ , and the variance of the sum of r.v.s may not be the sum of their variances if they are dependent.

Example 4.6.4 (Geometric and Negative Binomial variance). In this example we’ll use LOTUS to compute the variance of the Geometric distribution.

Let $X \sim \operatorname { G e o m } ( p )$ . We already know $E ( X ) = q / p .$ . By LOTUS,

$$
E (X ^ {2}) = \sum_ {k = 0} ^ {\infty} k ^ {2} P (X = k) = \sum_ {k = 0} ^ {\infty} k ^ {2} p q ^ {k} = \sum_ {k = 1} ^ {\infty} k ^ {2} p q ^ {k}.
$$

We’ll find this using a tactic similar to how we found the expectation, starting from the geometric series

$$
\sum_ {k = 0} ^ {\infty} q ^ {k} = \frac {1}{1 - q}
$$

and taking derivatives. After differentiating once with respect to $q ,$ we have

$$
\sum_ {k = 1} ^ {\infty} k q ^ {k - 1} = \frac {1}{(1 - q) ^ {2}}.
$$

We start the sum from $k = 1$ since the $k = 0$ term is 0 anyway. If we differentiate again, we’ll get $k ( k - 1 )$ instead of $k ^ { 2 }$ as we want, so let’s replenish our supply of $q ^ { \prime } \mathrm { s }$ by multiplying both sides by $q .$ This gives

$$
\sum_ {k = 1} ^ {\infty} k q ^ {k} = \frac {q}{(1 - q) ^ {2}}.
$$

Now we are ready to take another derivative:

$$
\sum_ {k = 1} ^ {\infty} k ^ {2} q ^ {k - 1} = \frac {1 + q}{(1 - q) ^ {3}},
$$

so

$$
E (X ^ {2}) = \sum_ {k = 1} ^ {\infty} k ^ {2} p q ^ {k} = p q \frac {1 + q}{(1 - q) ^ {3}} = \frac {q (1 + q)}{p ^ {2}}.
$$

Finally,

$$
\operatorname{Var} (X) = E (X ^ {2}) - (E X) ^ {2} = \frac {q (1 + q)}{p ^ {2}} - \left(\frac {q}{p}\right) ^ {2} = \frac {q}{p ^ {2}}.
$$

This is also the variance of the First Success distribution, since shifting by a constant does not affect the variance.

Since an $\mathrm { N B i n } ( r , p )$ r.v. can be represented as a sum of $r \mathrm { i . i . d }$ . Geom $( p )$ r.v.s by Theorem 4.3.10, and since variance is additive for independent random variables, it follows that the variance of the $\mathrm { N B i n } ( r , p )$ distribution is $r \cdot { \frac { q } { p ^ { 2 } } }$ 

LOTUS is an all-purpose tool for computing $E ( g ( X ) )$ for any $g ,$ but as it usually leads to complicated sums, it should be used as a last resort. For variance calculations, our trusty indicator r.v.s can sometimes be used in place of LOTUS, as in the next example.

Example 4.6.5 (Binomial variance). Let’s find the variance of $X \sim \operatorname { B i n } ( n , p )$ using indicator r.v.s to avoid tedious sums. Represent $X = I _ { 1 } + I _ { 2 } + \cdots + I _ { n }$ , where $I _ { j }$ is the indicator of the jth trial being a success. Each $I _ { j }$ has variance

$$
\mathrm{Var} (I _ {j}) = E (I _ {j} ^ {2}) - (E (I _ {j})) ^ {2} = p - p ^ {2} = p (1 - p).
$$

(Recall that $I _ { j } ^ { 2 } = I _ { j }$ , so $E ( I _ { j } ^ { 2 } ) = E ( I _ { j } ) = p . )$

Since the $I _ { j }$ are independent, we can add their variances to get the variance of their sum:

$$
\operatorname{Var} (X) = \operatorname{Var} (I _ {1}) + \dots + \operatorname{Var} (I _ {n}) = n p (1 - p).
$$

Alternatively, we can find $E ( X ^ { 2 } )$ by first finding $E { \binom { X } { 2 } }$ . The latter sounds more complicated, but actually it is simpler since $\textstyle { \binom { X } { 2 } }$ is the number of pairs of successful trials. Creating an indicator r.v. for each pair of trials, we have

$$
E \binom{X}{2} = \binom{n}{2} p ^ {2}.
$$

Thus,

$$
n (n - 1) p ^ {2} = E (X (X - 1)) = E (X ^ {2}) - E (X) = E (X ^ {2}) - n p,
$$

which again gives

$$
\mathrm{Var} (X) = E (X ^ {2}) - (E X) ^ {2} = (n (n - 1) p ^ {2} + n p) - (n p) ^ {2} = n p (1 - p).
$$

Exercise 48 uses this strategy to find the variance of the Hypergeometric.

## 4.7 Poisson

The last discrete distribution that we’ll introduce in this chapter is the Poisson, which is an extremely popular distribution for modeling discrete data. We’ll introduce its PMF, mean, and variance, and then discuss its story in more detail.

Definition 4.7.1 (Poisson distribution). An r.v. X has the Poisson distribution with parameter λ, where $\lambda > 0$ , if the PMF of X is

$$
P (X = k) = \frac {e ^ {- \lambda} \lambda^ {k}}{k !}, \quad k = 0, 1, 2, \dots .
$$

We write this as $X \sim  Pois (\lambda)$

This is a valid PMF because of the Taylor series $\begin{array} { r } { \sum _ { k = 0 } ^ { \infty } \frac { \lambda ^ { k } } { k ! } = e ^ { \lambda } } \end{array}$

Example 4.7.2 (Poisson expectation and variance). Let $X   \sim   \mathrm { P o i s } ( \lambda )$ . We will show that the mean and variance are both equal to λ. For the mean, we have

$$
\begin{array}{l} E (X) = e ^ {- \lambda} \sum_ {k = 0} ^ {\infty} k \frac {\lambda^ {k}}{k !} \\ = e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} k \frac {\lambda^ {k}}{k !} \\ = \lambda e ^ {- \lambda} \sum_ {k = 1} ^ {\infty} \frac {\lambda^ {k - 1}}{(k - 1) !} \\ = \lambda e ^ {- \lambda} e ^ {\lambda} = \lambda . \\ \end{array}
$$

First we dropped the $k = 0$ term because it was 0. Then we took a λ out of the sum so that what was left inside was just the Taylor series for $e ^ { \lambda }$

To get the variance, we first find $E ( X ^ { 2 } )$ . By LOTUS,

$$
E (X ^ {2}) = \sum_ {k = 0} ^ {\infty} k ^ {2} P (X = k) = e ^ {- \lambda} \sum_ {k = 0} ^ {\infty} k ^ {2} \frac {\lambda^ {k}}{k !}.
$$

From here, the derivation is very similar to that of the variance of the Geometric. Differentiate the familiar series

$$
\sum_ {k = 0} ^ {\infty} \frac {\lambda^ {k}}{k !} = e ^ {\lambda}
$$

with respect to λ and replenish:

$$
\begin{array}{l} \sum_ {k = 1} ^ {\infty} k \frac {\lambda^ {k - 1}}{k !} = e ^ {\lambda}, \\ \sum_ {k = 1} ^ {\infty} k \frac {\lambda^ {k}}{k !} = \lambda e ^ {\lambda}. \\ \end{array}
$$

Rinse and repeat:

$$
\begin{array}{l} \sum_ {k = 1} ^ {\infty} k ^ {2} \frac {\lambda^ {k - 1}}{k !} = e ^ {\lambda} + \lambda e ^ {\lambda} = e ^ {\lambda} (1 + \lambda), \\ \sum_ {k = 1} ^ {\infty} k ^ {2} \frac {\lambda^ {k}}{k !} = e ^ {\lambda} \lambda (1 + \lambda). \\ \end{array}
$$