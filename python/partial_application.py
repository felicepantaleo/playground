from functools import partial
from operator import itemgetter,getitem
def flat_key(n, pair):
    return getitem(pair,n) # it was pair[n]

def my_partial(callable, *args, **kwds):
    def proxy(*innerargs, **innerkwds):
        return callable(*args, *innerargs, **{**kwds, **innerkwds})
    return proxy


pwd = []
with open("/etc/passwd") as passwd_file:
     for line in passwd_file:
         name, _ , uid, _ = line.split(":",3)
         pwd.append((name,int(uid)))
partial_key = partial(flat_key,1)

print(sorted(pwd,key=partial_key))
partial_key = my_partial(flat_key,1)
print(sorted(pwd,key=partial_key))

print(sorted(pwd, key=itemgetter(0)))
