```markdown
> 3 + 4/2
[1] 5
> (3 + 4)/2
[1] 3.5
```

Other mathematical operations can be performed by using functions. Functions take in zero or more arguments, do some work, and output a return value. A very important fact about R’s functions is that they copy their arguments, and do not modify their arguments in place (there are some technical exceptions to this rule we’ll ignore). In contrast, Python’s functions can modify their arguments in place. Functions are the bread and butter of working in R, so it’s necessary to understand and be able to work with functions, function arguments, and return values.

R has numerous mathematical functions (see Table 8-1 for some commonly used ones). For example, we call the function sqrt() on a (nonnegative) numeric argument:

```txt
> sqrt(3.5)
[1] 1.870829
```

Table 8-1. Common mathematic functions

| Function Name | Description | Example |
| --- | --- | --- |
| exp(x) | Exponential function | exp(1), exp(2) |
| log(x, base=exp(1)), log10(), log2() | Natural, base 10, and base 2 logarithms | log(2), log10(100), log2(16) |
| sqrt(x) | Square root | sqrt(2) |
| sin(x), cos(x), tan(x), etc. | Trigonometric functions (see help(sin) for more) | sin(pi) |
| abs(x) | Absolute value | abs(-3) |
| factorial(x) | Factorial | factorial(5) |
| choose(n, k) | Binomial coefficient | choose(5, 3) |

## Significant Digits, print(), and Options in R

By default, R will print seven significant digits (which is what it did when we executed sqrt(3.5)). While seven significant digits is the default, it’s easy to print more digits of a value by using the function print(). For example:

```txt
> print(sqrt(3.5), digits=10)
[1] 1.870828693
```

Behind the scenes, R uses print() to format the R objects you see printed as output. (note that you won’t see print() explicitly called).

Alternatively, you can change the default number of significant digits R uses by changing the global option in R. You can view the current default value of an option by calling getOption() with the option name as an argument; for example, you can retrieve the number of significant digits printed as follows:

```txt
> getOption('digits')
[1] 7
```

A new option value can be set using the function options():

```txt
> options(digits=9)
```

options() contains numerous user-customizable global options. See help(options) for more information.

Here, 1.870829 is the return value of this function. This value can either be assigned to a variable (which we’ll see later), or passed directly to other functions as an argument. For example, we could pass this return value into another function, round(), to round our square root:

```txt
> round(sqrt(3.5))
[1] 2
```

The round() function rounds sqrt(3.5) to 2, keeping zero decimal places, because the round() function’s second argument (digits) has a default value of zero. You can learn about a function’s arguments and their default values through round()’s documentation, which you can access with help(round) (see “Getting Help in R” on page 180 for more depth on R’s help and documentation system). We can change the number of digits round() uses by specifying the value of this second digits argument either of two ways:

```txt
> round(sqrt(3.5), digits=3)
[1] 1.871
> round(sqrt(3.5), 3)
[1] 1.871
```

## Getting Help in R

As would be expected from a sophisticated scientific and statistical computing language, R has oodles of functions—far more than any reasonable human can expect to learn and remember. Consequently, you’ll need to master two of the most practical R skills:

• Knowing how to look up a function’s documentation to recall its arguments and how it works
• Being able to discover new useful functions

Each of R’s functions (and other objects such as constants like pi, classes, and packages) has integrated documentation accessible within R. R’s documentation includes descriptions and details about the function, all arguments of a function, and useful usage examples. You access access R’s built-in documentation with the help() function or its syntactic shortcut, ?:

```txt
> help(log)
> ?log
```

In RStudio, this opens a special help window containing log()’s documentation. In terminal R, this documentation is handled by your default pager (probably the program less). Operators such as + and ^ need to be quoted (e.g., help('+')). R also has documentation for general topics available; see, for example, help(Quotes).

R’s help() function is useful when you already know the name of the function you need documentation for. Unfortunately, we often only have a fuzzier idea of what we need help with (e.g., what was the function in R that calculates cross tabulate vectors?). For tasks like this, we can search R’s help system with the function help.search(), or its shortcut ??:

