#!/bin/sh

echo "Trimminh"
../../fastx_trimmer -i ERR738801.fastq -o ERR738801.trim.fastq -f 10 -l 100 -Q33
echo "Done\n\n"

echo "Creation of bwa alignment"
../../bwa aln ../reference/sequence.fasta ERR738801.fastq -f ERR738801.ref.fastq.aln
echo "Done\n\n"

echo "Creation of sam file"
../../bwa samse ../reference/sequence.fasta ERR738801.ref.fastq.aln ERR738801.fastq -f ERR738801.sam
echo "Done\n\n"

echo "Samtools to bam, sort, index && flagstat"
../../samtools view -Sb -o ERR738801.bam ERR738801.sam
../../samtools sort ERR738801.bam ERR738801.sorted
../../samtools index ERR738801.sorted.bam
../../samtools flagstat ERR738801.sorted.bam
echo "Done\n\n"
