def split_fields(lines):
    result = [[]]
    for line in lines:
        if line == '':
            result.append([])
        else:
            result[-1].append(line)
    return result


def find_field_mirror(field):
    results_horizontal = []
    results_vertical = []
    # horizontal mirror
    for i in range(1, len(field)):
        mismatches = 0
        for j in range(1, min(i, len(field) - i) + 1):
            a = field[i - j]
            b = field[i + j - 1]
            for k in range(0, len(a)):
                if a[k] != b[k]:
                    mismatches += 1
        if mismatches == 1:
            results_horizontal.append(i)
    for i in range(1, len(field[0])):
        mismatches = 0
        for j in range(1, min(i, len(field[0]) - i) + 1):
            a = [row[i - j] for row in field]
            b = [row[i + j - 1] for row in field]
            for k in range(0, len(a)):
                if a[k] != b[k]:
                    mismatches += 1
        if mismatches == 1:
            results_vertical.append(i)
    max_horizontal = max(results_horizontal) if len(results_horizontal) > 0 else 0
    max_vertical = max(results_vertical) if len(results_vertical) > 0 else 0
    if len(results_horizontal) == 0 and len(results_vertical) == 0:
        print(results_horizontal, results_vertical)
        for line in field:
            print(line)
    if max_horizontal > max_vertical:
        return max_horizontal * 100
    return max_vertical


test_lines = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.',
    '',
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#'
]

test_fields = split_fields(test_lines)
print(sum([find_field_mirror(field) for field in test_fields]))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    fields = split_fields(lines)
    print(sum([find_field_mirror(field) for field in fields]))
