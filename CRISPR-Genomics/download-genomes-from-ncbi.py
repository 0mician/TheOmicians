import requests
import re 

ncbi_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=fasta&retmode=text"
bacteria_info = open("bacteria_info_crisprdb.txt")
refseq = re.compile('(?<=RefSeq: )\w+')

### Quick count of the total number of sequences to fetch
f = open("bacteria_info_crisprdb.txt")
nb_seq = 0
for line in f:
    if(line != "#####\n"):
        nb_seq += 1
counter = 1

for line in bacteria_info:
    if("#####" in line):
        continue        
    ref = re.search(refseq, line).group()
    output_file = open("genomes/" + ref + ".txt", "w")
    print("%i out of %i: fetching genome of %s" % (counter, nb_seq, ref))
    genome = requests.get(ncbi_url % ref, stream=True)
    output_file.write(genome.text)
    output_file.close()
    counter += 1
