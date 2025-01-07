import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    numbers = [int(line.strip()) for line in file]

total = 0
for number in numbers:
    for _ in range(2000):
        number = (number ^ (number * 64)) % 16777216
        number = (number ^ (number // 32)) % 16777216
        number = (number ^ (number * 2048)) % 16777216
    printd(number)
    total += number
print(total)
