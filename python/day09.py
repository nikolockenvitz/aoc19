# Import and Setup
from aoc import *
from _intcode import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
p = createIntcodeProgramFromFile(aoc.getFile())

# Implementation
def part1():
    result = IntcodeComputer(p, 1).run()
    return result

def part2():
    result = IntcodeComputer(p, 2).run()
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
