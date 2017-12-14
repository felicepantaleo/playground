genumerate=1
ienumerate=2
cenumerate=3


def genumerate(iterable, start =0):
    count = start
    for item in iterable:
        yield count, item
        count +=1