```txt
> help.search("cross tabulate")
> ??"cross tabulate"
```

In this case, help.search() would help you find the function table(), which is useful in creating counts and cross tabulations from vectors.

Also, R has the neat feature that all examples in an R help file can be executed with the function example(). For example:

```txt
> example(log)

log> log(exp(3))
[1] 3
[...]
```

Finally, R also has functions for listing all functions in a package (e.g., library(help="base")) and finding functions by name (e.g., apropos(norm)), which are often useful in remembering a function’s name.

First, values are matched to arguments by name. Technically, R also allows partial matching of argument names but I would discourage this, as it decreases code readability. Second, values are matched based on position within the argument list. For functions that have many arguments with default values such as foo(x, a=3, b=4, c=5), it’s easier to set an argument later in the function by specifying it by name. For example, compare calling foo() with c=5 by using foo(2, 3, 4, 5) with foo(2, c=5).

## Variables and Assignment

To store a value for future use, we assign it to a variable (also known as a symbol in R jargon) using the <- assignment operator:

```txt
> x <- 3.1
```

Once the variable is assigned, we can retrieve its value by evaluating it on a line:

```txt
> x
3.1
```

Variables can also be used in expressions and passed to functions as arguments. R will substitute the variable’s value during evaluation and return the results. These results can then be assigned to other variables:

```txt
> (x + 2)/2
[1] 2.55
> exp(x)
[1] 22.1979513
> y <- exp(2*x) - 1
> y
[1] 491.749041
```

![](images/page_211_image_8.jpg)

## RStudio Assignment Operator Shortcut

In RStudio, you can create the <- assignment operator in one keystroke using Option - (that’s a dash) on OS X or Alt - on Windows/ Linux.

It’s also possible to use = for assignment, but <- is more conventional (and is what we’ll use throughout the chapter).

When we assign a value in our R session, we’re assigning it to an environment known as the global environment. The objects we create by assigning values to variables are kept in environments. We can see objects we’ve created in the global environment with the function ls():

```txt
> ls()
[1] "x"
```

Here, we see the variable name x, which we assigned the value 3.1 earlier. When R needs to lookup a variable name, it looks in the search path. Calling the function search() returns where R looks when searching for the value of a variable—which includes the global environment (.GlobalEnv) and attached packages.

## Vectors, Vectorization, and Indexing

Arguably the most important feature of the R language is its vectors. A vector is a container of contiguous data. Unlike most languages, R does not have a type for a single value (known as a scalar) such as 3.1 or “AGCTACGACT.” Rather, these values are stored in a vector of length 1. We can verify that values like 3.1 are vectors of length 1 by calling the function length() (which returns the length of a vector) on them:

```lisp
> length(3.1)
[1] 1
```

To create longer vectors, we combine values with the function c():

```txt
> x <- c(56, 95.3, 0.4)
> x
[1] 56.0 95.3  0.4
> y <- c(3.2, 1.1, 0.2)
> y
[1] 3.2 1.1 0.2
```

R’s vectors are the basis of one of R’s most important features: vectorization. Vectorization allows us to loop over vectors elementwise, without the need to write an explicit loop. For example, R’s arithmetic operators are all vectorized:

```markdown
> x + y
[1] 59.2 96.4  0.6
> x - y
[1] 52.8 94.2  0.2
> x/y
[1] 17.50000 86.63636  2.00000
```

Integer sequences crop up all over computing and statistics, so R has a few ways of creating these vectors. We’ll use these later in this section:

```txt
> seq(3, 5)
[1] 3 4 5
> 1:5
[1] 1 2 3 4 5
```

There’s one important subtle behavior of vectorized operations applied to two vectors simultaneously: if one vector is longer than the other, R will recycle the values in the shorter vector. This is an intentional behavior, so R won’t warn you when this happens (unless the recycled shorter vector’s length isn’t a multiple of the longer vector’s length). Recycling is what allows you to add a single value to all elements of a vector; the shorter vector (the single value in this case) is recycled to all elements of the longer vector:

```txt
> x
[1] 56.0 95.3  0.4
> x - 3
[1] 53.0 92.3 -2.6
```

