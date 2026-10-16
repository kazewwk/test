| 0000010 | G | C | T | A | G | C | T | A | C | T | A | G | C | A | G | C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0000020 | T | A | C | T | A | C | G | A | G | C | A | T | C | T | A | C |
| 0000030 | G | G | C | G | C | G | A | T | C | T | A | C | G | \\n | > | b |
| 0000040 | a | d | - | s | e | q | u | e | n | c | e | \\n | G | A | T | C |
| 0000050 | A | G | G | C | G | A | C | A | T | C | G | A | G | C | T | A |
| 0000060 | T | C | A | C | T | A | C | G | A | G | C | G | A | G | 221 |  |
| 0000070 | G | A | T | C | A | G | C | T | A | T | T | \\n |  |  |  |  |
| 000007c |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

As we can see, the character after “CGAGCGAG” in the second sequence is clearly not an ASCII character. Another way to see non-ASCII characters is using grep. This command is a bit tricky (it searches for characters outside a hexadecimal range), but it’s such a specific use case there’s little reason to explain it in depth:

```shell
$ LC_CTYPE=C grep --color='auto' -P "[\x80-\xFF]" improper.fa
GATCAGGCGACATCGAGCTATCACTACGAGCGAG[m♦GATCAGCTATT
```

Note that this does not work with BSD grep, the version that comes with Mac OS X. Another useful grep option to add to this is -n, which adds line numbers to each matching line. On my systems, I have this handy line aliased to nonascii in my shell configuration file (often \~/.bashrc or \~/.profile):

```shell
$ alias nonascii="LC_CTYPE=C grep --color='auto' -n -P '[\x80-\xFF]'"
```

Overall, file, hexdump, and the grep command are useful for those situations where something isn’t behaving correctly and you suspect a file’s encoding may be to blame (which happened even during preparing this book’s test data!). This is especially common with data curated by hand, by humans; always be wary of passing these files without inspection into an analysis pipeline.

## Sorting Plain-Text Data with Sort

Very often we need to work with sorted plain-text data in bioinformatics. The two most common reasons to sort data are as follows:

• Certain operations are much more efficient when performed on sorted data.
• Sorting data is a prerequisite to finding all unique lines, using the Unix sort | uniq idiom.

We’ll talk much more about sort | uniq in the next section; here we focus on how to sort data using sort.

First, like cut, sort is designed to work with plain-text data with columns. Running sort without any arguments simply sorts a file alphanumerically by line:

<table><tr><td colspan="3">$ cat example.bed</td></tr><tr><td>chr1</td><td>26</td><td>39</td></tr><tr><td>chr1</td><td>32</td><td>47</td></tr><tr><td>chr3</td><td>11</td><td>28</td></tr><tr><td>chr1</td><td>40</td><td>49</td></tr><tr><td>chr3</td><td>16</td><td>27</td></tr><tr><td>chr1</td><td>9</td><td>28</td></tr><tr><td>chr2</td><td>35</td><td>54</td></tr><tr><td>chr1</td><td>10</td><td>19</td></tr><tr><td colspan="3">$ sort example.bed</td></tr><tr><td>chr1</td><td>10</td><td>19</td></tr><tr><td>chr1</td><td>26</td><td>39</td></tr><tr><td>chr1</td><td>32</td><td>47</td></tr><tr><td>chr1</td><td>40</td><td>49</td></tr><tr><td>chr1</td><td>9</td><td>28</td></tr><tr><td>chr2</td><td>35</td><td>54</td></tr><tr><td>chr3</td><td>11</td><td>28</td></tr><tr><td>chr3</td><td>16</td><td>27</td></tr></table>

Because chromosome is the first column, sorting by line effectively groups chromosomes together, as these are “ties” in the sorted order. Grouped data is quite useful, as we’ll see.

![](images/page_177_image_2.jpg)

## Using Different Delimiters with sort

By default, sort treats blank characters (like tab or spaces) as field delimiters. If your file uses another delimiter (such as a comma for CSV files), you can specify the field separator with -t (e.g., -t",").

However, using sort’s defaults of sorting alphanumerically by line doesn’t handle tabular data properly. There are two new features we need:

• The ability to sort by particular columns
• The ability to tell sort that certain columns are numeric values (and not alpha numeric text; see the Tip "Leading Zeros and Sorting" in Chapter 2 for an example of the difference)

