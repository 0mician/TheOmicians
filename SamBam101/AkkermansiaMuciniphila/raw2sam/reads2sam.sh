#!/bin/sh

echo "Trimminh"
../../fastx_trimmer -i SRR073383.fastq -o SRR073383.trim.fastq -f 10 -l 100 -Q33
echo "Done\n\n"

echo "Creation of bwa alignment"
../../bwa aln ../reference/sequence.fasta SRR073383.fastq -f SRR073383.ref.fastq.aln
echo "Done\n\n"

echo "Creation of sam file"
../../bwa samse ../reference/sequence.fasta SRR073383.ref.fastq.aln SRR073383.fastq -f SRR073383.sam
echo "Done\n\n"

echo "Samtools to bam, sort, index && flagstat"
../../samtools view -Sb -o SRR073383.bam SRR073383.sam
../../samtools sort SRR073383.bam SRR073383.sorted
../../samtools index SRR073383.sorted.bam
../../samtools flagstat SRR073383.sorted.bam
echo "Done\n\n"
