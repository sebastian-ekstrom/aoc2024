import sys

def printd(*args, **kwargs):
    debug = False
    if debug:
        print(*args, **kwargs)

def in_bounds(width, height, x, y):
    return x >= 0 and x < width and y >= 0 and y < height

def find_region(grid, x, y):
    offsets = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    height = len(grid)
    width = len(grid[0])
    name = grid[y][x]
    tiles = set()
    circumference = 0
    current_tiles = [(x, y)]

    while len(current_tiles) > 0:
        next_tiles = []
        for x, y in current_tiles:
            if (x, y) in tiles:
                continue
            if not in_bounds(width, height, x, y) or grid[y][x] != name:
                circumference += 1
                continue
            tiles.add((x, y))
            for dx, dy in offsets:
                next_tiles.append((x + dx, y + dy))
        current_tiles = next_tiles

    printd(name, len(tiles), circumference)
    return tiles, circumference

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

total = 0
visited = set()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (x, y) in visited:
            continue
        tiles, circumference = find_region(grid, x, y)
        total += len(tiles) * circumference
        visited |= tiles

print(total)
