from itertools import count


def parse(data):
    return [line.split() for line in data.splitlines()]


def asmbunny(instructions, registers):
    output = []
    states = set()

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
            case "out":
                v = registers[inst[1]] if inst[1] in registers else int(inst[1])
                output.append(v)
                state = tuple(registers.values()) + (ipr,)
                if state in states:
                    return output, True
                states.add(state)
        ipr += 1
    return output, False


def part1(lines):
    target = int("0101010101010", 2)
    value = int(lines[1][1]) * int(lines[2][1])
    return target - value


def part2(lines):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
cpy a d
cpy 9 c
cpy 282 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0  null
cpy a b
cpy 0 a  {a: 0, b: i + 9 * 282, c: 0, d: i + 9 * 282}
cpy 2 c
jnz b 2
jnz 1 6  null
dec b
dec c
jnz c -4
inc a
jnz 1 -7 null
# cpy 2 b
# jnz c 2
# jnz 1 4
# dec b
# dec c
# jnz 1 -4
# jnz 0 0
# out b
# jnz a -19
# jnz 1 -21
""".rstrip()
] = (None, None)
