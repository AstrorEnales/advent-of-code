def reduce_possibility_space(ranges, possible_placements):
    result = [[y for y in x] for x in possible_placements]
    changed = True
    while changed:
        changed = False
        for i in range(0, len(result)):
            if len(result[i]) == 1:
                for j in range(0, i):
                    new_placements = [x for x in result[j] if x < result[i][0] - 1]
                    if len(new_placements) != len(result[j]):
                        changed = True
                    result[j] = new_placements
                for k in range(i + 1, len(result)):
                    new_placements = [x for x in result[k] if x > result[i][0] + ranges[i]]
                    if len(new_placements) != len(result[k]):
                        changed = True
                    result[k] = new_placements
    return result


def recurse_solutions(springs, ranges, possible_placements, counter):
    new_possible_placements = reduce_possibility_space(ranges, possible_placements)
    if any([len(x) == 0 for x in new_possible_placements]):
        return
    next_choice_index = -1
    for i in range(0, len(new_possible_placements)):
        if len(new_possible_placements[i]) > 1:
            next_choice_index = i
            break
    if next_choice_index == -1:
        # Check if the solution is valid and no extra # exist
        solution_test = springs
        for i in range(len(ranges) - 1, -1, -1):
            solution_test = solution_test[:new_possible_placements[i][0]] + solution_test[new_possible_placements[i][0] + ranges[i]:]
        if any([x == '#' for x in solution_test]):
            return
        counter[0] += 1
        counter.append([x[0] for x in new_possible_placements])
    else:
        for i in range(0, len(new_possible_placements[next_choice_index])):
            recurse_solutions(springs,
                              ranges,
                              new_possible_placements[:next_choice_index] +
                              [[new_possible_placements[next_choice_index][i]]] +
                              new_possible_placements[next_choice_index + 1:],
                              counter)


def get_possible_solution_count(line):
    springs, numbers = line.split(' ')
    broken_ranges = list(map(int, numbers.split(',')))
    possible_placements = []
    for r in broken_ranges:
        possible_placements.append([])
        for i in range(0, len(springs) + 1 - r):
            matches = True
            if springs[i] == '.':
                matches = False
            # if preceded by a # this place is not possible
            elif i > 0 and springs[i - 1] == '#':
                matches = False
            # if followed by a # this place is not possible
            elif i < len(springs) - r and springs[i + r] == '#':
                matches = False
            else:
                for j in range(0, r):
                    if springs[i + j] not in {'?', '#'}:
                        matches = False
            if matches:
                possible_placements[-1].append(i)
    possible_placements = reduce_possibility_space(broken_ranges, possible_placements)
    counter = [0]
    for i in range(0, len(possible_placements[0])):
        recurse_solutions(springs, broken_ranges, [[possible_placements[0][i]]] + possible_placements[1:], counter)
    return counter[0]


test_lines = [
    '???.### 1,1,3',
    '.??..??...?##. 1,1,3',
    '?#?#?#?#?#?#?#? 1,3,1,6',
    '????.#...#... 4,1,1',
    '????.######..#####. 1,6,5',
    '?###???????? 3,2,1'
]
print(sum([get_possible_solution_count(x) for x in test_lines]))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    print(sum([get_possible_solution_count(x) for x in lines]))
