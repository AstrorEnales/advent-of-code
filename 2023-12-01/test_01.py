def find_calibration_value(line: str) -> int:
    digits = [x for x in line if x.isnumeric()]
    return int(digits[0] + digits[-1])


with open('input_01.txt', 'r', encoding='utf-8') as f:
    print(sum([find_calibration_value(x) for x in f.readlines()]))
