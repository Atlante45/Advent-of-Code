from collections import defaultdict, deque


DIR = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}


def parse(data):
    return [list(line) for line in data.splitlines()]


def next(grid, i, j, d):
    i += DIR[d][0]
    j += DIR[d][1]

    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return None, None

    return i, j


def solve(grid, i, j, d):
    beams = deque()
    beams.append(((i, j), d))

    history = defaultdict(list)
    history[(i, j)] = [d]

    def move(i, j, d):
        i, j = next(grid, i, j, d)
        if i is None or d in history[(i, j)]:
            return
        history[(i, j)].append(d)
        beams.appendleft(((i, j), d))

    while len(beams) > 0:
        (i, j), direction = beams.popleft()
        # print(i, j, direction, grid[i][j], beams)

        match grid[i][j]:
            case ".":
                move(i, j, direction)
            case "/":
                match direction:
                    case ">":
                        move(i, j, "^")
                    case "<":
                        move(i, j, "v")
                    case "^":
                        move(i, j, ">")
                    case "v":
                        move(i, j, "<")
            case "\\":
                match direction:
                    case ">":
                        move(i, j, "v")
                    case "<":
                        move(i, j, "^")
                    case "^":
                        move(i, j, "<")
                    case "v":
                        move(i, j, ">")
            case "|":
                match direction:
                    case ">":
                        move(i, j, "v")
                        move(i, j, "^")
                    case "<":
                        move(i, j, "v")
                        move(i, j, "^")
                    case "^":
                        move(i, j, "^")
                    case "v":
                        move(i, j, "v")
            case "-":
                match direction:
                    case "^":
                        move(i, j, "<")
                        move(i, j, ">")
                    case "v":
                        move(i, j, "<")
                        move(i, j, ">")
                    case ">":
                        move(i, j, ">")
                    case "<":
                        move(i, j, "<")
    return len(history)


def part1(grid):
    return solve(grid, 0, 0, ">")


def part2(grid):
    res = 0
    for i in range(len(grid)):
        res = max(res, solve(grid, i, 0, ">"))
        res = max(res, solve(grid, i, len(grid[0]) - 1, "<"))

    for i in range(len(grid[0])):
        res = max(res, solve(grid, 0, i, "v"))
        res = max(res, solve(grid, len(grid) - 1, i, "^"))
    return res


TEST_DATA = {}
TEST_DATA[
    """\
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
""".rstrip()
] = (46, 51)
