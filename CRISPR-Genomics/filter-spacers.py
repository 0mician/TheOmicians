# Last modified: 28 May 2015
# Ming
import re
import os
import copy

pilerReportsPath = "crispr/"
spacerCountReport = "reports/spacer_count.txt"
genomesPath = "genomes_full/"
spacer_regex = re.compile('(?<=Spacer: )\w+')
occurence_regex = re.compile('\d+')
outputReport = "reports/filter_spacer_count.txt"

# This returns a dictionary, where each key is an integer representing the ith CRISPR region
# and each value is a list with the [start, end] of the region
def getCRISPRRegions(report):
    lst = report.split('SUMMARY BY POSITION')[1]
    lst = lst.split('\n')
    CRISPRregion = {}
    i = 1
        
    for line in lst:
        # pos = lines with [numbers][>= 1 space][numbers]
        pos = re.findall('[0-9]+(?:\s+|$)[0-9]+', line)
        if pos != []:
            a = re.split(" +",pos[0])
            CRISPRregion[i] = [int(a[0]), int(a[0]) + int(a[1])]
            i = i + 1
            
    return CRISPRregion

# Returns False if the position is outside of any CRISPR Region
def isInCrisprArray (pos, region):
    for array in region:
        # the +-1000 is a result of many false positive found in regions adjacent to the
        # crispr region as detected by pilercr (degenerate regions?)
        if(region[array][0] -1000 <= pos <= region[array][1] + 1000):
            return True
    return False

# Genome string
def getGenome(name):
    f =  open(genomesPath + name, "r")
    genome_temp = f.readlines()[1:]
    genome = "".join(genome_temp)
    genome = genome.replace("\n", "")
    return genome

# To keep track of progress, gets the number of blocks to analyze in spacer-count.txt
def getSizeReport():
    count = 0
    with open(spacerCountReport, 'r') as fp:
        for line in fp:
            if(line == "#####\n"):
                count += 1
    fp.close()
    return count


# Global variables 
flag_file = False
header = ""
spacerPos = {}
CRISPRregion = {}
genome = ""
out = open(outputReport, "w")
entries = getSizeReport()
tracking = 0

# Parses the spacer-count.txt report line by line
with open(spacerCountReport, 'r') as fp:
    for line in fp:
        # line is separator then reset variable
        if(line == "#####\n"):
            flag_file = True
            genome = ""
            CRISPRregion = {}
            spacerPos = {}
            tracking += 1
            print "Block %i out of %i processed" % (tracking, entries)
            continue

        # line is genome reference (eg NC_000961.txt)
        if(flag_file):
            header = line.rstrip()
            pilerFile = open(pilerReportsPath + header, "r")
            genome = getGenome(header)
            report_temp = pilerFile.read()
            CRISPRregion = getCRISPRRegions(report_temp)
            flag_file = False # do this only one per group of spacers (within same genome)
            continue

        # line is a spacer, and a report is loaded
        if(genome):      
            spacer = re.findall(spacer_regex, line)[0]
            occurence = re.findall(occurence_regex, line)[0]
            spacerPos[spacer] = [nucleotide.start()+1 for nucleotide in re.finditer(spacer, genome)]
            temp = copy.deepcopy(spacerPos)
            for position in spacerPos[spacer]:
                if(isInCrisprArray(position, CRISPRregion)):
                    temp[spacer].remove(position)
            if(len(temp[spacer]) > 0):
                if (header):
                    out.write(header + "\n")
                    header = ""
                out.write("Spacer: " + spacer + "\tOccurence: " + str(len(temp[spacer])) + "\t positions:" + str(temp[spacer]) + "\n")
fp.close()
out.close()