```txt
> x / 2
[1] 28.00 47.65 0.20
```

R does warn if it recycles the shorter vector and there are remainder elements left. Consider the following examples:

```python
> c(1, 2) + c(0, 0, 0, 0) ①
[1] 1 2 1 2
> c(1, 2) + c(0, 0, 0) ②
[1] 1 2 1
Warning message:
In c(1, 2) + c(0, 0, 0) :
    longer object length is not a multiple of shorter object length
```

R adds a shorter vector c(1, 2) to a longer vector c(0, 0, 0, 0) by recycling the shorter values. The longer vector is all zeros so this is easier to see.
When the shorter vector’s length isn’t a multiple of the longer vector’s length, there will be a remainder element. R warns about this.

In addition to operators like + and \*, many of R’s mathematical functions (e.g., sqrt(), round(), log(), etc.) are all vectorized:

```txt
> sqrt(x)
[1] 7.4833148 9.7621719 0.6324555
> round(sqrt(x), 3)
[1] 7.483 9.762 0.632
> log(x)/2 + 1 # note how we can combined vectorized operations
[1] 3.0126758 3.2785149 0.5418546
```

This vectorized approach is not only more clear and readable, it’s also often computationally faster. Unlike other languages, R allows us to completely forgo explicitly looping over vectors with a for loop. Later on, we’ll see other methods used for more explicit looping.

We can access specific elements of a vector through indexing. An index is an integer that specifies which element in the vector to retrieve. We can use indexing to get or set values to certain elements from a vector:

```txt
> x <- c(56, 95.3, 0.4)
> x[2] ①
[1] 95.3
> x[1]
[1] 56
> x[4] ②
[1] NA
> x[3] <- 0.5 ③
> x
[1] 56.0 95.3 0.5
```

1 R’s vectors are 1-indexed, meaning that the index 1 corresponds to the first element in a list (in contrast to 0-indexed languages like Python). Here, the value 95.3 is the 2nd item, and is accessed with x[2].
Trying to access an element that doesn’t exist in the vector leads R to return NA, the “not available” missing value.
We can change specific vector elements by combining indexing and assignment.

Vectors can also have names, which you can set while combining values with c():

```diff
> b <- c(a=3.4, b=5.4, c=0.4)
> b
    a   b   c
3.4 5.4 0.4
```

The names of a vector can be both accessed and set with names():

```txt
> names(b)
[1] "a" "b" "c"
> names(b) <- c("x", "y", "z") # change these names
> b
    x   y   z
3.4 5.4 0.4
```

And just as we can access elements by their positional index, we can also access them by their name:

```python
> b['x']
    x
3.4
> b['z']
    z
0.4
```

It is also possible to extract more than one element simultaneously from a vector using indexing. This is more commonly known as subsetting, and it’s a primary reason why the R language is so terrific for manipulating data. Indices like 3 in x[3] are just vectors themselves, so it’s natural to allow these vectors to have more than one element. R will return each element at the positions in the indexing vector:

```txt
> x[c(2, 3)]
[1] 95.3 0.4
```

Vectorized indexing provides some incredibly powerful ways to manipulate data, as we can use indexes to slice out sections of vector, reorder elements, and repeat values. For example, we can use the methods we used to create contiguous integer sequences we learned in “Vectors, Vectorization, and Indexing” on page 183 to create indexing vectors, as we often want to extract contiguous slices of a vector:

```txt
> z <- c(3.4, 2.2, 0.4, -0.4, 1.2)
> z[3:5] # extract third, fourth, and fifth elements
[1] 0.4 -0.4 1.2
```

![](images/page_215_image_1.jpg)

## Out-of-Range Indexing

Be aware that R does not issue a warning if you try to access an element in a position that’s greater than the number of elements— instead, R will return a missing value (NA; more on this later). For example:

```c
> z[c(2, 1, 10)]
[1] 2.2 3.4 NA
```

Similarly, missing values in indexes leads to an NA too.

It’s also possible to exclude certain elements from lists using negative indexes:

```txt
> z[c(-4, -5)]   # exclude fourth and fifth elements
[1] 3.4 2.2 0.4
```

