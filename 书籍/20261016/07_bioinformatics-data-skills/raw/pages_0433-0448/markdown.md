two strings are equal, whether two integers are equal, whether one integer is greater than or equal to another, etc.). Bash can’t rely on familiar syntax such as > for “greater than,” as this is used for redirection: instead, test has its own syntax (see Table 12-1 for a full list). You can get a sense of how test works by playing with it directly on the command line (using ; echo "\$?" to print the exit status):

```shell
$ test "ATG" = "ATG" ; echo "\$?"
0
$ test "ATG" = "atg" ; echo "\$?"
1
$ test 3 -lt 1 ; echo "\$?"
1
$ test 3 -le 3 ; echo "\$?"
0
```

Table 12-1. String and integer comparison operators

| String/integer | Description |
| --- | --- |
| -z str | String str is null (empty) |
| str1 = str2 | Strings str1 and str2 are identical |
| str1 != str2 | Strings str1 and str2 are different |
| int1 -eq int2 | Integers int1 and int2 are equal |
| int1 -ne int2 | Integers int1 and int2 are not equal |
| int1 -lt int2 | Integer int1 is less than int2 |
| int1 -gt int2 | Integer int1 is greater than int2 |
| int1 -le int2 | Integer int1 is less than or equal to int2 |
| int1 -ge int2 | Integer int1 is greater than or equal to int2 |

In practice, the most common conditions you’ll be checking aren’t whether some integer is less than another, but rather checking to see if files or directories exist and whether you can write to them. test supports numerous file- and directory-related test operations (the few that are most useful in bioinformatics are in Table 12-2). Let’s look at a few basic command-line examples:

```shell
$ test -d some_directory ; echo $? # is this a directory?
0
$ test -f some_file.txt ; echo $? # is this a file?
0
$ test -r some_file.txt ; echo $? $ is this file readable?
```

```tcl
$ test -w some_file.txt ; echo $? $ is this file writable?
1
```

Table 12-2. File and directory test expressions

| File/directory expression | Description |
| --- | --- |
| -d dir | dir is a directory |
| -f file | file is a file |
| -e file | file exists |
| -h link | link is a link |
| -r file | file is readable |
| -w file | file is writable |
| -x file | file is executable (or accessible if argument is expression) |

Combining test with if statements is simple; test is a command, so we could use:

```shell
if test -f some_file.txt
then
  [...] 
fi
```

However, Bash provides a simpler syntactic alternative to test statements: [ -f some\_file.txt ] . Note the spaces around and within the brackets—these are required. This makes for much simpler if statements involving comparisons:

```shell
if [ -f some_file.txt ]
then
  [...] 
fi
```

When using this syntax, we can chain test expressions with -a as logical AND, -o as logical OR, ! as negation, and parentheses to group statements. Our familiar && and || operators won’t work in test, because these are shell operators. As an example, suppose we want to ensure our script has enough arguments and that the input file is readable:

```shell
#!/bin/bash
set -e
set -u
set -o pipefail

if [ "$#" -ne 1 -o ! -r "$1" ]
```

```shell
then
    echo "usage: script.sh file_in.txt"
    exit 1
fi
```

As discussed earlier, we quote variables (especially those from human input); this is a good practice and prevents issues with special characters.

When chained together with -a or -e, test’s syntax uses short-circuit evaluation. This means that test will only evaluate as many expressions as needed to determine whether the entire statement is true or false. In this example, test won’t check if the file argument \$1 is readable if there’s not exactly one argument provided (the first condition is true). These two expressions are combined with a logical OR, which only requires one expression to be true for the entire condition to be true.

## Processing Files with Bash Using for Loops and Globbing

In bioinformatics, most of our data is split across multiple files (e.g., different treatments, replicates, genotypes, species, etc.). At the heart of any processing pipeline is some way to apply the same workflow to each of these files, taking care to keep track of sample names. Looping over files with Bash’s for loop is the simplest way to accomplish this. This is such an important part of bioinformatics processing pipelines that we’ll cover additional useful tools and methods in the next section of this chapter.

There are three essential parts to creating a pipeline to process a set of files:

• Selecting which files to apply the commands to
• Looping over the data and applying the commands
• Keeping track of the names of any output files created

There are different computational tricks to achieve each of these tasks. Let’s first look at the simple ways to select which files to apply commands to.

