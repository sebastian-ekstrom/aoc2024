import sys

def is_outside_grid(grid, x, y):
    return y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y])

def check_cross(grid, x, y, cross_offsets):
    # ~ print("debug1", x, y)
    for line in cross_offsets:
        # ~ print("debug2", line[0], line[1])
        x2 = x + line[0][0]
        y2 = y + line[0][1]
        x3 = x + line[1][0]
        y3 = y + line[1][1]
        if is_outside_grid(grid, x2, y2) or is_outside_grid(grid, x3, y3):
            return False
        letters = (grid[y2][x2], grid[y3][x3])
        # ~ print("debug3", letters)
        if "M" not in letters or "S" not in letters:
            return False
    # ~ print("debug1", x, y)
    # ~ for y2 in range(y-1, y+2):
        # ~ print("".join([grid[y2][x2] for x2 in range(x-1, x+2)]))
    return True

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

cross_offsets = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != "A":
            continue
        if check_cross(grid, x, y, cross_offsets):
            total += 1
print(total)
