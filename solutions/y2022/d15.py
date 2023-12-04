import re

REGEX = re.compile(r"(-?\d+)")


def numbers(string):
    return [int(v) for v in REGEX.findall(string)]


def overlap(s1, s2):
    low = max(s1[0], s2[0])
    high = min(s1[1], s2[1])
    return low <= high


def merge(s1, s2):
    low = min(s1[0], s2[0])
    high = max(s1[1], s2[1])
    return (low, high)


def add_range(ranges, new, max_c):
    if max_c is not None:
        if new[0] > max_c or new[1] < 0:
            return ranges
        new = max(0, new[0]), min(max_c, new[1])

    for r in ranges:
        if overlap(r, new):
            ranges.remove(r)
            return add_range(ranges, merge(r, new), max_c)
    return ranges + [new]


def compute(sensors, dist, max_c=None):
    ranges = []
    for (sx, sy), range in sensors.items():
        rem = range - abs(sy - dist)
        if rem >= 0:
            ranges = add_range(ranges, (sx - rem, sx + rem), max_c)
    return ranges


def parse(data):
    lines = data.splitlines()
    sensors = {}
    for line in lines:
        sx, sy, bx, by = numbers(line)
        sensors[(sx, sy)] = abs(sx - bx) + abs(sy - by)
    return sensors, len(lines) == 14


def part1(sensors, is_test):
    ranges = compute(sensors, 10 if is_test else 2000000)
    return sum(e - s for s, e in ranges)


def part2(sensors, is_test):
    max_c = 20 if is_test else 4000000
    for y in range(max_c):
        ranges = compute(sensors, y, max_c)
        if len(ranges) > 1:
            # print(ranges)
            return 4000000 * min(r[1] + 1 for r in ranges) + y


TEST_DATA = {}
TEST_DATA[
    """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".rstrip()
] = (26, 56000011)
