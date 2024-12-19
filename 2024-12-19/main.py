with open('input.txt', 'r', encoding='utf-8') as f:
    towels = f.readline().strip().split(', ')
    f.readline()
    patterns = [x.strip() for x in f.readlines()]

# 6, 16
# towels = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
# patterns = ['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb']

min_k = min([len(x) for x in towels])
max_k = max([len(x) for x in towels])

result1 = 0
result2 = 0
for i in range(len(patterns)):
    print(i + 1, '/', len(patterns))
    pattern = patterns[i]
    kmers = set()
    for k in range(min_k, max_k + 1):
        for j in range(0, len(pattern) - k + 1):
            kmer = pattern[j:j + k]
            if kmer in towels:
                kmers.add(kmer)
    lookup = [[len(kmer) for kmer in kmers if pattern[i:].startswith(kmer)] for i in range(0, len(pattern))]
    changed = True
    while changed:
        changed = False
        for j in range(0, len(pattern)):
            for k in range(len(lookup[j]) - 1, -1, -1):
                next_index = j + lookup[j][k]
                if next_index < len(pattern) and len(lookup[next_index]) == 0:
                    del lookup[j][k]
                    changed = True
    lookup_paths = [0] * (len(lookup) + 1)
    lookup_paths[0] = 1
    for j in range(0, len(lookup)):
        for k in lookup[j]:
            lookup_paths[j + k] += lookup_paths[j]
    if lookup_paths[-1] > 0:
        result1 += 1
    result2 += lookup_paths[-1]
print(result1, result2)
# 306, 604622004681855
