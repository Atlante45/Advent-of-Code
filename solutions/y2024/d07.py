def parse(data):
    res = []
    for line in data.splitlines():
        line = line.split(":")
        res.append((int(line[0]), [int(x) for x in line[1].split()]))
    return res


def recurse(num, vals, do_concat=False):
    if len(vals) == 1:
        return num == vals[0]
    
    val = vals[-1]

    res = False
    if num > val:
        res |= recurse(num - val, vals[:-1], do_concat)
    if num % val == 0:
        res |= recurse(num // val, vals[:-1], do_concat)
    if do_concat and str(num).endswith(str(val)) and len(str(num)) > len(str(val)):
        res |= recurse(int(str(num)[:-len(str(val))]), vals[:-1], do_concat)

    return res


def part1(eqs):
    return sum(eq[0] for eq in eqs if recurse(eq[0], eq[1]))


def part2(eqs):
    return sum(eq[0] for eq in eqs if recurse(eq[0], eq[1], do_concat=True))


TEST_DATA = {}
TEST_DATA[
    """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".rstrip()
] = (3749, 11387)
