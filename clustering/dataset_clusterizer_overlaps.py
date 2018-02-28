import numpy as np
titles = []


def exceptionInt(a):
    try :
        return int(a)

    except ValueError:
        titles.append(a)
        return 0

class Dataset:
    triggers = []
    threshold = 0.2
    def __init__(self, triggers):
        self.triggers = triggers

    def overlap(self, events, trigger, occupancy_cols):
        overlap = 0
        if trigger not in self.triggers:
            for ev in events:
                if ev[trigger] == 1:
                    sum = 0
                    for t in self.triggers:
                        if ev[t] == 1:
                            overlap +=1
                            break

            overlap /= occupancy_cols[trigger]
            if overlap > threshold:
                self.triggers.append(trigger)
                return True
        return False



    def overlapCluster(self, events, cluster, occupancy_cols):
        overlap = 0
        for ev in events:
            triggerThisCluster = False
            triggerOtherCluster = False
            for t in self.triggers:
                if ev[t] == 1:
                    triggerThisCluster = True
                    break
            for t in cluster.triggers:
                if ev[t] == 1:
                    triggerOtherCluster = True
                    break
            if triggerThisCluster and triggerOtherCluster:
                overlap+=1

        if trigger not in self.triggers:

                if ev[trigger] == 1:
                    sum = 0
                    for t in self.triggers:
                        if ev[t] == 1:
                            overlap +=1
                            break

            overlap /= occupancy_cols[trigger]
            if overlap > threshold:
                self.triggers.append(trigger)
                return True
        return False



    def merge(self, other)
        for t in other.triggers:
            if t not in self.triggers:
                self.triggers.append(t)
        other.triggers = []








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

overlaps = np.zeros((len(titles),len(titles)),dtype=np.int)


nTriggers = list(range(len(titles)))
nTriggers.remove(429)
occupancy_cols = np.zeros(len(titles),dtype=np.int)
for ev in events_array:
    for i in nTriggers:
        if ev[i] == 1:
            occupancy_cols[i] +=1

remaining_cols = nTriggers





import matplotlib.pyplot as plt
imgplot = plt.imshow(overlaps)
plt.show()
