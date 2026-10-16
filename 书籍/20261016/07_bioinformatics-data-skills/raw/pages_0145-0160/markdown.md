and set of results to an exact version of data summarized by the data’s checksum value.

## SHA and MD5 Checksums

The two most common checksum algorithms for ensuring data integrity are MD5 and SHA-1. We’ve already encountered SHA-1 in Chapter 4, as this is what Git uses for its commit IDs. MD5 is an older checksum algorithm, but one that is still commonly used. Both MD5 and SHA-1 behave similarly, but SHA-1 is newer and generally preferred. However, MD5 is more common; it’s likely to be what you encounter if a server has precomputed checksums on a set of files.

Let’s get acquainted with checksums using SHA-1. We can pass arbitrary strings to the program shasum (on some systems, it’s sha1sum) through standard in:

```shell
$ echo "bioinformatics is fun" | shasum
f9b70d0d1b0a55263f1b012adab6abf572e3030b  -
$ echo "bioinformatic is fun" | shasum
e7f33eedcfdc9aef8a9b4fec07e58f0cf292aa67  -
```

The long string of numbers and letters is the SHA-1 checksum. Checksums are reported in hexadecimal format, where each digit can be one of 16 characters: digits 0 through 9, and the letters a, b, c, d, e, and f. The trailing dash indicates this is the SHA-1 checksum of input from standard in. Note that when we omitted the “s” in “bioinformatics” and calculate the SHA-1 checksum, the checksum value has entirely changed. This is the strength of using checksums: they change when the tiniest part of the input changes. Checksums are completely deterministic, meaning that regardless of the time the checksum is calculated or the system used, checksum values will only differ if the input differs.

We can also use checksums with file input (note that the content of Csyrichta\_TAG‐GACT\_L008\_R1\_001.fastq is fake example data):

```txt
$ shasum Csyrichta_TAGGACT_L008_R1_001.fastq
fea7d7a582cdfb64915d486ca39da9ebf7ef1d83  Csyrichta_TAGGACT_L008_R1_001.fastq
```

If our sequencing center says the checksum of the Csyrichta\_TAG‐GACT\_L008\_R1\_001.fastq.gz sequencing file is “069bf5894783db241e26f4e44201bd12f2d5aa42” and our local SHA checksum is “fea7d7a582cdfb64915d486ca39da9ebf7ef1d83,” we know our file differs somehow from the original version.

When downloading many files, it can get rather tedious to check each checksum individually. The program shasum has a convenient solution—it can create and validate against a file containing the checksums of files. We can create a SHA-1 checksum file for all FASTQ files in the data/ directory as follows:

```txt
$ shasum data/*fastq > fastq_checksums.sha
$ cat fastq_checksums.sha
524d9a057c51b1[...]d8b1cbe2eaf92c96a9 data/Csyrichta_TAGGACT_L008_R1_001.fastq
d2940f444f00c7[...]4f9c9314ab7e1a1b16 data/Csyrichta_TAGGACT_L008_R1_002.fastq
623a4ca571d572[...]1ec51b9ecd53d3aef6 data/Csyrichta_TAGGACT_L008_R1_003.fastq
f0b3a4302daf7a[...]7bf1628dfcb07535bb data/Csyrichta_TAGGACT_L008_R1_004.fastq
53e2410863c36a[...]4c4c219966dd9a2fe5 data/Csyrichta_TAGGACT_L008_R1_005.fastq
e4d0ccf541e90c[...]5db75a3bef8c88ede7 data/Csyrichta_TAGGACT_L008_R1_006.fastq
```

Then, we can use shasum’s check option (-c) to validate that these files match the original versions:

```shell
$ shasum -c fastq_checksums.sha
data/Csyrichta_TAGGACT_L008_R1_001.fastq: OK
data/Csyrichta_TAGGACT_L008_R1_002.fastq: OK
data/Csyrichta_TAGGACT_L008_R1_003.fastq: OK
data/Csyrichta_TAGGACT_L008_R1_004.fastq: OK
data/Csyrichta_TAGGACT_L008_R1_005.fastq: OK
data/Csyrichta_TAGGACT_L008_R1_006.fastq: FAILED
shasum: WARNING: 1 computed checksum did NOT match
```

