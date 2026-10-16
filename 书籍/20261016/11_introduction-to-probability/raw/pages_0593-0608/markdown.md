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

![](images/page_592_chart_7.jpg)

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

![](images/page_596_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

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

## A.1.2 Subsets

If A and B are sets, then we say A is a subset of B (and write $A \subseteq B )$ if every element of A is also an element of B. For example, the set of all integers is a subset of the set of all real numbers. It is always true that $\varnothing$ and A itself are subsets of A; these are the extreme cases for subsets. A general strategy for showing that $A \subseteq B$ is to let x be an arbitrary element of A, and then show that x must also be an element of B. A general strategy for showing that $A = B$ for two sets A and B is to show that each is a subset of the other.

## A.1.3 Unions, intersections, and complements

The union of two sets A and B, written as $A \cup B$ , is the set of all objects that are in A or B (or both). The intersection of A and B, written as $A \cap B$ , is the set of all objects that are in both A and B. We say that A and $B$ are disjoint if ${ \overline { { A } } } \cap B = \emptyset$ For n sets $A _ { 1 } , \ldots , A _ { n }$ , the union $A _ { 1 } \cup A _ { 2 } \cup \cdots \cup A _ { n }$ is the set of all objects that are in at least one of the $A _ { j } { } ^ { \gamma } \mathrm { s } _ { 1 }$ while the intersection $A _ { 1 } \cap A _ { 2 } \cap \cdots \cap A _ { n }$ is the set of all objects that are in all of the $A _ { j } { } ^ { \mathfrak { j } } \mathrm { s }$

In many applications, all the sets we’re working with are subsets of some set $S$ (in probability, this may be the set of all possible outcomes of some experiment). When S is clear from the context, we define the complement of a set A to be the set of all objects in $S$ that are not in $A ;$ this is denoted by $A ^ { c }$

Unions, intersections, and complements can be visualized easily using Venn diagrams, such as the one shown below. The union is the entire shaded region, while the intersection is the football-shaped region of points that are in both A and B. The complement of A is all points in the rectangle that are outside of A.

![](images/page_598_image_8.jpg)

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

This is a form of the inclusion-exclusion theorem from Chapter 1. It says that to count how many elements are in the union of A and B, we can add the separate counts for each, and then adjust for the fact that we have double-counted the elements (if any) that are in both A and B.

Two sets A and B are said to have the same size or same cardinality if they can be put into one-to-one correspondence, i.e., if each element of A can be paired up with exactly one element of $B ,$ with no unpaired elements in either set. We say that A is smaller than B if there is not a one-to-one correspondence between A and B, but there is a one-to-one correspondence between A and some subset of B.

For example, suppose that we want to count the number of people in a movie theater with 100 seats. Assume that no one in the theater is standing, and no seat has more than one person in it. The obvious thing to do is to go around counting people one by one (though it’s surprisingly easy to miss someone or accidentally count someone twice). But if every seat is occupied, then a much easier method is to note that there must be 100 people, since there are 100 seats and there is a one-to-one correspondence between people and seats. If some seats are empty, then there must be fewer than 100 people there.

This idea of looking at one-to-one correspondences makes sense both for finite and for infinite sets. Consider the perfect squares $1 ^ { 2 } , 2 ^ { 2 } , 3 ^ { 2 } , \ldots .$ . Galileo pointed out the paradoxical result that on the one hand it seems like there are fewer perfect squares than positive integers (since every perfect square is a positive integer, but lots of positive integers aren’t perfect squares), but on the other hand it seems like these two sets have the same size since they can be put into one-to-one correspondence: pair $1 ^ { 2 }$ with 1, pair $2 ^ { 2 }$ with 2, pair $3 ^ { 2 }$ with 3, etc.

The resolution of Galileo’s paradox is to realize that intuitions about finite sets don’t necessarily carry over to infinite sets. By definition, the set of all perfect squares and the set of all positive integers do have the same size. Another famous example of this is Hilbert’s hotel. For any hotel in the real world the number of rooms is finite. If every room is occupied, there is no way to accommodate more guests, other than by cramming more people into already occupied rooms.

Now consider an imaginary hotel with an infinite sequence of rooms, numbered 1, 2, 3, . . . . Assume that all the rooms are occupied, and that a weary traveler arrives, looking for a room. Can the hotel give the traveler a room, without leaving any of the current guests without a room? Yes, one way is to have the guest in room n move to room $n + 1$ , for all $n = 1 , 2 , 3 , \ldots$ . This frees up room 1, so the traveler can stay there.

What if infinitely many travelers arrive at the same time, such that their cardinality is the same as that of the positive integers (so we can label the travelers as traveler 1, traveler $2 , \ldots ) ?$ The hotel could fit them in one by one by repeating the above procedure over and over again, but it would take forever (infinitely many moves) to accommodate everyone, and it would be bad for business to make the current guests keep moving over and over again. Can the room assignments be updated just once so that everyone has a room? Yes, one way is to have the guest in room n move to room to 2n for all $n = 1 , 2 , 3 , \ldots$ , and then have traveler n move into room $2 n - 1$ In this way, the current guests occupy all the even-numbered rooms, and the new guests occupy all the odd-numbered rooms.

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

## A.2.3 Even and odd functions

Let $f$ be a function from R to R. We say $f$ is an even function if $f(x) = f(-x)$ for all x, and we say $f$ is an odd function if $-f(x)=f(-x)$ for all x. If neither of these conditions is satisfied, then $f$ is neither even nor odd. Figure A.2 shows the graphs of two even functions and two odd functions.

![](images/page_603_image_4.jpg)

## FIGURE A.2

Even and odd functions. The graphs on the left are even functions: $f ( x ) = x ^ { 2 }$ on the top and $f ( x ) = e ^ { - x ^ { 2 } / 2 }$ on the bottom. The graphs on the right are odd functions: $f ( x ) = x ^ { 3 }$ on the top and $f ( x ) = x e ^ { - x ^ { 2 } / 2 }$ on the bottom.

Even and odd functions have nice symmetry properties. The graph of an even function remains the same if you reflect it about the vertical axis, and the graph of an odd function remains the same if you rotate it 180 degrees around the origin.

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

![](images/page_604_image_11.jpg)

<details>
<summary>text_image</summary>

y = g(x)
</details>

## FIGURE A.3

Graph of a convex function $g .$ We have $g ^ { \prime \prime } ( x ) \geq 0$ . Any line segment connecting two points on the curve lies above the curve. Any tangent line lies below the curve.

A function $g$ is concave ${ \mathrm { i f ~ } } { - g }$ is convex. If $g ^ { \prime \prime }$ exists, then $g$ is concave if and only if $g ^ { \prime \prime } ( x ) \leq 0$ for all $x$ in the domain. For example, $g ( x ) = \log ( x )$ defines a concave function on $( 0 , \infty )$ since $g''(x) = -1/x^2 < 0$ for all $x \in ( 0 , \infty )$

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

A matrix is a rectangular array of numbers, such as ${ \binom { 3 \quad 1 / e } { 2 \pi \quad 1 } } { \mathrm { ~ o r ~ } } { \binom { 1 \quad 1 \quad 0 } { 1 \quad 2 \quad 3 } }$ . We say that the dimensions of a matrix are m by n (also written $m \times n )$ if it has m rows and n columns (so the former example is 2 by 2, while the latter is 2 by 3). The matrix is called square if $m = n$ . If $m = 1$ , we have a row vector ; if $n = 1$ , we have a column vector. We write $A = ( a _ { i j } )$ to indicate that the row $i ,$ column $j$ entry of A is $a _ { i j }$

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