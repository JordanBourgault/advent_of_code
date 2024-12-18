import re

with open('2024/day17/input.txt') as f:
    data = f.read()
    data = list(map(int, re.findall(r'(\d+)', data)))


def init_program():
    global a, b, c, program, i_pointer
    a, b, c, *program = data
    i_pointer = 0

def adv(operand):
    global i_pointer, a
    a = a//(2**operand[1])
    i_pointer += 2

def bxl(operand):
    global i_pointer, b
    b = b ^ operand[0]
    i_pointer += 2

def bst(operand):
    global i_pointer, b
    b = operand[1] % 8
    i_pointer += 2

def jnz(operand):
    global i_pointer, a
    if a != 0:
        i_pointer = operand[0]
    else:
        i_pointer += 2

def bxc(operand=None):
    global i_pointer, b
    b = b ^ c
    i_pointer += 2

def out(operand):
    global i_pointer
    i_pointer += 2
    return operand[1] % 8

def bdv(operand):
    global i_pointer, b
    b = a//(2**operand[1])
    i_pointer += 2

def cdv(operand):
    global i_pointer, c
    c = a//(2**operand[1])
    i_pointer += 2

def prog(instruction, operand):
    match operand:
        case 4: operand = operand, a
        case 5: operand = operand, b
        case 6: operand = operand, c
        case _: operand = operand, operand
        
    match instruction:
        case 0: adv(operand)
        case 1: bxl(operand)
        case 2: bst(operand)
        case 3: jnz(operand)
        case 4: bxc(operand)
        case 5: return out(operand)
        case 6: bdv(operand)
        case 7: cdv(operand)


def solve_program(a_reg=None):
    global a, b, c, program
    init_program()
    output = []
    if a_reg:
        a = a_reg
    prev_i = None
    while i_pointer < len(program):
        res = prog(program[i_pointer], program[i_pointer+1])
        if i_pointer == prev_i:
            break
        prev_i = i_pointer
        if res is not None:
            output.append(res)
    return output

print('Part 1:', ','.join(map(str, solve_program())))


# Decompîled program:
#   Only depends on "a" register
#   Divides a by 8 until a is 0
#   Only last 3 bits count towards resul
def decompiled(a):
    output = []
    while a != 0:
        b = a % 8
        b = b ^ 1
        c = a//(2**b)
        b = b ^ 4
        b = b ^ c
        a = a//8
        output += [b%8]
    return output


res = []
def find(a, i):
    if solve_program(a) == program:
        res.append(a)
    if solve_program(a) == program[-i:] or not i:
        print(a)
        for n in range(8): find(8*a+n, i+1)

find(0, 0)
print('Part 2:', min(res))
