def parse(data):
    players = data.split("\n\n")
    return [list(map(int, player.splitlines()[1:])) for player in players]


def play(player1, player2):
    hands = set()
    while player1 and player2:
        card1, card2 = player1.pop(0), player2.pop(0)
        hand = (tuple(player1), tuple(player2))
        if hand in hands:
            return 1, player1, player2
        hands.add(hand)

        if len(player1) >= card1 and len(player2) >= card2:
            winner, _, _ = play(player1[:card1], player2[:card2])
            if winner == 1:
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])
        elif card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
    return 1 if player1 else 2, player1, player2


def part1(players):
    player1, player2 = players
    while player1 and player2:
        card1, card2 = player1.pop(0), player2.pop(0)
        if card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
    return sum((i + 1) * v for i, v in enumerate(reversed(player1 or player2)))


def part2(players):
    winner, player1, player2 = play(*players)
    return sum(
        (i + 1) * v for i, v in enumerate(reversed(player1 if winner == 1 else player2))
    )


TEST_DATA = {}
TEST_DATA[
    """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".rstrip()
] = (306, None)
