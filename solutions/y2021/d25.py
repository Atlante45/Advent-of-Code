import copy


def parse(data):
    return [list(line) for line in data.splitlines()]


def part1(input):
    res = 0
    while True:
        moved = False
        new_input = copy.deepcopy(input)
        for i in range(len(input)):
            for j in range(len(input[0])):
                j2 = (j + 1) % len(input[0])
                if input[i][j] == ">" and input[i][j2] == ".":
                    new_input[i][j] = "."
                    new_input[i][j2] = ">"
                    moved = True

        input = new_input
        new_input = copy.deepcopy(input)

        for i in range(len(input)):
            for j in range(len(input[0])):
                i2 = (i + 1) % len(input)
                if input[i][j] == "v" and input[i2][j] == ".":
                    new_input[i][j] = "."
                    new_input[i2][j] = "v"
                    moved = True
        input = new_input

        res += 1
        if not moved:
            break

    return res


def part2(input):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".rstrip()
] = (58, None)
