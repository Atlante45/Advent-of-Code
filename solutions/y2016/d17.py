from hashlib import md5
import heapq


DIRS = [(0, "U", -1, 0), (1, "D", 1, 0), (2, "L", 0, -1), (3, "R", 0, 1)]


def parse(data):
    return data.strip()


def part1(passcode):
    heap = [(0, 0, 0, "")]
    while heap:
        _, x, y, path = heapq.heappop(heap)
        hash = md5((passcode + path).encode()).hexdigest()[:4]
        for i, d, dx, dy in DIRS:
            if hash[i] not in "bcdef":
                continue
            nx = x + dx
            ny = y + dy
            if nx == 3 and ny == 3:
                return path + d
            if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                heapq.heappush(heap, (len(path + d), nx, ny, path + d))


def part2(passcode):
    res = 0
    heap = [(0, 0, 0, "")]
    while heap:
        _, x, y, path = heapq.heappop(heap)
        hash = md5((passcode + path).encode()).hexdigest()[:4]
        for i, d, dx, dy in DIRS:
            if hash[i] not in "bcdef":
                continue
            nx = x + dx
            ny = y + dy
            if nx == 3 and ny == 3:
                res = len(path + d)
                continue
            if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                heapq.heappush(heap, (len(path + d), nx, ny, path + d))
    return res


TEST_DATA = {}
TEST_DATA[
    """\
ihgpwlah
""".rstrip()
] = ("DDRRRD", None)
TEST_DATA[
    """\
kglvqrro
""".rstrip()
] = ("DDUDRLRRUDRD", None)
TEST_DATA[
    """\
ulqzkmiv
""".rstrip()
] = ("DRURDRUDDLLDLUURRDULRLDUUDDDRR", None)