sort has a simple syntax to do this. Let’s look at how we’d sort example.bed by chromosome (first column), and start position (second column):

<table><tr><td colspan="3">$ sort -k1,1 -k2,2n example.bed</td></tr><tr><td>chr1</td><td>9</td><td>28</td></tr><tr><td>chr1</td><td>10</td><td>19</td></tr><tr><td>chr1</td><td>26</td><td>39</td></tr><tr><td>chr1</td><td>32</td><td>47</td></tr><tr><td>chr1</td><td>40</td><td>49</td></tr><tr><td>chr2</td><td>35</td><td>54</td></tr><tr><td>chr3</td><td>11</td><td>28</td></tr><tr><td>chr3</td><td>16</td><td>27</td></tr></table>

Here, we specify the columns (and their order) we want to sort by as -k arguments. In technical terms, -k specifies the sorting keys and their order. Each -k argument takes a range of columns as start,end, so to sort by a single column we use start,start. In the preceding example, we first sorted by the first column (chromosome), as the first -k argument was -k1,1. Sorting by the first column alone leads to many ties in rows with the same chromosomes (e.g., “chr1” and “chr3”). Adding a second -k argument with a different column tells sort how to break these ties. In our example, -k2,2n tells sort to sort by the second column (start position), treating this column as numerical data (because there’s an n in -k2,2n).

The end result is that rows are grouped by chromosome and sorted by start position. We could then redirect the standard output stream of sort to a file:

```txt
\$ sort -k1,1 -k2,2n example.bed > example_sorted.bed
```

If you need all columns to be sorted numerically, you can use the argument -n rather than specifying which particular columns are numeric with a syntax like -k2,2n.

Understanding the -k argument syntax is so important we’re going to step through one more example. The Mus\_musculus.GRCm38.75\_chr1\_random.gtf file is Mus\_musculus.GRCm38.75\_chr1.gtf with permuted rows (and without a metadata header). Let’s suppose we wanted to again group rows by chromosome, and sort by position. Because this is a GTF file, the first column is chromosome and the fourth column is start position. So to sort this file, we’d use:

```csv
\$ sort -k1,1 -k4,4n Mus_musculus.GRCm38.75_chr1_random.gtf > \
Mus_musculus.GRCm38.75_chr1_sorted.gtf
```

![](images/page_178_image_6.jpg)

## Sorting Stability

There’s one tricky technical detail about sorting worth being aware of: sorting stability. To understand stable sorting, we need to go back and think about how lines that have identical sorting keys are handled. If two lines are exactly identical according to all sorting keys we’ve specified, they are indistinguishable and equivalent when being sorted. When lines are equivalent, sort will sort them according to the entire line as a last-resort effort to put them in some order. What this means is that even if the two lines are identical according to the sorting keys, their sorted order may be different from the order they appear in the original file. This behavior makes sort an unstable sort.

If we don’t want sort to change the order of lines that are equal according to our sort keys, we can specify the -s option. -s turns off this last-resort sorting, thus making sort a stable sorting algorithm.

Sorting can be computationally intensive. Unlike Unix tools, which operate on a single line a time, sort must compare multiple lines to sort a file. If you have a file that you suspect is already sorted, it’s much cheaper to validate that it’s indeed sorted rather than resort it. We can check if a file is sorted according to our -k arguments using -c:

```shell
$ sort -k1,1 -k2,2n -c example_sorted.bed ①
$ echo $?
0
$ sort -k1,1 -k2,2n -c example.bed ②
sort: example.bed:4: disorder: chr1      40      49
$ echo $?
1
```

This file is already sorted by -k1,1 -k2,2n -c, so sort exits with exit status 0 (true).
This file is not already sorted by -k1,1 -k2,2n -c, so sort returns the first outof-order row it finds and exits with status 1 (false).

It’s also possible to sort in reverse order with the -r argument:

```shell
$ sort -k1,1 -k2,2n -r example.bed
chr3    11      28
chr3    16      27
chr2    35      54
chr1    9      28
chr1    10      19
chr1    26      39
chr1    32      47
chr1    40      49
```

If you’d like to only reverse the sorting order of a single column, you can append r on that column’s -k argument:

```txt
$ sort -k1,1 -k2,2nr example.bed
chr1     40      49
chr1     32      47
chr1     26      39
chr1     10      19
chr1     9      28
chr2     35      54
chr3     16      27
chr3     11      28
```

