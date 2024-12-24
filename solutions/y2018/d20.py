from solutions.utils.graph import dijkstra, neighbors4

DIRS = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}


def parse(data):
    return data.strip()


def explore(starts, i, regex, edges):
    final_positions = set()
    positions = starts.copy()
    while i < len(regex) and regex[i] != ")":
        if regex[i] == "(":
            positions, i = explore(positions, i + 1, regex, edges)
        elif regex[i] == "|":
            final_positions.update(positions)
            positions = starts.copy()
        elif regex[i] == ")":
            final_positions.update(positions)
            return final_positions, i
        else:
            dx, dy = DIRS[regex[i]]

            new_positions = set()
            for x, y in positions:
                nx = x + dx
                ny = y + dy
                edges.add(((x, y), (nx, ny)))
                edges.add(((nx, ny), (x, y)))
                new_positions.add((nx, ny))
            positions = new_positions
        i += 1
    return positions, i


def parts(regex):
    edges = set()
    explore([(0, 0)], 0, regex[1:-1], edges)

    def neighbors(p):
        return [(x, y) for x, y in neighbors4(*p) if ((p, (x, y)) in edges)]

    _, cost_so_far = dijkstra([(0, 0)], neighbors)
    p1 = max(cost_so_far.values())
    p2 = sum(1 for c in cost_so_far.values() if c >= 1000)
    return p1, p2


TEST_DATA = {}
TEST_DATA[
    """\
^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$
""".rstrip()
] = (23, None)
TEST_DATA[
    """\
^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$
""".rstrip()
] = (31, None)
