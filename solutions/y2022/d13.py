import json
from functools import cmp_to_key
from more_itertools import chunked


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a > b) - (a < b)

    if isinstance(a, int):
        a = [a]

    if isinstance(b, int):
        b = [b]

    for i in range(min(len(a), len(b))):
        comp = compare(a[i], b[i])
        if comp != 0:
            return comp

    return compare(len(a), len(b))


def parse(data):
    return list(map(json.loads, filter(None, data.splitlines())))


def part1(packets):
    return sum(i + 1 for i, p in enumerate(chunked(packets, 2)) if compare(*p) == -1)


def part2(packets):
    packets = sorted(packets + [[[2]], [[6]]], key=cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


TEST_DATA = {}
TEST_DATA[
    """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".rstrip()
] = (13, 140)