In this example, the effect is to keep the chromosomes sorted in alphanumeric ascending order, but sort the second column of start positions in descending numeric order.

There are a few other useful sorting options to discuss, but these are available for GNU sort only (not the BSD version as found on OS X). The first is -V, which is a clever alphanumeric sorting routine that understands numbers inside strings. To see why this is useful, consider the file example2.bed. Sorting with sort -k1,1 -k2,2n groups chromosomes but doesn’t naturally order them as humans would:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
cat example2.bed
chr2     15      19
chr22   32      46
chr10   31      47
chr1    34      49
chr11   6      16
chr2    17      22
chr2    27      46
chr10   30      42
$ sort -k1,1 -k2,2n example2.bed
chr1     34      49
chr10   30      42
chr10   31      47
chr11   6      16
chr2    15      19
chr2    17      22
chr2    27      46
chr22   32      46
</div>

Here, “chr2” is following “chr11” because the character “1” falls before “2”—sort isn’t sorting by the number in the text. However, with V appended to -k1,1 we get the desired result:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$ sort -k1,1V -k2,2n example2.bed
chr1     34       49
chr2     15       19
chr2     17       22
chr2     27       46
chr10   30       42
chr10   31       47
chr11    6       16
chr22    32       46
</div>

In practice, Unix sort scales well to the moderately large text data we’ll need to sort in bioinformatics. sort does this by using a sorting algorithm called merge sort. One nice feature of the merge sort algorithm is that it allows us to sort files larger than fit in our memory by storing sorted intermediate files on the disk. For large files, reading and writing these sorted intermediate files to the disk may be a bottleneck (remember: disk operations are very slow). Under the hood, sort uses a fixed-sized memory buffer to sort as much data in-memory as fits. Increasing the size of this buffer allows more data to be sorted in memory, which reduces the amount of temporary sorted files that need to be written and read off the disk. For example:

\$ sort -k1,1 -k4,4n -S2G Mus\_musculus.GRCm38.75\_chr1\_random.gtf

The -S argument understands suffixes like K for kilobyte, M for megabyte, and G for gigabyte, as well as % for specifying what percent of total memory to use (e.g., 50% with -S 50%).

Another option (only available in GNU sort) is to run sort with the --parallel option. For example, to use four cores to sort Mus\_musculus.GRCm38.75\_chr1\_random.gtf:

```batch
\$ sort -k1,1 -k4,4n --parallel 4 Mus_musculus.GRCm38.75_chr1_random.gtf
```

But note that Mus\_musculus.GRCm38.75\_chr1\_random.gtf is much too small for either increasing the buffer size or parallelization to make any difference. In fact, because there is a fixed cost to parallelizing operations, parallelizing an operation run on a small file could actually be slower! In general, don’t obsess with performance tweaks like these unless your data is truly large enough to warrant them.

So, when is it more efficient to work with sorted output? As we’ll see when we work with range data in Chapter 9, working with sorted data can be much faster than working with unsorted data. Many tools have better performance when working on sorted files. For example, BEDTools’ bedtools intersect allows the user to indicate whether a file is sorted with -sorted. Using bedtools intersect with a sorted file is both more memory-efficient and faster. Other tools, like tabix (covered in more depth in “Fast Access to Indexed Tab-Delimited Files with BGZF and Tabix” on page 425) require that we presort files before indexing them for fast random-access.

## Finding Unique Values in Uniq

Unix’s uniq takes lines from a file or standard input stream, and outputs all lines with consecutive duplicates removed. While this is a relatively simple functionality, you will use uniq very frequently in command-line data processing. Let’s first see an example of its behavior:

```txt
$ cat letters.txt
A
A
B
C
B
C
C
C
$ uniq letters.txt
A
B
C
B
C
```

As you can see, uniq does not return the unique values letters.txt—it only removes consecutive duplicate lines (keeping one). If instead we did want to find all unique lines in a file, we would first sort all lines using sort so that all identical lines are grouped next to each other, and then run uniq. For example:

```txt
\$ sort letters.txt | uniq
A
B
C
```

If we had lowercase letters mixed in this file as well, we could add the option -i to uniq to be case insensitive.

uniq also has a tremendously useful option that’s used very often in command-line data processing: -c. This option shows the counts of occurrences next to the unique lines. For example:

