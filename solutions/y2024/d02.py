from itertools import pairwise


def parse(data):
    return [list(map(int, line.split())) for line in data.splitlines()]


def is_safe(line):
    diffs = [x - y for x, y in pairwise(line)]
    return all(x * y > 0 for x, y in pairwise(diffs)) and all(
        abs(x) >= 1 and abs(x) <= 3 for x in diffs
    )


def part1(lines):
    return sum(is_safe(line) for line in lines)


def part2(lines):
    safe = 0
    for line in lines:
        if any(is_safe(line[:i] + line[i + 1 :]) for i in range(len(line))):
            safe += 1
    return safe


TEST_DATA = {}
TEST_DATA[
    """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".rstrip()
] = (2, 4)
