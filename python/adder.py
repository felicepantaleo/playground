def make_adder(n):

    def adder(x):
        return n+x
    return adder

add3=make_adder(3)
dir(add3)

a=2

def f():
    print(a)
f()
