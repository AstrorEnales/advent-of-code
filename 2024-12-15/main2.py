with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    '''lines = [
        '########',
        '#..O.O.#',
        '##@.O..#',
        '#...O..#',
        '#.#.O..#',
        '#...O..#',
        '#......#',
        '########',
        '',
        '<^^>>>vv<v>>v<<'
    ]'''
    grid = []
    movements = ''
    reading_map = True
    for line in lines:
        if reading_map:
            if len(line.strip()) == 0:
                reading_map = False
            else:
                row = []
                for element in line.strip():
                    if element == '#':
                        row.append('#')
                        row.append('#')
                    elif element == 'O':
                        row.append('[')
                        row.append(']')
                    elif element == '.':
                        row.append('.')
                        row.append('.')
                    elif element == '@':
                        row.append('@')
                        row.append('.')
                grid.append(row)
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


def get_object(grid, coord):
    return grid[coord[1]][coord[0]]


def move(grid, robot, direction):
    # print('Moving', robot, 'in', direction)
    pending_objects = {(robot[0], robot[1])}
    visited = set()
    objects_by_distance = {}
    while len(pending_objects) > 0:
        pos = pending_objects.pop()
        visited.add(pos)
        target = (pos[0] + direction[0], pos[1] + direction[1])
        target_obj = get_object(grid, target)
        if target_obj == '#':
            return
        if target_obj == '[':
            if target not in visited:
                pending_objects.add(target)
            if (target[0] + 1, target[1]) not in visited:
                pending_objects.add((target[0] + 1, target[1]))
        elif target_obj == ']':
            if (target[0] - 1, target[1]) not in visited:
                pending_objects.add((target[0] - 1, target[1]))
            if target not in visited:
                pending_objects.add(target)
        action_length = max([(pos[0] - robot[0]) * direction[0], (pos[1] - robot[1]) * direction[1]])
        if action_length not in objects_by_distance:
            objects_by_distance[action_length] = []
        objects_by_distance[action_length].append(pos)
    for i in range(max(objects_by_distance.keys()), -1, -1):
        for action_pos in objects_by_distance[i]:
            target_pos = [action_pos[0] + direction[0], action_pos[1] + direction[1]]
            o = get_object(grid, action_pos)
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
        if grid[y][x] == '[':
            result += y * 100 + x
print(result)
