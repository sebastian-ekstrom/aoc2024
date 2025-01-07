import sys
from collections import defaultdict

def printd(*args, **kwargs):
    debug = True
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    rocks = {int(i): 1 for i in file.readline().split()}

for _ in range(75):
    next_rocks = defaultdict(int)
    for number, amount in rocks.items():
        string = str(number)
        if number == 0:
            next_rocks[1] += amount
        elif len(string) % 2 == 0:
            n1 = int(string[len(string) // 2:])
            n2 = int(string[:len(string) // 2])
            next_rocks[n1] += amount
            next_rocks[n2] += amount
        else:
            next_rocks[number * 2024] += amount
    rocks = next_rocks

print(sum(rocks.values()))
