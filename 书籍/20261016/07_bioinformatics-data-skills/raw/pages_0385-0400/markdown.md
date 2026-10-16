# Working with Alignment Data

In Chapter 9, we learned about range formats such as BED and GTF, which are often used to store genomic range data associated with genomic feature annotation data such as gene models. Other kinds of range-based formats are designed for storing large amounts of alignment data—for example, the results of aligning millions (or billions) of high-throughput sequencing reads to a genome. In this chapter, we’ll look at the most common high-throughput data alignment format: the Sequence Alignment/ Mapping (SAM) format for mapping data (and its binary analog, BAM). The SAM and BAM formats are the standard formats for storing sequencing reads mapped to a reference.

We study SAM and BAM for two reasons. First, a huge part of bioinformatics work is manipulating alignment files. Nearly every high-throughput sequencing experiment involves an alignment step that produces alignment data in the SAM/BAM formats. Because each sequencing read has an alignment entry, alignment data files are massive and require space-efficient complex binary file formats. Furthermore, modern aligners output an incredible amount of useful information about each alignment. It’s vital to have the skills necessary to extract this information and explore data kept in these complex formats.

Second, the skills developed through learning to work with SAM/BAM files are extensible and more widely applicable than to these specific formats. It would be unwise to bet that these formats won’t change (or even be replaced at some point)— the field of bioinformatics is notorious for inventing new data formats (the same goes with computing in general, see [xkcd’s “Standards” comic](http://xkcd.com/927/)). Some groups are already switching to storing alignments in CRAM format, a closely related alignment data format we’ll also discuss. So while learning how to work with specific bioinformatics formats may seem like a lost cause, skills such as following a format specification, manipulating binary files, extracting information from bitflags, and working with application programming interfaces (APIs) are essential skills when working with any format.

## Getting to Know Alignment Formats: SAM and BAM

Before learning to work with SAM/BAM, we need to understand the structure of these formats. We’ll do this by using celegans.sam, a small example SAM file included in this chapter’s directory in the GitHub repository.

![](images/page_385_image_3.jpg)

The celegans.sam file was created by aligning reads simulated directly from the C. elegans genome (version WBcel235) using the wgsim read simulator. These reads differ slightly from the reference genome through simulated mutations and base errors. Simulating reads, realigning back to the reference, and calling SNPs is a very useful exercise in understanding the limitations of aligners and SNP callers; I encourage you to try this on your own. See the documentation in this chapter’s directory on GitHub for more information on how these reads were simulated and why this is a useful exercise.

We’ll step through the basic ideas of the SAM/BAM format, but note that as with any well-specified bioinformatics format, the ultimate reference is the original format specification and documentation, which is available on [GitHub](http://samtools.github.io/hts-specs/). [The original SAM Format paper](http://bit.ly/sam-format) (Li et al., 2009) is also a good introduction.

## The SAM Header

Files in the SAM format consist of a header section and an alignment section. Because SAM files are plain text (unlike their binary counterpart, BAM), we can take a peek at a few lines of the header with head:

```powershell
$ head -n 10 celegans.sam
@SQ     SN:I    LN:15072434 ①
@SQ     SN:II   LN:15279421
@SQ     SN:III  LN:13783801
@SQ     SN:IV   LN:17493829
@SQ     SN:MtDNA      LN:13794
@SQ     SN:V    LN:20924180
@SQ     SN:X    LN:17718942
@RG     ID:VB00023_L001 SM:celegans-01 ②
@PG     ID:bwa  PN:bwa  VN:0.7.10-r789 [...] ③
I_2011868_2012306_0:0:0_0:0:0_2489 83 I 2012257 40 50M [...] ④
```

Header lines contain vital metadata about the reference sequences, read and sample information, and (optionally) processing steps and comments. Each header line begins with an @, followed by a two-letter code that distinguishes the different type of metadata records in the header. Following this two-letter code are tab-delimited keyvalue pairs in the format KEY:VALUE (the SAM format specification names these tags and values). The celegans.sam file contains the most common header records types you’ll encounter in SAM/BAM files. Let’s step through some of the header components in more detail:

1 @SQ header entries store information about the reference sequences (e.g., the chromosomes if you’ve aligned to a reference genome). The required key-values are SN, which stores the sequence name (e.g., the C. elegans chromosome I), and LN, which stores the sequence length (e.g., 15,072,434 bases). All separate sequences in your reference have a corresponding entry in the header.

② @RG header entries contain important read group and sample metadata. The read group identifier ID is required and must be unique. This ID value contains information about the origin of a set of reads. Some software relies on read groups to indicate a technical groups of reads, to account for batch effects (undesirable technical artifacts in data). Consequently, it’s beneficial to create read groups related to the specific sequencing run (e.g., ID could be related to the name of the sequencing run and lane).

Although ID is the only required key in @RG headers, in practice your SAM/BAM files should also keep track of sample information using the SM key. Sample infor mation is the metadata about your experiment’s samples (e.g., individual, treatment group, replicate, etc.). Finally, it’s worth noting that the SAM format specification also allows a PL key for indicating sequencing platform such as ILLUMINA, PACBIO, and so on. (See the specification for a full list of valid values.) Read group, sample, and platform information should be added to your SAM/BAM during alignment (and aligners have options for this).

@PG header entries contain metadata about the programs used to create and process a set of SAM/BAM files. Each program must have a unique ID value, and metadata such as program version number (via the VN key) and the exact command line (via the CL key) can be saved in these header entries. Many programs will add these lines automatically.
4 This is the first line of the alignment section (because this line does not begin with @). We’ll cover the alignment section in more detail in the following section.

This is just an introduction to the basics of the SAM format’s header section; see [the SAM format specification](http://samtools.github.io/hts-specs/) for more detail.

![](images/page_387_image_0.jpg)

## Read Groups

One of the best features of the SAM/BAM format is that it supports including an extensive amount of metadata about the samples, the alignment reference, processing steps, etc. to be included within the file. (Note that in contrast, the FASTQ format doesn’t provide a standard way to include this metadata; in practice, we use filenames to connect metadata kept in a separate spreadsheet or tabdelimited file.) Many downstream applications make use of the metadata contained in the SAM header (and many programs require it). Given that this metadata is important (and often required), you should add read group and sample metadata when you align reads to a reference.

Luckily, most aligners allow you to specify this important metadata through your alignment command. For example, BWA allows (using made-up files in this example):

```powershell
$ bwa mem -R'@RG\tID:readgroup_id\tSM:sample_id' ref.fa
in.fq
```

Bowtie2 similarly allows read group and sample information to be set with the --rg-id and --rg options.

Although head works to take a quick peek at the top of a SAM file, keep the following points in mind:

• head won’t always provide the entire header.
• It won’t work with binary BAM files.

The standard way of interacting with SAM/BAM files is through the SAMtools command-line program (samtools), which we’ll use extensively throughout the rest of this chapter. Like Git, samtools has many subcommands. samtools view is the general tool for viewing and converting SAM/BAM files. A universal way to look at an entire SAM/BAM header is with samtools view option -H:

```txt
$ samtools view -H celegans.sam
@SQ        SN:I    LN:15072434
@SQ        SN:II   LN:15279421
@SQ        SN:III  LN:13783801
[...]
```

This also works with BAM files, without any need to convert beforehand (samtools automatically detects whether the file is SAM or BAM):

```txt
$ samtools view -H celegans.bam
@SQ        SN:I    LN:15072434
@SQ        SN:II   LN:15279421
@SQ        SN:III  LN:13783801
[...]
```

Of course, all our usual Unix tricks can be combined with samtools commands through piping results to other commands. For example, we could see all read groups with:

\$ samtools view -H celegans.bam | grep "^@RG"

@RG ID:VB00023\_L001 SM:celegans-01

samtools view without any arguments returns the entire alignment section without the header:

```txt
$ samtools view celegans.sam | head -n 1
I_2011868_2012306_0:0:0:0:0:0:0_2489      83       I        2012257 40      50M
```

## The SAM Alignment Section

The alignment section contains read alignments (and usually includes reads that did not align, but this depends on the aligner and file). Each alignment entry is composed of 11 required fields (and optional fields after this).

![](images/page_388_image_7.jpg)

We’ll step through the basic structure of an alignment entry, but it would be unnecessarily redundant to include all information in the original SAM format specification in this section. I highly recommend reading the alignment section of the SAM format specification for more detail.

Let’s step through an alignment entry’s fields. Because these alignment lines are quite lengthy and would overflow the width of this page, I use tr to convert tabs to newlines for a single alignment entry in celegans.sam:

```txt
$ samtools view celegans.sam | tr '\t' '\n' | head -n 11
I_2011868_2012306_0:0:0_0:0:0_2489 ①
83 ②
I ③
2012257 ④
40 ⑤
50M ⑥
= ⑦
2011868
-439 ⑧
CAAAAAATTTTGAAAAAAAAATTGAATAAAATTCACGGATTTCTGGCT ⑨
22222222222222222222222222222222222222
```

QNAME, the query name (e.g., a sequence read’s name).
FLAG, the bitwise flag, which contains information about the alignment. Bitwise flags are discussed in “Bitwise Flags” on page 360 in much more detail.

3 RNAME, the reference name (e.g., which sequence the query aligned to, such as a specific chromosome name like “chr1”). The reference name must be in the SAM/BAM header as an SQ entry. If the read is unaligned, this entry may be \*.
POS, the position on the reference sequence (using 1-based indexing) of the first mapping base (leftmost) in the query sequence. This may be zero if the read does not align.
5 MAPQ is the mapping quality, which is a measure of how likely the read is to actually originate from the position it maps to. Mapping quality is estimated by the aligner (and beware that different aligners have different estimation procedures!). Many tools downstream of aligners filter out reads that map with low mapping quality (because a low mapping quality score indicates the alignment program is not confident about the alignment’s position). Mapping qualities are an incredibly important topic that we’ll discuss in more depth later. Mapping quality is discussed in more depth in “Mapping Qualities” on page 365.
6 CIGAR is the CIGAR string, which is a specialized format for describing the alignment (e.g., matching bases, insertions/deletions, clipping, etc.). We discuss CIGAR strings in much more detail in “CIGAR Strings” on page 363.
7 RNEXT and PNEXT (on the next line) are the reference name and position (the R and P in RNEXT and PNEXT) of a paired-end read’s partner. The value \* indicates RNEXT is not available, and = indicates that RNEXT is the same as RNAME. PNEXT will be 0 when not available.
TLEN is the template length for paired-end reads.
9 SEQ stores the original read sequence. This sequence will always be in the orientation it aligned in (and this may be the reverse complement of the original read sequence). Thus, if your read aligned to the reverse strand (which is information kept in the bitwise flag field), this sequence will be the reverse complement.
QUAL stores the original read base quality (in the same format as Sanger FASTQ files).

## Bitwise Flags

Many important pieces of information about an alignment are encoded using bitwise flags (also known as a bit field). There’s a lot of important information encoded in SAM/BAM bitwise flags, so it’s essential you understand how these work. Furthermore, bitwise flags are a very space-efficient and common way to encode attributes, so they’re worth understanding because you’re very likely to encounter them in other formats.

Bitwise flags are much like a series of toggle switches, each of which can be either on or off. Each switch represents whether a particular attribute of an alignment is true or false, such as whether a read is unmapped, is paired-end, or whether it aligned in the reverse orientation. Table 11-1 shows these bitwise flags and the attributes they encode, but the most up-to-date source will be the SAM format specification or the samtools flag command:

\$ samtools flags

```txt
About: Convert between textual and numeric flag representation
Usage: samtools flags INT|STR[,...]
```

Flags:

```txt
0x1 PAIRED .. paired-end (or multiple-segment) sequencing technology
0x2 PROPER_PAIR .. each segment properly aligned according to the aligner
0x4 UNMAP .. segment unmapped
[...]
```

Under the hood, each of these toggle switches’ values are bits (0 or 1) of a binary number (the base-2 system of computing that uses 0s and 1s). Each bit in a bitfield represents a particular attribute about an alignment, with 1 indicating that the attribute is true and 0 indicating it’s false.

Table 11-1. SAM bitwise flags

| Flag (in hexadecimal) | Meaning |
| --- | --- |
| 0x1 | Paired-end sequence (or multiple-segment, as in strobe sequencing) |
| 0x2 | Aligned in proper pair (according to the aligner) |
| 0x4 | Unmapped |
| 0x8 | Mate pair unmapped (or next segment, if multiple-segment) |
| 0x10 | Sequence is reverse complemented |
| 0x20 | Sequence of mate pair is reversed |
| 0x40 | The first read in the pair (or segment, if multiple-segment) |
| 0x80 | The second read in the pair (or segment, if multiple-segment) |
| 0x100 | Secondary alignment |
| 0x200 | QC failure |
| 0x400 | PCR or optical duplicate |
| 0x800 | Supplementary alignment |

As an example, suppose you encounter the bitflag 147 (0x93 in hexidecimal) and you want to know what this says about this alignment. In binary this number is represented as 0x1001 0011 (the space is used to make this more readable). We see that the first, second, fifth, and eighth bits are 1 (in our switch analogy, these are the switches that are turned on). These specific bits correspond to the hexidecimal values 0x1, 0x2, 0x10, and 0x80. Looking at Table 11-1, we see these hexidecimal values correspond to the attributes paired-end, aligned in proper pair, the sequence is reverse complemented, and that this is the second read in the pair—which describes how our read aligned.

![](images/page_391_image_2.jpg)

## Converting between Binary, Hexadecimal, and Decimal

I won’t cover the details of converting between binary, hexadecimal, and decimal number systems because the command samtools flags can translate bitflags for us. But if you continue to dig deeper into computing, it’s a handy and necessary skill. I’ve included some supplementary resources in the GitHub repository’s README file for this chapter. Many calculators, such as the OS X calculator in “programmer” mode will also convert these values for you.

Working through this each time would be quite tedious, so the samtools command contains the subcommand samtools flags, which can translate decimal and hexidecimal flags:

```txt
$ samtools flags 147
0x93    147    PAIRED,PROPER_PAIR,REVERSE,READ2
$ samtools flags 0x93
0x93    147    PAIRED,PROPER_PAIR,REVERSE,READ2
```

samtools flags can also convert attributes (of the prespecified list given by running samtools flags without arguments) to hexidecimal and decimal flags:

```csv
\$ samtools flags paired,read1,qcfail
0x241 577 PAIRED,READ1,QCFAIL
```

Later on, we’ll see how PySAM simplifies this through an interface where properties about an alignment are stored as attributes of an AlignedSegment Python object, which allows for easier checking of bitflag values with a syntax like aln.is\_proper\_pair or aln.is\_reverse.

## CIGAR Strings

Like bitwise flags, SAM’s CIGAR strings are another specialized way to encode information about an aligned sequence. While bitwise flags store true/false properties about an alignment, CIGAR strings encode information about which bases of an alignment are matches/mismatches, insertions, deletions, soft or hard clipped, and so on. I’ll assume you are familiar with the idea of matches, mismatches, insertions, and deletions, but it’s worth describing soft and hard clipping (as SAM uses them).

Soft clipping is when only part of the query sequence is aligned to the reference, leaving some portion of the query sequence unaligned. Soft clipping occurs when an aligner can partially map a read to a location, but the head or tail of the query sequence doesn’t match (or the alignment at the end of the sequence is questionable). Hard clipping is similar, but hard-clipped regions are not present in the sequence stored in the SAM field SEQ. A basic CIGAR string contains concatenated pairs of integer lengths and character operations (see Table 11-2 for a table of these operations).

Table 11-2. CIGAR operations

| Operation | Value | Description |
| --- | --- | --- |
| M | 0 | Alignment match (note that this could be a sequence match or mismatch!) |
| I | 1 | Insertion (to reference) |
| D | 2 | Deletion (from reference) |
| N | 3 | Skipped region (from reference) |
| S | 4 | Soft-clipped region (soft-clipped regions are present in sequence in SEQ field) |
| H | 5 | Hard-clipped region (not in sequence in SEQ field) |
| P | 6 | Padding (see section 3.1 of the SAM format specification for detail) |
| = | 7 | Sequence match |
| X | 8 | Sequence mismatch |

For example, a fully aligned 51 base pair read without insertions or deletions would have a CIGAR string containing a single length/operation pair: 51M. By the SAM format specification, M means there’s an alignment match, not that all bases in the query and reference sequence are identical (it’s a common mistake to assume this!).

![](images/page_393_image_2.jpg)

## Sequence Matches and Mismatches, and the NM and MD Tags

It’s important to remember that the SAM format specification simply lists what’s possible with the format. Along these lines, aligners choose how to output their results in this format, and there are differences among aligners in how they use the CIGAR string (and other parts of the SAM format). It’s common for many aligners to forgo using = and X to indicate sequence matches and mismatches, and instead just report these as M.

However, this isn’t as bad as it sounds—many aligners have differ ent goals (e.g., general read mapping, splicing-aware aligning, aligning longer reads to find chromosomal breakpoints). These tasks don’t require the same level of detail about the alignment, so in some cases explicitly reporting matches and mismatches with = and X would lead to needlessly complicated CIGAR strings.

Also, much of the information that = and X convey can be found in optional SAM tags that many aligners can include in their output. The NM tag is an integer that represents the edit distance between the aligned portion (which excludes clipped regions) and the reference. Additionally, the MD tag encodes mismatching positions from the reference (and the reference’s sequence at mismatching positions). See the SAM format specification for more detail. If your BAM file doesn’t have the NM and MD tags, samtools calmd can add them for you.

Let’s look at a trickier example: 43S6M1I26M. First, let’s break this down into pairs: 43S, 6M, 1I, and 26M. Using Table 11-2, we see this CIGAR string tells us that the first 43 bases were soft clipped, the next 6 were matches/mismatches, then a 1 base pair insertion to the reference, and finally, 26 matches. The SAM format specification mandates that all M, I, S, =, and X operations’ lengths must add to the length of the sequence. We can validate that’s the case here: 43 + 6 + 1 + 26 = 76, which is the length of the sequence in this SAM entry.

## Mapping Qualities

Our discussion of the SAM and BAM formats is not complete without mentioning mapping qualities (Li et al., 2008). Mapping qualities are one of the most important diagnostics in alignment. All steps downstream of alignment in all bioinformatics projects (e.g., SNP calling and genotyping, RNA-seq, etc.) critically depend on reliable mapping. Mapping qualities quantify mapping reliability by estimating how likely a read is to actually originate from the position the aligner has mapped it to. Similar to base quality, mapping quality is a log probability given by $Q = - 1 0 \log _ { 1 0 } P ( i n c o r r e c t$ mapping position). For example, a mapping quality of 20 translates to a $I O^{(20/-10)} = I \%$ chance the alignment is incorrect.

The idea of mapping quality is also related to the idea of mapping uniqueness. This is often defined as when a read’s second best hit has more mismatches than its first hit. However, this concept of uniqueness doesn’t account for the base qualities of mismatches, which carry a lot of information about whether a mismatch is due to a base calling error or a true variant (Li et al., 2008). Mapping quality estimates do account for base qualities of mismatches, which makes them a far better metric for measuring mapping uniqueness (as well as general mapping reliability).

We can use mapping qualities to filter out likely incorrect alignments (which we can do with samtools view, which we’ll learn about later), find regions where mapping quality is unusually low among most alignments (perhaps in repetitive or paralogous regions), or assess genome-wide mapping quality distributions (which could indicate alignment problems in highly repetitive or polyploid genomes).

## Command-Line Tools for Working with Alignments in the SAM Format

In this section, we’ll learn about the Samtools suite of tools for manipulating and working with SAM, BAM, and CRAM files. These tools are incredibly powerful, and becoming skilled in working with these tools will allow you to both quickly move forward in file-processing tasks and explore the data in alignment files. All commands are well documented both online (see [the Samtools website](http://www.htslib.org/doc/)) and in the programs themselves (run a program without arguments or use --help for more information).

## Using samtools view to Convert between SAM and BAM

Many samtools subcommands such as sort, index, depth, and mpileup all require input files (or streams) to be in BAM format for efficiency, so we often need to convert between plain-text SAM and binary BAM formats. samtools view allows us to convert SAM to BAM with the -b option:

\$ samtools view -b celegans.sam > celegans\_copy.bam

Similarly, we can go from BAM to SAM:

```txt
$ samtools view celegans.bam > celegans_copy.sam
$ head -n 3 celegans_copy.sam
I_2011868_2012306_0:0:0:0_0:0:0_2489    83    I   2012257    40 [...] 
I_2011868_2012306_0:0:0:0_0:0:0_2489    163    I   2011868    60 [...] 
I_13330604_13331055_2:0:0_0:0:0_3dd5   83    I   13331006    60 [...]
```

However, samtools view will not include the SAM header (see “The SAM Header” on page 356) by default. SAM files without headers cannot be turned back into BAM files:

```txt
\$ samtools view -b celegans_copy.sam > celegans_copy.bam
[E::sam_parse1] missing SAM header
[W::sam_read1] parse error at line 1
[main_samview] truncated file.
```

Converting BAM to SAM loses information when we don’t include the header. We can include the header with -h:

```txt
$ samtools view -h celegans.bam > celegans_copy.sam
$ samtools view -b celegans_copy.sam > celegans_copy.bam #now we can convert back
```

Usually we only need to convert BAM to SAM when manually inspecting files. In general, it’s better to store files in BAM format, as it’s more space efficient, compatible with all samtools subcommands, and faster to process (because tools can directly read in binary values rather than require parsing SAM strings).

## The CRAM Format

Samtools now supports (after version 1) a new, highly compressed file format known as CRAM (see Fritz et al., 2011). Compressing alignments with CRAM can lead to a 10%–30% filesize reduction compared to BAM (and quite remarkably, with no significant increase in compression or decompression time compared to BAM). CRAM is a reference-based compression scheme, meaning only the aligned sequence that’s different from the reference sequence is recorded. This greatly reduces file size, as many sequences may align with minimal difference from the reference. As a consequence of this reference-based approach, it’s imperative that the reference is available and does not change, as this would lead to a loss of data kept in the CRAM format. Because the reference is so important, CRAM files contain an MD5 checksum of the reference file to ensure it has not changed.

CRAM also has support for multiple different lossy compression methods. Lossy compression entails some information about an alignment and the original read is lost. For example, it’s possible to bin base quality scores using a lower resolution binning scheme to reduce the filesize. CRAM has other lossy compression models; see [CRAMTools](http://github.com/enasequence/cramtools) for more details.

Overall, working with CRAM files is not much different than working with SAM or BAM files; CRAM support is integrated into the latest Samtools versions. See [the documentation](http://bit.ly/cram-st) for more details on CRAM-based Samtools workflows.

## Samtools Sort and Index

In “Indexed FASTA Files” on page 352, we saw how we can index a FASTA file to allow for faster random access of the sequence at specific regions in a FASTA file. Similarly, we sort (by alignment position) and index a BAM file to allow for fast random access to reads aligned within a certain region (we’ll see how to extract these regions in the next section).

We sort alignments by their alignment position with samtools sort:

\$ samtools sort celegans\_unsorted.bam celegans\_sorted

Here, the second argument is the output filename prefix (samtools sort will append the .bam extension for you).

Sorting a large number of alignments can be very computationally intensive, so sam tools sort has options that allow you to increase the memory allocation and parallelize sorting across multiple threads. Very often, large BAM files won’t fit entirely in memory, so samtools sort will divide the file into chunks, sort each chunk and write to a temporary file on disk, and then merge the results together; in computer science lingo, samtools sort uses a merge sort (which was also discussed in “Sorting Plain-Text Data with Sort” on page 147). Increasing the amount of memory samtools sort can use decreases the number of chunks samtools sort needs to divide the file into (because larger chunks can fit in memory), which makes sorting faster. Because merge sort algorithms sort each chunk independently until the final merge step, this can be parallelized. We can use the samtools sort option -m to increase the memory, and -@ to specify how many threads to use. For example:

\$ samtools sort -m 4G -@ 2 celegans\_unsorted.bam celegans\_sorted

samtools sort’s -m option supports the suffixes K (kilobytes), M (megabytes), and G (gigabytes) to specify the units of memory. Also, note though that in this example, the toy data file celegans\_unsorted.bam is far too small for there to be any benefits in increasing the memory or parallelization.

Position-sorted BAM files are the starting point for most later processing steps such as SNP calling and extracting alignments from specific regions. Additionally, sorted BAM files are much more disk-space efficient than unsorted BAM files (and certainly more than plain-text SAM files). Most SAM/BAM processing tasks you’ll do in daily bioinformatics work will be to get you to this point.

Often, we want to work with alignments within a particular region in the genome. For example, we may want to extract these reads using samtools view or only call SNPs within this region using FreeBayes (Garrison et al., 2012) or samtools mpileup. Iterating through an entire BAM file just to work with a subset of reads at a position would be inefficient; consequently, BAM files can be indexed like we did in “Indexed FASTA Files” on page 352 with FASTA files. The BAM file must be sorted first, and we cannot index SAM files. To index a position-sorted BAM file, we simply use:

\$ samtools index celegans\_sorted.bam

This creates a file named celegans\_sorted.bam.bai, which contains the index for the celegans\_sorted.bam file.

## Extracting and Filtering Alignments with samtools view

Earlier, we saw how we can use samtools view to convert between SAM and BAM, but this is just scratching the surface of samtools view’s usefulness in working with alignment data. samtools view is a workhorse tool in extracting and filtering alignments in SAM and BAM files, and mastering it will provide you with important skills needed to explore alignments in these formats.

## Extracting alignments from a region with samtools view

With a position-sorted and indexed BAM file, we can extract specific regions of an alignment with samtools view. To make this example more interesting, let’s use a subset of the 1000 Genomes Project data (1000 Genomes Project Consortium, 2012) that’s included in this chapter’s repository on GitHub. First, let’s index it:

\$ samtools index NA12891\_CEU\_sample.bam

Then, let’s take a look at some alignments in the region chromosome 1, 215,906,469-215,906,652:

```txt
\$ samtools view NA12891_CEU_sample.bam 1:215906469-215906652 | head -n 3
SRR003212.5855757    147  1   215906433  60  33S43M = 215906402 [...] 
SRR003206.18432241  163  1   215906434  60  43M8S = 215906468 [...] 
SRR014595.5642583    16  1   215906435  37  8S43M * 0 [...]
```

We could also write these alignments in BAM format to disk with:

\$ samtools view -b NA12891\_CEU\_sample.bam 1:215906469-215906652 > USH2A\_sample\_alns.bam

Lastly, note that if you have many regions stored in the BED format, samtools view can extract regions from a BED file with the -L option:

```dockerfile
\$ samtools view -L USH2A_exons.bed NA12891_CEU_sample.bam | head -n 3
SRR003214.11652876 163 1 215796180 60 76M = 215796224 92 [...] 
SRR010927.6484300 163 1 215796188 60 51M = 215796213 76 [...] 
SRR005667.2049283 163 1 215796190 60 51M = 215796340 201 [...]
```

## Filtering alignments with samtools view

samtools view also has options for filtering alignments based on bitwise flags, mapping quality, read group. samtools view’s filtering features are extremely useful; very often we need to query BAM files for reads that match some criteria such as “all aligned proper-paired end reads with a mapping quality over 30.” Using samtools view, we can stream through and filter reads, and either pipe the results directly into another command or write them to a file.

First, note that samtools view (like other samtools subcommands) provides handy documentation within the program for all of its filtering options. You can see these any time by running the command without any arguments (to conserve space, I’ve included only a subset of the options):

\$ samtools view

```txt
Usage:  samtools view [options] <in.bam>|<in.sam>|<in.cram> [region ...]

Options: -b        output BAM
    -C        output CRAM (requires -T)
    -1        use fast BAM compression (implies -b)
    -u        uncompressed BAM output (implies -b)
    -h        include header in SAM output
    -H        print SAM header only (no alignments)
    -c        print only the count of matching records
[...]
```

Let’s first see how we can use samtools view to filter based on bitwise flags. There are two options related to this: -f, which only outputs reads with the specified flag(s), and -F, which only outputs reads without the specified flag(s). Let’s work through an example, using the samtools flags command to assist in figuring out the flags we need. Suppose you want to output all reads that are unmapped. UNMAP is a flag according to samtools flags:

```txt
\$ samtools flags unmap
0x4      4       UNMAP
```

Then, we use samtools view -f 4 to output reads with this flag set:

```txt
$ samtools view -f 4 NA12891_CEU_sample.bam | head -n 3
SRR003208.1496374    69   1   215623168 0  35M16S = 215623168 0  [...]
SRR002141.16953736   181   1   215623191 0  40M11S = 215623191 0  [...]
SRR002143.2512308   181   1   215623216 0 *     = 215623216 0  [...]
```

Note that each of these flags (the second column) have the bit corresponding to unmapped set. We could verify this with samtools flags:

```csv
\$ samtools flags 69
0x45    69    PAIRED,UNMAP,READ1
```

It’s also possible to output reads with multiple bitwise flags set. For example, we could find the first reads that aligned in a proper pair alignment. First, we use samtools flags to find out what the decimal representation of these two flags is:

```csv
\$ samtools flags READ1,PROPER_PAIR
0x42 66 PROPER_PAIR,READ1
```

Then, use samtools view’s -f option to extract these alignments:

```txt
$ samtools view -f 66 NA12891_CEU_sample.bam | head -n 3
SRR005672.8895       99  1   215622850  60  51M =  215623041  227    [...]
SRR005674.4317449   99  1   215622863  37  51M =  215622987  175    [...]
SRR010927.10846964  83  1   215622892  60  51M =  215622860 -83    [...]
```

We can use the -F option to extract alignments that do not have any of the bits set of the supplied flag argument. For example, suppose we wanted to extract all aligned reads. We do this by filtering out all reads with the 0x4 bit (meaning unmapped) set:

```txt
$ samtools flags UNMAP
0x4      4       UNMAP

$ samtools view -F 4 NA12891_CEU_sample.bam | head -n 3
SRR005672.8895     99   1  215622850  60  51M    =  215623041  227  [...] 
SRR010927.10846964  163   1  215622860  60  35M16S  =  215622892  83  [...] 
SRR005674.4317449   99   1  215622863  37  51M    =  215622987  175  [...]
```

Be aware that you will likely have to carefully combine bits to build queries that extract the information you want. For example, suppose you wanted to extract all reads that did not align in a proper pair. You might be tempted to approach this by filtering out all alignments that have the proper pair bit (0x2) set using:

```txt
$ samtools flags PROPER_PAIR
0x2      2       PROPER_PAIR
$ samtools view -F 2 NA12891_CEU_sample.bam | head -n 3
SRR005675.5348609   0  1  215622863  37  51M    [...]
SRR002133.11695147   0  1  215622876  37  48M    [...]
SRR002129.2750778   0  1  215622902  37  35M1S  [...]
```

But beware—this would be incorrect! Both unmapped reads and unpaired reads will also be included in this output. Neither unmapped reads, nor unpaired reads will be in a proper pair and have this bit set.