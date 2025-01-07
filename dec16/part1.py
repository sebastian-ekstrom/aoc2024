import sys
from heapq import *

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    grid = [[c for c in line.strip()] for line in file]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            x0 = x
            y0 = y
        elif grid[y][x] == "E":
            xe = x
            ye = y

positions = []
heappush(positions, (0, x0, y0, EAST))
visited = set()

while True:
    score, x, y, facing = heappop(positions)
    if x == xe and y == ye:
        print(score)
        break
    if (x, y, facing) in visited:
        continue
    visited.add((x, y, facing))
    dx, dy = offsets[facing]
    if grid[y + dy][x + dx] != "#":
        heappush(positions, (score + 1, x + dx, y + dy, facing))
    heappush(positions, (score + 1000, x, y, (facing + 1) % 4))
    heappush(positions, (score + 1000, x, y, (facing - 1) % 4))

