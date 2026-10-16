④ After resetting the position, calling the AlignmentFile.next() method returns the first alignment. Note that the query name, given by the attribute AlignedSeg ment.qname, is the same as the first alignment in Example 11-2.

Once you’re done working with an open SAM/BAM file, it’s a good idea to close it, which can be done with:

```txt
>>> bamfile.close()
```

Note, though, that all examples in this section will assume that bamfile is open (so if you’ve just executed the preceding line, reopen the file).

## Extracting SAM/BAM Header Information from an AlignmentFile Object

AlignmentFile objects also contain all information in the SAM header, which can be accessed using a variety of the AlignmentFile’s attributes and methods. The entire header is kept in a Python dictionary, which has the same possible keys as a SAM header:

```txt
>>> bamfile.header.keys()
['SQ', 'RG', 'PG', 'HD']
```

Each of the values corresponding to these keys contains a list of SAM header records. For example, the first record in the read group (RG) section and the third record in the sequence (SQ) section are:

```python
>>> bamfile.header['RG'][0]
{'LB': 'g1k-sc-NA12891-CEU-1', 'CN': 'SC', 'DS': 'SRP000032',
'SM': 'NA12891', 'PI': '200', 'ID': 'ERR001776', 'PL': 'ILLUMINA'}
>>> bamfile.header['SQ'][0]
{'LN': 249250621, 'M5': '1b22b98cdeb4a9304cb5d48026a85128',
'AS': 'NCBI37', 'SN': '1',
'UR': 'file:/lustre/scratch102/projects/g1k/ref/main_project/
human_g1k_v37.fasta'}
```

While the AlignmentFile.header dictionary contains all information in the header, there are higher-level and easier ways to access header information. For example, the reference sequence names and their lengths are stored in two tuples, Alignment File.references and AlignmentFile.lengths:

```txt
>>> bamfile.references
('1', '2', '3', '4', '5', '6', '7', [...])
>>> bamfile.lengths
(249250621, 243199373, 198022430, 191154276,
 180915260, 171115067, 159138663, [...])
```

When working with Pysam, one of the most common AlignmentFile methods you’ll use is AlignmentFile.getrname(). Whenever you process an AlignedSegment object, the reference is stored as a non-negative integer reference ID (also known as a target ID or tid in the documentation). The reference ID corresponds to a particular reference sequence. The AlignmentFile.getrname() method is used to retrieve the name of the reference corresponding to this this integer reference ID:

```txt
>>> # check if aligned (only aligned reads have meaningful reference)
>>> read.is_unmapped
False
>>> read.tid
0
>>> bamfile.getrname(read.reference_id)
'1'
```

It’s also possible to go the opposite direction, from name to reference ID:

```txt
>>> bamfile.gettid('MT')
24
```

Reference IDs can only be non-negative integers; a value of –1 indicates something is wrong (and your code should explicitly test for this possibility!). For example, if we attempted to access a reference named “Mt” by mistake:

```txt
>>> bamfile.gettid('Mt')
-1
```

There are numerous other useful AlignmentFile attributes we don’t have the space to cover here; see the Pysam documentation for a full list.

## Working with AlignedSegment Objects

Most SAM/BAM processing tasks you’ll tackle with Pysam will involve heavy work with AlignedSegment objects. These objects contain information about individual alignment records, which is what most SAM/BAM processing is centered around. All information about an alignment record is stored in this AlignedSegment object’s attributes. We’ll explore some of these attributes by taking a closer look at one AlignedSegment object from the NA12891\_CEU\_sample.bam file in this section. But note, the best and most up-to-date information will always come from the API documentation itself. This section quickly steps through the basics and highlights a few parts that can be tricky for those just starting out with Pysam.

First, let’s load a sample read from this file:

```txt
>>> bamfile = pysam.AlignmentFile(filename=fname, mode="rb")
>>> read = bamfile.next()
```

Basic information about the read (also known as the query), including its name, sequence, base qualities, and length are all stored as attributes:

```txt
>>> read.query_name ①
'SRR005672.8895'
>>> read.reference_start ②
```

```python
215622849
>>> read.query_sequence ③
'GGAATAAATATAGGAAATGTATAATATATAGGAAATATATATATATAGTAA'
>>> read.query_qualities ④
array('B', [26, 28, 27, 29, 28, 27, 29, 27, 24, 27, [...]])
>>> read.query_length ⑤
51
>>> read.query_length == len(read.query_sequence)
True
```