```shell
$ uniq -c letters.txt
    2 A
    1 B
    1 C
    1 B
    3 C
$ sort letters.txt | uniq -c
    2 A
    2 B
    4 C
```

Both sort | uniq and sort | uniq -c are frequently used shell idioms in bioinformatics and worth memorizing. Combined with other Unix tools like grep and cut, sort and uniq can be used to summarize columns of tabular data:

```shell
$ grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf | cut -f3 | sort | uniq -c
25901 CDS
7588 UTR
36128 exon
2027 gene
2290 start_codon
2299 stop_codon
4993 transcript
```

If we wanted these counts in order from most frequent to least, we could pipe these results to sort -rn:

```shell
$ grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf | cut -f3 | sort | uniq -c | \
    sort -rn
36128 exon
25901 CDS
7588 UTR
4993 transcript
2299 stop_codon
```

```txt
2290 start_codon
2027 gene
```

Because sort and uniq are line-based, we can create lines from multiple columns to count combinations, like how many of each feature (column 3 in this example GTF) are on each strand (column 7):

```shell
$ grep -v "^#" Mus_musculus.GRCm38.75_chr1.gtf | cut -f3,7 | sort | uniq -c
12891 CDS +  
13010 CDS -  
3754 UTR +  
3834 UTR -  
18134 exon +  
17994 exon -  
1034 gene +  
993 gene -  
1135 start_codon +  
1155 start_codon -  
1144 stop_codon +  
1155 stop_codon -  
2482 transcript +  
2511 transcript -
```

Or, if you want to see the number of features belonging to a particular gene identifier:

```shell
$ grep "ENSMUSG00000033793" Mus_musculus.GRCm38.75_chr1.gtf | cut -f3 | sort \
| uniq -c
13 CDS
 3 UTR
14 exon
 1 gene
 1 start_codon
 1 stop_codon
 1 transcript
```

These count tables are incredibly useful for summarizing columns of categorical data. Without having to load data into a program like R or Excel, we can quickly calculate summary statistics about our plain-text data files. Later on in Chapter 11, we’ll see examples involving more complex alignment data formats like SAM.

uniq can also be used to check for duplicates with the -d option. With the -d option, uniq outputs duplicated lines only. For example, the mm\_gene\_names.txt file (which contains a list of gene names) does not have duplicates:

```shell
$ uniq -d mm_gene_names.txt
# no output
$ uniq -d mm_gene_names.txt | wc -l
0
```

A file with duplicates, like the test.bed file, has multiple lines returned:

```batch
uniq -d test.bed | wc -l
22925
```

## Join

The Unix tool join is used to join different files together by a common column. This is easiest to understand with simple test data. Let’s use our example.bed BED file, and example\_lengths.txt, a file containing the same chromosomes as example.bed with their lengths. Both files look like this:

```shell
$ cat example.bed
chr1     26       39
chr1     32       47
chr3     11       28
chr1     40       49
chr3     16       27
chr1     9       28
chr2     35       54
chr1     10       19
$ cat example_lengths.txt
chr1     58352
chr2     39521
chr3     24859
```

Our goal is to append the chromosome length alongside each feature (note that the result will not be a valid BED-formatted file, just a tab-delimited file). To do this, we need to join both of these tabular files by their common column, the one containing the chromosome names (the first column in both example.bed and example\_lengths.txt).

To append the chromosome lengths to example.bed, we first need to sort both files by the column to be joined on. This is a vital step—Unix’s join will not work unless both files are sorted by the column to join on. We can appropriately sort both files with sort:

```shell
$ sort -k1,1 example.bed > example_sorted.bed
$ sort -c -k1,1 example_lengths.txt # verifies is already sorted
```

Now, let’s use join to join these files, appending the chromosome lengths to our example.bed file. The basic syntax is join -1 &lt;file_1_field&gt; -2 &lt;file_2_field&gt; &lt;file_1&gt; &lt;file_2&gt;, where &lt;file_1&gt; and &lt;file_2&gt; are the two files to be joined by a column &lt;file_1_field&gt; in &lt;file_1&gt; and column &lt;file_2_field&gt; in &lt;file_2&gt;. So, with example.bed and example\_lengths.txt this would be:

```shell
$ join -1 1 -2 1 example_sorted.bed example_lengths.txt
> example_with_lengths.txt
$ cat example_with_lengths.txt
chr1 10 19 58352
chr1 26 39 58352
chr1 32 47 58352
chr1 40 49 58352
chr1 9 28 58352
chr2 35 54 39521
```

