from solutions.utils.graph import dijkstra


def parse(data):
    return [list(map(int, line)) for line in data.splitlines()]


def previous(pos, came_from, count):
    if count == 0:
        return pos
    return previous(came_from[pos], came_from, count - 1) if pos in came_from else None


def valid(cur, next, came_from):
    if next == came_from[cur]:
        return False

    prev = previous(cur, came_from, 3)
    if prev is not None and (
        abs(prev[0] - next[0]) == 4 or abs(prev[1] - next[1]) == 4
    ):
        print("invalid", cur, next, prev)
        return False

    return True


def part1(grid):
    # print(grid)

    def cost(_, next):
        return grid[next[0]][next[1]]

    def neighbors(pos):
        i, j, d, s = pos
        ns = []

        if d == "^":
            if s < 3:
                ns.append((i - 1, j, "^", s + 1))
            ns.append((i, j + 1, ">", 1))
            ns.append((i, j - 1, "<", 1))
        elif d == "v":
            if s < 3:
                ns.append((i + 1, j, "v", s + 1))
            ns.append((i, j + 1, ">", 1))
            ns.append((i, j - 1, "<", 1))
        elif d == "<":
            if s < 3:
                ns.append((i, j - 1, "<", s + 1))
            ns.append((i + 1, j, "v", 1))
            ns.append((i - 1, j, "^", 1))
        elif d == ">":
            if s < 3:
                ns.append((i, j + 1, ">", s + 1))
            ns.append((i + 1, j, "v", 1))
            ns.append((i - 1, j, "^", 1))
        return [
            n
            for n in ns
            if n[0] >= 0 and n[1] >= 0 and n[0] < len(grid) and n[1] < len(grid[0])
        ]

    came_from, cost_so_far = dijkstra((0, 0, ">", 0), neighbors, cost)

    return min(
        [
            c
            for (i, j, d, s), c in cost_so_far.items()
            if i == len(grid) - 1 and j == len(grid[0]) - 1
        ]
    )


def part2(grid):
    # print(grid)

    def cost(_, next):
        return grid[next[0]][next[1]]

    def neighbors(pos):
        i, j, d, s = pos
        ns = []

        MAX = 10
        MIN = 3
        if d == "^":
            if s < MAX:
                ns.append((i - 1, j, "^", s + 1))
            if s > MIN:
                ns.append((i, j + 1, ">", 1))
                ns.append((i, j - 1, "<", 1))
        elif d == "v":
            if s < MAX:
                ns.append((i + 1, j, "v", s + 1))
            if s > MIN:
                ns.append((i, j + 1, ">", 1))
                ns.append((i, j - 1, "<", 1))
        elif d == "<":
            if s < MAX:
                ns.append((i, j - 1, "<", s + 1))
            if s > MIN:
                ns.append((i + 1, j, "v", 1))
                ns.append((i - 1, j, "^", 1))
        elif d == ">":
            if s < MAX:
                ns.append((i, j + 1, ">", s + 1))
            if s > MIN:
                ns.append((i + 1, j, "v", 1))
                ns.append((i - 1, j, "^", 1))
        else:
            ns.append((i + 1, j, "v", 1))
            ns.append((i - 1, j, "^", 1))
            ns.append((i, j + 1, ">", 1))
            ns.append((i, j - 1, "<", 1))

        return [
            n
            for n in ns
            if n[0] >= 0 and n[1] >= 0 and n[0] < len(grid) and n[1] < len(grid[0])
        ]

    came_from, cost_so_far = dijkstra((0, 0, ".", 0), neighbors, cost)

    return min(
        [
            c
            for (i, j, d, s), c in cost_so_far.items()
            if i == len(grid) - 1 and j == len(grid[0]) - 1 and s > 3
        ]
    )


TEST_DATA = {}
TEST_DATA[
    """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".rstrip()
] = (102, 94)
TEST_DATA[
    """\
111111111111
999999999991
999999999991
999999999991
999999999991
""".rstrip()
] = (None, 71)
