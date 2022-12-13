from solutions.utils import ocr


def render(holes):
    xs, ys = list(zip(*holes))
    max_x = max(xs)
    max_y = max(ys)

    render = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            render += "#" if (x, y) in holes else "."
        render += "\n"

    return render


def fold(holes, axis, val):
    folded = set()
    for hole in holes:
        if axis == "x":
            if hole[0] > val:
                folded.add((val - (hole[0] - val), hole[1]))
            elif hole[0] != val:
                folded.add(hole)
        elif axis == "y":
            if hole[1] > val:
                folded.add((hole[0], val - (hole[1] - val)))
            elif hole[1] != val:
                folded.add(hole)

    return list(folded)


def parse(data):
    holes = []
    folds = []
    for line in data.splitlines():
        if line.startswith("fold"):
            [a, b] = line.strip().split()[-1].split("=")
            folds += [(a, int(b))]
        elif len(line) > 1:
            [x, y] = [int(x) for x in line.strip().split(",")]
            holes += [(x, y)]
    return holes, folds


def part1(holes, folds):
    holes = fold(holes, folds[0][0], folds[0][1])
    return len(holes)


def part2(holes, folds):
    for axis, val in folds:
        holes = fold(holes, axis, val)
    return ocr.parse(render(holes))


TEST_DATA = {}
TEST_DATA[
    """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".rstrip()
] = (17, None)
