from collections import Counter, defaultdict
from itertools import pairwise
from math import prod


MONSTER = """\
..................#.
#....##....##....###
.#..#..#..#..#..#...
""".rstrip().splitlines()


def parse(data):
    tiles = {}
    for tile in data.split("\n\n"):
        id, *lines = tile.splitlines()
        id = int(id[:-1].split()[1])
        tiles[id] = lines
    return tiles


def part1(tiles):
    edges = defaultdict(list)
    for id, tile in tiles.items():
        edges[tuple(tile[0])].append(id)
        edges[tuple(tile[0][::-1])].append(id)
        edges[tuple(tile[-1])].append(id)
        edges[tuple(tile[-1][::-1])].append(id)
        edges[tuple(tile[i][0] for i in range(len(tile)))].append(id)
        edges[tuple(tile[i][-1] for i in range(len(tile)))].append(id)
        edges[tuple(tile[i][0] for i in range(len(tile) - 1, -1, -1))].append(id)
        edges[tuple(tile[i][-1] for i in range(len(tile) - 1, -1, -1))].append(id)

    counts = Counter([v[0] for v in edges.values() if len(v) == 1])
    return prod(k for k, v in counts.items() if v == 4)


def to_key(line):
    a, b = sorted((tuple(line), tuple(line[::-1])))
    return a, b


def get_left(tile):
    return tuple(tile[i][0] for i in range(len(tile)))


def get_right(tile):
    return tuple(tile[i][-1] for i in range(len(tile)))


def get_top(tile):
    return tuple(tile[0])


def get_bottom(tile):
    return tuple(tile[-1])


def get_sides(tile):
    return get_top(tile), get_bottom(tile), get_left(tile), get_right(tile)


def check_monster(water, monster_str, width, height):
    monster_width = len(monster_str[0])
    monster_height = len(monster_str)
    monster = set()
    for y, row in enumerate(monster_str):
        for x, cell in enumerate(row):
            if cell == "#":
                monster.add((x, y))

    monsters = 0
    monster_cells = set()
    for y in range(height - monster_height):
        for x in range(width - monster_width):
            if all((x + mx, y + my) in water for mx, my in monster):
                monsters += 1
                monster_cells.update((x + mx, y + my) for mx, my in monster)

    return monsters, len(water - monster_cells)


def part2(tiles):
    edges = defaultdict(set)
    sides = {}
    for id, tile in tiles.items():
        top, bottom, left, right = get_sides(tile)

        edges[top].add(id)
        sides[(top, id)] = (0, False)
        edges[top[::-1]].add(id)
        sides[(top[::-1], id)] = (0, True)
        edges[bottom].add(id)
        sides[(bottom, id)] = (1, False)
        edges[bottom[::-1]].add(id)
        sides[(bottom[::-1], id)] = (1, True)
        edges[left].add(id)
        sides[(left, id)] = (2, False)
        edges[left[::-1]].add(id)
        sides[(left[::-1], id)] = (2, True)
        edges[right].add(id)
        sides[(right, id)] = (3, False)
        edges[right[::-1]].add(id)
        sides[(right[::-1], id)] = (3, True)

    counts = Counter([list(v)[0] for v in edges.values() if len(v) == 1])
    corners = [k for k, v in counts.items() if v == 4]

    grid = []
    used = set()
    while len(grid) < 12:
        row = []
        right = None

        if len(grid) == 0:
            top_left_id = corners[0]
            top_left_tile = tiles[top_left_id]
            top, bottom, left, right = get_sides(top_left_tile)
            if len(edges[top]) != 1:
                top_left_tile = top_left_tile[::-1]
            if len(edges[left]) != 1:
                top_left_tile = [row[::-1] for row in top_left_tile]

            right = get_right(top_left_tile)
            row.append(top_left_tile)
            used.add(top_left_id)
        else:
            tile_above = grid[-1][0]
            bottom = get_bottom(tile_above)

            next = edges[bottom] - used
            assert len(next) == 1
            next_id = next.pop()
            next_tile = tiles[next_id]

            side, _ = sides[(bottom, next_id)]
            if side in (2, 3):
                next_tile = list(zip(*next_tile))

            to, bo, _, _ = get_sides(next_tile)
            if bottom == to[::-1]:
                next_tile = [row[::-1] for row in next_tile]
            elif bottom == bo:
                next_tile = next_tile[::-1]
            elif bottom == bo[::-1]:
                next_tile = [row[::-1] for row in next_tile[::-1]]
            else:
                assert bottom == to

            assert bottom == get_top(next_tile)

            right = get_right(next_tile)
            row.append(next_tile)
            used.add(next_id)

        while len(row) < 12:
            next = edges[right] - used
            assert len(next) == 1
            next_id = next.pop()
            next_tile = tiles[next_id]

            side, _ = sides[(right, next_id)]
            if side in (0, 1):
                next_tile = list(zip(*next_tile))

            _, _, le, ri = get_sides(next_tile)
            if right == le[::-1]:
                next_tile = next_tile[::-1]
            elif right == ri:
                next_tile = [row[::-1] for row in next_tile]
            elif right == ri[::-1]:
                next_tile = [row[::-1] for row in next_tile[::-1]]

            assert right == get_left(next_tile)

            right = get_right(next_tile)
            row.append(next_tile)
            used.add(next_id)

        assert len(edges[right]) == 1
        grid.append(row)

    for y in range(12):
        for x0, x1 in pairwise(range(12)):
            assert get_right(grid[y][x0]) == get_left(grid[y][x1])

    for x in range(12):
        for y0, y1 in pairwise(range(12)):
            assert get_bottom(grid[y0][x]) == get_top(grid[y1][x])

    big_grid = []
    for row in grid:
        big_row = [None] * (len(row[0]) - 2)
        for tile in row:
            cut = [row[1:-1] for row in tile[1:-1]]
            for i in range(len(cut)):
                if big_row[i] is None:
                    big_row[i] = []
                big_row[i].extend(cut[i])
        big_grid.extend(big_row)

    # for row in big_grid:
    #     print("".join(row))

    width = len(big_grid[0])
    height = len(big_grid)
    water = set()
    for y, row in enumerate(big_grid):
        for x, cell in enumerate(row):
            if cell == "#":
                water.add((x, y))

    global MONSTER
    monster = MONSTER
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count
    monster = MONSTER[::-1]
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count
    monster = [row[::-1] for row in MONSTER]
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count
    monster = [row[::-1] for row in MONSTER[::-1]]
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count
    MONSTER = list(zip(*MONSTER))
    monster = MONSTER
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count
    monster = MONSTER[::-1]
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count
    monster = [row[::-1] for row in MONSTER]
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count
    monster = [row[::-1] for row in MONSTER[::-1]]
    monsters, water_count = check_monster(water, monster, width, height)
    if monsters > 0:
        return water_count


TEST_DATA = {}
TEST_DATA[
    """\
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""".rstrip()
] = (20899048083289, 273)
