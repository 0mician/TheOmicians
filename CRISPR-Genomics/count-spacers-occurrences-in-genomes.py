import os
import re
from collections import Counter
from difflib import get_close_matches, SequenceMatcher

##### Specify file path #####
# pilerDir = file path of pilercr reports
# genomePath = file path of genome, function will look for spacers in this genome, FASTA format
# crisprHits = if multiple crispr spacers are found in a genome (outside of CRISPR region)

pilerDir = "crispr/"
genomePath = "genomes/" 
spacers_regex = re.compile('(?<=\.\.\.    )\w+')
report_out = open("spacer_count.txt", "w")

### How many files to process?
genomePath = "genomes/"
nb_genomes = len([name for name in os.listdir(genomePath)])
counter = 1

### Get spacers from output.txt 
for fn in os.listdir(pilerDir):
    ### Tracking progress
    print "Processing genome %i of %i" % (counter, nb_genomes)
    counter += 1

    ### Obtain pilercr report and get spacers
    report = open(pilerDir + fn, 'r')
    report = report.read()
    spacers = re.findall(spacers_regex, report)

    ### create dic with values as number of repetitions of a given spacer
    #spacers = list(set(spacers))
    count = Counter(spacers)
    #print type(count)

    ### Read genome associated with report
    g = open(genomePath + fn, 'r')
    genome = g.readlines()[1:]
    genome = "".join(genome)
    genome = genome.replace('\n', "")

    ### Count spacer occurrence in genome
    flag_file = False
    spacer_dic = {}
    for spacer in spacers:
        n = genome.count(spacer)
        if(n > 1 and len(spacer) > 15):
            if(flag_file == False):
                report_out.write(fn + "\n")
                flag_file = True
            spacer_dic[spacer] = n

    ### Filter out spacers that are repeated in the CRISPR regions
    for key in spacer_dic:   
        if (count[key] < spacer_dic[key]):
            report_out.write("Spacer: %s\tOccurrence: %i \n" % (key, spacer_dic[key]))
            
report_out.close()
 

##### Count loose match of spacer in genome #####
# print "\n\nSequences similar to spacers\n"
# print "************ Spacer ************ Match ************ Similarity ************"

# for spacer in spacers:
# 	i = 0
# 	index = genome.find(spacer)
# 	interval = index + len(spacer)
# 	window = index - len(spacer)	
	
# 	for nucleotide in genome:
# 		i = i + 1
# 		if i < window or i > interval:
# 			seq = genome[i:i+window]
# 			match = SequenceMatcher(None, spacer, seq).ratio()
# 			if match > 0.80:
# 				print spacer + '\t' + seq + '\t' + str(match)
# 			else:
# 				continue
# 		else:
# 			continue

# print "\t\t\t\t ***** END *****"

