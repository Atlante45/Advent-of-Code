import re


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
SYM = [">", "V", "<", "^"]


REGEX = re.compile(r"(\d+|.)")


def find_top(map):
    for i in range(len(map[0])):
        if map[0][i] != " ":
            return (i, 0)


def get(map, x, y):
    try:
        return map[y][x]
    except IndexError:
        return " "


def get_next(map, pos, dir):
    x, y = pos
    dx, dy = DIRS[dir]

    max_y = len(map)
    max_x = max(len(row) for row in map)

    y = (y + dy) % max_y
    x = (x + dx) % max_x

    while True:
        ch = get(map, x, y)
        if ch != " ":
            return (x, y), ch

        y = (y + dy) % max_y
        x = (x + dx) % max_x


def get_next_face(pos):
    pass


def get_next_cubed(map, pos, dir):
    x, y = pos
    dx, dy = DIRS[dir]

    side_l = len(map) // 4
    print(side_l)

    max_y = len(map)
    max_x = max(len(row) for row in map)

    y = (y + dy) % max_y
    x = (x + dx) % max_x

    while True:
        ch = get(map, x, y)
        if ch != " ":
            return (x, y), ch, dir

        y = (y + dy) % max_y
        x = (x + dx) % max_x


def parse(data):
    map, path = data.split("\n\n")
    return map.splitlines(), REGEX.findall(path.strip())


def part1(map, path):
    print("\n".join(map))
    print(path)
    pos = find_top(map)
    dir = 0

    for move in path:
        print(move)
        if move.isnumeric():
            for _ in range(int(move)):
                map[pos[1]] = (
                    map[pos[1]][: pos[0]] + SYM[dir] + map[pos[1]][pos[0] + 1 :]
                )
                nex, ch = get_next(map, pos, dir)
                print("    ", nex, ch)
                if ch == "#":
                    break
                pos = nex
        else:
            dir = (dir + (1 if move == "R" else -1)) % len(DIRS)
        print(pos, dir)
        # print("\n".join(map))
        # input()

    # print("\n".join(map))
    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + dir


def part2(map, path):
    print("\n".join(map))
    print(path)
    pos = find_top(map)
    dir = 0

    for move in path:
        print(move)
        if move.isnumeric():
            for _ in range(int(move)):
                map[pos[1]] = (
                    map[pos[1]][: pos[0]] + SYM[dir] + map[pos[1]][pos[0] + 1 :]
                )
                nex, ch = get_next_cubed(map, pos, dir)
                print("    ", nex, ch)
                if ch == "#":
                    break
                pos = nex
        else:
            dir = (dir + (1 if move == "R" else -1)) % len(DIRS)
        print(pos, dir)
        # print("\n".join(map))
        # input()

    # print("\n".join(map))
    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + dir


TEST_DATA = {}
TEST_DATA[
    """\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".rstrip()
] = (6032, None)
