import sys
from collections import defaultdict

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def to_transitions(start, sequence):
    expanded = start + sequence
    transitions = defaultdict(int)
    for i in range(len(expanded) - 1):
        transitions[(expanded[i], expanded[i+1])] += 1
    return transitions

def expand_transitions(transitions, pad):
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

    new_transitions = defaultdict(int)
    for transition, freq in transitions.items():
        char1, char2 = transition
        x, y = grid[char1]
        x2, y2 = grid[char2]
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
            string = hstring + vstring + "A"
        elif x == x_bad and y2 == y_bad:
            string = hstring + vstring + "A"
        elif x2 == x_bad and y == y_bad:
            string = vstring + hstring + "A"
        # see optimizations.txt for calculations for below
        elif x2 < x and y2 < y:
            # <^ better than ^<
            string = hstring + vstring + "A"
        elif x2 > x and y2 < y:
            # ^> is better than >^
            string = vstring + hstring + "A"
        elif x2 < x and y2 > y:
            # <v better than v<
            string = hstring + vstring + "A"
        elif x2 > x and y2 > y:
            # v> better than >v
            string = vstring + hstring + "A"

        part_transitions = to_transitions("A", string)
        printd(char1, char2, freq, string, dict(part_transitions))
        for transition2, freq2 in part_transitions.items():
            new_transitions[transition2] += freq * freq2
    return new_transitions


filename = sys.argv[1]
with open(filename) as file:
    codes = [line.strip() for line in file]

pad1 = ["789", "456", "123", " 0A"]
pad2 = [" ^A", "<v>"]

keypads = 25
total = 0
for code in codes:
    printd(code)
    transitions = to_transitions("A", code)
    printd(dict(transitions))
    transitions = expand_transitions(transitions, pad1)
    printd(dict(transitions))
    for _ in range(keypads):
        transitions = expand_transitions(transitions, pad2)
        printd(dict(transitions))
    printd(sum(transitions.values()))
    total += sum(transitions.values()) * int(code[:-1])

print(total)
