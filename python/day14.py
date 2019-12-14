# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

class Chemical:
    def __init__(self, text):
        self.amount = int(text.split()[0])
        self.name = text.split()[1]

    def __repr__(self):
        return str(self.amount)+" "+self.name

d = {}
for line in file:
    inputs = []
    left = line.split(" => ")[0]
    for t in left.split(", "):
        inputs.append(Chemical(t))
    right = line.split(" => ")[1]
    amount = int(right.split()[0])
    product = right.split()[1]
    d[product] = [amount, inputs]

ore = "ORE"

# Implementation
def h(name, amount, reactions):
    inputs = d[name][1]
    n = amount // d[name][0]
    if (amount % d[name][0]): n += 1
    r = 0
    reactions.append([n, Chemical(str(d[name][0])+" "+name), aoc.copyList(inputs)])
    for el in inputs:
        if (el.name == ore): return n*el.amount
        r += h(el.name, n*el.amount, reactions)
    return r
    
def part1(fuel=1, part2additionalChemicals=None):
    result = 0
    reactions = []
    maxore = h("FUEL",fuel,reactions)
    p = {ore: maxore}
    for i in range(len(reactions)-1,-1,-1):
        r = reactions[i]
        el = r[1].name
        if (el in p):
            p[el] += r[0]*r[1].amount
        else:
            p[el] = r[0]*r[1].amount
        for inp in r[2]:
            p[inp.name] -= r[0]*inp.amount

    if (part2additionalChemicals != None):
        for k in part2additionalChemicals.keys():
            p[k] += part2additionalChemicals[k]

    # revert reactions
    while(1):
        stop = True
        for k in p.keys():
            if (k == ore or k == "FUEL"): continue
            if (p[k] >= d[k][0]):
                n = p[k] // d[k][0]
                p[k] -= n*d[k][0]
                for inp in d[k][1]:
                    p[inp.name] += n*inp.amount
                stop = False
        if (stop): break
    
    result = maxore - p[ore]
    if (part2additionalChemicals == None):
        return result
    else:
        return [result, p]

def part2():
    result = 0
    remainingOre = 1000000000000
    remainingChemicals = {}
    orePerFuel = part1()
    while(1):
        fuel = max(1,remainingOre//orePerFuel)
        usedOre, remaining = part1(fuel, remainingChemicals)
        remainingOre -= usedOre
        if (remainingOre < 0): break
        result += fuel
        for k in remaining.keys():
            if (k == ore or k == "FUEL"): continue
            remainingChemicals[k] = remaining[k]
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
