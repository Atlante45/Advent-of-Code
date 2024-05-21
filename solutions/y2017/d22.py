def parse(data):
    lines = data.splitlines()
    assert len(lines) == len(lines[0])
    assert len(lines) % 2 == 1

    offset = len(lines) // 2

    infected = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                infected.add((x - offset, y - offset))
    return infected


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part1(infected):
    pos = (0, 0)
    dir = 0

    infections = 0
    for _ in range(10000):
        if pos in infected:
            dir = (dir + 1) % 4
            infected.remove(pos)
        else:
            dir = (dir - 1) % 4
            infected.add(pos)
            infections += 1

        pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])

    return infections


def part2(infected):
    states = {pos: 2 for pos in infected}

    pos = (0, 0)
    dir = 0

    infections = 0
    for _ in range(10_000_000):
        state = states.get(pos, 0)

        dir = (dir + state - 1) % 4
        new_state = (state + 1) % 4

        states[pos] = new_state

        if new_state == 2:
            infections += 1

        pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])

    return infections


TEST_DATA = {}
TEST_DATA[
    """\
..#
#..
...
""".rstrip()
] = (5587, 2511944)
