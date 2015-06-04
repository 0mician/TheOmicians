#!/bin/bash

export PATH="$PATH:/vagrant/Tools/ncbi-blast/bin"
export BLASTDB="/vagrant/Tools/ncbi-blast/db"

blastn -query reports/all-spacers-uniq.fasta -db nt -show_gis -out reports/blast_result_local.txt
