from itertools import product
import re

REGEX = r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+\d+%"


def parse(data):
    nodes = {}
    for line in data.splitlines()[2:]:
        x, y, size, used, avail = map(int, re.match(REGEX, line).groups())
        nodes[y, x] = size, used, avail
    xs = [x for _, x in nodes.keys()]
    return nodes, max(xs)


def part1(nodes, max_x):
    def is_viable(n1, n2):
        return n1 != n2 and nodes[n1][1] > 0 and nodes[n1][1] <= nodes[n2][2]

    return sum(is_viable(n1, n2) for n1, n2 in product(nodes, nodes))


def part2(nodes, max_x):
    empty_node = next(k for k, v in nodes.items() if v[1] == 0)
    gap = min(k[1] for k, v in nodes.items() if v[0] > 100) - 1
    if len(nodes) < 10:
        gap = empty_node[1]

    return (
        empty_node[0]
        + (max_x - 1 - empty_node[1])
        + 2 * (empty_node[1] - gap)
        + 4 * (max_x - 1)
        + max_x
    )


TEST_DATA = {}
TEST_DATA[
    """\
root@ebhq-gridcenter# df -h
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2  320T  280T    40T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%
""".rstrip()
] = (14, 7)
