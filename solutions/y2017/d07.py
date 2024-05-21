import re
from more_itertools import flatten


def parse(data):
    tree = {}
    for line in data.splitlines():
        prog, weigth, progs = re.match(
            r"([a-z]+) \((\d+)\)(?: -> ([a-z, ]+))?", line
        ).groups()
        progs = progs.split(", ") if progs is not None else []
        tree[prog] = (int(weigth), progs)
    return tree


def parts(tree):
    root = set(tree.keys()) - set(flatten([progs for _, progs in tree.values()]))
    root = root.pop()

    ordered = []
    visited = [root]
    while visited:
        prog = visited.pop()
        ordered.append(prog)
        visited.extend(tree[prog][1])

    weight_map = {}
    for prog in reversed(ordered):
        weight, progs = tree[prog]
        progs = [(p, weight_map[p]) for p in progs]
        weights = [w for _, w in progs]

        if len(set(weights)) > 1:
            target = [w for w in weights if weights.count(w) > 1][0]
            current = [w for w in weights if weights.count(w) == 1][0]
            wrong_prog = [p for p, w in progs if w == current][0]
            diff = target - current
            return (root, tree[wrong_prog][0] + diff)

        weight_map[prog] = weight + sum(weights)


TEST_DATA = {}
TEST_DATA[
    """\
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".rstrip()
] = ("tknk", 60)
