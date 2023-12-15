def hash_string(text):
    result = 0
    for i in range(0, len(text)):
        result += ord(text[i])
        result *= 17
        result %= 256
    return result


def hash_list(text):
    return sum([hash_string(x) for x in text.split(',')])


print(hash_string('HASH'))
print(hash_list('rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'))
with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    print(hash_list(lines[0]))
