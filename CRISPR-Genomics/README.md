# CRISPR-Genomics

## Introduction

    1. Get list of names of bacterias know to contain CRISPR regions (from crisprdb)
	list available here: http://crispr.u-psud.fr/crispr/ parsing it through script, eliminating "questionable structure" for now
    2. Download (automatically?) the genomes of these bacterias from NCBI
    3. Run pilercr on each genome and produce report on spacers 
    4. Go through the report and extract spacer sequences, save spacer sequences in 1 file per bacteria
    5. Go through files produced in step 4 and search for matches of spacer sequence in genome of bacteria (1 match at least from crispr -> interesting if more than 1 match)
    6. Go through matches and look at annotation for these regions
    7. If region not annotated, potential virus inserted in chromosomal dna?

## 1

The python script get-list-bacterias.py connects to the website  http://crispr.u-psud.fr/crispr/ and retrieves all the names of bacterias

