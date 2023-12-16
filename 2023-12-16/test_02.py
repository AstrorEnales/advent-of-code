def traverse_beams(lines, beams):
    w = len(lines[0])
    h = len(lines)
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
    result = 0
    for y in range(0, h):
        for x in range(0, w):
            if len(visited[y][x]) > 0:
                result += 1
    return result


def find_most_efficient_start_beam(lines):
    w = len(lines[0])
    h = len(lines)
    max_energized = 0
    for x in range(0, w):
        max_energized = max(max_energized, traverse_beams(lines, [[x, -1, 0, 1]]))
        max_energized = max(max_energized, traverse_beams(lines, [[x, h, 0, -1]]))
    for y in range(0, h):
        max_energized = max(max_energized, traverse_beams(lines, [[-1, y, 1, 0]]))
        max_energized = max(max_energized, traverse_beams(lines, [[w, y, -1, 0]]))
    print(max_energized)


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
find_most_efficient_start_beam(test_lines)
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    find_most_efficient_start_beam(lines)
