#!/usr/local/bin/python3
import os

def priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def part1(input):
    res = 0

    for line in input:
        mid = int(len(line) / 2)
        first = line[:mid]
        second = line[mid:]
        for item in first:
            if item in second:
                res += priority(item)
                break

    return res

def part2(input):
    res = 0

    for i in range(int(len(input)/3)):
        for c in input[3*i]:
            if c in input[3*i + 1] and c in input[3*i + 2]:
                res += priority(c)
                break

    return res


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
