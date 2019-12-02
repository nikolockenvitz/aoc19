# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile()

f = [int(x) for x in file.split(",")]

# Implementation
def part1(noun=12, verb=2):
    numbers = aoc.copyList(f)
    numbers[1] = noun
    numbers[2] = verb

    result = 0
    ix = 0
    while(1):
        if (numbers[ix] == 1):
            numbers[numbers[ix+3]] = numbers[numbers[ix+1]] + numbers[numbers[ix+2]]
        elif (numbers[ix] == 2):
            numbers[numbers[ix+3]] = numbers[numbers[ix+1]] * numbers[numbers[ix+2]]
        elif (numbers[ix] == 99):
            break
        else:
            print("err")
            break
        ix += 4
    result = numbers[0]
    return result

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
