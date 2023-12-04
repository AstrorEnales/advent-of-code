import regex

spelled_letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
pattern = regex.compile(r'([0-9]|one|two|three|four|five|six|seven|eight|nine)')


def find_calibration_value(line: str) -> int:
    matches = pattern.findall(line, overlapped=True)
    digits = [(spelled_letters.index(x) + 1) if x in spelled_letters else int(x) for x in matches]
    return int(str(digits[0]) + str(digits[-1]))


test_lines = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen'
]
print(sum([find_calibration_value(x) for x in test_lines]))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    print(sum([find_calibration_value(x) for x in f.readlines()]))
