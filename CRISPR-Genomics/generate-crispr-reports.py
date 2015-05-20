import os

##### Specify file path #####
# output = file path of output for pilercr reports
# genomePath = file path of genome, function will look for spacers in this genome, FASTA format

pilerOut = "crispr/%s"
genomePath = "genomes_full/"
number_of_files = len([name for name in os.listdir(genomePath)])
i = 1

##### Find CRISPR using pilercr #####
for fn in os.listdir(genomePath):
    print "Generating report %i out of %i" % (i, number_of_files)
    cmd = "/vagrant/pilercr1.06/pilercr -in %s -out %s"%(genomePath + fn,pilerOut % fn)
    os.system(cmd + "> /dev/null 2>&1") 
    i += 1
