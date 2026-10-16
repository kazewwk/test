32. In Evan’s history class, 10 out of 100 key terms will be randomly selected to appear on the final exam; Evan must then choose 7 of those 10 to define. Since he knows the format of the exam in advance, Evan is trying to decide how many key terms he should study.

(a) Suppose that Evan decides to study s key terms, where s is an integer between 0 and 100. Let X be the number of key terms appearing on the exam that he has studied. What is the distribution of X? Give the name and parameters, in terms of s.
(b) Using R or other software, calculate the probability that Evan knows at least $7$ o f the 10 key terms that appear on the exam, assuming that he studies $s = 7 5$ key terms.

33. A book has n typos. Two proofreaders, Prue and Frida, independently read the book. Prue catches each typo with probability $p _ { 1 }$ and misses it with probability $q _ { 1 } = 1 - p _ { 1 }$ independently, and likewise for Frida, who has probabilities $p _ { 2 }$ of catching and $q _ { 2 } = 1   -   p _ { 2 }$ of missing each typo. Let $X _ { 1 }$ be the number of typos caught by Prue, $X _ { 2 }$ be the number caught by Frida, and X be the number caught by at least one of the two proofreaders.

(a) Find the distribution of X.
(b) For this part only, assume that $p _ { 1 }   =   p _ { 2 }$ . Find the conditional distribution of $X _ { 1 }$ given that $X _ { 1 } + X _ { 2 } = t$

34. There are n students at a certain school, of whom $X \sim \operatorname { B i n } ( n , p )$ are Statistics majors. A simple random sample of size m is drawn (“simple random sample” means sampling without replacement, with all subsets of the given size equally likely).

(a) Find the $\mathrm { P M F }$ of the number of Statistics majors in the sample, using the law of total probability (don’t forget to say what the support is). You can leave your answer as a sum (though with some algebra it can be simplified, by writing the binomial coefficients in terms of factorials and using the binomial theorem).
(b) Give a story proof derivation of the distribution of the number of Statistics majors in the sample; simplify fully.

Hint: Does it matter whether the students declare their majors before or after the random sample is drawn?

35. s Players A and B take turns in answering trivia questions, starting with player A answering the first question. Each time A answers a question, she has probability $p _ { 1 }$ getting it right. Each time B plays, he has probability $p _ { 2 }$ of getting it right.

(a) If A answers m questions, what is the PMF of the number of questions she gets right?
(b) If A answers m times and B answers n times, what is the PMF of the total number of questions they get right (you can leave your answer as a sum)? Describe exactly when/whether this is a Binomial distribution.
(c) Suppose that the first player to answer correctly wins the game (with no predetermined maximum number of questions that can be asked). Find the probability that A wins the game.

36. There are n voters in an upcoming election in a certain country, where n is a large, even number. There are two candidates: Candidate A (from the Unite Party) and Candidate B (from the Untie Party). Let X be the number of people who vote for Candidate A. Suppose that each voter chooses randomly whom to vote for, independently and with equal probabilities.

(a) Find an exact expression for the probability of a tie in the election (so the candidates end up with the same number of votes).

(b) Use Stirling’s approximation, which approximates the factorial function as

$$
n! \approx \sqrt {2 \pi n} \left(\frac {n}{e}\right) ^ {n},
$$

to find a simple approximation to the probability of a tie. Your answer should be of the form $1 / { \sqrt { c n } } ,$ with c a constant (which you should specify).

37. s A message is sent over a noisy channel. The message is a sequence x1, $x _ { 2 } , \ldots , x _ { n }$ of n bits $( x _ { i } \in \{ 0 , 1 \} )$ . Since the channel is noisy, there is a chance that any bit might be corrupted, resulting in an error (a 0 becomes a 1 or vice versa). Assume that the error events are independent. Let $p$ be the probability that an individual bit has an error $( 0 < p < 1 / 2 )$ . Let $y _ { 1 } , y _ { 2 } , \ldots , y _ { n }$ be the received message (so $y _ { i } = x _ { i }$ if there is no error in that bit, but $y _ { i } = 1 - x _ { i }$ if there is an error there).

To help detect errors, the nth bit is reserved for a parity check: $x _ { n }$ is defined to be 0 if $x _ { 1 } + x _ { 2 } + \cdots + x _ { n - 1 }$ is even, and 1 if $x _ { 1 } + x _ { 2 } + \cdots + x _ { n - 1 }$ is odd. When the message is received, the recipient checks whether $y _ { n }$ has the same parity as $y _ { 1 } + y _ { 2 } + \cdots + y _ { n - 1 }$ . If the parity is wrong, the recipient knows that at least one error occurred; otherwise, the recipient assumes that there were no errors.

