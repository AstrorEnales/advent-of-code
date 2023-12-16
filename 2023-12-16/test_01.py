def traverse_beams(lines):
    w = len(lines[0])
    h = len(lines)
    beams = [[-1, 0, 1, 0]]
    visited = [[set() for _ in range(0, w)] for _ in range(0, h)]
    while len(beams) > 0:
        beam = beams.pop()
        next_x = beam[0] + beam[2]
        next_y = beam[1] + beam[3]
        if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
            continue
        symbol = lines[next_y][next_x]
        new_beams = []
        pass_through_beam = [next_x, next_y, beam[2], beam[3]]
        if symbol == '.':
            new_beams.append(pass_through_beam)
        elif symbol == '|':
            if beam[3] != 0:
                new_beams.append(pass_through_beam)
            else:
                new_beams.append([next_x, next_y, 0, -1])
                new_beams.append([next_x, next_y, 0, 1])
        elif symbol == '-':
            if beam[2] != 0:
                new_beams.append(pass_through_beam)
            else:
                new_beams.append([next_x, next_y, -1, 0])
                new_beams.append([next_x, next_y, 1, 0])
        elif symbol == '/':
            if beam[2] != 0:
                new_beams.append([next_x, next_y, 0, -beam[2]])
            else:
                new_beams.append([next_x, next_y, -beam[3], 0])
        elif symbol == '\\':
            if beam[2] != 0:
                new_beams.append([next_x, next_y, 0, beam[2]])
            else:
                new_beams.append([next_x, next_y, beam[3], 0])
        for new_beam in new_beams:
            direction = (new_beam[2], new_beam[3])
            if direction not in visited[next_y][next_x]:
                beams.append(new_beam)
                visited[next_y][next_x].add(direction)

    # print_energized(w, h, lines, visited)
    result = 0
    for y in range(0, h):
        for x in range(0, w):
            if len(visited[y][x]) > 0:
                result += 1
    print(result)


def print_energized(w, h, lines, visited):
    result = [list(x) for x in lines]
    for y in range(0, h):
        for x in range(0, w):
            if len(visited[y][x]) > 0 and lines[y][x] == '.':
                result[y][x] = '#'
    for x in result:
        print(''.join(x))


test_lines = [
    '.|...\....',
    '|.-.\.....',
    '.....|-...',
    '........|.',
    '..........',
    '.........\\',
    '..../.\\\\..',
    '.-.-/..|..',
    '.|....-|.\\',
    '..//.|....'
]
traverse_beams(test_lines)
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    traverse_beams(lines)
