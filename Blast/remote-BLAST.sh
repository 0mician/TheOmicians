#!/bin/bash

export PATH="$PATH:/vagrant/Blast/ncbi-blast/bin"

blastn -remote -query reports/all-spacers-uniq.fasta -db nt -show_gis -out reports/blast_result_remote.txt
