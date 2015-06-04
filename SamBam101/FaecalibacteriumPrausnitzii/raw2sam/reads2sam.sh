#!/bin/bash

FUNCTION_FILE=../../functions.sh
FILE=$PWD/SRR089473
REF=../reference/sequence.fasta
DL_ADDRESS="ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR275/SRR275650/SRR275650.sra"

if [[ -f $FUNCTION_FILE ]]; then
    . $FUNCTION_FILE
fi

if [ $# -lt 1 ]
then
    echo "Usage : $0 [clean | all | dl2fastq | sambam | stats]"
    exit
fi

function getData() {
    dl_ncbi $DL_ADDRESS $FILE.sra
    convert_sra_fastq $FILE.sra
}

function processData() {
        trimming $FILE.fastq $FILE.trim.fastq 10 100
        bwa_align $REF $FILE.trim.fastq $FILE.ref.fastq.aln
        sam_creationb $REF $FILE.ref.fastq.aln $FILE.trim.fastq $FILE.sam
        bam_creation $FILE.bam $FILE.sam $FILE.sorted $FILE.sorted.bam 
        bam_stats $FILE.sorted.bam
}

case "$1" in

    "clean") 
        echo "cleaning up the folder"
        find ! -name 'reads2sam.sh' -and ! -name '.gitignore' -type f -exec rm -f {} +
        ;;
    "all")
        echo "Starting from scratch"
        getData
        processData
        ;;
    "dl2fastq")
        echo "Downloading from NCBI and converting to fastq"
        getData
        ;;
    "sambam")
        echo "generating sam bam and extra files from fastq"
        processData
        ;;
    "stats")
        bam_stats $FILE.sorted.bam
        ;;
    *)
        echo "Usage : $0 [clean | all | dl2fastq | sambam | stats]"
        exit
        ;;
esac
