# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

# Implementation
def getFuel(n):
    return max(0, int(n)//3 - 2)

def part1():
    result = 0
    for line in file:
        result += getFuel(line)
    return result

def part2():
    result = 0
    for line in file:
        cur = getFuel(line)
        while(cur > 0):
            result += cur
            cur = getFuel(cur)
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
