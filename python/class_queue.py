class myqueue:

    def __init__(self):
        self._size = 0
        self._container = []

    def push(self, elt):
        self._size +=1
        self._container.append(elt)

    def pop(self):
        if self._size > 0:
            self._size-=1
            return self._container.pop(0)
        else:
            raise EmptyQueueError("empty queue!")


class EmergencyQueue(myqueue):
    def push_front(self,elt):
        self._container.insert(0,elt)


class EmptyQueueError(Exception):
    pass
