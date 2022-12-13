from collections import deque


def parse(data):
    return data.splitlines()


def part1(input):
    res = 0
    last = int(input[0])

    for line in input:
        cur = int(line)

        if cur > last:
            res += 1

        last = cur

    return res


def part2(input):
    res = 0
    vals = deque([])

    for line in input:
        cur = int(line)

        if len(vals) == 3 and cur > vals.popleft():
            res += 1

        vals.append(cur)

    return res


TEST_DATA = {}
TEST_DATA[
    """\
199
200
208
210
200
207
240
269
260
263
""".rstrip()
] = (7, 5)
