from solutions.utils.graph import neighbors4, neighbors8


def parse(data):
    return data.splitlines()


def part1(lines):
    sum = 0

    max_i = len(lines)
    max_j = len(lines[0])

    num = 0
    part = False
    for i in range(len(lines)):
        # print(lines[i])
        for j in range(len(lines[i])):
            # print(lines[i][j])
            if lines[i][j].isdigit():
                num = 10 * num + int(lines[i][j])
                for x, y in neighbors8(i, j, max_i, max_j):
                    if not lines[x][y].isdigit() and lines[x][y] != ".":
                        part = True
                        break
            elif part:
                sum += num
                num = 0
                part = False
            else:
                num = 0
                part = False
        if part:
            sum += num
            num = 0
            part = False
        else:
            num = 0
            part = False
    return sum


def get_number(lines, x, y):
    while y > 0 and lines[x][y - 1].isdigit():
        y -= 1

    num = 0
    while y < len(lines[0]) and lines[x][y].isdigit():
        num = 10 * num + int(lines[x][y])
        y += 1
    return num


def part2(lines):
    sum = 0

    max_i = len(lines)
    max_j = len(lines[0])
    valid = lambda i, j: i >= 0 and j >= 0 and i < max_i and j < max_j

    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                ratio = 1
                count = 0

                x = i
                y = j - 1
                if valid(x, y) and lines[x][y].isdigit():
                    ratio *= get_number(lines, x, y)
                    count += 1
                y = j + 1
                if valid(x, y) and lines[x][y].isdigit():
                    ratio *= get_number(lines, x, y)
                    count += 1

                x = i - 1
                y = j
                if valid(x, y) and lines[x][y].isdigit():
                    ratio *= get_number(lines, x, y)
                    count += 1
                else:
                    y = j - 1
                    if valid(x, y) and lines[x][y].isdigit():
                        ratio *= get_number(lines, x, y)
                        count += 1
                    y = j + 1
                    if valid(x, y) and lines[x][y].isdigit():
                        ratio *= get_number(lines, x, y)
                        count += 1

                x = i + 1
                y = j
                if valid(x, y) and lines[x][y].isdigit():
                    ratio *= get_number(lines, x, y)
                    count += 1
                else:
                    y = j - 1
                    if valid(x, y) and lines[x][y].isdigit():
                        ratio *= get_number(lines, x, y)
                        count += 1
                    y = j + 1
                    if valid(x, y) and lines[x][y].isdigit():
                        ratio *= get_number(lines, x, y)
                        count += 1

                if count == 2:
                    sum += ratio

    return sum


TEST_DATA = {}
TEST_DATA[
    """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".rstrip()
] = (4361, 467835)
