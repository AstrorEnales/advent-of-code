with open('input.txt', 'r', encoding='utf-8') as f:
    grid = [[int(y) for y in x.strip()] for x in f]


def traverse(pos, heads):
    value = grid[pos[1]][pos[0]]
    if value == 9:
        heads.append(pos)
    else:
        if pos[0] > 0 and grid[pos[1]][pos[0] - 1] == value + 1:
            traverse((pos[0] - 1, pos[1]), heads)
        if pos[0] < len(grid[0]) - 1 and grid[pos[1]][pos[0] + 1] == value + 1:
            traverse((pos[0] + 1, pos[1]), heads)

        if pos[1] > 0 and grid[pos[1] - 1][pos[0]] == value + 1:
            traverse((pos[0], pos[1] - 1), heads)
        if pos[1] < len(grid) - 1 and grid[pos[1] + 1][pos[0]] == value + 1:
            traverse((pos[0], pos[1] + 1), heads)

result = 0
ratings_result = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if grid[y][x] == 0:
            heads = []
            traverse((x, y), heads)
            result += len(set(heads))
            ratings_result += len(heads)
print(result)
print(ratings_result)
