import sys

def printd(*args, **kwargs):
    debug = True
    if debug:
        print(*args, **kwargs)

def print_disk(filesystem):
    debug = False
    if not debug:
        return
    string = ""
    for i in filesystem:
        if i == -1:
            string += "."
        else:
            string += str(i)
    print(string)


filename = sys.argv[1]
with open(filename) as file:
    diskmap = [int(i) for i in file.readline().strip()]

filesystem = []
empty = False
file_nbr = 0
for i in diskmap:
    if empty:
        for _ in range(i):
            filesystem.append(-1)
    else:
        for _ in range(i):
            filesystem.append(file_nbr)
        file_nbr += 1
    empty = not empty
    print_disk(filesystem)

insert_index = 0
remove_index = len(filesystem) - 1

while True:
    while insert_index < remove_index and filesystem[insert_index] != -1:
        insert_index += 1
    while remove_index > insert_index and filesystem[remove_index] == -1:
        remove_index -= 1
    if insert_index >= remove_index:
        break
    filesystem[insert_index] = filesystem[remove_index]
    filesystem[remove_index] = -1
    insert_index += 1
    remove_index -= 1
    print_disk(filesystem)

total = 0
for i in range(len(filesystem)):
    if filesystem[i] >= 0:
        total += i * filesystem[i]
print(total)
