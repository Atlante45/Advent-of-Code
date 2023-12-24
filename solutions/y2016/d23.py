from math import factorial


def parse(data):
    lines = data.splitlines()
    return int(lines[19].split()[1]) * int(lines[20].split()[1])


def part1(n):
    return n + factorial(7)


def part2(n):
    return n + factorial(12)


TEST_DATA = {}
