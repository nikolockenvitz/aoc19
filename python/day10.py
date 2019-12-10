# Import and Setup
from aoc import *
import math
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

d = {}
y = 0
for line in file:
    x = 0
    for el in line:
        if (el != "."):
            d[(x,y)] = 0
        x += 1
    y += 1

height = y
width = len(file[0])

# Implementation
pos = []

def isAsteroidBetween(asteroid, a2):
    if (asteroid[0] == a2[0]):
        # vertical line
        asteroidBetween = False
        for y in range(min(asteroid[1],a2[1]),
                       max(asteroid[1],a2[1])):
            if (y == asteroid[1] or y == a2[1]): continue
            if ((asteroid[0],y) in d):
                asteroidBetween = True
                break
        return asteroidBetween
    else:
        m = (asteroid[1] - a2[1]) / (asteroid[0] - a2[0])
        n = asteroid[1] - m*asteroid[0]
        asteroidBetween = False
        x = min(asteroid[0],a2[0])
        while(x < max(asteroid[0],a2[0])):
            if (x == asteroid[0] or x == a2[0]):
                x += 1
                continue
            y = m*x + n
            y = round(y,5)
            if ((x,y) in d):
                asteroidBetween = True
                break
            x += 1
        return asteroidBetween

def part1():
    global pos
    result = 0
    for asteroid in d.keys():
        detectableAsteroids = 0
        # find all other asteroids
        for a2 in d.keys():
            if(asteroid == a2): continue
            if (not isAsteroidBetween(asteroid, a2)):
                detectableAsteroids -=- 1
        if(detectableAsteroids > result):
            pos = [asteroid[0], asteroid[1]]
        result = max(result, detectableAsteroids)
    return result

def part2():
    del d[(pos[0],pos[1])]

    degrees = {}
    for el in d.keys():
        [x,y] = el
        theta_radians = math.atan2(x-pos[0], pos[1]-y)
        theta_degrees = math.degrees(theta_radians)%360
        degrees[(x,y)] = theta_degrees

    thetas = list(degrees.values())
    thetas.sort()

    destroyedAsteroids = 0
    while(1):
        oldTheta = -1
        for theta in thetas:
            if (theta == oldTheta): continue
            # find asteroid for that theta and destroy
            asteroidPositions = list(d.keys())
            for a in asteroidPositions:
                if(degrees[a] == theta and not isAsteroidBetween(pos, a)):
                    destroyedAsteroids-=-1
                    if(destroyedAsteroids == 299):
                        return 100*a[0] + a[1]
                    oldTheta = theta
                    del d[a]
                    del degrees[a]
                    break
    

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
