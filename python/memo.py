from time import time as tick


def time(fn,*args,**kwds):
    start = tick()
    result = fn(*args,**kwds)
    end = tick()
    return (end-start), result



def fib(a):

    if a>=2:
        return fib(a-1) + fib(a-2)
    else:
        return 1



def memofn(callable):
    memo_dictionary= dict()
    def proxy(*args):
        if args not in memo_dictionary:
            memo_dictionary[args] = callable(*args)
        return memo_dictionary[args]
    return proxy



class memo():
    def __init__(self, fn):
        self._function = fn
        self._memo_dictionary= dict()

    def __call__(self,*args):
        if args not in self._memo_dictionary:
            self._memo_dictionary[args] = self._function(*args)
        return self._memo_dictionary[args]
