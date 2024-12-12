with open('input.txt', 'r', encoding='utf-8') as f:
    grid = [x.strip() for x in f.readlines()]

# grid = ['AAAA', 'BBCD', 'BBCC', 'EEEC']
# grid = ['OOOOO', 'OXOXO', 'OOOOO', 'OXOXO', 'OOOOO']
# grid = ['EEEEE', 'EXXXX', 'EEEEE', 'EXXXX', 'EEEEE']
# grid = ['AAAAAA', 'AAABBA', 'AAABBA', 'ABBAAA', 'ABBAAA', 'AAAAAA']
# grid = ['RRRRIICCFF', 'RRRRIICCCF', 'VVRRRCCFFF', 'VVRCCCJFFF', 'VVVVCJJCFE', 'VVIVCCJJEE', 'VVIIICJJEE', 'MIIIIIJJEE',
#         'MIIISIJEEE', 'MMMISSJEEE']

visited = [[0] * len(x) for x in grid]
labels = [[None] * len(x) for x in grid]
linked_labels = {}
next_label = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        plot_type = grid[y][x]
        candidates = set()
        if y > 0 and grid[y - 1][x] == plot_type:
            candidates.add(labels[y - 1][x])
        if x > 0 and grid[y][x - 1] == plot_type:
            candidates.add(labels[y][x - 1])
        if len(candidates) == 0:
            linked_labels[next_label] = set()
            labels[y][x] = next_label
            next_label += 1
        else:
            labels[y][x] = min(candidates)
            for l in candidates:
                linked_labels[l].update(candidates)

changed = True
while changed:
    changed = False
    for l in linked_labels:
        size_before = len(linked_labels[l])
        for other_label in list(linked_labels[l]):
            if other_label != l:
                linked_labels[l].update(linked_labels[other_label])
                linked_labels[other_label].update(linked_labels[l])
        if len(linked_labels[l]) != size_before:
            changed = True

reduced_lookup = {l: min(linked_labels[l]) if len(linked_labels[l]) > 0 else l for l in linked_labels}
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        labels[y][x] = reduced_lookup[labels[y][x]]

result = 0
result2 = 0
for l in range(0, next_label):
    area = 0
    perimeter = 0
    perimeters = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if labels[y][x] == l:
                area += 1
                # Left
                if x == 0 or labels[y][x - 1] != l:
                    perimeter += 1
                    perimeters.append([x, y, 0, 1, 1, 0, -1])
                # Right
                if x == len(grid[0]) - 1 or labels[y][x + 1] != l:
                    perimeter += 1
                    perimeters.append([x + 1, y, 0, 1, 1, 0, 1])
                # Up
                if y == 0 or labels[y - 1][x] != l:
                    perimeter += 1
                    perimeters.append([x, y, 1, 0, 1, -1, 0])
                # Down
                if y == len(grid) - 1 or labels[y + 1][x] != l:
                    perimeter += 1
                    perimeters.append([x, y + 1, 1, 0, 1, 1, 0])
    result += area * perimeter

    changed = True
    while changed:
        changed = False
        for i in range(len(perimeters) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                p1 = perimeters[i]
                p2 = perimeters[j]
                if p1[2] == p2[2] and p1[3] == p2[3] and p1[5] == p2[5] and p1[6] == p2[6]:
                    if p1[0] == p2[0] + p2[2] * p2[4] and p1[1] == p2[1] + p2[3] * p2[4]:
                        p2[4] += p1[4]
                        changed = True
                        del perimeters[i]
                        break
                    elif p1[0] + p1[2] * p1[4] == p2[0] and p1[1] + p1[3] * p1[4] == p2[1]:
                        p2[0] = p1[0]
                        p2[1] = p1[1]
                        p2[4] += p1[4]
                        changed = True
                        del perimeters[i]
                        break
    sides = len(perimeters)
    result2 += area * sides
print(result)
print(result2)
