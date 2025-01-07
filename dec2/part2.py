import sys

filename = sys.argv[1]
with open(filename) as file:
    lines = [[int(i) for i in line.strip().split()] for line in file]

nbr_safe = 0
for line in lines:
    # ~ print(line)
    safe = False
    for j in range(len(line)):
        short_line = line[:j] + line[j + 1:]
        diffs = [short_line[i + 1] - short_line[i] for i in range(len(short_line) - 1)]
        if all([i > 0 and i <= 3 for i in diffs]) or all([i < 0 and i >= -3 for i in diffs]):
            # ~ print(short_line)
            # ~ print("safe")
            safe = True
            break
    if safe:
        nbr_safe += 1
print(nbr_safe)
