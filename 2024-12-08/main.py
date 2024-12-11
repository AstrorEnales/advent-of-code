
with open('input.txt', 'r', encoding='utf-8') as f:
    grid = [x.strip() for x in f]

towers = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        c = grid[y][x]
        if c != '.':
            if c not in towers:
                towers[c] = []
            towers[c].append((x, y))

antinodes = set()
for key in towers:
    for p1 in towers[key]:
        for p2 in towers[key]:
            if p1 == p2:
                continue
            v = (p2[0] - p1[0], p2[1] - p1[1])
            target = (p2[0] + v[0], p2[1] + v[1])
            if target[0] >= 0 and target[1] >= 0 and target[0] < len(grid[0]) and target[1] < len(grid):
                antinodes.add(target)
print(len(antinodes))
# Part 2
antinodes = set()
for key in towers:
    for p1 in towers[key]:
        for p2 in towers[key]:
            if p1 == p2:
                continue
            antinodes.add(p1)
            antinodes.add(p2)
            v = (p2[0] - p1[0], p2[1] - p1[1])
            target = (p2[0] + v[0], p2[1] + v[1])
            while target[0] >= 0 and target[1] >= 0 and target[0] < len(grid[0]) and target[1] < len(grid):
                antinodes.add(target)
                target = (target[0] + v[0], target[1] + v[1])
print(len(antinodes))
