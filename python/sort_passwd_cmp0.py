def cmpfactory(column):
    def comparepasswd(a,b):
        return cmp(a[column],b[column])
    return comparepasswd


def keyfactory(column):
    def getlabel(a):
        return a[column]
    return getlabel



pwd = []
with open("/etc/passwd") as passwd_file:
     for line in passwd_file:
         name, _ , uid, _ = line.split(":",3)
         pwd.append((name,int(uid)))

print("\n\n with cmp factory")

print(sorted(pwd, cmp=cmpfactory(0)))



print("\n\n with key factory")

print(sorted(pwd, key=keyfactory(0)))
