import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def expand(code, pad, find_all):
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

    if find_all:
        strings = {""}
    else:
        string = ""
    x = x0
    y = y0
    for char in code:
        if find_all:
            next_strings = set()
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
        if find_all:
            if x2 != x_bad or y != y_bad:
                for string in strings:
                    next_strings.add(string + hstring + vstring + "A")
            if x != x_bad or y2 != y_bad:
                for string in strings:
                    next_strings.add(string + vstring + hstring + "A")
            strings = next_strings
        else:
            if x2 != x_bad and y != y_bad:
                string = string + hstring + vstring + "A"
            else:
                string = string + vstring + hstring + "A"
        x = x2
        y = y2
    if find_all:
        return list(strings)
    return [string]


filename = sys.argv[1]
with open(filename) as file:
    codes = [line.strip() for line in file]

pad1 = ["789", "456", "123", " 0A"]
pad2 = [" ^A", "<v>"]

total = 0
for code in codes:
    printd(code)
    sequences = expand(code, pad1, True)
    # ~ printd(sequence, len(sequence))
    sequences2 = []
    for sequence in sequences:
        sequences2 += expand(sequence, pad2, True)
    # ~ printd(sequence, len(sequence))
    sequences3 = []
    for sequence in sequences2:
        sequences3 += expand(sequence, pad2, False)
    # ~ printd(sequence, len(sequence))
    printd(min([len(sequence) for sequence in sequences3]))
    total += min([len(sequence) for sequence in sequences3]) * int(code[:-1])

print(total)
