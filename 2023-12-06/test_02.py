import re

pattern = re.compile(r'[0-9\s]+')


def find_race_solutions(time, distance):
    possible_race_distances = [pressed_time * (time - pressed_time) for pressed_time in range(0, time + 1)]
    new_record_distances = [x for x in possible_race_distances if x > distance]
    print('Race', time, distance, 'possibilities', len(new_record_distances))


find_race_solutions(71530, 940200)
with open('input_01.txt', 'r', encoding='utf-8') as f:
    time = int(pattern.findall(f.readline())[0].replace(' ', ''))
    distance = int(pattern.findall(f.readline())[0].replace(' ', ''))
    find_race_solutions(time, distance)
