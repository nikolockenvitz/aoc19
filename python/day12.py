# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

class Moon:
    def __init__(self, line):
        self.px = int(line.split("x=")[1].split(",")[0])
        self.py = int(line.split("y=")[1].split(",")[0])
        self.pz = int(line.split("z=")[1].split(">")[0])
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __repr__(self):
        return "pos=<x="+str(self.px)+", y="+str(self.py)+", z="+str(self.pz)+">, vel=<x="+str(self.vx)+", y="+str(self.vy)+", z="+str(self.vz)+">"

moons = []
for line in file:
    moons.append(Moon(line))

# Implementation
def applyGravity():
    for i in range(len(moons)):
        for j in range(i+1,len(moons)):
            if (moons[i].px < moons[j].px):
                moons[i].vx += 1
                moons[j].vx -= 1
            elif (moons[i].px > moons[j].px):
                moons[i].vx -= 1
                moons[j].vx += 1
            if (moons[i].py < moons[j].py):
                moons[i].vy += 1
                moons[j].vy -= 1
            elif (moons[i].py > moons[j].py):
                moons[i].vy -= 1
                moons[j].vy += 1
            if (moons[i].pz < moons[j].pz):
                moons[i].vz += 1
                moons[j].vz -= 1
            elif (moons[i].pz > moons[j].pz):
                moons[i].vz -= 1
                moons[j].vz += 1

def applyVelocity():
    for i in range(len(moons)):
        moons[i].px += moons[i].vx
        moons[i].py += moons[i].vy
        moons[i].pz += moons[i].vz

def getTotalEnergy():
    totalEnergy = 0
    for i in range(len(moons)):
        pot = abs(moons[i].px) + abs(moons[i].py) + abs(moons[i].pz)
        kin = abs(moons[i].vx) + abs(moons[i].vy) + abs(moons[i].vz)
        totalEnergy += pot*kin
    return totalEnergy

def part1():
    for i in range(1000):
        applyGravity()
        applyVelocity()
    return getTotalEnergy()

def part2():
    result = 0
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
