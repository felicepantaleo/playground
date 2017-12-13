class Counter:
    def __init__(self,start):
        self.count=start

    def up(self,n=1):
        self.count+=n
    def down(self, n=1):
        self.count-=n

class Addcounter(Counter):
    def __repr__(self):
        return 'Addcounter({.count})'.format(self)
    def __add__(self):
        return Addcounter(self.count+other.count)


a=Counter(10)
a.up(2)
a.foo=9
print(a.count)
