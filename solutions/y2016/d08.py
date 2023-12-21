import solutions.utils.ocr as ocr


def parse(data):
    return data.splitlines()


def parts(lines):
    screen = [[False for _ in range(50)] for _ in range(6)]

    for line in lines:
        if line.startswith("rect"):
            width, height = map(int, line.split()[1].split("x"))
            for x in range(width):
                for y in range(height):
                    screen[y][x] = True
        elif line.startswith("rotate row"):
            y, amount = map(int, line.split("=")[1].split(" by "))
            screen[y] = screen[y][-amount:] + screen[y][:-amount]
        elif line.startswith("rotate column"):
            x, amount = map(int, line.split("=")[1].split(" by "))
            column = [row[x] for row in screen]
            column = column[-amount:] + column[:-amount]
            for y in range(len(screen)):
                screen[y][x] = column[y]

    drawing = "\n".join("".join("#" if c else "." for c in row) for row in screen)
    code = ocr.parse(drawing) if len(lines) > 5 else None
    return sum(sum(row) for row in screen), code


TEST_DATA = {}
TEST_DATA[
    """\
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
""".rstrip()
] = (6, None)
