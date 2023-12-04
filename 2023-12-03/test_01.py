def all_number_ranges(line: str):
    result = []
    inside_number = False
    for i in range(0, len(line)):
        if line[i].isnumeric():
            if inside_number:
                result[-1][1] = i
            else:
                result.append([i, i])
                inside_number = True
        else:
            inside_number = False
    return result


def is_allowed_symbol(s: str) -> bool:
    return s != '.' and not s.isnumeric()


test_lines = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    result = 0
    for i, line in enumerate(lines):
        number_ranges = all_number_ranges(line)
        part_numbers = []
        for start, end in number_ranges:
            part_number = int(line[start:end + 1])
            is_adjacent_to_symbol = False
            if start > 0 and is_allowed_symbol(line[start - 1]):
                print('1', part_number)
                is_adjacent_to_symbol = True
            if end < len(line) - 1 and is_allowed_symbol(line[end + 1]):
                print('2', part_number)
                is_adjacent_to_symbol = True
            for j in range(max(0, start - 1), min(end + 2, len(line))):
                if i > 0 and is_allowed_symbol(lines[i - 1][j]):
                    print('3', part_number)
                    is_adjacent_to_symbol = True
                if i < len(lines) - 1 and is_allowed_symbol(lines[i + 1][j]):
                    print('4', part_number)
                    is_adjacent_to_symbol = True

            if is_adjacent_to_symbol:
                part_numbers.append(part_number)
        print(part_numbers)
        result += sum(part_numbers)
    print(result)
