from functools import cache

from tqdm import tqdm


def parse(data):
    return int(data.strip())


# ((x + 10) * y + n) * (x + 10)
# xxy + 20xy + nx + 100y + 10n


@cache
def power(x, y, n):
    p = ((x + 10) * y + n) * (x + 10)
    return (p // 100) % 10 - 5


def part1(serial_number):
    max_power = 0
    max_x = 0
    max_y = 0
    for x in range(1, 298):
        for y in range(1, 298):
            p = sum(
                power(x + dx, y + dy, serial_number)
                for dx in range(3)
                for dy in range(3)
            )
            if p > max_power:
                max_power = p
                max_x = x
                max_y = y
    return f"{max_x},{max_y}"


def part2(serial_number):
    grid = [
        [power(x + 1, y + 1, serial_number) for x in range(300)] for y in range(300)
    ]

    # for y in range(300):
    #     for x in range(80):
    #         color = "\033[0;31m" if grid[y][x] < 0 else "\033[0;32m"
    #         print(f"{color}{grid[y][x]:3}\033[0m", end="")
    #     print()

    # return None

    max_power = 0
    max_x = 0
    max_y = 0
    max_size = 0
    for x in tqdm(range(300)):
        for y in range(300):
            p = grid[y][x]
            for size in range(2, 300 - max(x, y)):
                p += sum(grid[y + size - 1][x + dx] for dx in range(size - 1))
                p += sum(grid[y + dy][x + size - 1] for dy in range(size - 1))
                p += grid[y + size - 1][x + size - 1]
                if p > max_power:
                    max_power = p
                    max_x = x + 1
                    max_y = y + 1
                    max_size = size
    return f"{max_x},{max_y},{max_size}"


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
