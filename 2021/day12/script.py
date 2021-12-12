#!/usr/bin/env python3
import os

def dfs(path, links, canRevis):
    if path[-1] == 'end':
        return 1
    if path[-1] == 'start' and len(path) > 1:
        return 0

    res = 0

    for n in links[path[-1]]:
        revis = any(c for c in n if c.islower()) and n in path
        if revis and not canRevis:
            continue
        res += dfs(path + [n], links, canRevis and not revis)

    return res

def part1(links):
    return dfs(['start'], links, False)

def part2(links):
    return dfs(['start'], links, True)


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        links = {}
        for line in input:
            a, b = line.strip().split('-')
            links[a] = links.get(a, []) + [b]
            links[b] = links.get(b, []) + [a]

        print(f'Solving {filename}')
        print(f"    Part 1: {part1(links)}")
        print(f"    Part 2: {part2(links)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
