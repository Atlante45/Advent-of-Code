import json


def recurse(val, filter):
    res = 0
    if isinstance(val, dict):
        for k, v in val.items():
            if filter and v == "red":
                return 0
            res += recurse(k, filter) + recurse(v, filter)

    if isinstance(val, list):
        for v in val:
            res += recurse(v, filter)

    if isinstance(val, int):
        res += val

    return res


def parse(data):
    return json.loads(data)


def part1(data):
    return recurse(data, False)


def part2(data):
    return recurse(data, True)


TEST_DATA = {}
TEST_DATA[
    """\
{"a":[-1,13]}
""".rstrip()
] = (None, None)
