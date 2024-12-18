from itertools import count
from math import floor
import re

from solutions.utils import ocr


def parse(data):
    points = []
    for line in data.splitlines():
        x, y, vx, vy = re.findall(r"-?\d+", line)
        points.append((int(x), int(y), int(vx), int(vy)))
    return points


def render_points(points, min_x, max_x, min_y, max_y):
    assert max_x - min_x < 100
    assert max_y - min_y < 20

    render = ""
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            render += "#" if (x, y) in points else "."
        render += "\n"
    return render


def parts(points):
    ax, _, avx, _ = points[0]
    bx, _, bvx, _ = next(point for point in points if point[2] != avx)

    n = (ax - bx) / (bvx - avx)

    for i in count(floor(n - 100)):
        positions = set((x + vx * i, y + vy * i) for x, y, vx, vy in points)

        min_x = min(x for x, _ in positions)
        max_x = max(x for x, _ in positions)
        min_y = min(y for _, y in positions)
        max_y = max(y for _, y in positions)

        if max_y - min_y == 9:
            render = render_points(positions, min_x, max_x, min_y, max_y)
            return ocr.parse(render), i


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
