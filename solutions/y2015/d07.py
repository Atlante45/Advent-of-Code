from functools import cache

mapping = None


@cache
def value_for(x):
    global mapping

    # print(x, isinstance(x, int))

    if isinstance(x, int):
        return x
    if x.isnumeric():
        return int(x)

    val = mapping[x]

    val = val.split()
    if len(val) == 1:
        if val[0].isnumeric():
            return int(val[0])
        else:
            return value_for(val[0])

    res = 0
    if val[0] == "NOT":
        res = ~value_for(val[1])
    if val[1] == "AND":
        res = value_for(val[0]) & value_for(val[2])
    if val[1] == "OR":
        res = value_for(val[0]) | value_for(val[2])
    if val[1] == "LSHIFT":
        res = value_for(val[0]) << int(val[2])
    if val[1] == "RSHIFT":
        res = value_for(val[0]) >> int(val[2])

    if res < 0:
        res = 65536 + res

    return res


def parse(data):
    global mapping
    mapping = {}
    for line in data.splitlines():
        a, b = line.split("->")
        mapping[b.strip()] = a.strip()

    return mapping


def part1(input):
    return value_for("a")


def part2(input):

    val = value_for("a")
    mapping["b"] = str(val)

    # print(value_for.cache_info())
    value_for.cache_clear()

    return value_for("a")


TEST_DATA = {}
