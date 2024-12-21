def parse(data):
    a, b = data.split("\n\n\n\n")

    samples = []
    for sample in a.split("\n\n"):
        before, instruction, after = sample.splitlines()
        before = eval(before.split(": ")[1])
        instruction = tuple(map(int, instruction.split()))
        after = eval(after.split(": ")[1])

        samples.append((before, instruction, after))

    program = []
    for line in b.splitlines():
        program.append(tuple(map(int, line.split())))

    return samples, program


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


def part1(samples, program):
    count = 0
    for before, instruction, after in samples:
        op, a, b, c = instruction

        matches = sum(1 for op in INSTRUCTIONS if execute(op, a, b, before) == after[c])
        if matches >= 3:
            count += 1
    return count


def part2(samples, program):
    instructions = {op: set(INSTRUCTIONS) for op in range(len(INSTRUCTIONS))}

    for before, instruction, after in samples:
        op, a, b, c = instruction

        matches = [op for op in INSTRUCTIONS if execute(op, a, b, before) == after[c]]
        instructions[op] &= set(matches)

    mapping = {}
    while len(instructions) > 0:
        for op, candidates in instructions.items():
            if len(candidates) > 1:
                continue

            op_str = next(iter(candidates))
            mapping[op] = op_str

            for _, candidates2 in instructions.items():
                if op_str in candidates2:
                    candidates2.discard(op_str)

            break

        del instructions[op]

    registers = [0, 0, 0, 0]
    for op, a, b, c in program:
        registers[c] = execute(mapping[op], a, b, registers)

    return registers[0]


TEST_DATA = {}
TEST_DATA[
    """\
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]
""".rstrip()
] = (None, None)
