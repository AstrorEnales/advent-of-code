with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]

#lines = [
#    'MMMSXXMASM',
#    'MSAMXMSMSA',
#    'AMXSXMAAMM',
#    'MSAMASMSMX',
#    'XMASAMXAMM',
#    'XXAMMXXAMA',
#    'SMSMSASXSS',
#    'SAXAMASAAA',
#    'MAMMMXMMMM',
#    'MXMXAXMASX'
#]

XMAS = 'XMAS'
counter = 0
for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        l = 1
        r = 1
        u = 1
        d = 1
        lu = 1
        ld = 1
        ru = 1
        rd = 1
        for i in range(0, 4):
            has_left = x - i >= 0
            has_right = x + i < len(lines[0])
            has_down = y + i < len(lines)
            has_up = y - i >= 0
            if not has_left or lines[y][x - i] != XMAS[i]:
                l = 0
            if not has_right or lines[y][x + i] != XMAS[i]:
                r = 0
            if not has_up or lines[y - i][x] != XMAS[i]:
                u = 0
            if not has_down or lines[y + i][x] != XMAS[i]:
                d = 0
            if not has_left or not has_up or lines[y - i][x - i] != XMAS[i]:
                lu = 0
            if not has_left or not has_down or lines[y + i][x - i] != XMAS[i]:
                ld = 0
            if not has_right or not has_up or lines[y - i][x + i] != XMAS[i]:
                ru = 0
            if not has_right or not has_down or lines[y + i][x + i] != XMAS[i]:
                rd = 0
        counter += l + r + u + d + lu + ld + ru + rd
print(counter)

counter = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        if lines[y][x] != 'A':
            continue
        a = sorted([lines[y - 1][x - 1], lines[y + 1][x + 1]])
        b = sorted([lines[y + 1][x - 1], lines[y - 1][x + 1]])
        if a[0] == 'M' and a[1] == 'S' and b[0] == 'M' and b[1] == 'S':
            counter += 1
print(counter)
