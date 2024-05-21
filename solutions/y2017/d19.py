def parse(data):
    lines = data.splitlines()
    diagram = {}

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == " ":
                continue
            diagram[i, j] = c

    return diagram, (0, lines[0].index("|"))


def parts(diagram, start):
    pos = start
    direction = (1, 0)
    letters = []
    steps = 0

    while True:
        steps += 1
        pos = (pos[0] + direction[0], pos[1] + direction[1])

        if pos not in diagram:
            break

        c = diagram[pos]

        if c == "+":
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    d != direction
                    and d != (-direction[0], -direction[1])
                    and (pos[0] + d[0], pos[1] + d[1]) in diagram
                ):
                    direction = d
                    break
        elif c.isalpha():
            letters.append(c)

    return "".join(letters), steps


TEST_DATA = {}
TEST_DATA[
    """\
     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
""".rstrip()
] = ("ABCDEF", 38)
