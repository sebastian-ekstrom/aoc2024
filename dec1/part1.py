import sys

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

list1 = []
list2 = []
for line in lines:
    a, b = [int(i) for i in line.split()]
    list1.append(a)
    list2.append(b)

list1.sort()
list2.sort()
total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
print(total)
