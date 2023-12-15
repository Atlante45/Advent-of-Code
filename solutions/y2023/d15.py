from collections import defaultdict
from functools import reduce


def hash(seq):
    return reduce(lambda a, b: 17 * (a + ord(b)) % 256, seq, 0)


def execute(step, boxes, lenses):
    if "=" in step:
        label, focal_length = step.split("=")
        box = boxes[hash(label)]
        lenses[label] = int(focal_length)
        if label not in box:
            box.append(label)
    else:
        label = step[:-1]
        box = boxes[hash(label)]
        if label in box:
            box.remove(label)


def power(boxes, lenses):
    return sum(
        (i + 1) * (j + 1) * lenses[label]
        for i in range(256)
        for j, label in enumerate(boxes[i])
    )


def parse(data):
    return data.split(",")


def part1(sequence):
    return sum(hash(step) for step in sequence)


def part2(sequence):
    boxes = defaultdict(list)
    lenses = {}

    for step in sequence:
        execute(step, boxes, lenses)
    return power(boxes, lenses)


TEST_DATA = {}
TEST_DATA[
    """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".rstrip()
] = (1320, 145)
