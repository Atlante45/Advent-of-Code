def parse(data):
    return [tuple(map(int, line.split("/"))) for line in data.splitlines()]


def build_bridge(components, start, strength):
    max_strength = strength
    for i, (a, b) in enumerate(components):
        if a == start:
            new_components = components[:i] + components[i + 1 :]
            max_strength = max(
                max_strength, build_bridge(new_components, b, strength + a + b)
            )
        elif b == start:
            new_components = components[:i] + components[i + 1 :]
            max_strength = max(
                max_strength, build_bridge(new_components, a, strength + a + b)
            )
    return max_strength


def build_long_bridge(components, start, strength, length):
    max_strength = strength
    max_length = length
    for i, (a, b) in enumerate(components):
        if a == start:
            new_components = components[:i] + components[i + 1 :]
            new_strength, new_length = build_long_bridge(
                new_components, b, strength + a + b, length + 1
            )
            if new_length > max_length or (
                new_length == max_length and new_strength > max_strength
            ):
                max_strength = new_strength
                max_length = new_length
        elif b == start:
            new_components = components[:i] + components[i + 1 :]
            new_strength, new_length = build_long_bridge(
                new_components, a, strength + a + b, length + 1
            )
            if new_length > max_length or (
                new_length == max_length and new_strength > max_strength
            ):
                max_strength = new_strength
                max_length = new_length
    return max_strength, max_length


def part1(components):
    return build_bridge(components, 0, 0)


def part2(components):
    return build_long_bridge(components, 0, 0, 0)[0]


TEST_DATA = {}
TEST_DATA[
    """\
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".rstrip()
] = (31, None)
