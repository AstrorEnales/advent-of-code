def is_safe(report):
    valid = True
    test = report[1] > report[0]
    for i in range(1, len(report)):
        offset = abs(report[i] - report[i - 1])
        if test != (report[i] > report[i - 1]) or offset < 1 or offset > 3:
            valid = False
            break
    return valid


with open('input.txt', 'r', encoding='utf-8') as f:
    reports = [[int(x) for x in row.strip().split(' ')] for row in f if len(row) > 1]

result = 0
for report in reports:
    if is_safe(report):
        result += 1
print(result)

result = 0
for report in reports:
    if is_safe(report):
        result += 1
    else:
        for i in range(0, len(report)):
            dampened_report = report[:i] + report[i + 1:]
            if is_safe(dampened_report):
                result += 1
                break
print(result)
