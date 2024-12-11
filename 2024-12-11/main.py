from collections import defaultdict

with open('input.txt', 'r', encoding='utf-8') as f:
    line = [int(x) for x in f.readline().strip().split(' ')]

# line = [[0], [1], [10], [99], [999]]
# line = [[125], [17]]

counter = defaultdict(lambda: 0)
for x in line:
    counter[x] += 1

for i in range(0, 75):
    new_counter = defaultdict(lambda: 0)
    for n, count in counter.items():
        if n == 0:
            new_counter[1] += count
        elif len(str(n)) % 2 == 0:
            half_len = len(str(n)) // 2
            new_counter[int(str(n)[0:half_len])] += count
            new_counter[int(str(n)[half_len:])] += count
        else:
            new_counter[n * 2024] += count
    counter = new_counter
print(sum(x for x in counter.values()))
