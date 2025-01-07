import sys

def printd(*args, **kwargs):
    debug = True
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

area_counts = [0, 0, 0, 0]
w = 101
h = 103
t = 100
for line in lines:
    tokens = line.split()
    x0, y0 = [int(i) for i in tokens[0][2:].split(",")]
    vx, vy = [int(i) for i in tokens[1][2:].split(",")]
    x = (x0 + vx * t) % w
    y = (y0 + vy * t) % h
    mid_x = w // 2
    mid_y = h // 2
    if x < mid_x and y < mid_y:
        area_counts[0] += 1
    elif x > mid_x and y < mid_y:
        area_counts[1] += 1
    elif x < mid_x and y > mid_y:
        area_counts[2] += 1
    elif x > mid_x and y > mid_y:
        area_counts[3] += 1

print(area_counts[0] * area_counts[1] * area_counts[2] * area_counts[3])