(a) For $n   =   5 , p   =   0 . 1$ , what is the probability that the received message has errors which go undetected?
(b) For general n and p, write down an expression (as a sum) for the probability that the received message has errors which go undetected.
(c) Give a simplified expression, not involving a sum of a large number of terms, for the probability that the received message has errors which go undetected.

Hint for (c): Letting

$$
a = \sum_ {k \text {even}, k \geq 0} \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} \text {and} b = \sum_ {k \text {odd}, k \geq 1} \binom {n} {k} p ^ {k} (1 - p) ^ {n - k},
$$

the binomial theorem makes it possible to find simple expressions for $a + b$ and $a - b ,$ which then makes it possible to obtain a and b.

## Independence of r.v.s

38. (a) Give an example of dependent r.v.s X and Y such that $P(X < Y) = 1$

(b) Give an example of independent r.v.s X and Y such that $P(X < Y) = 1$

39. Give an example of two discrete random variables X and Y on the same sample space such that X and Y have the same distribution, with support $\{ 1 , 2 , \ldots , 1 0 \}$ , but the event $X = Y$ never occurs. If X and Y are independent, is it still possible to construct such an example?

40. Suppose X and Y are discrete r.v.s such that $P(X = Y) = 1$ . This means that X and Y always take on the same value.

(a) Do X and Y have the same PMF?
(b) Is it possible for X and Y to be independent?

41. If $X , Y , Z$ are r.v.s such that X and Y are independent and Y and $Z$ are independent, does it follow that X and Z are independent?

Hint: Think about simple and extreme examples.

42. s Let X be a random day of the week, coded so that Monday is 1, Tuesday is 2, etc. (so X takes values $1 , 2 , \ldots , 7 ,$ with equal probabilities). Let Y be the next day after X (again represented as an integer between 1 and 7). Do X and Y have the same distribution? What is $P(X < Y)?$

43. (a) Is it possible to have two r.v.s X and Y such that X and Y have the same distribution but $P ( X < Y ) \geq p ,$ where:

$p = 0 . 9 7$
$p = 0 . 9 9 ?$
• p = 0.9999999999999?
$p = 1 ?$

For each, give an example showing it is possible, or prove it is impossible.

Hint: Do the previous question first.

(b) Consider the same question as in Part (a), but now assume that X and Y are independent. Do your answers change?

44. For x and y binary digits (0 or 1), let $x \oplus y$ be 0 if $x = y$ and $1 { \mathrm { ~ i f ~ } } x \neq y$ (this operation is called exclusive or (often abbreviated to XOR), or addition mod 2 ).

(a) Let $X   \sim   \mathrm { B e r n } ( p )$ and $Y \sim \operatorname { B e r n } ( 1 / 2 )$ , independently. What is the distribution of $X \oplus Y ?$
(b) With notation as in (a), is $X \oplus Y$ independent of X? Is $X \oplus Y$ independent of $Y ?$ Be sure to consider both the case $p = 1 / 2$ and the case $p \neq 1 / 2$
(c) Let $X _ { 1 } , \ldots , X _ { n }$ be i.i.d. Bern(1/2). For each nonempty subset J of $\{ 1 , 2 , \ldots , n \}$ , let

$$
Y _ {J} = \bigoplus_ {j \in J} X _ {j},
$$

where the notation means to $" \mathrm{add''}$ in the ⊕ sense all the elements of $J ;$ the order in which this is done doesn’t matter since x ⊕ $y = y \oplus x$ and $( x \oplus y ) \oplus z = x \oplus ( y \oplus z )$ Show that $Y _ { J }   \sim   \mathrm { B e r n } ( 1 / 2 )$ and that these $2 ^ { n } - 1$ r.v.s are pairwise independent, but not independent. For example, we can use this to simulate 1023 pairwise independent fair coin tosses using only 10 independent fair coin tosses.

Hint: Apply the previous parts with $p = 1 / 2$ . Show that if J and K are two different nonempty subsets of $\{ 1 , 2 , \ldots , n \}$ , then we can write $Y _ { J } = A   \oplus   B , Y _ { K } = A   \oplus   C ,$ where A consists of the $X _ { i }$ with $i \in J \cap K$ , B consists of the $X _ { i }$ with $i \in J \cap K ^ { c }$ , and C consists of the $X _ { i }$ with $i \in J ^ { c } \cap K$ . Then $A , B , C$ are independent since they are based on disjoint sets of $X _ { i } .$ Also, at most one of these sets of $X _ { i }$ can be empty. If $J \cap K   =   \emptyset$ , then $Y _ { J } = B , Y _ { K } = C$ . Otherwise, compute $P(Y_{J} = y,Y_{K} = z)$ by conditioning on whether $A = 1$

