def parse(data):
    return data.splitlines()


def seat_id(line):
    return int(
        line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), 2
    )


def part1(lines):
    return max(seat_id(line) for line in lines)


def part2(lines):
    seat_ids = set(seat_id(line) for line in lines)
    min_id = min(seat_ids)
    max_id = max(seat_ids)
    return next(i for i in range(min_id, max_id) if i not in seat_ids)


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
