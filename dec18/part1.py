import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def in_bounds(x, y, w, h):
    return x >= 0 and x < w and y >= 0 and y < h

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

# ~ coords = [(int(c) for c in line.split(",")) for line in lines]
coords = []
for line in lines:
    x, y = [int(c) for c in line.split(",")]
    coords.append((x, y))

if "example" in filename:
    blocks = set(coords[:12])
    w = 7
    h = 7
else:
    blocks = set(coords[:1024])
    w = 71
    h = 71
target_x = w - 1
target_y = h - 1

steps = -1
positions = {(0, 0)}
visited = set()

found = False
while not found:
    if len(positions) == 0:
        print("error: no path found")
        break
    steps += 1
    next_positions = set()
    for x, y in positions:
        visited.add((x, y))
        if x == target_x and y == target_y:
            found = True
            break
        for x2, y2 in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if in_bounds(x2, y2, w, h) and (x2, y2) not in visited and (x2, y2) not in blocks:
                next_positions.add((x2, y2))
    positions = next_positions
    if debug:
        print(positions, steps)
        input()
print(steps)
