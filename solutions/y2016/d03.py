from more_itertools import chunked


def parse(data):
    return [[int(v) for v in line.split()] for line in data.splitlines()]


def part1(lines):
    return sum(1 for a, b, c in lines if a + b > c and a + c > b and b + c > a)


def part2(lines):
    count = 0
    for a, b, c in chunked(lines, 3):
        for i, j, k in zip(a, b, c):
            if i + j > k and i + k > j and j + k > i:
                count += 1
    return count


TEST_DATA = {}
TEST_DATA[
    """\
5 10 25
""".rstrip()
] = (0, None)
TEST_DATA[
    """\
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
""".rstrip()
] = (None, 6)
