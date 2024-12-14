from PIL import Image

robots = []
with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    #lines = [
    #    'p=0,4 v=3,-3',
    #    'p=6,3 v=-1,-3',
    #    'p=10,3 v=-1,2',
    #    'p=2,0 v=2,-1',
    #    'p=0,0 v=1,3',
    #    'p=3,0 v=-2,-2',
    #    'p=7,6 v=-1,-3',
    #    'p=3,0 v=-1,-2',
    #    'p=9,3 v=2,3',
    #    'p=7,3 v=-1,2',
    #    'p=2,4 v=2,-3',
    #    'p=9,5 v=-3,-3'
    #]
    for row in lines:
        p, v = [[int(y) for y in x.split('=')[1].split(',')] for x in row.strip().split(' ')]
        robots.append([p, v])
width = 101
height = 103
#width = 11
#height = 7
center = [width // 2, height // 2]
for t in range(1, 7573):  # 101
    for robot in robots:
        robot[0][0] += robot[1][0]
        robot[0][1] += robot[1][1]
        while robot[0][0] < 0:
            robot[0][0] += width
        while robot[0][0] >= width:
            robot[0][0] -= width
        while robot[0][1] < 0:
            robot[0][1] += height
        while robot[0][1] >= height:
            robot[0][1] -= height
    if t == 7572:
        data = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]
        img = Image.new('RGB', (width, height))
        for robot in robots:
            img.putpixel(tuple(robot[0]), (255, 255, 255))
        img.save('frame_%s.png' % t)

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
    if robot[0][0] < center[0]:
        if robot[0][1] < center[1]:
            q1 += 1
        elif robot[0][1] > center[1]:
            q3 += 1
    elif robot[0][0] > center[0]:
        if robot[0][1] < center[1]:
            q2 += 1
        elif robot[0][1] > center[1]:
            q4 += 1

print(q1 * q2 * q3 * q4)
