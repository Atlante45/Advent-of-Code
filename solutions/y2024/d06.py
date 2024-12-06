from collections import defaultdict


def parse(data):
    grid = [list(line) for line in data.splitlines()]
    start = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                start = (i, j)
                break
        if start:
            break
    grid[start[0]][start[1]] = '.'
    return grid, start

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part1(grid, start):
    dir = 0
    pos = start

    visited = set([pos])


    while True:
        next_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(grid) or next_pos[1] >= len(grid[0]):
            break
        if grid[next_pos[0]][next_pos[1]] == '.':
            pos = next_pos
            visited.add(pos)    
        else:
            dir = (dir + 1) % 4

    return len(visited)
        

def does_loop(grid, start, obstacle):
    dir = 0
    pos = start

    visited = defaultdict(set)
    visited[pos].add(dir)

    while True:
        next_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        next_dir = (dir + 1) % 4

        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(grid) or next_pos[1] >= len(grid[0]):
            break

        if grid[next_pos[0]][next_pos[1]] == '.' and next_pos != obstacle:
            pos = next_pos   
        else:
            dir = next_dir
        
        if dir in visited[pos]:
            return True
        visited[pos].add(dir)

    return False

def part2(grid, start):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.' and (i, j) != start:
                if does_loop(grid, start, (i, j)):
                    sum += 1
    return sum


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