There are two common ways to select which files to apply a bioinformatics workflow to: approaches that start with a text file containing information about samples (their sample names, file path, etc.), and approaches that select files in directories using some criteria. Either approach is fine—it mostly comes down to what’s most efficient for a given task. We’ll first look at an approach that starts with sample names and return to how to look for files later. Suppose you have a file called samples.txt that tells you basic information about your raw data: sample name, read pair, and where the file is. Here’s an example (which is also in this chapter’s directory on GitHub):

```txt
$ cat samples.txt
zmaysA R1 seq/zmaysA_R1.fastq
zmaysA R2 seq/zmaysA_R2.fastq
```

```txt
zmaysB R1 seq/zmaysB_R1.fastq
zmaysB R2 seq/zmaysB_R2.fastq
zmaysC R1 seq/zmaysC_R1.fastq
zmaysC R2 seq/zmaysC_R2.fastq
```

The first column gives sample names, the second column contains read pairs, and the last column contains the path to the FASTQ file for this sample/read pair combination. The first two columns are called metadata (data about data), which is vital to relating sample information to their physical files. Note that the metadata is also in the filename itself, which is useful because it allows us to extract it from the filename if we need to.

With this samples.txt file, the first step of creating the pipeline is complete: all information about our files to be processed, including their path, is available. The second and third steps are to loop over this data, and do so in a way that keeps the samples straight. How we accomplish this depends on the specific task. If your command takes a single file and returns a single file, the solution is trivial: files are the unit we are processing. We simply loop over each file and use a modified version of that file’s name for the output.

Let’s look at an example: suppose that we want to loop over every file, gather quality statistics on each and every file (using the imaginary program fastq\_stat), and save this information to an output file. Each output file should have a name based on the input file, so if a summary file indicates something is wrong we know which file was affected. There’s a lot of little parts to this, so we’re going to step through how to do this a piece at a time learning about Bash arrays, basename, and a few other shell tricks along the way.

First, we load our filenames into a Bash array, which we can then loop over. Bash arrays can be created manually using:

```txt
\$ sample_names=(zmaysA zmaysB zmaysC)
```

And specific elements can be extracted with (note Bash arrays are 0-indexed):

```shell
$ echo ${sample_names[0]}
zmaysA
$ echo ${sample_names[2]}
zmaysC
```

All elements are extracted with the cryptic-looking \${sample\_files[@]}:

```txt
$ echo ${sample_names[@]}
zmaysA zmaysB zmaysC
```

You can also access how many elements are in the array (and each element’s index) with the following:

```txt
$ echo ${#sample_names[@]}
3
```

```shell
$ echo ${!sample_names[@]}
0 1 2
```

But creating Bash arrays by hand is tedious and error prone, especially because we already have our filenames in our sample.txt file. The beauty of Bash is that we can use a command substitution (discussed in “Command Substitution” on page 54) to construct Bash arrays (though this can be dangerous; see the following warning). Because we want to loop over each file, we need to extract the third column using cut -f 3 from samples.txt. Demonstrating this in the shell:

```shell
$ sample_files=$($(cut -f 3 samples.txt))
$ echo ${sample_files[@]}
seq/zmaysA_R1.fastq seq/zmaysA_R2.fastq seq/zmaysB_R1.fastq
seq/zmaysB_R2.fastq seq/zmaysC_R1.fastq seq/zmaysC_R2.fastq
```

Again, this only works if you can make strong assumptions about your filenames— namely that they only contain alphanumeric characters, (\_), and (-)! If spaces, tabs, newlines, or special characters like \* end up in filenames, it will break this approach.

![](images/page_436_image_4.jpg)

## The Internal Field Separator, Word Splitting, and Filenames

When creating a Bash array through command substitution with sample\_files=(\$(cut -f 3 samples.txt)), Bash uses word splitting to split fields into array elements by splitting on the characters in the Internal Field Separator (IFS). The Internal Field Separator is stored in the Bash variable IFS, and by default includes spaces, tabs, and newlines. You can inspect the value of IFS with:

```txt
\$ printf %q "\$IFS"
\$' \t\n'
```

Note that space is included in IFS (the first character). This can introduce problems when filenames contain spaces, as Bash will split on space characters breaking the filename into parts. Again, the best way to avoid issues is to not use spaces, tabs, newlines, or special characters (e.g., \*) in filenames—only use alphanumeric characters, (-), and (\_). The techniques taught in this section assume files are properly named and are not robust against improperly named files. If spaces are present in filenames, you can set the value of IFS to just tabs and newlines; see this chapter’s README file on GitHub for additional details on this topic.

