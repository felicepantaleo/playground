import numpy as np
titles = []


def exceptionInt(a):
    try :
        return int(a)

    except ValueError:
        titles.append(a)
        return 0


def event_mask_cmp(event, mask):
    for bit in mask:
        if event[bit] == 0:
            return False
    return True


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


class Cluster:
    numberOfEvents = 0
    required_triggers = []
    required_not_triggers = []

    def __init__(self, true_bits, false_bits,n):
        self.required_triggers = true_bits
        self.required_not_triggers = false_bits
        self.numberOfEvents = n
    def checkEvent(self, event):
        for trigger in self.required_triggers:
            if event[trigger] != 1:
                return False
        for trigger in self.required_not_triggers:
            if event[trigger] != 0:
                return False
        return True

occupancy_cols = np.zeros(len(titles))
remaining_cols = list(range(len(titles)))
remaining_events = list(range(len(events)))
remaining_cols.remove(429)
found_clusters = []

threshold = 0.1

current_true_mask = []
current_false_mask = []
eventsInCluster = 0
firstColumnOFCluster = True
while remaining_cols and remaining_events:
    print("remaining columns", len(remaining_cols))

    for col in remaining_cols:
        occupancy_cols[col] = 0
        for evid in remaining_events:
            if event_mask_cmp(events_array[evid], current_true_mask) and events_array[evid][col]==1 :
                occupancy_cols[col]+=1
    maxcol = np.argmax(occupancy_cols)

    if (occupancy_cols[maxcol]/len(remaining_events)) > threshold:
        current_true_mask.append(maxcol)
        firstColumnOFCluster = False
        print("cluster getting too many events, adding another filter")
    else:
        current_true_mask.append(maxcol)
        print("found new cluster with events: ",occupancy_cols[maxcol])
        tmpCluster = Cluster(current_true_mask,current_false_mask, occupancy_cols[maxcol])
        current_false_mask = current_false_mask + current_true_mask
        current_true_mask = []
        remaining_events = list(filter(lambda a : not tmpCluster.checkEvent(events_array[a]), remaining_events))
        found_clusters.append(tmpCluster)
        firstColumnOFCluster = True

    print("trigger ", maxcol, " contains  ", occupancy_cols[maxcol], " events")
    if firstColumnOFCluster :
        remaining_cols.remove(maxcol)
    occupancy_cols[maxcol] = 0
    print("remaining cols and events " , len(remaining_cols), len(remaining_events))



# import matplotlib.pyplot as plt
#
# plt.hist(clusterizer.labels_, bins=max(clusterizer.labels_))  # arguments are passed to np.histogram
# plt.title("histo clusterizer.labels_")
# plt.show()
