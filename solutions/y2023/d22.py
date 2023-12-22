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


def part1(bricks):
    bricks.sort(key=lambda x: x[0][2])

    brick_heights = {}
    support_bricks = set()
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
        brick_heights[i] = support_height + 1
        if len(supports) == 1:
            support_bricks.add(supports[0])

    return len(bricks) - len(support_bricks)


def part2(bricks):
    bricks.sort(key=lambda x: x[0][2])

    brick_heights = {}
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
        brick_heights[i] = support_height + 1

        support_lists[i] = supports
        for j in supports:
            supports_lists[j].append(i)

    res = 0
    for i in range(len(bricks)):
        sum = 0
        todo = [i]
        fell = set(support_lists[i])
        while todo:
            brick = todo.pop()
            if brick not in fell and all(j in fell for j in support_lists[brick]):
                sum += 1
                fell.add(brick)
                for j in supports_lists[brick]:
                    if j not in fell:
                        todo.append(j)

        if sum > 1:
            res += sum - 1
    return res


# 1179 too low

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
