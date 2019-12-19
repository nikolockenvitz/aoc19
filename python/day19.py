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
def isInTractorBeam(x,y):
    c = IntcodeComputer(p)
    c.addInput(x)
    c.addInput(y)
    c.run()
    return c.output

d = {}
def part1(show=False):
    result = 0
    y = 0
    x = 0
    firstX = 0
    while(1):
        x = firstX if firstX != None else 0
        if (show): print(" "*x, end="")
        firstX = None
        while(1):
            b = isInTractorBeam(x,y)
            if (b):
                result += 1
                d[(x,y)] = 1
                if (firstX == None):
                    firstX = x
                if (show): print("#",end="")
            else:
                if (show): print(".",end="")
            if ((firstX != None and not b) or
                x >= 50):
                break
            x += 1
        if (show): print("")
        y += 1
        if(y >= 50): break
    return result

def helper(x,y, increaseTo100=True):
    xs = []
    xs100 = []
    while(1):
        b = isInTractorBeam(x,y)
        if (b):
            xs.append(x)
            if (isInTractorBeam(x,y+99)):
                xs100.append(x)
        else:
            if (xs != []):
                break
        x += 1
    if (len(xs100) >= 100 or increaseTo100 == False):
        return [xs[0],y,len(xs100),xs100[0]]
    
    factor = 100 / len(xs100)
    yold = y
    y = int(y * factor)
    x = int(0.98*y*xs[0]/yold)
    return helper(x,y)

def part2():
    result = 0
    xs = []
    for k in d.keys():
        if(k[1] == 49): # last calculted row
            xs.append(k[0])
    y = int(2 * 49 * (100 / len(xs)))
    x = int(0.95*y*xs[0]/49)

    t = helper(x,y) # height = 100 (y - y+99)
    result = [t[0],t[1]]
    while(1):
        t = helper(result[0]-5,result[1]-max(1,t[2]-100),False)
        if (t[2] < 100):
            break
        result = [t[0],t[1],t[2],t[3]]
    result = 10000*result[3] + result[1]
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
