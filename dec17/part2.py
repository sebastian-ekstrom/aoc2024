import sys

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

program = [int(c) for c in lines[-1][9:].split(",")]

# ~ Program: 2,4, 1,2, 7,5, 1,3, 4,4, 5,5, 0,3, 3,0
# ~ bst 4
# ~ bxl 2
# ~ cdv 5
# ~ bxl 3
# ~ bxc 4
# ~ out 5
# ~ adv 3
# ~ jnz 0

def execute_program(a):
    b = 0
    c = 0
    output = []
    while a != 0:
        printd((a, b, c))
        b = a % 8
        printd((a, b, c))
        b = b ^ 2
        printd((a, b, c))
        c = a // (2 ** b)
        printd((a, b, c))
        b = b ^ 3
        printd((a, b, c))
        b = b ^ c
        printd((a, b, c))
        output.append(b % 8)
        printd(b % 8)
        a = a // 8
        if debug:
            input()
    return output

if False:
    a = 48744869
    output = execute_program(a)
    print(",".join([str(i) for i in output]))

printd(program)
possible_as = [0]
for digit in reversed(program):
    next_as = []
    for a in possible_as:
        for i in range(8):
            if a == 0 and i == 0:
                continue
            output = execute_program(a * 8 + i)
            if output[0] == digit:
                printd(a * 8 + i, output)
                next_as.append(a * 8 + i)
    possible_as = next_as

next_as.sort()
print(next_as[0], execute_program(next_as[0]))