With our filenames in a Bash array, we’re almost ready to loop over them. The last component is to strip the path and extension from each filename, leaving us with the most basic filename we can use to create an output filename. The Unix program base name strips paths from filenames:

```txt
$ basename seqs/zmaysA_R1.fastq
zmaysA_R1.fastq
```

basename can also strip a suffix (e.g., extension) provided as the second argument from a filename (or alternatively using the argument -s):

```shell
$ basename seqs/zmaysA_R1.fastq .fastq
zmaysA_R1
$ basename -s .fastq seqs/zmaysA_R1.fastq
zmaysA_R1
```

We use basename to return the essential part of each filename, which is then used to create output filenames for fastq\_stat’s results.

Now, all the pieces are ready to construct our processing script:

```shell
#!/bin/bash

set -e
set -u
set -o pipefail

# specify the input samples file, where the third
# column is the path to each sample FASTQ file
sample_info=samples.txt

# create a Bash array from the third column of $sample_info
sample_files=$(cut -f 3 "$sample_info")) ①

for fastq_file in ${sample_files[@]} ②
do
    # strip .fastq from each FASTQ file, and add suffix
    # "-stats.txt" to create an output filename for each FASTQ file
    results_file="$(basename $fastq_file .fastq)-stats.txt" ③

    # run fastq_stat on a file, writing results to the filename we've
    # above
    fastq_stat $fastq_file > stats/$results_file ④
done
```

1 This line uses command substitution to create a Bash array containing all FASTQ files. Note that this uses the filename contained in the variable \$sample\_info, which can later be easily be changed if the pipeline is to be run on a different set of samples.
Next, we loop through each sample filename using a Bash for loop. The expression \${sample\_files[@]} returns all items in the Bash array.
This important line creates the output filename, using the input file’s filename. The command substitution \$(basename \$fastq\_file .fastq) takes the current filename of the iteration, stored in \$fastq\_file, and strips the .fastq extension off. What’s left is the portion of the sample name that identifies the original file, to which the suffix -stats.txt is added.

Finally, the command fastq\_stat is run, using the filename of the current iteration as input, and writing results to stats/\$results\_file.

That’s all there is to it. A more refined script might add a few extra features, such as using an if statement to provide a friendly error if a FASTQ file does not exist or a call to echo to report which sample is currently being processed.

This script was easy to write because our processing steps took a single file as input, and created a single file as output. In this case, simply adding a suffix to each filename was enough to keep our samples straight. However, many bioinformatics pipelines combine two or more input files into a single output file. Aligning paired-end reads is a prime example: most aligners take two input FASTQ files and return one output alignment file. When writing scripts to align paired-end reads, we can’t loop over each file like we did earlier. Instead, each sample, rather than each file, is the processing unit. Our alignment step takes both FASTQ files for each sample, and turns this into a single alignment file for this sample. Consequently, our loop must iterate over unique sample names, and we use these sample names to re-create the input FASTQ files used in alignment. This will be clearer in an example; suppose that we use the aligner BWA and our genome reference is named zmays\_AGPv3.20.fa:

```shell
#!/bin/bash
set -e
set -u
set -o pipefail

# specify the input samples file, where the third
# column is the path to each sample FASTQ file
sample_info=samples.txt

# our reference
reference=zmays_AGPv3.20.fa

# create a Bash array from the first column, which are
# sample names. Because there are duplicate sample names
# (one for each read pair), we call uniq
sample_names=$(cut -f 1 "$sample_info" | uniq)) ①

for sample in ${sample_names[@]}
do
    # create an output file from the sample name
    results_file="${sample}.sam" ②
    bwa mem $reference ${sample}_R1.fastq ${sample}_R2.fastq \ ③
    > $results_file
done
```

This is much like the previous example, except now we use cut to grab the first column (corresponding to sample names), and (most importantly) pipe these sample names to uniq so duplicates of the same sample name are removed. This is necessary because our first column repeats each sample name twice, once for each paired-end file.
As before, we create an output filename for the current sample being iterated over. In this case, all that’s needed is the sample name stored in \$sample.
3 Our call to bwa provides the reference, and the two paired-end FASTQ files for this sample as input. Note how we can re-create the two input FASTQ files for a given sample name, as the naming of these files across samples is consistent. In practice, this is possible for a large amount of bioinformatics data, which often comes from machines that name files consistently. Finally, the output of bwa is redirected to \$results\_file. For clarity, I’ve omitted quoting variables in this command, but you may wish to add this.

