from itertools import accumulate


def parse(data):
    return data.splitlines()


def part1(lines):
    lines = list(zip(*[map(int, line.split()[1:]) for line in lines]))

    res = 1
    for time, dist in lines:
        ways = 0
        for t in range(time):
            if t * (time - t) > dist:
                ways += 1

        res *= ways

    return res


def part2(lines):
    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))

    ways = 0
    for t in range(time):
        if t * (time - t) > dist:
            ways += 1
    return ways


TEST_DATA = {}
TEST_DATA[
    """\
Time:      7  15   30
Distance:  9  40  200
""".rstrip()
] = (288, 71503)
