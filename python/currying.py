def key(n):
    def key(pair):
        return pair[n]
    return key

pwd = []
with open("/etc/passwd") as passwd_file:
     for line in passwd_file:
         name, _ , uid, _ = line.split(":",3)
         pwd.append((name,int(uid)))

print(sorted(pwd,key=key(1)))
