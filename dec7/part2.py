import sys

def printd(*args, **kwargs):
    debug = False
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

equations = []
for line in lines:
    separator = line.find(":")
    value = int(line[:separator])
    operands = [int(i) for i in line[separator+1:].split()]
    equations.append((value, operands))

total = 0
for value, operands in equations:
    current_numbers = [value]
    for i in range(len(operands) - 1, 0, -1):
        next_numbers = []
        for number in current_numbers:
            if number % operands[i] == 0:
                next_numbers.append(number // operands[i])
            if str(number).endswith(str(operands[i])) and number != operands[i]:
                printd(number, operands[i])
                next_numbers.append(int(str(number)[:-len(str(operands[i]))]))
            if number > operands[i]:
                next_numbers.append(number - operands[i])
        current_numbers = next_numbers
    if operands[0] in current_numbers:
        total += value
        printd(value, operands)
print(total)
