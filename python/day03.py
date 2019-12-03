# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

wire1 = file[0]
wire2 = file[1]

size = 40000

def gx(x):
    return x - size//2
def gy(y):
    return y - size//2

def mp(x,y):
    return m[y+size//2][x+size//2]

# Implementation
def go(pos, instruction, wire):
    direction = instruction[0]
    distance = int(instruction[1:])
    crossings = []
    if (direction == "U" or direction == "D"):
        if (direction == "U"):
            d = -distance - 1
            s = -1
        elif (direction == "D"):
            d = distance + 1
            s = 1
        for y in range(pos[1],pos[1]+d,s):
            if (wire == 2 and mp(pos[0],y) == 1):
                crossings.append([pos[0],y])
            if (mp(pos[0],y) & wire == 0):
                m[gy(y)][gx(pos[0])] += wire
        pos = [pos[0],pos[1]+d-s]
    elif (direction == "R" or direction == "L"):
        if (direction == "R"):
            d = distance + 1
            s = 1
        elif (direction == "L"):
            d = -distance - 1
            s = -1
        for x in range(pos[0],pos[0]+d,s):
            if (wire == 2 and mp(x,pos[1]) == 1):
                crossings.append([x,pos[1]])
            if (mp(x,pos[1]) & wire == 0):
                m[gy(pos[1])][gx(x)] += wire
        pos = [pos[0]+d-s,pos[1]]
    return [pos, crossings]

def md(point):
    return abs(point[0]) + abs(point[1])
    
def part1():
    result = 0
    pos = [0,0]
    cross = []
    for instruction in wire1.split(","):
        [newpos, crossings] = go(pos, instruction, 1)
        pos[0],pos[1] = newpos[0],newpos[1]
    pos = [0,0]
    for instruction in wire2.split(","):
        [newpos, crossings] = go(pos, instruction, 2)
        pos[0],pos[1] = newpos[0],newpos[1]
        for el in crossings:
            if (md(el) > 0):
                if (cross == []):
                    cross = [el[0],el[1]]
                elif (md(cross) > md(el)):
                    cross = [el[0],el[1]]
    return md(cross)

def go2(pos, instruction, wire, steps):
    direction = instruction[0]
    distance = int(instruction[1:])
    crossings = []
    steps -= 1
    if (direction == "U" or direction == "D"):
        if (direction == "U"):
            d = -distance - 1
            s = -1
        elif (direction == "D"):
            d = distance + 1
            s = 1
        for y in range(pos[1],pos[1]+d,s):
            steps+=1
            if (wire == 2 and mp(pos[0],y)[0] > 0):
                crossings.append([pos[0],y])
            if (mp(pos[0],y)[wire-1] == 0):
                m[gy(y)][gx(pos[0])][wire-1] = steps
        pos = [pos[0],pos[1]+d-s]
    elif (direction == "R" or direction == "L"):
        if (direction == "R"):
            d = distance + 1
            s = 1
        elif (direction == "L"):
            d = -distance - 1
            s = -1
        for x in range(pos[0],pos[0]+d,s):
            steps+=1
            if (wire == 2 and mp(x,pos[1])[0] > 0):
                crossings.append([x,pos[1]])
            if (mp(x,pos[1])[wire-1] == 0):
                m[gy(pos[1])][gx(x)][wire-1] = steps
        pos = [pos[0]+d-s,pos[1]]
    return [pos, crossings, steps]

def ms(point):
    return sum(mp(point[0],point[1]))

def part2():
    result = 0
    pos = [0,0]
    cross = []
    steps = 0
    for instruction in wire1.split(","):
        [newpos, crossings, newsteps] = go2(pos, instruction, 1, steps)
        pos[0],pos[1] = newpos[0],newpos[1]
        steps = newsteps
    pos = [0,0]
    steps = 0
    for instruction in wire2.split(","):
        [newpos, crossings, newsteps] = go2(pos, instruction, 2, steps)
        pos[0],pos[1] = newpos[0],newpos[1]
        steps = newsteps
        for el in crossings:
            if (el[0] > 0 and el[1] > 0):
                if (cross == []):
                    cross = [el[0],el[1]]
                elif (ms(cross) > ms(el)):
                    cross = [el[0],el[1]]
                    print(ms(cross))
        if(steps > ms(cross)):
            break
    return ms(cross)

# Processing
#m = []
#for i in range(size):
#    m.append([0]*size)

#result1 = part1()

m = []
for i in range(size):
    m.append([])
    for j in range(size):
        m[i].append([0,0])

result2 = part2()

# Output
aoc.output(result1, result2)
