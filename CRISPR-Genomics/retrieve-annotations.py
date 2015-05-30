import os 
import requests

inputReport = "reports/filter_spacer_count.txt"
outputFolder = "annotations/"
ncbi_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=%s&rettype=gbwithparts&retmode=text"

# Progress tracking
f = open(inputReport)
nb_seq = 0
for line in f:
    if(".txt" in line):
        nb_seq += 1

# Fetching the annotations
counter = 0
with open(inputReport, "r") as report:
    for line in report:
        if(".txt" in line):
            ref = line.rstrip(".txt\n")
            output_file = open( outputFolder + ref + ".txt" , "w")
            genome = requests.get(ncbi_url % ref, stream=True)
            output_file.write(genome.text)
            output_file.close()
            counter += 1
            print("%i out of %i: fetching annotation" % (counter, nb_seq))

report.close()
