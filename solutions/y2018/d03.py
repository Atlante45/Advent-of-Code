from collections import defaultdict
import re


REGEX = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"


def parse(data):
    claims = []
    for line in data.splitlines():
        id, x, y, w, h = map(int, re.match(REGEX, line).groups())
        claims.append((id, x, y, w, h))
    return claims


def parts(claims):
    fabric = defaultdict(int)
    for _, x, y, w, h in claims:
        for i in range(x, x + w):
            for j in range(y, y + h):
                fabric[(i, j)] += 1

    res1 = sum(1 for v in fabric.values() if v > 1)
    res2 = None

    def valid(x, y, w, h):
        for i in range(x, x + w):
            for j in range(y, y + h):
                if fabric[(i, j)] != 1:
                    return False
        return True

    for id, x, y, w, h in claims:
        if valid(x, y, w, h):
            res2 = id
            break

    return res1, res2


TEST_DATA = {}
