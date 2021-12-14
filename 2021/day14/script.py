#!/usr/bin/env python3
from cmath import nan
from collections import defaultdict
import math
import os

def step(template, pairs):
    res = ''
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        res += template[i]
        res += pairs[pair]
    res += template[-1]

    return res

def part1(template, pairs):
    res = 0

    for _ in range(10):
        template = step(template, pairs)

    counts = [template.count(i) for i in set(template)]
    return max(counts) - min(counts)

def step2(template, pairs):
    current = defaultdict(int)

    for p in template:
        current[p[0] + pairs[p]] += template[p]
        current[pairs[p] + p[1]] += template[p]

    return current


def part2(template, pairs):
    res = 0

    current = defaultdict(int)
    for i in range(len(template) - 1):
        current[template[i:i+2]] += 1

    for _ in range(40):
        current = step2(current, pairs)

    counts = defaultdict(int)
    for p in current:
        counts[p[0]] += current[p]
        counts[p[1]] += current[p]

    least = math.ceil(min(counts.values()) / 2)
    most = math.ceil(max(counts.values()) / 2)

    return most - least


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        template = input[0].strip()

        pairs = {}
        for line in input[2:]:
            (p, i) = line.strip().split(' -> ')
            pairs[p] = i


        print(f'Solving {filename}')
        print(f"    Part 1: {part1(template, pairs)}")
        print(f"    Part 2: {part2(template, pairs)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
