from functools import reduce
from operator import add

def exceptionInt(a):
    try :
        return int(a)

    except ValueError:
        print("skipping element, garbage detected: ", a)
        return 0


with open("numbers.dat") as inputFile:
    for line in inputFile:
        a = line.split()

        nInLine = list(map(exceptionInt,a))
        print(nInLine)

        print("reduction: ",reduce(add, nInLine,0))
