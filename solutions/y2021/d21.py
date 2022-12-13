from functools import cache
from itertools import count


def roll(die):
    return 1 + (next(die) - 1) % 100


def step(positions, scores, player, die):
    move = roll(die) + roll(die) + roll(die)
    positions[player] = (positions[player] + move) % 10
    scores[player] += positions[player] + 1


def parse(data):
    return [int(line.split()[-1]) for line in data.splitlines()]


def part1(input):
    die = count(1)

    positions = [p - 1 for p in input]
    scores = [0, 0]
    for turn in count(0):
        player = turn % 2
        step(positions, scores, player, die)
        if scores[player] >= 1000:
            return (next(die) - 1) * scores[player - 1]


ROLLS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@cache
def quantum_turn(pos1, score1, pos2, score2):
    wins, losses = 0, 0
    for roll, freq in ROLLS.items():
        new_pos1 = (pos1 + roll) % 10
        new_score1 = score1 + new_pos1 + 1
        if new_score1 >= 21:
            wins += freq
        else:
            new_losses, new_wins = quantum_turn(pos2, score2, new_pos1, new_score1)
            wins += freq * new_wins
            losses += freq * new_losses
    return wins, losses


def part2(input):
    return max(quantum_turn(input[0] - 1, 0, input[1] - 1, 0))


TEST_DATA = {}
TEST_DATA[
    """\
Player 1 starting position: 4
Player 2 starting position: 8
""".rstrip()
] = (739785, 444356092776315)
