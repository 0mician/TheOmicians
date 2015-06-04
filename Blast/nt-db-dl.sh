#!/bin/bash

DL_ADDRESS="ftp://ftp.ncbi.nlm.nih.gov/blast/db/"

mkdir nt-db && cd nt-db
curl $DL_ADDRESS$FILE_NAME"nt.[00-28].tar.gz" -O

mkdir /vagrant/Tools/ncbi-blast/db && tar zxvpf /vagrant/Blast/nt-db/*.tar.gz -C /vagrant/Tools/ncbi-blast/db/

rm -r /vagrant/Blast/nt-db
