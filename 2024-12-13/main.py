with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    # lines = [
    #     'Button A: X+94, Y+34',
    #     'Button B: X+22, Y+67',
    #     'Prize: X=8400, Y=5400',
    #     '',
    #     'Button A: X+26, Y+66',
    #     'Button B: X+67, Y+21',
    #     'Prize: X=12748, Y=12176',
    #     '',
    #     'Button A: X+17, Y+86',
    #     'Button B: X+84, Y+37',
    #     'Prize: X=7870, Y=6450',
    #     '',
    #     'Button A: X+69, Y+23',
    #     'Button B: X+27, Y+71',
    #     'Prize: X=18641, Y=10279'
    # ]
    result = 0
    result2 = 0
    for i in range(0, len(lines), 4):
        a = lines[i].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')
        b = lines[i + 1].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')
        p = lines[i + 2].split(': ')[1].replace('X=', '').replace('Y=', '').split(', ')
        ax = int(a[0])
        ay = int(a[1])
        bx = int(b[0])
        by = int(b[1])
        px = int(p[0]) + 10000000000000
        py = int(p[1]) + 10000000000000
        # px = j * bx + k * ax
        # py = j * by + k * ay
        # k = (-py * bx + px * by) / (ax * by - ay * bx)
        k = (-py * bx + px * by) / (ax * by - ay * bx)
        j = (px - k * ax) / bx
        if k == int(k) and j == int(j):
            # print('-', j, k, j + k * 3)
            result2 += int(j + k * 3)
        # for j in range(int(px / bx), -1, -1):
        #     bxi = bx * j
        #     rest = px - bxi
        #     if rest % ax == 0:
        #         k = int(rest / ax)
        #         if py - by * j == k * ay:
        #             min_tokens = j + k * 3
        #             # print('', int(i / 4), j, k, j + k * 3)
        #             result += min_tokens
print(result, result2)
