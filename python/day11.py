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
def paint(startingColor=0):
    d = {(0,0): startingColor}
    x,y,direction = 0,0,0
    c = IntcodeComputer(p)
    while(not c.halted):
        if((x,y) in d and d[(x,y)] == 1):
            inp = 1 #white
        else:
            inp = 0
        c.addInput(inp)
        while(not c.halted and len(c.outputs) < 2):
            c.runInstruction()
        if(len(c.outputs) < 2 and c.halted):
            break
        d[(x,y)] = c.outputs[0]
        if(c.outputs[1] == 0):
            direction = (direction+1)%4 # left
        else:
            direction = (direction-1)%4
        if(direction == 0):
            y += 1
        elif(direction == 1):
            x -= 1
        elif(direction == 2):
            y -= 1
        elif(direction == 3):
            x += 1
        c.outputs = []
    return d

def showPainting(painting):
    minx,maxx,miny,maxy=0,0,0,0
    for k in painting.keys():
        minx = min(minx, k[0])
        maxx = max(maxx, k[0])
        miny = min(miny, k[1])
        maxy = max(maxy, k[1])
    for y in range(maxy, miny-1, -1):
        for x in range(minx, maxx+1):
            if((x,y) in painting and painting[(x,y)] == 1):
                print("#",end="")
            else:
                print(".",end="")
        print("")

def part1():
    painting = paint()
    return len(painting)

def part2():
    showPainting(paint(1))
    return None

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
