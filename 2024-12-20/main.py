with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    # lines = [
    #     '###############',
    #     '#...#...#.....#',
    #     '#.#.#.#.#.###.#',
    #     '#S#...#.#.#...#',
    #     '#######.#.#.###',
    #     '#######.#.#...#',
    #     '#######.#.###.#',
    #     '###..E#...#...#',
    #     '###.#######.###',
    #     '#...###...#...#',
    #     '#.#####.#.###.#',
    #     '#.#...#.#.#...#',
    #     '#.#.#.#.#.#.###',
    #     '#...#...#...###',
    #     '###############'
    # ]
    lines = [list(x) for x in lines]

start_position = (0, 0)
end_position = (0, 0)
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'S':
            start_position = (x, y)
        elif lines[y][x] == 'E':
            end_position = (x, y)

valid_chars = ['.', 'E', 'S']
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
path = {start_position: 0}
position = (start_position[0], start_position[1])
while position != end_position:
    for direction in directions:
        target = (position[0] + direction[0], position[1] + direction[1])
        if 0 < target[0] < len(lines[0]) - 1 and 0 < target[1] < len(lines) - 1 and \
                lines[target[1]][target[0]] in valid_chars and target not in path:
            path[target] = path[position] + 1
            position = target
            break

regular_time = max(path.values())
print('Regular time:', regular_time)
shortcuts2ps = []
for position in path:
    for direction in directions:
        target1 = (position[0] + direction[0], position[1] + direction[1])
        target2 = (position[0] + direction[0] * 2, position[1] + direction[1] * 2)
        if 0 < target1[0] < len(lines[0]) - 1 and 0 < target1[1] < len(lines) - 1 and lines[target1[1]][target1[0]] == '#':
            if 0 < target2[0] < len(lines[0]) - 1 and 0 < target2[1] < len(lines) - 1 and lines[target2[1]][target2[0]] in valid_chars:
                if path[target2] > path[position]:
                    shortcuts2ps.append([position, target2])
print('2ps Shortcuts:', len(shortcuts2ps))
cheated_times = {}
for shortcut in shortcuts2ps:
    new_time = path[shortcut[0]] + 2 + (regular_time - path[shortcut[1]])
    if new_time not in cheated_times:
        cheated_times[new_time] = 1
    else:
        cheated_times[new_time] += 1
result = 0
for key in sorted(cheated_times, reverse=True):
    saved_time = regular_time - key
    if saved_time >= 100:
        result += cheated_times[key]
    # print('There are', cheated_times[key], 'cheats that save', saved_time, 'picoseconds.')
print('2ps Shortcuts saving 100+:', result)

shortcuts20ps = set()
for position in path:
    for iy in range(-20, 21):
        for ix in range(-20, 21):
            target = (position[0] + ix, position[1] + iy)
            if 0 < target[0] < len(lines[0]) - 1 and 0 < target[1] < len(lines) - 1 and \
                    lines[target[1]][target[0]] in valid_chars:
                cheat_duration = abs(target[0] - position[0]) + abs(target[1] - position[1])
                if cheat_duration <= 20 and path[target] > path[position]:
                    shortcuts20ps.add((position, target, cheat_duration))
print('20ps Shortcuts:', len(shortcuts20ps))
cheated_times = {}
for shortcut in shortcuts20ps:
    new_time = path[shortcut[0]] + shortcut[2] + (regular_time - path[shortcut[1]])
    if new_time not in cheated_times:
        cheated_times[new_time] = 1
    else:
        cheated_times[new_time] += 1
result = 0
for key in sorted(cheated_times, reverse=True):
    saved_time = regular_time - key
    if saved_time >= 100:
        result += cheated_times[key]
        # print('There are', cheated_times[key], 'cheats that save', saved_time, 'picoseconds.')
print('20ps Shortcuts saving 100+:', result)
