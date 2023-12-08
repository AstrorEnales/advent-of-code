def traverse_instructions(instructions, nodes):
    current = 'AAA'
    counter = 0
    while current != 'ZZZ':
        direction = instructions[counter % len(instructions)]
        current = nodes[current][0 if direction == 'L' else 1]
        counter += 1
    print(counter)


instructions = 'LLR'
nodes = {
    'AAA': ('BBB', 'BBB'),
    'BBB': ('AAA', 'ZZZ'),
    'ZZZ': ('ZZZ', 'ZZZ')
}
traverse_instructions(instructions, nodes)
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    instructions = lines[0]
    nodes = {}
    for line in lines[2:]:
        key, value = line.split(' = ', 2)
        moves = value.replace('(', '').replace(')', '').split(', ', 2)
        nodes[key] = (moves[0], moves[1])
    traverse_instructions(instructions, nodes)
