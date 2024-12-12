from functools import cache


def parse(data):
    return list(map(int, data.split()))


@cache
def recurse(num, blinks):
    if blinks == 0:
        return 1
    if num == 0:
        return recurse(1, blinks - 1)
    
    num_str = str(num)
    if len(num_str) % 2 == 0:
        half = len(num_str) // 2
        left = int(num_str[:half])
        right = int(num_str[half:])
        return recurse(left, blinks - 1) + recurse(right, blinks - 1)
    else:
        return recurse(num * 2024, blinks - 1)


def part1(lines):
    return sum(recurse(num, 25) for num in lines)


def part2(lines):
    return sum(recurse(num, 75) for num in lines)


TEST_DATA = {}
TEST_DATA[
    """\
125 17
""".rstrip()
] = (55312, None)
