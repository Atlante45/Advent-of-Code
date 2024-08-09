from itertools import cycle


def parse(data):
    return list(map(int, data.splitlines()))


def part1(lines):
    return sum(lines)


def part2(lines):
    frequencies = set()
    frequency = 0
    for i in cycle(lines):
        frequency += i
        if frequency in frequencies:
            return frequency
        frequencies.add(frequency)


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
