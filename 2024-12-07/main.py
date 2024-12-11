calculations = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for row in f:
        parts = row.strip().split(':')
        components = [int(x) for x in parts[1].split(' ') if len(x) > 0]
        calculations.append([int(parts[0]), components, []])

operators = ['+', '*']


def recurse(calculation, path):
    if len(path) == len(calculation[1]) - 1:
        s = calculation[1][0]
        for i in range(0, len(path)):
            op = path[i]
            value = calculation[1][i + 1]
            if op == '+':
                s += value
            elif op == '*':
                s *= value
            elif op == '||':
                s = int(str(s) + str(value))
        if s == calculation[0]:
            calculation[2].append(path)
    else:
        for op in operators:
            recurse(calculation, path + [op])


result = 0
for calculation in calculations:
    recurse(calculation, [])
    if len(calculation[2]) > 0:
        result += calculation[0]
print(result)

result = 0
operators = ['+', '*', '||']
for calculation in calculations:
    recurse(calculation, [])
    if len(calculation[2]) > 0:
        result += calculation[0]
print(result)
