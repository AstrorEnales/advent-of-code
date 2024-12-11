import math

rules = set()
updates = []
with open('input.txt', 'r', encoding='utf-8') as f:
    in_rules = True
    for line in f:
        line = line.strip()
        if line == '':
            in_rules = False
            continue
        if in_rules:
            rules.add(line)
        else:
            updates.append(line.split(','))


def is_update_valid(update):
    valid = True
    for i in range(0, len(update) - 1):
        for j in range(i + 1, len(update)):
            if '%s|%s' % (update[j], update[i]) in rules:
                valid = False
                break
        if not valid:
            break
    return valid


incorrect_updates = []
result = 0
for update in updates:
    if is_update_valid(update):
        result += int(update[math.floor(len(update) / 2)])
    else:
        incorrect_updates.append(update)
print(result)

result = 0
for update in incorrect_updates:
    while not is_update_valid(update):
        modified = False
        for i in range(0, len(update) - 1):
            for j in range(i + 1, len(update)):
                if '%s|%s' % (update[j], update[i]) in rules:
                    a = update[i]
                    b = update[j]
                    update[i] = b
                    update[j] = a
                    modified = True
                    break
            if modified:
                break
    result += int(update[math.floor(len(update) / 2)])
print(result)
