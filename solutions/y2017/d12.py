from solutions.utils.graph import dijkstra


def parse(data):
    graph = {}
    for line in data.splitlines():
        node, neighbors = line.split(" <-> ")
        graph[node] = neighbors.split(", ")
    return graph


def part1(graph):
    def neighbors(n):
        return graph[n]

    _, cost_so_far = dijkstra("0", neighbors)
    return len(cost_so_far)


def part2(graph):
    nodes = set(graph.keys())
    res = 0

    def neighbors(n):
        return graph[n]

    while nodes:
        node = nodes.pop()
        _, cost_so_far = dijkstra(node, neighbors)
        nodes -= set(cost_so_far.keys())
        res += 1

    return res


TEST_DATA = {}
TEST_DATA[
    """\
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""".rstrip()
] = (6, 2)
