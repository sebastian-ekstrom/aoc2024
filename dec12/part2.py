import sys

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def printd(*args, **kwargs):
    debug = False
    if debug:
        print(*args, **kwargs)

def in_bounds(width, height, x, y):
    return x >= 0 and x < width and y >= 0 and y < height

def find_region(grid, x, y):
    offsets = [(0, -1, NORTH), (-1, 0, WEST), (1, 0, EAST), (0, 1, SOUTH)]

    height = len(grid)
    width = len(grid[0])
    name = grid[y][x]
    tiles = set()
    fences = []
    current_tiles = [(x, y)]

    while len(current_tiles) > 0:
        next_tiles = set()
        for x, y in current_tiles:
            tiles.add((x, y))
            for dx, dy, direction in offsets:
                x2 = x + dx
                y2 = y + dy
                if (x2, y2) in tiles:
                    continue
                if not in_bounds(width, height, x2, y2) or grid[y2][x2] != name:
                    fences.append((x, y, direction))
                    continue
                next_tiles.add((x2, y2))
        current_tiles = next_tiles

    fences.sort()
    sides = 0
    while len(fences) > 0:
        x, y, direction = fences[0]
        sides += 1
        if direction == NORTH or direction == SOUTH:
            dx = 1
            dy = 0
        else:
            dx = 0
            dy = 1
        n = 0
        while (x + n * dx, y + n * dy, direction) in fences:
            fences.remove((x + n * dx, y + n * dy, direction))
            n += 1


    printd(name, len(tiles), sides)
    return tiles, sides

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

total = 0
visited = set()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (x, y) in visited:
            continue
        tiles, sides = find_region(grid, x, y)
        total += len(tiles) * sides
        visited |= tiles

print(total)