```txt
chr3 11 28 24859
chr3 16 27 24859
```

There are many types of joins; we will talk about each kind in more depth in Chapter 13. For now, it’s important that we make sure join is working as we expect. Our expectation is that this join should not lead to fewer rows than in our example.bed file. We can verify this with wc -l:

```txt
$ wc -l example_sorted.bed example_with_lengths.txt
     8 example_sorted.bed
     8 example_with_lengths.txt
    16 total
```

We see that we have the same number of lines in our original file and our joined file. However, look what happens if our second file, example\_lengths.txt, is truncated such that it doesn’t have the lengths for chr3:

```powershell
$ head -n2 example_lengths.txt > example_lengths_alt.txt # truncate file
$ join -1 1 -2 1 example_sorted.bed example_lengths_alt.txt
chr1 10 19 58352
chr1 26 39 58352
chr1 32 47 58352
chr1 40 49 58352
chr1 9 28 58352
chr2 35 54 39521
$ join -1 1 -2 1 example_sorted.bed example_lengths_alt.txt | wc -l
6
```

Because chr3 is absent from example\_lengths\_alt.txt, our join omits rows from example\_sorted.bed that do not have an entry in the first column of example\_lengths\_alt.txt. In some cases (such as this), we don’t want this behavior. GNU join implements the -a option to include unpairable lines—ones that do not have an entry in either file. (This option is not implemented in BSD join.) To use -a, we specify which file is allowed to have unpairable entries:

```shell
$ join -1 1 -2 1 -a 1 example_sorted.bed example_lengths_alt.txt # GNU join only
chr1 10 19 58352
chr1 26 39 58352
chr1 32 47 58352
chr1 40 49 58352
chr1 9 28 58352
chr2 35 54 39521
chr3 11 28
chr3 16 27
```

Unix’s join is just one of many ways to join data, and is most useful for simple quick joins. Joining data by a common column is a common task during data analysis; we’ll see how to do this in R and with SQLite in future chapters.

## Text Processing with Awk

Throughout this chapter, we’ve seen how we can use simple Unix tools like grep, cut, and sort to inspect and manipulate plain-text tabular data in the shell. For many trivial bioinformatics tasks, these tools allow us to get the job done quickly and easily (and often very efficiently). Still, some tasks are slightly more complex and require a more expressive and powerful tool. This is where the language and tool Awk excels— extracting data from and manipulating tabular plain-text files. Awk is a tiny, specialized language that allows you to do a variety of text-processing tasks with ease.

We’ll introduce the basics of Awk in this section—enough to get you started with using Awk in bioinformatics. While Awk is a fully fledged programming language, it’s a lot less expressive and powerful than Python. If you need to implement something complex, it’s likely better (and easier) to do so in Python. The key to using Awk effectively is to reserve it for the subset of tasks it’s best at: quick data-processing tasks on tabular data. Learning Awk also prepares us to learn bioawk, which we’ll cover in “Bioawk: An Awk for Biological Formats” on page 163.

![](images/page_186_image_3.jpg)

## Gawk versus Awk

As with many other Unix tools, Awk comes in a few flavors. First, you can still find the original Awk written by Alfred Aho, Peter Weinberger, and Brian Kernighan (whose last names create the name Awk) on some systems. If you use Mac OS X, you’ll likely be using the BSD Awk. There’s also GNU Awk, known as Gawk, which is based on the original Awk but has many extended features (and an excellent manual; see man gawk). In the examples in this section, I’ve stuck to a common subset of Awk functionality shared by all these Awks. Just take note that there are multiple Awk implementations. If you find Awk useful in your work (which can be a personal preference), it’s worthwhile to use Gawk.

To learn Awk, we’ll cover two key parts of the Awk language: how Awk processes records, and pattern-action pairs. After understanding these two key parts the rest of the language is quite simple.

First, Awk processes input data a record at a time. Each record is composed of fields, separate chunks that Awk automatically separates. Because Awk was designed to work with tabular data, each record is a line, and each field is a column’s entry for that record. The clever part about Awk is that it automatically assigns the entire record to the variable \$0, and field one’s value is assigned to \$1, field two’s value is assigned to \$2, field three’s value is assigned to \$3, and so forth.

Second, we build Awk programs using one or more of the following structures:

