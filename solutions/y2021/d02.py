def parse(data):
    return data.splitlines()


def part1(input):
    x = 0
    z = 0

    for line in input:
        line = line.split()

        direction = line[0]
        length = int(line[1])
        if direction == "forward":
            x += length
        elif direction == "up":
            z -= length
        elif direction == "down":
            z += length

    return x * z


def part2(input):
    aim = 0
    x = 0
    z = 0

    for line in input:
        line = line.split()

        direction = line[0]
        length = int(line[1])
        if direction == "forward":
            x += length
            z += aim * length
        elif direction == "up":
            aim -= length
        elif direction == "down":
            aim += length

    return x * z


TEST_DATA = {}
TEST_DATA[
    """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".rstrip()
] = (150, 900)
