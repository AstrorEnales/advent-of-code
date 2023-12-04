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
    return s == '*'


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
    gear_part_numbers = {}
    for i, line in enumerate(lines):
        number_ranges = all_number_ranges(line)
        part_numbers = []
        for start, end in number_ranges:
            part_number = int(line[start:end + 1])
            gear_indices = set()
            if start > 0 and is_allowed_symbol(line[start - 1]):
                gear_indices.add((i, start - 1))
            if end < len(line) - 1 and is_allowed_symbol(line[end + 1]):
                gear_indices.add((i, end + 1))
            for j in range(max(0, start - 1), min(end + 2, len(line))):
                if i > 0 and is_allowed_symbol(lines[i - 1][j]):
                    gear_indices.add((i - 1, j))
                if i < len(lines) - 1 and is_allowed_symbol(lines[i + 1][j]):
                    gear_indices.add((i + 1, j))
            for gear_index in gear_indices:
                if gear_index not in gear_part_numbers:
                    gear_part_numbers[gear_index] = set()
                gear_part_numbers[gear_index].add(part_number)
    for key, value in gear_part_numbers.items():
        if len(value) == 2:
            part_numbers = list(value)
            result += part_numbers[0] * part_numbers[1]
    print(result)
