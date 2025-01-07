import sys
from collections import defaultdict

def printd(*args, **kwargs):
    debug = True
    if debug:
        print(*args, **kwargs)

def in_bounds(width, height, x, y):
    return x >= 0 and x < width and y >= 0 and y < height

filename = sys.argv[1]
with open(filename) as file:
    grid = [[int(c) for c in line.strip()] for line in file]

height = len(grid)
width = len(grid[0])

paths = defaultdict(list)
trailheads = []

for y in range(height):
    for x in range(width):
        if grid[y][x] == 0:
            trailheads.append((x, y))
        if grid[y][x] < 9:
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                x2 = x + dx
                y2 = y + dy
                if in_bounds(width, height, x2, y2) and grid[y2][x2] - grid[y][x] == 1:
                    paths[(x, y)].append((x2, y2))

total = 0
for start_x, start_y in trailheads:
    positions = [(start_x, start_y)]
    while len(positions) > 0:
        next_positions = []
        for x, y in positions:
            if grid[y][x] == 9:
                total += 1
                continue
            for x2, y2 in paths[(x, y)]:
                next_positions.append((x2, y2))
        positions = next_positions

print(total)

