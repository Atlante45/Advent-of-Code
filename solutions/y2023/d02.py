import re


def parse(data):
    return data.splitlines()


CUBES = {"red": 12, "green": 13, "blue": 14}

PATTERN = "(\d+) {color}"


def part1(lines):
    sum = 0
    for i in range(len(lines)):
        sum += i + 1
        for color, num in CUBES.items():
            dices = map(int, re.findall(PATTERN.format(color=color), lines[i]))
            if max(dices) > num:
                sum -= i + 1
                break
    return sum


def part2(lines):
    sum = 0
    for i in range(len(lines)):
        power = 1
        for color, _ in CUBES.items():
            dices = map(int, re.findall(PATTERN.format(color=color), lines[i]))
            power *= max(dices)
        sum += power

    return sum


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
