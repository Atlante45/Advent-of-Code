from more_itertools import pairwise


def parse(data):
    return [list(map(int, line.split())) for line in data.splitlines()]


def part1(lines):
    res = 0
    for line in lines:
        all_lines = [line]
        current = line
        while not all(v == 0 for v in current):
            current = [b - a for a, b in pairwise(current)]
            all_lines += [current]
        res += sum(a[-1] for a in all_lines)

        # print(all_lines)

    return res


def part2(lines):
    res = 0
    for line in lines:
        all_lines = [line]
        current = line
        while not all(v == 0 for v in current):
            current = [b - a for a, b in pairwise(current)]
            all_lines += [current]
        p = 0
        for a in reversed(all_lines):
            p = a[0] - p
            # print(p)
        res += p

        # print(all_lines)

    return res


TEST_DATA = {}
TEST_DATA[
    """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".rstrip()
] = (114, 2)