![](images/page_215_image_8.jpg)

## Negative Indexes and the Colon Operator

One important subtle gotcha occurs when trying to combine negative indexes with the colon operator. For example, if you wanted to exclude the second through fourth elements of a vector x, you might be tempted to use x[-2:4]. However, if you enter -2:4 in the R interpreter, you’ll see that it creates a sequence from -2 to 4—not –2, –3, and –4. To remedy this, wrap the sequence in parentheses:

```txt
> -(2:4)
[1] -2 -3 -4
```

Indices are also often used to reorder elements. For example, we could rearrange the elements of this vector z with:

```txt
> z[c(3, 2, 4, 5, 1)]
[1] 0.4 2.2 -0.4 1.2 3.4
```

Or we could reverse the elements of this vector by creating the sequence of integers from 5 down to 1 using 5:1:

```txt
> z[5:1]
[1] 1.2 -0.4 0.4 2.2 3.4
```

Similarly, we can use other R functions to create indexes for us. For example, the function order() returns a vector of indexes that indicate the (ascending) order of the elements. This can be used to reorder a vector into increasing or decreasing order:

```txt
> order(z)
[1] 4 3 5 2 1
> z[order(z)]
```

```txt
[1] -0.4  0.4  1.2  2.2  3.4
> order(z, decreasing=TRUE)
[1] 1 2 5 3 4
> z[order(z, decreasing=TRUE)]
[1]  3.4  2.2  1.2  0.4 -0.4
```

Again, R’s vector index rule is simple: R will return the element at the i<sup>th</sup> position for each i in the indexing vector. This also allows us to repeat certain values in vectors:

```c
> z[c(2, 2, 1, 4, 5, 4, 3)]
[1]   2.2   2.2   3.4 -0.4   1.2 -0.4   0.4
```

Again, often we use functions to generate indexing vectors for us. For example, one way to resample a vector (with replacement) is to randomly sample its indexes using the sample() function:

```diff
> set.seed(0)   # we set the random number seed so this example is reproducible
> i <- sample(length(z), replace=TRUE)
> i
[1] 5 2 2 3 5
> z[i]
[1] 1.2 2.2 2.2 0.4 1.2
```

Just as we use certain functions to generate indexing vectors, we can use comparison operators like ==, !=, <, <=, >, and >= (see Table 8-2) to build logical vectors of TRUE and FALSE values indicating the result of the comparison test for each element in the vector. R’s comparison operators are also vectorized (and will be recycled according to R’s rule). Here are some examples:

```c
> v <- c(2.3, 6, -3, 3.8, 2, -1.1)
> v == 6
[1] FALSE   TRUE FALSE FALSE FALSE FALSE
> v <= -3
[1] FALSE FALSE   TRUE FALSE FALSE FALSE
> abs(v) > 5
[1] FALSE   TRUE FALSE FALSE FALSE FALSE
```

Logical vectors are useful because they too can be used as indexing vectors—R returns the elements with corresponding TRUE values in the indexing vector (see Example 8-1).

Example 8-1. Indexing vectors with logical vectors

```txt
> v[c(TRUE, TRUE, FALSE, TRUE, FALSE, FALSE)]
[1] 2.3 6.0 3.8
```

But it’s tedious to construct these logical vectors of TRUE and FALSE by hand; if we wanted to select out particular elements using an integer, indexes would involve much less typing. But as you might have guessed, the power of using logical vectors in subsetting comes from creating logical vectors using comparison operators. For example, to subset v such that only elements greater than 2 are kept, we’d use:

```javascript
> v[v > 2]
[1] 2.3 6.0 3.8
```

Note that there’s no magic or special evaluation going on here: we are simply creating a logical vector using v > 2 and then using this logical vector to select out certain elements of v. Lastly, we can use comparison operators (that return logical vectors) with vectorized logical operations (also known as Boolean algebra in other disciplines) such as & (AND), | (OR), and ! (NOT). For example, to find all elements of v greater than 2 and less than 4, we’d construct a logical vector and use this to index the vector:

