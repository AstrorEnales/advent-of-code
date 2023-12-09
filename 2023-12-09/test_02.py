def extrapolate_back(sequence) -> int:
    sequences = [sequence]
    while not all([x == 0 for x in sequences[-1]]):
        next_sequence = [sequences[-1][i + 1] - sequences[-1][i] for i in range(0, len(sequences[-1]) - 1)]
        sequences.append(next_sequence)
    sequences[-1].insert(0, 0)
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])
    return sequences[0][0]


test_sequences = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]
]

print(sum([extrapolate_back(sequence) for sequence in test_sequences]))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    sequences = [[int(y) for y in x.strip().split(' ')] for x in f.readlines()]
    print(sum([extrapolate_back(sequence) for sequence in sequences]))
