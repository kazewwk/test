You may be wondering why we slogged through all of the split(), lapply(), and do.call() material given how much simpler it is to call tapply() or aggregate(). The answer is twofold. First, R’s base functions like split(), lapply(), and do.call() give you some raw power and flexibility in how you use the split-applycombine pattern. In working with genomics datasets (and with Bioconductor packages), we often need this flexibility. Second, Hadley Wickham’s package dplyr (which we see in the next section) is both simpler and more powerful than R’s built-in splitapply-combine functions like tapply() and aggregate().

The take-home point of this section: the split-apply-combine pattern is an essential part of data analysis. As Hadley Wickham’s article points out, this strategy is similar to Google’s map-reduce framework and SQL’s GROUP BY and AGGREGATE functions (which we cover in “SQLite Aggregate Functions” on page 442).

## Exploring Dataframes with dplyr

Every data analysis you conduct will likely involve manipulating dataframes at some point. Quickly extracting, transforming, and summarizing information from dataframes is an essential R skill. The split-apply-combine pattern implemented from R base functions like split() and lapply() is versatile, but not always the fastest or simplest approach. R’s split-apply-combine convenience functions like tapply() and aggregate() simplify the split-apply-combine, but their output still often requires some cleanup before the next analysis step. This is where Hadley Wickham’s dplyr package comes in: dplyr consolidates and simplifies many of the common operations we perform on dataframes. Also, dplyr is very fast; much of its key functionality is written in C++ for speed.

dplyr has five basic functions for manipulating dataframes: arrange(), filter(), mutate(), select(), and summarize(). None of these functions perform tasks you can’t accomplish with R’s base functions. But dplyr’s advantage is in the added consistency, speed, and versatility of its data manipulation interface. dplyr’s design drastically simplifies routine data manipulation and analysis tasks, allowing you to more easily and effectively explore your data.

Because it’s common to work with dataframes with more rows and columns than fit in your screen, dplyr uses a simple class called tbl\_df that wraps dataframes so that they don’t fill your screen when you print them (similar to using head()). Let’s convert our d dataframe into a tbl\_df object with the tbl\_df() function:

```txt
> install.packages("dplyr") # install dplyr if it's not already installed
> library(dplyr)
> d_df <- tbl_df(d)
> d_df
Source: local data frame [59,140 x 20]
```

```txt
start end total.SNPs total.Bases depth unique.SNPs dhSNPs reference.Bases
1 55001 56000          0       1894 3.41         0      0           556
2 56001 57000          5       6683 6.68         2      2           1000
3 57001 58000          1       9063 9.06         1      0           1000
[...]
```

Variables not shown: Theta (dbl), Pi (dbl), Heterozygosity (dbl), percent.GC (dbl), Recombination (dbl), Divergence (dbl), Constraint (int), SNPs (int), cent (lgl), diversity (dbl), position (dbl), GC.binned (fctr)

Let’s start by selecting some columns from d\_df using dplyr’s select() function:

> select(d\_df, start, end, Pi, Recombination, depth)

Source: local data frame [59,140 x 5]

```txt
start end     Pi Recombination depth
1 55001 56000 0.000   0.009601574 3.41
2 56001 57000 10.354   0.009601574 6.68
3 57001 58000 1.986   0.009601574 9.06
[...]
```

This is equivalent to d[, c("start", "end", "Pi", "Recombination", "depth")], but dplyr uses special evaluation rules that allow you to omit quoting column names in select() (and the returned object is a tbl\_df). select() also understands ranges of consecutive columns like select(d\_df, start:total.Bases). Additionally, you can drop columns from a dataframe by prepending a negative sign in front of the column name (and this works with ranges too):

```txt
> select(d_df, -(start:cent))
Source: local data frame [59,140 x 3]

    position   GC.binned diversity
1   55500.5 (51.6,68.5] 0.0000000
2   56500.5 (34.7,51.6] 0.0010354
3   57500.5 (34.7,51.6] 0.0001986
[...]
```

Similarly, we can select specific rows as we did using dataframe subsetting in “Exploring Data Through Slicing and Dicing: Subsetting Dataframes” on page 203 using the dplyr function filter(). filter() is similar to subsetting dataframes using expressions like d[d\$Pi > 16 & d\$percent.GC > 80, ], though you can use multiple statements (separated by commas) instead of chaining them with &:

