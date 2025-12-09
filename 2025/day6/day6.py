from math import prod

with open("2025/day6/input.txt") as f:
    dat_1 = []
    dat_2 = []
    for line in f:
        dat_1.append(line.split())
        dat_2.append(list(line.strip('\n')))

total = 0
for i in range(len(dat_1[0])):
    op = prod if dat_1[-1][i] == '*' else sum
    total += op([int(dat_1[j][i]) for j in range(len(dat_1)-1)])

print('Part 1: ', total)

total_2 = 0
col = len(dat_2[0])-1
problem = []
for col in range(len(dat_2[0])-1, -1, -1):
    num = ''
    for j in range(len(dat_2)-1):
        num += dat_2[j][col] if dat_2[j][col] != ' ' else ''
    if num:
        problem.append(int(num))
    num = ''
    if dat_2[-1][col] != ' ':
        op = prod if dat_2[-1][col] == '*' else sum
        total_2 += op(problem)
        problem = []

print('Part 2: ', total_2)