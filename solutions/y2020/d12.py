def parse(data):
    directions = []
    for line in data.splitlines():
        d, n = line[0], int(line[1:])
        directions.append((d, n))
    return directions


def part1(directions):
    x, y = 0, 0
    r = 0

    for d, n in directions:
        if d == "N":
            y -= n
        elif d == "S":
            y += n
        elif d == "E":
            x += n
        elif d == "W":
            x -= n
        elif d == "R":
            r = (r + n // 90) % 4
        elif d == "L":
            r = (r - n // 90) % 4
        elif d == "F":
            if r == 0:
                x += n
            elif r == 1:
                y += n
            elif r == 2:
                x -= n
            elif r == 3:
                y -= n
    return abs(x) + abs(y)


def part2(directions):
    x, y = 10, -1
    sx, sy = 0, 0

    for d, n in directions:
        if d == "N":
            y -= n
        elif d == "S":
            y += n
        elif d == "E":
            x += n
        elif d == "W":
            x -= n
        elif d == "R":
            if n == 90:
                x, y = -y, x
            elif n == 180:
                x, y = -x, -y
            elif n == 270:
                x, y = y, -x
        elif d == "L":
            if n == 90:
                x, y = y, -x
            elif n == 180:
                x, y = -x, -y
            elif n == 270:
                x, y = -y, x
        elif d == "F":
            sx += x * n
            sy += y * n

    return abs(sx) + abs(sy)


TEST_DATA = {}
TEST_DATA[
    """\
F10
N3
F7
R90
F11
""".rstrip()
] = (25, 286)
