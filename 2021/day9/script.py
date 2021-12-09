#!/usr/bin/env python3
import os
import copy


def part1(input):
    res = 0

    hm = []
    for line in input:
        hm.append([int(v) for v in line.strip()])

    for i in range(len(hm)):
        for j in range(len(hm[0])):
            if i > 0 and hm[i][j] >= hm[i - 1][j]:
                continue
            if i < len(hm) - 1 and hm[i][j] >= hm[i + 1][j]:
                continue
            if j > 0 and hm[i][j] >= hm[i][j - 1]:
                continue
            if j < len(hm[0]) - 1 and hm[i][j] >= hm[i][j + 1]:
                continue


    # print(hm)

    return res


def neigh(hm, i, j):
    n = []
    if i > 0:
        n.append((i - 1, j))
    if i < len(hm) - 1:
        n.append((i + 1, j))
    if j > 0:
        n.append((i, j - 1))
    if j < len(hm[0]) - 1:
        n.append((i, j + 1))

    return n

def spread(hm, i, j):
    res = 0
    for (i1, j1) in neigh(hm, i, j):
        if hm[i1][j1] >= hm[i][j]:
            continue

        hm[i1][j1] = 9
        res += 1 + spread(hm, i1, j1)
    return res


def computeBasin(hm, i, j):
    hm = copy.deepcopy(hm)

    hm[i][j] = 9
    return 1 + spread(hm, i, j)


def part2(input):
    res = 0

    basins = []
    hm = []
    for line in input:
        hm.append([int(v) for v in line.strip()])

    for i in range(len(hm)):
        for j in range(len(hm[0])):
            if i > 0 and hm[i][j] >= hm[i - 1][j]:
                continue
            if i < len(hm) - 1 and hm[i][j] >= hm[i + 1][j]:
                continue
            if j > 0 and hm[i][j] >= hm[i][j - 1]:
                continue
            if j < len(hm[0]) - 1 and hm[i][j] >= hm[i][j + 1]:
                continue

            basins.append(computeBasin(hm, i, j))


    basins = sorted(basins)
    print(basins)
    print(basins[-1], basins[-2], basins[-3])

    return basins[-1] * basins[-2] * basins[-3]


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        print(f'Solving {filename}')
        print(f"    Part 1: {part1(input)}")
        print(f"    Part 2: {part2(input)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
