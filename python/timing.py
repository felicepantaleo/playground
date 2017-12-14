from time import time as tick


def time(fn,*args,**kwds):
    start = tick()
    result = fn(*args,**kwds)
    end = tick()
    return (end-start), result
