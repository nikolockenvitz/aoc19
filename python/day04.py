# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile().split("-")
rangeStart = int(file[0])
rangeEnd   = int(file[1])

# Implementation
def checkPassword(pw):
    pw = str(pw)
    double1, double2 = False, False
    for i in range(5):
        if(pw[i] == pw[i+1]):
            double1 = True
            if(i+2<6 and pw[i+2] == pw[i]):
                pass
            elif(i-1>=0 and pw[i-1] == pw[i]):
                pass
            else:
                double2 = True
        if(int(pw[i]) > int(pw[i+1])):
            return [False, False]
    return [double1, double2]
    
def part1n2():
    result1, result2 = 0, 0
    for i in range(rangeStart, rangeEnd+1):
        [p1, p2] = checkPassword(i)
        if (p1): result1 += 1
        if (p2): result2 += 1
    return [result1, result2]

# Processing
[result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
