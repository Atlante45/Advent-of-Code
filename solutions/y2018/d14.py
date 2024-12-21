def parse(data):
    return int(data.strip())


def part1(target):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(recipes) < target + 10:
        new_recipe = recipes[elf1] + recipes[elf2]
        recipes.extend(int(d) for d in str(new_recipe))
        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    return "".join(str(r) for r in recipes[target : target + 10])


def part2(target):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    target = list(map(int, str(target)))

    while True:
        new_recipe = recipes[elf1] + recipes[elf2]
        recipes.extend(int(d) for d in str(new_recipe))
        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

        if len(recipes) <= len(target):
            continue

        start = len(recipes) - len(target) - 1
        if all(target[i] == recipes[start + i] for i in range(len(target))):
            return start
        if all(target[i] == recipes[start + i + 1] for i in range(len(target))):
            return start + 1


TEST_DATA = {}
TEST_DATA[
    """\
9
""".rstrip()
] = ("5158916779", None)
TEST_DATA[
    """\
5
""".rstrip()
] = ("0124515891", None)
TEST_DATA[
    """\
18
""".rstrip()
] = ("9251071085", None)
TEST_DATA[
    """\
2018
""".rstrip()
] = ("5941429882", None)
