def parse(data):
    lines = data.splitlines()
    a = int(lines[0].split()[-1])
    b = int(lines[1].split()[-1])
    c = int(lines[2].split()[-1])
    program = [int(x) for x in lines[4].split()[1].split(",")]
    return a, b, c, program


def run_program(program, a, b, c):
    iptr = 0
    output = []
    while iptr >= 0 and iptr < len(program):
        op = program[iptr]
        arg = program[iptr + 1]
        iptr += 2

        if arg >= 0 and arg <= 3:
            val = arg
        elif arg == 4:
            val = a
        elif arg == 5:
            val = b
        elif arg == 6:
            val = c
        elif arg == 7:
            raise "invalid arg"

        if op == 0:
            a = a // 2**val
        elif op == 1:
            b = b ^ arg
        elif op == 2:
            b = val % 8
        elif op == 3:
            if a != 0:
                iptr = arg
        elif op == 4:
            b = b ^ c
        elif op == 5:
            output.append(val % 8)
        elif op == 6:
            b = a // 2**val
        elif op == 7:
            c = a // 2**val
        else:
            raise "invalid op"

    return output


def part1(a, b, c, program):
    output = run_program(program, a, b, c)
    return ",".join([str(x) for x in output])


def generate(program, a, iptr):
    if iptr < 0:
        return a

    for i in range(8):
        ta = (a << 3) | i
        output = run_program(program, ta, 0, 0)
        if output[0] == program[iptr]:
            res = generate(program, ta, iptr - 1)
            if res is not None:
                return res


def part2(a, b, c, program):
    return generate(program, 0, len(program) - 1)


TEST_DATA = {}
TEST_DATA[
    """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".rstrip()
] = ("4,6,3,5,6,3,5,2,1,0", None)
TEST_DATA[
    """\
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
""".rstrip()
] = ("0,1,2", None)
TEST_DATA[
    """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".rstrip()
] = ("4,2,5,6,7,7,7,7,3,1,0", None)
TEST_DATA[
    """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".rstrip()
] = (None, 117440)
