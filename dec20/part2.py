import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def find_tiles_within_distance(x, y, d):
    for dy in range(-d, d+1):
        for dx in range(abs(dy)-d, d-abs(dy)+1):
            yield (x+dx, y+dy)

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

for y in range(len(grid)):
    x = grid[y].find("S")
    if x >= 0:
        x0 = x
        y0 = y
    x = grid[y].find("E")
    if x >= 0:
        xe = x
        ye = y

t = 0
x = x0
y = y0
xprev = x0
yprev = y0
times = {}

while True:
    times[(x, y)] = t
    if x == xe and y == ye:
        break
    for x2, y2 in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
        if grid[y2][x2] != "#" and (x2 != xprev or y2 != yprev):
            xprev = x
            yprev = y
            x = x2
            y = y2
            break
    t += 1

total = 0
for x, y in times:
    for x2, y2 in find_tiles_within_distance(x, y, 20):
        d = abs(x2-x) + abs(y2-y)
        if (x2, y2) in times and times[(x2, y2)] - times[(x, y)] >= 100 + d:
            total += 1
print(total)
