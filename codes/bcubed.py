#!/usr/bin/python
import sys

#-------------------------------

# Parse arguments
resultFile = sys.argv[1]
truthFile = sys.argv[2]

# Initialize other variables
rFile = []
rDataList = {}
rCluster = []
tDataList = {}
tCluster = []

precision = 0.0
recall = 0.0

#-------------------------------

# Read in data from the clustering output file
with open(resultFile) as file:
	line = file.readline()
	line = file.readline()

	n = int( file.readline().strip() )
	for i in range(0, n+1):
		rCluster.append([])

	for line in file:
		line = line.strip()

		pos = line.find(",")
		pos = line.find(",", pos+1)
		rFile.append( line[0:pos] )
		rDataList[ line[0:pos] ] = int( line[pos+1:] )
		rCluster[ int( line[pos+1:] ) ].append( line[0:pos] )

#-------------------------------

# Read in data from the ground truth file
with open(truthFile) as file:
	line = file.readline()

	n = int( file.readline().strip() )
	for i in range(0, n+1):
		tCluster.append([])

	for line in file:
		line = line.strip()

		pos = line.find(",")
		pos = line.find(",", pos+1)
		tDataList[ line[0:pos] ] = int( line[pos+1:] )
		tCluster[ int( line[pos+1:] ) ].append( line[0:pos] )

#-------------------------------

# B-cubed evaluation
corrNum = []
for i in range(0, len(rCluster)):
	lst = []
	for j in range(0, len(tCluster)):
		lst.append(0)
	corrNum.append(lst)

for i in range(0, len(rFile)):
	rC = rDataList[ rFile[i] ]
	tC = tDataList[ rFile[i] ]

	if rC == 0: # it is classified as an outlier in the clustering output file
		precision += 1.0
		if tC == 0:
			recall += 1.0
		else:
			recall += 1.0 / len( tCluster[tC] )
	else: # it is not classified as an outlier in the clustering output file
		if tC == 0:
			precision += 1.0 / len( rCluster[rC] )
			recall += 1.0
		else:
			if corrNum[rC][tC] == 0:
				for j in range(0, len(rCluster[rC])):
					if rCluster[rC][j] in tCluster[tC]:
						corrNum[rC][tC] += 1
			precision += float( corrNum[rC][tC] ) / float( len(rCluster[rC]) )
			recall += float( corrNum[rC][tC] ) / float( len(tCluster[tC]) )

precision /= float( len(rFile) )
recall /= float( len(rFile) )

print "precision: " + "{0:.3f}".format(precision)
print "recall: " + "{0:.3f}".format(recall)




