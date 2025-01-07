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
height = len(grid)
width = len(grid[0])
for y in range(height):
    for x in range(width):
        if grid[y][x] == "#":
            obstacles.add((x, y))
        elif grid[y][x] == "^":
            start_x = x
            start_y = y
facing = NORTH

x_pos = start_x
y_pos = start_y
original_path = set()
while in_bounds(width, height, x_pos, y_pos):
    original_path.add((x_pos, y_pos))
    move_x, move_y = moves[facing]
    if (x_pos + move_x, y_pos + move_y) in obstacles:
        facing = (facing + 1) % 4
    else:
        x_pos += move_x
        y_pos += move_y

total = 0
for obstacle_x, obstacle_y in original_path:
    if obstacle_x == start_x and obstacle_y == start_y:
        continue
    x_pos = start_x
    y_pos = start_y
    facing = NORTH
    visited = set()
    loop = False
    while in_bounds(width, height, x_pos, y_pos):
        if (x_pos, y_pos, facing) in visited:
            loop = True
            break
        visited.add((x_pos, y_pos, facing))
        move_x, move_y = moves[facing]
        if (x_pos + move_x, y_pos + move_y) in obstacles or (x_pos + move_x == obstacle_x and y_pos + move_y == obstacle_y):
            facing = (facing + 1) % 4
        else:
            x_pos += move_x
            y_pos += move_y
    if loop:
        total += 1
print(total)
