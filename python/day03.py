# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

wire1 = file[0].split(",")
wire2 = file[1].split(",")

d = {}

# Implementation
def go(x, y, instruction, wire, steps):
    direction = instruction[0]
    distance = int(instruction[1:])
    crosses = []
    cx, cy = x, y
    for i in range(distance):
        if (direction == "U"): cy += 1
        if (direction == "R"): cx += 1
        if (direction == "D"): cy -= 1
        if (direction == "L"): cx -= 1
        steps += 1

        if((cx,cy) in d):
            if(d[(cx,cy)][wire-1] == 0):
                d[(cx,cy)][wire-1] = steps
            if(d[(cx,cy)][1-(wire-1)] > 0):
                crosses.append((cx,cy))
        else:
            d[(cx,cy)] = [0,0]
            d[(cx,cy)][wire-1] = steps

    return [cx, cy, steps, crosses]

def m1(point):
    return abs(point[0]) + abs(point[1])

def m2(point):
    return sum(d[(point[0],point[1])])

def part1n2():
    result1, result2 = 0, 0
    cross1, cross2 = [], []
    x,y, steps = 0, 0, 0
    for instruction in wire1:
        [x, y, steps, crosses] = go(x, y, instruction, 1, steps)
    x,y, steps = 0, 0, 0
    for instruction in wire2:
        [x, y, steps, crosses] = go(x, y, instruction, 2, steps)
        for el in crosses:
            if(el[0] == 0 and el[1] == 0): continue
            if (cross1 == [] or m1(el) < m1(cross1)):
                cross1 = [el[0],el[1]]
            if (cross2 == [] or m2(el) < m2(cross2)):
                cross2 = [el[0],el[1]]
    result1 = m1(cross1)
    result2 = m2(cross2)
    return [result1, result2]

# Processing
[result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
