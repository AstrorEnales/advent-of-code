import re

allowed = {'red': 12, 'green': 13, 'blue': 14}
pattern = re.compile(r'([0-9]+)\s+(red|green|blue)')


def sum_of_valid_game_ids(lines) -> int:
    result = 0
    for line in lines:
        game, reveals = line.split(': ')
        game_id = int(game.split(' ')[-1])
        valid = True
        for reveal in pattern.findall(reveals):
            if int(reveal[0]) > allowed[reveal[1]]:
                valid = False
                break
        if valid:
            result += game_id
    return result


test_games = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]
print(sum_of_valid_game_ids(test_games))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    print(sum_of_valid_game_ids(f.readlines()))
