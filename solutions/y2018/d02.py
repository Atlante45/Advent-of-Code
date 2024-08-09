from typing import Counter


def parse(data):
    return data.splitlines()


def part1(lines):
    twos = 0
    threes = 0

    for line in lines:
        counts = Counter(line).values()
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1
    return twos * threes


def part2(lines):
    for i, line1 in enumerate(lines):
        for line2 in lines[i + 1 :]:
            pot = [c1 for c1, c2 in zip(line1, line2) if c1 == c2]
            if len(pot) == len(line1) - 1:
                return "".join(pot)


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
