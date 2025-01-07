import sys
from collections import deque

debug = False

def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def print_grid(grid, boxes, x, y):
    if not debug:
        return
    for y2 in range(len(grid)):
        string = ""
        for x2 in range(len(grid[y2])):
            if y == y2 and x == x2:
                string += "@"
            elif (x2, y2) in boxes:
                string += "["
            elif (x2 - 1, y2) in boxes:
                string += "]"
            else:
                string += grid[y2][x2]
        print(string)
    # ~ input()

def try_push(grid, boxes, x, y, dx, dy):
    boxes_to_move = set()
    boxes_to_check = deque()
    x2 = x + dx
    y2 = y + dy
    if (x2, y2) in boxes:
        boxes_to_check.append((x2, y2))
    elif (x2 - 1, y2) in boxes:
        boxes_to_check.append((x2 - 1, y2))

    while len(boxes_to_check) > 0:
        bx, by = boxes_to_check.popleft()
        printd(f"try to push box at {(bx, by)}")
        if dx == -1:
            if grid[by][bx - 1] == "#":
                printd(f"blocked by wall at {(bx - 1, by)}")
                return (False, [])
            boxes_to_move.add((bx, by))
            if (bx - 2, by) in boxes:
                printd(f"blocked by box at {(bx - 2, by)}")
                boxes_to_check.append((bx - 2, by))
        elif dx == 1:
            if grid[by][bx + 2] == "#":
                printd(f"blocked by wall at {(bx + 2, by)}")
                return (False, [])
            boxes_to_move.add((bx, by))
            if (bx + 2, by) in boxes:
                printd(f"blocked by box at {(bx + 2, by)}")
                boxes_to_check.append((bx + 2, by))
        else:
            if grid[by + dy][bx] == "#":
                printd(f"blocked by wall at {(bx, by + dy)}")
                return (False, [])
            if grid[by + dy][bx + 1] == "#":
                printd(f"blocked by wall at {(bx + 1, by + dy)}")
                return (False, [])
            boxes_to_move.add((bx, by))
            if (bx - 1, by + dy) in boxes:
                printd(f"blocked by box at {(bx - 1, by + dy)}")
                boxes_to_check.append((bx - 1, by + dy))
            if (bx, by + dy) in boxes:
                printd(f"blocked by box at {(bx, by + dy)}")
                boxes_to_check.append((bx, by + dy))
            if (bx + 1, by + dy) in boxes:
                printd(f"blocked by box at {(bx + 1, by + dy)}")
                boxes_to_check.append((bx + 1, by + dy))
    return (True, boxes_to_move)

def try_move(grid, boxes, x, y, move):
    offsets = {"^": (0, -1), "<": (-1, 0), ">": (1, 0), "v": (0, 1)}
    dx, dy = offsets[move]
    x2 = x + dx
    y2 = y + dy
    # wall, don't move bot
    if grid[y2][x2] == "#":
        return (x, y)
    if (x2, y2) in boxes or (x2 - 1, y2) in boxes:
        pushable, boxes_to_move = try_push(grid, boxes, x, y, dx, dy)
        if pushable:
            for bx, by in boxes_to_move:
                box_id = boxes.index((bx, by))
                printd(f"Move box from {(bx, by)} to {(bx + dx, by + dy)}")
                boxes[box_id] = (bx + dx, by + dy)
            return (x2, y2)
        return (x, y)
    return (x2, y2)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

grid = []
boxes = []
i = 0
for i in range(len(lines)):
    if len(lines[i]) == 0:
        break
    lines[i] = lines[i].replace("#", "##")
    lines[i] = lines[i].replace(".", "..")
    lines[i] = lines[i].replace("O", "O.")
    lines[i] = lines[i].replace("@", "@.")
    grid.append([c for c in lines[i]])
    for x2 in range(len(lines[i])):
        if lines[i][x2] == "@":
            y = i
            x = x2
            grid[i][x2] = "."
        elif lines[i][x2] == "O":
            boxes.append((x2, i))
            grid[i][x2] = "."

instructions = ""
for j in range(i, len(lines)):
    instructions += lines[j]

for move in instructions:
    printd(move)
    x, y = try_move(grid, boxes, x, y, move)
    print_grid(grid, boxes, x, y)

total = 0
for bx, by in boxes:
    total += bx + by * 100
print(total)
