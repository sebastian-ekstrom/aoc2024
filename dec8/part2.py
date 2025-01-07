import sys
from collections import defaultdict
from math import gcd

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
            divisor = gcd(dx, dy)
            dx //= divisor
            dy //= divisor
            printd(f"dx = {dx}, dy = {dy}")
            x = x1
            y = y1
            while in_bounds(width, height, x, y):
                printd(f"antinode at {x, y}")
                antinodes.add((x, y))
                x -= dx
                y -= dy
            x = x2
            y = y2
            while in_bounds(width, height, x, y):
                printd(f"antinode at {x, y}")
                antinodes.add((x, y))
                x += dx
                y += dy
print(len(antinodes))
