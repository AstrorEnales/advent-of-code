# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

x_connections = {'FS', 'LS', '-S', 'S-', 'S7', 'SJ', '--', '-J', '-7', 'F-', 'F7', 'FJ', 'L-', 'LJ', 'L7'}
y_connections = {'S|', 'SL', 'SJ', '|S', 'FS', '7S', '||', '7|', 'F|', '7J', '7L', 'FJ', 'FL', '|J', '|L'}


def find_connecting_pipes(lines, position):
    sign = lines[position[1]][position[0]]
    connections = []
    if position[0] > 0:
        candidate = lines[position[1]][position[0] - 1]
        if candidate + sign in x_connections:
            connections.append([position[0] - 1, position[1]])
    if position[0] < len(lines[0]) - 1:
        candidate = lines[position[1]][position[0] + 1]
        if sign + candidate in x_connections:
            connections.append([position[0] + 1, position[1]])
    if position[1] > 0:
        candidate = lines[position[1] - 1][position[0]]
        if candidate + sign in y_connections:
            connections.append([position[0], position[1] - 1])
    if position[1] < len(lines) - 1:
        candidate = lines[position[1] + 1][position[0]]
        if sign + candidate in y_connections:
            connections.append([position[0], position[1] + 1])
    return connections


def find_loop(lines):
    start_coords = [-1, -1]
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == 'S':
                start_coords = [x, y]
                break
        if start_coords[0] != -1:
            break
    candidates = [find_connecting_pipes(lines, start_coords)]
    loop = [start_coords]
    while True:
        # Backtrack if necessary
        while len(candidates[-1]) == 0:
            candidates.pop()
            loop.pop()
        next_candidate = candidates[-1].pop()
        if next_candidate[0] == start_coords[0] and next_candidate[1] == start_coords[1]:
            break
        connections = find_connecting_pipes(lines, next_candidate)
        connections = list(filter(lambda x:
                                  x not in loop or
                                  (len(loop) > 2 and x[0] == start_coords[0] and x[1] == start_coords[1]),
                                  connections))
        if len(connections) > 0:
            candidates.append(connections)
            loop.append(next_candidate)

    with open('test.html', 'w', encoding='utf-8') as f2:
        f2.write('<html>')
        f2.write('<body>')
        f2.write('<table>')
        for y in range(0, len(lines)):
            f2.write('<tr>')
            for x in range(0, len(lines[0])):
                f2.write('<td style="background-color:%s">%s</td>' % ('#22ff22' if [x, y] in loop else '#ffffff', lines[y][x]))
            f2.write('</tr>')
        f2.write('</table>')
        f2.write('</body>')
        f2.write('</html>')
    print(len(loop) // 2)


test_lines_01 = [
    '.....',
    '.S-7.',
    '.|.|.',
    '.L-J.',
    '.....'
]
test_lines_02 = [
    '..F7.',
    '.FJ|.',
    'SJ.L7',
    '|F--J',
    'LJ...'
]
find_loop(test_lines_01)
find_loop(test_lines_02)
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    find_loop(lines)
