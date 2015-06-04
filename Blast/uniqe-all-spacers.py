import re

sequence_regex = re.compile('[(A|T|C|G)]+\n')
refseq_regex = re.compile('\w\w_.*')
all_spacers = open("reports/all-spacers.fasta", 'r')
all_spacers_uniq = open("reports/all-spacers-uniq.fasta", 'w')
all_spacers = all_spacers.read()

### Obtain all spacers
spacers = re.findall(sequence_regex, all_spacers)
ids = re.findall(refseq_regex, all_spacers)


### Build a dictionary of all found spacers {spacer: uniqe_key}
#	uniq_key is the index to uniq_spacers_ids with all ids of a particular spacer
uniq_spacers = {}
uniq_spacers_ids = []
i = 0
print "Creating a unique list of all spacers"
while i<len(spacers):
	if spacers[i] in uniq_spacers:
		uniq_spacers_ids[uniq_spacers[spacers[i]]] += " | %s" % (ids[i])
	else:
		uniq_spacers_ids.append(">%s" % (ids[i]))
		uniq_spacers[spacers[i]] = len(uniq_spacers_ids)-1
	i += 1

counter = 1
for item in uniq_spacers:
	all_spacers_uniq.writelines("%s\n%s" % (uniq_spacers_ids[uniq_spacers[item]], item))
	counter += 1

print "Done!"

all_spacers_uniq.close()