Finally, in some cases it might be easier to directly loop over files, rather than working a file containing sample information like samples.txt. The easiest (and safest) way to do this is to use Bash’s wildcards to glob files to loop over (recall we covered globbing in “Organizing Data to Automate File Processing Tasks” on page 26). The syntax of this is quite easy:

```shell
#!/bin/bash
set -e
set -u
set -o pipefail

for file in *.fastq
do
    echo "$file: " $(bioawk -c fastx 'END {print NR}' $file)
done
```

This simple script uses bioawk to count how many FASTQ records are in a file, for each file in the current directory ending in .fastq.

Bash’s loops are a handy way of applying commands to numerous files, but have a few downsides. First, compared to the Unix tool find (which we see in the next section), globbing is not a very powerful way to select certain files. Second, Bash’s loop syntax is lengthy for simple operations, and a bit archaic. Finally, there’s no easy way to parallelize Bash loops in a way that constrains the number of subprocesses used. We’ll see a powerful file-processing Unix idiom in the next section that works better for some tasks where Bash scripts may not be optimal.

# Automating File-Processing with find and xargs

In this section, we’ll learn about a more powerful way to specify files matching some criteria using Unix find. We’ll also see how files printed by find can be passed to another tool called xargs to create powerful Unix-based processing workflows.

## Using find and xargs

First, let’s look at some common shell problems that find and xargs solve. Suppose you have a program named process\_fq that takes multiple filenames through standard in to process. If you wanted to run this program on all files with the suffix .fq, you might run:

```txt
$ ls *.fq
treatment-01.fq treatment 02.fq treatment-03.fq
$ ls *.fq | process_fq
```

Your shell expands this wildcard to all matching files in the current directory, and ls prints these filenames. Unfortunately, this leads to a common complication that makes ls and wildcards a fragile solution. Suppose your directory contains a filename called treatment 02.fq. In this case, ls returns treatment 02.fq along with other files. However, because files are separated by spaces, and this file contains a space, process\_fq will interpret treatment 02.fq as two separate files, named treatment and 02.fq. This problem crops up periodically in different ways, and it’s necessary to be aware of when writing file-processing pipelines. Note that this does not occur with file globbing in arguments—if process\_fq takes multiple files as arguments, your shell handles this properly:

```txt
$ process_fq *.fq
```

Here, your shell automatically escapes the space in the filename treatment 02.fq, so process\_fq will correctly receive the arguments treatment-01.fq, treatment 02.fq, treatment-03.fq. So why not use this approach? Alas, there’s a limit to the number of files that can be specified as arguments. It’s not unlikely to run into this limit when processing numerous files. As an example, suppose that you have a tmp/ directory with thousands and thousands of temporary files you want to remove before rerunning a script. You might try rm tmp/\*, but you’ll run into a problem:

```txt
\$ rm tmp/*
/bin/rm: cannot execute [Argument list too long]
```

New bioinformaticians regularly encounter these two problems (personally, I am asked how to resolve these issues at least once every other month by various colleagues). The solution to both of these problems is through find and xargs, as we will see in the following sections.

## Finding Files with find

Unlike ls, find is recursive (it will search for matching files in subdirectories, and subdirectories of subdirectories, etc.). This makes find useful if your project directory is deeply nested and you wish to search the entire project for a file. In fact, running find on a directory (without other arguments) can be a quick way to see a project directory’s structure. Again, using the zmays-snps/ toy directory we created in “Organizing Data to Automate File Processing Tasks” on page 26:

```txt
$ find zmays-snps
zmays-snps
zmays-snps/analysis
zmays-snps/data
zmays-snps/data/seqs
zmays-snps/data/seqs/zmaysA_R1.fastq
zmays-snps/data/seqs/zmaysA_R2.fastq
zmays-snps/data/seqs/zmaysB_R1.fastq
zmays-snps/data/seqs/zmaysB_R2.fastq
zmays-snps/data/seqs/zmaysC_R1.fastq
zmays-snps/data/seqs/zmaysC_R2.fastq
zmays-snps/scripts
```

find’s recursive searching can be limited to search only a few directories deep with the argument -maxdepth. For example, to search only within the current directory, use -maxdepth 1; to search within the current directory and its subdirectories (but not within those subdirectories), use -maxdepth 2.

