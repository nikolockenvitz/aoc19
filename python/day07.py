# Import and Setup
from aoc import *
from _intcode import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

from itertools import permutations

# Initialization
result1 = None
result2 = None

# Input
p = createIntcodeProgramFromFile(aoc.getFile())

# Implementation
def findBestCombination(values):
    result = 0
    perms = list(permutations(values))
    for perm in perms:
        loop = IntcodeComputerLoop(p, 5,
                                   [[perm[0],0],
                                    [perm[1]],
                                    [perm[2]],
                                    [perm[3]],
                                    [perm[4]]])        
        result = max(result, loop.run())
    return result

def part1():
    return findBestCombination([0,1,2,3,4])

def part2():
    return findBestCombination([5,6,7,8,9])

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
