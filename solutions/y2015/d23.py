def parse(data):
    return data.splitlines()


def execute(lines, reg):
    iptr = 0
    while iptr < len(lines):
        if iptr < 0 or iptr >= len(lines):
            break
        inst = lines[iptr]
        match inst[:3]:
            case "hlf":
                reg[inst[4]] //= 2
            case "tpl":
                reg[inst[4]] *= 3
            case "inc":
                reg[inst[4]] += 1
            case "jmp":
                iptr += int(inst[4:])
                continue
            case "jie":
                if reg[inst[4]] % 2 == 0:
                    iptr += int(inst[7:])
                    continue
            case "jio":
                if reg[inst[4]] == 1:
                    iptr += int(inst[7:])
                    continue

        iptr += 1


def part1(lines):
    reg = {"a": 0, "b": 0}
    execute(lines, reg)
    return reg["b"]


def part2(lines):
    reg = {"a": 1, "b": 0}
    execute(lines, reg)
    return reg["b"]


TEST_DATA = {}
TEST_DATA[
    """\
inc b
jio b, +2
tpl b
inc b
""".rstrip()
] = (2, None)
