import re
import operator
from functools import reduce

pattern = re.compile(r'[0-9]+')


def find_race_solutions(times, distances):
    possible_race_distances = [
        [pressed_time * (times[race_index] - pressed_time) for pressed_time in range(0, times[race_index] + 1)]
        for race_index in range(0, len(times))
    ]
    print('Race', times, distances)
    for x in possible_race_distances:
        print(x)
    new_record_distances = [
        [x for x in possible_race_distances[race_index] if x > distances[race_index]]
        for race_index in range(0, len(times))
    ]
    print('New records', new_record_distances)
    print('Result', reduce(operator.mul, [len(x) for x in new_record_distances], 1))

find_race_solutions([7, 15, 30], [9, 40, 200])
with open('input_01.txt', 'r', encoding='utf-8') as f:
    times = [int(x) for x in pattern.findall(f.readline())]
    distances = [int(x) for x in pattern.findall(f.readline())]
    find_race_solutions(times, distances)
