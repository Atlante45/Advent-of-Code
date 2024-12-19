from collections import defaultdict


def parse(data):
    return int(data.strip())


def power(x, y, n):
    p = ((x + 10) * y + n) * (x + 10)
    return (p // 100) % 10 - 5


def parts(serial_number):
    grid = defaultdict(int)
    for y in range(1, 301):
        for x in range(1, 301):
            p = power(x, y, serial_number)
            grid[x, y] = p + grid[x - 1, y] + grid[x, y - 1] - grid[x - 1, y - 1]

    max_power_1 = 0
    max_x_1 = 0
    max_y_1 = 0

    max_power_2 = 0
    max_x_2 = 0
    max_y_2 = 0
    max_size_2 = 0
    for y in range(1, 301):
        for x in range(1, 301):
            for size in range(1, min(x, y)):
                p = (
                    grid[x, y]
                    - grid[x - size, y]
                    - grid[x, y - size]
                    + grid[x - size, y - size]
                )
                if size == 3 and p > max_power_1:
                    max_power_1 = p
                    max_x_1 = x - size + 1
                    max_y_1 = y - size + 1
                if p > max_power_2:
                    max_power_2 = p
                    max_x_2 = x - size + 1
                    max_y_2 = y - size + 1
                    max_size_2 = size
    return f"{max_x_1},{max_y_1}", f"{max_x_2},{max_y_2},{max_size_2}"


TEST_DATA = {}
TEST_DATA[
    """\
18
""".rstrip()
] = ("33,45", None)
TEST_DATA[
    """\
42
""".rstrip()
] = ("21,61", None)
