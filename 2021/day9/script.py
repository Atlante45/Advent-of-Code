#!/usr/bin/env python3
import os

def findNeighbors(heighmap, i, j):
    neighbors = []
    height = len(heighmap)
    width = len(heighmap[0])
    if i > 0:
        neighbors.append((i - 1, j))
    if i < height - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < width - 1:
        neighbors.append((i, j + 1))

    return neighbors

def findLowestPoints(heighmap):
    lowestPoints = []
    height = len(heighmap)
    width = len(heighmap[0])
    for i in range(height):
        for j in range(width):
            lowest = True
            for (i1, j1) in findNeighbors(heighmap, i, j):
                if heighmap[i][j] >= heighmap[i1][j1]:
                    lowest = False
                    break
            if lowest:
                lowestPoints += [(i, j)]

    return lowestPoints

def computeBasin(heighmap, i, j):
    res = 1
    heighmap[i][j] = 9
    for (i1, j1) in findNeighbors(heighmap, i, j):
        if heighmap[i1][j1] != 9:
            res += computeBasin(heighmap, i1, j1)

    return res


def part1(heighmap):
    res = 0

    for (i, j) in findLowestPoints(heighmap):
        res += 1 + heighmap[i][j]

    return res

def part2(heighmap):
    res = 0

    basins = []

    for (i, j) in findLowestPoints(heighmap):
        basins.append(computeBasin(heighmap, i, j))

    basins = sorted(basins)
    return basins[-3] * basins[-2] * basins[-1]


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    heighmap = []
    for line in input:
        heighmap.append([int(v) for v in line.strip()])

    if input:
        print(f'Solving {filename}')
        print(f"    Part 1: {part1(heighmap)}")
        print(f"    Part 2: {part2(heighmap)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
