from collections import deque
from hashlib import md5

from more_itertools import sliding_window


def parse(data):
    return data.strip()


def generate(salt, index):
    hash = md5((salt + str(index)).encode()).hexdigest()
    triples = [w[0] for w in sliding_window(hash, 3) if len(set(w)) == 1]
    fivers = [w[0] for w in sliding_window(hash, 5) if len(set(w)) == 1]
    return hash, triples[0] if triples else None, fivers


def generate2(salt, index):
    hash = md5((salt + str(index)).encode()).hexdigest()
    for _ in range(2016):
        hash = md5(hash.encode()).hexdigest()
    triples = [w[0] for w in sliding_window(hash, 3) if len(set(w)) == 1]
    fivers = [w[0] for w in sliding_window(hash, 5) if len(set(w)) == 1]
    return hash, triples[0] if triples else None, fivers


def solve(salt, generator):
    hashes = deque()
    keys = 0

    index = 0
    while len(hashes) < 1000:
        hashes.append((index, *generator(salt, index)))
        index += 1

    while True:
        hashes.append((index, *generator(salt, index)))
        index += 1

        i, _, triple, _ = hashes.popleft()
        if triple:
            for _, _, _, fivers in hashes:
                if triple in fivers:
                    keys += 1
                    if keys == 64:
                        return i
                    break


def part1(salt):
    return solve(salt, generate)


def part2(salt):
    return solve(salt, generate2)


TEST_DATA = {}
TEST_DATA[
    """\
abc
""".rstrip()
] = (22728, 22551)
