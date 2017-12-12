from functools import reduce
from operator import add




with open("numbers.dat") as inputFile:
    for line in inputFile:
        a = list(line.split(" "))
        a[-1] = a[-1].strip()

        nInLine = map(int,a)

        print("reduction: ",reduce(add, nInLine))
