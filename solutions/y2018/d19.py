from math import sqrt


def parse(data):
    lines = data.splitlines()
    ip = int(lines[0].split()[1])
    program = []
    for line in lines[1:]:
        op, a, b, c = line.split()
        program.append((op, int(a), int(b), int(c)))

    return ip, program


INSTRUCTIONS = [
    "addr",
    "addi",
    "mulr",
    "muli",
    "banr",
    "bani",
    "borr",
    "bori",
    "setr",
    "seti",
    "gtir",
    "gtri",
    "gtrr",
    "eqir",
    "eqri",
    "eqrr",
]


def execute(op, a, b, registers):
    match op:
        case "addr":
            return registers[a] + registers[b]
        case "addi":
            return registers[a] + b
        case "mulr":
            return registers[a] * registers[b]
        case "muli":
            return registers[a] * b
        case "banr":
            return registers[a] & registers[b]
        case "bani":
            return registers[a] & b
        case "borr":
            return registers[a] | registers[b]
        case "bori":
            return registers[a] | b
        case "setr":
            return registers[a]
        case "seti":
            return a
        case "gtir":
            return 1 if a > registers[b] else 0
        case "gtri":
            return 1 if registers[a] > b else 0
        case "gtrr":
            return 1 if registers[a] > registers[b] else 0
        case "eqir":
            return 1 if a == registers[b] else 0
        case "eqri":
            return 1 if registers[a] == b else 0
        case "eqrr":
            return 1 if registers[a] == registers[b] else 0
        case _:
            raise ValueError(f"Invalid instruction: {op}")


def sum_of_divisors(num):
    sum_of_divisors = 0
    for i in range(1, int(sqrt(num))):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors


def parts(ip, program):
    ip_reg = ip
    registers = [1, 0, 0, 0, 0, 0]

    p1 = None

    ip = 0
    while ip < len(program):
        registers[ip_reg] = ip
        op, a, b, c = program[ip]

        if op == "addr" and c == ip_reg:
            p1 = sum_of_divisors(max(registers))

        if op == "seti" and c == 0:
            break

        registers[c] = execute(op, a, b, registers)

        ip = registers[ip_reg] + 1

    p2 = sum_of_divisors(max(registers))
    return p1, p2


TEST_DATA = {}
TEST_DATA[
    """\
#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
""".rstrip()
] = (6, None)
