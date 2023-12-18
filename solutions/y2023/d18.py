from solutions.utils.graph import p, v


DIR = [v(0, 1), v(1, 0), v(0, -1), v(-1, 0)]


def shoelace(plan, parse_step):
    area = 0
    perim = 0

    pos = p(0, 0)
    for step in plan:
        dir, length = parse_step(*step)
        new_pos = pos + length * dir
        area += pos[0] * new_pos[1] - pos[1] * new_pos[0]
        perim += length
        pos = new_pos
    return abs(area) // 2 + perim // 2 + 1


def parse(data):
    return [line.split() for line in data.splitlines()]


def part1(plan):
    return shoelace(plan, lambda a, b, _: (DIR["RDLU".index(a)], int(b)))


def part2(plan):
    return shoelace(plan, lambda a, _b, c: (DIR[int(c[7])], int(c[2:7], 16)))


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
