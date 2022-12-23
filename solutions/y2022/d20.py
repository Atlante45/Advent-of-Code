def parse(data):
    return list(enumerate(map(int, data.splitlines())))


def mix(file):
    for i in range(len(file)):
        index, value = next(
            (index, val) for index, (id, val) in enumerate(file) if id == i
        )

        del file[index]
        file.insert((index + value) % len(file), (i, value))
    return file


def part1(file):
    file = mix(file)
    index = next(index for index, (_, val) in enumerate(file) if val == 0)
    return sum([file[(index + i) % len(file)][1] for i in [1000, 2000, 3000]])


def part2(file):
    file = list(map(lambda v: (v[0], v[1] * 811589153), file))
    for _ in range(10):
        file = mix(file)
    index = next(index for index, (_, val) in enumerate(file) if val == 0)
    return sum([file[(index + i) % len(file)][1] for i in [1000, 2000, 3000]])


TEST_DATA = {}
TEST_DATA[
    """\
1
2
-3
3
-2
0
4
""".rstrip()
] = (3, 1623178306)
