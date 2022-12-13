from functools import reduce


def compute_monad(constants, func):
    monad = [None] * 14
    stack = []
    for j in range(14):
        if constants[0][j] == 1:
            stack.append(j)
        else:
            i = stack.pop()
            monad[i], monad[j] = func(constants[2][i] + constants[1][j])

    return reduce(lambda a, b: 10 * a + b, monad, 0)


def parse(data):
    data = [line.split() for line in data.splitlines()]

    constants = []
    for offset in [4, 5, 15]:
        constants.append([int(data[18 * i + offset][2]) for i in range(14)])

    # assert(all(c0 in [1, 26] for c0 in constants[0]))
    # assert(constants[0].count(1) == constants[0].count(26))
    # assert(all(9 - c1 >= 0 and 9 - c1 < 26 for c0, c1, _ in zip(*constants) if c0 == 26))
    # assert(all(9 + c2 >= 0 and 9 + c2 < 26 for c0, _, c2 in zip(*constants) if c0 == 1))
    return constants


def part1(constants):
    maximize = lambda c: (9 - c, 9) if c > 0 else (9, 9 + c)
    return compute_monad(constants, maximize)


def part2(constants):
    minimize = lambda c: (1, 1 + c) if c > 0 else (1 - c, 1)
    return compute_monad(constants, minimize)


TEST_DATA = {}