In the event that the checksums of a file disagree, shasum will show you which file failed validation and exit with a nonzero error status.

The program md5sum (or md5 on OS X) calculates MD5 hashes and is similar in operation to shasum. However, note that on OS X, the md5 command doesn’t have the -c option, so you’ll need to install the GNU version for this option. Also, some servers use an antiquated checksum implementation such as sum or chsum. How we use these older command-line checksum programs is similar to using shasum and md5sum.

Finally, you may be curious how all files can be summarized by a 40-character-long SHA-1 checksum. They can’t—there are only 16<sup>40</sup> possible different checksums. However, 16<sup>40</sup> is a huge number so the probability of a checksum collision is very, very small. For the purposes of checking data integrity, the risk of a collision is negligible.

## Looking at Differences Between Data

While checksums are a great method to check if files are different, they don’t tell us how files differ. One approach to this is to compute the diff between two files using the Unix tool diff. Unix’s diff works line by line, and outputs blocks (called hunks) that differ between files (resembling Git’s git diff command we saw in Chapter 4).

Suppose you notice a collaborator was working with a different version of a file than the one you’re using. Her version is gene-2.bed, and your version is gene-1.bed (these files are on GitHub if you’d like to follow along). Because downstream results depend on this dataset, you want to check if the files are indeed different. After comparing the SHA-1 checksums, you find the files aren’t identical. Before rerunning your analysis using your collaborator’s version, you’d like to check whether the files differ significantly. We can do this by computing the diff between gene-1.bed and gene-2.bed:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$ diff -u gene-1.bed gene-2.bed
--- gene-1.bed 2014-02-22 12:53:14.000000000 -0800 ①
+++ gene-2.bed 2015-03-10 01:55:01.000000000 -0700
@@ -1,22 +1,19 @@ ②
1 6206197 6206270 GENE00000025907
1 6223599 6223745 GENE00000025907 ③
1 6227940 6228049 GENE00000025907
+1 6222341 6228319 GENE00000025907 ④
1 6229959 6230073 GENE00000025907
-1 6230003 6230005 GENE00000025907 ⑤
1 6233961 6234087 GENE00000025907
1 6234229 6234311 GENE00000025907
1 6206227 6206270 GENE00000025907
1 6227940 6228049 GENE00000025907
1 6229959 6230073 GENE00000025907
-1 6230003 6230073 GENE00000025907 ⑥
+1 6230133 6230191 GENE00000025907
1 6233961 6234087 GENE00000025907
1 6234229 6234399 GENE00000025907
1 6238262 6238384 GENE00000025907
-1 6214645 6214957 GENE00000025907
1 6227940 6228049 GENE00000025907
1 6229959 6230073 GENE00000025907
-1 6230003 6230073 GENE000OOO259O7
1 6233961 6234O87 GENEOOOOOO259O7
1 6234229 6234399 GENEOOOOOO259O7
-1 6238262 6238464 GENEOOOOOO259O7
1 6239952 624O378 GENEOOOOOO259O7
</div>

The option -u tells diff to output in unified diff format, which is a format nearly identical to the one used by git diff. I’ve chosen to use unified diffs rather than diff’s default diff format because unified diffs provide more context.

Unified diffs are broken down into hunks that differ between the two files. Let’s step through the key parts of this format:

These two lines are the header of the unified diff. The original file gene-1.bed is prefixed by ---, and the modified file gene-2.bed is prefixed by +++. The date and time in these two lines are the modification times of these files.
This line indicates the start of a changed hunk. The pairs of integers between @@ and @@ indicate where the hunk begins, and how long it is, in the original file (-1,22) and modified file (+1,19), respectively.
Lines in the diff that begin with a space indicate the modified file’s line hasn’t changed.

