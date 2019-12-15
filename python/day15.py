# Import and Setup
from aoc import *
from _intcode import *
from random import randint
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
p = createIntcodeProgramFromFile(aoc.getFile())

# Implementation
NORTH, SOUTH, WEST, EAST = 1, 2, 3, 4

def show(d, droids=[]):
    xminmax = [0,0]
    yminmax = [0,0]
    for k in d.keys():
        xminmax = [min(xminmax[0],k[0]),max(xminmax[1],k[0])]
        yminmax = [min(yminmax[0],k[1]),max(yminmax[1],k[1])]
    for droid in droids:
        xminmax = [min(xminmax[0],droid[0]),max(xminmax[1],droid[0])]
        yminmax = [min(yminmax[0],droid[1]),max(yminmax[1],droid[1])]
    print("-"*(xminmax[1]-xminmax[0]+1))
    for y in range(yminmax[0],yminmax[1]+1):
        for x in range(xminmax[0],xminmax[1]+1):
            if(x==16 and y in (12,13,14)): print("\n",x,y,d[(x,y)],"\n")
            if ((x,y) in droids):
                print("D",end="")
            elif ((x,y) == (0,0)):
                print("S",end="")
            elif ((x,y) not in d):
                print(" ",end="")
            else:
                print("#.O"[d[(x,y)]],end="")
        print("")
    print("-"*(xminmax[1]-xminmax[0]+1),"\n")

def turnLeft(direction):
    if (direction == NORTH): return WEST
    if (direction == SOUTH): return EAST
    if (direction == WEST): return SOUTH
    if (direction == EAST): return NORTH

def turnRight(direction):
    if (direction == NORTH): return EAST
    if (direction == SOUTH): return WEST
    if (direction == WEST): return NORTH
    if (direction == EAST): return SOUTH

def getNewPos(x,y,direction):
    if (direction == NORTH): return [x,y-1]
    if (direction == SOUTH): return [x,y+1]
    if (direction == WEST): return [x-1,y]
    if (direction == EAST): return [x+1,y]

def goStep(computer, x, y, direction, d):
    computer.addInput(direction)
    computer.outputs = []
    while(1):
        computer.runInstruction()
        if (len(computer.outputs) == 1):
            break
    result = computer.outputs[0]
    nx,ny = getNewPos(x,y,direction)
    d[(nx,ny)] = result
    if (result): x,y =nx,ny
    return [result,x,y]

def part1n2():
    # create graph with right-hand-rule / wall follower
    # bfs with copying computer didn't work
    c = IntcodeComputer(p)
    x, y = 0, 0
    d = {(x,y): 1} # 1 for nothing, 0 for wall, 2 for oxygen
    direction = NORTH
    ox,oy = 0,0 # oxygen position
    while(1):
        for i in range(4):
            if (i == 0): direction = turnRight(direction)
            else: direction = turnLeft(direction)
            r,x,y = goStep(c, x, y, direction, d)
            if (r):
                if (r == 2): ox,oy=x,y
                break
        if (x == 0 and y == 0): break # back at start

    # bfs from (ox,oy)
    result1, result2 = None, 0
    fields = [(ox,oy)]
    while(1):
        newfields = []
        for f in fields:
            for i in [NORTH,SOUTH,EAST,WEST]:
                x,y = getNewPos(f[0],f[1],i)
                if (x == 0 and y == 0 and result1 == None):
                    result1 = result2 + 1
                if (d[(x,y)] == 1):
                    d[(x,y)] = 2
                    newfields.append([x,y])
        fields = newfields
        if(len(fields) == 0): break
        result2 += 1
    return result1, result2

# Processing
result1, result2 = part1n2()

# Output
aoc.output(result1, result2)
