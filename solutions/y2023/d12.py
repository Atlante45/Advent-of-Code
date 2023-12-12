from functools import cache


def parse(data):
    return data.splitlines()

@cache
def mems(springs, nums, count):
    if len(springs) == 0:
        if count > 0 and len(nums) == 1 and count == nums[0]:
            return 1
        else:
            return 1 if len(nums) == 0 and count == 0 else 0

    s = springs[0]
    if s == "#":
        if len(nums) == 0 or nums[0] <= count:
            return 0
        else:
            return mems(springs[1:], nums, count + 1)
    elif s == "?":
        if count == 0:
            return mems(springs[1:], nums, count + 1) + mems(springs[1:], nums, 0)
        elif len(nums) > 0 and count == nums[0]:
            return mems(springs[1:], nums[1:], 0)
        elif len(nums) == 0 or nums[0] <= count:
            return 0
        else:
            return mems(springs[1:], nums, count + 1)
    elif count == 0:
        return mems(springs[1:], nums, count)
    elif len(nums) > 0 and count == nums[0]:
        return mems(springs[1:], nums[1:], 0)
    else:
        return 0

def solve(line):
    springs, nums = line.split()
    nums = list(map(int, nums.split(",")))
    
    return mems(springs, tuple(nums), 0)

def solve2(line):
    springs, nums = line.split()
    springs = (5 * (springs + "?"))[:-1]
    nums = (5 * (nums + ","))[:-1]
    
    nums = list(map(int, nums.split(",")))

    return mems(springs, tuple(nums), 0)

def part1(lines):
    return sum(solve(line) for line in lines)


def part2(lines):
    return sum(solve2(line) for line in lines)


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
