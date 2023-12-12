from functools import cache


@cache
def count_ways(springs, runs, i, j, count):
    if j == len(runs):
        return 1 if "#" not in springs[i:] else 0
    if i == len(springs):
        return 1 if runs[j:] == (count,) else 0

    match springs[i]:
        case "#":
            if count < runs[j]:
                return count_ways(springs, runs, i + 1, j, count + 1)
            else:
                return 0
        case ".":
            if count == 0:
                return count_ways(springs, runs, i + 1, j, 0)
            elif count == runs[j]:
                return count_ways(springs, runs, i + 1, j + 1, 0)
            else:
                return 0
        case "?":
            if count == 0:
                r1 = count_ways(springs, runs, i + 1, j, 1)
                r2 = count_ways(springs, runs, i + 1, j, 0)
                return r1 + r2
            elif count == runs[j]:
                return count_ways(springs, runs, i + 1, j + 1, 0)
            else:
                return count_ways(springs, runs, i + 1, j, count + 1)


def solve(line, factor):
    springs, runs = line.split()
    springs = "?".join(factor * [springs])
    runs = ",".join(factor * [runs])

    runs = list(map(int, runs.split(",")))

    return count_ways(springs, tuple(runs), 0, 0, 0)


def parse(data):
    return data.splitlines()


def part1(lines):
    return sum(solve(line, 1) for line in lines)


def part2(lines):
    return sum(solve(line, 5) for line in lines)


TEST_DATA = {}
TEST_DATA[
    """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".rstrip()
] = (21, 525152)
