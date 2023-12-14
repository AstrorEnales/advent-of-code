def tilt_north(lines):
    result = [list(x) for x in lines]
    for i in range(1, len(result)):
        for j in range(0, len(result[0])):
            if result[i][j] == 'O':
                for k in range(i - 1, -1, -1):
                    if result[k][j] == '#':
                        break
                    if result[k][j] == '.':
                        result[k + 1][j] = '.'
                        result[k][j] = 'O'
    return result


def calculate_north_load(stones):
    result = 0
    for i in range(0, len(stones)):
        for j in range(0, len(stones[0])):
            if stones[i][j] == 'O':
                result += len(stones) - i
    return result


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
test_stones = tilt_north(test_lines)
print(calculate_north_load(test_stones))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    stones = tilt_north(lines)
    print(calculate_north_load(stones))
