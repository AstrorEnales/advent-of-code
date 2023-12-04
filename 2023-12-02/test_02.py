import re

pattern = re.compile(r'([0-9]+)\s+(red|green|blue)')


def power_of_minimal_cubes(line: str) -> int:
    max_cubes = {'red': 0, 'green': 0, 'blue': 0}
    reveals = line.split(': ')[1]
    for reveal in pattern.findall(reveals):
        max_cubes[reveal[1]] = max(max_cubes[reveal[1]], int(reveal[0]))
    return max_cubes['red'] * max_cubes['green'] * max_cubes['blue']


test_games = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]
print(sum([power_of_minimal_cubes(x) for x in test_games]))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    print(sum([power_of_minimal_cubes(x) for x in f.readlines()]))
