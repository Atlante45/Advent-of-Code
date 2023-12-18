from solutions.utils.graph import neighbors8


def step(display, rows, cols):
    new_display = set()
    for i in range(rows):
        for j in range(cols):
            count = sum(1 for r, c in neighbors8(i, j, rows, cols) if (r, c) in display)
            if (i, j) in display:
                if count in [2, 3]:
                    new_display.add((i, j))
            else:
                if count == 3:
                    new_display.add((i, j))
    return new_display


def parse(data):
    lines = data.splitlines()
    display = set()
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == "#":
                display.add((i, j))
    return display, len(lines), len(lines[0])


def part1(display, rows, cols):
    for _ in range(100):
        display = step(display, rows, cols)

    return len(display)


def part2(display, rows, cols):
    display.add((0, 0))
    display.add((0, cols - 1))
    display.add((rows - 1, 0))
    display.add((rows - 1, cols - 1))

    for _ in range(100):
        display = step(display, rows, cols)
        display.add((0, 0))
        display.add((0, cols - 1))
        display.add((rows - 1, 0))
        display.add((rows - 1, cols - 1))

    return len(display)


TEST_DATA = {}
