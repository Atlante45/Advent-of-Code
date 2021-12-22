#!/usr/local/bin/python3
from collections import defaultdict
import itertools
import math
import os
import re

SIZE = 100

def prod3(a, b, c):
    return ([x, y, z] for (x, y), z in itertools.product(itertools.product(a, b), c))

def make_cube(start, end):
    start = [x - .5 for x in start]
    end = [x + .5 for x in end]
    return Cube(start, end)

def p_greater(p1, p2):
    return all([a < b for a, b in zip(p1, p2)])

def p_avg(points):
    return [round(sum(l) / len(points) - 0.5) + 0.5 for l in zip(*points)]

class Cube:
    def __init__(self, start, end):
        self.start = [min(a, b) for a, b in zip(start, end)]
        self.end = [max(a, b) for a, b in zip(start, end)]
        self.corners = list(prod3(*zip(start, end)))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.start == other.start and self.end == other.end
    def __repr__(self):
        return "Cube()"
    def __str__(self):
        return f'  start={self.start}\n  end={self.end}    corners={self.corners}'

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
        assert(p in self.corners)
        x, y, z = [start if corner != start else end for start, end, corner in zip(self.start, self.end, p)]
        return (x, y, z)

    def intersection(self, other):
        start = [max(a, b) for a, b in zip(self.start, other.start)]
        end = [min(a, b) for a, b in zip(self.end, other.end)]
        return Cube(start, end) if all([a < b for a, b in zip(start, end)]) else None

    def partition_point(self, other):
        try:
            return next(p for p in other.corners if self.is_inside(p))
        except:
            common_corners = [value for value in self.corners if value in other.corners]
            num_common_corners = len(common_corners)
            if num_common_corners in [2, 4]:
                return p_avg([other.opposite(p) for p in common_corners])
            elif num_common_corners == 0:
                return p_avg(other.corners)
            else:
                print('PANIC!!!!')


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
    return x*SIZE**2 + y*SIZE + z

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
            cubes[index] = int(command == 'on')

    return sum(cubes)

def part2(commands):
    cubes = []

    for command, start, end in commands:
        new_cube = make_cube(start, end)
        new_cubes = []
        for cube in cubes:
            new_cubes += cube.subtract(new_cube)

        if command == 'on':
            new_cubes.append(new_cube)

        cubes = new_cubes

    return int(sum([c.count() for c in cubes]))


def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        commands = []
        for line in input:
            groups = re.search('^(on|off) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)', line).groups()
            start = [int(groups[v]) for v in [1, 3, 5]]
            end = [int(groups[v]) for v in [2, 4, 6]]
            commands.append((groups[0], start, end))

        print(f'Solving {filename}')
        print(f"    Part 1: {part1(commands)}")
        print(f"    Part 2: {part2(commands)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
