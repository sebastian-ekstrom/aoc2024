import sys

def printd(*args, **kwargs):
    debug = True
    if debug:
        print(*args, **kwargs)

def in_bounds(width, height, x, y):
    return x >= 0 and x < width and y >= 0 and y < height

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

obstacles = set()
visited = set()
height = len(grid)
width = len(grid[0])
for y in range(height):
    for x in range(width):
        if grid[y][x] == "#":
            obstacles.add((x, y))
        elif grid[y][x] == "^":
            x_pos = x
            y_pos = y
facing = NORTH

while in_bounds(width, height, x_pos, y_pos):
    visited.add((x_pos, y_pos))
    move_x, move_y = moves[facing]
    if (x_pos + move_x, y_pos + move_y) in obstacles:
        facing = (facing + 1) % 4
    else:
        x_pos += move_x
        y_pos += move_y

print(len(visited))
