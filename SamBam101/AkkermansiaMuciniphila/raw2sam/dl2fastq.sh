#!/bin/sh

echo "Retrieving reads from NCBI"
curl "ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR073/SRR073383/SRR073383.sra" -o SRR073383.sra
echo "Done\n\n"

echo "Converting to fastq"
../../fastq-dump.2.5.0 SRR073383.sra
echo "Done\n\n"

