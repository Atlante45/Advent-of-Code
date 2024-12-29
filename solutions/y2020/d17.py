from itertools import product


def parse(data):
    cubes = set()
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                cubes.add((x, y, 0))
    return cubes


def neighbors(cube):
    for dc in product(range(-1, 2), repeat=len(cube)):
        if all(d == 0 for d in dc):
            continue
        yield tuple(c + d for c, d in zip(cube, dc))


def step(cubes):
    new_cubes = set()
    to_check = set()
    for cube in cubes:
        ns = set(neighbors(cube))
        to_check.update(ns)
        active = len(set.intersection(ns, cubes))
        if active in (2, 3):
            new_cubes.add(cube)

    for cube in to_check:
        ns = set(neighbors(cube))
        active = len(set.intersection(ns, cubes))
        if active == 3:
            new_cubes.add(cube)

    return new_cubes


def part1(cubes):
    for _ in range(6):
        cubes = step(cubes)
    return len(cubes)


def part2(cubes):
    cubes = set((*cube, 0) for cube in cubes)
    for _ in range(6):
        cubes = step(cubes)
    return len(cubes)


TEST_DATA = {}
TEST_DATA[
    """\
.#.
..#
###
""".rstrip()
] = (112, 848)
