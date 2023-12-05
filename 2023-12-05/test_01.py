def map_from_to(maps, from_key, to_key, _id):
    ranges = maps[from_key][to_key]
    for r in ranges:
        if r[0] <= _id <= r[1]:
            return r[2] + (_id - r[0])
    return _id


def find_lowest_location_number(lines) -> int:
    seeds = set()
    last_source = ''
    last_dest = ''
    maps = {}
    for line in lines:
        if len(line) == 0:
            continue
        if line.startswith('seeds: '):
            seeds.update([int(x.strip()) for x in line.split(':')[1].split(' ') if len(x.strip()) > 0])
        elif ':' in line:
            last_source, _, last_dest = line.split(' ')[0].split('-')
            if last_source not in maps:
                maps[last_source] = {}
            if last_source not in maps[last_source]:
                maps[last_source][last_dest] = []
        elif last_source != '' and last_dest != '':
            m = maps[last_source][last_dest]
            dest_start, source_start, count = [int(x) for x in line.split(' ', 3)]
            m.append([source_start, source_start + count - 1, dest_start, dest_start + count - 1])
    locations = set()
    for seed in seeds:
        soil = map_from_to(maps, 'seed', 'soil', seed)
        fertilizer = map_from_to(maps, 'soil', 'fertilizer', soil)
        water = map_from_to(maps, 'fertilizer', 'water', fertilizer)
        light = map_from_to(maps, 'water', 'light', water)
        temperature = map_from_to(maps, 'light', 'temperature', light)
        humidity = map_from_to(maps, 'temperature', 'humidity', temperature)
        location = map_from_to(maps, 'humidity', 'location', humidity)
        print(seed, soil, fertilizer, water, light, temperature, humidity, location)
        locations.add(location)
    return min(locations)


test_lines = [
    'seeds: 79 14 55 13',
    'seed-to-soil map:',
    '50 98 2',
    '52 50 48',
    'soil-to-fertilizer map:',
    '0 15 37',
    '37 52 2',
    '39 0 15',
    'fertilizer-to-water map:',
    '49 53 8',
    '0 11 42',
    '42 0 7',
    '57 7 4',
    'water-to-light map:',
    '88 18 7',
    '18 25 70',
    'light-to-temperature map:',
    '45 77 23',
    '81 45 19',
    '68 64 13',
    'temperature-to-humidity map:',
    '0 69 1',
    '1 0 69',
    'humidity-to-location map:',
    '60 56 37',
    '56 93 4'
]

print(find_lowest_location_number(test_lines))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    print(find_lowest_location_number(lines))