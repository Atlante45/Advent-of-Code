import re


def parse(data):
    clay = set()
    for line in data.splitlines():
        a, b, c = map(int, re.findall(r"\d+", line))
        if line[0] == "x":
            for y in range(b, c + 1):
                clay.add((a, y))
        else:
            for x in range(b, c + 1):
                clay.add((x, a))
    return clay


def dfs(pos, clay, settled, flowing, depth):
    path = []
    while (
        pos not in settled
        and pos not in flowing
        and pos not in clay
        and pos[1] <= depth
    ):
        path.append(pos)
        pos = (pos[0], pos[1] + 1)

    if pos[1] > depth or pos in flowing:
        flowing |= set(path)
        return True

    if not path:
        return False

    is_flowing = False

    while path:
        pos = path.pop()

        visited = set([pos])

        # debug_print(clay, settled | flowing | visited | set(path), pos[1] - 30)

        lx, ly = pos
        lx -= 1
        while (lx, ly) not in clay and (lx, ly) not in settled:
            visited.add((lx, ly))
            if dfs((lx, ly + 1), clay, settled, flowing, depth):
                is_flowing = True
                break
            lx -= 1

        # debug_print(clay, settled | flowing | visited | set(path), pos[1] - 30)
        rx, ry = pos
        rx += 1
        while (rx, ry) not in clay and (rx, ry) not in settled:
            visited.add((rx, ry))
            if dfs((rx, ry + 1), clay, settled, flowing, depth):
                is_flowing = True
                break
            rx += 1

        # debug_print(clay, settled | flowing | visited | set(path), pos[1] - 30)

        if is_flowing:
            flowing |= visited
            break
        else:
            settled |= visited

    if is_flowing:
        flowing |= set(path)
    else:
        assert not path

    return is_flowing


def debug_print(clay, visited, min_y=None):
    return
    min_x = min(x for x, _ in clay)
    max_x = max(x for x, _ in clay)
    min_y = min_y or min(y for _, y in clay)
    max_y = max(y for _, y in clay)

    for y in range(min_y, min(min_y + 80, max_y + 1)):
        for x in range(min_x - 1, max_x + 2):
            if (x, y) in clay:
                print("\033[91m#\033[0m", end="")
            elif (x, y) in visited:
                print("\033[92m~\033[0m", end="")
            else:
                print(" ", end="")
        print()
    input()


def parts(clay):
    min_y = min(y for _, y in clay)
    max_y = max(y for _, y in clay)

    source = (500, max(min_y, 0))

    settled = set()
    flowing = set()

    res = dfs(source, clay, settled, flowing, max_y)
    assert res

    return len(settled) + len(flowing), len(settled)


TEST_DATA = {}
TEST_DATA[
    """\
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
""".rstrip()
] = (57, 29)
# TEST_DATA[
#     """\
# x=495, y=2..7
# x=498, y=10..13
# x=504, y=10..13
# y=13, x=498..504
# x=495, y=18..21
# x=510, y=18..21
# y=21, x=495..510
# """.rstrip()
# ] = (57, None)
