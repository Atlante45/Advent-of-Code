import re


REQ = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def parse(data):
    passports = []
    for p in data.split("\n\n"):
        passports.append(dict(line.split(":") for line in p.replace("\n", " ").split()))
    return passports


def validate1(p):
    return not REQ - p.keys()


def validate2(p):
    return (
        validate1(p)
        and 1920 <= int(p["byr"]) <= 2002
        and 2010 <= int(p["iyr"]) <= 2020
        and 2020 <= int(p["eyr"]) <= 2030
        and (
            p["hgt"][-2:] == "cm"
            and 150 <= int(p["hgt"][:-2]) <= 193
            or p["hgt"][-2:] == "in"
            and 59 <= int(p["hgt"][:-2]) <= 76
        )
        and re.match(r"^#[0-9a-f]{6}$", p["hcl"])
        and p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        and re.match(r"^\d{9}$", p["pid"])
    )


def part1(passports):
    return sum(1 for p in passports if validate1(p))


def part2(passports):
    return sum(1 for p in passports if validate2(p))


TEST_DATA = {}
TEST_DATA[
    """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".rstrip()
] = (2, None)
