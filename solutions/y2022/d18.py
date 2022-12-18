from solutions.utils.graph import neighbors6


def parse(data):
    return set(tuple(map(int, line.split(","))) for line in data.splitlines())


def part1(cubes):
    res = 0
    for x, y, z in cubes:
        res += sum(n not in cubes for n in neighbors6(x, y, z, 50))
    return res


def part2(cubes):
    water = set()
    boundery = set()
    boundery.add((0, 0, 0))
    res = 0

    while boundery:
        x, y, z = boundery.pop()
        for n in neighbors6(x, y, z, 60):
            if n in cubes:
                res += 1
            elif n not in water:
                boundery.add(n)
        water.add((x, y, z))

    return res


TEST_DATA = {}
TEST_DATA[
    """\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".rstrip()
] = (64, 58)
