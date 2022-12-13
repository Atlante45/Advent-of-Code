def findNeighbors(heighmap, i, j):
    neighbors = []
    height = len(heighmap)
    width = len(heighmap[0])
    if i > 0:
        neighbors.append((i - 1, j))
    if i < height - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < width - 1:
        neighbors.append((i, j + 1))

    return neighbors


def findLowestPoints(heighmap):
    lowestPoints = []
    height = len(heighmap)
    width = len(heighmap[0])
    for i in range(height):
        for j in range(width):
            lowest = True
            for (i1, j1) in findNeighbors(heighmap, i, j):
                if heighmap[i][j] >= heighmap[i1][j1]:
                    lowest = False
                    break
            if lowest:
                lowestPoints += [(i, j)]

    return lowestPoints


def computeBasin(heighmap, i, j):
    res = 1
    heighmap[i][j] = 9
    for (i1, j1) in findNeighbors(heighmap, i, j):
        if heighmap[i1][j1] != 9:
            res += computeBasin(heighmap, i1, j1)

    return res


def parse(data):
    heighmap = []
    for line in data.splitlines():
        heighmap.append([int(v) for v in line.strip()])
    return heighmap


def part1(heighmap):
    res = 0

    for (i, j) in findLowestPoints(heighmap):
        res += 1 + heighmap[i][j]

    return res


def part2(heighmap):
    basins = []

    for (i, j) in findLowestPoints(heighmap):
        basins.append(computeBasin(heighmap, i, j))

    basins = sorted(basins)
    return basins[-3] * basins[-2] * basins[-1]


TEST_DATA = {}
TEST_DATA[
    """\
2199943210
3987894921
9856789892
8767896789
9899965678
""".rstrip()
] = (15, 1134)
