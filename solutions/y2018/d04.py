from collections import defaultdict
import re

R1 = re.compile(r"\[(.*) \d{2}:(\d{2})\] (.*)")


def parse(data):
    guard = None
    sleep_start = None

    events = []
    for line in sorted(data.splitlines()):
        _, minute, action = R1.match(line).groups()
        if action.startswith("Guard"):
            guard = int(action.split()[1][1:])
        elif action.startswith("falls"):
            sleep_start = int(minute)
        elif action.startswith("wakes"):
            events.append((guard, sleep_start, int(minute)))
    return events


def part1(events):
    max_minute = 0
    max_guard = 0

    sleep_times = defaultdict(lambda: defaultdict(int))
    for guard, sleep_start, sleep_end in events:
        for minute in range(sleep_start, sleep_end):
            sleep_times[guard][minute] += 1

    max_guard = max(sleep_times.keys(), key=lambda x: sum(sleep_times[x].values()))
    max_minute = max(
        sleep_times[max_guard].keys(), key=lambda x: sleep_times[max_guard][x]
    )

    return max_guard * max_minute


def part2(events):
    max_minute = 0
    max_guard = 0

    sleep_times = defaultdict(lambda: defaultdict(int))
    for guard, sleep_start, sleep_end in events:
        for minute in range(sleep_start, sleep_end):
            sleep_times[guard][minute] += 1
        mins = max(sleep_times[guard].values())
        if mins > max_minute:
            max_minute = mins
            max_guard = guard

    return (
        max_guard * [k for k, v in sleep_times[max_guard].items() if v == max_minute][0]
    )


TEST_DATA = {}
TEST_DATA[
    """\
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
""".rstrip()
] = (240, 4455)
