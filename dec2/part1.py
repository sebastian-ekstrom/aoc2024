import sys

filename = sys.argv[1]
with open(filename) as file:
    lines = [[int(i) for i in line.strip().split()] for line in file]

safe = 0
for line in lines:
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    # ~ print(line)
    # ~ print(diffs)
    if all([i > 0 and i <= 3 for i in diffs]) or all([i < 0 and i >= -3 for i in diffs]):
        # ~ print("safe")
        safe += 1
print(safe)
