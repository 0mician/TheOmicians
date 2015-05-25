#!/bin/sh

echo "Retrieving sequence from NCBI"
curl -s "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=187734516&rettype=fasta&retmode=txt" > sequence.fasta
echo "Done\n\n"

echo "Generating BWA index"
../../bwa index -a bwtsw sequence.fasta
echo "Done\n\n"

echo "Generating fasta file index"
../../samtools faidx sequence.fasta
echo "Done\n\n"

echo "Generating sequence Dictionary"
java -jar ../../picard.jar CreateSequenceDictionary REFERENCE=sequence.fasta OUTPUT=sequence.dict
echo "Done\n\n"
