#!/bin/sh

echo "Retrieving reads from NCBI"
curl "ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/ERR/ERR738/ERR738801/ERR738801.sra" -o ERR738801.sra
echo "Done\n\n"

echo "Converting to fastq"
../../fastq-dump.2.5.0 ERR738801.sra
echo "Done\n\n"

