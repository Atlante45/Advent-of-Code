#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

import itertools
import math
import re

SIZE = 100


def make_cube(start, end):
    start = [x - 0.5 for x in start]
    end = [x + 0.5 for x in end]
    return Cube(start, end)


def p_greater(p1, p2):
    return all([a < b for a, b in zip(p1, p2)])


def p_avg(points):
    return [round(sum(l) / len(points) - 0.5) + 0.5 for l in zip(*points)]


class Cube:
    def __init__(self, start, end):
        self.start = [min(a, b) for a, b in zip(start, end)]
        self.end = [max(a, b) for a, b in zip(start, end)]
        self.corners = list(itertools.product(*zip(start, end)))

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.start == other.start
            and self.end == other.end
        )

    def __repr__(self):
        return "Cube()"

    def __str__(self):
        return f"  start={self.start}\n  end={self.end}    corners={self.corners}"

    def count(self):
        return math.prod([b - a for a, b in zip(self.start, self.end)])

    def is_inside(self, other):
        return p_greater(self.start, other) and p_greater(other, self.end)

    def touches(self, other):
        start = [max(a, b) for a, b in zip(self.start, other.start)]
        end = [min(a, b) for a, b in zip(self.end, other.end)]
        return p_greater(start, end)

    def split(self, center):
        return [Cube(corner, center) for corner in self.corners]

    def opposite(self, p):
        assert p in self.corners
        x, y, z = [
            start if corner != start else end
            for start, end, corner in zip(self.start, self.end, p)
        ]
        return (x, y, z)

    def intersection(self, other):
        start = [max(a, b) for a, b in zip(self.start, other.start)]
        end = [min(a, b) for a, b in zip(self.end, other.end)]
        return Cube(start, end) if all([a < b for a, b in zip(start, end)]) else None

    def partition_point(self, other):
        try:
            return next(p for p in other.corners if self.is_inside(p))
        except StopIteration:
            common_corners = [value for value in self.corners if value in other.corners]
            num_common_corners = len(common_corners)
            if num_common_corners in [2, 4]:
                return p_avg([other.opposite(p) for p in common_corners])
            elif num_common_corners == 0:
                return p_avg(other.corners)
            else:
                print("PANIC!!!!")

    def subtract(self, other):
        sub_cube = self.intersection(other)
        if not sub_cube:
            return [self]

        if self == sub_cube:
            return []

        p = self.partition_point(sub_cube)
        new_cubes = [cube.subtract(sub_cube) for cube in self.split(p)]

        return list(itertools.chain.from_iterable(new_cubes))


def get_index(x, y, z):
    return x * SIZE**2 + y * SIZE + z


def valid_range(start, end):
    if start < -50 and end < -50 or start > 50 and end > 50:
        return None

    return min(50, max(-50, start)), min(50, max(-50, end))


def get_coords(start, end):
    r1 = valid_range(start[0], end[0])
    r2 = valid_range(start[1], end[1])
    r3 = valid_range(start[2], end[2])
    if r1 and r2 and r3:
        plane = itertools.product(range(r1[0], r1[1] + 1), range(r2[0], r2[1] + 1))
        return itertools.product(plane, range(r3[0], r3[1] + 1))
    else:
        return []


def part1(commands):
    cubes = [0] * SIZE**3

    for command, start, end in commands:
        for (x, y), z in get_coords(start, end):
            index = get_index(x, y, z)
            cubes[index] = int(command == "on")

    return sum(cubes)


def part2(commands):
    cubes = []

    for command, start, end in commands:
        new_cube = make_cube(start, end)
        new_cubes = []
        for cube in cubes:
            new_cubes += cube.subtract(new_cube)

        if command == "on":
            new_cubes.append(new_cube)

        cubes = new_cubes

    return int(sum([c.count() for c in cubes]))


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    commands = []
    for line in data.splitlines():
        groups = re.search(
            r"^(on|off) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", line
        ).groups()
        start = [int(groups[v]) for v in [1, 3, 5]]
        end = [int(groups[v]) for v in [2, 4, 6]]
        commands.append((groups[0], start, end))

    ans_1 = part1(commands)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(commands)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (547648, 1206644425246111)
TEST_RESULT = (590784, None)
TEST_DATA = """\
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
