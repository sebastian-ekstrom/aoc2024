import sys

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def calculate_value(name, values, inputs):
    if name in values:
        return values[name]
    input1, input2, op = inputs[name]
    value1 = calculate_value(input1, values, inputs)
    value2 = calculate_value(input2, values, inputs)
    if op == "AND":
        value = value1 & value2
    elif op == "OR":
        value = value1 | value2
    elif op == "XOR":
        value = value1 ^ value2

    values[name] = value
    return value

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

values = {}
inputs = {}

for line in lines:
    if ":" in line:
        name, value = line.split(": ")
        values[name] = int(value)
    elif len(line) > 0:
        input1, op, input2, _, output = line.split()
        inputs[output] = (input1, input2, op)

total = 0
for name in inputs:
    if name.startswith("z"):
        total += calculate_value(name, values, inputs) * (2 ** int(name[1:]))

print(total)
