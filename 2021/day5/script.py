#!/usr/bin/env python3

import os
import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def parsePoints(line):
    x = re.search("^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line) 
    return (Point(int(x.group(1)), int(x.group(2))), Point(int(x.group(3)), int(x.group(4))))

def computeLine(p1, p2, straightLinesOnly):
    vx = (p2.x - p1.x)
    vy = (p2.y - p1.y)
    s = max(abs(vx), abs(vy))
    vx /= s
    vy /= s

    if straightLinesOnly and vx != 0 and vy != 0:
        return []

    return [Point(p1.x + i * vx, p1.y + i * vy) for i in range(s + 1)]


def printVents(vents, n, m):
    string = ''
    for y in range(m + 1):
        for x in range(n + 1):
            string += str(vents.get((x, y), '.'))
        string += '\n'
    print(string)

def countVents(lines, straightLinesOnly):
    vents = {}

    n = 0
    m = 0

    for line in lines:
        (p1, p2) = parsePoints(line)
        n = max(n, max(p1.x, p2.x))
        m = max(m, max(p1.y, p2.y))
        
        line = computeLine(p1, p2, straightLinesOnly)
        for p in line:
            numVents = vents.get((p.x, p.y), 0)
            vents[(p.x, p.y)] = numVents + 1
   
    # printVents(vents, n, m)

    count = 0
    for v in vents.values():
        if v > 1:
            count += 1
    
    return count


def part1(lines):
    print(f'Part 1: {countVents(lines, True)}')


def part2(lines):
    print(f'Part 2: {countVents(lines, False)}')



def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def main():
    # inputfile = os.path.join(os.path.dirname(__file__), 'test.txt')
    inputfile = os.path.join(os.path.dirname(__file__), 'input.txt')

    lines = readInput(inputfile)

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()