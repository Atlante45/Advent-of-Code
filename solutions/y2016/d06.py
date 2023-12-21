from typing import Counter


def parse(data):
    return data.splitlines()


def part1(lines):
    return "".join(Counter(col).most_common(1)[0][0] for col in zip(*lines))


def part2(lines):
    return "".join(Counter(col).most_common()[-1][0] for col in zip(*lines))


TEST_DATA = {}
TEST_DATA[
    """\
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
""".rstrip()
] = ("easter", "advent")
