def parse(data):
    return data.splitlines()

def recurse(num, vals):
    if len(vals) == 1:
        return num == vals[0]

    res = recurse(num - vals[-1], vals[:-1])
    if num % vals[-1] == 0:
        res |= recurse(num // vals[-1], vals[:-1])

    return res

def recurse2(num, vals):
    if len(vals) == 1:
        return num == vals[0]
    
    val = vals[-1]

    res = False
    if num > val:
        res = recurse2(num - val, vals[:-1])
    if num % val == 0:
        res |= recurse2(num // val, vals[:-1])

    if str(num).endswith(str(val)) and len(str(num)) > len(str(val)):
        res |= recurse2(int(str(num)[:-len(str(val))]), vals[:-1])
    

    return res

def part1(lines):
    res = 0

    for line in lines:
        line = line.split(":")
        num = int(line[0])
        vals = [int(x) for x in line[1].split()]


        if recurse(num, vals):
            res += num

    return res


def part2(lines):
    res = 0

    for line in lines:
        line = line.split(":")
        num = int(line[0])
        vals = [int(x) for x in line[1].split()]

        if recurse2(num, vals):
            res += num

    return res


TEST_DATA = {}
TEST_DATA[
    """\
192: 17 8 14
""".rstrip()
] = (None, 192)
# TEST_DATA[
#     """\
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """.rstrip()
# ] = (3749, 11387)