Lines in the diff that begin with a + indicate a line has been added to the modified file.
Similarly, - indicates lines removed in the modified file.
An adjacent line deletion and line addition indicates that this line was changed in the modified file.

Diff files appear very cryptic at first, but you’ll grow familiar with them over time. diff’s output can also be redirected to a file, which creates a patch file. Patch files act as instructions on how to update a plain-text file, making the changes contained in the diff file. The Unix tool patch can apply changes to a file needed to be patched. Patches are used more commonly in software development than bioinformatics, so we won’t cover them in detail. Lastly, it’s important to note that diffs can be computationally expensive to compute on large files, so be cautious when running diff on large datasets.

## Compressing Data and Working with Compressed Data

Data compression, the process of condensing data so that it takes up less space (on disk drives, in memory, or across network transfers), is an indispensable technology in modern bioinformatics. For example, sequences from a recent Illumina HiSeq run when compressed with Gzip take up 21,408,674,240 bytes, which is a bit under 20 gigabytes. Uncompressed, this file is a whopping 63,203,414,514 bytes (around 58 gigabytes). This FASTQ file has 150 million 200bp reads, which is 10x coverage of the human genome, 190x coverage of the Arabidopsis genome, or a measly 2x coverage of the hexaploid wheat genome. The compression ratio (uncompressed size/ compressed size) of this data is approximately 2.95, which translates to a significant space saving of about 66%. Your own bioinformatics projects will likely contain much more data, especially as sequencing costs continue to drop and it’s possible to sequence genomes to higher depth, include more biological replicates or time points in expression studies, or sequence more individuals in genotyping studies.

For the most part, data can remain compressed on the disk throughout processing and analyses. Most well-written bioinformatics tools can work natively with compressed data as input, without requiring us to decompress it to disk first. Using pipes and redirection (covered in Chapter 3), we can stream compressed data and write compressed files directly to the disk. Additionally, common Unix tools like cat, grep, and less all have variants that work with compressed data, and Python’s gzip module allows us to read and write compressed data from within Python. So while working with large datasets in bioinformatics can be challenging, using the compression tools in Unix and software libraries make our lives much easier.

## gzip

The two most common compression systems used on Unix are gzip and bzip2. Both have their advantages: gzip compresses and decompresses data faster than bzip2, but bzip2 has a higher compression ratio (the previously mentioned FASTQ file is only about 16 GB when compressed with bzip2). Generally, gzip is used in bioinformatics to compress most sizable files, while bzip2 is more common for long-term data archiving. We’ll focus primarily on gzip, but bzip2’s tools behave very similarly to gzip.

The command-line tool gzip allows you to compress files in a few different ways. First, gzip can compress results from standard input. This is quite useful, as we can compress results directly from another bioinformatics program’s standard output. For example, suppose we have a program that removes low-quality bases from FASTQ files called trimmer (this is an imaginary program). Our trimmer program can handle gzipped input files natively, but writes uncompressed trimmed FASTQ results to standard output. Using gzip, we can compress trimmer’s output in place, before writing to the disk:

```txt
$ trimmer in.fastq.gz | gzip > out.fastq.gz
```

gzip takes input from standard in, compresses it, and writes this compressed output to standard out.

gzip also can compress files on disk in place. If our in.fastq.gz file weren’t compressed, we could compress it as follows:

```ignorefile
$ ls
in.fastq
$ gzip in.fastq
$ ls
in.fastq.gz
```

gzip will compress this file in place, replacing the original uncompressed version with the compressed file (appending the extension .gz to the original filename). Similarly, we can decompress files in place with the command gunzip:

```txt
$ gunzip in.fastq.gz
$ ls
in.fastq
```

Note that this replaces our in.fastq.gz file with the decompressed version (removing the .gz suffix, too). Both gzip and gunzip can also output their results to standard out (rather than changing files in place). This can be enabled using the -c option:

