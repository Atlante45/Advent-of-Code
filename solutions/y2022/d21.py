def parse(data):
    monkeys = {}
    for line in data.splitlines():
        monkey, val = line.split(": ")
        if val.isnumeric():
            val = int(val)
        monkeys[monkey] = val
    # print(len(monkeys))
    reduce(monkeys)
    # print(len(monkeys))
    # print(monkeys)
    return monkeys


def reduce(monkeys, monkey="root"):
    if monkey == "humn":
        return None

    val = monkeys[monkey]
    if isinstance(val, int):
        return val
    mon1, op, mon2 = val.split(" ")
    m1 = reduce(monkeys, mon1)
    m2 = reduce(monkeys, mon2)

    if m1 is None and m2 is None:
        print("both none")
        return None
    if m1 is None or m2 is None:
        return None

    res = None
    match op:
        case "*":
            res = m1 * m2
        case "+":
            res = m1 + m2
        case "-":
            res = m1 - m2
        case "/":
            res = m1 // m2

    monkeys[monkey] = res
    del monkeys[mon1]
    del monkeys[mon2]
    return res


def compute(monkeys, monkey="root"):
    val = monkeys[monkey]
    if isinstance(val, int):
        return val
    m1, op, m2 = val.split(" ")
    m1 = compute(monkeys, m1)
    m2 = compute(monkeys, m2)
    match op:
        case "*":
            return m1 * m2
        case "+":
            return m1 + m2
        case "-":
            return m1 - m2
        case "/":
            return m1 // m2


def compute2(monkeys, monkey="root", total=None):
    if monkey == "humn":
        return total

    val = monkeys[monkey]
    m1, op, m2 = val.split(" ")

    if m1 != "humn" and isinstance(monkeys[m1], int):
        m1 = monkeys[m1]
    if m2 != "humn" and isinstance(monkeys[m2], int):
        m2 = monkeys[m2]

    if monkey == "root":
        if isinstance(m1, int):
            return compute2(monkeys, m2, m1)
        else:
            return compute2(monkeys, m1, m2)

    match op:
        case "*":
            if isinstance(m1, int):
                return compute2(monkeys, m2, total // m1)
            else:
                return compute2(monkeys, m1, total // m2)
        case "+":
            if isinstance(m1, int):
                return compute2(monkeys, m2, total - m1)
            else:
                return compute2(monkeys, m1, total - m2)
        case "-":
            if isinstance(m1, int):
                return compute2(monkeys, m2, m1 - total)
            else:
                return compute2(monkeys, m1, total + m2)
        case "/":
            if isinstance(m1, int):
                return compute2(monkeys, m2, m1 // total)
            else:
                return compute2(monkeys, m1, total * m2)


def part1(monkeys):
    return compute(monkeys)


def part2(monkeys):
    return compute2(monkeys)


TEST_DATA = {}
TEST_DATA[
    """\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".rstrip()
] = (152, 301)