## Mixed practice

45. s A new treatment for a disease is being tested, to see whether it is better than the standard treatment. The existing treatment is effective on 50% of patients. It is believed initially that there is a $2 / 3$ chance that the new treatment is effective on 60% of patients, and a $1 / 3$ chance that the new treatment is effective on 50% of patients. In a pilot study, the new treatment is given to 20 random patients, and is effective for 15 of them.

(a) Given this information, what is the probability that the new treatment is better than the standard treatment?
(b) A second study is done later, giving the new treatment to 20 new random patients. Given the results of the first study, what is the PMF for how many of the new patients the new treatment is effective on? (Letting p be the answer to (a), your answer can be left in terms of $p . )$

46. Independent Bernoulli trials are performed, with success probability $1 / 2$ for each trial. An important question that often comes up in such settings is how many trials to perform. Many controversies have arisen in statistics over the issue of how to analyze data coming from an experiment where the number of trials can depend on the data collected so far.

For example, if we can follow the rule “keep performing trials until there are more than twice as many failures as successes, and then stop”, then naively looking at the ratio of failures to successes (if and when the process stops) will give more than 2:1 rather than the true theoretical 1:1 ratio; this could be a very misleading result! However, it might never happen that there are more than twice as many failures as successes; in this problem, you will find the probability of that happening.

(a) Two gamblers, A and B, make a series of bets, where each has probability $1 / 2$ of winning a bet, but A gets \$2 for each win and loses \$1 for each loss (a very favorable game for A!). Assume that the gamblers are allowed to borrow money, so they can and do gamble forever. Let $p _ { k }$ be the probability that A, starting with \$k, will ever reach \$0, for each $k \geq 0$ . Explain how this story relates to the original problem, and how the original problem can be solved if we can find $p _ { k }$

(b) Find $p _ { k }$

Hint: As in the gambler’s ruin, set up and solve a difference equation for $p _ { k }$ . We have $p _ { k } \to 0$ as $k \to \infty$ (you don’t need to prove this, but it should make sense since the game is so favorable to A, which will result in A’s fortune going to $\infty ;   \mathrm { a }$ formal proof, not required here, could be done using the law of large numbers, an important theorem from Chapter 10). The solution can be written neatly in terms of the golden ratio.

(c) Find the probability of ever having more than twice as many failures as successes with independent $\mathrm { B e r n } ( 1 / 2 )$ trials, as originally desired.

47. A copy machine is used to make n pages of copies per day. The machine has two trays in which paper gets loaded, and each page used is taken randomly and independently from one of the trays. At the beginning of the day, the trays are refilled so that they each have m pages.

(a) Let pbinom $( x , n , p )$ be the CDF of the $\operatorname { B i n } ( n , p )$ distribution, evaluated at $x .$ In terms of pbinom, find a simple expression for the probability that both trays have enough paper on any particular day, when this probability is strictly between 0 and 1 (also specify the values of m for which the probability is 0 and the values for which it is 1).

Hint: Be careful about whether inequalities are strict, since the Binomial is discrete.

(b) Using a computer, find the smallest value of m for which there is at least a 95% chance that both trays have enough paper on a particular day, for $n = 1 0 , n = 1 0 0 , n = 1 0 0 0$ and $n = 1 0 0 0 0$

Hint: If you use R, you may find the following commands useful:

