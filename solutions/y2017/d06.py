from itertools import count


def parse(data):
    return [int(b) for b in data.split()]


def parts(banks):
    visited = {}

    for step in count(1):
        max_val = max(banks)
        max_ind = banks.index(max_val)
        banks[max_ind] = 0
        dist_a = max_val // len(banks)
        dist_b = max_val % len(banks)
        for i in range(len(banks)):
            banks[i] += dist_a
            if max_ind + dist_b >= len(banks):
                banks[i] += (
                    1 if max_ind < i or i <= (max_ind + dist_b) % len(banks) else 0
                )
            else:
                banks[i] += 1 if max_ind < i and i <= max_ind + dist_b else 0

        tup = tuple(banks)
        if tup in visited:
            return step, step - visited[tup]
        visited[tup] = step


TEST_DATA = {}
TEST_DATA[
    """\
0  2  7  0
""".rstrip()
] = (5, 4)
