#!/usr/bin/env python3
import copy
import os


# segments = {
#     1: "cf",
#     7: "acf",
#     4: "bcdf",
#     2: "acdeg",
#     3: "acdfg",
#     5: "abdfg",
#     6: "abdefg",
#     9: "abcdfg",
#     0: "abcefg",
#     8: "abcdefg",
# }

def sub(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3

def part1(input):
    total = 0
    for line in input:
        line = line.strip().split('|')[1].split()
        for i in line:
            if len(i) in [2, 4, 3, 7]:
                total += 1

    return total

def part2(input):
    total = 0
    for line in input:
        [pattern, key] = line.strip().split('|')
        pattern = pattern.split()
        key = key.split()

        pattern.sort(key=len)

        value = 0
        for i in key:
            if len(i) == 2:
                value += 1
            elif len(i) == 3:
                value += 7
            elif len(i) == 4:
                value += 4
            elif len(i) == 7:
                value += 8
            elif len(i) == 5:
                if len(sub(i, pattern[2])) == 3:
                    value += 2
                elif len(sub(i, pattern[0])) == 3:
                    value += 3
                else:
                    value += 5
            elif len(i) == 6:
                if len(sub(i, pattern[0])) == 5:
                    value += 6
                elif len(sub(i, pattern[2])) == 2:
                    value += 9
                else:
                    value += 0
            else:
                print("ERROR")
            value *= 10

        value = value//10
        print(f"{key} - {value}")
        total += value

    return total


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
