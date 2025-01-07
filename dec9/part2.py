import sys

def printd(*args, **kwargs):
    debug = False
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
file_nbr = filesystem[-1]

while file_nbr > 0:
    printd(f"attempting to move file {file_nbr}")
    while filesystem[remove_index] != file_nbr:
        remove_index -= 1
    file_end = remove_index + 1
    while filesystem[remove_index] == file_nbr:
        remove_index -= 1
    file_start = remove_index + 1
    file_size = file_end - file_start

    insert_index = 0
    while insert_index < remove_index:
        while filesystem[insert_index] != -1:
            insert_index += 1
        hole_start = insert_index
        while filesystem[insert_index] == -1:
            insert_index += 1
        hole_end = insert_index
        hole_size = hole_end - hole_start
        if file_start <= hole_start:
            break
        if hole_size < file_size:
            continue
        printd(f"move file {file_nbr} from {file_start} to {hole_start}")
        for i in range(file_size):
            filesystem[hole_start + i] = filesystem[file_start + i]
            filesystem[file_start + i] = -1
        print_disk(filesystem)
        break
    file_nbr -= 1

total = 0
for i in range(len(filesystem)):
    if filesystem[i] >= 0:
        total += i * filesystem[i]
print(total)
