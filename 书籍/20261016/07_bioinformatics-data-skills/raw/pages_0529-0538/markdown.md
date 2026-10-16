binning data with cut() and bar plots with ggplot2, 215-218

bioinformatics packages from Bioconductor, 269

Comprehensive R Archive Network (CRAN), 177

debugging code, 236-237

developing workflows with R scripts, 253-261

control flow, if, for, and while, 253

exporting data, 260

loading and combining multiple files, 257

working with R scripts, 254

exploring and transforming dataframes, 199-203

exploring data by subsetting dataframes, 203-207

exploring data visually with ggplot2 scatterplots and densities, 207-213 smoothing, 213-215

exploring dataframes with dplyr, 243-248

futher directions and resources, 261

getting started with R and RStudio, 176

installing R, 178

lists

list apply functions, sapply() and mapply(), 237

loading data into R, 194-198

getting data into shape, 198

inspecting file at command line before loading, 195

large genomics data, 195

working directory, 194

merging and combining data, 219-224

more data structures, lists, 228-234

packages for data, 309

RSQLite package, 464

split-apply-combine pattern in data analysis, 239-243

stopifnot function, 12

visualizing grouped data with ggplot2 facets, 224-228

working with data, 193

working with ranges, 289

working with strings, 248-253

writing functions, 234-236

range data, 263-337

basic range operations on IRanges object, 275

calculating coverage for GRanges objects, 327

finding and working with overlapping ranges, 324-327

finding nearest ranges and calculating distance, 290

finding overlapping ranges, 281 intricacies of overlap operations, 286

genomic ranges and coordinate systems, 264-269

getting intergenic and intronic regions, 319

installing and working with Bioconductor packages, 269

ranges, 263, 264

run-length encoding and views, 292-299

creating ranges from run-length encoded sequences, 296

ranges and their coverage, 294

views, 297

storing generic ranges with IRanges, 270

storing genomic ranges with GenomicRanges, 299

grouping data with GRangesList, 303

working with annotation data, using GenomicFeatures and rtracklayer, 308

working with on command line, using BED‐Tools, 329-337

computing overlaps with intersect, 330-333

genomecov, 335

other subcommands and pybedtools, 336

slop and flank, 333

range width, 267

accessing for GRanges object, 301

getting for IRanges object, 273

ranges() function

using with GRanges, 301

using with Hits object, 288

ranges, handling in Unix shell, 29

raw vectors (R), 190

rbind() function (R), 240, 258

read groups (SAM/BAM files), 358

read.csv() function (R), 200

coercion of column of strings into factor, 197

commonly used arguments, 196

loading large data files more quickly, 195

returning results as data.frame, 200

read.delim() function (R), 260

coercion of column of strings into factor, 197

commonly used arguments, 196

loading large data files more quickly, 195

returning results as data.frame, 200

read.table() function (R), 196

readfq parser, 350

README files, 16

project documentation in, 25

recombination, 194

records, 128

NR variable in awk, 160

processing with awk, 157

recursive downloading (wget), 111

redirection, 38

combining with pipes, 48

using tee program, 49

redirecting standard error, 43

redirecting standard out to file, 41

using standard input redirection, 45

xargs, pipes, and redirects, 420

reduce() function, 278, 321

calling on GRangesList, 307

extracting and collapsing overlapping exons with, 325

ranges collapsed into non-overlapping ranges with, 278

reference genomes, 265

reference-based compression scheme, 366

regexpr() function (R), 248, 249

regular expressions

capturing groups, 250

capturing text between delimiters in sed, 168

in R, 248

help on, 249

list.files() function, 257

use by sub() function, 251

POSIX Basic Regular Expressions (BREs), support by grep, 143

POSIX Extended Regular Expressions (ERE), support by grep, 143

support in sed, 166

with grep, 47

relational database management system

(RDBMS), 428, 477

relational databases, 428, 477

organizing, 448

when to use in bioinformatics, 429

relative paths, 23, 255

remote branches (Git), 106

remote machines, working with, 57-65

