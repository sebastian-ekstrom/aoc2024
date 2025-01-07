import sys

debug = False

def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def print_grid(grid, x, y):
    if not debug:
        return
    for y2 in range(len(grid)):
        string = ""
        for x2 in range(len(grid[y2])):
            if y == y2 and x == x2:
                string += "@"
            else:
                string += grid[y2][x2]
        print(string)
    print("")

def try_move(grid, x, y, move):
    offsets = {"^": (0, -1), "<": (-1, 0), ">": (1, 0), "v": (0, 1)}
    dx, dy = offsets[move]
    x2 = x + dx
    y2 = y + dy
    # wall, don't move bot
    if grid[y2][x2] == "#":
        return (x, y)
    # empty, move bot
    if grid[y2][x2] == ".":
        return (x2, y2)
    # pushable box, bot can maybe move
    printd(f"try to move box on {(x2, y2)}")
    x3 = x2 + dx
    y3 = y2 + dy
    while grid[y3][x3] == "O":
        x3 += dx
        y3 += dy
    # box(es) would be pushed into wall, don't move bot
    if grid[y3][x3] == "#":
        return (x, y)
    # box(es) would be pushed into empty space, move box(es) and bot
    grid[y3][x3] = "O"
    grid[y2][x2] = "."
    printd(f"move box from {(x2, y2)} to {(x3, y3)}")
    return (x2, y2)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

grid = []
i = 0
for i in range(len(lines)):
    if len(lines[i]) == 0:
        break
    grid.append([c for c in lines[i]])
    if "@" in lines[i]:
        y = i
        x = lines[i].find("@")
        grid[y][x] = "."

instructions = ""
for j in range(i, len(lines)):
    instructions += lines[j]

for move in instructions:
    x, y = try_move(grid, x, y, move)
    print_grid(grid, x, y)

total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "O":
            total += 100 * y + x
print(total)
