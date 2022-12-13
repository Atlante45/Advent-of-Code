from collections import defaultdict
import os


def add_file(directories, path, size):
    cwd = ""
    for dir in path:
        cwd = os.path.join(cwd, dir)
        directories[cwd] += size


def parse(data):
    directories = defaultdict(int)

    path = ["/"]
    for line in data.splitlines():
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


def part1(directories):
    return sum(size for size in directories.values() if size < 100000)


def part2(directories):
    available = 70000000 - directories["/"]
    needed = 30000000 - available
    return min(size for size in directories.values() if size >= needed)


TEST_DATA = {}
TEST_DATA[
    """\
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
] = (95437, 24933642)