```python
> filter(d_df, Pi > 16, percent.GC > 80)
Source: local data frame [3 x 20]
```

```txt
start     end total.SNPs total.Bases depth unique.SNPs dhSNPs
1 63097001 63098000       5       947 2.39        2      1
2 63188001 63189000       2       1623 3.21        2      0
3 63189001 63190000       5       1395 1.89        3      2
Variables not shown: reference.Bases (int), Theta (dbl), Pi (dbl),
    Heterozygosity (dbl), percent.GC (dbl), Recombination (dbl), Divergence
```

(dbl), Constraint (int), SNPs (int), cent (lgl), position (dbl), GC.binned (fctr), diversity (dbl)

To connect statements with logical OR, you need to use the standard logical operator | we learned about in “Vectors, Vectorization, and Indexing” on page 183.

dplyr also simplifies sorting by columns with the function arrange(), which behaves like d[order(d\$percent.GC), ]:

```txt
> arrange(d_df, depth)
Source: local data frame [59,140 x 20]
```

```txt
start       end total.SNPs total.Bases depth unique.SNPs dhSNPs
1  1234001 1235000      0          444   1          0     0
2  1584001 1585000      0          716   1          0     0
3  2799001 2800000      0          277   1          0     0
[...]
```

You can sort a column in descending order using arrange() by wrapping its name in the function desc(). Also, additional columns can be specified to break ties:

```txt
> arrange(d_df, desc(total.SNPs), desc(depth))
Source: local data frame [59,140 x 20]
```

```txt
start       end total.SNPs total.Bases depth unique.SNPs dhSNPs
1   2621001 2622000      93       11337 11.34       13     10
2  13023001 13024000      88       11784 11.78       11     1
3  47356001 47357000      87       12505 12.50       9     7
[...]
```

Using dplyr’s mutate() function, we can add new columns to our dataframe: For example, we added a rescaled version of the Pi column as d\$diversity—let’s drop d \$diversity using select() and then recalculate it:

```txt
> d_df <- select(d_df, -diversity) # remove our earlier diversity column
> d_df <- mutate(d_df, diversity = Pi/(10*1000))
> d_df
Source: local data frame [59,140 x 20]
```

```txt
start end total.SNPs total.Bases depth unique.SNPs dhSNPs reference.Bases
1 55001 56000          0       1894 3.41         0      0           556
2 56001 57000          5       6683 6.68         2      2           1000
3 57001 58000          1       9063 9.06         1      0           1000
[...]
... ... ...     ...     ... ...     ...    ...
Variables not shown: Theta (dbl), Pi (dbl), Heterozygosity (dbl), percent.GC
 (dbl), Recombination (dbl), Divergence (dbl), Constraint (int), SNPs (int),
 cent (lgl), position (dbl), GC.binned (fctr), diversity (dbl)
```

mutate() creates new columns by transforming existing columns. You can refer to existing columns directly by name, and not have to use notation like d\$Pi.

