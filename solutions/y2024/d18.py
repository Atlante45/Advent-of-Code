from solutions.utils.graph import dijkstra, neighbors4


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


def part2(lines):
    size = 71 if len(lines) > 1024 else 7

    for i in range(1, len(lines)):
        obstacles = set(lines[:i])

        def neighbors(cell):
            x, y = cell
            return [n for n in neighbors4(x, y, size) if n not in obstacles]

        _, cost = dijkstra((0, 0), neighbors)
        if (size - 1, size - 1) not in cost:
            return f"{lines[i - 1][0]},{lines[i - 1][1]}"

    return None


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