connecting via SSH, 57

maintaining long-running jobs with nohup and tmux, 61-65

quick authentication with SSH keys, 59

remote repositories (Git), 84

removing files with git rm, 80

RepeatMasker, 343

repositories (Git), 70, 82

creating with git clone, 71

creating with git init, 70

reproducible research

adopting reproducible practices, 9

case study, Duke Saga, 7

definition in bioinformatics, 6

downloading files reproducibly, case study, 120-122

environment variables and, 401

new challenges for, 5

recommendations for, 16-17

documenting everything, 16

making figures and statistics result from scripts, 17

releasing your code and data, 16

using code as documentation, 17

Unix one-liners and pipelines, documenting, 128

using knitr and Rmarkdown packages, 254

versions of R and R packages, 256

reshape2 package (R), 198

restrict() function, 276

return value, 179, 180

for functions in R, 234

reverse complement, 268

right outer joins, 224, 454

emulating in SQLite, 454

Rle object, 293

subsetting, using IRanges object, 295

Rle() function, 293

RleList object, 305

Rmarkdown package, 255

RNA-seq quantification tools, 325

RNA-seq studies, 263, 282

overlaps and, 286, 324

RNAME (reference name), 360

RNEXT and PNEXT, 360

rngs\_cov object, 296

robust, 477

robust research, 8

adopting robust practices, 9

challenges for, 8

checking how programs change our data, 349

consistent file naming in, 30

Golden Rule of Bioinformatics, 9

recommendations for, 10-16

developing frequently used scripts into tools, 15

experimental design, 10

letting data prove it's high quality, 15

letting the computer do the work, 12

making assertions and being loud, 12

testing code, 13

treating data as read-only, 14

using existing libraries when possible, 14

writing code for humans, data for computers, 11

using Unix data tools, 137

round() function (R), 180

row.names() function (R), 199, 200

rows

dataframes in R, 199

selecting specific rows with deply function filter(), 244

subsetting, 206

filtering in SQLite with SELECT WHERE, 437

grouping in SQLite with GROUP BY, 444

ordering in SQLite with ORDER BY, 436

RSQLite package, 196, 464

RStudio, 176

(see also R language)

installing, 178

sending a whole function definition at once, 235

rsync program, 113

rtracklayer package, 269, 308, 313-314

export methods for range data saved to common formats, 313

import() function, 313

run-length encoding, 293

calculating coverage reads, 328

coverage() function and, 294

operations supported by Rle objects, 293

runLengths() function, 294

runs, 293

runValues() function, 294

\r\n (carriage return and linefeed), 129

## S

S3 object-oriented system (R), 193

SAM alignment format, 353, 355

specification, 356

SAM/BAM files, 355-365

bitwise flags, 360

CIGAR strings, 363

command-line tools for working with alignments in SAM, 365

creating processing tools with Pysam, 384-394

mapping qualities, 365

SAM alignment section, 359

SAM header, 356

sequence matches and mismatches and NM and MD tags, 364

sample() function (R), 187, 328

SAMtools, 358, 365

extracting and filtering alignments with samtools view, 368-372

pileups with samtools pileup, variant calling, and Base Alignment Quality, 378-384

samtools calmd, 364

samtools faidx, 353

samtools flag, 361

samtools flagstat, 393

samtools mpileup, 368, 378

samtools tview, 372

samtools view, 358

sort and index, 367

subcommands implemented by Pysam, 394

support for CRAM file format, 366

using samtools view to convert between SAM and BAM, 365

Sanger quality scheme, 345

Sanger sequencing, 477

sapply() function (R), 237, 240

using with GRangesList, 307

save() function (R), 260

save.image() function (R), 261

savehistory command (R), 177

savehistory() function (R), 261

scale, x and y axes in ggplot2, 209

facet\_wrap() and facet\_grid() functions, 227

scatterplot of nucleotide diversity, creating with ggplot2, 208-212

schema, 432, 477

scientific coding, paradox of, 13

scoping, 235

SCP (secure copy), 112

scp (secure copy) command, 114

