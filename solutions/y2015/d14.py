#!/usr/bin/env python3
from collections import defaultdict
from solutions.utils import logger
from aocd import data

import re

REGEX = r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."


def distance(speed, t1, t2, duration):
    time_speeding = t1 * (duration // (t1 + t2)) + min(t1, (duration % (t1 + t2)))
    return speed * time_speeding


def step(speed, t1, t2, t):
    return speed if t % (t1 + t2) < t1 else 0


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


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    DURATION = 2503 if name == "input" else 1000

    deers = {}
    for line in data:
        deer, speed, t1, t2 = re.search(REGEX, line).groups()
        deers[deer] = (int(speed), int(t1), int(t2))

    ans_1 = part1(deers, DURATION)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(deers, DURATION)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (2660, 1256)
TEST_RESULT = (1120, 689)
TEST_DATA = """\
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
