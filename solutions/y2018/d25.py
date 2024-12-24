import networkx as nx


def parse(data):
    return [tuple(map(int, line.split(","))) for line in data.splitlines()]


def part1(points):
    G = nx.Graph()
    for i in range(len(points)):
        G.add_node(i)
        for j in range(i + 1, len(points)):
            if sum(abs(a - b) for a, b in zip(points[i], points[j])) <= 3:
                G.add_edge(i, j)

    return len(list(nx.connected_components(G)))


def part2(points):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0
""".rstrip()
] = (2, None)
TEST_DATA[
    """\
-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0
""".rstrip()
] = (4, None)
TEST_DATA[
    """\
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
""".rstrip()
] = (3, None)
TEST_DATA[
    """\
1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2
""".rstrip()
] = (8, None)
