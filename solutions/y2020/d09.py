def parse(data):
    return [int(line) for line in data.splitlines()]


def parts(numbers):
    preamble_size = 25 if len(numbers) > 100 else 5

    p1 = None
    for i in range(preamble_size, len(numbers)):
        preamble = numbers[i - preamble_size : i]
        if not any(
            numbers[i] - a != a and numbers[i] - a in preamble for a in preamble
        ):
            p1 = numbers[i]
            break

    p2 = None
    for i in range(len(numbers)):
        for j in range(i + 2, len(numbers)):
            if sum(numbers[i:j]) == p1:
                p2 = min(numbers[i:j]) + max(numbers[i:j])
                break

    return p1, p2


TEST_DATA = {}
TEST_DATA[
    """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".rstrip()
] = (127, 62)
