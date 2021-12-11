#!/usr/bin/env python3
import os



def neighbors(i, j, max_i, max_j):
    cells = [
        (i - 1, j - 1),
        (i + 1, j + 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ]

    return [(x, y) for (x, y) in cells if x >= 0 and x < max_i and y >= 0 and y < max_j]

def step(energy, i, j):
    res = 0

    if energy[i][j] > 9:
        return 0

    energy[i][j] += 1
    if energy[i][j] > 9:
        res += 1
        for (x, y) in neighbors(i, j, len(energy), len(energy[0])):
            res += step(energy, x, y)

    return res

def part1(input):
    res = 0

    energy = []
    for line in input:
        energy.append([int(v) for v in line.strip()])

    for _ in range(100):
        for i in range(len(energy)):
            for j in range(len(energy[0])):
                res += step(energy, i, j)

        for i in range(len(energy)):
            for j in range(len(energy[0])):
                if energy[i][j] > 9:
                    energy[i][j] = 0


    return res

def part2(input):
    res = 0

    energy = []
    for line in input:
        energy.append([int(v) for v in line.strip()])

    for n in range(10000000):
        for i in range(len(energy)):
            for j in range(len(energy[0])):
                res += step(energy, i, j)

        count = 0
        for i in range(len(energy)):
            for j in range(len(energy[0])):
                if energy[i][j] > 9:
                    count += 1
                    energy[i][j] = 0

        if count == len(energy) * len(energy[0]):
            return n + 1

    return res


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
