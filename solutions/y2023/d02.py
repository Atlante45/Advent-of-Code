from math import prod
import re


COLORS = ["red", "green", "blue"]
CUBES = [12, 13, 14]

PATTERN = "(\\d+) {color}"


def parse_line(line):
    cubes = [
        max(map(int, re.findall(PATTERN.format(color=color), line))) for color in COLORS
    ]
    return cubes, all([c <= C for c, C in zip(cubes, CUBES)])


def parse(data):
    return [parse_line(line) for line in data.splitlines()]


def part1(games):
    return sum(i + 1 for i, (_, valid) in enumerate(games) if valid)


def part2(games):
    return sum(prod(cubes) for cubes, _ in games)


TEST_DATA = {}
TEST_DATA[
    """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".rstrip()
] = (8, 2286)
