#!/usr/local/bin/python3
import copy
import os

def part1(input):
    res = 0
    while True:
        moved = False
        new_input = copy.deepcopy(input)
        for i in range(len(input)):
            for j in range(len(input[0])):
                j2 = (j + 1) % len(input[0])
                if input[i][j] == '>' and input[i][j2] == '.':
                    new_input[i][j] = '.'
                    new_input[i][j2] = '>'
                    moved = True

        input = new_input
        new_input = copy.deepcopy(input)

        for i in range(len(input)):
            for j in range(len(input[0])):
                i2 = (i + 1) % len(input)
                if input[i][j] == 'v' and input[i2][j] == '.':
                    new_input[i][j] = '.'
                    new_input[i2][j] = 'v'
                    moved = True
        input = new_input

        res += 1
        if not moved:
            break

    return res

def part2(input):
    res = 0

    return res


def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        input = [list(line) for line in input]

        print(f'Solving {filename}')
        print(f"    Part 1: {part1(input)}")
        print(f"    Part 2: {part2(input)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