```txt
> v > 2 & v < 4
[1]  TRUE FALSE FALSE  TRUE FALSE FALSE
> v[v > 2 & v < 4]
[1] 2.3 3.8
```

Table 8-2. R’s comparison and logical operators

| Operator | Description |
| --- | --- |
| > | Greater than |
| &lt; | Less than |
| >= | Greater than or equal to |
| &lt;= | Less than or equal to |
| == | Equal to |
| ! | Not equal to |
| &amp; | Elementwise logical AND |
| \| | Elementwise logical OR |
| ! | Elementwise logical NOT |
| &amp;&amp; | Logical AND (first element only, for if statements) |
| \|\| | Logical OR (first element only, for if statements) |

We’ll keep returning to this type of subsetting, as it’s the basis of some incredibly powerful data manipulation capabilities in R.

## Vector types

The last topic about vectors to cover before diving into working with real data is R’s vector types. Unlike Python’s lists or Perl’s arrays, R’s vectors must contain elements of the same type. In the context of working with statistical data, this makes sense: if we add two vectors x and y together with a vectorized approach like x + y, we want to know ahead of time whether all values in both vectors have the same type and can indeed be added together. It’s important to be familiar with R’s types, as it’s common as an R beginner to run into type-related issues (especially when loading in data that’s messy).

R supports the following vector types (see also Table 8-3):

## Numeric

Numeric vectors (also known as double vectors) are used for real-valued numbers like 4.094, –12.4, or 23.0. By default, all numbers entered into R (e.g., c(5, 3, 8)) create numeric vectors, regardless of whether they’re an integer.

## Integer

R also has an integer vector type for values like –4, 39, and 23. Because R defaults to giving integer values like –4, 39, and 23 the type numeric, you can explicitly tell R to treat a value as an integer by appending a capital L after the value (e.g., -4L, 39L, and 23L). (Note that the seemingly more sensible i or I aren’t used to avoid confusion with complex numbers with an imaginary component like 4 + 3i).

## Character

Character vectors are used to represent text data, also known as strings. Either single or double quotes can be used to specify a character vector (e.g., c("AGTC GAT", "AGCTGGA")). R’s character vectors recognize special characters common to other programming languages such as newline (\n) and tab (\t).

## Logical

Logical values are used to represent Boolean values, which in R are TRUE and FALSE. T and F are assigned the values TRUE and FALSE, and while you might be tempted to use these shortcuts, do not. Unlike TRUE and FALSE, T and F can be redefined in code. Defining T <- 0 will surely cause problems.

Table 8-3. R’s vector types

| Type | Example | Creation function | Test function | Coercion function |
| --- | --- | --- | --- | --- |
| Numeric | c(23.1, 42, -1) | numeric() | is.numeric() | as.numeric() |
| Integer | c(1L, -3L, 4L) | integer() | is.integer() | as.integer() |
| Character | c("a", "c") | character() | is.character() | as.character() |
| Logical | c(TRUE, FALSE) | logical() | is.logical() | as.logical() |

In addition to double, integer, character, and logical vectors, R has two other vector types: complex to represent complex numbers (those with an imaginary component), and raw, to encode raw bytes. These types have limited application in bioinformatics, so we’ll skip discussing them.

## R’s Special Values

R has four special values (NA, NULL, Inf/-Inf, and NaN) that you’re likely to encounter in your work:

## NA

NA is R’s built-in value to represent missing data. Any operation on an NA will return an NA (e.g., 2 + NA returns NA). There are numerous functions to handle NAs in data; see na.exclude() and complete.cases(). You can find which elements of a vector are NA with the function is.na().

## NULL

NULL represents not having a value (which is different than having a value that’s missing). It’s analogous to Python’s None value. You can test if a value is NULL with the function is.null().

## -Inf, Inf

These are just as they sound, negative infinite and positive infinite values. You can test whether a value is finite with the function is.finite() (and its complement is.infinite()).

## NaN

NaN stands for “not a number,” which can occur in some computations that don’t return numbers, i.e., 0/0 or Inf + -Inf. You can test for these with is.nan().

Again, the most important thing to remember about R’s vectors and data types is that vectors are of homogenous type. R enforces this restriction through coercion, which like recycling is a subtle behavior that’s important to remember about R.

