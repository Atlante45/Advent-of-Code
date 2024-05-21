from collections import defaultdict


def parse(data):
    return data.splitlines()


def part1(lines):
    registers = defaultdict(int)

    def get_value(x):
        try:
            return int(x)
        except ValueError:
            return registers[x]

    instr = 0
    mul_count = 0
    while 0 <= instr < len(lines):
        parts = lines[instr].split()
        match parts[0]:
            case "set":
                registers[parts[1]] = get_value(parts[2])
            case "sub":
                registers[parts[1]] -= get_value(parts[2])
            case "mul":
                registers[parts[1]] *= get_value(parts[2])
                mul_count += 1
            case "jnz":
                if get_value(parts[1]) != 0:
                    instr += get_value(parts[2])
                    continue
        instr += 1
    return mul_count


def run(input_val):
    h = 0

    b = 100 * input_val + 100000
    for _ in range(1001):
        for d in range(2, b):
            if b % d == 0:
                h += 1
                break
        b += 17

    return h


def part2(lines):
    input_val = int(lines[0].split()[2])
    return run(input_val)


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
