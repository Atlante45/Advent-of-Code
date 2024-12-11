from solutions.utils.graph import neighbors4


def parse(data):
    return [list(map(int, line)) for line in data.splitlines()]


def recurse(lines, i, j):
    val = lines[i][j]

    if val == 9:
        s = set()
        s.add((i, j))
        return s

    count = set()
    for a, b in neighbors4(i, j, len(lines), len(lines[0])):
        if lines[a][b] == val + 1:
            count |= recurse(lines, a, b)

    return count

def recurse2(lines, i, j):
    val = lines[i][j]

    if val == 9:
        return 1

    count = 0
    for a, b in neighbors4(i, j, len(lines), len(lines[0])):
        if lines[a][b] == val + 1:
            count += recurse2(lines, a, b)

    return count


def part1(lines):
    total = 0
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 0:
                total += len(recurse(lines, i, j))

    return total


def part2(lines):
    total = 0
    for i, line in enumerate(lines):
        for j, cell in enumerate(line):
            if cell == 0:
                total += recurse2(lines, i, j)

    return total


TEST_DATA = {}
# TEST_DATA[
#     """\
# 1110111
# 1111111
# 1112111
# 6543456
# 7111117
# 8111118
# 9111119
# """.rstrip()
# ] = (2, None)
# TEST_DATA[
#     """\
# 1011911
# 2111811
# 3111711
# 4567654
# 1118113
# 1119112
# 1111101
# """.rstrip()
# ] = (2, None)
TEST_DATA[
    """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".rstrip()
] = (36, 81)
