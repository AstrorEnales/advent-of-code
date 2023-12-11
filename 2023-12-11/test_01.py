def get_length(position_1, position_2):
    return abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1])


def get_pairs(galaxies):
    result = set()
    for i in range(0, len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            result.add((i, j))
    return result


def find_galaxies(lines):
    result = []
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == '#':
                result.append([x, y])
    return result


def expand_universe(lines):
    result = []
    for line in lines:
        if all([x == '.' for x in line]):
            result.append(line)
        result.append(line)
    for i in range(len(lines[0]) - 1, 0, -1):
        if all([x[i] == '.' for x in lines]):
            for j in range(0, len(result)):
                result[j] = result[j][:i] + '.' + result[j][i:]
    return result


test_input = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....'
]
test_input_expanded = expand_universe(test_input)
test_galaxies = find_galaxies(test_input_expanded)
print(test_galaxies)
test_pairs = get_pairs(test_galaxies)
print(sum([get_length(test_galaxies[pair[0]], test_galaxies[pair[1]]) for pair in test_pairs]))

with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    lines_expanded = expand_universe(lines)
    galaxies = find_galaxies(lines_expanded)
    pairs = get_pairs(galaxies)
    print(sum([get_length(galaxies[pair[0]], galaxies[pair[1]]) for pair in pairs]))
