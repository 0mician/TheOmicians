#!/bin/bash

DL_ADDRESS="ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/"

FILE_NAME=`curl -s $DL_ADDRESS | grep x64-linux.tar.gz |awk -F" " '{print $9;}'`

curl $DL_ADDRESS$FILE_NAME -o ../Tools/ncbi-blast.tar.gz

mkdir ../Tools/ncbi-blast && tar zxvpf ../Tools/ncbi-blast.tar.gz -C ../Tools/ncbi-blast --strip-components  1
