from collections import defaultdict
import re


R = re.compile(r"^(.+) \(contains (.+)\)$")


def parse(data):
    foods = []
    for line in data.splitlines():
        match = R.match(line)
        assert match
        ingredients, allergens = match.groups()
        foods.append((ingredients.split(), allergens.split(", ")))
    return foods


def parts(foods):
    all_ingredients = set()
    all_allergens = set()
    for ingredients, allergens in foods:
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)

    alergens = defaultdict(lambda: all_ingredients.copy())
    for ingredients, allergens in foods:
        assert len(ingredients) == len(set(ingredients))
        assert len(allergens) == len(set(allergens))
        for allergen in allergens:
            alergens[allergen] &= set(ingredients)

    while any(len(v) > 1 for v in alergens.values()):
        for allergen in alergens:
            if len(alergens[allergen]) == 1:
                for other in alergens:
                    if other != allergen:
                        alergens[other] -= alergens[allergen]

    allergens = {k: v.pop() for k, v in alergens.items()}

    safe = all_ingredients - set(allergens.values())

    p1 = sum(len(safe & set(ingredients)) for ingredients, _ in foods)
    p2 = ",".join(allergens[k] for k in sorted(allergens.keys()))
    return p1, p2


TEST_DATA = {}
TEST_DATA[
    """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".rstrip()
] = (5, "mxmxvkd,sqjhc,fvjkl")
