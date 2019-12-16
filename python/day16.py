# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile()

# Implementation
def part1():
    result = 0
    digits = [int(n) for n in file]
    for i in range(100):
        newdigits = []
        for j in range(len(digits)):
            cur = 0
            k = j
            p = 1
            while(1):
                if ((k+1)%(2*(j+1)) == 0):
                    k += j+1
                    p *= -1
                if(k >= len(digits)): break
                cur += p * digits[k]
                k += 1
            newdigits.append(abs(cur)%10)
        digits = newdigits
    for d in digits[:8]:
        result *= 10
        result += d
    return result

def part2():
    result = 0
    repeat = 10000
    offset = int(file[:7])
    length = repeat*len(file) - offset
    digits = []
    for i in range(offset, offset+length):
        digits.append(int(file[i%len(file)]))
    for i in range(100):
        for j in range(length-2,-1,-1):
            digits[j] = (digits[j] + digits[j+1])%10
    for d in digits[:8]:
        result *= 10
        result += d
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
