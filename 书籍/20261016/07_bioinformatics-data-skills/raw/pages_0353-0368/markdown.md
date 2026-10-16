Here’s what amy1\_exons now looks like (only one transcript’s exons shown):

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&gt; amy1_exons
GRangesList object of length 5:
$18879
GRanges object with 11 ranges and 3 metadata columns:
    seqnames        ranges strand | exon_id exon_name [...] [...]
        &lt;Rle&gt;        &lt;IRanges&gt; &lt;Rle&gt; | &lt;integer&gt; &lt;character&gt; [...] [...]
[1]     chr3 [113577701, 113577830]   - | 68142      &lt;NA&gt; [...] [...]
[2]     chr3 [113569845, 113570057]   - | 68139      &lt;NA&gt; [...] [...]
[3]     chr3 [113569382, 113569528]   - | 68138      &lt;NA&gt; [...] [...]
[4]     chr3 [113564869, 113565066]   - | 68136      &lt;NA&gt; [...] [...]
[5]     chr3 [113563445, 113563675]   - | 68135      &lt;NA&gt; [...] [...]
[...]
</div>

Now, we want to process each transcript and its exons pairwise. Our exons are already grouped by transcript, but our transcripts are in a single GRanges object (because these are transcripts grouped by gene, and we’re looking at one gene). So we split up transcript ranges into a GRangeList object, this time grouping by transcript identifier:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&gt; amy1_tx &lt;- split(amy1, amy1\$tx_id)
&gt; amy1_tx
GRangesList object of length 5:
\$18879
GRanges object with 1 range and 2 metadata columns:
    seqnames          ranges strand | tx_id        tx_name
        &lt;Rle&gt;           &lt;IRanges&gt; &lt;Rle&gt; | &lt;integer&gt;       &lt;character&gt;
[1]     chr3 [113555710, 113577830]   - |  18879 ENSMUST00000067980

\$18880
GRanges object with 1 range and 2 metadata columns:
    seqnames          ranges strand | tx_id        tx_name
[1]     chr3 [113555953, 113574762]   - | 18880 ENSMUST00000106540
[...]
</div>

With both our exons and transcripts grouped by transcript, we can finally take the pairwise set difference (with psetdiff()) which creates the set of introns for each transcript. Remember, it’s imperative when using pairwise set functions to make sure your two objects are correctly matched up!

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&gt; all(names(amy1_tx) == names(amy1_exons))  # check everything's matched up
[1] TRUE
&gt; amy1_introns &lt;- psetdiff(amy1_tx, amy1_exons)
&gt; head(amy1_introns[['18880']]. 2) # the first two introns of amylase
                      # 1 transcript 18880
GRanges with 2 ranges and 0 metadata columns:
        seqnames            ranges strand
            &lt;Rle&gt;              &lt;IRanges&gt; &lt;Rle&gt;
[1]     chr3 [113556174, 113558092]    -
[2]     chr3 [113558219, 113558321]    -
---
</div>

seqlengths:

| chr1 | chr2 ... | chrUn_JH584304 |
| --- | --- | --- |
| 195471971 | 182113224 ... | 114452 |

Are the introns we created manually for this gene identical to those created by the function intronsByTranscripts()? It’s always a good idea to validate your methods through comparison to another method or visual inspection using a genome browser. Here, we compare to the introns found with intronsByTranscript():

```txt
> identical(mm_introns[names(amy1_tx)], amy1_introns)
[1] TRUE
```

Indeed, the manual method using psetdiff() works.

## Finding and Working with Overlapping Ranges

Finding and counting overlaps are probably the most important operations in working with GRanges objects and ranges in general. Bioconductor’s GenomicRanges package has functions for finding overlaps, subsetting by overlaps, and counting overlaps that are nearly identical to methods found in the IRanges package. There are a couple exceptions:

• Overlap methods that work with GRanges objects.
• Only consider overlaps of ranges on the same chromosome or sequence.
• You have the choice to consider how strands are handled.

## Mind Your Overlaps (Part II)

