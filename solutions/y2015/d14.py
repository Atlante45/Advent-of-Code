from collections import defaultdict


import re

REGEX = r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."


def distance(speed, t1, t2, duration):
    time_speeding = t1 * (duration // (t1 + t2)) + min(t1, (duration % (t1 + t2)))
    return speed * time_speeding


def step(speed, t1, t2, t):
    return speed if t % (t1 + t2) < t1 else 0


def parse(data):
    deers = {}
    for line in data.splitlines():
        deer, speed, t1, t2 = re.search(REGEX, line).groups()
        deers[deer] = (int(speed), int(t1), int(t2))

    DURATION = 2503 if len(deers) > 2 else 1000

    return deers, DURATION


def part1(deers, duration):
    return max(distance(*deer, duration) for deer in deers.values())


def part2(deers, duration):
    positions = defaultdict(int)
    points = defaultdict(int)

    for t in range(duration):
        first = 0
        for name, stats in deers.items():
            positions[name] += step(*stats, t)
            first = max(first, positions[name])

        for name, pos in positions.items():
            if pos == first:
                points[name] += 1

    return max(points.values())


TEST_DATA = {}
TEST_DATA[
    """\
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".rstrip()
] = (1120, 689)