scripts

frequently used, developing into tools, 15

making figures and statistics the results of, 17

making Python scripts executable, 352

working with R scripts, 254

executing scripts from command line, 256

executing scripts with source(), 255

retrieving command-line argumens passed to scripts, 256

search() function (R), 182

secure shell (see SSH)

sed, 165-169

cleaning up gene names matched by grep, 145

editing chroms.txt file (example), 165

GNU versus BSD sed, 165

performance, grep versus, 140

piping subshell command output to, 170

substitutions, using pattern matching and regular expressions, 166

using regular expressions to capture text between delimiters, 168

SELECT statement, 434

filtering rows with WHERE clause, 437

limiting results with LIMIT, 435

ordering rows with ORDER BY, 436

selecting columns, 435

select() function (dplyr), 244

separators

Internal Field Separator (IFS), 407

setting in awk, 161

setting in bioawk, 164

seq command, 130

SEQ field, 360

seqencing depth, 194

seqinfo() function, 316

seqlevels() function, 318

seqlevelsStyle() function, 318

seqnames() function, 301

Seqtk (SEQuence ToolKit), 71, 346

seqtk trimfq, inspecting and trimming lowquality bases, 347

Sequence Alignment/Mapping (see SAM alignment format)

sequence data, 339-354

base qualities, 344

counting FASTA/FASTQ entries, 342

counting nucleotides, FASTA/FASTQ parsing example, 349

FASTA format, 339

FASTQ format, 341

indexed FASTA files, 352

inspecting and trimming low-quality bases (example), 346

nucleotide codes, 343

sequence lengths, table of, creating using bioawk on a FASTA file, 164

sequence name, 264

sequencing depth

relationship of GC content to, 215

relationship with SNPs, 214

sequential command execution with ;, 53

sequential versus piped commands, 169

seq\_along() function (R), 254

serialization, 260, 477

sessionInfo() function (R), 256

sessions (Tmux), 62

set operations

creating gaps using range operations, 320

on ranges, 280

pairwise set operations, 281

using range set operations to get intronic regions, 321

setdiff() function, 321

setwd() function (R), 194

scripts and, 255

SFTP (secure FTP), 112

SHA-1 checksums, 79

checking data integrity with shasum, 115

shared central repository, collaborating over, 84

shebang, 397, 477

shell expansion, tips on, 27

shell scripting, basic Bash scripting, 396-410

shell wildcards (see wildcards)

short-circuit evaluation, 405

short-circuiting operators, 52

sickle program, 346

inspecting and trimming low-quality bases (example), 347

SIGHUP signals, 51, 61

SIGINT signals, 131

significant digits (R), 179

SIGPIPE signals, 131

silent errors, 8

implicit assumptions leading to, 12

single nucleotide polymorphisms (SNPs), 203

relationship with depth of sequencing, 214

slice() function, 296

slop (bedtools), 333

smoothing (ggplot2), 213-215

bin widths and, 218

snapshots of your project, keeping with Git, 68

SNPs (see single nucleotide polymorphisms)

soft and hard clipping, 363

soft masked, 343

software regression, 68

Solexa quality scheme, 345

sort (samtools), 367

sort program, 147

--parallel option, 152

-s option, sorting stability and, 149

-V option, 150

cleaning up gene names matched by grep, 145

grouping ranges for bedtools genomecov, 336

handling tabular data properly, 148

merge sort algorithm, 151

sort | uniq, 153

sorting BED files for bedtools intersect, 332

using different delimiters with sort, 148

validating sorting of a file, 150

sorting

dataframe columns in R, using dplyr function arrange(), 245

using tools other than Unix sort, 152

sorting stability, 149, 477

source() function (R), 255

space-delimited file formats, 129

split() function (R)

GRangesList objects created by, 322

using on GRanges, 306

split-apply-combine pattern (R), 239-243

applying a function using lapply(), 239

combining data, 240

using do.call(), 241

using summay() function, 240

convenience functions wrapping split(), lapply() and combine steps, 242

splitting data with split(), 239

