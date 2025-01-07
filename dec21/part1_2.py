import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def expand(code, pad):
    grid = {}
    for y in range(len(pad)):
        for x in range(len(pad[y])):
            if pad[y][x] != " ":
                grid[pad[y][x]] = (x, y)
                if pad[y][x] == "A":
                    x0 = x
                    y0 = y
            else:
                x_bad = x
                y_bad = y

    string = ""
    x = x0
    y = y0
    for char in code:
        x2, y2 = grid[char]
        dx = x2 - x
        dy = y2 - y
        if dx > 0:
            hstring = ">" * dx
        else:
            hstring = "<" * -dx
        if dy > 0:
            vstring = "v" * dy
        else:
            vstring = "^" * -dy
        if x == x2 or y == y2:
            string = string + hstring + vstring + "A"
        elif x == x_bad and y2 == y_bad:
            string = string + hstring + vstring + "A"
        elif x2 == x_bad and y == y_bad:
            string = string + vstring + hstring + "A"
        # see optimizations.txt for calculations for below
        elif x2 < x and y2 < y:
            string = string + hstring + vstring + "A"
        elif x2 > x and y2 < y:
            string = string + hstring + vstring + "A"
        elif x2 < x and y2 > y:
            string = string + hstring + vstring + "A"
        elif x2 > x and y2 > y:
            string = string + vstring + hstring + "A"

        x = x2
        y = y2
    return string


filename = sys.argv[1]
with open(filename) as file:
    codes = [line.strip() for line in file]

pad1 = ["789", "456", "123", " 0A"]
pad2 = [" ^A", "<v>"]

keypads = 2
total = 0
for code in codes:
    printd(code)
    sequence = expand(code, pad1)
    printd(sequence, len(sequence))
    for _ in range(keypads):
        sequence = expand(sequence, pad2)
        printd(sequence, len(sequence))
    total += len(sequence) * int(code[:-1])

print(total)