pattern { action }

Each pattern is an expression or regular expression pattern. Patterns are a lot like if statements in other languages: if the pattern’s expression evaluates to true or the regular expression matches, the statements inside action are run. In Awk lingo, these are pattern-action pairs and we can chain multiple pattern-action pairs together (separated by semicolons). If we omit the pattern, Awk will run the action on all records. If we omit the action but specify a pattern, Awk will print all records that match the pattern. This simple structure makes Awk an excellent choice for quick text-processing tasks. This is a lot to take in, but these two basic concepts—records and fields, and pattern-action pairs—are the foundation of writing text-processing programs with Awk. Let’s see some examples.

First, we can simply mimic cat by omitting a pattern and printing an entire record with the variable \$0:

```txt
$ awk '{ print $0 }' example.bed
chr1     26      39
chr1     32      47
chr3     11      28
chr1     40      49
chr3     16      27
chr1     9      28
chr2     35      54
chr1     10      19
```

print prints a string. Optionally, we could omit the \$0, because print called without an argument would print the current record.

Awk can also mimic cut:

```txt
$ awk '{ print $2 "\t" $3 }' example.bed
26         39
32         47
11         28
40         49
16         27
9         28
35         54
10         19
```

Here, we’re making use of Awk’s string concatenation. Two strings are concatenated if they are placed next to each other with no argument. So for each record, \$2"\t"\$3 concatenates the second field, a tab character, and the third field. This is far more typing than cut -f2,3, but demonstrates how we can access a certain column’s value for the current record with the numbered variables \$1, \$2, \$3, etc.

Let’s now look at how we can incorporate simple pattern matching. Suppose we wanted to write a filter that only output lines where the length of the feature (end position - start position) was greater than 18. Awk supports arithmetic with the standard operators +, -, \*, /, % (remainder), and ^ (exponentiation). We can subtract within a pattern to calculate the length of a feature, and filter on that expression:

```txt
$ awk '$3 - $2 > 18' example.bed
chr1       9          28
chr2       35          54
```

See Table 7-2 for reference to Awk comparison and logical operators.

Table 7-2. Awk comparison and logical operations

| Comparison | Description |
| --- | --- |
| a == b | a is equal to b |
| a != b | a is not equal to b |
| a &lt; b | a is less than b |
| a > b | a is greater than b |
| a &lt;= b | a is less than or equal to b |
| a >= b | a is greater than or equal to b |
| a ~ b | a matches regular expression pattern b |
| a !~ b | a does not match regular expression pattern b |
| a &amp;&amp; b | logical and a and b |
| a \|\| b | logical or a and b |
| !a | not a (logical negation) |

We can also chain patterns, by using logical operators && (AND), || (OR), and ! (NOT). For example, if we wanted all lines on chromosome 1 with a length greater than 10:

```shell
$ awk '$1 ~ /chr1/ && $3 - $2 > 10' example.bed
chr1       26         39
chr1       32         47
chr1       9         28
```

The first pattern, \$1 \~ /chr1/, is how we specify a regular expression. Regular expressions are in slashes. Here, we’re matching the first field, \$1\$, against the regular expression chr1. The tilde, \~ means match; to not match the regular expression we would use !\~ (or !(\$1 \~ /chr1/)).

We can combine patterns and more complex actions than just printing the entire record. For example, if we wanted to add a column with the length of this feature (end position - start position) for only chromosomes 2 and 3, we could use:

```txt
$ awk '$1 ~ /chr2|chr3/ { print $0 "\t" $3 - $2 }' example.bed
chr3     11       28       17
chr3     16       27       11
chr2     35       54       19
```

So far, these exercises have illustrated two ways Awk can come in handy:

• For filtering data using rules that can combine regular expressions and arithmetic
• Reformatting the columns of data using arithmetic

These two applications alone make Awk an extremely useful tool in bioinformatics, and a huge time saver. But let’s look at some slightly more advanced use cases. We’ll start by introducing two special patterns: BEGIN and END.

Like a bad novel, beginning and end are optional in Awk. The BEGIN pattern specifies what to do before the first record is read in, and END specifies what to do after the last record’s processing is complete. BEGIN is useful to initialize and set up variables, and END is useful to print data summaries at the end of file processing. For example, suppose we wanted to calculate the mean feature length in example.bed. We would have to take the sum feature lengths, and then divide by the total number of records. We can do this with:

