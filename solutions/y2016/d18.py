def parse(data):
    return data.strip()


def solve(row, count):
    safe_tiles = row.count(".")
    for _ in range(count - 1):
        safe_row = "." + row + "."
        new_row = ""
        for i in range(len(row)):
            if safe_row[i : i + 3] in ["^^.", ".^^", "^..", "..^"]:
                new_row += "^"
            else:
                new_row += "."
        safe_tiles += new_row.count(".")
        row = new_row
    return safe_tiles


def part1(row):
    return solve(row, 40)


def part2(row):
    return solve(row, 400000)


TEST_DATA = {}
TEST_DATA[
    """\
.^^.^.^^^^
""".rstrip()
] = (None, None)
