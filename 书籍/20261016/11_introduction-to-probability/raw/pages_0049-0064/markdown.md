same line as the corresponding code; longer comments should be on separate lines. For example, a commented version of the above simulation is:

```r
n <- 100
r <- replicate(10^4,sum(sample(n)==(1:n))) # number of cards
sum(r>=1)/10^4
# shuffle; count matches
# proportion with a match
```

What did you get when you ran the code? We got 0.63, which is quite close to 1 − 1/e.

## Birthday problem calculation and simulation

The following code uses prod (which gives the product of a vector) to calculate the probability of at least one birthday match in a group of 23 people:

```txt
k <- 23
1-prod((365-k+1):365)/365^k
```

Better yet, R has built-in functions, pbirthday and qbirthday, for the birthday problem! pbirthday(k) returns the probability of at least one match if the room has k people. qbirthday(p) returns the number of people needed in order to have probability p of at least one match. For example, pbirthday(23) is 0.507 and qbirthday(0.5) is 23.

We can also find the probability of having at least one triple birthday match, i.e., three people with the same birthday; all we have to do is add coincident=3 to say we’re looking for triple matches. For example, pbirthday(23,coincident=3) returns 0.014, so 23 people give us only a 1.4% chance of a triple birthday match. qbirthday(0.5,coincident=3) returns 88, so we’d need 88 people to have at least a 50% chance of at least one triple birthday match.

To simulate the birthday problem, we can use

```r
b <- sample(1:365,23,replace=TRUE)
tabulate(b)
```

to generate random birthdays for 23 people and then tabulate the counts of how many people were born on each day (the command table(b) creates a prettier table, but is slower). We can run 10<sup>4</sup>repetitions as follows:

```r
r <- replicate(10^4, max(tabulate(sample(1:365,23,replace=TRUE))))
sum(r>=2)/10^4
```

If the probabilities of various days are not all equal, the calculation becomes much more difficult, but the simulation can easily be extended since sample allows us to specify the probability of each day (by default sample assigns equal probabilities, so in the above the probability is 1/365 for each day).

## 1.9 Exercises