The AlignedSegment.query\_name attribute returns the read (query) name.
The AlignedSegment.reference\_start attribute returns the alignment position (the column POS in the SAM/BAM file).
AlignedSegment.query\_sequence retrieves the read sequence.
④ AlignedSegment.query\_qualities retrieves the read qualities, as a Python array. These qualities have already been converted; there’s no need to subtract 33 from these values.
The length of the query be accessed with AlignedSegment.query\_length. This gives the entire query length, which as you see on the next line will be equal to the length of the sequence.

Earlier, in “Bitwise Flags” on page 360, we learned how to extract information from the SAM format’s bitwise flags. Pysam makes this much simpler by providing a series of clearly named attributes that get at the values of these bitwise flags. The following are some examples, but see the Pysam documentation for a full list:

```txt
>>> read.is_unmapped
False
>>> read.is_paired
True
>>> read.is_proper_pair
True
>>> read.mate_is_unmapped
False
>>> read.is_read1
True
>>> read.is_read2
False
>>> read.is_reverse
False
>>> read.mate_is_reverse
True
>>> read.is_qcfail
False
```

There are two attributes to access an alignment’s CIGAR alignment details: Aligned Segment.cigartuples and AlignedSegment.cigarstring. The former returns a list of tuples that use integers to encode the CIGAR operation and its length (see the documentation for these operation codes). The latter returns the CIGAR alignment as a string.

One important consideration when working with Pysam’s AlignedSegment objects is how certain values handle soft-clipped alignments. With soft clipping, it’s possible that the length of the aligned query sequence is less than the original read sequence. Because we often want to work with only the aligned portion of query sequences when processing alignments, AlignedSegment has attributes that take soft clipping into account—be sure to use the correct attribute for your task! For example, let’s find a soft-clipped read by iterating over all reads until we find one with “S” in the CIGAR string, then break out of the loop:

```python
>>> bamfile = pysam.AlignmentFile('NA12891_CEU_sample.bam')
>>> for read in bamfile:
...     if 'S' in read.cigarstring:
...         break
...
>>> read.cigarstring
'35M16S'
```

AlignedSegment objects have some attributes with “alignment” in the name to emphasize these exclude soft-clipped bases. For example, note the difference between AlignedSegment.query\_sequence and AlignedSegment.query\_align ment\_sequence:

```txt
>>> read.query_sequence
'TAGGAAATGTATAATATATAGGAAATATATATATATAGGAAATATATAATA'
>>> read.query_alignment_sequence
'TAGGAAATGTATAATATATAGGAAATATATATATA'
>>> len(read.query_sequence) - len(read.query_alignment_sequence)
16
```

The difference between these two strings is the soft-clipped bases; AlignedSeg ment.query\_alignment\_sequence doesn’t include these soft-clipped bases and is 16 bases shorter. There are similar attributes, including AlignedSegment.query\_align ment\_start and AlignedSegment.query\_alignment\_end (which give the start and end indices in the aligned portion of the query sequence), AlignedSeg ment.query\_alignment\_length (which returns the alignment length), and Aligned Segment.query\_alignment\_qualities (which returns the sequence base qualities, excluding the soft-clipped bases).

## Writing a Program to Record Alignment Statistics

We’re now ready to employ our knowledge of AlignedSegment objects to write a simple short program that gathers alignment statistics from a SAM or BAM file. We’ll then validate this tool by comparing its results to those from samtools flagstat, a tool that reports statistics about SAM bitwise flags:

```python
import sys
import pysam
from collections import Counter

if len(sys.argv) < 2:
    sys.exit("usage: alnstat.py in.bam")

fname = sys.argv[1]
bamfile = pysam.AlignmentFile(fname) ①

stats = Counter() ②
for read in bamfile:
    stats['total'] += 1
    stats['qcfail'] += int(read.is_qcfail) ③

    # record paired end info
    stats['paired'] += int(read.is_paired) ④
    stats['read1'] += int(read.is_read1)
    stats['read2'] += int(read.is_read2)

    if read.is_unmapped: ⑤
        stats['unmapped'] += 1
        continue # other flags don't apply

    # record if mapping quality <= 30 ⑥
    stats["mapping quality <= 30"] += int(read.mapping_quality <= 30)

    stats['mapped'] += 1 ⑦
    stats['proper pair'] += int(read.is_proper_pair) ⑧

# specify the output order, since dicts don't have order ⑨
output_order = ("total", "mapped", "unmapped", "paired",
               "read1", "read2", "proper pair", "qcfail",
               "mapping quality <= 30")

# format output and print to standard out
for key in output_order:
    format_args = (key, stats[key], 100*stats[key]/float(stats["total"]))
    sys.stdout.write("%s: %d (%0.2f%)\n" % format_args) ⑪
```