using with GRangesList, 307

spreadsheet syndrome, 448, 478

SQL (Structured Query Language), 430

SQLite, 428, 431-465

aggregate functions, 442

grouping rows with GROUP BY, 444

database underlying TranscriptDb objects, 313

dropping tables and deleting databases, 458

dumping databases, 465

exploring databases with the command-line interface, 431

functions, 441

installing, 431

interacting with, from Python, 459

conecting to databases and creating tables, 459

loading data into a table, 461

organizing relational databases and joins, 448-455

inner joins, 451

left outer joins, 453

querying data with SELECT command, 434-440

filtering rows with WHERE, 437

limiting results with LIMIT, 435

ordering rows with ORDER BY, 436

selecting columns, 435

RSQLite package, 196

subqueries, 447

writing to databases, 455-458

creating tables, 455

indexing, 457

inserting records into tables, 457

sqlite3 (command-line tool), 431

working with, 434

sqrt() function (R), 179

SSH, 478

connecting to remote machines via, 57

quick authentication with SSH keys, 59

SSH config files, 58

using SSH keys for authentication in Git‐Hub, 87

ssh command, 57

-add option, 60

-agent option, 60

-copy-id options, 60

-keygen option, 59

-p option, 58

stable sorting, 149

staging files (Git), 73

git diff and, 78

tracked files’ changes, staging and committing, 76

undoing with git reset, 83

standard error, 478

file descriptor, 44

redirected, monitoring with tail -f, 45

redirecting, 43, 49

standard input, 478

file descriptor, 44

redirection, using, 45

standard output, 478

curl command writing to, 112

file descriptor, 44

redirecting standard error to, 49

redirecting to a file, 41

start position and end position (ranges), 264

accessing for GRanges object, 301

getting for IRanges object, 273

statistical analysis of high-dimensional genomics data, 176

statistics and probability, 468

stop() function (R), 252

stopifnot() function (R), 252

str() function (R), 230

calling on IRanges object, 273

strand() function, 301

strands, 265

bedtools intersect and, 332

flank() handling of, 315

forward and reverse, genomic features on, 268

gaps between ranges and, 319

streams, 39, 41, 45

(see also standard error; standard input; standard output)

editing with sed, 165-169

file descriptors on Unix, 44

strings

character vectors in R, 189, 191

column of strings, coercion into factors, 197, 200

comparison operators in Bash, 402

concatenating in awk, 158

string-matching functions to search BSgenome objects, 317

working with in R, 248-253

combining sub() and strsplit(), 252

grep() function, 248

nchar() function, 248

paste() function, 252

regexpr() function, 249

sub() function, 250

substr() function, 250

strsplit() function (R), 252

sub() function (R), 250, 258

combining with strsplit(), 252

subcommands (Git), 70

subject ranges (sbj), 283

and select parameter of findOverlaps(), 285

building interval trees from, 286

mapping between qry ranges and, representing overlap, 283

using countOverlaps() and subsetByOverlaps() with, 289

subjectHits() function, 284

subj\_it object, 287

subprojects, creating using diretories, 26

subqueries, 447

subset() function (R), 206

subsetByOverlaps() function, 289, 327

subsetting, 185

dataframes in R, 203-207

using filter() function in dplyr, 244

GRanges object, 302

IRanges object, 274

lists in R, 229

run-length encoded sequences, 295

subshells, 169, 426

combining sequential commands' standard output into single stream, 170

substitute command (sed), 166

substr() function (R), 250

use of closed intervals, 267

sum program, 121

sum() function (R), 203

summarize() function (dplyr), 247

summary() function (R), 193, 203

using in split-apply-combine pattern, 240

suspending a process, 51

## T

t-test, 175

tab-delimited files, 128

bioawk options for working with, 164

columns and, 139

indexing with Tabix, 427

reading with read.delim() function in R, 196

Tabix, 426

compressing files for, using bgzip, 426

indexing files with, 427

using to make fast queries, 427

table() function (R), 192, 202

counting items in a bin, 216

tables (database)

