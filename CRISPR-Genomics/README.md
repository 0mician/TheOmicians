# CRISPR-Genomics

## Introduction

For the Genomics analysis pipeline, we decided to implement the following steps:

1. Get list of names of bacterias know to contain CRISPR regions (from
crisprdb](http://crispr.u-psud.fr/crispr/) parsing it through script
(no API unfortunately)
2. Download (automatically?) the genomes of these bacterias from NCBI.
3. Run pilercr on each genome and produce report on spacers.
4. Go through the report and extract spacer sequences, save spacer
sequences in 1 file per bacteria.
5. Go through files produced in step 4 and search for matches of
spacer sequence in genome of bacteria (1 match at least from crispr,
hence interesting if more than 1 match)
6. Go through matches and look at annotation for these regions 
7. If region not annotated, potential virus inserted in chromosomal
dna.

## 1 Retrieval of the information on the bacterias of interest

The python script *get-bacteria-links-from-cripsrdb.py* connects to
[crisprdb](http://crispr.u-psud.fr/crispr/) and retrieves all the
links to individual baxterias' webpage. The output of that script is a
text file: *bacteria_links_crispr.txt* which is fed to the next script

The python script *extract-refseq-from-crisprdb.py* connects to each
of the bacterias' individual pages and gets info on them, such as the
reference genome studied, the genbank id, the number of CRISPR cluster
found. The output of that script is a text file:
*bacteria_info_crisprdb.txt* which is fed to the next script in Part 2.

## 2 Downloading of the genomes of bacterias

The python script *download-genomes-from-ncbi.py* makes use of the
REST API of NCBI (Entrez) to download each genomes into a local
file. There are about 5200 of them, amounting to a total of 10 Gb of
genomic information. Make sure that you have enough room to save them.

### Note

You can avoid this step (and spare NCBI's servers) by downloading the
archive (compressed to 2.5gb) from [this
address](https://altersid.net/owncloud/index.php/s/d4GhPsbQ3a2wNfO). The
corresponding sha1sum is:

```
> sha1sum genomes_full.tar.bz2
acff7aa9d6fb29977f1471640a901c42a8d98237  genomes_full.tar.bz2
```

## 3 Generation of reports on CRISPR

The python script *generate-crispr-reports.py* makes use of the crispr
tool to produce one file/report per bacteria in the *genomes*
folder. The reports are output to the *crispr* folder.

  
## 4 Analysis of the reports

The python script *count-spacers-occurences-in-genomes.py* parses the
crispr reports to search for repeats of spacers in non-crispr regions
of the genomes. At the moment, it ignores spacers that are too short 
15 nucleotides). There is a lot of result, probably need to add a filtering
step.

## 5 and more

**In Progress**
