import sys
from collections import defaultdict

def printd(*args, **kwargs):
    debug = False
    if debug:
        print(*args, **kwargs)

def in_bounds(width, height, x, y):
    return x >= 0 and x < width and y >= 0 and y < height

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

antennas = defaultdict(list)

height = len(grid)
width = len(grid[0])

for y in range(height):
    for x in range(width):
        if grid[y][x] != ".":
            antennas[grid[y][x]].append((x, y))

printd(f"grid size: {width}x{height}")
antinodes = set()
for freq, positions in antennas.items():
    printd(f"freq = {freq}")
    for i in range(len(positions) - 1):
        x1, y1 = positions[i]
        for j in range(i + 1, len(positions)):
            x2, y2 = positions[j]
            printd(f"positions: {(x1, y1), (x2, y2)}")
            dx = x2 - x1
            dy = y2 - y1
            x3 = x1 - dx
            y3 = y1 - dy
            if in_bounds(width, height, x3, y3):
                printd(f"antinode at {(x3, y3)}")
                antinodes.add((x3, y3))
            x4 = x2 + dx
            y4 = y2 + dy
            if in_bounds(width, height, x4, y4):
                printd(f"antinode at {(x4, y4)}")
                antinodes.add((x4, y4))
print(len(antinodes))
