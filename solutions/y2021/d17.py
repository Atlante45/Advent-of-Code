import math
import re

# For any positive Y velocity, the highest point reached it V0*(V0+1)/2
# Additionally, any poisitive Y velocity will eventually come back
# to exactly Y = 0 at step 2*V0 + 1 and with a velocity of -(V0 + 1)

# pos = vel + (vel + acc) + (vel + 2 * acc) + (vel + 3 * acc) + ...
# pos = (1 + 1 + 1 + 1 + ...) * vel + (0 + 1 + 2 + 3 + ...) * acc
# pos = step * vel + (step - 1)*step/2 * acc
# pos = acc/2 * step**2 + (vel - acc/2) * step


def roots(a, b, c):
    d = math.sqrt(b * b - 4 * a * c)
    if d >= 0:
        return [(-b - d) / (2 * a), (-b + d) / (2 * a)]

    return []


def intersect(range1, range2):
    if not range1 or not range2:
        return False
    return max(range1[0], range2[0]) <= min(range1[1], range2[1])


def min_yvel(y_range):
    return y_range[0]


def max_yvel(y_range):
    return -y_range[0] - 1


def min_xvel(x_range):
    return math.ceil(max(roots(1 / 2, 1 / 2, -x_range[0])))


def max_xvel(x_range):
    return x_range[1]


def yhit_range(vel, target):
    steps = 0
    if vel >= 0:
        steps += 2 * vel + 1
        vel = -vel - 1

    acc = -1
    root_a = max(roots(acc / 2, vel - acc / 2, -target[1]))
    root_b = max(roots(acc / 2, vel - acc / 2, -target[0]))

    if math.ceil(root_a) <= math.floor(root_b):
        return (steps + math.ceil(root_a), steps + math.floor(root_b))

    return []


def xhit_range(vel, target):
    max_range = vel * (vel + 1) // 2
    if max_range < target[0]:
        return []

    acc = -1
    root_a = min(roots(acc / 2, vel - acc / 2, -target[0]))

    if max_range <= target[1]:
        return [math.ceil(root_a), 1000000000]

    root_b = min(roots(acc / 2, vel - acc / 2, -target[1]))

    if math.ceil(root_a) <= math.floor(root_b):
        return (math.ceil(root_a), math.floor(root_b))

    return []


def parse(data):
    minx, maxx, miny, maxy = re.search(
        r"^target area: x=(.+)\.\.(.+), y=(.+)\.\.(.+)", data.strip()
    ).groups()
    x_range = (int(minx), int(maxx))
    y_range = (int(miny), int(maxy))

    return x_range, y_range


def part1(_, y_range):
    v = max_yvel(y_range)
    return v * (v + 1) // 2


def part2(x_range, y_range):
    count = 0

    xhitranges = {}
    for xvel in range(min_xvel(x_range), max_xvel(x_range) + 1):
        xhitranges[xvel] = xhit_range(xvel, x_range)

    for yvel in range(min_yvel(y_range), max_yvel(y_range) + 1):
        hit_range = yhit_range(yvel, y_range)
        count += sum([intersect(r, hit_range) for r in xhitranges.values()])

    return count


TEST_DATA = {}
TEST_DATA[
    """\
target area: x=20..30, y=-10..-5
""".rstrip()
] = (45, 112)
