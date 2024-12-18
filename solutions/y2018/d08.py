def parse(data):
    return list(map(int, data.split()))


def read_tree(tree, i):
    children, metadata = tree[i], tree[i + 1]
    i += 2

    sum = 0
    for _ in range(children):
        meta, i = read_tree(tree, i)
        sum += meta

    for _ in range(metadata):
        sum += tree[i]
        i += 1

    return sum, i


def part1(tree):
    return read_tree(tree, 0)[0]


def weight(tree, i):
    children, metadata = tree[i], tree[i + 1]
    i += 2

    if children == 0:
        return sum(tree[i : i + metadata]), i + metadata

    weights = [0]
    for _ in range(children):
        w, i = weight(tree, i)
        weights.append(w)

    w = sum(weights[x] for x in tree[i : i + metadata] if x < len(weights))
    return w, i + metadata


def part2(tree):
    return weight(tree, 0)[0]


TEST_DATA = {}
TEST_DATA[
    """\
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
""".rstrip()
] = (138, 66)
