from collections import defaultdict

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse(data):
    lines = data.splitlines()

    size = len(lines), len(lines[0])
    start = None
    obstacles = set()



    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                obstacles.add((i, j))
            elif c == '^':
                start = (i, j)
    return start, obstacles, size


def does_loop(obstacles, start, size, obstacle):
    dir = 0
    pos = start

    visited = defaultdict(set)
    visited[pos].add(dir)

    while True:
        next_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])

        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= size[0] or next_pos[1] >= size[1]:
            break

        if next_pos != obstacle and next_pos not in obstacles:
            pos = next_pos   
        else:
            dir = (dir + 1) % 4
        
        if dir in visited[pos]:
            return True
        visited[pos].add(dir)

    return False

def parts(start, obstacles, size):
    dir = 0
    pos = start

    visited = set([pos])


    while True:
        next_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])

        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= size[0] or next_pos[1] >= size[1]:
            break

        if next_pos not in obstacles:
            pos = next_pos
            visited.add(pos)    
        else:
            dir = (dir + 1) % 4

    ans1 = len(visited)
        
    visited.remove(start)
    ans2 = sum(does_loop(obstacles, start, size, pos) for pos in visited)

    return ans1, ans2


TEST_DATA = {}
TEST_DATA[
    """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".rstrip()
] = (41, 6)
