# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

from itertools import permutations

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

# Implementation
class IntcodeComputer:
    def __init__(self, program, inputVals):
        self.program = copyIntcodeProgram(program)
        self.inputVals = inputVals
        self.outputIntcodeComputers = []
        
        self.ip = 0
        self.output = 0
        self.inputIndex = 0
        self.halted = False

    def addOutputIntcodeComputer(self, outputIntcodeComputer):
        self.outputIntcodeComputers.append(outputIntcodeComputer)

    def addInput(self, inputValue):
        self.inputVals.append(inputValue)

    def run(self):
        while(not self.halted):
            self.runInstruction()
        return self.output

    def runInstruction(self):
        instruction = self.program[self.ip].get()
        opcode = instruction%100

        if (opcode not in numberOfParametersPerOpcode):
            print("unknown opcode")
            return

        # parameters
        params = []
        for i in range(numberOfParametersPerOpcode[opcode]):
            mode = (self.program[self.ip].get()%(10**(i+3))//(10**(i+2)))

            if (mode == POSITION_MODE):
                params.append(self.program[self.program[self.ip+i+1].get()])
            elif (mode == IMMEDIATE_MODE):
                params.append(self.program[self.ip+i+1])
            else:
                print("unknown mode")

        ipset = False
        if (opcode == 1): #add
            params[2].set(params[0].get() + params[1].get())
        elif (opcode == 2): #multiply
            params[2].set(params[0].get() * params[1].get())
        elif (opcode == 3): #input
            if(self.inputIndex >= len(self.inputVals)):
                raise IndexError('Need more inputs')
            params[0].set(self.inputVals[self.inputIndex])
            self.inputIndex-=-1
        elif (opcode == 4): #output
            self.output = params[0].get()
            for outputIntcodeComputer in self.outputIntcodeComputers:
                outputIntcodeComputer.addInput(self.output)
        elif (opcode == 5): #jump-if-true
            if (params[0].get() != 0):
                self.ip = params[1].get()
                ipset = True
        elif (opcode == 6): #jump-if-false
            if (params[0].get() == 0):
                self.ip = params[1].get()
                ipset = True
        elif (opcode == 7): #less-than
            params[2].set(1 if params[0].get() < params[1].get() else 0)
        elif (opcode == 8): #equals
            params[2].set(1 if params[0].get() == params[1].get() else 0)
        elif (opcode == 99): #halt
            self.halted = True
            return

        if (not ipset):
            self.ip += numberOfParametersPerOpcode[opcode] + 1

def part1():
    result = 0
    perms = list(permutations([0,1,2,3,4]))
    for perm in perms:
        a = IntcodeComputer(copyIntcodeProgram(p), [perm[0],0]).run()
        b = IntcodeComputer(copyIntcodeProgram(p), [perm[1],a]).run()
        c = IntcodeComputer(copyIntcodeProgram(p), [perm[2],b]).run()
        d = IntcodeComputer(copyIntcodeProgram(p), [perm[3],c]).run()
        e = IntcodeComputer(copyIntcodeProgram(p), [perm[4],d]).run()
        result = max(result, e)
    return result

def part2():
    result = 0
    perms = list(permutations([5,6,7,8,9]))
    for perm in perms:
        a = IntcodeComputer(copyIntcodeProgram(p), [perm[0],0])
        b = IntcodeComputer(copyIntcodeProgram(p), [perm[1]])
        c = IntcodeComputer(copyIntcodeProgram(p), [perm[2]])
        d = IntcodeComputer(copyIntcodeProgram(p), [perm[3]])
        e = IntcodeComputer(copyIntcodeProgram(p), [perm[4]])
        a.addOutputIntcodeComputer(b)
        b.addOutputIntcodeComputer(c)
        c.addOutputIntcodeComputer(d)
        d.addOutputIntcodeComputer(e)
        e.addOutputIntcodeComputer(a)
        while(1):
            try:
                while(not a.halted):
                    a.runInstruction()
            except IndexError:
                pass
            try:
                while(not b.halted):
                    b.runInstruction()
            except IndexError:
                pass
            try:
                while(not c.halted):
                    c.runInstruction()
            except IndexError:
                pass
            try:
                while(not d.halted):
                    d.runInstruction()
            except IndexError:
                pass
            try:
                while(not e.halted):
                    e.runInstruction()
            except IndexError:
                pass
            if(e.halted): break
        result = max(result, e.output)
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
