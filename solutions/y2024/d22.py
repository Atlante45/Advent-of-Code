from collections import defaultdict


def parse(data):
    return data.splitlines()


def step(number):
    number ^= number * 64
    number %= 16777216
    number ^= number // 32
    number %= 16777216
    number ^= number * 2048
    number %= 16777216
    return number


def generate(number, steps):
    for _ in range(steps):
        number = step(number)
    return number


def generate2(number, steps):
    price = [number % 10]
    changes = []

    mapping = defaultdict(int)
    for _ in range(steps):
        number = step(number)
        price.append((number % 10))
        changes.append(price[-1] - price[-2])

        if tuple(changes[-4:]) in mapping:
            continue
        mapping[tuple(changes[-4:])] = price[-1]

    return mapping


def part1(lines):
    return sum(generate(int(line), 2000) for line in lines)


def part2(lines):
    mappings = []
    for line in lines:
        mapping = generate2(int(line), 2000)
        mappings.append(mapping)

    all_sequences = set()
    for m in mappings:
        all_sequences.update(m.keys())

    max_p = 0
    for sequence in all_sequences:
        max_p = max(max_p, sum(m[sequence] for m in mappings))

    return max_p


TEST_DATA = {}
TEST_DATA[
    """\
1
10
100
2024
""".rstrip()
] = (37327623, None)
TEST_DATA[
    """\
1
2
3
2024
""".rstrip()
] = (None, 23)
