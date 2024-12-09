from datetime import datetime
from itertools import repeat
from multiprocessing import Pool

startTime = datetime.now()

with open('days/day6/input.txt') as f:
    lines = f.readlines()
    data = {(row, col): cell_data for row, row_data in enumerate(lines) for col, cell_data in enumerate(row_data.strip())}

def get_guard_initial_pos(grid):
    guard_orientations = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
        }
    for key, value in grid.items():
        if value in guard_orientations:
            return key, guard_orientations[value]

guard_pos = get_guard_initial_pos(data)


def rotate_orientation(orientation):
    return orientation[1], -1*orientation[0]


def move_guard(grid, return_pos=True, special_obstacle=None):
    pos, direction = guard_pos
    path = set()
    while pos in grid and (pos, direction) not in path:
        path |= {(pos, direction)}
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        next_value = grid.get(next_pos, '.')
        if next_value == '#' or next_pos == special_obstacle:
            direction = rotate_orientation(direction)
            continue
        
        pos = next_pos
        
    if return_pos:
        return {pos for pos, _ in path}, None
    else: 
        return None, (pos, direction) in path


moves, _ = move_guard(data)
print('Part 1:', len(moves))
print(datetime.now() - startTime)


with Pool() as pool:
    res = [path for _, path in pool.starmap(move_guard, zip(repeat(data), repeat(False), moves))]

print('Part 2:', res.count(True))
print(datetime.now() - startTime)