The basic syntax for find is find path expression. Here, path specifies which directory find is to search for files in (if you’re currently in this directory, it’s simply find .). The expression part of find’s syntax is where find’s real power comes in. Expressions are how we describe which files we want to find return. Expressions are built from predicates, which are chained together by logical AND and OR operators. find only returns files when the expression evaluates to true. Through expressions, find can match files based on conditions such as creation time or the permissions of the file, as well as advanced combinations of these conditions, such as “find all files created after last week that have read-only permissions.”

To get a taste of how simple predicates work, let’s see how to use find to match files by filename using the -name predicate. Earlier we used unquoted wildcards with ls, which are expanded by the shell to all matching filenames. With find, we quote patterns (much like we did with grep) to avoid our shells from interpreting characters like \*. For example, suppose we want to find all files matching the pattern "zmaysB\*fastq" (e.g., FASTQ files from sample “B”, both read pairs) to pass to a pipeline. We would use the command shown in Example 12-1:

## Example 12-1. Find through filename matching

```txt
$ find data/seqs -name "zmaysB*fastq"
data/seqs/zmaysB_R1.fastq
data/seqs/zmaysB_R2.fastq
```

This gives similar results to ls zmaysB\*fastq, as we’d expect. The primary difference is that find reports results separated by newlines and, by default, find is recursive.

## find’s Expressions

find’s expressions allow you to narrow down on specific files using a simple syntax. In the previous example, the find command (Example 12-1) would return directories also matching the pattern "zmaysB\*fastq". Because we only want to return FASTQ files (and not directories with that matching name), we might want to limit our results using the -type option:

```txt
$ find data/seqs -name "zmaysB*fastq" -type f
data/seqs/zmaysB_R1.fastq
data/seqs/zmaysB_R2.fastq
```

There are numerous different types you can search for (e.g., files, directories, named pipes, links, etc.), but the most commonly used are f for files, d for directories, and l for links.

By default, find connects different parts of an expression with logical AND. The find command in this case returns results where the name matches "zmaysB\*fastq" and is a file (type “f ”). find also allows explicitly connecting different parts of an expression with different operators. The preceding command is equivalent to:

```shell
$ find data/seqs -name "zmaysB*fastq" -and -type f
data/seqs/zmaysB_R1.fastq
data/seqs/zmaysB_R2.fastq
```

We might also want all FASTQ files from samples A or C. In this case, we’d want to chain expressions with another operator, -or (see Table 12-3 for a full list):

```shell
$ find data/seqs -name "zmaysA*fastq" -or -name "zmaysC*fastq" -type f
data/seqs/zmaysA_R1.fastq
data/seqs/zmaysA_R2.fastq
data/seqs/zmaysC_R1.fastq
data/seqs/zmaysC_R2.fastq
```

Table 12-3. Common find expressions and operators

| Operator/expression | Description |
| --- | --- |
| -name | Match a filename to, using the same special characters (*,?, and [...] as Bash) |
| -iname | Identical to -name, but is case insensitive |
| -empty | Matches empty files or directories |
| -type | Matches types x (f for files, d for directories, l for links) |
| -size | Matches files where theis the file size (shortcuts for kilobytes (k), megabytes (M), gigabytes (G), and terabytes (T) can be used); sizes preceded with + (e.g., +50M) match files at least this size; sizes preceded with - (e.g., -50M) match files at most this size |
| -regex | Match by regular expression (extended regular expressions can be enabled with -E) |
| -iregex | Identical to -regex, but is case insensitive |
| -print0 | Separate results with null byte, not newline |
| expr -and expr | Logical “and” |
| expr -or expr | Logical “or” |
| -not/“!”expr | Negation |
| (expr) | Group a set of expressions |

An identical way to select these files is with negation:

```txt
$ find seqs -type f "!" -name "zmaysC*fastq"
seqs/zmaysA_R1.fastq
seqs/zmaysA_R2.fastq
seqs/zmaysB_R1.fastq
seqs/zmaysB_R2.fastq
```

Let’s see one more advanced example. Suppose that a messy collaborator decided to create a file named zmaysB\_R1-temp.fastq in seqs/. You notice this file because now your find command is matching it (we are still in the zmays/data directory):

```txt
\$ touch seqs/zmaysB_R1-temp.fastq
\$ find seqs -type f "!" -name "zmaysC*fastq"
seqs/zmaysB_R1-temp.fastq
seqs/zmaysA_R1.fastq
seqs/zmaysA_R2.fastq
seqs/zmaysB_R1.fastq
seqs/zmaysB_R2.fastq
```

