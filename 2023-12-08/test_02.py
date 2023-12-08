import functools


def find_period(instructions, nodes, key):
    current = key
    counter = 0
    found = False
    while not found:
        direction = instructions[counter % len(instructions)]
        current = nodes[current][0 if direction == 'L' else 1]
        counter += 1
        found = current == key
    return counter


def find_first_end(instructions, nodes, key):
    current = key
    counter = 0
    while current[2] != 'Z':
        direction = instructions[counter % len(instructions)]
        current = nodes[current][0 if direction == 'L' else 1]
        counter += 1
    return [counter, current]


def ggt(numbers):
    for i in range(0, len(numbers) - 1):
        while numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0] % numbers[1]
        numbers[1] = numbers[i + 1]

    return numbers[0]


def kgv(numbers):
    return functools.reduce(lambda a, b: a * b // ggt([a, b]), numbers)

def traverse_instructions(instructions, nodes):
    end_nodes = [x for x in nodes.keys() if x[2] == 'Z']
    end_node_periods = {x: find_period(instructions, nodes, x) for x in end_nodes}
    start_nodes = [[x] + find_first_end(instructions, nodes, x) for x in nodes.keys() if x[2] == 'A']
    print(end_node_periods)
    print(start_nodes)
    # As the counter to the first end of each start is equal to the end's period, we can simply use the kgv
    print(kgv(end_node_periods.values()))
    #while len({x[1] for x in start_nodes}) != 1:
    #    max_counter = max([x[1] for x in start_nodes])
    #    for i in range(0, len(start_nodes)):
    #        if start_nodes[i][1] < max_counter:
    #            start_nodes[i][1] += end_node_periods[start_nodes[i][2]]
    #print(start_nodes[0][1])


instructions = 'LR'
nodes = {
    '11A': ('11B', 'XXX'),
    '11B': ('XXX', '11Z'),
    '11Z': ('11B', 'XXX'),
    '22A': ('22B', 'XXX'),
    '22B': ('22C', '22C'),
    '22C': ('22Z', '22Z'),
    '22Z': ('22B', '22B'),
    'XXX': ('XXX', 'XXX')
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
