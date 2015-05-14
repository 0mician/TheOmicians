import os
import re
from difflib import get_close_matches, SequenceMatcher

##### Specify file path #####
# pilerIn = file path of input for pilerCR
# output = file path of output from pilerCR
# pilercrDir = file path of pilercr folder
# genomePath = file path of genome, function will look for spacers in this genome, FASTA format
 
pilerIn = "../ICP1.fasta"
pilerOut = "../output.txt"
pilercrDir = "/Users/yiminggan/Desktop/pilercr1.06"
genomePath = "/Users/yiminggan/Desktop/vpICP1_2011_A.fasta" 

##### Find CRISPR using pilercr #####
os.chdir(pilercrDir)
cmd = "./pilercr -in %s -out %s"%(pilerIn,pilerOut)
os.system(cmd) 


##### Get spacers from output.txt #####
report = open(pilerOut, 'r')
report = report.read()
spacers = re.findall('[ATCG]{30}', report)


##### Read genome #####
genome = open(genomePath,'r')

# Join genome in one string, removing first line
genome = genome.readlines()[1:]
genome = "".join(genome)
genome = genome.replace('\n', "")


##### Count spacer occurrence in genome #####
print "\n\nSpacers from: " + pilerIn
print "Genome from: " + genomePath
print "==================== RESULTS ====================\n"

for spacer in spacers:
	n = genome.count(spacer)
	print "Spacer: {}	Count: {}".format(spacer, n) 


##### Count loose match of spacer in genome #####
print "\n\nSequences similar to spacers\n"
print "************ Spacer ************ Match ************ Similarity ************"

for spacer in spacers:
	i = 0
	index = genome.find(spacer)
	interval = index + len(spacer)
	window = index - len(spacer)	
	
	for nucleotide in genome:
		i = i + 1
		if i < window or i > interval:
			seq = genome[i:i+window]
			match = SequenceMatcher(None, spacer, seq).ratio()
			if match > 0.80:
				print spacer + '\t' + seq + '\t' + str(match)
			else:
				continue
		else:
			continue

print "\t\t\t\t ***** END *****"
