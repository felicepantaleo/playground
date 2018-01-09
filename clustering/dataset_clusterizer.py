import numpy as np
from sklearn.cluster import DBSCAN
import hdbscan


titles = []
def exceptionInt(a):
    try :
        return int(a)

    except ValueError:
        titles.append(a)
        return 0




events = []



with open("results") as inputFile:
    for line in inputFile:
        a = line.split()
        nInLine = np.array(list(map(exceptionInt,a)))
        # nInLine = list(map(exceptionInt,a))
        assert(len(nInLine) == len(titles))
        events.append(nInLine)
print("events in file ", len(events))
events_array = np.array(events)

# dbscan = DBSCAN(eps=0.5, metric='euclidean', min_samples=5,)
# dbscan.fit(events_array)

print("initializing clusterizer")
clusterizer = hdbscan.HDBSCAN(algorithm='best', min_samples=1, approx_min_span_tree=True,
    gen_min_span_tree=False,
    metric='euclidean', min_cluster_size=10)
print("evaluating clusters")
clusterizer.fit(events_array)

nClusters = max(clusterizer.labels_)
print("found ", nClusters, " clusters" )


import matplotlib.pyplot as plt

plt.hist(clusterizer.labels_, bins=max(clusterizer.labels_))  # arguments are passed to np.histogram
plt.title("histo clusterizer.labels_")
plt.show()
