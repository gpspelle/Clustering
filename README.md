# Clustering Algorithms

This code was built to organize in vertical clusters bounding boxes that were
found in an image. These clusters are related to horizontal information, so, 
each cluster has an mean centered vertical position and the objects that are
in these vertical region.

## Usage (1)

The parameters that you may change easily is threshold that controls how
far from the center it's okay to a bounding boxe enter in a specific cluster.
Threshold = 1: if the distance equals to the boxe size; 0.5 for half sized.
 
The other parameter is the information that you want to cluster. Note that,
the format is (y1, y2, x1, x2) where (x1, y1) is the top-left corner and
(x2, y2) is the down-right corner.

$ python3 clustering.py

## Usage (2)

The parameters that you may want to change are those related to convergence, 
more specificaly the number of iterations and initial points, which are passed
as parameters to clustering(). Note that the data foramt is still hardcoded in
the same way as described in Usage (1). 

$ python3 k_means.py
