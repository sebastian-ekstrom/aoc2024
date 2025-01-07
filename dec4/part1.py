import sys

def is_outside_grid(grid, x, y):
    return y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y])

def find_string(grid, x, y, offset_x, offset_y, target):
    for n in range(1, len(target)):
        x2 = x + n * offset_x
        y2 = y + n * offset_y
        if is_outside_grid(grid, x2, y2):
            return False
        if grid[y2][x2] != target[n]:
            return False
    return True

filename = sys.argv[1]
with open(filename) as file:
    grid = [line.strip() for line in file]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != "X":
            continue
        for offset_x, offset_y in directions:
            if find_string(grid, x, y, offset_x, offset_y, "XMAS"):
                total += 1
print(total)
