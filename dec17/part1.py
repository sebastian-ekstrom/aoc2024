import sys

def get_combo_operand(operand, regs):
    if operand <= 3:
        return operand
    return regs[operand - 4]

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

regs = [int(lines[i].split()[-1]) for i in range(3)]
program = [int(c) for c in lines[-1][9:].split(",")]
pc = 0

names = ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"]

output = []
while pc >= 0 and pc < len(program):
    opcode = program[pc]
    operand = program[pc+1]
    if opcode == 0: # adv
        num = regs[0]
        den = 2 ** get_combo_operand(operand, regs)
        regs[0] = num // den
    elif opcode == 1: # bxl
        op1 = regs[1]
        op2 = operand
        regs[1] = op1 ^ op2
    elif opcode == 2: # bst
        op = get_combo_operand(operand, regs)
        regs[1] = op % 8
    elif opcode == 3: # jnz
        if regs[0] != 0:
            pc = operand - 2
    elif opcode == 4: # bxc
        op1 = regs[1]
        op2 = regs[2]
        regs[1] = op1 ^ op2
    elif opcode == 5: # out
        op = get_combo_operand(operand, regs)
        output.append(op % 8)
    elif opcode == 6: # bdv
        num = regs[0]
        den = 2 ** get_combo_operand(operand, regs)
        regs[1] = num // den
    elif opcode == 7: # cdv
        num = regs[0]
        den = 2 ** get_combo_operand(operand, regs)
        regs[2] = num // den
    pc += 2
    if debug:
        print(f"{names[opcode]} {operand}")
        print(regs)
        input()

print(",".join([str(i) for i in output]))