$\tt g \; \textless - \; f u n c t i o n ( m , n )$ [your answer from $( a ) J$ defines a function g such that $g ( m , n )$ is your answer from $(a), \mathrm{g}(1:100,100)$ gives the vector $( g ( 1 , 1 0 0 ) , \ldots , g ( 1 0 0 , 1 0 0 ) )$ which $(v>0.95)$ gives the indices of the components of vector v that exceed 0.95, and min(w) gives the minimum of a vector $\mathbf { w }$

![](images/page_164_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

## 4.1 Definition of expectation

In the previous chapter, we introduced the distribution of a random variable, which gives us full information about the probability that the r.v. will fall into any particular set. For example, we can say how likely it is that the r.v. will exceed 1000, that it will equal 5, or that it will be in the interval [0, 7]. It can be unwieldy to manage so many probabilities though, so often we want just one number summarizing the “average” value of the r.v.

There are several senses in which the word “average” is used, but by far the most commonly used is the mean of an r.v., also known as its expected value. In addition, much of statistics is about understanding variability in the world, so it is often important to know how “spread out” the distribution is; we will formalize this with the concepts of variance and standard deviation. As we’ll see, variance and standard deviation are defined in terms of expected values, so the uses of expected values go far beyond just computing averages.

Given a list of numbers $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ , the familiar way to average them is to add them up and divide by n. This is called the arithmetic mean, and is defined by

$$
\bar {x} = \frac {1}{n} \sum_ {j = 1} ^ {n} x _ {j}.
$$

More generally, we can define a weighted mean of $x _ { 1 } , \ldots , x _ { n }$ as

$$
\text {weighted - mean} (x) = \sum_ {j = 1} ^ {n} x _ {j} p _ {j},
$$

where the weights $p _ { 1 } , \ldots , p _ { n }$ are pre-specified nonnegative numbers that add up to 1 (so the unweighted mean ¯x is obtained when $p _ { j } = 1 / n$ for all $j )$

The definition of expectation for a discrete r.v. is inspired by the weighted mean of a list of numbers, with weights given by probabilities.

Definition 4.1.1 (Expectation of a discrete r.v.). The expected value (also called the expectation or mean) of a discrete r.v. X whose distinct possible values are

$x _ { 1 } , x _ { 2 } , \ldots$ is defined by

$$
E (X) = \sum_ {j = 1} ^ {\infty} x _ {j} P (X = x _ {j}).
$$

If the support is finite, then this is replaced by a finite sum. We can also write

$$
E (X) = \sum_ {x} \underbrace {x} _ {\text {value}} \underbrace {P (X = x)} _ {\text {PMF at} x},
$$

where the sum is over the support of X (in any case, x $P ( X = x )$ is 0 for any x not in the support). The expectation is undefined if $\textstyle \sum _ { j = 1 } ^ { \infty } | x _ { j } | { \stackrel { \cdot } { P } } ( X = x _ { j } )$ diverges, since then the series for $E ( X )$ diverges or its value depends on the order in which the $x _ { j }$ are listed.

In words, the expected value of X is a weighted average of the possible values that X can take on, weighted by their probabilities. Let’s check that the definition makes sense in a few simple examples:

1. Let X be the result of rolling a fair 6-sided die, so X takes on the values 1, 2, 3, 4, 5, 6, with equal probabilities. Intuitively, we should be able to get the average by adding up these values and dividing by 6. Using the definition, the expected value is

$$
E (X) = \frac {1}{6} (1 + 2 + \dots + 6) = 3. 5,
$$

as we expected. Note that X never equals its mean in this example. This is similar to the fact that the average number of children per household in some country could be 1.8, but that doesn’t mean that a typical household has 1.8 children!

2. Let $X \sim \mathrm { B e r n } ( p )$ and $q = 1 - p .$ Then

$$
E (X) = 1 p + 0 q = p,
$$

which makes sense intuitively since it is between the two possible values of X, compromising between 0 and 1 based on how likely each is. This is illustrated in Figure 4.1 for a case with $p   <   1 / 2 { : }$ two pebbles are being balanced on a seesaw. For the seesaw to balance, the fulcrum (shown as a triangle) must be at $p ,$ which in physics terms is the center of mass.

The frequentist interpretation would be to consider a large number of independent Bernoulli trials, each with probability $p$ of success. Writing 1 for “success” and 0 for “failure”, in the long run we would expect to have data consisting of a list of numbers where the proportion of 1’s is very close to $p .$ The average of a list of 0’s and 1’s is the proportion of 1’s.

3. Let X have 3 distinct possible values, $a _ { 1 } , a _ { 2 } , a _ { 3 }$ , with probabilities $p _ { 1 } , p _ { 2 } , p _ { 3 }$ respectively. Imagine running a simulation where n independent draws

![](images/page_167_image_2.jpg)

<details>
<summary>text_image</summary>

q
0
p
0.5
1
p
</details>

## FIGURE 4.1

Center of mass of two pebbles, depicting that $E ( X ) = p$ for $X \sim \mathrm { B e r n } ( p )$ . Here $q$ and $p$ denote the masses of the two pebbles.

from the distribution of X are generated. For n large, we would expect to have about $p _ { 1 } n \; a _ { 1 }  \mathrm { ' s , } \; p _ { 2 } n \; a _ { 2 }  \mathrm { ' s }$ , and $p _ { 3 } n ~ { a _ { 3 } } ^ { \mathrm { { ' } } } \mathrm { { s } } .$ . (We will look at a more mathematical version of this example when we study the law of large numbers in Chapter 10.) If the simulation results are close to these expected results, then the arithmetic mean of the simulation results is approximately

$$
\frac {p _ {1} n \cdot a _ {1} + p _ {2} n \cdot a _ {2} + p _ {3} n \cdot a _ {3}}{n} = p _ {1} a _ {1} + p _ {2} a _ {2} + p _ {3} a _ {3} = E (X).
$$

Note that $E ( X )$ depends only on the distribution of X. This follows directly from the definition, but is worth recording since it is fundamental.

Proposition 4.1.2. If X and Y are discrete r.v.s with the same distribution, then $E(X) = E(Y)$ (if either side exists).

Proof. In the definition of $E ( X )$ , we only need to know the PMF of $X$ .

The converse of the above proposition is false since the expected value is just a onenumber summary, not nearly enough to specify the entire distribution; it’s a measure of where the “center” is but does not determine, for example, how spread out the distribution is or how likely the r.v. is to be positive. Figure 4.2 shows an example of two different PMFs with the same expected value (balancing point).

h 4.1.3 (Replacing an r.v. by its expectation). For any discrete r.v. X, the expected value $E ( X )$ is a number (if it exists). A common mistake is to replace an r.v. by its expectation without justification, which is wrong both mathematically (X is a function, $E ( X )$ is a constant) and statistically (it ignores the variability of X), except in the degenerate case where X is a constant.

Notation 4.1.4. We often abbreviate $E ( X )$ to EX. Similarly, we often abbreviate $E ( X ^ { 2 } )$ to $E X ^ { 2 }$ , and $E ( X ^ { n } )$ to $E X ^ { n }$

h 4.1.5. Paying attention to the order of operations is crucial when working with expectation. As stated above, $E X ^ { 2 }$ is the expectation of the random variable $X ^ { 2 }$ , not the square of the number EX. Unless the parentheses explicitly indicate otherwise,

![](images/page_168_image_2.jpg)

## FIGURE 4.2

The expected value does not determine the distribution: different PMFs can have the same balancing point.

for the expectation of an r.v. raised to a power, first we take the power and then we take the expectation. For example, $E ( X - 1 ) ^ { 4 }$ is $E\left( (X - 1)^{4} \right)$ , not $(E(X - 1))^4$

## 4.2 Linearity of expectation

The most important property of expectation is linearity: the expected value of a sum of r.v.s is the sum of the individual expected values.

Theorem 4.2.1 (Linearity of expectation). For any r.v.s $X , Y$ and any constant $c _ { \gamma }$

$$
E (X + Y) = E (X) + E (Y),
$$

$$
E (c X) = c E (X).
$$

The second equation says that we can take out constant factors from an expectation; this is both intuitively reasonable and easily verified from the definition. The first equation, $E ( X + Y ) = E ( X ) + E ( Y )$ , also seems reasonable when X and $Y$ are independent. What may be surprising is that it holds even if X and $Y$ are dependent! To build intuition for this, consider the extreme case where X always equals $Y .$ Then $X + Y = 2 X$ , and both sides of $E(X + Y) = E(X) + E(Y)$ are equal to $2 E ( X )$ , so linearity still holds even in the most extreme case of dependence.

Linearity is true for all r.v.s, not just discrete r.v.s, but in this chapter we will prove it only for discrete r.v.s. Before proving linearity, it is worthwhile to recall some basic facts about averages. If we have a list of numbers, say $( 1 , 1 , 1 , 1 , 1 , 3 , 3 , 5 )$ , we can calculate their mean by adding all the values and dividing by the length of the list, so that each element of the list gets a weight of $\frac{1}{8}$ :

$$
\frac {1}{8} (1 + 1 + 1 + 1 + 1 + 3 + 3 + 5) = 2.
$$

But another way to calculate the mean is to group together all the 1’s, all the $\mathbf { 3 ^ { \prime } s } ,$ and all the 5’s, and then take a weighted average, giving appropriate weights to 1’s, $3 ^ { \flat } \mathrm { s } ,$ and 5’s:

$$
\frac {5}{8} \cdot 1 + \frac {2}{8} \cdot 3 + \frac {1}{8} \cdot 5 = 2.
$$

This insight—that averages can be calculated in two ways, ungrouped or grouped— is all that is needed to prove linearity! Recall that X is a function which assigns a real number to every outcome s in the sample space. The r.v. X may assign the same value to multiple sample outcomes. When this happens, our definition of expectation groups all these outcomes together into a super-pebble whose weight, $P ( X   =   x )$ , is the total weight of the constituent pebbles. This grouping process is illustrated in Figure 4.3 for a hypothetical r.v. taking values in $\{ 0 , 1 , 2 \}$ . So our definition of expectation corresponds to the grouped way of taking averages.

![](images/page_169_image_5.jpg)

## FIGURE 4.3

Left: X assigns a number to each pebble in the sample space. Right: Grouping the pebbles by the value that X assigns to them, the 9 pebbles become 3 super-pebbles. The weight of a super-pebble is the sum of the weights of the constituent pebbles.

The advantage of this definition is that it allows us to work with the distribution of X directly, without returning to the sample space. The disadvantage comes when we have to prove theorems like this one, for if we have another r.v. Y on the same sample space, the super-pebbles created by Y are different from those created from X, with different weights $P ( Y = y )$ ; this makes it difficult to combine $\textstyle \sum _ { x } x P ( X = x )$ and $\textstyle \sum _ { y } y P ( Y = y )$

Fortunately, we know there’s another equally valid way to calculate an average: we can take a weighted average of the values of individual pebbles. In other words, if $X ( s )$ is the value that X assigns to pebble s, we can take the weighted average

$$
E (X) = \sum_ {s} X (s) P (\{s \}),
$$

where $P ( \{ s \} )$ is the weight of pebble s. This corresponds to the ungrouped way of taking averages. The advantage of this definition is that it breaks down the sample space into the smallest possible units, so we are now using the same weights $P ( \{ s \} )$ for every random variable defined on this sample space. If Y is another random

variable, then

$$
E (Y) = \sum_ {s} Y (s) P (\{s \}).
$$

We can combine $\textstyle \sum _ { s } X ( s ) P ( \{ s \} )$ and $\textstyle \sum _ { s } Y ( s ) P ( \{ s \} )$ , which gives

$$
E (X) + E (Y) = \sum_ {s} X (s) P (\{s \}) + \sum_ {s} Y (s) P (\{s \}) = \sum_ {s} (X + Y) (s) P (\{s \}) = E (X + Y).
$$

Another intuition for linearity of expectation is via the concept of simulation. If we simulate many, many times from the distribution of $X ,$ the histogram of the simulated values will look very much like the true PMF of $X$ . In particular, the arithmetic mean of the simulated values will be very close to the true value of $E ( X )$ (the precise nature of this convergence is described by the law of large numbers, an important theorem that we will discuss in detail in Chapter 10).

Let X and Y be r.v.s summarizing a certain experiment. Suppose we perform the experiment n times, where n is a very large number, and we write down the values realized by X and $Y$ each time. For each repetition of the experiment, we obtain an X value, a Y value, and (by adding them) an $X + Y$ value. In Figure 4.4, each row represents a repetition of the experiment. The left column contains the draws of X, the middle column contains the draws of $Y ,$ and the right column contains the draws of $X + Y$

There are two ways to calculate the sum of all the numbers in the last column. The straightforward way is just to add all the numbers in that column. But an equally valid way is to add all the numbers in the first column, add all the numbers in the second column, and then add the two column sums.

Dividing by n everywhere, what we’ve argued is that the following procedures are equivalent:

• Taking the arithmetic mean of all the numbers in the last column. By the law of large numbers, this is very close to $E ( X + Y )$
• Taking the arithmetic mean of the first column and the arithmetic mean of the second column, then adding the two column means. By the law of large numbers, this is very close to $E ( X ) + E ( Y )$

Linearity of expectation thus emerges as a simple fact about arithmetic (we’re just adding numbers in two different orders)! Notice that nowhere in our argument did we rely on whether X and $Y$ were independent. In fact, in Figure 4.4, X and $Y$ appear to be dependent: Y tends to be large when X is large, and $Y$ tends to be small when $X$ is small (in the language of Chapter 7, we say that X and Y are positively correlated). But this dependence is irrelevant: shuffling the draws of $Y$ could completely alter the pattern of dependence between X and $Y ,$ but would have no effect on the column sums.

| X | Y | $X + Y$ |
| --- | --- | --- |
| 3 | 4 | 7 |
| 2 | 2 | 4 |
| 6 | 8 | 14 |
| 10 | 23 | 33 |
| 1 | -3 | -2 |
| 1 | 0 | 1 |
| 5 | 9 | 14 |
| 4 | 1 | 5 |
| ⋮ | ⋮ | ⋮ |

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} + \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} + y _ {i})
$$

$$
E (X) + E (Y) = E (X + Y)
$$

## FIGURE 4.4

Intuitive view of linearity of expectation. Each row represents a repetition of the experiment; the three columns are the realized values of $X ,   Y$ , and $X + Y$ , respectively. Adding all the numbers in the last column is equivalent to summing the first column and the second column separately, then adding the two column sums. So the mean of the last column is the sum of the first and second column means; this is linearity of expectation.

Linearity is an extremely handy tool for calculating expected values, often allowing us to bypass the definition of expected value altogether. Let’s use linearity to find the expectations of the Binomial and Hypergeometric distributions.

Example 4.2.2 (Binomial expectation). For $X \sim \mathrm { B i n } ( n , p )$ , let’s find $E ( X )$ in two ways. By definition of expectation,

$$
E (X) = \sum_ {k = 0} ^ {n} k P (X = k) = \sum_ {k = 0} ^ {n} k \binom {n} {k} p ^ {k} q ^ {n - k}.
$$

From Example 1.5.2, we know $\begin{array} { r } { k \binom { n } { k } = n \binom { n - 1 } { k - 1 } } \end{array}$ , so

$$
\begin{array}{l} \sum_ {k = 0} ^ {n} k \binom {n} {k} p ^ {k} q ^ {n - k} = n \sum_ {k = 0} ^ {n} \binom {n - 1} {k - 1} p ^ {k} q ^ {n - k} \\ = n p \sum_ {k = 1} ^ {n} \binom {n - 1} {k - 1} p ^ {k - 1} q ^ {n - k} \\ = n p \sum_ {j = 0} ^ {n - 1} \binom {n - 1} {j} p ^ {j} q ^ {n - 1 - j} \\ = n p. \\ \end{array}
$$

The sum in the penultimate line equals 1 because it is the sum of the $\operatorname { B i n } ( n - 1 , p )$ $\mathrm { P M F }$ (or by the binomial theorem). Therefore, $E ( X ) = n p .$

This proof required us to remember combinatorial identities and manipulate binomial coefficients. Using linearity of expectation, we obtain a much shorter path to the same result. Let’s write X as the sum of n independent $\operatorname { B e r n } ( p )$ r.v.s:

$$
X = I _ {1} + \dots + I _ {n},
$$

where each $I _ { j }$ has expectation $E ( I _ { j } ) = 1 p + 0 q = p$ . By linearity,

$$
E (X) = E (I _ {1}) + \dots + E (I _ {n}) = n p.
$$

Example 4.2.3 (Hypergeometric expectation). Let $X   \sim   \operatorname { H G e o m } ( w , b , n )$ , interpreted as the number of white balls in a sample of size n drawn without replacement from an urn with w white and b black balls. As in the Binomial case, we can write X as a sum of Bernoulli random variables,

$$
X = I _ {1} + \dots + I _ {n},
$$

where $I _ { j }$ equals 1 if the jth ball in the sample is white and 0 otherwise. By symmetry, $I _ { j } \sim \mathrm { B e r n } ( p )$ with $p = w / ( w   +   b )$ , since unconditionally the jth ball drawn is equally likely to be any of the balls.

Unlike in the Binomial case, the $I _ { j }$ are not independent, since the sampling is without replacement: given that a ball in the sample is white, there is a lower chance that another ball in the sample is white. However, linearity still holds for dependent random variables! Thus,

$$
E (X) = n w / (w + b).
$$

As another example of the power of linearity, we can give a quick proof of the intuitive idea that “bigger r.v.s have bigger expectations”.

Proposition 4.2.4 (Monotonicity of expectation). Let X and Y be r.v.s such that $X \geq Y$ with probability 1. Then $E ( X ) \geq E ( Y )$ , with equality holding if and only if $X = Y$ with probability 1.

Proof. This result holds for all r.v.s, but we will prove it only for discrete r.v.s since this chapter focuses on discrete r.v.s. The r.v. $Z   =   X - Y$ is nonnegative (with probability 1), so $E ( Z ) \geq 0$ since $E ( Z )$ is defined as a sum of nonnegative terms. By linearity,

$$
E (X) - E (Y) = E (X - Y) \geq 0,
$$

as desired. If $E(X) = E(Y)$ , then by linearity we also have $E ( Z ) = 0$ , which implies that $P(X = Y) = P(Z = 0) = 1$ since if even one term in the sum defining $E ( Z )$ is positive, then the whole sum is positive. 

## 4.3 Geometric and Negative Binomial

We now introduce two more famous discrete distributions, the Geometric and Negative Binomial, and calculate their expected values.

Story 4.3.1 (Geometric distribution). Consider a sequence of independent Bernoulli trials, each with the same success probability $p \in ( 0 , 1 )$ , with trials performed until a success occurs. Let X be the number of failures before the first successful trial. Then X has the Geometric distribution with parameter $p ;$ we denote this by $X \sim \operatorname { G e o m } ( p )$ 

For example, if we flip a fair coin until it lands Heads for the first time, then the number of Tails before the first occurrence of Heads is distributed as Geom(1/2).

To get the Geometric PMF from the story, imagine the Bernoulli trials as a string of 0’s (failures) ending in a single 1 (success). Each 0 has probability $q = 1 - p$ and the final 1 has probability $p ,$ so a string of k failures followed by one success has probability $q ^ { k } p$

Theorem 4.3.2 (Geometric PMF). If $X \sim \operatorname { G e o m } ( p )$ , then the PMF of X is

$$
P (X = k) = q ^ {k} p
$$

for $k = 0 , 1 , 2 , \ldots ,$ where $q = 1 - p$

This is a valid PMF because, summing a geometric series (see the math appendix for a review of geometric series), we have

$$
\sum_ {k = 0} ^ {\infty} q ^ {k} p = p \sum_ {k = 0} ^ {\infty} q ^ {k} = p \cdot \frac {1}{1 - q} = 1.
$$

Just as the binomial theorem shows that the Binomial PMF is valid, a geometric series shows that the Geometric PMF is valid! A geometric series can also be used to obtain the Geometric CDF.

Theorem 4.3.3 (Geometric CDF). If $X \sim \operatorname { G e o m } ( p )$ , then the CDF of X is

$$
F (x) = \left\{ \begin{array}{l} 1 - q ^ {\lfloor x \rfloor + 1}, \text {if} x \geq 0; \\ 0, \text {if} x <   0, \end{array} \right.
$$

where $q = 1 - p$ and $[ x ]$ is the greatest integer less than or equal to x.

Proof. Let F be the CDF of X. We will find $F ( x )$ first for the case $x < 0$ , then for the case that x is a nonnegative integer, and lastly for the case that x is a nonnegative real number. For $x < 0,   F(x) = 0$ since X can’t be negative. For n a nonnegative integer,

$$
F (n) = \sum_ {k = 0} ^ {n} P (X = k) = p \sum_ {k = 0} ^ {n} q ^ {k} = p \cdot \frac {1 - q ^ {n + 1}}{1 - q} = 1 - q ^ {n + 1}.
$$

We can also get the same result from the fact that the event $X \geq n + 1$ means that the first $n + 1$ trials were failures:

$$
F (n) = 1 - P (X > n) = 1 - P (X \geq n + 1) = 1 - q ^ {n + 1}.
$$

For real $x \geq 0$

$$
F (x) = P (X \leq x) = P (X \leq \lfloor x \rfloor),
$$

since X always takes on integer values. For example,

$$
P (X \leq 3. 7) = P (X \leq 3) + P (3 <   X \leq 3. 7) = P (X \leq 3).
$$

Therefore, F is as claimed.

Figure 4.3 displays the Geom(0.5) PMF and CDF from 0 to 6. All Geometric PMFs have a similar shape; the greater the success probability p, the more quickly the PMF decays to 0.

h 4.3.4 (Conventions for the Geometric). There are differing conventions for the definition of the Geometric distribution; some sources define the Geometric as the total number of trials, including the success. In this book, the Geometric distribution excludes the success, and the First Success distribution includes the success.

![](images/page_175_image_2.jpg)

FIGURE 4.5

Geom(0.5) PMF and CDF.

Definition 4.3.5 (First Success distribution). In a sequence of independent Bernoulli trials with success probability $p ,$ let $Y$ be the number of trials until the first successful trial, including the success. Then $Y$ has the First Success distribution with parameter $p ;$ we denote this by $Y \sim \mathrm { F S } ( p )$

It is easy to convert back and forth between the two but important to be careful about which convention is being used. If $Y \sim \mathrm { F S } ( p )$ then $Y - 1 \sim \mathrm { G e o m } ( p )$ , and we can convert between the PMFs of $Y$ and $Y - 1$ by writing

$$
P (Y = k) = P (Y - 1 = k - 1).
$$

Conversely, if $X \sim \operatorname { G e o m } ( p )$ , then $X + 1 \sim \mathrm { F S } ( p )$

Example 4.3.6 (Geometric expectation). Let $X \sim \operatorname { G e o m } ( p )$ . By definition,

$$
E (X) = \sum_ {k = 0} ^ {\infty} k q ^ {k} p,
$$

where $q = 1 - p$ . This sum looks unpleasant; it’s not a geometric series because of the extra k multiplying each term. But we notice that each term looks similar to $k q ^ { k - 1 }$ , the derivative of $q ^ { k }$ (with respect to $q )$ , so let’s start there:

$$
\sum_ {k = 0} ^ {\infty} q ^ {k} = \frac {1}{1 - q}.
$$

This geometric series converges since $0   <   q   <   1$ . Differentiating both sides with respect to $q ,$ we get

$$
\sum_ {k = 0} ^ {\infty} k q ^ {k - 1} = \frac {1}{(1 - q) ^ {2}}.
$$