from functools import lru_cache
from math import prod
import re


REGEX = re.compile(r"(-?\d+)")


def numbers(string):
    return [int(v) for v in REGEX.findall(string)]


@lru_cache(maxsize=None)
def step(
    bp,
    t,
    max_t,
    ore,
    clay,
    obs,
    geo,
    ore_r,
    max_ore_r,
    clay_r,
    max_clay_r,
    obs_r,
    geo_r,
):
    if t == max_t:
        return geo

    time_left = max_t - t
    ore_max = time_left * max_ore_r - ore_r * (time_left - 1)
    clay_max = time_left * max_clay_r - clay_r * (time_left - 1)
    obs_max = time_left * bp[6] - obs_r * (time_left - 1)

    res = 0
    if ore >= bp[5] and obs >= bp[6]:
        res = max(
            res,
            step(
                bp,
                t + 1,
                max_t,
                min(ore_max, ore + ore_r - bp[5]),
                min(clay_max, clay + clay_r),
                min(obs_max, obs + obs_r - bp[6]),
                geo + geo_r,
                ore_r,
                max_ore_r,
                clay_r,
                max_clay_r,
                obs_r,
                geo_r + 1,
            ),
        )
    if ore >= bp[3] and clay >= bp[4] and obs < obs_max:
        res = max(
            res,
            step(
                bp,
                t + 1,
                max_t,
                min(ore_max, ore + ore_r - bp[3]),
                min(clay_max, clay + clay_r - bp[4]),
                min(obs_max, obs + obs_r),
                geo + geo_r,
                ore_r,
                max_ore_r,
                clay_r,
                max_clay_r,
                obs_r + 1,
                geo_r,
            ),
        )

    if ore >= bp[2] and clay < clay_max:
        res = max(
            res,
            step(
                bp,
                t + 1,
                max_t,
                min(ore_max, ore + ore_r - bp[2]),
                min(clay_max, clay + clay_r),
                min(obs_max, obs + obs_r),
                geo + geo_r,
                ore_r,
                max_ore_r,
                clay_r + 1,
                max_clay_r,
                obs_r,
                geo_r,
            ),
        )
    if ore >= bp[1] and ore < ore_max:
        res = max(
            res,
            step(
                bp,
                t + 1,
                max_t,
                min(ore_max, ore + ore_r - bp[1]),
                min(clay_max, clay + clay_r),
                min(obs_max, obs + obs_r),
                geo + geo_r,
                ore_r + 1,
                max_ore_r,
                clay_r,
                max_clay_r,
                obs_r,
                geo_r,
            ),
        )
    res = max(
        res,
        step(
            bp,
            t + 1,
            max_t,
            min(ore_max, ore + ore_r),
            min(clay_max, clay + clay_r),
            min(obs_max, obs + obs_r),
            geo + geo_r,
            ore_r,
            max_ore_r,
            clay_r,
            max_clay_r,
            obs_r,
            geo_r,
        ),
    )

    return res


def quality_level(bp):
    max_prod = step(
        bp, 0, 24, 0, 0, 0, 0, 1, max(bp[1], bp[2], bp[3], bp[5]), 0, bp[4], 0, 0
    )
    return bp[0] * max_prod


def max_geods(bp):
    max_prod = step(
        bp, 0, 32, 0, 0, 0, 0, 1, max(bp[1], bp[2], bp[3], bp[5]), 0, bp[4], 0, 0
    )
    return max_prod


def parse(data):
    return [tuple(numbers(line)) for line in data.splitlines()]


def part1(blueprints):
    return sum(quality_level(bp) for bp in blueprints)


def part2(blueprints):
    return prod(max_geods(bp) for bp in blueprints[0:3])


TEST_DATA = {}
TEST_DATA[
    """\
Blueprint 1:\
  Each ore robot costs 4 ore.\
  Each clay robot costs 2 ore.\
  Each obsidian robot costs 3 ore and 14 clay.\
  Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2:\
  Each ore robot costs 2 ore.\
  Each clay robot costs 3 ore.\
  Each obsidian robot costs 3 ore and 8 clay.\
  Each geode robot costs 3 ore and 12 obsidian.
""".rstrip()
] = (33, 56 * 62)
