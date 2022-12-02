#!/usr/local/bin/python3
import os

def part1(input):
    res = 0

    cur = 0
    for line in input:
        if line:
            cur += int(line)
        else:
            res = max(res, cur)
            cur = 0

    return res

def part2(input):
    cals = []
    cur = 0
    for line in input:
        if line:
            cur += int(line)
        else:
            cals += [cur]
            cur = 0

    cals = sorted(cals)
    return sum(cals[-3:])


def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

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
