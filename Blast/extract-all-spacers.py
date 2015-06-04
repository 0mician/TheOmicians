import os
import re
from collections import Counter

#### Specify file path ####
# pilerDir = file path of pilercr reports

pilerDir = "../CRISPR-Genomics/crispr/"
spacers_regex = re.compile('(?<=\.\.\.    )\w+')
file_out = open("reports/all-spacers.fasta", 'w')

### How many files to process?
number_of_files = len([name for name in os.listdir(pilerDir)])
i = 1

### Going trough all pilercr reports
for fn in os.listdir(pilerDir):
    ### Tracking progress
    print "Extracting spacers: %i out of %i" % (i, number_of_files)
    i += 1
    
    ### Obtain pilercr report and get all spacers
    piler_report = open(pilerDir + fn, 'r')
    piler_report = piler_report.read()
    spacers = re.findall(spacers_regex, piler_report)
	
    ### Creating output only if it has spacer(s)
    if spacers:
		### Removing ".txt" at the end
		fn = fn.split('.txt')[0]    
		j=1
    
		### Write '>' in each line followed by a Spacer in the line next line
		for spacer in spacers:
			file_out.writelines(">%s_%i\n" % (fn, j))
			file_out.writelines("%s\n" % (spacer))
			j += 1

file_out.close()
