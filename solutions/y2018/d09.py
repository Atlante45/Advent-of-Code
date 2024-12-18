from collections import deque


def parse(data):
    tokens = data.split()
    return int(tokens[0]), int(tokens[-2])


def winner_score(players, last_marble):
    circle = deque([0])
    scores = [0] * players

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(marble)
    return max(scores)


def part1(players, last_marble):
    return winner_score(players, last_marble)


def part2(players, last_marble):
    return winner_score(players, last_marble * 100)


TEST_DATA = {}
TEST_DATA[
    """\
9 players; last marble is worth 25 points
""".rstrip()
] = (32, None)
TEST_DATA[
    """\
10 players; last marble is worth 1618 points
""".rstrip()
] = (8317, None)
TEST_DATA[
    """\
13 players; last marble is worth 7999 points
""".rstrip()
] = (146373, None)
TEST_DATA[
    """\
17 players; last marble is worth 1104 points
""".rstrip()
] = (2764, None)
TEST_DATA[
    """\
21 players; last marble is worth 6111 points
""".rstrip()
] = (54718, None)
TEST_DATA[
    """\
30 players; last marble is worth 5807 points
""".rstrip()
] = (37305, None)
