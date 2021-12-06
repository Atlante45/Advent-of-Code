#!/usr/bin/env python3

import os

def readInput(filename):
    with open(filename) as f:
        return f.readlines()


def count(input, gens):
    ageCounts = [0] * 9
    for i in range(9):
        ageCounts[i] = input.count(i)

    for _ in range(gens):
        replicatingFish = ageCounts.pop(0)
        ageCounts[6] += replicatingFish
        ageCounts.append(replicatingFish)

    return sum(ageCounts)

def main():
    inputfile = os.path.join(os.path.dirname(__file__), 'test.txt')
    # inputfile = os.path.join(os.path.dirname(__file__), 'input.txt')

    lines = readInput(inputfile)

    ages = [int(v) for v in lines[0].split(',')]

    print(f"Part 1: {count(ages, 80)}")
    print(f"Part 2: {count(ages, 256)}")

if __name__ == "__main__":
    main()