creating, 455

dropping, 458

tabular data, wide and long formats, 198

tabular plain-text data formats, 128

handling tabular data with sort, 148

processing with awk, 136

tail -f, monitoring redirected standard error with, 45

tail program, 130

cutting off comments with tail -n, 137

weakness of using tail -n to remove comment header, 137

Tandem Repeats Finder, 343

tapply() function (in R), 242

tar program, 120

tbl\_df class, 243

tcsh shell, 40

tee program, 49

terminal colors setting (Git), 70

terminal multiplexer (see Tmux)

terminal pagers, 131

test command (Bash), 402

combining with if statements, 404

file and directory test expressions, 403

testing code, 13

importance of, strategy for determining, 13

text streams, 39

text-processing tasks, R language and, 248

titles, plot titles in ggplot2, 209

TLEN (template length), 360

Tmux (terminal multiplexer), 61-65

common key sequences, 64

common subcommands, 65

creating, detaching, and attaching sessions, 62

installing and configuring, 62

working with Tmux windows, 64

tools

developing frequently used scripts into, 15

for bioinformatics, 467

rapid development for bioinformatics, 3

TopHat and Cufflinks suite of tools, 325

Torvalds, Linus, 67

touch command, creating README files, 25

transcript annotation packages, 309

(see also annotation data)

TranscriptDb object, 308, 310

coercing chromosome information into GRanges object, 320

creating, 312

extracting and collapsing overlapping exons with reduce(), 325

extracting exons from, 322

transcription termination site (TTS), 277

transcripts, 269, 322

(see also TranscriptDb object)

retrieving with GenomicFeatures, 311

transcriptsByOverlaps() function, 312

transition start site (TSS), 277

transparency level (alpha), 211

trimmer program, 119

Tukey, J. W., 175

tuple unpacking, 351

tview (samtools), 372

TxDb.Mmusculus.UCSC.mm10.ensGene package, 309

type affinities, 433

type coercion in R, 190

coercing TranscriptDb object's chromosome information into GRanges, 320

column of strings, coercion into factors, 197

sum() function, coercing logical values to integers, 203

typeof() function (R), 191

## U

UCSC chromosome name style, 318

UCSC Ensembl track, 309

UCSC Genome Browser, 110, 440

creating TranscriptDb object for annotation data, 312

no inconsistent naming issues with, 251

rtracklayer interfacing with, 314

undersmoothing, 218

unified diff format, 78, 117

union, 280

unionbedg (bedtools), 337

uniq program, 152

-d (duplicates) option, 154

-i option for case insensitivity, 153

cleaning up gene names matched by grep, 145

sort | uniq, 153

sort | uniq and sort | uniq -c, 153

unit testing, 13, 478

Unix, 467

common filename wildcards, 29

Unix data tools, 125-174, 169, 330

(see also BEDTools)

(see also Unix shell)

implementations, BSD utils and GNU coreutils, 142

inspecting and manipulating text data, 128 bioawk, 163-165

column data, using cut and column, 138

decoding plain-text data, 145

finding uniqe values with uniq, 152

grep, 140-145

information on plain-text files with wc, ls, and awk, 134

inspecting data with head and tail, 129

join, 155

sorting plain-text data with sort, 147

text processing with awk, 157-163

using less, 131

using one-liners and pipelines, historical example, 125

using pipeline approach, 127

Unix philosophy, 173

Unix shell, 37-56

advanced shell tricks, 169-173

named pipes and process substitution, 171

subshells, 169

command substitution, 54

managing and interacting with processes, 50-53

many versions, 40

modularity and the Unix philosophy, 37

pipes, 45-50

power of, 40

working with streams and redirection, 41-45

unlist() function (R), 240

UNMAP flag, 369

unsplit() function (R), 241, 306

unstable sorting, 149

upstream flanking (ranges), 277

user accounts, getting with whoami command, 59

UTF-8 encoding, 146

## V

values, special, in R, 190

variables

Bash, 398

in awk, 157, 160

in R, 182

Variant Call Format (VCF), 380-383, 478

