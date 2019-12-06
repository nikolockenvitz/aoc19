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
orbits = {}

for line in file:
    l = line.split(")")
    orbits[l[1]] = l[0]

def getNumberOfOrbits(o):
    if (o == "COM"): return 0
    parent = orbits[o]
    return 1 + getNumberOfOrbits(parent)

def getAllParents(o):
    parents = []
    while(1):
        parent = orbits[o]
        if (parent == "COM"): return parents+["COM"]
        parents.append(parent)
        o = parent

def part1():
    result = 0
    for k in orbits.keys():
        result += getNumberOfOrbits(k)
    return result

def part2():
    result = 0
    you = getAllParents("YOU")
    san = getAllParents("SAN")
    for i in range(len(you)):
        if(you[i] in san):
            result = i + san.index(you[i])
            break
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
