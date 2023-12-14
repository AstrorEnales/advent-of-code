def tilt_north(w, h, result, stone_positions):
    stone_positions.sort(key=lambda x: x[1])
    last_stone_y = [-1] * w
    for i in range(0, len(stone_positions)):
        x, y = stone_positions[i]
        for k in range(y - 1, last_stone_y[x], -1):
            if result[k][x] == '#':
                break
            stone_positions[i][1] -= 1
            last_stone_y[x] = stone_positions[i][1]
        last_stone_y[x] = max(last_stone_y[x], stone_positions[i][1])


def tilt_south(w, h, result, stone_positions):
    stone_positions.sort(key=lambda x: x[1], reverse=True)
    last_stone_y = [h] * w
    for i in range(0, len(stone_positions)):
        x, y = stone_positions[i]
        for k in range(y + 1, last_stone_y[x]):
            if result[k][x] == '#':
                break
            stone_positions[i][1] += 1
            last_stone_y[x] = stone_positions[i][1]
        last_stone_y[x] = min(last_stone_y[x], stone_positions[i][1])


def tilt_east(w, h, result, stone_positions):
    stone_positions.sort(key=lambda x: x[0], reverse=True)
    last_stone_x = [w] * h
    for i in range(0, len(stone_positions)):
        x, y = stone_positions[i]
        for k in range(x + 1, last_stone_x[y]):
            if result[y][k] == '#':
                break
            stone_positions[i][0] += 1
            last_stone_x[y] = stone_positions[i][0]
        last_stone_x[y] = min(last_stone_x[y], stone_positions[i][0])


def tilt_west(w, h, result, stone_positions):
    stone_positions.sort(key=lambda x: x[0])
    last_stone_x = [-1] * h
    for i in range(0, len(stone_positions)):
        x, y = stone_positions[i]
        for k in range(x - 1, last_stone_x[y], -1):
            if result[y][k] == '#':
                break
            stone_positions[i][0] -= 1
            last_stone_x[y] = stone_positions[i][0]
        last_stone_x[y] = max(last_stone_x[y], stone_positions[i][0])


def tilt_cycle(w, h, result, stone_positions):
    tilt_north(w, h, result, stone_positions)
    tilt_west(w, h, result, stone_positions)
    tilt_south(w, h, result, stone_positions)
    tilt_east(w, h, result, stone_positions)


def calculate_north_load(h, stone_positions):
    return sum(h - x[1] for x in stone_positions)


def find_stones_and_clear_plate(lines):
    result = []
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if lines[i][j] == 'O':
                result.append([j, i])
                lines[i][j] = '.'
    return result


def iterate_stones(lines):
    iterations = 1_000_000_000
    result = [list(x) for x in lines]
    w = len(result[0])
    h = len(result)
    stone_positions = find_stones_and_clear_plate(result)
    history = []
    for i in range(0, iterations):
        tilt_cycle(w, h, result, stone_positions)
        s = set(map(tuple, stone_positions))
        if s in history:
            cycle_index = history.index(s)
            cycle_length = i - cycle_index
            offset = (iterations - 1 - i) % cycle_length
            stone_positions = list(history[cycle_index + offset])
            break
        history.append(s)
    print(calculate_north_load(h, stone_positions))


test_lines = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....'
]
iterate_stones(test_lines)
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    iterate_stones(lines)