This is a quick script, without many bells and whistles. In general, when writing scripts for simple tasks like this, it’s best to follow the KISS principle. Don’t needlessly overcomplicate things or add extra features—these can all come in later revisions after daily use has shown an inadequacy. Let’s step through some key parts:

After loading the necessary modules and checking there are a sufficient number of arguments to run the script, we open the SAM or BAM file. Here, we don’t explicitly specify a mode, because Pysam’s AlignmentFile can infer this (see the AlignmentFile documentation for more information).
Here, we initiate the Counter object from the collections module (Counter is an incredibly useful class in bioinformatics scripts!). Counter behaves much like a Python dictionary, which is how we see it used here.
3 Here’s an example of incrementing a key in the Counter object depending on what the value of an AlignedSegment attribute is. The attribute AlignedSeg ment.is\_qcfail returns whether the QC fail bit is set, which is a Boolean value (True or False). To be explicit, we convert this to an integer, and add this value (either 1 for True or 0 for False) to the current count kept in the Counter object stats.
Similar to how we increment the key for QC fail, we increment the counters for whether a read is paired, is read 1, or is read 2.
5 Some flags only make sense if a read mapped to the reference. At this point, we check if the read is unmapped, and increment the unmapped counter if so. Since the rest of the values we check in the for loop block depend on a read being aligned, if a read is unmapped we use continue to skip over this code (because none of these later keys should be incremented if a read is unmapped).
At this point, all alignments are mapped. We increment a counter here recording whether the read mapped with mapping quality is less than 30 (any threshold can be used, but this is a common threshold for “low quality” alignments).
Here we increment the 'mapped' key, since all alignments at this point are mapped. We also increment if the read is in a proper pair (only aligned reads can be a proper pair).
Counter objects are based on Python’s dictionaries, so keys are not in any particular order. Here, we define the order to output keys (and their values) as a tuple. We’ll see how this is used in the next step.
In this loop, we iterate over each of the keys in the tuple output\_order, which defines the order of output values in the Counter object stats. Each line of output has three values: the key name, the total counts for that key in the Counter object stats, and that key’s percentage of the total number of SAM/BAM entries.

This line creates a tuple of these values, which are used to propagate the string formatting values in the next line.

This line writes a formatted string (using the tuple format\_args created in the previous line) to standard output.

Let’s run this script on our NA12891\_CEU\_sample.bam file:

```txt
$ python alnstat/alnstat.py NA12891_CEU_sample.bam
total: 636207 (100.00%)
mapped: 630875 (99.16%)
unmapped: 5332 (0.84%)
paired: 435106 (68.39%)
read1: 217619 (34.21%)
read2: 217487 (34.18%)
proper pair: 397247 (62.44%)
qcfail: 0 (0.00%)
mapping quality <= 30: 90982 (14.30%)
```

Even for simple scripts such as this one, it’s essential to validate the results. For longer scripts, frequently used programs, or critical parts of a workflow, we might employ unit testing (because if something’s wrong, everything will be wrong). Unit testing involves breaking code up into separate functions, and writing code that automatically tests that each function is working by checking its values (called unit tests). For a small script like this, this might be overkill. Fortunately, there are two simpler (but less robust) alternatives:

• Creating a small test dataset where you’ve worked out what the results should be by hand and can check your program’s results
• Using another program or application to validate the results

We’ll use the latter option, by validating our tool with samtools flagstat (which our program emulates):

