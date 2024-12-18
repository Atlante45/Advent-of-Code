from collections import defaultdict
from queue import PriorityQueue

from more_itertools import flatten


def parse(data):
    next = defaultdict(list)
    prev = defaultdict(list)
    all_steps = set()
    for line in data.splitlines():
        parts = line.split()
        all_steps.add(parts[1])
        all_steps.add(parts[7])
        next[parts[1]].append(parts[7])
        prev[parts[7]].append(parts[1])
    return next, prev, all_steps


def part1(next, prev, all_steps):
    starts = all_steps - set(flatten(next.values()))
    order = []

    while len(starts) > 0:
        start = sorted(starts)[0]
        starts.remove(start)
        order.append(start)
        starts.update([n for n in next[start] if len(set(prev[n]) - set(order)) == 0])
    return "".join(order)


def part2(next, prev, all_steps):
    workers = 5 if len(all_steps) > 6 else 2
    time_added = 60 if len(all_steps) > 6 else 0

    starts = all_steps - set(flatten(next.values()))
    assert len(starts) <= workers

    done = []
    active = PriorityQueue()
    todo = []
    for start in starts:
        active.put((time_added + ord(start) - ord("A") + 1, start))

    while active.qsize() > 0:
        time, start = active.get()
        done.append(start)
        todo.extend([n for n in next[start] if len(set(prev[n]) - set(done)) == 0])

        todo = sorted(todo)
        while active.qsize() < workers and len(todo) > 0:
            next_start = todo.pop(0)
            active.put((time + time_added + ord(next_start) - ord("A") + 1, next_start))

    return time


TEST_DATA = {}
TEST_DATA[
    """\
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".rstrip()
] = ("CABDFE", 15)
