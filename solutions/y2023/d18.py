from itertools import pairwise


DIRS = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

CONV = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def solve(lines, read):
    vertical = set()
    horizontal = set()

    pos = (0, 0)
    for line in lines:
        dir, length = read(*line.split())

        if dir in "UD":
            sign = 1 if dir == "D" else -1
            new_pos = (pos[0] + sign * length, pos[1])
            vertical.add((min(pos[0], new_pos[0]), max(pos[0], new_pos[0]), pos[1]))
        else:
            sign = 1 if dir == "R" else -1
            new_pos = (pos[0], pos[1] + sign * length)
            horizontal.add((min(pos[1], new_pos[1]), max(pos[1], new_pos[1]), pos[0]))

        pos = new_pos

    vertical = sorted(vertical, key=lambda x: x[2])
    horizontal = sorted(horizontal, key=lambda x: x[2])
    transitions = sorted(set([h[2] for h in horizontal]))
    # print(vertical)
    # print(horizontal)

    area = 0
    for i in transitions:
        inside = False
        on_perim = False
        pos_j = None
        for v1, v2, j in vertical:
            if i > v1 and i <= v2:
                inside = not inside
            if i == v1 or i == v2:
                on_perim = not on_perim
            if (inside or on_perim) and pos_j is None:
                pos_j = j
            if not inside and not on_perim and pos_j is not None:
                # print("slice ", j, pos_j, j - pos_j + 1)
                area += j - pos_j + 1
                pos_j = None

    for i1, i2 in pairwise(transitions):
        if i1 + 1 == i2:
            continue
        i = i1 + 1

        inside = False
        pos_j = None
        for v1, v2, j in vertical:
            if i > v1 and i <= v2:
                inside = not inside
                if inside:
                    pos_j = j
                else:
                    area += (j - pos_j + 1) * (i2 - i1 - 1)
                    # print("area ", j, pos_j, (j - pos_j + 1) * (i2 - i1 - 1))

    return area


def parse(data):
    return data.splitlines()


def part1(lines):
    return solve(lines, lambda a, b, _: (a, int(b)))


def part2(lines):
    return solve(lines, lambda a, _b, c: (CONV[c[7]], int(c[2:7], 16)))


TEST_DATA = {}
TEST_DATA[
    """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".rstrip()
] = (62, None)
