from itertools import combinations
import numpy as np
from z3 import Solver, Real, Reals

from solutions.utils.graph import p, v


def parse(data):
    hailstones = []
    for line in data.splitlines():
        pos, vel = line.split(" @ ")
        hailstones.append(
            (
                p(*[int(x) for x in pos.split(", ")]),
                v(*[int(x) for x in vel.split(", ")]),
            )
        )
    return hailstones


def intersection(h1, h2, axis):
    c1 = np.cross(h1[1][:axis], h2[1][:axis])
    if 0 in c1:
        return None
    c2 = np.cross(h2[1][:axis], h1[1][:axis])
    t1 = np.cross(h2[0][:axis] - h1[0][:axis], h2[1][:axis]) / c1
    t2 = np.cross(h1[0][:axis] - h2[0][:axis], h1[1][:axis]) / c2
    if t1 < 0 or t2 < 0:
        return None
    return h1[0][:axis] + h1[1][:axis] * t1


def part1(hailstones):
    res = 0
    start = 7 if len(hailstones) < 10 else 200_000_000_000_000
    end = 27 if len(hailstones) < 10 else 400_000_000_000_000
    for h1, h2 in combinations(hailstones, 2):
        intersect = intersection(h1, h2, 2)
        if intersect is not None and all(p >= start and p <= end for p in intersect):
            res += 1
    return res


def part2(hailstones):
    S = Solver()
    x, y, z, vx, vy, vz = Reals("x y z vx vy vz")
    for i, (pos, vel) in enumerate(hailstones[:3]):
        t = Real(f"t{i}")
        S.add(pos[0] + vel[0] * t == x + vx * t)
        S.add(pos[1] + vel[1] * t == y + vy * t)
        S.add(pos[2] + vel[2] * t == z + vz * t)
    S.check()
    return sum(S.model()[a].as_long() for a in [x, y, z])


TEST_DATA = {}
TEST_DATA[
    """\
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".rstrip()
] = (2, 47)
