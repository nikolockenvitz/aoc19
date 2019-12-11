# Library for Intcode Computers #

POSITION_MODE  = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE  = 2

numberOfParametersPerOpcode = {
    1: 3, # add
    2: 3, # multiply
    3: 1, # input
    4: 1, # output
    5: 2, # jump-if-true
    6: 2, # jump-if-false
    7: 3, # less than
    8: 3, # equals
    9: 1, # adjust relative base
    99: 0, # halt
}

def createIntcodeProgramFromFile(fileContent):
    return [IntcodeInteger(n) for n in fileContent.split(",")]

def copyIntcodeProgram(program):
    newProgram = []
    for el in program:
        newProgram.append(IntcodeInteger(el.get()))
    return newProgram

class IntcodeInteger:
    def __init__(self, value):
        self.value = int(value)

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def __repr__(self):
        return "Intcode Integer: " + str(self.value)

class IntcodeComputer:
    def __init__(self, program, inputValues=None):
        self.program = {}
        copy = copyIntcodeProgram(program)
        for n in range(len(copy)):
            self.program[n] = copy[n]

        if(inputValues == None):
            self.inputValues = []
        elif(type(inputValues) == int):
            self.inputValues = [inputValues]
        else:
            self.inputValues = inputValues

        self.outputIntcodeComputers = []

        self.ip = 0
        self.output = 0
        self.outputs = []
        self.inputIndex = 0
        self.relativeBase = 0
        self.halted = False

    def replaceValue(self, address, value):
        self.program[address] = IntcodeInteger(value)

    def addOutputIntcodeComputer(self, outputIntcodeComputer):
        self.outputIntcodeComputers.append(outputIntcodeComputer)

    def addInput(self, inputValue):
        self.inputValues.append(inputValue)

    def run(self):
        while(not self.halted):
            self.runInstruction()
        return self.output

    def runInstruction(self):
        instruction = self.program[self.ip].get()
        opcode = instruction%100

        if (opcode not in numberOfParametersPerOpcode):
            print("unknown opcode", opcode)
            return

        # parameters
        params = []
        for i in range(numberOfParametersPerOpcode[opcode]):
            mode = (self.program[self.ip].get()%(10**(i+3))//(10**(i+2)))

            if ((self.ip+i+1) not in self.program):
                self.program[self.ip+i+1] = IntcodeInteger(0)

            if (mode == POSITION_MODE):
                pos = self.program[self.ip+i+1].get()
                if (pos not in self.program):
                    self.program[pos] = IntcodeInteger(0)
                params.append(self.program[pos])
            elif (mode == IMMEDIATE_MODE):
                params.append(self.program[self.ip+i+1])
            elif (mode == RELATIVE_MODE):
                pos = self.relativeBase + self.program[self.ip+i+1].get()
                if (pos not in self.program):
                    self.program[pos] = IntcodeInteger(0)
                params.append(self.program[pos])
            else:
                print("unknown mode")

        ipset = False
        if (opcode == 1): #add
            params[2].set(params[0].get() + params[1].get())
        elif (opcode == 2): #multiply
            params[2].set(params[0].get() * params[1].get())
        elif (opcode == 3): #input
            if(self.inputIndex >= len(self.inputValues)):
                raise IndexError('Need more inputs')
            params[0].set(self.inputValues[self.inputIndex])
            self.inputIndex-=-1
        elif (opcode == 4): #output
            self.output = params[0].get()
            self.outputs.append(self.output)
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
        elif (opcode == 9): #adjust relative base
            self.relativeBase += params[0].get()
        elif (opcode == 99): #halt
            self.halted = True
            return

        if (not ipset):
            self.ip += numberOfParametersPerOpcode[opcode] + 1

class IntcodeComputerLoop:
    def __init__(self, program, numberOfComputers, inputs):
        self.computers = []
        for i in range(numberOfComputers):
            computer = IntcodeComputer(copyIntcodeProgram(program), inputs[i])
            self.computers.append(computer)
        for i in range(numberOfComputers):
            self.computers[i].addOutputIntcodeComputer(self.computers[(i+1)%numberOfComputers])

    def run(self):
        while(1):
            for computer in self.computers:
                try:
                    while(not computer.halted):
                        computer.runInstruction()
                except IndexError:
                    pass
            if(self.computers[-1].halted): break
        return self.computers[-1].output

