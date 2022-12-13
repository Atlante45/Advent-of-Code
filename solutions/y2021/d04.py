class BingoCard:
    def __init__(self, lines):
        self.grid = []
        self.count = 0
        self.cols = [0] * 5
        self.rows = [0] * 5
        self.won = False

        for line in lines:
            line = line.strip()
            for val in line.split():
                self.grid.append(int(val))
                self.count += int(val)

    def check(self, number):
        if self.won:
            return False

        if number in self.grid:
            self.count -= number

            index = self.grid.index(number)
            row = index // 5
            col = index % 5

            self.rows[row] += 1
            self.cols[col] += 1

            self.won = self.rows[row] == 5 or self.cols[col] == 5

            return self.won

        return False


def parse(data):
    lines = data.splitlines()
    numbers = lines[0].strip().split(",")
    numbers = list(map(lambda v: int(v), numbers))
    lines = lines[2:]

    cards = []

    while lines:
        cards.append(BingoCard(lines[0:5]))
        lines = lines[6:]

    return numbers, cards


def part1(numbers, cards):
    res = 0

    for n in numbers:
        for c in cards:
            if c.check(n):
                res = c.count * n
                break

        if res:
            break

    return res


def part2(numbers, cards):
    res = 0

    cardsLeft = len(cards)

    for n in numbers:
        for c in cards:
            if c.check(n):
                cardsLeft -= 1

                if cardsLeft == 0:
                    res = c.count * n
                    break

        if res:
            break

    return res


TEST_DATA = {}
TEST_DATA[
    """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".rstrip()
] = (4512, 1924)