So far we’ve been using dplyr to get our dataframes into shape by selecting columns, filtering and arranging rows, and creating new columns. In daily work, you’ll need to use these and other dplyr functions to manipulate and explore your data. While we could assign output after each step to an intermediate variable, it’s easier (and more memory efficient) to chain dplyr operations. One way to do this is to nest functions (e.g., filter(select(hs\_df, seqname, start, end, strand), strand == "+")). However, reading a series of data manipulation steps from the inside of a function outward is a bit unnatural. To make it easier to read and create data-processing pipelines, dplyr uses %>% (known as pipe) from [the magrittr package](http://github.com/smbache/magrittr). With these pipes, the lefthand side is passed as the first argument of the righthand side function, so d\_df %>% filter(percent.GC > 40) becomes filter(d\_df, percent.GC > 40. Using pipes in dplyr allows us to clearly express complex data manipulation operations:

```txt
> d_df %>% mutate(GC.scaled = scale(percent.GC)) %>%
        filter(GC.scaled > 4, depth > 4) %>%
        select(start, end, depth, GC.scaled, percent.GC) %>%
        arrange(desc(depth))

Source: local data frame [18 x 5]
    start      end depth GC.scaled percent.GC
1 62535001 62536000 7.66 4.040263   73.9740
2 63065001 63066000 6.20 4.229954   75.3754
3 62492001 62493000 5.25 4.243503   75.4755
[...]
```

Pipes are a recent innovation, but one that’s been quickly adopted by the R community. You can learn more about magrittr’s pipes in help('%>%').

dplyr’s raw power comes from the way it handles grouping and summarizing data. For these examples, let’s use the mtfs dataframe (loaded into R in “Merging and Combining Data: Matching Vectors and Merging Dataframes” on page 219), as it has some nice factor columns we can group by:

```txt
> mtfs_df <- tbl_df(mtfs)
```

Now let’s group by the chromosome column chr. We can group by one or more columns by calling group\_by() with their names as arguments:

```txt
> mtfs_df %>% group_by(chr)
Source: local data frame [20,050 x 10]
Groups: chr

    chr motif_start motif_end     dist recomb_start recomb_end  recom
1  chrX      35471312 35471325 39323.0     35430651   35433340 0.0015
2  chrX      35471312 35471325 36977.0     35433339   35435344 0.0015
[...]
```

Note that dplyr’s output now includes a line indicating which column(s) the dataset is grouped by. But this hasn’t changed the data; now dplyr’s functions will be applied per group rather than on all data (where applicable). The most common use case is to create summaries as we did with tapply() and aggregate() using the summarize() function:

```txt
> mtfs_df %>%
    group_by(chr) %>%
    summarize(max_recom = max(recom), mean_recom = mean(recom), num=n())

Source: local data frame [23 x 4]
    chr max_recom mean_recom num
1   chr1   41.5648   2.217759 2095
2   chr10   42.4129   2.162635 1029
3   chr11   36.1703   2.774918  560
[...]
```

dplyr’s summarize() handles passing the relevant column to each function and automatically creates columns with the supplied argument names. Because we’ve grouped this data by chromosome, summarize() computes per-group summaries. Try this same expression without group\_by().

dplyr provides some convenience functions that are useful in creating summaries. Earlier, we saw that n() returns the number of observations in each group. Similarly, n\_distinct() returns the unique number of observations in each group, and first(), last() and nth() return the first, last, and n<sup>th</sup> observations, respectively. These latter three functions are mostly useful on data that has been sorted with arrange() (because specific rows are arbitrary in unsorted data).

We can chain additional operations on these grouped and summarized results; for example, if we wanted to sort by the newly created summary column max\_recom:

```txt
> mtfs_df %>%
    group_by(chr) %>%
    summarize(max_recom = max(recom), mean_recom = mean(recom), num=n()) %>%
    arrange(desc(max_recom))

Source: local data frame [23 x 4]
    chr max_recom mean_recom num
1   chrX  74.0966   2.686840  693
2   chr8   62.6081   1.913325 1727
3   chr3   56.2775   1.889585 1409
4   chr16   54.9638   2.436250  535
[...]
```

dplyr has a few other functions we won’t cover in depth: distinct() (which returns only unique values), and sampling functions like sample\_n() and sample\_frac() (which sample observations). Finally, one of the best features of dplyr is that all of these same methods also work with database connections. For example, you can manipulate a SQLite database (the subject of Chapter 13) with all of the same verbs we’ve used here. See [dplyr’s databases vignette](http://bit.ly/dplyr_data) for more information on this.

## Working with Strings

In bioinformatics, we often need to extract data from strings. R has several functions to manipulate strings that are handy when working with bioinformatics data in R. Note, however, that for most bioinformatics text-processing tasks, R is not the preferred language to use for a few reasons. First, R works with all data stored in memory; many bioinformatics text-processing tasks are best tackled with the stream-based approaches (discussed in Chapters 3 and 7), which explicitly avoid loading all data in memory at once. Second, R’s string processing functions are admittedly a bit clunky compared to Python’s. Even after using these functions for years, I still have to constantly refer to their documentation pages.

Despite these limitations, there are many cases when working with strings in R is the best solution. If we’ve already loaded data into R to explore, it’s usually easier to use R’s string processing functions than to write and process data through a separate Python script. In terms of performance, we’ve already incurred the costs of reading data from disk, so it’s unlikely there will be performance gains from using Python or another language. With these considerations in mind, let’s jump into R’s string processing functions.

First, remember that all strings in R are actually character vectors. Recall that this means a single string like “AGCTAG” has a length of 1 (try length("AGCTAG")). If you want to retrieve the number of characters of each element of a character vector, use nchar(). Like many of R’s functions, nchar() is vectorized:

```lua
> nchar(c("AGCTAG", "ATA", "GATCTGAG", ""))
[1] 6 3 8 0
```

We can search for patterns in character vectors using either grep() or regexpr(). These functions differ slightly in their behavior, making both useful under different circumstances. The function grep(pattern, x) returns the positions of all elements in x that match pattern:

```txt
> re_sites <- c("CTGCAG", "CGATCG", "CAGCTG", "CCCACA")
> grep("CAG", re_sites)
[1] 1 3
```

By default, grep() uses POSIX extended regular expressions, so we could use more sophisticated patterns:

```erlang
> grep("CT[CG]", re_sites)
[1] 1 3
```

grep() and R’s other regular-expression handling functions (which we’ll see later) support Perl Compatible Regular Expressions (PCRE) with the argument perl=TRUE, and fixed string matching (e.g., not interpreting special characters) with fixed=TRUE. If a regular expression you’re writing isn’t working, it may be using features only available in the more modern PCRE dialect; try enabling PCRE with perl=TRUE.

Because grep() is returning indices that match the pattern, grep() is useful as a pattern-matching equivalent of match(). For example, we could use grep() to pull out chromosome 6 entries from a vector of chromosome names with sloppy, inconsistent naming:

```txt
> chrs <- c("chrom6", "chr2", "chr6", "chr4", "chr1", "chr16", " chrom8")
> grep("[^\d]6", chrs, perl=TRUE)
[1] 1 3
> chrs[grep("[^\d]6", chrs, perl=TRUE)]
[1] "chrom6" "chr6"
```

There are some subtle details in this example worth discussing. First, we can’t use a simpler regular expression like chrs[grep("6", chrs)] because this would match entries like "chr16". We prevent this by writing a restrictive pattern that is any non-numeric character ([^\\d]) followed by a 6. Note that we need an additional backslash to escape the backslash in \d. Finally, \d is a special symbol available in Perl Compatible Regular Expressions, so we need to specify perl=TRUE. See help(regex) for more information on R’s regular expressions.

![](images/page_278_image_4.jpg)

## The Double Backslash

The double backslash is a very important part of writing regular expressions in R. Backslashes don’t represent themselves in R strings (i.e., they are used as escape characters as in "\"quote\" string" or the newline character \n). To actually include a blackslash in a string, we need to escape the backslash’s special meaning with another backslash.

Unlike grep(), regexpr(pattern, x) returns where in each element of x it matched pattern. If an element doesn’t match the pattern, regexpr() returns –1. For example:

```txt
> regexpr("[^\d]6", chrs, perl=TRUE)
[1]  5 -1  3 -1 -1 -1 -1
attr(,"match.length")
[1]  2 -1  2 -1 -1 -1 -1
attr(,"useBytes")
[1] TRUE
```

regexpr() also returns the length of the matching string using attributes. We haven’t discussed attributes, but they’re essentially a way to store meta-information alongside objects. You can access attributes with the function attributes(). For more information on regexpr’s output, see help(regexpr).

Clearly, the vector chromosome named chrs is quite messy and needs tidying. One way to do this is to find the informative part of each name with regexpr() and extract this part of the string using substr(). substr(x, start, stop) takes a string x and returns the characters between start and stop:

```javascript
> pos <- regexr("\\d+", chrs, perl=TRUE)
> pos
[1] 6 4 4 4 4 4 7
attr(,"match.length")
[1] 1 1 1 1 1 2 1
attr(,"useBytes")
[1] TRUE
> substr(chrs, pos, pos + attributes(pos)$match.length)
[1] "6" "2" "6" "4" "1" "16" "8"
```

While this solution introduced the helpful substr() function, it is fragile code and we can improve upon it. The most serious flaw to this approach is that it isn’t robust to all valid chromosome names. We’ve written code that solves our immediate problem, but may not be robust to data this code may encounter in the future. If our code were rerun on an updated input with chromosomes “chrY” or “chrMt,” our regular expression would fail to match these. While it may seem like a far-fetched case to worry about, consider the following points:

• These types of errors can bite you and are time consuming to debug.
• Our code should anticipate biologically realistic input data (like sex and mitochondrial chromosomes).

We can implement a cleaner, more robust solution with the sub() function. sub() allows us to substitute strings for other strings. Before we continue with our example, let’s learn about sub() through a simple example that doesn’t use regular expressions. sub(pattern, replacement, x) replaces the first occurrence of pattern with replacement for each element in character vector x. Like regexpr() and grep(), sub() supports perl=TRUE and fixed=TRUE:

```python
> sub(pattern="Watson", replacement="Watson, Franklin",
       x="Watson and Crick discovered DNA's structure.")
[1] "Watson, Franklin, and Crick discovered DNA's structure."
```

Here, we’ve replaced the string “Watson” with the string “Watson, Franklin,” using sub(). Fixed text substitution like this works well for some problems, but to tidy our chr vector we want to capture the informative part of chromosome name (e.g., 1, 2, X, Y, or M) and substitute it into a consistent naming scheme (e.g., chr1, chr2, chrX, or chrM). We do this with regular expression capturing groups. If you’re completely unfamiliar with these, do study how they work in other scripting languages you use; capturing groups are extremely useful in bioinformatics string processing tasks. In this case, the parts of our regular expression in parentheses are captured and can be used later by referencing which group they are. Let’s look at a few simple examples and then use sub() to help tidy our chromosomes:

```txt
> sub("gene=(\\w+)", "\\1", "gene=LEAFY", perl=TRUE) ①
[1] "LEAFY"

> sub(">[^ ]+ *(.*)", "\\1", ">1 length=301354135 type=dna") ②
[1] "length=301354135 type=dna"

> sub(".*(\d+|X|Y|M)", "chr\1", "chr19", perl=TRUE) ③
[1] "chr9"

> sub(" *[chrom]+(\d+|X|Y|M) *" , "chr\1", c("chr19", "chrY"), perl=TRUE) ④
[1] "chr19" "chrY"
```

1 This line extracts a gene name from a string formatted as gene=&lt;name&gt;. We anchor our expression with gene=, and then use the word character \\w. This matches upper- and lowercase letters, digits, and underscores. Note that this regular expression assumes our gene name will only include alphanumeric characters and underscores; depending on the data, this regular expression may need to be changed.
This expression extracts all text after the first space. This uses a common idiom: specify a character class of characters not to match. In this case, [^ ]+ specifies match all characters that aren’t spaces. Then, match zero or more spaces, and capture one or more of any character (.\*).
Here, we show a common problem with regular expressions and sub(). Our intention was to extract the informative part of a chromosome name like “chr19” (in this case, “19”). However, our regular expression was too greedy. Because the part .\* matches zero more of any character, this matches through to the “1” of “chr19.” The “9” is still matched by the rest of the regular expression, captured, and inserted into the replacement string. Note that this error is especially dangerous because it silently makes your data incorrect.
4 This expression can be used to clean up the messy chromosome name data. Both “chr” and “chrom” (as well as other combinations of these characters) are matched. The informative part of each chromosome name is captured, and replaced into the string “chr” to give each entry a consistent name. We’re assuming that we only have numeric, X, Y, and mitochondrion (M) chromosomes in this example.

Parsing inconsistent naming is always a daily struggle for bioinformaticians. Inconsistent naming isn’t usually a problem with genome data resources like Ensembl or the UCSC Genome Browser; these resources are well curated and consistent. Data input by humans is often the cause of problems, and unfortunately, no regular expression can handle all errors a human can make when inputting data. Our best strategy is to try to write general parsers and explicitly test that parsed values make sense (see the following tip).

![](images/page_281_image_1.jpg)

## Friendly Functions for Loud Code

The Golden Rule of Bioinformatics is to not trust your data (or tools). We can be proactive about this in code by using functions like stopifnot(), stop() warning(), and message() that stop execution or let the user know of issues that occur when running code. The function stopifnot() errors out if any of its arguments don’t evaluate to TRUE. warning() and message() don’t stop execution, but pass warnings and messages to users. Occasionally, it’s useful to turn R warnings into errors so that they stop execution. We can enable this behavior with options(warn=2) (and set options(warn=0) to return to the default).

Another useful function is paste(), which constructs strings by “pasting” together the parts. paste() takes any number of arguments and concatenates them together using the separating string specified by the sep argument (which is a space by default). Like many of R’s functions, paste() is vectorized:

```txt
> paste("chr", c(1:22, "X", "Y"), sep="")
[1] "chr1"  "chr2"  "chr3"  "chr4"  "chr5"  "chr6"  "chr7"  "chr8"  "chr9"
[10] "chr10"  "chr11"  "chr12"  "chr13"  "chr14"  "chr15"  "chr16"  "chr17"  "chr18"
[19] "chr19"  "chr20"  "chr21"  "chr22"  "chrX"  "chrY"
```

Here, paste() pasted together the first vector (chr) and second vector (the autosome and sex chromosome names), recycling the shorter vector chr. paste() can also paste all these results together into a single string (see paste()’s argument collapse).

![](images/page_281_image_7.jpg)

## Extracting Multiple Values from a String

For some strings, like “chr10:158395-172881,” we might want to extract several chunks. Processing the same string many times to extract different parts is not efficient. A better solution is to combine sub() and strsplit():

```txt
> region <- "chr10:158395-172881"
> chunks <- sub("(chr[\d+MYX]+):(\d+)-(\d+)",
              "\\1;;\2;;\3",
              region, perl=TRUE)
> strsplit(chunks, ";;")
[[1]]
[1] "chr10"  "158395" "172881"
```

The final function essential to string processing in R is strsplit(x, split), which splits string x by split. Like R’s other string processing functions, strsplit() supports optional perl and fixed arguments. For example, if we had a string like gene=LEAFY;locus=2159208;gene\_model=AT5G61850.1 and we wished to extract each part, we’d need to split by “;”:

```txt
> leafy <- "gene=LEAFY;locus=2159208;gene_model=AT5G61850.1"
> strsplit(leafy, ";")
[[1]]
[1] "gene=LEAFY"      "locus=2159208"      "gene_model=AT5G61850.1"
```

Also, like all of R’s other string functions, strsplit() is vectorized, so it can process entire character vectors at once. Because the number of split chunks can vary, strsplit() always returns results in a list.

## Developing Workflows with R Scripts

In the last part of this section, we’ll focus on some topics that will help you develop the data analysis techniques we’ve learned so far into reusable workflows stored in scripts. We’ll look at control flow, R scripts, workflows for working with many files, and exporting data.

## Control Flow: if, for, and while

You might have noticed that we’ve come this far in the chapter without using any control flow statements common in other languages, such as if, for, or while. Many data analysis tasks in R don’t require modifying control flow, and we can avoid using loops by using R’s apply functions like lapply(), sapply(), and mapply(). Still, there are some circumstances where we need these classic control flow and looping statements. The basic syntax of if, for, and while are:

```txt
if (x == some_value) {
    # do some stuff in here
} else {
    # else is optional
}

for (element in some_vector) {
    # iteration happens here
}

while (something_is_true) {
    # do some stuff
}
```

You can break out of for and while loops with a break statement, and advance loops to the next iteration with next. If you do find you need loops in your R code, read the additional notes about loops and pre-allocation in this chapter’s README on Git‐Hub.

![](images/page_283_image_1.jpg)

## Iterating over Vectors

In for loops, it’s common to create a vector of indexes like:

```txt
for (i in 1:length(vec)) {
    # do something
}
```

However, there’s a subtle gotcha here—if the vector vec has no elements, it’s length is 0, and 1:0 would return the sequence 1, 0. The behavior we want is for the loop to not be evaluated at all. R provides the function seq\_along() to handle this situation safely:

```txt
> vec <- rnorm(3)
> seq_along(vec)
[1] 1 2 3
> seq_along(numeric(0)) # numeric(0) returns an empty
                                # numeric vector
integer(0)
```

seq\_len(length.out) is a similar function, which returns a sequence length.out elements long.

R also has a vectorized version of if: the ifelse function. Rather than control program flow, ifelse(test, yes, no) returns the yes value for all TRUE cases of test, and no for all FALSE cases. For example:

```txt
> x <- c(-3, 1, -5, 2)
> ifelse(x < 0, -1, 1)
[1] -1 1 -1 1
```

## Working with R Scripts

Although we’ve learned R interactively though examples in this chapter, in practice your analyses should be kept in scripts that can be run many times throughout development. Scripts can be organized into project directories (see Chapter 2) and checked into Git repositories (see Chapter 5). There’s also a host of excellent R tools to help in creating well-documented, reproducible projects in R; see the following sidebar for examples.

## Reproducibility with Knitr and Rmarkdown

For our work to be reproducible (and to make our lives easier if we need to revisit code in the future), it’s essential that our code is saved, version controlled, and well documented. Although in-code comments are a good form of documentation, R has two related packages that go a step further and create reproducible project reports:

knitr and Rmarkdown. Both packages allow you to integrate chunks of R code into your text documents (such as a lab notebook or manuscript), so you can describe your data and analysis steps. Then, you can render (also known as “knit”) your document, which runs all R code and outputs the result in a variety of formats such as HTML or PDF (using LaTeX). Images, tables, and other output created by your R code will also appear in your finalized rendered document. Each document greatly improves reproducibility by integrating code and explanation (an approach inspired by Donald Knuth’s literate programming, which was discussed in “Unix Data Tools and the Unix One-Liner Approach: Lessons from Programming Pearls” on page 125).

While we don’t have the space to cover these packages in this chapter, both are easy to learn on your own with resources online. If you’re just beginning R, I’d recommend starting with Rmarkdown. Rmarkdown is well integrated into RStudio and is very easy to use. R code is simply woven between Markdown text using a simple syntax:

The following code draws 100 random normally distributed value and finds their mean:

```txt
set.seed(0)
x <- rnorm(100)
mean(x)
...
```

Then, you can save and call Rmarkdown’s render() on this file—creating an HTML version containing the documentation, code, and the results of the R block between {r} and \`\`\`. There are numerous other options; the best introductions are:

• [RStudio’s Rmarkdown tutorial](http://bit.ly/rstudio-rmkdwn)
• [Karl Broman’s knitr in a knutshell](http://kbroman.org/knitr_knutshell/)
• [Minimal Examples of Knitr](http://yihui.name/knitr/demo/minimal/)

You can run R scripts from R using the function source(). For example, to execute an R script named my\_analysis.R use:

**> source**("my\_analysis.R")

As discussed in “Loading Data into R” on page 194, it’s important to mind R’s working directory. Scripts should not use setwd() to set their working directory, as this is not portable to other systems (which won’t have the same directory structure). For the same reason, use relative paths like data/achievers.txt when loading in data, and not absolute paths like /Users/jlebowski/data/achievers.txt (as point also made in “Project Directories and Directory Structures” on page 21). Also, it’s a good idea to indicate (either in comments or a README file) which directory the user should set as their working directory.

Alternatively, we can execute a script in batch mode from the command line with:

\$ Rscript --vanilla my\_analysis.R

This comes in handy when you need to rerun an analysis on different files or with different arguments provided on the command line. I recommend using --vanilla because by default, Rscript will restore any past saved environments and save its current environment after the execution completes. Usually we don’t want R to restore any past state from previous runs, as this can lead to irreproducible results (because how a script runs depends on files only on your machine). Additionally, saved environments can make it a nightmare to debug a script. See R --help for more information.

## Reproducibility and sessionInfo()

Versions of R and any R packages installed change over time. This can lead to reproducibility headaches, as the results of your analyses may change with the changing version of R and R packages. Solving these issues is an area of ongoing development (see, for example, [the packrat package](http://rstudio.github.io/packrat/)). At the very least, you should always record the versions of R and any packages you use for an analysis. R actually makes this incredibly easy to do—just call the sessionInfo() function:

```txt
> sessionInfo()
R version 3.1.2 (2014-10-31)
Platform: x86_64-apple-darwin14.0.0 (64-bit)

locale:
[1] en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8
[...]

loaded via a namespace (and not attached):
 [1] assertthat_0.1    colorspace_1.2-4 DBI_0.3.1      digest_0.6.4
 [5] gtable_0.1.2     labeling_0.3      lattice_0.20-29 lazyeval_0.1.10
[17] scales_0.2.4     stringr_0.6.2      tools_3.1.2

[...]
```

Lastly, if you want to retrieve command-line arguments passed to your script, use R’s commandArgs() with trailingOnly=TRUE. For example, this simple R script just prints all arguments:

```markdown
## args.R -- a simple script to show command line args
args <- commandArgs(TRUE)
print(args)
```

We run this with:

\$ Rscript --vanilla args.R arg1 arg2 arg3

[1] "arg1" "arg2" "arg3"

## Workflows for Loading and Combining Multiple Files

In bioinformatics projects, sometimes loading data into R can be half the battle. Loading data is nontrivial whenever data resides in large files and when it’s scattered across many files. We’ve seen some tricks to deal with large files in “Loading Data into R” on page 194 and we’ll see a different approach to this problem when we cover databases in Chapter 13. In this section, we’ll learn some strategies and workflows for loading and combining multiple files. These workflows tie together many of the R tools we’ve learned so far: lapply(), do.call(), rbind(), and string functions like sub().

Let’s step through how to load and combine multiple tab-delimited files in a directory. Suppose you have a directory containing genome-wide hotspot data separated into different files by chromosome. Data split across many files is a common result of pipelines that have been parallelized by chromosome. I’ve created example data of this nature in this chapter’s GitHub repository under the hotspots/ directory:

```txt
$ ls -l hotspots
[vinceb]% ls -l hotspots
total 1160
-rw-r--r-- 1 vinceb staff 42041 Feb 11 13:54 hotspots_chr1.bed
-rw-r--r-- 1 vinceb staff 26310 Feb 11 13:54 hotspots_chr10.bed
-rw-r--r-- 1 vinceb staff 24760 Feb 11 13:54 hotspots_chr11.bed
[...]
```

The first step to loading this data into R is to programmatically access these files from R. If your project uses a well-organized directory structure and consistent filenames (see Chapter 2), this is easy. R’s function list.files() lists all files in a specific directory. Optionally, list.files() takes a regular-expression pattern used to select matching files. In general, it’s wise to use this pattern argument to be as restrictive as possible so as to prevent problems if a file accidentally ends up in your data directory. For example, to load in all chromosomes’ .bed files:

```txt
> list.files("hotspots", pattern="hotspots.*\\.bed")
[1] "hotspots_chr1.bed"  "hotspots_chr10.bed" "hotspots_chr11.bed"
[4] "hotspots_chr12.bed" "hotspots_chr13.bed" "hotspots_chr14.bed"
[...]
```

Note that our regular expression needs to use two backslashes to escape the period in the .bed extension. list.files() also has an argument that returns full relative paths to each file:

```txt
> hs_files <- list.files("hotspots", pattern="hotspots.*\\.bed", full.names=TRUE)
> hs_files
[1] "hotspots/hotspots_chr1.bed"  "hotspots/hotspots_chr10.bed"
```

```txt
[3] "hotspots/hotspots_chr11.bed" "hotspots/hotspots_chr12.bed"
[...]
```

We’ll use the hs\_files vector because it includes the path to each file. list.files() has other useful arguments; see help(list.files) for more information.

With list.files() programmatically listing our files, it’s then easy to lapply() a function that loads each file in. For example:

```txt
> bedcols <- c("chr", "start", "end")
> loadFile <- function(x) read.delim(x, header=FALSE, col.names=bedcols)
> hs <- lapply(hs_files, loadFile)
> head(hs[[1]])
    chr   start     end
1 chr1 1138865 1161866
2 chr1 2173749 2179750
3 chr1 2246749 2253750
[...]
```

Often, it’s useful to name each list item with the filename (sans full path). For example:

```txt
> names(hs) <- list.files("hotspots", pattern="hotspots.*\\.bed")
```

Now, we can use do.call() and rbind to merge this data together:

```txt
> hsd <- do.call(rbind, hs)
> head(hsd)
                  chr  start   end
hotspots_chr1.bed.1 chr1 1138865 1161866
hotspots_chr1.bed.2 chr1 2173749 2179750
hotspots_chr1.bed.3 chr1 2246749 2253750
[...]
> row.names(hsd) <- NULL
```

rbind() has created some row names for us (which aren’t too helpful), but you can remove them with row.names(hsd) <- NULL.

Often, we need to include a column in our dataframe containing meta-information about files that’s stored in each file’s filename. For example, if you had to load in multiple samples’ data like sampleA\_repl01.txt, sampleA\_repl02.txt, …, sampleC\_repl01.txt you will likely want to extract the sample name and replicate information and attach these as columns in your dataframe. As a simple example of this, let’s pretend we did not have the column chr in our hotspot files and needed to extract this information from each filename using sub(). We’ll modify our load File() function accordingly:

```r
loadFile <- function(x) {
  # read in a BED file, extract the chromosome name from the file,
  # and add it as a column
  df <- read.delim(x, header=FALSE, col.names=bedcols)
  df\$chr_name <- sub("hotspots_([^\\.]+)\.bed", "\\1", basename(x))
```