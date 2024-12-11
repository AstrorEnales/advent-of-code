list_a = []
list_b = []
with open('input.txt', 'r', encoding='utf-8') as f:
    for row in f:
        if len(row) > 1:
            a, b = row.strip().split('   ')
            list_a.append(int(a))
            list_b.append(int(b))
list_a.sort()
list_b.sort()
result = 0
for i in range(len(list_a)):
    result += abs(list_a[i] - list_b[i])
print(result)
counter_a = {}
counter_b = {}
for i in range(len(list_a)):
    value_a = list_a[i]
    value_b = list_b[i]
    if value_a not in counter_a:
        counter_a[value_a] = 1
    else:
        counter_a[value_a] += 1
    if value_b not in counter_b:
        counter_b[value_b] = 1
    else:
        counter_b[value_b] += 1
result = 0
for key, value in counter_a.items():
    if key in counter_b:
        result += value * counter_b[key] * key
print(result)