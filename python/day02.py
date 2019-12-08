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
def part1(noun=12, verb=2):
    c = IntcodeComputer(p)
    c.replaceValue(1, noun)
    c.replaceValue(2, verb)
    c.run()
    return c.program[0].get()

t = 19690720
def part2():
    result = 0
    for n in range(100):
        for v in range(100):
            if (part1(n,v) == t):
                result = 100*n + v
                break
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