Exercises marked with s have detailed solutions at [http://stat110.net](http://stat110.net).

## Counting

1. How many ways are there to permute the letters in the word MISSISSIPPI?

2. (a) How many 7-digit phone numbers are possible, assuming that the first digit can’t be a 0 or a 1?

(b) Re-solve (a), except now assume also that the phone number is not allowed to start with 911 (since this is reserved for emergency use, and it would not be desirable for the system to wait to see whether more digits were going to be dialed after someone has dialed 911).

3. Fred is planning to go out to dinner each night of a certain week, Monday through Friday, with each dinner being at one of his ten favorite restaurants.

(a) How many possibilities are there for Fred’s schedule of dinners for that Monday through Friday, if Fred is not willing to eat at the same restaurant more than once?

(b) How many possibilities are there for Fred’s schedule of dinners for that Monday through Friday, if Fred is willing to eat at the same restaurant more than once, but is not willing to eat at the same place twice in a row (or more)?

4. A round-robin tournament is being held with n tennis players; this means that every player will play against every other player exactly once.

(a) How many possible outcomes are there for the tournament (the outcome lists out who won and who lost for each game)?

(b) How many games are played in total?

5. A knock-out tournament is being held with 2ntennis players. This means that for each round, the winners move on to the next round and the losers are eliminated, until only one person remains. For example, if initially there are $2 ^ { 4 } = 1 6$ players, then there are 8 games in the first round, then the 8 winners move on to round 2, then the 4 winners move on to round 3, then the 2 winners move on to round 4, the winner of which is declared the winner of the tournament. (There are various systems for determining who plays whom within a round, but these do not matter for this problem.)

(a) How many rounds are there?
(b) Count how many games in total are played, by adding up the numbers of games played in each round.
(c) Count how many games in total are played, this time by directly thinking about it without doing almost any calculation.

Hint: How many players need to be eliminated?

6. There are 20 people at a chess club on a certain day. They each find opponents and start playing. How many possibilities are there for how they are matched up, assuming that in each game it does matter who has the white pieces (in a chess game, one player has the white pieces and the other player has the black pieces)?

7. Two chess players, A and B, are going to play 7 games. Each game has three possible outcomes: a win for A (which is a loss for B), a draw (tie), and a loss for A (which is a win for B). A win is worth 1 point, a draw is worth 0.5 points, and a loss is worth 0 points.

(a) How many possible outcomes for the individual games are there, such that overall player A ends up with 3 wins, 2 draws, and 2 losses?
(b) How many possible outcomes for the individual games are there, such that A ends up with 4 points and B ends up with 3 points?
(c) Now assume that they are playing a best-of-7 match, where the match will end when either player has 4 points or when 7 games have been played, whichever is first. For example, if after 6 games the score is 4 to 2 in favor of A, then A wins the match and they don’t play a 7th game. How many possible outcomes for the individual games are there, such that the match lasts for 7 games and A wins by a score of 4 to 3?

8. s (a) How many ways are there to split a dozen people into 3 teams, where one team has 2 people, and the other two teams have 5 people each?

(b) How many ways are there to split a dozen people into 3 teams, where each team has 4 people?

9. s (a) How many paths are there from the point (0, 0) to the point (110, 111) in the plane such that each step either consists of going one unit up or one unit to the right?

(b) How many paths are there from (0, 0) to (210, 211), where each step consists of going one unit up or one unit to the right, and the path has to go through (110, 111)?

10. To fulfill the requirements for a certain degree, a student can choose to take any 7 out of a list of 20 courses, with the constraint that at least 1 of the 7 courses must be a statistics course. Suppose that 5 of the 20 courses are statistics courses.

(a) How many choices are there for which 7 courses to take?
(b) Explain intuitively why the answer to (a) is not ${ \binom { 5 } { 1 } }   \cdot   { \binom { 1 9 } { 6 } }$

11. Let A and B be sets with $|A| = n, |B| = m.$

(a) How many functions are there from A to B (i.e., functions with domain A, assigning an element of B to each element of A)?
(b) How many one-to-one functions are there from A to B? (See Section A.2.1 of the math appendix for information about one-to-one functions.)

12. Four players, named A, B, C, and D, are playing a card game. A standard, well-shuffled deck of cards is dealt to the players (so each player receives a 13-card hand).

(a) How many possibilities are there for the hand that player A will get? (Within a hand, the order in which cards were received doesn’t matter.)
(b) How many possibilities are there overall for what hands everyone will get, assuming that it matters which player gets which hand, but not the order of cards within a hand?
(c) Explain intuitively why the answer to Part (b) is not the fourth power of the answer to Part (a).

13. A certain casino uses 10 standard decks of cards mixed together into one big deck, which we will call a superdeck. Thus, the superdeck has 52 · 10 = 520 cards, with 10 copies of each card. How many different 10-card hands can be dealt from the superdeck? The order of the cards does not matter, nor does it matter which of the original 10 decks the cards came from. Express your answer as a binomial coefficient.

Hint: Bose-Einstein.

14. You are ordering two pizzas. A pizza can be small, medium, large, or extra large, with any combination of 8 possible toppings (getting no toppings is allowed, as is getting all 8). How many possibilities are there for your two pizzas?

## Story proofs

15. s Give a story proof that $\begin{array} { r } { \sum _ { k = 0 } ^ { n } \binom { n } { k } = 2 ^ { n } } \end{array}$

16. s Show that for all positive integers n and k with $n \geq k .$

$$
\binom{n}{k} + \binom{n}{k - 1} = \binom{n + 1}{k},
$$

doing this in two ways: (a) algebraically and (b) with a story, giving an interpretation for why both sides count the same thing.

Hint for the story proof: Imagine an organization consisting of $n + 1$ people, with one of them pre-designated as the president of the organization.

17. Give a story proof that

$$
\sum_ {k = 0} ^ {n} \binom{n}{k} ^ {2} = \binom{2 n}{n},
$$

for all positive integers n.

18. Give a story proof that

$$
\sum_ {k = 1} ^ {n} k \binom{n}{k} ^ {2} = n \binom{2 n - 1}{n - 1},
$$

for all positive integers n.

Hint: Consider choosing a committee of size n from two groups of size n each, where only one of the two groups has people eligible to become the chair of the committee.

19. Give a story proof that

$$
\sum_ {k = 2} ^ {n} \binom{k}{2} \binom{n - k + 2}{2} = \binom{n + 3}{5},
$$

for all integers $n \geq 2 .$

Hint: Consider the middle number in a subset of $\{ 1 , 2 , \ldots , n + 3 \}$ of size 5.

20. s (a) Show using a story proof that

$$
\binom{k}{k} + \binom{k + 1}{k} + \binom{k + 2}{k} + \dots + \binom{n}{k} = \binom{n + 1}{k + 1},
$$

where n and k are positive integers with $n \geq k$ . This is called the hockey stick identity. Hint: Imagine arranging a group of people by age, and then think about the oldest person in a chosen subgroup.

(b) Suppose that a large pack of Haribo gummi bears can have anywhere between 30 and 50 gummi bears. There are 5 delicious flavors: pineapple (clear), raspberry (red), orange (orange), strawberry (green, mysteriously), and lemon (yellow). There are 0 non-delicious flavors. How many possibilities are there for the composition of such a pack of gummi bears? You can leave your answer in terms of a couple binomial coefficients, but not a sum of lots of binomial coefficients.

21. Define $\left\{ { n \atop k } \right\}$ as the number of ways to partition $\{ 1 , 2 , \ldots , n \}$ into k nonempty subsets, or the number of ways to have n students split up into k groups such that each group has at least one student. For example, $\bar { \{ _ { 2 } \} } = 7$ because we have the following possibilities.

• {1}, {2, 3, 4} • {1, 2}, {3, 4}
• {2}, {1, 3, 4}
• {3}, {1, 2, 4}
• {4}, {1, 2, 3}
• {1, 3}, {2, 4}
• {1, 4}, {2, 3}

Prove the following identities:

(a)

$$
\left\{ \begin{array}{c} n + 1 \\ k \end{array} \right\} = \left\{ \begin{array}{c} n \\ k - 1 \end{array} \right\} + k \left\{ \begin{array}{c} n \\ k \end{array} \right\}.
$$

Hint: I’m either in a group by myself or I’m not.

(b)

$$
\sum_ {j = k} ^ {n} \binom {n} {j} \left\{ \begin{array}{c} j \\ k \end{array} \right\} = \left\{ \begin{array}{c} n + 1 \\ k + 1 \end{array} \right\}.
$$

Hint: First decide how many people are not going to be in my group.

22. The Dutch mathematician R.J. Stroeker remarked:

Every beginning student of number theory surely must have marveled at the miraculous fact that for each natural number n the sum of the first n positive consecutive cubes is a perfect square. [26]

Furthermore, it is the square of the sum of the first n positive integers! That is,

$$
1 ^ {3} + 2 ^ {3} + \dots + n ^ {3} = (1 + 2 + \dots + n) ^ {2}.
$$

Usually this identity is proven by induction, but that does not give much insight into why the result is true, nor does it help much if we wanted to compute the left-hand side but didn’t already know this result. In this problem, you will give a story proof of the identity.

(a) Give a story proof of the identity

$$
1 + 2 + \dots + n = \binom{n + 1}{2}.
$$

Hint: Consider a round-robin tournament (see Exercise 4).

(b) Give a story proof of the identity

$$
1 ^ {3} + 2 ^ {3} + \dots + n ^ {3} = 6 \binom{n + 1}{4} + 6 \binom{n + 1}{3} + \binom{n + 1}{2}.
$$

It is then just basic algebra (not required for this problem) to check that the square of the right-hand side in (a) is the right-hand side in (b).

Hint: Imagine choosing a number between 1 and n and then choosing 3 numbers between 0 and n smaller than the original number, with replacement. Then consider cases based on how many distinct numbers were chosen.

## Naive definition of probability

23. Three people get into an empty elevator at the first floor of a building that has 10 floors. Each presses the button for their desired floor (unless one of the others has already pressed that button). Assume that they are equally likely to want to go to floors 2 through 10 (independently of each other). What is the probability that the buttons for 3 consecutive floors are pressed?

24. s A certain family has 6 children, consisting of 3 boys and 3 girls. Assuming that all birth orders are equally likely, what is the probability that the 3 eldest children are the 3 girls?

25. s A city with 6 districts has 6 robberies in a particular week. Assume the robberies are located randomly, with all possibilities for which robbery occurred where equally likely. What is the probability that some district had more than 1 robbery?

26. A survey is being conducted in a city with 1 million residents. It would be far too expensive to survey all of the residents, so a random sample of size 1000 is chosen (in practice, there are many challenges with sampling, such as obtaining a complete list of everyone in the city, and dealing with people who refuse to participate). The survey is conducted by choosing people one at a time, with replacement and with equal probabilities.

(a) Explain how sampling with vs. without replacement here relates to the birthday problem.
(b) Find the probability that at least one person will get chosen more than once.

27. A hash table is a commonly used data structure in computer science, allowing for fast information retrieval. For example, suppose we want to store some people’s phone numbers. Assume that no two of the people have the same name. For each name x, a hash function h is used, letting h(x) be the location that will be used to store x’s phone number. After such a table has been computed, to look up x’s phone number one just recomputes h(x) and then looks up what is stored in that location.

The hash function h is deterministic, since we don’t want to get different results every time we compute h(x). But h is often chosen to be pseudorandom. For this problem, assume that true randomness is used. Let there be k people, with each person’s phone number stored in a random location (with equal probabilities for each location, independently of where the other people’s numbers are stored), represented by an integer between 1 and n. Find the probability that at least one location has more than one phone number stored there.

28. s A college has 10 time slots for its courses, and blithely assigns courses to completely random time slots, independently. The college offers exactly 3 statistics courses. What is the probability that 2 or more of the statistics courses are in the same time slot?

29. s For each part, decide whether the blank should be filled in with =, <, or >, and give a clear explanation.

(a) (probability that the total after rolling 4 fair dice is 21) (probability that the total after rolling 4 fair dice is 22)
(b) (probability that a random 2-letter word is a palindrome<sup>3</sup>) (probability that a random 3-letter word is a palindrome)

30. With definitions as in the previous problem, find the probability that a random n-letter word is a palindrome for n = 7 and for n = 8.

31. s Elk dwell in a certain forest. There are N elk, of which a simple random sample of size n are captured and tagged (“simple random sample” means that all  Nn sets of n elk are equally likely). The captured elk are returned to the population, and then a new sample is drawn, this time with size m. This is an important method that is widely used in ecology, known as capture-recapture. What is the probability that exactly k of the m elk in the new sample were previously tagged? (Assume that an elk that was captured before doesn’t become more or less likely to be captured again.)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3<sub>A</sub> palindrome is an expression such as “A man, a plan, a canal: Panama” that reads the same backwards as forwards (ignoring spaces, capitalization, and punctuation). Assume for this problem that all words of the specified length are equally likely, that there are no spaces or punctuation, and that the alphabet consists of the lowercase letters a, b, . . . , z. A word is any string of letters from the alphabet; it does not need to be a word that has a meaning in the English language.</span></small>

32. Four cards are face down on a table. You are told that two are red and two are black, and you need to guess which two are red and which two are black. You do this by pointing to the two cards you’re guessing are red (and then implicitly you’re guessing that the other two are black). Assume that all configurations are equally likely, and that you do not have psychic powers. Find the probability that exactly j of your guesses are correct, for j = 0, 1, 2, 3, 4.

33. s A jar contains r red balls and g green balls, where r and g are fixed positive integers. A ball is drawn from the jar randomly (with all possibilities equally likely), and then a second ball is drawn randomly.

(a) Explain intuitively why the probability of the second ball being green is the same as the probability of the first ball being green.
(b) Define notation for the sample space of the problem, and use this to compute the probabilities from (a) and show that they are the same.
(c) Suppose that there are 16 balls in total, and that the probability that the two balls are the same color is the same as the probability that they are different colors. What are r and g (list all possibilities)?

34. s A random 5-card poker hand is dealt from a standard deck of cards. Find the probability of each of the following possibilities (in terms of binomial coefficients).

(a) A flush (all 5 cards being of the same suit; do not count a royal flush, which is a flush with an ace, king, queen, jack, and 10).
(b) Two pair (e.g., two 3’s, two 7’s, and an ace).

35. A random 13-card hand is dealt from a standard deck of cards. What is the probability that the hand contains at least 3 cards of every suit?

36. A group of 30 dice are thrown. What is the probability that 5 of each of the values 1, 2, 3, 4, 5, 6 appear?

37. A deck of cards is shuffled well. The cards are dealt one by one, until the first time an ace appears.

(a) Find the probability that no kings, queens, or jacks appear before the first ace.
(b) Find the probability that exactly one king, exactly one queen, and exactly one jack appear (in any order) before the first ace.

38. Tyrion, Cersei, and ten other people are sitting at a round table, with their seating arrangement having been randomly assigned. What is the probability that Tyrion and Cersei are sitting next to each other? Find this in two ways:

(a) using a sample space of size 12!, where an outcome is fully detailed about the seating;
(b) using a much smaller sample space, which focuses on Tyrion and Cersei.

39. An organization with 2n people consists of n married couples. A committee of size k is selected, with all possibilities equally likely. Find the probability that there are exactly j married couples within the committee.

40. There are n balls in a jar, labeled with the numbers 1, 2, . . . , n. A total of k balls are drawn, one by one with replacement, to obtain a sequence of numbers.

(a) What is the probability that the sequence obtained is strictly increasing?
(b) What is the probability that the sequence obtained is increasing (but not necessarily strictly increasing, i.e., there can be repetitions)?

41. Each of n balls is independently placed into one of n boxes, with all boxes equally likely. What is the probability that exactly one box is empty?

42. s A norepeatword is a sequence of at least one (and possibly all) of the usual 26 letters $\mathrm { a , } \mathrm { b , } \mathrm { c , } \mathrm { \ldots , } \mathrm { z , }$ with repetitions not allowed. For example, “course” is a norepeatword, but “statistics” is not. Order matters, e.g., “course” is not the same as “source”.

A norepeatword is chosen randomly, with all norepeatwords equally likely. Show that the probability that it uses all 26 letters is very close to $1 / e .$

## Axioms of probability

43. Show that for any events A and $B ,$

$$
P (A) + P (B) - 1 \leq P (A \cap B) \leq P (A \cup B) \leq P (A) + P (B).
$$

For each of these three inequalities, give a simple criterion for when the inequality is actually an equality (e.g., give a simple condition such that $P(A \cap B) = P(A \cup B)$ if and only if the condition holds).

44. Let A and B be events. The difference $B - A$ is defined to be the set of all elements of B that are not in A. Show that if $A \subseteq B$ , then

$$
P (B - A) = P (B) - P (A),
$$

directly using the axioms of probability.

45. Let A and B be events. The symmetric difference $A \triangle B$ is defined to be the set of all elements that are in A or B but not both. In logic and engineering, this event is also called the XOR (exclusive or ) of A and B. Show that

$$
P (A \triangle B) = P (A) + P (B) - 2 P (A \cap B),
$$

directly using the axioms of probability.

46. Let $A _ { 1 } , A _ { 2 } , \ldots , A _ { n }$ be events. Let $B _ { k }$ be the event exactly k of the $A _ { i }$ occur, and $C _ { k }$ be the event that at least k of the A<sub>i</sub> occur, for $0 \leq k \leq n$ . Find a simple expression for $P ( B _ { k } )$ in terms of $P ( C _ { k } )$ and $P ( C _ { k + 1 } )$

47. Events A and B are independent if $P(A \cap B) = P(A)P(B)$ (independence is explored in detail in the next chapter).

(a) Give an example of independent events A and B in a finite sample space S (with neither equal to ∅ or S), and illustrate it with a Pebble World diagram.

(b) Consider the experiment of picking a random point in the rectangle

$$
R = \{(x, y): 0 <   x <   1, 0 <   y <   1 \},
$$

where the probability of the point being in any particular region contained within R is the area of that region. Let $A _ { 1 }$ and $B _ { 1 }$ be rectangles contained within $R ,$ with areas not equal to 0 or 1. Let A be the event that the random point is in $A _ { 1 }$ , and B be the event that the random point is in $B _ { 1 }$ . Give a geometric description of when it is true that A and B are independent. Also, give an example where they are independent and another example where they are not independent.

(c) Show that if A and B are independent, then

$$
P (A \cup B) = P (A) + P (B) - P (A) P (B) = 1 - P (A ^ {c}) P (B ^ {c}).
$$

48. s Arby has a belief system assigning a number $P _ { \mathrm { A r b y } } ( A )$ between 0 and 1 to every event A (for some sample space). This represents Arby’s degree of belief about how likely A is to occur. For any event A, Arby is willing to pay a price of $1 0 0 0 \cdot P _ { \operatorname { A r b y } } ( A )$ dollars to buy a certificate such as the one shown below:

## Certificate

The owner of this certificate can redeem it for \$1000 if A occurs. No value if A does not occur, except as required by federal, state, or local law. No expiration date.

Likewise, Arby is willing to sell such a certificate at the same price. Indeed, Arby is willing to buy or sell any number of certificates at this price, as Arby considers it the “fair” price.

Arby stubbornly refuses to accept the axioms of probability. In particular, suppose that there are two disjoint events A and B with

$$
P _ {\mathrm{Arby}} (A \cup B) \neq P _ {\mathrm{Arby}} (A) + P _ {\mathrm{Arby}} (B).
$$

Show how to make Arby go bankrupt, by giving a list of transactions Arby is willing to make that will guarantee that Arby will lose money (you can assume it will be known whether A occurred and whether B occurred the day after any certificates are bought/sold).

## Inclusion-exclusion

49. A fair die is rolled n times. What is the probability that at least 1 of the 6 values never appears?

50. s A card player is dealt a 13-card hand from a well-shuffled, standard deck of cards. What is the probability that the hand is void in at least one suit (“void in a suit” means having no cards of that suit)?

51. s For a group of 7 people, find the probability that all 4 seasons (winter, spring, summer, fall) occur at least once each among their birthdays, assuming that all seasons are equally likely.

52. A certain class has 20 students, and meets on Mondays and Wednesdays in a classroom with exactly 20 seats. In a certain week, everyone in the class attends both days. On both days, the students choose their seats completely randomly (with one student per seat). Find the probability that no one sits in the same seat on both days of that week.

53. Fred needs to choose a password for a certain website. Assume that he will choose an 8-character password, and that the legal characters are the lowercase letters $\mathrm { a ,   b ,   c ,   \ldots , }$ $\mathbf { Z } _ { \gamma }$ the uppercase letters $\mathrm { A ,   B ,   C ,   \ldots ,   Z , }$ and the numbers $0 ,   1 ,   \ldots ,   9 .$

(a) How many possibilities are there if he is required to have at least one lowercase letter in his password?
(b) How many possibilities are there if he is required to have at least one lowercase letter and at least one uppercase letter in his password?
(c) How many possibilities are there if he is required to have at least one lowercase letter, at least one uppercase letter, and at least one number in his password?

54. s Alice attends a small college in which each class meets only once a week. She is deciding between 30 non-overlapping classes. There are 6 classes to choose from for each day of the week, Monday through Friday. Trusting in the benevolence of randomness, Alice decides to register for 7 randomly selected classes out of the 30, with all choices equally likely. What is the probability that she will have classes every day, Monday through Friday? (This problem can be done either directly using the naive definition of probability, or using inclusion-exclusion.)

55. A club consists of 10 seniors, 12 juniors, and 15 sophomores. An organizing committee of size 5 is chosen randomly (with all subsets of size 5 equally likely).

(a) Find the probability that there are exactly 3 sophomores in the committee.
(b) Find the probability that the committee has at least one representative from each of the senior, junior, and sophomore classes.

## Mixed practice

56. For each part, decide whether the blank should be filled in with =, <, or >, and give a clear explanation. In (a) and (b), order doesn’t matter.

(a) (number of ways to choose 5 people out of 10) (number of ways to choose 6 people out of 10)
(b) (number of ways to break 10 people into 2 teams of 5) (number of ways to break 10 people into a team of 6 and a team of 4)
(c) (probability that all 3 people in a group of 3 were born on January 1) (probability that in a group of 3 people, 1 was born on each of January 1, 2, and 3)

Martin and Gale play an exciting game of “toss the coin”, where they toss a fair coin until the pattern HH occurs (two consecutive Heads) or the pattern T H occurs (Tails followed immediately by Heads). Martin wins the game if and only if HH occurs before T H occurs.

(d) (probability that Martin wins) 1/2

57. Take a deep breath before attempting this problem. In the book Innumeracy [20], John Allen Paulos writes:

Now for better news of a kind of immortal persistence. First, take a deep breath. Assume Shakespeare’s account is accurate and Julius Caesar gasped [“Et tu, Brute!”] before breathing his last. What are the chances you just inhaled a molecule which Caesar exhaled in his dying breath?

Assume that one breath of air contains 10<sup>22</sup> molecules, and that there are 10<sup>44</sup> molecules in the atmosphere. (These are slightly simpler numbers than the estimates that Paulos gives; for the purposes of this problem, assume that these are exact. Of course, in reality there are many complications such as different types of molecules in the atmosphere, chemical reactions, variation in lung capacities, etc.)

Suppose that the molecules in the atmosphere now are the same as those in the atmosphere when Caesar was alive, and that in the 2000 years or so since Caesar, these molecules have been scattered completely randomly through the atmosphere. Also assume that Caesar’s last breath was sampled without replacement but that your breathing is sampled with replacement (without replacement makes more sense but with replacement is easier to work with, and is a good approximation since the number of molecules in the atmosphere is so much larger than the number of molecules in one breath).

Find the probability that at least one molecule in the breath you just took was shared with Caesar’s last breath, and give a simple approximation in terms of e.

Hint: As discussed in the math appendix, $\begin{array} { r } { ( 1 + \frac { x } { n } ) ^ { n } \approx e ^ { x } } \end{array}$ for n large.

58. A widget inspector inspects 12 widgets and finds that exactly 3 are defective. Unfortunately, the widgets then get all mixed up and the inspector has to find the 3 defective widgets again by testing widgets one by one.

(a) Find the probability that the inspector will now have to test at least 9 widgets.
(b) Find the probability that the inspector will now have to test at least 10 widgets.

59. There are 15 chocolate bars and 10 children. In how many ways can the chocolate bars be distributed to the children, in each of the following scenarios?

(a) The chocolate bars are fungible (interchangeable).
(b) The chocolate bars are fungible, and each child must receive at least one.
Hint: First give each child a chocolate bar, and then decide what to do with the rest.
(c) The chocolate bars are not fungible (it matters which particular bar goes where).
(d) The chocolate bars are not fungible, and each child must receive at least one.

Hint: The strategy suggested in (b) does not apply. Instead, consider randomly giving the chocolate bars to the children, and apply inclusion-exclusion.

60. Given $n \geq 2$ numbers $( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ with no repetitions, a bootstrap sample is a sequence $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ formed from the $a _ { j } { } ^ { \flat } \mathbf { s }$ by sampling with replacement with equal probabilities. Bootstrap samples arise in a widely used statistical method known as the bootstrap. For example, if $n = 2$ and $( a _ { 1 } , a _ { 2 } ) = ( 3 , 1 )$ , then the possible bootstrap samples are $( 3 , 3 ) , ( 3 , 1 ) , ( 1 , 3 )$ , and (1, 1).

(a) How many possible bootstrap samples are there for $( a _ { 1 } , \ldots , a _ { n } ) ?$
(b) How many possible bootstrap samples are there for $( a _ { 1 } , \ldots , a _ { n } )$ , if order does not matter (in the sense that it only matters how many times each $a _ { j }$ was chosen, not the order in which they were chosen)?
(c) One random bootstrap sample is chosen (by sampling from $a _ { 1 } , \ldots , a _ { n }$ with replacement, as described above). Show that not all unordered bootstrap samples (in the sense of (b)) are equally likely. Find an unordered bootstrap sample $\mathbf { b } _ { 1 }$ that is as likely as possible, and an unordered bootstrap sample $\mathbf { b } _ { 2 }$ that is as unlikely as possible. Let $p _ { 1 }$ be the probability of getting $\mathbf { b } _ { 1 }$ and $p _ { 2 }$ be the probability of getting $\mathbf { b } _ { 2 }$ (so $p _ { i }$ is the probability of getting the specific unordered bootstrap sample $\mathbf { b } _ { i } )$ . What is $p _ { 1 } / p _ { 2 } ?$ What is the ratio of the probability of getting an unordered bootstrap sample whose probability is $p _ { 1 }$ to the probability of getting an unordered sample whose probability is $p _ { 2 } ?$

61. s There are 100 passengers lined up to board an airplane with 100 seats (with each seat assigned to one of the passengers). The first passenger in line crazily decides to sit in a randomly chosen seat (with all seats equally likely). Each subsequent passenger takes their assigned seat if available, and otherwise sits in a random available seat. What is the probability that the last passenger in line gets to sit in their assigned seat? (This is a common interview problem, and a beautiful example of the power of symmetry.)

Hint: Call the seat assigned to the jth passenger in line “seat $j ^ { \prime \prime }$ (regardless of whether the airline calls it seat 23A or whatever). What are the possibilities for which seats are available to the last passenger in line, and what is the probability of each of these possibilities?

62. In the birthday problem, we assumed that all 365 days of the year are equally likely (and excluded February 29). In reality, some days are slightly more likely as birthdays than others. For example, scientists have long struggled to understand why more babies are born $9$ months after a holiday. Let $\mathbf { p } = ( p _ { 1 } , p _ { 2 } , \ldots , p _ { 3 6 5 } )$ be the vector of birthday probabilities, with $p _ { j }$ the probability of being born on the jth day of the year (February 29 is still excluded, with no offense intended to Leap Dayers).

The kth elementary symmetric polynomial in the variables $x _ { 1 } , \ldots , x _ { n }$ is defined by

$$
e _ {k} (x _ {1}, \dots , x _ {n}) = \sum_ {1 \leq j _ {1} <   j _ {2} <   \dots <   j _ {k} \leq n} x _ {j _ {1}} \dots x _ {j _ {k}}.
$$

This just says to add up all of the $\left( \begin{matrix} { n } \\ { k } \\ \end{matrix} \right)$ terms we can get by choosing and multiplying k of the variables. For example, e1 $( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } + x _ { 2 } + x _ { 3 } , \quad e _ { 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } x _ { 2 } +$ x1x3 + x2x3, and $e _ { 3 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = x _ { 1 } x _ { 2 } x _ { 3 }$

Now let $k \geq 2$ be the number of people.

(a) Find a simple expression for the probability that there is at least one birthday match, in terms of $\mathbf { p }$ and an elementary symmetric polynomial.

(b) Explain intuitively why it makes sense that $P ( \mathrm { a t }$ least one birthday match) is minimized when $\begin{array} { r } { p _ { j } = \frac { 1 } { 3 6 5 } } \end{array}$ for all $j ,$ by considering simple and extreme cases.

(c) The famous arithmetic mean-geometric mean inequality says that for $x , y \geq 0$

$$
\frac {x + y}{2} \geq \sqrt {x y}.
$$

This inequality follows from adding 4xy to both sides of $x^{2}-2xy+y^{2}=(x-y)^{2}\geq0$ Define $\mathbf { r } = ( r _ { 1 } , \ldots , r _ { 3 6 5 } )$ by $r _ { 1 } = r _ { 2 } = ( p _ { 1 } + p _ { 2 } ) / 2 ,   r _ { j } = p _ { j }$ for $3 \leq j \leq 3 6 5$ . Using the arithmetic mean-geometric mean bound and the fact, which you should verify, that

$$
e _ {k} (x _ {1}, \dots , x _ {n}) = x _ {1} x _ {2} e _ {k - 2} (x _ {3}, \dots , x _ {n}) + (x _ {1} + x _ {2}) e _ {k - 1} (x _ {3}, \dots , x _ {n}) + e _ {k} (x _ {3}, \dots , x _ {n}),
$$

show that

with strict inequality if $\mathbf { p } \neq \mathbf { r } ,$ where the “given $\mathbf { r } ^ { 9 9 }$ notation means that the birthday probabilities are given by r. Using this, show that the value of $\mathbf { p }$ that minimizes the probability of at least one birthday match is given by $\begin{array} { r } { p _ { j } = \frac { 1 } { 3 6 5 } } \end{array}$ for all $j .$

![](images/page_60_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

## Conditional probability

We have introduced probability as a language for expressing our degrees of belief or uncertainties about events. Whenever we observe new evidence (i.e., obtain data), we acquire information that may affect our uncertainties. A new observation that is consistent with an existing belief could make us more sure of that belief, while a surprising observation could throw that belief into question. Conditional probability is the concept that addresses this fundamental question: how should we update our beliefs in light of the evidence we observe?

## 2.1 The importance of thinking conditionally

Conditional probability is essential for scientific, medical, and legal reasoning, since it shows how to incorporate evidence into our understanding of the world in a logical, coherent manner. In fact, a useful perspective is that all probabilities are conditional; whether or not it’s written explicitly, there is always background knowledge (or assumptions) built into every probability.

Suppose, for example, that one morning we are interested in the event R that it will rain that day. Let $P ( R )$ be our assessment of the probability of rain before looking outside. If we then look outside and see ominous clouds in the sky, then presumably our probability of rain should increase; we denote this new probability by $P ( R | C )$ (read as “probability of R given $C ^ { \prime \prime } )$ , where C is the event of there being ominous clouds. When we go from $P ( R )$ to $P ( R | C )$ , we say that we are “conditioning on $C ^ { \flat \flat }$ . As the day progresses, we may obtain more and more information about the weather conditions, and we can continually update our probabilities. If we observe that events $B _ { 1 } , \ldots , B _ { n }$ occurred, then we write our new conditional probability of rain given this evidence as $P ( R | B _ { 1 } , \ldots , B _ { n } )$ . If eventually we observe that it does start raining, our conditional probability becomes 1.

Furthermore, we will see that conditioning is a very powerful problem-solving strategy, often making it possible to solve a complicated problem by decomposing it into manageable pieces with case-by-case reasoning. Just as in computer science a common strategy is to break a large problem up into bite-size pieces (or even byte-size pieces), in probability a common strategy is to reduce a complicated probability problem to a bunch of simpler conditional probability problems. In particular, we will discuss a strategy known as first-step analysis, which often allows us to obtain recursive solutions to problems where the experiment has multiple stages.

Due to the central importance of conditioning, both as the means by which we update beliefs to reflect evidence and as a problem-solving strategy, we say that

Conditioning is the soul of statistics.

## 2.2 Definition and intuition

Definition 2.2.1 (Conditional probability). If A and B are events with $P ( B ) > 0 ,$ then the conditional probability of A given B, denoted by $P ( A | B )$ , is defined as

$$
P (A | B) = \frac {P (A \cap B)}{P (B)}.
$$

Here A is the event whose uncertainty we want to update, and B is the evidence we observe (or want to treat as given). We call $P ( A )$ the prior probability of A and $P ( A | B )$ the posterior probability of A (“prior” means before updating based on the evidence, and “posterior” means after updating based on the evidence).

It is important to interpret the event appearing after the vertical conditioning bar as the evidence that we have observed or that is being conditioned on: $P ( A | B )$ is the probability of A given the evidence B, not the probability of some entity called $A | B$ . As discussed in h 2.4.1, there is no such event as $A | B$

For any event A, $P(A|A) \; = \; P(A \cap A)/P(A) \; = \; 1$ . Upon observing that A has occurred, our updated probability for A is 1. If this weren’t the case, we would demand a new definition of conditional probability!

Example 2.2.2 (Two cards). A standard deck of cards is shuffled well. Two cards are drawn randomly, one at a time without replacement. Let A be the event that the first card is a heart, and B be the event that the second card is red. Find $P ( A | B )$ and $P ( B | A )$

Solution:

By the naive definition of probability and the multiplication rule,

$$
P (A \cap B) = \frac {1 3 \cdot 2 5}{5 2 \cdot 5 1} = \frac {2 5}{2 0 4},
$$

since a favorable outcome is determined by choosing any of the 13 hearts and then any of the remaining 25 red cards. Also, $P ( A ) = 1 / 4$ since the 4 suits are equally likely, and

$$
P (B) = \frac {2 6 \cdot 5 1}{5 2 \cdot 5 1} = \frac {1}{2}
$$

since there are 26 favorable possibilities for the second card, and for each of those, the first card can be any other card (recall from Chapter 1 that chronological order is not needed in the multiplication rule).

A neater way to see that $P ( B ) = 1 / 2$ is by symmetry: from a vantage point before having done the experiment, the second card is equally likely to be any card in the deck.

We now have all the pieces needed to apply the definition of conditional probability:

$$
P (A | B) = \frac {P (A \cap B)}{P (B)} = \frac {2 5 / 2 0 4}{1 / 2} = \frac {2 5}{1 0 2},
$$

$$
P (B | A) = \frac {P (B \cap A)}{P (A)} = \frac {2 5 / 2 0 4}{1 / 4} = \frac {2 5}{5 1}.
$$

This is a simple example, but already there are several things worth noting.

1. It’s extremely important to be careful about which events to put on which side of the conditioning bar. In particular, $P ( A | B ) \neq P ( B | A )$ . The next section explores how $P ( A | B )$ and $P ( B | A )$ are related in general. Confusing these two quantities is called the prosecutor’s fallacy and is discussed in Section 2.8. If instead we had defined B to be the event that the second card is a heart, then the two conditional probabilities would have been equal.

2. Both $P ( A | B )$ and $P ( B | A )$ make sense (intuitively and mathematically); the chronological order in which cards were chosen does not dictate which conditional probabilities we can look at. When we calculate conditional probabilities, we are considering what information observing one event provides about another event, not whether one event causes another. For further intuition, imagine that someone spreads out the cards and draws one card with their left hand and another card with their right hand, at the same time. Defining A and B based on the left hand’s card and the right hand’s card rather than the first card and second card would not change the structure of the problem in any important way.

3. We can also see that $P ( B | A ) = 2 5 / 5 1$ by a direct interpretation of what conditional probability means: if the first card drawn is a heart, then the remaining cards consist of 25 red cards and 26 black cards (all of which are equally likely to be drawn next), so the conditional probability of getting a red card is $2 5 / ( 2 5 + 2 6 ) = 2 5 / 5 1$ It is harder to find $P ( A | B )$ in this way: if we learn that the second card is red, we might think “that’s nice to know, but what we really want to know is whether it’s a heart!” The conditional probability results from later sections in this chapter give us methods for getting around this issue. 

To shed more light on what conditional probability means, here are two intuitive interpretations.