You don’t want to delete his file or rename it, because your collaborator may need that file and/or rely on it having that specific name. So, the best way to deal with it seems to be to change your find command and talk to your collaborator about this mystery file later. Luckily, find allows this sort of advanced file querying:

```txt
$ find seqs -type f "!" -name "zmaysC*fastq" -and "!" -name "*-temp*"
seqs/zmaysA_R1.fastq
seqs/zmaysA_R2.fastq
seqs/zmaysB_R1.fastq
seqs/zmaysB_R2.fastq
```

Note that find’s operators like !, (, and ) should be quoted so as to avoid your shell from interpreting these.

## find’s -exec: Running Commands on find’s Results

While find is useful for locating a file, its real strength in bioinformatics is as a tool to programmatically access certain files you want to run a command on. In the previous section, we saw how find’s expressions allow you to select distinct files that match certain conditions. In this section, we’ll see how find allows you to run commands on each of the files find returns, using find’s -exec option.

Let’s look at a simple example to understand how -exec works. Continuing from our last example, suppose that a messy collaborator created numerous temporary files. Let’s emulate this (in the zmays-snps/data/seqs directory):

```txt
$ touch zmays{A,C}_R{1,2}-temp.fastq
$ ls
zmaysA_R1-temp.fastq zmaysB_R1-temp.fastq zmaysC_R1.fastq
zmaysA_R1.fastq     zmaysB_R1.fastq     zmaysC_R2-temp.fastq
zmaysA_R2-temp.fastq zmaysB_R2.fastq     zmaysC_R2.fastq
zmaysA_R2.fastq      zmaysC_R1-temp.fastq
```

Suppose your collaborator allows you to delete all of these temporary files. One way to delete these files is with rm \*-temp.fastq. However, rm with a wildcard in a direc tory filled with important data files is too risky. If you’ve accidentally left a space between \* and -temp.fastq, the wildcard \* would match all files in the current directory and pass them to rm, leading to everything in the directory being accidentally deleted. Using find’s -exec is a much safer way to delete these files.

find’s -exec works by passing each file that matches find’s expressions to the command specified by -exec. With -exec, it’s necessary to use a semicolon at the end of the command to indicate the end of your command. For example, let’s use find - exec and rm -i to delete these temporary files. rm’s -i forces rm to be interactive, prompting you to confirm that you want to delete a file. Our find and remove command is:

```shell
$ find . -name "*.-temp.fastq" -exec rm -i {} \;
remove ./zmaysA_R1-temp.fastq? y
remove ./zmaysA_R2-temp.fastq? y
remove ./zmaysB_R1-temp.fastq? y
remove ./zmaysC_R1-temp.fastq? y
remove ./zmaysC_R2-temp.fastq? y
```

In one line, we’re able to pragmatically identify and execute a command on files that match a certain pattern. Our command was rm but can just as easily be a bioinformatics program. Using this approach allows you to call a program on any number of files in a directory. With find and -exec, a daunting task like processing a directory of 100,000 text files with a program is simple.

![](images/page_445_image_2.jpg)

## Deleting Files with find -exec

Deleting files with find -exec is a such a common operation that find also has a -delete option you can use in place of -exec -rm {} (but it will not be interactive, unlike rm with -i).

When using -exec, always write your expression first and check that the files returned are those you want to apply the command to. Then, once your find command is returning the proper subset of files, add in your -exec statement. find - exec is most appropriate for quick, simple tasks (like deleting files, changing permissions, etc.). For larger tasks, xargs (which we see in the next section) is a better choice.

## xargs: A Unix Powertool

If there were one Unix tool that introduced me to the incredible raw power of Unix, it is xargs. xargs allows us to take input passed to it from standard in, and use this input as arguments to another program, which allows us to build commands programmatically from values received through standard in (in this way, it’s somewhat similar to R’s do.call()). Using find with xargs is much like find with -exec, but with some added advantages that make xargs a better choice for larger bioinformatics file-processing tasks.

Let’s re-create our messy temporary file directory example again (from the zmayssnps/data/seqs directory):

\$ touch zmays{A,C}\_R{1,2}-temp.fastq # create the test files