![](images/page_220_image_0.jpg)

## Type Coercion in R

Because all elements in a vector must have homogeneous data type, R will silently coerce elements so that they have the same type.

R’s coercion rules are quite simple; R coerces vectors to a type that leads to no information loss about the original value. For example, if you were to try to create a vector containing a logical value and a numeric value, R would coerce the logical TRUE and FALSE values to 1 and 0, as these represent TRUE and FALSE without a loss of information:

```txt
> c(4.3, TRUE, 2.1, FALSE)
[1] 4.3 1.0 2.1 0.0
```

Similarly, if you were to try to create a vector containing integers and numerics, R would coerce this to a numeric vector, because integers can be represented as numeric values without any loss of information:

```txt
> c(-9L, 3.4, 1.2, 3L)
[1] -9.0 3.4 1.2 3.0
```

Lastly, if a string were included in a vector containing integers, logicals, or numerics, R would convert everything to a character vector, as this leads to the least amount of information loss:

```python
> c(43L, TRUE, 3.2413341, "a string")
[1] "43"          "TRUE"      "3.2413341" "a string"
```

We can see any object’s type (e.g., a vector’s type) using the function typeof():

```txt
> q <- c(2, 3.5, -1.1, 3.8)
> typeof(q)
[1] "double"
```

## Factors and classes in R

Another kind of vector you’ll encounter are factors. Factors store categorical variables, such as a treatment group (e.g., “high,” “medium,” “low,” “control”), strand (forward or reverse), or chromosome (“chr1,” “chr2,” etc.). Factors crop up all over R, and occasionally cause headaches for new R users (we’ll discuss why in “Loading Data into R” on page 194).

Suppose we had a character vector named chr\_hits containing the Drosophila mela nogaster chromosomes where we find a particular sequence aligns. We can create a factor from this vector using the function factor():

```r
> chr_hits <- c("chr2", "chr2", "chr3", "chrX", "chr2", "chr3", "chr3")
> hits <- factor(chr_hits)
> hits
```

[1] chr2 chr2 chr3 chrX chr2 chr3 chr3

Levels: chr2 chr3 chrX

Printing the hits object shows the original sequence (i.e., chr2, chr2, chr3, etc.) as well as all of this factor’s levels. The levels are the possible values a factor can contain (these are fixed and must be unique). We can view a factor’s levels by using the function levels():

```txt
> levels(hits)
[1] "chr2" "chr3" "chrX"
```

Biologically speaking, our set of levels isn’t complete. Drosophila melanogaster has two other chromosomes: chrY and chr4. Although our data doesn’t include these chromosomes, they are valid categories and should be included as levels in the factor. When creating our factor, we could use the argument levels to include all relevant levels:

```txt
> hits <- factor(chr_hits, levels=c("chrX", "chrY", "chr2", "chr3", "chr4"))
> hits
[1] chr2 chr2 chr3 chrX chr2 chr3 chr3
Levels: chrX chrY chr2 chr3 chr4
```

If we’ve already created a factor, we can add or rename existing levels with the function levels(). This is similar to how we assigned vector names using names(obj) <- . When setting names, we use a named character vector to provide a mapping between the original names and the new names:

```txt
> levels(hits) <- list(chrX="chrX", chrY="chrY", chr2="chr2",
                      chr3="chr3", chr4="chr4")
> hits
[1] chr2 chr2 chr3 chrX chr2 chr3 chr3
Levels: chrX chrY chr2 chr3 chr4
```

We can count up how many of each level there are in a factor using the function table():

```txt
> table(hits)
hits
chrX chrY chr2 chr3 chr4
    1     0     3     3     0
```

Factors are a good segue into briefly discussing classes in R. An object’s class endows objects with higher-level properties that can affect how functions treat that R object. We won’t get into the technical details of creating classes or R’s object orientation system in this section (see a text like Hadley Wickham’s Advanced R for these details). But it’s important to have a working familiarity with the idea that R’s objects have a class and this can change how certain functions treat R objects.

To discern the difference between an object’s class and its type, notice that factors are just integer vectors under the hood:

