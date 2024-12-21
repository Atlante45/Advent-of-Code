from tqdm import tqdm


def parse(data):
    initial_state, rules = data.split("\n\n")
    initial_state = set(i for i, c in enumerate(initial_state.split()[-1]) if c == "#")
    rules = {
        rule.split(" => ")[0]: rule.split(" => ")[1] for rule in rules.splitlines()
    }
    return initial_state, rules


def part1(initial_state, rules):
    for _ in range(20):
        min_i = min(initial_state)
        max_i = max(initial_state)

        new_state = set()
        for i in range(min_i - 2, max_i + 3):
            str_i = "".join(
                "#" if i in initial_state else "." for i in range(i - 2, i + 3)
            )
            if str_i in rules and rules[str_i] == "#":
                new_state.add(i)
        initial_state = new_state
    return sum(initial_state)


def part2(initial_state, rules):
    for generation in range(50000000000):
        min_i = min(initial_state)
        max_i = max(initial_state)

        new_state = set()
        for i in range(min_i - 2, max_i + 3):
            str_i = "".join(
                "#" if i in initial_state else "." for i in range(i - 2, i + 3)
            )
            if str_i in rules and rules[str_i] == "#":
                new_state.add(i)

        if len(initial_state) == len(new_state):
            sorted_diff = sorted(b - a for a, b in zip(initial_state, new_state))
            if all(diff == sorted_diff[0] for diff in sorted_diff):
                return (
                    sum(initial_state)
                    + len(initial_state) * (50000000000 - generation) * sorted_diff[0]
                )

        initial_state = new_state

    return sum(initial_state)


TEST_DATA = {}
TEST_DATA[
    """\
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".rstrip()
] = (325, None)
