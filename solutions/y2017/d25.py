def parse(data):
    lines = data.splitlines()

    starting_state = lines[0][-2]
    steps = int(lines[1].split()[-2])

    rules = {}
    for i in range(3, len(lines), 10):
        state = lines[i][9]
        rules[state] = {}
        for j in range(i + 1, i + 9, 4):
            value = int(lines[j][26])
            write = int(lines[j + 1][22])
            move = 1 if lines[j + 2][27:] == "right." else -1
            next_state = lines[j + 3][26]
            rules[state][value] = (write, move, next_state)

    return starting_state, steps, rules


def part1(state, steps, rules):
    index = 0
    tape = set()

    for _ in range(steps):
        value = 1 if index in tape else 0
        write, move, next_state = rules[state][value]
        if write:
            tape.add(index)
        else:
            tape.discard(index)
        index += move
        state = next_state
    return len(tape)


def part2(state, steps, rules):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
""".rstrip()
] = (3, None)
