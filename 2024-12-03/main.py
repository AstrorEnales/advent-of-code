import re

r = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
r2 = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don\'t\(\)')

result = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for row in f:
        for match in r.finditer(row):
            a = int(match.group(1))
            b = int(match.group(2))
            result += a * b
print(result)
result = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    enabled = True
    for row in f:
        for match in r2.finditer(row):
            if match.group() == 'do()':
                enabled = True
            elif match.group() == 'don\'t()':
                enabled = False
            elif enabled:
                a = int(match.group(1))
                b = int(match.group(2))
                result += a * b
print(result)
