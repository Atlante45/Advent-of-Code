from solutions.utils import logger, ocr
from aocd import data


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


def part1(holes, folds):
    holes = fold(holes, folds[0][0], folds[0][1])
    return len(holes)


def part2(holes, folds):
    for axis, val in folds:
        holes = fold(holes, axis, val)
    return ocr.parse(render(holes))


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    holes = []
    folds = []
    for line in data.splitlines():
        if line.startswith("fold"):
            [a, b] = line.strip().split()[-1].split("=")
            folds += [(a, int(b))]
        elif len(line) > 1:
            [x, y] = [int(x) for x in line.strip().split(",")]
            holes += [(x, y)]

    ans_1 = part1(holes, folds)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(holes, folds)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (751, "PGHRKLKL")
TEST_RESULT = (17, None)
TEST_DATA = """\
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

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
