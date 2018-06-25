import numpy as np

threshold = 0.25

# Opening file
file = np.load('bb_15.npy', encoding='latin1')

t = 0
# Through every totem
clusters = []
for totem in file:
    # Ordering a totem
    totem = sorted(totem ,key=lambda x: x[0])
    print("Number of boxes in image %d: %d" % (t, len(totem)))
    t+=1

    # Empty cluster list
    cluster_t = []
    cluster = []
    counter = 0
    index = 0
    while True:

        top_y = totem[index][0]
        bottom_y = totem[index][1]

        height = bottom_y - top_y
        
        for j in range(index, len(totem)):
            #print(totem[j])
            diff_top_y = top_y - totem[j][0] 
            diff_bottom_y = bottom_y - totem[j][1] 

            if diff_top_y < 0:
                diff_top_y *= -1

            if diff_bottom_y < 0:
                diff_bottom_y *= -1

            if height * threshold < diff_top_y or height * threshold < diff_bottom_y:
                cluster_t.append(cluster)
                cluster = []
                break
            else:
                cluster.append(totem[j])
                index += 1

        if index >= len(totem):
            cluster_t.append(cluster)
            break
    clusters.append(cluster_t)


i = 0
for totem in clusters:
    print("Imprimindo totem: %d com %d bounding boxes" % (i , len(totem)))
    i+=1
    for cluster in totem:
        print(cluster, len(cluster))
