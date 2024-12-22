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


def generate(number, steps, sequences):
    last_price = number % 10
    changes = []

    seen = set()
    for _ in range(4):
        number = step(number)
        price = number % 10
        changes.append(price - last_price)
        last_price = price

    for _ in range(steps - 4):
        number = step(number)
        price = number % 10
        changes.append(price - last_price)
        last_price = price

        changes.pop(0)

        t = tuple(changes)
        if t in seen:
            continue
        seen.add(t)
        sequences[t] += price

    return number


def parts(lines):
    mappings = defaultdict(int)
    p1res = sum(generate(int(line), 2000, mappings) for line in lines)
    p2res = max(mappings.values())
    return p1res, p2res


TEST_DATA = {}
TEST_DATA[
    """\
1
10
100
2024
""".rstrip()
] = (37327623, 24)
TEST_DATA[
    """\
1
2
3
2024
""".rstrip()
] = (37990510, 23)
