def parse(data):
    return [
        int(v) for v in list(zip(*[line.split() for line in data.splitlines()]))[-1]
    ]


MOD = 2**16


def part1(nums):
    res = 0
    a, b = nums
    for _ in range(40_000_000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a % MOD == b % MOD:
            res += 1
    return res


def part2(nums):
    res = 0
    a, b = nums
    for _ in range(5_000_000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647

        while a % 4 != 0:
            a = (a * 16807) % 2147483647
        while b % 8 != 0:
            b = (b * 48271) % 2147483647

        if a % MOD == b % MOD:
            res += 1
    return res


TEST_DATA = {}
TEST_DATA[
    """\
Generator A starts with 65
Generator B starts with 8921
""".rstrip()
] = (588, 309)
