import math
from itertools import product

with open('days/day7/input.txt') as f:
    data = [tuple(line.strip().split(':')) for line in f]
    data = [(int(a), list(map(int, b.strip().split(' ')))) for a, b in data]


def num_digits(b):
    return int(math.log10(b)) + 1

def ends_with(a, b):
    return (a - b) % (10) ** num_digits(b) == 0


def solve_backwards(test_value, equation, check_concat=False):
    *head, n = equation
    if not head:
        return n == test_value
    total_div, modulo_div = divmod(test_value, n)
    if modulo_div == 0 and solve_backwards(total_div, head, check_concat):
        return True
    if check_concat and ends_with(test_value, n) and solve_backwards(test_value // (10 ** num_digits(n)), head, check_concat):
        return True
    return solve_backwards(test_value - n, head, check_concat)


total_1 = 0
total_2 = 0
for line in data:
    if solve_backwards(line[0], line[1], False):
        total_1 += line[0]
    if solve_backwards(line[0], line[1], True):
        total_2 += line[0]

print('Part 1:', total_1)
print('Part 2:', total_2)