```txt
$ samtools flagstat NA12891_CEU_sample.bam
636207 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
0 + 0 supplementary
29826 + 0 duplicates
630875 + 0 mapped (99.16%:nan%)
435106 + 0 paired in sequencing
217619 + 0 read1
217487 + 0 read2
397247 + 0 properly paired (91.30%:nan%)
424442 + 0 with itself and mate mapped
5332 + 0 singletons (1.23%:nan%)
5383 + 0 with mate mapped to a different chr
2190 + 0 with mate mapped to a different chr (mapQ>=5)
```

Looking at the raw counts (in the first column, before +) we can see that each our values check out. samtools flagstat doesn’t return a figure for how many reads have a mapping quality less than or equal to 30, so we have to validate our value another way. One way is to use samtools view’s -q option, which returns the number of alignments with a mapping quality greater than or equal to the supplied value. We combine this with -c, which returns the count, rather than the alignments themselves:

```batch
\$ samtools view -c -q 31 NA12891_CEU_sample.bam
539893
```

Now, to find the number of reads with mapping quality less than or equal to 30, we need to subtract this value from the total number of mapped reads. We count the total number of mapped reads with samtools flagstat, filtering out alignments with the unmapped bit (0x4) set:

```batch
samtools view -c -F 4 NA12891_CEU_sample.bam
630875
```

Note that 630,875 – 539,893 = 90,982, which is exactly what we found with our alnstat.py script—this value checks out, too.

## Additional Pysam Features and Other SAM/BAM APIs

In this introduction, we’ve skipped over some additional features of Pysam. For example, Pysam also includes an interface for creating and working with pileup data, through the AlignmentFile.pileup() method. In addition, Pysam implements some common samtools subcommands—for example, sort, view, and calmd are implemented as pysam.sort, pysam.view, pysam.calmd. Pysam also has a Python interface to Tabix files through pysam.TabixFile (we cover Tabix files later in “Fast Access to Indexed Tab-Delimited Files with BGZF and Tabix” on page 425), and FASTQ files through pysam.FastqFile. These are all well-written and easy-to-use interfaces; unfortunately, we don’t have the space to cover all of these in this section, so see Pysam’s excellent documentation for more details.

