import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def possible_pattern(pattern, towels):
    global possible
    if debug:
        input()
    if pattern in possible:
        printd(f"{pattern} already checked, result {possible[pattern]}")
        return possible[pattern]
    printd(f"checking {pattern}")
    for towel in towels:
        if pattern == towel:
            printd(f"{pattern} matches {towel}")
            possible[pattern] = True
            return True
        elif pattern.startswith(towel):
            printd(f"{pattern} starts with {towel}")
            if possible_pattern(pattern[len(towel):], towels):
                possible[pattern] = True
                return True
    printd("no matches")
    possible[pattern] = False
    return False

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

towels = lines[0].split(", ")
patterns = lines[2:]

possible = {}
total = 0
for pattern in patterns:
    if possible_pattern(pattern, towels):
        total += 1
print(total)
