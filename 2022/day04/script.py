#!/usr/local/bin/python3
import os


def contained(a, b):
    return int(a[0]) <= int(b[0]) and int(b[1]) <= int(a[1])


def overlap(a, b):
    return int(a[0]) <= int(b[0]) and int(b[0]) <= int(a[1])


def part1(input):
    res = 0

    for line in input:
        sections = [section.split("-") for section in line.split(",")]
        # print(sections)
        if contained(sections[0], sections[1]) or contained(sections[1], sections[0]):
            res += 1

    return res


def part2(input):
    res = 0

    for line in input:
        sections = [section.split("-") for section in line.split(",")]
        # print(sections)
        if overlap(sections[0], sections[1]) or overlap(sections[1], sections[0]):
            res += 1

    return res


def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        print(f"Solving {filename}")
        print(f"    Part 1: {part1(input)}")
        print(f"    Part 2: {part2(input)}")


def main():
    solve("example.txt")
    solve("input.txt")


if __name__ == "__main__":
    main()
