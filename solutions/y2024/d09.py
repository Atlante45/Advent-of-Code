def parse(data):
    return list(map(int, data.strip()))


def part1(lines):
    assert(len(lines) % 2 == 1)
    n = len(lines) // 2
    
    res = 0
    idx = 0

    head_id = 0
    last_id = len(lines) // 2
    last_count = lines[-1]
    lines.pop()
    lines.pop()

    while len(lines) > 0:
        res += sum(range(idx, idx + lines[0])) * head_id
        idx += lines[0]
        head_id += 1
        lines.pop(0)
        if len(lines) == 0:
            break

        empty_count = lines[0]
        lines.pop(0)

        for i in range(empty_count):
            if last_count == 0:
                if len(lines) == 0:
                    break
                last_id -= 1
                last_count = lines[-1]
                lines.pop()
                lines.pop()
            res += (idx + i) * last_id
            last_count -= 1
        idx += empty_count
    
    for i in range(last_count):
        res += (idx + i) * last_id
    idx += last_count


    return res

def part2(lines):
    moved = set()
    last_id = len(lines) // 2

    res = 0
    idx = 0
    for i, v in enumerate(lines):
        file_id = i // 2
        if i % 2 == 0 and file_id not in moved:
            res += sum(index * file_id for index in range(idx, idx + v))
        else:
            last_v = v
            while v > 0:
                for j in range(last_id, file_id, -1):
                    if j not in moved and lines[2 * j] <= v:
                        res += sum(index * j for index in range(idx, idx + lines[2 * j]))
                        moved.add(j)
                        v -= lines[2 * j]
                        idx += lines[2 * j]
                        break
                if v == last_v:
                    break
                last_v = v
        idx += v
    return res






TEST_DATA = {}
TEST_DATA[
    """\
2333133121414131402
""".rstrip()
] = (1928, 2858)
