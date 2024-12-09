import operator
from itertools import product

with open('days/day7/input.txt') as f:
    data = [tuple(line.strip().split(':')) for line in f]
    data = [(int(a), list(map(int, b.strip().split(' ')))) for a, b in data]


def try_operator(line, operators):
    total, equation = line
    perms = product(operators, repeat=len(equation)-1)
    skip = set()
    for perm in perms:
        value = 0
        for i, op in enumerate(perm):
            if perm[:i] in skip:
                continue
            if i == 0:
                value = equation[i]
            value = op(value, equation[i+1])

            if value > total:
                skip.add(perm[:i])
                break

        if value == total:
            return True

    return False

operators = [operator.add, operator.mul]
total = 0
total_true = 0
total_false = 0
for line in data:
    if try_operator(line, operators):
        total += line[0]

print('Part 1:', total)



def concat(a, b):
    return int(f'{a}{b}')


operators = [operator.add, operator.mul, concat]
total = 0
for line in data:
    if try_operator(line, operators):
        total += line[0]

print('Part 2:', total)