# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

POSITION_MODE = 0
IMMEDIATE_MODE = 1

# Input
p = [int(n) for n in aoc.getFile().split(",")]

# Implementation
def intcodeComputer(p, inputVal):
    ip = 0
    output = 0
    while(1):
        opcode = p[ip]%100
        parametermodes = []
        for i in range(3): # 3 = current max number of parameters
            parametermodes.append((p[ip]%(10**(i+3))//(10**(i+2))))

        #print(ip, p[ip], opcode, parametermodes)

        if (opcode == 1): #add
            p1 = p[ip+1]
            if (parametermodes[0] == POSITION_MODE): p1 = p[p1]
            p2 = p[ip+2]
            if (parametermodes[1] == POSITION_MODE): p2 = p[p2]

            p[p[ip+3]] = p1 + p2
            ip += 4
        elif (opcode == 2): #multiply
            p1 = p[ip+1]
            if (parametermodes[0] == POSITION_MODE): p1 = p[p1]
            p2 = p[ip+2]
            if (parametermodes[1] == POSITION_MODE): p2 = p[p2]

            p[p[ip+3]] = p1 * p2
            ip += 4
        elif (opcode == 3): #input
            p[p[ip+1]] = inputVal
            ip += 2
        elif (opcode == 4): #output
            output = p[p[ip+1]]
            #print("output", output)
            ip += 2
        elif (opcode == 5): #jump-if-true
            p1 = p[ip+1]
            if (parametermodes[0] == POSITION_MODE): p1 = p[p1]
            p2 = p[ip+2]
            if (parametermodes[1] == POSITION_MODE): p2 = p[p2]

            if (p1 != 0): ip = p2
            else: ip += 3
        elif (opcode == 6): #jump-if-false
            p1 = p[ip+1]
            if (parametermodes[0] == POSITION_MODE): p1 = p[p1]
            p2 = p[ip+2]
            if (parametermodes[1] == POSITION_MODE): p2 = p[p2]

            if (p1 == 0): ip = p2
            else: ip += 3
        elif (opcode == 7): #less-than
            p1 = p[ip+1]
            if (parametermodes[0] == POSITION_MODE): p1 = p[p1]
            p2 = p[ip+2]
            if (parametermodes[1] == POSITION_MODE): p2 = p[p2]

            p[p[ip+3]] = 1 if p1 < p2 else 0
            ip += 4
        elif (opcode == 8): #equals
            p1 = p[ip+1]
            if (parametermodes[0] == POSITION_MODE): p1 = p[p1]
            p2 = p[ip+2]
            if (parametermodes[1] == POSITION_MODE): p2 = p[p2]

            p[p[ip+3]] = 1 if p1 == p2 else 0
            ip += 4
        elif (opcode == 99): #stop
            break
        else:
            print("wrong opcode", opcode)
            break
    return output

def part1():
    return intcodeComputer(aoc.copyList(p), 1)

def part2():
    return intcodeComputer(aoc.copyList(p), 5)

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
