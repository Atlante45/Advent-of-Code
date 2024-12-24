import re


def parse(data):
    nums = sorted(set(map(int, re.findall(r"\d+", data))))
    return nums[-2]


def next_r3(r3, value):
    r2 = r3 | 0b10000000000000000
    r3 = value
    while r2 > 0:
        r3 += r2 & 0b11111111
        r3 *= 65899  # 10000000101101011
        r3 &= 0b111111111111111111111111
        r2 = r2 // 256
    return r3


def parts(value):
    seen = set()

    p1 = next_r3(0, value)
    r3 = p1
    while True:
        new_r3 = next_r3(r3, value)
        if new_r3 in seen:
            return p1, r3
        r3 = new_r3
        seen.add(r3)


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
