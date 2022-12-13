import re


def parse_line(line):
    a, b, c, d = list(map(int, re.search(r"^(\d+)-(\d+),(\d+)-(\d+)", line).groups()))
    return [(a, b), (c, d)]


def contained(sections):
    s1, s2 = sections
    low = max(s1[0], s2[0])
    high = min(s1[1], s2[1])
    return (low, high) == s1 or (low, high) == s2


def overlap(sections):
    s1, s2 = sections
    low = max(s1[0], s2[0])
    high = min(s1[1], s2[1])
    return low <= high


def compute(sections, func):
    return len(list(filter(func, sections)))


def parse(data):
    return [parse_line(line) for line in data.splitlines()]


def part1(input):
    return compute(input, contained)


def part2(input):
    return compute(input, overlap)


TEST_DATA = {}
TEST_DATA[
    """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".rstrip()
] = (2, 4)
