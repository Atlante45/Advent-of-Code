from math import prod
import re


def parse(data):
    REGEX = r"mul\((\d+,\d+)\)|(do)\(\)|(don't)\(\)"
    return re.findall(REGEX, data)


def parts(matches):
    enabled = True
    sum1 = 0
    sum2 = 0
    for i in range(len(matches)):
        if matches[i][1] == 'do':
            enabled = True
        elif matches[i][2] == "don't":
            enabled = False
        else:
            x = prod(map(int, matches[i][0].split(',')))
            sum1 += x
            sum2 += x if enabled else 0

    return sum1, sum2




TEST_DATA = {}
TEST_DATA[
    """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".rstrip()
] = (161, 161)
TEST_DATA[
    """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".rstrip()
] = (161, 48)
