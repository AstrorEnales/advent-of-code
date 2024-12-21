with open('input.txt', 'r', encoding='utf-8') as f:
    codes = [x.strip() for x in f.readlines()]
codes = ['029A', '980A', '179A', '456A', '379A']

inverse_directions = {'>': '<', '<': '>', 'v': '^', '^': 'v'}

big_keypad = {
    '0': {
        'A': ['>'],
        '1': ['^<'],
        '2': ['^'],
        '3': ['^>', '>^'],
        '4': ['^^<'],  #, '^<^'
        '5': ['^^'],
        '6': ['^^>', '>^^'],  #, '^>^'
        '7': ['^^^<'],  #, '^<^^', '^^<^'
        '8': ['^^^'],
        '9': ['^^^>', '>^^^'],  #, '^>^^', '^^>^'
    },
    '1': {
        'A': ['>>v'],  #, '>v>'
        '2': ['>'],
        '3': ['>>'],
        '4': ['^'],
        '5': ['^>', '>^'],
        '6': ['>>^', '^>>'],  #, '>^>'
        '7': ['^^'],
        '8': ['^^>', '>^^'],  #, '^>^'
        '9': ['>>^^', '^^>>'],  #, '^>^>', '>^^>', '>^>^'
    },
    '2': {
        'A': ['>v', 'v>'],
        '3': ['>'],
        '4': ['<^', '^<'],
        '5': ['^'],
        '6': ['^>', '>^'],
        '7': ['<^^', '^^<'],  #, '^<^'
        '8': ['^^'],
        '9': ['>^^', '^^>'],  #, '^>^'
    },
    '3': {
        'A': ['v'],
        '4': ['<<^', '^<<'],  #, '<^<'
        '5': ['<^', '^<'],
        '6': ['^'],
        '7': ['<<^^', '^^<<'], #, '^<^<', '^<<^', '<^<^'
        '8': ['<^^', '^^<'],  #, '^<^'
        '9': ['^^'],
    },
    '4': {
        'A': ['>>vv'],  #, '>v>v', '>vv>', 'v>v>', 'v>>v'
        '5': ['>'],
        '6': ['>>'],
        '7': ['^'],
        '8': ['^>', '>^'],
        '9': ['>>^', '^>>'],  #, '>^>'
    },
    '5': {
        'A': ['vv>', '>vv'],  #, 'v>v'
        '6': ['>'],
        '7': ['<^', '^<'],
        '8': ['^'],
        '9': ['^>', '>^'],
    },
    '6': {
        'A': ['vv'],
        '7': ['^<<', '<<^'],  #, '<^<'
        '8': ['<^', '^<'],
        '9': ['^'],
    },
    '7': {
        'A': ['>>vvv'],  #, '>v>vv', '>vv>v', '>vvv>', 'v>>vv', 'v>v>v', 'v>vv>', 'vv>v>', 'vv>>v'
        '8': ['>'],
        '9': ['>>'],
    },
    '8': {
        'A': ['vvv>', '>vvv'],  #, 'v>vv', 'vv>v'
        '9': ['>'],
    },
    '9': {
        'A': ['vvv'],
    },
    'A': {}
}

big_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
for x in big_chars:
    for y in big_chars:
        if x != y and y not in big_keypad[x]:
            big_keypad[x][y] = [''.join([inverse_directions[c] for c in pattern]) for pattern in big_keypad[y][x]]

for x in big_chars:
    for y in big_chars:
        if x != y:
            big_keypad[x][y] = [list(pattern) + ['A'] for pattern in big_keypad[x][y]]

small_keypad = {
    '<': {
        '^': ['>^'],
        'v': ['>'],
        '>': ['>>'],
        'A': ['>>^'],  #, '>^>'
    },
    '>': {
        '^': ['^<', '<^'],
        'v': ['<'],
        'A': ['^'],
    },
    '^': {
        'v': ['v'],
        'A': ['>'],
    },
    'v': {
        'A': ['>^', '^>'],
    },
    'A': {}
}

small_chars = ['<', '>', '^', 'v', 'A']
for x in small_chars:
    for y in small_chars:
        if x != y and y not in small_keypad[x]:
            small_keypad[x][y] = [''.join([inverse_directions[c] for c in pattern]) for pattern in small_keypad[y][x]]

for x in small_chars:
    for y in small_chars:
        if x != y:
            small_keypad[x][y] = [list(pattern) + ['A'] for pattern in small_keypad[x][y]]


def recurse_paths(keypad, position, code, index, moves, results):
    if index == len(code):
        results.add(''.join(moves))
        return
    c = code[index]
    if position != c:
        options = keypad[position][c]
        for option in options:
            recurse_paths(keypad, c, code, index + 1, moves + option, results)
    else:
        recurse_paths(keypad, c, code, index + 1, moves + ['A'], results)


result = 0
for code in codes:
    results = [set(), set(), set(), set()]
    recurse_paths(big_keypad, 'A', code, 0, [], results[0])
    print(len(results[0]))
    for depth in range(1, 4):
        for path in results[depth - 1]:
            recurse_paths(small_keypad, 'A', path, 0, [], results[depth])

        min_length = min([len(x) for x in results[depth]])
        results[depth] = [x for x in results[depth] if len(x) == min_length]

        print(len(results[depth]))
    print(len(results[0]), len(results[1]), len(results[2]), len(results[3]))
    min_length = min([len(x) for x in results[3]])
    complexity = min_length * int(code.replace('A', ''))
    print(complexity)
    result += complexity
print(result)
