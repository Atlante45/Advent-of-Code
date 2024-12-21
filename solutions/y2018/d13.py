from itertools import count


DIR_KEY = ">v<^"
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse(data):
    grid = []
    carts = []
    for y, line in enumerate(data.splitlines()):
        row = []
        for x, c in enumerate(line):
            if c in "<>^v":
                row.append("-" if c in "<>" else "|")
                carts.append((x, y, DIR_KEY.index(c), 0))
            else:
                row.append(c)
        grid.append(row)

    return grid, carts


def parts(grid, carts):
    p1res = None

    for _ in count(1):
        carts = sorted(carts, key=lambda c: (c[1], c[0]))

        for i in range(len(carts)):
            if carts[i] is None:
                continue

            x, y, d, s = carts[i]
            dx, dy = DIRS[d]
            nx, ny = x + dx, y + dy
            if grid[ny][nx] == "\\":
                d = (d + 1 if d % 2 == 0 else d - 1) % 4
            elif grid[ny][nx] == "/":
                d = (d + 1 if d % 2 == 1 else d - 1) % 4
            elif grid[ny][nx] == "+":
                d = (d + s - 1) % 4
                s = (s + 1) % 3

            collision = next(
                (
                    j
                    for j in range(len(carts))
                    if carts[j] is not None and carts[j][0] == nx and carts[j][1] == ny
                ),
                None,
            )
            if collision is not None:
                if p1res is None:
                    p1res = f"{nx},{ny}"
                carts[i] = None
                carts[collision] = None
            else:
                carts[i] = (nx, ny, d, s)

        carts = [c for c in carts if c is not None]

        if len(carts) == 1:
            return p1res, f"{carts[0][0]},{carts[0][1]}"

        if len(carts) == 0:
            return p1res, None


TEST_DATA = {}
TEST_DATA[
    """\
/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   
""".rstrip()
] = ("7,3", None)
TEST_DATA[
    """\
/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/
""".rstrip()
] = ("2,0", "6,4")
