#dbscan.py
Perform DBSCAN on the given set of 2-dimensional data points.

##Dataset file
First line: number of data points<br>
Each of the following lines corresponds to a data point, which contains two floating-point numbers as the coordinates separated by a comma. It is advised that the data points should be normalised before running the script.

##Output file
First line: minPts<br>
Second line: epsilon<br>
Third line: number of clusters<br>
Each of the following lines corresponds to a data point in the dataset file. It contains three numbers. The first two are the coordinates of a point; the last one is an integer [1…m] indicating which m clusters the point belongs to, or 0 if the point is an outlier. The three numbers are separated by commas.

##Usage
- command to run the script: python dbscan.py datasetFile outputFile minPts epsilon
  e.g. python dbscan.py ../data/data_normalized.txt ../results/dbscanResult.txt 25 0.065
- all the parent directories of the output file should be created first
  e.g. ../results/ should be created first

#bcubed.py
Compute b-cubed precision and recall from the given clustering output file and ground truth file of 2-dimensional data points. Correct to 3 decimal places.

##Clustering output file
The format is the same as the output file of dbscan.py.

##Ground truth file
Fist line: number of data points<br>
Second line: number of clusters<br>
Each of the following lines corresponds to a data point. It contains three numbers. The first two are the coordinates of a point; the last one is an integer [1…m] indicating which m clusters the point belongs to, or 0 if the point is an outlier. The three numbers are separated by commas. Please note that the index of cluster is unimportant. It is simply a notation to indicate which points belong to the same cluster.

##Usage
- command to run the script: python bcubed.py outputFile truthFile
  e.g. python bcubed.py ../results/dbscanResult.txt ../data/truth_normalized.txt
