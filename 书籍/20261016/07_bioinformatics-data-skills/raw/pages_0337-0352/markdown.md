Grouped data is also the basis of the split-apply-combine pattern (covered in “Working with the Split-Apply-Combine Pattern” on page 239). With R’s base lists, we could use lapply() and sapply() to iterate through all elements and apply a function. Both of these functions work with GRangesLists objects, too:

```txt
> lapply(gr_split, function(x) order(width(x))) ①
\$chr3
[1] 1 2 3 4

\$chr1
[1] 1 2

\$chr2
[1] 1 4 2 3
> sapply(gr_split, function(x) min(start(x))) ②
chr3 chr1 chr2
    90    21    38
> sapply(gr_split, length) ③
chr3 chr1 chr2
    4    2    4
> elementLengths(gr_split) ④
chr3 chr1 chr2
    4    2    4
```

Return the order of widths (smallest range to largest) of each GRanges element in a GRangesList.
2 Return the start position of the earliest (leftmost) range.
The number of ranges in every GRangesList object can be returned with this R idiom.
However, a faster approach to calculating element lengths is with the specialized function elementLengths().

lapply() and sapply() (as well as mapply()) give you the most freedom to write and use your own functions to apply to data. However, for many overlap operation functions (e.g., reduce(), flank(), coverage(), and findOverlaps()), we don’t need to explicitly apply them—they can work directly with GRangesList objects. For example, reduce() called on a GRangesList object automatically works at the list-element level:

```txt
> reduce(gr_split)
GRangesList of length 3:
\$chr3
GRanges with 1 range and 0 metadata columns:
    seqnames   ranges strand
        <Rle> <IRanges>  <Rle>
[1]     chr3 [90, 117]      *
```

```txt
\$chr1
GRanges with 1 range and 0 metadata columns:
    seqnames   ranges strand
[1]     chr1 [21, 44]      *

\$chr2
GRanges with 2 ranges and 0 metadata columns:
    seqnames   ranges strand
[1]     chr2 [38, 44]      *
[2]     chr2 [58, 96]      *

---
seqlengths:
chr3 chr1 chr2
NA    NA    NA
```

reduce() illustrates an important (and extremely helpful) property of GRangesList objects: many methods applied to GRangesList objects work at the grouped-data level automatically. Had this list contained exons grouped by transcript, only overlapping exons within a list element (transcript) would be collapsed with reduce(). findO verlaps() behaves similarly; overlaps are caclulated at the list-element level. We’ll see a more detailed example of findOverlaps() with GRangesList objects once we start working with real annotation data in the next section.

## Working with Annotation Data: GenomicFeatures and rtracklayer

We’ve been working a lot with toy data thus far to learn basic range concepts and operations we can perform on ranges. Because the GenomicRanges package shines when working interactively with moderately large amounts of data, let’s switch gears and learn about two Bioconductor packages for importing and working with external data. Both packages have different purposes and connect with GenomicRanges. The first, GenomicFeatures, is designed for working with transcript-based genomic annotations. The second, rtracklayer, is designed for importing and exporting annotation data into a variety of different formats. As with other software covered in this book, both of these packages have lots of functionality that just can’t be covered in a single section; I highly recommend that you consult both packages’ vignettes.

GenomicFeatures is a Bioconductor package for creating and working with transcript-based annotation. GenomicFeatures provides methods for creating and working with TranscriptDb objects. These TranscriptDb objects wrap annotation data in a way that allows genomic features, like genes, transcripts, exons, and coding sequences (CDS), to be extracted in a consistent way, regardless of the organism and origin of the annotation data. In this section, we’ll use a premade TranscriptDb object, contained in one of Bioconductor’s transcript annotation packages. Later on, we’ll see some functions GenomicFeatures has for creating TranscriptDb objects (as well as transcript annotation packages) from external annotation data.

![](images/page_338_image_1.jpg)

## R Packages for Data

While it may sound strange to use an R package that contains data rather than R code, it’s actually a clever and appropriate use of an R package. Bioconductor uses packages for many types of data, including transcript and organism annotation data, experimental data, compressed reference genomes, and microarray and SNP platform details. Packages are a terrific way to unite data from multiple sources into a single easily loaded and explicitly versioned shared resource. Using data packages can eliminate the hassle of coordinating which files and what versions (and from what websites) collaborators need to download and use for an analysis. Overall, working with data from packages facilitates reproducibility; if you’re working with annotation data in R, use the appropriate package if it exists.

Let’s start by installing GenomicFeatures and the transcript annotation package for mouse, Mus musculus. We’ve already installed Bioconductor’s package installer, so we can install GenomicFeatures with:

```txt
> library(BiocInstaller)
> biocLite("GenomicFeatures")
```

