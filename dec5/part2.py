import sys
from collections import defaultdict

def printd(*args, **kwargs):
    debug = False
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

prerequisites = defaultdict(list)
for i in range(len(lines)):
    if len(lines[i]) == 0:
        break
    tokens = lines[i].split("|")
    prerequisites[int(tokens[1])].append(int(tokens[0]))
for n in prerequisites:
    printd(n, prerequisites[n])

updates = []
for j in range(i + 1, len(lines)):
    updates.append([int(n) for n in lines[j].split(",")])

unordered_updates = []
for update in updates:
    printd(update)
    ordered = True
    for i in range(len(update) - 1):
        for j in range(i, len(update)):
            if update[j] in prerequisites[update[i]]:
                ordered = False
                unordered_updates.append(update)
                break
        if not ordered:
            printd(f"not ordered, {update[j]} before {update[i]}")
            break

total = 0
for update in unordered_updates:
    printd(f"unordered: {update}")
    ordered_update = []
    while len(update) > 0:
        for i in range(len(update)):
            first_remaining = True
            printd(f"testing {update[i]}")
            for j in range(len(update)):
                if i == j:
                    continue
                if update[j] in prerequisites[update[i]]:
                    printd(f"{update[j]} comes before {update[i]}, {update[i]} can't be first")
                    first_remaining = False
                    break
            printd(f"{update[i]} testing done: {first_remaining}")
            if first_remaining:
                ordered_update.append(update[i])
                update.remove(update[i])
                printd(f"removed {ordered_update[-1]}, remaining {update}")
                break
    printd(f"ordered: {ordered_update}")
    total += ordered_update[len(ordered_update) // 2]
print(total)
