```powershell
$ sqlite3 gwascat.db "SELECT * FROM gwascat" > results.txt
$ head -n 1 results.txt
1|2014-08-02|24388013|Ferreira MA|2013-12-30|J Allergy Clin Immunol| [...]
```

The sqlite3 program also has options that allow us to change how these results are returned. The option -separator can be used to specify how columns are separated (e.g., "," for CSV or "\t" for tab) and -header and -noheader can be used to display or omit the column headers.

## Limiting results with LIMIT

To avoid printing all 17,290 rows of the gwascat table, we can add a LIMIT clause to this SELECT statement. LIMIT is an optional clause that limits the number of rows that are fetched. Like the Unix command head, LIMIT can be used to take a peek at a small subset of the data:

```txt
sqlite> SELECT * FROM gwascat LIMIT 2;
id|dbdate|pubmedid|author|date|journal| [...]
1|08/02/2014|24388013|Ferreira MA|12/30/2013|J Allergy Clin Immunol| [...]
2|08/02/2014|24388013|Ferreira MA|12/30/2013|J Allergy Clin Immunol| [...]
```

Unlike the rows in a file, the order in which rows of a table are stored on disk is not guaranteed, and could change even if the data stays the same. You could execute the same SELECT query, but the order of the resulting rows may be entirely different. This is an important characteristic of relational databases, and it’s important that how you process the results from a SELECT query doesn’t depend on row ordering. Later on, we’ll see how to use an ORDER BY clause to order by one or more columns.

## Selecting columns with SELECT

There are 36 columns in the gwascat table, far too many to print on a page without wrapping (which is why I’ve cropped the previous example). Rather than selecting all columns, we can specify a comma-separated subset we care about:

```sql
sqlite> SELECT trait, chrom, position, strongest_risk_snp, pvalue
...> FROM gwascat LIMIT 5;
trait|chrom|position|strongest_risk_snp|pvalue
Asthma and hay fever|6|32658824|rs9273373|4.0e-14
Asthma and hay fever|4|38798089|rs4833095|5.0e-12
Asthma and hay fever|5|111131801|rs1438673|3.0e-11
Asthma and hay fever|2|102350089|rs10197862|4.0e-11
Asthma and hay fever|17|39966427|rs7212938|4.0e-10
```

When we’re selecting only a few columns, SQLite’s default list output mode isn’t very clear. We can adjust SQLite’s settings so results are a bit clearer:

```txt
sqlite> .header on
sqlite> .mode column
```

Now, displaying the results is a bit easier:

| trait | chrom | position | strongest_risk_snp | pvalue |
| --- | --- | --- | --- | --- |
| Asthma and hay fever | 6 | 32658824 | rs9273373 | 4.0e-14 |
| Asthma and hay fever | 4 | 38798089 | rs4833095 | 5.0e-12 |
| Asthma and hay fever | 5 | 111131801 | rs1438673 | 3.0e-11 |
| Asthma and hay fever | 2 | 102350089 | rs10197862 | 4.0e-11 |
| Asthma and hay fever | 17 | 39966427 | rs7212938 | 4.0e-10 |

In cases where there are many columns, SQLite’s list mode is usually clearer (you can turn this back on with .mode list).

## Ordering rows with ORDER BY

As mentioned earlier, the rows returned by SELECT are not ordered. Often we want to get order by a particular column. For example, we could look at columns related to the study, ordering by author’s last name:

