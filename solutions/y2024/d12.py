from solutions.utils.graph import neighbors4


def parse(data):
    return data.splitlines()


def visit(grid, x, y, visited):
    visited.add((x, y))

    for i, j in neighbors4(x, y, grid):
        if grid[i][j] == grid[x][y] and (i, j) not in visited:
            visit(grid, i, j, visited)

    return visited


def n4(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def perimeter1(area):
    return sum(1 for x, y in area for i, j in n4(x, y) if (i, j) not in area)


def perimeter2(area):
    edges = 0

    min_i = min(i for i, _ in area)
    max_i = max(i for i, _ in area)
    min_j = min(j for _, j in area)
    max_j = max(j for _, j in area)

    for i in range(min_i, max_i + 1):
        top_was_edge = False
        bottom_was_edge = False
        for j in range(min_j, max_j + 1):
            top_is_edge = (i, j) in area and (i - 1, j) not in area
            bottom_is_edge = (i, j) in area and (i + 1, j) not in area

            if top_is_edge and not top_was_edge:
                edges += 1
            if bottom_is_edge and not bottom_was_edge:
                edges += 1

            top_was_edge = top_is_edge
            bottom_was_edge = bottom_is_edge

    for j in range(min_j, max_j + 1):
        left_was_edge = False
        right_was_edge = False
        for i in range(min_i, max_i + 1):
            left_is_edge = (i, j) in area and (i, j - 1) not in area
            right_is_edge = (i, j) in area and (i, j + 1) not in area

            if left_is_edge and not left_was_edge:
                edges += 1
            if right_is_edge and not right_was_edge:
                edges += 1

            left_was_edge = left_is_edge
            right_was_edge = right_is_edge

    return edges


def parts(grid):
    regions = []

    all_visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in all_visited:
                visited = visit(grid, i, j, set())
                all_visited |= visited
                regions.append(visited)

    p1 = sum(len(region) * perimeter1(region) for region in regions)
    p2 = sum(len(region) * perimeter2(region) for region in regions)

    return p1, p2

TEST_DATA = {}
TEST_DATA[
    """\
AAAA
BBCD
BBCC
EEEC
""".rstrip()
] = (140, 80)
TEST_DATA[
    """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".rstrip()
] = (1930, 1206)
