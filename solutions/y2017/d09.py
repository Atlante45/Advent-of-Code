def parse(data):
    return data.strip()


def is_escaped(stream, index):
    if index == 0:
        return False

    i = index - 1
    while stream[i] == "!":
        i -= 1

    return (index - i) % 2 == 0


def parts(stream):
    p1res = 0
    p2res = 0

    index = 0
    depth = 0
    while index < len(stream):
        match stream[index]:
            case "{":
                depth += 1
                p1res += depth
            case "}":
                depth -= 1
            case "<":
                pot = stream.find(">", index)
                while is_escaped(stream, pot):
                    pot = stream.find(">", pot + 1)
                p2res += pot - index - 1
                index = pot
        index += 1

    index = stream.find("!")
    while 0 <= index and index < len(stream):
        p2res -= 2
        index = stream.find("!", index + 2)

    return p1res, p2res


TEST_DATA = {}
TEST_DATA[
    """\
\{\{{},{},{{}}}}
""".rstrip()
] = (16, 0)
TEST_DATA[
    """\
{<{o"i!a,<{i<a>}
""".rstrip()
] = (1, 10)
