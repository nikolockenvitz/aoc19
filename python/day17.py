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
d = {}
intersections = []
start = []
end = []
def part1():
    global start
    global end
    result = 0
    c = IntcodeComputer(p)
    c.run()

    x,y=0,0
    for el in c.outputs:
        if (el == 35): d[(x,y)] = "#"
        elif (el == 46): d[(x,y)] = "."
        elif (el == 10):
            y += 1
            x = -1
        else:
            d[(x,y)] = chr(el)
            start = [x,y]
        x += 1
        #print(chr(el),end="")
    
    for k in d.keys():
        if (d[k] != "#"): continue
        x,y=k[0],k[1]
        cur = 0
        for diff in [[0,-1],[1,0],[0,1],[-1,0]]:
            if ((x+diff[0],y+diff[1]) in d and
                d[(x+diff[0],y+diff[1])] == "#"):
                cur += 1
        if (cur >= 3):
            result += x*y
            intersections.append((x,y))
        if (cur == 1):
            end = [x,y]
    return result

def part2():
    result = 0
    x,y = start[0],start[1]
    direction = ["^",">","v","<"].index(d[(x,y)]) # 0N, 1E, 2S, 3W
    path = []
    diffs = [[0,-1],[1,0],[0,1],[-1,0]]
    while(1):
        if (x == end[0] and y == end[1]):
            break
        scaff = [0,0,0,0] # NESW
        for i in range(4):
            nx,ny = x+diffs[i][0],y+diffs[i][1]
            if( (nx,ny) in d and d[(nx,ny)] in "#^>v<"):
                scaff[i] = 1
        if (scaff == [1,1,1,1] or # intersection
            (scaff[direction] == 1 and
             scaff[(direction+2)%4] == 1)): # straight
            path[-1] += 1
            x += diffs[direction][0]
            y += diffs[direction][1]
        else:
            nd = -1
            for i in range(4):
                if (scaff[i] == 1 and
                    i != (direction-2)%4):
                    nd = i
                    break
            if((nd-direction)%4 == 3):
                path.append("L")
            elif((nd-direction)%4 == 1):
                path.append("R")
            direction = nd
            x += diffs[direction][0]
            y += diffs[direction][1]
            path.append(1)
    
    pathstring = path[0]
    for i in range(1,len(path)):
        pathstring += "," + str(path[i])

    #    maxlenght:34567890123456789#
    patterns = ["L,4,L,4,L,6",
                "L,6,R,12,L,6,L,8,L,8",
                "L,6,R,12,R,8,L,8"]
    # TODO: find patterns automatically
    for i in range(len(patterns)):
        pathstring = pathstring.replace(patterns[i], chr(65+i))
    
    c = IntcodeComputer(p)
    c.replaceValue(0,2)
    def sendInput(computer, text):
        numbers = [ord(l) for l in text]
        for n in numbers+[10]:
            computer.addInput(n)
    sendInput(c, pathstring)
    for pattern in patterns:
        sendInput(c, pattern)
    sendInput(c, "n")
    c.run()
    result = c.output
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