Now, we need to install the appropriate Mus musculus transcript annotation package. We can check which annotation packages are available on the [Bioconductor annotation package page](http://bit.ly/anno-data). There are a few different packages for Mus musculus. At the time I’m writing this, TxDb.Mmusculus.UCSC.mm10.ensGene is the most recent. Let’s install this version:

```txt
> biocLite("TxDb.Mmusculus.UCSC.mm10.ensGene")
```

While this is installing, notice the package’s naming scheme. All transcript annotation packages use the same consistent naming scheme—that is, TxDb.&lt;organism&gt;.&lt;annotation-source&gt;.&lt;annotation-version&gt;. This annotation is for mouse genome version mm10 (Genome Reference Consortium version GRCm38), and the annotation comes from UCSC’s Ensembl track. Once these packages have installed, we’re ready to load them and start working with their data:

```txt
> library(TxDB.Mmusculus.UCSC.mm10.ensGene)
> txdb <- TxDb.Mmusculus.UCSC.mm10.ensGene
> txdb
TranscriptDb object:
| Db type: TranscriptDb
| Supporting package: GenomicFeatures
| Data source: UCSC
```

```csv
| Genome: mm10
| Organism: Mus musculus
| UCSC Table: ensGene
| Resource URL: http://genome.ucsc.edu/
| Type of Gene ID: Ensembl gene ID
| Full dataset: yes
| miRBase build ID: NA
| transcript_nrow: 94647
| exon_nrow: 348801
| cds_nrow: 226282
| Db created by: GenomicFeatures package from Bioconductor
| Creation time: 2014-03-17 16:22:04 -0700 (Mon, 17 Mar 2014)
| GenomicFeatures version at creation time: 1.15.11
| RSQLite version at creation time: 0.11.4
| DBSCHEMAVERSION: 1.0
> class(txdb)
[1] "TranscriptDb"
attr(,"package")
[1] "GenomicFeatures"
```

Loading TxDb.Mmusculus.UCSC.mm10.ensGene gives us access to a transcriptDb object with the same name as the package. The package name is quite long and would be a burden to type, so it’s conventional to alias it to txdb. When we look at the tran scriptDb object txdb, we get a lot of metadata about this annotation object’s version (how it was created, when it was created, etc.). Under the hood, this object simply represents a SQLite database contained inside this R package (we’ll learn more about these in Chapter 13). We don’t need to know any SQLite to interact with and extract data from this object; the GenomicFeatures package provides all methods we’ll need. This may sound a bit jargony now, but will be clear after we look at a few examples.

First, suppose we wanted to access all gene regions in Mus musculus (in this version of Ensembl annotation). There’s a simple accessor function for this, unsurprisingly named genes():

```snap
> mm_genes <- genes(txdb)
> head(mm_genes)
> head(mm_genes)
GRanges with 6 ranges and 1 metadata column:
        seqnames          ranges strand |       gene_id
            <Rle>           <IRanges> <Rle> | <CharacterList>
ENSMUSG00000000001    chr3 [108107280, 108146146]   - | ENSMUSG00000000001
ENSMUSG00000000003    chrX [ 77837901,  77853623]   - | ENSMUSG00000000003
ENSMUSG00000000028    chr16 [ 18780447,  18811987]   - | ENSMUSG00000000028
ENSMUSG00000000031    chr7 [142575529, 142578143]   - | ENSMUSG00000000031
ENSMUSG00000000037    chrX [161117193, 161258213]   + | ENSMUSG00000000037
ENSMUSG00000000049    chr11 [108343354, 108414396]   + | ENSMUSG00000000049
---
seqlengths:
        chr1                chr2 ...         chrUn_JH584304
        195471971               182113224 ...                 114452
```

```txt
> length(mm_genes)
[1] 39017
```

GenomicFeatures returns the data in a GRanges object, so all the tricks we’ve learned for working with GRanges can be used to work with this data.

Note that the GRanges object containing all mouse genes has 39,014 ranges. This includes coding genes, short noncoding genes, long noncoding genes, and pseudogenes—everything that comprises the entire ensGene track on UCSC (and all genes with an Ensembl gene identifier). It’s always a good idea to make sure you know what you’re getting with gene annotation; you should also validate that the totals make sense against an external source. For example, I’ve validated that the total number of genes is consistent with [Ensembl’s gene annotation summary page for mouse genome version mm10](http://bit.ly/ensembl-mouse).

GenomicFeatures has other functions for retrieving all transcripts, exons, coding sequences (CDS), and promoters—the functions transcripts(), exons(), cds(), and promoters(). Consult the documentation for this family of functions for extracting information from transcriptDb objects at help(transcripts).

It’s often more natural to work with a GRangesList object of these types of features grouped by some other type of feature than working with a massive GRanges list object of everything. For example, we might want to retrieve all exons grouped by transcript or gene:

```c
> mm_exons_by_tx <- exonsBy(txdb, by="tx")
> mm_exons_by_gn <- exonsBy(txdb, by="gene")
> length(mm_exons_by_tx)
[1] 94647
> length(mm_exons_by_gn)
[1] 39017
```

These functions that extract grouped features all take the transcriptDb object as their first argument and which type of feature to group by (e.g., gene, tx, exon, or cds) as their second argument. There are variety of these types of functions—for example, transcriptsBy(), exonsBy(), cdsBy(), intronsBy(), fiveUTRsByTranscript(), and threeUTRsByTranscript() (see help(transcriptsBy) for more information).

GenomicFeatures also provides functions for extracting subsets of features that overlap a specific chromosome or range. We can limit our queries to use a subset of chromosomes by setting which sequences our transcriptDb should query using the following approach:

```r
> seqlevels(txdb, force=TRUE) <- "chr1"
> chr1_exons <- exonsBy(txdb, "tx")
> all(unlist(seqnames(chr1_exons)) == "chr1")
[1] TRUE
> txdb <- restoreSeqlevels(txdb) # restore txdb so it queries all sequences
```

To extract feature data that only overlaps a specific region, use the following family of functions: transcriptsByOverlaps(), exonsByOverlaps(), and cdsByOverlaps() (see help(transcriptByOverlaps() for more information). For example, say a QTL study has identified a quantitative trait loci in the region roughly on chromosome 8, from 123,260,562 to 123,557,264. Our coordinates are rough, so we’ll add 10kbp. Recall that with IRanges, we grow ranges by a fixed number of bases by adding that number of bases to the object (from “Basic Range Operations: Arithmetic, Transformations, and Set Operations” on page 275); the same method is used to resize GRanges objects. So we can get all genes within this expanded region with:

> qtl\_region <- GRanges("chr8", IRanges(123260562, 123557264))
> qtl\_region\_expanded <- qtl\_region + 10e3
> transcriptsByOverlaps(txdb, qtl\_region\_expanded)

GRanges with 73 ranges and 2 metadata columns:

<table><tr><td rowspan="2"></td><td>seqnames</td><td colspan="2">ranges strand</td><td>tx_id</td><td>tx_name</td></tr><tr><td>&lt;Rle&gt;</td><td>&lt;IRanges&gt;</td><td>&lt;Rle&gt;</td><td>|integer&gt;</td><td>&lt;character&gt;</td></tr><tr><td>[1]</td><td>chr8 [119910841, 124345722]</td><td>+</td><td>|</td><td>47374</td><td>ENSMUST00000127664</td></tr><tr><td>[2]</td><td>chr8 [123254195, 123269745]</td><td>+</td><td>|</td><td>47530</td><td>ENSMUST00000001092</td></tr><tr><td>[3]</td><td>chr8 [123254271, 123257636]</td><td>+</td><td>|</td><td>47531</td><td>ENSMUST00000150356</td></tr><tr><td>[4]</td><td>chr8 [123254284, 123269743]</td><td>+</td><td>|</td><td>47532</td><td>ENSMUST00000156896</td></tr><tr><td>[5]</td><td>chr8 [123254686, 123265070]</td><td>+</td><td>|</td><td>47533</td><td>ENSMUST00000154450</td></tr><tr><td>...</td><td>...</td><td>...</td><td>... ...</td><td>...</td><td>...</td></tr><tr><td>[69]</td><td>chr8 [123559201, 123559319]</td><td>-</td><td>|</td><td>49320</td><td>ENSMUST00000178208</td></tr><tr><td>[70]</td><td>chr8 [123560888, 123561006]</td><td>-</td><td>|</td><td>49321</td><td>ENSMUST00000179143</td></tr><tr><td>[71]</td><td>chr8 [123562595, 123562713]</td><td>-</td><td>|</td><td>49322</td><td>ENSMUST00000178297</td></tr><tr><td>[72]</td><td>chr8 [123564286, 123564404]</td><td>-</td><td>|</td><td>49323</td><td>ENSMUST00000179019</td></tr><tr><td>[73]</td><td>chr8 [123565969, 123566087]</td><td>-</td><td>|</td><td>49324</td><td>ENSMUST00000179081</td></tr><tr><td>---</td><td></td><td></td><td></td><td></td><td></td></tr></table>

seqlengths:

| chr1 | chr2 ... | chrUn_JH584304 |
| --- | --- | --- |
| 195471971 | 182113224 ... | 114452 |

transcriptByOverlaps() returns all transcripts overlapping this range. All functions in this family also take a maxgap argument, which can be used to specify how large a gap between ranges is considered an overlap (0 by default). Setting the maxgap argument to 10kbp has the same effect as widening our ranges and then extracting ele ments as we did in the preceding example.

## Creating TranscriptDb Objects

If there isn’t a transcript annotation package containing a transcriptDb object for your organism, annotation track, or genome version of choice, GenomicFeatures provides a multitude of methods to create one. If the annotation track you’d like to use is on the UCSC Genome Browser or a BioMart (e.g., a data management system used by databases Ensembl and WormBase), GenomicFeatures contains the functions make TranscriptDbFromUCSC() and makeTranscriptDbFromBiomart() for creating transcriptDb from these databases. For some nonmodel systems, annotation only exists as a Gene Transfer Format (GTF) or Gene Feature Format (GFF) file. In this case, a transcriptDb object can be created with the makeTranscriptDbFromGFF() method. Once you’ve created a transcriptDb object using one of these methods, you can save the underlying SQLite database with saveDb() and load it again with loadDb(). As a demonstration of how easy this is, the following line downloads all required annotation data from Ensembl to create a transcriptDb object for Platypus:

```txt
> species <- "oanatinus_gene_ensembl"
> platypus_txdb <- makeTranscriptDbFromBiomart("ensembl", species)
```

Although creating transcriptDb directly and saving these objects as SQLite databases certainly works, GenomicFeatures makes it easy to create a transcript annotation package directly from tracks from the UCSC Genome Browser, Biomart, or from a transcriptDb object. See the functions makeTxDbPackageFromUCSC(), makeTxDbPack ageFromBiomart(), and makeTxDbPackage(), and [the GenomicFeatures vignette](http://bit.ly/genom-feat) or documentation for more detail on how to use these functions.

The transcriptDb objects and the methods provided by the GenomicFeatures package provide a consistent representation of transcript-based annotation and consistent functions for interacting with these objects. However, like everything in life, there are trade-offs. Convenience and consistency can come at the cost of flexibility. The rtracklayer package includes flexible functions for importing and exporting data that stores ranges from a variety of formats like GTF/GFF, BED, BED Graph, and Wiggle. These functions automatically convert entries to GRanges objects and handle technicalities like missing values and assigning columns in the file to metadata columns—features that general solutions like read.delim() don’t have. Let’s look at how the rtracklayer function import() loads the Mus\_musculus.GRCm38.75\_chr1.gtf.gz file (available on this book’s GitHub page):

```python
> mm_gtf <- import('Mus_musculus.GRCm38.75_chr1.gtf.gz')
> colnames(mcols(mm_gtf)) # metadata columns read in
[1] "source"          "type"           "score"
[4] "phase"            "gene_id"          "gene_name"
[7] "gene_source"      "gene_biotype"      "transcript_id"
[10] "transcript_name"   "transcript_source"  "tag"
[13] "exon_number"       "exon_id"          "ccds_id"
[16] "protein_id"
```

The function import() detects the file type (with hints from the file extension— another reason to use the proper extension) and imports all data as a GRanges object. There are also specific functions (e.g., import.bed(), import.gff(), import.wig(), etc.) that can you can use if you want to specify the format.

The rtracklayer package also provides export methods, for taking range data and saving it to a variety of common range formats. For example, suppose we wanted to write five random pseudogenes to a GTF file. We could use:

```txt
> set.seed(0)
> pseudogene_i <- which(mm_gtf\$gene_biotype == "pseudogene" &
 mm_gtf\$type == "gene")
> pseudogene_sample <- sample(pseudogene_i, 5)
> export(mm_gtf[pseudogene_sample], con="five_random_pseudogene.gtf",
 format="GTF")
```

If we didn’t care about the specifics of these ranges (e.g., the information stored in the metadata columns), the BED file format may be more appropriate. BED files require at a minimum three columns: chromosomes (or sequence name), start position, and end position (sometimes called the BED3 format). The easiest way to save only this information would be:

```r
> bed_data <- mm_gtf[pseudogene_sample]
> mcols(bed_data) <- NULL # clear out metadata columns
> export(bed_data, con="five_random_pseudogene.bed", format="BED")
```

Finally, it’s worth noting that we’re just scratching the surface of rtracklayer’s capabilities. In addition to its import/export functions, rtracklayer also interfaces with genome browsers like [UCSC’s Genome Browser](http://genome.ucsc.edu). Using rtracklayer, one can create tracks for UCSC’s browser directly from GRanges objects and send these to a UCSC Genome Browser web session directly from R. If you find yourself using the UCSC Genome Browser frequently, it’s worth reading [the rtracklayer vignette](http://bit.ly/rtracklayer) and learning how to interact with it through R.

## Retrieving Promoter Regions: Flank and Promoters

Now, let’s start seeing how the range operations in GenomicRanges can solve real bioinformatics problems. For example, suppose we wanted to grab the promoter regions of all protein-coding genes from the GRCh38 Mus musculus Ensembl GTF annotation track for chromosome 1 we loaded in using rtracklayer in the previous section. We’ll use this object rather than extracting genes from a transcriptDb object because it contains additional information about the type of transcript (such as the gene\_bio type and type columns we used in the previous section to find pseudogenes). So, first we could find the subset of genes we’re interested in—in this case, let’s say all protein coding genes:

> table(mm\_gtf\$gene\_biotype)

```txt
antisense          lincRNA         miRNA
    480            551           354
misc_RNA polymorphic_pseudogene processed_transcript
    93            61           400
protein_coding        pseudogene      rRNA
    77603            978           69
sense_intronic     sense_overlapping       snoRNA
    21            4           297
snRNA
```

```txt
315
> chr1_pcg <- mm_gtf[mm_gtf\$type == "gene" & ②
        mm_gtf\$gene_biotype == "protein_coding"]
> summary(width(chr1_pcg))
    Min. 1st Qu.   Median     Mean 3rd Qu.    Max.
      78    9429    25750    60640    62420 1076000
> length(chr1_pcg)
[1] 1240
> chr1_pcg_3kb_up <- flank(chr1_pcg, width=3000) ③
>
```

1 First, let’s do some basic EDA. We know we want to select protein coding genes, which we can do by subsetting the gene\_bioype column. Calling table() on it returns the number of features of each biotype. A full list of biotypes can be found on [the GENCODE website](http://bit.ly/gencode-bio). We see that there are around 78,000 features with the protein coding biotype.
Next, we can subset all features that have type “gene” (rather than exon, CDS, transcript, etc.) and biotype “protein\_coding.” As a sanity check, we make sure that the length distribution and number of features makes sense (remember, this is just chromosome 1 data).
Then, we can use flank to grab 3kbp upstream of each feature. Read help(flank) to refresh your memory of this method. You first question should be, “how does flank() handle strand?” Looking at the documentation, we see that by default flank() takes strand into consideration (option ignore.strand=FALSE), so we just specify the width of our flanking region. Note that our promoter regions are those defined from the start of our gene region to 3kbp upstream.

Extracting promoter regions is such a common operation that GenomicRanges packages have a convenience function to make it even simpler: promoters(). promoters() default arguments extract 3kbp upstream of each range, and 200bp downstream. For example, we could mimic our flank() call and show that the results are identical with:

```txt
> chr1_pcg_3kb_up2 <- promoters(chr1_pcg, upstream=3000, downstream=0)
> identical(chr1_pcg_3kb_up, chr1_pcg_3kb_up2)
[1] TRUE
```

## Retrieving Promoter Sequence: Connection GenomicRanges with Sequence Data

Once we’ve created promoter ranges using flank() (or promoters()), we can use these to grab the promoter nucleotide sequences from a genome. There are two different ways we could do this:

• Entirely through Bioconductor’s packages (as we’ll see in this section)
• By exporting the GenomicRanges objects to a range file format like BED, and using a command-line tool like BEDTools

Either method works, but the Bioconductor approach requires that genome sequences be stored in a special R package (similar to the annotation packages we encountered earlier). If your organism doesn’t have a premade genome package, it may be faster to write the promoter ranges to a file and use BEDTools. Because our example promoter regions are in mouse (a model organism), Bioconductor has a premade genome package we can download and use:

```txt
> library(BiocInstaller)
> biocLite("BSgenome")
# Note: this file is about 712MB, so be ensure you have enough
# disk space before installing!
> biocLite("BSgenome.Mmusculus.UCSC.mm10")
```

This is a BSgenome package, where BS stands for Biostrings, a Bioconductor package that contains classes for storing sequence data and methods for working with it. BSgenome packages contain the full reference genome for a particular organism, compressed and wrapped in a user-friendly package with common accessor methods. We’ll just scratch the surface of these packages in this section, so it’s definitely worth reading their vignettes on Bioconductor’s website.

Let’s first load the BSgenome.Mmusculus.UCSC.mm10 package and poke around:

```txt
> library(BSgenome.Mmusculus.UCSC.mm10)
> mm_gm <- BSgenome.Mmusculus.UCSC.mm10
> organism(mm_gm)
[1] "Mus musculus"
> providerVersion(mm_gm)
[1] "mm10"
> provider(mm_gm)
[1] "UCSC"
```

organisim(), providerVersion(), and provider() are all accessor functions to extract information from BSgenome packages.

We can use the accessor function seqinfo() to look at sequence information. BSgenome packages contain sequences for each chromosome, stored in a list-like structure we can access using indexing:

```perl
> seqinfo(mm_gm)
Seqinfo of length 66
seqnames        seqlengths isCircular genome
chr1            195471971       FALSE    mm10
chr2            182113224       FALSE    mm10
[...]
> mm_gm\$chrM
```

```txt
16299-letter "DNAString" instance
seq: GTTAATGTAGCTTAATAACAAAGCAAAGCACTGAAA...TCTAATCATACTCTATTACGCAATAAACATTAACAA
> mm_gm[[22]]
16299-letter "DNAString" instance
seq: GTTAATGTAGCTTAATAACAAAGCAAAGCACTGAAA...TCTAATCATACTCTATTACGCAATAAACATTAACAA
```

While we won’t go into this topic in detail, it’s worth mentioning that BSgenome objects can be searched using the string-matching and alignment functions in the Bio strings packages. These are meant for a few, quick queries (certainly not large-scale alignment or mapping!). For example:

```txt
> library(Biostrings)
> matchPattern("GGCGCGCC", mm_gm\$chr1)
  Views on a 195471971-letter DNAString subject
subject: NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN...NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
views:
```

```txt
start     end width
[1] 4557138 4557145    8 [GGCGCGCC]
[2] 4567326 4567333    8 [GGCGCGCC]
[3] 6960128 6960135    8 [GGCGCGCC]
[4] 7397441 7397448    8 [GGCGCGCC]
[5] 7398352 7398359    8 [GGCGCGCC]
```

Using these promoter regions and the Mus musculus promoter regions we created in the previous section, we’re ready to extract promoter sequences. Unfortunately, we need to adjust our promoter GRanges object first because the genome annotation file Mus\_musculus.GRCm38.75\_chr1.gtf.gz uses chromosome names like “1”, “2”, etc. while the BSgenome.Mmusculus.UCSC.mm10 package uses names like “chr1”, “chr2”, etc. Having to remap one chromosome naming scheme to another is quite a common operation as there is no standard chromosome naming scheme. Bioconductor provides some nice functions to make this as simple and safe as possible. We’ll see the problem, how to fix is manually, and how to fix it using convenience functions:

```txt
> all(seqlevels(chr1_pcg_3kb_up) %in% seqlevels(mm_gm)) ①
[1] FALSE
> gr <- GRanges(c("chr1", "chr2"), IRanges(start=c(3, 4), width=10)) ②
> seqlevels(gr)
[1] "chr1" "chr2"
> seqlevels(gr) <- c("1", "2") ③
> seqlevels(gr)
[1] "1" "2"

> seqlevelsStyle(chr1_pcg_3kb_up) ④
[1] "NCBI"
> seqlevelsStyle(mm_gm)
[1] "UCSC"
> seqlevelsStyle(chr1_pcg_3kb_up) <- "UCSC" ⑤
> all(seqlevels(chr1_pcg_3kb_up) %in% seqlevels(mm_gm))
[1] TRUE
```

0 First, always check that all sequences we want to grab are in the BSgenome object. Because the BSgenome.Mmusculus.UCSC.mm10 file uses the UCSC chromosome name style and our annotation file uses Ensembl/NCBI style, this is not the case.
Let’s create a test GRanges object so we can show how we can manually change chromosome names. Bioconductor packages treat sequence names much like the factors we saw in “Factors and classes in R” on page 191. We can access and set the names of these levels using the seqlevels() function.
Here, we change the sequence levels using seqlevels(). We provide the sequence level names in the same order as the original sequence levels.
④ Because having to switch between the style “chr1” (UCSC style) and “1” (Ensembl/NCBI style) is common, Bioconductor provides a convenience function seqlevelsStyle(). Here, we see that the style of chr1\_pcg\_3kb\_up is indeed “NCBI”.
Now, we set the style to “UCSC”. After (as demonstrated on the next line), the sequence levels are consistent between the two objects.

With our chromosome names consistent between our GRanges promoter regions and the mouse BSgenome package, it’s easy to grab the sequences for particular regions kept in a GRanges object:

```txt
> chr1_3kb_seqs <- getSeq(mm_gm, chr1_pcg_3kb_up)
> chr1_3kb_seqs
  A DNAStringSet instance of length 1240
    width seq
  [1]  3000 ATTCTGAGATGTGGTTACTAGATCAATGGGAT...CGGCTAGCCGGGCCCAGCGCCCAGCCCCGCGG
  [2]  3000 GAAGTGGTATATCTGCCTAGTCTAGGTGTGCA...GCTGTACTTAATCTGTGAGCACACATGCTAGT
  [3]  3000 CTTAAAAACCTAGATATTCTATTTTTTTTTTT...CTTTGATAACGTCGTGAGCTCGGCTTCCAACA
  [4]  3000 GAATTGGCACAGTTTCACATGATTGGTCCATT...GTACGGCCGCTGCAGCGCGACAGGGGCCGGGC
  [5]  3000 AAATATAAAGTTAACATACAAAAACTAGTCGC...TCGGGGCGCGAGCTCGGGGCCGAACGCGAGGA
  ...   ... ...
[1236]  3000 CAACATGGGTAGTAGTGGGGGAGCTTTAGTTC...GAGGGGCTGGCCTCACCAAGACGCAACAGGGA
[1237]  3000 AGGTGTGTTATATAATAATTGGTTTGACACTG...CTTAAAACTTGCTCTCTGGCTTCCTGGCGCCC
[1238]  3000 TTGGCCAGGTGATTGATCTTGTCCAACTGGAA...GTAAGGCCGGGCTATATGCAAACCGAGTTCCC
[1239]  3000 GGCATTCCCCTATACTGGGGCATAGAACCTTC...ATTTAAGGGTCTGCTCCCCACTGCTTACAGCC
[1240]  3000 GTAAATTTTCAGGTATATTTCTTTCTACTCTT...CTTTGATATTTCTGTGGTCCTTATTTCTAGGT
```

The method getSeq() takes a BSgenome object and a GRanges object, and returns the sequences for each range. We could then write these sequences to a FASTA file using:

```txt
> writeXStringSet(chr1_3kb_seqs, file="mm10_chr1_3kb_promoters.fasta",
format="fasta")
```

It’s worth mentioning that Bioconductor has many other packages for working with promoter sequences, extracting motifs, and creating sequence logo plots. This functionality is well documented in a detailed workflow on [the Bioconductor website](http://bit.ly/gene-binding).

## Getting Intergenic and Intronic Regions: Gaps, Reduce, and Setdiffs in Practice

As another example, let’s look at gaps() applied to GRanges objects. The gaps() method illustrates a rather important point about applying range operations to genomic data: we need to consider how range operations will work with strand and work across difference chromosomes/sequences. With IRanges, gaps were simple: they’re just the areas of a sequence with a range on them. With genomic ranges, gaps are calculated on every combination of strand and sequence. Here’s an example of this on a toy GRanges object so it’s clear what’s happening:

```txt
> gr2 <- GRanges(c("chr1", "chr2"), IRanges(start=c(4, 12), width=6),
                    strand=c("+", "-"), seqlengths=c(chr1=21, chr2=41))
> gr2 # so we can see what these ranges look like
GRanges with 2 ranges and 0 metadata columns:
    seqnames      ranges strand
        <Rle> <IRanges>  <Rle>
[1]     chr1  [ 4,  9]       +
[2]     chr2  [12, 17]       -
---
seqlengths:
    chr1 chr2
        21   41
> gaps(gr2)
GRanges with 8 ranges and 0 metadata columns:
    seqnames      ranges strand
        <Rle> <IRanges>  <Rle>
[1]     chr1  [ 1,  3]       +
[2]     chr1  [10, 21]       +
[3]     chr1  [ 1, 21]       -
[4]     chr1  [ 1, 21]       *
[5]     chr2  [ 1, 41]       +
[6]     chr2  [ 1, 11]       -
[7]     chr2  [18, 41]       -
[8]     chr2  [ 1, 41]       *
---
seqlengths:
    chr1 chr2
        21   41
```

That’s a lot of gaps—a lot more than we’d expect from two ranges! What’s going on? This function is dealing with the complexities of strands. When applied to GRanges, gaps() creates ranges for all sequences (chr1 and chr2 here) and all strands (+, -, and ambiguous strand \*). For sequence-strand combinations without any ranges, the gap spans the entire chromosome. GRanges does this because this is the safest way to return gaps: anything less would lead to a loss of information. If we just care about gaps irrespective of strand, we could take the original gr2 ranges, ditch strand information, and then create gaps with these (ignoring the gaps across entire chromosome-strand combinations):

```txt
> gr3 <- gr2
> strand(gr3) <- "*"
> gaps(gr3)[strand(gaps(gr3)) == "*"]
GRanges with 4 ranges and 0 metadata columns:
    seqnames   ranges strand
        <Rle> <IRanges>  <Rle>
[1]     chr1 [ 1,  3]      *
[2]     chr1 [10, 21]      *
[3]     chr2 [ 1, 11]      *
[4]     chr2 [18, 41]      *
---
seqlengths:
    chr1 chr2
        21   41
```

Replacing strand with the ambiguous strand \* is a common trick when we don’t care about keeping strand information. With gaps, we usually don’t care about the specifics of strand—we usually say a region is covered by a range, or it’s a gap.

Another approach to creating gaps using range operations is to use the set operations covered in “Basic Range Operations: Arithmetic, Transformations, and Set Operations” on page 275. A good illustration of the advantage of using set operations on GRanges objects is creating intergenic regions from all transcripts. This can be thought of as taking a set of ranges that represent entire chromosomes, and taking the set difference of these and all transcripts:

```txt
> chrom_grngs <- as(seqinfo(txdb), "GRanges") ①
> head(chrom_grngs, 2)
GRanges with 2 ranges and 0 metadata columns:
    seqnames      ranges strand
        <Rle>     <IRanges> <Rle>
chr1     chr1 [1, 195471971]      *
chr2     chr2 [1, 182113224]      *
---
seqlengths:
                  chr1            chr2 ...          chrUn_JH584304
                  195471971           182113224 ...          114452
> collapsed_tx <- reduce(transcripts(txdb)) ②
> strand(collapsed_tx) <- "*" ③
> intergenic <- setdiff(chrom_grngs, collapsed_tx) ④
```

First, we use the as() method to coerce the TranscriptDb object’s chromosome information (such as names, lengths, etc.) into a GRanges object representing the ranges for entire chromosomes. In general, Bioconductor packages include many helpful coercion methods through the as() method. As the next line demonstrates, the result of this is indeed a GRanges object representing entire chromosomes.

Next, we take all transcripts from our txdb TranscriptDb object and reduce them, so overlapping transcripts are collapsed into a single range. We collapse these overlapping ranges because we don’t care about the gaps between each transcript, but rather any region covered by a transcript (which is what reduce() returns).
As before, we ditch strand because we want all regions uncovered by a transcript on either strand.
4 Finally, we take the set difference between ranges representing an entire chromosome, and those that represent transcripts on those ranges. This leaves all regions without a transcript, which are the intergenic regions. Technically, this is a more inclusive set of intergenic ranges, as we’re saying a “gene” is any transcript, not just protein coding transcripts. This is yet another example where a common bioinformatics task can be easily accomplished with range operations and rangethinking. Try drawing the reduced transcript ranges and chromosome ranges out and seeing what setdiff() does to understand what’s going on.

Now, let’s look at how to create GRanges objects representing the introns of transcripts. We’re going to do this two ways: first, using a simple convenience function appropriately named intronsByTranscripts(), then using range set operations. The former method is simple and fast (it gives you a fish), while the latter method teaches you really important range manipulations that will allow you to solve many other range problems (it teaches you to fish). First, let’s consider the simple solution that uses the TranscriptDb object txdb we loaded earlier:

```txt
> mm_introns <- intronsByTranscript(txdb)
> head(mm_introns[['18880']]. 2) # get first two introns for transcript 18880
GRanges with 2 ranges and 0 metadata columns:
    seqnames             ranges strand
        <Rle>              <IRanges> <Rle>
[1]     chr3 [113556174, 113558092]   -
[2]     chr3 [113558219, 113558321]   -
---
seqlengths:
            chr1                chr2 ...     chrUn_JH584304
            195471971               182113224 ...         114452
```

We’ll now look at the manual approach that uses range set operations. This is a bit advanced, so if you’re feeling lost, you can skip ahead and come back to this later (but it does illustrate some awesome range manipulation tricks). We’ll make this example simpler by only creating the introns for a single gene, amylase 1 (which from the

Ensembl website has gene identifier ENSMUSG00000074264). The set operation approach we’ll take considers introns as the set difference between transcripts range and the exons’ ranges for these transcripts. Each set difference is computed pairwise between the exons of a particular transcript and the transcript’s range. Let’s first get the transcripts for the amylase 1 gene:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
&gt; amy1 &lt;- transcriptsBy(txdb, 'gene')$ENSMUSG00000074264
&gt; amy1
GRanges with 5 ranges and 2 metadata columns:
    seqnames                  ranges strand | tx_id        tx_name
        &lt;Rle&gt;              &lt;IRanges&gt; &lt;Rle&gt; | &lt;integer&gt;       &lt;character&gt;
[1]     chr3 [113555710, 113577830]   - |      18879 ENSMUST00000067980
[2]     chr3 [113555953, 113574762]   - |      18880 ENSMUST00000106540
[3]     chr3 [113556149, 113562018]   - |      18881 ENSMUST00000172885
[4]     chr3 [113562690, 113574272]   - |      18882 ENSMUST00000142505
[5]     chr3 [113564987, 113606699]   - |      18883 ENSMUST00000174147
---
seqlengths:
                   chr1                 chr2 ...         chrUn_JH584304
                   195471971               182113224 ...             114452
</div>

There are five transcripts in the amylase 1 gene that we need to create introns for. Each of these transcripts contains a different set of exons. We’ll extract all exons from the TranscriptDb object first, and then subset out the ones we need for these transcripts later:

```txt
> mm_exons <- exonsBy(txdb, "tx")
> mm_exons[[18881]]  # an example exon GRanges object to see what it looks like
GRanges object with 5 ranges and 3 metadata columns:
```

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
seqnames
&lt;Rle&gt;
        ranges strand | exon_id exon_name exon_rank
        &lt;IRanges&gt; &lt;Rle&gt; | &lt;integer&gt; &lt;character&gt; &lt;integer&gt;
[1]    chr3 [113561824, 113562018]   - | 68132 &lt;NA&gt; 1
[2]    chr3 [113561632, 113561731]   - | 68130 &lt;NA&gt; 2
[3]    chr3 [113558322, 113558440]   - | 68129 &lt;NA&gt; 3
[4]    chr3 [113558093, 113558218]   - | 68128 &lt;NA&gt; 4
[5]    chr3 [113556149, 113556173]   - | 68127 &lt;NA&gt; 5
</div>

seqinfo: 66 sequences (1 circular) from mm10 genome

mm\_exons contains all mouse exons, so we first need to extract only the exons belonging to our amylase 1 gene transcripts. A nice feature of GRangesList objects created by the split() method is that each list element is given the name of the vector used to split the ranges. Similarly, each list element created by exonsBy(txdb, "tx") is also named, using the transcript names (because we used by="tx"). Thus, we can easily match up our transcripts and exons by transcript identifiers, which are the element names of both the GRangesList objects amy1\_tx and mm\_exons. Matching these two GRangesList objects is then just a matter of using match():

> amy1\_exons <- mm\_exons[match(names(amy1\_tx), names(mm\_exons))]