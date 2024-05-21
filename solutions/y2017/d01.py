from itertools import pairwise


def parse(data):
    return data.strip()


def part1(captcha):
    return sum(int(a) for a, b in pairwise(captcha + captcha[0]) if a == b)


def part2(lines):
    L = len(lines)
    return sum(int(lines[i]) for i in range(L) if lines[i] == lines[(i + L // 2) % L])


TEST_DATA = {}
TEST_DATA[
    """\
91212129
""".rstrip()
] = (9, None)
TEST_DATA[
    """\
12131415
""".rstrip()
] = (None, 4)
