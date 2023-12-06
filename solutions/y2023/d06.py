from math import ceil, floor, prod, sqrt


def solve_eq(a, b, c):
    d = sqrt(b * b - 4 * a * c)
    r0 = (-b + d) / (2 * a)
    r1 = (-b - d) / (2 * a)
    return (r0, r1)


def win_ways(time, dist):
    # t * (time - t) > dist
    # -t*t + time * t - dist > 0
    r0, r1 = solve_eq(-1, time, -dist)
    r0 = floor(r0 + 1)
    r1 = ceil(r1 - 1)
    return r1 - r0 + 1


def parse(data):
    return data.splitlines()


def part1(lines):
    lines = list(zip(*[map(int, line.split()[1:]) for line in lines]))
    return prod(win_ways(time, dist) for time, dist in lines)


def part2(lines):
    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))
    return win_ways(time, dist)


TEST_DATA = {}
TEST_DATA[
    """\
Time:      7  15   30
Distance:  9  40  200
""".rstrip()
] = (288, 71503)
