def parse(data):
    return data.split(",")


def dance(moves, programs):
    for move in moves:
        match move[0]:
            case "s":
                n = int(move[1:])
                programs = programs[-n:] + programs[:-n]
            case "x":
                a, b = move[1:].split("/")
                a, b = int(a), int(b)
                programs[a], programs[b] = programs[b], programs[a]
            case "p":
                a, b = move[1:].split("/")
                a, b = programs.index(a), programs.index(b)
                programs[a], programs[b] = programs[b], programs[a]
    return programs


def part1(moves):
    programs = list("abcdefghijklmnop") if len(moves) > 5 else list("abcde")
    programs = dance(moves, programs)
    return "".join(programs)


def part2(lines):
    programs = list("abcdefghijklmnop")

    visited = {"".join(programs): 0}
    for i in range(1_000_000_000):
        programs = dance(lines, programs)
        key = "".join(programs)
        if key in visited:
            remainder = 1_000_000_000 - i - 1
            cycle = i + 1 - visited[key]
            for _ in range(remainder % cycle):
                programs = dance(lines, programs)
            return "".join(programs)
        visited[key] = i + 1


TEST_DATA = {}
TEST_DATA[
    """\
s1,x3/4,pe/b
""".rstrip()
] = ("baedc", None)
