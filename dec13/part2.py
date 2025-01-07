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
    xp = int(tokens_3[1][2:-1]) + 10000000000000
    yp = int(tokens_3[2][2:]) + 10000000000000

    if x1 * y2 != x2 * y1:
        if (xp * y2 - x2 * yp) % (x1 * y2 - x2 * y1) != 0:
            continue
        if (xp * y1 - x1 * yp) % (x2 * y1 - x1 * y2) != 0:
            continue
        n1 = (xp * y2 - x2 * yp) // (x1 * y2 - x2 * y1)
        n2 = (xp * y1 - x1 * yp) // (x2 * y1 - x1 * y2)
        total += n1 * 3 + n2
    else:
        print("maybe infinite solutions")

print(total)

