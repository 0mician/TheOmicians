import re

f = open("filter_spacer_count.txt", "r")
a = open("sequence.gb")

spacercount = f.readlines()
annotation = a.read()

##### id_region {genomeid : start position of each filtered spacer} #####

id_region = {}

for line in spacercount:
	if bool(re.search('\w+(?=.txt)', line)):
		key = line.strip(".txt\n")
		id_region[key] = []
		continue
	else:
		value = re.findall('[0-9]{3,}', line)
		value = map(int, value)
		# value = re.findall('\[(.+)\]', line)
	for v in value:
		id_region[key].append(v)


##### Annotation #####

# get annotation only
# exclude genome sequence and information
annotation = annotation.split("FEATURES")[1].split("ORIGIN")[0].replace("\n                     ", "").split("\n")


# region_features{start position of feature : feature}
region_features = {}
for line in annotation:
	if bool(re.findall('\d+\.\.\d+', line)):
		key = re.findall('\d+(?=\.\.\d+)', line)[0]
		key = int(key)
		region_features[key] = line
	else:
		continue


##### Map region of interest to annotation #####

spacer_feature = {}
# for key in id_region:
for value in id_region['NC_021838']:
	for region in reversed(sorted(region_features)):
		if value > region:
			spacer_feature[value] = region_features[region]
			break

for key in spacer_feature:
	print key
	print spacer_feature[key]


f.close()
a.close()
