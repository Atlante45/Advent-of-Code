#!/usr/bin/env python3
import os

chars = {
    '<': '>',
    '[': ']',
    '{': '}',
    '(': ')'
}

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

vals = {
    '<': 4,
    '[': 2,
    '{': 3,
    '(': 1
}

def part1(input):
    res = 0

    stack = []
    for line in input:
        for c in line.strip():
            if c in chars.keys():
                stack.append(c)
            elif chars[stack.pop()] != c:
                res += score[c]
                break
        stack.clear()

    return res

def part2(input):
    res = 0

    scores = []

    stack = []
    for line in input:
        skip = False
        for c in line.strip():
            if c in chars.keys():
                stack.append(c)
            elif chars[stack.pop()] != c:
                skip = True
                break

        if not skip:
            score = 0
            for i in reversed(stack):
                score = 5 * score + vals[i]
            scores.append(score)

        stack.clear()

    scores = sorted(scores)

    return scores[len(scores) // 2]


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
