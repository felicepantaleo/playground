memofib = []



def fib(a):

    if a>=2:
        return fib(a-1) + fib(a-2)
    else:
        return 1
