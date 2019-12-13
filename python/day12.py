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

def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def part1n2():
    result1, result2 = 0, 0

    ix = (moons[0].px, moons[0].vx, moons[1].px, moons[1].vx, moons[2].px, moons[2].vx, moons[3].px, moons[3].vx)
    iy = (moons[0].py, moons[0].vy, moons[1].py, moons[1].vy, moons[2].py, moons[2].vy, moons[3].py, moons[3].vy)
    iz = (moons[0].pz, moons[0].vz, moons[1].pz, moons[1].vz, moons[2].pz, moons[2].vz, moons[3].pz, moons[3].vz)
    rx,ry,rz = 0,0,0

    i = 0
    while(1):
        if (rx == 0 and ix == (moons[0].px, moons[0].vx, moons[1].px, moons[1].vx, moons[2].px, moons[2].vx, moons[3].px, moons[3].vx)):
            rx = i
        if (ry == 0 and iy == (moons[0].py, moons[0].vy, moons[1].py, moons[1].vy, moons[2].py, moons[2].vy, moons[3].py, moons[3].vy)):
            ry = i
        if (rz == 0 and iz == (moons[0].pz, moons[0].vz, moons[1].pz, moons[1].vz, moons[2].pz, moons[2].vz, moons[3].pz, moons[3].vz)):
            rz = i
        if (rx != 0 and ry != 0 and rz != 0):
            result2 = lcm(lcm(rx,ry),rz)
            break
        applyGravity()
        applyVelocity()
        i += 1
        if (i == 1000):
            result1 = getTotalEnergy()

    return [result1, result2]

# Processing
[result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