variant calling, 378, 379-383

vectorization (R), 183

vectorized logical operations, 188

vectors (R), 183

accessing elements by name, 185

creating a dataframe from, 200

dataframe column returned as a vector, 202

dataframe columns as vectors, 205

factors and classes, 191

functions returning index of first minimum or maximum element, 206

homogeneous data type and type coercion, 190

indexing of, 184

lists versus, 228

matching, 219

vector types, 189

version control systems (VCS), 67

(see also Git)

versions

documenting data version informtion, 25

documenting for software used, 25

views, 292, 296, 297

vignettes for Bioconductor packages, 270

visualization, 176

## W

warning() function (R), 252

wc (word count) program, 134

assumption of well-formatted data, 136

wget program, 110

--user and --ask-password options, 110

recursive downloading, 111

useful options, 111

wgsim read simulator, 356

WHERE clause, 437

aggregate functions with, 443

common operators used in, 438

which() function (R), 206

which.max() function (R), 206

which.min() function (R), 206

while loops (R), 253

whitespace, finding in a file with grep, 136

whoami command, 59

Wickham, Hadley, 207, 235, 243

wide format (tabular data), 198

wildcards

expanding to match file names, 28

matching, brace expansion versus, 29

using in Bash for file globbing, 410

Wilk, M. B., 175

word count program (see wc program)

word splitting in Bash, 407

workflows (GitHub)

forking repositories, 97

shared central repository, 84

working directory in R, 194, 255

write.table() function (R), 260

## X

xargs program, 416

and parallelization, 419

BSD and GNU xargs, 419

playing safe with, 417

using, 411

using with replacement strings to apply commands to files, 418

xargs, pipes, and redirects, 420

## Z

zdiff program, 120

zeros, leading, in filenames, 30

zgrep, 120, 170

extracting FASTA headers from gzipped file, 121

zless program, 120

zsh (Z shell), 40

## About the Author

**Vince Buffalo** is currently a first-year graduate student in Graham Coop’s lab at UC Davis in the Population Biology Graduate Group. Before starting his PhD in population genetics, Vince worked professionally as a bioinformatician in the Bioinformatics Core at the UC Davis Genome Center and in the Department of Plant Sciences.

An obsessive programmer since he was a young teenager, Vince was drawn to the statistical and computational problems of genomics. He works on open source bioinformatics tools in his work and free time, and enjoys fly fishing and cooking when away from the computer.

## Colophon

The animal on the cover of Bioinformatics Data Skills is a European hamster (Cricetus cricetus). Also known as the Eurasian or black-bellied hamster, this species is much larger and than the dwarf hamsters that are commonly kept as pets. The European hamster is native to the low-lying farmland of Belgium, Russia, Romania, and the countries in between.

As a nocturnal species, European hamsters prefer to spend the day sleeping in one of the rooms of their complex burrow systems. At night, they emerge to forage for seeds, legumes, root vegetables, and insects. Using their elastic cheek pouches, hamsters can carry food back to their burrows and deposit it in special storage chambers. These chambers can grow very large and store up to 65 grams of food.

From October through March, European hamsters hibernate, waking every five to seven days to feed from the storage chambers. Once hibernation is over, the hamsters emerge to breed and raise their young. After a gestation period of only 20 days, litters of three to fifteen babies are born, and will stay with the mother for three weeks.

Although the overall population of European hamsters is healthy, it is considered critically endangered in some countries. In 2011, the Court of Justice in Luxembourg ruled that France needed to adjust its agricultural and urbanization policies to better protect the European hamster, or else face fines of up to \$24.6 million.

Many of the animals on O’Reilly covers are endangered; all of them are important to the world. To learn more about how you can help, go to [animals.oreilly.com](http://animals.oreilly.com).

The cover image is from Lydekker’s Royal Natural History. The cover fonts are URW Typewriter and Guardian Sans. The text font is Adobe Minion Pro; the heading font is Adobe Myriad Condensed; and the code font is Dalton Maag’s Ubuntu Mono.