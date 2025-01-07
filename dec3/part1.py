import sys
import re

filename = sys.argv[1]
with open(filename) as file:
    string = "\n".join([line.strip() for line in file])

total = 0
while True:
    match = re.search("mul\((\d+),(\d+)\)", string)
    if not match:
        break
    total += int(match.group(1)) * int(match.group(2))
    string = string[match.end(0):]
print(total)
