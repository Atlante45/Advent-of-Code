VOWELS = "aeiou"
BAD = ["ab", "cd", "pq", "xy"]


def parse(data):
    return data.splitlines()


def part1(input):
    res = 0

    for line in input:
        if sum([c in VOWELS for c in line]) < 3:
            continue
        if any([k in line for k in BAD]):
            continue
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                res += 1
                break

    return res


def part2(input):
    res = 0
    for line in input:
        cond1, cond2 = False, False
        for i in range(len(line) - 2):
            cond1 = cond1 or line[i : i + 2] in line[i + 2 :]
            cond2 = cond2 or line[i] == line[i + 2]
            if cond1 and cond2:
                res += 1
                break

    return res


TEST_DATA = {}
TEST_DATA[
    """\
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
""".rstrip()
] = (2, 0)
