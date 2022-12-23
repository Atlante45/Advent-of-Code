from math import gcd
import re


REGEX = re.compile(r"(\d+|.)")
SYM = [">", "V", "<", "^"]

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Face indices:
#  0
# 1234
#  5

# F: [R, D, L, U]
# (Face, Relative orientation)
#  0: 0 deg, 1: 90 deg, 2: 180 deg, 3: 270 deg
FACES = {
    0: [(3, 3), (2, 0), (1, 1), (4, 2)],
    1: [(2, 0), (5, 1), (4, 0), (0, 3)],
    2: [(3, 0), (5, 0), (1, 0), (0, 0)],
    3: [(4, 0), (5, 3), (2, 0), (0, 1)],
    4: [(1, 0), (5, 2), (3, 0), (0, 2)],
    5: [(3, 1), (4, 2), (1, 3), (2, 0)],
}
ROTS = {(f0, f1): rot for f0, neigh in FACES.items() for (f1, rot) in neigh}


def get(map, x, y):
    try:
        return map[y][x]
    except IndexError:
        return " "


class Cube:
    def __init__(self, map, pos) -> None:
        self.map = map
        self.max_y = len(self.map)
        self.max_x = max(len(row) for row in self.map)
        self.side_l = gcd(self.max_x, self.max_y)
        self.width = self.max_x // self.side_l
        self.height = self.max_y // self.side_l
        self.top = (pos[0] // self.side_l, pos[1] // self.side_l)

        self.faces = {}
        self.face_coords = {}
        self.face_rots = {}
        self.map_faces(self.top[0], self.top[1], 0, 0)

    def __str__(self) -> str:
        rows = []
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) in self.faces:
                    row += str(self.faces[(x, y)])
                else:
                    row += " "
            row += " | "
            for x in range(self.width):
                if (x, y) in self.faces:
                    row += str(SYM[self.face_rots[self.faces[(x, y)]] - 1])
                else:
                    row += " "
            rows += [row]
        return "\n".join(rows)

    def is_face(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return get(self.map, x * self.side_l, y * self.side_l) != " "

    def map_faces(self, x, y, face, rot):
        if face in self.face_coords:
            return

        if not self.is_face(x, y):
            return

        self.faces[(x, y)] = face
        self.face_coords[face] = (x, y)
        self.face_rots[face] = rot

        for i, (dx, dy) in enumerate(DIRS):
            if self.is_face(x + dx, y + dy):
                f, r = FACES[face][(i - rot) % 4]
                self.map_faces(x + dx, y + dy, f, (rot + r) % 4)

    def get_next(self, pos, dir):
        x, y = pos
        dx, dy = DIRS[dir]

        face0 = (x // self.side_l, y // self.side_l)
        new_x = x + dx
        new_y = y + dy
        face1 = (new_x // self.side_l, new_y // self.side_l)

        if face0 != face1:
            f0 = self.faces[face0]
            frot = self.face_rots[f0]
            f1, rrot = FACES[f0][(dir - frot) % 4]
            rot = ((self.face_rots[f1] - self.face_rots[f0]) - rrot) % 4
            xoff = (x + dx) % self.side_l
            yoff = (y + dy) % self.side_l

            match rot:
                case 1:
                    temp = xoff
                    xoff = self.side_l - 1 - yoff
                    yoff = temp
                case 2:
                    xoff = self.side_l - 1 - xoff
                    yoff = self.side_l - 1 - yoff
                case 3:
                    temp = xoff
                    xoff = yoff
                    yoff = self.side_l - 1 - temp

            dir = (dir + rot) % 4
            face1 = self.face_coords[f1]
            new_x = face1[0] * self.side_l + xoff
            new_y = face1[1] * self.side_l + yoff

        return (new_x, new_y), dir, get(self.map, new_x, new_y)


def find_top(map):
    for i in range(len(map[0])):
        if map[0][i] != " ":
            return (i, 0)


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


def parse(data):
    map, path = data.split("\n\n")
    return map.splitlines(), REGEX.findall(path.strip())


def part1(map, path):
    pos = find_top(map)
    dir = 0

    for move in path:
        if move.isnumeric():
            for _ in range(int(move)):
                nex, ch = get_next(map, pos, dir)
                if ch == "#":
                    break
                pos = nex
        else:
            dir = (dir + (1 if move == "R" else -1)) % len(DIRS)

    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + dir


def part2(map, path):
    pos = find_top(map)
    cube = Cube(map, pos)
    dir = 0

    for move in path:
        if move == "R" and pos == (12, 9):
            break
        if move.isnumeric():
            for _ in range(int(move)):
                nex, ndir, ch = cube.get_next(pos, dir)
                if ch == "#":
                    break
                pos = nex
                dir = ndir
                map[pos[1]] = (
                    map[pos[1]][: pos[0]] + SYM[dir] + map[pos[1]][pos[0] + 1 :]
                )
        else:
            dir = (dir + (1 if move == "R" else -1)) % len(DIRS)
            map[pos[1]] = map[pos[1]][: pos[0]] + SYM[dir] + map[pos[1]][pos[0] + 1 :]

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
] = (6032, 5031)
