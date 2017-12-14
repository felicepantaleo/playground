from operator import itemgetter




class EmptyQueue(Exception):
    pass

class PriorityQueue():

    def __init__(self):
        self._size = 0
        self._container = [[],[],[],[],[]]
        # self._minPriority = 99999
    def add(self, elt, priority=2):
        if priority <0 or priority > 4:
            raise ValueError
        if not isinstance(priority,int):
            raise TypeError
        self._size +=1
        self._container[priority].append( elt)
    def pop(self):
        if self._size > 0:
            self._size-=1
            for priorityBlock in self._container:
                if priorityBlock:
                    return priorityBlock.pop(0)
        else:
            raise EmptyQueue("empty queue!")

    def __len__(self):
        return self._size


#
# class myqueue:
#
#     def __init__(self):
#         self._size = 0
#         self._container = []
#
#     def push(self, elt):
#         self._size +=1
#         self._container.append(elt)
#
#     def pop(self):
#         if self._size > 0:
#             self._size-=1
#             return self._container.pop(0)
#         else:
#             raise EmptyQueueError("empty queue!")
#
#
# class EmergencyQueue(myqueue):
#     def push_front(self,elt):
#         self._container.insert(0,elt)
#
#
# class EmptyQueueError(Exception):
#     pass