Overlaps get quite complex very quickly (as discussed in a warning earlier). Nowhere is this more apparent than with RNA-seq, where many technical issues can make the simple act of estimating transcript abundance (by counting how many aligned sequencing reads overlap a transcript region) incredibly complicated. First, counting overlaps in RNA-seq yields quantitative results that are used in downstream statistical analyses (e.g., the abundance of estimates for a particular transcript). This means that bias and noise that enter the range overlap quantification process could lead to inaccuracies in differential expression tests. Second, sequencing reads may align ambiguously—to multiple spots in the genome equally well. Do we count these multiple mapping reads (sometimes known as “multireads”)? Or discard them entirely? Some modern RNA-seq quantification methods like RSEM (Li et al., 2011) attempt to rescue these multireads. Third, some reads may align uniquely, but overlap an exon that’s shared by two or more transcripts’ isoforms. Should we ignore this read, count it once for each transcript (leading to double counting), or assign it to a transcript? All of these rather technical decisions in finding and counting overlaps can unfortunately lead to different biological results. Accurate RNA-seq quantification is still an actively researched area, and methods are still being developed and improving. In general, the methods in this section are only appropriate for simple overlap operations, and may not be appropriate for quantification tasks like estimating transcript abundance for RNA-seq.

Some popular RNA-seq quantification tools are:

• [RSEM, or RNA-Seq by Expectation Maximization](http://deweylab.biostat.wisc.edu/rsem/) (Li et al., 2011).
• [TopHat](http://bit.ly/TopHat-tool) and [The TopHat and Cufflinks](http://cufflinks.cbcb.umd.edu/) suite of tools (Trapnell et al., 2009; Trapnell et al., 2012).
• [HTSeq](http://bit.ly/HTSeq) (Anders et al., 2014).
• [The GenomicAlignments Bioconductor package](http://bit.ly/genom-align) (Lawrence et al., 2013). This new package from Bioconductor has special structures for storing genomic alignments and working with these alignments. This package also contains a summari zeOverlaps() method, which supports specific overlap options (and works directly on BAM files).

To demonstrate how findOverlaps() can be used with GRanges objects, we’ll load in a BED file of dbSNP (build 137) variants (in addition to SNPs, dbSNP also includes other types of variants like insertions/deletions, short tandem repeats, multi-nucleotide polymorphisms) for mouse chromosome 1. This BED file is available in the book’s GitHub repository, in the directory for this chapter. Using rtracklayer, we’ll load these in:

**> library**(rtracklayer)
> dbsnp137 <- import("mm10\_snp137\_chr1\_trunc.bed.gz")

Suppose we want to find out how many of these variants fall into exonic regions, and how many do not. Using the mouse TranscriptDb object we loaded earlier (txdb) we can extract and collapse all overlapping exons with reduce(). We’ll also subset so that we’re only looking at chromosome 1 exons (because our variants are only from chromosome 1):

> collapsed\_exons <- reduce(exons(txdb), ignore.strand=**TRUE**)
> chr1\_collapsed\_exons <- collapsed\_exons[seqnames(collapsed\_exons) == "chr1"]

Let’s explore our dbsnp137 object before looking for overlaps (remember the Golden Rule: don’t trust your data). Let’s look at the length distribution of our variants:

```txt
> summary(width(dbsnp137))
    Min. 1st Qu.   Median      Mean 3rd Qu.     Max.
    0.000   1.000   1.000   1.138   1.000 732.000
> dbsnp137\$name[which.max(width(dbsnp137))]
[1] "rs232497063"
```

The variant that’s 732 bases long is a bit large, so we find out which entry it is and grab its RS identifier. Checking on [the dbSNP website](http://bit.ly/ref-snp), we see that this is indeed a real variant—a rather large insertion/deletion on chromosome 1. From our summary(), we see that the vast majority of variants are 1 nucleotide long, which are either SNPs or 1 basepair insertons/deletions. Note that the minimum width is zero—there are also variants with zero widths. Using dbsnp137[width(dbsnp137) == 0], we can take look at a few of these. In most cases, these correspond to insertions into the reference genome (these can be easily verified with the dbSNP or UCSC Genome Browser websites). Zero-width ranges will not overlap any feature, as they don’t have any region to overlap another range (create some range with zero widths and validate this). These technical details are rather annoying, but illustrate why it’s important to inspect and understand our data and not just blindly apply functions. To count these zero-width features too, we’ll resize using the resize() function:

```txt
> dbsnp137_resized <- dbsnp137
> zw_i <- width(dbsnp137_resized) == 0
> dbsnp137_resized[zw_i] <- resize(dbsnp137_resized[zw_i], width=1)
```

With this set of ranges, it’s easy now to find out how many variants overlap our chromosome 1 exon regions. We’ll use findOverlaps() to create a Hits object. We’ll tell findOverlaps() to ignore strand:

```txt
> hits <- findOverlaps(dbsnp137_resized, chr1_collapsed_exons,
    ignore.strand=TRUE)
> hits
Hits of length 58346
queryLength: 2700000
subjectLength: 15048
    queryHits subjectHits
        <integer>      <integer>
1           1250          1
2           1251          1
3           1252          1
4           1253          1
5           1254          1
[...]
> length(unique(queryHits(hits)))
[1] 58343
> length(unique(queryHits(hits)))/length(dbsnp137_resized)
[1] 0.02160852
```

The number of dbSNP variants on chromosome 1 that overlap our exons is given by the number of unique query hits in the Hits object: 118,594. This represents about 2% of the variants on chromosome 1, a figure that makes sense given that exonic regions make up small proportion of chromosome 1 (you should be able to work out what proportion of this is using GenomicRanges methods fairly easily).

Suppose we now wanted to look at the variants that do overlap these exons. We could do this by using the indices in the Hits object, but a simpler method is to use the method subsetByOverlaps():

> subsetByOverlaps(dbsnp137\_resized, chr1\_collapsed\_exons, ignore.strand=**TRUE**) GRanges with 118594 ranges and 2 metadata columns:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
        seqnames          ranges strand | name   score
        &lt;Rle&gt;          &lt;IRanges&gt; &lt;Rle&gt; | &lt;character&gt; &lt;numeric&gt;
[1]    chr1     [3054535, 3054535]  + | rs30525614      0
[2]    chr1     [3054556, 3054556]  + | rs233033126      0
[3]    chr1     [3054666, 3054666]  + | rs51218981      0
[4]    chr1     [3054674, 3054674]  + | rs49979360      0
[5]    chr1     [3054707, 3054707]  + | rs108510965      0
[...]
</div>

Note that the length of this GRanges object matches up with the number of overlapping variants that overlap exons earlier.

GenomicRanges also includes a method for counting overlaps, countOverlaps(). So suppose we wanted to count the number of variants that overlap each exonic region. Because we want the counts to be based on the exonic regions (which were the subject ranges in these operations), we reverse the order of the arguments:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&gt; var_counts &lt;- countOverlaps(chr1_collapsed_exons, dbsnp137_resized,
    ignore.strand=TRUE)
&gt; head(var_counts)
[1]  6  0 35 48  2  5
</div>

To make these easier to follow, let’s append them to our chromosome 1 exonic regions GRanges object as a metadata column:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&gt; chr1_collapsed_exons\$num_vars &lt;- var_counts
&gt; chr1_collapsed_exons
GRanges with 15048 ranges and 1 metadata column:
        seqnames                  ranges strand | num_vars
            &lt;Rle&gt;              &lt;IRanges&gt; &lt;Rle&gt; | &lt;integer&gt;
    [1]     chr1      [3054233, 3054733]   * |       6
    [2]     chr1      [3102016, 3102125]   * |       0
    [3]     chr1      [3205901, 3207317]   * |       35
    [4]     chr1      [3213439, 3216968]   * |       48
    [5]     chr1      [3421702, 3421901]   * |       2
[...]
</div>

At this point, it wouldn’t be a bad idea to visit some of these regions (like “chr1:3054233-3054733”) on the mouse UCSC Genome Browser and check that the number of variants on the dbSNP track matches up with the number we see here (6).

## Calculating Coverage of GRanges Objects

The same coverage methods we saw with IRanges also work with GRanges and GRangesList objects. Let’s generate some random fake 150bp reads on chromosome

19 (because it’s the smallest chromosome) of our mouse genome and then empirically measure their coverage. We’ll target 5x coverage. Using the famous Lander-Waterman coverage equation for coverage (C = LN/G, where C is coverage, L is the read length, N is the sequence length, and N is the number of reads), we see that for 150bp reads, a chromosome length of 61,431,566bp, and a target of 5x coverage, we need: 5\*61,431,566/150 = 2,047,719 reads. Let’s generate these using R’s sample() function:

```r
> set.seed(0)
> chr19_len <- seqlengths(txdb)['chr19']
> chr19_len
    chr19
61431566
> start_pos <- sample(1:(chr19_len-150), 2047719, replace=TRUE)
> reads <- GRanges("chr19", IRanges(start=start_pos, width=150))
```

Now, let’s use the coverage() method from GenomicRanges to calculate the coverage of these random reads:

```txt
> cov_reads <- coverage(reads)
```

Coverage is calculated per every chromosome in the ranges object, and returned as a run-length encoded list (much like sequence names are returned by seqnames() from a GRangesList). We can calculate mean coverage per chromosome easily:

```python
> mean(cov_reads)
    chr19
5.000001
```

It’s also easy to calculate how much of this chromosome has no reads covering it (this will happen with shotgun sequencing, due to the random nature of read placement). We can do this two ways. First, we could use == and table():

```txt
> table(cov_reads == 0)
        FALSE      TRUE
chr19 61025072   406487
```

Or, we could use some run-length encoding tricks (these are faster, and scale to larger data better):

```txt
> sum(runLength(cov_reads)[runValue(cov_reads) == 0])
chr19
406487
> 406487/chr19_len
    chr19
0.006616908
```

So, about 0.6% of our chromosome 19 remains uncovered. Interestingly, this is very close to the proportion of uncovered bases expected under Lander-Waterman, which is Poisson distributed with λ = c (where c is coverage). Under the Poisson distribution, the expected proportion of uncovered genome is e-<sup>c</sup> where c is coverage, which in this case is e-<sup>c</sup> \~ 0.0067 (where e is Napier/Euler’s constant).

## Working with Ranges Data on the Command Line with BEDTools

While Bioconductor’s IRanges, GenomicRanges, and GenomicFeatures packages are all powerful libraries for working with genomic interval data in R, for some tasks working with range data on the command line can be more convenient. While GenomicRanges offers the huge advantage of allowing interactive work, there’s a cost to loading all data into memory at once so we can work with it. For example, suppose you wanted to calculate the coverage across a genome for each of 300 BED files. A single command that reads a BED file and calculates coverage would would be easier to run than loading the data into R, writing (simple) code to calculate coverage, and saving the results to file. While a custom solution allows more fine-tuned control, this means more work. A specialized command-line tool may offer less flexibility, but it’s easier to get up and running and parallelize in Unix (we’ll see how we could parallelize this in Chapter 12).

The BEDTools suite is a set of command-line tools for working directly with data kept in range file formats like BED, GTF, and GFF. Much like Git, BEDTools is a single command that uses a series of subcommands that do specific tasks. Each of these subcommands has similarities with one or more range operations we’ve seen in IRanges and GenomicRanges. The skills you’ve learned for manipulating IRanges and GenomicRanges objects are directly applicable to the range operations you’ll perform with BEDTools. Because you’re likely very familiar with range operations and “rangethinking” by now, we’ll move through this material quickly, mostly as a demonstration of how powerful BEDTools is and when it will be useful in your work.

First, let’s download the toy data we’ll be playing with. All of these files are available in this chapter’s directory in the GitHub repository. We’ll continue using the data from Mus musculus, genome version mm10. Specifically, we’ll use the following files:

• ranges-qry.bed is a simple BED file containing six ranges. These are the query ranges used in the GenomicRanges findOverlaps examples (except, because these are in BED format, they are 0-indexed).
• ranges-sbj.bed is the counterpart of ranges-sbj; these are the subject ranges used in the GenomicRanges findOverlaps examples. Both ranges-sbj.bed and rangesqry.bed are depicted in Figure 9-11 (though, this visualization uses 1-based coordinates).
• Mus\_musculus.GRCm38.75\_chr1.gtf.gz are features on chromosome 1 of Mus\_musculus.GRCm38.75.gtf.gz. The latter file is Ensembl’s annotation file for mm10 (which is the same as GRCh38) and was downloaded from [Ensembl’s FTP site](http://bit.ly/mus-dl).

• Mus\_musculus.GRCm38\_genome.txt is a tab-delimited file of all chromosome names and lengths from the mm10/GRCm38 genome version.

As a Unix command-line tool that works with plain-text range formats like BED, GTF, and GFF, BEDTools is desgined to be used in collaboration with other Unix tools like cut, sort, grep, and awk. For example, while BEDTools has its own sortBed command, it’s more efficient to use Unix sort. Also, BEDTools operations that can be applied to many independent files can also be parallelized using Unix tools like xargs or GNU parallel (covered in Chapter 12).

## Computing Overlaps with BEDTools Intersect

Overlaps are the most commonly used range-based operations in bioinformatics, so they’re a natural place to start with BEDTools. The BEDTools intersect subcommand computes the overlaps between two sets of ranges. Run in the default mode, bedtools intersect works exactly like the GenomicRanges intersect() function. Let’s use the BED files ranges-qry.bed and ranges-sbj.bed, which contain the same ranges used in the findOverlaps() example. Rather than thinking about ranges as query and subject, BEDTools labels ranges “A” and “B.” We specify the input BED files “A” and “B” through the options -a and -b. We’ll use BED files, but a nice feature of BEDTools is that its commands also work with GTF/GFF files.

Below, we calculate the intersection using bedtools intersect.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$ cat ranges-qry.bed
chr1     0       15      a
chr1     25       29      b
chr1     18       18      c
chr1     10       14      d
chr1     20       23      e
chr1     6       7      f
$ cat ranges-sbj.bed
chr1     0       4      x
chr1     18       28      y
chr1     9       15      z
$ bedtools intersect -a ranges-qry.bed -b ranges-sbj.bed
chr1     0       4      a
chr1     9       15      a
chr1     25       28      b
chr1     18       18      c
chr1     10       14      d
chr1     20       23      e
</div>

bedtools intersect returns the intersecting ranges with names from the file passed to the -a argument. Like GenomicRanges intersect(), only the overlap region is returned. For example, only the sections of range a in ranges-qry.bed that overlap the x and z ranges in ranges-sbj.bed are returned.

![](images/page_360_image_0.jpg)

## Alignment Files with BEDTools

While we’re focusing on annotation/track formats like BED and GFF/GTF, BEDTools also has full support to work with BAM files, a binary alignment format we’ll talk about in much detail in Chap ter 10. For now, note that for subcommands like intersect and genomecov, you can also work with BAM files directly. BEDTools also has a subcommand to convert BAM files to BED files (bed tools bamtobed), but usually it’s best to work with BAM files directly: the conversion from BAM to BED loses information stored about each alignment.

Often, we don’t want just the intersect of overlapping query and subject ranges, but the entire query range. This is akin to using findOverlaps() to create a Hits object, and taking all query ranges with an overlap (covered in “Finding Overlapping Ranges” on page 281). With BEDTools, we can do this using the option -wa, which returns the ranges in “A” that overlap “B”:

<table><tr><td colspan="4">$ bedtools intersect -a ranges-qry.bed -b ranges-sbj.bed -wa</td></tr><tr><td>chr1</td><td>0</td><td>15</td><td>a</td></tr><tr><td>chr1</td><td>0</td><td>15</td><td>a</td></tr><tr><td>chr1</td><td>25</td><td>29</td><td>b</td></tr><tr><td>chr1</td><td>18</td><td>18</td><td>c</td></tr><tr><td>chr1</td><td>10</td><td>14</td><td>d</td></tr><tr><td>chr1</td><td>20</td><td>23</td><td>e</td></tr></table>

Now, note that because the range “a” overlaps two subjects (x and z), the full “a” range is reported twice, one for each subject. If you don’t want these duplicates, you could specify the flag -u (for unique).

Similarly, there’s a -wb option too:

<table><tr><td colspan="8">$ bedtools intersect -a ranges-qry.bed -b ranges-sbj.bed -wb</td></tr><tr><td>chr1</td><td>0</td><td>4</td><td>a</td><td>chr1</td><td>0</td><td>4</td><td>x</td></tr><tr><td>chr1</td><td>9</td><td>15</td><td>a</td><td>chr1</td><td>9</td><td>15</td><td>z</td></tr><tr><td>chr1</td><td>25</td><td>28</td><td>b</td><td>chr1</td><td>18</td><td>28</td><td>y</td></tr><tr><td>chr1</td><td>18</td><td>18</td><td>c</td><td>chr1</td><td>18</td><td>28</td><td>y</td></tr><tr><td>chr1</td><td>10</td><td>14</td><td>d</td><td>chr1</td><td>9</td><td>15</td><td>z</td></tr><tr><td>chr1</td><td>20</td><td>23</td><td>e</td><td>chr1</td><td>18</td><td>28</td><td>y</td></tr></table>

Here, the overlapping region is first reported (this is the same as bedtools inter sect without any additional arguments), followed by the full ranges of “B” that “A” overlaps. Flags -wa and -wb can be combined to return the full “A” and “B” ranges that are overlapping:

<table><tr><td colspan="8">$ bedtools intersect -a ranges-qry.bed -b ranges-sbj.bed -wa -wb</td></tr><tr><td>chr1</td><td>0</td><td>15</td><td>a</td><td>chr1</td><td>0</td><td>4</td><td>x</td></tr><tr><td>chr1</td><td>0</td><td>15</td><td>a</td><td>chr1</td><td>9</td><td>15</td><td>z</td></tr><tr><td>chr1</td><td>25</td><td>29</td><td>b</td><td>chr1</td><td>18</td><td>28</td><td>y</td></tr><tr><td>chr1</td><td>18</td><td>18</td><td>c</td><td>chr1</td><td>18</td><td>28</td><td>y</td></tr></table>

| chr1 | 10 | 14 | d | chr1 | 9 | 15 | z |
| --- | --- | --- | --- | --- | --- | --- | --- |
| chr1 | 20 | 23 | e | chr1 | 18 | 28 | y |

Running bedtools intersect on large files can use a lot of your system’s memory. For very large files, it can be much more efficient to first sort both “A” and “B” files by chromosome and position, and then compute intersects on these sorted input files. bedtools intersect has a special algorithm that works faster (and uses less memory) on sorted input files; we enable this with -sorted. For example, using the fake files query-sorted.bed and subject-sorted.bed:

\$ bedtools intersect -a query-sorted.bed -b subject-sorted.bed --sorted

These BED files would have to be sorted first, as we did in “Sorting Plain-Text Data with Sort” on page 147 with sort -k1,1 -k2,2n. Note that the performance benefits pay off most when intersecting large files; with small files, the benefits may be too small to notice or might be swamped out by fixed costs.

BEDTools’s intersect has lots of functionality beyond just overlaps. For example, you can also return the number of overlapping bases with the -wo argument:

<table><tr><td colspan="9">$ bedtools intersect -a ranges-qry.bed -b ranges-sbj.bed -wo</td></tr><tr><td>chr1</td><td>0</td><td>15</td><td>a</td><td>chr1</td><td>0</td><td>4</td><td>x</td><td>4</td></tr><tr><td>chr1</td><td>0</td><td>15</td><td>a</td><td>chr1</td><td>9</td><td>15</td><td>z</td><td>6</td></tr><tr><td>chr1</td><td>25</td><td>29</td><td>b</td><td>chr1</td><td>18</td><td>28</td><td>y</td><td>3</td></tr><tr><td>chr1</td><td>18</td><td>18</td><td>c</td><td>chr1</td><td>18</td><td>28</td><td>y</td><td>0</td></tr><tr><td>chr1</td><td>10</td><td>14</td><td>d</td><td>chr1</td><td>9</td><td>15</td><td>z</td><td>4</td></tr><tr><td>chr1</td><td>20</td><td>23</td><td>e</td><td>chr1</td><td>18</td><td>28</td><td>y</td><td>3</td></tr></table>

Like grep -v (which returns nonmatching lines), bedtools intersect also has a -v option, which returns all nonoverlapping ranges.

| $ bedtools intersect -a ranges-qry.bed -b ranges-sbj.bed -vchr1 6 7 f |
| --- |

![](images/page_361_image_8.jpg)

## Getting Help in BEDTools

Much like Git, BEDTools has extensive documentation built into the BEDTools command (and luckily, it’s much less technical and easier to understand than Git’s documentation). We can see all BEDTools subcommands by simply running bedtools without any arguments. Running a subcommand such as bedtools intersect without any arguments prints out the arguments, options, and useful notes for this command.

This test data isn’t stranded, but with real data we need to be concerned with strand. bedtools intersect does not consider strand by default, so if you want to only look for intersects of features on the same strand, you must specify -s.

This is just a quick demonstration of bedtools intersect; see [the full documentation](http://bit.ly/bt-intersect) for much more information.

## BEDTools Slop and Flank

Like GenomicRanges, BEDTools has support for increasing the size of features and extracting flanking sequences. Earlier we saw how we could grow GRanges objects using arithemetic operators like + or the resize() function. With BEDTools, we grow ranges with bedtools slop. Unlike bedtools intersect, slop takes a single input range file through the argument -i. We also need to provide bedtools slop with a tab-delimited genome file that specifies the length of each chromosome—this is what BEDTools uses to ensure that ranges don’t grow past the end of the of the chromosome. For our fake test data, we’ll create this using echo, but in general we could use bioawk (discussed in “Bioawk: An Awk for Biological Formats” on page 163):

\$ bioawk -c fastx '{print \$name"\t"length(\$seq)}' your\_genome.fastq > genome.txt So for our test data, we’d use:

```shell
$ echo -e "chr1\t100" > genome.txt
$ bedtools slop -i ranges-qry.bed -g genome.txt -b 4 ①
chr1     0       19      a
chr1     21       33      b
chr1     14       22      c
chr1     6       18      d
chr1     16       27      e
chr1     2       11      f
$ bedtools slop -i ranges-qry.bed -g genome.txt -l 3 -r 5 ②
chr1     0       20      a
chr1     22       34      b
chr1     15       23      c
chr1     7       19      d
chr1     17       28      e
chr1     3       12      f
```

0 Here, the argument -b 4 tells bedtools slop to grow both sides of each range by 4 base pairs. If this runs past the beginning or end of the chromosome (as range a in ranges-qry.bed does), this will return 0 or the total chromosome length, respectively.
Optionally, you can specify how many bases to add to the left (-l) and right (-r) sides of each range. Either can be set to zero to resize only one side.

BEDTools also has a tool for extracting flanking ranges, which is handy for getting promoter sequences. As with slop, flank needs a genome file containing the lengths of each chromosome sequence. Let’s use bedtools flank to extract some promoter regions for genes. We’ll use the Mus\_musculus.GRCm38.75\_chr1.gtf.gz GTF file.

However, this file contains all types of features: exons, transcripts, CDS, noncoding regions, and so on (look at it with zless for confirmation). If we only want to use promoters for each protein coding gene, we can use the Unix tricks of Chapter 7 to extract only these ranges:

```shell
$ bioawk -cgff '{if ($feature == "gene") print $0}' \
Mus_musculus.GRCm38.75_chr1.gtf.gz | \
grep 'gene_biotype "protein_coding";' > mm_GRCm38.75_protein_coding_genes.gtf
```

![](images/page_363_image_2.jpg)

## Mind Your Chromosome Names

It’s very likely that when working with data (annotation or other data) from other sources, you’ll run into the different chromosome naming scheme problem. For example, the UCSC Genome Browser gives Mus musculus chromosome names like “chr1,” “chrX,” etc. while Ensembl uses named like “1,” “X,” etc. BEDTools is good about warning you when it can’t find a sequence length in a genome file, but it won’t warn for subcommands that don’t require a genome file (like intersect). Always check that your chromosome names across different data sources are compatible.

Now, using these protein coding gene feature and the mm10/GRCm38 genome file in this chapter’s GitHub repository, we can extract 3kbp left of each range:

```txt
$ bedtools flank -i mm_GRCm38.75_protein_coding_genes.gtf \
              -g Mus_musculus.GRCm38_genome.txt \
              -l 3000 -r 0 > mm_GRCm38_3kb_promoters.gtf
$ cut -f1,4,5,7 mm_GRCm38.75_protein_coding_genes.gtf | head -n 3
1       3205901 3671498 -
1       4343507 4360314 -
1       4490928 4496413 -
$ cut -f1,4,5,7 mm_GRCm38_3kb_promoters.gtf | head -n 3
1       3671499 3674498 -
1       4360315 4363314 -
1       4496414 4499413 -
```

Check that these upstream ranges make sense, minding the very important fact that these are all on the negative strand (a common stumbling block).

We can use the bedtools getfasta subcommand to extract sequences for a given set of ranges. For example, we could use bedtools getfasta to extract the promoter sequences for the ranges we’ve just created. Including the entire mouse genome in this book’s GitHub repository would be a bit too much, so rather than using the full genome, we’ll use the chromosome 1 file, Mus\_musculus.GRCm38.75.dna\_rm.toplevel\_chr1.fa. You’ll need to unzip this first from Mus\_musculus.GRCm38.75.dna\_rm.toplevel\_chr1.fa.gz, then run bedtools getfasta:

```shell
$ gunzip Mus_musculus.GRCm38.75.dna_rm.toplevel_chr1.fa.gz
$ bedtools getfasta -fi Mus_musculus.GRCm38.75.dna_rm.toplevel_chr1.fa \
-bed mm_GRCm38_3kb_promoters.gtf -fo mm_GRCm38_3kb_promoters.fasta
```

The input FASTA file with -fi.
Input BED file is specified with -bed and output FASTA file of extracted sequences is specified with -fo.

## Coverage with BEDTools

BEDTools’s genomecov subcommand is a versatile tool for summarizing the coverage of features along chromosome sequences. By default, it summarizes the coverage per chromosome sequence (and across the entire genome) as a histogram. A simple example will make this clearer:

```powershell
$ cat ranges-cov.bed
chr1     4       9
chr1     1       6
chr1     8       19
chr1     25       30
chr2     0       20

$ cat cov.txt
chr1     30
chr2     20

$ bedtools genomecov -i ranges-cov.bed -g cov.txt
chr1     0       7       30      0.233333 ①
chr1     1       20      30      0.666667
chr1     2       3       30      0.1
chr2     1       20      20      1 ②
genome    0       7       50      0.14 ③
genome    1       40      50      0.8
genome    2       3       50      0.06
```

1 By default, genomecov summarizes the number of bases covered at a certain depth, per chromosome. The columns are depth, how many bases covered at this depth, total number of bases per chromosome, and proportion of bases covered at this depth. Here, we see that 23% of chr1’s bases are not covered (coverage of zero); 7/30 is around 0.23.
chr2 is entirely covered by the only range on this sequence, so its proportion covered at depth 1 is 1.
genomecov also includes genome-wide statistics on coverage.

![](images/page_365_image_0.jpg)

## Sorting Chromosomes

BEDTools genomecov requires that all ranges from a particular chromosome are grouped together—in other words, consecutive in the BED file. Because the first column of a BED file is the chromosome, we can easily group features with Unix sort, using: sort - k1,1 ranges.bed > ranges.sorted.bed. See “Sorting Plain-Text Data with Sort” on page 147 for more information on Unix sort.

With bedtools genomecov, it’s also possible to get per-base pair coverage. This is much like GenomicRanges coverage():

```powershell
$ bedtools genomecov -i ranges-cov.bed -g cov.txt -d | head -n5
chr1     1       0
chr1     2       1
chr1     3       1
chr1     4       1
chr1     5       2
```

These three columns correspond to the chromosome, the position on that chromosome, and the coverage at that position. As you might imagine, this is not the most compact format for per-base coverage statistics. A much better solution is to use the BedGraph format. BedGraph is similar to the run-length encoding we encountered earlier, except runs of the same depth are stored as the ranges. We can tell genomecov to output data in BedGraph format using:

```powershell
$ bedtools genomecov -i ranges-cov.bed -g cov.txt -bg
chr1     1       4       1
chr1     4       6       2
chr1     6       8       1
chr1     8       9       2
chr1     9       19       1
chr1     25       30       1
chr2     0       20       1
```

## Other BEDTools Subcommands and pybedtools

There are many other useful subcommands in the BEDTools suite that we don’t have the space to discuss. BEDTools subcommands are extensively well documented though, both within the command itself (discussed earlier) and online at [the BED‐Tools documentation site](http://bedtools.readthedocs.org). The following are a few useful subcommands worth reading about:

## bedtools annotate

This is an incredibly useful command that takes a set of files (e.g., BED files for CpG islands, conservation tracks, methylation regions, etc.) and annotates how much coverage each of these files has over another input file (e.g., exonic regions).

bedtools merge

merge is a lot like the GenomicRanges reduce() method; it merges overlapping ranges into a single range.

bedtools closest

This subcommand is a lot like the GenomicRanges nearest() method.

bedtools complement

This is the BEDTools version of gaps() (similar to setdiff() too).

bedtools multicov

multicov counts the number of alignments in multiple BAM files that overlap a specified BED file. This is an incredibly useful tool for counting overlaps across numerous BED files, which could represent different samples or treatments.

bedtools multiinter

This subcommand is similar to bedtools intersect, but works with multiple file inputs. multiinter will return whether each input BED file overlaps a given feature. This is useful for comparing whether experimental data (e.g., ChIP-Seq peaks or DNase I hypersensitivity sites) for many samples intersect features differently across samples. Similarly, the subcommand bedtools jaccard can calculate similarity metrics for pairs of datasets to summarize similarities across samples through a simple statistic (Jaccard Similarity).

bedtools unionbedg

This subcommand merges multiple BedGraph files into a single file.

This is not an exhaustive subcommand list; see the full listing at [the BEDTools documentation website](http://bedtools.readthedocs.org/).

Finally, it’s worth mentioning [the Pybedtools library](http://pythonhosted.org/pybedtools/) (Dale et al., 2011). Pybedtools is an excellent Python wrapper for BEDTools that allows you to employ BEDTools’s range operations from within Python.