Finally, Pysam is just one popular SAM/BAM API—there are numerous others available in different languages. For example, Samtools has [its own C API](http://bit.ly/st-capi). If you work in Java, [Picard](http://broadinstitute.github.io/picard/) offers a Java API for working with SAM and BAM files. Finally, Bioconductor has two excellent packages used for working with SAM and BAM files and genome alignments: [Rsamtools](http://bit.ly/rsamtools) and [GenomicAlignment](http://bit.ly/genom-align).

# Bioinformatics Shell Scripting, Writing Pipelines, and Parallelizing Tasks

I’ve waited until the penultimate chapter this book to share a regrettable fact: everyday bioinformatics work often involves a great deal of tedious data processing. Bioinformaticians regularly need to run a sequence of commands on not just one file, but dozens (sometimes even hundreds) of files. Consequently, a large part of bioinformatics is patching together various processing steps into a pipeline, and then repeatedly applying this pipeline to many files. This isn’t exciting scientific work, but it’s a necessary hurdle before tackling more exciting analyses.

While writing pipelines is a daily burden of bioinformaticians, it’s essential that pipelines are written to be robust and reproducible. Pipelines must be robust to problems that might occur during data processing. When we execute a series of commands on data directly into the shell, we usually clearly see if something goes awry—output files are empty when they should contain data or programs exit with an error. However, when we run data through a processing pipeline, we sacrifice the careful attention we paid to each step’s output to gain the ability to automate processing of numerous files. The catch is that not only are errors likely to still occur, they’re more likely to occur because we’re automating processing over more data files and using more steps. For these reasons, it’s critical to construct robust pipelines.

Similarly, pipelines also play an important role in reproducibility. A well-crafted pipeline can be a perfect record of exactly how data was processed. In the best cases, an individual could download your processing scripts and data, and easily replicate your exact steps. However, it’s unfortunately quite easy to write obfuscated or sloppy pipelines that hinder reproducibility. We’ll see some principles that can help you avoid these mistakes, leading to more reproducible projects.

In this chapter, we’ll learn the essential tools and skills to construct robust and reproducible pipelines. We’ll see how to write rerunnable Bash shell scripts, automate file processing tasks with find and xargs, run pipelines in parallel, and see a simple makefile. Note that the subset of techniques covered in this chapter do not target a specific cluster or high-performance computing (HPC) architecture—these are general Unix solutions that work well on any machine. For parallelization techniques specific to your HPC system, you will need consult its documentation.

## Basic Bash Scripting

We’ve found that duct tape is not a perfect solution for anything. But with a little ingenuity, in a pinch, it’s an adequate solution for just about everything.

— Mythbusters’ Jamie Hyneman

Bash, the shell we’ve used interactively throughout the book, is also a full-fledged scripting language. Like many other tools presented in this book, the trick to using Bash scripts effectively in bioinformatics is knowing when to use them and when not to. Unlike Python, Bash is not a general-purpose language. Bash is explicitly designed to make running and interfacing command-line programs as simple as possible (a good characteristic of a shell!). For these reasons, Bash often takes the role as the duct tape language of bioinformatics (also referred to as a glue language), as it’s used to tape many commands together into a cohesive workflow.

Before digging into how to create pipelines in Bash, it’s important to note that Python may be a more suitable language for commonly reused or advanced pipelines. Python is a more modern, fully featured scripting language than Bash. Compared to Python, Bash lacks several nice features useful for data-processing scripts: better numeric type support, useful data structures, better string processing, refined option parsing, availability of a large number of libraries, and powerful functions that help with structuring your programs. However, there’s more overhead when calling command-line programs from a Python script (known as calling out or shelling out) compared to Bash. Although Bash lacks some of Python’s features, Bash is often the best and quickest “duct tape” solution (which we often need in bioinformatics).

## Writing and Running Robust Bash Scripts

Most Bash scripts in bioinformatics are simply commands organized into a rerunnable script with some added bells and whistles to check that files exist and ensuring any error causes the script to abort. These types of Bash scripts are quite simple to write: you’ve already learned important shell features like pipes, redirects, and background processes that play an important role in Bash scripts. In this section, we’ll cover the basics of writing and executing Bash scripts, paying particular attention to how create robust Bash scripts.

## A robust Bash header

By convention, Bash scripts have the extension .sh. You can create them in your favorite text editor (and decent text editors will have support for Bash script syntax highlighting). Anytime you write a Bash script, you should use the following Bash script header, which sets some Bash options that lead to more robust scripts (there’s also a copy of this header in the template.sh file in this chapter’s directory on GitHub):

```shell
#!/bin/bash ①
set -e ②
set -u ③
set -o pipefail ④
```

1 This is called the shebang, and it indicates the path to the interpreter used to execute this script. This is only necessary when running the script as a program (more on this in a bit). Regardless of how you plan to run your Bash script, it’s best to include a shebang line.
By default, a shell script containing a command that fails (exits with a nonzero exit status) will not cause the entire shell script to exit—the shell script will just continue on to the next line. This is not a desirable behavior; we always want errors to be loud and noticeable. set -e prevents this, by terminating the script if any command exited with a nonzero exit status. Note, however, that set -e has complex rules to accommodate cases when a nonzero exit status indicates “false” rather than failure. For example, test -d file.txt will return a nonzero exit status if its argument is not a directory, but in this context this isn’t meant to represent an error. set -e ignores nonzero statuses in if conditionals for this reason (we’ll discuss this later). Also, set -e ignores all exit statuses in Unix pipes except the last one—this relates to set -o pipefail, which we discuss later.

3 set -u fixes another unfortunate default behavior of Bash scripts: any command containing a reference to an unset variable name will still run. As a horrifying example of what this can lead to, consider: rm -rf \$TEMP\_DIR/\*. If the shell variable \$TEMP\_DIR isn’t set, Bash will still substitute its value (which is nothing) in place of it. The end result is rm -rf /\*! You can see this for yourself:

```shell
$ echo "rm $NOTSET/blah"
rm /blah
```

set -u prevents this type of error by aborting the script if a variable’s value is unset.

As just discussed, set -e will cause a script to abort if a nonzero exit status is encountered, with some exceptions. One such exception is if a program run in a Unix pipe exited unsuccessfully; unless this program was the last program in the pipe, this would not cause the script to abort even with set -e. Including set -o pipefail will prevent this undesirable behavior—any program that returns a nonzero exit status in the pipe will cause the entire pipe to return a nonzero status. With set -e enabled, too, this will lead the script to abort.

![](images/page_427_image_1.jpg)

## The Robust Bash Header in Bash Script Examples in this Chapter

I will omit this header in Bash scripts throughout this chapter for clarity and to save space, but you should always use it in your own work.

These three options are the first layer of protection against Bash scripts with silent errors and unsafe behavior. Unfortunately, Bash is a fragile language, and we need to mind a few other oddities to use it safely in bioinformatics. We’ll see these as we learn more about the language.

## Running Bash scripts

Running Bash scripts can be done one of two ways: with the bash program directly (e.g., bash script.sh), or calling your script as a program (./script.sh). For our purposes, there’s no technical reason to prefer one approach over the other. Practically, it’s wise to get in the habit of running scripts you receive with ./script.sh, as they might use interpreters other than /bin/bash (e.g., zsh, csh, etc.). But while we can run any script (as long as it has read permissions) with bash script.sh, calling the script as an executable requires that it have executable permissions. We can set these using:

\$ chmod u+x script.sh

This adds executable permissions (+x) for the user who owns the file (u). Then, the script can be run with ./script.sh.

## Variables and Command Arguments

Bash variables play an extremely important role in robust, reproducible Bash scripts. Processing pipelines having numerous settings that should be stored in variables (e.g., which directories to store results in, parameter values for commands, input files, etc.). Storing these settings in a variable defined at the top of the file makes adjusting settings and rerunning your pipelines much easier. Rather than having to change numerous hardcoded values in your scripts, using variables to store settings means you only have to change one value—the value you’ve assigned to the variable. Bash also reads command-line arguments into variables, so you’ll need to be familiar with accessing variables’ values to work with command-line arguments.

Unlike other programming languages, Bash’s variables don’t have data types. It’s helpful to think of Bash’s variables as strings (but that may behave differently depending on context). We can create a variable and assign it a value with (note that spaces matter when setting Bash variables—do not use spaces around the equals sign!):

```txt
results_dir="results/"
```

To access a variable’s value, we use a dollar sign in front of the variable’s name (e.g., \$results\_dir). You can experiment with this in a Bash script, or directly on the command line:

```shell
$ results_dir="results/"
$ echo $results_dir
results/
```

As mentioned in the previous section, you should always set set -u to force a Bash script to exit if a variable is not set.

Even though accessing a variable’s value using the dollar sign syntax works, it has one disadvantage: in some cases it’s not clear where a variable name ends and where an adjacent string begins. For example, suppose a section of your Bash script created a directory for a sample’s alignment data, called &lt;sample&gt;\_aln/, where &lt;sample&gt; is replaced by the sample’s name. This would look like:

```txt
sample="CNTRL01A"
mkdir $sample_aln/
```

Although the intention of this code block was to create a directory called CNTRL01A\_aln/, this would actually fail, because Bash will try to retrieve the value of a variable named \$sample\_aln. To prevent this, wrap the variable name in braces:

```txt
sample="CNTRL01A"
mkdir \${sample}_aln/
```

Now, a directory named CNTRL01A\_aln/ will be created. While this solves our immediate problem of Bash interpreting sample\_aln as the variable name, there’s one more step we should take to make this more robust: quoting variables. This prevents commands from interpreting any spaces or other special characters that the variable may contain. Our final command would look as follows:

```hcl
sample="CNTRL01A"
mkdir "\${sample}_aln/"
```

## Command-line arguments

Let’s now look at how Bash handles command-line arguments (which are assigned to the value \$1, \$2, \$3, etc.). The variable \$0 stores the name of the script. We can see this ourselves with a simple example script:

```shell
#!/bin/bash
```

```shell
echo "script name: $0"
echo "first arg: $1"
echo "second arg: $2"
echo "third arg: $3"
```

Running this file prints arguments assigned to \$0, \$1, \$2, and \$3:

```yaml
\$ bash args.sh arg1 arg2 arg3
script name: args.sh
first arg: arg1
second arg: arg2
third arg: arg3
```

Bash assigns the number of command-line arguments to the variable \$# (this does not count the script name, \$0, as an argument). This is useful for user-friendly messages (this uses a Bash if conditional, which we’ll cover in more depth in the next section):

```shell
#!/bin/bash

if [ "\$#" -lt 3 ] # are there less than 3 arguments?
then
    echo "error: too few arguments, you provided \$#, 3 required"
    echo "usage: script.sh arg1 arg2 arg3"
    exit 1
fi

echo "script name: \$0"
echo "first arg: \$1"
echo "second arg: \$2"
echo "third arg: \$3"
```

Running this with too few arguments gives an error (and leads the process to exit with a nonzero exit status—see “Exit Status: How to Programmatically Tell Whether Your Command Worked” on page 52 if you’re rusty on what exit statuses mean):

```asm
$ ./script.sh some_arg
error: too few arguments, you provided 1, 3 required
usage: script.sh arg1 arg2 arg3
```

It’s possible to have more complex options and argument parsing with the Unix tool getopt. This is out of the scope of this book, but the manual entry for getopt is quite thorough. However, if you find your script requires numerous or complicated options, it might be easier to use Python instead of Bash. Python’s argparse module is much easier to use than getopt.

![](images/page_430_image_0.jpg)

## Reproducibility and Environmental Variables

Some bioinformaticians make use of environmental variables to store settings using the command export, but in general this makes scripts less portable and reproducible. Instead, all important settings should be stored inside the script as variables, rather than as external environmental variables. This way, the script is self-contained and reproducible.

Variables created in your Bash script will only be available for the duration of the Bash process running that script. For example, running a script that creates a variable with some\_var=3 will not create some\_var in your current shell, as the script runs in an entirely separate shell process.

## Conditionals in a Bash Script: if Statements

Like other scripting languages, Bash supports the standard if conditional statement. What makes Bash a bit unique is that a command’s exit status provides the true and false (remember: contrary to other languages, 0 represents true/success and anything else is false/failure). The basic syntax is:

```txt
if [commands] ①
then
    [if-statements] ②
else
    [else-statements] ③
fi
```

1 [commands] is a placeholder for any command, set of commands, pipeline, or test condition (which we’ll see later). If the exit status of these commands is 0, execution continues to the block after then; otherwise execution continues to the block after else. The then keyword can be placed on the same line as if, but then a semicolon is required: if [commands]; then.
[if-statements] is a placeholder for all statements executed if [commands] evaluates to true (0).
[else-statements] is a placeholder for all statements executed if [commands] evaluates to false (1). The else block is optional.

Bash’s if condition statements may seem a bit odd compared to languages like Python, but remember: Bash is primarily designed to stitch together other commands. This is an advantage Bash has over Python when writing pipelines: Bash allows your scripts to directly work with command-line programs without requiring any overhead to call programs. Although it can be unpleasant to write complicated programs in Bash, writing simple programs is exceedingly easy because Unix tools and Bash harmonize well. For example, suppose we wanted to run a set of commands only if a file contains a certain string. Because grep returns 0 only if it matches a pattern in a file and 1 otherwise, we could use:

```shell
#!/bin/bash

if grep "pattern" some_file.txt > /dev/null ①
then
    # commands to run if "pattern" is found
    echo "found 'pattern' in 'some_file.txt"
fi
```

This grep command is our condition statement. The redirection is to tidy the output of this script such that grep’s output is redirected to /dev/null and not to the script’s standard out.

The set of commands in an if condition can use all features of Unix we’ve mastered so far. For example, chaining commands with logical operators like && (logical AND) and || (logical OR):

```shell
#!/bin/bash

if grep "pattern" file_1.txt > /dev/null &&
    grep "pattern" file_2.txt > /dev/null
then
    echo "found 'pattern' in 'file_1.txt' and in 'file_2.txt'"
fi
```

We can also negate our program’s exit status with !:

```shell
#!/bin/bash

if ! grep "pattern" some_file.txt > /dev/null
then
  echo "did not find 'pattern' in 'some_file.txt"
fi
```

Finally, it’s possible to use pipelines in if condition statements. Note, however, that the behavior depends on set -o pipefail. If pipefail is set, any nonzero exit status in a pipe in your condition statement will cause execution to continue on, skipping the if-statements section (and going on to the else block if it exists). However, if pipefail is not set, only the exit status of the last command is considered. Rather than trying to remember all of these rules, just use the robust header provided earlier —pipefail is a more sensible default.

The final component necessary to understand Bash’s if statements is the test command. Like other programs, test exits with either 0 or 1. However test’s exit status indicates the return value of the test specified through its arguments, rather than exit success or error. test supports numerous standard comparison operators (whether