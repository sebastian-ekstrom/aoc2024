import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

keys = []
locks = []
for i in range((len(lines) + 1) // 8):
    schematic = lines[i * 8:i * 8 + 7]
    heights = [0, 0, 0, 0, 0]
    if schematic[0][0] == "#":
        for x in range(5):
            for y in range(7):
                if schematic[y][x] == "#":
                    heights[x] = y
        locks.append(heights)
    else:
        for x in range(5):
            for y in range(7):
                if schematic[6-y][x] == "#":
                    heights[x] = y
        keys.append(heights)

total = 0
for key in keys:
    for lock in locks:
        fit = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                fit = False
                break
        if fit:
            total += 1
print(total)
