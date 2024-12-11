from typing import Tuple

right_turns = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1)
}

with open('input.txt', 'r', encoding='utf-8') as f:
    grid = [x.strip() for x in f.readlines()]

start_pos = None
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if grid[y][x] == '^':
            start_pos = (x, y)
            break
    if start_pos is not None:
        break

print('Start pos:', start_pos)
facing = (0, -1)
pos = (start_pos[0], start_pos[1])
visited = [[' '] * len(grid[0]) for _ in range(0, len(grid))]
visited[pos[1]][pos[0]] = 'X'
while True:
    next_pos = (pos[0] + facing[0], pos[1] + facing[1])
    if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
        break
    if grid[next_pos[1]][next_pos[0]] == '#':
        facing = right_turns[facing]
    else:
        pos = next_pos
        visited[pos[1]][pos[0]] = 'X'

print(sum([sum([1 if x == 'X' else 0 for x in row]) for row in visited]))


def check_layout(grid, start_pos: Tuple[int, int]):
    pos = (start_pos[0], start_pos[1])
    facing = (0, -1)
    visited = [[set() for _ in range(0, len(grid[0]))] for _ in range(0, len(grid))]
    visited[pos[1]][pos[0]].add(facing)
    while True:
        next_pos = (pos[0] + facing[0], pos[1] + facing[1])
        if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
            return False
        if grid[next_pos[1]][next_pos[0]] == '#':
            facing = right_turns[facing]
        else:
            pos = next_pos
        if facing in visited[pos[1]][pos[0]]:
            return True
        visited[pos[1]][pos[0]].add(facing)


result = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        run = x + y * len(grid[0])
        if run % 1000 == 0:
            print(run, '/', len(grid) * len(grid[0]))
        if grid[y][x] == '#' or grid[y][x] == '^':
            continue
        grid_copy = [[grid[iy][ix] for ix in range(0, len(grid[0]))] for iy in range(0, len(grid))]
        grid_copy[y][x] = '#'
        if check_layout(grid_copy, start_pos):
            result += 1
print(result)
