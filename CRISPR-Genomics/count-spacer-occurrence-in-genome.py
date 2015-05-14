import os
import re

##### Specify file path #####
# pilerIn = file path of input for pilerCR
# output = file path of output from pilerCR
# pilercrDir = file path of pilercr folder
# genomePath = file path of genome, function will look for spacers in this genome, FASTA format
 
pilerIn = "../somesequence.fasta"
pilerOut = "../output.txt"
pilercrDir = "/somepath/pilercr1.06"
genomePath = "/somepath/somegenome.fasta" 


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
for spacer in spacers:
	n = genome.count(spacer)
	print "Spacer: {}	Occurrence: {}".format(spacer, n) 


##### Count loose match of spacer in genome #####
