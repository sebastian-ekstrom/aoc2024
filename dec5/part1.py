import sys
from collections import defaultdict

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

prerequisites = defaultdict(list)
for i in range(len(lines)):
    if len(lines[i]) == 0:
        break
    tokens = lines[i].split("|")
    prerequisites[int(tokens[1])].append(int(tokens[0]))

updates = []
for j in range(i + 1, len(lines)):
    updates.append([int(n) for n in lines[j].split(",")])

total = 0
for update in updates:
    # ~ print(update)
    ordered = True
    for i in range(len(update) - 1):
        for j in range(i, len(update)):
            if update[j] in prerequisites[update[i]]:
                ordered = False
                break
        if not ordered:
            # ~ print(f"not ordered, {update[j]} before {update[i]}")
            break
    if ordered:
        # ~ print("ordered")
        total += update[len(update) // 2]
print(total)
