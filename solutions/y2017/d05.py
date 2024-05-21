from itertools import count


def parse(data):
    return [int(v) for v in data.splitlines()]


def part1(lines):
    iptr = 0
    for step in count(1):
        lines[iptr] += 1
        iptr += lines[iptr] - 1
        if iptr < 0 or iptr >= len(lines):
            return step


def part2(lines):
    iptr = 0
    for step in count(1):
        jump = lines[iptr]
        lines[iptr] += 1 if jump < 3 else -1
        iptr += jump
        if iptr < 0 or iptr >= len(lines):
            return step


TEST_DATA = {}
TEST_DATA[
    """\
0
3
0
1
-3
""".rstrip()
] = (5, 10)
