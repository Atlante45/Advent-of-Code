from collections import defaultdict
from functools import reduce


def parse(data):
    return data.split(",")


def hash(seq):
    return reduce(lambda a, b: 17 * (a + ord(b)) % 256, seq, 0)


def part1(sequence):
    return sum(hash(s) for s in sequence)


def part2(sequence):
    boxes = defaultdict(list)

    for s in sequence:
        if "=" in s:
            k, v = s.split("=")
            h = hash(k)
            box = boxes[h]
            done = False
            for i in range(len(box)):
                if box[i][0] == k:
                    done = True
                    box[i] = (k, int(v))
                    break
            if not done:
                box.append((k, int(v)))
        else:
            h = hash(s[:-1])
            boxes[h] = [b for b in boxes[h] if b[0] != s[:-1]]

    return sum(
        (i + 1) * (j + 1) * b[1] for i in range(256) for j, b in enumerate(boxes[i])
    )


TEST_DATA = {}
TEST_DATA[
    """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".rstrip()
] = (1320, 145)
