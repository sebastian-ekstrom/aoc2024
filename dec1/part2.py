import sys
from collections import defaultdict

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

list1 = []
list2 = defaultdict(int)
for line in lines:
    a, b = [int(i) for i in line.split()]
    list1.append(a)
    list2[b] += 1

total = 0
for i in list1:
    total += i * list2[i]

print(total)


