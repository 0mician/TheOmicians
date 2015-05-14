import os
import re

##### Specify file path #####
# pilerIn = file path of input for pilerCR
# output = file path of output from pilerCR
# pilercrDir = file path of pilercr folder
# genomePath = file path of genome, function will look for spacers in this genome, FASTA format
 
pilerDir = "crispr/"
pilerOut = "crispr/%s"
genomePath = "genomes/" 
crisprHits = "crispr-hits/"
spacers_regex = re.compile('(?<=\.\.\.    )\w+')

##### Find CRISPR using pilercr #####
for fn in os.listdir(genomePath):
        cmd = "pilercr -in %s -out %s"%(genomePath + fn,pilerOut % fn)
        os.system(cmd) 

##### Get spacers from output.txt #####
for fn in os.listdir(pilerDir):
        report = open(pilerDir + fn, 'r')
        report = report.read()
        spacers = re.findall(spacers_regex, report)
        ##### Read genome #####
        g = open(genomePath + fn, 'r')
        print fn
        genome = g.readlines()[1:]
        genome = "".join(genome)
        genome = genome.replace('\n', "")
        ##### Count spacer occurrence in genome and save output #####
        for spacer in spacers:
                n = genome.count(spacer)
                print "Spacer: %s\tOccurrence: %i" % (spacer, n) 

