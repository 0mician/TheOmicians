import re

# substring = spacer to look for in the genome
# file = sequence of genome in ONE string, excluded first line of fasta file
substring = "TAACCTTAAGCGGGAGGGAACTTGTTGAGTTCATAAGGG"
file = open("NC000961-string.txt","r")


genome = file.read()

print substring + '\t\t' + "Position:" + str([nucleotide.start()+1 for nucleotide in re.finditer(substring, genome)]) + '\n'

file.close()