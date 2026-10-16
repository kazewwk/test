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

where $\mid \left[ \frac { \partial ( x ,   y ) } { \partial ( u ,   v ) } \right] \mid$ is the absolute value of the determinant of the Jacobian matrix. A few technical assumptions are needed for this result, such as that the partial derivatives that appear in the Jacobian matrix exist and are continuous, and that the determinant of the Jacobian matrix is never 0.

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

![](images/page_616_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

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

![](images/page_622_image_0.jpg)

## Taylor & Francis

Taylor & Francis Group

http://taylorandfrancis.com

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