def genumerate(iterable, start =0):
    count = start
    for item in iterable:
        yield count, item
        count +=1

from itertools import count


def ienumerate (iterable, start=0):
    return zip(count(start=start), iterable)
