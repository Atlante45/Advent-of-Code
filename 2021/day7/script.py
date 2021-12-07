#!/usr/bin/env python3
from math import floor
import os

def computeCost(pos, fuelCost):
    minCost = None
    for i in range(min(pos), max(pos) + 1):
        cost = sum([fuelCost(abs(i - n)) for n in pos])
        if minCost and cost > minCost:
            return minCost
        minCost = cost

def part1(pos):
    return computeCost(pos, lambda n: n)


def part2(pos):
    return computeCost(pos, lambda n: int((n * (n + 1)) / 2))


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    pos = [int(v) for v in input[0].split(',')]

    if input:
        print(f'Solving {filename}')
        print(f"    Part 1: {part1(pos)}")
        print(f"    Part 2: {part2(pos)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
