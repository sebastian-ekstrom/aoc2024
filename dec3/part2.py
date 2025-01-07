import sys
import re

filename = sys.argv[1]
with open(filename) as file:
    string = "\n".join([line.strip() for line in file])

total = 0
enable = True
while True:
    match = re.search("do\(\)|don't\(\)|mul\((\d+),(\d+)\)", string)
    if not match:
        break
    if match.group(0) == "do()":
        enable = True
    elif match.group(0) == "don't()":
        enable = False
    else:
        if enable:
            total += int(match.group(1)) * int(match.group(2))
    string = string[match.end(0):]
print(total)
