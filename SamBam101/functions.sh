#!/bin/bash

PATH_TOOLS=/vagrant/Tools

# params: input_fastq output_fastq trim_from trim_to
function trimming() {
    echo "Trimming"
    $PATH_TOOLS/fastx_trimmer -i $1 -o $2 -f $3 -l $4 -Q33
    echo "Done"
}

# params: reference_genome fastq_file output_aln_fastq
function bwa_align() {
    echo "Creation of bwa alignment"
    $PATH_TOOLS/bwa aln $1 $2 -f $3
    echo "Done"
}

# params: reference_genome aln_fastq trimmed_fastq output_sam
function sam_creation(){
    echo "Creation of sam file"
    $PATH_TOOLS/bwa samse $1 $2 $3 -f $4
    echo "Done"
}

# params: reference_genome aln_fastq1 aln_fastq2 trimmed_fastq1 trimmer_fastq2  output_sam
function sam_creation_pe(){
    echo "Creation of sam file"
    $PATH_TOOLS/bwa sampe $1 $2 $3 $4 $5 -f $6
    echo "Done"
}

# params: input_sam output_bam output_sorted output_sorted_bam
function bam_creation(){
    echo "Samtools to bam, sort, index"
    $PATH_TOOLS/samtools view -Sb -o $1 $2
    $PATH_TOOLS/samtools sort $1 $3
    $PATH_TOOLS/samtools index $4
    echo "Done"
}

# params: sorted_bam_input
function bam_stats() {
    echo "Samtools bam flagstat"    
    $PATH_TOOLS/samtools flagstat $1
    echo "Done"
}

# params: sra_input
function convert_sra_fastq() {
    echo "Converting to fastq"
    $PATH_TOOLS/fastq-dump.2.5.0 $1
    echo "Done"
}

# params: sra_input
function convert_sra_fastq_pe() {
    echo "Converting to fastq"
    $PATH_TOOLS/fastq-dump.2.5.0 -I --split-3 $1
    echo "Done"
}

# params: rest_get_adress reference_fasta_output 
function dl_ncbi() {
    echo "Retrieving reads from NCBI"
    curl $1 -o $2
    echo "Done"
}

# params: reference_fasta_input
function generate_bwa_index() {
    echo "Generating BWA index"
    $PATH_TOOLS/bwa index -a bwtsw $1
    echo "Done" 
}

# params: reference_fasta_input 
function generate_fasta_index() {
    echo "Generating fasta file index"
    $PATH_TOOLS/samtools faidx $1
    echo "Done" 
}

# params: reference_fasta_input reference_dic_output
function generate_seq_dic() {
    echo "Generating sequence Dictionary"
    java -jar $PATH_TOOLS/picard.jar CreateSequenceDictionary REFERENCE=$1 OUTPUT=$2
    echo "Done" 
}



