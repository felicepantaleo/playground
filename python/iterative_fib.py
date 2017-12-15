# this has linear time complexity,
def fibi(n):
    c,p=1,1
    while n>1:
        c,p = c+p,c
        n-=1
    return c


# this has linear time complexity,
def fibir(n, c=1, p=1):
    if n>1:
        return fibir(n-1,c+p, c)
    return c


# this has linear time complexity,
def fibig():
    c,p=1,1
    yield 1
    yield 1
    while True:
        c,p = c+p,c
        yield c
    return
