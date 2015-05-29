#!/bin/bash

DL_ADDRESS="http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=148642060&rettype=fasta&retmode=txt"
FUNCTION_FILE=../../functions.sh

if [[ -f $FUNCTION_FILE ]]; then
    . $FUNCTION_FILE
fi

if [ $# -lt 1 ]
then
    echo "Usage : $0 [clean | all | dlref | prepref]"
    exit
fi

case "$1" in

    "clean") 
        echo "cleaning up the folder"
        find ! -name 'prepare_ref.sh' -and ! -name '.gitignore' -type f -exec rm -f {} +
        ;;
    "all")
        echo "Starting from scratch"
        dl_ncbi $DL_ADDRESS $PWD/sequence.fasta
        generate_bwa_index sequence.fasta
        generate_fasta_index sequence.fasta
        generate_seq_dic sequence.fasta sequence.dict
        ;;
    "dlref")
        dl_ncbi $DL_ADDRESS $PWD/sequence.fasta
        ;;
    "prepref")
        echo "generating sam bam and extra files from fastq"
        generate_bwa_index sequence.fasta
        generate_fasta_index sequence.fasta
        generate_seq_dic sequence.fasta sequence.dict
        ;;
    *)
        echo "Usage : $0 [clean | all | dlref | prepref]"
        exit
        ;;
esac