```powershell
$ awk 'BEGIN{ s = 0 }; { s += ($3-$2) }; END{ print "mean: " s/NR };' example.bed mean: 14
```

There’s a special variable we’ve used here, one that Awk automatically assigns in addition to \$0, \$1, \$2, etc.: NR. NR is the current record number, so on the last record NR is set to the total number of records processed. In this example, we’ve initialized a variable s to 0 in BEGIN (variables you define do not need a dollar sign). Then, for each record we increment s by the length of the feature. At the end of the records, we print this sum s divided by the number of records NR, giving the mean.

![](images/page_190_image_0.jpg)

## Setting Field, Output Field, and Record Separators

While Awk is designed to work with whitespace-separated tabular data, it’s easy to set a different field separator: simply specify which separator to use with the -F argument. For example, we could work with a CSV file in Awk by starting with awk -F",".

It’s also possible to set the record (RS), output field (OFS), and output record (ORS) separators. These variables can be set using Awk’s -v argument, which sets a variable using the syntax awk -v VAR=val. So, we could convert a three-column CSV to a tab file by just setting the field separator F and output field separator OFS: awk -F"," -v OFS="\t" {print \$1,\$2,\$3}. Setting OFS="\t" saves a few extra characters when outputting tab-delimited results with statements like print "\$1 "\t" \$2 "\t" \$3.

We can use NR to extract ranges of lines, too; for example, if we wanted to extract all lines between 3 and 5 (inclusive):

```txt
awk 'NR >= 3 && NR <= 5' example.bed
chr3       11          28
chr1       40          49
chr3       16          27
```

Awk makes it easy to convert between bioinformatics files like BED and GTF. For example, we could generate a three-column BED file from Mus\_musculus.GRCm38.75\_chr1.gtf as follows:

```shell
$ awk '!/^#/ { print $1 "\t" $4-1 "\t" $5 }' Mus_musculus.GRCm38.75_chr1.gtf | \
head -n 3
1       3054232 3054733
1       3054232 3054733
1       3054232 3054733
```

Note that we subtract 1 from the start position to convert to BED format. This is because BED uses zero-indexing while GTF uses 1-indexing; we’ll learn much more about this in Chapter 10. This is a subtle detail, certainly one that’s been missed many times. In the midst of analysis, it’s easy to miss these small details.

Awk also has a very useful data structure known as an associative array. Associative arrays behave like Python’s dictionaries or hashes in other languages. We can create an associative array by simply assigning a value to a key. For example, suppose we wanted to count the number of features (third column) belonging to the gene “Lypla1.” We could do this by incrementing their values in an associative array:

```txt
# This example has been split on multiple lines to improve readability
$ awk '/Lypla1/ { feature[$3] += 1 }; \
    END { for (k in feature)          \
    print k "\t" feature[k] }' Mus_musculus.GRCm38.75_chr1.gtf
exon            69
```

```txt
CDS          56
UTR          24
gene        1
start_codon  5
stop_codon  5
transcript  9
```

This example illustrates that Awk really is a programming language—within our action blocks, we can use standard programming statements like if, for, and while, and Awk has several useful built-in functions (see Table 7-3 for some useful common functions). However, when Awk programs become complex or start to span multiple lines, I usually prefer to switch to Python at that point. You’ll have much more functionality at your disposal for complex tasks with Python: Python’s standard library, the Python debugger (PDB), and more advanced data structures. However, this is a personal preference—there are certainly programmers who write lengthy Awk processing programs.

Table 7-3. Useful built-in Awk functions

| length(s) | Length of a string s. |
| --- | --- |
| tolower(s) | Convert string s to lowercase |
| toupper(s) | Convert string s to uppercase |
| substr(s, i, j) | Return the substring of s that starts at i and ends at j |
| split(s, x, d) | Split string s into chunks by delimiter d, place chunks in array x |
| sub(f, r, s) | Find regular expression f in s and replace it with r (modifying s in place); use gsub for global substitution; returns a positive value if string is found |

It’s worth noting that there’s an entirely Unix way to count features of a particular gene: grep, cut, sort, and uniq -c:

```shell
$ grep "Lypla1" Mus_musculus.GRCm38.75_chr1.gtf | cut -f 3 | sort | uniq -c
56 CDS
24 UTR
69 exon
1 gene
5 start_codon
5 stop_codon
9 transcript
```