import re
import networkx as nx
from z3 import Ints, Solver, Abs, sat


def parse(data):
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in data.splitlines()]


def part1(nanobots):
    strongest_avenger = max(nanobots, key=lambda x: x[3])
    x0, y0, z0, r = strongest_avenger
    return sum(
        1 for x, y, z, _ in nanobots if abs(x - x0) + abs(y - y0) + abs(z - z0) <= r
    )


def part2(nanobots):
    G = nx.Graph()
    for i in range(len(nanobots)):
        for j in range(i + 1, len(nanobots)):
            x0, y0, z0, r0 = nanobots[i]
            x1, y1, z1, r1 = nanobots[j]
            if abs(x0 - x1) + abs(y0 - y1) + abs(z0 - z1) <= r0 + r1:
                G.add_edge(i, j)

    cliques = sorted(nx.find_cliques(G), key=len, reverse=True)
    largest_clique = cliques[0]

    s = Solver()
    x, y, z = Ints("x y z")
    for i in largest_clique:
        x0, y0, z0, r0 = nanobots[i]
        s.add(Abs(x - x0) + Abs(y - y0) + Abs(z - z0) <= r0)

    assert s.check() == sat
    return sum(s.model()[i].as_long() for i in [x, y, z])


TEST_DATA = {}
TEST_DATA[
    """\
pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1
""".rstrip()
] = (7, None)
