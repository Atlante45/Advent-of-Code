def parse(data):
    return [line.split() for line in data.splitlines()]


def asmbunny(instructions, registers):
    ipr = 0
    while ipr >= 0 and ipr < len(instructions):
        inst = instructions[ipr]

        match inst[0]:
            case "cpy":
                if inst[1] in registers:
                    registers[inst[2]] = registers[inst[1]]
                else:
                    registers[inst[2]] = int(inst[1])
            case "inc":
                registers[inst[1]] += 1
            case "dec":
                registers[inst[1]] -= 1
            case "jnz":
                v = registers[inst[1]] if inst[1] in registers else int(inst[1])
                if v != 0:
                    ipr += int(inst[2])
                    continue
        ipr += 1
    return registers


def part1(instructions):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    asmbunny(instructions, registers)
    return registers["a"]


def part2(instructions):
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    asmbunny(instructions, registers)
    return registers["a"]


TEST_DATA = {}
TEST_DATA[
    """\
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
""".rstrip()
] = (42, None)
