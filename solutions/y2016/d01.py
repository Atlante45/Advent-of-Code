from solutions.utils.graph import p, v


def parse(data):
    return data.split(", ")


DIR = [v(1, 0), v(0, 1), v(-1, 0), v(0, -1)]
TURN = {"L": -1, "R": 1}


def part1(sequence):
    dir = 0
    pos = p(0, 0)

    for step in sequence:
        dir = (dir + TURN[step[0]]) % 4
        pos += DIR[dir] * int(step[1:])

    return abs(pos[0]) + abs(pos[1])


def part2(sequence):
    dir = 0
    pos = p(0, 0)

    visited = set()
    visited.add(tuple(pos))
    for step in sequence:
        dir = (dir + TURN[step[0]]) % 4
        for _ in range(int(step[1:])):
            pos += DIR[dir]
            if tuple(pos) in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.add(tuple(pos))


TEST_DATA = {}
TEST_DATA[
    """\
R2, L3
""".rstrip()
] = (5, None)
TEST_DATA[
    """\
R2, R2, R2
""".rstrip()
] = (2, None)
TEST_DATA[
    """\
R5, L5, R5, R3
""".rstrip()
] = (12, None)
TEST_DATA[
    """\
R8, R4, R4, R8
""".rstrip()
] = (None, 4)
