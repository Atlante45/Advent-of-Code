#!/usr/bin/env python3
import os


def render(holes):
    maximum = max(holes)

    render = ''
    for y in range(maximum[1] + 1):
        for x in range(maximum[0] + 1):
            render += '#' if (x, y) in holes else '.'
        render += '\n'

    return render

def fold(holes, axis, val):
    folded = set()
    for hole in holes:
        if axis == 'x' and hole[0] > val:
            folded.add((val - (hole[0] - val), hole[1]))
        elif axis == 'y' and hole[1] > val:
            folded.add((hole[0], val - (hole[1] - val)))
        else:
            folded.add(hole)

    return list(folded)


def part1(holes, folds):
    holes = fold(holes, folds[0][0], folds[0][1])
    return len(holes)

def part2(holes, folds):
    for axis, val in folds:
        holes = fold(holes, axis, val)
    return '\n' + render(holes)


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        holes = []
        folds = []
        for line in input:
            if line.startswith('fold'):
                [a, b] = line.strip().split()[-1].split('=')
                folds += [(a, int(b))]
            elif len(line) > 1:
                [x, y] = [int(x) for x in line.strip().split(',')]
                holes += [(x, y)]

        print(f'Solving {filename}')
        print(f"    Part 1: {part1(holes, folds)}")
        print(f"    Part 2: {part2(holes, folds)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
