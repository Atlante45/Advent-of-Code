from collections import defaultdict
import re

REGEX = r"p=<(.+)>, v=<(.+)>, a=<(.+)>"


def parse(data):
    particles = []
    for line in data.splitlines():
        particles.append(
            [list(map(int, p.split(","))) for p in re.match(REGEX, line).groups()]
        )
    return particles


def part1(particles):
    min_a = float("inf")
    min_i = None
    for i, (_, _, a) in enumerate(particles):
        a = sum(map(abs, a))
        if a < min_a:
            min_a = a
            min_i = i
    return min_i


def part2(particles):
    for _ in range(100):
        for i, (p, v, a) in enumerate(particles):
            v = [vi + ai for vi, ai in zip(v, a)]
            p = [pi + vi for pi, vi in zip(p, v)]
            particles[i] = (p, v, a)

        collisions = defaultdict(list)
        for i, (p, _, _) in enumerate(particles):
            collisions[tuple(p)].append(i)

        particles = [
            particles[i]
            for i in range(len(particles))
            if len(collisions[tuple(particles[i][0])]) == 1
        ]
        if len(particles) == 1:
            return len(particles)
    return len(particles)


TEST_DATA = {}
TEST_DATA[
    """\
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
""".rstrip()
] = (0, None)
TEST_DATA[
    """\
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
""".rstrip()
] = (None, 1)
