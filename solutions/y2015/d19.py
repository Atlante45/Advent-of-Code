import re


def parse(data):
    replacements, molecule = data.split("\n\n")
    return [r.split() for r in replacements.splitlines()], molecule


def generate(molecule, replacements):
    molecules = set()
    for a, _, c in replacements:
        i = molecule.find(a)
        while i != -1:
            new_molecule = molecule[:i] + c + molecule[i + len(a) :]
            molecules.add(new_molecule)
            i = molecule.find(a, i + len(a))
    return molecules


def part1(replacements, molecule):
    molecules = generate(molecule, replacements)
    return len(molecules)


def part2(replacements, molecule):
    atoms = re.findall(r"[A-Z][a-z]?", molecule)
    # print(atoms)
    return (
        len(atoms)
        - atoms.count("Rn")
        - atoms.count("Ar")
        - 2 * atoms.count("Y")
        - (1 if len(atoms) > 10 else 0)
    )


TEST_DATA = {}
TEST_DATA[
    """\
e => H
e => O
H => HO
H => OH
O => HH

HOH
""".rstrip()
] = (4, 3)
TEST_DATA[
    """\
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
""".rstrip()
] = (7, 6)
