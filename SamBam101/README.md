# SamBam101

In this section, we will go through one of the required step of our
project, which is to show mastery of the
[Sam/Bam](https://samtools.github.io/hts-specs/SAMv1.pdf) tools and
files for sequence alignment.

# The victims

We conducted the analysis on 4 different bacterias, which were advised to us by one of our teacher, due to their implication in the human gut flora. The bacterias are:

- [Methanobrevibacter Smithii](https://en.wikipedia.org/wiki/Methanobrevibacter_smithii)
- [Bacteroides Fragilis](https://en.wikipedia.org/wiki/Bacteroides_fragilis)
- [Faecalibacterium Prausnitzii](https://en.wikipedia.org/wiki/Faecalibacterium_prausnitzii)
- [Akkermansia Muciniphila](https://en.wikipedia.org/wiki/Akkermansia_muciniphila)

For all these bacterias, the full analysis described below was performed. We'll limit the examples to one, as the others are very similar and can be reproduced easily.

# Methanobrevibacter Smithii

## Reference Genome and Preparation of the files for mapping

This [NCBI page](http://www.ncbi.nlm.nih.gov/genome/genomes/821) reveals that a reference genome is available, for which the fasta file can be obtained. 

To automate the processing of retrieving the sequence, and the preparation of the genome for subsequent "mapping to reference" analysis, the script **prep_reference.sh** has been prepared:

```
$ vagrant up
$ vagrant ssh
$ cd /vagrant/SamBam101/MethanobreVibacterSmithii/reference/
$ chmod +x prepare_ref.sh
$ ./prepare_ref.sh all
```

The script has different options which can be displayed by omiting the argument:

```
$ ./prepare_ref.sh
Usage : ./prepare_ref.sh [clean | all | dlref | prepref]
```

The option 'all' will successively:

1. download the reference genome from NCBI (through Entrez REST API)
2. generate the burrows-wheeler index
3. generate the fasta file index
4. generate the sequence dictionary

The option 'clean' will remove all files in the directory to start from scratch.
The option 'dlref' will only proceed to download the genome (step 1).
The option 'prepref' will proceed with the generation of the misc. files (step 2-3-4)

## Raw reads

Once the reference genome is ready, a set of raw reads (from a different sequencing project) was selected. The one used here was downloaded from the [SRA Database](http://www.ncbi.nlm.nih.gov/sra/?term=Methanobrevibacter+smithii). Attention was put on a selecting a Whole Genome Sequencing project, with decent metrics (nb of reads, size of reads, ...). [This link](http://www.ncbi.nlm.nih.gov/sra?term=SRP001946) will show you the selected project, and the archive file can downloaded [here](ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR036/SRR036257).

To automate the process of generating the SAM/BAM files, and the download of the project reads, the script **reads2sam.sh** was created :

```
$ vagrant up 
$ vagrant ssh
$ cd /vagrant/SamBam101/MethanobreVibacterSmithii/raw2sam/
$ chmod +x reads2sam.sh
$ ./reads2sam.sh all
```

The script has similar options to the one mentioned above, which can be listed by omiting the argument:

```
$ ./reads2sam.sh
Usage : ./reads2sam.sh [clean | all | dl2fastq | sambam | stats]
```

The option "all" will go through the following steps:

1. Downloading the SRA file from NCBI (these can be quite large)
2. Dump the SRA into a fastq file (or 2 fastq file if the sequencing was "paired end")
3. Trimming the sequence based on the quality of the reads (see section "Analysis of the quality of the reads")
4. Finding the Suffix Array (SA) coordinates of the reads
5. Conversion of the SA to chromosome position and creation of SAM file
6. Creation of the BAM file and associated files
7. Retrieval of statistics on the quality of the alignment.

### Analysis of the quality of the reads

Before running the script, one should decide on the cutoff values of the reads based on the quality metrics. For this, FastQC can be used. We used the following information to set our cutoff values from 10 to 100:

![QC before trimming reads](https://raw.githubusercontent.com/Milt0n/TheOmicians/master/SamBam101/img/QCBefore.png)

Which resulted in the following QC report:

![QC after trimming reads](https://raw.githubusercontent.com/Milt0n/TheOmicians/master/SamBam101/img/QCAfter.png)
