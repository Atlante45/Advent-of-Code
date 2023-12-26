from collections import defaultdict
from math import prod
from igraph import Graph


def parse(data):
    graph = defaultdict(set)
    for line in data.splitlines():
        comp, wires = line.split(": ")
        for wire in wires.split():
            graph[comp].add(wire)
            graph[wire].add(comp)
    return graph


def part1(graph):
    return prod(Graph.ListDict(graph).mincut().sizes())


def part2(lines):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
""".rstrip()
] = (54, None)
