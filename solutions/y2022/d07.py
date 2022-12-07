#!/usr/bin/env python3
from collections import defaultdict
import os

from solutions.utils import logger
from aocd import data


def add_file(directories, path, size):
    cwd = ""
    for dir in path:
        cwd = os.path.join(cwd, dir)
        directories[cwd] += size


def parse_directories(data):
    directories = defaultdict(int)

    path = ["/"]
    for line in data:
        if line == "$ ls" or line.startswith("dir"):
            continue

        if line == "$ cd /":
            path = ["/"]
        elif line == "$ cd ..":
            path.pop()
        elif line.startswith("$ cd"):
            path.append(line.split()[-1])
        else:
            add_file(directories, path, int(line.split()[0]))

    return directories


def part1(data):
    directories = parse_directories(data)
    return sum(size for size in directories.values() if size < 100000)


def part2(data):
    directories = parse_directories(data)
    available = 70000000 - directories["/"]
    needed = 30000000 - available
    return min(size for size in directories.values() if size >= needed)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (1844187, 4978279)
TEST_RESULT = (95437, 24933642)
TEST_DATA = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
