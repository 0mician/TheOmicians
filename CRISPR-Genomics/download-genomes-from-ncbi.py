import requests
import re 

ncbi_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=fasta&retmode=text"
bacteria_info = open("bacteria_info_crisprdb.txt")
refseq = re.compile('(?<=RefSeq: )\w+')
counter = 1 # There are 5166 genomes to fetch

for line in bacteria_info:
    if("#####" in line):
        continue
        
    ref = re.search(refseq, line).group()

    output_file = open("genomes/" + ref + ".txt", "w")

    print("%i out of 5166: fetching genome of %s" % (counter, ref))
    genome = requests.get(ncbi_url % ref, stream=True)
    output_file.write(genome.text)
    output_file.close()
    counter += 1
