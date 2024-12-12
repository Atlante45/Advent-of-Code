from solutions.utils.graph import neighbors4


def parse(data):
    return data.splitlines()


def visit(lines, x, y, visited):
    edges = 0
    area = 1
    visited.add((x, y))

    for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if i >= 0 and i < len(lines) and j >= 0 and j < len(lines[i]) and lines[i][j] == lines[x][y]:
            if (i, j) in visited:
                continue
            a, e = visit(lines, i, j, visited)
            area += a
            edges += e
        else:
            edges += 1
    return area, edges


def visit2(lines, x, y, visited):
    visited.add((x, y))

    for i, j in neighbors4(x, y, lines):
        if lines[i][j] == lines[x][y] and (i, j) not in visited:
            visit2(lines, i, j, visited)


def perimeter(area, width, height):
    edges = 0

    for i in range(height):
        top = False
        bottom = False
        for j in range(width):
            if (i, j) in area and (i - 1, j) not in area:
                if not top:
                    edges += 1
                    top = True
            else:
                top = False
            if (i, j) in area and (i + 1, j) not in area:
                if not bottom:
                    edges += 1
                    bottom = True
            else:
                bottom = False

    for j in range(width):
        left = False
        right = False
        for i in range(height):
            if (i, j) in area and (i, j - 1) not in area:
                if not left:
                    edges += 1
                    left = True
            else:
                left = False
            if (i, j) in area and (i, j + 1) not in area:
                if not right:
                    edges += 1
                    right = True
            else:
                right = False
    return edges


def part1(lines):
    cost = 0
    visited = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if (i, j) not in visited:
                area, edges = visit(lines, i, j, visited)
                cost += area * edges
    return cost


def part2(lines):
    width = len(lines[0])
    height = len(lines)
    visited = set()
    res = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if (i, j) not in visited:
                area = set()
                visit2(lines, i, j, area)
                visited |= area
                # print(c, len(area), perimeter(area, width, height))
                res += len(area) * perimeter(area, width, height)


    return res


TEST_DATA = {}
TEST_DATA[
    """\
AAAA
BBCD
BBCC
EEEC
""".rstrip()
] = (None, 80)
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
