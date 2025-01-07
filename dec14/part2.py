import sys

def printd(*args, **kwargs):
    debug = True
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

area_counts = [0, 0, 0, 0]
robots = []
w = 101
h = 103
for line in lines:
    tokens = line.split()
    x0, y0 = [int(i) for i in tokens[0][2:].split(",")]
    vx, vy = [int(i) for i in tokens[1][2:].split(",")]
    robots.append((x0, y0, vx, vy))

x_gather_1 = 27
x_gather_2 = 128
y_gather_1 = 75
y_gather_2 = 178
x_period = x_gather_2 - x_gather_1
y_period = y_gather_2 - y_gather_1
t = 0
while t % x_period != x_gather_1 or t % y_period != y_gather_1:
    t += 1

positions = [((x0 + t * vx) % w, (y0 + t * vy) % h) for x0, y0, vx, vy in robots]
while True:
    print(f"t = {t}")
    for y in range(h):
        string = ""
        for x in range(w):
            if (x, y) in positions:
                string += "#"
            else:
                string += " "
        print(string)
    input()

    t += 1
    for i in range(len(robots)):
        x, y = positions[i]
        positions[i] = ((x + robots[i][2]) % w, (y + robots[i][3]) % h)

