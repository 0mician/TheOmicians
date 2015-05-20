import os
import re

##### Specify file path #####
# output = file path of output for pilercr reports
# genomePath = file path of genome, function will look for spacers in this genome, FASTA format

pilerOut = "crispr/%s"
genomePath = "genomes/" 

##### Find CRISPR using pilercr #####
for fn in os.listdir(genomePath):
        cmd = "/vagrant/pilercr1.06/pilercr -in %s -out %s"%(genomePath + fn,pilerOut % fn)
        os.system(cmd) 
