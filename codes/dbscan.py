#!/usr/bin/python
import sys
import math

#-------------------------------

# Parse arguments
inputFile = sys.argv[1]
outputFile = sys.argv[2]
minPts = int( sys.argv[3] )
epsilon = float( sys.argv[4] )

# Initialize other variables
cluster = 1

class Data:
	x = 0.0
	y = 0.0
	cluster = -1 # let cluster = -1 denotes that the data point is unvisited
	def __init__(self, x, y):
		self.x = x
		self.y = y

dataList = []

#-------------------------------

# Read in data from the input file
with open(inputFile) as file:
	n = int( file.readline().strip() )
	for i in range(0, n):
		line = file.readline().strip()
		pos = line.find(",")
		data = Data( float(line[0:pos]), float(line[pos+1:]) )
		dataList.append(data)

#-------------------------------

# Compute the Euclidean distance
def dist(x1, y1, x2, y2):
	xSquare = math.pow( x1-x2, 2 )
	ySquare = math.pow( y1-y2, 2 )
	return math.sqrt( xSquare + ySquare )

#-------------------------------

# DBSCAN
for i in range(0, len(dataList)):
	if dataList[i].cluster == -1:
		dataList[i].cluster = 0

		# find the epsilon neighbourhood
		neighbourhood = []
		for j in range(0, len(dataList)):
			if dist( dataList[i].x, dataList[i].y, dataList[j].x, dataList[j].y ) <= epsilon:
				neighbourhood.append(dataList[j])
		
		if len(neighbourhood) >= minPts: # a core point
			dataList[i].cluster = cluster

			while len(neighbourhood) > 0:
				data = neighbourhood.pop(0)

				if data.cluster == -1:
					neighbourhood2 = []
					for j in range(0, len(dataList)):
						if dist( dataList[j].x, dataList[j].y, data.x, data.y ) <= epsilon:
							neighbourhood2.append(dataList[j])

					if len(neighbourhood2) >= minPts:
						neighbourhood += neighbourhood2

				if data.cluster <= 0:
					data.cluster = cluster

			cluster += 1

cluster -= 1

#-------------------------------

# Write the classification result to the output file
f = open(outputFile, "w")
f.write(str(minPts) + "\n")
f.write(str(epsilon) + "\n")
f.write(str(cluster) + "\n")
for data in dataList:
	f.write( "{0:.6f}".format(data.x) + "," + "{0:.6f}".format(data.y) + "," + str(data.cluster) + "\n" )


