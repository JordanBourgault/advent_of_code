from copy import deepcopy
from datetime import datetime

from itertools import repeat
from multiprocessing import Pool

startTime = datetime.now()

with open('days/day6/input.txt') as f:
    data = [list(line.strip()) for line in f]


def get_guard_initial_pos(grid):
    guard_orientations = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
        }
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            if grid[row_num][col_num] in guard_orientations.keys():
                return (row_num, col_num), guard_orientations[grid[row_num][col_num]]


def rotate_orientation(orientation):
    return orientation[1], -1*orientation[0]


def move_guard(grid, return_grid=True):
    start, direction = get_guard_initial_pos(data)
    row_num, col_num = start
    row_mul, col_mul = direction

    while 0 <= row_num + row_mul <= len(grid) and 0 <= col_num + col_mul <= len(grid[0]):
        row_mul, col_mul = direction
        row_ahead_num = row_num + row_mul
        col_ahead_num = col_num + col_mul
        try:
            next_pos = grid[row_ahead_num][col_ahead_num]
        except IndexError:
            next_pos = '.'

        current = grid[row_num][col_num]
        
        if type(current) == set:
            if direction in current:
                return False
            current.add(direction)
        else:
            grid[row_num][col_num] = {direction}

        if next_pos == '#':
            direction = rotate_orientation((row_mul, col_mul))
            continue

        row_num, col_num = row_ahead_num, col_ahead_num
    return grid if return_grid else True

def count_positions(grid):
    return sum([sum([isinstance(element, set) for element in row]) for row in grid])


grid = deepcopy(data)
initial_moves_grid = move_guard(grid)
print('Part1:', count_positions(initial_moves_grid))


def get_indexes(grid):
    return [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if isinstance(cell, set)]

def get_obstacle_loop(index, data):
    grid = deepcopy(data)
    grid[index[0]][index[1]] = '#'
    return move_guard(grid, return_grid=False)

indexes = get_indexes(initial_moves_grid)
with Pool() as pool:
    res = pool.starmap(get_obstacle_loop, zip(indexes, repeat(data)))

print('Part2:', res.count(False))
print(datetime.now() - startTime)