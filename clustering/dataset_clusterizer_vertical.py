import numpy as np
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
        if np.sum(nInLine)>0:
            events.append(nInLine)
print("events in file ", len(events))
events_array = np.array(events)

triggers = []
nTriggers = list(range(len(titles)))

nTriggers.remove(429)
for t in nTriggers:
    tmpList = []
    for ev in events_array:
        tmpList.append(ev[t])
    triggers.append(np.array(tmpList,dtype=bool))

triggers_array = np.array(triggers)
import hdbscan

print("initializing clusterizer")
clusterizer = hdbscan.HDBSCAN(algorithm='best', min_samples=1, approx_min_span_tree=True,
    gen_min_span_tree=False,
    metric='euclidean', min_cluster_size=10)
print("evaluating clusters")
clusterizer.fit(triggers_array)

nClusters = max(clusterizer.labels_)
print("found ", nClusters, " clusters" )