```txt
> typeof(hits)
[1] "integer"
> as.integer(hits)
[1] 3 3 4 1 3 4 4
```

Functions like table() are generic—they are designed to work with objects of all kinds of classes. Generic functions are also designed to do the right thing depending on the class of the object they’re called on (in programming lingo, we say that the function is polymorphic). For example, table() treats a factor differently than it would treat an integer vector. As another example, consider how the function sum mary() (which summarizes an object such as vector) behaves when it’s called on a vector of numeric values versus a factor:

```txt
> nums <- c(0.97, -0.7, 0.44, 0.25, -1.38, 0.08)
> summary(nums)
    Min.  1st Qu.   Median      Mean  3rd Qu.     Max.
-1.38000 -0.50500  0.16500 -0.05667  0.39250  0.97000
> summary(hits)
chrX chrY chr2 chr3 chr4
    1     0     3     3     0
```

When called on numeric values, summary() returns a numeric summary with the quartiles and the mean. This numeric summary wouldn’t be meaningful for the categorical data stored in a factor, so instead summary() returns the level counts like table() did. This is function polymorphism, and occurs because nums has class “numeric” and hits has class “factor”:

```lisp
> class(nums)
[1] "numeric"
> class(hits)
[1] "factor"
```

These classes are a part of R’s S3 object-oriented system. R actually has three object orientation systems (S3, S4, and reference classes). Don’t worry too much about the specifics; we’ll encounter classes in this chapter (and also in Chapter 9), but it won’t require an in-depth knowledge of R’s OO systems. Just be aware that in addition to a type, objects have a class that changes how certain functions treat that object.

## Working with and Visualizing Data in R

With a knowledge of basic R language essentials from the previous section, we’re ready to start working with real data. We’ll work a few different datasets in this chapter. All files to load these datasets into R are available in this chapter’s directory on GitHub.

The dataset we’ll use for learning data manipulation and visualization skills is from the 2006 paper [“The Influence of Recombination on Human Genetic Diversity”](http://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.0020148) by

Spencer et al. I’ve chosen this dataset (Dataset\_S1.txt on GitHub) for the following reasons:

• It’s an excellent piece of genomic research with interesting biological findings.
• The article is open access and thus freely accessible the public.
• The raw data is also freely available and is tidy, allowing us to start exploring it immediately.
• All scripts used in the authors’ analyses are freely available (making this a great example of reproducible research).

In addition, this type of genomic dataset is also characteristic of the data generated from lower-level bioinformatics workflows that are then analyzed in R.

Dataset\_S1.txt contains estimates of population genetics statistics such as nucleotide diversity (e.g., the columns Pi and Theta), recombination (column Recombination), and sequence divergence as estimated by percent identity between human and chimpanzee genomes (column Divergence). Other columns contain information about the sequencing depth (depth), and GC content (percent.GC). We’ll only work with a few columns in our examples; see the description of Dataset\_S1.txt in this paper’s supplementary information for more detail. Dataset\_S1.txt includes these estimates for 1kb windows in human chromosome 20.

## Loading Data into R

The first step of any R data analysis project is loading data into R. For some datasets (e.g., Dataset\_S1.txt), this is quite easy—the data is tidy enough that R’s functions for loading in data work on the first try. In some cases, you may need to use Unix tools (Chapter 7) to reformat the data into a tab-delimited or CSV plain-text format, or do some Unix sleuthing to find strange characters in the file (see “Decoding Plain-Text Data: hexdump” on page 145). In other cases, you’ll need to identify and remove improper values from data within R or coerce columns.

Before loading in this file, we need to discuss R’s working directory. When R is running, the process runs in a specific working directory. It’s important to mind this working directory while loading data into R, as which directory R is running in will affect how you specify relative paths to data files. By default, command-line R will use the directory you start the R program with; RStudio uses your home directory (this is a customizable option). You can use getwd() to get R’s current working directory and setwd() to set the working directory:

```txt
> getwd()
[1] "/Users/vinceb"
> setwd("~/bds-files/chapter-08-r") # path to this chapter's
# directory in the Github repository.
```