def comparepasswd(a,b):
    return a[1]-b[1]

def getlabel(a):
    return a[1]

pwd = []
with open("/etc/passwd") as passwd_file:
     for line in passwd_file:
         name, _ , uid, _ = line.split(":",3)
         pwd.append((name,int(uid)))
print("\n\n with cmp")
print(sorted(pwd, cmp=comparepasswd))

print("\n\n with cmp with lambda")
print(sorted(pwd, cmp=lambda x,y: x[1]-y[1]))


print("\n\n with key")
print(sorted(pwd, key=getlabel))
print("\n\n with key with lambda")
print(sorted(pwd, key=lambda x: x[1]))
