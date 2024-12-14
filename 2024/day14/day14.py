import re
from copy import deepcopy

with open('2024/day14/input.txt') as f:
    robots = [[int(match[0]), int(match[1]), int(match[2]), int(match[3])] for row in f for match in re.findall(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', row)]

robots_copy = deepcopy(robots)

num_rows = 103
num_cols = 101

def simulate(num_s, robots=robots):
    for t in range(num_s):
        for i, robot in enumerate(robots):
            x, y, vx, vy = robot
            robots[i][0] = (x + vx)%num_cols
            robots[i][1] = (y + vy)%num_rows


def draw_grid(draw=False, robots=robots):
    grid = [[0 for col in range(num_cols)] for row in range(num_rows)]
    quad_0 = quad_1 = quad_2 = quad_3 = 0
    for robot in robots:
        x, y, vx, vy = robot
        grid[y][x] += 1
        if x < num_cols//2:
            if y < num_rows//2:
                quad_0 += 1
            elif y > num_rows//2:
                quad_1 += 1
        elif x > num_cols//2:
            if y < num_rows//2:
                quad_2 += 1
            elif y > num_rows//2:
                quad_3 += 1
    if draw:
        for row in grid:
            for item in row:
                if item: print('#', end='')
                else: print('.', end='')
            print()
    return quad_0 * quad_1 * quad_2 * quad_3


min_safety = None
min_time = 0
for t in range(1, 10000):
    simulate(1)
    safety = draw_grid()
    if not min_safety or safety < min_safety:
        min_safety = safety
        min_time = t

    if t == 100:
        print('Part 1:', safety)

print('Part 2:', min_time)
simulate(min_time, robots_copy)
draw_grid(True, robots_copy)