```shell
$ gzip -c in.fastq > in.fastq.gz
$ gunzip -c in.fastq.gz > duplicate_in.fastq
```

A nice feature of the gzip compression algorithm is that you can concatenate gzip compressed output directly to an existing gzip file. For example, if we wanted to compress the in2.fastq file and append it to our compressed in.fastq.gz file, we wouldn’t have to decompress in.fastq.gz first, concatenate the two files, and then compress the concatenated file. Instead, we can do the following:

```txt
$ ls
in.fastq.gz in2.fastq
$ gzip -c in2.fastq >> in.fastq.gz
```

Importantly, note that the redirection operator we use is >>; had we used >, we would overwrite our compressed version of in2.fastq to in.fastq.gz (rather than append to it). Always exercise caution when using redirection, and make sure you’re using the appropriate operator (and keep file backups!). You may get a slightly better compression ratio by compressing everything together (e.g., with cat in.fastq in2.fastq | gzip > in.fastq.gz), but the convenience of appending to an existing gzipped file is useful. Also, note that gzip does not separate these compressed files: files compressed together are concatenated. If you need to compress multiple separate files into a single archive, use the tar utility (see the examples section of man tar for details).

## Working with Gzipped Compressed Files

Perhaps the greatest advantage of gzip (and bzip2) is that many common Unix and bioinformatics tools can work directly with compressed files. For example, we can search compressed files using grep’s analog for gzipped files, zgrep. Likewise, cat has zcat (on some systems like OS X, this is gzcat), diff has zdiff, and less has zless. If programs cannot handle compressed input, you can use zcat and pipe output directly to the standard input of another program.

These programs that handle compressed input behave exactly like their standard counterpart. For example, all options available in grep are available in zgrep:

```powershell
$ zgrep --color -i -n "AGATAGAT" Csyrichta_TAGGACT_L008_R1_001.fastq.gz
2706: ACTTCGGAGAGCCCATATATACACACTAAGATAGATAGCGTTAGCTAATGTAGATAGATT
```

There can be a slight performance cost in working with gzipped files, as your CPU must decompress input first. Usually, the convenience of z-tools like zgrep, zless, and zcat and the saved disk space outweigh any potential performance hits.

## Case Study: Reproducibly Downloading Data

Downloading data reproducibly can be deceptively complex. We usually download genomic resources like sequence and annotation files from remote servers over the Internet, which may change in the future. Furthermore, new versions of sequence and annotation data may be released, so it’s imperative that we document everything about how data was acquired for full reproducibility. As a demonstration of this, let’s step through a case study. We’ll download a few genomic and sequence resources for mouse (Mus musculus) and document how we acquired them.

