def parse(data):
    instructions = []
    for line in data.splitlines():
        op, arg = line.split()
        instructions.append((op, int(arg)))
    return instructions


def run(instructions, ip, acc, visited, fix):
    while ip < len(instructions):
        if ip in visited:
            return True, acc

        visited.add(ip)
        op, arg = instructions[ip]

        if fix and op == "nop":
            looped, n_acc = run(instructions, ip + arg, acc, visited.copy(), False)
            if not looped:
                return False, n_acc
        elif fix and op == "jmp":
            looped, n_acc = run(instructions, ip + 1, acc, visited.copy(), False)
            if not looped:
                return False, n_acc

        if op == "nop":
            ip += 1
        elif op == "acc":
            acc += int(arg)
            ip += 1
        elif op == "jmp":
            ip += int(arg)

    return False, acc


def part1(instructions):
    looped, acc = run(instructions, 0, 0, set(), False)
    assert looped
    return acc


def part2(instructions):
    for i, instruction in enumerate(instructions):
        op, arg = instruction
        if op == "nop" and arg != 0:
            looped, acc = run(instructions, 0, 0, set(), True)
            if not looped:
                return acc
        elif op == "jmp" and arg != 0:
            looped, acc = run(instructions, 0, 0, set(), True)
            if not looped:
                return acc


TEST_DATA = {}
TEST_DATA[
    """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".rstrip()
] = (5, 8)
