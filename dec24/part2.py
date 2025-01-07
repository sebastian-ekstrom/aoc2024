import sys
import math
from collections import deque

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def calculate_value(name, gates, x, y, swaps):
    if name in swaps:
        name = swaps[name]
    if name.startswith("x"):
        number = int(name[1:])
        return (x & (2 ** number)) // (2 ** number)
    elif name.startswith("y"):
        number = int(name[1:])
        return (y & (2 ** number)) // (2 ** number)
    input1, input2, gate = gates[name]
    value1 = calculate_value(input1, gates, x, y, swaps)
    value2 = calculate_value(input2, gates, x, y, swaps)
    if gate == "AND":
        value = value1 & value2
    elif gate == "OR":
        value = value1 | value2
    elif gate == "XOR":
        value = value1 ^ value2

    return value

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

gates = {}

for line in lines:
    if "->" in line:
        input1, gate, input2, _, output = line.split()
        gates[output] = (input1, input2, gate)

nbr_bits = 45

search = False
if search:
    correct_swaps = set()
    names = sorted([name for name in gates])

    for i1 in range(len(names) - 1):
        gate1 = names[i1]
        printd(f"test swapping {gate1}")
        if gate1 in correct_swaps:
            continue
        for i2 in range(i1 + 1, len(names)):
            gate2 = names[i2]
            printd(f"test swapping {gate1} with {gate2}")
            if gate2 in correct_swaps:
                continue

            swaps = {gate1: gate2, gate2: gate1}

            wrong_bits = 0
            for i in range(nbr_bits):
                total = 0
                x = 2 ** i
                y = 0
                total_correct = x + y
                try:
                    for z in range(nbr_bits + 1):
                        total += calculate_value("z{:02d}".format(z), gates, x, y, swaps) * (2 ** z)
                    if total != total_correct:
                        # ~ print(f"bit {i}: should be 2^{i}, got 2^{int(math.log2(total))}")
                        # ~ print(f"bit {i}: should be {total_correct:b}, got {total:b}")
                        wrong_bits += 1
                        if wrong_bits >= 4:
                            break
                except RecursionError:
                    wrong_bits = 1e10
                    break
            if wrong_bits < 4:
                printd(f"swap {gate1} and {gate2}")
                correct_swaps.add((gate1, gate2))

    print(correct_swaps)

# {('nhn', 'stq'), ('bbn', 'stq'), ('cdc', 'nhn'), ('khg', 'z25'), ('nhn', 'z21'), ('kmm', 'z33'), ('vdc', 'z12'), ('pps', 'z12'),
# ('khg', 'tbn'), ('grb', 'khg'), ('jhd', 'khg'), ('mfp', 'z25'), ('khg', 'tvb'), ('gst', 'z33'), ('fbk', 'z12')}
test = True
if test:
    swaps = {}
    swaps["vdc"] = "z12"
    swaps["z12"] = "vdc"
    swaps["nhn"] = "z21"
    swaps["z21"] = "nhn"
    swaps["khg"] = "tvb"
    swaps["tvb"] = "khg"
    swaps["gst"] = "z33"
    swaps["z33"] = "gst"


    for i in range(nbr_bits):
        total = 0
        x = 0
        y = 2 ** i
        total_correct = x + y
        for z in range(nbr_bits + 1):
            total += calculate_value("z{:02d}".format(z), gates, x, y, swaps) * (2 ** z)
        if total != total_correct:
            print(f"bit {i}: 2^{int(math.log2(total_correct))}, got 2^{int(math.log2(total))}")
            # ~ print(f"bit {i}: should be {total_correct:b}, got {total:b}")
    print(",".join(sorted(swaps.keys())))

