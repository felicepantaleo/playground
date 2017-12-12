
def myEnumerate(b):
    indices = range(len(b))
    return list(zip(indices,b))


a = myEnumerate("yeah!")

print(a)
