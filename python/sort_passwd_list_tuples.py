sorted_pwd = []
with open("/etc/passwd") as passwd_file:
     for line in passwd_file:
         name, _ , uid, _ = line.split(":",3)
         sorted_pwd.append((name,int(uid)))

print(sorted(sorted_pwd, key=lambda x:x[1]))
