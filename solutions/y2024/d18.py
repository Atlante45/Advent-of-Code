from solutions.utils.graph import binary_search, dijkstra, neighbors4


def parse(data):
    return [tuple(map(int, line.split(","))) for line in data.splitlines()]


def part1(lines):
    bytes = 1024 if len(lines) > 1024 else 12
    size = 71 if len(lines) > 1024 else 7

    obstacles = set(lines[:bytes])

    def neighbors(cell):
        x, y = cell
        return [n for n in neighbors4(x, y, size) if n not in obstacles]

    _, cost = dijkstra((0, 0), neighbors)

    return cost[(size - 1, size - 1)]


def find_path(bytes, size):
    obstacles = set(bytes)

    def neighbors(cell):
        x, y = cell
        return [n for n in neighbors4(x, y, size) if n not in obstacles]

    came_from, cost = dijkstra((0, 0), neighbors)

    if (size - 1, size - 1) not in cost:
        return None

    path = set()
    cell = (size - 1, size - 1)
    while cell != (0, 0):
        path.add(cell)
        cell = came_from[cell]
    path.add((0, 0))
    return path


def part2(lines):
    size = 71 if len(lines) > 1024 else 7

    i = binary_search(lambda i: not find_path(lines[:i], size), 0, len(lines))

    return f"{lines[i - 1][0]},{lines[i - 1][1]}"


TEST_DATA = {}
TEST_DATA[
    """\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".rstrip()
] = (None, "6,1")
