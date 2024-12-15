with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # lines = [
    #     '########',
    #     '#..O.O.#',
    #     '##@.O..#',
    #     '#...O..#',
    #     '#.#.O..#',
    #     '#...O..#',
    #     '#......#',
    #     '########',
    #     '',
    #     '<^^>>>vv<v>>v<<'
    # ]
    grid = []
    movements = ''
    reading_map = True
    for line in lines:
        if reading_map:
            if len(line.strip()) == 0:
                reading_map = False
            else:
                grid.append(list(line.strip()))
        else:
            movements += line.strip()

width = len(grid[0])
height = len(grid)
robot = [0, 0]
for y in range(height):
    for x in range(width):
        if grid[y][x] == '@':
            robot = [x, y]


def print_grid(grid):
    for row in grid:
        print(row)
    print()


def move(grid, robot, direction):
    # print('Moving', robot, 'in', direction)
    action_length = 0
    action_pos = [robot[0], robot[1]]
    while True:
        action_pos[0] += direction[0]
        action_pos[1] += direction[1]
        if action_pos[0] == 0 or action_pos[0] == width - 1 or \
                action_pos[1] == 0 or action_pos[1] == height - 1 or \
                grid[action_pos[1]][action_pos[0]] == '#' or grid[action_pos[1]][action_pos[0]] == '.':
            break
        action_length += 1
    for i in range(action_length, -1, -1):
        action_pos = [robot[0] + direction[0] * i, robot[1] + direction[1] * i]
        target_pos = [action_pos[0] + direction[0], action_pos[1] + direction[1]]
        o = grid[action_pos[1]][action_pos[0]]
        if o == 'O' or o == '@':
            if grid[target_pos[1]][target_pos[0]] == '.':
                grid[target_pos[1]][target_pos[0]] = o
                grid[action_pos[1]][action_pos[0]] = '.'
                if o == '@':
                    robot[0] = target_pos[0]
                    robot[1] = target_pos[1]
    # print_grid(grid)


# print_grid(grid)
for i in range(len(movements)):
    movement = movements[i]
    if movement == '<':
        move(grid, robot, [-1, 0])
    elif movement == '>':
        move(grid, robot, [1, 0])
    elif movement == '^':
        move(grid, robot, [0, -1])
    elif movement == 'v':
        move(grid, robot, [0, 1])

result = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] == 'O':
            result += y * 100 + x
print(result)