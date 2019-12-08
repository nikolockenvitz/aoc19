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
    return IntcodeComputer(p, 1).run()

def part2():
    return IntcodeComputer(p, 5).run()

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
