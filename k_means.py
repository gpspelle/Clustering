import numpy as np
import random

def clustering(initial_points, ep, item):

    # Ordering information
    item = sorted(item, key=lambda x: x[0])

    min_v = item[0][0]
    max_v = item[-1][0]

    # Creating a list of initial points for clusters
    clusters = [] 

    for i in range(initial_points): # uniform init for the begin points
        clusters.append([random.uniform(min_v, max_v)])

    for i in range(ep): # for every epoch

        # The below steps will assign every item to one of these clusters.
        # More precisely, the closest clusters. Where distance is measured
        # with euclidean-distance.

        for data in item: # for every data in a item assign it to a point 
            min = max_v
            for c in clusters: # for every possible cluster

                if c[0] < 0:
                    continue

                d = abs(c[0] - data[0]) # euclidean-distance from a cluster
                                        # to a data point
                if d < min:
                    min = d
                    nearest_cluster = c

            data = list(data)

            for c in clusters:
                if data in c[1:]:
                    c[1:].remove(data)

            # Not adding repetead elements
            nearest_cluster = clusters.index(nearest_cluster)
            cluster_datas = clusters[nearest_cluster][1:]

            if data not in cluster_datas:
                clusters[nearest_cluster].append(data)
                
        # Now we need to update the centroids of our clusters
        
        for c in clusters:

            # Avoid zero division because a cluster has no boxes in it
            if len(c[1:]) == 0:
                continue

            sum = 0
            for i in c[1:]:
                sum += i[0]

            c[0] = sum / len(c[1:])

    for c in clusters:
        for c_ in clusters:
            if c == c_ or c_[0] < 0:
                continue

            if abs(c[0] - c_[0]) < 5:
                for i in c_[1:]:
                    if i not in c[1:]:
                        c.append(i)

                clusters.remove(c_)
                c_[0] = -1
                c_ = c_[0]

    for c in clusters:
        if len(c) == 1:
            continue

        print(c)
        print("")

    for i in item:
        print(i)

    return clusters

# Opening file

totems = np.load('bb_15.npy', encoding='latin1')

for item in totems:
    clusters = clustering(200, 50, item)

