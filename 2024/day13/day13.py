import re

with open('2024/day13/input.txt') as f:
    problems = [{
        "but_a": list(map(int, re.findall(r'Button A: X\+(\d+), Y\+(\d+)', prob)[0])), 
        "but_b": list(map(int, re.findall(r'Button B: X\+(\d+), Y\+(\d+)', prob)[0])),
        "ans": list(map(int, re.findall(r'Prize: X=(\d+), Y=(\d+)', prob)[0]))
              } for prob in f.read().split('\n\n')]


def solve(problem, offset = 0):
    (z_x, z_y), (A_x, A_y), (B_x, B_y) = problem['ans'], problem['but_a'], problem['but_b']
    z_x += offset
    z_y += offset
    b = (A_x * z_y - A_y * z_x) / (A_x * B_y - A_y * B_x)
    a = (z_x - B_x * b) / A_x

    if any([not num.is_integer() for num in [a, b]]) or (A_x * a + B_x * b, A_y * a + B_y * b) != (z_x, z_y):
        return 0
    
    return round(3*a + b)


print('Part 1:', sum([solve(problem) for problem in problems]))
print('Part 2:', sum([solve(problem, 10000000000000) for problem in problems]))