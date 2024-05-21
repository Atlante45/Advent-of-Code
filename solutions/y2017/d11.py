def parse(data):
    return data.split(",")


def parts(path):
    p1res = 0
    p2res = 0

    x = y = 0
    for dir in path:
        match dir:
            case "n":
                y += 1
            case "s":
                y -= 1
            case "ne":
                x += 1
            case "sw":
                x -= 1
            case "nw":
                x -= 1
                y += 1
            case "se":
                x += 1
                y -= 1

        if x * y > 0:
            p1res = abs(x) + abs(y)
        else:
            p1res = max(abs(x), abs(y))
        p2res = max(p2res, p1res)

    return p1res, p2res


TEST_DATA = {}
TEST_DATA[
    """\
ne,ne,ne
""".rstrip()
] = (3, 3)
TEST_DATA[
    """\
ne,ne,sw,sw
""".rstrip()
] = (0, 2)
TEST_DATA[
    """\
ne,ne,s,s
""".rstrip()
] = (2, 2)
TEST_DATA[
    """\
se,sw,se,sw,sw
""".rstrip()
] = (3, 3)