<table><tr><td colspan="3">sqlite&gt; SELECT author, trait, journal</td></tr><tr><td colspan="3">...&gt; FROM gwascat ORDER BY author LIMIT 5;</td></tr><tr><td>author</td><td>trait</td><td>journal</td></tr><tr><td>Aberg K</td><td>Antipsychotic-induced QTc interval prolongation</td><td>Pharmacogenomics J</td></tr><tr><td>Aberg K</td><td>Antipsychotic-induced QTc interval prolongation</td><td>Pharmacogenomics J</td></tr><tr><td>Aberg K</td><td>Antipsychotic-induced QTc interval prolongation</td><td>Pharmacogenomics J</td></tr><tr><td>Aberg K</td><td>Response to antipsychotic therapy (extrapyramid</td><td>Biol Psychiatry</td></tr><tr><td>Aberg K</td><td>Response to antipsychotic therapy (extrapyramid</td><td>Biol Psychiatry</td></tr></table>

To return results in descending order, add DESC to the ORDER BY clause:

<table><tr><td colspan="3">sqlite&gt; SELECT author, trait, journal</td></tr><tr><td colspan="3">...&gt; FROM gwascat ORDER BY author DESC LIMIT 5;</td></tr><tr><td>author</td><td>trait</td><td>journal</td></tr><tr><td>van der Zanden LF</td><td>Hypospadias</td><td>Nat Genet</td></tr><tr><td>van der Valk RJ</td><td>Fractional</td><td>J Allergy</td></tr><tr><td>van der Valk RJ</td><td>Fractional</td><td>J Allergy</td></tr><tr><td>van der Valk RJ</td><td>Fractional</td><td>J Allergy</td></tr><tr><td>van der Valk RJ</td><td>Fractional</td><td>J Allergy</td></tr></table>

Remember, SQLite’s columns do not have strict types. Using ORDER BY on a column that contains a mix of data value types will follow the order: NULL values, integer and real values (sorted numerically), text values, and finally blob values. It’s especially important to note that NULL values will always be first when sorting by ascending or descending order. We can see this in action by ordering by ascending p-value:

<table><tr><td colspan="5">sqlite&gt; SELECT trait, chrom, position, strongest_risk_snp, pvalue...-&gt; FROM gwascat ORDER BY pvalue LIMIT 5;</td></tr><tr><td>trait</td><td>chrom</td><td>position</td><td>strongest_risk_snp</td><td>pvalue</td></tr><tr><td>Brain imaging</td><td></td><td></td><td>rs10932886</td><td></td></tr></table>

| Brain imaging | rs429358 |
| --- | --- |
| Brain imaging | rs7610017 |
| Brain imaging | rs6463843 |
| Brain imaging | rs2075650 |

In the next section, we’ll see how we can filter out rows with NULL values with WHICH clauses.

As discussed in Chapter 8, ordering data to look for suspicious outliers is a great way to look for problems in data. For example, consider what happens when we sort pvalues (which as a probability, must mathematically be between 0 and 1, inclusive) in descending order:

<table><tr><td colspan="3">sqlite&gt; SELECT trait, strongest_risk_snp, pvalue</td></tr><tr><td colspan="3">...&gt; FROM gwascat ORDER BY pvalue DESC LIMIT 5;</td></tr><tr><td>trait</td><td>strongest_risk_snp</td><td>pvalue</td></tr><tr><td>Serum protein levels (sST2)</td><td>rs206548</td><td>90000000.0</td></tr><tr><td>Periodontitis (Mean PAL)</td><td>rs12050161</td><td>4000000.0</td></tr><tr><td rowspan="2">Coronary artery disease or Lipid traits</td><td>rs964184</td><td>2.0e-05</td></tr><tr><td>rs10158897</td><td>9.0e-06</td></tr><tr><td>Rheumatoid arthritis</td><td>rs8032939</td><td>9.0e-06</td></tr></table>

Yikes! These two erroneous p-values likely occurred as a data entry mistake. It’s very easy to miss the negative when entering p-values in scientific notation (e.g., 9e-7 versus 9e7). Problems like these once again illustrate why it’s essential to not blindly trust your data.

## Filtering which rows with WHERE

Up until now, we’ve been selecting all rows from a database table and adding ORDER BY and LIMIT clauses to sort and limit the results. But the strength of a relational database isn’t in selecting all data from a table, it’s in using queries to select out specific informative subsets of data. We filter out particular rows using WHERE clauses, which is the heart of making queries with SELECT statements.

Let’s look at a simple example—suppose we wanted to find rows where the strongest risk SNP is rs429358:

sqlite> SELECT chrom, position, trait, strongest\_risk\_snp, pvalue...> FROM gwascat WHERE strongest\_risk\_snp = "rs429358";

| chrom | position | trait | strongest_risk_snp | pvalue |
| --- | --- | --- | --- | --- |
| 19 | 44908684 | Alzheimer's disease biomarkers | rs429358 | 5.0e-14 |
| 19 | 44908684 | Alzheimer's disease biomarkers | rs429358 | 1.0e-06 |
|  |  | Brain imaging | rs429358 |  |

SQLite uses = or == to compare values. Note that all entries are case sensitive, so if your values have inconsistent case, you can use the lower() function to convert values to lowercase before comparison:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
sqlite&gt; SELECT chrom, position, trait, strongest_risk_snp, pvalue
...&gt; FROM gwascat WHERE lower(strongest_risk_snp) = "rs429358";
chrom     position    trait                 strongest_risk_snp  pvalue
--------   ----------   ----------   ----------   ----------   -----------
19      44908684    Alzheimer's disease biomarkers  rs429358          5.0e-14
19      44908684    Alzheimer's disease biomarkers  rs429358          1.0e-06
                   Brain imaging              rs429358
</div>

In our case, this doesn’t lead to a difference because the RS identifiers all have “rs” in lowercase. It’s best to try to use consistent naming, but if you’re not 100% sure that all RS identifiers start with a lowercase “rs,” converting everything to the same case is the robust solution.

The equals operator (=) is just one of many useful SQLite comparison operators; see Table 13-2 for a table of some common operators.

Table 13-2. Common operators used in WHERE statements

| Operator | Description |
| --- | --- |
| =, == | Equals |
| !=, &lt;> | Not equals |
| IS, IS NOT | Identical to = and !=, except that IS and IS NOT can be used to check for NULL values |
| &lt;, &lt;= | Less than, less than or equal to |
| >, >= | Greater than, greater than or equal to |
| x IN (a, b, ...) | Returns whether x is in the list of items (a, b, ...) |
| x NOT IN (a, b, ...) | Returns whether x is not in the list of items (a, b, ...) |
| NOT | Logical negation |
| LIKE | Pattern matching (use % as a wildcard, e.g. like Bash's *) |
| BETWEEN | x BETWEEN start AND END is a shortcut for x >= start AND x &lt;= end |
| - | Negative |
| + | Positive |

Additionally, we can build larger expressions by using AND and OR. For example, to retrieve all rows with p-value less than 10 x 10-1<sup>5</sup> and on chromosome 22:

<table><tr><td colspan="5">sqlite&gt; SELECT chrom, position, trait, strongest_risk_snp, pvalue...-&gt; FROM gwascat WHERE chrom = &quot;22&quot; AND pvalue &lt; 10e-15;</td></tr><tr><td>chrom</td><td>position</td><td>trait</td><td>strongest_risk_snp</td><td>pvalue</td></tr><tr><td>22</td><td>39351666</td><td>Rheumatoid arthritis</td><td>rs909685</td><td>1.0e-16</td></tr><tr><td>22</td><td>21577779</td><td>HDL cholesterol</td><td>rs181362</td><td>4.0e-18</td></tr><tr><td>22</td><td>39146287</td><td>Multiple myeloma</td><td>rs877529</td><td>8.0e-16</td></tr><tr><td>22</td><td>37185445</td><td>Graves&#x27; disease</td><td>rs229527</td><td>5.0e-20</td></tr><tr><td>22</td><td>40480230</td><td>Breast cancer</td><td>rs6001930</td><td>9.0e-19</td></tr><tr><td>[...]</td><td></td><td></td><td></td><td></td></tr></table>

It’s important to note that using colname = NULL will not work, as NULL is not equal to anything by definition; IS needs to be used in this case. This is useful when we combine create SELECT statements that use ORDER BY to order by a column that contains NULLs (which show up at the top). Compare:

<table><tr><td colspan="5">sqlite&gt; SELECT chrom, position, trait, strongest_risk_snp, pvalue...-&gt; FROM gwascat ORDER BY pvalue LIMIT 5;</td></tr><tr><td>chrom</td><td>position</td><td>trait</td><td>strongest_risk_snp</td><td>pvalue</td></tr><tr><td></td><td></td><td>Brain imaging</td><td>rs10932886</td><td></td></tr><tr><td></td><td></td><td>Brain imaging</td><td>rs429358</td><td></td></tr><tr><td></td><td></td><td>Brain imaging</td><td>rs7610017</td><td></td></tr><tr><td></td><td></td><td>Brain imaging</td><td>rs6463843</td><td></td></tr></table>

to using WHERE pvalue IS NOT NULL to eliminate NULL values before ordering:

<table><tr><td colspan="5">sqlite&gt; SELECT chrom, position, trait, strongest_risk_snp, pvalue...-&gt; FROM gwascat WHERE pvalue IS NOT NULL ORDER BY pvalue LIMIT 5;</td></tr><tr><td>chrom</td><td>position</td><td>trait</td><td>strongest_risk_snp</td><td>pvalue</td></tr><tr><td>16</td><td>56959412</td><td>HDL cholesterol</td><td>rs3764261</td><td>0.0</td></tr><tr><td>10</td><td>122454932</td><td>Age-related mac</td><td>rs10490924</td><td>0.0</td></tr><tr><td>1</td><td>196710325</td><td>Age-related mac</td><td>rs10737680</td><td>0.0</td></tr><tr><td>4</td><td>9942428</td><td>Urate levels</td><td>rs12498742</td><td>0.0</td></tr><tr><td>6</td><td>43957789</td><td>Vascular endoth</td><td>rs4513773</td><td>0.0</td></tr></table>

OR can be used to select rows that satisfy either condition:

<table><tr><td colspan="4">sqlite&gt; SELECT chrom, position, strongest_risk_snp, pvalue FROM gwascat</td></tr><tr><td colspan="4">...&gt; WHERE (chrom = &quot;1&quot; OR chrom = &quot;2&quot; OR chrom = &quot;3&quot;)</td></tr><tr><td colspan="4">...&gt; AND pvalue &lt; 10e-11 ORDER BY pvalue LIMIT 5;</td></tr><tr><td>chrom</td><td>position</td><td>strongest_risk_snp</td><td>pvalue</td></tr><tr><td>----</td><td>----</td><td>----</td><td>----</td></tr><tr><td>1</td><td>196710325</td><td>rs10737680</td><td>0.0</td></tr></table>

| 2 | 233763993 | rs6742078 | 4.94065645 |
| --- | --- | --- | --- |
| 3 | 165773492 | rs1803274 | 6.0e-262 |
| 1 | 196690107 | rs1061170 | 1.0e-261 |
| 2 | 73591809 | rs13391552 | 5.0e-252 |

This approach works, but is complex. It’s helpful to group complex statements with parentheses, both to improve readability and ensure that SQLite is interpreting your statement correctly.

Rather than listing out all possible values a column can take with OR and =, it’s often simpler to use IN (or take the complement with NOT IN):

```sql
sqlite> SELECT chrom, position, strongest_risk_snp, pvalue FROM gwascat
...> WHERE chrom IN ("1", "2", "3") AND pvalue < 10e-11
...> ORDER BY pvalue LIMIT 5;
chrom          position     strongest_risk_snp  pvalue
--------   --------------   --------------   --------------
1               196710325    rs10737680      0.0
2               233763993    rs6742078       4.94065645
3               165773492    rs1803274       6.0e-262
1               196690107    rs1061170       1.0e-261
2               73591809    rs13391552       5.0e-252
```

Finally, the BETWEEN … AND … operator is useful for retrieving entries between specific values. x BETWEEN start AND end works like x > = start AND x < = end:

```txt
sqlite> SELECT chrom, position, strongest_risk_snp, pvalue
  ...> FROM gwascat WHERE chrom = "22"
  ...> AND position BETWEEN 24000000 AND 25000000
  ...> AND pvalue IS NOT NULL ORDER BY pvalue LIMIT 5;
chrom          position     strongest_risk_snp   pvalue
--------   --------------   --------------   --------------
22           24603137    rs2073398         1.0e-109
22           24594246    rs4820599         7.0e-53
22           24600663    rs5751902         8.0e-20
22           24594246    rs4820599         4.0e-11
22           24186073    rs8141797         2.0e-09
```

However, note that this approach is not as efficient as other methods that use specialized data structures to handle ranges, such as Tabix, BedTools, or the interval trees in GenomicRanges. If you find many of your queries require finding rows that overlap regions and you’re running into bottlenecks, using one of these tools might be a better choice. Another option is to implement binning scheme, which assigns features to specific bins. To find features within a particular range, one can precalculate which bins these features would fall in and include only these bins in the WHERE clause. The UCSC Genome Browser uses this scheme (originally suggested by Lincoln Stein and Richard Durbin): see Kent et al., (2002) [The Human Genome Browser at UCSC](http://bit.ly/hgb-ucsc) for more information. We’ll discuss more efficiency tricks later on when we learn about table indexing.

## SQLite Functions

So far, we’ve just accessed column data exactly as they are in the table using SELECT. But it’s also possible to use expressions to create new columns from existing columns. We use SQLite functions and operators to do this, and AS to give each new column a descriptive name. For example, we could create a region string in the format “chr4:165773492” for each row and convert all traits to lowercase:

```sql
sqlite> SELECT lower(trait) AS trait,
    ...> "chr" || chrom || ":" || position AS region FROM gwascat LIMIT 5;
trait                          region
------------------------------------------  -------------------------
asthma and hay fever   chr6:32658824
asthma and hay fever   chr4:38798089
asthma and hay fever   chr5:11113180
asthma and hay fever   chr2:10235008
asthma and hay fever   chr17:3996642
```

Here, || is the concatenation operator, which concatenates two strings. As another example, we may want to replace all NULL values with “NA” if we needed to write results to a file that may be fed into R. We can do this using the ifnull() function:

```sql
sqlite> SELECT ifnull(chrom, "NA") AS chrom, ifnull(position, "NA") AS position,
...> strongest_risk_snp, ifnull(pvalue, "NA") AS pvalue FROM gwascat
...> WHERE strongest_risk_snp = "rs429358";
chrom        position     strongest_risk_snp  pvalue
--------   --------------   ---------------   ---------------
19          44908684    rs429358         5.0e-14
19          44908684    rs429358         1.0e-06
NA          NA           rs429358         NA
```

Later, we’ll see a brief example of how we can interact with SQLite databases directly in R (which automatically converts NULLs to R’s NAs). Still, if you’re interfacing with a SQLite database at a different stage in your work, ifnull() can be useful.

We’re just scratching the surface of SQLite’s capabilities here; see Table 13-3 for other useful common functions.

Table 13-3. Common SQLite functions

| Function | Description |
| --- | --- |
| ifnull(x, val) | If x is NULL, return with val, otherwise return x; shorthand for coalesce() with two arguments |
| min(a, b, c, ...) | Return minimum in a, b, c, ... |
| max(a, b, c, ...) | Return maximum in a, b, c, ... |
| abs(x) | Absolute value |
| coalesce(a, b, c, ...) | Return first non-NULL value in a, b, c, ... or NULL if all values are NULL |
| length(x) | Returns number of characters in x |
| lower(x) | Return x in lowercase |
| upper(x) | Return x in uppercase |
| replace(x, str, repl) | Return x with all occurrences of str replaced with repl |
| round(x, digits) | Round x to digits (default 0) |
| trim(x, chars), ltrim(x, chars), rtrim(x, chars) | Trim off chars (spaces if chars is not specified) from both sides, left side, and right side of x, respectively. |
| substr(x, start, length) | Extract a substring from x starting from character start and is length characters long |

## SQLite Aggregate Functions

Another type of SQLite function takes a column retrieved from a query as input and returns a single value. For example, consider counting all values in a column: a count() function would take all values in the column and return a single value (how many non-NULL values there are in the column). SQLite’s count() function given the argument \* (and without a filtering WHERE clause) will return how many rows are in a database:

```sql
sqlite> SELECT count(*) FROM gwascat;
count(*)
---------
17290
```

Using count(\*) will always count the rows, regardless of whether there are NULLs. In contrast, calling count(colname) where colname is a particular column will return the number of non-NULL values:

```sql
sqlite> SELECT count(pvalue) FROM gwascat;
count(pvalue)
-----------------------------------
17279
```

We can use expressions and AS to print the number of NULL p-values, by subtracting the total number non-NULL p-values from the total number of rows to return the number of NULL p-values:

```sql
sqlite> SELECT count(*) - count(pvalue) AS number_of_null_pvalues FROM gwascat;
number_of_null_pvalues
-----------------------------------
11
```

Other aggregate functions can be used to find the average, minimum, maximum, or sum of a column (see Table 13-4). Note that all of these aggregating functions work with WHERE clauses, where the aggregate function is only applied to the filtered results. For example, we could find out how many entries have publication dates in 2007 (i.e., after December 31, 2006, but before January 1, 2008):

```sql
sqlite> select "2007" AS year, count(*) AS number_entries
    ...> from gwascat WHERE date BETWEEN "2007-01-01" AND "2008-01-01";
year          number_entries
--------  --------------
2007         435
```

Table 13-4. Common SQLite aggregate functions

| Function | Description |
| --- | --- |
| count(x), count(*) | Return the number of non-NULL values in column x and the total number of rows, respectively |
| avg(x) | Return the average of column x |
| max(x), min(x) | Return the maximum and minimum values in x, respectively |
| sum(x), total(x) | Return the sum of column x; if all values of x are NULL, sum(x) will return NULL and total(x) will return 0. sum() will return integers if all data are integers; total() will always return a real value |

Note that unlike other relational databases like MySQL and PostgreSQL, SQLite does not have a dedicated date type. Although the date is text, this works because dates in this table are stored in ISO 8601 format (introduced briefly in “Command Substitution” on page 54), which uses leading zeros and is in the form: YYYY-MM-DD. Because this format cleverly arranges the date from largest period (year) to smallest (day), sorting and comparing this date as text is equivalent to comparing the actual dates. This is the benefit of storing dates in a tidy format (see XKCD’s [ISO 8601](http://xkcd.com/1179/)).

A nice feature of aggregate functions is that they allow prefiltering of duplicated values through the DISTINCT keyword. For example, to count the number of unique non-NULL RS IDs in the strongest\_risk\_snp column:

```sql
sqlite> SELECT count(DISTINCT strongest_risk_snp) AS unique_rs FROM gwascat;
unique_rs
---------
13619
```

## Grouping rows with GROUP BY

If you’re familiar with R (covered in Chapter 8), you’ve probably noticed that many of SQLite’s querying capabilities overlap R’s. We extract specific columns from a SQLite table using SELECT a, b FROM tbl;, which is similar to tbl[, c("a", "b")] to access columns a and b in an R dataframe. Likewise, SQL’s WHERE clauses filter rows much like R’s subsetting. Consider the similarities between SELECT a, b FROM tbl WHERE a < 4 AND b = 1; and tbl[tbl\$a < 4 & b == 1, c("a", "b")]. In this section, we’ll learn about the SQL GROUP BY statement, which is similar to the splitapply-combine strategy covered in “Working with the Split-Apply-Combine Pattern” on page 239.

As the name suggests, GROUP BY gathers rows into groups by some column’s value. Rather importantly, the aggregate functions we saw in the previous section are applied to each group separately. In this way, GROUP BY is analogous to using R’s split() function to split a dataframe by a column and using lapply() to apply an aggregating function to each split list item. Let’s look at an example—we’ll count how many associations there are in the GWAS catalog per chromosome:

```sql
sqlite> SELECT chrom, count(*) FROM gwascat GROUP BY chrom;
chrom        count(*)
--------   ------------
              70
1         1458
10       930
11       988
12       858
13       432
[...]
```

We can order our GROUP BY results from most hits to least with ORDER BY. To tidy up our columns, we’ll also use AS to name the count(\*) nhits:

```sql
sqlite> SELECT chrom, count(*) as nhits FROM gwascat GROUP BY chrom
...> ORDER BY nhits DESC;
chrom        nhits
--------   -------
6            1658
1            1458
2            1432
3            1033
11            988
10            930
[...]
```

As a more interesting example, let’s look at the top five most frequent strongest risk SNPs in the table:

```txt
sqlite> select strongest_risk_snp, count(*) AS count
  ...> FROM gwascat GROUP BY strongest_risk_snp
  ...> ORDER BY count DESC LIMIT 5;
strongest_risk_snp   count
--------   -------
rs1260326          36
rs4420638          30
rs1800562          28
rs7903146          27
rs964184          25
```

It’s also possible to group by multiple columns. Suppose, for example, that you weren’t just interested in the number of associations per strongest risk SNP, but also the number of associations for each allele in these SNPs. In this case, we want to compute count(\*) grouping by both SNP and allele:

```txt
sqlite> select strongest_risk_snp, strongest_risk_allele, count(*) AS count
...> FROM gwascat GROUP BY strongest_risk_snp, strongest_risk_allele
...> ORDER BY count DESC LIMIT 10;
strongest_risk_snp strongest_risk_allele count
---------------------------------------- -------------------------
rs1260326          T                          22
rs2186369            G                          22
rs1800562            A                          20
rs909674            C                          20
rs11710456            G                          19
rs7903146            T                          19
rs4420638            G                          18
rs964184            G                          15
rs11847263            G                          14
rs3184504            T                          12
```

All other aggregate functions similarly work on grouped data. As an example of how we can combine aggregate functions with GROUP BY, let’s look at the average log10 pvalue for all association studies grouped by year. The gwascat table doesn’t have a year column, but we can easily extract year from the date column using the substr() function. Let’s build up the query incrementally, first ensuring we’re extracting year correctly:

```sql
sqlite> SELECT substr(date, 1, 4) AS year FROM gwascat GROUP BY year;
year
---------
2005
2006
2007
2008
2009
2010
```

```csv
2011
2012
2013
```

Now that this is working, let’s add in a call to avg() to find the average -log10 pvalues per year (using round() to simplify the output) and count() to get the number of cases in each group:

```sql
sqlite> SELECT substr(date, 1, 4) AS year,
    ...> round(avg(pvalue_mlog), 4) AS mean_log_pvalue,
    ...> count(pvalue_mlog) AS n
    ...> FROM gwascat GROUP BY year;
year        mean_log_pvalue  n
--------  ----------  -------
2005         6.2474          2
2006         7.234            8
2007         11.0973          434
2008         11.5054          971
2009         12.6279          1323
2010         13.0641          2528
2011         13.3437          2349
2012         9.6976          4197
2013         10.3643          5406
```

The primary trend is an increase in -log10 p-values over time. This is likely caused by larger study sample sizes; confirming this will take a bit more sleuthing.

It’s important to note that filtering with WHERE applies to rows before grouping. If you want to filter groups themselves on some condition, you need to use the HAVING clause. For example, maybe we only want to report per-group averages when we have more than a certain number of cases (because our -log10 p-value averages may not be reliable with too few cases). You can do that with:

```sql
sqlite> SELECT substr(date, 1, 4) AS year,
    ...> round(avg(pvalue_mlog), 4) AS mean_log_pvalue,
    ...> count(pvalue_mlog) AS n
    ...> FROM gwascat GROUP BY year
    ...> HAVING count(pvalue_mlog) > 10;
year        mean_log_pvalue  n
----------  ----------  -------
2007         11.0973          434
2008         11.5054          971
2009         12.6279          1323
2010         13.0641          2528
2011         13.3437          2349
2012         9.6976          4197
2013         10.3643          5406
```

We’ve filtered here on the total per-group number of cases, but in general HAVING works with any aggregate functions (e.g., avg(), sum(), max(), etc.).

## Subqueries

As a teaser of the power of SQL queries, let’s look at a more advanced example that uses aggregation. The structure of the gwascat table is that a single study can have multiple rows, each row corresponding to a different significant association in the study. As study sample sizes grow larger (and have increased statistical power), intuitively it would make sense if later publications find more significant trait associations. Let’s build up a query to summarize the data to look for this pattern. The first step is to count how many associations each study has. Because the PubMed ID (column pubmedid) is unique per publication, this is an ideal grouping factor (see Example 13-1).

Example 13-1. An example subquery

```txt
sqlite> SELECT substr(date, 1, 4) AS year, author, pubmedid,
...> count(*) AS num_assoc FROM gwascat GROUP BY pubmedid
...> LIMIT 5;
year        author     pubmedid    num_assoc
--------   --------------   --------------   --------------
2005         Klein RJ    15761122    1
2005         Maraganore  16252231    1
2006         Arking DE    16648850    1
2006         Fung HC    17052657    3
2006         Dewan A    17053108    1
```

I’ve included the author and pubmedid columns in output so it’s easier to see what’s going on here. These results are useful, but what we really want is another level of aggregation: we want to find the average number of associations across publications, per year. In SQL lingo, this means we need to take the preceding results, group by year, and use the aggregating function avg() to calculate the average number of associations per publication, per year. SQLite (and other SQL databases too) have a method for nesting queries this way called subqueries. We can simply wrap the preceding query in parentheses, and treat it like a database we’re specifying with FROM:

```sql
sqlite> SELECT year, avg(num_assoc)
    ...> FROM (SELECT substr(date, 1, 4) AS year,
    ...>      author,
    ...>      count(*) AS num_assoc
    ...>      FROM gwascat GROUP BY pubmedid)
    ...> GROUP BY year;
year        avg(num_assoc)
--------  ----------
2005         1.0
2006         1.6
2007         5.87837837
2008         7.64566929
2009         6.90625
2010         9.21660649
```

| 2011 | 7.49681528 |
| --- | --- |
| 2012 | 13.4536741 |
| 2013 | 16.6055045 |

Indeed, it looks like there are more associations being found per study in more recent studies. While this subquery looks complex, structurally it’s identical to SELECT year, avg(num\_assoc) FROM tbl GROUP BY year; where tbl is replaced by the SELECT query Example 13-1. While we’re still only scratching the surface of SQL’s capabilities, subqueries are good illustration of the advanced queries that can be done entirely within SQL.

## Organizing Relational Databases and Joins

The solution to this redundancy is to organize data into multiple tables and use joins in queries to tie the data back together. If WHERE statements are the heart of making queries with SELECT statements, joins are the soul.

## Organizing relational databases

If you poke around in the gwascat table, you’ll notice there’s a great deal of redundancy. Each row of the table contains a single trait association from a study. Many studies included in the table find multiple associations, meaning that there’s a lot of duplicate information related to the study. Consider a few rows from the study with PubMed ID “24388013”:

<table><tr><td colspan="4">sqlite&gt; SELECT date, pubmedid, author, strongest_risk_snp...&gt; FROM gwascat WHERE pubmedid = &quot;24388013&quot; LIMIT 5;</td></tr><tr><td>date</td><td>pubmedid</td><td>author</td><td>strongest_risk_snp</td></tr><tr><td>2013-12-30</td><td>24388013</td><td>Ferreira MA</td><td>rs9273373</td></tr><tr><td>2013-12-30</td><td>24388013</td><td>Ferreira MA</td><td>rs4833095</td></tr><tr><td>2013-12-30</td><td>24388013</td><td>Ferreira MA</td><td>rs1438673</td></tr><tr><td>2013-12-30</td><td>24388013</td><td>Ferreira MA</td><td>rs10197862</td></tr><tr><td>2013-12-30</td><td>24388013</td><td>Ferreira MA</td><td>rs7212938</td></tr></table>

I’ve only selected a few columns to include here, but all rows from this particular study have duplicated author, date, journal, link, study, initial\_samplesize, and replication\_samplesize column values. This redundancy is not surprising given that this data originates from a spreadsheet, where data is always organized in flat tables. The database community often refers to unnecessary redundancy in database tables as spreadsheet syndrome. With large databases, this redundancy can unnecessarily increase required disk space.

Before learning about the different join operations and how they work, it’s important to understand the philosophy of organizing data in a relational database so as to avoid spreadsheet syndrome. This philosophy is database normalization, and it’s an extensive topic in its own right. Database normalization is a hierarchy of increasingly normalized levels called normal forms. Though the technical definitions of the normal forms are quite complicated, the big picture is most important when starting to organize your own relational databases. I’ll step through a few examples that illustrate how reorganizing data in a table can reduce redundancy and simplify queries. I’ll mention the normal forms in passing, but I encourage you to further explore database normalization, especially if you’re creating and working with a complex relational database.

First, it’s best to organize data such that every column of a row only contains one data value. Let’s look at an imaginary table called assocs that breaks this rule:

| id | pubmedid | year | journal | trait | strongest_risk_snp |
| --- | --- | --- | --- | --- | --- |
| -- | -------- | ---- | -------- | -------- | -------- |
| 1 | 24388013 | 2013 | J Allergy | Asthma, hay fever | rs9273373,rs4833095,rs1438673 |
| 2 | 17554300 | 2007 | Nature | Hypertension | rs2820037 |
| 3 | 17554300 | 2007 | Nature | Crohn's disease | rs6596075 |

From what we’ve learned so far about SQL queries, you should be able to see why the organization of this table is going to cause headaches. Suppose a researcher asks you if rs4833095 is an identifier in the strongest risk SNP column of this table. Using the SQL querying techniques you learned earlier in this chapter, you might use SELECT \* FROM assoc WHERE strongest\_risk\_snp = "rs4833095" to find matching records. However, this would not work, as multiple values are combined in a single column of the row containing rs4833095!

A better way to organize this data is to create a separate row for each data value. We can do this by splitting the records with multiple values in a column into multiple rows (in database jargon, this is putting the table in first normal form):

| id | pubmedid | year | journal | trait | strongest_risk_snp |
| --- | --- | --- | --- | --- | --- |
| -- | -------- | ---- | -------- | ------ | -------- |
| 1 | 24388013 | 2013 | J Allergy | Asthma, hay fever | rs9273373 |
| 2 | 24388013 | 2013 | J Allergy | Asthma, hay fever | rs4833095 |
| 3 | 24388013 | 2013 | J Allergy | Asthma, hay fever | rs1438673 |
| 4 | 17554300 | 2007 | Nature | Hypertension | rs2820037 |
| 5 | 17554300 | 2007 | Nature | Crohn's disease | rs6596075 |

You might notice something about this table now though: there’s now duplication in journal, year, and pubmedid column values. This duplication is avoidable, and arises because the year and journal columns are directly dependent on the pubmedid column (and no other columns).

A better way of organizing this data is to split the table into two tables (one for association results, and one for studies):

assocs:

```csv
id pubmedid trait strongest_risk_snp
-- ------------ ---- ------------
1 24388013 Asthma, hay fever rs9273373
2 24388013 Asthma, hay fever rs4833095
3 24388013 Asthma, hay fever rs1438673
4 17554300 Hypertension rs2820037
5 17554300 Crohn's disease rs6596075
```

studies:

```txt
pubmedid year journal
-------- ---- ---------
24388013 2013 J Allergy
17554300 2007 Nature
```

Organizing data this way considerably reduces redundancy (in database jargon, this scheme is related to the second and third normal forms). Now, our link between these two different tables are the pubmedid identifiers. Because pubmedid is a primary key that uniquely identifies each study, we can use these keys to reference studies from the assocs table. The pubmedid of the assocs table is called a foreign key, as it uniquely identifies a record in a different table, the studies table.

While we used pubmedid as a foreign key in this example, in practice it’s also common to give records in the studies column an arbitrary primary key (like id in assocs) and store pubmedid as an additional column. This would look like:

assocs:

```txt
id study_id trait strongest_risk_snp
-- ------------ ---- -------------------
1 1 Asthma, hay fever rs9273373
2 1 Asthma, hay fever rs4833095
3 1 Asthma, hay fever rs1438673
4 2 Hypertension rs2820037
5 2 Crohn's disease rs6596075
```

studies:

```txt
id     pubmedid    year      journal
--   ------   -----       -------
1     24388013   2013     J Allergy
2     17554300   2007     Nature
```

Now that we’ve organized our data into two tables, we’re ready to use joins to unite these two tables in queries.