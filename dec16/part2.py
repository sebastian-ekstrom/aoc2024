import sys
from heapq import *
from collections import defaultdict, deque

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
heappush(positions, (0, x0, y0, EAST, -1, -1, -1))
best_scores = {}
predecessors = defaultdict(list)

min_score = 1e20
while True:
    score, x, y, facing, xprev, yprev, fprev = heappop(positions)
    if score > min_score:
        break
    if (x, y, facing) in best_scores:
        if score == best_scores[(x, y, facing)]:
            predecessors[(x, y, facing)].append((xprev, yprev, fprev))
        continue
    best_scores[(x, y, facing)] = score
    predecessors[(x, y, facing)].append((xprev, yprev, fprev))
    if x == xe and y == ye:
        min_score = score
        end_facing = facing
        continue
    dx, dy = offsets[facing]
    if grid[y + dy][x + dx] != "#":
        heappush(positions, (score + 1, x + dx, y + dy, facing, x, y, facing))
    heappush(positions, (score + 1000, x, y, (facing + 1) % 4, x, y, facing))
    heappush(positions, (score + 1000, x, y, (facing - 1) % 4, x, y, facing))

positions = deque([(xe, ye, end_facing)])
visited = set()
while len(positions) > 0:
    x, y, facing = positions.popleft()
    visited.add((x, y))
    if x == x0 and y == y0:
        continue
    for x2, y2, f2 in predecessors[(x, y, facing)]:
        positions.append((x2, y2, f2))
print(len(visited))
