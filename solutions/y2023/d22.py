from collections import defaultdict


def parse(data):
    bricks = []
    for line in data.splitlines():
        a, b = line.split("~")
        s = list(map(int, a.split(",")))
        e = list(map(int, b.split(",")))
        bricks.append((s, e))

    return bricks


def overlaps(b1, b2):
    b1s, b1e = b1
    b2s, b2e = b2
    overlaps_x = b1s[0] <= b2e[0] and b2s[0] <= b1e[0]
    overlaps_y = b1s[1] <= b2e[1] and b2s[1] <= b1e[1]
    return overlaps_x and overlaps_y


def bheight(b):
    return b[1][2] - b[0][2]


def cascade(brick, support_lists, supports_lists):
    todo = supports_lists[brick]
    fell = set([brick])
    while todo:
        brick = todo.pop()
        if brick in fell or any(j not in fell for j in support_lists[brick]):
            continue
        fell.add(brick)
        todo.extend([b for b in supports_lists[brick] if b not in fell])
    return len(fell) - 1


def parts(bricks):
    bricks.sort(key=lambda x: x[0][2])

    brick_heights = {}
    # Yes, I like distinct and descriptive names :)
    support_bricks = set()
    supports_lists = defaultdict(list)
    support_lists = defaultdict(list)

    for i, brick in enumerate(bricks):
        supports = {
            j: height + bheight(bricks[j])
            for j, height in brick_heights.items()
            if overlaps(brick, bricks[j])
        }
        if not supports:
            brick_heights[i] = 1
            continue
        support_height = max(supports.values())
        supports = [i for i, h in supports.items() if h == support_height]

        if len(supports) == 1:
            support_bricks.add(supports[0])

        brick_heights[i] = support_height + 1
        support_lists[i] = supports
        for j in supports:
            supports_lists[j].append(i)

    p1res = len(bricks) - len(support_bricks)
    p2res = sum(cascade(i, support_lists, supports_lists) for i in range(len(bricks)))
    return p1res, p2res


TEST_DATA = {}
TEST_DATA[
    """\
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".rstrip()
] = (5, 7)
