import sys

def printd(*args, **kwargs):
    debug = True
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

total = 0
for i in range(0, len(lines), 4):
    tokens_1 = lines[i].split()
    x1 = int(tokens_1[2][2:-1])
    y1 = int(tokens_1[3][2:])
    tokens_2 = lines[i+1].split()
    x2 = int(tokens_2[2][2:-1])
    y2 = int(tokens_2[3][2:])
    tokens_3 = lines[i+2].split()
    xp = int(tokens_3[1][2:-1])
    yp = int(tokens_3[2][2:])

    min_cost = 1e20
    for a in range(100):
        for b in range(100):
            if a * x1 + b * x2 == xp and a * y1 + b * y2 == yp:
                cost = a * 3 + b
                min_cost = min(cost, min_cost)
    if min_cost < 1e20:
        total += min_cost

print(total)

