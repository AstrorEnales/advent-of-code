def hash_string(text):
    result = 0
    for i in range(0, len(text)):
        result += ord(text[i])
        result *= 17
        result %= 256
    return result


def process_operation(output, operation: str):
    if '-' in operation:
        label, value = operation.split('-')
        label_hash = hash_string(label)
        for i in range(len(output[label_hash]) - 1, -1, -1):
            if output[label_hash][i][0] == label:
                del output[label_hash][i]
    else:
        label, value = operation.split('=')
        label_hash = hash_string(label)
        replaced = False
        for i in range(len(output[label_hash]) - 1, -1, -1):
            if output[label_hash][i][0] == label:
                replaced = True
                output[label_hash][i][1] = int(value)
                break
        if not replaced:
            output[label_hash].append([label, int(value)])


def hashmap(text):
    result = [[] for _ in range(0, 256)]
    for operation in text.split(','):
        process_operation(result, operation)
    return result


def calculate_focal_power(output):
    result = 0
    for i in range(0, len(output)):
        for j, lens in enumerate(output[i]):
            result += (i + 1) * (j + 1) * lens[1]
    return result


print(calculate_focal_power(hashmap('rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7')))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    print(calculate_focal_power(hashmap(lines[0])))
