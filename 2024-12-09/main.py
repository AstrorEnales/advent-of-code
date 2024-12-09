disk = []
with open('input.txt', 'r', encoding='utf-8') as f:
    l = f.readline().strip()
    # l = '2333133121414131402'
    _id = 0
    for i in range(0, len(l)):
        if i % 2 == 0:
            disk.append([_id, int(l[i])])
            _id += 1
        else:
            disk.append([None, int(l[i])])

original_disk = [[y for y in x] for x in disk]


def has_any_empty(disk):
    return any(x for x in disk if x[0] is None)


next_empty_index = 1
while has_any_empty(disk):
    last_block = disk[-1]
    empty_block = disk[next_empty_index]
    capacity_to_fill = min(empty_block[1], last_block[1])
    free_space = empty_block[1] - capacity_to_fill
    # print('|'.join((str(x[0]) if x[0] is not None else '.') * x[1] for x in disk), next_empty_index, capacity_to_fill, free_space)
    empty_block[0] = last_block[0]
    empty_block[1] = capacity_to_fill
    if capacity_to_fill == last_block[1]:
        del disk[-1]
        del disk[-1]
    else:
        last_block[1] -= capacity_to_fill
    if free_space > 0:
        next_empty_index += 1
        if next_empty_index < len(disk):
            disk.insert(next_empty_index, [None, free_space])
    else:
        next_empty_index += 2

# print('|'.join((str(x[0]) if x[0] is not None else '.') * x[1] for x in disk))
result = 0
counter = 0
for block in disk:
    for j in range(0, block[1]):
        result += block[0] * counter
        counter += 1
print(result)

disk = original_disk
# print('|'.join((str(x[0]) if x[0] is not None else '.') * x[1] for x in disk))
for i in range(len(disk) - 1, 0, -1):
    last_block = disk[i]
    if last_block[0] is None:
        continue
    for j in range(0, i):
        block = disk[j]
        if block[0] is None and block[1] >= last_block[1]:
            free_space = block[1] - last_block[1]
            block[0] = last_block[0]
            block[1] = last_block[1]
            last_block[0] = None
            if free_space > 0:
                disk.insert(j + 1, [None, free_space])
            break
    # print('|'.join((str(x[0]) if x[0] is not None else '.') * x[1] for x in disk))
result = 0
counter = 0
for block in disk:
    for j in range(0, block[1]):
        if block[0] is not None:
            result += block[0] * counter
        counter += 1
print(result)
