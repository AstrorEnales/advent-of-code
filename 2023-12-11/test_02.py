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


def expand_galaxies(lines, galaxies, expansion):
    for i in range(len(lines) - 1, 0, -1):
        if all([x == '.' for x in lines[i]]):
            for galaxy in galaxies:
                if galaxy[1] > i:
                    galaxy[1] += expansion - 1
    for i in range(len(lines[0]) - 1, 0, -1):
        if all([x[i] == '.' for x in lines]):
            for galaxy in galaxies:
                if galaxy[0] > i:
                    galaxy[0] += expansion - 1
    return galaxies


test_input = [
    #0123456789
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
test_galaxies = expand_galaxies(test_input, find_galaxies(test_input), 2)
test_pairs = get_pairs(test_galaxies)
print(sum([get_length(test_galaxies[pair[0]], test_galaxies[pair[1]]) for pair in test_pairs]))

test_galaxies = expand_galaxies(test_input, find_galaxies(test_input), 10)
test_pairs = get_pairs(test_galaxies)
print(sum([get_length(test_galaxies[pair[0]], test_galaxies[pair[1]]) for pair in test_pairs]))

test_galaxies = expand_galaxies(test_input, find_galaxies(test_input), 100)
test_pairs = get_pairs(test_galaxies)
print(sum([get_length(test_galaxies[pair[0]], test_galaxies[pair[1]]) for pair in test_pairs]))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    galaxies = expand_galaxies(lines, find_galaxies(lines), 1000000)
    pairs = get_pairs(galaxies)
    print(sum([get_length(galaxies[pair[0]], galaxies[pair[1]]) for pair in pairs]))
