# CRISPR-Genomics

## Introduction

    1. Get list of names of bacterias know to contain CRISPR regions (from crisprdb)
	list available here: http://crispr.u-psud.fr/crispr/ parsing it through scrip
    2. Download (automatically?) the genomes of these bacterias from NCBI
    3. Run pilercr on each genome and produce report on spacers 
    4. Go through the report and extract spacer sequences, save spacer sequences in 1 file per bacteria
    5. Go through files produced in step 4 and search for matches of spacer sequence in genome of bacteria (1 match at least from crispr -> interesting if more than 1 match)
    6. Go through matches and look at annotation for these regions
    7. If region not annotated, potential virus inserted in chromosomal dna?

## 1

The python script get-bacteria-links-from-cripsrdb.py connects to the website  http://crispr.u-psud.fr/crispr/ and retrieves all the links to individual baxterias' webpage. The output of that script is a text file: bacteria_links_crispr.txt which is fed to the next script

The python script run extract-refseq-from-crisprdb.py connects to each of the bacterias' pages and gets info on them, such as the reference genome studied, the genbank id, the number of CRISPR cluster found. The output of that script is a text file: bacteria_info_crisprdb.txt which is fed to the next script in Part 2.