xargs works by taking input from standard in and splitting it by spaces, tabs, and newlines into arguments. Then, these arguments are passed to the command supplied. For example, to emulate the behavior of find -exec with rm, we use xargs with rm:

```shell
$ find . -name "*.temp.fastq"
./zmaysA_R1-temp.fastq
./zmaysA_R2-temp.fastq
./zmaysC_R1-temp.fastq
./zmaysC_R2-temp.fastq
$ find . -name "*.temp.fastq" | xargs rm
```

![](images/page_446_image_1.jpg)

## Playing It Safe with find and xargs

There’s one important gotcha with find and xargs: spaces in filenames can break things, because spaces are considered argument separators by xargs. This would lead to a filename like treatment 02.fq being interpreted as two separate arguments, treatment and 02.fq. The find and xargs developers created a clever solution: both allow for the option to use the null byte as a separator. Here is an example of how to run find and xargs using the null byte delimiter:

\$ find . -name "samples [AB].txt" -print0 | xargs -0 rm In addition to this precaution, it’s also wise to simply not use filenames that contain spaces or other strange characters. Simple alphanumeric names with either dashes or underscores are best. To simplify examples, I will omit -print0 and -0, but these should always be used in practice.

Essentially, xargs is splitting the output from find into arguments, and running:

```shell
\$ rm ./zmaysA_R1-temp.fastq ./zmaysA_R2-temp.fastq \
./zmaysC_R1-temp.fastq ./zmaysC_R2-temp.fastq
```

xargs passes all arguments received through standard in to the supplied program (rm in this example). This works well for programs like rm, touch, mkdir, and others that take multiple arguments. However, other programs only take a single argument at a time. We can set how many arguments are passed to each command call with xargs’s -n argument. For example, we could call rm four separate times (each on one file) with:

```powershell
$ find . -name "*-temp.fastq" | xargs -n 1 rm
```

One big benefit of xargs is that it separates the process that specifies the files to operate on (find) from applying a command to these files (through xargs). If we wanted to inspect a long list of files find returns before running rm on all files in this list, we could use:

```shell
$ find . -name "*-temp.fastq" > files-to-delete.txt
$ cat files-to-delete.txt
./zmaysA_R1-temp.fastq
./zmaysA_R2-temp.fastq
./zmaysC_R1-temp.fastq
```

```txt
./zmaysC_R2-temp.fastq
\$ cat files-to-delete.txt | xargs rm
```

Another common trick is to use xargs to build commands that are written to a simple Bash script. For example, rather than running rm directly, we could call echo on rm, and then allow xargs to place arguments after this command (remember, xargs’s behavior is very simple: it just places arguments after the command you provide). For example:

```shell
$ find . -name "*.temp.fastq" | xargs -n 1 echo "rm -i" > delete-temp.sh
$ cat delete-temp.sh
rm -i ./zmaysA_R1-temp.fastq
rm -i ./zmaysA_R2-temp.fastq
rm -i ./zmaysC_R1-temp.fastq
rm -i ./zmaysC_R2-temp.fastq
```

Breaking up the task in this way allows us to inspect the commands we’ve built using xargs (because the command xargs runs is echo, which just prints everything). Then, we could run this simple script with:

```shell
\$ bash delete-temp.sh
remove ./zmaysA_R1-temp.fastq? y
remove ./zmaysA_R2-temp.fastq? y
remove ./zmaysC_R1-temp.fastq? y
remove ./zmaysC_R2-temp.fastq? y
```

## Using xargs with Replacement Strings to Apply Commands to Files

So far, xargs builds commands purely by adding arguments to the end of the command you’ve supplied. However, some programs take arguments through options, like program --in file.txt --out-file out.txt; others have many positional arguments like program arg1 arg2. xargs’s -I option allows more fine-grained placement of arguments into a command by replacing all instances of a placeholder string with a single argument. By convention, the placeholder string we use with -I is {}.

Let’s look at an example. Suppose the imaginary program fastq\_stat takes an input file through the option --in, gathers FASTQ statistics information, and then writes a summary to the file specified by the --out option. As in our Bash loop example (“Processing Files with Bash Using for Loops and Globbing” on page 405), we want our output filenames to be paired with our input filenames and have corresponding names. We can tackle this with find, xargs, and basename. The first step is to use find to grab the files you want to process, and then use xargs and basename to extract the sample name. basename allows us to remove suffixes through the argument -s:

```txt
$ find . -name "*.fastq" | xargs basename -s ".fastq" zmaysA_R1
```