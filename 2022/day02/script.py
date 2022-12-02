#!/usr/local/bin/python3
import os

def part1(input):
    res = 0

    for (adv, me) in input:
        res += me + 1
        if (adv + 1) % 3 == me:
            res += 6
        elif adv == me:
            res += 3

    return res

def part2(input):
    res = 0

    for (adv, end) in input:
        if end == 0:
            res += 0 + 1 + (adv + 2) % 3
        elif end == 1:
            res += 3 + 1 + adv
        else:
            res += 6 + 1 + (adv + 1) % 3

    return res


def readInput(filename):
    with open(filename) as f:
        return [(ord(line[0]) - ord('A'), ord(line[2]) - ord('X')) for line in f.readlines()]

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
