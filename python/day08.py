# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile()

width = 25
height = 6

layers = len(file)//(width*height)

# Implementation
def part1():
    result = [None, 0] # 0, 1*2
    for i in range(layers):
        sub = file[i*(width*height):(i+1)*(width*height)]
        z = sub.count("0")
        if(result[0] == None or z < result[0]):
            result = [z, sub.count("1")*sub.count("2")]
    return result[1]

def part2():
    p = []
    for i in range(height):
        p.append([])
        for j in range(width):
            p[i].append(2)
    for i in range(layers):
        x,y = 0, 0
        for pixel in file[i*(width*height):(i+1)*(width*height)]:
            if(p[y][x] == 2): p[y][x] = int(pixel)
            x += 1
            if (x >= width):
                x = 0
                y += 1
    for c in [0,1]:
        print(["black:","white:"][c])
        for y in range(height):
            for x in range(width):
                if(p[y][x] == c):
                    print("#",end="")
                else:
                    print(" ",end="")
            print("")
        print("")
    return

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
