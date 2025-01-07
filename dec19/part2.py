import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def nbr_combinations(pattern, towels):
    global combinations
    if debug:
        input()
    if pattern in combinations:
        printd(f"{pattern} already checked, result {combinations[pattern]}")
        return combinations[pattern]
    printd(f"checking {pattern}")
    combinations[pattern] = 0
    for towel in towels:
        if pattern == towel:
            printd(f"{pattern} matches {towel}")
            combinations[pattern] += 1
        elif pattern.startswith(towel):
            printd(f"{pattern} starts with {towel}")
            combinations[pattern] += nbr_combinations(pattern[len(towel):], towels)

    return combinations[pattern]

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

towels = lines[0].split(", ")
patterns = lines[2:]

combinations = {}
total = 0
for pattern in patterns:
    total += nbr_combinations(pattern, towels)
print(total)
