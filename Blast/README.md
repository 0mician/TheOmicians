# BLAST

In this section, we will run a BLAST on all obtained spacers, using NCBI BLAST+ command line program available at [here](ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)to see if we can map the spacers back to phages and plasmids which their full genomes are available in NCBI nucleotide database.
First we will download BLAST+ and the Nucleotide BLAST database, then we will extract spacers from pilercr reports and finally run a BLAST.

## 1.BLAST+ setup

To start run
```
$ vagrant up
$ vagrant ssh
$ cd /vagrant/Blast/
```
### 1.1.BLAST+ program download

The following script will download the latest version of BLAST+ from NCBI and extract it in /Tools directory:
(Alternatively you can do it manually and place it in /Tools/ncbi-blast )

```
$ chmod +x BLAST-setup.sh
$ ./BLAST-setup.sh
```

### 1.2.Nucleotide BLAST database download

Now we need to download nucleotide BLAST database from [here](ftp://ftp.ncbi.nlm.nih.gov/blast/db/).
This database is about 16GB, so make sure that you have enough space.
The following script will download nucleotide BLAST database and extract it to /Tools/ncbi-blast/db/
(If you don't have enough space, you can also run BLAST remotely)

```
$ chmod +x nt-db-dl.sh
$ ./nt-db-dl.sh
```

## 2.Obtaining spacers from pilercr reports

The python script *extract-all-spacers.py* will extract all found spacers from pilercr reports. Then by running *uniqe-all-spacers.py* pyhton script, we will obtain a unique list of all spacers which is appropriate for running BLAST.

## 3.Run BLAST

In order to use the BLAST+ program, the PATH and BLASTDB environment variables need to be modified and specified respectively.
The following script, will modify and specify environment variables and then will run the BLAST using blastn tool from BLAST+ program.
Since we have a big query, this job would take as long as several hours, so be patient!

```
$ chmod +x local-BLAST.sh
$ ./local-BLAST.sh
``` 
BLAST reports would be saved in /Blast/reports as a text file.

### Note:
You can alternatively run a remote BLAST using the *remote-BLAST.sh* script.
However because of our big query it's prone to network failures and would take much longer than local BLAST.

## 4.Analysis of the BLAST report

Finally using "GNU Grep" we can obtain some stats from BLAST report:

```
$ grep phage blast_result_local.txt | grep '>'|wc -l
$ grep plasmid blast_result_real_local.txt | grep '>'|wc -l
```

### A complete tutorial on BLAST+ setup could be found [here](http://www.ncbi.nlm.nih.gov/books/NBK52640/)