sorted_pwd = {}
with open("/etc/passwd") as passwd_file:
     for line in passwd_file:
         name, _ , uid, _ = line.split(":",3)
         sorted_pwd[int(uid)] = name




a = list(sorted_pwd.keys())
b = sorted(a)
print(b)

for sortedkey in b:
    print(sortedkey, sorted_pwd[sortedkey])
