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
p = [IntcodeInteger(n) for n in aoc.getFile().split(",")]

# Implementation
numberOfParametersPerOpcode = {
    1: 3, # add
    2: 3, # multiply
    3: 1, # input
    4: 1, # output
    5: 2, # jump-if-true
    6: 2, # jump-if-false
    7: 3, # less than
    8: 3, # equals
    99: 0, # halt
}

def intcodeComputer(program, inputVal):
    ip = 0
    output = 0
    while(1):
        instruction = program[ip].get()
        opcode = instruction%100

        if (opcode not in numberOfParametersPerOpcode):
            print("unknown opcode")
            break

        # parameters
        params = []
        for i in range(numberOfParametersPerOpcode[opcode]):
            mode = (program[ip].get()%(10**(i+3))//(10**(i+2)))

            if (mode == POSITION_MODE):
                params.append(program[program[ip+i+1].get()])
            elif (mode == IMMEDIATE_MODE):
                params.append(program[ip+i+1])
            else:
                print("unknown mode")

        ipset = False
        if (opcode == 1): #add
            params[2].set(params[0].get() + params[1].get())
        elif (opcode == 2): #multiply
            params[2].set(params[0].get() * params[1].get())
        elif (opcode == 3): #input
            params[0].set(inputVal)
        elif (opcode == 4): #output
            output = params[0].get()
        elif (opcode == 5): #jump-if-true
            if (params[0].get() != 0):
                ip = params[1].get()
                ipset = True
        elif (opcode == 6): #jump-if-false
            if (params[0].get() == 0):
                ip = params[1].get()
                ipset = True
        elif (opcode == 7): #less-than
            params[2].set(1 if params[0].get() < params[1].get() else 0)
        elif (opcode == 8): #equals
            params[2].set(1 if params[0].get() == params[1].get() else 0)
        elif (opcode == 99): #halt
            break

        if (not ipset):
            ip += numberOfParametersPerOpcode[opcode] + 1
    return output

def part1():
    return intcodeComputer(copyIntcodeProgram(p), 1)

def part2():
    return intcodeComputer(copyIntcodeProgram(p), 5)

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