For this example, we’ll download the GRCm38 mouse reference genome and accompanying annotation. Note that this case study involves downloading large files, so you may not want to follow along with these examples. The mouse, human (Homo sapiens), and zebrafish (Danio rerio) genomes releases are coordinated through [the Genome Reference Consortium](http://bit.ly/gene-ref-con). The “GRC” prefix in GRCm38 refers to the Genome Reference Consortium. We can download GRCm38 from Ensembl (a member of the consortium) using wget. For this and other examples in this section, I’ve had to truncate the URLs so they fit within a book’s page width; see this chapter’s README.md on GitHub for the full links for copying and pasting if you’re following along.

\$ wget ftp://ftp.ensembl.org/[...]/Mus\_musculus.GRCm38.74.dna.toplevel.fa.gz

Ensembl’s website provides links to reference genomes, annotation, variation data, and other useful files for many organisms. This FTP link comes from navigating to [http://www.ensembl.org](http://www.ensembl.org), clicking the mouse project page, and then clicking the “Download DNA sequence” link. If we were to document how we downloaded this file, our Markdown README.md might include something like:

Mouse (\*Mus musculus\*) reference genome version GRCm38 (Ensembl release 74) was downloaded on Sat Feb 22 21:24:42 PST 2014, using:

wget ftp://ftp.ensembl.org/[...]/Mus\_musculus.GRCm38.74.dna.toplevel.fa.gz

We might want to look at the chromosomes, scaffolds, and contigs this files contains as a sanity check. This file is a gzipped FASTA file, so we can take a quick peek at all sequence headers by grepping for the regular expression "^>", which matches all lines beginning with > (a FASTA header). We can use the zgrep program to extract the FASTA headers on this gzipped file:

\$ zgrep "^>" Mus\_musculus.GRCm38.74.dna.toplevel.fa.gz | less

Ensembl also provides a checksum file in the parent directory called CHECKSUMS. This checksum file contains checksums calculated using the older Unix tool sum. We can compare our checksum values with those in CHECKSUMS using the sum program:

\$ wget ftp://ftp.ensembl.org/pub/release-74/fasta/mus\_musculus/dna/CHECKSUMS\$ sum Mus\_musculus.GRCm38.74.dna.toplevel.fa.gz 53504 793314

The checksum 53504 agrees with the entry in the CHECKSUMS file for the entry Mus\_musculus.GRCm38.74.dna.toplevel.fa.gz. I also like to include the SHA-1 sums of all important data in my data README.md file, so future collaborators can verify their data files are exactly the same as those I used. Let’s calculate the SHA-1 sum using shasum:

```txt
$ shasum Mus_musculus.GRCm38.74.dna.toplevel.fa.gz
01c868e22a981[...]c2154c20ae7899c5f  Mus_musculus.GRCm38.74.dna.toplevel.fa.gz
```

Then, we can copy and paste this SHA-1 sum into our README.md. Next, we can download an accompanying GTF from Ensembl and the CHECKSUMS file for this directory:

```txt
$ wget ftp://ftp.ensembl.org/[...]/Mus_musculus.GRCm38.74.gtf.gz
$ wget ftp://ftp.ensembl.org/[...]/CHECKSUMS
```

Again, let’s ensure that our checksums match those in the CHECKSUMS file and run shasum on this file for our own documentation:

```txt
$ sum Mus_musculus.GRCm38.74.gtf.gz
00985 15074
$ shasum cf5bb5f8bda2803410bb04b708bff59cb575e379 Mus_musculus.GRCm38.74.gtf.gz
```

And again, we copy the SHA-1 into our README.md. So far, our README.md might look as follows:

```markdown
## Genome and Annotation Data
```

```txt
Mouse (*Mus musculus*) reference genome version GRCm38 (Ensembl release 74) was downloaded on Sat Feb 22 21:24:42 PST 2014, using:
```

```javascript
wget ftp://ftp.ensembl.org/[...]/Mus_musculus.GRCm38.74.dna.toplevel.fa.gz
```

```txt
Gene annotation data (also Ensembl release 74) was downloaded from Ensembl on Sat Feb 22 23:30:27 PST 2014, using:
```

```txt
wget ftp://ftp.ensembl.org/[...]/Mus_musculus.GRCm38.74.gtf.gz
```

```markdown
## SHA-1 Sums
```

```txt
- `Mus_musculus.GRCm38.74.dna.toplevel.fa.gz`: 01c868e22a9815c[...]c2154c20ae7899c5f
- `Mus_musculus.GRCm38.74.gtf.gz`: cf5bb5f8bda2803[...]708bff59cb575e379
```

Although this isn’t a lot of documentation, this is infinitely better than not documenting how data was acquired. As this example demonstrates, it takes very little effort to properly track the data that enters your project, and thereby ensure reproducibility. The most important step in documenting your work is that you’re consistent and make it a habit.

## Practice: Bioinformatics Data Skills

# Unix Data Tools

We often forget how science and engineering function. Ideas come from previous exploration more often than from lightning strokes.

—John W. Tukey

In Chapter 3, we learned the basics of the Unix shell: using streams, redirecting output, pipes, and working with processes. These core concepts not only allow us to use the shell to run command-line bioinformatics tools, but to leverage Unix as a modular work environment for working with bioinformatics data. In this chapter, we’ll see how we can combine the Unix shell with command-line data tools to explore and manipulate data quickly.

## Unix Data Tools and the Unix One-Liner Approach: Lessons from Programming Pearls

Understanding how to use Unix data tools in bioinformatics isn’t only about learning what each tool does, it’s about mastering the practice of connecting tools together— creating programs from Unix pipelines. By connecting data tools together with pipes, we can construct programs that parse, manipulate, and summarize data. Unix pipelines can be developed in shell scripts or as “one-liners”—tiny programs built by connecting Unix tools with pipes directly on the shell. Whether in a script or as a oneliner, building more complex programs from small, modular tools capitalizes on the design and philosophy of Unix (discussed in “Why Do We Use Unix in Bioinformatics? Modularity and the Unix Philosophy” on page 37). The pipeline approach to building programs is a well-established tradition in Unix (and bioinformatics) because it’s a fast way to solve problems, incredibly powerful, and adaptable to a variety of a problems. An illustrative example of the power of simple Unix pipelines comes from a famous exchange between two brilliant computer scientists: Donald Knuth and Doug McIlroy (recall from Chapter 3 that McIlroy invented Unix pipes).

In a 1986 “Programming Pearls” column in the Communications of the ACM maga zine, columnist Jon Bentley had computer scientist Donald Knuth write a simple program to count and print the k most common words in a file alongside their counts, in descending order. Knuth was chosen to write this program to demonstrate literate programming, a method of programming that Knuth pioneered. Literate programs are written as a text document explaining how to solve a programming problem (in plain English) with code interspersed throughout the document. Code inside this document can then be “tangled” out of the document using literate programming tools (this approach might be recognizable to readers familiar with R’s knitr or Sweave—both are modern descendants of this concept). Knuth’s literate program was seven pages long, and also highly customized to this particular programming problem; for example, Knuth implemented a custom data structure for the task of counting English words. Bentley then asked that McIlroy critique Knuth’s seven-page-long solution. McIlroy commended Knuth’s literate programming and novel data structure, but overall disagreed with his engineering approach. McIlroy replied with a sixline Unix script that solved the same programming problem:

```shell
tr -cs A-Za-z '\n' | ①
tr A-Z a-z | ②
sort | ③
uniq -c | ④
sort -rn | ⑤
sed \${1}q ⑥
```

While you shouldn’t worry about fully understanding this now (we’ll learn these tools in this chapter), McIlroy’s basic approach was:

Translate all nonalphabetical characters (-c takes the complement of the first argument) to newlines and squeeze all adjacent characters together (-s) after translating. This creates one-word lines for the entire input stream.
(2) Translate all uppercase letters to lowercase.
Sort input, bringing identical words on consecutive lines.
④ Remove all duplicate consecutive lines, keeping only one with a count of the occurrences (-c).
Sort in reverse (-r) numeric order (-n).
Print the first k number of lines supplied by the first argument of the script (\${1}) and quit.

McIlroy’s solution is a beautiful example of the Unix approach. McIlroy originally wrote this as a script, but it can easily be turned into a one-liner entered directly on the shell (assuming k here is 10). However, I’ve had to add a line break here so that the code does not extend outside of the page margins:

```shell
$ cat input.txt \
| tr -cs A-Za-z '\n' | tr A-Z a-z | sort | uniq -c | sort -rn | sed 10q
```

McIlroy’s script was doubtlessly much faster to implement than Knuth’s program and works just as well (and arguably better, as there were a few minor bugs in Knuth’s solution). Also, his solution was built on reusable Unix data tools (or as he called them, “Unix staples”) rather than “programmed monolithically from scratch,” to use McIlroy’s phrasing. The speed and power of this approach is why it’s a core part of bioinformatics work.

## When to Use the Unix Pipeline Approach and How to Use It Safely

Although McIlroy’s example is appealing, the Unix one-liner approach isn’t appropriate for all problems. Many bioinformatics tasks are better accomplished through a custom, well-documented script, more akin to Knuth’s program in “Programming Pearls.” Knowing when to use a fast and simple engineering solution like a Unix pipeline and when to resort to writing a well-documented Python or R script takes experience. As with most tasks in bioinformatics, choosing the most suitable approach can be half the battle.

Unix pipelines entered directly into the command line shine as a fast, low-level data manipulation toolkit to explore data, transform data between formats, and inspect data for potential problems. In this context, we’re not looking for thorough, theoryshattering answers—we usually just want a quick picture of our data. We’re willing to sacrifice a well-documented implementation that solves a specific problem in favor of a quick rough picture built from modular Unix tools. As McIlroy explained in his response:

The simple pipeline … will suffice to get answers right now, not next week or next month. It could well be enough to finish the job. But even for a production project … it would make a handsome down payment, useful for testing the value of the answers and for smoking out follow-on questions.

—Doug McIlroy (my emphasis)

Many tasks in bioinformatics are of this nature: we want to get a quick answer and keep moving forward with our project. We could write a custom script, but for simple tasks this might be overkill and would take more time than necessary. As we’ll see later in this chapter, building Unix pipelines is fast: we can iteratively assemble and test Unix pipelines directly in the shell.

For larger, more complex tasks it’s often preferable to write a custom script in a language like Python (or R if the work involves lots of data analysis). While shell approaches (whether a one-liner or a shell script) are useful, these don’t allow for the same level of flexibility in checking input data, structuring programs, use of data structures, code documentation, and adding assert statements and tests as languages like Python and R. These languages also have better tools for stepwise documentation of larger analyses, like R’s knitr (introduced in the “Reproducibility with Knitr and Rmarkdown” on page 254) and iPython notebooks. In contrast, lengthy Unix pipelines can be fragile and less robust than a custom script.

So in cases where using Unix pipelines is appropriate, what steps can we take to ensure they’re reproducible? As mentioned in Chapter 1, it’s essential that everything that produces a result is documented. Because Unix one-liners are entered directly in the shell, it’s particularly easy to lose track of which one-liner produced what version of output. Remembering to record one-liners requires extra diligence (and is often neglected, especially in bioinformatics work). Storing pipelines in scripts is a good approach—not only do scripts serve as documentation of what steps were performed on data, but they allow pipelines to be rerun and can be checked into a Git repository. We’ll look at scripting in more detail in Chapter 12.

## Inspecting and Manipulating Text Data with Unix Tools

In this chapter, our focus is on learning how to use core Unix tools to manipulate and explore plain-text data formats. Many formats in bioinformatics are simple tabular plain-text files delimited by a character. The most common tabular plain-text file format used in bioinformatics is tab-delimited. This is not an accident: most Unix tools such as cut and awk treat tabs as delimiters by default. Bioinformatics evolved to favor tab-delimited formats because of the convenience of working with these files using Unix tools. Tab-delimited file formats are also simple to parse with scripting languages like Python and Perl, and easy to load into R.

## Tabular Plain-Text Data Formats

Tabular plain-text data formats are used extensively in computing. The basic format is incredibly simple: each row (also known as a record) is kept on its own line, and each column (also known as a field) is separated by some delimiter. There are three flavors you will encounter: tab-delimited, comma-separated, and variable space-delimited.

Of these three formats, tab-delimited is the most commonly used in bioinformatics. File formats such as BED, GTF/GFF, SAM, tabular BLAST output, and VCF are all examples of tab-delimited files. Columns of a tab-delimited file are separated by a sin gle tab character (which has the escape code \t). A common convention (but not a standard) is to include metadata on the first few lines of a tab-delimited file. These metadata lines begin with # to differentiate them from the tabular data records. Because tab-delimited files use a tab to delimit columns, tabs in data are not allowed.

Comma-separated values (CSV) is another common format. CSV is similar to tabdelimited, except the delimiter is a comma character. While not a common occurrence in bioinformatics, it is possible that the data stored in CSV format contain commas (which would interfere with the ability to parse it). Some variants just don’t allow this, while others use quotes around entries that could contain commas. Unfortunately, there’s no standard CSV format that defines how to handle this and many other issues with CSV—though some guidelines are given in [RFC 4180](http://bit.ly/rfc-4180).

Lastly, there are space-delimited formats. A few stubborn bioinformatics programs use a variable number of spaces to separate columns. In general, tab-delimited formats and CSV are better choices than space-delimited formats because it’s quite common to encounter data containing spaces.

Despite the simplicity of tabular data formats, there’s one major common headache: how lines are separated. Linux and OS X use a single linefeed character (with the escape code \n) to separate lines, while Windows uses a DOS-style line separator of a carriage return and a linefeed character (\r\n). CSV files generally use this DOS-style too, as this is specified in the CSV specification RFC-4180 (which in practice is loosely followed). Occasionally, you might encounter files separated by only carriage returns, too.

In this chapter, we’ll work with very simple genomic feature formats: BED (threecolumn) and GTF files. These file formats store the positions of features such as genes, exons, and variants in tab-delimited format. Don’t worry too much about the specifics of these formats; we’ll cover both in more detail in Chapter 9. Our goal in this chapter is primarily to develop the skills to freely manipulate plain-text files or streams using Unix data tools. We’ll learn each tool separately, and cumulatively work up to more advanced pipelines and programs.

## Inspecting Data with Head and Tail

Many files we encounter in bioinformatics are much too long to inspect with cat— running cat on a file a million lines long would quickly fill your shell with text scroll ing far too fast to make sense of. A better option is to take a look at the top of a file with head. Here, let’s took a look at the file Mus\_musculus.GRCm38.75\_chr1.bed:

```txt
\$ head Mus_musculus.GRCm38.75_chr1.bed
1       3054233 3054733
1       3054233 3054733
1       3054233 3054733
1       3102016 3102125
1       3102016 3102125
1       3102016 3102125
1       3205901 3671498
1       3205901 3216344
```

```txt
1         3213609 3216344
1         3205901 3207317
```

We can also control how many lines we see with head through the -n argument:

```txt
\$ head -n 3 Mus_musculus.GRCm38.75_chr1.bed
1       3054233 3054733
1       3054233 3054733
1       3054233 3054733
```

head is useful for a quick inspection of files. head -n3 allows you to quickly inspect a file to see if a column header exists, how many columns there are, what delimiter is being used, some sample rows, and so on.

head has a related command designed to look at the end, or tail of a file. tail works just like head:

```txt
$ tail -n 3 Mus_musculus.GRCm38.75_chr1.bed
1       195240910        195241007
1       195240910        195241007
1       195240910        195241007
```

We can also use tail to remove the header of a file. Normally the -n argument specifies how many of the last lines of a file to include, but if -n is given a number x preceded with a + sign (e.g., +x), tail will start from the x<sup>th</sup> line. So to chop off a header, we start from the second line with -n +2. Here, we’ll use the command seq to generate a file of 3 numbers, and chop of the first line:

```txt
$ seq 3 > nums.txt
$ cat nums.txt
1
2
3
$ tail -n +2 nums.txt
2
3
```

Sometimes it’s useful to see both the beginning and end of a file—for example, if we have a sorted BED file and we want to see the positions of the first feature and last feature. We can do this using a trick from data scientist (and former bioinformatician) Seth Brown:

```txt
$ (head -n 2; tail -n 2) < Mus_musculus.GRCm38.75_chr1.bed
1       3054233 3054733
1       3054233 3054733
1       195240910      195241007
1       195240910      195241007
```

This is a useful trick, but it’s a bit long to type. To keep it handy, we can create a shortcut in your shell configuration file, which is either \~/.bashrc or \~/.profile: