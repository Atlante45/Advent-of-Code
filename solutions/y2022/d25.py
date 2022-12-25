from math import log, ceil


DIGITS = ["=", "-", "0", "1", "2"]


def add_one(num):
    if num == "":
        return "1"
    if num[-1] == "0":
        return num[:-1] + "1"
    if num[-1] == "1":
        return num[:-1] + "2"
    if num[-1] == "2":
        return add_one(num[:-1]) + "="
    if num[-1] == "=":
        return num[:-1] + "-"
    if num[-1] == "-":
        return num[:-1] + "0"


def parse(data):
    return data.splitlines()


def part1(lines):
    total = 0
    for line in lines:
        n = 0
        m = 1
        for c in reversed(line):
            n += (DIGITS.index(c) - 2) * m
            m *= 5
        total += n

    res = ""
    p = ceil(log(total, 5))
    for m in range(p, -1, -1):
        match total // 5**m:
            case 0:
                if res != "":
                    res += "0"
            case 1:
                res += "1"
            case 2:
                res += "2"
            case 3:
                res = add_one(res) + "="
            case 4:
                res = add_one(res) + "-"
        total %= 5**m

    return res


def part2(lines):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
""".rstrip()
] = ("2=-1=0", None)
