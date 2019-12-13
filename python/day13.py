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
    result = 0
    c = IntcodeComputer(p)
    c.run()
    for i in range(len(c.outputs)):
        if(i%3 == 2 and c.outputs[i] == 2):
            result += 1
    return result

def showArcardeCabinet(d):
    xmax = 0
    ymax = 0
    for k in d.keys():
        xmax = max(xmax,k[0])
        ymax = max(ymax,k[1])
    for y in range(ymax+1):
        for x in range(xmax+1):
            if((x,y) in d):
                tileid = d[(x,y)]
                if (tileid == 0): tile = " "
                elif (tileid == 1): tile = "w"
                elif (tileid == 2): tile = "b"
                elif (tileid == 3): tile = "-"
                elif (tileid == 4): tile = "o"
            else:
                tile = " "
            print(tile, end="")
        print("")

def part2():
    result = 0
    d = {}
    c = IntcodeComputer(p)
    c.replaceValue(0, 2)
    ballx = 0
    paddlex = 0
    while(not c.halted):
        try:
            c.runInstruction()
        except:
            #showArcardeCabinet(d)
            #c.addInput(int(input("-1/0/1: ")))
            if (ballx > paddlex): inp = 1
            elif (ballx < paddlex): inp = -1
            else: inp = 0
            c.addInput(inp)
        if(len(c.outputs) == 3):
            x = c.outputs[0]
            y = c.outputs[1]
            t = c.outputs[2]
            c.outputs = []
            if (x==-1 and y==0):
                result = t
                #print(result)
                #showArcardeCabinet(d)
            else:
                d[(x,y)] = t
                if (t == 4): ballx = x
                if (t == 3): paddlex = x
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
