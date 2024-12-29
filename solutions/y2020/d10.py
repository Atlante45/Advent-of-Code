def parse(data):
    numbers = [int(line) for line in data.splitlines()]
    numbers.sort()
    numbers.insert(0, 0)
    numbers.append(numbers[-1] + 3)
    return numbers


def part1(numbers):
    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    return diffs.count(1) * diffs.count(3)


def part2(numbers):
    counts = [0] * len(numbers)
    counts[0] = 1
    for i in range(len(numbers)):
        for j in range(max(0, i - 3), i):
            if numbers[i] - numbers[j] <= 3:
                counts[i] += counts[j]
    return counts[-1]


TEST_DATA = {}
TEST_DATA[
    """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".rstrip()
] = (220, 19208)
