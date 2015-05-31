import re

f = open("reports/filter_spacer_count.txt", "r")

spacercount = f.readlines()
outputAnnotation = open("reports/annotated_hits.txt", "w")

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

size = len(id_region)
count = 1

for key in id_region:
    # keeping track of progress
    print("Processing entry %i out of %i\n" % (count, size))
    count += 1

    # parsing annotation file
    outputAnnotation.write(str(key) + "\n")
    annotation_file = open("annotations/"+key+".txt", "r")
    annotation = annotation_file.read()
    annotation = annotation.split("FEATURES")[1].split("ORIGIN")[0].replace("\n                     ", "").split("\n")

    # region_features{start position of feature : feature}
    region_features = {}
    for line in annotation:
        if bool(re.findall('\d+\.\.\d+', line)):
            start = re.findall('\d+(?=\.\.\d+)', line)[0]
            stop = re.findall('(?<=\.\.)\d+', line)[0]
            start = int(start)
            stop = int(stop)
            region_features[start] = [stop, line]
        else:
            continue

    spacer_feature = {}
    # for key in id_region:
    for value in id_region[key]:
        for region in reversed(sorted(region_features)):
            if value > region :
                if value < region_features[region][0]:
                    spacer_feature[value] = region_features[region][1]
                else:
                    spacer_feature[value] = "Not annotated\n"
                break
                
    for a in spacer_feature:
        outputAnnotation.write(str(a) + "\n")
        line = spacer_feature[a].split("/")
        line = "\n\t".join(line)
        outputAnnotation.write(line + "\n\n")
    annotation_file.close()

f.close()
