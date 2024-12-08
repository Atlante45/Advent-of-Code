from collections import defaultdict
from itertools import combinations


def parse(data):
    antennas = defaultdict(list)
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c != '.':
                antennas[c].append((i, j))
    width = len(line)
    height = len(data.splitlines())
    return antennas, width, height


def part1(antennas, width, height):
    antinodes = set()
    for _, nodes in antennas.items():
        for a, b in combinations(nodes, 2):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            antinodes.add((a[0] + dx, a[1] + dy))
            antinodes.add((b[0] - dx, b[1] - dy))


    antinodes = [x for x in antinodes if 0 <= x[0] < height and 0 <= x[1] < width]
    return len(antinodes)



def part2(antennas, width, height):
    antinodes = set()
    for _, nodes in antennas.items():
        for a, b in combinations(nodes, 2):
            dx = a[0] - b[0]
            dy = a[1] - b[1]

            x, y = a[0], a[1]
            while 0 <= x < height and 0 <= y < width:
                antinodes.add((x, y))
                x += dx
                y += dy

            x, y = b[0], b[1]
            while 0 <= x < height and 0 <= y < width:
                antinodes.add((x, y))
                x -= dx
                y -= dy


    antinodes = [x for x in antinodes if 0 <= x[0] < height and 0 <= x[1] < width]
    return len(antinodes)


TEST_DATA = {}
TEST_DATA[
    """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".rstrip()
] = (14, 34)
