from collections import defaultdict
from itertools import combinations


def parse(data):
    nodes = set()
    edges = defaultdict(list)
    for line in data.splitlines():
        a, b = line.split("-")
        edges[a].append(b)
        edges[b].append(a)
        nodes.add(a)
        nodes.add(b)
    return nodes, edges


def part1(nodes, edges):
    res = 0
    done = set()
    for node in nodes:
        if node in done:
            continue

        done.add(node)
        for c in combinations(edges[node], 2):
            if c[0] in done or c[1] in done:
                continue
            if c[0] in edges[c[1]]:
                if "t" in [node[0], c[0][0], c[1][0]]:
                    res += 1

    return res


def part2(nodes, edges):
    largest = []

    done = set()
    for node in nodes:
        if node in done:
            continue

        done.add(node)

        for i in range(len(edges[node]), 0, -1):
            for c in combinations(edges[node], i):
                conn = all(c1[0] in edges[c1[1]] for c1 in combinations(c, 2))
                if not conn:
                    continue
                if len(c) + 1 > len(largest):
                    largest = list(c) + [node]

    return ",".join(sorted(largest))


TEST_DATA = {}
TEST_DATA[
    """\
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".rstrip()
] = (7, "co,de,ka,ta")
