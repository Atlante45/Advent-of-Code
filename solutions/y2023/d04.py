def parse(data):
    return [line.split(":")[1].split("|") for line in data.splitlines()]


def part1(lines):
    sum = 0
    for line in lines:
        win = list(map(int, line[0].split()))
        nums = list(map(int, line[1].split()))
        points = 0
        for num in nums:
            if num in win:
                if points > 0:
                    points *= 2
                else:
                    points += 1
        sum += points

    return sum


def part2(lines):
    cards = len(lines) * [1]

    for i, line in enumerate(lines):
        win = list(map(int, line[0].split()))
        nums = list(map(int, line[1].split()))
        points = 0
        for num in nums:
            if num in win:
                points += 1
        for j in range(points):
            cards[i + 1 + j] += cards[i]

    return sum(cards)


TEST_DATA = {}
TEST_DATA[
    """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".rstrip()
] = (13, 30)
